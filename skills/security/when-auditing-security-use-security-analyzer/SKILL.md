---
name: when-auditing-security-use-security-analyzer
description: Routing skill that activates the security analyzer workflow for audits, vulnerability reviews, and remediation planning.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: security
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## Purpose
Provide a clear entry point to security audits using the security analyzer stack. Encodes **skill-forge** structure-first expectations and **prompt-architect** constraint/confidence practices to route, scope, and validate audits.

## Use When / Redirect When
- **Use when:** a user asks for a security audit, vulnerability review, or remediation plan for code/services/infrastructure.
- **Redirect when:** network/sandbox policy setup (`network-security-setup`, `sandbox-configurator`) or reverse engineering tasks (`reverse-engineering-*`).

## Guardrails
- Operate only with written authorization and defined scope.
- Collect evidence for every claim; no speculative vulnerabilities.
- Respect deny-by-default for active testing; isolate from production unless approved.
- Confidence ceilings enforced (inference/report ≤0.70, research 0.85, observation/definition 0.95).

## Prompt Architecture Overlay
1. Capture HARD/SOFT/INFERRED constraints (assets, environments, risk tolerance, timelines).
2. Two-pass refinement: structure (routing, coverage) then epistemic (evidence, ceilings).
3. English-only outputs with explicit confidence line.

## SOP (Audit Routing Loop)
1. **Intake & Routing**
   - Confirm authorization, assets, and objectives (assessment vs. remediation).
   - Choose downstream paths: `security`, `network-security-setup`, `sandbox-configurator`, or reverse-engineering skills.
2. **Plan**
   - Define test modes (static, dynamic, supply-chain) and safety controls.
   - Establish evidence plan (PoC/logs/config snapshots) and MCP tags (`WHO=security-analyzer-{session}`, `WHY=skill-execution`).
3. **Execute**
   - Trigger security analyzer processes (scans, code review, dependency checks) with deny-by-default networking.
4. **Validate**
   - Require dual validation for critical/high findings; map to CVE/CWE/OWASP.
   - Confirm confidence ceilings and note gaps/false positives.
5. **Deliver**
   - Findings register, remediation backlog, and executive summary; archive to `skills/security/when-auditing-security-use-security-analyzer/{project}/{timestamp}`.

## Deliverables
- Scoped audit plan with safety controls.
- Findings + remediation with evidence and severity.
- Validation log and residual risk summary.

## Quality Gates
- Structure-first documentation; missing resources/examples/tests logged.
- Authorization and isolation confirmed.
- Evidence + confidence ceiling for each claim; dual validation on critical/high.

## Anti-Patterns
- Running scans without approval or isolation.
- Reporting without evidence or remediation guidance.
- Over-claiming severity/confidence.

## Output Format
- Scope + constraints table (HARD/SOFT/INFERRED).
- Audit plan, routed skills, and executed checks.
- Findings/remediations and validation summary.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY) - reason`.

Confidence: 0.72 (ceiling: inference 0.70) - Audit routing skill aligned with skill-forge structure and prompt-architect constraint handling.
