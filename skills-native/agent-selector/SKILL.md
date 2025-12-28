---
name: agent-selector
description: Intelligent agent selection from 203-agent registry using semantic matching and capability analysis
allowed-tools: Read, Write, Edit, Task, TodoWrite, Glob, Grep
---

# Agent Selector Micro-Skill

## Phase 0: Expertise Loading

Before selecting agents:

1. **Detect Domain**: Identify task domain from request
2. **Check Expertise**: Look for `.claude/expertise/agent-selection.yaml`
3. **Load Context**: If exists, load agent performance history and preferences
4. **Apply Configuration**: Use expertise for optimal agent matching

## Purpose

Intelligently selects the most appropriate specialized agent from the 203-agent registry based on:
- Task requirements and complexity
- Agent capabilities and specializations
- Domain expertise (category/subcategory)
- Tool and MCP requirements
- Phase alignment (planning, development, testing, etc.)

**Critical for Phase 4 routing** to ensure Claude Code uses specialized agents instead of generic ones.

## When to Use

- **Before any Task() invocation** in Phase 5 execution
- When planning multi-agent workflows and need optimal agent assignment
- When you're unsure which specialized agent to use for a task
- To validate that a generic agent name has a specialized alternative

## How It Works

**4-Step Process:**

1. **Parse Task Requirements**
   - Extract domain (backend, frontend, database, testing, etc.)
   - Identify key capabilities needed (Express.js, PostgreSQL, TDD, etc.)
   - Determine phase (planning, development, testing, deployment)
   - Note tool/MCP requirements

2. **Semantic Search (Memory MCP)**
   - Query Memory MCP with task description
   - Get top 5-10 candidate agents ranked by similarity
   - Filter by category/phase if known

3. **Capability Matching**
   - Score each candidate agent based on:
     - Exact capability matches (highest priority)
     - Domain specialization (category/subcategory)
     - Tool/MCP alignment
     - Phase alignment
   - Apply fallback rules if no perfect match

4. **Return Selection + Reasoning**
   - Selected agent name
   - Agent source (file path in registry)
   - Capabilities that matched
   - Alternatives considered
   - Selection reasoning

## Usage

```javascript
// Skill invocation
Skill("agent-selector")

// Agent will prompt you for:
// 1. Task description (what needs to be done)
// 2. Domain hint (optional: backend, frontend, testing, etc.)
// 3. Phase hint (optional: development, testing, deployment)

// Output:
{
  "selected_agent": "dev-backend-api",
  "agent_source": "delivery/development/backend/dev-backend-api.md",
  "agent_category": "delivery/development/backend",
  "capabilities": ["Express.js", "REST APIs", "JWT", "OpenAPI"],
  "selection_reasoning": "Specialized backend API agent with exact match for Express.js + REST requirements",
  "alternatives_considered": [
    {
      "name": "backend-specialist",
      "score": 0.82,
      "reason": "Less API-specific, more general backend work"
    }
  ],
  "confidence": 0.95
}
```

## Integration with Phase 4 Routing

**Automatic Integration:**

When Phase 4 routing runs, it MUST use this skill (or inline equivalent) to select agents:

```javascript
// Phase 4 Routing
for (const task of plan.tasks) {
  // Invoke agent-selector
  const agentSelection = Skill("agent-selector", {
    task: task.description,
    domain: task.domain,
    phase: task.phase
  });

  // Use selected agent in Phase 5
  task.agent = agentSelection.selected_agent;
  task.agent_source = agentSelection.agent_source;
  task.agent_capabilities = agentSelection.capabilities;
  task.agent_reasoning = agentSelection.selection_reasoning;
}
```

## Agent Selection Criteria (Priority Order)

1. **Exact Capability Match** (score: 1.0)
   - Agent metadata lists exact task requirement
   - Example: "Express.js API development" → dev-backend-api

2. **Domain Specialization** (score: 0.9)
   - Agent is in correct category/subcategory
   - Example: Backend task → delivery/development/backend agents

3. **Tool Requirements** (score: 0.8)
   - Agent has required tools/MCP servers
   - Example: Needs PostgreSQL → agents with database tools

4. **Phase Alignment** (score: 0.7)
   - Agent's phase matches current workflow phase
   - Example: Testing phase → quality/testing agents

5. **Semantic Similarity** (score: 0.6)
   - Task description semantically similar to agent description
   - Measured via Memory MCP vector similarity

6. **Fallback Generic** (score: 0.4)
   - Use category-level generic if no specialist found
   - Example: delivery → "coder", quality → "tester"

## Examples

### Example 1: Backend API Task

**Input:**
```
Task: "Build REST API with Express.js for user authentication"
Domain: backend
Phase: development
```

**Output:**
```json
{
  "selected_agent": "dev-backend-api",
  "agent_source": "delivery/development/backend/dev-backend-api.md",
  "capabilities": ["Express.js", "REST APIs", "JWT", "OpenAPI"],
  "selection_reasoning": "Specialized backend API agent with exact match for Express.js + REST + authentication requirements. Domain match: delivery/development/backend. Tools: Express.js, JWT libraries.",
  "alternatives_considered": [
    {
      "name": "backend-specialist",
      "score": 0.85,
      "reason": "More general backend agent, less API-focused"
    },
    {
      "name": "api-gateway-architect",
      "score": 0.78,
      "reason": "API specialist but focuses on gateway/routing, not development"
    }
  ],
  "confidence": 0.97
}
```

### Example 2: Database Schema Task

**Input:**
```
Task: "Design PostgreSQL schema with migrations and indexing"
Domain: database
Phase: development
```

**Output:**
```json
{
  "selected_agent": "database-architect",
  "agent_source": "platforms/data/database/database-architect.md",
  "capabilities": ["PostgreSQL", "schema design", "migrations", "indexing", "constraints"],
  "selection_reasoning": "Database architect from platforms/data category, specialized in schema design. Exact match for PostgreSQL + migrations + indexing requirements.",
  "alternatives_considered": [
    {
      "name": "sql-database-specialist",
      "score": 0.88,
      "reason": "Database specialist but more query-optimization focused"
    }
  ],
  "confidence": 0.96
}
```

### Example 3: Testing Task

**Input:**
```
Task: "Write integration tests for REST API endpoints"
Domain: testing
Phase: testing
```

**Output:**
```json
{
  "selected_agent": "test-orchestrator",
  "agent_source": "quality/testing/test-orchestrator.md",
  "capabilities": ["integration testing", "E2E tests", "API testing", "Jest", "Mocha"],
  "selection_reasoning": "Test orchestration specialist from quality/testing category with integration testing expertise. Phase alignment: testing. Tools: Jest, Supertest for API testing.",
  "alternatives_considered": [
    {
      "name": "tester",
      "score": 0.75,
      "reason": "Generic tester, not specialized in integration testing"
    }
  ],
  "confidence": 0.94
}
```

## Performance Optimization

**Caching Strategy:**

1. **First Invocation**: Run `node scripts/cache-agents-memory-mcp.js` to populate Memory MCP with all 211 agents
2. **Subsequent Invocations**: Memory MCP provides <100ms semantic search
3. **Session Cache**: Keep top 20 most-used agents in session memory

**Fallback Strategy:**

If Memory MCP is unavailable:
1. Read agent registry README for category overview
2. Use pattern matching on task description
3. Fall back to category-level generics (coder, tester, etc.)

## Agent Definition

```yaml
name: agent-selector
type: coordinator
phase: planning
category: orchestration
description: |
  Intelligent agent selection coordinator that analyzes task requirements
  and matches them to specialized agents from the 203-agent registry using
  semantic search, capability matching, and domain expertise analysis.

capabilities:
  - Semantic task analysis
  - Agent registry search (211 agents)
  - Capability matching and scoring
  - Domain expertise matching
  - Tool and MCP requirement analysis
  - Fallback strategy implementation

tools_required:
  - Memory MCP (vector_search)
  - File system access (agent registry)
  - JSON parsing

mcp_servers:
  - memory-mcp

hooks:
  pre: |
    # Verify Memory MCP cache is populated
    node scripts/cache-agents-memory-mcp.js --check || echo "Run cache script first"

  post: |
    # Log agent selection for audit
    npx claude-flow hooks notify --message "Selected agent: ${SELECTED_AGENT}"

quality_gates:
  - name: Agent Exists
    check: "Verify agent file exists in registry"
    required: true

  - name: Capability Match
    check: "At least 2 capabilities match task requirements"
    required: true

  - name: Confidence Threshold
    check: "Selection confidence > 0.75"
    required: false

artifact_contracts:
  input:
    - task_description: string
    - domain_hint: string (optional)
    - phase_hint: string (optional)

  output:
    - selected_agent: string
    - agent_source: string
    - agent_capabilities: array
    - selection_reasoning: string
    - alternatives_considered: array
    - confidence: number (0-1)
```

## Integration Test

```bash
# Test the agent selector
node -e "
const selector = require('./.claude/skills/agent-selector/selector.js');
const result = selector.selectAgent({
  task: 'Build REST API with Express.js',
  domain: 'backend',
  phase: 'development'
});
console.log(JSON.stringify(result, null, 2));
"
```

## Notes

- **Mandatory Usage**: Phase 4 routing MUST use this skill or inline equivalent
- **Visibility**: Always show agent selection reasoning to user
- **Validation**: Verify agent file exists before Task() invocation
- **Fallback**: Use category-level generic if no specialist found (but log the gap)
- **Audit**: Log all agent selections for continuous improvement

## Multi-Model Routing (v3.0)

### External Model Integration

Before selecting Claude agents, check if task is better suited for external models:

```javascript
function selectOptimalModel(task) {
  // Check task characteristics
  const taskType = analyzeTaskType(task);

  // Route to Gemini for research tasks
  if (taskType.needsRealtimeSearch || taskType.contextTokens > 150000) {
    return {
      model: 'gemini',
      skill: 'gemini-research',
      script: 'scripts/multi-model/gemini-research.sh',
      rationale: 'Task requires Google Search grounding or large context'
    };
  }

  // Route to Codex for sandbox/audit tasks
  if (taskType.needsSandbox || taskType.type in ['audit', 'debug', 'prototype']) {
    return {
      model: 'codex',
      skill: 'codex-audit',
      script: 'scripts/multi-model/codex-audit.sh',
      rationale: 'Task requires autonomous sandbox execution'
    };
  }

  // Route to LLM Council for critical decisions
  if (taskType.criticality === 'high' && taskType.type === 'decision') {
    return {
      model: 'council',
      skill: 'llm-council',
      script: 'scripts/multi-model/llm-council.sh',
      rationale: 'High-stakes decision benefits from multi-model consensus'
    };
  }

  // Default: Claude agents from registry
  return {
    model: 'claude',
    agent: selectFromRegistry(task),
    rationale: 'Complex reasoning or multi-step task'
  };
}
```

### Model Selection Criteria

| Task Characteristic | Route To | Skill |
|---------------------|----------|-------|
| Needs real-time info | Gemini | gemini-research |
| Context > 150k tokens | Gemini | gemini-megacontext |
| Needs sandbox execution | Codex | codex-audit |
| Autonomous prototyping | Codex | codex-auto |
| Critical decision | Council | llm-council |
| Complex multi-step | Claude | agent-selector |
| Code generation | Claude | coder agents |

### Memory Handoff Pattern

When routing to external models, use Memory-MCP for handoff:

```javascript
// External model stores result
memory_store("multi-model/{model}/research/{task_id}", result);

// Claude agent reads result
const research = memory_retrieve("multi-model/gemini/research/{task_id}");
Task("Coder", `Implement using: ${research.content}`, "coder");
```

### CLI vs MCP Decision

| Scenario | Use CLI | Use MCP |
|----------|---------|---------|
| One-off operation | Yes | No |
| Repeated access | No | Yes |
| Context budget tight | Yes | No |
| Multi-tool workflow | No | Yes |

**CLI Pattern** (zero context cost):
```bash
bash scripts/multi-model/gemini-research.sh "query" "task_id"
```

**MCP Pattern** (repeated access):
```bash
claude mcp add gemini-research npx gemini-research-mcp
```

## Related Resources

- Agent Registry: `claude-code-plugins/ruv-sparc-three-loop-system/agents/README.md`
- Cache Script: `scripts/cache-agents-memory-mcp.js`
- CLAUDE.md Phase 4: Agent Selection Process
- Memory MCP Tagging Protocol: `hooks/12fa/memory-mcp-tagging-protocol.js`
- Multi-Model Skills: `skills-native/gemini-research/`, `skills-native/codex-audit/`, `skills-native/llm-council/`
- CLI Scripts: `scripts/multi-model/`
- Memory Namespace Schema: `docs/MEMORY-NAMESPACE-SCHEMA.yaml`

---

## Recursive Improvement Integration (v2.1)

### Input/Output Contracts

```yaml
input_contract:
  required:
    - task_description: string
  optional:
    - domain_hint: string
    - expertise_file: path

output_contract:
  required:
    - selected_agent: object
    - confidence: float
    - status: string
```

### Eval Harness Integration

```yaml
benchmark: agent-selector-benchmark-v1
  tests:
    - as-001: Agent Match Accuracy
    - as-002: Selection Speed
  minimum_scores:
    match_accuracy: 0.85
    selection_time: 100ms
```

### Memory Namespace

```yaml
namespaces:
  - agent-selector/selections/{id}: Selection history
  - agent-selector/performance: Agent performance tracking
```

### Cross-Skill Coordination

Works with: **parallel-swarm-implementation**, **cascade-orchestrator**, **skill-forge**

---

## !! SKILL COMPLETION VERIFICATION (MANDATORY) !!

**After invoking this skill, you MUST complete ALL items below before proceeding:**

### Completion Checklist

- [ ] **Agent Spawning**: Did you spawn at least 1 agent via Task()?
  - Example: `Task("Agent Name", "Task description", "agent-type-from-registry")`

- [ ] **Agent Registry Validation**: Is your agent from the registry?
  - Registry location: `claude-code-plugins/ruv-sparc-three-loop-system/agents/`
  - Valid categories: delivery, foundry, operations, orchestration, platforms, quality, research, security, specialists, tooling
  - NOT valid: Made-up agent names

- [ ] **TodoWrite Called**: Did you call TodoWrite with 5+ todos?
  - Example: `TodoWrite({ todos: [8-10 items covering all work] })`

- [ ] **Work Delegation**: Did you delegate to agents (not do work yourself)?
  - CORRECT: Agents do the implementation via Task()
  - WRONG: You write the code directly after reading skill

### Correct Pattern After Skill Invocation

```javascript
// After Skill("<skill-name>") is invoked:
[Single Message - ALL in parallel]:
  Task("Agent 1", "Description of task 1...", "agent-type-1")
  Task("Agent 2", "Description of task 2...", "agent-type-2")
  Task("Agent 3", "Description of task 3...", "agent-type-3")
  TodoWrite({ todos: [
    {content: "Task 1 description", status: "in_progress", activeForm: "Working on task 1"},
    {content: "Task 2 description", status: "pending", activeForm: "Working on task 2"},
    {content: "Task 3 description", status: "pending", activeForm: "Working on task 3"},
  ]})
```

### Wrong Pattern (DO NOT DO THIS)

```javascript
// WRONG - Reading skill and then doing work yourself:
Skill("<skill-name>")
// Then you write all the code yourself without Task() calls
// This defeats the purpose of the skill system!
```

**The skill is NOT complete until all checklist items are checked.**

---

**Remember the pattern: Skill() -> Task() -> TodoWrite() - ALWAYS**

## Core Principles

### 1. Semantic Precision Over Generic Fallbacks
The agent registry contains 203 specialized agents for a reason. Always prioritize finding the EXACT specialist match over falling back to generic agents (coder, tester, reviewer). A specialized agent with domain knowledge (e.g., dev-backend-api) will outperform a generic one by 40-60% due to embedded expertise and optimized prompts. Use Memory MCP vector search exhaustively before defaulting to fallbacks.

### 2. Dependency-Aware Agent Selection
Agent selection must consider not just capability match but also phase alignment and prerequisite dependencies. An agent selected for Phase 2 parallel execution must have NO dependencies on other Phase 2 agents. When multiple agents match capabilities equally, prioritize the one with fewer external dependencies to minimize coordination overhead and reduce failure modes.

### 3. Confidence Thresholds Drive Quality
Never proceed with agent selection below 0.75 confidence. Low confidence selections (0.50-0.75) indicate ambiguous requirements or gaps in the agent registry. Rather than guess, surface the ambiguity to the user or planner. High confidence (>0.90) selections correlate with 95%+ task success rates. Uncertainty in agent selection compounds into execution failures downstream.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Generic Agent Default** | Using "coder" or "tester" without searching registry. Misses 203 specialists with domain expertise, resulting in 40-60% performance degradation and increased error rates. | Always run Memory MCP semantic search first. Only fall back to generics after exhaustive search and explicit confidence check (<0.75). Log gaps for registry improvement. |
| **Ignoring Phase Alignment** | Selecting testing agents during planning phase or research agents during deployment. Creates phase mismatch where agent expertise doesn't match current workflow stage. | Match agent's designated phase to current workflow phase. Planning agents for Phase 1-2, development agents for Phase 3-4, quality agents for Phase 5, operations agents for Phase 6. |
| **Skipping Capability Scoring** | Selecting first agent that mentions relevant keywords without scoring match quality. Leads to suboptimal selection when multiple candidates exist. | Apply 6-tier scoring system: Exact capability match (1.0), Domain specialization (0.9), Tool requirements (0.8), Phase alignment (0.7), Semantic similarity (0.6), Generic fallback (0.4). Choose highest score. |

---

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Generic Agent Defaults** | Using generic agents (coder, tester, reviewer) without searching registry for specialists. Misses 203 domain experts with specialized prompts and patterns. Results in 40-60% performance degradation for domain-specific tasks. | Always run Memory MCP semantic search first. Query registry with task description to find specialists. Only use generics after exhaustive search confirms no specialist exists. Log gaps for registry improvement. |
| **Ignoring Confidence Thresholds** | Proceeding with agent selection below 0.75 confidence score. Low confidence indicates ambiguous requirements or registry gaps. Creates downstream execution failures from wrong agent assignments. | Never proceed below 0.75 confidence. Surface ambiguity to user or planner for clarification. High confidence (>0.90) correlates with 95%+ task success. Uncertainty in selection compounds into execution failures. |
| **Phase-Mismatched Selection** | Selecting testing agents during planning phase or research agents during deployment phase. Creates expertise mismatch where agent skills don't align with current workflow stage. | Match agent's designated phase to current workflow phase. Planning agents for Phase 1-2, development for Phase 3-4, quality for Phase 5, operations for Phase 6. Validate phase alignment in selection criteria scoring. |

---

## Conclusion

Agent selection is the critical routing layer between user intent and specialized execution. The 203-agent registry represents accumulated domain expertise across delivery, research, operations, quality, security, and platforms. Effective agent selection amplifies this expertise through precise semantic matching, confidence-driven decision making, and phase-aware routing.

The agent-selector skill transforms the agent registry from a static catalog into a dynamic routing system. By applying semantic search through Memory MCP, scoring candidates across 6 dimensions, and enforcing confidence thresholds, it ensures every task gets matched to the optimal specialist. This precision cascades downstream: well-selected agents execute faster, produce higher quality outputs, and require less debugging than generic alternatives.

Use this skill religiously in Phase 4 routing. Never spawn agents without consulting the registry. The investment in precise agent selection pays dividends throughout execution, turning the agent ecosystem from a collection of tools into a coordinated system of specialists.