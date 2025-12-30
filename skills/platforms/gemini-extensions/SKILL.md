/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] Access Gemini's 70+ extensions ecosystem including Figma, Stripe, Postman, Shopify [ground:given] [conf:0.95] [state:confirmed]
category: platforms
tags:
- gemini
- extensions
- figma
- stripe
- integrations
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

# Gemini Extensions Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Leverage Gemini CLI's ecosystem of 70+ extensions to integrate with Figma, Stripe, Postman, Shopify, and other third-party services that Claude Code cannot directly access.

## Unique Capability
**What Claude Code Can't Do**: Direct integration with design tools (Figma), payment APIs (Stripe), API testing (Postman), e-commerce (Shopify), and 70+ other extensions. Gemini CLI provides native integrations via its extension system.

## When to Use

### Perfect For:
✅ Extracting designs from Figma and generating code
✅ Testing Stripe payment integrations
✅ Running Postman API collections
✅ Querying Shopify store data
✅ Accessing Dynatrace, Elastic, Snyk, Harness data
✅ Any task requiring third-party tool integration

### Available Extensions:
- **Figma**: Extract frames, components, design tokens → generate code
- **Stripe**: Test APIs, query payment data, validate integrations
- **Postman**: Run collections, test endpoints, validate APIs
- **Shopify**: Query products, orders, customer data
- **Dynatrace**: Performance monitoring data
- **Elastic**: Search and analytics queries
- **Snyk**: Security vulnerability scanning
- **Harness**: CD pipeline integration

Plus 60+ community extensions on GitHub.

## Usage

```bash
# Install extension
/gemini-extensions --install figma

# Use Figma
/gemini-extensions "Extract components from Figma frame XYZ and generate React code"

# Use Stripe
/gemini-extensions "Test Stripe payment intent creation with test card"

# Use Postman
/gemini-extensions "Run the 'User API' Postman collection and report results"
```

## Real Examples

### Figma → Code
```
/gemini-extensions "Extract button component from Figma frame 'Components/Buttons' and generate React component with TypeScript and styled-components"
```

### Stripe Testing
```
/gemini-extensions "Create a test payment intent for $50 USD using Stripe test API, verify webhook firing"
```

### API Testing
```
/gemini-extensions "Run my Postman collection 'API Tests v2' and identify any failing endpoints"
```

---

**See full documentation** in `.claude/agents/gemini-extensions-agent.md`


---
*Promise: `<promise>SKILL_VERIX_COMPLIANT</promise>`*

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
