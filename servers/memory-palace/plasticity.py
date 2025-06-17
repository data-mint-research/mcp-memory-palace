#!/usr/bin/env python3
"""
File:             plasticity.py
Purpose:          Adaptive plasticity for structure creation and growth
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          2025-06-17
Last Modified:    2025-06-17 by skr
Status:           Stable
Tags:             plasticity, adaptation, structure, learning
"""

from mcp.types import Tool
from pathlib import Path
import json

STRUCTURE_PATH = Path.home() / ".mint-mcp" / "memory-palace" / "structures.json"
STRUCTURE_PATH.parent.mkdir(parents=True, exist_ok=True)

def plasticity(structure_type: str, name: str, definition: str = "") -> str:
    structures = {}
    if STRUCTURE_PATH.exists():
        structures = json.loads(STRUCTURE_PATH.read_text())
    
    if structure_type not in structures:
        structures[structure_type] = {}
    
    if definition:
        structures[structure_type][name] = definition
        STRUCTURE_PATH.write_text(json.dumps(structures, indent=2))
        return f"Struktur '{name}' vom Typ '{structure_type}' angelegt."
    else:
        if name in structures.get(structure_type, {}):
            return f"{name}: {structures[structure_type][name]}"
        return f"Struktur '{name}' nicht gefunden."

plasticity_tool = Tool(
    name="memory_plasticity",
    description="Erstelle adaptive Strukturen",
    input_schema={"type": "object", "properties": {"structure_type": {"type": "string"}, "name": {"type": "string"}, "definition": {"type": "string"}}, "required": ["structure_type", "name"]},
    fn=lambda arguments: plasticity(arguments["structure_type"], arguments["name"], arguments.get("definition", ""))
)