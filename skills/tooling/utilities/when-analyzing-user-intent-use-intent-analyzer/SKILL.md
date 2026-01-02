---
name: when-analyzing-user-intent-use-intent-analyzer
description: Route intent analysis requests to the intent-analyzer skill with explicit constraints, confidence ceilings, and delivery format.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling/utilities
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### STANDARD OPERATING PROCEDURE

Purpose: detect when the user needs intent analysis and invoke `intent-analyzer` with Prompt Architect clarity.

**Trigger Conditions**
- Positive: ambiguous requests needing classification/constraints, routing decisions, or task decomposition.
- Negative: concrete tasks with clear outputs; route directly to relevant skill.

**Execution**
1. Capture raw request and context.
2. Send to `intent-analyzer` with constraints, success criteria, and confidence ceiling expectations.
3. Return summarized intent, constraints, and recommended skill route.

**Output**
- Intent summary, constraints, recommended skill, and `Confidence: X.XX (ceiling: TYPE Y.YY)`.

Guardrails: structure-first docs maintained; no hallucinated routes; memory tagging for traceability.
