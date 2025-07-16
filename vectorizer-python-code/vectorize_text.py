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
# --- MODIFICATION: Use the final production filename ---
OUTPUT_FILENAME = 'hyperion_embeddings.parquet'

# Use a powerful and cost-effective embedding model from Bedrock
BEDROCK_MODEL_ID = "amazon.titan-embed-text-v1"

# --- Main Logic ---

def main():
    """
    Main function to run the vectorization process on the ENTIRE dataset.
    """
    if not S3_BUCKET:
        logging.error("S3_BUCKET_NAME environment variable not set. Exiting.")
        return

    logging.info(f"--- Starting FULL Vectorization Run for bucket: {S3_BUCKET} ---")
    
    # 1. Initialize clients and LangChain components
    s3_client = boto3.client('s3')
    # It's good practice to specify the region for the Bedrock client
    bedrock_client = boto3.client('bedrock-runtime', region_name='eu-central-1') 
    
    embeddings = BedrockEmbeddings(client=bedrock_client, model_id=BEDROCK_MODEL_ID)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
    )
    
    all_chunks_with_metadata = []
    files_processed = 0

    # 2. List all processed text files from S3
    logging.info(f"Listing all files from s3://{S3_BUCKET}/{PROCESSED_TEXT_PREFIX}")
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=S3_BUCKET, Prefix=PROCESSED_TEXT_PREFIX)
    
    # 3. Read, chunk, and prepare text from each file
    for page in pages:
        for obj in page.get('Contents', []):
            if not obj['Key'].endswith('.txt'):
                continue
            
            s3_key = obj['Key']
            catalogue_number = os.path.basename(s3_key).replace('.txt', '')
            
            # Log progress every 100 files to keep track
            if (files_processed + 1) % 100 == 0:
                logging.info(f"Processing file {files_processed + 1}...")
            
            try:
                response = s3_client.get_object(Bucket=S3_BUCKET, Key=s3_key)
                text_content = response['Body'].read().decode('utf-8')
                
                chunks = text_splitter.split_text(text_content)
                
                for i, chunk in enumerate(chunks):
                    all_chunks_with_metadata.append({
                        'catalogue_number': catalogue_number,
                        'chunk_id': f"{catalogue_number}_{i}",
                        'chunk_text': chunk,
                        's3_source_key': s3_key
                    })
                
                files_processed += 1
            except Exception as e:
                logging.error(f"Failed to process file {s3_key}. Error: {e}")

    if not all_chunks_with_metadata:
        logging.warning("No text chunks were generated. Exiting.")
        return

    logging.info(f"Generated a total of {len(all_chunks_with_metadata)} chunks from {files_processed} files to be vectorized.")

    # 4. Vectorize all chunks in a single, efficient batch call
    all_texts = [item['chunk_text'] for item in all_chunks_with_metadata]
    
    logging.info(f"Calling Amazon Bedrock to create embeddings for all {len(all_texts)} chunks. This may take some time...")
    try:
        vectors = embeddings.embed_documents(all_texts)
        logging.info("Successfully received embeddings from Bedrock.")
    except Exception as e:
        logging.error(f"Bedrock embedding failed. Error: {e}")
        return

    # 5. Combine metadata and vectors into a DataFrame
    for i, item in enumerate(all_chunks_with_metadata):
        item['vector'] = vectors[i]
        
    df = pd.DataFrame(all_chunks_with_metadata)

    # 6. Save the DataFrame as a Parquet file and upload to S3
    local_path = f"/tmp/{OUTPUT_FILENAME}"
    df.to_parquet(local_path, index=False)
    logging.info(f"Successfully saved embeddings to local Parquet file: {local_path}")
    
    s3_output_key = f"{VECTOR_STORE_PREFIX}{OUTPUT_FILENAME}"
    logging.info(f"Uploading Parquet file to s3://{S3_BUCKET}/{s3_output_key}")
    try:
        s3_client.upload_file(local_path, S3_BUCKET, s3_output_key)
        logging.info("Upload successful!")
    except Exception as e:
        logging.error(f"S3 upload failed. Error: {e}")

    logging.info("--- FULL Vectorization process complete! ---")

if __name__ == '__main__':
    main()