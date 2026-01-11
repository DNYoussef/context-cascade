---
name: codex-sandbox
description: Run code in Codex fully isolated sandbox - network disabled, CWD only, Seatbelt/Docker isolation
allowed-tools: Bash, Read, Write, TodoWrite, Glob, Grep
---

# Codex Sandbox Skill



---

## LIBRARY-FIRST PROTOCOL (MANDATORY)

**Before writing ANY code, you MUST check:**

### Step 1: Library Catalog
- Location: `.claude/library/catalog.json`
- If match >70%: REUSE or ADAPT

### Step 2: Patterns Guide
- Location: `.claude/docs/inventories/LIBRARY-PATTERNS-GUIDE.md`
- If pattern exists: FOLLOW documented approach

### Step 3: Existing Projects
- Location: `D:\Projects\*`
- If found: EXTRACT and adapt

### Decision Matrix
| Match | Action |
|-------|--------|
| Library >90% | REUSE directly |
| Library 70-90% | ADAPT minimally |
| Pattern exists | FOLLOW pattern |
| In project | EXTRACT |
| No match | BUILD (add to library after) |

---

## Purpose

Execute code in Codex's fully isolated sandbox environment for safe experimentation with untrusted or risky code.

## Unique Capability

**What Claude Can't Do**: Claude runs in your environment. Codex sandbox provides:
- **Network DISABLED**: No external connections
- **CWD only**: Cannot access parent directories
- **OS-level isolation**: macOS Seatbelt or Docker
- **Resource limits**: CPU, memory constraints
- **Safe experimentation**: Can't break your system

## When to Use

### Perfect For:
- Running untrusted code safely
- Risky refactoring experiments
- Testing code with potential bugs
- Isolated prototyping
- Security research
- Experimental dependencies

### Don't Use When:
- Need network access
- Need to access files outside project
- Production debugging

## Usage

```bash
# Basic sandbox execution
/codex-sandbox "Refactor auth system and run tests"

# With iteration limit
/codex-sandbox "Fix all tests" --max-iterations 10

# Risky experiment
/codex-sandbox "Try experimental algorithm implementation"
```

## CLI Command

```bash
codex --full-auto --sandbox true --network disabled "Your task"

# Via script
CODEX_MODE=sandbox bash scripts/multi-model/codex-yolo.sh "Task" "id" "." "10" "sandbox"
```

## Isolation Layers

| Layer | Protection |
|-------|------------|
| Network | DISABLED - no external connections |
| Filesystem | CWD only - no parent access |
| OS-Level | Seatbelt (macOS) / Docker |
| Process | Subprocess jail with limits |
| Commands | Blocked: rm -rf, sudo, etc. |

## Integration Pattern

```javascript
// 1. Run risky refactoring in sandbox
const result = await codexSandbox("Refactor entire auth system");

// 2. If successful, apply to real codebase
if (result.tests_pass) {
  Task("Coder", "Apply sandboxed changes to main", "coder");
}
```

## Memory Integration

- Key: `multi-model/codex/sandbox/{session_id}`
- Contains: commands, files created/modified, test results
