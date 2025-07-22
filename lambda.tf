# lambdas.tf

# --- 1. Define and zip the Dispatcher Lambda's code (NO CHANGES) ---
data "archive_file" "dispatcher_zip" {
  type        = "zip"
  source_dir  = "${path.module}/lambda_functions/dispatcher_lambda/"
  output_path = "${path.module}/dispatcher_lambda.zip"
}

resource "aws_lambda_function" "dispatcher_lambda" {
  filename         = data.archive_file.dispatcher_zip.output_path
  function_name    = "hyperion-dispatcher"
  role             = aws_iam_role.dispatcher_lambda_role.arn
  handler          = "dispatcher_lambda.lambda_handler"
  runtime          = "python3.9"
  source_code_hash = data.archive_file.dispatcher_zip.output_base64sha256
  timeout          = 300

  environment {
    variables = {
      S3_BUCKET_NAME = var.s3_bucket_name
      SQS_QUEUE_URL  = aws_sqs_queue.processing_queue.id
    }
  }
}

# --- 2. Define and zip the Worker Lambda's code (NO CHANGES TO THIS BLOCK) ---
# This block will now zip up your worker_lambda.py AND its dependencies (pypdf)
# because you will install them into the same directory.
data "archive_file" "worker_zip" {
  type        = "zip"
  source_dir  = "${path.module}/lambda_functions/worker_lambda/"
  output_path = "${path.module}/worker_lambda.zip"
}

# --- 3. Define the Worker Lambda, now WITHOUT any layers ---
resource "aws_lambda_function" "worker_lambda" {
  filename         = data.archive_file.worker_zip.output_path
  function_name    = "hyperion-worker"
  role             = aws_iam_role.worker_lambda_role.arn
  handler          = "worker_lambda.lambda_handler"
  runtime          = "python3.9"
  source_code_hash = data.archive_file.worker_zip.output_base64sha256
  memory_size      = 512 # Good for PDF processing
  timeout          = 300 # 5 minutes

  # --- MODIFIED SECTION: The 'layers' attribute is now gone. ---
  # layers = [aws_lambda_layer_version.pymupdf_local_layer.arn] # <-- THIS LINE IS DELETED

  environment {
    variables = {
      S3_BUCKET_NAME = var.s3_bucket_name
    }
  }
}

