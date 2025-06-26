import boto3
import requests
from bs4 import BeautifulSoup
import json
import os
import time
import logging

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

S3_BUCKET_NAME = 'hyperion-classical-assistant'
PDF_PREFIX = 'pdf/'

REQUEST_DELAY_SECONDS = 2 

REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# --- Core Functions ---

def scrape_album_metadata(catalogue_number):
    """
    Scrapes the Hyperion website for a given catalogue number to get metadata.
    Returns a dictionary of metadata or None if it fails.
    """
    url = f"https://www.hyperion-records.co.uk/dc.asp?dc=D_{catalogue_number}"
    logging.info(f"Scraping URL: {url}")

    try:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=15)
        # Raise an exception for bad status codes (like 404, 500)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # --- Metadata Extraction ---
        title = soup.find('meta', property='og:title')
        page_url = soup.find('meta', property='og:url')
        
        # For composer/performers, we need to search the body, as they aren't in meta tags.
        # This is a heuristic: we look for links pointing to composer/performer pages.
        composer_tags = soup.select('a[href*="/cr.asp?cr="]')
        performers_tags = soup.select('a[href*="/il.asp?il="]')
        
        composers = [tag.text.strip() for tag in composer_tags]
        performers = [tag.text.strip() for tag in performers_tags]

        metadata = {
            'album_title': title['content'] if title else 'N/A',
            'source_url': page_url['content'] if page_url else url,
            'catalogue_number': catalogue_number,
            'composers': list(set(composers)), # Use set to remove duplicates
            'performers': list(set(performers))
        }
        
        # Check if we got at least a title
        if metadata['album_title'] == 'N/A':
            logging.warning(f"Could not find a title for {catalogue_number}. Page might be malformed.")
            return None

        return metadata

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch {url}. Error: {e}")
        return None
    except Exception as e:
        logging.error(f"Failed to parse page for {catalogue_number}. Error: {e}", exc_info=True)
        return None


def main():
    """
    Main execution function. Lists PDFs, scrapes metadata, and saves it back to S3.
    """
    logging.info("--- Starting Metadata Patch Script ---")
    s3_client = boto3.client('s3')

    # Use a paginator to handle more than 1000 objects if necessary
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=S3_BUCKET_NAME, Prefix=PDF_PREFIX)

    success_count = 0
    fail_count = 0
    
    for page in pages:
        for obj in page.get('Contents', []):
            key = obj['Key']
            
            # We only care about .pdf files
            if not key.lower().endswith('.pdf'):
                continue

            # Check if metadata already exists to avoid re-processing
            catalogue_number = os.path.basename(key).replace('.pdf', '')
            metadata_key = f"{PDF_PREFIX}{catalogue_number}_metadata.json"
            try:
                s3_client.head_object(Bucket=S3_BUCKET_NAME, Key=metadata_key)
                logging.info(f"Metadata for {catalogue_number} already exists. Skipping.")
                continue
            except s3_client.exceptions.ClientError:
                # This is expected if the file doesn't exist.
                pass

            # --- Process the file ---
            metadata = scrape_album_metadata(catalogue_number)
            
            if metadata:
                # Save the successfully scraped metadata to S3
                s3_client.put_object(
                    Bucket=S3_BUCKET_NAME,
                    Key=metadata_key,
                    Body=json.dumps(metadata, indent=4),
                    ContentType='application/json'
                )
                logging.info(f"Successfully saved metadata for {catalogue_number}")
                success_count += 1
            else:
                logging.warning(f"Could not retrieve metadata for {catalogue_number}")
                fail_count += 1
            
            # --- Be Polite! ---
            time.sleep(REQUEST_DELAY_SECONDS)

    logging.info("--- Script Finished ---")
    logging.info(f"Successfully processed: {success_count}")
    logging.info(f"Failed to process: {fail_count}")

# --- Script Entry Point ---
if __name__ == '__main__':
    main()