#!/bin/bash
#
# This script is designed to be fully automated and robust.
# It will:
# 1. Set up a log file to record its entire execution.
# 2. Exit immediately if any command fails.
# 3. Install all necessary system and Python dependencies.
# 4. Clone the application code from GitHub.
# 5. Correctly set file ownership for easier manual debugging if ever needed.
# 6. Configure the AWS environment for the script.
# 7. Run the Python vectorization script.
# 8. Automatically shut down the instance upon successful completion to save costs.
#

# --- 1. Robustness and Logging Setup ---
# The 'set -e' command ensures that the script will exit immediately if any command fails.
set -e

# Redirect all output (both stdout and stderr) from this script to a log file.
# This creates a "black box recorder" so you can debug what happened if the instance fails.
# You can view this log by SSH-ing into the instance and running: cat /var/log/user-data.log
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1

echo "--- Starting EC2 user data script execution ---"


# --- 2. Install Dependencies ---
echo "Updating system and installing dependencies..."
yum update -y
yum install -y git python3-pip

# Install the required Python packages globally.
# This is run as the root user, so all users can access them.
pip3 install boto3 langchain langchain_aws pyarrow pandas s3fs


# --- 3. Clone Application and Set Permissions ---
echo "Cloning the application repository from GitHub..."
# We clone into a sub-directory of the ec2-user's home.
git clone https://github.com/kauber/cdiscover-ai.git /home/ec2-user/app

echo "Setting correct ownership for the cloned repository..."
# The user_data script runs as root, so we must change the ownership of the
# cloned directory to the 'ec2-user'. This makes manual debugging via SSH possible.
chown -R ec2-user:ec2-user /home/ec2-user/app


# --- 4. Configure AWS Environment ---
echo "Configuring AWS region for the root user..."
# The script itself runs as the root user, so we configure the AWS region for root.
mkdir -p /root/.aws
echo -e "[default]\nregion = eu-central-1" > /root/.aws/config


# --- 5. Run the Main Application ---
echo "Changing to the script directory..."
cd /home/ec2-user/app/vectorizer-python-code

echo "Starting the Python vectorization script..."
# Export the S3 bucket name as an environment variable so the Python script can access it.
# The "${bucket_name}" is the variable passed in from your Terraform main.tf file.
export S3_BUCKET_NAME="${bucket_name}"

# Run the Python script. If this script fails, the 'set -e' at the top
# will cause this entire user_data script to stop immediately.
python3 vectorize_text.py


# --- 6. Automated Shutdown ---
echo "--- Python script completed successfully. Shutting down the instance to save costs. ---"
# This command will only be reached if the python3 script above exits with a success code (0).
shutdown -h now