---
name: when-auditing-code-style-use-style-audit
description: Route style and linting concerns to the style-audit skill with explicit constraints and evidence.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Ensure style/linting/code-health reviews run through `style-audit` with constraint clarity and confidence ceilings.

### Trigger Conditions
- **Positive:** requests to enforce style guides, linting, readability, or consistency.
- **Negative:** functionality or security issues (use other sub-skills accordingly).

### Guardrails
- Constraints bucketed: HARD (style guide, blockers), SOFT (team preferences), INFERRED (ownership, risk tolerance).
- Two-pass loop: routing/scope → validation of findings with evidence.
- Evidence and ceilings accompany each recommendation.

### Inputs
- Code snippets/path, target style guides, tooling preferences.

### Workflow
1. **Scope & Route**: Confirm style-focused request; record constraints.
2. **Invoke Style-Audit**: Provide code, guides, and preferences.
3. **Validate Findings**: Ensure evidence, severity, and ceilings are present.
4. **Summarize & Store**: Deliver recommendations with owners; archive outputs.

### Validation & Quality Gates
- Routing justified; constraints captured.
- Findings include evidence and severity; ceilings applied.
- Actions/owners assigned.

### Response Template
```
**Routing**: Using style-audit because ...
**Constraints**: HARD / SOFT / INFERRED.
**Findings**: issue → evidence → severity → confidence ceiling.
**Actions**: ...

Confidence: 0.79 (ceiling: inference 0.70) - based on validated style findings.
```

Confidence: 0.79 (ceiling: inference 0.70) - reflects style audit routing with evidence-backed recommendations.
