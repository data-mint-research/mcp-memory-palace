#!/usr/bin/env python3
"""
File:             plasticity.py
Purpose:          Adaptive memory structure creation and evolution
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, memory, plasticity, adaptation, structure
"""

from typing import Dict, Any, List
from mcp import tool
from .utils import load_brain, save_brain

@tool("memory_plasticity")
def plasticity(region: str, structure: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create/modify brain structure (plasticity).
    
    Args:
        region: Brain region to modify
        structure: New structure to create or merge
        
    Returns:
        Plasticity result with region status
    """
    brain = load_brain()
    
    if region not in brain:
        brain[region] = {}
    
    # Deep merge structure into region
    for key, value in structure.items():
        if isinstance(value, dict) and key in brain[region] and isinstance(brain[region][key], dict):
            # Recursive merge for nested dicts
            brain[region][key].update(value)
        else:
            brain[region][key] = value
    
    save_brain(brain)
    
    return {
        "region": region,
        "status": "modified",
        "structure": brain[region]
    }
