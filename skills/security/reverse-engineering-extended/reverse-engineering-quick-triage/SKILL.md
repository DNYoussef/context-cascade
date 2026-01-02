---
name: reverse-engineering-quick-triage
description: Extended quick triage for rapid IOC and capability extraction with stricter timeboxes and safety rails.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Deliver rapid IOC/capability summaries under strict time/effort constraints while preserving evidence quality. Adheres to **skill-forge** structure-first and **prompt-architect** constraint/confidence rules.

## Use When / Redirect When
- **Use when:** urgent containment decisions need quick evidence-backed signals.
- **Redirect when:** deeper behavior/exploitability required (`reverse-engineering-deep-analysis`) or firmware-specific tasks (`reverse-engineering-firmware-analysis`).

## Guardrails
- Isolation required; no external uploads without approval.
- Keep execution minimal; prefer static methods and controlled emulation.
- Confidence ceilings enforced (inference/report ≤0.70, research 0.85, observation/definition 0.95).

## Prompt Architecture Overlay
1. HARD/SOFT/INFERRED constraints (time budget, tooling, outputs needed, risk tolerance).
2. Two-pass refinement (structure → epistemic).
3. English-only output with explicit confidence line.

## SOP (Extended Quick Loop)
1. **Scope & Safety**: Authorize sample, hash it, and pin time budget; isolate environment and network.
2. **Static Pass**: Identify format/arch, packers, strings/URLs, signatures, and entropy/section anomalies.
3. **Controlled Dynamic (optional)**: Emulate/sandbox with strict egress blocks; capture minimal process/file/network events.
4. **Synthesize**: Build IOC list and capability summary; flag uncertainties and escalation needs.
5. **Deliver**: Provide containment recommendations and evidence; archive to `skills/security/reverse-engineering-extended/reverse-engineering-quick-triage/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-quick-triage-{session}`, `WHY=skill-execution`).

## Deliverables
- IOC/capability summary with sources and timestamps.
- Risk assessment and containment actions.
- Evidence bundle (tool outputs/logs).

## Quality Gates
- Structure-first documentation; missing resources/examples/tests tracked.
- Timebox adhered to; uncertainties and gaps noted.
- Evidence per claim with confidence ceiling.

## Anti-Patterns
- Running outside isolation or with unrestricted egress.
- Reporting IOCs without source/evidence.
- Over-claiming beyond timebox evidence.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- IOC/capability summary with evidence.
- Containment recommendations and gaps/escalations.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.71 (ceiling: inference 0.70) - Extended quick triage aligned with skill-forge and prompt-architect standards.
