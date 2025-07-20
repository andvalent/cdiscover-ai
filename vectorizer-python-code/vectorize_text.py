import boto3
import pandas as pd
import os
import logging
from langchain_aws import BedrockEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

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


def main():
    """
    Main function to run the vectorization process in memory-efficient batches.
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
    
    # This list will only hold one batch at a time, not everything.
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
            catalogue_number = os.path.basename(s3_key).replace('.txt', '')
            
            try:
                response = s3_client.get_object(Bucket=S3_BUCKET, Key=s3_key)
                text_content = response['Body'].read().decode('utf-8')
                
                chunks = text_splitter.split_text(text_content)
                
                for i, chunk in enumerate(chunks):
                    current_batch.append({
                        'catalogue_number': catalogue_number,
                        'chunk_id': f"{catalogue_number}_{i}",
                        'chunk_text': chunk,
                        's3_source_key': s3_key
                    })
                    
                    # --- CORE LOGIC CHANGE ---
                    # When the batch is full, process it and clear it.
                    if len(current_batch) >= BATCH_SIZE:
                        batch_counter += 1
                        process_and_upload_batch(current_batch, batch_counter, embeddings, s3_client)
                        current_batch.clear() # Free the memory
                
                files_processed += 1
                if files_processed % 100 == 0:
                    logging.info(f"Files processed so far: {files_processed}")

            except Exception as e:
                logging.error(f"Failed to process file {s3_key}. Error: {e}")

    # --- After the loop, process any remaining chunks in the last batch ---
    if current_batch:
        batch_counter += 1
        process_and_upload_batch(current_batch, batch_counter, embeddings, s3_client)

    logging.info(f"--- BATCH Vectorization process complete! Processed {files_processed} files in {batch_counter} batches. ---")

if __name__ == '__main__':
    main()