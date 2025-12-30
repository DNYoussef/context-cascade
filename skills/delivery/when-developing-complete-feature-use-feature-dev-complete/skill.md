/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: skill
version: 1.0.0
description: |
  [assert|neutral] skill skill for delivery workflows [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute skill workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "skill",
  category: "delivery",
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
  keywords: ["skill", "delivery", "workflow"],
  context: "user needs skill capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# When Developing Complete Feature Use Feature Dev Complete

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



---
name: when-developing-complete-feature-use-feature-dev-complete
trigger: "when user requests complete feature development from research to deployment"
description: "Comprehensive end-to-end feature development using multi-agent coordination with research, architecture, implementation, testing, and documentation phases"
version: 2.0.0
author: Base Template Generator
category: development
tags:
  - feature-development
  - multi-agent
  - end-to-end
  - tdd
  - documentation
agents:
  - researcher
  - system-architect
  - coder
  - tester
  - reviewer
  - api-docs
  - cicd-engineer
coordinator: hierarchical-coordinator
memory_patterns:
  - swarm/feature-dev/requirements
  - swarm/feature-dev/architecture
  - swarm/feature-dev/implementation
  - swarm/feature-dev/test-results
  - swarm/feature-dev/review-findings
success_criteria:
  - All requirements captured and validated
  - Architecture design approved
  - Code implementation complete with 90%+ coverage
  - All tests passing
  - Documentation generated
  - Deployment pipeline configured
---

## Assigned Agents

### Primary Agent
- **researcher** - Best match for Phase 1 (requirements analysis). Handles feature requirement gathering, best practice research, constraint identification, and success criteria definition. Coordinates initial research phase and sets foundation for all downstream work.

### Secondary Agents
- **system-architect** - Phase 2: Architecture design and API contract definition
- **planner** - Phase 3: Implementation planning and task breakdown
- **coder** - Phase 4b: Feature implementation following TDD approach
- **tester** - Phase 4a: Test specification and validation (TDD first)
- **reviewer** - Phase 5: Code review, security scanning, and quality assurance
- **api-docs** - Phase 6: API documentation and user guide generation
- **cicd-engineer** - Phase 7: CI/CD pipeline configuration and deployment setup

### Fallback Agents
- **sparc-coord** - Alternative coordinator if hierarchical-coordinator unavailable
- **sparc-coder** - Alternative implementation if coder unavailable
- **production-validator** - Alternative validation if reviewer unavailable

### Coordination Pattern
**Pattern**: Hierarchical Multi-Phase Workflow (7 phases)
**Topology**: Hierarchical coordination with sequential phases and memory-based handoffs
**Memory Namespace**: `swarm/feature-dev/*` (requirements, architecture, planning, implementation, review, docs, deployment)

**Agent Collaboration**:
1. **Sequential Dependencies**: Each phase waits for previous phase completion via memory
2. **Parallel Execution**: Phase 4 has tester + coder working concurrently (TDD)
3. **Quality Gates**: Phase 5 review must approve before Phase 6/7 proceed
4. **Hooks Integration**: All agents use pre-task/post-task/notify hooks for coordination
5. **Session Management**: Complete workflow tracked with session-id for restore/export

**Utilization**: This is a high-coordination skill using 7 specialized agents across the complete development lifecycle. Demonstrates full SPARC methodology integration.

---

## Trigger Conditions

Use this skill when:
- User requests a new feature from conception to production
- Complete feature lifecycle needed (research → deploy)
- Multi-phase development with quality gates required
- Cross-functional coordination between multiple specialists
- Comprehensive documentation and testing needed
- Production-ready deployment required

## Skill Overview

This skill orchestrates a complete feature development lifecycle using a 12-stage workflow with specialized agents coordinating through hierarchical topology and shared memory patterns.

## 7-Phase Skill-Forge Methodology

### Phase 1: Intent Analysis

**Objective**: Understand feature requirements and establish development goals

**Agent**: `researcher`

**Activities**:
- Analyze us

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
  pattern: "skills/delivery/skill/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "skill-{session_id}",
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

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
