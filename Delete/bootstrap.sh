#!/bin/bash
set -e

echo "MINT MCP Memory Palace - Linux/Mac Bootstrap"
echo "==========================================="

if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo "Error: Git is not installed"
    exit 1
fi

INSTALL_DIR="$HOME/mint-mcp"

if [ -d "$INSTALL_DIR" ]; then
    echo "Installation directory already exists: $INSTALL_DIR"
    read -p "Update existing installation? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
    cd "$INSTALL_DIR"
    git pull
else
    git clone https://github.com/data-mint-research/mint-mcp.git "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

python3 -m pip install -r requirements.txt

echo "Installation complete!"
echo "To start the server: cd $INSTALL_DIR && python3 main.py"