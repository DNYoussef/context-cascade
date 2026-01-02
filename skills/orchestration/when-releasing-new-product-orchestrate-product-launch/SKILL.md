---
name: when-releasing-new-product-orchestrate-product-launch
description: Orchestrate product launches with staged readiness checks, risk controls, and validated rollouts.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Coordinate cross-functional product launches—from GTM to engineering readiness—using gated milestones, evidence-backed signoffs, and explicit confidence ceilings.

### Trigger Conditions
- **Positive:** launch planning, release readiness reviews, staged rollouts, incident playbooks, cross-team alignment, success metric tracking.
- **Negative:** minor content updates, prompt-only edits (route to prompt-architect), or meta-skill creation (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** keep `SKILL.md`, `examples/`, `tests/` current; add `resources/`/`references/` or log remediation tasks.
- **Prompt-Architect hygiene:** capture HARD/SOFT/INFERRED constraints (dates, channels, compliance), maintain English-only outputs, and state ceilings.
- **Launch safety:** define go/no-go criteria, rollback/canary plans, comms templates, and owner assignments; enforce registry use and hook budgets.
- **Adversarial validation:** run readiness drills, rollback tests, and scenario planning for failure modes; capture evidence.
- **MCP tagging:** store launch logs under WHO=`product-launch-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & constraints:** define launch goals, dates, channels, and SLAs; confirm inferred requirements.
2. **Plan & roles:** create milestone map with owners, dependencies, and signoff criteria.
3. **Risk & safety:** document risks, mitigation, rollback, and comms; set monitoring.
4. **Validation loop:** run dry-runs, load/ops readiness, and incident drills; log evidence.
5. **Rollout:** stage release, monitor metrics, and adjust; keep rollback ready.
6. **Delivery:** provide status, evidence, residual risks, and confidence ceiling.

### Output Format
- Launch brief with goals, constraints, and milestones.
- Owner map, risk register, and rollback/comms plans.
- Validation evidence (drills, readiness checks) and open issues.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or ticketed; examples/tests align to launch scenarios.
- Go/no-go criteria set; rollback/comms ready; registry and hooks validated.
- Adversarial/COV runs stored with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Launch is ready when milestones are met, risks are owned with mitigations, validation evidence is stored, and rollback/comms plans are in place with MCP logs.

Confidence: 0.70 (ceiling: inference 0.70) - Product launch orchestration rewritten with skill-forge scaffolding and prompt-architect evidence/confidence guardrails.
