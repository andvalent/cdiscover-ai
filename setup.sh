#!/bin/bash
# This script is the final, verified version for automated deployment via Terraform.
# It incorporates all fixes discovered during our interactive debugging session.
set -e

# --- 1. System Updates and Core Dependencies ---
# Includes policycoreutils-python-utils, which provides the 'chcon' command for the SELinux fix.
sudo dnf update -y
sudo dnf install -y git python3.9 python3-pip policycoreutils-python-utils

# --- 2. Get the Application Code from Git ---
APP_DIR="/opt/rag-api"
# This URL will be populated by Terraform variables.
GIT_REPO_URL="https://${github_username}:${github_pat}@github.com/${github_username}/classical-rag-app-code.git"

# Ensure idempotency by removing the directory if it exists from a previous failed run.
sudo rm -rf $APP_DIR
# Clone the repository as root.
sudo git clone $GIT_REPO_URL $APP_DIR

# --- 3. Install Python Dependencies & Fix All Permissions ---
cd $APP_DIR
sudo pip3 install -r requirements.txt

# FIX #1: Standard Permissions. Change ownership from root to the user the service runs as.
sudo chown -R ec2-user:ec2-user $APP_DIR

# FIX #2: SELinux Permissions. Apply the correct security context to allow web service access.
# This fixes the systemd '200/CHDIR' error.
sudo chcon -t httpd_sys_content_t -R /opt/rag-api

# --- 4. Create and Configure the Systemd Service ---
# FIX #3: Gunicorn Path. Use the correct, static path to the executable.
# This fixes the systemd '203/EXEC' (command not found) error.
GUNICORN_PATH="/usr/local/bin/gunicorn"
NUM_WORKERS=$(($(nproc --all) * 2 + 1))

# Create the service file. The environment variables will be populated by Terraform.
sudo bash -c 'cat > /etc/systemd/system/rag-api.service' <<EOF
[Unit]
Description=Hyperion RAG API Server
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/opt/rag-api
Environment="S3_BUCKET_NAME=${s3_bucket_name}"
Environment="AWS_REGION=${aws_region}"
ExecStart=$GUNICORN_PATH --workers $NUM_WORKERS --bind 0.0.0.0:8080 --preload app:app
Restart=always
RestartSec=10
TimeoutStartSec=400

[Install]
WantedBy=multi-user.target
EOF

# --- 5. Start the Service ---
sudo systemctl daemon-reload
sudo systemctl enable rag-api.service
sudo systemctl start rag-api.service

echo "Hyperion RAG API setup complete and service started." >> /tmp/setup-finished.log