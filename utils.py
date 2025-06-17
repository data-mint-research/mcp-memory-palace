""" utils.py ? Utility functions for path handling and audit logging """

import os
import json
from datetime import datetime

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def write_audit_log(area: str, payload: dict):
    log_path = f"brain.fs/audit/{area}.log.jsonl"
    ensure_dir(os.path.dirname(log_path))
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": payload
    }
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
