# Web CLI Teleport

Bridge actions between browser and terminal while keeping safety and auditability in place.

## Quick Start
1. Define goal and constraints (read-only vs write, network limits, credentials allowed).
2. Capture current web and CLI states; note assumptions.
3. Plan steps across web/CLI, identifying risky commands and mitigations.
4. Execute with logging and dry-runs where possible; verify after each step.
5. Summarize actions, evidence, and confidence ceiling; store session memory.

## Inputs
- Goal, environments/URLs, working directories, risk appetite.

## Outputs
- Action log (web + CLI), artifacts collected, gaps/risks, next steps.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)`; memory key `skills/tooling/web-cli-teleport/{project}/{timestamp}`.

## Guardrails
- Never log secrets; gate destructive commands with confirmations.
- Respect Prompt Architect constraint ordering and Skill Forge structure-first docs.
- Enforce confidence ceilings on inferred states.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect clarity.
