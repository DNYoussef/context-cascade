/*============================================================================*/
/* BASE-TEMPLATE-GENERATOR SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: base-template-generator
version: 2.0.0
description: |
  [assert|neutral] Generate clean, production-ready boilerplate templates for Node.js, Python, Go, React, Vue, and other frameworks. Use when starting new projects or creating consistent foundational code structures. Pr [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- foundry
- creation
- meta-tools
author: ruv
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute base-template-generator workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "base-template-generator",
  category: "foundry",
  version: "2.0.0",
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
  keywords: ["base-template-generator", "foundry", "workflow"],
  context: "user needs base-template-generator capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- Starting new projects requiring solid foundational structure
- Creating consistent boilerplate across team projects
- Scaffolding microservices or API backends
- Setting up frontend applications with modern tooling
- Need Docker and CI/CD ready out-of-box
- Require automated validation and quality checks

### When NOT to Use This Skill
- For existing projects (use refactoring skills instead)
- When custom architecture is required (templates enforce patterns)
- For prototypes that won't reach production
- When dependencies must be minimized beyond template defaults

### Success Criteria
- [assert|neutral] primary_outcome: "Production-ready project template with modern tooling, automated validation, Docker support, and CI/CD integration" [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] quality_threshold: 0.88 [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] verification_method: "Template generates successfully, passes validation scripts, builds without errors, includes working tests and CI/CD pipeline" [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases
- case: "Template type not supported (not in 6 core types)"
  handling: "Identify closest template match, customize post-generation, or request new template type"
- case: "Conflicting dependency requirements"
  handling: "Document conflicts, provide manual override instructions, suggest alternative template"
- case: "Custom project structure needed"
  handling: "Use base template as starting point, document customizations, consider creating new template variant"

### Skill Guardrails
NEVER:
  - "Generate templates with excessive dependencies (minimal deps philosophy)"
  - "Skip validation scripts (automated quality checks required)"
  - "Omit Docker/CI/CD support (production-readiness requirement)"
  - "Use outdated patterns (modern best practices enforced)"
ALWAYS:
  - "Include automated validation tools and quality checks"
  - "Provide Docker support and CI/CD integration out-of-box"
  - "Use modern ES modules, async/await, type hints per language"
  - "Follow standard layout (cmd/internal/pkg for Go, src/tests for others)"
  - "Include comprehensive README with setup and usage instructions"

### Evidence-Based Execution
self_consistency: "After template generation, validate structure matches specification, all scripts execute successfully, and quality checks pass"
program_of_thought: "Decompose generation into: 1) Select template type, 2) Generate base structure, 3) Configure tooling, 4) Add validation, 5) Setup Docker/CI/CD, 6) Validate output"
plan_and_solve: "Plan: Identify project requirements + select template -> Execute: Generate + configure + validate -> Verify: Build success + tests pass + CI/CD ready"
<!-- END SKILL SOP IMPROVEMENT -->

# Base Template Generator (Gold Tier)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Generate clean, production-ready foundational code templates for modern development frameworks with automated validation, Docker support, and CI/CD integration.

## When to Use This Skill

Use this skill when:
- Starting new projects that need solid foundational structure
- Creating consistent boilerplate across team projects
- Scaffolding microservices or API backends
- Setting up frontend applications with modern tooling
- Need Docker and CI/CD ready out-of-box
- Require automated validation and quality checks

## Template Types (6 Supported)

### Backend Templates
- **Node.js with Express** - ES modules, modern async/await, minimal deps
- **Python with FastAPI** - Type hints, async, Pydantic validation
- **Go with standard library** - Standard layout (cmd/internal/pkg), minimal deps

### Frontend Templates
- **React 18 with Vite** - TypeScript, fast HMR, modern tooling
- **Vue 3 Composition API** - TypeScript, Pinia, modern patterns
- *

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
  pattern: "skills/foundry/base-template-generator/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "base-template-generator-{session_id}",
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

[commit|confident] <promise>BASE_TEMPLATE_GENERATOR_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
