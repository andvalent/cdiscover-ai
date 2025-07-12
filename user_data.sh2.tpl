#!/bin/bash
# Update the instance and install our dependencies
sudo yum update -y
sudo yum install -y git python3-pip

# Install the required Python packages for the vectorization script
pip3 install --user boto3 langchain langchain_aws pyarrow pandas

# Clone your GitHub repository
# !!! IMPORTANT: Replace this URL with your actual GitHub repository URL !!!
git clone https://github.com/your-username/cdiscover-ai.git /home/ec2-user/app

# Change into the application directory
cd /home/ec2-user/app

# Run the vectorization script, passing the S3 bucket name as an environment variable.
# The "${bucket_name}" variable is injected by Terraform's templatefile function.
S3_BUCKET_NAME="${bucket_name}"  # python3 vectorize_text.py

# When the script is finished, automatically shut down the instance to save costs.
# sudo shutdown -h now