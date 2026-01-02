---
name: intent-analyzer
description: Determine the true user intent, constraints, and success criteria for research tasks with explicit confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Clarify what the user actually needs before executing research work.
- Separate HARD / SOFT / INFERRED constraints and validate them.
- Prepare downstream skills with structured context and explicit ceilings.

### Trigger Conditions
- **Positive:** unclear or under-specified research requests; conflicting goals; prioritization questions.
- **Negative:** clear prompt-optimization tasks (route to `prompt-architect`) or full orchestration (use `deep-research-orchestrator`).

### Guardrails
- Two-pass refinement: (1) capture/structure signals; (2) epistemic check with confidence ceilings.
- Avoid inventing goals; label INFERRED items and request confirmation if possible.
- Maintain structure-first outputs: SKILL + README + examples + references updated when patterns emerge.

### Inputs
- Raw request or prompt snippet.
- Known context (domain, audience, deadlines, format).

### Workflow
1. **Signal Extraction**: Pull verbs, objects, audience, deliverable types, timelines, and exclusions.
2. **Constraint Bucketing**: Sort into HARD / SOFT / INFERRED with evidence/source labels.
3. **Intent Hypothesis**: Draft the likely intent, success criteria, and anti-goals.
4. **Validation Pass**: Check for ambiguity, conflicts, or missing constraints; propose clarifying questions.
5. **Handoff Prep**: Produce a concise brief for downstream skills with confidence ceiling stated.

### Validation & Quality Gates
- INFERRED items explicitly marked and minimized.
- Confidence ceiling included; avoid overclaiming beyond inference/report.
- Output is English-only and structured for reuse.

### Response Template
```
**Intent Hypothesis**
- Primary: ...
- Secondary: ...

**Constraints**
- HARD: ...
- SOFT: ...
- INFERRED (confirm): ...

**Success / Anti-Goals**
- ...

**Clarifying Questions**
- ...

Confidence: 0.76 (ceiling: inference 0.70) - based on parsed request signals.
```

Confidence: 0.76 (ceiling: inference 0.70) - Default after completing the SOP.
