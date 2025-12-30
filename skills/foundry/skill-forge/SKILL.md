---
name: skill-forge
description: Advanced skill creation system for Claude Code that combines deep intent analysis, evidence-based prompting principles, and systematic skill engineering. Use when creating new skills or refining exist
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
---


---
<!-- S0 META-IDENTITY                                                             -->
---

[define|neutral] SKILL := {
  name: "skill-forge",
  category: "foundry",
  version: "3.0.1",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

---
<!-- S1 COGNITIVE FRAME                                                           -->
---

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

---
<!-- S2 TRIGGER CONDITIONS                                                        -->
---

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["skill-forge", "foundry", "workflow"],
  context: "user needs skill-forge capability"
} [ground:given] [conf:1.0] [state:confirmed]

---
<!-- S3 CORE CONTENT                                                              -->
---

<!-- ANTHROPIC OFFICIAL FORMAT TEMPLATE v1.0 -->
## CRITICAL: Skill Output Format (Anthropic Compliant)

When creating skills, you MUST use this exact YAML frontmatter format:

```yaml
---
name: skill-name-here
description: Plain text description of when to use this skill (NO VERIX notation here)
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
x-version: 1.0.0
x-category: delivery|foundry|operations|orchestration|platforms|quality|research|security|specialists|tooling
x-tags:
  - tag1
  - tag2
x-author: author-name
x-verix-description: Optional VERIX notation for AI-to-AI communication
---
```

### REQUIRED Fields (Anthropic Official):
- `name`: Skill identifier (lowercase, hyphenated)
- `description`: Plain text - NO [assert|neutral] or VERIX notation
- `allowed-tools`: Comma-separated list of allowed tools

### OPTIONAL Fields (x- prefixed custom extensions):
- `x-version`: Semantic version
- `x-category`: Category for organization
- `x-tags`: Array of tags for discovery
- `x-author`: Creator name
- `x-verix-description`: VERIX notation (for backward compatibility)
- `x-cognitive-frame`: Frame metadata (evidential, aspectual, etc.)

### Content Body Format:
- Use standard markdown (# headings, ## subheadings)
- Use HTML comments for section markers: `<!-- S0 META-IDENTITY -->`
- VERIX notation is allowed in the body, not in YAML frontmatter description
- NO `/* */` comment blocks - use markdown instead

### Example Correct Skill:
```markdown
---
name: my-new-skill
description: Automates database migration with rollback support
allowed-tools: Read, Write, Edit, Bash, Task
x-version: 1.0.0
x-category: operations
x-tags:
  - database
  - migration
x-author: ruv
---

# My New Skill

## When to Use
- Database schema changes needed
- Data migration required

## Procedure
1. Analyze current schema
2. Generate migration scripts
3. Test rollback procedure
4. Execute migration

## Success Criteria
- All migrations applied successfully
- Rollback tested and verified
```

<!-- END ANTHROPIC FORMAT TEMPLATE -->

<!-- HOOK SKILL CREATION GUIDE v1.0 -->
## Creating Hook-Related Skills

When creating skills that automate Claude Code hooks, follow these additional guidelines:

### Hook Skill Naming Convention

Use the trigger-first pattern with hook context:
- `when-validating-commands-use-pre-hook-validator`
- `when-auditing-operations-use-post-hook-logger`
- `when-managing-sessions-use-session-hooks`

### Required Integration Points

Hook-related skills MUST reference:
```yaml
x-integration:
  hook_reference: hooks/12fa/docs/CLAUDE-CODE-HOOKS-REFERENCE.md
  identity_system: hooks/12fa/utils/identity.js
  templates: skills/specialists/when-creating-claude-hooks-use-hook-creator/resources/templates/
```

### Hook Event Types Reference

Skills may target any of the 10 Claude Code hook events:

| Category | Event | Purpose |
|----------|-------|---------|
| Blocking | UserPromptSubmit | Validate/modify prompts |
| Blocking | SessionStart | Initialize sessions |
| Blocking | PreToolUse | Validate tool calls |
| Blocking | PermissionRequest | Auto-approve/deny |
| Observational | PostToolUse | Log results |
| Observational | Notification | Forward notifications |
| Observational | Stop | Agent cleanup |
| Observational | SubagentStop | Subagent tracking |
| Observational | PreCompact | Preserve context |
| Observational | SessionEnd | Session cleanup |

### Hook Skill File Structure

```
skills/specialists/my-hook-skill/
  SKILL.md              # Main skill definition
  metadata.json         # Sidecar with custom fields
  resources/
    scripts/
      hook-logic.js     # Main hook implementation
    templates/
      config.yaml       # Hook configuration template
  tests/
    test-scenarios.md   # Test cases
  examples/
    example-usage.md    # Usage examples
```

### Performance Requirements

Document performance targets in metadata.json:
```json
{
  "x-performance": {
    "pre_hook_target_ms": 20,
    "pre_hook_max_ms": 100,
    "post_hook_target_ms": 100,
    "post_hook_max_ms": 1000
  }
}
```

### Related Resources

- **Hook Creator Skill**: `skills/specialists/when-creating-claude-hooks-use-hook-creator/`
- **Hook Reference**: `hooks/12fa/docs/CLAUDE-CODE-HOOKS-REFERENCE.md`
- **Existing Hook Skill**: `skills/operations/hooks-automation/`
<!-- END HOOK SKILL CREATION GUIDE -->

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

---
<!-- S4 SUCCESS CRITERIA                                                          -->
---

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

---
<!-- S5 MCP INTEGRATION                                                           -->
---

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

---
<!-- S6 MEMORY NAMESPACE                                                          -->
---

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

---
<!-- S7 SKILL COMPLETION VERIFICATION                                             -->
---

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

---
<!-- S8 ABSOLUTE RULES                                                            -->
---

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

---
<!-- PROMISE                                                                      -->
---

[commit|confident] <promise>SKILL_FORGE_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]