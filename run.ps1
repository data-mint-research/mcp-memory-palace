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

# Check PowerShell version
if ($PSVersionTable.PSVersion.Major -lt 5) {
    Write-Host "ERROR: PowerShell 5.0 or higher required" -ForegroundColor Red
    exit 1
}

# Core installation functions
function Test-Python {
    try {
        $pythonVersion = python --version 2>&1
        if ($pythonVersion -match "Python (\d+)\.(\d+)") {
            $major = [int]$matches[1]
            $minor = [int]$matches[2]
            return ($major -eq 3 -and $minor -ge 10)
        }
    } catch {}
    return $false
}

function Test-Git {
    try {
        $null = git --version 2>&1
        return $?
    } catch {
        return $false
    }
}

function Test-Docker {
    try {
        $null = docker --version 2>&1
        return $?
    } catch {
        return $false
    }
}

function Install-Python {
    Write-Host "Installing Python..." -ForegroundColor Yellow
    $pythonUrl = "https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe"
    $installer = "$env:TEMP\python-installer.exe"
    
    Invoke-WebRequest -Uri $pythonUrl -OutFile $installer
    Start-Process -FilePath $installer -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1" -Wait
    Remove-Item $installer
    
    # Refresh PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}

function Install-Git {
    Write-Host "Installing Git..." -ForegroundColor Yellow
    $gitUrl = "https://github.com/git-for-windows/git/releases/download/v2.45.2.windows.1/Git-2.45.2-64-bit.exe"
    $installer = "$env:TEMP\git-installer.exe"
    
    Invoke-WebRequest -Uri $gitUrl -OutFile $installer
    Start-Process -FilePath $installer -ArgumentList "/VERYSILENT", "/NORESTART" -Wait
    Remove-Item $installer
    
    # Refresh PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
}

function Install-Dependencies {
    param([switch]$Force)
    
    if ($Force -or !(Test-Python)) {
        Install-Python
    }
    
    if ($Force -or !(Test-Git)) {
        Install-Git
    }
    
    if (!$Quiet) {
        Write-Host "Dependencies verified" -ForegroundColor Green
    }
}

function Clone-Repository {
    param([string]$Path)
    
    if (Test-Path $Path) {
        if (!$Quiet) {
            Write-Host "Repository already exists at $Path" -ForegroundColor Yellow
        }
        return
    }
    
    Write-Host "Cloning MINT-MCP repository..." -ForegroundColor Yellow
    git clone $REPOSITORY_URL $Path
}

function Install-MintMCP {
    param(
        [string]$Server,
        [string]$InstallPath,
        [switch]$Force,
        [switch]$Quiet
    )
    
    # Install dependencies
    Install-Dependencies -Force:$Force
    
    # Clone repository if needed
    Clone-Repository -Path $InstallPath
    
    # Install Python dependencies for server
    $serverPath = Join-Path $InstallPath "servers\$Server"
    if (Test-Path $serverPath) {
        Push-Location $serverPath
        if (!$Quiet) {
            Write-Host "Installing $Server dependencies..." -ForegroundColor Yellow
        }
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        Pop-Location
    }
    
    if (!$Quiet) {
        Write-Host "$Server installed successfully!" -ForegroundColor Green
    }
}

function Start-MintMCPServer {
    param(
        [string]$Server,
        [string]$InstallPath,
        [switch]$Quiet
    )
    
    $serverPath = Join-Path $InstallPath "servers\$Server\main.py"
    if (!(Test-Path $serverPath)) {
        Write-Host "ERROR: Server not found. Run with -Mode install first." -ForegroundColor Red
        exit 1
    }
    
    if (!$Quiet) {
        Write-Host "Starting $Server..." -ForegroundColor Yellow
    }
    
    python $serverPath
}

function Get-MintMCPStatus {
    param(
        [string]$Server,
        [string]$InstallPath
    )
    
    Write-Host "`nMINT-MCP Status Report" -ForegroundColor Cyan
    Write-Host ("=" * 30) -ForegroundColor Cyan
    
    # Check installation
    $serverPath = Join-Path $InstallPath "servers\$Server"
    if (Test-Path $serverPath) {
        Write-Host "? $Server installed" -ForegroundColor Green
    } else {
        Write-Host "? $Server not installed" -ForegroundColor Red
    }
    
    # Check dependencies
    Write-Host "`nDependencies:" -ForegroundColor Cyan
    if (Test-Python) {
        $pyVersion = python --version
        Write-Host "? Python: $pyVersion" -ForegroundColor Green
    } else {
        Write-Host "? Python not found" -ForegroundColor Red
    }
    
    if (Test-Git) {
        $gitVersion = git --version
        Write-Host "? Git: $gitVersion" -ForegroundColor Green
    } else {
        Write-Host "? Git not found" -ForegroundColor Red
    }
    
    if (Test-Docker) {
        $dockerVersion = docker --version
        Write-Host "? Docker: $dockerVersion" -ForegroundColor Green
    } else {
        Write-Host "? Docker not found (optional)" -ForegroundColor Yellow
    }
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
        Write-Host "Stop functionality not yet implemented" -ForegroundColor Yellow
    }
    "status" {
        Get-MintMCPStatus -Server $Server -InstallPath $InstallPath
    }
    "update" {
        Push-Location $InstallPath
        git pull
        Pop-Location
        Install-MintMCP -Server $Server -InstallPath $InstallPath -Quiet:$Quiet
    }
}

if (!$Quiet) {
    Write-Host "`n$PROJECT_NAME operation completed successfully!" -ForegroundColor Green
    Write-Host "Support: $CONTACT" -ForegroundColor Gray
}