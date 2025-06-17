#!/usr/bin/env python3
"""
File:             memorize.py
Purpose:          Active memorization of important information
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             memorization, active-memory, storage
"""

from mcp.types import Tool
from datetime import datetime
from config import MEMORY_PATH

def memorize(content: str, tags: str = "") -> str:
    timestamp = datetime.now().isoformat()
    entry = f"[{timestamp}] {content}"
    if tags:
        entry += f" #{tags}"
    
    with open(MEMORY_PATH, "a", encoding="utf-8") as f:
        f.write(entry + "\n")
    
    return "Gespeichert."

memorize_tool = Tool(
    name="memory_memorize",
    description="Speichere Information aktiv",
    input_schema={"type": "object", "properties": {"content": {"type": "string"}, "tags": {"type": "string"}}, "required": ["content"]},
    fn=lambda arguments: memorize(arguments["content"], arguments.get("tags", ""))
)