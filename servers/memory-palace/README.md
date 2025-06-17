# Memory Palace Server

Advanced context-aware memory system for MINT-MCP.

## Overview

Memory Palace implements a sophisticated long-term memory system with:
- Passive observation with relevance scoring
- Active memorization with tagging
- Semantic recall with soft pattern matching
- Mental focus threads (Cortex)
- Adaptive plasticity for structure creation

## Installation

### Quick Start
```bash
cd mint-mcp
./run.ps1 -Server memory-palace
```

### Manual Installation
```bash
cd servers/memory-palace
pip install -r requirements.txt
python main.py
```

## Configuration

### Environment Variables
- `MEMORY_PATH`: Path to memory storage (default: `~/.mint-mcp/memory-palace/brain.fs`)

### Client Configuration

#### Claude Desktop
```json
{
  "mcpServers": {
    "mint-memory-palace": {
      "command": "python",
      "args": ["C:/path/to/mint-mcp/servers/memory-palace/main.py"],
      "env": {
        "MEMORY_PATH": "C:/path/to/mint-mcp/servers/memory-palace/brain.fs"
      }
    }
  }
}
```

## Tools

### memory_observe
Passively observe information with automatic relevance assessment.
```json
{
  "content": "Information to observe"
}
```

### memory_memorize
Actively store important information with optional tags.
```json
{
  "content": "Important information",
  "tags": "project,meeting"
}
```

### memory_recall
Retrieve memories using semantic search.
```json
{
  "query": "search terms",
  "limit": 5
}
```

### memory_focus
Manage mental focus threads for context.
```json
{
  "action": "create|list|focus",
  "thread_name": "project-x",
  "content": "Focus description"
}
```

### memory_plasticity
Create adaptive structures for organizing knowledge.
```json
{
  "structure_type": "concept",
  "name": "architecture",
  "definition": "System design patterns"
}
```

## Architecture

### File-Based Storage
- Simple, portable memory storage
- Append-only for audit trails
- UTF-8 encoded for international support

### Relevance Engine
- Automatic scoring for passive observations
- Keyword detection
- Structure recognition
- Length-based importance

### Soft Pattern Matching
- Substring matching
- Word-based matching
- Fuzzy string similarity
- Configurable thresholds

## Development

### File Structure
```
memory-palace/
??? main.py           # Server entry point
??? config.py         # Configuration
??? observe.py        # Passive observation
??? memorize.py       # Active memorization
??? recall.py         # Memory retrieval
??? cortex.py         # Focus threads
??? plasticity.py     # Adaptive structures
??? relevance.py      # Scoring engine
??? utils.py          # Common utilities
??? suggest.py        # Deprecated
```

### Testing
```bash
python -m pytest tests/
```

## Support

- **Documentation**: [docs/servers/memory-palace.md](../../docs/servers/memory-palace.md)
- **Issues**: [GitHub Issues](https://github.com/data-mint-research/mint-mcp/issues)
- **Contact**: mint-research@neomint.com

## Legal

- **Author**: skr
- **Copyright**: NeoMINT GmbH 2025
- **License**: MIT