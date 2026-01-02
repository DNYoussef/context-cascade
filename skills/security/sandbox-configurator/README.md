# Sandbox Configurator

## Purpose
Design and enforce secure sandbox policies (filesystem, network, secrets, observability) for development runtimes. Uses **skill-forge** structure-first discipline and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Scope**: Runtime/tooling needs, allowed network destinations, mounts (read-only vs. writable), secrets handling, and observability.
2. **Design**: Deny-by-default network, read-only code mounts, isolated writable temp, minimal process capabilities, and logging/metrics.
3. **Implement**: Apply configs/scripts, inject secrets securely, and record change logs.
4. **Validate**: Test allowed workflows and confirm blocked operations fail; run regression for installs and tooling.
5. **Deliver**: Policy pack, validation log, and rollback/runbook archived at `skills/security/sandbox-configurator/{project}/{timestamp}` with MCP tags (`WHO=sandbox-configurator-{session}`, `WHY=skill-execution`).

## Guardrails
- Authorized scopes only; no plaintext secrets.
- Deny-by-default for network and sensitive filesystem paths.
- Evidence + confidence ceiling on every claim; rollback path tested.

Confidence: 0.70 (ceiling: inference 0.70) - README aligned to the updated sandbox SOP.
