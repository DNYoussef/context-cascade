# Audit Activation Process

## Inputs
- Authorization and scope (assets, environments, objectives).
- Constraints (timebox, test modes allowed, risk tolerance).
- Required outputs (findings, remediation plan, executive summary).

## Steps
1. **Scope & Routing**
   - Capture HARD/SOFT/INFERRED constraints per prompt-architect guidance.
   - Select downstream skills: `security`, `network-security-setup`, `sandbox-configurator`, or `reverse-engineering-*` as needed.
2. **Plan & Safety**
   - Define test modes (static, dynamic, supply-chain) and isolation controls (deny-by-default network).
   - Establish evidence plan (PoC/logs/config snapshots) and MCP tags (`WHO=security-analyzer-{session}`, `WHY=skill-execution`).
3. **Execute**
   - Run planned checks with change logs and timestamps.
4. **Validate**
   - Dual validation for critical/high; map to CVE/CWE/OWASP; note confidence ceilings and gaps.
5. **Deliver**
   - Findings + remediation backlog, validation log, executive summary, and archive under `skills/security/when-auditing-security-use-security-analyzer/{project}/{timestamp}`.

## Outputs
- Audit plan, routed skills, executed checks, evidence bundle, remediation actions, and residual risk summary.

Confidence: 0.70 (ceiling: inference 0.70) - Process aligned to skill-forge structure and prompt-architect constraint handling.
