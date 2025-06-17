# ==============================================================================
# File:             Dockerfile
# Purpose:          Docker container for Memory Palace MCP server
# Author:           skr
# Owner:            MINT-RESEARCH / NeoMINT GmbH
# Contact:          mint-research@neomint.com
# License:          MIT / ? NeoMINT GmbH 2025
# Created:          2025-06-17
# Last Modified:    2025-06-17 by skr
# Status:           Stable
# Tags:             docker, container, memory-palace
# ==============================================================================

FROM python:3.11-slim

LABEL maintainer="mint-research@neomint.com"
LABEL org.opencontainers.image.source="https://github.com/data-mint-research/mint-mcp"
LABEL org.opencontainers.image.description="MINT-MCP Memory Palace Server"
LABEL org.opencontainers.image.licenses="MIT"

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy server files
COPY . .

# Create memory directory
RUN mkdir -p /data

# Environment
ENV MEMORY_PATH=/data/brain.fs
ENV PYTHONUNBUFFERED=1

# Run server
CMD ["python", "main.py"]