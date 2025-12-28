# Agent Creator - Recursive Improvement Addendum

## Purpose

Connect **agent-creator** with the **Recursive Self-Improvement System** to enable:
1. Agent Creator being improved by the recursive loop
2. Agents created by Agent Creator to integrate with improvement system
3. Auditor agents created for recursive improvement

---

## Role in Recursive Loop

```
                    +------------------+
                    |   AGENT CREATOR  |
                    +------------------+
                            |
              +-------------+-------------+
              |             |             |
              v             v             v
        +---------+   +---------+   +---------+
        | Auditor |   | Domain  |   | Core    |
        | Agents  |   | Experts |   | Agents  |
        +---------+   +---------+   +---------+
              |             |
              v             v
        +----------------------------------+
        |    RECURSIVE IMPROVEMENT LOOP    |
        +----------------------------------+
```

**Agent Creator creates the agents that power the recursive loop:**
- prompt-auditor
- skill-auditor
- expertise-auditor
- output-auditor
- domain-expert
- expertise-adversary

---

## Integration Points

### 1. As Improvement Target

Agent Creator itself can be improved by the recursive loop.

```yaml
target_integration:
  auditor: "skill-auditor"  # Agent Creator is a skill
  evaluator: "eval-harness"
  benchmarks:
    - "agent-generation-benchmark-v1"
  regressions:
    - "agent-creator-regression-v1"

  improvement_areas:
    phase_structure:
      current: "5-phase (Phase 0-4)"
      status: "COMPLETED - Phase 0 expertise loading added in v2.0"
    mcp_integration:
      current: "Documented in agent"
      potential: "Auto-validate MCP availability"
    hook_generation:
      current: "Manual specification"
      potential: "Auto-generate from agent purpose"
```

### 2. Creating Improvement-Aware Agents

Agents created by Agent Creator should integrate with the improvement system.

```yaml
improvement_aware_agent:
  required_sections:
    expertise_integration:
      - "Check for domain expertise before action"
      - "Load expertise if available"
      - "Flag discoveries for expertise update"

    self_improvement_hooks:
      - "Track performance metrics"
      - "Report learnings to improvement system"
      - "Support audit by auditor agents"

    memory_integration:
      - "Namespace for agent-specific memory"
      - "Learning delta storage"
      - "Metric tracking"
```

### 3. Creating Auditor Agents

Agent Creator creates the specialized auditor agents for the recursive loop.

```yaml
auditor_agent_template:
  purpose: "Find issues, generate proposals"

  required_capabilities:
    - detection: "Identify issues in target domain"
    - prioritization: "Rank issues by severity"
    - proposal_generation: "Create actionable diffs"
    - validation: "Verify proposals are valid"

  output_format:
    audit_report:
      - issues: "List with severity"
      - proposals: "Actionable changes"
      - metrics: "Quality scores"

  integration:
    - memory: "Store audits in improvement namespace"
    - eval_harness: "Support benchmark testing"
    - bootstrap_loop: "Integrate with improvement cycle"
```

---

## New Agent Template: Improvement-Aware

Add this to agents created for the recursive improvement system:

```markdown
## Improvement System Integration

### Expertise Loading

Before any domain-specific action:
1. Detect domain from task
2. Check for expertise: `.claude/expertise/{domain}.yaml`
3. If exists: Validate and load
4. If missing: Flag for discovery mode

### Performance Tracking

Track these metrics for improvement:
- Task completion rate
- Error frequency
- Validation pass rate
- Learning discoveries

### Learning Reporting

After significant work:
1. Extract learnings
2. Store in memory: `improvement/learnings/{agent}/{timestamp}`
3. Flag for expertise update consideration

### Audit Support

Support auditing by:
- Structured output format
- Clear success criteria
- Measurable quality metrics
- Traceable actions
```

---

## Auditor Agent Generation

### Template: Auditor Agent

```yaml
auditor_agent:
  identity:
    name: "{domain}-auditor"
    category: "foundry/recursive-improvement"
    purpose: "Find issues in {domain}, generate improvement proposals"

  detection_capabilities:
    - "{Domain-specific detection 1}"
    - "{Domain-specific detection 2}"
    - "{Domain-specific detection 3}"

  audit_protocol:
    1. "Structural analysis"
    2. "Quality scoring"
    3. "Issue prioritization"
    4. "Proposal generation"

  output_format:
    audit_report:
      structural_analysis: {...}
      quality_scores: {...}
      issues:
        critical: [...]
        high: [...]
        medium: [...]
      proposals: [...]
      recommendation: "PASS|NEEDS_IMPROVEMENT|REJECT"

  guardrails:
    never:
      - "Accept without thorough analysis"
      - "Generate vague proposals"
      - "Skip failure mode detection"
    always:
      - "Provide specific locations"
      - "Include before/after diffs"
      - "Predict improvement impact"

  integration:
    memory_namespace: "improvement/audits/{domain}/{target}"
    coordinates_with: ["prompt-forge", "skill-forge", "eval-harness"]
```

### Existing Auditor Agents (Created)

| Agent | Location | Purpose |
|-------|----------|---------|
| prompt-auditor | `agents/foundry/recursive-improvement/prompt-auditor.md` | Audit prompts |
| skill-auditor | `agents/foundry/recursive-improvement/skill-auditor.md` | Audit skills |
| expertise-auditor | `agents/foundry/recursive-improvement/expertise-auditor.md` | Audit expertise |
| output-auditor | `agents/foundry/recursive-improvement/output-auditor.md` | Audit outputs |

---

## Eval Harness Integration

### Agent Generation Benchmark

```yaml
agent_generation_benchmark:
  id: "agent-generation-benchmark-v1"

  tests:
    - id: "ag-001"
      input: "Create agent for code review"
      expected:
        - has_identity_section: true
        - has_capabilities: true
        - has_guardrails: true
        - has_memory_integration: true
      scoring:
        completeness: 0.0-1.0
        specificity: 0.0-1.0
        integration: 0.0-1.0

  minimum_passing:
    completeness: 0.8
    specificity: 0.75
    integration: 0.7
```

### Agent Creator Regression

```yaml
agent_creator_regression:
  id: "agent-creator-regression-v1"

  tests:
    - id: "acr-001"
      name: "Identity section present"
      expected: "Output has clear identity"
      must_pass: true

    - id: "acr-002"
      name: "Capabilities defined"
      expected: "Output lists capabilities"
      must_pass: true

    - id: "acr-003"
      name: "Guardrails included"
      expected: "Output has guardrails section"
      must_pass: true

    - id: "acr-004"
      name: "Memory integration specified"
      expected: "Output specifies memory namespace"
      must_pass: true

  failure_threshold: 0
```

---

## Memory Namespaces

| Namespace | Purpose |
|-----------|---------|
| `agent-creator/generations/{id}` | Agents created |
| `agent-creator/auditors/{id}` | Auditor agents created |
| `improvement/commits/agent-creator` | Version history |
| `improvement/audits/agent/{agent}` | Audits of agents |

---

## Safety Constraints

### NEVER:

1. **Create agents that bypass eval harness**
2. **Create agents that modify frozen benchmarks**
3. **Create agents without guardrails**
4. **Create auditors that auto-approve**
5. **Remove improvement integration from agents**

### ALWAYS:

1. **Include improvement integration section**
2. **Specify memory namespaces**
3. **Define measurable outputs**
4. **Support auditing**
5. **Track learning delta**

---

## Workflow Updates

### Standard Agent Creation (enhanced)

```
User Request
    |
    v
Agent Creator
    |
    +--> Standard Agent (with improvement integration)
    |        |
    |        +--> Expertise loading hook
    |        +--> Performance tracking
    |        +--> Learning reporting
    |        +--> Audit support
    |
    +--> Auditor Agent (if requested)
             |
             +--> Detection capabilities
             +--> Proposal generation
             +--> Eval harness integration
```

### Creating Auditor Agents

```
Auditor Request
    |
    v
Agent Creator (auditor template)
    |
    v
New Auditor Agent
    |
    +--> Detection for domain
    +--> Proposal generation
    +--> Memory integration
    +--> Eval harness hooks
```

---

**Version**: 1.0.0
**Last Updated**: 2025-12-15
**Key Constraint**: All created agents must support improvement system integration
