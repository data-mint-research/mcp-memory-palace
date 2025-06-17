# bootstrap.ps1 ? One-line startup for MCP Memory Palace (PowerShell)

$repo = "https://github.com/data-mint-research/mcp-memory-palace.git"
$folder = "mcp-memory-palace"

if (-not (Test-Path $folder)) {
    git clone $repo
}

Set-Location $folder
docker build -t memory-palace .
docker run -p 8080:8080 -v "${PWD}/brain.fs:/app/brain.fs" memory-palace