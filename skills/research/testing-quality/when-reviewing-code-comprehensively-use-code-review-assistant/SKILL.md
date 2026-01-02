---
name: when-reviewing-code-comprehensively-use-code-review-assistant
description: Route comprehensive code reviews to the code-review-assistant with explicit constraints and evidence.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Direct comprehensive research code reviews through the `code-review-assistant` workflow with proper constraint capture and ceilings.

### Trigger Conditions
- **Positive:** requests for deep code review, maintainability checks, or defect discovery.
- **Negative:** runtime validation only (use `functionality-audit`) or styling-only feedback (`style-audit`).

### Guardrails
- Constraints bucketed as HARD (security, compliance, blocking defects), SOFT (style prefs), INFERRED (ownership, risk tolerance).
- Two-pass loop: route + scope → epistemic validation of findings.
- Evidence-first reporting with explicit confidence ceilings.

### Inputs
- Codebase path/snippets, context, testing scope, and risk tolerance.

### Workflow
1. **Scope & Route**: Confirm comprehensive review fit; capture constraints.
2. **Invoke Code-Review-Assistant**: Provide context, priorities, and constraints.
3. **Validate Findings**: Ensure evidence, severity, and ceilings accompany each issue.
4. **Summarize & Store**: Deliver consolidated review, risks, and actions; store outputs.

### Validation & Quality Gates
- Routing decision logged; constraints captured.
- Findings include evidence and severity with ceilings.
- Actions assigned with owners/dates.

### Response Template
```
**Routing**: Using code-review-assistant because ...
**Constraints**: HARD / SOFT / INFERRED.
**Key Findings**: issue → evidence → severity → confidence ceiling.
**Actions**: remediation + owner.

Confidence: 0.80 (ceiling: inference 0.70) - based on validated review outputs.
```

Confidence: 0.80 (ceiling: inference 0.70) - reflects routed comprehensive review with evidence-backed findings.
