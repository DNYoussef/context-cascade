---
name: when-optimizing-agent-learning-use-reasoningbank-intelligence
description: Route agent-learning optimization requests to the reasoningbank-intelligence skill with clear constraints and validation gates.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: tooling/utilities
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### STANDARD OPERATING PROCEDURE

Purpose: detect when agent-learning improvements are needed and delegate to `reasoningbank-intelligence` with the right context.

**Trigger Conditions**
- Positive: requests to enhance agent learning, retrieval quality, or training signals.
- Negative: non-learning tasks or single prompt tweaks.

**Execution**
1. Capture target agent, goals (accuracy, latency, coverage), datasets, and constraints.
2. Invoke `reasoningbank-intelligence` with context and required validation (evals, telemetry).
3. Return plan/results and `Confidence: X.XX (ceiling: TYPE Y.YY)`.

Guardrails: structure-first docs maintained; avoid overpromising without data; tag memory for traceability.
