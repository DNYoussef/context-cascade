/*============================================================================*/
/* WHEN-AUTOMATING-GITHUB-ACTIONS-USE-WORKFLOW-AUTOMATION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-automating-github-actions-use-workflow-automation
version: 1.0.0
description: |
  [assert|neutral] Advanced GitHub Actions workflow automation with AI swarm coordination, intelligent CI/CD pipelines, and comprehensive repository management. Coordinates cicd-engineer, workflow-automation, tester, an [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-automating-github-actions-use-workflow-automation workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-automating-github-actions-use-workflow-automation",
  category: "orchestration",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["when-automating-github-actions-use-workflow-automation", "orchestration", "workflow"],
  context: "user needs when-automating-github-actions-use-workflow-automation capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# GitHub Actions Workflow Automation Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Design, implement, and optimize GitHub Actions CI/CD workflows using intelligent agent coordination. This skill provides end-to-end workflow automation including pipeline generation, security hardening, performance optimization, test orchestration, and debugging for robust continuous integration and deployment.

## When to Use This Skill

Activate this skill when creating new CI/CD pipelines from scratch, optimizing slow or inefficient workflows, implementing matrix testing strategies, hardening workflow security and secrets management, debugging failing workflows or flaky tests, establishing organizational workflow standards, or migrating from other CI systems (Jenkins, Travis, CircleCI) to GitHub Actions.

Use for both simple single-job workflows and complex multi-stage pipelines, monorepo workflows with selective job triggering, scheduled workflows and cron jobs, or workflow templates for organization-wide reuse.

## Agent Coordination Architecture

### Swarm Topology

Initialize a **mesh topology** enabling parallel workflow development with peer-to-peer coordination between specialized agents. Mesh topology allows security, testing, and performance agents to collaborate directly.

```bash
# Initialize mesh swarm for workflow automation
npx claude-flow@alpha swarm init --topology mesh --max-agents 6 --strategy balanced
```

### Specialized Agent Roles

**CI/CD Engineer** (`cicd-engineer`): Primary workflow architect that designs pipeline structure, selects appropriate actions, configures jobs and steps, and implements deployment strategies. Owns overall workflow design.

**Workflow Automation** (`workflow-automation`): Specializes in GitHub Actions-specific optimizations including caching strategies, artifact management, workflow reuse, and matrix configurations. Expert in GitHub Actions ecosystem.

**Test Engineer** (`tester`): Designs test orchestration strategies including parallel testing, matrix testing, test reporting, and failure analysis. Ensures comprehensive test coverage in CI/CD.

**Security Auditor** (`security-auditor`): Hardens workflows against security vulnerabilities including secrets management, third-party action vetting, permission scoping, and supply chain security.

**Performance Analyzer** (`perf-analyzer`): Optimizes workflow execution time through parallelization, caching, selective job triggering, and resource optimization. Monitors workflow performance metrics.

## Workflow Automation Processes (SOP)

### Workflow 1: Generate CI/CD Pipeline from Scratch

Create comprehensive CI/CD workflow for new or existing project.

**Phase 1: Requirements Analysis**

**Step 1.1: Initialize Mesh Swarm**

```bash
# Set up mesh swarm for collaborative workflow development
mcp__claude-flow__swarm_init topology=mesh maxAgents=6 strategy=balanced

# Spawn specialized agents
mcp__claude-flow__agent_spawn type=coder name=cicd-engineer
mcp__claude-flow__agent_spawn type=coordinator name=workflow-automation
mcp__claude-flow__agent_spawn type=researcher name=tester
mcp__claude-flow__agent_spawn type=analyst name=security-auditor
mcp__claude-flow__agent_spawn type=optimizer name=perf-analyzer
```

**Step 1.2: Analyze Project Structure**

```plaintext
Task("CI/CD Engineer", "
  Analyze project and determine CI/CD requirements:

  1. Detect project type (Node.js, Python, Rust, Go, Java, etc.)
  2. Identify build system (npm, cargo, maven, gradle, make)
  3. Discover test frameworks and test locations
  4. Check for linting and formatting tools
  5. Identify deployment targets (npm registry, Docker Hub, AWS, etc.)
  6. Review existing workflows if migrating from other CI

  Use scripts/project-analyzer.sh for detection
  Store project analysis in memory: github-actions/analysis
  Run hooks: npx claude-flow@alpha hooks pre-task --description 'project analysis'
", "cicd-engineer")
```

**

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
  pattern: "skills/orchestration/when-automating-github-actions-use-workflow-automation/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-automating-github-actions-use-workflow-automation-{session_id}",
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

[commit|confident] <promise>WHEN_AUTOMATING_GITHUB_ACTIONS_USE_WORKFLOW_AUTOMATION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
