#!/bin/bash
yum update -y
yum install -y git python3-pip

# Set the S3 bucket name as an environment variable for all users.
# The ${bucket_name} part will be replaced by Terraform with the real bucket name.
echo 'export S3_BUCKET_NAME="${bucket_name}"' >> /etc/profile