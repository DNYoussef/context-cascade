/*============================================================================*/
/* DOCUMENTATION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: documentation
version: 2.2.0
description: |
  [assert|neutral] Documentation generation hub for code documentation, API docs, READMEs, and inline comments. Routes to doc-generator and related documentation tools. Use when generating or improving project documenta [ground:given] [conf:0.95] [state:confirmed]
category: tooling
tags:
- general
author: system
cognitive_frame:
  primary: honorific
  goal_analysis:
    first_order: "Execute documentation workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic tooling processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "documentation",
  category: "tooling",
  version: "2.2.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Honorific",
  source: "Japanese",
  force: "Who is the audience?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["documentation", "tooling", "workflow"],
  context: "user needs documentation capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Documentation

## Keigo Wakugumi (Honorific Frame Activation)
Taishougisha nintei moodoga yuukoudesu.



Central hub for generating and maintaining project documentation.

## Phase 0: Expertise Loading & Cognitive Frame Activation

```yaml
expertise_check:
  domain: documentation
  file: .claude/expertise/documentation.yaml

  if_exists:
    - Load documentation standards
    - Load project conventions
    - Apply style guides

  if_not_exists:
    - Flag discovery mode
    - Document patterns learned

cognitive_activation:
  - Activate hierarchical documentation framework (Keigo Wakugumi)
  - Activate morphological concept extraction (Al-Itar al-Sarfi)
  - Map codebase to audience levels
  - Extract documentation concepts from code structure
```

## Cognitive Frame 1: Keigo Wakugumi (Hierarchical Documentation)

Documentation organized by **audience level** and **scope hierarchy** - from executive summaries to implementation details.

### Rejisutaa Shurui (Audience Register Levels)

**SONKEIGO (Executive/Respectful)** - High-level overview, business value:
- **Purpose**: Explain "why this exists" for executives, product managers
- **Content**: Business value, ROI, strategic alignment, high-level architecture
- **Format**: Executive summary, one-page overviews, architecture diagrams
- **Example**: "This authentication system reduces security incidents by 40% and enables SSO integration"

**TEINEIGO (Developer/Polite)** - Technical details, API reference:
- **Purpose**: Enable developers to integrate and use the system
- **Content**: API reference, function signatures, parameters, return values, examples
- **Format**: OpenAPI specs, JSDoc, function-level documentation
- **Example**: "POST /api/auth/login - Accepts email/password, returns JWT token (200) or error (401)"

**CASUAL (Internal/Plain)** - Implementation notes, quick reference:
- **Purpose**: Help maintainers understand internal workings
- **Content**: Code comments, implementation notes, architectural decisions (ADRs)
- **Format**: Inline comments, ADRs, internal wikis
- **Example**: "// Uses bcrypt with cost factor 12 - balances security vs performance"

### Hierarchy Structure (Multi-Level Documentation)

```
LEVEL 1 (SYSTEM) - Architecture Overview
├── What: System purpose and scope
├── Why: Business drivers and constraints
├── How: High-level architecture
└── Who: Stakeholders and users
    |
    ├── LEVEL 2 (COMPONENT) - Module Documentation
    |   ├── Component responsibility
    |   ├── Dependencies and interfaces
    |   ├── Data flow diagrams
    |   └── Configuration options
    |       |
    |       ├── LEVEL 3 (INTERFACE) - API/Function Docs
    |       |   ├── Function signatures
    |       |   ├── Parameters and types
    |       |   ├── Return values and errors
    |       |   └── Usage examples
    |       |       |
    |       |       └── LEVEL 4 (IMPLEMENTATION) - Code Comments
    |       |           ├── Algorithm explanations
    |       |           ├── Edge case handling
    |       |           ├── Performance considerations
    |       |           └── TODO/FIXME notes
```

### Documentation Routing by Audience

| Audience | Register | Level | Example |
|----------|----------|-------|---------|
| CTO, Product Manager | SONKEIGO | L1 System | "Reduces auth latency by 60%" |
| External Developer | TEINEIGO | L3 Interface | "auth.login(email, password) -> Promise<Token>" |
| Team Developer | TEINEIGO | L2 Component | "Auth module handles JWT, OAuth, SAML" |
| Maintainer | CASUAL | L4 Implementation | "// Edge case: token refresh race condition" |
| New Hire | TEINEIGO | L2-L3 | "Architecture + API quick start" |

## Cognitive Frame 2: Al-Itar al-Sarfi lil-Tawthiq (Morphological Documentation)

Documentation sections **derived from code structure** - extract concepts from patterns, root words, and compositions.

### Concept Extraction Process

**ROOT (Jidhir)** - Core concept identified from codebase:
- Extracted from: Class names, module names, 

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
  pattern: "skills/tooling/documentation/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "documentation-{session_id}",
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

[commit|confident] <promise>DOCUMENTATION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
