# Legacy Files - TO BE DELETED

This directory contains all legacy files that were moved from the root directory during the MINT-MCP migration.

## Files Moved Here:

### Python Files (now in servers/memory-palace/)
- `config.py` - Configuration module
- `cortex.py` - Cortex threading system  
- `main.py` - Main entry point
- `memorize.py` - Active memorization
- `observe.py` - Passive observation
- `plasticity.py` - Adaptive structures
- `recall.py` - Memory recall
- `relevance.py` - Relevance assessment
- `suggest.py` - Deprecated suggestions
- `utils.py` - Utility functions

### Bootstrap Scripts (replaced by run.ps1)
- `bootstrap.ps1` - Old Windows bootstrap
- `bootstrap.sh` - Old Linux/Mac bootstrap

### Docker (now in servers/memory-palace/docker/)
- `Dockerfile` - Old Docker configuration

## Action Required:

1. Verify the migration is complete by running:
   ```powershell
   .\shared\scripts\validate-migration.ps1
   ```

2. Test the new structure:
   ```powershell
   .\run.ps1
   ```

3. Once verified, delete this entire `Delete` directory:
   ```powershell
   Remove-Item -Path Delete -Recurse -Force
   ```

## Note:
The original files in the root directory still need to be deleted manually.
This directory just contains copies for reference.