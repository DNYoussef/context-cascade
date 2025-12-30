/*============================================================================*/
/* WHEN-BUILDING-BACKEND-API-ORCHESTRATE-API-DEVELOPMENT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-building-backend-api-orchestrate-api-development
version: 1.0.0
description: |
  [assert|neutral] Use when building a production-ready REST API from requirements through deployment. Orchestrates 8-12 specialist agents across 5 phases using Test-Driven Development methodology. Covers planning, arch [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-building-backend-api-orchestrate-api-development workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-building-backend-api-orchestrate-api-development",
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
  keywords: ["when-building-backend-api-orchestrate-api-development", "orchestration", "workflow"],
  context: "user needs when-building-backend-api-orchestrate-api-development capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# API Development Orchestration Workflow

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Complete REST API development workflow using Test-Driven Development and multi-agent coordination. Orchestrates 8-12 specialist agents across planning, architecture design, TDD implementation, testing, documentation, and production deployment in a systematic 2-week process.

## Overview

This SOP implements a comprehensive API development workflow emphasizing quality through Test-Driven Development (TDD). The workflow balances speed with thoroughness, using hierarchical coordination for planning phases and parallel execution for development and testing. Each phase produces validated deliverables that subsequent phases consume, ensuring continuity and traceability.

The TDD approach ensures high test coverage (>90%), reduces bugs, and produces well-designed, maintainable code. Parallel execution of specialized reviews accelerates quality validation while maintaining comprehensive coverage of security, performance, and architectural concerns.

## MCP Requirements

This skill operates using Claude Code's built-in tools only. No additional MCP servers required.

This orchestration workflow uses native Claude Flow commands (swarm init, agent spawn, task orchestrate, hooks, memory) which are all part of the core system. No external MCPs needed for API development coordination.

## Trigger Conditions

Use this workflow when:
- Building a new REST API or microservice from scratch
- Migrating existing API to modern architecture with comprehensive testing
- Need systematic TDD approach with documented test coverage
- Require production-ready API with security, performance, and scalability validation
- Timeline is 2-4 weeks with clear milestones and deliverables
- Quality gates (testing, security, performance) are non-negotiable
- Need comprehensive API documentation and operational runbooks

## Orchestrated Agents (12 Total)

### Planning & Architecture Agents
- **`product-manager`** - Requirements gathering, endpoint definition, API contracts, success criteria
- **`system-architect`** - API architecture design, RESTful patterns, versioning, error handling strategy
- **`database-architect`** - Schema design, query optimization, indexing, migration planning
- **`qa-engineer`** - Test planning, TDD strategy, coverage targets, performance benchmarks

### Development Agents (TDD Cycle)
- **`tester`** - Write tests first (red phase), integration tests, E2E scenarios
- **`backend-developer`** - Implement to pass tests (green phase), refactor for quality
- **`code-reviewer`** - Code quality review, refactoring suggestions, best practices validation

### Quality & Validation Agents
- **`security-specialist`** - Security architecture, OWASP validation, penetration testing
- **`performance-analyst`** - Load testing, stress testing, bottleneck identification, optimization
- **`api-documentation-specialist`** - OpenAPI specs, developer guides, code examples

### Deployment & Operations Agents
- **`devops-engineer`** - CI/CD pipeline, Docker/K8s deployment, infrastructure as code
- **`production-validator`** - Pre-production validation, go/no-go decision, smoke testing
- **`performance-monitor`** - Production monitoring, logging, alerting, SLO tracking

## Workflow Phases

### Phase 1: Planning & Design (Days 1-2, Sequential)

**Duration**: 2 days
**Execution Mode**: Sequential analysis and design
**Agents**: `product-manager`, `system-architect`, `database-architect`, `qa-engineer`

**Process**:

1. **Gather API Requirements** (Day 1 Morning)
   ```bash
   npx claude-flow hooks pre-task --description "API Development: ${API_NAME}"
   npx claude-flow swarm init --topology hierarchical --max-agents 12 --strategy specialized
   npx claude-flow agent spawn --type planner
   ```

   **Product Manager** defines:
   - Complete endpoint list with HTTP methods (GET, POST, PUT, DELETE, PATCH)
   - Data models and relationships (entities

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
  pattern: "skills/orchestration/when-building-backend-api-orchestrate-api-development/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-building-backend-api-orchestrate-api-development-{session_id}",
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

[commit|confident] <promise>WHEN_BUILDING_BACKEND_API_ORCHESTRATE_API_DEVELOPMENT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
