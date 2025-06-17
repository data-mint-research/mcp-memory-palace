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
import argparse
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server

from config import MEMORY_PATH
from observe import observe_tool
from memorize import memorize_tool
from recall import recall_tool
from cortex import cortex_thread_tool
from plasticity import plasticity_tool

MEMORY_FILE = Path(MEMORY_PATH)
MEMORY_FILE.parent.mkdir(exist_ok=True)

server = Server("mint-memory-palace")

server.add_tool(observe_tool)
server.add_tool(memorize_tool)
server.add_tool(recall_tool)
server.add_tool(cortex_thread_tool)
server.add_tool(plasticity_tool)

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream)

if __name__ == "__main__":
    asyncio.run(main())