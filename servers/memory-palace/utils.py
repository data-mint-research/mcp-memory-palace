#!/usr/bin/env python3
"""
File:             utils.py
Purpose:          Shared utilities for memory operations
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, memory, utilities, helpers
"""

import os
import json
from typing import Dict, Any

MEMORY_PATH = os.getenv("MEMORY_PATH", "./brain.fs")

def load_brain() -> Dict[str, Any]:
    """
    Load brain state from persistent storage.
    
    Returns:
        Brain dictionary or empty dict if not exists
    """
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_brain(brain: Dict[str, Any]) -> None:
    """
    Save brain state to persistent storage.
    
    Args:
        brain: Brain dictionary to persist
    """
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    with open(MEMORY_PATH, 'w', encoding='utf-8') as f:
        json.dump(brain, f, indent=2, ensure_ascii=False)

def soft_match(pattern: str, text: str) -> bool:
    """
    Soft pattern matching (case-insensitive, partial).
    
    Args:
        pattern: Search pattern
        text: Text to search in
        
    Returns:
        True if pattern found in text
    """
    return pattern.lower() in text.lower()
