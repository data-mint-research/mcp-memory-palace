# Changelog

All notable changes to MINT-MCP will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-06-17

### Added
- Complete MINT-MCP rebranding from mint-mcp-memory-palace
- Professional UX/UI standards implementation
- Modular multi-server architecture
- Comprehensive documentation structure
- GitHub-native integration with templates and workflows
- Machine-readable metadata in .well-known/
- Automated structure validation
- Docker support for all servers
- Enhanced run.ps1 installer script

### Changed
- Migrated from single server to multi-server architecture
- Restructured repository according to UX/UI standards
- Updated all file headers with complete metadata
- Improved documentation organization
- Enhanced security practices

### Removed
- Legacy bootstrap.ps1 and bootstrap.sh
- Root-level Python files (moved to servers/memory-palace/)
- Deprecated suggest.py functionality

## [1.0.0] - 2025-01-01

### Added
- Initial release of mint-mcp-memory-palace
- Basic memory storage and recall
- Passive observation with relevance scoring
- Active memorization with tags
- Cortex threading system
- Plasticity for adaptive structures

### Security
- Local file storage only
- No network exposure
- Process isolation

## [0.1.0] - 2024-12-01

### Added
- Proof of concept implementation
- Basic MCP server structure
- Simple memory storage

---

## Unreleased

### Planned
- MINT Registrar server implementation
- Template Server for rapid development
- OAuth 2.0 authentication
- Vector embeddings for semantic search
- Distributed memory systems
- Advanced monitoring and metrics

---

## Version History

- **2.0.0** - Current stable release
- **1.0.0** - Initial production release
- **0.1.0** - Proof of concept

## Support

For questions about changes:
- Review [commit history](https://github.com/data-mint-research/mint-mcp/commits/main)
- Check [release notes](https://github.com/data-mint-research/mint-mcp/releases)
- Contact: mint-research@neomint.com