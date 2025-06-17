#!/usr/bin/env python3
"""
File:             utils.py
Purpose:          Utility functions for Memory Palace server
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             utilities, helpers, common-functions
"""

import re
from difflib import SequenceMatcher

def soft_match(query: str, text: str, threshold: float = 0.3) -> bool:
    """Perform soft pattern matching with fuzzy search."""
    query_lower = query.lower()
    text_lower = text.lower()
    
    # Direct substring match
    if query_lower in text_lower:
        return True
    
    # Word-based matching
    query_words = set(query_lower.split())
    text_words = set(text_lower.split())
    
    if query_words.intersection(text_words):
        return True
    
    # Fuzzy matching
    similarity = SequenceMatcher(None, query_lower, text_lower).ratio()
    return similarity > threshold