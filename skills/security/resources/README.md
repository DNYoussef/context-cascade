# Security Skill Resources

Curated scripts, templates, and examples that support the security skill group. Organized with **skill-forge** structure-first discipline and **prompt-architect** explicit constraints/confidence ceilings.

## Structure
- `scripts/`: Operational tools (OWASP scanning, dependency/CVE audit, pentest harness, static analysis).
- `templates/`: Checklists and report skeletons (security policy, pentest plan, vulnerability report).
- `examples/`: Usage patterns for sandboxed security workflows.

## Guardrails
- Authorized targets only; never run active testing against production without approval.
- Default to deny-by-default networking when executing scripts.
- Protect secrets and tokens; do not embed in configs or logs.
- Attach evidence and confidence ceilings to findings produced via these resources.

## Usage Pattern
1. Select the script/template that matches the SOP being executed (security audit, network lockdown, reverse engineering support).
2. Capture HARD/SOFT/INFERRED constraints (scope, targets, output paths, safety controls).
3. Run in isolated environments; store outputs with hashes/timestamps under the corresponding skill path.
4. Summarize results with confidence notation, citing the scripts/templates used.

## Example Commands
- OWASP/top-10 scan: `python resources/scripts/owasp-scanner.py --target ./src --output /tmp/owasp-report.json`
- Dependency audit: `node resources/scripts/dependency-auditor.js --package-json ./package.json --output /tmp/cve-report.json`
- Pentest harness (safe mode): `bash resources/scripts/penetration-tester.sh --target https://localhost:3000 --safe-mode --output /tmp/pentest-report.html`
- Static analysis: `python resources/scripts/secure-code-analyzer.py --scan-dir ./src --output /tmp/security-analysis.json`

## Outputs to Expect
- JSON/YAML/HTML/Markdown reports with timestamps.
- Logs and artifacts hashed; stored under the invoking skill’s directory with MCP tags.
- Validation notes indicating which tests passed/failed and the applied confidence ceilings.

Confidence: 0.71 (ceiling: inference 0.70) - Resources README aligned to the updated security skill SOPs with prompt-architect constraint handling.
