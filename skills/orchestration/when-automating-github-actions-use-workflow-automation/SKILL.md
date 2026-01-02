---
name: when-automating-github-actions-use-workflow-automation
description: Orchestrate GitHub Actions automation with gated checks, safe rollouts, and evidence-backed validation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Design, update, and validate GitHub Actions workflows with explicit constraints, safety rails, and confidence ceilings on automation changes.

### Trigger Conditions
- **Positive:** new workflow creation, automation refactors, permission tightening, runner/secret updates, rollout validation, failure triage.
- **Negative:** manual one-off runs, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (secrets, runners, approvals), output English-only, and state ceilings.
- **Automation safety:** enforce least privilege, idempotency, rollback toggles, concurrency limits, and registry-only agents; keep hooks within latency budgets.
- **Adversarial validation:** simulate secret loss, permission denial, flaky runners, and rollback; capture evidence.
- **MCP tagging:** log workflow changes under WHO=`workflow-automation-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define automation goal, compliance needs, and approvals; confirm inferred risks.
2. **Workflow design:** map jobs/steps, permissions, caches, and triggers; set concurrency/cancellation rules.
3. **Safety nets:** add dry-runs, rollback flags, and failure notifications; guard secrets and artifacts.
4. **Validation loop:** run tests on branches, simulate failures, measure timing, and record evidence.
5. **Rollout:** stage deployment, monitor, and capture telemetry; prepare rollback.
6. **Delivery:** summarize changes, evidence, risks, and confidence ceiling.

### Output Format
- Automation objective, constraints, and workflow map.
- Permissions/secrets plan, safety toggles, and rollback approach.
- Validation evidence (dry-run, failure drills) and risk register.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests updated or planned.
- Permissions, concurrency, and rollback validated; registry and hooks healthy.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Automation is ready when workflows pass validation, rollback is tested, risks are owned, and MCP logs persist with session tags.

Confidence: 0.70 (ceiling: inference 0.70) - GitHub Actions orchestration reframed with skill-forge scaffolding and prompt-architect confidence discipline.
