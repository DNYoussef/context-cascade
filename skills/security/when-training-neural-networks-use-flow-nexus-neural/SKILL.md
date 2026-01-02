---
name: when-training-neural-networks-use-flow-nexus-neural
description: Routing and safety skill for neural network training that enforces secure sandboxing, data governance, and Flow Nexus neural workflows.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Ensure ML training requests invoke the Flow Nexus neural pipeline with proper security, compliance, and sandbox controls. Applies **skill-forge** structure-first requirements and **prompt-architect** constraint/confidence rules.

## Use When / Redirect When
- **Use when:** a user requests neural network training, fine-tuning, or data prep and needs secure routing to Flow Nexus neural tooling.
- **Redirect when:** general security triage (`security`) or sandbox/network policy setup (`sandbox-configurator`, `network-security-setup`).

## Guardrails
- Require explicit authorization and data handling policy (PII/PHI/licensing).
- Enforce sandbox isolation and network allowlists; prefer offline/controlled data ingress.
- Verify dataset provenance and license; avoid unapproved external uploads.
- Confidence ceilings enforced (inference/report ≤0.70, research 0.85, observation/definition 0.95).

## Prompt Architecture Overlay
1. HARD/SOFT/INFERRED constraints (task type, model family, data sensitivity, infra, timelines).
2. Two-pass refinement: structure (routing, coverage) then epistemic (evidence, ceilings).
3. English-only outputs with explicit confidence line.

## SOP (Flow Nexus Neural Routing)
1. **Intake & Safety**
   - Confirm authorization, data classifications, and allowed environments.
   - Choose sandbox + network profile; tag MCP (`WHO=flow-nexus-neural-{session}`, `WHY=skill-execution`).
2. **Plan**
   - Select Flow Nexus neural workflow (training/fine-tune/eval), resource needs, and checkpoints.
   - Define data ingress/egress controls, encryption, and retention.
3. **Execute**
   - Invoke Flow Nexus neural pipeline; monitor resource use and compliance gates.
4. **Validate**
   - Verify training logs, metrics, and guardrails (no PII leakage, license compliance).
   - Run adversarial/safety evaluations as applicable.
5. **Deliver**
   - Provide run summary, model artifacts/locations, evaluation metrics, and risks; archive under `skills/security/when-training-neural-networks-use-flow-nexus-neural/{project}/{timestamp}`.

## Deliverables
- Training plan and safety controls.
- Execution log with metrics and checkpoints.
- Evaluation results and risk summary with mitigation steps.

## Quality Gates
- Structure-first documentation; missing resources/examples/tests noted.
- Data governance verified (provenance, licensing, PII/PHI handling).
- Evidence + confidence ceiling for every claim; safety evals recorded.

## Anti-Patterns
- Using unvetted datasets or licenses.
- Training in non-isolated environments with unrestricted egress.
- Skipping safety/adversarial evaluations.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- Plan, executed steps, metrics, and safety checks.
- Risks, mitigations, and artifact locations.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.72 (ceiling: inference 0.70) - Flow Nexus neural routing aligned with skill-forge and prompt-architect standards.
