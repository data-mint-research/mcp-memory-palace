# Development Guide

Comprehensive guide for developing with and contributing to MINT-MCP.

## Getting Started

### Prerequisites

- Python 3.10+
- Git
- Docker (optional)
- VS Code or preferred IDE

### Development Setup

```bash
# Clone repository
git clone https://github.com/data-mint-research/mint-mcp.git
cd mint-mcp

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt
```

## Project Structure

```
mint-mcp/
??? servers/                 # MCP server implementations
?   ??? memory-palace/       # Production memory server
?   ??? mint-registrar/      # Server orchestration (planned)
?   ??? template-server/     # Development templates (planned)
??? shared/                  # Shared utilities and libraries
?   ??? scripts/             # Build and deployment scripts
?   ??? utils/               # Common utilities
?   ??? config/              # Shared configurations
??? docs/                    # Documentation
??? .github/                 # GitHub workflows and templates
??? .well-known/             # Machine-readable metadata
```

## Development Standards

### Code Style

**Python**:
- Follow PEP 8
- Use type hints
- Maximum line length: 88 characters
- Use Black for formatting

```python
# Example of proper style
from typing import List, Optional

def process_memory(content: str, tags: Optional[List[str]] = None) -> str:
    """Process and store memory content.
    
    Args:
        content: The content to memorize
        tags: Optional list of tags
        
    Returns:
        Confirmation message
    """
    if tags is None:
        tags = []
    # Implementation...
```

**File Headers**:

All files must include standardized headers:

```python
#!/usr/bin/env python3
"""
File:             filename.py
Purpose:          Brief description
Author:           skr
Owner:            MINT-RESEARCH / NeoMINT GmbH
Contact:          mint-research@neomint.com
License:          MIT / ? NeoMINT GmbH 2025
Created:          YYYY-MM-DD
Last Modified:    YYYY-MM-DD by author
Status:           Draft|Stable|Deprecated
Tags:             relevant, tags, here
"""
```

### Naming Conventions

- **Files**: `snake_case.py`
- **Directories**: `kebab-case/`
- **Classes**: `PascalCase`
- **Functions**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`

### Git Workflow

1. **Branching Strategy**:
   - `main`: Production-ready code
   - `develop`: Integration branch
   - `feature/*`: New features
   - `fix/*`: Bug fixes
   - `docs/*`: Documentation updates

2. **Commit Messages**:
   ```
   type(scope): subject
   
   body (optional)
   
   footer (optional)
   ```
   
   Types: feat, fix, docs, style, refactor, test, chore

3. **Pull Request Process**:
   - Create feature branch
   - Make changes with atomic commits
   - Update tests and documentation
   - Submit PR using template
   - Address review feedback
   - Squash and merge

## Creating a New MCP Server

### Using Template (Future)

```bash
./run.ps1 -Mode create -Template basic -Name my-server
```

### Manual Creation

1. **Create Directory Structure**:
   ```
   servers/my-server/
   ??? main.py
   ??? config.py
   ??? requirements.txt
   ??? README.md
   ??? tests/
   ```

2. **Implement Server**:
   ```python
   # main.py
   import asyncio
   from mcp.server import Server
   from mcp.server.stdio import stdio_server
   
   server = Server("my-server")
   
   # Add tools
   server.add_tool(my_tool)
   
   async def main():
       async with stdio_server() as (read, write):
           await server.run(read, write)
   
   if __name__ == "__main__":
       asyncio.run(main())
   ```

3. **Define Tools**:
   ```python
   from mcp.types import Tool
   
   my_tool = Tool(
       name="my_tool",
       description="Tool description",
       input_schema={
           "type": "object",
           "properties": {
               "param": {"type": "string"}
           },
           "required": ["param"]
       },
       fn=lambda args: process(args["param"])
   )
   ```

## Testing

### Unit Tests

```python
# tests/test_memory.py
import pytest
from memory_palace import recall

def test_recall_empty():
    result = recall("test query")
    assert result == "Keine relevanten Erinnerungen gefunden."

def test_recall_with_data():
    # Setup test data
    # Test recall
    # Assert results
```

### Integration Tests

```python
# tests/test_integration.py
import asyncio
from mcp.client import Client

async def test_server_communication():
    async with Client() as client:
        await client.connect("memory-palace")
        result = await client.call_tool("memory_observe", {"content": "test"})
        assert "Beobachtet" in result
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=servers/memory-palace

# Run specific test
pytest tests/test_memory.py::test_recall_empty
```

## Contributing

### Before Contributing

1. Check existing issues
2. Discuss major changes
3. Follow coding standards
4. Write tests
5. Update documentation

### Submission Process

1. Fork repository
2. Create feature branch
3. Make changes
4. Run tests
5. Submit pull request
6. Address feedback

### Code Review Checklist

- [ ] Follows coding standards
- [ ] Includes tests
- [ ] Updates documentation
- [ ] No security issues
- [ ] Performance considered
- [ ] Backward compatible

## Support

- **Development Chat**: Coming soon
- **Issues**: [GitHub Issues](https://github.com/data-mint-research/mint-mcp/issues)
- **Email**: mint-research@neomint.com

## Resources

- [MCP Specification](https://modelcontextprotocol.io)
- [Python Best Practices](https://docs.python-guide.org)
- [Docker Documentation](https://docs.docker.com)
- [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)