---
name: compliance
description: Evidence-led regulatory compliance playbook for GDPR, HIPAA, SOC 2, PCI-DSS, and ISO 27001 with auditable outputs.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose & Positioning
Deliver certification-ready compliance assessments and documentation across GDPR, HIPAA, SOC 2, PCI-DSS, and ISO 27001. The skill mirrors **skill-forge** structure-first rules (SKILL + examples/tests/resources) and **prompt-architect** clarity (explicit constraints, confidence ceilings).

## When to Engage / When to Redirect
- **Use when:** preparing for audits, mapping controls to evidence, building remediation plans, or running continuous compliance monitoring.
- **Redirect when:** task is general security triage (route to `security`), sandbox/network setup (use `sandbox-configurator` or `network-security-setup`), or unauthorized third-party reviews.

## Pre-Flight Guardrails
- Operate only with explicit authorization and documented scope.
- Protect PII/PHI with encryption in transit/at rest and least privilege.
- Never fabricate evidence; every claim requires timestamped proof.
- Work in isolated environments; avoid testing on production.
- Respect confidence ceilings: inference/report ≤0.70, research 0.85, observation/definition 0.95.

## Prompt Architecture Overlay
1. Extract constraints into HARD/SOFT/INFERRED with sources; confirm inferred items.
2. Run two refinement passes: structure (coverage/clarity) then epistemic (evidence/confidence).
3. Keep outputs in English with explicit confidence ceiling notation.

## SOP (Compliance Delivery Loop)
1. **Scoping**
   - Identify frameworks in-scope, data types (PII/PHI/PCI), jurisdictions, and system boundaries.
   - Confirm objectives (certification, readiness check, remediation plan).
2. **Control Inventory**
   - Map requirements to existing controls and owners.
   - Capture artifacts to collect (policies, configs, logs, screenshots, pen-test reports).
3. **Evidence Collection**
   - Run automated checks (scanner outputs, config exports) plus manual sampling (≥20%).
   - Tag artifacts with source, timestamp, environment, and reviewer.
4. **Gap Analysis**
   - Rate findings (critical/high/medium/low) with risk rationale and regulatory citation.
   - Draft remediation tasks with owners and due dates.
5. **Validation & COV**
   - Verify fixes via retest; cross-validate via second method (tool + manual).
   - Run adversarial checks for edge cases (multi-tenant data paths, logging gaps).
6. **Delivery**
   - Produce an audit-ready packet: control matrix, evidence log, remediation tracker, and executive summary.
   - Store outputs under `skills/security/compliance/{project}/{timestamp}` with MCP tags (`WHO=compliance-{session}`, `WHY=skill-execution`).

## Deliverables
- Control/evidence matrix with framework mapping.
- Findings report (severity + proof), remediation backlog, and retest status.
- Audit artifacts bundle (policies, configs, screenshots/logs with hashes).
- Executive summary with residual risk and next steps.

## Quality Gates
- Structure-first: SKILL.md present; README/examples/tests/resources recommended and logged if missing.
- Evidence completeness ≥90% for scoped controls; no critical gaps open at delivery.
- Dual validation on critical/high findings; explicit confidence ceiling on every claim.
- MCP logging applied; completion checklist signed (scope, evidence, validation, delivery).

## Anti-Patterns to Avoid
- Scanning or testing without authorization.
- Mixing production data into test artifacts.
- Confidence inflation or missing ceilings.
- Unmapped controls (no requirement → control → evidence chain).

## Output Format
- Summary of scope and frameworks.
- Constraints table (HARD/SOFT/INFERRED + confirmations).
- Control/evidence highlights and remediation queue.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.72 (ceiling: inference 0.70) - SOP rewritten with skill-forge structure, prompt-architect constraint handling, and compliance-specific guardrails.
