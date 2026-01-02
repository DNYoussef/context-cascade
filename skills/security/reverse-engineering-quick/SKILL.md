---
name: reverse-engineering-quick
description: Fast IOC-focused triage for binaries/documents with minimal execution, geared toward immediate containment decisions.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Extract IOCs and risk signals within tight timeboxes to enable allow/deny/contain decisions. Leverages **skill-forge** structure-first expectations and **prompt-architect** explicit constraints and confidence ceilings.

## Use When / Redirect When
- **Use when:** you need hashes, strings, metadata, and high-level behavior quickly.
- **Redirect when:** deeper behavior analysis (`reverse-engineering-deep`), firmware (`reverse-engineering-firmware`), or broad security triage (`security`).

## Guardrails
- Hash before handling; isolate from production networks.
- Avoid full execution unless explicitly approved; prefer static extraction.
- Do not upload samples externally without consent.
- Confidence ceilings enforced (inference/report ≤0.70, research 0.85, observation/definition 0.95).

## Prompt Architecture Overlay
1. Define HARD/SOFT/INFERRED constraints (time budget, tool allowlist, sample type, desired outputs).
2. Two-pass refinement (structure → epistemic) to ensure coverage and evidence.
3. Output in English with explicit confidence line.

## SOP (Quick IOC Loop)
1. **Scope & Setup**: Confirm authorization, compute hashes, stage in isolated workspace.
2. **Static Extraction**: File type detection, metadata, entropy/section checks, strings/URLs, YARA signatures.
3. **Safe Peek Execution (optional)**: Sandbox/emulation with strict egress controls; capture basic process/file/network events.
4. **IOC Consolidation**: Normalize hashes, domains/IPs, file paths, mutexes, and persistence hints.
5. **Validation & Delivery**: Cross-check findings across tools, note gaps, and archive outputs to `skills/security/reverse-engineering-quick/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-quick-{session}`, `WHY=skill-execution`).

## Deliverables
- IOC pack (hashes, domains/IPs, paths, signatures) with sources.
- Risk summary and recommended containment actions.
- Evidence bundle (tool outputs, logs) with timestamps.

## Quality Gates
- Structure-first documentation; missing resources/examples/tests captured for backlog.
- Evidence attached to each IOC; confidence ceiling stated.
- Safety controls verified (isolation, blocked network).
- Timebox honored; escalation path documented if more depth required.

## Anti-Patterns
- Executing with unrestricted network.
- Reporting IOCs without source/evidence.
- Exceeding confidence ceilings.
- Skipping escalation when signals are ambiguous.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- IOC list with evidence and source tools.
- Risk summary and next-step recommendations.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.71 (ceiling: inference 0.70) - Quick triage rebuilt with skill-forge structure and prompt-architect constraint handling.
