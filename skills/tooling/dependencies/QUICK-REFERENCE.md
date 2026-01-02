# Dependencies Hub – Quick Reference (v3.2.0)

Purpose: one-stop entry for dependency graphing, security/freshness checks, and routing to dependency-mapper when visualization is primary.

## Triggers
- Graph or audit dependencies; plan upgrades; detect circular/unused packages.
- Route mapping-heavy requests to `when-mapping-dependencies-use-dependency-mapper`.

## Fast Path
1. Detect ecosystems (lockfiles): npm/pnpm/yarn, pip/poetry, cargo, go mod, maven/gradle, composer.
2. Collect data: tree/graph, vulnerabilities, outdated/unused/circular signals.
3. Summarize risks and blast radius.
4. Recommend actions (pin/upgrade/remove/isolate) with commands.
5. Validate (audit/tests) and state confidence with ceiling syntax.

## Commands (per ecosystem)
- npm/pnpm/yarn: `npm ls --all`, `npm audit`, `npm outdated`.
- Python: `pip list --format=freeze`, `pip-audit`, `pip install -U <pkg>`.
- Rust: `cargo tree`, `cargo audit`, `cargo update -p <crate>`.
- Go: `go list -m all`, `govulncheck`, `go get -u ./...`.
- Java: `mvn dependency:tree`, `gradle dependencies`, use OWASP Dependency-Check.
- PHP: `composer show`, `composer outdated`, `composer audit`.

## Outputs
- Ecosystem and scope, graph highlights, vulnerability/freshness summary.
- Remediation plan with owners, commands, rollback notes.
- Confidence line `Confidence: X.XX (ceiling: TYPE Y.YY)` and memory keys used.

## Validation Checklist
- Ecosystem detected; routing noted.
- Vulnerability data sourced and cited.
- Proposed actions have blast radius + rollback guidance.
- Memory tags applied (`WHO/WHY/PROJECT/WHEN`).
- Confidence ceiling declared.

Confidence: 0.70 (ceiling: inference 0.70) – Quick reference rewritten with Prompt Architect constraint order.
