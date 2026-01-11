# Library-to-Skill/Agent Mapping Plan

## Overview

This document maps 82 library components to relevant skills and agents that should reference them.

---

## Library-First Directive Template

### For Agents (Insert at TOP of file, after YAML frontmatter)

```markdown
---

## Library-First Directive

This agent operates under library-first constraints:

1. **Pre-Check Required**: Before writing code, search:
   - `.claude/library/catalog.json` (components)
   - `.claude/docs/inventories/LIBRARY-PATTERNS-GUIDE.md` (patterns)
   - `D:\Projects\*` (existing implementations)

2. **Decision Matrix**:
   | Result | Action |
   |--------|--------|
   | Library >90% | REUSE directly |
   | Library 70-90% | ADAPT minimally |
   | Pattern documented | FOLLOW pattern |
   | In existing project | EXTRACT and adapt |
   | No match | BUILD new |

---
```

### For Skills (Insert after "Purpose" section in SOP)

```markdown
### Library Component References

Before implementing, check these library components:
{component_list}

**Decision Matrix**:
| Match | Action |
|-------|--------|
| >90% | REUSE `from library.{domain} import {Component}` |
| 70-90% | ADAPT with minimal changes |
| Pattern | FOLLOW documented pattern |
| No match | BUILD new (document decision) |
```

---

## Component to Skill/Agent Mapping

### Trading Domain (3 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `circuit-breaker-trading` | `operations/cicd-intelligent-recovery`, `delivery/debugging`, `operations/production-readiness` | `devops-specialist`, `reliability-engineer` |
| `gate-system-manager` | `delivery/sparc-methodology`, `specialists/finance/*` | `quant-analyst`, `risk-manager` |
| `kelly-criterion-calculator` | `specialists/finance/*`, `platforms/machine-learning` | `quant-analyst`, `ml-specialist` |

### Banking/Accounting Domain (4 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `banking-plaid` | `delivery/sop-api-development`, `specialists/finance/*` | `backend-specialist`, `api-specialist` |
| `banking-models` | `delivery/sop-api-development`, `specialists/finance/*` | `db-architect`, `backend-specialist` |
| `accounting-transactions` | `specialists/finance/*` | `quant-analyst`, `data-engineer` |
| `money-handling` | ALL skills touching financial data | ALL agents touching money |

### API Domain (3 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `fastapi-router-template` | `delivery/sop-api-development`, `delivery/api-docs` | `api-specialist`, `backend-specialist` |
| `pydantic-base-models` | `delivery/sop-api-development`, `delivery/api-docs` | `api-specialist`, `backend-specialist` |
| `express-middleware-chain` | `delivery/debugging`, `delivery/sop-api-development` | `backend-specialist`, `security-engineer` |

### Authentication Domain (2 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `jwt-auth-middleware` | `security/compliance`, `delivery/sop-api-development` | `security-engineer`, `backend-specialist` |
| `fastapi-jwt-auth` | `security/compliance`, `delivery/sop-api-development` | `security-engineer`, `backend-specialist` |

### Cognitive Domain (8 components) - HIGHEST PRIORITY

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `skill-base` | `foundry/*` (ALL) | `skill-creator`, `agent-architect` |
| `agent-base` | `foundry/*` (ALL) | `agent-architect`, `skill-creator` |
| `command-base` | `foundry/*` (ALL) | `skill-creator` |
| `playbook-base` | `foundry/*` (ALL) | `agent-architect` |
| `hook-base` | `foundry/*` (ALL), `operations/hooks-automation` | `hook-developer` |
| `script-base` | `foundry/*` (ALL), `operations/*` | `devops-specialist` |
| `verix-parser` | `foundry/cognitive-lensing`, `foundry/prompt-architect` | `prompt-engineer` |
| `cognitive-config` | `foundry/cognitive-lensing` | `prompt-engineer` |

### Analysis Domain (6 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `pattern-matcher` | `quality/*` (ALL), `research/*` | `code-reviewer`, `security-auditor` |
| `scoring-aggregator` | `quality/*` (ALL) | `code-reviewer`, `linter` |
| `violation-factory` | `quality/*` (ALL) | `code-reviewer`, `linter` |
| `statistical-analyzer` | `research/*`, `quality/*` | `researcher`, `statistician` |
| `ast-visitor-base` | `quality/code-review-assistant`, `quality/connascence-quality-gate` | `code-reviewer` |
| `metric-collector` | `quality/*`, `operations/observability/*` | `monitoring-agent` |

### Validation Domain (3 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `spec-validation` | `quality/*`, `delivery/sop-api-development` | `validator`, `reviewer` |
| `skill-validator` | `foundry/skill-forge`, `foundry/skill-builder` | `skill-creator`, `validator` |
| `quality-validator` | `quality/*` (ALL) | `code-reviewer`, `theater-detector` |

### Testing Domain (3 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `pytest-fixtures-base` | `quality/*`, `delivery/debugging` | `tester`, `e2e-tester` |
| `jest-setup-base` | `quality/*`, `delivery/debugging` | `tester`, `e2e-tester` |
| `backtest-harness` | `specialists/finance/*`, `platforms/machine-learning` | `quant-analyst`, `ml-specialist` |

### Observability Domain (3 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `tagging-protocol` | `operations/observability/*`, `platforms/agentdb*` | `monitoring-agent`, `data-engineer` |
| `audit-logging` | `operations/observability/*`, `security/compliance` | `compliance-auditor`, `security-engineer` |
| `opentelemetry-lite` | `operations/observability/*` | `monitoring-agent`, `devops-specialist` |

### UI/Frontend Domain (7 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `radix-dialog-wrapper` | `delivery/landing-page-generator`, `delivery/frontend-specialist` | `frontend-specialist` |
| `radix-dropdown-menu` | `delivery/landing-page-generator`, `delivery/frontend-specialist` | `frontend-specialist` |
| `design-system` | `delivery/landing-page-generator`, `delivery/frontend-specialist` | `frontend-specialist` |
| `kanban-store` | `delivery/frontend-specialist` | `frontend-specialist` |
| `react-hooks` | `delivery/frontend-specialist` | `frontend-specialist` |
| `auth-context` | `delivery/frontend-specialist`, `security/compliance` | `frontend-specialist`, `security-engineer` |
| `fetch-api-client` | `delivery/frontend-specialist`, `delivery/sop-api-development` | `frontend-specialist`, `api-specialist` |

### Orchestration/Pipeline Domain (3 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `content-pipeline-template` | `orchestration/cascade-orchestrator`, `orchestration/stream-chain` | `coordinator`, `swarm-master` |
| `multi-model-router` | `orchestration/llm-council`, `platforms/multi-model` | `coordinator` |
| `pipeline-executor` | `orchestration/*` (ALL) | `coordinator`, `parallel-executor` |

### Utilities Domain (4 components)

| Component ID | Relevant Skills | Relevant Agent Personas |
|--------------|-----------------|-------------------------|
| `quality-gate` | `quality/*` (ALL), `orchestration/*` | `code-reviewer`, `validator` |
| `circuit-breaker` | `operations/*`, `delivery/debugging` | `devops-specialist`, `reliability-engineer` |
| `health-monitor` | `operations/observability/*` | `monitoring-agent` |
| `yaml-safe-write` | `operations/*`, `foundry/*` | `devops-specialist`, `skill-creator` |

---

## Execution Plan

### Phase 1: Update All Agents (260 files)

Run parallel agents to add Library-First Directive to each agent category:
- delivery/ (18 agents)
- quality/ (18 agents)
- research/ (11 agents)
- orchestration/ (21 agents)
- security/ (15 agents)
- platforms/ (12 agents)
- specialists/ (45 agents)
- tooling/ (24 agents)
- foundry/ (18 agents)
- operations/ (29 agents)

### Phase 2: Update All Skills (196 files)

Run parallel agents to insert Library Component References into each skill category:
- delivery/ (20+ skills)
- quality/ (22+ skills)
- research/ (21+ skills)
- orchestration/ (23+ skills)
- security/ (13+ skills)
- platforms/ (18+ skills)
- foundry/ (22+ skills)
- operations/ (23+ skills)
- tooling/ (17+ skills)
- specialists/ (10+ skills)

### Phase 3: Fix Skill Packager Paths

Update skill-packager.py to use correct context-cascade paths.

### Phase 4: Package All Skills

Run `python skill-packager.py --package` to create .skill files.

---

## Template for Skill Library References

### Trading Skills
```markdown
### Library Component References

Before implementing trading functionality, check these components:
- `circuit-breaker-trading` - Six types of trading circuit breakers
- `gate-system-manager` - Capital-based gate system (G0-G12)
- `kelly-criterion-calculator` - Position sizing using Kelly Criterion
- `money-handling` - CRITICAL: Decimal-only currency handling
```

### Quality Skills
```markdown
### Library Component References

Before implementing quality checks, check these components:
- `pattern-matcher` - Generic pattern detection with regex
- `scoring-aggregator` - Weighted score aggregation
- `violation-factory` - SARIF-compatible violation creation
- `quality-validator` - Evidence-based quality validation
- `ast-visitor-base` - Python AST traversal for code analysis
```

### Foundry Skills
```markdown
### Library Component References

Before creating skills/agents/hooks, check these base classes:
- `skill-base` - Abstract base class for skills with lifecycle
- `agent-base` - Abstract base class for agents with Memory MCP
- `command-base` - Abstract base class for slash commands
- `playbook-base` - Abstract base class for playbooks
- `hook-base` - Abstract base class for hooks
- `script-base` - Abstract base class for automation scripts
```

---

## Success Criteria

1. All 260 agents have Library-First Directive at TOP
2. All 196 skills have Library Component References in SOP
3. No existing content is removed - only additions
4. All skills packaged to .skill format in skills/packaged/
5. Packager uses correct context-cascade paths
