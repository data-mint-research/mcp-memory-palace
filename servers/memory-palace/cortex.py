#!/usr/bin/env python3
"""
File:             cortex.py
Purpose:          Cortex threading for mental focus and context
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, memory, focus, context, threading
"""

from typing import Dict, Any, List
from mcp import tool
from .utils import load_brain, save_brain

@tool("memory_focus")
def focus(thought: str) -> Dict[str, Any]:
    """
    Set mental focus point for context threading.
    
    Args:
        thought: The thought or concept to focus on
        
    Returns:
        Focus confirmation with context
    """
    brain = load_brain()
    if "cortex" not in brain:
        brain["cortex"] = {}
    
    brain["cortex"]["focus"] = thought
    save_brain(brain)
    
    return {
        "focus": thought,
        "status": "focused",
        "context": brain["cortex"].get("threads", [])
    }

@tool("memory_thread")
def thread(connection: str) -> Dict[str, Any]:
    """
    Create associative thread from current focus.
    
    Args:
        connection: Related thought or concept to thread
        
    Returns:
        Threading result with updated context
    """
    brain = load_brain()
    if "cortex" not in brain:
        brain["cortex"] = {"threads": []}
    if "threads" not in brain["cortex"]:
        brain["cortex"]["threads"] = []
    
    focus_point = brain["cortex"].get("focus", "undefined")
    thread_entry = f"{focus_point} -> {connection}"
    
    brain["cortex"]["threads"].append(thread_entry)
    save_brain(brain)
    
    return {
        "focus": focus_point,
        "connection": connection,
        "thread": thread_entry,
        "total_threads": len(brain["cortex"]["threads"])
    }
