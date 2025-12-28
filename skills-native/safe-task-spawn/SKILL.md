---
name: safe-task-spawn
description: Skill for safe-task-spawn
---

# Safe Task Spawn - Registry-Validated Task Spawning

**Version**: 1.0.0 (Gold Tier)
**Purpose**: Prevent invalid agent spawns through registry validation, skill requirement matching, and comprehensive audit logging

## Overview

Safe Task Spawn is a validated wrapper around Task() calls that acts as a security gate for agent spawning. Instead of directly calling Task() with potentially invalid agent types, this skill validates against the canonical agent registry at `claude-code-plugins/ruv-sparc-three-loop-system/agents/`, ensures spawned agents match skill requirements, and logs all attempts to Memory MCP for audit trails.

**The Problem**:
- Skills spawn agents with Task() using arbitrary agent_type strings
- No validation that agent_type exists in the registry (211 valid agents)
- No verification that spawned agent matches what the skill needs
- No audit trail of spawn attempts (success or failure)
- Silent failures when invalid agents are requested

**The Solution**:
- Validate agent_type against canonical registry before spawning
- Match agent capabilities to skill requirements
- Provide clear error messages with suggestions from registry
- Log all spawn attempts to Memory MCP with WHO/WHEN/PROJECT/WHY tags
- Return validated Task() call or actionable error

## When to Use This Skill

Use **safe-task-spawn** when:
- Any skill needs to spawn agents via Task() calls
- Orchestration workflows coordinate multiple agents
- You need audit trails of agent spawn attempts
- You want to prevent invalid agent spawns at runtime
- Skills require specific agent capabilities/categories
- Debugging why Task() calls are failing silently

**Auto-triggers on keywords**: "spawn agent", "Task()", "delegate to agent", "create task", "agent spawning"

## When NOT to Use This Skill

Skip **safe-task-spawn** when:
- Using hardcoded agents known to be valid (coder, researcher, tester, reviewer)
- Direct Task() call is required for performance (already validated)
- Working in development mode where failures are acceptable
- Agent registry is unavailable (fallback to direct Task())

## Core Principles

### 1. Fail Fast with Actionable Errors
Invalid agent spawns should fail immediately with clear suggestions from the registry, not spawn generic agents or fail silently.

**Example**:
```
ERROR: Agent type 'backend-developer' not found in registry

Did you mean one of these?
- backend-dev (delivery/development/backend/dev-backend-api.md)
- backend-api-enhanced (delivery/development/backend/dev-backend-api-enhanced.md)
- golang-backend-specialist (delivery/development/golang/golang-backend-specialist.md)

Registry path: claude-code-plugins/ruv-sparc-three-loop-system/agents/
```

### 2. Skill-Agent Compatibility Validation
When a skill provides context about required agent capabilities, validate the requested agent matches those requirements.

**Example**:
```javascript
// Skill requires backend API development
skill_context = {
  required_capabilities: ["api-design", "database-integration", "authentication"],
  category: "delivery",
  phase: "development"
}

// Validates agent has required capabilities
safe_task_spawn("backend-dev", "Build REST API...", skill_context)
// ✅ PASS: backend-dev has all required capabilities

safe_task_spawn("frontend-dev", "Build REST API...", skill_context)
// ❌ FAIL: frontend-dev missing "api-design", "database-integration"
```

### 3. Comprehensive Audit Logging
Every spawn attempt (success or failure) is logged to Memory MCP for debugging, compliance, and pattern analysis.

**Example**:
```javascript
// Logged to Memory MCP
{
  "namespace": "orchestration/safe-task-spawn/{project}/{timestamp}",
  "agent_type": "backend-dev",
  "description": "Implement authentication endpoints",
  "status": "success",
  "skill_context": {...},
  "validation_results": {
    "registry_found": true,
    "capabilities_match": true,
    "category_match": true
  },
  "tags": {
    "who": "safe-task-spawn",
    "when": "2025-12-17T10:30:00Z",
    "project": "api-development",
    "why": "task-spawning"
  }
}
```

## Workflow

### Phase 1: Input Validation
```
Input: agent_type, description, prompt, skill_context (optional)
├─ Validate agent_type is non-empty string
├─ Validate description is non-empty string
├─ Validate prompt is non-empty string
└─ Parse skill_context for requirements (if provided)
```

### Phase 2: Registry Lookup
```
Load Registry:
├─ Read: claude-code-plugins/ruv-sparc-three-loop-system/agents/README.md
├─ Parse: 211 agents across 10 categories
├─ Build index: agent_type -> metadata (category, capabilities, phase, file_path)
└─ Cache: Registry in memory for subsequent calls

Search:
├─ Exact match: agent_type === registry[agent_type]
├─ Fuzzy match: Levenshtein distance < 3 for suggestions
└─ Category match: Filter by skill_context.category if provided
```

### Phase 3: Capability Validation (if skill_context provided)
```
Match Requirements:
├─ required_capabilities: Agent must have ALL
├─ category: Agent category must match
├─ phase: Agent phase must match (planning, development, testing, etc.)
├─ tools_required: Agent must support required tools
└─ mcp_servers: Agent must have required MCP servers

Score:
├─ Calculate match score (0-100)
├─ Threshold: >= 80 to pass
└─ Return: Pass/fail with detailed breakdown
```

### Phase 4: Spawn or Error
```
If valid:
├─ Spawn: Task(agent_type, description, prompt)
├─ Log: Success to Memory MCP
└─ Return: Task object

If invalid:
├─ Generate suggestions from registry (fuzzy match, category match)
├─ Log: Failure to Memory MCP with suggestions
├─ Return: Error with actionable guidance
└─ Throw: ValidationError with structured details
```

### Phase 5: Audit Logging
```
Store to Memory MCP:
├─ Namespace: "orchestration/safe-task-spawn/{project}/{timestamp}"
├─ Tags: WHO (safe-task-spawn), WHEN (ISO), PROJECT (detected), WHY (task-spawning)
├─ Metadata: {agent_type, description, status, validation_results, suggestions}
└─ TTL: 30 days (configurable)
```

## Input Contract

```typescript
interface SafeTaskSpawnInput {
  agent_type: string;              // Agent identifier (e.g., "backend-dev")
  description: string;             // Task description (e.g., "Build REST API")
  prompt: string;                  // Detailed instructions for agent
  skill_context?: {                // Optional skill requirements
    required_capabilities?: string[];
    category?: string;             // delivery, operations, quality, etc.
    phase?: string;                // planning, development, testing, etc.
    tools_required?: string[];     // Read, Write, Bash, etc.
    mcp_servers?: {
      required?: string[];         // memory-mcp, ruv-swarm, etc.
      optional?: string[];
    };
  };
  project_id?: string;             // For audit logging namespace
  validate_only?: boolean;         // If true, validate but don't spawn
}
```

## Output Contract

### Success Case
```typescript
interface SafeTaskSpawnSuccess {
  status: "success";
  task: Task;                      // Spawned Task object
  agent_metadata: {
    agent_type: string;
    category: string;
    capabilities: string[];
    file_path: string;
  };
  validation_results: {
    registry_found: true;
    capabilities_match: boolean;
    category_match: boolean;
    match_score: number;           // 0-100
  };
  audit_log_key: string;           // Memory MCP key for audit record
}
```

### Failure Case
```typescript
interface SafeTaskSpawnFailure {
  status: "error";
  error_type: "agent_not_found" | "capability_mismatch" | "validation_failed";
  message: string;                 // Human-readable error
  suggestions: Array<{
    agent_type: string;
    category: string;
    match_score: number;           // 0-100 (similarity to requested)
    file_path: string;
    reason: string;                // Why this is suggested
  }>;
  validation_results: {
    registry_found: boolean;
    capabilities_match: boolean;
    category_match: boolean;
    match_score: number;
  };
  audit_log_key: string;           // Memory MCP key for failure record
}
```

## Anti-Patterns Table

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|-------------|------------------|
| Direct Task("backend-developer", ...) without validation | agent_type "backend-developer" doesn't exist (correct: "backend-dev") | safe_task_spawn("backend-dev", ...) validates against registry |
| Spawning generic "coder" when specific specialist needed | Generic coder lacks domain expertise (API design, database, etc.) | Use skill_context to match specialist: backend-dev, frontend-dev, etc. |
| No audit trail of spawn attempts | Cannot debug why tasks fail or analyze patterns | All spawns logged to Memory MCP with validation results |
| Silent failures when agent not found | Task fails with no guidance on correct agent | Returns error with fuzzy-matched suggestions from registry |
| Hardcoding agent_type without checking registry | Registry evolves, hardcoded types become stale | Validate dynamically against live registry |
| Spawning agent with missing MCP servers | Agent requires memory-mcp but it's not enabled | Validate mcp_servers.required and prompt to enable if missing |

## Implementation Examples

### Example 1: Basic Validation
```javascript
// Direct Task() call (risky - no validation)
Task("backend-developer", "Build REST API", "Implement user auth endpoints...")
// ❌ FAIL: "backend-developer" not in registry

// Safe Task Spawn (validated)
safe_task_spawn(
  "backend-dev",  // Validated against registry
  "Build REST API",
  "Implement user authentication endpoints with JWT..."
)
// ✅ SUCCESS: Spawns backend-dev agent
// ✅ LOGGED: Audit record in Memory MCP
```

### Example 2: Skill Context Validation
```javascript
// Skill requires specific capabilities
const skill_context = {
  required_capabilities: ["api-design", "authentication", "database-integration"],
  category: "delivery",
  phase: "development",
  mcp_servers: {
    required: ["memory-mcp"]
  }
};

// Attempt 1: Wrong specialist
safe_task_spawn("frontend-dev", "Build REST API", "...", skill_context)
// ❌ FAIL: frontend-dev missing "api-design", "database-integration"
// Returns suggestions: backend-dev, golang-backend-specialist, rust-systems-developer

// Attempt 2: Correct specialist
safe_task_spawn("backend-dev", "Build REST API", "...", skill_context)
// ✅ SUCCESS: backend-dev has all required capabilities (match_score: 95)
```

### Example 3: Validate-Only Mode
```javascript
// Pre-flight validation before orchestration
const validation = safe_task_spawn(
  "ml-training-agent",
  "Train neural network",
  "...",
  { validate_only: true }  // Don't spawn, just validate
)

if (validation.status === "success") {
  // Proceed with orchestration
  orchestrate_ml_pipeline()
} else {
  // Handle invalid agent, show suggestions
  console.error(validation.message)
  console.log("Suggestions:", validation.suggestions)
}
```

### Example 4: Audit Log Analysis
```javascript
// Query Memory MCP for spawn patterns
const spawn_logs = memory_retrieve({
  pattern: "orchestration/safe-task-spawn/*",
  filters: {
    status: "error",  // Only failed spawns
    time_range: "last_7_days"
  }
})

// Analyze common failures
const failures = spawn_logs.map(log => ({
  requested: log.agent_type,
  suggestions: log.suggestions[0].agent_type
}))

// Identify patterns (e.g., "backend-developer" -> "backend-dev" is common mistake)
```

## Registry Structure

The agent registry is organized into 10 categories:

| Category | Agent Count | Example Agents |
|----------|-------------|----------------|
| delivery | 18 | backend-dev, frontend-dev, sparc-architect |
| foundry | 19 | base-template-generator, skill-boilerplate-generator |
| operations | 28 | cicd-engineer, terraform-provisioner, kubernetes-specialist |
| orchestration | 21 | hierarchical-coordinator, byzantine-coordinator |
| platforms | 44 | automl-optimizer, flow-nexus-agent, sql-database-specialist |
| quality | 18 | code-analyzer, test-orchestrator, functionality-audit |
| research | 11 | archivist, researcher, root-cause-analyzer |
| security | 5 | soc-compliance-auditor, penetration-testing-agent |
| specialists | 18 | business-analyst, quant-analyst, logistics-optimizer |
| tooling | 24 | api-docs, pr-manager, github-release-manager |

**Registry Path**: `claude-code-plugins/ruv-sparc-three-loop-system/agents/`
**Total Agents**: 211 (as of 2025-11-26)

## Error Messages

### Agent Not Found
```
ERROR: Agent type 'ml-trainer' not found in registry (211 agents)

Did you mean one of these?
1. automl-optimizer (platforms/ai-ml/automl/automl-optimizer.md)
   - Category: platforms
   - Capabilities: hyperparameter-tuning, model-selection, neural-architecture-search
   - Match: 78% (similar name, correct category)

2. ml-developer (platforms/ai-ml/ml-developer.md)
   - Category: platforms
   - Capabilities: model-training, dataset-preparation, experiment-tracking
   - Match: 72% (similar capabilities)

3. neural-training-coordinator (platforms/neural/neural-training-coordinator.md)
   - Category: platforms
   - Capabilities: distributed-training, multi-gpu, training-orchestration
   - Match: 65% (training focus)

Registry: claude-code-plugins/ruv-sparc-three-loop-system/agents/
Browse all agents: agents/README.md
```

### Capability Mismatch
```
ERROR: Agent 'frontend-dev' missing required capabilities

Required by skill:
- api-design ❌
- authentication ❌
- database-integration ❌

Agent has:
- ui-components ✅
- react-development ✅
- accessibility ✅

Match score: 32% (below threshold of 80%)

Suggested agents with required capabilities:
1. backend-dev (95% match)
2. golang-backend-specialist (88% match)
3. rust-systems-developer (82% match)
```

### MCP Server Missing
```
WARNING: Agent 'automl-optimizer' requires MCP servers that are not enabled

Required MCPs (missing):
- flow-nexus (for cloud neural training)

Optional MCPs (missing):
- ruv-swarm (for distributed coordination)

Enable required MCPs:
  claude mcp add flow-nexus npx flow-nexus@latest mcp start

Continue anyway? (not recommended) [y/N]
```

## Integration with Existing Skills

### Before (Direct Task() - Risky)
```javascript
// In any skill.md or orchestrator
Task("backend-developer", "Build API", "...")  // No validation
Task("ml-trainer", "Train model", "...")       // Invalid agent
Task("devops-guy", "Deploy app", "...")        // Typo
```

### After (Safe Task Spawn - Validated)
```javascript
// Import safe-task-spawn
Skill("safe-task-spawn")

// Validated spawns
safe_task_spawn("backend-dev", "Build API", "...", {
  required_capabilities: ["api-design"],
  category: "delivery"
})

safe_task_spawn("automl-optimizer", "Train model", "...", {
  mcp_servers: { required: ["flow-nexus"] }
})

safe_task_spawn("cicd-engineer", "Deploy app", "...", {
  category: "operations"
})
```

## Memory MCP Schema

All spawn attempts are logged to Memory MCP with this schema:

```javascript
{
  "namespace": "orchestration/safe-task-spawn/{project_id}/{timestamp}",
  "key": "{agent_type}-{uuid}",
  "value": {
    "agent_type": "backend-dev",
    "description": "Build REST API with authentication",
    "status": "success" | "error",
    "validation_results": {
      "registry_found": true,
      "capabilities_match": true,
      "category_match": true,
      "phase_match": true,
      "tools_match": true,
      "mcp_servers_match": true,
      "match_score": 95
    },
    "agent_metadata": {
      "category": "delivery",
      "capabilities": ["api-design", "authentication", "database-integration"],
      "phase": "development",
      "file_path": "delivery/development/backend/dev-backend-api.md",
      "mcp_servers": {
        "required": ["memory-mcp"],
        "optional": []
      }
    },
    "suggestions": [],  // Empty on success, populated on error
    "error": null,      // Null on success, error details on failure
    "spawned_at": "2025-12-17T10:30:00.000Z",
    "skill_context": {...}
  },
  "tags": {
    "who": "safe-task-spawn",
    "when": "2025-12-17T10:30:00.000Z",
    "project": "api-development",
    "why": "task-spawning",
    "status": "success"
  },
  "ttl": 2592000  // 30 days
}
```

## Success Metrics

Safe Task Spawn succeeds when:
- ✅ Agent registry loaded and indexed successfully (211 agents)
- ✅ Agent type validated against registry (exact or fuzzy match)
- ✅ Capability requirements matched (if skill_context provided)
- ✅ MCP server requirements checked (warn if missing)
- ✅ Task spawned successfully (valid Task() call)
- ✅ Audit log written to Memory MCP with all metadata
- ✅ On error: Actionable suggestions provided from registry

Failure modes:
- ❌ Agent type not found and no close matches (< 50% similarity)
- ❌ Capability mismatch score below threshold (< 80%)
- ❌ Required MCP servers missing and user declines to continue
- ❌ Registry unavailable (fallback: warn and spawn anyway)

## Performance Considerations

### Caching Strategy
```javascript
// Registry is cached in memory after first load
let registry_cache = null;
let cache_timestamp = null;
const CACHE_TTL = 300000; // 5 minutes

function load_registry() {
  const now = Date.now();
  if (registry_cache && (now - cache_timestamp) < CACHE_TTL) {
    return registry_cache;  // Return cached
  }

  // Reload registry
  registry_cache = parse_agent_registry();
  cache_timestamp = now;
  return registry_cache;
}
```

### Batch Validation
```javascript
// Validate multiple spawns before executing
const spawns = [
  { agent_type: "backend-dev", description: "...", prompt: "..." },
  { agent_type: "frontend-dev", description: "...", prompt: "..." },
  { agent_type: "tester", description: "...", prompt: "..." }
];

const validations = safe_task_spawn_batch(spawns);
if (validations.every(v => v.status === "success")) {
  // All valid, spawn in parallel
  spawns.forEach(s => Task(s.agent_type, s.description, s.prompt));
} else {
  // Handle invalid spawns
  validations.filter(v => v.status === "error").forEach(error => {
    console.error(error.message);
    console.log(error.suggestions);
  });
}
```

## Related Skills

- **swarm-orchestration**: Multi-agent coordination with safe spawning
- **cascade-orchestrator**: Workflow cascades with validated agent selection
- **hive-mind-advanced**: Collective intelligence with registry-backed agents
- **agent-selector**: Intelligent agent selection from registry (211 agents)
- **agent-creation/agent-creator**: Create new agents for registry

## Configuration

### Environment Variables
```bash
# Registry location (default: claude-code-plugins/ruv-sparc-three-loop-system/agents/)
SAFE_TASK_SPAWN_REGISTRY_PATH=/custom/path/to/agents

# Validation strictness (strict|lenient|off)
SAFE_TASK_SPAWN_VALIDATION_MODE=strict

# Match threshold (0-100, default: 80)
SAFE_TASK_SPAWN_MATCH_THRESHOLD=80

# Cache TTL in milliseconds (default: 300000 = 5 minutes)
SAFE_TASK_SPAWN_CACHE_TTL=300000

# Audit logging (on|off, default: on)
SAFE_TASK_SPAWN_AUDIT_LOGGING=on

# Memory MCP namespace prefix
SAFE_TASK_SPAWN_NAMESPACE_PREFIX=orchestration/safe-task-spawn
```

### Settings.json Integration
```json
{
  "skills": {
    "safe-task-spawn": {
      "validation_mode": "strict",
      "match_threshold": 80,
      "cache_ttl": 300000,
      "audit_logging": true,
      "fallback_agents": ["coder", "researcher", "tester", "reviewer"],
      "auto_enable_mcp_servers": true
    }
  }
}
```

## Conclusion

Safe Task Spawn transforms agent spawning from a risky operation with silent failures into a validated, audited, and safe process. By enforcing registry compliance, matching agent capabilities to skill requirements, and logging all attempts to Memory MCP, it provides:

1. **Safety**: Invalid spawns fail fast with actionable guidance
2. **Auditability**: Complete trail of all spawn attempts
3. **Intelligence**: Fuzzy matching and suggestions from 211-agent registry
4. **Compatibility**: Validates agent capabilities match skill needs
5. **Observability**: Memory MCP integration for pattern analysis

Every skill that spawns agents should use Safe Task Spawn to prevent invalid spawns and build audit trails for debugging and compliance.

**Status**: Production-Ready (Gold Tier)
**Category**: Orchestration
**Documentation**: Complete with validation logic, audit schema, and integration examples

---

**Maintained by**: Claude Code (Sonnet 4.5)
**Registry Source**: claude-code-plugins/ruv-sparc-three-loop-system/agents/ (211 agents)
**Version**: 1.0.0
**Last Updated**: 2025-12-17