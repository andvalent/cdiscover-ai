#!/bin/bash
yum update -y
yum install -y git python3-pip

# Set the S3 bucket name environment variable
export S3_BUCKET_NAME="${bucket_name}"
echo 'export S3_BUCKET_NAME="${bucket_name}"' >> /home/ec2-user/.bash_profile

# Switch to the ec2-user's home directory
cd /home/ec2-user

# Clone the repository AS the ec2-user
sudo -u ec2-user git clone https://github.com/kauber/cdiscover-ai.git
cd cdiscover-ai/python-scraper-code

# Install Python dependencies
pip3 install -r requirements.txt

# Run the entire scraping process automatically, in the background.
# The 'nohup' command ensures it keeps running even if you disconnect.
# The '&' runs it in the background.
# Output is logged to a file for debugging.
nohup sudo -u ec2-user python3 hyperion_scraper.py > /home/ec2-user/scraper.log 2>&1 &