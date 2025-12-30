/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for platforms workflows [ground:given] [conf:0.95] [state:confirmed]
category: platforms
tags:
- general
author: system
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic platforms processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "platforms",
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
  keywords: ["SKILL", "platforms", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Flow Nexus Platform Management SOP

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



```yaml
metadata:
  skill_name: when-using-flow-nexus-platform-use-flow-nexus-platform
  version: 1.0.0
  category: platform-integration
  difficulty: intermediate
  estimated_duration: 30-60 minutes
  trigger_patterns:
    - "flow nexus platform"
    - "manage flow nexus"
    - "flow nexus authentication"
    - "deploy to flow nexus"
    - "flow nexus sandboxes"
  dependencies:
    - flow-nexus MCP server
    - Valid email for registration
    - Claude Flow hooks
  agents:
    - cicd-engineer (infrastructure orchestrator)
    - backend-dev (service integrator)
    - system-architect (platform designer)
  success_criteria:
    - Authentication successful
    - Services configured and running
    - Application deployed
    - Monitoring active
    - Payment system operational
```

## Overview

Comprehensive Flow Nexus platform management covering authentication, sandboxes, storage, databases, app deployment, payments, and monitoring. This SOP provides end-to-end platform operations.

## MCP Requirements

This skill requires the following MCP servers for optimal functionality:

### Flow-Nexus MCP (78.3k tokens)

**Purpose**: Provides comprehensive cloud platform management including authentication, sandboxes, storage, databases, workflows, templates, payments, and monitoring for this skill's complete workflow.

**Tools Used**:
- `mcp__flow-nexus__user_register`: Register new user accounts
- `mcp__flow-nexus__user_login`: Authenticate and create sessions
- `mcp__flow-nexus__sandbox_create`: Create cloud execution sandboxes
- `mcp__flow-nexus__sandbox_configure`: Configure sandbox environments
- `mcp__flow-nexus__sandbox_execute`: Execute code in sandboxes
- `mcp__flow-nexus__template_list`: List available deployment templates
- `mcp__flow-nexus__template_deploy`: Deploy applications from templates
- `mcp__flow-nexus__storage_upload`: Upload files to cloud storage
- `mcp__flow-nexus__realtime_subscribe`: Subscribe to real-time database changes
- `mcp__flow-nexus__execution_stream_subscribe`: Monitor deployment execution
- `mcp__flow-nexus__check_balance`: Check credit balance
- `mcp__flow-nexus__configure_auto_refill`: Configure automatic credit refills
- `mcp__flow-nexus__system_health`: Check platform health status

**Activation** (PowerShell):
```powershell
# Check if already active
claude mcp list

# Add if not present
claude mcp add flow-nexus npx flow-nexus@latest mcp start

# Verify connection
claude mcp list | Select-String "flow-nexus"
```

**Authentication Required**:
```powershell
# Register new account
npx flow-nexus@latest register

# Login
npx flow-nexus@latest login

# Check authentication
npx flow-nexus@latest whoami
```

**Usage Example**:
```javascript
// Complete platform setup workflow (from Phase 1)
mcp__flow-nexus__user_register({
  email: "user@example.com",
  password: "SecurePassword123!",
  username: "platform_user"
})

mcp__flow-nexus__user_login({
  email: "user@example.com",
  password: "SecurePassword123!"
})

// Create and configure sandbox (Phase 2)
mcp__flow-nexus__sandbox_create({
  template: "node",
  name: "dev-sandbox",
  timeout: 3600,
  env_vars: { NODE_ENV: "development" }
})

// Deploy application (Phase 3)
mcp__flow-nexus__template_deploy({
  template_name: "nextjs-starter",
  deployment_name: "my-app",
  variables: { app_name: "My Application" }
})
```

**Token Cost**: 78.3k tokens (39.2% of 200k context)
**When to Load**: Required for all phases of this skill (authentication, service configuration, deployment, operations, billing)

## Prerequisites

**Required:**
- Flow Nexus MCP server installed
- Valid email address
- Internet connectivity

**Optional:**
- E2B API key for enhanced features
- Anthropic API key for Claude Code sandboxes
- Payment method for credits

**Verification:**
```bash
# Check Flow Nexus MCP availability
claude mcp list | grep flow-nexus

# Test co

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
  pattern: "skills/platforms/SKILL/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "SKILL-{session_id}",
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
