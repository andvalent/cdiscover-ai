#!/bin/bash
set -e

# --- 1. System Updates and Core Dependencies ---
sudo yum update -y
sudo yum install -y git
sudo amazon-linux-extras enable python3.8 -y
sudo yum clean metadata
sudo yum install -y python3.8 python3-pip

# --- 2. Get the Application Code from Git ---
APP_DIR="/opt/rag-api"
GIT_REPO_URL="https://andvalent:${github_pat}@github.com/andvalent/classical-rag-app-code.git"

# Clone the repo
sudo git clone $GIT_REPO_URL $APP_DIR

# --- 3. Install Python Dependencies ---
cd $APP_DIR
sudo pip3 install -r requirements.txt

# --- 4. Create and Configure the Systemd Service ---
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
