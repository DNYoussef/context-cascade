---
name: skill-builder
description: Scaffold new Claude Code skills with correct frontmatter, directory layout, contracts, and validation assets.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rewrote the builder SOP using the Skill Forge required sections and structure-first guardrails.
- Added prompt-architect constraint extraction, confidence ceilings, and completion checks for every artifact.

## STANDARD OPERATING PROCEDURE

### Purpose
Create or template skills with complete SKILL.md content, examples, tests, references, and metadata aligned to Skill Forge standards.

### Trigger Conditions
- Positive: requests to create a new skill template, reorganize an existing skill, or ensure compliance with required sections.
- Negative/reroute: prompt tuning only (prompt-architect/prompt-forge) or agent design (agent-creator/agent-creation).

### Guardrails
- Always generate SKILL.md with YAML frontmatter, SOP, integration, and closure sections; no skeleton-only outputs unless explicitly timeboxed.
- Provide English outputs with explicit confidence ceilings.
- Include directory scaffolding: examples/, tests/, resources/, references/ as appropriate.
- Record any missing sections as TODO with remediation steps.

### Execution Phases
1. **Scoping**: Capture skill name, category, purpose, triggers, and constraints; classify HARD/SOFT/INFERRED.
2. **Structure**: Lay out directories and placeholder files as needed; ensure SKILL.md includes required sections (Purpose → Completion Verification).
3. **Content Authoring**: Fill SOP, guardrails, integrations, and contracts with skill-specific details.
4. **Validation**: Check section completeness against Skill Forge required sections; run sanity tests/examples where applicable.
5. **Delivery**: Summarize outputs, open gaps, and confidence ceilings; register in indexes if required.

### Pattern Recognition
- New greenfield skill → start from base template and focus on purpose/triggers first.
- Migrating legacy skill → map old sections to required ones and fill gaps.
- Skill extension → add integrations and recursive-improvement hooks.

### Advanced Techniques
- Use checklists from REQUIRED-SECTIONS.md to avoid omissions.
- Pre-fill anti-patterns and guidelines to set expectations for maintainers.
- Reuse prompt-architect output to tighten instructions and refusal policy.

### Common Anti-Patterns
- Missing closure sections (examples, troubleshooting, completion verification).
- Over-general descriptions without IO contracts.
- Forgetting to add validation/test scaffolds.

### Practical Guidelines
- Keep SKILL.md concise but complete; link to references for depth.
- Prefer stable versioning (x-version) and compliance markers.
- Document memory/tags if MCP is expected.

### Cross-Skill Coordination
- Upstream: prompt-architect for clarity; skill-forge for meta quality gates.
- Parallel: cognitive-lensing for alternative approaches; meta-tools for supporting utilities.
- Downstream: agent-creator/agent-selector using the resulting skills.

### MCP Requirements
- Optional memory/vector MCP to store templates; tag WHO=skill-builder-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  skill_name: string  # required name
  category: string  # required category
  purpose: string  # required description
  constraints: list[string]  # optional constraints or policies
outputs:
  skill_files: list[file]  # SKILL.md and supporting scaffolds
  validation_report: summary  # checklist of required sections
  next_steps: list[string]  # follow-up improvements
```

### Recursive Improvement
- Run recursive-improvement to close checklist gaps and refine guidance after initial usage feedback.

### Examples
- Scaffold a security-audit skill with SKILL.md, examples, and tests for dependency review.
- Convert a legacy orchestration skill to the Skill Forge section model with completion checklist.

### Troubleshooting
- Missing section → reference REQUIRED-SECTIONS.md and add content or TODO with owner.
- Directory not created → regenerate scaffolding and verify permissions.
- Ambiguous constraints → rerun constraint extraction and confirm with requester.

### Completion Verification
- [ ] SKILL.md includes all required sections and frontmatter.
- [ ] Directory scaffolding created (examples/tests/resources/references as needed).
- [ ] Confidence ceiling stated; validation checklist completed.
- [ ] Registration or index updates noted.

Confidence: 0.70 (ceiling: inference 0.70) - Skill Builder SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
