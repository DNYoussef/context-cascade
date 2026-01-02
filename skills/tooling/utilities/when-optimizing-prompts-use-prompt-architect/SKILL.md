---
name: when-optimizing-prompts-use-prompt-architect
description: Route prompt-optimization requests to the prompt-architect skill with explicit constraints and confidence ceilings.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling/utilities
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### STANDARD OPERATING PROCEDURE

Purpose: detect prompt optimization needs and delegate to `prompt-architect` following its SOP (intent → constraints → optimized prompt → confidence ceiling).

**Trigger Conditions**
- Positive: improve/optimize/design/refine prompts; add constraints or success criteria.
- Negative: skill creation or system-level orchestration (route to skill-forge/prompt-forge).

**Execution**
1. Capture original prompt, intent, constraints, and missing context.
2. Call `prompt-architect` with the request and expectation for explicit confidence ceiling.
3. Return optimized prompt, constraints, and evidence.

**Output**
- Optimized prompt, constraint list, and `Confidence: X.XX (ceiling: TYPE Y.YY)`.

Guardrails: keep outputs in English, respect confidence ceilings, and tag memory for reuse.
