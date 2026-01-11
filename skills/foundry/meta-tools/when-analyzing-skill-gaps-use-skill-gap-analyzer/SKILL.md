/*============================================================================*/
/* WHEN-ANALYZING-SKILL-GAPS-USE-SKILL-GAP-ANALYZER SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-analyzing-skill-gaps-use-skill-gap-analyzer
version: 1.0.0
description: |
  [assert|neutral] Analyze skill library to identify coverage gaps, redundant overlaps, optimization opportunities, and provide recommendations for skill portfolio improvement [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- meta-tool
- skill-management
- gap-analysis
- portfolio-optimization
author: ruv
cognitive_frame:
  primary: compositional
  goal_analysis:
    first_order: "Execute when-analyzing-skill-gaps-use-skill-gap-analyzer workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-analyzing-skill-gaps-use-skill-gap-analyzer",
  category: "foundry",
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
  keywords: ["when-analyzing-skill-gaps-use-skill-gap-analyzer", "foundry", "workflow"],
  context: "user needs when-analyzing-skill-gaps-use-skill-gap-analyzer capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- [AUTO-EXTRACTED from skill description and content]
- [Task patterns this skill is optimized for]
- [Workflow contexts where this skill excels]

### When NOT to Use This Skill
- [Situations where alternative skills are better suited]
- [Anti-patterns that indicate wrong skill choice]
- [Edge cases this skill doesn't handle well]

### Success Criteria
- primary_outcome: "[SKILL-SPECIFIC measurable result based on skill purpose]"
- [assert|neutral] quality_threshold: 0.85 [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- verification_method: "[How to validate skill executed correctly and produced expected outcome]"

### Edge Cases
- case: "Ambiguous or incomplete input"
  handling: "Request clarification, document assumptions, proceed with explicit constraints"
- case: "Conflicting requirements or constraints"
  handling: "Surface conflict to user, propose resolution options, document trade-offs"
- case: "Insufficient context for quality execution"
  handling: "Flag missing information, provide template for needed context, proceed with documented limitations"

### Skill Guardrails
NEVER:
  - "[SKILL-SPECIFIC anti-pattern that breaks methodology]"
  - "[Common mistake that degrades output quality]"
  - "[Shortcut that compromises skill effectiveness]"
ALWAYS:
  - "[SKILL-SPECIFIC requirement for successful execution]"
  - "[Critical step that must not be skipped]"
  - "[Quality check that ensures reliable output]"

### Evidence-Based Execution
self_consistency: "After completing this skill, verify output quality by [SKILL-SPECIFIC validation approach]"
program_of_thought: "Decompose this skill execution into: [SKILL-SPECIFIC sequential steps]"
plan_and_solve: "Plan: [SKILL-SPECIFIC planning phase] -> Execute: [SKILL-SPECIFIC execution phase] -> Verify: [SKILL-SPECIFIC verification phase]"
<!-- END SKILL SOP IMPROVEMENT -->

# Skill Gap Analyzer

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Purpose:** Perform comprehensive analysis of skill library to identify missing capabilities, redundant functionality, optimization opportunities, and provide actionable recommendations for skill portfolio improvement.

## When to Use This Skill

- When building a new skill library
- Quarterly skill portfolio reviews
- Before large refactoring efforts
- When considering new skill additions
- After major project pivots
- When optimizing resource allocation

## Analysis Dimensions

### 1. Coverage Gap Analysis
- Domain coverage mapping
- Missing capability identification
- Use case scenario testing
- Workflow completeness assessment
- Integration point analysis

### 2. Redundancy Detection
- Duplicate functionality identification
- Overlapping capability mapping
- Consolidation opportunity analysis
- Version conflict detection
- Naming collision identification

### 3. Optimization Opportunities
- Under-utilized skill detection
- Over-complex skill identification
- Composability improvement suggestions
- Dependency optimization
- Performance bottleneck analysis

### 4. Usage Pattern Analysis
- Frequency metrics
- Co-occurrence patterns
- Success rate tracking
- Token efficiency measurement
- Agent utilization patterns

### 5. Recommendation Generation
- Prioritized action items
- Consolidation strategies
- New skill proposals
- Deprecation candidates
- Restructuring plans

## Execution Process

### Phase 1: Library Inventory

```bash
# Initialize analysis session
npx claude-flow@alpha hooks pre-task --description "Analyzing skill library gaps"

# Scan skill directories
find ~/.claude/skills -name "SKILL.md" -o -name "*.skill.md"
```

**Inventory Script:**
```javascript
function inventorySkills(skillDirectory) {
  const inventory = {
    totalSkills: 0,
    categories: {},
    capabilities: {},
    agents: {},
    complexity: {},
    tags: {}
  };

  // Parse each SKILL.md file
  const skillFiles = findSki

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
  pattern: "skills/foundry/when-analyzing-skill-gaps-use-skill-gap-analyzer/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-analyzing-skill-gaps-use-skill-gap-analyzer-{session_id}",
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

[commit|confident] <promise>WHEN_ANALYZING_SKILL_GAPS_USE_SKILL_GAP_ANALYZER_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
