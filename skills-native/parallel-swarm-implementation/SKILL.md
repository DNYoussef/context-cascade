---
name: parallel-swarm-implementation
description: Loop 2 of the Three-Loop Integrated Development System. META-SKILL that dynamically compiles Loop 1 plans into agent+skill execution graphs. Queen Coordinator selects optimal agents from 86-agent registry and assigns skills (when available) or custom instructions. 9-step swarm with theater detection and reality validation. Receives plans from research-driven-planning, feeds to cicd-intelligent-recovery. Use for adaptive, theater-free implementation.
---

## Orchestration Skill Guidelines

### When to Use This Skill
- **Parallel multi-agent execution** requiring concurrent task processing
- **Complex implementation** with 6+ independent tasks
- **Theater-free development** requiring 0% tolerance validation
- **Dynamic agent selection** from 86+ agent registry
- **High-quality delivery** needing Byzantine consensus validation

### When NOT to Use This Skill
- **Single-agent tasks** with no parallelization benefit
- **Simple sequential work** completing in <2 hours
- **Planning phase** (use research-driven-planning first)
- **Trivial changes** to single files

### Success Criteria
- **Agent+skill matrix generated** with optimal assignments
- **Parallel execution successful** with 8.3x speedup achieved
- **Theater detection passes** with 0% theater detected
- **Integration tests pass** at 100% rate
- **All agents complete** with no orphaned workers

### Edge Cases to Handle
- **Agent failures** - Implement agent health monitoring and replacement
- **Task timeout** - Configure per-task timeout with escalation
- **Consensus failure** - Have fallback from Byzantine to weighted consensus
- **Resource exhaustion** - Limit max parallel agents, queue excess
- **Conflicting outputs** - Implement merge conflict resolution strategy

### Guardrails (NEVER Violate)
- **NEVER lose agent state** - Persist agent progress to memory continuously
- **ALWAYS track swarm health** - Monitor all agent statuses in real-time
- **ALWAYS validate consensus** - Require 4/5 agreement for theater detection
- **NEVER skip theater audit** - Zero tolerance, any theater blocks merge
- **ALWAYS cleanup workers** - Terminate agents on completion/failure

### Evidence-Based Validation
- **Check all agent statuses** - Verify each agent completed successfully
- **Validate parallel execution** - Confirm tasks ran concurrently, not sequentially
- **Measure speedup** - Calculate actual speedup vs sequential baseline
- **Audit theater detection** - Run 6-agent consensus, verify 0% detection
- **Verify integration** - Execute sandbox tests, confirm 100% pass rate


# Parallel Swarm Implementation (Loop 2) - META-SKILL

## Purpose

**META-SKILL ORCHESTRATOR** that dynamically compiles Loop 1 planning packages into executable agent+skill graphs, then coordinates theater-free parallel implementation.

## Specialist Agent Coordination

I am **Queen Coordinator (Seraphina)** orchestrating the "swarm compiler" pattern.

**Meta-Skill Architecture**:
1. **Analyze** Loop 1 planning package
2. **Select** optimal agents from 86-agent registry per task
3. **Assign** skills to agents (when skills exist) OR generate custom instructions
4. **Create** agent+skill assignment matrix
5. **Execute** dynamically based on matrix with continuous monitoring
6. **Validate** theater-free execution through multi-agent consensus

**Methodology** (9-Step Adaptive SOP):
1. **Initialization**: Queen-led hierarchical topology with dual memory
2. **Analysis**: Queen analyzes Loop 1 plan and creates agent+skill matrix
3. **MECE Validation**: Ensure tasks are Mutually Exclusive, Collectively Exhaustive
4. **Dynamic Deployment**: Spawn agents with skills OR custom instructions per matrix
5. **Theater Detection**: 6-agent consensus validation (0% tolerance)
6. **Integration**: Sandbox testing until 100% working
7. **Documentation**: Auto-sync with implementation
8. **Test Validation**: Reality check all tests
9. **Completion**: Package for Loop 3

**Integration**: Loop 2 of 3. Receives → `research-driven-planning` (Loop 1), Feeds → `cicd-intelligent-recovery` (Loop 3).

## Input Contract

```yaml
input:
  loop1_planning_package: path (required)
    # Location: .claude/.artifacts/loop1-planning-package.json
    # Must include: specification, research, planning, risk_analysis

  execution_options:
    max_parallel_agents: number (default: 11, range: 5-20)
      # Concurrent agents (more = faster but higher coordination cost)
    theater_tolerance: number (default: 0, range: 0-5)
      # Percentage of theater allowed (0% recommended)
    sandbox_validation: boolean (default: true)
      # Execute code in sandbox to prove functionality
    integration_threshold: number (default: 100, range: 80-100)
      # Required integration test pass rate

  agent_preferences:
    prefer_skill_based: boolean (default: true)
      # Use existing skills when available vs. custom instructions
    agent_registry: enum[claude-flow-86, custom] (default: claude-flow-86)
      # Which agent ecosystem to use
```

## Output Contract

```yaml
output:
  agent_skill_matrix:
    total_tasks: number
    skill_based_agents: number  # Agents using existing skills
    custom_instruction_agents: number  # Agents with ad-hoc instructions
    matrix_file: path  # .claude/.artifacts/agent-skill-assignments.json

  implementation:
    files_created: array[path]
    tests_coverage: number  # Target: ≥90%
    theater_detected: number  # Target: 0
    sandbox_validation: boolean  # Target: true

  quality_metrics:
    integration_test_pass_rate: number  # Target: 100%
    functionality_audit_pass: boolean
    theater_audit_pass: boolean
    code_review_score: number (0-100)

  integration:
    delivery_package: path  # loop2-delivery-package.json
    memory_namespace: string  # integration/loop2-to-loop3
    ready_for_loop3: boolean
```

## Step 1: Queen Analyzes & Creates Agent+Skill Matrix (META-ORCHESTRATION)

**Objective**: Queen Coordinator reads Loop 1 plan and dynamically generates agent+skill assignment matrix.

### Execute Queen's Meta-Analysis SOP

**Agent**: Queen Coordinator (Seraphina) - `hierarchical-coordinator`

```javascript
// STEP 1: META-ANALYSIS - Queen Creates Agent+Skill Assignment Matrix
// This is the "swarm compiler" phase

[Single Message - Queen Meta-Orchestration]:
  Task("Queen Coordinator (Seraphina)",
    `MISSION: Compile Loop 1 planning package into executable agent+skill graph.

    PHASE 1: LOAD LOOP 1 CONTEXT
    - Load planning package: .claude/.artifacts/loop1-planning-package.json
    - Extract: MECE task breakdown, research recommendations, risk mitigations
    - Parse: $(jq '.planning.enhanced_plan' .claude/.artifacts/loop1-planning-package.json)

    PHASE 2: TASK ANALYSIS
    For each task in Loop 1 plan:
    1. Identify task type: backend, frontend, database, testing, documentation, infrastructure
    2. Determine complexity: simple (1 agent), moderate (2-3 agents), complex (4+ agents)
    3. Extract required capabilities from task description
    4. Apply Loop 1 research recommendations for technology/library selection
    5. Apply Loop 1 risk mitigations as constraints

    PHASE 3: AGENT SELECTION (from 86-agent registry)
    For each task:
    1. Match task type to agent type:
       - backend tasks → backend-dev, system-architect
       - testing tasks → tester, tdd-london-swarm
       - quality tasks → theater-detection-audit, functionality-audit, code-review-assistant
       - docs tasks → api-docs, docs-writer
    2. Select optimal agent based on:
       - Agent capabilities matching task requirements
       - Agent availability (workload balancing)
       - Agent specialization score

    PHASE 4: SKILL ASSIGNMENT (key meta-skill decision)
    For each agent assignment:
    1. Check if specialized skill exists for this task type:
       - Known skills: tdd-london-swarm, theater-detection-audit, functionality-audit,
         code-review-assistant, api-docs, database-schema-design, etc.
    2. If skill exists:
       - useSkill: <skill-name>
       - customInstructions: Context-specific parameters for skill
    3. If NO skill exists:
       - useSkill: null
       - customInstructions: Detailed instructions from Loop 1 + Queen's guidance

    PHASE 5: GENERATE ASSIGNMENT MATRIX
    Create .claude/.artifacts/agent-skill-assignments.json:
    {
      "project": "<from Loop 1>",
      "loop1_package": "integration/loop1-to-loop2",
      "tasks": [
        {
          "taskId": "string",
          "description": "string",
          "taskType": "enum[backend, frontend, database, test, quality, docs, infrastructure]",
          "complexity": "enum[simple, moderate, complex]",
          "assignedAgent": "string (from 86-agent registry)",
          "useSkill": "string | null",
          "customInstructions": "string (detailed if useSkill is null, contextual if using skill)",
          "priority": "enum[low, medium, high, critical]",
          "dependencies": ["array of taskIds"],
          "loop1_research": "relevant research findings",
          "loop1_risk_mitigation": "relevant risk mitigations"
        }
      ],
      "parallelGroups": [
        {
          "group": number,
          "tasks": ["array of taskIds"],
          "reason": "why these can execute in parallel"
        }
      ],
      "statistics": {
        "totalTasks": number,
        "skillBasedAgents": number,
        "customInstructionAgents": number,
        "uniqueAgents": number,
        "estimatedParallelism": "string (e.g., '3 groups, 8.3x speedup')"
      }
    }

    PHASE 6: OPTIMIZATION
    1. Identify independent tasks for parallel execution
    2. Group dependent tasks into sequential phases
    3. Balance agent workload (no agent handles >3 tasks simultaneously)
    4. Identify critical path (longest dependency chain)
    5. Suggest topology adjustments if needed

    VALIDATION CHECKPOINTS:
    - All Loop 1 tasks have agent assignments
    - No task is assigned to non-existent agent
    - Skill-based assignments reference real skills
    - Custom instructions are detailed and actionable
    - MECE compliance: no overlapping tasks, all requirements covered
    - Dependencies are acyclic (no circular deps)

    OUTPUT:
    1. Store matrix: .claude/.artifacts/agent-skill-assignments.json
    2. Memory store: npx claude-flow@alpha memory store 'agent_assignments' "$(cat .claude/.artifacts/agent-skill-assignments.json)" --namespace 'swarm/coordination'
    3. Generate execution plan summary
    4. Report: skill-based vs custom-instruction breakdown
    `,
    "hierarchical-coordinator")
```

**Evidence-Based Techniques Applied**:
- **Program-of-Thought**: Explicit 6-phase analysis (load → analyze → select → assign → generate → optimize)
- **Meta-Reasoning**: Queen reasons about which agents should use skills vs. custom instructions
- **Validation Checkpoints**: MECE compliance, dependency validation, assignment completeness

### Queen's Decision: Skill vs. Custom Instructions

**Decision Tree**:
```
For each task:
  Does a specialized skill exist?
    YES →
      useSkill: <skill-name>
      customInstructions: Context from Loop 1 (brief)
      Benefit: Reusable SOP, proven patterns

    NO →
      useSkill: null
      customInstructions: Detailed instructions from Queen + Loop 1
      Benefit: Handles novel tasks, fully adaptive
```

**Example Assignment Matrix** (Authentication System):
```json
{
  "project": "User Authentication System",
  "tasks": [
    {
      "taskId": "task-001",
      "description": "Implement JWT authentication endpoints",
      "taskType": "backend",
      "assignedAgent": "backend-dev",
      "useSkill": null,
      "customInstructions": "Implement JWT auth using jsonwebtoken library per Loop 1 research recommendation. Create endpoints: /auth/login (email+password → JWT), /auth/refresh (refresh token → new JWT), /auth/logout (invalidate refresh token). Apply defense-in-depth token validation per Loop 1 risk mitigation: 1) Validate token signature, 2) Check expiry, 3) Verify user still exists, 4) Check token not in revocation list. Store in src/auth/jwt.ts. Use TypeScript with strict typing.",
      "priority": "critical",
      "loop1_research": "Library recommendation: jsonwebtoken (10k+ stars, active maintenance)",
      "loop1_risk_mitigation": "Defense-in-depth validation (4 layers)"
    },
    {
      "taskId": "task-002",
      "description": "Create mock-based unit tests for JWT",
      "taskType": "test",
      "assignedAgent": "tester",
      "useSkill": "tdd-london-swarm",
      "customInstructions": "Apply tdd-london-swarm skill (London School TDD) to JWT authentication endpoints. Mock all external dependencies: database, token library, time service. Test scenarios: successful login, invalid credentials, expired token, refresh flow, logout. Target 90% coverage per Loop 1 requirement.",
      "priority": "high",
      "dependencies": ["task-001"]
    },
    {
      "taskId": "task-003",
      "description": "Theater detection scan",
      "taskType": "quality",
      "assignedAgent": "theater-detection-audit",
      "useSkill": "theater-detection-audit",
      "customInstructions": "Apply theater-detection-audit skill to scan for: completion theater (TODOs marked done, empty functions), mock theater (100% mocks with no integration validation), test theater (meaningless assertions). Compare against Loop 2 baseline. Zero tolerance - any theater blocks merge.",
      "priority": "critical",
      "dependencies": ["task-001", "task-002"]
    },
    {
      "taskId": "task-004",
      "description": "Sandbox validation",
      "taskType": "quality",
      "assignedAgent": "functionality-audit",
      "useSkill": "functionality-audit",
      "customInstructions": "Apply functionality-audit skill. Execute authentication endpoints in isolated sandbox. Test with realistic inputs: valid credentials, SQL injection attempts, XSS payloads. Verify tokens are valid JWTs. Prove functionality is genuine. Generate validation report.",
      "priority": "critical",
      "dependencies": ["task-001"]
    }
  ],
  "parallelGroups": [
    {"group": 1, "tasks": ["task-001"], "reason": "Foundation - must complete first"},
    {"group": 2, "tasks": ["task-002", "task-004"], "reason": "Independent quality checks"},
    {"group": 3, "tasks": ["task-003"], "reason": "Final validation after all implementations"}
  ],
  "statistics": {
    "totalTasks": 4,
    "skillBasedAgents": 3,
    "customInstructionAgents": 1,
    "uniqueAgents": 4,
    "estimatedParallelism": "3 groups, 2.5x speedup"
  }
}
```

**Validation Checkpoint**: Assignment matrix must pass MECE validation and dependency check.

**Output**: `.claude/.artifacts/agent-skill-assignments.json` with complete agent+skill graph

## Integration with Loop 3 (CI/CD Quality)

After Loop 2 completes, **automatically transition to Loop 3**:

```bash
"Execute cicd-intelligent-recovery skill using the delivery package from Loop 2.
Load implementation data from: .claude/.artifacts/loop2-delivery-package.json
Memory namespace: integration/loop2-to-loop3"
```

Loop 3 will:
1. Load Loop 2 delivery package and agent+skill matrix
2. Use matrix to understand implementation decisions
3. Apply intelligent fixes if CI/CD tests fail
4. Feed failure patterns back to Loop 1 for future pre-mortem

-----|----------------|---------------------|
| Agent Selection | Manual, ad-hoc | Dynamic from 86-agent registry |
| Skill Usage | Inconsistent | Adaptive (skill when available, custom otherwise) |
| Parallelism | Limited (1-3 devs) | High (11 parallel agents, 8.3x) |
| Theater Detection | None | 6-agent consensus (0% tolerance) |
| Integration | Manual, slow | Automated loop (100% success) |

## Troubleshooting

### Queen Can't Find Appropriate Skill

**Symptom**: Task assigned to agent with useSkill: null when skill might exist
**Diagnosis**: Queen's skill registry incomplete
**Fix**:
```bash
# Update Queen's skill registry
jq '.available_skills += ["new-skill-name"]' \
  .claude/.artifacts/skill-registry.json > tmp.json && mv tmp.json .claude/.artifacts/skill-registry.json

# Re-run Queen analysis
Task("Queen Coordinator", "Re-analyze with updated skill registry...", "hierarchical-coordinator")
```

### Theater Detection False Positive

**Symptom**: Valid code flagged as theater
**Diagnosis**: Need higher consensus threshold
**Fix**:
```bash
# Require 5/5 agreement (stricter) instead of 4/5
# Update Byzantine consensus threshold in Step 5
```

### Integration Loop Not Converging

**Symptom**: Tests still failing after multiple iterations
**Diagnosis**: Fundamental implementation issue, not fixable in loop
**Fix**:
```bash
# Escalate to Loop 3
echo "⚠️ Integration loop failed to converge"
echo "Transitioning to Loop 3 (cicd-intelligent-recovery) for deep analysis"
# Loop 3 will apply Gemini + 7-agent analysis + graph-based root cause
```

## Memory Namespaces

Loop 2 uses these memory locations:

| Namespace | Purpose | Producers | Consumers |
|-----------|---------|-----------|-----------|
| `integration/loop1-to-loop2` | Loop 1 planning package | Loop 1 | Queen Coordinator |
| `swarm/coordination` | Agent+skill assignment matrix | Queen Coordinator | All agents |
| `swarm/realtime` | Real-time agent communication | All agents | Queen, agents |
| `swarm/persistent` | Cross-session state | All agents | Loop 3 |
| `integration/loop2-to-loop3` | Delivery package for Loop 3 | Step 9 | Loop 3 |

**Status**: Production-Ready Meta-Skill with Dynamic Agent+Skill Selection
**Version**: 2.0.0 (Optimized with Meta-Skill Architecture)
**Loop Position**: 2 of 3 (Implementation)
**Integration**: Receives Loop 1, Feeds Loop 3
**Agent Coordination**: Dynamic selection from 86-agent registry with skill-based OR custom instructions
**Key Innovation**: "Swarm Compiler" pattern - compiles plans into executable agent+skill graphs
## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Hardcoded Agent Assignments** | Agent+skill assignments baked into skill code. Every project uses same 6 agents regardless of task requirements. Novel tasks force-fit into existing agents, resulting in suboptimal execution. | Queen dynamically selects agents from 86+ registry based on Loop 1 task breakdown. Backend tasks -> backend-dev, ML tasks -> ml-developer, security tasks -> security-specialist. Assignments stored in matrix, not hardcoded in skill. |
| **Skill-Only or Custom-Only Execution** | Force all agents to use existing skills (fails on novel tasks without skills). OR force all agents to use custom instructions (ignores proven skill SOPs). Both extremes are suboptimal. | Queen's decision tree: If specialized skill exists for task type, assign skill with context parameters. If no skill exists, assign custom instructions with Loop 1 guidance. Hybrid approach leverages skills when available, adapts when necessary. |
| **Accepting Theater as "Good Enough"** | Single theater detector reports 5% theater. Team ships anyway because "it's not that bad" or "we'll fix it later." Theater compounds - mocked functions never get real implementations, TODOs never get resolved, test theater spreads to new code. | Zero tolerance enforced through Byzantine consensus. 6 agents validate independently, 4/5 agreement required for theater confirmation. ANY confirmed theater blocks merge. Theater debt is never acceptable - it only grows. |

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Hardcoded Agent Assignments** | Agent+skill assignments baked into skill code. Every project uses same 6 agents regardless of task requirements. Novel tasks force-fit into existing agents, resulting in suboptimal execution. | Queen dynamically selects agents from 86+ registry based on Loop 1 task breakdown. Backend tasks -> backend-dev, ML tasks -> ml-developer, security tasks -> security-specialist. Assignments stored in matrix, not hardcoded in skill. |
| **Skill-Only or Custom-Only Execution** | Force all agents to use existing skills (fails on novel tasks without skills). OR force all agents to use custom instructions (ignores proven skill SOPs). Both extremes are suboptimal. | Queen's decision tree: If specialized skill exists for task type, assign skill with context parameters. If no skill exists, assign custom instructions with Loop 1 guidance. Hybrid approach leverages skills when available, adapts when necessary. |
| **Accepting Theater as "Good Enough"** | Single theater detector reports 5% theater. Team ships anyway because "it's not that bad" or "we'll fix it later." Theater compounds - mocked functions never get real implementations, TODOs never get resolved, test theater spreads to new code. | Zero tolerance enforced through Byzantine consensus. 6 agents validate independently, 4/5 agreement required for theater confirmation. ANY confirmed theater blocks merge. Theater debt is never acceptable - it only grows. |

## Conclusion

Parallel Swarm Implementation (Loop 2) provides adaptive meta-skill orchestration that dynamically compiles Loop 1 plans into agent+skill execution graphs with theater-free parallel implementation and 100% integration validation.

Key takeaways:
- Meta-orchestration separates planning from execution - Queen Coordinator compiles declarative plans into imperative agent+skill graphs enabling adaptive project handling
- Dynamic agent selection from 86+ registry with hybrid skill-based or custom-instruction execution based on task requirements and skill availability
- Theater detection through 6-agent Byzantine consensus (4/5 agreement required) with zero tolerance enforcement - any confirmed theater blocks merge
- Integration loop until 100% test pass rate with fail-fast local fixes before Loop 3 CI/CD, typically converging in 1-3 iterations
- Performance: 8.3x speedup from parallelization, 0% theater, 100% integration success, 90%+ test coverage

Use this skill when Loop 1 planning complete (validated research + risk analysis), implementation requires complex multi-agent coordination (6+ independent tasks), 0% theater tolerance is mandatory, and production-quality delivery needed (4-8 hours). Avoid for planning phase (use research-driven-planning first), simple sequential work (<2 hours), or trivial single-file changes.