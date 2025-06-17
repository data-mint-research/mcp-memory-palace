# Shared Utilities

This directory contains shared utilities and common code used across MINT-MCP servers.

## Structure

```
utils/
??? logging/          # Logging utilities
??? config/           # Configuration helpers
??? security/         # Security utilities
??? mcp/              # MCP protocol helpers
```

## Usage

Import utilities in your server:

```python
from shared.utils.logging import get_logger
from shared.utils.config import load_config
from shared.utils.security import validate_input
```

## Contributing

When adding new utilities:
1. Create appropriate subdirectory
2. Include comprehensive documentation
3. Add unit tests
4. Update this README