# Expertise Manager - Quick Reference v2.1.0

## Purpose
Manages .claude/expertise/ YAML files for domain-specific configurations.

## Expertise File Location

```
.claude/expertise/
  |-- {domain}.yaml         # Domain expertise
  |-- {project-name}.yaml   # Project-specific
  |-- {framework}.yaml      # Framework patterns
  |-- expertise-index.yaml  # Index of all expertise
```

## Operations

| Operation | Command | Result |
|-----------|---------|--------|
| Create | `Create expertise for: {domain}` | New YAML file |
| Update | `Update expertise: {domain}` | Merge changes |
| Query | `Get expertise for: {domain}` | Return config |
| List | `List all expertise` | Index contents |
| Delete | `Remove expertise: {domain}` | Archive & delete |

## Expertise YAML Schema

```yaml
# .claude/expertise/{domain}.yaml
domain: string           # Domain identifier
version: semver          # Schema version
last_updated: ISO8601    # Last modification

file_locations:          # Known file paths
  config: "path/to/config"
  tests: "path/to/tests"

patterns:                # Domain patterns
  naming: "camelCase"
  structure: "layered"

conventions:             # Coding conventions
  imports: "absolute"
  exports: "named"

known_issues:            # Common pitfalls
  - issue: "description"
    solution: "how to fix"

tools:                   # Preferred tools
  linter: "eslint"
  formatter: "prettier"

integrations:            # External systems
  - name: "system"
    endpoint: "url"
```

## Quick Commands

```bash
# Create new expertise
Use expertise-manager to create expertise for: React TypeScript project

# Update existing
Use expertise-manager to update: react-typescript

# Query for loading
Use expertise-manager to get: react-typescript

# Validate expertise
Use expertise-manager to validate: react-typescript
```

## Phase 0 Integration

All skills use expertise in Phase 0:

```yaml
Phase 0: Expertise Loading
  1. Detect domain from task
  2. Check: .claude/expertise/{domain}.yaml
  3. If exists: Load configuration
  4. Apply: Use for informed execution
```

## Expertise Categories

| Category | Use For |
|----------|---------|
| Language | JavaScript, Python, Rust, etc. |
| Framework | React, Next.js, FastAPI, etc. |
| Platform | AWS, GCP, Vercel, etc. |
| Domain | Healthcare, Finance, Gaming, etc. |
| Project | Specific project configurations |

## Index File Format

```yaml
# .claude/expertise/expertise-index.yaml
version: "1.0.0"
last_scan: "2025-01-15T10:00:00Z"

expertise_files:
  - domain: "react-typescript"
    path: "react-typescript.yaml"
    updated: "2025-01-14"

  - domain: "python-fastapi"
    path: "python-fastapi.yaml"
    updated: "2025-01-10"
```

## Validation Rules

| Rule | Check |
|------|-------|
| Schema | Valid YAML structure |
| Required Fields | domain, version present |
| Paths | Referenced files exist |
| Patterns | Valid regex/glob patterns |
| Versions | Valid semver format |

## Usage by Other Skills

Skills that use expertise:
- agent-selector (domain matching)
- code-review-assistant (conventions)
- clarity-linter (patterns)
- cicd-intelligent-recovery (known issues)
- All skills with Phase 0

## Creating Expertise from Codebase

```bash
# Auto-generate expertise
Use expertise-manager to analyze: ./project-root

# Output: .claude/expertise/{detected-domain}.yaml
# Populated with:
#   - File structure patterns
#   - Detected conventions
#   - Tool configurations
#   - Framework signatures
```

## Related Skills

- **agent-selector** - Uses expertise for matching
- **skill-forge** - Creates skills with expertise loading
- **research-driven-planning** - Informs expertise creation
