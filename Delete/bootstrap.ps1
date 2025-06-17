$scriptUrl = "https://raw.githubusercontent.com/data-mint-research/mint-mcp/main/setup.ps1"
$localPath = "$env:TEMP\mint-mcp-setup.ps1"

try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest -Uri $scriptUrl -OutFile $localPath -UseBasicParsing
    
    $setupArgs = $args -join ' '
    
    if ($setupArgs) {
        & $localPath $setupArgs
    } else {
        & $localPath
    }
    
    Remove-Item $localPath -Force -ErrorAction SilentlyContinue
} catch {
    Write-Host "Error: Failed to download or run setup script" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}