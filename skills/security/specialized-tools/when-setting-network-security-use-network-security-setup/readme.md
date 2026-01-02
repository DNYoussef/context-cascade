# When Setting Network Security, Use Network Security Setup

## Purpose
Route network hardening requests into the updated `network-security-setup` SOP. Built on **skill-forge** structure-first standards and **prompt-architect** constraint/confidence rules.

## Quick Flow
1. Capture constraints (environments, allowlists, proxy requirements, TLS posture) as HARD/SOFT/INFERRED.
2. Enforce safety: authorization, change log, isolation; avoid scanning unknown targets.
3. Invoke `network-security-setup`; log MCP tags (`WHO=network-security-setup-{session}`, `WHY=skill-execution`).
4. Validate allowed vs. blocked connectivity and TLS checks with evidence + confidence ceilings.
5. Deliver policy pack + validation log under `skills/security/specialized-tools/when-setting-network-security-use-network-security-setup/{project}/{timestamp}`.

Confidence: 0.70 (ceiling: inference 0.70) - README aligned with the refreshed network-security-setup workflow.
