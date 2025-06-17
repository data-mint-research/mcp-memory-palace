#!/usr/bin/env python3
"""
File:             relevance.py
Purpose:          Relevance evaluation for memory storage decisions
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             mcp, memory, relevance, evaluation
"""

def is_relevant(interaction: str) -> bool:
    """
    Determine if interaction is worth memorizing.
    
    Current implementation: Simple heuristic based on content.
    Future: Could use ML or more sophisticated analysis.
    
    Args:
        interaction: Content to evaluate
        
    Returns:
        True if relevant enough to store
    """
    # Simple heuristic: store if not too short
    return len(interaction) > 10
