#!/usr/bin/env python3
"""
File:             recall.py
Purpose:          Memory recall with soft pattern matching
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, memory, recall, search
"""

import os
from typing import List, Dict, Any
from mcp import tool
from .utils import load_brain, soft_match

@tool("memory_recall")
def recall(pattern: str) -> Dict[str, Any]:
    """
    Recall memories matching pattern (soft matching).
    
    Args:
        pattern: Search pattern (case-insensitive, partial match)
        
    Returns:
        Matching memories organized by relevance
    """
    brain = load_brain()
    memories = []
    
    if "long_term" in brain:
        for timestamp, memory in brain["long_term"].items():
            if soft_match(pattern, memory):
                memories.append({
                    "timestamp": timestamp,
                    "content": memory
                })
    
    # Sort by timestamp (newest first)
    memories.sort(key=lambda x: x["timestamp"], reverse=True)
    
    return {
        "pattern": pattern,
        "matches": len(memories),
        "memories": memories
    }
