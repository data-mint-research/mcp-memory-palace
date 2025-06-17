""" cortex.py ? Maintains current focus, mental threads and context continuity """

import json
import os
from datetime import datetime
from .utils import ensure_dir, write_audit_log
from .config import get_config

STATE_PATH = "brain.fs/state.json"

def get_current_state() -> dict:
    """ Load the current mental state from flatfile """
    if not os.path.exists(STATE_PATH):
        return {"focus": None, "threads": [], "last_updated": None}

    with open(STATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def update_focus(topic: str):
    """ Set a new topic as current focus """
    state = get_current_state()
    state["focus"] = topic
    state["last_updated"] = datetime.utcnow().isoformat()
    write_audit_log("cortex", {"action": "focus_changed", "to": topic})
    _save_state(state)
    return {"status": "focus updated", "focus": topic}

def add_thread(note: str):
    """ Append a mental thread (temporary thought) """
    state = get_current_state()
    state.setdefault("threads", []).append({
        "note": note,
        "timestamp": datetime.utcnow().isoformat()
    })
    write_audit_log("cortex", {"action": "thread_added", "note": note})
    _save_state(state)
    return {"status": "thread added"}

def _save_state(state: dict):
    ensure_dir(os.path.dirname(STATE_PATH))
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
