---
name: agent-creation
description: Systematic agent creation using evidence-based prompting principles and 4-phase SOP methodology. Use when creating new specialist agents, refining existing agent prompts, or designing multi-agent systems. Applies Chain-of-Thought, few-shot learning, and role-based prompting. Includes validation scripts, templates, comprehensive tests, and production-ready examples.
---

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- Creating new specialist agents with domain-specific expertise
- Refining existing agent system prompts for better performance
- Designing multi-agent coordination systems
- Implementing role-based agent hierarchies
- Building production-ready agents with embedded domain knowledge

### When NOT to Use This Skill
- For simple one-off tasks that don't need agent specialization
- When existing agents already cover the required domain
- For casual conversational interactions without systematic requirements
- When the task is better suited for a slash command or micro-skill

### Success Criteria
- primary_outcome: "Production-ready agent with optimized system prompt, clear role definition, and validated performance"
- quality_threshold: 0.9
- verification_method: "Agent successfully completes domain-specific tasks with consistent high-quality output, passes validation tests, and integrates with Claude Agent SDK"

### Edge Cases
- case: "Vague agent requirements"
  handling: "Use Phase 1 (Initial Analysis) to research domain, identify patterns, and clarify scope before proceeding"
- case: "Overlapping agent capabilities"
  handling: "Conduct agent registry search, identify gaps vs duplicates, propose consolidation or specialization"
- case: "Agent needs multiple conflicting personas"
  handling: "Decompose into multiple focused agents with clear coordination pattern"

### Skill Guardrails
NEVER:
  - "Create agents without deep domain research (skipping Phase 1 undermines quality)"
  - "Use generic prompts without evidence-based techniques (CoT, few-shot, role-based)"
  - "Skip validation testing (Phase 3) before considering agent production-ready"
  - "Create agents that duplicate existing registry agents without justification"
ALWAYS:
  - "Complete all 4 phases: Analysis -> Prompt Engineering -> Testing -> Integration"
  - "Apply evidence-based prompting: Chain-of-Thought for reasoning, few-shot for patterns, clear role definition"
  - "Validate with diverse test cases and measure against quality criteria"
  - "Document agent capabilities, limitations, and integration points"

### Evidence-Based Execution
self_consistency: "After agent creation, test with same task multiple times to verify consistent outputs and reasoning quality"
program_of_thought: "Decompose agent creation into: 1) Domain analysis, 2) Capability mapping, 3) Prompt architecture, 4) Test design, 5) Validation, 6) Integration"
plan_and_solve: "Plan: Research domain + identify capabilities -> Execute: Build prompts + test cases -> Verify: Multi-run consistency + edge case handling"
<!-- END SKILL SOP IMPROVEMENT -->

# Agent Creation - Systematic Agent Design

Evidence-based agent creation following best practices for prompt engineering and agent specialization.



## 4-Phase Agent Creation SOP

### Phase 1: Specification
- Define agent purpose and domain
- Identify core capabilities needed
- Determine input/output formats
- Specify quality criteria

**Tools**: Use `resources/scripts/generate_agent.sh` for automated generation

### Phase 2: Prompt Engineering
- Apply evidence-based prompting principles
- Use Chain-of-Thought for reasoning tasks
- Implement few-shot learning with examples (2-5 examples)
- Define role and persona clearly

**Reference**: See `references/prompting-principles.md` for detailed techniques

### Phase 3: Testing & Validation
- Test with diverse inputs
- Validate output quality using `resources/scripts/validate_agent.py`
- Measure performance metrics
- Iterate based on results

**Tests**: Run tests from `tests/` directory (basic, specialist, integration)

### Phase 4: Integration
- Define agent coordination protocols
- Establish communication patterns via Memory MCP
- Configure memory and state management
- Deploy with monitoring using Claude-Flow hooks

**Examples**: See `examples/example-1-python-specialist.md` for complete walkthrough



## Evidence-Based Prompting Principles

### 1. Role Definition
Clear agent identity and expertise improves performance by 15-30%

```yaml
role:
  identity: "You are a [Specific Role] with expertise in [Domain]"
  expertise: ["skill-1", "skill-2", "skill-3"]
  responsibilities: ["task-1", "task-2"]
```

### 2. Chain-of-Thought Reasoning
Explicit reasoning steps improve accuracy by 20-40% on complex tasks

```yaml
reasoning_steps:
  - "Step 1: Analyze requirements"
  - "Step 2: Identify solutions"
  - "Step 3: Evaluate trade-offs"
  - "Step 4: Select optimal approach"
```

### 3. Few-Shot Learning
2-5 examples improve performance by 30-50% compared to zero-shot

```yaml
examples:
  - input: "Concrete example input"
    reasoning: "Step-by-step thinking"
    output: "Expected output with explanation"
```

### 4. Plan-and-Solve
Planning before execution reduces errors by 25-35% on complex workflows

```yaml
workflow:
  - name: "Planning Phase"
    steps: ["Understand requirements", "Outline approach"]
  - name: "Execution Phase"
    steps: ["Implement solution", "Handle edge cases"]
```

**Reference**: Complete guide in `references/prompting-principles.md`



## Integration

### Claude Code Task Tool

```javascript
// Spawn agent for parallel execution
Task("Agent Name", "Task description", "category")
```

### Memory MCP

```yaml
integration:
  memory_mcp:
    enabled: true
    tagging_protocol:
      WHO: "agent-name"
      WHEN: "timestamp"
      PROJECT: "project-name"
      WHY: "intent"
```

### Claude-Flow Hooks

```yaml
integration:
  hooks:
    pre_task: ["npx claude-flow@alpha hooks pre-task"]
    post_task: ["npx claude-flow@alpha hooks post-task"]
```



## Quality Assurance

### Validation Checks
- YAML syntax and structure
- Metadata completeness (name, version, category, description)
- Role definition (identity, expertise, responsibilities)
- Capability specifications (primary, secondary, tools)
- Prompting techniques (chain-of-thought, few-shot, role-based)
- Few-shot examples (2+ with input/reasoning/output)
- Quality criteria (success criteria, failure modes, metrics)
- Integration configuration (Memory MCP, Claude-Flow hooks)

### Success Criteria
- Functional correctness > 95%
- Output completeness > 90%
- Test coverage > 80%
- Response time < 30 seconds



## Next Steps

1. **Read Documentation**: Start with `references/prompting-principles.md`
2. **Run Example**: Follow `examples/example-1-python-specialist.md`
3. **Generate Agent**: Use `resources/scripts/generate_agent.sh`
4. **Validate**: Run `resources/scripts/validate_agent.py`
5. **Test**: Execute tests from `tests/` directory
6. **Deploy**: Copy to Claude-Flow and test with Claude Code
7. **Monitor**: Track performance and iterate



## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Generic Prompt Templates** | Copying boilerplate prompts without domain research. Results in agents that lack specialized knowledge and apply generic patterns to domain-specific problems, reducing effectiveness by 50%+. | Complete Phase 1 (Specification) with deep domain research. Study existing codebases, best practices, and domain-specific patterns. Embed this expertise in prompt through examples, constraints, and reasoning steps. |
| **Zero-Shot Agents Without Examples** | Creating agents without few-shot examples. Reduces performance by 30-50% compared to agents with 2-5 concrete examples showing input-output patterns and reasoning. | Always include 2-5 few-shot examples in agent prompts. Examples should cover common cases, edge cases, and demonstrate desired reasoning patterns. Each example must show input, reasoning steps, and output. |
| **Skipping Validation Testing** | Deploying agents without Phase 3 testing against diverse inputs and edge cases. Agents appear to work in demos but fail 40% of the time in production due to untested edge cases. | Run comprehensive Phase 3 validation: test with typical inputs, edge cases, error conditions, and adversarial inputs. Measure success rate, validate against quality criteria (>95% functional correctness). Iterate until thresholds met. |

-----------|---------|----------|
| **Zero-Shot Agents Without Examples** | Creating agents with no few-shot examples in system prompt. Reduces performance by 30-50% compared to agents with 2-5 concrete examples demonstrating desired input-output patterns and reasoning steps. | Include 2-5 few-shot examples covering common cases, edge cases, and desired reasoning patterns. Each example must show input, step-by-step reasoning, and expected output. Validate examples during Phase 3 testing. |
| **Generic Agent Prompts** | Using template prompts without domain-specific research. Results in agents lacking specialized knowledge who apply generic patterns to domain-specific problems. Performance degradation of 50%+ compared to expert agents. | Complete Phase 1 Specification with deep domain research. Study codebases, documentation, best practices. Embed expertise through concrete examples, domain constraints, and specialized reasoning steps. Agent should demonstrate domain mastery, not general capability. |
| **Skipping Validation Testing** | Deploying agents without Phase 3 testing against diverse inputs and edge cases. Agents appear functional in demos but fail 40% of the time in production due to untested scenarios. | Run comprehensive Phase 3 validation: test typical inputs, edge cases, error conditions, adversarial inputs. Measure success rate against quality criteria (>95% functional correctness). Iterate prompt until thresholds met before production deployment. |

---

## Conclusion

Agent creation is not prompt writing, it is systematic engineering. The difference between a casual prompt and a production-ready agent is the application of evidence-based techniques, deep domain research, and rigorous validation. Agents built through the 4-phase SOP consistently achieve 90%+ success rates because they embed expertise rather than rely on the model to figure it out on the fly.

The agent-creation skill transforms vague requirements into specialized agents with clear roles, evidence-based prompts, and validated performance. By combining Chain-of-Thought reasoning, few-shot learning, role definition, and plan-and-solve workflows, it creates agents that don't just follow instructions but reason through problems systematically. This methodology scales from simple specialist agents to complex coordinator agents managing multi-agent workflows.

Use this skill whenever creating new agents or refining existing ones. The upfront investment in systematic design pays exponential dividends: agents that work consistently, handle edge cases gracefully, and integrate seamlessly into the broader agent ecosystem. Build specialists, not generalists. Apply evidence, not intuition. Test rigorously, not casually.