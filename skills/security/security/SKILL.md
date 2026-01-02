---
name: security
description: Central hub for secure design, vulnerability assessment, and remediation routing across the security skill group.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose & Role
Serve as the entry point for security work, orchestrating assessments, secure coding guidance, and routing to specialized skills (reverse engineering, sandbox configuration, network lockdown, compliance). Mirrors **skill-forge** structure-first discipline and **prompt-architect** clarity/constraint extraction.

## Use When / Redirect When
- **Use when:** performing secure code reviews, prioritizing vulnerabilities, designing mitigations, or coordinating security tasks across the stack.
- **Redirect when:** network/sandbox setup (`network-security-setup`, `sandbox-configurator`), reverse engineering (`reverse-engineering-*`), or compliance certifications (`compliance`).

## Guardrails
- Work only on authorized assets; never test production without change control.
- Require evidence for every finding (PoC/log/location/severity); no speculative claims.
- Default to least privilege and encryption for secrets, credentials, and keys.
- Respect confidence ceilings (inference/report ≤0.70, research 0.85, observation/definition 0.95) and state them explicitly.

## Prompt Architecture Overlay
1. Capture constraints as HARD/SOFT/INFERRED with sources; confirm inferred items.
2. Run two passes: structure (coverage, clarity, routing) then epistemic (evidence, ceilings).
3. Output in English with an explicit confidence line.

## SOP (Security Delivery Loop)
1. **Intake & Scoping**
   - Identify assets, threat model, frameworks (OWASP/CWE/CVSS), and goals (review, triage, remediation).
   - Choose downstream specialists or MCP tools as needed.
2. **Baseline & Recon**
   - Load prior findings/patterns from MCP (`skills/security/security/{project}/{timestamp}`).
   - Enumerate entry points (auth, data flows, dependencies, infra endpoints).
3. **Analysis**
   - Static review: insecure patterns, authz/authn gaps, crypto misuse, secrets exposure.
   - Dynamic/DAST (if authorized): controlled tests with evidence capture.
   - Supply chain: dependency/CVE/typosquat review.
4. **Findings & Morphology**
   - Document each finding with location, CVE/CWE mapping, PoC, severity, and root-cause decomposition (root vs. derived issues).
   - Provide least-effort, highest-impact fixes first.
5. **Validation**
   - Retest fixes; require dual validation for critical/high issues (tool + manual).
   - Apply adversarial checks (bypass attempts, authz edge cases, rate limits).
6. **Delivery**
   - Ship prioritized remediation backlog, evidence bundle, and executive summary.
   - Log artifacts with MCP tags (`WHO=security-{session}`, `WHY=skill-execution`).

## Deliverables
- Findings register with CVE/CWE map, PoC evidence, severity, and root cause.
- Remediation plan (owners, effort, ETA) and verification steps.
- Risk summary with threat model coverage and residual risk.
- Changelog of scope, tools used, and validation outcomes.

## Quality Gates
- Structure-first: SKILL.md present; README/examples/tests/resources tracked and added when available.
- Every claim has evidence + confidence ceiling; no critical items without PoC.
- Coverage: authz/authn, data protection, input handling, logging/monitoring, supply chain.
- MCP logging applied; completion checklist signed (scope, analysis, validation, delivery).

## Anti-Patterns
- Running active tests without approval or isolation.
- Confidence inflation or missing ceilings.
- Listing vulnerabilities without remediation or root-cause analysis.
- Ignoring downstream routing to specialists when needed.

## Output Format
- Scope summary and constraints table (HARD/SOFT/INFERRED).
- Findings list with evidence, severity, and root cause/remediation.
- Validation log and residual risk.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.73 (ceiling: inference 0.70) - Security hub rewritten with skill-forge structure, prompt-architect constraint handling, and evidence-first guardrails.
