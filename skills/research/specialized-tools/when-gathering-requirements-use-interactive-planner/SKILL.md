---
name: when-gathering-requirements-use-interactive-planner
description: Route requirement-gathering requests to the interactive planner with structured constraints and validated outputs.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Ensure requirement-gathering sessions leverage the `interactive-planner` skill with constraint hygiene and confidence ceilings.
- Provide a lightweight router plus guardrails for research requirement discovery.

### Trigger Conditions
- **Positive:** any request to gather or clarify requirements for research work.
- **Negative:** already-scoped tasks ready for execution (use `general-research-workflow`).

### Guardrails
- Capture HARD / SOFT / INFERRED requirements and confirm ambiguous items.
- Two-pass refinement: routing/structure check then epistemic validation of captured needs.
- Keep outputs English-only with explicit ceilings.

### Inputs
- Raw request describing desired research outcomes.
- Known constraints (timeline, stakeholders, compliance) if provided.

### Workflow
1. **Identify Fit**: Confirm the request is requirement gathering; if not, reroute appropriately.
2. **Constraint Capture**: Bucket requirements into HARD / SOFT / INFERRED; note missing info.
3. **Route to Interactive Planner**: Provide the constraint set, goals, and stakeholders.
4. **Validate Handoff**: Ensure deliverables include plan, risks, and confidence ceiling.
5. **Store Artifacts**: Save brief and planner outputs for traceability.

### Validation & Quality Gates
- Rerouting decision documented; constraints captured with sources.
- Planner outputs include milestones, risks, and ceilings.
- Artifacts stored with tags for recall.

### Response Template
```
**Routing Decision**
- Use interactive-planner because ...

**Requirements (H/S/I)**
- HARD: ...
- SOFT: ...
- INFERRED (confirm): ...

**Handoff Notes**
- Stakeholders, timeline, desired outputs.

Confidence: 0.75 (ceiling: inference 0.70) - based on captured requirements and routing check.
```

Confidence: 0.75 (ceiling: inference 0.70) - reflects validated routing and constraint capture.
