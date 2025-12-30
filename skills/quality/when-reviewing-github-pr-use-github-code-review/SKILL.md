/*============================================================================*/
/* WHEN-REVIEWING-GITHUB-PR-USE-GITHUB-CODE-REVIEW SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-reviewing-github-pr-use-github-code-review
version: 1.0.0
description: |
  [assert|neutral] Comprehensive GitHub pull request code review using multi-agent swarm with specialized reviewers for security, performance, style, tests, and documentation. Coordinates security-auditor, perf-analyzer [ground:given] [conf:0.95] [state:confirmed]
category: quality
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-reviewing-github-pr-use-github-code-review workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic quality processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-reviewing-github-pr-use-github-code-review",
  category: "quality",
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
  keywords: ["when-reviewing-github-pr-use-github-code-review", "quality", "workflow"],
  context: "user needs when-reviewing-github-pr-use-github-code-review capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# GitHub Code Review Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Execute comprehensive, multi-dimensional code reviews for GitHub pull requests using coordinated agent swarms. This skill orchestrates five specialized agents working in parallel to analyze security, performance, code quality, test coverage, and documentation, then synthesizes findings into actionable feedback with merge readiness assessment.

## When to Use This Skill

Activate this skill when reviewing pull requests before merge approval, conducting security audits on code changes, assessing performance implications of new code, validating test coverage and quality standards, or providing structured feedback to contributors.

Use this skill for both internal team PRs and external contributor submissions, complex feature additions requiring thorough review, refactoring changes that impact system architecture, or establishing code review standards and automation.

## Agent Coordination Architecture

### Swarm Topology

Initialize a **mesh topology** for maximum parallel execution and peer-to-peer communication between specialized reviewers. Mesh topology enables each agent to share findings directly with others, creating a comprehensive understanding through collective intelligence.

```bash
# Initialize mesh swarm for PR review
npx claude-flow@alpha swarm init --topology mesh --max-agents 5 --strategy specialized
```

### Specialized Agent Roles

**Security Auditor** (`security-auditor`): Analyze code for security vulnerabilities, injection risks, authentication/authorization flaws, secrets exposure, and dependency vulnerabilities. Check for OWASP Top 10 violations and compliance requirements.

**Performance Analyzer** (`perf-analyzer`): Evaluate performance implications including algorithmic complexity, memory usage patterns, database query efficiency, caching opportunities, and potential bottlenecks. Flag resource-intensive operations.

**Code Analyzer** (`code-analyzer`): Assess code quality, maintainability, and adherence to style guidelines. Check naming conventions, code organization, design patterns, complexity metrics, and architectural consistency.

**Test Engineer** (`tester`): Review test coverage, test quality, and testing best practices. Validate unit tests, integration tests, edge case handling, and test maintainability. Identify gaps in coverage.

**Documentation Reviewer** (`reviewer`): Evaluate documentation quality including code comments, API documentation, README updates, and inline documentation. Ensure clarity and completeness for future maintainers.

## Review Workflow (SOP)

### Phase 1: Initialization and Context Loading

**Step 1.1: Initialize Swarm Coordination**

Set up mesh topology for parallel agent execution:

```bash
# Use MCP tools to initialize coordination
mcp__claude-flow__swarm_init topology=mesh maxAgents=5 strategy=specialized

# Spawn specialized agents
mcp__claude-flow__agent_spawn type=analyst name=security-auditor
mcp__claude-flow__agent_spawn type=optimizer name=perf-analyzer
mcp__claude-flow__agent_spawn type=analyst name=code-analyzer
mcp__claude-flow__agent_spawn type=researcher name=tester
mcp__claude-flow__agent_spawn type=researcher name=reviewer
```

**Step 1.2: Fetch PR Context**

Use the bundled `github-api.sh` script to fetch PR details:

```bash
# Fetch PR metadata, files changed, and existing comments
bash scripts/github-api.sh fetch-pr <owner> <repo> <pr-number>
```

Store PR context in memory for agent access:

```bash
# Save PR context for swarm coordination
npx claude-flow@alpha hooks post-edit \
  --file "pr-context.json" \
  --memory-key "github/pr-review/context"
```

**Step 1.3: Load Review Criteria**

Reference `references/review-criteria.md` for comprehensive standards. This document contains security checklists, performance benchmarks, code style guidelines, test coverage requirements, and documentation standards.

### Phase 2: Parallel A

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
  pattern: "skills/quality/when-reviewing-github-pr-use-github-code-review/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-reviewing-github-pr-use-github-code-review-{session_id}",
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

[commit|confident] <promise>WHEN_REVIEWING_GITHUB_PR_USE_GITHUB_CODE_REVIEW_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
