#!/bin/bash
# Update the instance and install our dependencies
sudo yum update -y
sudo yum install -y git python3-pip

# Install the required Python packages globally so all users can access them
sudo pip3 install boto3 langchain langchain_aws pyarrow pandas

# Clone your GitHub repository
# !!! IMPORTANT: Replace this URL with your actual GitHub repository URL !!!
git clone https://github.com/kauber/cdiscover-ai.git /home/ec2-user/app

# Set the AWS region configuration for all users, including root
mkdir -p /home/ec2-user/.aws
echo -e "[default]\nregion = eu-central-1" > /home/ec2-user/.aws/config
# Also set it for the root user running this script
mkdir -p /root/.aws
echo -e "[default]\nregion = eu-central-1" > /root/.aws/config
# Change ownership of the ec2-user's config directory
chown -R ec2-user:ec2-user /home/ec2-user/.aws


# Change into the application directory
# cd /home/ec2-user/app/vectorizer-python-code

# Run the vectorization script. The script is run as the root user.
# The "${bucket_name}" variable is injected by Terraform's templatefile function.
# S3_BUCKET_NAME="${bucket_name}" python3 vectorize_text.py

# When the script is finished, automatically shut down the instance to save costs.
# sudo shutdown -h now

