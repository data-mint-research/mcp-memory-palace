from mcp.types import Tool
from datetime import datetime
from pathlib import Path
from config import MEMORY_PATH
from relevance import assess_relevance

def observe(content: str) -> str:
    score = assess_relevance(content)
    if score > 0.3:
        timestamp = datetime.now().isoformat()
        with open(MEMORY_PATH, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {content}\n")
        return f"Beobachtet (Relevanz: {score:.1%})"
    return f"Beobachtet, aber nicht gespeichert (Relevanz: {score:.1%})"

observe_tool = Tool(
    name="memory_observe",
    description="Beobachte Information passiv",
    input_schema={"type": "object", "properties": {"content": {"type": "string"}}, "required": ["content"]},
    fn=lambda arguments: observe(arguments["content"])
)