# AI Memory Vault Template

This is a template Obsidian vault structure for use with Memory-MCP.

## Directory Structure

```
AI-Memory-Vault/
  agents/
    findings/     - Issues found by agents
    fixes/        - Applied fixes
    decisions/    - Design decisions
  expertise/
    domains/      - Domain knowledge
    patterns/     - Code patterns
  projects/
    _template/    - Project template
  daily/          - Daily notes (auto-generated)
```

## Setup

1. Copy this folder to your Documents:
   ```bash
   cp -r obsidian-vault-template ~/Documents/AI-Memory-Vault
   ```

2. Open in Obsidian as a new vault

3. Configure Memory-MCP to use this vault:
   ```yaml
   # In memory-mcp-triple-system/config/memory-mcp.yaml
   storage:
     obsidian_vault: ~/Documents/AI-Memory-Vault
   ```

## Tagging Protocol

All memories use WHO/WHEN/PROJECT/WHY tags:

```markdown
---
WHO: code-analyzer:abc123
WHEN: 2025-12-28T15:00:00Z
PROJECT: my-project
WHY: analysis
---

Content here...
```

## Memory Categories

### Findings (`agents/findings/`)
Issues found during code analysis:
- Security vulnerabilities
- Quality violations
- Performance issues

### Fixes (`agents/fixes/`)
Applied solutions:
- Bug fixes
- Refactoring
- Optimizations

### Decisions (`agents/decisions/`)
Design and architecture decisions:
- Technology choices
- Pattern selections
- Trade-off analyses

### Expertise (`expertise/`)
Domain knowledge accumulated:
- Best practices
- Code patterns
- Known issues

### Projects (`projects/`)
Project-specific memories:
- Context for each project
- Progress tracking
- Issue history
