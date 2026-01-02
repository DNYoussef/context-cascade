---
name: meta-tools
description: Design, validate, and orchestrate development tools with reusable patterns, composition rules, and evidence-backed tests.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rebuilt the meta-tools guidance with Skill Forge required sections, tool composition guardrails, and verification steps.
- Added prompt-architect style constraint extraction plus confidence ceilings for tool recommendations.

## STANDARD OPERATING PROCEDURE

### Purpose
Create and evolve a library of development tools with clear contracts, composition patterns, and validation evidence so downstream agents can reliably orchestrate them.

### Trigger Conditions
- Positive: requests to design a new tool, improve an existing one, or compose multiple tools into a workflow.
- Negative/reroute: single-use prompts (prompt-architect), agent design (agent-creator), or pure skill scaffolding (skill-builder/skill-forge).

### Guardrails
- Define explicit inputs/outputs, side effects, and failure modes for every tool.
- Include safety and rate-limit considerations for external integrations.
- Maintain English outputs with explicit confidence ceilings for recommendations.
- Require tests (unit/simulation) before promoting a tool for orchestration use.

### Execution Phases
1. **Discovery**: Capture problem, environment, constraints, and integration surfaces; classify hard/soft/inferred constraints.
2. **Interface Design**: Specify input/output contracts, error semantics, and idempotency expectations.
3. **Implementation/Selection**: Build or adapt tools; ensure portability and minimal dependencies.
4. **Validation**: Run functional, boundary, and misuse tests; record evidence and metrics.
5. **Composition**: Document how the tool chains with others, including pre/post hooks.

### Pattern Recognition
- IO-transformer tools → emphasize deterministic formats and schema validation.
- External-service tools → highlight auth, retries, and timeout strategies.
- Orchestration helpers → clarify preconditions and postconditions for safe chaining.

### Advanced Techniques
- Provide composable adapters (wrappers) to normalize outputs for downstream tools/agents.
- Use circuit-breaker patterns for unstable integrations.
- Capture provenance metadata so agent-selector can trust the tool pedigree.

### Common Anti-Patterns
- Ambiguous side effects or undocumented environment requirements.
- Overloaded tools that do too many things.
- Missing validation or confidence ceilings for claims about reliability.

### Practical Guidelines
- Prefer small, single-purpose tools with clear naming.
- Include example invocations and sample payloads in references/resources.
- Version tools when contracts change; keep changelog notes.

### Cross-Skill Coordination
- Upstream: prompt-architect for clarity; cognitive-lensing for alternative designs.
- Parallel: skill-builder/skill-forge for directory and documentation alignment.
- Downstream: agent-creator/agent-selector using tool metadata; recursive-improvement for tuning reliability.

### MCP Requirements
- Document required MCP servers and permissions; tag WHO=meta-tools-{session}, WHY=skill-execution for memory usage.

### Input/Output Contracts
```yaml
inputs:
  problem: string  # required problem statement
  environment: string  # optional runtime/environment notes
  constraints: list[string]  # optional constraints
outputs:
  tool_specs: list[file]  # definitions with contracts and examples
  validation_report: file  # tests executed and results
  composition_notes: summary  # how tools chain together
```

### Recursive Improvement
- Use recursive-improvement when tools fail tests or integration friction is high; capture deltas between iterations.

### Examples
- Build a schema-validator tool to sanitize API payloads before database writes.
- Compose a doc-generation toolchain combining linting, formatting, and preview steps.

### Troubleshooting
- Flaky integrations → add retries, backoff, and circuit breakers.
- Schema drift → pin versions and add validation layers.
- Tool overlap → consolidate or specialize with clear naming and scope.

### Completion Verification
- [ ] Tool contracts defined with inputs/outputs and failure modes.
- [ ] Validation evidence recorded; ceilings stated for reliability claims.
- [ ] Composition guidance documented for orchestration use.
- [ ] Dependencies and permissions disclosed.

Confidence: 0.70 (ceiling: inference 0.70) - Meta-tools SOP aligned to Skill Forge cadence with prompt-architect guardrails.
