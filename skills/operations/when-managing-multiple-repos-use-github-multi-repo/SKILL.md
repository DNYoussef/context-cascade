/*============================================================================*/
/* WHEN-MANAGING-MULTIPLE-REPOS-USE-GITHUB-MULTI-REPO SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-managing-multiple-repos-use-github-multi-repo
version: 1.0.0
description: |
  [assert|neutral] Multi-repository coordination, synchronization, and architecture management with AI swarm orchestration. Coordinates repo-architect, code-analyzer, and coordinator agents across multiple repositories  [ground:given] [conf:0.95] [state:confirmed]
category: operations
tags:
- general
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute when-managing-multiple-repos-use-github-multi-repo workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic operations processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-managing-multiple-repos-use-github-multi-repo",
  category: "operations",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Compositional",
  source: "German",
  force: "Build from primitives?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["when-managing-multiple-repos-use-github-multi-repo", "operations", "workflow"],
  context: "user needs when-managing-multiple-repos-use-github-multi-repo capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# GitHub Multi-Repository Management Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Orchestrate complex operations across multiple related GitHub repositories with intelligent agent coordination. This skill enables consistent architecture enforcement, synchronized dependency updates, cross-repo refactoring, and coordinated releases for microservices, multi-package ecosystems, and distributed system architectures.

## When to Use This Skill

Activate this skill when managing microservices architectures spanning multiple repositories, coordinating changes across frontend/backend/infrastructure repos, migrating from monorepo to multi-repo structure, propagating breaking changes across dependent repositories, maintaining consistent coding standards across teams, synchronizing releases for multi-package systems, or enforcing architectural patterns across an organization.

Use for both small-scale coordination (2-5 repos) and large-scale orchestration (10+ repositories), one-time migrations or ongoing maintenance, and establishing governance for multi-repo ecosystems.

## Agent Coordination Architecture

### Swarm Topology

Initialize a **hierarchical topology** with a coordinator agent managing specialized worker agents. Hierarchical structure enables centralized decision-making for consistency while delegating specialized tasks to expert agents.

```bash
# Initialize hierarchical swarm for multi-repo coordination
npx claude-flow@alpha swarm init --topology hierarchical --max-agents 8 --strategy adaptive
```

### Specialized Agent Roles

**Hierarchical Coordinator** (`hierarchical-coordinator`): Top-level orchestrator that maintains global view of all repositories, makes architectural decisions, coordinates cross-repo operations, and ensures consistency. Acts as the single source of truth for multi-repo strategy.

**Repository Architect** (`repo-architect`): Analyzes repository structures, defines architectural patterns, creates dependency graphs, identifies coupling issues, and designs migration strategies. Maintains the architectural vision across repositories.

**Code Analyzer** (`code-analyzer`): Scans codebases for patterns, dependencies, and inconsistencies. Identifies code duplication across repos, tracks API contracts, and validates architectural compliance.

**CI/CD Engineer** (`cicd-engineer`): Manages build pipelines, deployment workflows, and release orchestration. Coordinates continuous integration across repositories and handles versioning strategies.

**Worker Agents** (spawned dynamically): Execute repository-specific tasks such as refactoring, testing, documentation updates, and dependency bumps. Scaled based on number of target repositories.

## Multi-Repository Workflows (SOP)

### Workflow 1: Cross-Repository Change Propagation

Propagate breaking changes, API updates, or architectural patterns across multiple repositories.

**Phase 1: Impact Analysis**

**Step 1.1: Initialize Hierarchical Coordination**

```bash
# Set up hierarchical swarm
mcp__claude-flow__swarm_init topology=hierarchical maxAgents=8 strategy=adaptive

# Spawn coordinator and specialists
mcp__claude-flow__agent_spawn type=coordinator name=hierarchical-coordinator
mcp__claude-flow__agent_spawn type=analyst name=repo-architect
mcp__claude-flow__agent_spawn type=analyst name=code-analyzer
mcp__claude-flow__agent_spawn type=coder name=cicd-engineer
```

**Step 1.2: Analyze Repository Dependencies**

Use `scripts/repo-graph.sh` to build dependency graph:

```bash
# Generate dependency graph across all repositories
bash scripts/repo-graph.sh build-graph \
  --repos "repo1,repo2,repo3" \
  --output "references/dependency-graph.dot"
```

Visualize the dependency graph to identify impact scope:

```bash
# Render graph visualization
dot -Tpng references/dependency-graph.dot -o dependency-graph.png
```

**Step 1.3: Identify Affected Repositories**

Launch coordinator to analyze impact:

```plaintext


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
  pattern: "skills/operations/when-managing-multiple-repos-use-github-multi-repo/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-managing-multiple-repos-use-github-multi-repo-{session_id}",
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

[commit|confident] <promise>WHEN_MANAGING_MULTIPLE_REPOS_USE_GITHUB_MULTI_REPO_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
