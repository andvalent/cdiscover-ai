#!/bin/bash
set -e

# --- 1. System Updates and Core Dependencies (using dnf for AL2023) ---
sudo dnf update -y
sudo dnf install -y git python3.9 python3-pip

# --- 2. Get the Application Code from Git ---
APP_DIR="/opt/rag-api"
GIT_REPO_URL="https://${github_username}:${github_pat}@github.com/${github_username}/classical-rag-app-code.git"

# Clone the repo (as root)
sudo git clone $GIT_REPO_URL $APP_DIR

# --- 3. Install Python Dependencies & Fix Permissions ---
cd $APP_DIR
sudo pip3 install -r requirements.txt

# This allows the service, running as ec2-user, to operate correctly.
sudo chown -R ec2-user:ec2-user $APP_DIR
# --- END OF FIX ---

# --- 4. Create and Configure the Systemd Service ---
GUNICORN_PATH=$(sudo /usr/bin/python3.9 -m pip show gunicorn | grep Location | awk '{print $2}')/gunicorn
NUM_WORKERS=$(($(nproc --all) * 2 + 1))

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