---
name: interactive-planner
description: Conduct structured, interactive planning sessions for research tasks with explicit constraints and validated outputs.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Facilitate live planning conversations that convert vague goals into actionable research plans.
- Apply prompt-architect constraint extraction and confidence ceilings to every checkpoint.
- Preserve structure-first artifacts for reuse and auditing.

### Trigger Conditions
- **Positive:** collaborative planning, requirements gathering, research backlog shaping.
- **Negative:** fully scoped tasks ready for execution (use `general-research-workflow`), or prompt-only tuning (`prompt-architect`).

### Guardrails
- Use HARD / SOFT / INFERRED constraint buckets and confirm INFERRED items during the session.
- Two-pass refinement: draft plan → validate against constraints and risks.
- Record decisions, owners, and timelines; keep outputs in English with explicit ceilings.

### Inputs
- Stated goal, timeline, and stakeholders.
- Known constraints (data, compliance, compute) and preferred deliverables.

### Workflow
1. **Session Setup**: State purpose, timebox, and agenda; capture participant roles.
2. **Constraint Capture**: Fill HARD / SOFT / INFERRED lists with sources or owners.
3. **Plan Drafting**: Lay out milestones, owners, dependencies, and validation checkpoints.
4. **Risk & Validation Pass**: Test plan against constraints, edge cases, and evidence needs; adjust accordingly.
5. **Commit & Store**: Finalize plan, record decisions, and save to shared references/examples.

### Validation & Quality Gates
- Constraints confirmed; unresolved INFERRED items have owners.
- Plan includes milestones, validation steps, and communication cadence.
- Confidence ceiling provided with rationale.

### Response Template
```
**Goal & Horizon**
- ...

**Constraints**
- HARD: ...
- SOFT: ...
- INFERRED (confirm): ...

**Plan**
- Milestones, owners, checkpoints.

**Risks / Follow-ups**
- ...

Confidence: 0.79 (ceiling: inference 0.70) - based on collaborative planning outcomes.
```

Confidence: 0.79 (ceiling: inference 0.70) - reflects validated plan with documented constraints.
