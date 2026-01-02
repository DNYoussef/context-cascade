---
name: when-validating-code-works-use-functionality-audit
description: Route functionality validation to the functionality-audit skill with clear constraints and evidence.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Ensure functional correctness checks are executed via `functionality-audit` with explicit constraints and ceilings.

### Trigger Conditions
- **Positive:** validating that code behaves as intended, verifying acceptance criteria, or reproducing issues.
- **Negative:** style-only or deep review concerns (use other sub-skills accordingly).

### Guardrails
- Capture HARD / SOFT / INFERRED constraints (coverage, environments, inputs, latency budgets).
- Two-pass loop: plan tests → validate evidence and ceilings from audit.
- Evidence required for each finding; confidence ceilings applied per observation/inference.

### Inputs
- Code, scenarios, acceptance criteria, environments, and known bugs.

### Workflow
1. **Scope**: Confirm functional validation need; gather constraints and scenarios.
2. **Invoke Functionality-Audit**: Provide inputs, expected behaviors, and environments.
3. **Validate Findings**: Ensure repro steps, evidence, and ceilings accompany results.
4. **Summarize Actions**: Recommend fixes, owners, and deadlines; store outputs.

### Validation & Quality Gates
- Constraints captured; environments noted.
- Findings include repro steps and evidence.
- Confidence ceilings aligned with observation/inference.

### Response Template
```
**Routing**: Using functionality-audit because ...
**Constraints**: HARD / SOFT / INFERRED.
**Findings**: case → result/evidence → severity → confidence ceiling.
**Actions**: remediation + owner.

Confidence: 0.81 (ceiling: observation 0.95) - based on validated functional checks.
```

Confidence: 0.81 (ceiling: observation 0.95) - reflects executed functionality validation with evidence.
