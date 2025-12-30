/*============================================================================*/
/* SOP-API-DEVELOPMENT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: sop-api-development
version: 1.0.0
description: |
  [assert|neutral] Complete REST API development workflow coordinating backend, database, testing, documentation, and DevOps agents. 2-week timeline with TDD approach. [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- delivery
- development
- workflow
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute sop-api-development workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "sop-api-development",
  category: "delivery",
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
  keywords: ["sop-api-development", "delivery", "workflow"],
  context: "user needs sop-api-development capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# SOP: REST API Development

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.




## When to Use This Skill

- **Domain-Specific Work**: Tasks requiring specialized domain knowledge
- **Complex Problems**: Multi-faceted challenges needing systematic approach
- **Best Practice Implementation**: Following industry-standard methodologies
- **Quality-Critical Work**: Production code requiring high standards
- **Team Collaboration**: Coordinated work following shared processes

## When NOT to Use This Skill

- **Outside Domain**: Tasks outside this skill specialty area
- **Incompatible Tech Stack**: Technologies not covered by this skill
- **Simple Tasks**: Trivial work not requiring specialized knowledge
- **Exploratory Work**: Experimental code without production requirements

## Success Criteria

- [ ] Implementation complete and functional
- [ ] Tests passing with adequate coverage
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Performance benchmarks met
- [ ] Security considerations addressed
- [ ] Deployed or integrated successfully

## Edge Cases to Handle

- **Legacy Integration**: Working with older codebases or deprecated APIs
- **Missing Dependencies**: Unavailable libraries or external services
- **Version Conflicts**: Dependency version incompatibilities
- **Data Issues**: Malformed input or edge case data
- **Concurrency**: Race conditions or synchronization challenges
- **Error Handling**: Graceful degradation and recovery

## Guardrails

- **NEVER** skip testing to ship faster
- **ALWAYS** follow domain-specific best practices
- **NEVER** commit untested or broken code
- **ALWAYS** document complex logic and decisions
- **NEVER** hardcode sensitive data or credentials
- **ALWAYS** validate input and handle errors gracefully
- **NEVER** deploy without reviewing changes

## Evidence-Based Validation

- [ ] Automated tests passing
- [ ] Code linter/formatter passing
- [ ] Security scan completed
- [ ] Performance within acceptable range
- [ ] Manual testing completed
- [ ] Peer review approved
- [ ] Documentation reviewed

Complete REST API development using Test-Driven Development and multi-agent coordination.

## Timeline: 2 Weeks

**Phases**:
1. Planning & Design (Days 1-2)
2. Development (Days 3-8)
3. Testing & Documentation (Days 9-11)
4. Deployment (Days 12-14)

---

## Phase 1: Planning & Design (Days 1-2)

### Day 1: Requirements & Architecture

**Sequential Workflow**:

```javascript
// Step 1: Gather Requirements
await Task("Product Manager", `
Define API requirements:
- List all endpoints needed
- Define data models and relationships
- Specify authentication/authorization
- Define rate limiting and quotas
- Identify third-party integrations

Store requirements: api-dev/rest-api-v2/requirements
`, "planner");

// Step 2: API Design
await Task("System Architect", `
Using requirements: api-dev/rest-api-v2/requirements

Design:
- RESTful API structure (resources, HTTP methods)
- URL patterns and versioning strategy
- Request/response formats (JSON schemas)
- Error handling patterns
- API security architecture

Generate OpenAPI 3.0 specification
Store: api-dev/rest-api-v2/openapi-spec
`, "system-architect");

// Step 3: Database Design
await Task("Database Architect", `
Using API spec: api-dev/rest-api-v2/openapi-spec

Design database:
- Schema design (tables, columns, types)
- Relationships and foreign keys
- Indexes for performance
- Migration strategy
- Backup and recovery plan

Generate SQL schema
Store: api-dev/rest-api-v2/db-schema
`, "code-analyzer");
```

### Day 2: Test Planning

```javascript
// Step 4: Test Strategy
await Task("QA Engineer", `
Using:
- API spec: api-dev/rest-api-v2/openapi-spec
- DB schema: api-dev/rest-api-v2/db-schema

Create test plan:
- Unit test strategy (per endpoint)
- Integration test scenarios
- E2E test workflows
- Performance test targets
- Security test cases

Store test plan: api-dev/rest-api-v2/test-plan
`, "tester");

// 

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
  pattern: "skills/delivery/sop-api-development/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "sop-api-development-{session_id}",
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

[commit|confident] <promise>SOP_API_DEVELOPMENT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
