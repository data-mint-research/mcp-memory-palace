""" suggest.py ? Suggests memory entries based on soft triggers or semantic cues """

import os
import json
from datetime import datetime
from config import get_config
from utils import write_audit_log

def suggest(trigger: str):
    """
    Returns recent or thematically related memory entries
    that contain the given trigger word or its semantic neighbors.
    """
    config = get_config()
    memory_path = os.path.join(config["memory_path"], "memory.jsonl")
    suggestions = []

    if not os.path.exists(memory_path):
        return {"status": "no memory available", "suggestions": []}

    with open(memory_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
                content = json.dumps(entry).lower()
                if trigger.lower() in content:
                    suggestions.append(entry)
            except Exception:
                continue

    write_audit_log("suggest", {"trigger": trigger, "count": len(suggestions)})
    return {
        "status": "ok",
        "trigger": trigger,
        "suggestions": suggestions[:5]  # return top 5 only
    }
