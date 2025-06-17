# Security Documentation

Security policies and best practices for MINT-MCP.

## Overview

MINT-MCP implements defense-in-depth security principles to protect data and ensure system integrity.

## Security Architecture

### Authentication

**Current Implementation**:
- Local file system permissions
- Process isolation
- User-based access control

**Planned Features**:
- OAuth 2.0 integration
- API key authentication
- Multi-factor authentication

### Authorization

**Tool-Level Permissions**:
```json
{
  "permissions": {
    "memory_observe": ["read"],
    "memory_memorize": ["write"],
    "memory_recall": ["read"],
    "memory_focus": ["read", "write"],
    "memory_plasticity": ["write"]
  }
}
```

**Resource Access Control**:
- File system isolation
- Memory path restrictions
- Configuration validation

### Data Protection

**At Rest**:
- File system permissions
- Optional encryption (planned)
- Secure deletion

**In Transit**:
- STDIO isolation
- TLS 1.3 for network transport (future)
- Message signing

## Vulnerability Disclosure

### Reporting Security Issues

**DO NOT** report security vulnerabilities through public GitHub issues.

**Instead**:
1. Email: mint-research@neomint.com
2. Subject: "SECURITY: [Brief description]"
3. Include:
   - Description of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### Response Timeline

- **Acknowledgment**: Within 72 hours
- **Initial Assessment**: Within 1 week
- **Resolution Target**: Within 30 days
- **Public Disclosure**: After fix is deployed

## Security Practices

### Code Security

1. **Input Validation**:
   ```python
   def validate_memory_content(content: str) -> str:
       # Prevent injection attacks
       if not isinstance(content, str):
           raise TypeError("Content must be string")
       
       # Size limits
       if len(content) > MAX_CONTENT_SIZE:
           raise ValueError("Content too large")
       
       # Sanitize
       return content.strip()
   ```

2. **Path Traversal Prevention**:
   ```python
   from pathlib import Path
   
   def safe_file_path(user_path: str) -> Path:
       base = Path(MEMORY_PATH).parent
       requested = (base / user_path).resolve()
       
       if not requested.is_relative_to(base):
           raise SecurityError("Path traversal detected")
       
       return requested
   ```

3. **Command Injection Prevention**:
   - No shell command execution
   - Parameterized operations only
   - Whitelist-based validation

### Dependency Security

1. **Dependency Scanning**:
   ```bash
   # Regular security audits
   pip-audit
   safety check
   ```

2. **Version Pinning**:
   ```txt
   # requirements.txt
   mcp==1.0.0  # Exact version
   python-dotenv>=1.0.0,<2.0.0  # Range
   ```

3. **Update Policy**:
   - Monthly security updates
   - Immediate critical patches
   - Automated vulnerability scanning

### Cryptography

**Current Usage**:
- File system checksums
- Random token generation

**Implementation**:
```python
import secrets
import hashlib

def generate_token() -> str:
    """Generate cryptographically secure token."""
    return secrets.token_urlsafe(32)

def hash_content(content: str) -> str:
    """Create secure hash of content."""
    return hashlib.sha256(content.encode()).hexdigest()
```

## Operational Security

### Logging

**Security Events**:
```python
import logging
from datetime import datetime

security_logger = logging.getLogger("security")

def log_security_event(event_type: str, details: dict):
    security_logger.warning(
        f"Security Event: {event_type}",
        extra={"details": details, "timestamp": datetime.now().isoformat()}
    )
```

**Logged Events**:
- Authentication attempts
- Authorization failures
- Invalid input detection
- System errors

### Monitoring

**Key Metrics**:
- Failed authentication rate
- Unusual access patterns
- Resource usage anomalies
- Error rate spikes

**Alerting**:
```yaml
# monitoring/alerts.yaml
alerts:
  - name: high_error_rate
    condition: error_rate > 0.05
    action: email_admin
  
  - name: memory_exhaustion
    condition: memory_usage > 90%
    action: scale_resources
```

## Compliance

### Data Privacy

**GDPR Compliance**:
- Right to access
- Right to deletion
- Data minimization
- Purpose limitation

**Implementation**:
```python
def export_user_data(user_id: str) -> dict:
    """Export all data for GDPR request."""
    return {
        "memories": get_user_memories(user_id),
        "metadata": get_user_metadata(user_id),
        "export_date": datetime.now().isoformat()
    }

def delete_user_data(user_id: str) -> None:
    """Complete data deletion for GDPR."""
    delete_memories(user_id)
    delete_metadata(user_id)
    log_deletion(user_id)
```

### Audit Trail

**Requirements**:
- Immutable logs
- Timestamp accuracy
- User attribution
- Action recording

**Format**:
```json
{
  "timestamp": "2025-06-17T10:30:00Z",
  "user": "user-id",
  "action": "memory_memorize",
  "resource": "brain.fs",
  "result": "success",
  "metadata": {
    "content_hash": "sha256:...",
    "size": 1024
  }
}
```

## Incident Response

### Response Plan

1. **Detection**:
   - Automated monitoring
   - User reports
   - Security scans

2. **Containment**:
   - Isolate affected systems
   - Disable compromised accounts
   - Preserve evidence

3. **Eradication**:
   - Remove threat
   - Patch vulnerabilities
   - Update security measures

4. **Recovery**:
   - Restore services
   - Verify integrity
   - Monitor for recurrence

5. **Lessons Learned**:
   - Document incident
   - Update procedures
   - Share knowledge

### Contact Information

**Security Team**:
- Email: mint-research@neomint.com
- Response Time: 24/7 for critical issues

## Security Checklist

### Development
- [ ] Input validation implemented
- [ ] Authentication required
- [ ] Authorization checked
- [ ] Errors handled securely
- [ ] Secrets not hardcoded
- [ ] Dependencies updated

### Deployment
- [ ] File permissions set
- [ ] Unnecessary ports closed
- [ ] Logging configured
- [ ] Monitoring active
- [ ] Backups tested
- [ ] Incident plan ready

### Regular Reviews
- [ ] Monthly dependency scan
- [ ] Quarterly security audit
- [ ] Annual penetration test
- [ ] Continuous monitoring

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CIS Controls](https://www.cisecurity.org/controls)
- [Security Headers](https://securityheaders.com)

## Updates

This document is reviewed quarterly and updated as needed.

**Last Review**: 2025-06-17  
**Next Review**: 2025-09-17  
**Document Owner**: mint-research@neomint.com