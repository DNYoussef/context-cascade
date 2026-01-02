# Dependencies Hub

One entry point for dependency graphing, vulnerability checks, and upgrade planning, with routing to the dependency-mapper subskill when visualization is primary.

## Quick Start
1. Detect ecosystem from lockfiles (`package-lock.json`, `poetry.lock`, `Cargo.lock`, `go.sum`, `pom.xml`, `build.gradle`, `composer.lock`).
2. Collect data: tree/graph, vulnerability reports, outdated/unused/circular signals.
3. Summarize blast radius and propose actions (pin, upgrade, remove, isolate) with commands.
4. Validate with audits/tests; record confidence using ceiling syntax.

## Inputs
- Scope: file|directory/repo path.
- Options: `policy` (strict|standard|lenient), `report_format` (md|json), routing flag if deep mapping is required.

## Outputs
- Ecosystem detection, graph summary, vulnerability/freshness findings.
- Remediation plan with rollback notes and owners.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)` and memory keys used.

## Guardrails
- Follow Prompt Architect constraint ordering; keep structure-first docs updated.
- Keep eval/audit tooling sources cited; never mutate frozen benchmarks silently.
- Tag MCP memory: `skills/tooling/dependencies/{project}/{timestamp}` with WHO/WHY/PROJECT/WHEN.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Skill Forge delivery gates.
