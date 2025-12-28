---
name: codex-zdr
description: Zero Data Retention mode for sensitive/proprietary code - no code stored on OpenAI servers
allowed-tools: Bash, Read, Write, TodoWrite
---

# Codex Zero Data Retention (ZDR) Skill

## Purpose

Execute Codex with Zero Data Retention for sensitive, proprietary, or regulated code where no data should be stored on OpenAI servers.

## Unique Capability

**What This Provides**:
- **No code retention**: Code not stored on OpenAI servers
- **Privacy-first**: GDPR, HIPAA compatible
- **Regulated industries**: Suitable for healthcare, finance
- **Proprietary code**: Safe for trade secrets

## When to Use

### Perfect For:
- Medical/healthcare code (HIPAA)
- Financial systems (PCI-DSS)
- Proprietary algorithms
- Trade secrets
- Government contracts
- Client code under NDA

### Trade-offs:
- Slightly slower (no caching)
- Same functionality otherwise

## Usage

```bash
# ZDR for sensitive code
/codex-zdr "Implement medical record encryption"

# ZDR with full-auto
/codex-zdr "Build payment processing module" --full-auto

# ZDR with sandbox
/codex-zdr "Audit financial calculations" --sandbox
```

## CLI Command

```bash
codex --zdr "Your sensitive task"

# Combined with full-auto
codex --full-auto --zdr "Build and test"

# Via script
CODEX_MODE=zdr bash scripts/multi-model/codex-yolo.sh "Task" "id" "." "5" "zdr"
```

## Compliance Notes

| Regulation | ZDR Suitability |
|------------|-----------------|
| GDPR | Compliant |
| HIPAA | Compliant |
| PCI-DSS | Suitable |
| SOC 2 | Suitable |
| FedRAMP | Check specifics |

## Memory Integration

- Key: `multi-model/codex/zdr/{task_id}`
- Note: Only metadata stored locally, no code in memory
