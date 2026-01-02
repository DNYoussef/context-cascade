# Reverse Engineering Quick Triage (Extended)

## Purpose
Urgent IOC/capability extraction under strict timeboxes with evidence quality maintained. Uses **skill-forge** structure-first discipline and **prompt-architect** explicit constraints/confidence ceilings.

## Quick Flow
1. **Scope & Safety**: Authorization, hashes, time budget, isolation, and blocked/allowlisted network.
2. **Static Pass**: Format/arch, packers, strings/URLs, signatures, entropy/sections.
3. **Controlled Dynamic (optional)**: Minimal sandbox/emulation with strict egress controls to capture key events.
4. **Synthesize**: IOC list, capability summary, uncertainties, and escalation needs.
5. **Deliver**: Containment recommendations, evidence, and archive at `skills/security/reverse-engineering-extended/reverse-engineering-quick-triage/{project}/{timestamp}` with MCP tags (`WHO=reverse-engineering-quick-triage-{session}`, `WHY=skill-execution`).

## Guardrails
- Isolation mandatory; avoid external uploads without consent.
- Honor timebox; escalate if deeper analysis is required.
- Evidence + confidence ceiling for every claim.

Confidence: 0.70 (ceiling: inference 0.70) - README aligned to the extended quick SOP.
