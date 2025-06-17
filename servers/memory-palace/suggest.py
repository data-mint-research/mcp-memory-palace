#!/usr/bin/env python3
"""
File:             suggest.py
Purpose:          Suggestion engine for memory connections (deprecated)
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Deprecated
Tags:             suggestions, connections, deprecated
"""

# This module is deprecated and kept for backward compatibility
# Functionality has been integrated into recall.py and cortex.py

from mcp.types import Tool
from pathlib import Path
from config import MEMORY_PATH
import random

def suggest_connections(topic: str = "") -> str:
    """Legacy suggestion function - redirects to recall."""
    if not Path(MEMORY_PATH).exists():
        return "Keine Erinnerungen f?r Vorschl?ge vorhanden."
    
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        memories = [line.strip() for line in f if line.strip()]
    
    if not memories:
        return "Keine Erinnerungen vorhanden."
    
    # If topic provided, filter relevant memories
    if topic:
        relevant = [m for m in memories if topic.lower() in m.lower()]
        if relevant:
            memories = relevant
    
    # Select random memories for suggestions
    suggestions = random.sample(memories, min(3, len(memories)))
    
    return "Vorschl?ge basierend auf Erinnerungen:\n" + "\n".join(f"- {s}" for s in suggestions)

# Tool is not registered in main.py as it's deprecated
suggest_tool = Tool(
    name="memory_suggest",
    description="[DEPRECATED] Schlage Verbindungen vor",
    input_schema={"type": "object", "properties": {"topic": {"type": "string"}}},
    fn=lambda arguments: suggest_connections(arguments.get("topic", ""))
)