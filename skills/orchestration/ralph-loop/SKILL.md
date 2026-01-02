---
name: ralph-loop
description: Run Ralph-style iterative loops for reasoning, alignment, learning, planning, and handoff with strong evidence discipline.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Coordinate the RALPH sequence (Reason, Align, Learn, Plan, Handoff) with explicit constraints, validation, and confidence ceilings.

### Trigger Conditions
- **Positive:** structured iterative problem solving, alignment checkpoints, learning/reflection loops, plan-to-action handoffs.
- **Negative:** ad-hoc single-pass answers, prompt-only edits (route to prompt-architect), or new skill weaving (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** ensure `SKILL.md`, `examples/`, `tests/` exist; add `resources/`/`references/` or log remediation.
- **Prompt-Architect hygiene:** extract HARD/SOFT/INFERRED constraints at each phase, maintain pure English, and state confidence with ceilings.
- **Loop safety:** enforce phase boundaries, timeboxes, and evidence requirements; use registry agents only; keep hooks within latency budgets.
- **Adversarial validation:** run COV after each iteration, probe wrong-turn scenarios, and capture evidence.
- **MCP tagging:** save loop traces with WHO=`ralph-loop-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Reason:** clarify the problem, constraints, and gaps; confirm inferred assumptions.
2. **Align:** align stakeholders/agents on goals, guardrails, and success metrics.
3. **Learn:** gather evidence, test hypotheses, and record findings.
4. **Plan:** map actions with owners, timelines, and rollback checkpoints.
5. **Handoff:** delegate tasks, verify readiness, and monitor execution.
6. **Validation:** run adversarial checks, measure outcomes vs metrics, and log telemetry.
7. **Delivery:** present outcomes, evidence, residual risks, and confidence ceiling.

### Output Format
- Phase-by-phase summary (R, A, L, P, H) with constraints and decisions.
- Evidence log, risks, and open questions.
- Handoff plan with owners and checkpoints.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect RALPH flow.
- Phase gates respected; registry and hook budgets validated; rollback paths ready.
- Adversarial/COV runs logged with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Loop is complete when handoff executes against the plan, evidence confirms outcomes, risks are owned, and logs persist with MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - RALPH loop documentation aligned to skill-forge scaffolding and prompt-architect clarity with explicit evidence and ceilings.
