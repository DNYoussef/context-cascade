---
name: recursive-improvement
description: Drive iterative refinement loops with evidence capture, evaluation checkpoints, and stop conditions for skills, prompts, or agents.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Reworked the skill into Skill Forge required sections with explicit triggers, stop conditions, and evidence logging.
- Added prompt-architect ceiling discipline and contract-style IO to keep iterations auditable.

## STANDARD OPERATING PROCEDURE

### Purpose
Manage recursive improvement cycles that collect failures, propose targeted changes, validate them, and stop when marginal gains level off.

### Trigger Conditions
- Positive: iterative hardening of skills/prompts/agents, regression triage, A/B comparisons, or postmortem action items.
- Negative/reroute: net-new prompt design (prompt-architect/prompt-forge) or new skill scaffolding (skill-forge/skill-builder).

### Guardrails
- Define stop criteria up front (delta threshold, timebox, risk acceptance) to avoid infinite loops.
- Capture evidence for each iteration: inputs, changes, tests, and results with confidence ceilings.
- Keep outputs in English; avoid hidden reasoning.
- Do not silently discard failed experiments—record them for future avoidance.

### Execution Phases
1. **Intake**: Identify artifact to improve, goals, constraints, baseline metrics, and stop criteria; classify constraints as HARD/SOFT/INFERRED.
2. **Hypothesis**: Propose targeted changes addressing failures or goals; prioritize by impact.
3. **Apply & Test**: Implement changes, run validation (happy/edge/adversarial), and log results with ceilings.
4. **Assess**: Compare metrics vs baseline; decide to continue, pivot, or stop based on delta.
5. **Package**: Summarize iterations, residual risks, and recommended next steps.

### Pattern Recognition
- Quality drift → focus on regression tests and schema tightening.
- Safety issues → add guardrails, refusals, and escalation rules.
- Performance/latency complaints → simplify prompts and reduce tool calls.

### Advanced Techniques
- Use multi-armed bandit style sampling for competing variants with limited budget.
- Apply self-consistency or debate to stress-test high-risk changes.
- Snapshot checkpoints so reverting is easy when metrics regress.

### Common Anti-Patterns
- Iterating without baseline metrics.
- Changing multiple variables simultaneously, making results ambiguous.
- Ignoring ceiling discipline or failing to log evidence.

### Practical Guidelines
- Limit each iteration to one or two focused hypotheses.
- Keep a changelog with timestamps, metrics, and confidence statements.
- Escalate to domain specialists when improvements stall.

### Cross-Skill Coordination
- Upstream: prompt-architect/prompt-forge to clarify artifacts under test.
- Parallel: cognitive-lensing to unlock new hypotheses.
- Downstream: skill-forge/agent-creator to bake improvements into canonical docs.

### MCP Requirements
- Optional memory/vector MCP to store iteration history; tag WHO=recursive-improvement-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  target: string  # required artifact to improve
  goals: list[string]  # required goals/metrics
  constraints: list[string]  # optional constraints
  stop_conditions: object  # required thresholds/timebox
outputs:
  iterations: list[object]  # steps taken, tests, outcomes, ceilings
  recommendation: summary  # continue/stop with rationale
  artifacts: list[file]  # updated files if applicable
```

### Recursive Improvement
- Meta: apply this SOP to itself; stop when improvement delta < 2% or risks documented.

### Examples
- Harden a prompt that occasionally hallucinates by tightening schema and adding refusals.
- Improve a code-generation skill by adding edge-case tests and measuring deltas.

### Troubleshooting
- No improvement after multiple cycles → revisit hypotheses or broaden search (new lenses/tools).
- Metrics regressing → revert to last good checkpoint and reassess constraints.
- Timebox exceeded → summarize current best variant and open risks.

### Completion Verification
- [ ] Stop conditions defined and respected.
- [ ] Iteration logs include tests, results, and ceilings.
- [ ] Recommendation provided with residual risks.
- [ ] Artifacts updated or explicitly unchanged.

Confidence: 0.70 (ceiling: inference 0.70) - Recursive Improvement SOP rewritten with Skill Forge structure and prompt-architect ceilings.
