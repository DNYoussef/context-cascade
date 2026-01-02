# Security Skill Hub

## Purpose
Central coordinator for security work: evidence-backed reviews, vulnerability triage, remediation planning, and routing to specialized skills (reverse engineering, sandbox hardening, network isolation, compliance). Built with **skill-forge** structure-first discipline and **prompt-architect** constraint/clarity rules.

## Quick Start
1. **Scope**: Define assets, authorization, objectives (review/triage/fix), and applicable frameworks (OWASP/CWE/CVSS).
2. **Collect Signals**: Pull prior findings from MCP (`skills/security/security/{project}/{timestamp}`), enumerate entry points, and gather configs/logs.
3. **Analyze**: Perform static review (authz/authn/crypto/secrets/input handling), supply-chain checks, and authorized dynamic probes.
4. **Document**: For each finding capture location, CVE/CWE, PoC evidence, severity, and root cause vs. derived issues.
5. **Validate & Deliver**: Retest fixes (dual validation on critical/high), summarize residual risk, and log artifacts with MCP tags (`WHO=security-{session}`, `WHY=skill-execution`).

## Guardrails
- Authorized scopes only; isolate from production unless approved.
- Every claim includes evidence and an explicit confidence ceiling.
- Default to least privilege, encrypted secrets, and secure logging.
- Route to specialist skills when work exceeds core review/remediation.

## Outputs
- Findings register + remediation backlog with owners/ETAs.
- Evidence bundle (PoC/logs/configs) with timestamps and hashes.
- Executive summary with threat model coverage and residual risk.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.71 (ceiling: inference 0.70) - README aligned to the updated security SOP and prompt-architect constraint discipline.
