# iam.tf

# 1. The IAM Role (the "ID badge" for the EC2 instance)
resource "aws_iam_role" "s3_access_role" {
  name = "ec2-s3-hyperion-access-role"

  # This policy allows the EC2 service to "assume" this role
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
      },
    ],
  })
}

# 2. The IAM Policy (the "permission slip" detailing what the role can do)
resource "aws_iam_policy" "s3_access_policy" {
  name        = "hyperion-s3-access-policy"
  description = "Allows EC2 to write to the Hyperion data S3 bucket"

  # This policy grants permission to put objects in our specific bucket
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "s3:PutObject",
          "s3:GetObject"
        ],
        Effect   = "Allow",
        Resource = "${aws_s3_bucket.hyperion_data.arn}/*" # Only on objects inside the bucket
      },
      {
        Action = [
          "s3:ListBucket"
        ],
        Effect   = "Allow",
        Resource = aws_s3_bucket.hyperion_data.arn # Only on the bucket itself
      }
    ]
  })
}

# 3. Attach the policy to the role
resource "aws_iam_role_policy_attachment" "s3_policy_attach" {
  role       = aws_iam_role.s3_access_role.name
  policy_arn = aws_iam_policy.s3_access_policy.arn
}

# 4. Create an instance profile to make the role available to EC2
resource "aws_iam_instance_profile" "s3_access_profile" {
  name = "ec2-s3-hyperion-access-profile"
  role = aws_iam_role.s3_access_role.name
}


# Role for the Dispatcher Lambda
resource "aws_iam_role" "dispatcher_lambda_role" {
  name = "hyperion-dispatcher-lambda-role"
  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

# Policy allowing Dispatcher to list S3 and send to SQS
resource "aws_iam_policy" "dispatcher_policy" {
  name   = "hyperion-dispatcher-policy"
  policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        Action   = ["s3:ListBucket", "s3:GetObject"], # GetObject is useful for checking existence
        Effect   = "Allow",
        Resource = ["${aws_s3_bucket.hyperion_data.arn}", "${aws_s3_bucket.hyperion_data.arn}/*"]
      },
      {
        Action   = "sqs:SendMessage",
        Effect   = "Allow",
        Resource = aws_sqs_queue.processing_queue.arn
      }
    ]
  })
}
resource "aws_iam_role_policy_attachment" "dispatcher_policy_attach" {
  role       = aws_iam_role.dispatcher_lambda_role.name
  policy_arn = aws_iam_policy.dispatcher_policy.arn
}
resource "aws_iam_role_policy_attachment" "dispatcher_logs_attach" {
  role       = aws_iam_role.dispatcher_lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Role for the Worker Lambda
resource "aws_iam_role" "worker_lambda_role" {
  name = "hyperion-worker-lambda-role"
  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

# Policy allowing Worker to read/write S3 and manage SQS messages
resource "aws_iam_policy" "worker_policy" {
  name   = "hyperion-worker-policy"
  policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        Action   = ["s3:GetObject", "s3:PutObject"],
        Effect   = "Allow",
        Resource = "${aws_s3_bucket.hyperion_data.arn}/*"
      },
      {
        Action   = ["sqs:ReceiveMessage", "sqs:DeleteMessage", "sqs:GetQueueAttributes"],
        Effect   = "Allow",
        Resource = aws_sqs_queue.processing_queue.arn
      }
    ]
  })
}
resource "aws_iam_role_policy_attachment" "worker_policy_attach" {
  role       = aws_iam_role.worker_lambda_role.name
  policy_arn = aws_iam_policy.worker_policy.arn
}
resource "aws_iam_role_policy_attachment" "worker_logs_attach" {
  role       = aws_iam_role.worker_lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}