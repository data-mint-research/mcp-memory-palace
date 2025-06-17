#!/usr/bin/env python3
"""
File:             main.py
Purpose:          MINT-MCP Memory Palace server entry point
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, server, memory, entry-point
"""

import asyncio
import os
import sys
import logging

from mcp import Server

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

INSTRUCTIONS = """memory palace: minimalistic declarative memory"""

# Ensure imports from same directory work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from observe import observe
from recall import recall
from cortex import focus, thread
from plasticity import plasticity

# Initialize MCP server
app = Server("memory-palace")

# Register tools
app.add_tool(observe)
app.add_tool(recall)
app.add_tool(focus)
app.add_tool(thread)
app.add_tool(plasticity)

async def run():
    """Start the MCP server"""
    from mcp.server.stdio import stdio_server
    
    logger.info(f"Starting MINT Memory Palace server...")
    logger.info(f"Version: 2.0.0")
    logger.info(f"Storage: {os.getenv('MEMORY_PATH', './brain.fs')}")
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(run())
