# Dependencies - Quick Reference v2.1.0

## Purpose
Dependency management, analysis, and vulnerability detection.

## Analysis Types

| Type | Purpose |
|------|---------|
| graph | Visualize dependency tree |
| vulnerabilities | Security scanning |
| outdated | Version freshness |
| circular | Cycle detection |

## Quick Commands

```bash
# Map dependencies
Use dependencies map: [project path]

# Security audit
Use dependencies audit: [project path]

# Check updates
Use dependencies outdated: [project path]
```

## Package Commands

```bash
# JavaScript
npm ls --all
npm audit

# Python
pip list
pip-audit

# Rust
cargo tree
cargo audit
```

## Supported Ecosystems

- npm/yarn (JavaScript)
- pip/poetry (Python)
- cargo (Rust)
- go mod (Go)
- maven/gradle (Java)

## Related Skills

- **security**
- **code-review-assistant**
- **deployment-readiness**
