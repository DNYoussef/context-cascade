# When Configuring Sandbox Security, Use Sandbox Configurator

## Purpose
Route sandbox security requests into the updated `sandbox-configurator` SOP with clear scope, safety, and evidence expectations. Anchored in **skill-forge** structure-first and **prompt-architect** constraint/confidence practices.

## Quick Flow
1. Capture constraints (runtime, mounts, network allowlist, secrets, observability) as HARD/SOFT/INFERRED.
2. Enforce safety: isolation, deny-by-default network, secure secret handling, rollback plan.
3. Invoke `sandbox-configurator`; log MCP tags (`WHO=sandbox-configurator-{session}`, `WHY=skill-execution`).
4. Validate allowed vs. blocked behaviors and record evidence with confidence ceilings.
5. Deliver policy pack + validation log under `skills/security/specialized-tools/when-configuring-sandbox-security-use-sandbox-configurator/{project}/{timestamp}`.

Confidence: 0.70 (ceiling: inference 0.70) - README aligned with the refreshed sandbox-configurator workflow.
