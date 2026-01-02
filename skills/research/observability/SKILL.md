---
name: observability
description: Establish observability for research systems, experiments, and data pipelines with guardrails and confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Instrument research workflows (experiments, data pipelines, services) for visibility, debugging, and reproducibility.
- Capture constraints and SLIs/SLOs explicitly; prevent silent failures.
- Maintain structure-first artifacts and clear confidence ceilings for observations.

### Trigger Conditions
- **Positive:** need for telemetry on experiments, metrics tracking, drift detection, or reproducibility dashboards.
- **Negative:** pure analysis without systems impact (use `general-research-workflow`), or production SRE (route to operations skills).

### Guardrails
- Constraint buckets include privacy/compliance, performance budgets, cardinality limits, and ownership.
- Two-pass refinement: instrumentation plan → validation against constraints and data quality.
- Evidence-first reporting: observations use observation ceiling (0.95); inferred impacts use inference ceiling (0.70).

### Inputs
- System or experiment topology; key questions to answer.
- Metrics/SLIs, alert thresholds, and data retention policies.
- Tooling constraints (OpenTelemetry, logging stack, dashboards).

### Workflow
1. **Scope & Constraints**: Define observability goals, HARD/SOFT/INFERRED constraints, and stakeholders.
2. **Instrumentation Plan**: Select signals (logs, metrics, traces), sampling, and tagging strategy; align with budgets.
3. **Implement & Validate**: Configure exporters/collectors, run smoke tests, and verify data quality.
4. **Dashboard & Alerts**: Build views for key workflows; set alert thresholds and runbooks.
5. **Review & Iterate**: Check coverage against goals, refine noisy signals, and document ownership/storage.

### Validation & Quality Gates
- Signals mapped to questions and SLIs; sampling and retention documented.
- Privacy/compliance constraints respected.
- Alert/runbook coverage verified; noise level acceptable.
- Confidence ceilings stated for observations vs. inferences.

### Response Template
```
**Scope & Constraints**
- HARD / SOFT / INFERRED.

**Signals & Plan**
- Metrics/logs/traces + tagging.

**Validation**
- Smoke tests, data quality, alert checks.

**Coverage & Gaps**
- ...

Confidence: 0.84 (ceiling: observation 0.95) - based on validated signals and dashboards.
```

Confidence: 0.84 (ceiling: observation 0.95) - reflects verified telemetry and quality gates.
