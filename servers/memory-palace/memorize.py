#!/usr/bin/env python3
"""
File:             memorize.py
Purpose:          Core memory storage with audit trail
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, memory, storage, persistence
"""

import os
import json
from typing import Any, Dict
from .utils import load_brain, save_brain

def memorize(timestamp: str, interaction: str) -> None:
    """
    Store interaction in long-term memory.
    
    Args:
        timestamp: Unix timestamp as string
        interaction: Content to memorize
    """
    brain = load_brain()
    
    if "long_term" not in brain:
        brain["long_term"] = {}
    
    brain["long_term"][timestamp] = interaction
    save_brain(brain)
