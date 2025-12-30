/*============================================================================*/
/* WHEN-MANAGING-GITHUB-PROJECTS-USE-GITHUB-PROJECT-MANAGEMENT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-managing-github-projects-use-github-project-management
version: 1.0.0
description: |
  [assert|neutral] Comprehensive GitHub project management with swarm-coordinated issue tracking, project board automation, and sprint planning. Coordinates planner, issue-tracker, and project-board-sync agents to autom [ground:given] [conf:0.95] [state:confirmed]
category: operations
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute when-managing-github-projects-use-github-project-management workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic operations processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-managing-github-projects-use-github-project-management",
  category: "operations",
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
  keywords: ["when-managing-github-projects-use-github-project-management", "operations", "workflow"],
  context: "user needs when-managing-github-projects-use-github-project-management capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# GitHub Project Management Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Automate and orchestrate GitHub project management workflows using intelligent agent coordination. This skill provides comprehensive project management capabilities including automated issue triage, sprint planning, milestone tracking, project board synchronization, and team coordination through GitHub Projects v2 integration.

## When to Use This Skill

Activate this skill when planning and executing development sprints, managing issue backlogs and triage queues, coordinating work across distributed teams, automating project board updates and status tracking, tracking milestones and release schedules, or establishing project management workflows for new teams.

Use for both small team projects (2-5 developers) and large-scale coordination (10+ team members), agile/scrum sprint management, kanban-style continuous delivery, or hybrid project management approaches.

## Agent Coordination Architecture

### Swarm Topology

Initialize a **star topology** with a central coordinator agent managing specialized agents for issue tracking, planning, and board synchronization. Star topology enables centralized control with efficient communication to specialized agents.

```bash
# Initialize star swarm for project management
npx claude-flow@alpha swarm init --topology star --max-agents 6 --strategy balanced
```

### Specialized Agent Roles

**Central Coordinator** (`coordinator`): Hub agent that orchestrates all project management activities. Makes prioritization decisions, coordinates between teams, and ensures consistency across project artifacts. Acts as project manager.

**Planner** (`planner`): Handles sprint planning, capacity estimation, and resource allocation. Creates sprint goals, breaks down epics into stories, estimates effort, and balances workload across team members.

**Issue Tracker** (`issue-tracker`): Automates issue triage, labeling, assignment, and lifecycle management. Monitors new issues, applies initial classification, routes to appropriate team members, and tracks resolution progress.

**Project Board Sync** (`project-board-sync`): Maintains GitHub Projects v2 boards, updates issue status, manages custom fields, and enforces workflow automation. Ensures boards accurately reflect current project state.

## Project Management Workflows (SOP)

### Workflow 1: Automated Issue Triage

Process incoming issues with intelligent classification and routing.

**Phase 1: Issue Ingestion**

**Step 1.1: Initialize Star Topology**

```bash
# Set up star swarm with coordinator hub
mcp__claude-flow__swarm_init topology=star maxAgents=6 strategy=balanced

# Spawn coordinator and specialists
mcp__claude-flow__agent_spawn type=coordinator name=coordinator
mcp__claude-flow__agent_spawn type=researcher name=issue-tracker
mcp__claude-flow__agent_spawn type=researcher name=planner
mcp__claude-flow__agent_spawn type=coordinator name=project-board-sync
```

**Step 1.2: Monitor New Issues**

Set up real-time monitoring for new issues:

```bash
# Subscribe to new issues
bash scripts/github-webhook.sh subscribe \
  --repo <owner/repo> \
  --events "issues" \
  --callback "scripts/process-new-issue.sh"
```

Or use MCP real-time subscription if Flow-Nexus available:

```bash
mcp__flow-nexus__realtime_subscribe table=issues event=INSERT
```

**Step 1.3: Fetch Issue Details**

When new issue created, fetch comprehensive context:

```bash
# Get issue details with comments and reactions
bash scripts/github-api.sh fetch-issue \
  --repo <owner/repo> \
  --issue <number> \
  --include-comments true
```

**Phase 2: Intelligent Classification**

**Step 2.1: Analyze Issue Content**

```plaintext
Task("Issue Tracker", "
  Analyze and classify new issue #<NUMBER>:

  1. Read issue body and comments from memory: github/issues/<NUMBER>
  2. Classify issue type: bug|feature|enhancement|documentation|question
  3. Determine severity:

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
  pattern: "skills/operations/when-managing-github-projects-use-github-project-management/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-managing-github-projects-use-github-project-management-{session_id}",
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

[commit|confident] <promise>WHEN_MANAGING_GITHUB_PROJECTS_USE_GITHUB_PROJECT_MANAGEMENT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
