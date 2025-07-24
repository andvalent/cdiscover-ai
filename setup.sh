#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

# --- 1. System Updates and Core Dependencies ---
sudo yum update -y
sudo yum install -y git
sudo amazon-linux-extras install python3.8 -y 
sudo yum install -y python3-pip

# --- 2. Get the Application Code from Git ---
APP_DIR="/opt/rag-api"
GIT_REPO_URL="git@github.com:andvalent/classical-rag-app-code.git"

# --- REMOVED THE FLAWED ssh-keyscan LINE ---

# --- THIS IS THE CORRECTED AND DEFINITIVE COMMAND ---
# It tells Git to use an SSH command that disables the host key prompt for this one operation.
sudo GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no" git clone $GIT_REPO_URL $APP_DIR

# --- 3. Install Python Dependencies ---
cd $APP_DIR
sudo pip3 install -r requirements.txt

# --- 4. Create and Configure the Systemd Service ---
# This part is correct and remains unchanged.
sudo bash -c 'cat > /etc/systemd/system/rag-api.service' <<EOF
[Unit]
Description=Hyperion RAG API Server
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/opt/rag-api
# Pass environment variables to the application
# IMPORTANT: Remember to replace these placeholders with your actual values!
Environment="S3_BUCKET_NAME=<YOUR_S3_BUCKET_NAME>"
Environment="AWS_REGION=<YOUR_AWS_REGION>"
# The command to start the Gunicorn server
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind 0.0.0.0:80 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# --- 5. Start the Service ---
sudo systemctl daemon-reload
sudo systemctl enable rag-api.service
sudo systemctl start rag-api.service

echo "Hyperion RAG API setup complete and service started."