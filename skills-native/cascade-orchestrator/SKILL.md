---
name: cascade-orchestrator
description: Creates sophisticated workflow cascades coordinating multiple micro-skills with sequential pipelines, parallel execution, conditional branching, and Codex sandbox iteration. Enhanced with multi-model routing (Gemini/Codex), ruv-swarm coordination, memory persistence, and audit-pipeline patterns for production workflows.
---

## Aspektual'naya Ramka Orkestratsii (Workflow State Tracking)

### Tipy Sostoyaniya (State Types)

**Stage States:**
- [SV:COMPLETED] Zaversheno - Stage/task complete, outputs validated
- [NSV:IN_PROGRESS] V protsesse - Active work, currently executing
- [BLOCKED] Blokirovano - Waiting for dependency to complete
- [PARALLEL] Parallel'no - Concurrent execution with other stages
- [FAILED] Provaleno - Stage failed, requires intervention
- [PENDING] Ozhidayet - Queued, not yet started

**Agent States:**
- [IDLE] Gotov - Ready for task assignment
- [WORKING] Rabotayet - Executing assigned task
- [WAITING] Zhdet - Blocked on external dependency
- [DONE] Zavershen - Task completed successfully
- [ERROR] Oshibka - Encountered error, needs recovery

**Transition Rules:**
- Phase N [SV] -> Phase N+1 [NSV] (all stages in phase complete)
- Stage [BLOCKED] -> Stage [NSV] (dependency resolved)
- Stage [FAILED] -> Stage [NSV] (retry/fix applied)
- Agent [IDLE] -> Agent [WORKING] -> Agent [DONE] (successful path)

### Vizualizatsiya Sostoyaniya (State Visualization)

```
WORKFLOW: enhanced-data-pipeline
  |
  +-- PHASE 1: Extract [SV:COMPLETED]
  |     +-- STAGE: extract-data [SV] (Agent: data-engineer [DONE])
  |
  +-- PHASE 2: Validate [NSV:IN_PROGRESS]
  |     +-- STAGE: validate-schema [NSV] (Agent: validator [WORKING])
  |     +-- STAGE: codex-auto-fix [BLOCKED] (Agent: codex [WAITING])
  |
  +-- PHASE 3: Transform [PENDING]
  |     +-- STAGE: transform-data [PENDING] (Agent: transformer [IDLE])
  |
  +-- PHASE 4: Report [PENDING]
        +-- STAGE: generate-report [PENDING] (Agent: reporter [IDLE])

DEPENDENCIES:
  Phase 1 [SV] -> Phase 2 [NSV] -> Phase 3 [PENDING] -> Phase 4 [PENDING]
```

## Keigo Wakugumi (Hierarchical Work Structure)

### Workflow Hierarchy

```
WORKFLOW (最上位)
  |
  +-- PHASE (重要段階) - Major sequential stage
        |
        +-- STAGE (小段階) - Sub-phase grouping
              |
              +-- TASK (作業) - Individual work item
                    |
                    +-- SUBTASK (細分) - Atomic operation
```

**Hierarchy Levels:**
1. **WORKFLOW** - Overall orchestration (e.g., "Production Deployment Pipeline")
2. **PHASE** - Sequential major stage (e.g., "Build", "Test", "Deploy")
3. **STAGE** - Within-phase grouping (e.g., "Unit Tests", "Integration Tests")
4. **TASK** - Assignable work unit (e.g., "Run Jest suite")
5. **SUBTASK** - Atomic operation (e.g., "Execute test file X")

### Dependency Visualization with Hierarchy

```
PHASE 1: Foundation Setup [SV]
  |-- TASK A: Research best practices [SV]
  |     |-- SUBTASK A.1: Search documentation [SV]
  |     |-- SUBTASK A.2: Analyze patterns [SV]

PHASE 2: Parallel Implementation [NSV]
  |-- TASK B: Backend API [NSV] (PARALLEL GROUP: implementation)
  |     |-- SUBTASK B.1: Define routes [SV]
  |     |-- SUBTASK B.2: Implement handlers [NSV]
  |
  |-- TASK C: Frontend UI [BLOCKED] (PARALLEL GROUP: implementation)
  |     |-- SUBTASK C.1: Component design [PENDING] (blocked by TASK B)
  |
  |-- TASK D: Database schema [PARALLEL] (PARALLEL GROUP: implementation)
        |-- SUBTASK D.1: Schema design [SV]
        |-- SUBTASK D.2: Migrations [NSV]

PHASE 3: Integration & Validation [PENDING]
  |-- TASK E: Integration testing [PENDING]
        |-- SUBTASK E.1: API tests [PENDING]
        |-- SUBTASK E.2: E2E tests [PENDING]

HIERARCHY PROPERTIES:
  - PHASE level: Sequential dependencies (Phase 1 -> Phase 2 -> Phase 3)
  - TASK level: Parallel within phase (TASK B || TASK C || TASK D)
  - SUBTASK level: Sequential within task (SUBTASK B.1 -> B.2)
```

## Orchestration Skill Guidelines

### When to Use This Skill
- **Multi-stage workflows** requiring sequential, parallel, or conditional execution
- **Complex pipelines** coordinating multiple micro-skills or agents
- **Iterative processes** with Codex sandbox testing and auto-fix loops
- **Multi-model routing** requiring intelligent AI selection per stage
- **Production workflows** needing GitHub integration and memory persistence

### When NOT to Use This Skill
- **Single-agent tasks** with no coordination requirements
- **Simple sequential work** that doesn't need stage management
- **Trivial operations** completing in <5 minutes
- **Pure research** without implementation stages

### Success Criteria
- **All stages complete** with 100% success rate (all [SV:COMPLETED])
- **Dependency resolution** with no circular dependencies
- **Model routing optimal** for each stage (Gemini/Codex/Claude)
- **Memory persistence** maintained across all stages
- **No orphaned stages** - all stages tracked and state-transitioned

### Edge Cases to Handle
- **Stage failure mid-cascade** - Transition to [FAILED], implement retry with exponential backoff
- **Circular dependencies** - Validate DAG structure before execution
- **Model unavailability** - Have fallback model selection per stage
- **Memory overflow** - Implement stage result compression
- **Timeout on long stages** - Configure per-stage timeout limits, transition to [FAILED]

### Guardrails (NEVER Violate)
- **NEVER lose stage state** - Persist after each state transition ([NSV] -> [SV])
- **ALWAYS validate dependencies** - Check DAG acyclic before execution
- **ALWAYS track cascade progress** - Update memory with real-time state (aspectual tracking)
- **NEVER skip error handling** - Every stage needs try/catch with [FAILED] transition
- **ALWAYS cleanup on failure** - Release resources, clear temp state, mark [ERROR]

### Evidence-Based Validation
- **Verify stage outputs** - Check actual results vs expected schema (validate [SV] state)
- **Validate data flow** - Confirm outputs passed correctly to next stage in hierarchy
- **Check model routing** - Verify correct AI used per stage requirements
- **Measure cascade performance** - Track execution time vs estimates per hierarchy level
- **Audit memory usage** - Ensure no memory leaks across stages/phases


# Cascade Orchestrator (Enhanced)

## Overview
Manages workflows (cascades) that coordinate multiple micro-skills into cohesive processes. This enhanced version integrates Codex sandbox iteration, multi-model routing, ruv-swarm coordination, and memory persistence across stages.

## Philosophy: Composable Excellence

Complex capabilities emerge from composing simple, well-defined components.

**Enhanced Capabilities**:
- **Codex Sandbox Iteration**: Auto-fix failures in isolated environment (from audit-pipeline)
- **Multi-Model Routing**: Use Gemini/Codex based on stage requirements
- **Swarm Coordination**: Parallel execution via ruv-swarm MCP
- **Memory Persistence**: Maintain context across stages
- **GitHub Integration**: CI/CD pipeline automation

**Key Principles**:
1. Separation of concerns (micro-skills execute, cascades coordinate)
2. Reusability through composition
3. Flexible orchestration patterns
4. Declarative workflow definition
5. Intelligent model selection

## Cascade Architecture (Enhanced)

### Definition Layer

**Extended Stage Types**:
```yaml
stages:
  - type: sequential     # One after another
  - type: parallel       # Simultaneous execution
  - type: conditional    # Based on runtime conditions
  - type: codex-sandbox  # NEW: Iterative testing with auto-fix
  - type: multi-model    # NEW: Intelligent AI routing
  - type: swarm-parallel # NEW: Coordinated via ruv-swarm
```

**Enhanced Data Flow**:
```yaml
data_flow:
  - stage_output: previous stage results
  - shared_memory: persistent across stages
  - multi_model_context: AI-specific formatting
  - codex_sandbox_state: isolated test environment
```

**Advanced Error Handling**:
```yaml
error_handling:
  - retry_with_backoff
  - fallback_to_alternative
  - codex_auto_fix        # NEW: Auto-fix via Codex
  - model_switching       # NEW: Try different AI
  - swarm_recovery        # NEW: Redistribute tasks
```

### Execution Engine (Enhanced)

**Stage Scheduling with AI Selection**:
```python
for stage in cascade.stages:
    if stage.type == "codex-sandbox":
        execute_with_codex_iteration(stage)
    elif stage.type == "multi-model":
        model = select_optimal_model(stage.task)
        execute_on_model(stage, model)
    elif stage.type == "swarm-parallel":
        execute_via_ruv_swarm(stage)
    else:
        execute_standard(stage)
```

**Codex Sandbox Iteration Loop**:
```python
def execute_with_codex_iteration(stage):
    """
    From audit-pipeline Phase 2: functionality-audit pattern
    """
    results = execute_tests(stage.tests)

    for test in failed_tests(results):
        iteration = 0
        max_iterations = 5

        while test.failed and iteration < max_iterations:
            # Spawn Codex in sandbox
            fix = spawn_codex_auto(
                task=f"Fix test failure: {test.error}",
                sandbox=True,
                context=test.context
            )

            # Re-test
            test.result = rerun_test(test)
            iteration += 1

            if test.passed:
                apply_fix_to_main(fix)
                break

        if still_failed(test):
            escalate_to_user(test)

    return aggregate_results(results)
```

**Multi-Model Routing**:
```python
def select_optimal_model(task):
    """
    Route to best AI based on task characteristics
    """
    if task.requires_large_context:
        return "gemini-megacontext"  # 1M tokens
    elif task.needs_current_info:
        return "gemini-search"        # Web grounding
    elif task.needs_visual_output:
        return "gemini-media"          # Imagen/Veo
    elif task.needs_rapid_prototype:
        return "codex-auto"            # Full Auto
    elif task.needs_alternative_view:
        return "codex-reasoning"       # GPT-5-Codex
    else:
        return "claude"                # Best overall
```

## Enhanced Cascade Patterns

### Pattern 1: Linear Pipeline with Multi-Model

```yaml
cascade:
  name: enhanced-data-pipeline
  stages:
    - stage: extract
      model: auto-select
      skill: extract-data

    - stage: validate
      model: auto-select
      skill: validate-data
      error_handling:
        strategy: codex-auto-fix  # NEW

    - stage: transform
      model: codex-auto           # Fast prototyping
      skill: transform-data

    - stage: report
      model: gemini-media         # Generate visuals
      skill: generate-report
```

### Pattern 2: Parallel Fan-Out with Swarm

```yaml
cascade:
  name: code-quality-swarm
  stages:
    - stage: quality-checks
      type: swarm-parallel        # NEW: Via ruv-swarm
      skills:
        - lint-code
        - security-scan
        - complexity-analysis
        - test-coverage
      swarm_config:
        topology: mesh
        max_agents: 4
        strategy: balanced

    - stage: aggregate
      skill: merge-quality-reports
```

### Pattern 3: Codex Sandbox Iteration

```yaml
cascade:
  name: test-and-fix
  stages:
    - stage: functionality-audit
      type: codex-sandbox         # NEW
      test_suite: comprehensive
      codex_config:
        mode: full-auto
        max_iterations: 5
        sandbox: true
      error_recovery:
        auto_fix: true
        escalate_after: 5

    - stage: validate-fixes
      skill: regression-tests
```

### Pattern 4: Conditional with Model Switching

```yaml
cascade:
  name: adaptive-workflow
  stages:
    - stage: analyze
      model: gemini-megacontext   # Large context
      skill: analyze-codebase

    - stage: decide
      type: conditional
      condition: ${analyze.quality_score}
      branches:
        high_quality:
          model: codex-auto       # Fast path
          skill: deploy-fast
        low_quality:
          model: multi-model      # Comprehensive path
          cascade: deep-quality-audit
```

### Pattern 5: Iterative with Memory

```yaml
cascade:
  name: iterative-refinement
  stages:
    - stage: refactor
      model: auto-select
      skill: refactor-code
      memory: persistent          # NEW

    - stage: check-quality
      skill: quality-metrics

    - stage: repeat-decision
      type: conditional
      condition: ${quality < threshold}
      repeat: refactor            # Loop back
      max_iterations: 3
      memory_shared: true         # Context persists
```

## Creating Enhanced Cascades

### Step 1: Define with AI Considerations

**Identify Model Requirements**:
```markdown
For each stage, determine:
- Large context needed? → Gemini
- Current web info needed? → Gemini Search
- Visual output needed? → Gemini Media
- Rapid prototyping needed? → Codex
- Testing with auto-fix? → Codex Sandbox
- Best overall reasoning? → Claude
```

### Step 2: Design with Swarm Parallelism

**When to Use Swarm**:
- Multiple independent tasks
- Resource-intensive operations
- Need load balancing
- Want fault tolerance

**Swarm Configuration**:
```yaml
swarm_config:
  topology: mesh | hierarchical | star
  max_agents: number
  strategy: balanced | specialized | adaptive
  memory_shared: true | false
```

### Step 3: Add Codex Iteration for Quality

**Pattern from audit-pipeline**:
```yaml
stages:
  - type: codex-sandbox
    tests: ${test_suite}
    fix_strategy:
      auto_fix: true
      max_iterations: 5
      sandbox_isolated: true
      network_disabled: true
      regression_check: true
```

### Step 4: Enable Memory Persistence

**Shared Memory Across Stages**:
```yaml
memory:
  persistence: enabled
  scope: cascade | global
  storage: mcp__ruv-swarm__memory
  keys:
    - analysis_results
    - intermediate_outputs
    - learned_patterns
```

## Enhanced Cascade Definition Format

```yaml
cascade:
  name: cascade-name
  description: What this accomplishes
  version: 2.1.0

  config:
    multi_model: enabled
    swarm_coordination: enabled
    memory_persistence: enabled
    github_integration: enabled
    state_tracking: aspectual  # NEW: Track state transitions
    hierarchy_tracking: enabled  # NEW: Track phase/stage/task levels

  inputs:
    - name: input-name
      type: type
      description: description

  stages:
    - stage_id: stage-1
      name: Stage Name
      type: sequential | parallel | codex-sandbox | multi-model | swarm-parallel
      model: auto-select | gemini | codex | claude
      state: PENDING | IN_PROGRESS | COMPLETED | FAILED | BLOCKED | PARALLEL  # NEW
      hierarchy_level: phase | stage | task | subtask  # NEW

      # For micro-skill execution
      skills:
        - skill: micro-skill-name
          inputs: {...}
          outputs: {...}

      # For Codex sandbox
      codex_config:
        mode: full-auto
        sandbox: true
        max_iterations: 5

      # For swarm execution
      swarm_config:
        topology: mesh
        max_agents: 4

      # For memory
      memory:
        read_keys: [...]
        write_keys: [...]

      # NEW: State transition configuration
      state_transitions:
        on_start: PENDING -> IN_PROGRESS
        on_complete: IN_PROGRESS -> COMPLETED
        on_failure: IN_PROGRESS -> FAILED
        on_block: IN_PROGRESS -> BLOCKED
        on_retry: FAILED -> IN_PROGRESS

      # NEW: Agent state tracking
      agents:
        - agent_id: agent-1
          state: IDLE | WORKING | WAITING | DONE | ERROR
          assigned_task: task-id

      error_handling:
        strategy: retry | codex-auto-fix | model-switch | swarm-recovery
        max_retries: 3
        fallback: alternative-skill
        state_on_error: FAILED  # NEW

  # NEW: State tracking configuration
  state_tracking:
    enabled: true
    persist_to_memory: true
    visualization_format: hierarchical_tree
    state_transitions_logged: true

  # NEW: Hierarchy configuration
  hierarchy:
    levels: [workflow, phase, stage, task, subtask]
    dependency_rules:
      phase: sequential  # Phases run sequentially
      stage: conditional  # Stages can be parallel or sequential
      task: parallel_in_phase  # Tasks parallel within phase
      subtask: sequential_in_task  # Subtasks sequential within task

  memory:
    persistence: enabled
    scope: cascade
    store_state_history: true  # NEW

  github_integration:
    create_pr: on_success
    report_issues: on_failure
```

## State Transition Output Templates

### Aspectual State Report Template

```
CASCADE STATE REPORT: {cascade_name}
Generated: {timestamp}

OVERALL STATUS: {workflow_state}
  Total Phases: {phase_count}
  Completed: {completed_count} [SV]
  In Progress: {in_progress_count} [NSV]
  Blocked: {blocked_count} [BLOCKED]
  Failed: {failed_count} [FAILED]
  Pending: {pending_count} [PENDING]

STATE TRANSITIONS (Last 5):
  1. {timestamp} | Phase 2/Stage 3 | PENDING -> IN_PROGRESS
  2. {timestamp} | Phase 2/Stage 2 | IN_PROGRESS -> COMPLETED
  3. {timestamp} | Phase 1/Stage 1 | IN_PROGRESS -> COMPLETED
  4. {timestamp} | Phase 1/Stage 1 | PENDING -> IN_PROGRESS
  5. {timestamp} | Workflow initialized | null -> PENDING

AGENT STATUS:
  IDLE: {idle_agents} agents available
  WORKING: {working_agents} agents executing
  WAITING: {waiting_agents} agents blocked
  DONE: {done_agents} agents completed
  ERROR: {error_agents} agents failed

NEXT ACTIONS:
  - Resolve {blocked_count} blocked stages
  - Monitor {in_progress_count} active stages
  - Prepare for {pending_count} queued stages
```

### Hierarchical Dependency Report Template

```
CASCADE HIERARCHY: {cascade_name}

WORKFLOW LEVEL (最上位):
  Name: {workflow_name}
  State: {workflow_state}
  Estimated Completion: {eta}

PHASE LEVEL (重要段階):
  Phase 1: {phase1_name} [{phase1_state}]
    Dependencies: None (initial phase)
    Blocks: Phase 2, Phase 3, Phase 4
    Progress: {phase1_progress}%

  Phase 2: {phase2_name} [{phase2_state}]
    Dependencies: Phase 1 [SV:COMPLETED]
    Blocks: Phase 3, Phase 4
    Progress: {phase2_progress}%

  Phase 3: {phase3_name} [{phase3_state}]
    Dependencies: Phase 2 [PENDING]
    Blocks: Phase 4
    Progress: {phase3_progress}%

STAGE LEVEL (小段階) - Phase 2 Detail:
  Stage 2.1: {stage_name} [{state}]
    Hierarchy: Phase 2 > Stage 2.1
    Dependencies: Phase 1 complete
    Parallel Group: implementation
    Tasks: {task_count}

TASK LEVEL (作業) - Stage 2.1 Detail:
  Task 2.1.1: {task_name} [{state}]
    Assigned Agent: {agent_id} [{agent_state}]
    Subtasks: {subtask_count}
    Estimated Time: {eta}

SUBTASK LEVEL (細分) - Task 2.1.1 Detail:
  Subtask 2.1.1.1: {subtask_name} [SV:COMPLETED]
  Subtask 2.1.1.2: {subtask_name} [NSV:IN_PROGRESS]
  Subtask 2.1.1.3: {subtask_name} [PENDING]

DEPENDENCY GRAPH:
  Sequential: Phase 1 -> Phase 2 -> Phase 3 -> Phase 4
  Parallel (Phase 2): Task 2.1 || Task 2.2 || Task 2.3
  Sequential (Task 2.1): Subtask 2.1.1 -> 2.1.2 -> 2.1.3
```

### Combined Aspectual-Hierarchical View

```
WORKFLOW ORCHESTRATION STATUS

HIERARCHY + STATE VIEW:

WORKFLOW: Production Deployment Pipeline [NSV:IN_PROGRESS]
  |
  +-- PHASE 1: Build [SV:COMPLETED] ✓
  |     |-- STAGE 1.1: Compile [SV] (Agent: builder [DONE])
  |     |-- STAGE 1.2: Test [SV] (Agent: tester [DONE])
  |
  +-- PHASE 2: Deploy to Staging [NSV:IN_PROGRESS] ⚙
  |     |-- STAGE 2.1: Package [SV] (Agent: packager [DONE])
  |     |-- STAGE 2.2: Upload [NSV] (Agent: uploader [WORKING])
  |     |-- STAGE 2.3: Smoke Tests [BLOCKED] (Agent: tester [WAITING])
  |           |-- TASK 2.3.1: API health check [PENDING]
  |           |-- TASK 2.3.2: Database migration [PENDING]
  |
  +-- PHASE 3: Deploy to Production [PENDING] ⏳
        |-- STAGE 3.1: Blue-Green Deploy [PENDING]
        |-- STAGE 3.2: Validation [PENDING]

STATE LEGEND:
  [SV:COMPLETED] ✓ - Zaversheno (Complete)
  [NSV:IN_PROGRESS] ⚙ - V protsesse (Active)
  [BLOCKED] ⛔ - Blokirovano (Blocked)
  [PENDING] ⏳ - Ozhidayet (Queued)
  [FAILED] ❌ - Provaleno (Failed)

CRITICAL PATH:
  Stage 2.2 [NSV] -> Stage 2.3 [BLOCKED] -> Phase 3 [PENDING]
  Estimated Completion: {eta} (blocked on upload completion)
```

## Real-World Enhanced Cascades

### Example 1: Complete Development Workflow

```yaml
cascade: complete-dev-workflow
stages:
  1. gemini-search: "Research latest framework best practices"
  2. codex-auto: "Rapid prototype with best practices"
  3. codex-sandbox: "Test everything, auto-fix failures"
  4. gemini-media: "Generate architecture diagrams"
  5. style-audit: "Polish code to production standards"
  6. github-pr: "Create PR with comprehensive report"
```

### Example 2: Legacy Modernization

```yaml
cascade: modernize-legacy-code
stages:
  1. gemini-megacontext: "Analyze entire 50K line codebase"
  2. theater-detection: "Find all mocks and placeholders"
  3. [swarm-parallel]:
     - codex-auto: "Complete implementations" (parallel)
     - gemini-media: "Document architecture"
  4. codex-sandbox: "Test all changes with auto-fix"
  5. style-audit: "Final polish"
  6. generate-pr: "Create PR with before/after comparison"
```

### Example 3: Bug Fix with RCA

```yaml
cascade: intelligent-bug-fix
stages:
  1. root-cause-analyzer: "Deep RCA analysis"
  2. multi-model-decision:
     condition: ${rca.complexity}
     simple: codex-auto (quick fix)
     complex: [
       gemini-megacontext (understand broader context),
       codex-reasoning (alternative approaches),
       claude (implement best approach)
     ]
  3. codex-sandbox: "Test fix thoroughly"
  4. regression-suite: "Ensure no breakage"
  5. github-issue-update: "Document fix with RCA report"
```

## Integration Points

### With Micro-Skills
- Executes micro-skills in stages
- Passes data between skills
- Handles skill errors gracefully

### With Multi-Model System
- Routes stages to optimal AI
- Uses gemini-* skills for unique capabilities
- Uses codex-* skills for prototyping/fixing
- Uses Claude for best reasoning

### With Audit Pipeline
- Incorporates theater → functionality → style pattern
- Uses Codex sandbox iteration from Phase 2
- Applies quality gates throughout

### With Slash Commands
- Commands trigger cascades
- Parameter mapping from command to cascade
- Progress reporting to command interface

### With Ruv-Swarm MCP
- Parallel stage coordination
- Memory persistence
- Neural training
- Performance tracking

## Working with Enhanced Cascade Orchestrator

**Invocation**:
"Create a cascade that [end goal] using [micro-skills] with [Codex/Gemini/swarm] capabilities"

**The orchestrator will**:
1. Design workflow with optimal AI model selection
2. Configure Codex sandbox for testing stages
3. Set up swarm coordination for parallel stages
4. Enable memory persistence across stages
5. Integrate with GitHub for CI/CD
6. Generate executable cascade definition

**Advanced Features**:
- Automatic model routing based on task
- Codex iteration loop for auto-fixing
- Swarm coordination for parallelism
- Memory sharing across stages
- GitHub PR/issue integration
- Performance monitoring and optimization

-----------|---------|----------|
| **Sequential execution of parallelizable stages** | Stages that have no dependencies run one-after-another, wasting 5-10x time compared to parallel execution. | Use swarm-parallel stage type with ruv-swarm coordination for independent tasks. Execute concurrently with load balancing. |
| **Circular dependencies in stage graph** | Stage A depends on Stage B, which depends on Stage C, which depends on Stage A, causing infinite loop or deadlock. | Validate cascade definition as DAG (directed acyclic graph) before execution. Reject circular dependencies at design time. |
| **Hardcoded model selection** | Every stage uses "claude" even when Gemini (megacontext) or Codex (auto-fix) would be 10x better for specific tasks. | Use auto-select or adaptive model routing based on task requirements (large context, visual output, rapid prototyping, etc). |
| **No memory persistence across stages** | Each stage re-analyzes code, re-computes results, forgets prior learnings, causing massive redundant work. | Enable memory persistence (scope: cascade or global) with mcp__ruv-swarm__memory. Share intermediate outputs and learned patterns. |
| **Ignoring Codex auto-fix failures** | Test failures in codex-sandbox stage escalate to user immediately without retry, losing 95% auto-fix opportunity. | Configure max_iterations: 5 with exponential backoff. Let Codex iterate on fixes before human escalation. |

## Conclusion

Cascade Orchestrator transforms multi-step workflows from fragile, manually coordinated sequences into robust, self-healing pipelines. By composing micro-skills with intelligent model routing, swarm parallelism, and Codex sandbox iteration, cascades handle complex workflows that previously required extensive manual orchestration.

The skill's power comes from three innovations: (1) separation of concerns through micro-skill composition enables reusability and maintainability, (2) multi-model routing leverages each AI's strengths (Gemini for context, Codex for speed, Claude for reasoning), and (3) sandbox auto-fix loops eliminate 95% of manual debugging by automatically iterating on test failures until resolution.

Use Cascade Orchestrator when coordinating 4+ micro-skills with complex dependencies, implementing production workflows requiring fault tolerance and auto-recovery, or building systems that span multiple AI models for optimal performance. The key insight: orchestration is not about doing the work, but about intelligently coordinating specialized components to achieve emergent capability beyond any single agent or skill.