---
name: hooks-automation
description: Automate Claude Code operations through hooks for pre/post-operation validation, session management, and RBAC security. Integrates with all 10 hook event types (PreToolUse, PostToolUse, UserPromptSubmit, etc.) for validation, logging, and workflow automation.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
---


---
<!-- S0 META-IDENTITY                                                             -->
---

[define|neutral] SKILL := {
  name: "SKILL",
  category: "operations",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

---
<!-- S1 COGNITIVE FRAME                                                           -->
---

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

---
<!-- S2 TRIGGER CONDITIONS                                                        -->
---

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["SKILL", "operations", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

---
<!-- S3 CORE CONTENT                                                              -->
---

# Hooks Automation

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Intelligent automation system that coordinates, validates, and learns from Claude Code operations through hooks integrated with MCP tools and neural pattern training.

## What This Skill Does

This skill provides a comprehensive hook system that automatically manages development operations, coordinates swarm agents, maintains session state, and continuously learns from coding patterns. It enables automated agent assignment, code formatting, performance tracking, and cross-session memory persistence.

**Key Capabilities:**
- **Pre-Operation Hooks**: Validate, prepare, and auto-assign agents before operations
- **Post-Operation Hooks**: Format, analyze, and train patterns after operations
- **Session Management**: Persist state, restore context, generate summaries
- **Memory Coordination**: Synchronize knowledge across swarm agents
- **Git Integration**: Automated commit hooks with quality verification
- **Neural Training**: Continuous learning from successful patterns
- **MCP Integration**: Seamless coordination with swarm tools

## Prerequisites

**Required:**
- Claude Flow CLI installed (`npm install -g claude-flow@alpha`)
- Claude Code with hooks enabled
- `.claude/settings.json` with hook configurations

**Optional:**
- MCP servers configured (claude-flow, ruv-swarm, flow-nexus)
- Git repository for version control
- Testing framework for quality verification

## Quick Start

### Initialize Hooks System

```bash
# Initialize with default hooks configuration
npx claude-flow init --hooks
```

This creates:
- `.claude/settings.json` with pre-configured hooks
- Hook command documentation in `.claude/commands/hooks/`
- Default hook handlers for common operations

### Basic Hook Usage

```bash
# Pre-task hook (auto-spawns agents)
npx claude-flow hook pre-task --description "Implement authentication"

# Post-edit hook (auto-formats and stores in memory)
npx claude-flow hook post-edit --file "src/auth.js" --memory-key "auth/login"

# Session end hook (saves state and metrics)
npx claude-flow hook session-end --session-id "dev-session" --export-metrics
```

---

## Complete Guide

### Available Hooks

#### Pre-Operation Hooks

Hooks that execute BEFORE operations to prepare and validate:

**pre-edit** - Validate and assign agents before file modifications
```bash
npx claude-flow hook pre-edit [options]

Options:
  --file, -f <path>         File path to be edited
  --auto-assign-agent       Automatically assign best agent (default: true)
  --validate-syntax         Pre-validate syntax before edit
  --check-conflicts         Check for merge conflicts
  --backup-file             Create backup before editing

Examples:
  npx claude-flow hook pre-edit --file "src/auth/login.js"
  npx claude-flow hook pre-edit -f "config/db.js" --validate-syntax
  npx claude-flow hook pre-edit -f "production.env" --backup-file --check-conflicts
```

**Features:**
- Auto agent assignment based on file type
- Syntax validation to prevent broken code
- Conflict detection for concurrent edits
- Automatic file backups for safety

**pre-bash** - Check command safety and resource requirements
```bash
npx claude-flow hook pre-bash --command <cmd>

Options:
  --command, -c <cmd>       Command to validate
  --check-safety            Verify command safety (default: true)
  --estimate-resources      Estimate resource usage
  --require-confirmation    Request user confirmation for risky commands

Examples:
  npx claude-flow hook pre-bash -c "rm -rf /tmp/cache"
  npx claude-flow hook pre-bash --command "docker build ." --estimate-resources
```

**Features:**
- Command safety validation
- Resource requirement estimation
- Destructive command confirmation
- Permission checks

**pre-task** - Auto-spawn agents and prepare for complex tasks
```bash
npx claude-flow hook pre-task [options]

Options:
  --description, -d <text>  Task description for context
  --auto-spawn-agent

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

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]