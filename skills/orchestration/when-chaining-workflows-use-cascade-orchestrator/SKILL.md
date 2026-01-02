---
name: when-chaining-workflows-use-cascade-orchestrator
description: Apply cascade-orchestrator patterns to chained workflows with gated handoffs and rollback-aware routing.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Design linked workflows that pass artifacts across stages, enforce entry/exit gates, and keep evidence plus confidence ceilings explicit.

### Trigger Conditions
- **Positive:** multi-stage pipelines, dependent steps, sequential rollouts, artifact handoffs, staged approvals.
- **Negative:** single-step tasks, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** document intent and HARD/SOFT/INFERRED constraints per stage, keep English-only outputs, and state ceilings.
- **Stage safety:** define gates, retries, and rollback/skip logic; enforce registry use and hook latency budgets.
- **Adversarial validation:** test partial failures, artifact integrity, and out-of-order execution; capture evidence.
- **MCP tagging:** store chain runs under WHO=`cascade-workflows-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** capture objectives, ordering, and dependencies; confirm inferred assumptions.
2. **Stage design:** map stages with owners, inputs/outputs, gates, and timers.
3. **Routing & safety:** set retries/backoff, rollback/skip rules, and escalation paths; guard shared state.
4. **Validation loop:** run dry-runs and failure drills; verify artifact integrity and timing.
5. **Delivery:** present chain map, gate outcomes, risks, and confidence ceiling.

### Output Format
- Workflow map with stages, gates, and dependencies.
- Constraint matrix and risk register.
- Validation evidence (dry-run, failure drills) and telemetry.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect chained workflow.
- Gates and rollback/skip rules validated; registry and hooks within budgets.
- Adversarial/COV runs logged with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Chain is ready when stages meet gate criteria, artifacts are verified, risks are owned, and logs persist with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Chained workflow doc aligned to skill-forge scaffolding and prompt-architect constraint/confidence discipline.
