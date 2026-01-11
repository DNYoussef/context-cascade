/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for operations workflows [ground:given] [conf:0.95] [state:confirmed]
category: operations
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic operations processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
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
  keywords: ["SKILL", "operations", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Deployment Readiness

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Validate ML models and systems for production deployment, ensuring operational readiness across performance, monitoring, security, and incident management dimensions.

---

## Aspektual'naya Ramka (Deployment State Tracking)

### Tipy Sostoyaniya (State Types)

**Perfective [SV] - Completed Actions**:
- `[SV:ZAVERSHENO]` - Stage fully completed
- `[SV:PROVERENO]` - Validated and verified
- `[SV:ODOBRENO]` - Approved for next stage
- `[SV:RAZVERNUTO]` - Deployed successfully

**Imperfective [NSV] - Ongoing/Incomplete Actions**:
- `[NSV:V_PROTSESSE]` - Stage actively in progress
- `[NSV:VYPOLNYAETSYA]` - Currently executing
- `[NSV:TESTIRUYETSYA]` - Testing in progress
- `[NSV:MONITORITSYA]` - Under monitoring

**Blocked/Special States**:
- `[ZABLOKIROVANO]` - Blocked by dependency
- `[OZHIDAET]` - Waiting for prerequisite
- `[OTKAT]` - Rollback initiated
- `[AVARIYA]` - Emergency state

### Deployment Pipeline States

```
Infrastructure Setup:
  Capacity Planning      [SV|NSV|ZABLOKIROVANO]
  Environment Setup      [SV|NSV|ZABLOKIROVANO]
  Network Configuration  [SV|NSV|ZABLOKIROVANO]
  → Output: [SV:ZAVERSHENO] or [NSV:V_PROTSESSE]

Performance Benchmarking:
  Latency Testing        [SV|NSV|ZABLOKIROVANO]
  Throughput Testing     [SV|NSV|ZABLOKIROVANO]
  Resource Utilization   [SV|NSV|ZABLOKIROVANO]
  → Output: [SV:PROVERENO] or [NSV:TESTIRUYETSYA]

Monitoring Setup:
  Metrics Collection     [SV|NSV|ZABLOKIROVANO]
  Alerting Configuration [SV|NSV|ZABLOKIROVANO]
  Dashboard Creation     [SV|NSV|ZABLOKIROVANO]
  → Output: [SV:ODOBRENO] or [NSV:V_PROTSESSE]

Deployment Execution:
  Staging Deployment     [SV|NSV|ZABLOKIROVANO|OTKAT]
  Production Deployment  [SV|NSV|ZABLOKIROVANO|OTKAT|AVARIYA]
  Post-Deploy Validation [SV|NSV|ZABLOKIROVANO]
  → Output: [SV:RAZVERNUTO] or [OTKAT] or [AVARIYA]
```

### State Transition Rules

1. **Sequential Progression**: `[NSV] → [SV] → Next Stage [NSV]`
2. **Rollback Path**: `[AVARIYA] → [OTKAT] → Previous [SV]`
3. **Blocking Cascade**: Parent `[ZABLOKIROVANO]` → Children `[OZHIDAET]`
4. **Monitoring Loop**: `[SV:RAZVERNUTO] → [NSV:MONITORITSYA]` (continuous)

### Example State Tracking Output

```markdown
## Deployment Status Report - 2025-12-19 14:32:00

### Infrastructure Validation [SV:ZAVERSHENO]
- Capacity Planning: [SV:ZAVERSHENO] at 2025-12-19 10:15
- Environment Setup: [SV:ZAVERSHENO] at 2025-12-19 12:45
- Network Configuration: [SV:PROVERENO] at 2025-12-19 13:20

### Performance Benchmarking [NSV:TESTIRUYETSYA]
- Latency Testing: [SV:PROVERENO] at 2025-12-19 14:00
- Throughput Testing: [NSV:VYPOLNYAETSYA] started 2025-12-19 14:15
- Resource Utilization: [OZHIDAET] (blocked by throughput test)

### Monitoring Setup [OZHIDAET]
- Blocked by: Performance Benchmarking [NSV:TESTIRUYETSYA]

### Deployment Execution [OZHIDAET]
- Blocked by: All prerequisites must be [SV:ZAVERSHENO]
```

---

## Liangci Kuangjia (Deployment Classification Framework)

### Deployment Type Classifiers

**FEATURE (xin gong-neng)** - New Functionality
- Risk: MEDIUM-HIGH
- Testing: Comprehensive E2E required
- Rollback: Feature flag toggle
- Monitoring: New metrics for feature usage
- Example: "New payment gateway integration"

**HOTFIX (jin-ji xiu-fu)** - Critical Bug Fix
- Risk: HIGH (expedited process)
- Testing: Focused regression on affected area
- Rollback: Immediate revert capability required
- Monitoring: Error rate alerts with 1-min interval
- Example: "Fix authentication bypass vulnerability"

**ROLLBACK (hui-gun)** - Revert to Previous Version
- Risk: LOW-MEDIUM (known good state)
- Testing: Smoke tests only
- Rollback: N/A (is rollback)
- Monitoring: Verify previous metrics restored
- Example: "Revert failed v2.3.0 deployment"

**CONFIG (pei-zhi)** - Configuration-Only Change
- Risk: LOW
- Testing: Config validation, no code changes
- Rollback: Config file revert
- Monitoring: Service health checks
-

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
  pattern: "skills/operations/SKILL/{project}/{timestamp}",
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
