# Memory Palace

Advanced context-aware memory system for the MINT-MCP ecosystem.

## Overview

Memory Palace provides persistent, context-aware memory capabilities with:
- Passive observation with relevance evaluation
- Semantic recall with soft pattern matching
- Cortex threading for mental focus
- Adaptive plasticity for structure evolution
- Multi-language support (German/English)

## Installation

### Automatic (Recommended)
```powershell
# From MINT-MCP root
./run.ps1 -Server memory-palace
```

### Manual
```bash
cd servers/memory-palace
pip install -r requirements.txt
python main.py
```

## Configuration

### Environment Variables
- `MEMORY_PATH`: Path to brain.fs storage (default: `./brain.fs`)

### Configuration File
Edit `config.yaml` to customize:
- Storage location
- Relevance thresholds
- Cortex settings
- Logging levels

## Tools

### memory_observe
Passively observe interactions and store if relevant.
```json
{
  "tool": "memory_observe",
  "arguments": {
    "interaction": "Important meeting at 3pm"
  }
}
```

### memory_recall
Recall memories matching a pattern.
```json
{
  "tool": "memory_recall",
  "arguments": {
    "pattern": "meeting"
  }
}
```

### memory_focus
Set mental focus point for context.
```json
{
  "tool": "memory_focus",
  "arguments": {
    "thought": "project planning"
  }
}
```

### memory_thread
Create associative threads from focus.
```json
{
  "tool": "memory_thread",
  "arguments": {
    "connection": "deadline next week"
  }
}
```

### memory_plasticity
Create or modify brain structures.
```json
{
  "tool": "memory_plasticity",
  "arguments": {
    "region": "projects",
    "structure": {
      "mint-mcp": {
        "status": "active",
        "priority": "high"
      }
    }
  }
}
```

### memory_suggest
Get contextual suggestions from memories.
```json
{
  "tool": "memory_suggest",
  "arguments": {
    "context": "development"
  }
}
```

## Architecture

### Brain Structure
```json
{
  "long_term": {
    "timestamp": "memory content"
  },
  "cortex": {
    "focus": "current focus",
    "threads": ["focus -> connection"]
  },
  "custom_regions": {
    // Created via plasticity
  }
}
```

### File Storage
Memories are stored in JSON format in `brain.fs` with:
- Automatic persistence on every write
- Human-readable format for debugging
- Atomic writes to prevent corruption

## Docker Support

```bash
docker build -t mint-mcp/memory-palace .
docker run -d --name memory-palace \
  -v ./brain.fs:/app/brain.fs \
  mint-mcp/memory-palace
```

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Contributing
See main [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

## Support

- **Issues**: [GitHub Issues](https://github.com/data-mint-research/mint-mcp/issues)
- **Contact**: mint-research@neomint.com

## Legal

- **Author**: skr
- **Copyright**: NeoMINT GmbH 2025
- **License**: MIT
