# Memory Palace Server Documentation

## Overview

Memory Palace is an advanced context-aware memory system that provides long-term memory capabilities for AI assistants. It implements passive observation, active memorization, semantic recall, and adaptive learning structures.

## Features

### Core Capabilities

1. **Passive Observation**
   - Automatic relevance assessment
   - Selective storage based on importance
   - Background learning from interactions

2. **Active Memorization**
   - Explicit storage commands
   - Tag-based organization
   - Timestamp tracking

3. **Semantic Recall**
   - Soft pattern matching
   - Fuzzy search capabilities
   - Context-aware retrieval

4. **Mental Focus (Cortex)**
   - Thread-based context management
   - Topic tracking
   - Conversation continuity

5. **Adaptive Plasticity**
   - Dynamic structure creation
   - Knowledge organization
   - Concept mapping

## Tool Reference

### memory_observe

Passively observe information with automatic relevance assessment.

**Parameters:**
- `content` (string, required): Information to observe

**Returns:** Observation status with relevance score

**Example:**
```json
{
  "tool": "memory_observe",
  "arguments": {
    "content": "The user prefers Python for data analysis"
  }
}
```

### memory_memorize

Actively store important information with optional tags.

**Parameters:**
- `content` (string, required): Information to memorize
- `tags` (string, optional): Comma-separated tags

**Returns:** Confirmation message

**Example:**
```json
{
  "tool": "memory_memorize",
  "arguments": {
    "content": "Project deadline is March 15, 2025",
    "tags": "project,deadline,important"
  }
}
```

### memory_recall

Retrieve memories using semantic search.

**Parameters:**
- `query` (string, required): Search query
- `limit` (integer, optional): Maximum results (default: 5)

**Returns:** Matching memories

**Example:**
```json
{
  "tool": "memory_recall",
  "arguments": {
    "query": "project deadline",
    "limit": 3
  }
}
```

### memory_focus

Manage mental focus threads for context.

**Parameters:**
- `action` (string, required): "create", "list", or "focus"
- `thread_name` (string, optional): Thread identifier
- `content` (string, optional): Thread description

**Returns:** Thread operation result

**Example:**
```json
{
  "tool": "memory_focus",
  "arguments": {
    "action": "create",
    "thread_name": "python-project",
    "content": "Working on Python data analysis project"
  }
}
```

### memory_plasticity

Create adaptive structures for organizing knowledge.

**Parameters:**
- `structure_type` (string, required): Type of structure
- `name` (string, required): Structure name
- `definition` (string, optional): Structure definition

**Returns:** Structure operation result

**Example:**
```json
{
  "tool": "memory_plasticity",
  "arguments": {
    "structure_type": "concept",
    "name": "data-pipeline",
    "definition": "ETL process with Python and SQL"
  }
}
```

## Storage Architecture

### File Structure

```
brain.fs/
??? memories.txt      # Append-only memory log
??? cortex.json       # Active focus threads
??? structures.json   # Adaptive structures
```

### Memory Format

```
[2025-06-17T10:30:00] Content text here #optional,tags
```

### Data Persistence

- **Append-only**: Ensures audit trail
- **UTF-8 encoding**: International language support
- **Timestamped**: Full temporal tracking
- **Tagged**: Optional categorization

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------||
| MEMORY_PATH | Path to memory storage | ~/.mint-mcp/memory-palace/brain.fs |

### Custom Configuration

Create a custom configuration file:

```yaml
# config/memory-palace.yaml
memory:
  path: /custom/path/brain.fs
  max_size: 100MB
  backup_enabled: true
  
relevance:
  threshold: 0.3
  keywords:
    - important
    - remember
    - note
```

## Integration Examples

### Claude Desktop

```json
{
  "mcpServers": {
    "mint-memory-palace": {
      "command": "python",
      "args": ["C:/mint-mcp/servers/memory-palace/main.py"],
      "env": {
        "MEMORY_PATH": "C:/mint-mcp/data/brain.fs"
      }
    }
  }
}
```

### Python Client

```python
import asyncio
from mcp import Client

async def use_memory():
    async with Client() as client:
        await client.connect("memory-palace")
        
        # Observe information
        await client.call_tool("memory_observe", {
            "content": "User prefers dark mode"
        })
        
        # Recall information
        result = await client.call_tool("memory_recall", {
            "query": "user preferences"
        })
        print(result)

asyncio.run(use_memory())
```

## Performance Considerations

### Scalability

- **Append-only design**: O(1) write performance
- **Linear search**: O(n) read performance
- **Recommended limit**: 100MB per brain file

### Optimization Tips

1. **Regular archiving**: Move old memories to archive
2. **Tag usage**: Improves search efficiency
3. **Thread management**: Keep active threads minimal
4. **Structure pruning**: Remove unused structures

## Security

### Access Control

- File system permissions
- Process isolation
- No network exposure by default

### Data Privacy

- Local storage only
- No external transmission
- User-controlled data lifecycle

## Troubleshooting

### Common Issues

**Memory not persisting**
- Check file permissions
- Verify MEMORY_PATH
- Ensure disk space available

**Recall not finding results**
- Check query terms
- Verify memory exists
- Try broader search terms

**Performance degradation**
- Archive old memories
- Reduce thread count
- Check file size

## Future Enhancements

- Vector embeddings for semantic search
- Distributed memory systems
- Memory compression
- Advanced query language
- Memory visualization

## Support

- **GitHub Issues**: [Report bugs](https://github.com/data-mint-research/mint-mcp/issues)
- **Documentation**: [Main docs](https://github.com/data-mint-research/mint-mcp/tree/main/docs)
- **Contact**: mint-research@neomint.com