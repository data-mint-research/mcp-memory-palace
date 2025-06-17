# ? MINT-MCP Migration Cleanup Required

This directory contains COPIES of all legacy files that need to be deleted from the root directory.

## ?? IMPORTANT: Manual Action Required

The following files and directories still exist in the root and need to be manually deleted:

### Python Files (duplicates - new versions are in servers/memory-palace/)
- [ ] `/config.py`
- [ ] `/cortex.py`
- [ ] `/main.py`
- [ ] `/memorize.py`
- [ ] `/observe.py`
- [ ] `/plasticity.py`
- [ ] `/recall.py`
- [ ] `/relevance.py`
- [ ] `/suggest.py`
- [ ] `/utils.py`

### Bootstrap Scripts (replaced by run.ps1)
- [ ] `/bootstrap.ps1`
- [ ] `/bootstrap.sh`

### Docker (replaced by servers/memory-palace/docker/)
- [ ] `/Dockerfile`

### Runtime Data (should not be in repository)
- [ ] `/brain.fs/` (entire directory)

### Other Legacy Items
- [ ] `/config/` (directory - if it contains legacy config)

## ? Migration Verification Steps

1. **Delete all files listed above from the root directory**

2. **Run the validation script:**
   ```powershell
   .\shared\scripts\validate-migration.ps1
   ```

3. **Test the new installation:**
   ```powershell
   .\run.ps1
   ```

4. **Check GitHub Actions:**
   The automated validation workflow should pass

5. **Delete this entire `Delete` directory:**
   ```powershell
   Remove-Item -Path Delete -Recurse -Force
   ```

## ? New Structure Overview

After cleanup, your repository should have this structure:

```
mint-mcp/
??? .github/              ? GitHub templates and workflows
??? .well-known/          ? Machine-readable metadata
??? docs/                 ? Documentation
??? servers/              ? MCP servers
?   ??? memory-palace/    ? Production memory server
??? shared/               ? Shared utilities
??? logs/                 ? Log directory
??? .editorconfig         ? Editor configuration
??? .env.example          ? Environment example
??? .gitignore            ? Git ignore rules
??? CHANGELOG.md          ? Version history
??? docker-compose.yml    ? Root Docker compose
??? LICENSE               ? MIT License
??? README.md             ? Professional landing page
??? run.ps1               ? One-line installer
```

## ? Migration Complete!

Once you've deleted all the legacy files from the root, the MINT-MCP migration will be complete!