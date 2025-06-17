#!/bin/bash
# bootstrap.sh ? One-line startup for MCP Memory Palace (Unix/macOS/Linux)

REPO="https://github.com/data-mint-research/mcp-memory-palace.git"
FOLDER="mcp-memory-palace"

if [ ! -d "$FOLDER" ]; then
    git clone "$REPO"
fi

cd "$FOLDER"
git pull origin main
docker build --no-cache -t memory-palace .
docker run -p 8080:8080 -v "${PWD}/brain.fs:/app/brain.fs" memory-palace