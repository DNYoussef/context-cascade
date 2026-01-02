# When Auditing Security, Use Security Analyzer

## Purpose
Route security audit requests into the security analyzer workflow with clear scope, safety controls, and evidence expectations. Built with **skill-forge** structure-first discipline and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Intake**: Confirm authorization, assets, goals (assessment vs. remediation), and timelines.
2. **Plan**: Choose static/dynamic/supply-chain checks; define safety controls (isolation, deny-by-default network) and evidence plan.
3. **Execute**: Trigger the security analyzer stack and any downstream specialists (`network-security-setup`, `sandbox-configurator`, `reverse-engineering-*`) as needed.
4. **Validate**: Dual validation for critical/high findings; map to CVE/CWE/OWASP; record confidence ceilings.
5. **Deliver**: Findings + remediation, validation log, and executive summary. Archive at `skills/security/when-auditing-security-use-security-analyzer/{project}/{timestamp}` with MCP tags (`WHO=security-analyzer-{session}`, `WHY=skill-execution`).

## Guardrails
- Authorized scopes only; isolate from production unless approved.
- Evidence required for every claim; no speculative vulnerabilities.
- Confidence ceilings on every statement.

Confidence: 0.70 (ceiling: inference 0.70) - README aligned to the updated audit routing SOP.
