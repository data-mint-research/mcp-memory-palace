#!/usr/bin/env python3
"""
File:             suggest.py
Purpose:          Memory-based suggestion engine
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, memory, suggestions, associations
"""

import random
from typing import Dict, Any, List
from mcp import tool
from .utils import load_brain

@tool("memory_suggest")
def suggest(context: str = "") -> Dict[str, Any]:
    """
    Suggest related memories based on context.
    
    Args:
        context: Optional context for suggestions
        
    Returns:
        Suggested memories and associations
    """
    brain = load_brain()
    suggestions = []
    
    # Get memories
    memories = brain.get("long_term", {})
    memory_list = list(memories.items())
    
    if not memory_list:
        return {
            "context": context,
            "suggestions": [],
            "message": "No memories to suggest from"
        }
    
    # Get current focus if available
    focus = brain.get("cortex", {}).get("focus", "")
    
    # If context provided, find related memories
    if context:
        for timestamp, memory in memory_list:
            if context.lower() in memory.lower():
                suggestions.append({
                    "timestamp": timestamp,
                    "memory": memory,
                    "relevance": "contextual"
                })
    
    # Add focus-related suggestions
    if focus and focus != context:
        for timestamp, memory in memory_list:
            if focus.lower() in memory.lower():
                suggestions.append({
                    "timestamp": timestamp,
                    "memory": memory,
                    "relevance": "focus-related"
                })
    
    # Add random suggestions if we have few
    if len(suggestions) < 3 and len(memory_list) > 0:
        random_memories = random.sample(memory_list, min(3, len(memory_list)))
        for timestamp, memory in random_memories:
            if not any(s["timestamp"] == timestamp for s in suggestions):
                suggestions.append({
                    "timestamp": timestamp,
                    "memory": memory,
                    "relevance": "random"
                })
    
    return {
        "context": context,
        "focus": focus,
        "suggestions": suggestions[:5]  # Limit to 5 suggestions
    }
