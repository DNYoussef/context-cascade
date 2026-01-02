# Security Quick Reference v3.2.0

## Purpose
Fast reminders for operating the security hub with **skill-forge** structure-first rules and **prompt-architect** constraint/confidence discipline.

## Routing
- Reverse engineering → `reverse-engineering-quick` / `-deep` / `-firmware`.
- Sandbox hardening → `sandbox-configurator`.
- Network lockdown → `network-security-setup`.
- Compliance → `compliance`.

## Guardrails
- Authorized scope only; isolate from production unless approved.
- Evidence required for every claim; attach confidence ceilings (inference/report ≤0.70, research 0.85, observation/definition 0.95).
- Deny-by-default network posture; protect secrets.

## Core Steps
1. Scope assets, objectives, and constraints (HARD/SOFT/INFERRED).
2. Run two-pass refinement (structure → epistemic).
3. Analyze (static/dynamic/supply-chain) with evidence capture.
4. Validate (dual validation on critical/high); map to CVE/CWE/OWASP.
5. Deliver findings, remediation plan, validation log, and confidence line.

## Finding Template
```
- Title / severity (CVSS vector)
- Location (file:line/service)
- Evidence (PoC/log/config)
- Root cause vs. derived issue
- Remediation + verification steps
- Confidence: X.XX (ceiling: TYPE Y.YY) - reason
```

## MCP Paths
- Store artifacts under `skills/security/security/{project}/{timestamp}` with tags `WHO=security-{session}`, `WHY=skill-execution`.

Confidence: 0.71 (ceiling: inference 0.70) - Quick reference synchronized with the updated security SOP.
