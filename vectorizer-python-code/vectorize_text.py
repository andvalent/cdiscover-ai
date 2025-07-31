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
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
    )
    
    current_batch = []
    batch_counter = 0
    files_processed = 0
    
    ### <<< ADD THIS LINE >>>
    # Set a limit for our test run. Set to None or remove for the full run.
    TEST_FILE_LIMIT = 10 
    
    logging.info(f"Listing all files from s3://{S3_BUCKET}/{PROCESSED_TEXT_PREFIX}")
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=S3_BUCKET, Prefix=PROCESSED_TEXT_PREFIX)
    
    stop_processing = False # A flag to help us break out of the nested loop
    for page in pages:
        for obj in page.get('Contents', []):
            if not obj['Key'].endswith('.txt'):
                continue
            
            s3_key = obj['Key']
            
            try:
                # [ ... All your existing processing logic for a single file remains here ... ]
                # It's perfect as it is.
                response = s3_client.get_object(Bucket=S3_BUCKET, Key=s3_key)
                text_content = response['Body'].read().decode('utf-8')
                parsed_metadata, main_content_to_chunk = parse_metadata_from_text(text_content)
                if not parsed_metadata.get('source_url') or not parsed_metadata.get('album_title'):
                    logging.warning(f"Skipping file {s3_key} due to missing essential metadata (URL or Title).")
                    continue
                chunks = text_splitter.split_text(main_content_to_chunk)
                for i, chunk_text in enumerate(chunks):
                    enriched_chunk_text = (
                        f"From the album titled '{parsed_metadata.get('album_title', 'N/A')}' by composer(s) {parsed_metadata.get('composer', 'N/A')}. "
                        f"Note snippet: {chunk_text}"
                    )
                    chunk_data = {
                        'chunk_text': enriched_chunk_text, 
                        'album_title': parsed_metadata.get('album_title'),
                        'catalogue_number': parsed_metadata.get('catalogue_number'),
                        'composer': parsed_metadata.get('composer'),
                        'performer': parsed_metadata.get('performer'),
                        'source_url': parsed_metadata.get('source_url'),
                        'chunk_id': f"{parsed_metadata.get('catalogue_number', 'unknown')}_{i}",
                        's3_source_key': s3_key
                    }
                    current_batch.append(chunk_data)
                    if len(current_batch) >= BATCH_SIZE:
                        batch_counter += 1
                        process_and_upload_batch(current_batch, batch_counter, embeddings, s3_client)
                        current_batch.clear()
                
                # We successfully processed one file, so we increment the counter
                files_processed += 1
                logging.info(f"Processed file {files_processed}/{TEST_FILE_LIMIT}: {s3_key}")
                
                ### <<< ADD THIS LINE >>>
                # Check if we have reached our test limit
                if files_processed >= TEST_FILE_LIMIT:
                    stop_processing = True
                    break # Exit the inner loop (for obj in page...)

            except Exception as e:
                logging.error(f"Failed to process file {s3_key}. Error: {e}", exc_info=True)
        
        ### <<< ADD THIS LINE >>>
        # If the flag is set, exit the outer loop (for page in pages...) too
        if stop_processing:
            logging.info(f"Reached test limit of {TEST_FILE_LIMIT} files. Stopping.")
            break

    # Process the final batch
    if current_batch:
        batch_counter += 1
        process_and_upload_batch(current_batch, batch_counter, embeddings, s3_client)

    logging.info(f"--- BATCH Vectorization process complete! Processed {files_processed} files in {batch_counter} batches. ---")