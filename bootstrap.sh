#!/bin/bash
# bootstrap.sh ? One-line startup for MCP Memory Palace (Unix/macOS/Linux)

REPO="https://github.com/data-mint-research/mcp-memory-palace.git"
FOLDER="mcp-memory-palace"

if [ ! -d "$FOLDER" ]; then
    echo "[INFO] Cloning repository..."
    git clone "$REPO"
else
    echo "[INFO] Repository exists, pulling latest changes..."
    cd "$FOLDER"
    git pull origin main
    cd ..
fi

cd "$FOLDER"

echo "[INFO] Building Docker image (no cache)..."
docker build --no-cache -t memory-palace .

echo "[INFO] Starting container on port 8080..."
docker run -p 8080:8080 -v "${PWD}/brain.fs:/app/brain.fs" memory-palace