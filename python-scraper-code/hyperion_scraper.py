import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
import boto3

# --- S3 Configuration ---
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME") 
if S3_BUCKET_NAME:
    s3 = boto3.client('s3')

def scrape_hyperion_album(url, bucket_name):
    """
    Scrapes Hyperion album data, handling both simple and tabbed note layouts,
    and saves the results directly to an S3 bucket.
    """
    
    BASE_URL = "https://www.hyperion-records.co.uk"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            print(f"  -> SKIPPING: 404 Not Found for {url}")
            return
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"  -> SKIPPING: Could not fetch URL {url}. Reason: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    metadata = {'source_url': url}
    
    album_div = soup.find('div', class_='hyp-albumdetail')
    if not album_div:
        print(f"  -> SKIPPING: Could not find main album detail div on {url}")
        return

    metadata['album_title'] = album_div.find('h3', class_='hyp-title').get_text(strip=True) if album_div.find('h3') else "Title not found"
    
    # Correctly handle catalogue numbers with slashes (e.g., CDA66071/2)
    metadata['catalogue_number'] = url.split('D_')[-1].replace('%2F', '/')
    filename_base = metadata['catalogue_number'].replace('/', '_') # Create a filesystem-safe name
    json_s3_key = f"json/{filename_base}.json"

    # ===================================================================
    # === NEW, SMARTER LINER NOTES EXTRACTION LOGIC =====================
    # ===================================================================
    liner_notes_parts = []
    
    # 1. First, check for the tabbed interface
    tabs_container = soup.find('ul', class_='nav-tabs')
    if tabs_container:
        print("  -> Found tabbed interface. Searching for 'English' and 'Synopsis' notes.")
        tabs_to_extract = {'English': '--- Liner Notes ---', 'Synopsis': '--- Synopsis ---'}
        
        for tab_name, header in tabs_to_extract.items():
            # Find the link for the specific tab by its text
            link = tabs_container.find('a', string=lambda text: text and tab_name in text)
            
            if link and link.has_attr('href') and link['href'].startswith('#'):
                div_id = link['href'][1:]  # Get the div ID, e.g., "CDD22050_1_1"
                notes_div = soup.find('div', id=div_id)
                
                # Ensure the div exists and doesn't just contain a loading gif
                if notes_div and not notes_div.find('img', alt='Waiting for content to load...'):
                    text_content = notes_div.get_text(separator=' ', strip=True)
                    if len(text_content) > 50:
                        liner_notes_parts.append(f"\n\n{header}\n{text_content}")

    # 2. If no notes found via tabs, fall back to the old method (for simple pages)
    if not liner_notes_parts:
        print("  -> Simple page layout found. Looking for default notes div.")
        # The catalogue number in the ID might have %2F for the slash
        notes_div_id = f"{metadata['catalogue_number'].replace('/', '%2F')}_1_1"
        notes_div = soup.find('div', id=notes_div_id)
        if notes_div and len(notes_div.get_text(strip=True)) > 50:
             liner_notes_parts.append(notes_div.get_text(separator=' ', strip=True))

    # 3. Make the final decision based on what was found
    if liner_notes_parts:
        metadata['liner_notes_text'] = "".join(liner_notes_parts).strip()
        metadata['requires_pdf_processing'] = False
        print("  -> Successfully extracted liner notes from HTML.")
    else:
        # Only if no HTML notes are found, do we try to get the PDF
        metadata['liner_notes_text'] = ""
        metadata['requires_pdf_processing'] = True
        
        pdf_link_tag = soup.find('a', class_='dc-sleevenotes')
        if pdf_link_tag and pdf_link_tag.has_attr('href'):
            try:
                full_pdf_url = BASE_URL + pdf_link_tag['href']
                pdf_s3_key = f"pdf/{filename_base}.pdf"
                
                print(f"  -> Notes not in HTML. Downloading PDF to S3: {pdf_s3_key}")
                pdf_response = requests.get(full_pdf_url, headers=headers, timeout=30)
                pdf_response.raise_for_status()
                
                s3.put_object(Bucket=bucket_name, Key=pdf_s3_key, Body=pdf_response.content)
                
            except Exception as e:
                print(f"  -> WARNING: Failed to download/upload PDF. Reason: {e}")
                metadata['requires_pdf_processing'] = False
        else:
            print("  -> No HTML notes or PDF link found.")
            metadata['requires_pdf_processing'] = False

    # ===================================================================
    # === END OF NEW LOGIC ==============================================
    # ===================================================================

    # Scrape remaining metadata (this logic is unchanged)
    composer_tag = album_div.find('h4')
    metadata['composer'] = composer_tag.get_text(strip=True) if composer_tag else "Composer not found"
    artists_heading = album_div.find('h5', class_='hyp-headlineartists')
    metadata['performers'] = [a.get_text(strip=True) for a in artists_heading.find_all('a')] if artists_heading else []
    anorak_panel = soup.find('div', class_='panel-body hyp-anorak')
    metadata['recording_details'] = anorak_panel.get_text(separator='\n', strip=True) if anorak_panel else "Details not found"
    image_tag = soup.find('img', class_='hyp-album')
    metadata['image_url'] = BASE_URL + image_tag['src'] if image_tag and image_tag.has_attr('src') else "Image not found"

    # Upload JSON directly to S3
    print(f"  -> Uploading metadata to S3: {json_s3_key}")
    s3.put_object(
        Bucket=bucket_name,
        Key=json_s3_key,
        Body=json.dumps(metadata, indent=4, ensure_ascii=False),
        ContentType='application/json'
    )
    
    print(f"  -> Successfully processed {filename_base}.")


# === MAIN EXECUTION BLOCK (Unchanged) ===
if __name__ == '__main__':
    if not S3_BUCKET_NAME:
        print("ERROR: S3_BUCKET_NAME environment variable not set.")
        print("This script is designed to run on an EC2 instance configured by Terraform.")
        exit(1)

    CODE_LIST_FILE = "catalogue_codes.json"
    try:
        with open(CODE_LIST_FILE, 'r') as f:
            codes_to_scrape = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: '{CODE_LIST_FILE}' not found. Please create it first.")
        exit(1)

    print(f"Data will be saved to S3 bucket: '{S3_BUCKET_NAME}'")
    total_codes = len(codes_to_scrape)
    print(f"Found {total_codes} total album codes to process.")

    for i, code in enumerate(codes_to_scrape):
        url_safe_code = code.replace('/', '%2F')
        url = f"https://www.hyperion-records.co.uk/dc.asp?dc=D_{url_safe_code}"
        
        print(f"\n--- Processing album {i+1} of {total_codes} (Code: {code}) ---")
        scrape_hyperion_album(url, S3_BUCKET_NAME) 
        
        time.sleep(random.uniform(1.0, 2.0))

    print("\n--- All albums have been processed! ---")