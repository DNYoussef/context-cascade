/*============================================================================*/
/* WHEN-DOCUMENTING-CODE-USE-DOC-GENERATOR SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-documenting-code-use-doc-generator
version: 1.0.0
description: |
  [assert|neutral] Automated comprehensive code documentation generation with API docs, README files, inline comments, and architecture diagrams [ground:given] [conf:0.95] [state:confirmed]
category: tooling
tags:
- documentation
- api-docs
- readme
- comments
- diagrams
author: system
cognitive_frame:
  primary: honorific
  goal_analysis:
    first_order: "Execute when-documenting-code-use-doc-generator workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic tooling processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-documenting-code-use-doc-generator",
  category: "tooling",
  version: "1.0.0",
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
  keywords: ["when-documenting-code-use-doc-generator", "tooling", "workflow"],
  context: "user needs when-documenting-code-use-doc-generator capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# When Documenting Code - Use Doc Generator

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

This skill provides automated, comprehensive documentation generation for codebases. It analyzes code structure, generates API documentation, creates README files, adds inline comments, and produces architecture diagrams using evidence-based documentation patterns.

## MCP Requirements

This skill operates using Claude Code's built-in tools only. No additional MCP servers required.

## Core Capabilities

1. **Code Analysis**: Extract APIs, functions, classes, types, and dependencies
2. **API Documentation**: Generate OpenAPI, JSDoc, TypeDoc, and Python docstrings
3. **README Generation**: Create comprehensive project documentation
4. **Inline Comments**: Add missing documentation with context-aware comments
5. **Diagram Generation**: Produce architecture and flow diagrams (Graphviz, Mermaid)

## SPARC Methodology: Documentation Generation

### Phase 1: SPECIFICATION - Analyze Documentation Requirements

**Objective**: Understand the codebase structure and documentation needs

**Actions**:
1. Scan project structure and identify file types
2. Detect programming languages and frameworks
3. Identify existing documentation (README, API docs, comments)
4. Analyze documentation gaps and missing coverage
5. Determine documentation standards (JSDoc, TSDoc, Python docstrings)

**Deliverables**:
- Project structure analysis
- Documentation gap report
- Recommended documentation strategy
- Style guide selection

**Agent**: `code-analyzer`

**Example Analysis**:
```
Project: express-api-server
Languages: JavaScript (TypeScript), 85% | JSON 10% | Markdown 5%
Frameworks: Express.js, Jest
Current Documentation:
  - README.md: Exists (outdated, 3 months old)
  - API Docs: None
  - Inline Comments: 12% coverage
  - Type Definitions: 45% coverage

Gaps Identified:
  - ❌ No API documentation (12 endpoints undocumented)
  - ❌ Missing installation instructions
  - ❌ No architecture diagrams
  - ⚠️  Low inline comment coverage
  - ✅ Package.json well-documented

Recommended Strategy:
  1. Generate OpenAPI 3.0 spec for REST API
  2. Add JSDoc comments to all public functions
  3. Create comprehensive README with badges
  4. Generate architecture diagram (system overview)
  5. Add usage examples for main features
```

### Phase 2: PSEUDOCODE - Design Documentation Structure

**Objective**: Plan documentation hierarchy and templates

**Actions**:
1. Design documentation structure (README, API, guides)
2. Define comment style and conventions
3. Create templates for each documentation type
4. Plan diagram types and structure
5. Define metadata and frontmatter standards

**Deliverables**:
- Documentation structure outline
- Template designs for each type
- Comment convention guide
- Diagram specifications

**Example Structure**:
```
Documentation Hierarchy:

docs/
├── README.md                 # Project overview
├── INSTALLATION.md          # Setup guide
├── API.md                   # API reference
├── ARCHITECTURE.md          # System design
├── CONTRIBUTING.md          # Contribution guide
├── diagrams/
│   ├── system-overview.svg  # High-level architecture
│   ├── data-flow.svg        # Data flow diagram
│   └── api-endpoints.svg    # API structure
└── examples/
    ├── basic-usage.md
    └── advanced-features.md

Comment Standards:
- JSDoc for all exported functions
- TypeDoc for TypeScript interfaces
- File header with purpose and author
- Inline comments for complex logic only

API Documentation:
- OpenAPI 3.0 specification
- Example requests/responses
- Error code documentation
- Authentication guide
```

### Phase 3: ARCHITECTURE - Define Generation Pipeline

**Objective**: Design the documentation generation workflow

**Actions**:
1. Define code parsing strategy (AST, regex, static analysis)
2. Design template engine for documentation generation
3. Plan diagram generation pipeline (Graphviz/Mermaid)
4. Define

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
  pattern: "skills/tooling/when-documenting-code-use-doc-generator/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-documenting-code-use-doc-generator-{session_id}",
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

[commit|confident] <promise>WHEN_DOCUMENTING_CODE_USE_DOC_GENERATOR_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
