# MINT-MCP

Multi-Server Model Context Protocol Architecture

## Overview

MINT-MCP provides a modular, enterprise-ready platform for deploying and managing multiple MCP servers. Built with professional standards for clarity, maintainability, and auditability.

## Quick Start

### One-Line Installation
```powershell
./run.ps1
```

### Requirements

- Windows 11 Pro or compatible system
- PowerShell 5.1 or later
- Internet connection

All dependencies are automatically detected and installed.

## Architecture

MINT-MCP implements a clean, modular architecture:

```
MINT-MCP Ecosystem
??? Memory Palace     Advanced memory system (Production Ready)
??? MINT Registrar    Server orchestration (Coming Soon)
??? Template Server   Development templates (Coming Soon)
```

## Servers

### Memory Palace

Context-aware long-term memory system with plasticity and semantic recall.

**Features**

- Passive observation with relevance evaluation
- Persistent file-based storage with audit trails
- Multi-language support (German/English)
- Semantic recall with soft pattern matching
- Cortex threading for mental focus
- Adaptive plasticity for structure creation

**Status**: Production Ready  
**Documentation**: [docs/servers/memory-palace.md](docs/servers/memory-palace.md)

### MINT Registrar

Git-based MCP server orchestration and deployment system.

**Purpose**: Deploy and manage custom MCP servers from company repositories  
**Status**: Coming Soon

### Template Server

Template system for rapid MCP server development.

**Purpose**: Standardized templates for consistent server creation  
**Status**: Coming Soon

## Documentation

- [Usage Guide](docs/usage.md) - Complete usage instructions
- [Architecture Overview](docs/architecture.md) - Technical architecture
- [Development Guide](docs/development.md) - Development setup and guidelines
- [Security Documentation](docs/security.md) - Security policies and practices

## Client Integration

### Claude Desktop

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

### Claude Code

```bash
claude --mcp-config config/mint-mcp.json \
       --allowedTools "mcp__mint-memory-palace__*"
```

### Docker

```bash
docker run -d --name mint-mcp-memory-palace \
  -v "./brain.fs:/app/brain.fs" \
  mint-mcp/memory-palace:latest
```

## Development

### Getting Started

```bash
git clone https://github.com/data-mint-research/mint-mcp.git
cd mint-mcp
./run.ps1 -Mode install
```

### Structure

```
mint-mcp/
??? servers/           MCP server implementations
??? shared/            Common utilities and configurations
??? docs/              Documentation
??? .github/           GitHub workflows and templates
??? .well-known/       Machine-readable metadata
```

### Contributing

1. Read [Development Guide](docs/development.md)
2. Follow UX/UI standards for all contributions
3. Ensure automated validation passes
4. Submit pull request with proper template

## Support

- **Issues**: [GitHub Issues](https://github.com/data-mint-research/mint-mcp/issues)
- **Documentation**: [docs/](docs/)
- **Security**: [security.md](docs/security.md)
- **Contact**: mint-research@neomint.com

## Legal

- **Author**: skr
- **Copyright**: NeoMINT GmbH 2025
- **Owner**: MINT-RESEARCH
- **Contact**: mint-research@neomint.com
- **License**: MIT
