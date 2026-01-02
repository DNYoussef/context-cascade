---
name: ralph-multimodel
description: Extend RALPH loops across multiple models, coordinating roles, evidence, and confidence ceilings per model.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Run multi-model RALPH flows that leverage specialized agents for reasoning, alignment, learning, planning, and handoff with controlled synthesis.

### Trigger Conditions
- **Positive:** problems needing diverse model strengths, cross-model validation, parallel evidence gathering, and adjudicated synthesis.
- **Negative:** single-model work, prompt-only edits (route to prompt-architect), or new skill creation (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` current; add `resources/`/`references/` or note gaps.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints per model/phase, avoid VCL leakage, and publish ceilings for confidence.
- **Multi-model safety:** assign roles, enforce registry usage, prevent uncontrolled self-calls, and keep hook latency within budget.
- **Adversarial validation:** run cross-model disagreement checks, COV per synthesis, and boundary tests; document evidence.
- **MCP tagging:** store runs with WHO=`ralph-multimodel-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & roster:** define objective, select models/roles, and confirm constraints.
2. **Phase wiring:** map RALPH phases to models, timeboxes, and success metrics.
3. **Deliberation:** gather model outputs, run challenges, and update shared evidence.
4. **Synthesis:** reconcile disagreements, choose outputs, and plan handoff with rollback paths.
5. **Validation loop:** stress-test synthesis, measure performance, and log telemetry.
6. **Delivery:** share decisions, evidence, risks, and confidence ceiling.

### Output Format
- Objective, constraints, and model roster with roles.
- Phase summaries, evidence, and dissent.
- Handoff/rollback plan and risk register.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests reflect multi-model paths.
- Role boundaries enforced; registry-only agents used; hook budgets verified; rollback ready.
- Adversarial/COV runs logged with MCP tags; confidence ceiling stated; English-only output.

### Completion Definition
Flow is complete when synthesis is chosen with evidence, handoff executes, risks are owned, and logs persist in MCP with session tags.

Confidence: 0.70 (ceiling: inference 0.70) - Multi-model RALPH doc aligned to skill-forge scaffolding and prompt-architect evidence/confidence discipline.
