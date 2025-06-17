import os
from pathlib import Path

MEMORY_PATH = os.getenv("MEMORY_PATH", str(Path.home() / ".mint-mcp" / "memory-palace" / "brain.fs"))
Path(MEMORY_PATH).parent.mkdir(parents=True, exist_ok=True)