""" recall.py ? Retrieves memory entries matching a topic keyword """

import os
import json
from .config import get_config

def recall(topic: str):
    config = get_config()
    path = os.path.join(config["memory_path"], "memory.jsonl")
    results = []

    if not os.path.exists(path):
        return {"status": "no memory found", "entries": []}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                record = json.loads(line)
                if topic.lower() in json.dumps(record).lower():
                    results.append(record)
            except Exception:
                continue

    return {"status": "ok", "topic": topic, "matches": results}
