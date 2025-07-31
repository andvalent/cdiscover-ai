import boto3
import pandas as pd
import os
import logging
from langchain_aws import BedrockEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
PROCESSED_TEXT_PREFIX = 'processed_text/'
VECTOR_STORE_PREFIX = 'vector-store/'
# Process 500 chunks at a time to keep memory usage low.
BATCH_SIZE = 500
# The base name for the output files. We will add parts to it.
OUTPUT_FILENAME_BASE = 'hyperion_embeddings'

BEDROCK_MODEL_ID = "amazon.titan-embed-text-v1"

# --- NEW: Helper function to process and upload one batch ---
def process_and_upload_batch(batch_chunks, batch_number, embeddings_client, s3_client):
    """
    Takes a batch of chunks, vectorizes them, and uploads the result as a Parquet file.
    """
    if not batch_chunks:
        logging.info("Skipping empty batch.")
        return

    logging.info(f"--- Processing batch {batch_number} with {len(batch_chunks)} chunks ---")

    # 1. Get the text from the batch
    batch_texts = [item['chunk_text'] for item in batch_chunks]

    # 2. Vectorize the batch
    try:
        vectors = embeddings_client.embed_documents(batch_texts)
        logging.info(f"Batch {batch_number}: Successfully received {len(vectors)} embeddings from Bedrock.")
    except Exception as e:
        logging.error(f"Batch {batch_number}: Bedrock embedding failed. Error: {e}")
        # Decide if you want to skip this batch or stop the whole process
        return

    # 3. Combine metadata and vectors into a DataFrame
    for i, item in enumerate(batch_chunks):
        item['vector'] = vectors[i]
    df = pd.DataFrame(batch_chunks)

    # 4. Save the DataFrame as a Parquet file and upload to S3
    output_filename = f"{OUTPUT_FILENAME_BASE}_part_{batch_number:05d}.parquet"
    local_path = f"/tmp/{output_filename}"
    s3_output_key = f"{VECTOR_STORE_PREFIX}{output_filename}"
    
    try:
        df.to_parquet(local_path, index=False)
        s3_client.upload_file(local_path, S3_BUCKET, s3_output_key)
        logging.info(f"Batch {batch_number}: Successfully uploaded to s3://{S3_BUCKET}/{s3_output_key}")
    except Exception as e:
        logging.error(f"Batch {batch_number}: S3 upload failed. Error: {e}")
    finally:
        # 5. Clean up the local file to save disk space
        if os.path.exists(local_path):
            os.remove(local_path)

def parse_metadata_from_text(text_content):
    """
    A new helper function to extract structured metadata from the raw text.
    This is the core of our fix for the metadata problem.
    """
    metadata = {}
    
    # Use regular expressions to find and extract our key-value pairs.
    # The 're.DOTALL' flag allows '.' to match newlines.
    # The '(.*?)' is a non-greedy match for the value.
    album_title_match = re.search(r"Album Title: (.*?)\n", text_content)
    if album_title_match:
        metadata['album_title'] = album_title_match.group(1).strip()

    catalogue_match = re.search(r"Catalogue Number: (.*?)\n", text_content)
    if catalogue_match:
        metadata['catalogue_number'] = catalogue_match.group(1).strip()
    
    composer_match = re.search(r"Composer\(s\): (.*?)\n", text_content)
    if composer_match:
        metadata['composer'] = composer_match.group(1).strip()

    performer_match = re.search(r"Performer\(s\): (.*?)\n", text_content)
    if performer_match:
        metadata['performer'] = performer_match.group(1).strip()

    url_match = re.search(r"Source URL: (.*?)\n", text_content)
    if url_match:
        metadata['source_url'] = url_match.group(1).strip()

    # Isolate the actual content to be chunked.
    # We can split the text after the metadata header. A simple way is to find the end of the URL line.
    content_start_index = 0
    if url_match:
        content_start_index = url_match.end()
    
    main_content = text_content[content_start_index:].strip()
    
    return metadata, main_content

def main():
    """
    Main function with corrected logic for parsing and chunking.
    """
    if not S3_BUCKET:
        logging.error("S3_BUCKET_NAME environment variable not set. Exiting.")
        return

    logging.info(f"--- Starting BATCH Vectorization Run for bucket: {S3_BUCKET} ---")
    
    s3_client = boto3.client('s3')
    bedrock_client = boto3.client('bedrock-runtime', region_name='eu-central-1') 
    
    embeddings = BedrockEmbeddings(client=bedrock_client, model_id=BEDROCK_MODEL_ID)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, # You might want to experiment with smaller sizes like 512
        chunk_overlap=100,
        length_function=len,
    )
    
    current_batch = []
    batch_counter = 0
    files_processed = 0

    logging.info(f"Listing all files from s3://{S3_BUCKET}/{PROCESSED_TEXT_PREFIX}")
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=S3_BUCKET, Prefix=PROCESSED_TEXT_PREFIX)
    
    for page in pages:
        for obj in page.get('Contents', []):
            if not obj['Key'].endswith('.txt'):
                continue
            
            s3_key = obj['Key']
            
            try:
                response = s3_client.get_object(Bucket=S3_BUCKET, Key=s3_key)
                text_content = response['Body'].read().decode('utf-8')
                
                # --- FIX #1: PARSE METADATA AND ISOLATE MAIN CONTENT ---
                # This is the most critical change.
                parsed_metadata, main_content_to_chunk = parse_metadata_from_text(text_content)
                
                # If we couldn't parse essential metadata, log a warning and skip.
                if not parsed_metadata.get('source_url') or not parsed_metadata.get('album_title'):
                    logging.warning(f"Skipping file {s3_key} due to missing essential metadata (URL or Title).")
                    continue

                # --- FIX #2: CHUNK ONLY THE NARRATIVE CONTENT ---
                chunks = text_splitter.split_text(main_content_to_chunk)
                
                for i, chunk_text in enumerate(chunks):
                    # --- FIX #3: ENRICH THE CHUNK TEXT FOR BETTER EMBEDDINGS ---
                    # Prepend key context to the text that will be embedded.
                    # This makes the vector much more specific and powerful.
                    # This new format ensures all key metadata is available to the LLM within the context.
                    enriched_chunk_text = (
                        f"Album Title: {parsed_metadata.get('album_title', 'N/A')}\n"
                        f"Catalogue Number: {parsed_metadata.get('catalogue_number', 'N/A')}\n"
                        f"Composer(s): {parsed_metadata.get('composer', 'N/A')}\n"
                        f"--- Note Snippet ---\n{chunk_text}"
                    )

                    # Create a dictionary containing the TRUE metadata, separate from the text.
                    # This is what you will store in Parquet and show to the user.
                    chunk_data = {
                        # This is the text we will vectorize
                        'chunk_text': enriched_chunk_text, 
                        
                        # These are the clean metadata fields for your application
                        'album_title': parsed_metadata.get('album_title'),
                        'catalogue_number': parsed_metadata.get('catalogue_number'),
                        'composer': parsed_metadata.get('composer'),
                        'performer': parsed_metadata.get('performer'),
                        'source_url': parsed_metadata.get('source_url'),
                        'chunk_id': f"{parsed_metadata.get('catalogue_number', 'unknown')}_{i}",
                        's3_source_key': s3_key
                    }
                    current_batch.append(chunk_data)
                    
                    # Batch processing logic remains the same
                    if len(current_batch) >= BATCH_SIZE:
                        batch_counter += 1
                        process_and_upload_batch(current_batch, batch_counter, embeddings, s3_client)
                        current_batch.clear()
                
                files_processed += 1
                if files_processed % 100 == 0:
                    logging.info(f"Files processed so far: {files_processed}")

            except Exception as e:
                logging.error(f"Failed to process file {s3_key}. Error: {e}", exc_info=True)

    # Process the final batch
    if current_batch:
        batch_counter += 1
        process_and_upload_batch(current_batch, batch_counter, embeddings, s3_client)

    logging.info(f"--- BATCH Vectorization process complete! Processed {files_processed} files in {batch_counter} batches. ---")

if __name__ == '__main__':
    main()