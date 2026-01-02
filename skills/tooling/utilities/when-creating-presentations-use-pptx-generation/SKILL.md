---
name: when-creating-presentations-use-pptx-generation
description: Route presentation requests to the pptx-generation skill with brief capture and validation guardrails.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling/utilities
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### STANDARD OPERATING PROCEDURE

Purpose: detect presentation/deck requests, collect the brief, and invoke `pptx-generation` with the right constraints.

**Trigger Conditions**
- Positive: slide deck, pitch, review, training, or summary presentation requests.
- Negative: non-slide design tasks or written-only docs.

**Execution**
1. Gather brief (audience, goal, brand kit, slide count, deadline).
2. Send to `pptx-generation` with structured brief and validation expectations.
3. Return outline/deck outputs and confidence ceiling.

**Output**
- Brief summary, routed command, expected artifacts, and `Confidence: X.XX (ceiling: TYPE Y.YY)`.

Guardrails: keep brand/accessibility constraints explicit; structure-first docs maintained; memory tagged.
