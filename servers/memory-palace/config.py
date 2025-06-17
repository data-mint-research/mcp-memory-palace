#!/usr/bin/env python3
"""
File:             config.py
Purpose:          Configuration settings for Memory Palace server
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             config, settings, memory-palace
"""

import os
from pathlib import Path

# Memory storage path
MEMORY_PATH = os.getenv("MEMORY_PATH", str(Path.home() / ".mint-mcp" / "memory-palace" / "brain.fs"))

# Ensure the directory exists
Path(MEMORY_PATH).parent.mkdir(parents=True, exist_ok=True)