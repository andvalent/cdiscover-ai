# --- IAM Role for EC2 ---
resource "aws_iam_role" "rag_ec2_role" {
  name = "hyperion-rag-ec2-role"
  assume_role_policy = jsonencode({
    Version   = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = { Service = "ec2.amazonaws.com" }
    }]
  })
}

# Re-use the same policy logic, but for an EC2 role
resource "aws_iam_policy" "rag_ec2_policy" {
  name   = "hyperion-rag-ec2-policy"
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
          "arn:aws:s3:::${var.s3_bucket_name}",
          "arn:aws:s3:::${var.s3_bucket_name}/vector-store/*"
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

resource "aws_iam_role_policy_attachment" "rag_ec2_policy_attach" {
  role       = aws_iam_role.rag_ec2_role.name
  policy_arn = aws_iam_policy.rag_ec2_policy.arn
}

resource "aws_iam_instance_profile" "rag_ec2_instance_profile" {
  name = "hyperion-rag-ec2-instance-profile"
  role = aws_iam_role.rag_ec2_role.name
}

# --- Security Group (Firewall) ---
resource "aws_security_group" "rag_ec2_sg" {
  name        = "hyperion-rag-ec2-sg"
  description = "Allow HTTP and SSH traffic"

  ingress {
    from_port   = 80 # HTTP
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22 # SSH
    to_port     = 22
    protocol    = "tcp"
    # IMPORTANT: For production, restrict this to your IP address.
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# --- EC2 Instance ---
resource "aws_instance" "rag_api_server" {
  # Standard Amazon Linux 2 AMI. Find the latest for your region if needed.
  ami           = "ami-003c9adf81de74b40" 
  instance_type = "t3.medium" # Need sufficient RAM for pandas
  key_name      = var.ssh_key_name

  iam_instance_profile = aws_iam_instance_profile.rag_ec2_instance_profile.name
  vpc_security_group_ids = [aws_security_group.rag_ec2_sg.id]

  # This runs our setup.sh script on first boot
  user_data = file("${path.module}/setup.sh")

  tags = {
    Name = "Hyperion RAG API Server"
  }
}

