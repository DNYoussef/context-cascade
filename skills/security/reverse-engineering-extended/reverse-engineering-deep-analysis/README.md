# Reverse Engineering Deep Analysis (Extended)

## Purpose
High-effort reverse engineering with deobfuscation, multi-stage unpacking, tracing, symbolic execution, and exploit validation. Follows **skill-forge** structure-first requirements and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Scope**: Authorization, hashes, protections expected, goals (PoC, IOC set, mitigation plan), and time budget.
2. **Prepare**: Detect packers/anti-debug/VM tricks; set breakpoints/hooks; craft harnesses and inputs.
3. **Execute**: Iteratively unpack/decrypt, trace control/data flows, and capture memory dumps in isolated sandboxes with controlled network.
4. **Assess**: Validate exploitability, mitigations, and produce IOCs; cross-check across static/dynamic/symbolic methods.
5. **Deliver**: Report, PoCs (if permitted), IOC inventory, and mitigation guidance; store artifacts at `skills/security/reverse-engineering-extended/reverse-engineering-deep-analysis/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-deep-analysis-{session}`, `WHY=skill-execution`).

## Guardrails
- Isolation and snapshots required; no uncontrolled network.
- Chain-of-custody (hashes, env, tool versions) preserved.
- Evidence + confidence ceiling for every claim; dual validation for critical findings.

Confidence: 0.71 (ceiling: inference 0.70) - README aligned with the extended deep SOP and prompt-architect constraints.
