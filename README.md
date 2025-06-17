# MCP Memory Palace

A modular, context-aware long-term memory module for humans and intelligent agents.  
Compliant with the Anthropic Model Context Protocol (MCP).

---

## ? One-Line Quickstart

### ? PowerShell (Windows):
```powershell
irm https://raw.githubusercontent.com/data-mint-research/mcp-memory-palace/main/bootstrap.ps1 | iex
```

### ? Bash/macOS:
```bash
bash <(curl -s https://raw.githubusercontent.com/data-mint-research/mcp-memory-palace/main/bootstrap.sh)
```

These commands will:
- Clone the repository if needed
- Build the Docker image  
- Launch the container with file-based memory

---

## Features

- Passive observation with relevance evaluation
- Flatfile-based memory with audit trails
- Language-sensitive trigger structure (DE/EN)
- Recall by topic with soft pattern match
- Cortex for mental focus and threading
- Plasticity for adaptive structure creation

---

## API

- `POST /observe` ? evaluate & optionally store input
- `POST /memorize` ? directly write to memory
- `GET  /recall?topic=XYZ` ? retrieve related memories
- `GET  /suggest?trigger=XYZ` ? suggest entries
- `POST /focus?topic=XYZ` ? set new thought focus
- `POST /thread?note=XYZ` ? add a mental thread
- `POST /plasticity?reason=XYZ` ? initiate adaptive structure

---

## Compliance

- `.well-known/mcp-memory-palace.json` describes system capabilities
- Configuration: `./config/config.yaml`