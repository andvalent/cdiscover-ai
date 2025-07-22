# api.tf
# This file contains all resources for the serverless RAG Search API.

# --- 1. IAM Role & Policy for the RAG API Lambda ---
resource "aws_iam_role" "rag_api_lambda_role" {
  name = "hyperion-rag-api-lambda-role" # Specific name
  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_policy" "rag_api_lambda_policy" {
  name   = "hyperion-rag-api-lambda-policy" # Specific name
  policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        Action   = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
        Effect   = "Allow",
        Resource = "arn:aws:logs:*:*:*"
      },
      {
        Action   = ["s3:GetObject", "s3:ListBucket"],
        Effect   = "Allow",
        Resource = [
          aws_s3_bucket.hyperion_data.arn,
          "${aws_s3_bucket.hyperion_data.arn}/vector-store/*"
        ]
      },
      {
        Action   = "bedrock:InvokeModel",
        Effect   = "Allow",
        Resource = [
          "arn:aws:bedrock:${var.aws_region}::foundation-model/amazon.titan-embed-text-v1",
          "arn:aws:bedrock:${var.aws_region}::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "rag_api_lambda_policy_attach" {
  role       = aws_iam_role.rag_api_lambda_role.name
  policy_arn = aws_iam_policy.rag_api_lambda_policy.arn
}

# --- 2. ZIP the Lambda Code ---
data "archive_file" "rag_api_zip" {
  type        = "zip"
  source_dir  = "${path.module}/rag_api_lambda" # Points to our new, specific directory
  output_path = "${path.module}/rag_api_deployment.zip"
}

# --- 3. The RAG API Lambda Function Resource ---
resource "aws_lambda_function" "rag_api_lambda" {
  filename         = data.archive_file.rag_api_zip.output_path
  function_name    = "hyperion-rag-api-handler" # Specific name
  role             = aws_iam_role.rag_api_lambda_role.arn
  handler          = "handler.lambda_handler" # File is handler.py, function is lambda_handler
  runtime          = "python3.10"             # <<-- UPDATED from python3.9 for modern support
  source_code_hash = data.archive_file.rag_api_zip.output_base64sha256

  # <<-- ADDED: The Klayers for Pandas, Numpy, and PyArrow
  layers = [
    # Layer 1: Pandas (which includes Numpy) for Python 3.10
    "arn:aws:lambda:${var.aws_region}:770693421928:layer:Klayers-p310-pandas:25",

    # Layer 2: PyArrow for Python 3.10
    "arn:aws:lambda:${var.aws_region}:770693421928:layer:Klayers-p310-pyarrow:5"
  ]

  memory_size = 1024
  timeout     = 30

  environment {
    variables = {
      S3_BUCKET_NAME = aws_s3_bucket.hyperion_data.id
      AWS_REGION     = var.aws_region
    }
  }
}

# --- 4. API Gateway REST API ---
resource "aws_api_gateway_rest_api" "rag_api" {
  name        = "HyperionRAG_API" # Specific name
  description = "API for the Hyperion RAG search application"
}

resource "aws_api_gateway_resource" "rag_api_search_resource" {
  rest_api_id = aws_api_gateway_rest_api.rag_api.id
  parent_id   = aws_api_gateway_rest_api.rag_api.root_resource_id
  path_part   = "search"
}

resource "aws_api_gateway_method" "rag_api_search_post" {
  rest_api_id   = aws_api_gateway_rest_api.rag_api.id
  resource_id   = aws_api_gateway_resource.rag_api_search_resource.id
  http_method   = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "rag_api_lambda_integration" {
  rest_api_id             = aws_api_gateway_rest_api.rag_api.id
  resource_id             = aws_api_gateway_resource.rag_api_search_resource.id
  http_method             = aws_api_gateway_method.rag_api_search_post.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.rag_api_lambda.invoke_arn
}

# --- 5. API Gateway Deployment and Stage ---
resource "aws_api_gateway_deployment" "rag_api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.rag_api.id
  depends_on  = [aws_api_gateway_integration.rag_api_lambda_integration]
  stage_name  = "v1"
}

# --- 6. Lambda Permission for API Gateway to Invoke ---
resource "aws_lambda_permission" "rag_api_gateway_permission" {
  statement_id  = "AllowAPIGatewayToInvokeRAGLambda"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.rag_api_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.rag_api.execution_arn}/*/${aws_api_gateway_method.rag_api_search_post.http_method}${aws_api_gateway_resource.rag_api_search_resource.path}"
}

# --- 7. Output the Final API Endpoint URL ---
output "rag_api_invoke_url" {
  description = "The invoke URL for the RAG API search endpoint"
  value       = "${aws_api_gateway_deployment.rag_api_deployment.invoke_url}${aws_api_gateway_resource.rag_api_search_resource.path}"
}