# main.tf

# 1. The VPC - Your private network
resource "aws_vpc" "hyperion_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "Hyperion-VPC"
  }
}

# 2. The Public Subnet - Where the EC2 instance will live
resource "aws_subnet" "hyperion_public_subnet" {
  vpc_id     = aws_vpc.hyperion_vpc.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true # gives the EC2 a public IP
  tags = {
    Name = "Hyperion-Public-Subnet"
  }
}

# 3. The Internet Gateway - The door to the internet
resource "aws_internet_gateway" "hyperion_gw" {
  vpc_id = aws_vpc.hyperion_vpc.id
  tags = {
    Name = "Hyperion-IGW"
  }
}

# 4. The Route Table - The map telling the subnet how to use the door
resource "aws_route_table" "hyperion_rt" {
  vpc_id = aws_vpc.hyperion_vpc.id

  route {
    cidr_block = "0.0.0.0/0" # All outbound traffic
    gateway_id = aws_internet_gateway.hyperion_gw.id
  }

  tags = {
    Name = "Hyperion-Public-Route-Table"
  }
}

# Associate the route table with our public subnet
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.hyperion_public_subnet.id
  route_table_id = aws_route_table.hyperion_rt.id
}

# 5. The S3 Bucket - Your private data store
resource "aws_s3_bucket" "hyperion_data" {
  # Change this line
  bucket = var.s3_bucket_name 

  tags = {
    Name = "HyperionData"
  }
}

# 6. The EC2 Instance Request
resource "aws_instance" "scraper_node" {
  ami           = "ami-092ff8e60e2d51e19" 
  instance_type = "t3.micro"
  
  # Attach the IAM role for S3 access
  iam_instance_profile = aws_iam_instance_profile.s3_access_profile.name

  # Place it in our public subnet and attach the firewall
  subnet_id              = aws_subnet.hyperion_public_subnet.id
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  
  # Associate our public SSH key
  key_name = aws_key_pair.deployer_key.key_name

  # Run our startup script
  user_data = templatefile("user_data.sh.tpl", {
  bucket_name = aws_s3_bucket.hyperion_data.id
  })


  tags = {
    Name = "Hyperion-Scraper-Node"
  }
}

# 7. SQS Queues for Job Management ---

# The Dead-Letter Queue (DLQ) for failed messages
resource "aws_sqs_queue" "processing_dlq" {
  name = "hyperion-processing-dlq"
}

# The main processing queue, configured to use the DLQ
resource "aws_sqs_queue" "processing_queue" {
  name                      = "hyperion-processing-queue"
  delay_seconds             = 0
  max_message_size          = 262144 # 256KB
  message_retention_seconds = 345600 # 4 days
  visibility_timeout_seconds = 300   # 5 minutes, should be > worker lambda timeout

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.processing_dlq.arn,
    maxReceiveCount     = 3 # After 3 failures, send to DLQ
  })
}

# --- 8. Lambda Triggers ---

# This resource connects the SQS queue to the Worker Lambda
resource "aws_lambda_event_source_mapping" "sqs_trigger" {
  event_source_arn = aws_sqs_queue.processing_queue.arn
  function_name    = aws_lambda_function.worker_lambda.arn
  batch_size       = 5 # Process up to 5 messages in parallel per invocation
}


# --- 9. EC2 Instance for Vectorization ---

# IAM Role and Policy for the vectorization EC2 instance

# Define variables for prefix and model ID if they're not hardcoded
variable "VECTOR_STORE_PREFIX" {
  description = "Prefix for objects in the vector store bucket"
  default     = "vector-store/"
}

variable "BEDROCK_MODEL_ID" {
  description = "Bedrock model ID"
  default     = "amazon.titan-embed-text-v1"
}

resource "aws_iam_role" "vectorization_ec2_role" {
  name = "hyperion-vectorization-ec2-role"
  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = { Service = "ec2.amazonaws.com" }
    }]
  })
}

resource "aws_iam_policy" "vectorization_ec2_policy" {
  name   = "hyperion-vectorization-ec2-policy"
  policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [
      {
        # Permissions to read the processed text files
        Action   = ["s3:GetObject", "s3:ListBucket"],
        Effect   = "Allow",
        Resource = ["${aws_s3_bucket.hyperion_data.arn}", "${aws_s3_bucket.hyperion_data.arn}/processed_text/*"]
      },
      {
        # Permission to write the final Parquet file
        Action   = "s3:PutObject",
        Effect   = "Allow",
        Resource = "${aws_s3_bucket.hyperion_data.arn}/${var.vector_store_prefix}*"
      },
      {
        # Permission to call the Bedrock embedding model
        Action   = "bedrock:InvokeModel",
        Effect   = "Allow",
        Resource = "arn:aws:bedrock:${var.aws_region}::foundation-model/${var.bedrock_model_id}"
      }
    ]
  })
  

}

resource "aws_iam_role_policy_attachment" "vectorization_ec2_policy_attach" {
  role       = aws_iam_role.vectorization_ec2_role.name
  policy_arn = aws_iam_policy.vectorization_ec2_policy.arn
}

# The Instance Profile attaches the role to the EC2 instance
resource "aws_iam_instance_profile" "vectorization_ec2_profile" {
  name = "hyperion-vectorization-ec2-profile"
  role = aws_iam_role.vectorization_ec2_role.name
}

resource "aws_instance" "vectorization_runner" {
  # Find the latest Amazon Linux 2 AMI for your region (eu-central-1)
  # This is a current one, but you can search for the latest if needed.
  ami           = "ami-0af9b40b1a16fe700" 
  
  # t3.medium is a good choice for this task as pandas/pyarrow can use more memory.
  instance_type = "t3.medium"
  
  # Attach the IAM role for S3 and Bedrock access
  iam_instance_profile = aws_iam_instance_profile.vectorization_ec2_profile.name

  # Place it in your public subnet and attach a firewall allowing SSH (for debugging)
  # Assumes you have these resources from your previous setup.
  subnet_id              = aws_subnet.hyperion_public_subnet.id
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  
  # Associate your public SSH key
  key_name = aws_key_pair.deployer_key.key_name

  # Run our startup script using the new template file
  user_data = templatefile("user_data.sh2.tpl", {
    # This passes the bucket name from your Terraform config into the template script
    bucket_name = aws_s3_bucket.hyperion_data.id
  })

  tags = {
    Name = "Hyperion Vectorization Runner"
  }
}