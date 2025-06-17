# ==============================================================================
# File:             Dockerfile
# Purpose:          Docker image for MINT Memory Palace server
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

# Metadata
LABEL maintainer="mint-research@neomint.com"
LABEL description="MINT-MCP Memory Palace Server"
LABEL version="2.0.0"

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create brain storage directory
RUN mkdir -p /app/brain.fs

# Environment variables
ENV MEMORY_PATH=/app/brain.fs/brain.json
ENV PYTHONUNBUFFERED=1

# Run as non-root user
RUN useradd -m -u 1000 memorypalace && \
    chown -R memorypalace:memorypalace /app
USER memorypalace

# Start server
CMD ["python", "main.py"]
