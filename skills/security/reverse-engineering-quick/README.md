# Reverse Engineering Quick

## Purpose
Timeboxed IOC extraction and rapid risk calls for binaries/documents. Uses **skill-forge** structure-first discipline and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Scope & Safety**: Authorize scope, hash the sample, and isolate the workspace.
2. **Static Extraction**: File type, metadata, entropy/sections, strings/URLs, YARA signatures.
3. **Optional Safe Peek**: Controlled sandbox/emulation with strict egress blocks to capture basic events.
4. **Consolidate**: Normalize hashes/domains/IPs/paths/mutexes and persistence hints; cite sources.
5. **Deliver**: IOC pack, risk summary, and evidence stored at `skills/security/reverse-engineering-quick/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-quick-{session}`, `WHY=skill-execution`).

## Guardrails
- No unrestricted execution; isolation required.
- No external uploads without consent.
- Evidence + confidence ceiling for every claim.

## Outputs
- IOC pack with sources, risk summary, and containment recommendations.
- Evidence bundle (tool outputs/logs) with timestamps.

Confidence: 0.70 (ceiling: inference 0.70) - README aligned to the updated quick triage SOP.
