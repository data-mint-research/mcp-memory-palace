from mcp.types import Tool
from pathlib import Path
from config import MEMORY_PATH
from utils import soft_match

def recall(query: str, limit: int = 5) -> str:
    if not Path(MEMORY_PATH).exists():
        return "Keine Erinnerungen vorhanden."
    
    results = []
    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if soft_match(query, line):
                results.append(line.strip())
    
    results = results[-limit:]
    return "\n".join(results) if results else "Keine relevanten Erinnerungen gefunden."

recall_tool = Tool(
    name="memory_recall",
    description="Erinnere dich an Information",
    input_schema={"type": "object", "properties": {"query": {"type": "string"}, "limit": {"type": "integer"}}, "required": ["query"]},
    fn=lambda arguments: recall(arguments["query"], arguments.get("limit", 5))
)