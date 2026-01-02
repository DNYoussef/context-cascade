---
name: agent-selector
description: Select the best-fit specialist agent from the registry using semantic matching, capability scoring, and tool alignment.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Reframed the selector playbook to follow Skill Forge required sections with explicit routing notes and completion checks.
- Added prompt-architect style constraint capture, confidence ceilings, and memory tagging to keep selections auditable.

## STANDARD OPERATING PROCEDURE

### Purpose
Route work to the highest-quality specialist agent by analyzing task intent, constraints, tools, and historical performance.

### Trigger Conditions
- Positive: choosing an agent for a task, validating an existing agent assignment, planning multi-agent workflows.
- Negative/reroute: creating a new agent (agent-creator/agent-creation) or optimizing prompts without agent routing (prompt-architect).

### Guardrails
- Require English outputs with explicit confidence ceilings for the selection rationale.
- Never return a generic agent when a specialized option exists; surface top alternatives with scores.
- Avoid opaque reasoning—show matched capabilities, tools, and decision factors.
- Respect registry integrity: only return agents that exist and are permitted for the task.

### Execution Phases
1. **Intent & Constraint Capture**: Extract domain, phase, tools, risk level, and success criteria; mark hard vs soft constraints.
2. **Candidate Retrieval**: Query registry/memory for agents; narrow by category, tools, and phase.
3. **Scoring & Ranking**: Score by capability match, domain fit, tool alignment, and historical outcomes; include tie-break rules.
4. **Recommendation & Rationale**: Provide selected agent, alternatives, reasoning, and integration notes; state confidence ceiling.
5. **Validation Loop**: If no suitable agent, recommend creation path and log gaps for skill-forge backlog.

### Pattern Recognition
- Tool-constrained tasks → prioritize agents with matching tool whitelists and error-handling experience.
- High-risk domains (security/compliance) → bias toward agents with safety guardrails and audits.
- Multi-phase projects → pick agents aligned to current phase (planning vs build vs test).

### Advanced Techniques
- Use semantic + rules-based scoring to avoid tool-only bias.
- Apply cooldowns for recently failing agents and boost for proven recent runs.
- Capture reason codes for why top alternatives were not chosen.

### Common Anti-Patterns
- Selecting based solely on name similarity.
- Ignoring tool requirements or phase context.
- Omitting confidence ceilings or rationale in the output.

### Practical Guidelines
- Provide 1 primary and 2-3 backup agents with concise reasons and score deltas.
- Include file paths for reproducibility and auditing.
- Encourage small validation task before full delegation when confidence <0.85.

### Cross-Skill Coordination
- Upstream: prompt-architect for refined task descriptions; skill-forge for complete agent metadata.
- Downstream: delivery/ops skills consuming the selected agent; recursive-improvement when selection fails.

### MCP Requirements
- Memory/vector search recommended for registry lookup; tag WHO=agent-selector-{session}, WHY=skill-execution.
- Ensure access controls before suggesting agents tied to sensitive tools.

### Input/Output Contracts
```yaml
inputs:
  task: string  # required description of the work
  domain: string  # optional domain hint
  phase: string  # optional project phase
  tools: list[string]  # optional required tools/MCP servers
outputs:
  primary_agent: object  # name, path, score, capabilities, tools
  alternatives: list[object]  # ranked backups with reasons
  rationale: string  # key decision factors and constraints satisfied
```

### Recursive Improvement
- Feed mis-selections and user feedback into recursive-improvement to tune scoring weights and filters.

### Examples
- Select a backend API agent for an Express+PostgreSQL feature with OpenAPI contract checks.
- Recommend a security review agent for dependency audit with SBOM parsing and CVE triage.

### Troubleshooting
- No match found → relax soft constraints, widen category, or trigger agent creation.
- Multiple top ties → expose tie-break factors (tools, recency, safety posture).
- Agent returned lacks required tool → fail selection and propose alternatives with matching tools.

### Completion Verification
- [ ] Primary agent and backups returned with scores and reasoning.
- [ ] Constraints and tools addressed; registry paths included.
- [ ] Confidence ceiling stated; memory tags applied if MCP used.
- [ ] Escalation path defined when no suitable agent exists.

Confidence: 0.70 (ceiling: inference 0.70) - Selector SOP aligned to Skill Forge structure with prompt-architect ceilings.
