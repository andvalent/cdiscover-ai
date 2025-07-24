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
# This part remains the same, but the ExecStart path might change slightly.
# Let's verify the gunicorn path. It's safer to use the path discovered by the system.
GUNICORN_PATH=$(sudo /usr/bin/python3.9 -m pip show gunicorn | grep Location | awk '{print $2}')/gunicorn

sudo bash -c 'cat > /etc/systemd/system/rag-api.service' <<EOF
[Unit]
Description=Hyperion RAG API Server
After=network.target

[Service]
User=root # Run as root to bind to port 80, or use a reverse proxy like Nginx
Group=root
WorkingDirectory=/opt/rag-api
Environment="S3_BUCKET_NAME=${s3_bucket_name}"
Environment="AWS_REGION=${aws_region}"
ExecStart=$GUNICORN_PATH --workers 3 --bind 0.0.0.0:80 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# --- 5. Start the Service ---
sudo systemctl daemon-reload
sudo systemctl enable rag-api.service
sudo systemctl start rag-api.service

echo "Hyperion RAG API setup complete and service started." >> /tmp/setup-finished.log