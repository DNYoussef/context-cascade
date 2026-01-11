/*============================================================================*/
/* WHEN-CHAINING-WORKFLOWS-USE-CASCADE-ORCHESTRATOR SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-chaining-workflows-use-cascade-orchestrator
version: 1.0.0
description: |
  [assert|neutral] Create sophisticated workflow cascades with sequential pipelines, parallel execution, and conditional branching [ground:given] [conf:0.95] [state:confirmed]
category: coordination
tags:
- cascade
- workflows
- orchestration
- conditional
- branching
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute when-chaining-workflows-use-cascade-orchestrator workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic coordination processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-chaining-workflows-use-cascade-orchestrator",
  category: "coordination",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["when-chaining-workflows-use-cascade-orchestrator", "coordination", "workflow"],
  context: "user needs when-chaining-workflows-use-cascade-orchestrator capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Cascade Orchestrator SOP

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Create sophisticated workflow cascades that chain multiple workflows together with sequential pipelines, parallel execution, conditional branching, and error handling.

## Agents & Responsibilities

### task-orchestrator
**Role:** Orchestrate workflow execution
**Responsibilities:**
- Coordinate workflow execution
- Handle workflow transitions
- Manage workflow state
- Monitor progress

### hierarchical-coordinator
**Role:** Manage workflow hierarchy
**Responsibilities:**
- Organize workflow levels
- Handle parent-child workflows
- Manage dependencies
- Ensure proper ordering

### memory-coordinator
**Role:** Manage workflow state and data flow
**Responsibilities:**
- Store workflow state
- Pass data between workflows
- Maintain execution history
- Ensure data consistency

## Phase 1: Design Cascade

### Objective
Design cascade structure with workflows, dependencies, and branching logic.

### Scripts

```bash
# Create cascade definition
cat > cascade-definition.yaml <<EOF
name: full-stack-development
workflows:
  - id: design
    type: sequential
    steps: [requirements, architecture, database-design]
  - id: backend
    type: parallel
    steps: [api-impl, auth-impl, db-impl]
    depends_on: [design]
  - id: frontend
    type: sequential
    steps: [ui-impl, integration]
    depends_on: [backend]
  - id: testing
    type: parallel
    steps: [unit-tests, integration-tests, e2e-tests]
    depends_on: [backend, frontend]
  - id: deployment
    type: conditional
    condition: "testing.success_rate > 0.95"
    steps: [build, deploy, verify]
    depends_on: [testing]
EOF

# Validate cascade
npx claude-flow@alpha cascade validate --definition cascade-definition.yaml

# Visualize cascade
npx claude-flow@alpha cascade visualize \
  --definition cascade-definition.yaml \
  --output cascade-diagram.png

# Store cascade definition
npx claude-flow@alpha memory store \
  --key "cascade/definition" \
  --file cascade-definition.yaml
```

### Cascade Patterns

**Sequential Cascade:**
```
Workflow A → Workflow B → Workflow C
```

**Parallel Cascade:**
```
         ┌─ Workflow B ─┐
Workflow A ├─ Workflow C ─┤ Workflow E
         └─ Workflow D ─┘
```

**Conditional Cascade:**
```
Workflow A → Decision → [if true] Workflow B
                      → [if false] Workflow C
```

**Hybrid Cascade:**
```
Design → ┬─ Backend ─┐
         └─ Frontend─┴─ [if tests pass] → Deploy
```

## Phase 2: Chain Workflows

### Objective
Connect workflows with proper data flow and dependency management.

### Scripts

```bash
# Initialize cascade
npx claude-flow@alpha cascade init \
  --definition cascade-definition.yaml

# Connect workflow stages
npx claude-flow@alpha cascade connect \
  --from design \
  --to backend \
  --data-flow "architecture-docs"

npx claude-flow@alpha cascade connect \
  --from design \
  --to frontend \
  --data-flow "ui-specs"

npx claude-flow@alpha cascade connect \
  --from backend \
  --to testing \
  --data-flow "api-endpoints"

# Setup conditional branching
npx claude-flow@alpha cascade branch \
  --workflow testing \
  --condition "success_rate > 0.95" \
  --true-path deployment \
  --false-path debugging

# Verify connections
npx claude-flow@alpha cascade status --show-connections
```

### Data Flow Configuration

```bash
# Configure data passing
npx claude-flow@alpha cascade data-flow \
  --from "design.architecture" \
  --to "backend.api-spec" \
  --transform "extract-api-endpoints"

# Setup shared state
npx claude-flow@alpha memory store \
  --key "cascade/shared-state" \
  --value '{
    "project": "full-stack-app",
    "version": "1.0.0",
    "environment": "production"
  }'
```

## Phase 3: Execute Cascade

### Objective
Execute cascading workflows with proper sequencing and error handling.

### Scripts

```bash
# Execute cascade
npx claude-flow@alpha cascade execute \
  --definition cascade-definition.

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/coordination/when-chaining-workflows-use-cascade-orchestrator/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-chaining-workflows-use-cascade-orchestrator-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>WHEN_CHAINING_WORKFLOWS_USE_CASCADE_ORCHESTRATOR_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
