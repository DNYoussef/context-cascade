# Network Security Setup

## Purpose
Enforce deny-by-default network controls, explicit allowlists, and TLS posture for sandboxes and CI. Uses **skill-forge** structure-first delivery and **prompt-architect** explicit constraints/confidence ceilings.

## Workflow
1. **Scope**: Define environment, approved destinations, proxy needs, TLS requirements, and credentials/cert handling.
2. **Design**: Choose isolation mode (offline/trusted/custom), draft firewall/egress/DNS rules, and TLS profile (min version, ciphers, OCSP/HSTS).
3. **Implement**: Apply scripts/templates, generate certificates, and record changes.
4. **Validate**: Test allowed connectivity, confirm blocks, validate certificates, and run regression checks.
5. **Monitor & Hand Off**: Enable logging/metrics, document rollback steps, and archive artifacts under `skills/security/network-security-setup/{project}/{timestamp}` with MCP tags (`WHO=network-security-setup-{session}`, `WHY=skill-execution`).

## Guardrails
- Authorized scopes only; never scan unknown targets.
- Deny-by-default; avoid wildcard allowlists.
- Secure storage/rotation for secrets and certificates.
- Explicit confidence ceilings on every claim.

## Deliverables
- Network policy pack (allow/deny, proxy, DNS), TLS profile, and certificate bundle.
- Validation log (allowed/blocked tests, TLS checks) with evidence.
- Operations runbook with monitoring and rollback steps.

Confidence: 0.71 (ceiling: inference 0.70) - README rebuilt to mirror the updated SOP and prompt-architect constraint discipline.
