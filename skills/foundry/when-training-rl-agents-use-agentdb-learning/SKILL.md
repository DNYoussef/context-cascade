---
name: agentdb-learning
description: Use AgentDB-supported reinforcement learning workflows for training agents with safe reward handling, evaluation, and deployment controls.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: agentdb
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Translated RL guidance into Skill Forge required sections with explicit safety rails and evaluation gates.
- Added prompt-architect constraint capture, confidence ceilings, and rollout controls for RL agents.

## STANDARD OPERATING PROCEDURE

### Purpose
Train and deploy reinforcement-learning-driven agents using AgentDB for experience storage, evaluation, and controlled rollout.

### Trigger Conditions
- Positive: RL training requests, policy tuning, or logging rollouts with AgentDB-backed storage.
- Negative/reroute: static prompt tuning (prompt-architect) or non-RL retrieval optimization (agentdb-optimization/vector-search).

### Guardrails
- Define reward functions and safety constraints before training.
- Separate train/validation/test splits and avoid reward hacking; monitor for exploitative behaviors.
- Keep outputs English-only with explicit confidence ceilings.
- Require rollback/freeze plans for policies that regress or behave unsafely.

### Execution Phases
1. **Objective & Constraints**: Capture reward signals, environment, success criteria, and safety bounds; classify HARD/SOFT/INFERRED.
2. **Data & Storage**: Configure AgentDB for trajectory storage, metadata tags, and access controls.
3. **Training Plan**: Choose algorithms, hyperparameters, and curriculum strategy; define logging and checkpoints.
4. **Evaluation**: Run offline and online tests with metrics (reward stability, safety violations); document ceilings.
5. **Deployment**: Stage rollout with canaries, monitoring, and rollback; keep changelog of policy versions.

### Pattern Recognition
- Sparse rewards → use shaping or curriculum learning.
- Safety-critical tasks → incorporate constraints/penalties and human oversight.
- Non-stationary environments → schedule periodic retraining and drift monitoring.

### Advanced Techniques
- Off-policy evaluation to reduce risk before deployment.
- Ensemble or policy distillation to stabilize behavior.
- Counterfactual logging for safer experimentation.

### Common Anti-Patterns
- Deploying policies without evaluation or monitoring.
- Unbounded exploration causing unsafe actions.
- Missing audit trail for policy versions.

### Practical Guidelines
- Tag data: WHO=agentdb-learning-{session}, WHY=skill-execution, WHEN=timestamp, ENV=environment.
- Limit learning rate of change in production; gate by metrics and reviews.
- Document reward definitions and known exploits.

### Cross-Skill Coordination
- Upstream: prompt-architect for clear goals; reasoningbank-agentdb for adaptive learning signals.
- Parallel: agentdb-memory for trajectory storage; recursive-improvement for postmortem analysis.
- Downstream: agent-creator embedding trained policies; agent-selector for routing policies.

### MCP Requirements
- Requires AgentDB storage with appropriate permissions; ensure encryption and retention rules for trajectory data.

### Input/Output Contracts
```yaml
inputs:
  objective: string  # required
  environment: string  # required description
  reward_design: string  # required reward definition
  constraints: list[string]  # optional safety constraints
outputs:
  training_plan: file  # algorithms, hyperparameters, checkpoints
  eval_report: file  # metrics, safety findings, ceilings
  rollout_plan: summary  # deployment stages, monitoring, rollback
```

### Recursive Improvement
- Feed evaluation regressions or incidents into recursive-improvement to adjust rewards, hyperparameters, or data quality.

### Examples
- Train an RL policy for API request routing with safety caps and latency targets.
- Tune a recommendation agent with counterfactual logging and staged rollout.

### Troubleshooting
- Reward hacking → adjust reward shaping and add constraints; review logs.
- Performance instability → retune hyperparameters, add regularization, or ensemble.
- Safety violations → freeze deployment, rollback, and add stricter constraints.

### Completion Verification
- [ ] Rewards and constraints defined with audit trail.
- [ ] Training/eval plans executed; metrics and ceilings recorded.
- [ ] Rollout/rollback plan documented with monitoring hooks.
- [ ] Policy versions and changelog updated.

Confidence: 0.70 (ceiling: inference 0.70) - AgentDB learning SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
