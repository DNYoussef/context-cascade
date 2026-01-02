---
name: skill-creator-agent
description: Pair skills with specialist agents, generating both the skill spec and the agent system prompt with validation and routing notes.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Reorganized the skill into the Skill Forge section pattern and added joint outputs for skill specs and agents.
- Applied prompt-architect ceilings, constraint extraction, and adversarial validation to both artifacts.

## STANDARD OPERATING PROCEDURE

### Purpose
Create skills that come packaged with a dedicated specialist agent, including SKILL.md content, agent prompt, and integration hooks for registry use.

### Trigger Conditions
- Positive: request to build a reusable skill that relies on a specialist agent, or to retrofit an existing skill with a dedicated agent.
- Negative/reroute: generic prompt tuning (prompt-architect), pure skill scaffolding (skill-builder), or standalone agent creation (agent-creator).

### Guardrails
- Deliver both artifacts: SKILL.md and agent spec with frontmatter; no status-only responses.
- Use English outputs with explicit confidence ceilings.
- Ensure agent scope matches skill scope; avoid duplicated capabilities.
- Run at least one validation scenario that exercises the skill+agent pair.

### Execution Phases
1. **Scoping**: Capture skill purpose, triggers, constraints, and domain; classify HARD/SOFT/INFERRED.
2. **Skill Drafting**: Author SKILL.md with SOP, guardrails, integrations, and IO contracts following Skill Forge.
3. **Agent Drafting**: Create agent prompt, tools, and refusal policy aligned to the skill.
4. **Validation**: Test the pair together (happy + edge cases) and record evidence with ceilings.
5. **Delivery**: Provide artifacts, routing metadata, and next-step improvements.

### Pattern Recognition
- Tool-driven skills → agent should manage tool orchestration and error handling.
- Review/analysis skills → agent must enforce evidence and ceiling discipline.
- Integration-heavy skills → include latency and timeout guidance in both artifacts.

### Advanced Techniques
- Use few-shot examples shared between skill and agent for consistency.
- Add capability tags so agent-selector can route correctly.
- Capture reusable snippets for meta-tools to compose in other skills.

### Common Anti-Patterns
- Skill and agent scopes diverge, causing confusion.
- Missing tests for the combined flow.
- Absent confidence ceilings or unclear output formats.

### Practical Guidelines
- Keep the agent persona pragmatic; focus on behaviors and contracts.
- Explicitly document inputs/outputs and refusal criteria in both artifacts.
- Provide registry path suggestions and tagging.

### Cross-Skill Coordination
- Upstream: prompt-architect for clarity; skill-builder/skill-forge for structure.
- Downstream: agent-selector for routing; recursive-improvement for ongoing tuning; meta-tools for tool wiring.

### MCP Requirements
- Document any MCP/tool dependencies and tags; tag WHO=skill-creator-agent-{session}, WHY=skill-execution if memory used.

### Input/Output Contracts
```yaml
inputs:
  skill_goal: string  # required objective
  domain: string  # required domain or category
  tools: list[string]  # optional tools/MCP servers
  constraints: list[string]  # optional constraints
outputs:
  skill_spec: file  # SKILL.md content
  agent_spec: file  # agent prompt with frontmatter
  validation: file  # tests and results for the pair
```

### Recursive Improvement
- Use recursive-improvement on both artifacts together; stop when deltas < 2% or risks logged.

### Examples
- Build a log-analysis skill with an observability agent handling query composition and summarization.
- Pair a security-advisory skill with an agent that enforces CVE evidence and refusal policy.

### Troubleshooting
- Agent oversteps scope → tighten persona and refusal rules.
- Skill unclear → rerun constraint extraction and simplify outputs.
- Tool errors → add retries and error handling in agent prompt; document limits in skill.

### Completion Verification
- [ ] SKILL.md and agent spec delivered with aligned scope.
- [ ] Validation evidence recorded with ceilings.
- [ ] Tool/MCP dependencies documented; routing metadata provided.
- [ ] Examples provided demonstrating combined use.

Confidence: 0.70 (ceiling: inference 0.70) - Skill Creator Agent SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
