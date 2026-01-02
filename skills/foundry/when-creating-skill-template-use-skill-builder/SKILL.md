---
name: skill-builder
description: Use the Skill Builder workflow when templating new skills to ensure required sections, structure, and validation are present.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: utilities
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Converted the guidance into a Skill Forge-aligned SOP with explicit triggers and completion checks for template creation.
- Added prompt-architect constraint capture and ceiling discipline so templates ship with clear contracts.

## STANDARD OPERATING PROCEDURE

### Purpose
Route template creation requests through Skill Builder to guarantee compliant SKILL.md content, scaffolding, and validation notes.

### Trigger Conditions
- Positive: any request to create a skill template or restructure a skill to meet documentation standards.
- Negative/reroute: prompt-only optimization (prompt-architect) or agent-focused work (agent-creator/agent-creation).

### Guardrails
- Require SKILL.md with full required sections; skeleton-only responses must include TODOs and owners.
- Keep outputs English-only with explicit confidence ceilings.
- Provide directory scaffolding (examples/tests/resources/references) unless out of scope.

### Execution Phases
1. **Capture Request**: Record skill name, category, purpose, and constraints; classify HARD/SOFT/INFERRED.
2. **Scaffold**: Generate directories and placeholders using Skill Builder patterns.
3. **Author Core Sections**: Populate Purpose, triggers, workflows, integrations, anti-patterns, and closure sections.
4. **Validate**: Check against REQUIRED-SECTIONS checklist; note any gaps with remediation steps.
5. **Deliver**: Summarize created artifacts, open TODOs, and confidence ceiling.

### Pattern Recognition
- Greenfield template → start from base pattern and fill critical sections first.
- Migration from legacy doc → map old headings to required sections and fill gaps.

### Advanced Techniques
- Use prompt-architect to clarify constraints before drafting.
- Leverage meta-tools to generate supporting scripts or references when needed.

### Common Anti-Patterns
- Missing closure sections (examples/troubleshooting/completion verification).
- Unclear IO contracts for the skill.
- No record of validation or TODO ownership.

### Practical Guidelines
- Keep templates concise; link to deeper references when needed.
- Add MCP tagging guidance if memory/vector search will be used.

### Cross-Skill Coordination
- Upstream: prompt-architect; skill-forge for meta-validation.
- Downstream: agent-creator and agent-selector once the skill is live; recursive-improvement for tuning.

### MCP Requirements
- Optional memory/vector MCP for template cataloging; tag WHO=skill-builder-template-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  skill_name: string  # required
  category: string  # required
  purpose: string  # required
  constraints: list[string]  # optional
outputs:
  template_files: list[file]  # SKILL.md and scaffolding
  checklist: summary  # required sections status
  followups: list[string]  # TODOs with owners
```

### Recursive Improvement
- After initial use, run recursive-improvement to close gaps and refine guidance.

### Examples
- Create a template for a logging skill with placeholders for integrations and tests.
- Update a legacy orchestration skill to the new section model with completion checklist.

### Troubleshooting
- Missing sections → consult REQUIRED-SECTIONS and fill or flag.
- Conflicting constraints → escalate to requester for confirmation.
- Directory issues → regenerate scaffolds and verify permissions.

### Completion Verification
- [ ] SKILL.md template includes all required sections.
- [ ] Scaffolding provided (examples/tests/resources/references where applicable).
- [ ] Confidence ceiling stated; TODOs captured with owners.
- [ ] Routing guidance back to Skill Builder recorded.

Confidence: 0.70 (ceiling: inference 0.70) - Template routing SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
