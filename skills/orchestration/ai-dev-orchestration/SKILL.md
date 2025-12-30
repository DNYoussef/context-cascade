/*============================================================================*/
/* AI-DEV-ORCHESTRATION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: ai-dev-orchestration
version: 2.1.0
description: |
  [assert|neutral] Meta-orchestrator for AI-assisted app development with behavioral guardrails and prompt templates. 5-phase SOP - Product Framing (planner) -> Setup & Foundations (system-architect) -> Feature Developm [ground:given] [conf:0.95] [state:confirmed]
category: orchestration
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute ai-dev-orchestration workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic orchestration processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "ai-dev-orchestration",
  category: "orchestration",
  version: "2.1.0",
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
  keywords: ["ai-dev-orchestration", "orchestration", "workflow"],
  context: "user needs ai-dev-orchestration capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# AI-Assisted App Development Orchestration

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Phase 0: Expertise Loading

Before orchestrating AI development:

1. **Detect Domain**: Identify app type and tech stack
2. **Check Expertise**: Look for `.claude/expertise/ai-dev-${stack}.yaml`
3. **Load Context**: If exists, load guardrail patterns and successful prompts
4. **Apply Configuration**: Use expertise for development orchestration

**Purpose**: Ship reliable apps with AI coding tools while minimizing bugs, rework, and chaos

**Core Principle**: Treat AI as a junior dev with superpowers inside a structured pipeline. Real leverage comes from tight specs, clean context, and strong foundations.

**Timeline**: Varies by complexity (Product Framing 30-60min, Foundations 1-2hrs, Per-Feature 1-3hrs, Testing 30-90min, Deployment 15-30min)

**Integration**: Wraps feature-dev-complete, sparc-methodology, cicd-intelligent-recovery with AI-specific guardrails

---

## System Architecture

```
[User Product Idea]
    ↓
[Phase 0: Product Framing] (planner) - OPTIONAL
    ↓  (App One-Pager, Persona, Validation)
    ↓
[Phase 1: Setup & Foundations] (system-architect)
    ↓  (Stack selection, MVP definition, Foundation implementation)
    ↓
[Phase 2: Feature Development Loop] (coder + tester + reviewer) - ITERATIVE
    ↓  (Per-feature: Plan → Implement → Test → Accept/Rollback)
    ↓  (Fresh context per feature, Do Not Touch lists, Manual testing)
    ↓
[Phase 3: Testing & Refactors] (tester + coder)
    ↓  (Bug fixes, Refactoring with scope limits)
    ↓
[Phase 4: Deployment] (cicd-engineer)
    ↓  (Staging/Production, Monitoring, Health checks)
    ↓
[Memory-MCP Storage] (with WHO/WHEN/PROJECT/WHY tags)
```

---

## When to Use This Skill

Activate this skill when:
- Building apps with AI coding tools (Cursor, Claude Code, Lovable, Bolt)
- Need to prevent AI coding chaos and "theater implementations"
- Want systematic approach to AI-assisted development
- Building greenfield projects (web, mobile, internal tools)
- Small teams or solo builders using AI agents
- Need AI-safe guardrails (scope limiting, context management, testing gates)

**DO NOT** use this skill for:
- Traditional development without AI assistance (use feature-dev-complete)
- Quick scripts or throwaway code (too much process)
- Well-understood repetitive tasks (use existing patterns)
- Emergency hotfixes (skip structured workflow)

---

## Guiding Principles (from second-order insights)

1. **Spec > Code**: Quality depends more on *how well you specify* than how fast you type
2. **Foundations First**: Mini-waterfall for architecture, agile for features
3. **Ephemeral Context**: Fresh chat per feature; persistent knowledge in code/docs, not chat history
4. **Guardrails Over Brute Force**: Constrain what AI can touch; use "do not change X" aggressively
5. **Small, Tested Steps**: One feature at a time, each fully tested before moving on
6. **Human Product Judgment**: AI can simulate validation, but real users validate markets
7. **AI is Factory, You are Orchestrator**: Your job is design specs, run pipeline, decide pass/fail

---

## Input Contract

```yaml
input:
  product:
    name: string (required)
    description: string (required)  # 1-2 sentence "who + what outcome"
    target_user: string (optional)  # Narrow customer segment
    differentiators: array[string] (optional)  # How you differ from competitors

  requirements:
    must_have_features: array[string] (1-2 core features for MVP)
    nice_to_have: array[string]
    constraints:
      technical: array[string]  # Required stack, frameworks
      timeline: string
      budget: string

  options:
    run_product_framing: boolean (default: true)  # Skip if already validated
    auto_test: boolean (default: true)  # Run tests after each feature
    manual_review: boolean (default: true)  # Human approval gates
    deployment_target: enum[staging, production] (default: staging)
`

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
  pattern: "skills/orchestration/ai-dev-orchestration/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "ai-dev-orchestration-{session_id}",
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

[commit|confident] <promise>AI_DEV_ORCHESTRATION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
