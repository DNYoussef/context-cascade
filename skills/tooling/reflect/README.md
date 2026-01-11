# Reflect Skill

**Version**: 1.0.0 | **Category**: tooling | **Loop**: 1.5

> Correct once, never again. Transform ephemeral session corrections into persistent skill improvements.

## Quick Start

```bash
# Manual reflection after a session
/reflect

# Target a specific skill
/reflect code-review

# Enable automatic reflection on session end
/reflect-on

# Disable automatic reflection
/reflect-off

# Check current status
/reflect-status
```

## What It Does

The Reflect skill solves a fundamental LLM limitation: **sessions don't persist learning**. When you correct Claude's output, that correction is forgotten by the next session.

Reflect captures:
- **Corrections**: "No, use X instead" -> HIGH confidence learning
- **Explicit Rules**: "Always do X" -> HIGH confidence learning
- **Approvals**: "Perfect, that's right" -> MEDIUM confidence learning
- **Observations**: Implicit preferences -> LOW confidence learning

And writes them to skill files where they become permanent knowledge.

## How It Works

```
Session -> Corrections/Patterns -> /reflect -> Skill Updated -> Next Session Improved
```

### The 7-Phase Pipeline

1. **Signal Detection** - Scan conversation for learning signals
2. **Skill Mapping** - Map signals to invoked skills
3. **Confidence Classification** - Apply VERIX-aligned confidence levels
4. **Change Proposal** - Generate diff preview
5. **Apply Updates** - Update SKILL.md files
6. **Memory Storage** - Store in Memory MCP for Meta-Loop
7. **Git Commit** - Version the evolution

### Confidence Levels

| Level | Confidence | Triggers |
|-------|------------|----------|
| **HIGH** | 0.90 | "Always", "Never", explicit corrections |
| **MEDIUM** | 0.75 | Approvals, patterns (2+ occurrences) |
| **LOW** | 0.55 | Single observations, style cues |

## Commands

| Command | Description |
|---------|-------------|
| `/reflect` | Manually trigger reflection on current session |
| `/reflect [skill]` | Reflect on specific skill only |
| `/reflect-on` | Enable automatic reflection on session end |
| `/reflect-off` | Disable automatic reflection |
| `/reflect-status` | Show current toggle state |

## Example Output

```markdown
## Session Reflection Report

### Signals Detected
- 2 corrections (HIGH)
- 1 approval (MEDIUM)

### Proposed Updates

**Skill: debug** (v2.1.0 -> v2.1.1)

```diff
+ ### High Confidence [conf:0.90]
+ - ALWAYS check for null before accessing properties [ground:user-correction:2026-01-05]
```

[Y] Accept  [N] Reject  [E] Edit
```

## Skill File Format

Reflect adds a `LEARNED PATTERNS` section to skill files:

```markdown
## LEARNED PATTERNS

### High Confidence [conf:0.90]
- ALWAYS check for SQL injection [ground:user-correction:2026-01-05]

### Medium Confidence [conf:0.75]
- Prefer async/await over .then() [ground:approval-pattern:2-sessions]

### Low Confidence [conf:0.55]
- User may prefer verbose logging [ground:observation:1-session]
```

## Integration

- **Memory MCP**: Stores learnings for Meta-Loop aggregation
- **Skill Forge**: Uses safe update patterns for SKILL.md
- **Git**: Versions skill evolution with descriptive commits
- **Meta-Loop**: Aggregated learnings feed 3-day optimization

## Safety Rules

1. **NEVER** modifies eval-harness (frozen per Bootstrap Loop)
2. **ALWAYS** shows diff preview before applying
3. **HIGH confidence** changes require explicit approval
4. **Auto-apply** only for MEDIUM/LOW when reflect-on is active

## Architecture: Loop 1.5

Reflect implements **Loop 1.5** - the missing feedback layer:

```
Loop 1:   Execution (per-request)
               |
Loop 1.5: Reflect (per-session) <-- THIS SKILL
               |
Loop 2:   Quality (per-session)
               |
Loop 3:   Meta-Loop (3-day)
```

## Files

```
skills/tooling/reflect/
  SKILL.md        # Main skill definition
  README.md       # This file
  examples/       # Usage examples
  tests/          # Validation tests
  resources/      # Templates
```

## See Also

- `/skill-forge` - Safe skill file updates
- `/prompt-architect` - Constraint classification
- `/bootstrap-loop` - Meta-skill improvement
- `/memory-manager` - Memory MCP operations

---

Confidence: 0.85 (ceiling: observation 0.95)
