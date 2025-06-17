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

## ? MCP Hosting via Docker Desktop (MCP Extension)

This project is fully compatible with the Docker Desktop MCP Extension  
(available via the Docker Marketplace or `docker extension install`).

To make this memory module discoverable by agents like Claude:

1. Open Docker Desktop
2. Go to: **Extensions > Model Context Protocol (MCP)**
3. Click "Add Local MCP Component"
4. Choose the project directory:
   ```
   ~/path/to/mcp-memory-palace/
   ```
5. Confirm and start the container

Once registered, Claude or other tools can access the API via:

```json
{
  "tool": "recall",
  "input": { "topic": "example" }
}
```

> Note: You may need to expose your endpoint via `ngrok`, `cloudflared`, or `fly.io`  
> for remote access beyond your local machine.

---

## Compliance

- `.well-known/mcp-memory-palace.json` describes system capabilities
- Configuration: `./config/config.yaml`

---

## Legal

- Author: skr  
- Copyright: NeoMINT GmbH 2025  
- Owner: MINT-RESEARCH  
- Contact: mint-research@neomint.com  
- License: [MIT](./LICENSE)