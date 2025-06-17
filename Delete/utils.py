import re
from difflib import SequenceMatcher

def soft_match(query: str, text: str, threshold: float = 0.3) -> bool:
    query_lower = query.lower()
    text_lower = text.lower()
    
    if query_lower in text_lower:
        return True
    
    query_words = set(query_lower.split())
    text_words = set(text_lower.split())
    
    if query_words.intersection(text_words):
        return True
    
    similarity = SequenceMatcher(None, query_lower, text_lower).ratio()
    return similarity > threshold