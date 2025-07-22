# This file (handler.py) contains the core logic for our RAG API Lambda function.
import boto3
import pandas as pd
import numpy as np
import os
import json
import logging

# (The rest of the Python code is exactly the same as provided in the previous response)
# ...
# --- Setup Logging ---
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# --- Environment Variables ---
S3_BUCKET = os.environ.get("S3_BUCKET_NAME") 
S3_PREFIX = "vector-store/"
BEDROCK_EMBEDDING_MODEL_ID = "amazon.titan-embed-text-v1"
BEDROCK_GENERATION_MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"
AWS_REGION = os.environ.get("AWS_REGION", "eu-central-1")

# --- Global Variables (for "warm start") ---
df = None
vectors = None
vector_norms = None

def load_vector_db():
    global df, vectors, vector_norms
    if df is not None:
        logger.info("Vector DB already loaded. Skipping.")
        return

    logger.info("Starting GLOBAL INITIALIZATION (cold start)...")
    logger.info(f"Loading vector database from s3://{S3_BUCKET}/{S3_PREFIX}")
    # Note: Lambda needs `s3fs` installed to read from s3:// paths
    df = pd.read_parquet(f"s3://{S3_BUCKET}/{S3_PREFIX}")
    
    # Pre-calculate the norms of the vectors for faster cosine similarity
    vectors = np.array(df['vector'].tolist())
    vector_norms = np.linalg.norm(vectors, axis=1)
    
    logger.info(f"Initialization complete. Loaded {len(df)} vectors.")

# Initialize Bedrock client globally
bedrock_runtime = boto3.client('bedrock-runtime', region_name=AWS_REGION)

def get_bedrock_embedding(text):
    # ... (same as before)
    body = json.dumps({"inputText": text})
    response = bedrock_runtime.invoke_model(
        body=body, modelId=BEDROCK_EMBEDDING_MODEL_ID, 
        contentType="application/json", accept="application/json"
    )
    response_body = json.loads(response['body'].read())
    return response_body['embedding']

def find_top_matches(query_vector, k=5):
    # ... (same as before)
    query_norm = np.linalg.norm(query_vector)
    cosine_similarities = np.dot(vectors, query_vector) / (vector_norms * query_norm)
    top_k_indices = np.argsort(cosine_similarities)[-k:][::-1]
    top_matches = df.iloc[top_k_indices]
    return top_matches

def generate_recommendation(query, context_chunks):
    # ... (same as before)
    context = "\n---\n".join(context_chunks)
    prompt = f"""Human: You are Hyperion, a helpful classical music recommendation assistant. A user is looking for music recommendations based on the following query: "{query}"

    Based on my internal knowledge base, I have found the following relevant pieces of information about various albums:
    <context>
    {context}
    </context>

    Please synthesize this information to provide a friendly, insightful, and helpful recommendation. Address the user directly. Explain *why* certain albums might be a good fit based on the context provided. Recommend 1-3 specific albums by their catalogue number and provide the relevant text chunks that support your recommendation. Do not make up information. Base your answer only on the provided context.

    Assistant:"""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}]
    })
    response = bedrock_runtime.invoke_model(
        body=body, modelId=BEDROCK_GENERATION_MODEL_ID,
        contentType="application/json", accept="application/json"
    )
    response_body = json.loads(response['body'].read())
    return response_body['content'][0]['text']

def lambda_handler(event, context):
    try:
        # Load the database on first invocation
        load_vector_db()

        if df is None:
            return {'statusCode': 500, 'body': json.dumps({'error': 'Vector database is not loaded.'})}
        
        body = json.loads(event.get('body', '{}'))
        query = body.get('query')
        if not query:
            return {'statusCode': 400, 'body': json.dumps({'error': 'Query not provided.'})}
        
        logger.info(f"Received query: {query}")
        
        query_vector = get_bedrock_embedding(query)
        top_matches_df = find_top_matches(query_vector)
        context_chunks = top_matches_df['chunk_text'].tolist()
        recommendation = generate_recommendation(query, context_chunks)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'recommendation': recommendation})
        }
    except Exception as e:
        logger.error(f"Error during lambda execution: {e}", exc_info=True)
        return {'statusCode': 500, 'body': json.dumps({'error': 'An internal server error occurred.'})}