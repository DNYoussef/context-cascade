/*============================================================================*/
/* SKILL-FORGE SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: skill-forge
version: 3.0.1
description: |
  [assert|neutral] Advanced skill creation system for Claude Code that combines deep intent analysis, evidence-based prompting principles, and systematic skill engineering. Use when creating new skills or refining exist [ground:given] [conf:0.95] [state:confirmed]
category: foundry
tags:
- foundry
- creation
- meta-tools
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute skill-forge workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic foundry processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "skill-forge",
  category: "foundry",
  version: "3.0.1",
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
  keywords: ["skill-forge", "foundry", "workflow"],
  context: "user needs skill-forge capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

<!-- SKILL SOP IMPROVEMENT v1.0 -->
## Skill Execution Criteria

### When to Use This Skill
- Creating new skills with comprehensive structure and validation
- Building agent-powered workflows with multi-agent orchestration
- Developing production-grade skills with proper documentation
- Need adversarial testing and COV protocol validation
- Creating skills that integrate with MCP servers and Claude Flow

### When NOT to Use This Skill
- For quick atomic micro-skills (use micro-skill-creator instead)
- For agent creation without skill wrapper (use agent-creator)
- For prompt optimization only (use prompt-architect)
- When simple script suffices without skill abstraction

### Success Criteria
- [assert|neutral] primary_outcome: "Production-grade skill with comprehensive structure, agent coordination, adversarial testing, and integration documentation" [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] quality_threshold: 0.91 [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] verification_method: "Skill passes adversarial testing protocol, survives COV validation, integrates with Claude Flow, includes examples and tests" [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases
- case: "Skill requires complex multi-agent coordination"
  handling: "Use agent orchestration patterns, define clear coordination protocol, test with ruv-swarm"
- case: "Skill needs MCP server integration"
  handling: "Declare MCP dependencies in frontmatter, add auto-enable logic, document requirements"
- case: "Skill has performance constraints"
  handling: "Add performance benchmarks, optimize agent selection, implement caching strategies"

### Skill Guardrails
NEVER:
  - "Skip adversarial testing (validation protocol required for production)"
  - "Create skills without proper file structure (examples, tests, resources mandatory)"
  - "Omit MCP integration points (skills should leverage available tools)"
  - "Use generic coordination (leverage specialized orchestration agents)"
ALWAYS:
  - "Follow file structure standards (examples/, tests/, resources/, references/)"
  - "Include adversarial testing protocol and COV validation"
  - "Declare MCP server dependencies in YAML frontmatter"
  - "Provide comprehensive examples with expected inputs/outputs"
  - "Document integration with Claude Flow and agent coordination"

### Evidence-Based Execution
self_consistency: "After skill creation, run multiple execution rounds with diverse inputs to verify consistent behavior and agent coordination quality"
program_of_thought: "Decompose skill forge into: 1) Define skill purpose, 2) Design agent coordination, 3) Build core structure, 4) Add examples/tests, 5) Apply adversarial validation, 6) Document integration"
plan_and_solve: "Plan: Identify skill scope + agents needed -> Execute: Build structure + coordinate agents + validate -> Verify: Adversarial testing + COV protocol + integration tests"
<!-- END SKILL SOP IMPROVEMENT -->

# Skill Forge

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



An advanced skill creation system that helps craft sophisticated, well-engineered skills for Claude Code by combining deep intent analysis, evidence-based prompting principles, and systematic skill engineering methodology.

## Overview

Skill Forge represents a meta-cognitive approach to skill creation. Rather than simply generating skill templates, it guides you through a comprehensive process that ensures every skill you create is strategically designed, follows best practices, and incorporates sophisticated prompt engineering techniques.

This skill operates as an intelligent collaborator that helps you think deeply about what you're trying to achieve, identifies the optimal structure for your skill, and applies evidence-based techniques to maximize effectiveness. The result is skills that are not just functional but genuinely powerful extensions of Claude's capab

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
  pattern: "skills/foundry/skill-forge/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "skill-forge-{session_id}",
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

[commit|confident] <promise>SKILL_FORGE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* LEARNED PATTERNS                                                            */
/*----------------------------------------------------------------------------*/

## LEARNED PATTERNS

### High Confidence [conf:0.90]
- Skill file update workflow: (1) Unzip skill.zip to temp dir, (2) Edit SKILL.md to add/update LEARNED PATTERNS section, (3) Update version in manifest.json, (4) Rezip with PowerShell Compress-Archive, (5) Copy back to dist folder [ground:witnessed:execution:2026-01-08]

### Medium Confidence [conf:0.75]
- Windows path handling: PowerShell Compress-Archive requires Windows paths (C:\...) not Unix paths (/tmp/...). Use `cygpath -w /path` to convert Git Bash paths to Windows paths when invoking PowerShell commands. [ground:error-correction:2026-01-08]
- File tool reliability: When Edit tool fails with "File has been unexpectedly modified" errors, use Bash heredoc (`cat > file << 'EOF'`) as fallback - more reliable for appending/replacing file contents [ground:observation:pattern:2026-01-08]
- MCP server integration pattern: When integrating new components (like ObsidianMCPClient), expose in __init__.py __all__ list, document config in .env, provide standalone test script, update README with usage examples [ground:approval:successful-pattern:2026-01-08]

### Low Confidence [conf:0.55]
- Python standalone scripts: Use Path(__file__).parent.parent to get project root, add to sys.path, and os.chdir() to project root before imports to avoid relative import issues [ground:observation:fix:2026-01-08]

