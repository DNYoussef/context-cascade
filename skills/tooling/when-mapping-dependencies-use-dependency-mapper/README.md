# Dependency Mapper

Visualize and analyze dependency graphs with evidence, safety, and reproducible commands.

## Quick Start
1. Detect ecosystem (lockfiles) and scope.
2. Run mapping commands (see below) to build graph.
3. Analyze risks: circular, unused, outdated, vulnerable packages.
4. Generate visualization and recommend actions with rollback notes.
5. Record confidence ceiling and store artifacts under `skills/tooling/when-mapping-dependencies-use-dependency-mapper/{project}/{timestamp}` (mirror path if nested).

## Commands by Ecosystem
- npm/pnpm/yarn: `npm ls --all`, `npm outdated`, `npm audit`.
- Python: `pip list --format=freeze`, `pipdeptree`, `pip-audit`.
- Rust: `cargo tree`, `cargo audit`.
- Go: `go list -m all`, `govulncheck`.
- Java: `mvn dependency:tree`, `gradle dependencies`, OWASP Dependency-Check.
- PHP: `composer show`, `composer outdated`, `composer audit`.

## Outputs
- Graph artifact, nodes/edges counts, hotspots, and risks.
- Remediation plan with commands and rollback guidance.
- Confidence: `Confidence: X.XX (ceiling: TYPE Y.YY)`.

## Guardrails
- Evidence-first; cite commands and lockfiles.
- Confidence ceilings enforced; flag incomplete data.
- Structure-first docs maintained; no secrets in logs.

Confidence: 0.70 (ceiling: inference 0.70) – README aligned to Prompt Architect clarity.
