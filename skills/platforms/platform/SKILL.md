/*============================================================================*/
/* PLATFORM SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: platform
version: 2.1.0
description: |
  [assert|neutral] Platform services hub routing to Flow Nexus platform skills. Use for cloud AI platform management, neural network training, swarm deployment, and platform authentication. Routes to flow-nexus-neural,  [ground:given] [conf:0.95] [state:confirmed]
category: platforms
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute platform workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic platforms processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "platform",
  category: "platforms",
  version: "2.1.0",
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
  keywords: ["platform", "platforms", "workflow"],
  context: "user needs platform capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Platform

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Central hub for Flow Nexus platform services and cloud AI capabilities.

## Phase 0: Expertise Loading

```yaml
expertise_check:
  domain: platform
  file: .claude/expertise/platform.yaml

  if_exists:
    - Load platform configurations
    - Load API patterns
    - Apply service quotas

  if_not_exists:
    - Flag discovery mode
    - Document patterns learned
```

## When to Use This Skill

Use platform when:
- Training neural networks in cloud sandboxes
- Deploying AI swarms to cloud
- Managing Flow Nexus platform services
- Setting up platform authentication
- Integrating payment systems

## Sub-Skills

| Skill | Use Case |
|-------|----------|
| flow-nexus-neural | Neural network training |
| flow-nexus-platform | Platform management |
| flow-nexus-swarm | Cloud swarm deployment |

## Routing Logic

```yaml
routing:
  if "neural" or "training" or "ml":
    route_to: flow-nexus-neural
  if "swarm" or "deploy":
    route_to: flow-nexus-swarm
  if "auth" or "payment" or "sandbox":
    route_to: flow-nexus-platform
  default:
    route_to: flow-nexus-platform
```

## MCP Requirements

- **claude-flow**: Platform coordination
- **memory-mcp**: State management

## Recursive Improvement Integration (v2.1)

### Eval Harness Integration

```yaml
benchmark: platform-benchmark-v1
  tests:
    - plat-001: Platform routing
    - plat-002: Service availability
  minimum_scores:
    routing_accuracy: 0.90
    service_uptime: 0.99
```

### Memory Namespace

```yaml
namespaces:
  - platform/services/{id}: Service configs
  - platform/metrics: Performance tracking
  - improvement/audits/platform: Skill audits
```

### Uncertainty Handling

```yaml
confidence_check:
  if confidence >= 0.8:
    - Route to appropriate service
  if confidence 0.5-0.8:
    - Present service options
  if confidence < 0.5:
    - Ask clarifying questions
```

### Cross-Skill Coordination

Works with: **flow-nexus-neural**, **flow-nexus-platform**, **flow-nexus-swarm**

---

## !! SKILL COMPLETION VERIFICATION (MANDATORY) !!

- [ ] **Agent Spawning**: Spawned agent via Task()
- [ ] **Agent Registry Validation**: Agent from registry
- [ ] **TodoWrite Called**: Called with 5+ todos
- [ ] **Work Delegation**: Delegated to agents

**Remember: Skill() -> Task() -> TodoWrite() - ALWAYS**


## Core Principles

1. **Service Abstraction**: Platform services abstract away infrastructure complexity (E2B sandboxes, QUIC synchronization, GPU allocation) behind unified API interfaces, allowing agents to focus on neural network design rather than cloud resource management.

2. **Resource Efficiency Through Routing**: Intelligent routing minimizes unnecessary service hops - neural training requests go directly to flow-nexus-neural, swarm deployments to flow-nexus-swarm, avoiding generic platform overhead when domain-specific paths are available.

3. **Graceful Degradation with Confidence Scoring**: When routing confidence falls below 0.8, the system presents service options rather than making incorrect assumptions, preventing wasted computation on misrouted requests while maintaining user control.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| Hardcoding service endpoints | Breaks when Flow Nexus platform migrates infrastructure or updates API versions | Use platform routing logic to resolve services dynamically, load from expertise files |
| Skipping Phase 0 expertise loading | Every request re-discovers service quotas, rate limits, and authentication patterns | Always check .claude/expertise/platform.yaml first, cache service configs in memory-mcp namespace |
| Bypassing confidence checks (forcing routes <0.5) | Routes neural training to generic platform service, wasting GPU time on incorrect setup | Respect confidence thresholds, present options or ask clarifying questions when uncertain |

## Conclusion

The 

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
  pattern: "skills/platforms/platform/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "platform-{session_id}",
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

[commit|confident] <promise>PLATFORM_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
