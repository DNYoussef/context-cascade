---
name: skill-forge
description: Meta-skill for producing production-grade skills with complete structure, validation, and self-improvement loops.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Re-sequenced the forge SOP into Skill Forge required sections with explicit guardrails, hooks, and validation gates surfaced earlier.
- Preserved adversarial validation and dogfooding requirements while adding prompt-architect ceiling discipline across outputs.

## STANDARD OPERATING PROCEDURE

### Purpose
Create or upgrade skills so they ship with full directory structure, SKILL.md content, examples, tests, references, and validation evidence.

### Trigger Conditions
- Positive: "create skill", "optimize skill", "adversarial validation", "skill improvement".
- Negative/reroute: micro-skill creation (micro-skill-creator), agent design (agent-creator/agent-creation), prompt-only tuning (prompt-architect/prompt-forge).

### Guardrails
- Structure-first: always produce SKILL.md plus examples/ and tests/; prefer resources/ and references/.
- Adversarial validation is mandatory (boundary, failure, chain-of-verification); do not declare done without evidence.
- Self-application required: run dogfooding loop until improvement delta < 2% or risks documented.
- Enforce confidence ceilings in outputs; English-only user-facing content.
- Hooks latency targets: pre_hook_target_ms 20 (max 100); post_hook_target_ms 100 (max 1000).

### Execution Phases
1. **Requirements Analysis**: Parse requested skill, domain, constraints, and success criteria; check reuse options.
2. **Structure Design**: Lay out directories and placeholders per required sections; log any deviations.
3. **Skill Definition**: Author SKILL.md with frontmatter, SOP, guardrails, integrations, IO contracts, and anti-patterns.
4. **Adversarial Validation**: Run boundary/failure/COV checks; capture evidence and metrics.
5. **Dogfooding Loop**: Apply skill-forge to itself or the target skill; iterate until convergence threshold or timebox.
6. **Packaging & Delivery**: Package artifacts, examples, tests, references/resources, and delivery notes with confidence ceilings.

### Pattern Recognition
- Greenfield skill → prioritize purpose, triggers, and contracts before details.
- Legacy skill migration → map to required sections and fill gaps with TODOs + owners.
- High-risk domain → expand adversarial probes and safety guardrails.

### Advanced Techniques
- Use checklists from REQUIRED-SECTIONS.md to ensure tier coverage.
- Apply contrastive examples to define scope and refusal boundaries.
- Capture MCP tagging (WHO=skill-forge-{session}, WHY=skill-execution) for traceability.

### Common Anti-Patterns
- Missing required sections (overview, workflows, integrations, closure).
- Skipping validation or omitting confidence ceilings.
- Generic cross-skill notes without actionable coordination.

### Practical Guidelines
- Keep instructions concise but complete; link to references for depth.
- Prefer deterministic output schemas for examples/tests.
- Document open risks and next steps when timeboxed.

### Cross-Skill Coordination
- Upstream: prompt-architect for clarity; cognitive-lensing for alternative framings.
- Parallel: meta-tools for supporting utilities; base-template-generator for scaffolds when code is included.
- Downstream: agent-creator/agent-selector for routing; recursive-improvement for ongoing tuning.

### MCP Requirements
- Memory/vector search recommended for pattern reuse; tag WHO=skill-forge-{session}, WHY=skill-execution.
- Record hooks/performance expectations in outputs.

### Input/Output Contracts
```yaml
inputs:
  skill_name: string  # required
  category: string  # required
  domain: string  # optional domain focus
  constraints: list[string]  # optional constraints and policies
outputs:
  skill_artifacts: list[file]  # SKILL.md, examples, tests, resources, references
  validation_report: file  # adversarial and COV results
  delivery_notes: summary  # packaging summary, risks, and next steps
```

### Recursive Improvement
- Self-apply: `skill_forge.improve(skill_forge)`; log iterations and stop at <2% delta or explicit risk acceptance.

### Examples
- Forge a security-audit skill with dependency review tests and refusal policy.
- Upgrade an orchestration skill to include cross-skill coordination and MCP requirements.

### Troubleshooting
- Missing sections → consult REQUIRED-SECTIONS.md and add content/TODO with owner.
- Validation gaps → create or update tests before delivery; document any deferrals.
- Convergence slow → tighten hypotheses and focus on highest-risk gaps.

### Completion Verification
- [ ] Required directories present; SKILL.md includes all tiers.
- [ ] Adversarial validation executed with evidence and ceilings.
- [ ] Dogfooding loop run or explicitly deferred with rationale.
- [ ] Delivery notes include risks, hooks, and MCP tags.

Confidence: 0.70 (ceiling: inference 0.70) - Skill Forge SOP rewritten to match required sections with ceiling discipline.
