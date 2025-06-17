#!/usr/bin/env python3
"""
File:             observe.py
Purpose:          Passive observation and relevance evaluation for memory storage
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, memory, observation, relevance
"""

import time
from typing import Dict, Any
from mcp import tool
from .memorize import memorize
from .relevance import is_relevant

@tool("memory_observe")
def observe(interaction: str) -> Dict[str, Any]:
    """
    Passively observe and optionally store if relevant.
    
    Args:
        interaction: The interaction or information to observe
        
    Returns:
        Observation result with timestamp and relevance evaluation
    """
    timestamp = str(int(time.time()))
    relevant = is_relevant(interaction)
    
    if relevant:
        memorize(timestamp, interaction)
        return {
            "timestamp": timestamp,
            "relevant": True,
            "status": "stored"
        }
    
    return {
        "timestamp": timestamp,
        "relevant": False,
        "status": "observed_only"
    }
