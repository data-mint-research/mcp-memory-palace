from mcp.types import Tool
from pathlib import Path
from config import MEMORY_PATH
import random

def suggest_connections(topic: str = "") -> str:
    if not Path(MEMORY_PATH).exists():
        return "Keine Erinnerungen f?r Vorschl?ge vorhanden."
    
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        memories = [line.strip() for line in f if line.strip()]
    
    if not memories:
        return "Keine Erinnerungen vorhanden."
    
    if topic:
        relevant = [m for m in memories if topic.lower() in m.lower()]
        if relevant:
            memories = relevant
    
    suggestions = random.sample(memories, min(3, len(memories)))
    
    return "Vorschl?ge basierend auf Erinnerungen:\n" + "\n".join(f"- {s}" for s in suggestions)

suggest_tool = Tool(
    name="memory_suggest",
    description="[DEPRECATED] Schlage Verbindungen vor",
    input_schema={"type": "object", "properties": {"topic": {"type": "string"}}},
    fn=lambda arguments: suggest_connections(arguments.get("topic", ""))
)