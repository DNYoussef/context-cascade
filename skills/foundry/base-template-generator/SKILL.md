---
name: base-template-generator
description: Generate production-ready project boilerplates with linting, testing, and minimal dependencies for common stacks.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Standardized the SOP with Skill Forge required sections and explicit completion checks for scaffolds.
- Added prompt-architect style constraint capture and safety rails to avoid bloated or insecure templates.

## STANDARD OPERATING PROCEDURE

### Purpose
Deliver clean starter templates for Node.js, Python, Go, React, Vue, and similar stacks with opinionated defaults for security, testing, and DX.

### Trigger Conditions
- Positive: starting a new project, creating reproducible boilerplates, aligning teams on baseline configs.
- Negative/reroute: small code snippets (use prompt-architect) or full platform scaffolds (consider meta-tools/platform skills).

### Guardrails
- Keep dependencies minimal and well-justified; avoid framework lock-in unless requested.
- Include linting, formatting, testing, and basic CI hooks; no silent TODO omissions.
- Output English documentation with explicit confidence ceilings.
- Surface security defaults (env handling, secrets, supply-chain hygiene).

### Execution Phases
1. **Intake**: Capture stack, language, package manager, deployment target, and constraints; classify hard/soft.
2. **Design**: Select template baseline, directory layout, and required tooling (lint, test, CI, containerization).
3. **Generate**: Produce files with sensible defaults, comments, and quickstart instructions.
4. **Validate**: Run static checks (lint/test) where feasible; note gaps and risks.
5. **Deliver**: Summarize outputs, commands to run, and next-step hardening items.

### Pattern Recognition
- API services → emphasize routing, logging, error handling, health checks.
- Frontend apps → focus on routing, state management, accessibility, testing harness.
- Libraries/SDKs → prioritize typing, semantic versioning, and publishing workflows.

### Advanced Techniques
- Provide switchable presets (secure-by-default vs minimal) with rationale.
- Include container artifacts (Dockerfile/compose) when deployment hints are given.
- Offer optional observability hooks (metrics/logging) without hard dependencies.

### Common Anti-Patterns
- Bundling unnecessary dependencies or example code that hides defects.
- Omitting env handling or secret management guidance.
- Shipping without runnable tests or lint configs.

### Practical Guidelines
- Prefer explicit scripts in package manifests for onboarding.
- Keep README quickstart under 10 steps; include expected tool versions.
- Document how to extend the template safely.

### Cross-Skill Coordination
- Upstream: prompt-architect to refine requirements; skill-builder/skill-forge for directory structure alignment.
- Downstream: delivery/operations skills for deployment; security skills for threat modeling.

### MCP Requirements
- Optional: filesystem + command MCP for scaffolding and verification; tag WHO=base-template-generator-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  stack: string  # required technology stack
  project_type: string  # api, frontend, library, cli
  constraints: list[string]  # optional hard/soft/inferred constraints
  ci_target: string  # optional platform (github-actions, gitlab, etc)
outputs:
  template_files: list[file]  # generated boilerplate
  quickstart: file  # README with setup/run/test steps
  validation: summary  # checks executed and gaps
```

### Recursive Improvement
- Run recursive-improvement using feedback from initial runs to trim bloat and improve defaults.

### Examples
- Create a Node.js REST API template with TypeScript, eslint, vitest, and OpenAPI stub.
- Build a React SPA starter with Vite, eslint, prettier, testing-library, and accessibility checks.

### Troubleshooting
- Dependency conflicts → downgrade to stable LTS or pin versions and document.
- Missing tests → scaffold minimal smoke tests and mark TODO with next steps.
- CI not available → provide local validation commands and stub workflows.

### Completion Verification
- [ ] Template includes lint/test/config with commands documented.
- [ ] Quickstart provided; env/secrets guidance included.
- [ ] Confidence ceiling stated with any TODOs noted.
- [ ] Directory layout matches requested stack.

Confidence: 0.70 (ceiling: inference 0.70) - Template SOP rewritten with Skill Forge and prompt-architect scaffolding.
