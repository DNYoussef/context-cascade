/*============================================================================*/
/* FLOW-NEXUS-PLATFORM SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: flow-nexus-platform
version: 2.0.0
description: |
  [assert|neutral] Comprehensive Flow Nexus platform management - authentication, sandboxes, app deployment, payments, and challenges (Gold Tier) [ground:given] [conf:0.95] [state:confirmed]
category: platform
tags:
- authentication
- sandboxes
- deployment
- payments
- gamification
author: Flow Nexus
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute flow-nexus-platform workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic platform processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "flow-nexus-platform",
  category: "platform",
  version: "2.0.0",
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
  keywords: ["flow-nexus-platform", "platform", "workflow"],
  context: "user needs flow-nexus-platform capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## When NOT to Use This Skill

- Local development without cloud infrastructure needs
- Simple scripts that do not require sandboxed execution
- Operations without distributed computing requirements
- Tasks that can run on single-machine environments

## Success Criteria
- [assert|neutral] API response time: <200ms for sandbox creation [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Deployment success rate: >99% [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Sandbox startup time: <5s [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Network latency: <50ms between sandboxes [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Resource utilization: <80% CPU/memory per sandbox [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Uptime: >99.9% for production deployments [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Edge Cases & Error Handling

- **Rate Limits**: Flow Nexus API has request limits; implement queuing and backoff
- **Authentication Failures**: Validate API tokens before operations; refresh expired tokens
- **Network Issues**: Retry failed requests with exponential backoff (max 5 retries)
- **Quota Exhaustion**: Monitor sandbox/compute quotas; alert before limits
- **Sandbox Timeouts**: Set appropriate timeout values; clean up orphaned sandboxes
- **Deployment Failures**: Implement rollback strategies; maintain previous working state

## Guardrails & Safety
- [assert|emphatic] NEVER: expose API keys or authentication tokens in code or logs [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate responses from Flow Nexus API before processing [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: implement timeout limits for long-running operations [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: trust user input for sandbox commands without validation [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: monitor resource usage to prevent runaway processes [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: clean up sandboxes and resources after task completion [ground:policy] [conf:0.98] [state:confirmed]

## Evidence-Based Validation

- Verify platform health: Check Flow Nexus status endpoint before operations
- Validate deployments: Test sandbox connectivity and functionality
- Monitor costs: Track compute usage and spending against budgets
- Test failure scenarios: Simulate network failures, timeouts, auth errors
- Benchmark performance: Compare actual vs expected latency/throughput


# Flow Nexus Platform Management

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Gold Tier Skill**: Comprehensive platform management for Flow Nexus with 4 automation scripts, 3 configuration templates, and comprehensive test suites - covering authentication, sandbox execution, app deployment, credit management, and coding challenges.

## Quick Access

- **Scripts**: `resources/scripts/` - 4 platform automation tools
- **Templates**: `resources/templates/` - 3 configuration templates
- **Tests**: `tests/` - 3 comprehensive test suites
- **Process Diagram**: `flow-nexus-platform-process.dot` - Visual workflow

## Automation Scripts

This skill includes functional automation scripts for streamlined platform operations:

### 1. Authentication Manager (`auth-manager.js`)

Automate user authentication workflows:

```bash
# Register new user
node resources/scripts/auth-manager.js register user@example.com SecurePass123 "John Doe"

# Login
node resources/scripts/auth-manager.js login user@example.com SecurePass123

# Check authentication status
node resources/scripts/auth-manager.js status --detailed

# Update profile
node resources/scripts/auth-manager.js update-profile user123 bio="AI Developer" github_username=johndoe

# Upgrade ti

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
  pattern: "skills/platform/flow-nexus-platform/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "flow-nexus-platform-{session_id}",
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

[commit|confident] <promise>FLOW_NEXUS_PLATFORM_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
