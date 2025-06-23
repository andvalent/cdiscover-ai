import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
import boto3 # The AWS library

# --- S3 Configuration ---
# Get the bucket name from an environment variable set by Terraform.
# This makes the script portable and secure.
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME") 
s3 = boto3.client('s3')

def scrape_hyperion_album(url, bucket_name):
    """
    Scrapes Hyperion album data and saves the results directly to an S3 bucket.
    """
    
    BASE_URL = "https://www.hyperion-records.co.uk"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.hyperion-records.co.uk/n.asp"
    }

    # --- This part is unchanged ---
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
    metadata['catalogue_number'] = url.split('D_')[-1].replace('%2F', '/')

    # --- LOGIC TO WRITE TO S3 INSTEAD OF LOCAL DISK ---
    
    filename_base = metadata['catalogue_number'].replace('/', '_')
    json_s3_key = f"json/{filename_base}.json"

    notes_div_id = f"{metadata['catalogue_number'].replace('/', '%2F')}_1_1"
    notes_div = soup.find('div', id=notes_div_id)
    has_html_notes = notes_div and len(notes_div.get_text(strip=True)) > 50 

    if has_html_notes:
        metadata['liner_notes_text'] = notes_div.get_text(separator=' ', strip=True)
        metadata['requires_pdf_processing'] = False
    else:
        metadata['liner_notes_text'] = ""
        metadata['requires_pdf_processing'] = True
        
        pdf_link_tag = soup.find('a', class_='dc-sleevenotes')
        if pdf_link_tag:
            try:
                full_pdf_url = BASE_URL + pdf_link_tag['href']
                pdf_s3_key = f"pdf/{filename_base}.pdf"
                
                print(f"  -> Notes not in HTML. Downloading PDF to S3: {pdf_s3_key}")
                pdf_response = requests.get(full_pdf_url, headers=headers, timeout=30)
                pdf_response.raise_for_status()
                
                # Upload PDF directly to S3
                s3.put_object(Bucket=bucket_name, Key=pdf_s3_key, Body=pdf_response.content)
                
            except Exception as e:
                print(f"  -> WARNING: Failed to download/upload PDF. Reason: {e}")
                metadata['requires_pdf_processing'] = False
        else:
            metadata['requires_pdf_processing'] = False

    # Scrape remaining metadata
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


# === MAIN EXECUTION BLOCK (Now handles missing env variable) ===
if __name__ == '__main__':
    # Check if the required environment variable is set
    if not S3_BUCKET_NAME:
        print("ERROR: S3_BUCKET_NAME environment variable not set.")
        print("This script is designed to run on an EC2 instance configured by Terraform.")
        exit(1) # Exit with an error code

    CODE_LIST_FILE = "catalogue_codes.json"
    try:
        with open(CODE_LIST_FILE, 'r') as f:
            codes_to_scrape = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: '{CODE_LIST_FILE}' not found. Please create it first.")
        exit()

    print(f"Data will be saved to S3 bucket: '{S3_BUCKET_NAME}'")
    total_codes = len(codes_to_scrape)
    print(f"Found {total_codes} total album codes to process.")

    for i, code in enumerate(codes_to_scrape):
        url_safe_code = code.replace('/', '%2F')
        url = f"https://www.hyperion-records.co.uk/dc.asp?dc=D_{url_safe_code}"
        
        print(f"\n--- Processing album {i+1} of {total_codes} (Code: {code}) ---")
        # Pass the bucket name to the function
        scrape_hyperion_album(url, S3_BUCKET_NAME) 
        
        time.sleep(random.uniform(1.0, 2.0))

    print("\n--- All albums have been processed! ---")