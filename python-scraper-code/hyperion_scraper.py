import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random

def scrape_hyperion_album(url):
    """
    Scrapes Hyperion album data. If liner notes are in the HTML, it skips the
    PDF download to save time and space. Otherwise, it downloads the PDF
    for later processing.
    """
    
    BASE_URL = "https://www.hyperion-records.co.uk"
    OUTPUT_DIR = "scraped_data"
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.hyperion-records.co.uk/n.asp"
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

    # Scrape the basic metadata that should always exist
    metadata['album_title'] = album_div.find('h3', class_='hyp-title').get_text(strip=True) if album_div.find('h3') else "Title not found"
    metadata['catalogue_number'] = url.split('D_')[-1].replace('%2F', '/') # Get code from URL as a reliable base

    # --- THE NEW CONDITIONAL LOGIC ---
    
    # 1. Check for liner notes in the HTML first
    notes_div_id = f"{metadata['catalogue_number'].replace('/', '%2F')}_1_1"
    notes_div = soup.find('div', id=notes_div_id)
    
    # Check if the div exists and has substantial text
    has_html_notes = notes_div and len(notes_div.get_text(strip=True)) > 50 

    if has_html_notes:
        print("  -> Found notes in HTML. PDF download is NOT required.")
        metadata['liner_notes_text'] = notes_div.get_text(separator=' ', strip=True)
        metadata['requires_pdf_processing'] = False
    else:
        print("  -> Notes not found in HTML. Attempting PDF download for later processing.")
        metadata['liner_notes_text'] = "" # Leave it empty for now
        metadata['requires_pdf_processing'] = True
        
        # 2. If no HTML notes, NOW we look for and download the PDF
        pdf_link_tag = soup.find('a', class_='dc-sleevenotes')
        if pdf_link_tag:
            try:
                full_pdf_url = BASE_URL + pdf_link_tag['href']
                filename_base = metadata['catalogue_number'].replace('/', '_')
                pdf_filepath = os.path.join(OUTPUT_DIR, f"{filename_base}.pdf")
                
                if not os.path.exists(pdf_filepath):
                    print(f"     Downloading PDF from {full_pdf_url}...")
                    pdf_response = requests.get(full_pdf_url, headers=headers)
                    pdf_response.raise_for_status()
                    with open(pdf_filepath, 'wb') as f:
                        f.write(pdf_response.content)
                else:
                    print(f"     PDF already exists, skipping download.")
            except Exception as e:
                print(f"  -> WARNING: Failed to download PDF. Reason: {e}")
                metadata['requires_pdf_processing'] = False # Can't process what we can't download
        else:
            print("  -> WARNING: No PDF booklet link found on page.")
            metadata['requires_pdf_processing'] = False # No PDF to process

    # --- Scrape remaining metadata (safely) ---
    composer_tag = album_div.find('h4')
    metadata['composer'] = composer_tag.get_text(strip=True) if composer_tag else "Composer not found"

    artists_heading = album_div.find('h5', class_='hyp-headlineartists')
    metadata['performers'] = [a.get_text(strip=True) for a in artists_heading.find_all('a')] if artists_heading else []

    anorak_panel = soup.find('div', class_='panel-body hyp-anorak')
    metadata['recording_details'] = anorak_panel.get_text(separator='\n', strip=True) if anorak_panel else "Details not found"
        
    image_tag = soup.find('img', class_='hyp-album')
    metadata['image_url'] = BASE_URL + image_tag['src'] if image_tag and image_tag.has_attr('src') else "Image not found"

    # Save the JSON file
    filename_base = metadata['catalogue_number'].replace('/', '_')
    json_filepath = os.path.join(OUTPUT_DIR, f"{filename_base}.json")
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    
    print(f"  -> Successfully processed. Data saved to {filename_base}.json")


# The main execution block at the bottom remains the same
if __name__ == '__main__':
    CODE_LIST_FILE = "catalogue_codes.json"

    try:
        with open(CODE_LIST_FILE, 'r') as f:
            codes_to_scrape = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: '{CODE_LIST_FILE}' not found. Run 'parse_codes.py' first.")
        exit()

    total_codes = len(codes_to_scrape)
    print(f"Found {total_codes} total album codes to process.")

    for i, code in enumerate(codes_to_scrape):
        url_safe_code = code.replace('/', '%2F')
        url = f"https://www.hyperion-records.co.uk/dc.asp?dc=D_{url_safe_code}"
        
        print(f"\n--- Processing album {i+1} of {total_codes} (Code: {code}) ---")
        scrape_hyperion_album(url)
        
        time.sleep(random.uniform(1.0, 2.0)) 

    print("\n--- All albums have been processed! ---")