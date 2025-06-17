import re

def assess_relevance(content: str) -> float:
    score = 0.0
    
    if any(word in content.lower() for word in ["wichtig", "merken", "erinnern", "important", "remember"]):
        score += 0.5
    
    if re.search(r'\d{4}-\d{2}-\d{2}|\b\d+\b|https?://', content):
        score += 0.3
    
    if len(content) > 100:
        score += 0.2
    
    return min(score, 1.0)