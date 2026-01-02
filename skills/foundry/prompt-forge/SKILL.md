---
name: prompt-forge
description: Generate and iteratively harden prompts and templates using frozen evaluation harnesses and adversarial validation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Aligned the forge SOP with Skill Forge required sections, adding explicit validation gates and delivery artifacts.
- Incorporated prompt-architect confidence ceilings, dual-pass refinement, and frozen eval harness references.

## STANDARD OPERATING PROCEDURE

### Purpose
Create or improve prompts/templates with systematic iteration, evaluation harnesses, and adversarial checks to ensure reliability and reuse.

### Trigger Conditions
- Positive: generating a new prompt/template, improving an existing prompt, or hardening prompts for CI/automation.
- Negative/reroute: broad prompt clarity work (prompt-architect) or full skill/agent creation (skill-forge/agent-creator).

### Guardrails
- Always pair generation with validation: run harness tests (happy, edge, adversarial) and record results.
- Keep outputs in English with explicit confidence ceilings and changelogs of iteration deltas.
- Avoid one-pass generation; require at least two refinement cycles or document why not.
- Respect template scoping; do not mix unrelated responsibilities.

### Execution Phases
1. **Intake**: Capture goal, audience, constraints, success criteria, and target format; classify constraints as HARD/SOFT/INFERRED.
2. **Drafting**: Produce an initial template with structure, inputs/outputs, refusal policy, and examples.
3. **Evaluation**: Run frozen harness cases and adversarial probes; record metrics and failures.
4. **Refinement**: Address failures, adjust structure, calibrate ceilings; repeat until pass or documented residual risk.
5. **Delivery**: Provide final prompt, test artifacts, usage notes, and confidence statement.

### Pattern Recognition
- Deterministic automation prompts → enforce strict formats and refusal rules.
- Creative prompts → use guardrails for IP/safety and clear tone guidance.
- Review/checklist prompts → add scoring rubrics and evidence expectations.

### Advanced Techniques
- Use self-play (two-model debate) for risky domains to expose weaknesses.
- Apply contrastive examples to narrow scope and improve refusal posture.
- Store successful patterns in references for reuse by skill-forge and agent-creator.

### Common Anti-Patterns
- Shipping prompts without evaluation evidence.
- Mixing multiple intents in one template.
- Omitting confidence ceilings or iteration logs.

### Practical Guidelines
- Keep templates modular; separate context, instructions, and output schema.
- Include quick-start examples and boundary cases.
- Maintain a small changelog of iteration deltas with dates/metrics.

### Cross-Skill Coordination
- Upstream: prompt-architect for clarity; base-template-generator for structural scaffolds when code is involved.
- Downstream: skill-forge/agent-creator embedding the prompt; recursive-improvement for ongoing tuning.

### MCP Requirements
- Optional memory/vector MCP to store harness results; tag WHO=prompt-forge-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  goal: string  # required description of what the prompt must achieve
  audience: string  # required target user/agent
  constraints: list[string]  # optional constraints and policies
  format: string  # optional output format
outputs:
  prompt_template: string  # final prompt/template text
  eval_report: file  # harness results and adversarial findings
  change_log: file  # iteration deltas and confidence ceilings
```

### Recursive Improvement
- Feed harness failures into recursive-improvement to propose targeted edits until metrics meet thresholds or risk is documented.

### Examples
- Forge a CI-ready code-review prompt with security and performance rubrics.
- Improve a research-synthesis prompt with source-citation enforcement and ceiling discipline.

### Troubleshooting
- Harness failures → prioritize fixes by severity and rerun critical cases.
- Overly long prompts → modularize sections and remove redundancy.
- Drift in outputs → tighten schema, add examples, and reassert refusal rules.

### Completion Verification
- [ ] Draft + refined prompt delivered with changelog.
- [ ] Evaluation harness results recorded (happy/edge/adversarial).
- [ ] Confidence ceiling stated; residual risks documented.
- [ ] Usage notes and output schema included.

Confidence: 0.70 (ceiling: inference 0.70) - Prompt Forge SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
