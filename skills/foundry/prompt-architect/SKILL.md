---
name: prompt-architect
description: Optimize prompts for clarity, structure, determinism, and epistemic hygiene with explicit confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rebuilt the SOP using the Skill Forge section cadence and added structure-first guardrails for outputs and contracts.
- Elevated the confidence ceiling rule into every section and added iterative refinement plus adversarial validation steps.

## STANDARD OPERATING PROCEDURE

### Purpose
Rewrite or design prompts so they are unambiguous, constraint-aware, and validated against epistemic risk with documented ceilings.

### Trigger Conditions
- Positive: "optimize prompt", "improve my prompt", "design a prompt", "self-consistency check".
- Negative/reroute: full skill/agent creation (skill-forge/agent-creator), micro-skill creation (micro-skill-creator).

### Guardrails
- **Confidence ceiling is mandatory** in every output: format `Confidence: X.XX (ceiling: TYPE Y.YY)`.
- Use English-only user-facing outputs; keep VCL/notation internal.
- Run at least two passes: structural pass then epistemic pass; record deltas.
- Separate HARD vs SOFT vs INFERRED constraints and label sources.
- Avoid overclaiming; do not exceed ceiling tables (inference/report 0.70, research 0.85, observation/definition 0.95).

### Execution Phases
1. **Intent Analysis**: Identify task type, audience, success criteria, and constraints (hard/soft/inferred).
2. **Structural Rewrite**: Clarify roles, steps, IO formats, and refusal rules; remove ambiguity.
3. **Epistemic Audit**: Calibrate confidence ceilings, add evidence hooks, and flag assumptions needing confirmation.
4. **Validation**: Check constraint coverage, run example scenarios (happy + edge), and ensure deterministic outputs.
5. **Delivery**: Present optimized prompt, constraint list, rationale, and ceilings; note open questions.

### Pattern Recognition
- Code generation prompts → emphasize inputs, outputs, examples, and safety (no destructive actions).
- Analysis/explanation prompts → require evidence tags and ceiling statements.
- Planning prompts → use numbered steps, checkpoints, and success metrics.

### Advanced Techniques
- Apply self-consistency (multiple drafts + convergence) for reasoning-heavy tasks.
- Use contrastive examples to bound scope and refusals.
- Add deterministic formatting (JSON, tables) when downstream parsing is needed.

### Common Anti-Patterns
- Single-pass rewrite without epistemic audit.
- Confidence inflation or missing ceilings.
- Ambiguous pronouns or missing actor/subject.

### Practical Guidelines
- Keep optimized prompts concise but explicit about roles, inputs, outputs, and refusal policy.
- Surface INFERRED constraints for confirmation before finalizing.
- Include reminders to avoid leaking internal notation.

### Cross-Skill Coordination
- Upstream: cognitive-lensing for alternative frames; skill-builder for structure scaffolds.
- Downstream: skill-forge/agent-creator to embed optimized prompts; recursive-improvement for ongoing tuning.

### MCP Requirements
- Optional memory/vector MCP for recalling prior optimizations; tag WHO=prompt-architect-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  source_prompt: string  # required original prompt
  context: string  # optional domain/context
  constraints: list[string]  # optional constraints
  audience: string  # optional user/agent audience
outputs:
  optimized_prompt: string  # rewritten prompt ready for use
  constraints_documented: object  # HARD/SOFT/INFERRED lists with sources
  validation_notes: summary  # tests run, gaps, and ceilings
```

### Recursive Improvement
- Use recursive-improvement when prompts still produce drift or low confidence; iterate until delta < 2% or risks logged.

### Examples
- Optimize a code-review prompt to enforce security, performance, and diff-only outputs with ceilings.
- Rewrite a research-summary prompt with HARD source-citation rules and INFERRED constraints flagged for confirmation.

### Troubleshooting
- Output remains verbose → tighten role instructions and output format.
- Hallucinated certainty → lower ceilings and add evidence requirements.
- Missing constraints → re-run extraction and confirm INFERRED items with requester.

### Completion Verification
- [ ] Constraints captured as HARD/SOFT/INFERRED with sources.
- [ ] Structural and epistemic passes completed with noted deltas.
- [ ] Optimized prompt delivered with deterministic format where needed.
- [ ] Confidence ceiling stated and validation notes recorded.

Confidence: 0.70 (ceiling: inference 0.70) - Prompt Architect SOP rewritten with Skill Forge cadence and enforced ceilings.
