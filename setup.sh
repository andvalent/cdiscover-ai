#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

# --- 1. System Updates and Core Dependencies ---
sudo yum update -y
sudo yum install -y git
sudo amazon-linux-extras install python3.8 -y # Using 3.8 as it's stable and well-supported on AL2
sudo yum install -y python3-pip

# --- 2. Get the Application Code from Git ---
# IMPORTANT: Replace this with the URL to YOUR private Git repository.
# You will need to add the EC2 instance's SSH key to your repository's deploy keys.
APP_DIR="/opt/rag-api"
GIT_REPO_URL="git@github.com:andvalent/classical-rag-app-code.git"
sudo git clone $GIT_REPO_URL $APP_DIR

# --- 3. Install Python Dependencies ---
cd $APP_DIR
sudo pip3 install -r requirements.txt

# --- 4. Create and Configure the Systemd Service ---
# This will run our app with Gunicorn and keep it running.
# It also passes the environment variables to the app.
sudo bash -c 'cat > /etc/systemd/system/rag-api.service' <<EOF
[Unit]
Description=Hyperion RAG API Server
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/opt/rag-api
# Pass environment variables to the application
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