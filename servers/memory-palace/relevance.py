#!/usr/bin/env python3
"""
File:             relevance.py
Purpose:          Relevance assessment for passive observation
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             relevance, assessment, scoring
"""

import re

def assess_relevance(content: str) -> float:
    """Assess relevance of content for automatic storage."""
    score = 0.0
    
    # Keywords that increase relevance
    if any(word in content.lower() for word in ["wichtig", "merken", "erinnern", "important", "remember"]):
        score += 0.5
    
    # Structured data increases relevance
    if re.search(r'\d{4}-\d{2}-\d{2}|\b\d+\b|https?://', content):
        score += 0.3
    
    # Longer content is more relevant
    if len(content) > 100:
        score += 0.2
    
    return min(score, 1.0)