---
name: ai-dev-orchestration
description: Coordinate multi-agent software delivery with guardrails for planning, implementation, testing, and release.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Run full-stack AI-assisted development loops—framing, architecture, implementation, validation, and launch—while keeping confidence ceilings explicit and artifacts auditable.

### Trigger Conditions
- **Positive:** end-to-end feature delivery, AI-assisted coding reviews, test orchestration, release-readiness drills, backlog triage for complex builds.
- **Negative:** single-file edits without coordination, pure prompt engineering (route to prompt-architect), or meta-skill creation (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** ensure `SKILL.md`, `examples/`, and `tests/` exist; stage `resources/` and `references/` or log remediation tasks before completion.
- **Prompt-Architect clarity:** capture HARD/SOFT/INFERRED requirements, user acceptance criteria, and produce pure-English outputs with ceiling-aware confidence.
- **SDLC safety:** enforce branch/CI policy, code review checkpoints, test coverage gates, and rollback/feature-flag plans for risky changes.
- **Adversarial validation:** probe failure modes (flaky tests, dependency drift, latency regressions) and record evidence.
- **MCP tagging:** store orchestration logs under WHO=`ai-dev-orchestration-{session}` and WHY=`skill-execution` for reuse.

### Execution Playbook
1. **Intent & scope:** map goals to release milestones; confirm non-functional targets (latency, reliability, compliance).
2. **Plan & topology:** assign planner, builder, reviewer, and tester agents; define lanes, SLAs, and review cadence.
3. **Build & delegate:** break work into increments, wire hooks to CI, and enforce registry-only agent usage.
4. **Quality gates:** run unit/integration/e2e suites, security/lint checks, and performance baselines with thresholds.
5. **Adversarial loop:** simulate rollback, partial failures, and migration paths; document deltas and evidence.
6. **Delivery:** summarize implemented changes, validation results, residual risk, and next actions with confidence ceiling.

### Output Format
- Release objective, scope, and constraints.
- Role topology (planner/builder/reviewer/tester) with ownership and timelines.
- Delivery plan and checkpoints (CI hooks, review gates).
- Validation evidence (tests, performance, security) and risk log.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale` in pure English.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests updated or planned.
- HARD/SOFT/INFERRED requirements addressed with owners and evidence.
- CI/review gates executed; rollback path documented; hooks within latency budgets.
- Adversarial and COV runs logged with MCP tags; confidence ceiling declared.

### Completion Definition
Feature is deliverable when code, tests, and deployment assets meet acceptance criteria, risks are owned, rollback is ready, and orchestration notes persist in MCP.

Confidence: 0.70 (ceiling: inference 0.70) - SOP reframed with skill-forge structure, prompt-architect constraint handling, and SDLC orchestration guardrails.
