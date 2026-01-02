# Playbook Architect

Design, refactor, and validate operational playbooks with phased steps, evidence checkpoints, and rollback paths. This readme mirrors the Skill Forge-aligned SKILL.md and highlights quick-start usage.

## Quick Start
```javascript
Skill("playbook-architect")
```
Use when creating a new playbook or tightening an existing one; reroute prompt-only requests to `prompt-architect` or agent design to `agent-creator`/`agent-creation`.

## Core Principles
- **Structure-first**: Define phases with entry/exit criteria, roles, and success metrics before detailing steps.
- **Safety-first**: Include rollback/abort conditions and evidence checkpoints in every phase.
- **Confidence discipline**: State confidence with ceilings (inference/report 0.70; research 0.85; observation/definition 0.95).
- **Validation**: Table-top or dry-run each playbook and record gaps.

## Minimal Playbook Template
```yaml
playbook: <name>
version: 3.2.0
triggers:
  positive: [keywords]
  negative: [reroute conditions]
phases:
  - name: Phase 1
    entry: [signals]
    exit: [evidence]
    roles: [owner, reviewer]
    steps: [ordered actions]
    rollback: [conditions]
success_criteria:
  primary: <measurable outcome>
  evidence: [artifacts to collect]
guardrails:
  always: [requirements]
  never: [anti-patterns]
```

## Cross-Skill Coordination
- Upstream: `prompt-architect` for constraint clarity.
- Downstream: `agent-selector`/`agent-creator` when automation is required; `recursive-improvement` for postmortem tuning.

## Files
- `SKILL.md` – full SOP and completion checklist.
- `README.md` – quick start and template (this file).

Confidence: 0.70 (ceiling: inference 0.70) - README rewritten to match Skill Forge cadence and prompt-architect ceilings.
