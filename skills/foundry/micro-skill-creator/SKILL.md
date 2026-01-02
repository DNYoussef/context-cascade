---
name: micro-skill-creator
description: Rapidly craft atomic, single-purpose skills with tight contracts, examples, and validation so they can be composed safely.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Restructured the micro-skill playbook using the Skill Forge required sections and explicit completion gates.
- Added prompt-architect constraint extraction, confidence ceilings, and examples to avoid over-broad micro-skills.

## STANDARD OPERATING PROCEDURE

### Purpose
Produce narrowly-scoped skills that do one job exceptionally well, with clear inputs/outputs, examples, and validation evidence for easy composition.

### Trigger Conditions
- Positive: need a reusable micro-skill, want to refactor a large skill into smaller parts, or require fast iterations on a narrow task.
- Negative/reroute: full agent creation (agent-creator), broad prompt tuning (prompt-architect), or full skill scaffolding (skill-builder/skill-forge).

### Guardrails
- Keep the scope single-purpose; avoid feature creep.
- Provide English outputs with explicit confidence ceilings and deterministic formats.
- Include at least one example and one edge-case check.
- Document how this micro-skill composes with others and where it should NOT be used.

### Execution Phases
1. **Intake**: Capture the atomic task, constraints, success criteria, and consumers; classify hard/soft/inferred constraints.
2. **Design**: Define inputs/outputs, preconditions, and failure behaviors; choose minimal dependencies.
3. **Author**: Write the SKILL.md content, examples, and tests.
4. **Validate**: Run happy/edge tests; record evidence and ceilings.
5. **Publish**: Provide usage notes and composition guidance; register with meta-tools/skill-forge index if needed.

### Pattern Recognition
- Data formatting/conversion → deterministic IO, schema validation.
- Guard/validation micro-skills → explicit error codes and refusal policy.
- Retrieval micro-skills → caching hints and rate-limit safety.

### Advanced Techniques
- Use table-driven prompts to keep behavior predictable.
- Apply few-shot examples demonstrating both success and refusal paths.
- Add lightweight observability (logs/notes) for downstream debugging.

### Common Anti-Patterns
- Multi-purpose scope disguised as micro-skill.
- Missing examples or unclear error handling.
- Over-reliance on assumptions instead of explicit constraints.

### Practical Guidelines
- Keep the SKILL.md concise; link to references/resources for depth.
- Mark optional parameters and defaults clearly.
- Encourage idempotent behaviors where possible.

### Cross-Skill Coordination
- Upstream: prompt-architect for clarity; cognitive-lensing for alternative framings.
- Downstream: meta-tools for composition; agent-creator for embedding into agents; recursive-improvement for tuning.

### MCP Requirements
- Optional memory MCP to store usage notes; tag WHO=micro-skill-creator-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  task: string  # required atomic task
  constraints: list[string]  # optional constraints
  io_format: string  # optional preferred format
outputs:
  skill_spec: file  # SKILL.md content for the micro-skill
  examples: list[file]  # example invocations
  tests: list[file]  # validation checks
```

### Recursive Improvement
- Run recursive-improvement after initial use to capture failure cases and tighten scope; stop when delta < 2% or risks noted.

### Examples
- Create a JSON schema validator micro-skill with refusal path for invalid input.
- Build a markdown-to-summary micro-skill with length and tone controls.

### Troubleshooting
- Skill too broad → split into smaller micro-skills.
- Unclear errors → add structured error outputs and refusals.
- Flaky results → add few-shot anchors and deterministic formatting.

### Completion Verification
- [ ] Scope single-purpose and documented.
- [ ] Examples and tests included with evidence.
- [ ] Confidence ceiling stated; inputs/outputs explicit.
- [ ] Composition guidance provided.

Confidence: 0.70 (ceiling: inference 0.70) - Micro-skill SOP rewritten with Skill Forge scaffolding and prompt-architect ceilings.
