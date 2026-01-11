---
name: ralph-multimodel
description: Ralph Wiggum persistence loop with intelligent multi-model routing (Gemini, Codex, Claude, Council)
allowed-tools: Bash, Read, Write, TodoWrite, Task, Glob, Grep
---

# Ralph Wiggum Multi-Model Persistence Loop



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

Extend the Ralph Wiggum persistence pattern with intelligent model routing:
- **Gemini** for research phases (search, megacontext, media)
- **Codex** for autonomous iteration (yolo, full-auto, sandbox)
- **Claude** for complex reasoning
- **LLM Council** for critical decisions

## Unique Capability

**What This Adds**:
- Automatic model selection based on task phase
- Best-of-breed capabilities per iteration
- Fire-and-forget with optimal tool selection
- Multi-model consensus for critical decisions

## When to Use

### Perfect For:
- Complex tasks requiring multiple model strengths
- Overnight autonomous development
- Tasks mixing research + implementation + testing
- Critical decisions needing consensus
- Large codebase refactoring with validation

### Don't Use When:
- Simple single-model tasks
- Time-critical (model switching adds latency)
- Need human oversight at each step

## How It Works

```
ITERATION N:
    |
    +---> Detect Task Phase
    |         |
    |         +---> Research? --> Gemini (search/megacontext)
    |         +---> Media?    --> Gemini (imagen/veo)
    |         +---> Iterate?  --> Codex (yolo/full-auto)
    |         +---> Decide?   --> LLM Council (consensus)
    |         +---> Reason?   --> Claude (agents)
    |
    +---> Execute with Optimal Model
    |
    +---> Check Completion Promise
    |         |
    |         +---> Found? --> EXIT SUCCESS
    |         +---> Not found? --> CONTINUE
    |
    +---> ITERATION N+1 (until max)
```

## Usage

### Basic Multi-Model Loop
```bash
/ralph-multimodel "Build REST API, research best practices, implement, test, fix failures until all pass"
```

### With Codex Sandbox Mode
```bash
CODEX_MODE=sandbox /ralph-multimodel "Experiment with auth refactoring, verify tests"
```

### With LLM Council for Decisions
```bash
USE_COUNCIL=true /ralph-multimodel "Design authentication architecture with consensus"
```

### Overnight Task
```bash
MAX_ITERATIONS=100 /ralph-multimodel "Complete feature X with documentation, Output <promise>DONE</promise> when finished"
```

## Command Pattern

```bash
bash scripts/multi-model/ralph-multimodel.sh "<task>" "<loop_id>"

# Environment options:
MAX_ITERATIONS=30        # Maximum loop iterations
COMPLETION_PROMISE=DONE  # Text signaling completion
USE_COUNCIL=false        # Use LLM Council for decisions
CODEX_MODE=full-auto     # Codex mode: yolo, full-auto, sandbox
```

## Phase Detection & Routing

| Phase Detected | Keywords | Model Used |
|----------------|----------|------------|
| Research | "search", "latest", "documentation", "best practices" | Gemini |
| Megacontext | "entire codebase", "all files", "architecture overview" | Gemini --all-files |
| Media | "diagram", "mockup", "image", "video" | Gemini (Imagen/Veo) |
| Autonomous | "fix tests", "debug", "iterate", "prototype" | Codex (yolo/full-auto) |
| Decision | "decide", "choose", "architecture decision" | LLM Council |
| Reasoning | Default | Claude |

## Memory Integration

Results stored per iteration:
- Gemini: `multi-model/gemini/yolo/ralph-{iteration}`
- Codex: `multi-model/codex/yolo/ralph-{iteration}`
- Council: `multi-model/council/decisions/ralph-{iteration}`

State files:
- `~/.claude/ralph-wiggum/loop-state.json`
- `~/.claude/ralph-wiggum/loop-history.log`

## Integration with Meta-Loop

Ralph Multi-Model connects to the recursive improvement system:

```
META-LOOP INTEGRATION:
    |
    +---> PROPOSE (auditors detect issues)
    |         |
    |         +---> Ralph Multi-Model for implementation
    |
    +---> TEST (frozen eval harness)
    |
    +---> COMPARE (baseline vs candidate)
    |
    +---> COMMIT (if improved)
    |
    +---> MONITOR (7-day window)
    |
    +---> ROLLBACK (if regressed)
```

## Real-World Examples

### Example 1: Full-Stack Feature
```bash
/ralph-multimodel "Build user dashboard:
1. Research React dashboard best practices (Gemini)
2. Generate UI mockup (Gemini Media)
3. Implement frontend components (Claude)
4. Build backend API (Codex yolo)
5. Write tests (Claude)
6. Fix all failing tests (Codex full-auto)
Output <promise>ALL_TESTS_PASS</promise> when done"
```

### Example 2: Codebase Refactoring
```bash
MAX_ITERATIONS=50 CODEX_MODE=sandbox /ralph-multimodel "
Refactor auth system:
1. Analyze entire codebase architecture (Gemini megacontext)
2. Identify all auth touchpoints
3. Implement new JWT pattern in sandbox (Codex)
4. Run tests and fix failures
Output <promise>REFACTOR_COMPLETE</promise> when all tests pass"
```

### Example 3: Architecture Decision
```bash
USE_COUNCIL=true /ralph-multimodel "
Decide database strategy:
1. Research PostgreSQL vs MongoDB for our use case (Gemini)
2. Get multi-model consensus on approach (Council)
3. Document decision
Output <promise>DECISION_MADE</promise>"
```

## Success Indicators

- Loop completes with COMPLETION_PROMISE found
- Optimal model used for each phase
- Memory contains full iteration history
- State files show successful completion

## Troubleshooting

### Loop Never Completes
- Check COMPLETION_PROMISE is achievable
- Increase MAX_ITERATIONS
- Verify task includes clear completion criteria

### Wrong Model Selected
- Be more explicit in task description
- Use phase keywords (see routing table)

### Codex Failures
- Check Codex CLI is installed
- Verify ChatGPT Plus subscription active
- Try different CODEX_MODE

## Related Resources

- Ralph Wiggum Loop: `skills/orchestration/ralph-loop/SKILL.md`
- Multi-Model Scripts: `scripts/multi-model/`
- Meta-Loop: `skills/recursive-improvement/`
- Memory Namespace: `docs/MEMORY-NAMESPACE-SCHEMA.yaml`
