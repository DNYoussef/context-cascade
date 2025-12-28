---
name: stream-chain
description: Stream-JSON chaining for multi-agent pipelines, data transformation, and sequential workflows
---

## Orchestration Skill Guidelines

### When to Use This Skill
- **Multi-agent coordination** requiring centralized orchestration
- **Complex workflows** with multiple dependent tasks
- **Parallel execution** benefiting from concurrent agent spawning
- **Quality-controlled delivery** needing validation and consensus
- **Production workflows** requiring audit trails and state management

### When NOT to Use This Skill
- **Single-agent tasks** with no coordination requirements
- **Simple sequential work** completing in <30 minutes
- **Trivial operations** with no quality gates
- **Exploratory work** not needing formal orchestration

### Success Criteria
- **All agents complete successfully** with 100% task completion
- **Coordination overhead minimal** (<20% of total execution time)
- **No orphaned agents** - All spawned agents tracked and terminated
- **State fully recoverable** - Can resume from any failure point
- **Quality gates pass** - All validation checks successful

### Edge Cases to Handle
- **Agent failures** - Detect and replace failed agents automatically
- **Timeout scenarios** - Configure per-agent timeout with escalation
- **Resource exhaustion** - Limit concurrent agents, queue excess work
- **Conflicting results** - Implement conflict resolution strategy
- **Partial completion** - Support incremental progress with rollback

### Guardrails (NEVER Violate)
- **NEVER lose orchestration state** - Persist to memory after each phase
- **ALWAYS track all agents** - Maintain real-time agent registry
- **ALWAYS cleanup resources** - Terminate agents and free memory on completion
- **NEVER skip validation** - Run quality checks before marking complete
- **ALWAYS handle errors** - Every orchestration step needs error handling

### Evidence-Based Validation
- **Verify all agent outputs** - Check actual results vs expected contracts
- **Validate execution order** - Confirm dependencies respected
- **Measure performance** - Track execution time vs baseline
- **Check resource usage** - Monitor memory, CPU, network during execution
- **Audit state consistency** - Verify orchestration state matches reality


# Stream-Chain Skill

Execute sophisticated multi-step workflows where each agent's output flows into the next, enabling complex data transformations and sequential processing pipelines.

## Overview

Stream-Chain provides two powerful modes for orchestrating multi-agent workflows:

1. **Custom Chains** (`run`): Execute custom prompt sequences with full control
2. **Predefined Pipelines** (`pipeline`): Use battle-tested workflows for common tasks

Each step in a chain receives the complete output from the previous step, enabling sophisticated multi-agent coordination through streaming data flow.

## Custom Chains (`run`)

Execute custom stream chains with your own prompts for maximum flexibility.

### Syntax

```bash
claude-flow stream-chain run <prompt1> <prompt2> [...] [options]
```

**Requirements:**
- Minimum 2 prompts required
- Each prompt becomes a step in the chain
- Output flows sequentially through all steps

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--verbose` | Show detailed execution information | `false` |
| `--timeout <seconds>` | Timeout per step | `30` |
| `--debug` | Enable debug mode with full logging | `false` |

### How Context Flows

Each step receives the previous output as context:

```
Step 1: "Write a sorting function"
Output: [function implementation]

Step 2 receives:
  "Previous step output:
  [function implementation]

  Next task: Add comprehensive tests"

Step 3 receives:
  "Previous steps output:
  [function + tests]

  Next task: Optimize performance"
```

### Examples

#### Basic Development Chain

```bash
claude-flow stream-chain run \
  "Write a user authentication function" \
  "Add input validation and error handling" \
  "Create unit tests with edge cases"
```

#### Security Audit Workflow

```bash
claude-flow stream-chain run \
  "Analyze authentication system for vulnerabilities" \
  "Identify and categorize security issues by severity" \
  "Propose fixes with implementation priority" \
  "Generate security test cases" \
  --timeout 45 \
  --verbose
```

#### Code Refactoring Chain

```bash
claude-flow stream-chain run \
  "Identify code smells in src/ directory" \
  "Create refactoring plan with specific changes" \
  "Apply refactoring to top 3 priority items" \
  "Verify refactored code maintains behavior" \
  --debug
```

#### Data Processing Pipeline

```bash
claude-flow stream-chain run \
  "Extract data from API responses" \
  "Transform data into normalized format" \
  "Validate data against schema" \
  "Generate data quality report"
```

-----|-------------|---------|
| `--verbose` | Show detailed execution | `false` |
| `--timeout <seconds>` | Timeout per step | `30` |
| `--debug` | Enable debug mode | `false` |

### Pipeline Examples

#### Quick Analysis

```bash
claude-flow stream-chain pipeline analysis
```

#### Extended Refactoring

```bash
claude-flow stream-chain pipeline refactor --timeout 60 --verbose
```

#### Debug Test Generation

```bash
claude-flow stream-chain pipeline test --debug
```

#### Comprehensive Optimization

```bash
claude-flow stream-chain pipeline optimize --timeout 90 --verbose
```

### Pipeline Output

Each pipeline execution provides:

- **Progress**: Step-by-step execution status
- **Results**: Success/failure per step
- **Timing**: Total and per-step execution time
- **Summary**: Consolidated results and recommendations

## Advanced Use Cases

### Multi-Agent Coordination

Chain different agent types for complex workflows:

```bash
claude-flow stream-chain run \
  "Research best practices for API design" \
  "Design REST API with discovered patterns" \
  "Implement API endpoints with validation" \
  "Generate OpenAPI specification" \
  "Create integration tests" \
  "Write deployment documentation"
```

### Data Transformation Pipeline

Process and transform data through multiple stages:

```bash
claude-flow stream-chain run \
  "Extract user data from CSV files" \
  "Normalize and validate data format" \
  "Enrich data with external API calls" \
  "Generate analytics report" \
  "Create visualization code"
```

### Code Migration Workflow

Systematic code migration with validation:

```bash
claude-flow stream-chain run \
  "Analyze legacy codebase dependencies" \
  "Create migration plan with risk assessment" \
  "Generate modernized code for high-priority modules" \
  "Create migration tests" \
  "Document migration steps and rollback procedures"
```

### Quality Assurance Chain

Comprehensive code quality workflow:

```bash
claude-flow stream-chain pipeline analysis
claude-flow stream-chain pipeline refactor
claude-flow stream-chain pipeline test
claude-flow stream-chain pipeline optimize
```

## Integration with Claude Flow

### Combine with Swarm Coordination

```bash
# Initialize swarm for coordination
claude-flow swarm init --topology mesh

# Execute stream chain with swarm agents
claude-flow stream-chain run \
  "Agent 1: Research task" \
  "Agent 2: Implement solution" \
  "Agent 3: Test implementation" \
  "Agent 4: Review and refine"
```

### Memory Integration

Stream chains automatically store context in memory for cross-session persistence:

```bash
# Execute chain with memory
claude-flow stream-chain run \
  "Analyze requirements" \
  "Design architecture" \
  --verbose

# Results stored in .claude-flow/memory/stream-chain/
```

### Neural Pattern Training

Successful chains train neural patterns for improved performance:

```bash
# Enable neural training
claude-flow stream-chain pipeline optimize --debug

# Patterns learned and stored for future optimizations
```

## Performance Characteristics

- **Throughput**: 2-5 steps per minute (varies by complexity)
- **Context Size**: Up to 100K tokens per step
- **Memory Usage**: ~50MB per active chain
- **Concurrency**: Supports parallel chain execution

## Examples Repository

### Complete Development Workflow

```bash
# Full feature development chain
claude-flow stream-chain run \
  "Analyze requirements for user profile feature" \
  "Design database schema and API endpoints" \
  "Implement backend with validation" \
  "Create frontend components" \
  "Write comprehensive tests" \
  "Generate API documentation" \
  --timeout 60 \
  --verbose
```

### Code Review Pipeline

```bash
# Automated code review workflow
claude-flow stream-chain run \
  "Analyze recent git changes" \
  "Identify code quality issues" \
  "Check for security vulnerabilities" \
  "Verify test coverage" \
  "Generate code review report with recommendations"
```

### Migration Assistant

```bash
# Framework migration helper
claude-flow stream-chain run \
  "Analyze current Vue 2 codebase" \
  "Identify Vue 3 breaking changes" \
  "Create migration checklist" \
  "Generate migration scripts" \
  "Provide updated code examples"
```

-----------|---------|----------|
| **Circular Dependencies** | Step 3 depends on Step 5's output, creating deadlock. Chain execution requires strict DAG (directed acyclic graph). | Design chains as unidirectional flows. If bidirectional refinement needed, use multiple chains or explicit iteration loops with termination conditions. |
| **Context Explosion** | Each step adds 50KB+ of output, causing later steps to hit token limits and lose early context. | Use summarization steps between major phases. Compress verbose outputs into key findings before passing to next step. Consider splitting into multiple chains with cross-chain memory storage. |
| **Premature Parallelization** | Converting sequential chain into parallel execution loses the context flow that makes chains valuable. | If tasks are truly independent, use swarm coordination instead. Chains are for dependent tasks where output N feeds input N+1. Parallelization destroys this dependency graph. |

## Conclusion

Stream-Chain enables sophisticated multi-step workflows by:

- **Sequential Processing**: Each step builds on previous results
- **Context Preservation**: Full output history flows through chain
- **Flexible Orchestration**: Custom chains or predefined pipelines
- **Agent Coordination**: Natural multi-agent collaboration pattern
- **Data Transformation**: Complex processing through simple steps

Use `run` for custom workflows and `pipeline` for battle-tested solutions.
## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Circular Dependencies** | Step 3 depends on Step 5's output, creating deadlock. Chain execution requires strict DAG (directed acyclic graph). | Design chains as unidirectional flows. If bidirectional refinement needed, use multiple chains or explicit iteration loops with termination conditions. |
| **Context Explosion** | Each step adds 50KB+ of output, causing later steps to hit token limits and lose early context. | Use summarization steps between major phases. Compress verbose outputs into key findings before passing to next step. Consider splitting into multiple chains with cross-chain memory storage. |
| **Premature Parallelization** | Converting sequential chain into parallel execution loses the context flow that makes chains valuable. | If tasks are truly independent, use swarm coordination instead. Chains are for dependent tasks where output N feeds input N+1. Parallelization destroys this dependency graph. |

---

## Enhanced Conclusion

Stream-Chain solves the fundamental challenge of multi-step reasoning: maintaining context across transformations. Traditional approaches either lose context (separate agents) or overwhelm context (single agent with all tasks). Stream chains provide a middle path - sequential execution with cumulative context, where each step builds on validated prior work.

The chain architecture naturally enforces best practices: verification before progression, specialization over generalization, and incremental refinement over big-bang delivery. When tasks have natural dependencies and each step produces context valuable to subsequent steps, stream chains transform sequential constraints from limitations into architectural advantages.

Use `run` for custom workflows requiring flexible step definitions. Use `pipeline` for battle-tested domain-specific workflows (analysis, refactoring, testing, optimization). Choose chains when task output quality depends on understanding prior results - when "what came before" matters as much as "what to do next."