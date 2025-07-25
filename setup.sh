#!/bin/bash
set -e

# --- 1. System Updates and Core Dependencies (using dnf for AL2023) ---
sudo dnf update -y
sudo dnf install -y git python3.9 python3-pip  # Much simpler!

# --- 2. Get the Application Code from Git ---
APP_DIR="/opt/rag-api"
GIT_REPO_URL="https://${github_username}:${github_pat}@github.com/${github_username}/classical-rag-app-code.git"

# Clone the repo
sudo git clone $GIT_REPO_URL $APP_DIR

# --- 3. Install Python Dependencies ---
cd $APP_DIR
# The default python3 and pip3 will now be 3.9
sudo pip3 install -r requirements.txt

# --- 4. Create and Configure the Systemd Service ---
# This version includes the critical --preload flag and binds to port 8080.
GUNICORN_PATH=$(sudo /usr/bin/python3.9 -m pip show gunicorn | grep Location | awk '{print $2}')/gunicorn

# Dynamically calculate the number of workers based on CPU cores for better performance
NUM_WORKERS=$(($(nproc --all) * 2 + 1))

sudo bash -c 'cat > /etc/systemd/system/rag-api.service' <<EOF
[Unit]
Description=Hyperion RAG API Server
After=network.target

[Service]
# Run as a non-privileged user since we are not binding to a privileged port (< 1024)
User=ec2-user
Group=ec2-user
WorkingDirectory=/opt/rag-api
# Pass environment variables from Terraform to the application
Environment="S3_BUCKET_NAME=${s3_bucket_name}"
Environment="AWS_REGION=${aws_region}"
# CRITICAL: Added --preload to load data only once in the master process.
# CRITICAL: Changed bind port to 8080 to match security group.
# DYNAMIC: Use calculated number of workers.
ExecStart=$GUNICORN_PATH --workers $NUM_WORKERS --bind 0.0.0.0:8080 --preload app:app
Restart=always
# Add a timeout to allow for the initial data loading on slow starts
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