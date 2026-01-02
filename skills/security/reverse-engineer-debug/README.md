# Reverse Engineer Debug

## Purpose
Rapid, safe triage of binaries to identify capabilities and IOCs using static signals and controlled light dynamic execution. Built with **skill-forge** structure-first requirements and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Scope & Safety**: Confirm authorization, hash the sample, and work in an isolated sandbox with blocked or allowlisted network.
2. **Static Recon**: Identify format/arch, imports, packers, and suspicious strings/URLs; run YARA and section/entropy checks.
3. **Light Dynamic**: Emulate or sandbox with syscall/file/network capture; halt on scope breach.
4. **Assess**: Summarize capabilities and risk; propose deeper follow-up if needed.
5. **Deliver**: Provide evidence (tool outputs, logs, hashes) and archive under `skills/security/reverse-engineer-debug/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineer-debug-{session}`, `WHY=skill-execution`).

## Guardrails
- Isolation required; never execute unknown binaries on production hosts.
- No uploads to third-party services without approval.
- Evidence + confidence ceiling for every claim.

## Outputs
- Capability summary, IOC list, risk level, and recommended next steps.
- Evidence bundle with timestamps and hashes.

Confidence: 0.70 (ceiling: inference 0.70) - README aligned to the triage SOP and prompt-architect constraints.
