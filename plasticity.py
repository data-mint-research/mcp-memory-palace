""" plasticity.py ? Creates new structure types based on usage patterns """

import os
import json
from datetime import datetime
from config import get_config
from utils import write_audit_log, ensure_dir

def trigger_plasticity(reason: str, structure_hint: str = "topic-cluster") -> dict:
    """
    Triggers a plastic restructuring event when content volume or failure rate
    suggests that the current memory form is insufficient.
    """
    config = get_config()
    target_dir = os.path.join(config["memory_path"], "../index/", structure_hint)
    ensure_dir(target_dir)

    structure_file = os.path.join(target_dir, f"{datetime.utcnow().isoformat()}.json")
    placeholder_structure = {
        "triggered_at": datetime.utcnow().isoformat(),
        "reason": reason,
        "structure_type": structure_hint,
        "status": "created",
        "notes": "Placeholder structure for future cluster or linkage logic"
    }

    with open(structure_file, "w", encoding="utf-8") as f:
        json.dump(placeholder_structure, f, indent=2)

    write_audit_log("plasticity", placeholder_structure)
    return {"status": "plasticity event", "created": structure_file}
