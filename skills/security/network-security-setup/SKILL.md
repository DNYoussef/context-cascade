---
name: network-security-setup
description: Network isolation, allow/deny policy design, and TLS posture for sandboxes and CI with auditable enforcement.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Design and deploy defense-in-depth network controls (deny-by-default, trusted domain allowlists, TLS hardening, monitoring) for sandboxes and pipelines. Applies **skill-forge** structure-first requirements and **prompt-architect** explicit constraints/confidence ceilings.

## Use When / Redirect When
- **Use when:** locking down egress/ingress, configuring proxies, setting TLS baselines, or verifying network controls before development tasks.
- **Redirect when:** sandbox policy authoring (`sandbox-configurator`) or general security triage (`security`).

## Guardrails
- Enforce authorized scopes; never run active scans against unknown targets.
- Default to deny-all with explicit allowlists; keep change log and approvals.
- Protect credentials and certificates; rotate and store securely.
- Confidence ceilings: inference/report ≤0.70, research 0.85, observation/definition 0.95.

## Prompt Architecture Overlay
1. HARD/SOFT/INFERRED constraints with sources (targets, allowed domains, proxy rules, TLS requirements).
2. Two-pass refinement: structure (coverage + routing) then epistemic (evidence + ceilings).
3. English-only outputs with explicit confidence line.

## SOP (Network Hardening Loop)
1. **Scope & Inputs**
   - Define environment (sandbox/CI/prod-like), trust zones, proxy requirements, and approved destinations.
   - Inventory credentials/certs and designate storage/rotation approach.
2. **Design**
   - Choose isolation mode (offline, trusted allowlist, custom).
   - Draft firewall rules, egress controls, DNS policy, and TLS posture (min version, ciphers, OCSP/HSTS).
3. **Implementation**
   - Apply scripts/templates (firewall, proxy, SSL setup) with change logging.
   - Generate certificates as needed; install to trust stores.
4. **Validation**
   - Connectivity tests for allowed targets; ensure blocked paths fail.
   - Run compliance checks (NIST/CIS baseline), certificate validation, and regression tests for existing services.
5. **Monitoring & Handoff**
   - Configure logging/metrics (allowed vs blocked, cert expiry, proxy health).
   - Deliver runbook, rule set, and rollback steps; store artifacts at `skills/security/network-security-setup/{project}/{timestamp}` with MCP tags (`WHO=network-security-setup-{session}`, `WHY=skill-execution`).

## Deliverables
- Network policy pack (allowlist/deny rules, proxy settings, DNS policy).
- TLS profile (min versions, ciphers, renewal plan) and certificate bundle.
- Validation log (tests executed, results, regressions, evidence).
- Runbook covering operations, rollbacks, and monitoring hooks.

## Quality Gates
- Structure-first documentation present; missing resources/examples/tests are logged.
- Deny-by-default enforced; no unapproved domains/IPs.
- Validation covers connectivity, block testing, TLS checks, and logging.
- Evidence attached with confidence ceiling per claim.

## Anti-Patterns
- Allowing “*” domains or bypassing controls for convenience.
- Running scans without scoping/approval.
- Leaving certificates untracked or without rotation dates.
- Omitting rollback steps or monitoring hooks.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- Final rule set and TLS profile with evidence of enforcement.
- Validation summary and runbook pointers.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.72 (ceiling: inference 0.70) - SOP rewritten with skill-forge structure, prompt-architect constraint handling, and network hardening guardrails.
