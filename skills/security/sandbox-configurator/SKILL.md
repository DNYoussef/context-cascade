---
name: sandbox-configurator
description: Secure sandbox policy design (filesystem, network, secrets, observability) with auditable guardrails for development runtimes.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Configure sandbox environments with least-privilege controls across filesystem, network, processes, and secrets. Built on **skill-forge** structure-first delivery and **prompt-architect** constraint/confidence practices.

## Use When / Redirect When
- **Use when:** defining sandbox policies, tightening egress, mounting read-only assets, and setting observability for development tasks.
- **Redirect when:** broader network design (`network-security-setup`) or general security triage (`security`).

## Guardrails
- Authorized scopes only; deny-by-default for network and filesystem writes.
- No plaintext secrets; use ephemeral tokens or secret stores.
- Capture audit logs for policy changes; include rollback steps.
- Confidence ceilings: inference/report ≤0.70, research 0.85, observation/definition 0.95.

## Prompt Architecture Overlay
1. HARD/SOFT/INFERRED constraints (runtime, language, network needs, mounts, secrets, observability).
2. Two-pass refinement (structure → epistemic) to ensure coverage and evidence.
3. English-only outputs with explicit confidence line.

## SOP (Sandbox Hardening Loop)
1. **Scope & Inventory**
   - Identify runtime (node/python/etc.), required tools, artifacts, and allowed destinations.
   - Decide filesystem mounts (read-only vs. writable) and secrets injection method.
2. **Policy Design**
   - Network: deny-by-default with allowlist; integrate with `network-security-setup` if needed.
   - Filesystem: read-only code, isolated writable temp, blocked sensitive paths.
   - Process: limit capabilities, resource quotas, and disallow dangerous syscalls where possible.
   - Observability: enable logging/metrics for policy hits/misses.
3. **Implementation**
   - Apply configs/scripts; record changes and approvals.
   - Inject secrets via environment/secret store with rotation notes.
4. **Validation**
   - Test allowed workflows succeed; confirm blocked actions fail.
   - Run regression for dependency installs and common developer actions.
5. **Delivery**
   - Provide policy bundle, runbook, and rollback steps.
   - Archive artifacts at `skills/security/sandbox-configurator/{project}/{timestamp}` with MCP tags (`WHO=sandbox-configurator-{session}`, `WHY=skill-execution`).

## Deliverables
- Sandbox policy pack (network, filesystem, process, secrets) and change log.
- Validation log (allowed vs. blocked tests) with evidence.
- Runbook (operations, monitoring, rollback) and secret handling notes.

## Quality Gates
- Structure-first documentation; missing resources/examples/tests noted.
- Deny-by-default enforced; secrets handled securely.
- Evidence attached to claims with confidence ceilings.
- Rollback path verified and documented.

## Anti-Patterns
- Granting blanket write access or unrestricted network.
- Hardcoding secrets or disabling logging.
- Skipping rollback testing.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- Policy summary with validation results and evidence.
- Runbook pointers and residual risks.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.72 (ceiling: inference 0.70) - Sandbox SOP rewritten with skill-forge structure and prompt-architect constraint handling.
