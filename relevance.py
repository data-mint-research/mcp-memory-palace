""" relevance.py ? Assigns a basic relevance score to a text input """

def relevance_score(text: str) -> float:
    if not text:
        return 0.0
    length_factor = min(len(text) / 100, 1.0)
    keyword_boost = 0.2 if any(w in text.lower() for w in ["remember", "merken", "speichern"]) else 0.0
    return round(0.5 + length_factor * 0.3 + keyword_boost, 2)
