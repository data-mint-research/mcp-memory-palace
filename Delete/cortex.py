from mcp.types import Tool
from datetime import datetime
from pathlib import Path
import json

CORTEX_PATH = Path.home() / ".mint-mcp" / "memory-palace" / "cortex.json"
CORTEX_PATH.parent.mkdir(parents=True, exist_ok=True)

def cortex_thread(action: str, thread_name: str = "", content: str = "") -> str:
    threads = {}
    if CORTEX_PATH.exists():
        threads = json.loads(CORTEX_PATH.read_text())
    
    if action == "create":
        threads[thread_name] = {"created": datetime.now().isoformat(), "focus": content}
        CORTEX_PATH.write_text(json.dumps(threads, indent=2))
        return f"Thread '{thread_name}' erstellt."
    
    elif action == "list":
        if not threads:
            return "Keine aktiven Threads."
        return "\n".join([f"- {name}: {data['focus']}" for name, data in threads.items()])
    
    elif action == "focus":
        if thread_name in threads:
            return f"Fokus auf '{thread_name}': {threads[thread_name]['focus']}"
        return f"Thread '{thread_name}' nicht gefunden."
    
    return "Unbekannte Aktion."

cortex_thread_tool = Tool(
    name="memory_thread",
    description="Verwalte mentale Fokus-Threads",
    input_schema={"type": "object", "properties": {"action": {"type": "string"}, "thread_name": {"type": "string"}, "content": {"type": "string"}}, "required": ["action"]},
    fn=lambda arguments: cortex_thread(arguments["action"], arguments.get("thread_name", ""), arguments.get("content", ""))
)