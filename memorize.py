""" memorize.py ? Stores relevant memory entries as JSONL in brain.fs """

import os
import json
from datetime import datetime
from .config import get_config
from .utils import ensure_dir

def memorize(input_data: dict):
    config = get_config()
    path = config["memory_path"]
    ensure_dir(path)
    filename = os.path.join(path, "memory.jsonl")
    record = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": input_data
    }
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    return {"status": "memorized", "score": input_data.get("score", None)}
