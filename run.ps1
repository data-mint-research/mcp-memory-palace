# ==============================================================================
# File:             run.ps1
# Purpose:          MINT-MCP one-line environment starter and installer
# Author:           skr
# Owner:            MINT-RESEARCH / NeoMINT GmbH
# Contact:          mint-research@neomint.com
# License:          MIT / ? NeoMINT GmbH 2025
# Created:          2025-06-17
# Last Modified:    2025-06-17 by skr
# Status:           Stable
# Tags:             startup, installer, mcp, environment, docker
# ==============================================================================

<#
.SYNOPSIS
    MINT-MCP Multi-Server Architecture Starter
.DESCRIPTION
    Intelligent installer and starter for MINT-MCP ecosystem.
    Automatically detects, installs, and configures all dependencies.
.PARAMETER Server
    Specific server to install/start (default: memory-palace)
.PARAMETER Mode
    Operation mode: install, start, stop, status (default: install)
.PARAMETER InstallPath
    Installation directory (default: $env:USERPROFILE\mint-mcp)
.PARAMETER Force
    Force reinstallation of components
.PARAMETER Quiet
    Suppress non-error output
.EXAMPLE
    .\run.ps1
    Install and start Memory Palace with default settings
.EXAMPLE
    .\run.ps1 -Server memory-palace -Mode start
    Start existing Memory Palace installation
.EXAMPLE
    .\run.ps1 -Force -Quiet
    Force reinstall all components silently
#>

[CmdletBinding()]
param(
    [ValidateSet("memory-palace", "mint-registrar", "template-server")]
    [string]$Server = "memory-palace",
    
    [ValidateSet("install", "start", "stop", "status", "update")]
    [string]$Mode = "install",
    
    [string]$InstallPath = "$env:USERPROFILE\mint-mcp",
    
    [switch]$Force,
    [switch]$Quiet
)

# Project constants
$PROJECT_NAME = "MINT-MCP"
$PROJECT_VERSION = "2.0.0"
$REPOSITORY_URL = "https://github.com/data-mint-research/mint-mcp.git"
$CONTACT = "mint-research@neomint.com"

# Initialize logging
if (!$Quiet) {
    Write-Host "$PROJECT_NAME v$PROJECT_VERSION" -ForegroundColor Green
    Write-Host "Copyright (c) NeoMINT GmbH 2025" -ForegroundColor Gray
    Write-Host ("=" * 50) -ForegroundColor Green
}

# Temporary implementation until shared scripts are ready
function Install-MintMCP {
    param($Server, $InstallPath, $Force, $Quiet)
    
    if (!$Quiet) { Write-Host "`nChecking dependencies..." -ForegroundColor Cyan }
    
    # Check Python
    try {
        $pythonVersion = python --version 2>&1
        if (!$Quiet) { Write-Host "? Python installed: $pythonVersion" -ForegroundColor Green }
    } catch {
        Write-Host "? Python not found. Please install Python 3.10+" -ForegroundColor Red
        Write-Host "   Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
        exit 1
    }
    
    # Check Git
    try {
        $gitVersion = git --version
        if (!$Quiet) { Write-Host "? Git installed: $gitVersion" -ForegroundColor Green }
    } catch {
        Write-Host "? Git not found. Please install Git" -ForegroundColor Red
        Write-Host "   Download from: https://git-scm.com/download/win" -ForegroundColor Yellow
        exit 1
    }
    
    # Clone or update repository
    if (Test-Path "$InstallPath") {
        if (!$Quiet) { Write-Host "`nUpdating existing installation..." -ForegroundColor Cyan }
        Push-Location $InstallPath
        git pull origin main
        Pop-Location
    } else {
        if (!$Quiet) { Write-Host "`nCloning MINT-MCP repository..." -ForegroundColor Cyan }
        git clone $REPOSITORY_URL $InstallPath
    }
    
    # Install Python dependencies for selected server
    $serverPath = Join-Path $InstallPath "servers\$Server"
    if (Test-Path "$serverPath\requirements.txt") {
        if (!$Quiet) { Write-Host "`nInstalling Python dependencies for $Server..." -ForegroundColor Cyan }
        Push-Location $serverPath
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        Pop-Location
    }
    
    if (!$Quiet) { Write-Host "`n? Installation complete!" -ForegroundColor Green }
}

function Start-MintMCPServer {
    param($Server, $InstallPath, $Quiet)
    
    $serverPath = Join-Path $InstallPath "servers\$Server"
    $mainPy = Join-Path $serverPath "main.py"
    
    if (!(Test-Path $mainPy)) {
        Write-Host "? Server not found: $Server" -ForegroundColor Red
        Write-Host "   Run with -Mode install first" -ForegroundColor Yellow
        exit 1
    }
    
    if (!$Quiet) { Write-Host "`nStarting $Server..." -ForegroundColor Cyan }
    Push-Location $serverPath
    python main.py
    Pop-Location
}

function Stop-MintMCPServer {
    param($Server, $InstallPath, $Quiet)
    
    if (!$Quiet) { Write-Host "`nStopping $Server..." -ForegroundColor Cyan }
    # Implementation depends on how servers are run (process management)
    Write-Host "Stop functionality coming soon" -ForegroundColor Yellow
}

function Get-MintMCPStatus {
    param($Server, $InstallPath)
    
    Write-Host "`nMINT-MCP Status" -ForegroundColor Cyan
    Write-Host "===============" -ForegroundColor Cyan
    
    # Check installation
    if (Test-Path $InstallPath) {
        Write-Host "? Installation found: $InstallPath" -ForegroundColor Green
        
        # Check server
        $serverPath = Join-Path $InstallPath "servers\$Server"
        if (Test-Path $serverPath) {
            Write-Host "? Server available: $Server" -ForegroundColor Green
        } else {
            Write-Host "? Server not found: $Server" -ForegroundColor Red
        }
    } else {
        Write-Host "? Not installed at: $InstallPath" -ForegroundColor Red
    }
    
    # Check dependencies
    Write-Host "`nDependencies:" -ForegroundColor Cyan
    try {
        $pythonVersion = python --version 2>&1
        Write-Host "? Python: $pythonVersion" -ForegroundColor Green
    } catch {
        Write-Host "? Python: Not installed" -ForegroundColor Red
    }
    
    try {
        $gitVersion = git --version
        Write-Host "? Git: $gitVersion" -ForegroundColor Green
    } catch {
        Write-Host "? Git: Not installed" -ForegroundColor Red
    }
}

function Update-MintMCP {
    param($Server, $InstallPath, $Quiet)
    
    if (!$Quiet) { Write-Host "`nUpdating MINT-MCP..." -ForegroundColor Cyan }
    
    if (!(Test-Path $InstallPath)) {
        Write-Host "? Not installed. Run with -Mode install first" -ForegroundColor Red
        exit 1
    }
    
    Push-Location $InstallPath
    git pull origin main
    Pop-Location
    
    # Update dependencies
    $serverPath = Join-Path $InstallPath "servers\$Server"
    if (Test-Path "$serverPath\requirements.txt") {
        if (!$Quiet) { Write-Host "Updating dependencies for $Server..." -ForegroundColor Cyan }
        Push-Location $serverPath
        pip install -r requirements.txt --upgrade
        Pop-Location
    }
    
    if (!$Quiet) { Write-Host "? Update complete!" -ForegroundColor Green }
}

# Execute based on mode
switch ($Mode) {
    "install" {
        Install-MintMCP -Server $Server -InstallPath $InstallPath -Force:$Force -Quiet:$Quiet
    }
    "start" {
        Start-MintMCPServer -Server $Server -InstallPath $InstallPath -Quiet:$Quiet
    }
    "stop" {
        Stop-MintMCPServer -Server $Server -InstallPath $InstallPath -Quiet:$Quiet
    }
    "status" {
        Get-MintMCPStatus -Server $Server -InstallPath $InstallPath
    }
    "update" {
        Update-MintMCP -Server $Server -InstallPath $InstallPath -Quiet:$Quiet
    }
}

if (!$Quiet) {
    Write-Host "`n$PROJECT_NAME operation completed successfully!" -ForegroundColor Green
    Write-Host "Support: $CONTACT" -ForegroundColor Gray
}
