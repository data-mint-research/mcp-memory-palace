# ==============================================================================
# File:             setup-core.ps1
# Purpose:          Core setup functions for MINT-MCP installation
# Author:           skr
# Owner:            MINT-RESEARCH / NeoMINT GmbH
# Contact:          mint-research@neomint.com
# License:          MIT / ? NeoMINT GmbH 2025
# Created:          2025-06-17
# Last Modified:    2025-06-17 by skr
# Status:           Stable
# Tags:             setup, installation, core-functions
# ==============================================================================

# This file would contain the detailed implementation of setup functions
# Currently integrated into run.ps1 for simplicity
# Future versions will modularize these functions here

function Get-MintMCPRoot {
    return Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
}

function Test-MintMCPDependencies {
    param(
        [string[]]$Dependencies = @("Python", "Git")
    )
    
    $results = @{}
    foreach ($dep in $Dependencies) {
        $results[$dep] = switch ($dep) {
            "Python" { Test-Python }
            "Git" { Test-Git }
            "Docker" { Test-Docker }
            default { $false }
        }
    }
    return $results
}

function Initialize-MintMCPEnvironment {
    param(
        [string]$InstallPath
    )
    
    # Create necessary directories
    $dirs = @(
        "$InstallPath\logs",
        "$InstallPath\data",
        "$InstallPath\config"
    )
    
    foreach ($dir in $dirs) {
        if (!(Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }
}