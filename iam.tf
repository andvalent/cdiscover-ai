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