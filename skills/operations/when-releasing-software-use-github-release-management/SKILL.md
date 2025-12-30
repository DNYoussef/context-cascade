/*============================================================================*/
/* WHEN-RELEASING-SOFTWARE-USE-GITHUB-RELEASE-MANAGEMENT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-releasing-software-use-github-release-management
version: 1.0.0
description: |
  [assert|neutral] Comprehensive GitHub release orchestration with AI swarm coordination for automated versioning, testing, deployment, and rollback management. Coordinates release-manager, cicd-engineer, tester, and do [ground:given] [conf:0.95] [state:confirmed]
category: operations
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-releasing-software-use-github-release-management workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic operations processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-releasing-software-use-github-release-management",
  category: "operations",
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
  keywords: ["when-releasing-software-use-github-release-management", "operations", "workflow"],
  context: "user needs when-releasing-software-use-github-release-management capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# GitHub Release Management Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Orchestrate end-to-end software release processes with intelligent agent coordination. This skill automates version bumping, changelog generation, release candidate testing, deployment orchestration, post-release validation, and rollback procedures for GitHub-hosted projects using comprehensive CI/CD integration.

## When to Use This Skill

Activate this skill when creating production releases with automated validation, coordinating multi-environment deployments (staging, production), generating release notes and changelogs automatically, managing semantic versioning across projects, implementing deployment strategies (rolling, blue-green, canary), handling hotfix releases and emergency patches, or establishing release automation for new projects.

Use for both small single-repository releases and complex multi-service deployments, scheduled regular releases or on-demand deployments, and establishing release governance and compliance.

## Agent Coordination Architecture

### Swarm Topology

Initialize a **hierarchical topology** with release-manager as coordinator overseeing specialized deployment, testing, and documentation agents. Hierarchical structure ensures coordinated decision-making for critical release operations.

```bash
# Initialize hierarchical swarm for release management
npx claude-flow@alpha swarm init --topology hierarchical --max-agents 8 --strategy specialized
```

### Specialized Agent Roles

**Release Manager** (`release-manager`): Top-level coordinator that oversees entire release process. Makes go/no-go decisions, coordinates deployment timing, manages rollback decisions, and ensures release quality standards. Acts as release captain.

**CI/CD Engineer** (`cicd-engineer`): Manages build pipelines, deployment automation, infrastructure provisioning, and deployment strategy execution. Handles technical deployment mechanics and environment configuration.

**Test Engineer** (`tester`): Validates release candidates through automated testing, regression testing, performance testing, and smoke testing. Verifies deployment success and monitors post-deployment health.

**Code Reviewer** (`reviewer`): Performs final code review of release branch, validates security compliance, checks for last-minute issues, and approves release artifacts.

**Documentation Writer** (`docs-writer`): Generates release notes, updates changelogs, creates deployment runbooks, and documents breaking changes. Ensures comprehensive release documentation.

## Release Management Workflows (SOP)

### Workflow 1: Standard Release (Major/Minor/Patch)

Execute full release cycle from version bump to production deployment.

**Phase 1: Pre-Release Preparation**

**Step 1.1: Initialize Release Swarm**

```bash
# Set up hierarchical release swarm
mcp__claude-flow__swarm_init topology=hierarchical maxAgents=8 strategy=specialized

# Spawn release team
mcp__claude-flow__agent_spawn type=coordinator name=release-manager
mcp__claude-flow__agent_spawn type=coder name=cicd-engineer
mcp__claude-flow__agent_spawn type=researcher name=tester
mcp__claude-flow__agent_spawn type=analyst name=reviewer
mcp__claude-flow__agent_spawn type=researcher name=docs-writer
```

**Step 1.2: Determine Release Version**

```plaintext
Task("Release Manager", "
  Determine next release version:

  1. Fetch current version from package.json / Cargo.toml / VERSION file
  2. Analyze commits since last release using git log
  3. Classify changes: breaking|features|fixes|docs
  4. Apply semantic versioning rules:
     - Breaking changes → major version bump
     - New features → minor version bump
     - Bug fixes only → patch version bump
  5. Check for forced version override in environment

  Use scripts/semver.sh for version calculation
  Store version decision in memory: release/version
  Run hooks: npx claude-flow@alpha hooks pre-task --description

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
  pattern: "skills/operations/when-releasing-software-use-github-release-management/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-releasing-software-use-github-release-management-{session_id}",
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

[commit|confident] <promise>WHEN_RELEASING_SOFTWARE_USE_GITHUB_RELEASE_MANAGEMENT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
