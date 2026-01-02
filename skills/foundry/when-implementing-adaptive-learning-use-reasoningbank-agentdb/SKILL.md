---
name: reasoningbank-agentdb
description: Apply ReasoningBank adaptive learning patterns with AgentDB for training, feedback capture, and policy updates.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: agentdb
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rewrote the guidance into Skill Forge required sections with clear learning loops, validation, and ceilings.
- Added prompt-architect constraint capture and MCP tagging for adaptive learning pipelines.

## STANDARD OPERATING PROCEDURE

### Purpose
Guide adaptive learning setups using ReasoningBank with AgentDB, covering data capture, policy updates, evaluation, and safety controls.

### Trigger Conditions
- Positive: building or tuning adaptive learning loops, adding feedback-driven updates, or integrating ReasoningBank with AgentDB.
- Negative/reroute: static semantic search (agentdb-vector-search) or non-AgentDB learning stacks.

### Guardrails
- Enforce data provenance and consent for training data.
- Separate training/eval datasets; avoid feedback loops without validation.
- Keep outputs English-only with explicit confidence ceilings.
- Document rollback and freeze mechanisms for regressions.

### Execution Phases
1. **Design**: Capture objectives, signals, constraints, and safety requirements; classify HARD/SOFT/INFERRED.
2. **Data Pipeline**: Define data ingestion, labeling, and storage schemas in AgentDB; ensure privacy controls.
3. **Learning Loop**: Configure ReasoningBank policies, update cadence, and gating criteria.
4. **Evaluation**: Run offline/online tests with guardrails for regressions; record metrics and ceilings.
5. **Deployment**: Roll out updates with monitoring, rollback triggers, and documentation.

### Pattern Recognition
- Feedback classification tasks → emphasize label quality and disagreement handling.
- Policy tuning → use holdout sets and staged rollout with kill switches.
- Safety-sensitive domains → require human-in-loop checkpoints.

### Advanced Techniques
- Use bandit-style experiments for gradual deployment.
- Capture feature importance and drift signals for monitoring.
- Automate regression alarms tied to AgentDB metrics.

### Common Anti-Patterns
- Updating policies without eval or rollback plans.
- Mixing training and eval data.
- Missing consent or privacy controls on captured data.

### Practical Guidelines
- Version datasets, models, and policies; store metadata in AgentDB.
- Limit update frequency based on risk; document thresholds.
- Keep a change log with timestamps, metrics, and ceilings.

### Cross-Skill Coordination
- Upstream: prompt-architect for clear objectives; recursive-improvement for hypothesis testing.
- Parallel: agentdb-learning for RL-style training; agentdb-optimization for retrieval tuning if needed.
- Downstream: agent-creator embedding updated policies into agents.

### MCP Requirements
- Requires AgentDB storage; tag WHO=reasoningbank-agentdb-{session}, WHY=skill-execution for traceability.

### Input/Output Contracts
```yaml
inputs:
  objective: string  # required
  data_sources: list[string]  # required
  constraints: list[string]  # optional safety/privacy constraints
outputs:
  learning_plan: file  # pipeline design and schedules
  eval_report: file  # metrics, tests, and ceilings
  rollout_plan: summary  # deployment, monitoring, rollback steps
```

### Recursive Improvement
- Feed eval regressions and user feedback into recursive-improvement to refine policies and data quality steps.

### Examples
- Set up adaptive summarization tuning with feedback scoring and staged rollout.
- Configure a classification policy update with drift monitoring and human approval gates.

### Troubleshooting
- Regressions detected → freeze updates, rollback to last good version, and analyze drift.
- Noisy feedback → improve labeling, add consensus rules, or weight trusted signals.
- Slow learning → adjust cadence or expand data coverage.

### Completion Verification
- [ ] Data pipeline defined with privacy and provenance controls.
- [ ] Learning loop configured with eval + rollback plans.
- [ ] Metrics and ceilings recorded; change log updated.
- [ ] Monitoring and feedback routes documented.

Confidence: 0.70 (ceiling: inference 0.70) - ReasoningBank AgentDB SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
