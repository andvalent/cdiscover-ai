import boto3
import os
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

S3_BUCKET = os.environ['S3_BUCKET_NAME']
SQS_QUEUE_URL = os.environ['SQS_QUEUE_URL']
PROCESSED_TEXT_PREFIX = 'processed_text/'
JSON_PREFIX = 'json/'

s3 = boto3.client('s3')
sqs = boto3.client('sqs')

def lambda_handler(event, context):
    """
    Scans the S3 bucket for JSON files that haven't been processed yet
    and sends a message to SQS for each one.
    Accepts an optional 'batch_size' in the event payload.
    """
    logger.info("Dispatcher starting...")
    batch_size = event.get('batch_size', 100) # Default to a batch of 100
    
    # 1. Get a list of already processed files for efficient checking
    processed_paginator = s3.get_paginator('list_objects_v2')
    processed_pages = processed_paginator.paginate(Bucket=S3_BUCKET, Prefix=PROCESSED_TEXT_PREFIX)
    processed_files = {os.path.basename(obj['Key']).replace('.txt', '') for page in processed_pages for obj in page.get('Contents', [])}
    logger.info(f"Found {len(processed_files)} already processed files.")

    # 2. Iterate through source JSON files and queue up unprocessed ones
    json_paginator = s3.get_paginator('list_objects_v2')
    json_pages = json_paginator.paginate(Bucket=S3_BUCKET, Prefix=JSON_PREFIX)
    
    messages_sent = 0
    for page in json_pages:
        for obj in page.get('Contents', []):
            if messages_sent >= batch_size:
                logger.info(f"Batch size of {batch_size} reached. Stopping.")
                return {'statusCode': 200, 'body': f'Successfully queued {messages_sent} jobs.'}

            if not obj['Key'].endswith('.json'):
                continue
            
            # Filename base is the catalogue number, e.g., CDA68123 or CDA66071_2
            filename_base = os.path.basename(obj['Key']).replace('.json', '')
            
            if filename_base not in processed_files:
                message_body = {'s3_key': obj['Key']}
                sqs.send_message(
                    QueueUrl=SQS_QUEUE_URL,
                    MessageBody=json.dumps(message_body)
                )
                logger.info(f"Queued job for: {obj['Key']}")
                messages_sent += 1

    logger.info(f"Dispatcher finished. Sent {messages_sent} new jobs to the queue.")
    return {'statusCode': 200, 'body': f'Successfully queued {messages_sent} jobs.'}