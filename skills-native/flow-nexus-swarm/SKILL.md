---
name: flow-nexus-swarm
description: Cloud-based AI swarm deployment and event-driven workflow automation with Flow Nexus platform
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


# Flow Nexus Swarm & Workflow Orchestration

Deploy and manage cloud-based AI agent swarms with event-driven workflow automation, message queue processing, and intelligent agent coordination.

## 📋 Table of Contents

1. [Overview](#overview)
2. [Swarm Management](#swarm-management)
3. [Workflow Automation](#workflow-automation)
4. [Agent Orchestration](#agent-orchestration)
5. [Templates & Patterns](#templates--patterns)
6. [Advanced Features](#advanced-features)
7. [Best Practices](#best-practices)

## Overview

Flow Nexus provides cloud-based orchestration for AI agent swarms with:

- **Multi-topology Support**: Hierarchical, mesh, ring, and star architectures
- **Event-driven Workflows**: Message queue processing with async execution
- **Template Library**: Pre-built swarm configurations for common use cases
- **Intelligent Agent Assignment**: Vector similarity matching for optimal agent selection
- **Real-time Monitoring**: Comprehensive metrics and audit trails
- **Scalable Infrastructure**: Cloud-based execution with auto-scaling

## Swarm Management

### Initialize Swarm

Create a new swarm with specified topology and configuration:

```javascript
mcp__flow-nexus__swarm_init({
  topology: "hierarchical", // Options: mesh, ring, star, hierarchical
  maxAgents: 8,
  strategy: "balanced" // Options: balanced, specialized, adaptive
})
```

**Topology Guide:**
- **Hierarchical**: Tree structure with coordinator nodes (best for complex projects)
- **Mesh**: Peer-to-peer collaboration (best for research and analysis)
- **Ring**: Circular coordination (best for sequential workflows)
- **Star**: Centralized hub (best for simple delegation)

**Strategy Guide:**
- **Balanced**: Equal distribution of workload across agents
- **Specialized**: Agents focus on specific expertise areas
- **Adaptive**: Dynamic adjustment based on task complexity

### Spawn Agents

Add specialized agents to the swarm:

```javascript
mcp__flow-nexus__agent_spawn({
  type: "researcher", // Options: researcher, coder, analyst, optimizer, coordinator
  name: "Lead Researcher",
  capabilities: ["web_search", "analysis", "summarization"]
})
```

**Agent Types:**
- **Researcher**: Information gathering, web search, analysis
- **Coder**: Code generation, refactoring, implementation
- **Analyst**: Data analysis, pattern recognition, insights
- **Optimizer**: Performance tuning, resource optimization
- **Coordinator**: Task delegation, progress tracking, integration

### Orchestrate Tasks

Distribute tasks across the swarm:

```javascript
mcp__flow-nexus__task_orchestrate({
  task: "Build a REST API with authentication and database integration",
  strategy: "parallel", // Options: parallel, sequential, adaptive
  maxAgents: 5,
  priority: "high" // Options: low, medium, high, critical
})
```

**Execution Strategies:**
- **Parallel**: Maximum concurrency for independent subtasks
- **Sequential**: Step-by-step execution with dependencies
- **Adaptive**: AI-powered strategy selection based on task analysis

### Monitor & Scale Swarms

```javascript
// Get detailed swarm status
mcp__flow-nexus__swarm_status({
  swarm_id: "optional-id" // Uses active swarm if not provided
})

// List all active swarms
mcp__flow-nexus__swarm_list({
  status: "active" // Options: active, destroyed, all
})

// Scale swarm up or down
mcp__flow-nexus__swarm_scale({
  target_agents: 10,
  swarm_id: "optional-id"
})

// Gracefully destroy swarm
mcp__flow-nexus__swarm_destroy({
  swarm_id: "optional-id"
})
```

## Workflow Automation

### Create Workflow

Define event-driven workflows with message queue processing:

```javascript
mcp__flow-nexus__workflow_create({
  name: "CI/CD Pipeline",
  description: "Automated testing, building, and deployment",
  steps: [
    {
      id: "test",
      action: "run_tests",
      agent: "tester",
      parallel: true
    },
    {
      id: "build",
      action: "build_app",
      agent: "builder",
      depends_on: ["test"]
    },
    {
      id: "deploy",
      action: "deploy_prod",
      agent: "deployer",
      depends_on: ["build"]
    }
  ],
  triggers: ["push_to_main", "manual_trigger"],
  metadata: {
    priority: 10,
    retry_policy: "exponential_backoff"
  }
})
```

**Workflow Features:**
- **Dependency Management**: Define step dependencies with `depends_on`
- **Parallel Execution**: Set `parallel: true` for concurrent steps
- **Event Triggers**: GitHub events, schedules, manual triggers
- **Retry Policies**: Automatic retry on transient failures
- **Priority Queuing**: High-priority workflows execute first

### Execute Workflow

Run workflows synchronously or asynchronously:

```javascript
mcp__flow-nexus__workflow_execute({
  workflow_id: "workflow_id",
  input_data: {
    branch: "main",
    commit: "abc123",
    environment: "production"
  },
  async: true // Queue-based execution for long-running workflows
})
```

**Execution Modes:**
- **Sync (async: false)**: Immediate execution, wait for completion
- **Async (async: true)**: Message queue processing, non-blocking

### Monitor Workflows

```javascript
// Get workflow status and metrics
mcp__flow-nexus__workflow_status({
  workflow_id: "id",
  execution_id: "specific-run-id", // Optional
  include_metrics: true
})

// List workflows with filters
mcp__flow-nexus__workflow_list({
  status: "running", // Options: running, completed, failed, pending
  limit: 10,
  offset: 0
})

// Get complete audit trail
mcp__flow-nexus__workflow_audit_trail({
  workflow_id: "id",
  limit: 50,
  start_time: "2025-01-01T00:00:00Z"
})
```

### Agent Assignment

Intelligently assign agents to workflow tasks:

```javascript
mcp__flow-nexus__workflow_agent_assign({
  task_id: "task_id",
  agent_type: "coder", // Preferred agent type
  use_vector_similarity: true // AI-powered capability matching
})
```

**Vector Similarity Matching:**
- Analyzes task requirements and agent capabilities
- Finds optimal agent based on past performance
- Considers workload and availability

### Queue Management

Monitor and manage message queues:

```javascript
mcp__flow-nexus__workflow_queue_status({
  queue_name: "optional-specific-queue",
  include_messages: true // Show pending messages
})
```

## Agent Orchestration

### Full-Stack Development Pattern

```javascript
// 1. Initialize swarm with hierarchical topology
mcp__flow-nexus__swarm_init({
  topology: "hierarchical",
  maxAgents: 8,
  strategy: "specialized"
})

// 2. Spawn specialized agents
mcp__flow-nexus__agent_spawn({ type: "coordinator", name: "Project Manager" })
mcp__flow-nexus__agent_spawn({ type: "coder", name: "Backend Developer" })
mcp__flow-nexus__agent_spawn({ type: "coder", name: "Frontend Developer" })
mcp__flow-nexus__agent_spawn({ type: "coder", name: "Database Architect" })
mcp__flow-nexus__agent_spawn({ type: "analyst", name: "QA Engineer" })

// 3. Create development workflow
mcp__flow-nexus__workflow_create({
  name: "Full-Stack Development",
  steps: [
    { id: "requirements", action: "analyze_requirements", agent: "coordinator" },
    { id: "db_design", action: "design_schema", agent: "Database Architect" },
    { id: "backend", action: "build_api", agent: "Backend Developer", depends_on: ["db_design"] },
    { id: "frontend", action: "build_ui", agent: "Frontend Developer", depends_on: ["requirements"] },
    { id: "integration", action: "integrate", agent: "Backend Developer", depends_on: ["backend", "frontend"] },
    { id: "testing", action: "qa_testing", agent: "QA Engineer", depends_on: ["integration"] }
  ]
})

// 4. Execute workflow
mcp__flow-nexus__workflow_execute({
  workflow_id: "workflow_id",
  input_data: {
    project: "E-commerce Platform",
    tech_stack: ["Node.js", "React", "PostgreSQL"]
  }
})
```

### Research & Analysis Pattern

```javascript
// 1. Initialize mesh topology for collaborative research
mcp__flow-nexus__swarm_init({
  topology: "mesh",
  maxAgents: 5,
  strategy: "balanced"
})

// 2. Spawn research agents
mcp__flow-nexus__agent_spawn({ type: "researcher", name: "Primary Researcher" })
mcp__flow-nexus__agent_spawn({ type: "researcher", name: "Secondary Researcher" })
mcp__flow-nexus__agent_spawn({ type: "analyst", name: "Data Analyst" })
mcp__flow-nexus__agent_spawn({ type: "analyst", name: "Insights Analyst" })

// 3. Orchestrate research task
mcp__flow-nexus__task_orchestrate({
  task: "Research machine learning trends for 2025 and analyze market opportunities",
  strategy: "parallel",
  maxAgents: 4,
  priority: "high"
})
```

### CI/CD Pipeline Pattern

```javascript
mcp__flow-nexus__workflow_create({
  name: "Deployment Pipeline",
  description: "Automated testing, building, and multi-environment deployment",
  steps: [
    { id: "lint", action: "lint_code", agent: "code_quality", parallel: true },
    { id: "unit_test", action: "unit_tests", agent: "test_runner", parallel: true },
    { id: "integration_test", action: "integration_tests", agent: "test_runner", parallel: true },
    { id: "build", action: "build_artifacts", agent: "builder", depends_on: ["lint", "unit_test", "integration_test"] },
    { id: "security_scan", action: "security_scan", agent: "security", depends_on: ["build"] },
    { id: "deploy_staging", action: "deploy", agent: "deployer", depends_on: ["security_scan"] },
    { id: "smoke_test", action: "smoke_tests", agent: "test_runner", depends_on: ["deploy_staging"] },
    { id: "deploy_prod", action: "deploy", agent: "deployer", depends_on: ["smoke_test"] }
  ],
  triggers: ["github_push", "github_pr_merged"],
  metadata: {
    priority: 10,
    auto_rollback: true
  }
})
```

### Data Processing Pipeline Pattern

```javascript
mcp__flow-nexus__workflow_create({
  name: "ETL Pipeline",
  description: "Extract, Transform, Load data processing",
  steps: [
    { id: "extract", action: "extract_data", agent: "data_extractor" },
    { id: "validate_raw", action: "validate_data", agent: "validator", depends_on: ["extract"] },
    { id: "transform", action: "transform_data", agent: "transformer", depends_on: ["validate_raw"] },
    { id: "enrich", action: "enrich_data", agent: "enricher", depends_on: ["transform"] },
    { id: "load", action: "load_data", agent: "loader", depends_on: ["enrich"] },
    { id: "validate_final", action: "validate_data", agent: "validator", depends_on: ["load"] }
  ],
  triggers: ["schedule:0 2 * * *"], // Daily at 2 AM
  metadata: {
    retry_policy: "exponential_backoff",
    max_retries: 3
  }
})
```

## Templates & Patterns

### Use Pre-built Templates

```javascript
// Create swarm from template
mcp__flow-nexus__swarm_create_from_template({
  template_name: "full-stack-dev",
  overrides: {
    maxAgents: 6,
    strategy: "specialized"
  }
})

// List available templates
mcp__flow-nexus__swarm_templates_list({
  category: "quickstart", // Options: quickstart, specialized, enterprise, custom, all
  includeStore: true
})
```

**Available Template Categories:**

**Quickstart Templates:**
- `full-stack-dev`: Complete web development swarm
- `research-team`: Research and analysis swarm
- `code-review`: Automated code review swarm
- `data-pipeline`: ETL and data processing

**Specialized Templates:**
- `ml-development`: Machine learning project swarm
- `mobile-dev`: Mobile app development
- `devops-automation`: Infrastructure and deployment
- `security-audit`: Security analysis and testing

**Enterprise Templates:**
- `enterprise-migration`: Large-scale system migration
- `multi-repo-sync`: Multi-repository coordination
- `compliance-review`: Regulatory compliance workflows
- `incident-response`: Automated incident management

### Custom Template Creation

Save successful swarm configurations as reusable templates for future projects.

## Advanced Features

### Real-time Monitoring

```javascript
// Subscribe to execution streams
mcp__flow-nexus__execution_stream_subscribe({
  stream_type: "claude-flow-swarm",
  deployment_id: "deployment_id"
})

// Get execution status
mcp__flow-nexus__execution_stream_status({
  stream_id: "stream_id"
})

// List files created during execution
mcp__flow-nexus__execution_files_list({
  stream_id: "stream_id",
  created_by: "claude-flow"
})
```

### Swarm Metrics & Analytics

```javascript
// Get swarm performance metrics
mcp__flow-nexus__swarm_status({
  swarm_id: "id"
})

// Analyze workflow efficiency
mcp__flow-nexus__workflow_status({
  workflow_id: "id",
  include_metrics: true
})
```

### Multi-Swarm Coordination

Coordinate multiple swarms for complex, multi-phase projects:

```javascript
// Phase 1: Research swarm
const researchSwarm = await mcp__flow-nexus__swarm_init({
  topology: "mesh",
  maxAgents: 4
})

// Phase 2: Development swarm
const devSwarm = await mcp__flow-nexus__swarm_init({
  topology: "hierarchical",
  maxAgents: 8
})

// Phase 3: Testing swarm
const testSwarm = await mcp__flow-nexus__swarm_init({
  topology: "star",
  maxAgents: 5
})
```

## Best Practices

### 1. Choose the Right Topology

```javascript
// Simple projects: Star
mcp__flow-nexus__swarm_init({ topology: "star", maxAgents: 3 })

// Collaborative work: Mesh
mcp__flow-nexus__swarm_init({ topology: "mesh", maxAgents: 5 })

// Complex projects: Hierarchical
mcp__flow-nexus__swarm_init({ topology: "hierarchical", maxAgents: 10 })

// Sequential workflows: Ring
mcp__flow-nexus__swarm_init({ topology: "ring", maxAgents: 4 })
```

### 2. Optimize Agent Assignment

```javascript
// Use vector similarity for optimal matching
mcp__flow-nexus__workflow_agent_assign({
  task_id: "complex-task",
  use_vector_similarity: true
})
```

### 3. Implement Proper Error Handling

```javascript
mcp__flow-nexus__workflow_create({
  name: "Resilient Workflow",
  steps: [...],
  metadata: {
    retry_policy: "exponential_backoff",
    max_retries: 3,
    timeout: 300000, // 5 minutes
    on_failure: "notify_and_rollback"
  }
})
```

### 4. Monitor and Scale

```javascript
// Regular monitoring
const status = await mcp__flow-nexus__swarm_status()

// Scale based on workload
if (status.workload > 0.8) {
  await mcp__flow-nexus__swarm_scale({ target_agents: status.agents + 2 })
}
```

### 5. Use Async Execution for Long-Running Workflows

```javascript
// Long-running workflows should use message queues
mcp__flow-nexus__workflow_execute({
  workflow_id: "data-pipeline",
  async: true // Non-blocking execution
})

// Monitor progress
mcp__flow-nexus__workflow_queue_status({ include_messages: true })
```

### 6. Clean Up Resources

```javascript
// Destroy swarm when complete
mcp__flow-nexus__swarm_destroy({ swarm_id: "id" })
```

### 7. Leverage Templates

```javascript
// Use proven templates instead of building from scratch
mcp__flow-nexus__swarm_create_from_template({
  template_name: "code-review",
  overrides: { maxAgents: 4 }
})
```

## Integration with Claude Flow

Flow Nexus swarms integrate seamlessly with Claude Flow hooks:

```bash
# Pre-task coordination setup
npx claude-flow@alpha hooks pre-task --description "Initialize swarm"

# Post-task metrics export
npx claude-flow@alpha hooks post-task --task-id "swarm-execution"
```

## Common Use Cases

### 1. Multi-Repo Development
- Coordinate development across multiple repositories
- Synchronized testing and deployment
- Cross-repo dependency management

### 2. Research Projects
- Distributed information gathering
- Parallel analysis of different data sources
- Collaborative synthesis and reporting

### 3. DevOps Automation
- Infrastructure as Code deployment
- Multi-environment testing
- Automated rollback and recovery

### 4. Code Quality Workflows
- Automated code review
- Security scanning
- Performance benchmarking

### 5. Data Processing
- Large-scale ETL pipelines
- Real-time data transformation
- Data validation and quality checks

## Authentication & Setup

```bash
# Install Flow Nexus
npm install -g flow-nexus@latest

# Register account
npx flow-nexus@latest register

# Login
npx flow-nexus@latest login

# Add MCP server to Claude Code
claude mcp add flow-nexus npx flow-nexus@latest mcp start
```

## Support & Resources

- **Platform**: https://flow-nexus.ruv.io
- **Documentation**: https://github.com/ruvnet/flow-nexus
- **Issues**: https://github.com/ruvnet/flow-nexus/issues

## Core Principles

Flow Nexus Swarm operates on 3 fundamental principles:

### Principle 1: Topology-Driven Agent Coordination
Swarm behavior emerges from network topology - hierarchical trees for delegation, mesh networks for collaboration, rings for pipelines, stars for centralization.

In practice:
- Choose hierarchical topology for complex projects with clear coordinator roles
- Use mesh topology for research tasks requiring peer-to-peer collaboration
- Apply ring topology for sequential workflows with ordered handoffs
- Select star topology for simple task delegation with centralized orchestration

### Principle 2: Event-Driven Workflow Orchestration
Workflows execute asynchronously via message queues, enabling non-blocking parallel execution with dependency management.

In practice:
- Define workflow steps with explicit dependencies using `depends_on` arrays
- Mark independent steps with `parallel: true` for concurrent execution
- Use async execution (`async: true`) for long-running workflows to avoid blocking
- Implement retry policies and timeout limits for resilient workflows

### Principle 3: Intelligent Agent Assignment via Vector Similarity
Agents match to tasks through semantic similarity search, not manual assignment, optimizing capability-to-requirement alignment.

In practice:
- Enable `use_vector_similarity: true` for optimal agent-task matching
- Let the system analyze task requirements and agent capabilities automatically
- Trust the platform to consider past performance and current workload
- Override with explicit `agent_type` only when domain constraints require it

-----------|---------|----------|
| **Wrong Topology Selection** | Using star topology for collaborative research or hierarchical for simple tasks wastes coordination overhead | Match topology to workflow: mesh for collaboration, hierarchical for delegation, ring for pipelines, star for simplicity |
| **Ignoring Dependencies** | Executing dependent steps in parallel causes race conditions and corrupted state | Always define `depends_on` arrays; use parallel execution only for truly independent steps |
| **Manual Agent Assignment** | Hardcoding agent assignments ignores capability matching and load balancing | Use `use_vector_similarity: true` to leverage AI-powered agent selection |
| **Sync Execution for Long Workflows** | Blocking on multi-hour workflows prevents concurrent work | Set `async: true` for workflows >5 minutes; monitor via `workflow_queue_status()` |
| **No Failure Handling** | Swarms fail silently or cascade failures without recovery | Implement `retry_policy: "exponential_backoff"`, set `max_retries`, define `on_failure` actions |

---

## Conclusion

The Flow Nexus Swarm skill enables cloud-based multi-agent orchestration with topology-aware coordination and event-driven workflow automation. By separating workflow definition from execution infrastructure, it provides scalable agent coordination without local resource constraints.

Use this skill for complex multi-agent tasks requiring parallel execution (6+ agents), distributed compute workloads, or sophisticated workflow pipelines with dependencies. The swarm architecture excels at full-stack development, research projects, CI/CD automation, and data processing pipelines where coordination overhead justifies cloud infrastructure.

Key takeaways: Select topology based on coordination patterns, leverage event-driven workflows for long-running tasks, and trust vector similarity for agent assignment. The platform's template library, real-time monitoring, and multi-swarm coordination capabilities enable enterprise-scale agent orchestration with minimal configuration overhead.