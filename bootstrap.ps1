# bootstrap.ps1 ? One-line startup for MCP Memory Palace (PowerShell)

$repo = "https://github.com/data-mint-research/mcp-memory-palace.git"
$folder = "mcp-memory-palace"

if (-not (Test-Path $folder)) {
    Write-Host "[INFO] Cloning repository..." -ForegroundColor Green
    git clone $repo
} else {
    Write-Host "[INFO] Repository exists, pulling latest changes..." -ForegroundColor Green
    Set-Location $folder
    git pull origin main
    Set-Location ..
}

Set-Location $folder

Write-Host "[INFO] Building Docker image (no cache)..." -ForegroundColor Green
docker build --no-cache -t memory-palace .

Write-Host "[INFO] Starting container on port 8080..." -ForegroundColor Green
docker run -p 8080:8080 -v "${PWD}/brain.fs:/app/brain.fs" memory-palace