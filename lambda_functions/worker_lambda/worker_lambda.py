import boto3
import json
from pypdf import PdfReader
import os
import io
import logging
import re

# --- Configuration (from Lambda Environment Variables) ---
S3_BUCKET = os.environ['S3_BUCKET_NAME']
SOURCE_JSON_PREFIX = 'json/'
SOURCE_PDF_PREFIX = 'pdf/'
DESTINATION_PREFIX = 'processed_text/'

s3 = boto3.client('s3')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# --- PDF Cleaning Logic (from our local script) ---
def clean_extracted_pdf_text(text: str) -> str:
    # This function remains unchanged.
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    boilerplate_patterns = [
        r'please note\s+FULL DIGITAL ARTWORK.*?SCANNED BOOKLET\.',
        r'The Compact Disc Digital Audio System.*?listening enjoyment\.',
    ]
    for pattern in boilerplate_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)
    
    cleaned_lines = [line for line in text.split('\n') if not line.strip().isdigit()]
    text = "\n".join(cleaned_lines)
    return ' '.join(text.split())

def lambda_handler(event, context):
    """
    Triggered by SQS. Processes one album message at a time.
    """
    for record in event['Records']:
        message_body = json.loads(record['body'])
        source_json_key = message_body['s3_key']
        logger.info(f"Processing job for: {source_json_key}")

        try:
            # 1. Read the main JSON file (No changes here)
            json_obj = s3.get_object(Bucket=S3_BUCKET, Key=source_json_key)
            data = json.loads(json_obj['Body'].read().decode('utf-8'))
            filename_base = os.path.basename(source_json_key).replace('.json', '')

            # 2. Start building the final text document (No changes here)
            performers = ", ".join(filter(None, data.get('performers', [])))
            final_text_parts = [
                f"Album Title: {data.get('album_title', 'N/A')}",
                f"Catalogue Number: {data.get('catalogue_number', 'N/A')}",
                f"Composer(s): {data.get('composer', 'N/A')}",
                f"Performer(s): {performers}",
                f"Source URL: {data.get('source_url', 'N/A')}\n",
            ]
            
            # 3. Add liner notes from JSON if they exist (No changes here)
            if data.get('liner_notes_text'):
                final_text_parts.append(f"--- Liner Notes ---\n{data['liner_notes_text']}\n")

            # 4. Check if we also need to process a linked PDF
            if data.get('requires_pdf_processing', False):
                pdf_key = f"{SOURCE_PDF_PREFIX}{filename_base}.pdf"
                try:
                    # --- THIS IS THE SECTION THAT HAS CHANGED ---
                    pdf_obj = s3.get_object(Bucket=S3_BUCKET, Key=pdf_key)
                    pdf_buffer = io.BytesIO(pdf_obj['Body'].read())
                    
                    # Use pypdf's PdfReader to open the in-memory buffer
                    reader = PdfReader(pdf_buffer)
                    
                    # Iterate through pages and extract text
                    page_texts = [page.extract_text() for page in reader.pages]
                    raw_pdf_text = "\n".join(page_texts)
                    # --- END OF CHANGED SECTION ---
                    
                    cleaned_pdf_text = clean_extracted_pdf_text(raw_pdf_text)
                    final_text_parts.append(f"--- Cleaned Booklet Notes ---\n{cleaned_pdf_text}\n")
                    logger.info(f"Successfully processed and merged PDF: {pdf_key}")
                except s3.exceptions.NoSuchKey:
                    logger.warning(f"Flag 'requires_pdf_processing' was true, but PDF not found at {pdf_key}")
                except Exception as e:
                    logger.error(f"Failed to process PDF {pdf_key}. Error: {e}")

            # 5. Assemble and save the final .txt file (No changes here)
            final_text = "\n".join(final_text_parts)
            destination_key = f"{DESTINATION_PREFIX}{filename_base}.txt"
            
            s3.put_object(
                Bucket=S3_BUCKET,
                Key=destination_key,
                Body=final_text.encode('utf-8')
            )
            logger.info(f"Successfully created processed file: {destination_key}")

        except Exception as e:
            logger.error(f"FATAL: Could not process message for {source_json_key}. Error: {e}", exc_info=True)
            raise e

    return {'statusCode': 200, 'body': 'Processing complete'}