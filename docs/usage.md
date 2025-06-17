# Usage Guide

Complete guide for using MINT-MCP servers with various clients.

## Prerequisites

- Windows 11 Pro or compatible system
- PowerShell 5.1 or later
- Internet connection for automatic dependency installation

## Installation

### Automatic Installation
```powershell
./run.ps1
```

The installer will automatically detect and install:
- Python 3.11+
- Git
- Docker Desktop
- Required dependencies

### Manual Installation

```bash
git clone https://github.com/data-mint-research/mint-mcp.git
cd mint-mcp/servers/memory-palace
pip install -r requirements.txt
python main.py
```

## Client Configuration

### Claude Desktop

Add to claude_desktop_config.json:

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

## Server Operations

### Memory Palace Operations

```bash
# Start server
python servers/memory-palace/main.py

# With custom config
python servers/memory-palace/main.py --config custom-config.yaml

# Docker mode
docker-compose -f servers/memory-palace/docker/docker-compose.yml up -d
```

## Troubleshooting

### Common Issues

#### Python Not Found

```powershell
# Run installer to install Python
./run.ps1 -Force
```

#### Permission Errors

```powershell
# Run as administrator
Start-Process PowerShell -Verb RunAs
./run.ps1
```

#### Docker Issues

```bash
# Check Docker status
docker --version
docker ps

# Restart Docker Desktop if needed
```

### Log Files

- Server logs: `servers/{server-name}/logs/`
- Installation logs: `logs/installation.log`

## Advanced Usage

### Multiple Servers

```bash
# Start specific server
./run.ps1 -Server memory-palace

# Future: Start multiple servers
./run.ps1 -Servers memory-palace,mint-registrar
```

### Custom Configuration

```yaml
# config/custom.yaml
server:
  name: "custom-memory-palace"
  port: 8001
  
memory:
  storage_path: "./custom-brain.fs"
  backup_enabled: true
```

## Support

For additional help:
- Check [troubleshooting guide](troubleshooting.md)
- Review [architecture documentation](architecture.md)
- Submit [GitHub issue](https://github.com/data-mint-research/mint-mcp/issues)