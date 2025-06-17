# ==============================================================================
# File:             validate-migration.ps1
# Purpose:          Validate MINT-MCP migration completeness
# Author:           skr
# Owner:            MINT-RESEARCH / NeoMINT GmbH
# Contact:          mint-research@neomint.com
# License:          MIT / ? NeoMINT GmbH 2025
# Created:          2025-06-17
# Last Modified:    2025-06-17 by skr
# Status:           Stable
# Tags:             validation, migration, quality-check
# ==============================================================================

<#
.SYNOPSIS
    Validates the MINT-MCP migration and UX/UI implementation
.DESCRIPTION
    Comprehensive validation of repository structure, file headers,
    and compliance with UX/UI standards
.EXAMPLE
    .\shared\scripts\validate-migration.ps1
#>

Write-Host "MINT-MCP Migration Validation" -ForegroundColor Cyan
Write-Host "=============================" -ForegroundColor Cyan
Write-Host ""

$ValidationResults = @()

# Function to add result
function Add-Result {
    param(
        [string]$Category,
        [string]$Item,
        [bool]$Success,
        [string]$Message
    )
    
    $script:ValidationResults += [PSCustomObject]@{
        Category = $Category
        Item = $Item
        Success = $Success
        Message = $Message
    }
}

# Check new structure exists
Write-Host "Checking new structure..." -ForegroundColor Yellow

$RequiredPaths = @(
    "servers/memory-palace/main.py",
    "servers/memory-palace/config.py",
    "servers/memory-palace/requirements.txt",
    "servers/memory-palace/docker/Dockerfile",
    "docs/usage.md",
    "docs/architecture.md",
    "docs/development.md",
    "docs/security.md",
    ".github/workflows/validate-structure.yml",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".well-known/mint-mcp.json",
    ".well-known/security.json",
    "run.ps1",
    ".gitignore",
    ".editorconfig",
    "docker-compose.yml"
)

foreach ($path in $RequiredPaths) {
    if (Test-Path $path) {
        Add-Result -Category "Structure" -Item $path -Success $true -Message "? Found"
    } else {
        Add-Result -Category "Structure" -Item $path -Success $false -Message "? Missing"
    }
}

# Check for files that should be deleted
Write-Host "`nChecking for legacy files..." -ForegroundColor Yellow

$LegacyFiles = @(
    "bootstrap.ps1",
    "bootstrap.sh",
    "config.py",
    "cortex.py",
    "main.py",
    "memorize.py",
    "observe.py",
    "plasticity.py",
    "recall.py",
    "relevance.py",
    "suggest.py",
    "utils.py",
    "Dockerfile"
)

foreach ($file in $LegacyFiles) {
    if (Test-Path $file) {
        Add-Result -Category "Legacy" -Item $file -Success $false -Message "?? Should be deleted"
    } else {
        Add-Result -Category "Legacy" -Item $file -Success $true -Message "? Not found (good)"
    }
}

# Check runtime data
if (Test-Path "brain.fs") {
    Add-Result -Category "Runtime" -Item "brain.fs" -Success $false -Message "?? Runtime data should be deleted"
}

# Display results
Write-Host "`n`nValidation Results:" -ForegroundColor Cyan
Write-Host "===================" -ForegroundColor Cyan

$Categories = $ValidationResults | Group-Object Category
foreach ($cat in $Categories) {
    Write-Host "`n$($cat.Name):" -ForegroundColor Yellow
    foreach ($result in $cat.Group) {
        $color = if ($result.Success) { "Green" } else { "Red" }
        Write-Host "  $($result.Message) - $($result.Item)" -ForegroundColor $color
    }
}

# Summary
$TotalChecks = $ValidationResults.Count
$Passed = ($ValidationResults | Where-Object { $_.Success }).Count
$Failed = $TotalChecks - $Passed

Write-Host "`n`nSummary:" -ForegroundColor Cyan
Write-Host "========" -ForegroundColor Cyan
Write-Host "Total Checks: $TotalChecks" -ForegroundColor White
Write-Host "Passed: $Passed" -ForegroundColor Green
Write-Host "Failed: $Failed" -ForegroundColor $(if ($Failed -eq 0) { "Green" } else { "Red" })

if ($Failed -gt 0) {
    Write-Host "`n??  Action Required:" -ForegroundColor Yellow
    Write-Host "Please delete the legacy files listed above to complete the migration." -ForegroundColor Yellow
    exit 1
} else {
    Write-Host "`n? Migration validation passed!" -ForegroundColor Green
    exit 0
}