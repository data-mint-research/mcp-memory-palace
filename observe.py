""" observe.py ? Evaluates input and optionally stores it based on relevance """

from relevance import relevance_score
from memorize import memorize
from config import get_config
from utils import write_audit_log

def observe(input_data: dict):
    text = input_data.get("text", "")
    score = relevance_score(text)
    config = get_config()

    write_audit_log("observe", {"text": text, "score": score})

    if score >= config["relevance_threshold"]:
        return memorize({"text": text, "score": score})
    else:
        return {
            "status": "ignored",
            "reason": "below relevance threshold",
            "score": score
        }
