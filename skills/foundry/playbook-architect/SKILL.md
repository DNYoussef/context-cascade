---
name: playbook-architect
description: Design, refactor, and validate operational playbooks with clear phases, triggers, and evidence-backed checkpoints.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Introduced Skill Forge sectioning with explicit guardrails, validation, and completion gates for playbook design.
- Added prompt-architect constraint extraction, ceiling discipline, and structured IO contracts for repeatable playbooks.

## STANDARD OPERATING PROCEDURE

### Purpose
Create actionable playbooks with phased steps, triggers, roles, evidence requirements, and completion criteria that teams can execute consistently.

### Trigger Conditions
- Positive: need a new playbook, refactoring an existing one, aligning multiple teams to a standard procedure.
- Negative/reroute: single prompt rewrites (prompt-architect) or agent creation (agent-creator/agent-creation).

### Guardrails
- Define start/stop triggers and success metrics for each phase.
- Keep outputs English-only with explicit confidence ceilings.
- Include evidence checkpoints and rollback/abort conditions to avoid unsafe execution.
- Make playbooks tool-agnostic unless a tool requirement is explicit.

### Execution Phases
1. **Intake & Constraints**: Capture objective, scope, actors, tools, and risks; classify HARD/SOFT/INFERRED constraints.
2. **Structure**: Lay out phases with entry/exit criteria, roles, and artifacts.
3. **Detailing**: Add step-by-step actions, decision points, and communication cadences.
4. **Validation**: Dry-run or table-top the playbook; record findings, gaps, and ceilings.
5. **Delivery**: Provide the finalized playbook, change log, and adoption guidance.

### Pattern Recognition
- Incident response → emphasize triage, containment, comms, and postmortem steps.
- Release management → focus on pre-flight checks, gates, rollback plans.
- Research/analysis → define evidence collection, synthesis, and decision checkpoints.

### Advanced Techniques
- Embed checklists and timeboxes for high-stress scenarios.
- Provide branching paths for common forks (e.g., severity levels).
- Include "stop the line" rules with authority levels.

### Common Anti-Patterns
- Ambiguous ownership or missing role definitions.
- No rollback/abort conditions.
- Lack of evidence checkpoints or confidence ceilings.

### Practical Guidelines
- Keep steps concise; prefer numbered lists and clear handoffs.
- Provide templates for logs/updates to ensure consistent communication.
- Note prerequisites and environmental assumptions explicitly.

### Cross-Skill Coordination
- Upstream: prompt-architect for clarity; cognitive-lensing for alternative playbook framings.
- Parallel: meta-tools for tool alignment; base-template-generator for any supporting scripts.
- Downstream: agent-selector/agent-creator when playbooks require agent execution; recursive-improvement for continuous tuning.

### MCP Requirements
- Optional memory MCP to store runbooks and lessons learned; tag WHO=playbook-architect-{session}, WHY=skill-execution.

### Input/Output Contracts
```yaml
inputs:
  objective: string  # required goal
  scope: string  # required boundaries
  actors: list[string]  # required roles/owners
  constraints: list[string]  # optional constraints and tools
outputs:
  playbook: file  # phased steps with triggers and checkpoints
  validation_notes: file  # dry-run findings and gaps
  adoption_plan: summary  # rollout steps and responsibilities
```

### Recursive Improvement
- After first execution, run recursive-improvement on feedback to refine phases and guardrails.

### Examples
- Draft an incident response playbook for P1 outages with severity-based branches and comms templates.
- Refine a release playbook to add feature flag rollouts and rollback checkpoints.

### Troubleshooting
- Steps unclear → rewrite with subject-verb-object and explicit owners.
- Playbook too long → modularize by phase and severity.
- Missing safety nets → add abort conditions and rollback steps.

### Completion Verification
- [ ] Phases include entry/exit criteria, roles, and success metrics.
- [ ] Evidence checkpoints and rollback/abort conditions documented.
- [ ] Confidence ceiling stated; validation notes captured.
- [ ] Adoption guidance provided (who uses it, when, and how).

Confidence: 0.70 (ceiling: inference 0.70) - Playbook Architect SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
