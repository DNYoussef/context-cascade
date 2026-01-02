---
name: baseline-replication
description: Run disciplined replication of published or internal baselines with provenance, controls, and validation gates.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: research
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Reproduce baseline experiments faithfully before new development.
- Capture every constraint (data, metrics, hardware, randomness) and document variances.
- Produce artifacts that downstream skills can trust (configs, logs, checkpoints).

### Trigger Conditions
- **Positive:** requests to replicate a paper’s baseline, re-run internal baselines, validate claims prior to extension.
- **Negative:** greenfield method design (use `method-development`), or pure prompt tuning (route to `prompt-architect`).

### Guardrails
- Structure-first delivery: SKILL + README + examples + references; stash configs/resources alongside outputs.
- Constraint extraction in HARD / SOFT / INFERRED buckets with sources (paper, repo, maintainer notes).
- Two-pass refinement: (1) structure and environment parity; (2) epistemic validation and variance explanation.
- Confidence ceilings enforced; never overstate beyond observation/research limits.

### Inputs
- Original specification (paper section, repo, config files).
- Target hardware/software stack and allowed variance.
- Success criteria (metric thresholds, tolerances, reproducibility bounds).

### Workflow
1. **Scope & Constraints**: Capture dataset versions, metrics, seeds, hardware, and tolerances; confirm INFERRED assumptions.
2. **Environment Parity Plan**: Mirror dependencies; document any substitutions and expected impact.
3. **Reproduce Runs**: Execute baseline with fixed seeds; log configs, hashes, and environment fingerprints.
4. **Validate**: Compare against claimed results with statistical checks; explain deviations.
5. **Package Artifacts**: Store configs, logs, checkpoints, and a replication report; update examples/references as needed.

### Validation & Quality Gates
- Environment parity documented; deviations justified.
- Metrics within agreed tolerance or deviation analysis provided.
- Replication report includes evidence, seeds, and reproducibility notes.
- Confidence line item included with appropriate ceiling (observation 0.95, research 0.85).

### Response Template
```
**Constraints**
- HARD: ...
- SOFT: ...
- INFERRED (confirm): ...

**Plan**
- Environment + run strategy.

**Results**
- Metric(s): ... vs. claim ...
- Variance analysis: ...

**Artifacts**
- Configs/logs: <paths>
- Checkpoints: <paths>

Confidence: 0.82 (ceiling: research 0.85) - based on replicated runs and logged evidence.
```

Confidence: 0.82 (ceiling: research 0.85) - Assumes replication gates and evidence checks completed.
