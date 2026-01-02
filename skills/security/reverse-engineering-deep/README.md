# Reverse Engineering Deep

## Purpose
Advanced dynamic tracing, memory inspection, and symbolic execution for complex binaries. Applies **skill-forge** structure-first rules and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Scope & Safety**: Authorization, hashes, platform/arch, objectives; isolate with snapshots and controlled network.
2. **Prep**: Identify protections, unpack if permitted, set instrumentation hooks, and build harnesses.
3. **Dynamic Analysis**: Trace syscalls/memory/IPC/network, capture dumps, and run symbolic execution to reach guarded paths.
4. **Assess**: Validate exploitability, enumerate mitigations, extract permitted secrets/configs.
5. **Deliver**: Behavioral report, IOC set, exploitability assessment, and mitigation plan; archive at `skills/security/reverse-engineering-deep/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-deep-{session}`, `WHY=skill-execution`).

## Guardrails
- Isolated sandboxes only; snapshots required.
- Controlled/blocked network; avoid external uploads.
- Evidence + confidence ceiling for every claim; dual validation for critical items.

## Outputs
- Traces/dumps (hashed), IOC inventory, exploitability assessment, and mitigations.
- Reproduction steps and harnesses/scripts.

Confidence: 0.71 (ceiling: inference 0.70) - README aligned to the deep analysis SOP.
