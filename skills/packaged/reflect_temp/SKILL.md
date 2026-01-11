---
name: reflect
description: Extract learnings from session corrections and patterns, update skill files with persistent memory. Implements Loop 1.5 - per-session micro-learning between execution and meta-optimization.
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: sonnet
x-version: 1.0.1
x-category: tooling
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
x-loop: 1.5
x-last-reflection: 2026-01-05T00:00:00Z
x-reflection-count: 1
---

### L1 Improvement
- Created as new skill following Skill Forge v3.2 required sections
- Implements Loop 1.5 (Session Reflection) to fill gap between Loop 1 (Execution) and Loop 3 (Meta-Loop)
- Integrates with Memory MCP, Skill Forge, and Ralph Wiggum stop hooks

---



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

## TIER 1: CRITICAL SECTIONS

### Overview

The Reflect skill solves a fundamental limitation of LLMs: **they don't learn from session to session**. Every conversation starts from zero, causing the same mistakes to recur and forcing users to repeat corrections endlessly.

**Philosophy**: Corrections are signals. Approvals are confirmations. Both should be captured, classified, and persisted into skill files where they become permanent knowledge that survives across sessions.

**Methodology**: 7-phase extraction and update pipeline that:
1. Detects learning signals in conversation
2. Maps them to invoked skills
3. Classifies confidence levels (VERIX-aligned)
4. Proposes skill file updates
5. Applies changes via Skill Forge patterns
6. Stores in Memory MCP for Meta-Loop aggregation
7. Commits to Git for version tracking

**Value Proposition**: Correct once, never again. Transform ephemeral session corrections into persistent skill improvements that compound over time.

### Core Principles

The Reflect skill operates on 5 core principles:

#### Principle 1: Signals Over Commands
**Corrections are the strongest learning signals.** When a user says "No, use X instead", this is more valuable than explicit instructions because it reveals a gap between expectation and delivery.

In practice:
- Parse conversation for correction patterns (negation + alternative)
- Weight corrections higher than approvals
- Track correction frequency per skill

#### Principle 2: Evidence-Based Confidence
**All learnings must have VERIX-aligned confidence ceilings.** Don't overclaim certainty from limited evidence.

In practice:
- HIGH (0.90): Explicit "always/never" rules from user
- MEDIUM (0.75): Patterns confirmed across 2+ occurrences
- LOW (0.55): Single observations requiring review

#### Principle 3: Skill File as Memory
**Store learnings in SKILL.md, not in embeddings.** Skill files are human-readable, version-controlled, and immediately effective.

In practice:
- Add LEARNED PATTERNS section to skill files
- Increment x-version on each update
- Track x-last-reflection timestamp

#### Principle 4: Safe by Default
**Preview all changes before applying.** HIGH confidence changes require explicit approval; automation only for MEDIUM/LOW.

In practice:
- Show diff preview before any edit
- Require Y/N for HIGH confidence learnings
- Enable auto-apply only when reflect-on is active

#### Principle 5: Feed the Meta-Loop
**Session learnings aggregate into system optimization.** Micro-learning feeds macro-optimization.

In practice:
- Store all learnings in Memory MCP
- Tag with WHO/WHEN/PROJECT/WHY
- Meta-Loop queries and aggregates every 3 days

### When to Use

**Use Reflect when:**
- You've corrected Claude's output during a session
- A skill produced good results you want to reinforce
- You notice recurring mistakes across sessions
- You want to capture style or preference cues
- Session is ending and you want to preserve learnings
- You see explicit rules emerge ("always X", "never Y")

**Do NOT use Reflect when:**
- Conversation is trivial (< 5 exchanges)
- No skills were invoked in session
- User explicitly says "don't remember this"
- Target is the eval-harness (FORBIDDEN - stays frozen)
- Changes would bypass existing safety gates

### Main Workflow

#### Phase 1: Signal Detection
**Purpose**: Scan conversation for learning signals
**Agent**: intent-parser (from registry)

**Input Contract**:
```yaml
inputs:
  conversation_context: string  # Full session transcript
  invoked_skills: list[string]  # Skills used in session
```

**Process**:
1. Parse conversation for signal patterns
2. Classify each signal by type and strength
3. Extract the learning content

**Signal Types**:
| Type | Pattern | Confidence |
|------|---------|------------|
| Correction | "No, use X", "That's wrong", "Actually..." | HIGH (0.90) |
| Explicit Rule | "Always do X", "Never do Y" | HIGH (0.90) |
| Approval | "Perfect", "Yes, exactly", "That's right" | MEDIUM (0.75) |
| Rejection | User rejected proposed solution | MEDIUM (0.75) |
| Style Cue | Formatting or naming preferences | LOW (0.55) |
| Observation | Implicit preference detected | LOW (0.55) |

**Output Contract**:
```yaml
outputs:
  signals: list[Signal]
  Signal:
    type: correction|explicit_rule|approval|rejection|style_cue|observation
    content: string  # The actual learning
    context: string  # Surrounding context
    confidence: float  # 0.55-0.90
    ground: string  # Evidence source
```

#### Phase 2: Skill Mapping
**Purpose**: Map signals to the skills they apply to
**Agent**: skill-mapper (custom logic)

**Process**:
1. Parse conversation for Skill() invocations
2. Check command history for /skill-name calls
3. Match each signal to its relevant skill
4. Handle multi-skill sessions (separate updates per skill)

**Output Contract**:
```yaml
outputs:
  skill_signals: dict[skill_name, list[Signal]]
```

#### Phase 3: Confidence Classification
**Purpose**: Apply VERIX-aligned confidence levels
**Agent**: prompt-architect patterns

**Classification Rules**:
```
HIGH   [conf:0.90] = Explicit "never/always" rules
                      Direct corrections with clear alternative
                      User used emphatic language

MEDIUM [conf:0.75] = Successful patterns (2+ confirmations)
                      Single strong approval
                      Rejection with implicit preference

LOW    [conf:0.55] = Single observations
                      Style cues without explicit statement
                      Inferred preferences
```

**Ceiling Enforcement**:
- Never exceed 0.95 (observation ceiling)
- Report-based learnings max 0.70
- Inference-based learnings max 0.70

#### Phase 4: Change Proposal
**Purpose**: Generate proposed skill file updates
**Agent**: skill-forge patterns

**Process**:
1. Read current SKILL.md for target skill
2. Check if LEARNED PATTERNS section exists (create if not)
3. Generate diff showing proposed additions
4. Format commit message

**Output Format**:
```markdown
## Proposed Updates

**Skill: {skill_name}** (v{old} -> v{new})

### Signals Detected
- {count} corrections (HIGH)
- {count} approvals (MEDIUM)
- {count} observations (LOW)

### Diff Preview
```diff
+ ### High Confidence [conf:0.90]
+ - {learning content} [ground:{source}:{date}]
```

### Commit Message
reflect({skill}): [{LEVEL}] {description}

---
[Y] Accept  [N] Reject  [E] Edit with natural language
```

#### Phase 5: Apply Updates
**Purpose**: Safely update skill files
**Agent**: skill-forge

**Process**:
1. If approved (manual) or auto-mode enabled:
2. Read skill file
3. Find or create LEARNED PATTERNS section
4. Append new learnings under appropriate confidence level
5. Increment x-version in frontmatter
6. Set x-last-reflection to current timestamp
7. Increment x-reflection-count
8. Write updated file

**LEARNED PATTERNS Section Format**:
```markdown
## LEARNED PATTERNS

### High Confidence [conf:0.90]
- ALWAYS check for SQL injection vulnerabilities [ground:user-correction:2026-01-05]
- NEVER use inline styles in components [ground:user-correction:2026-01-03]

### Medium Confidence [conf:0.75]
- Prefer async/await over .then() chains [ground:approval-pattern:3-sessions]
- Use descriptive variable names in examples [ground:approval-pattern:2-sessions]

### Low Confidence [conf:0.55]
- User may prefer verbose error messages [ground:observation:1-session]
```

#### Phase 6: Memory MCP Storage
**Purpose**: Persist learnings for Meta-Loop aggregation
**Agent**: memory-mcp integration

**Storage Format**:
```json
{
  "WHO": "reflect-skill:{session_id}",
  "WHEN": "{ISO8601_timestamp}",
  "PROJECT": "{project_name}",
  "WHY": "session-learning",
  "x-skill": "{skill_name}",
  "x-version-before": "{old_version}",
  "x-version-after": "{new_version}",
  "x-signals": {
    "corrections": 2,
    "approvals": 1,
    "observations": 1
  },
  "x-learnings": [
    {
      "content": "ALWAYS check for SQL injection",
      "confidence": 0.90,
      "ground": "user-correction",
      "category": "HIGH"
    }
  ]
}
```

**Storage Path**: `sessions/reflect/{project}/{skill}/{timestamp}`

#### Phase 7: Git Commit (Optional)
**Purpose**: Version the skill evolution
**Agent**: bash git commands

**Commit Format**:
```
reflect({skill_name}): [{LEVEL}] {description}

- Added {n} learnings from session
- Confidence levels: HIGH:{n}, MEDIUM:{n}, LOW:{n}
- Evidence: user-correction, approval-pattern, observation

Generated by reflect skill v1.0.0
```

---

## TIER 2: ESSENTIAL SECTIONS

### Pattern Recognition

Different session types require different reflection approaches:

#### Debugging Session
**Patterns**: "bug", "fix", "error", "not working"
**Common Corrections**: Framework choice, error handling patterns, edge cases
**Key Focus**: What was the root cause? What pattern prevents recurrence?
**Approach**: Extract diagnostic insights and prevention rules

#### Code Review Session
**Patterns**: "review", "check", "looks good", "change this"
**Common Corrections**: Style violations, security concerns, naming
**Key Focus**: What standards emerged? What was consistently flagged?
**Approach**: Extract style rules and security patterns

#### Feature Development Session
**Patterns**: "build", "create", "implement", "add"
**Common Corrections**: Architecture choices, component usage, API patterns
**Key Focus**: What design decisions worked? What was rejected?
**Approach**: Extract architectural preferences and component rules

#### Documentation Session
**Patterns**: "document", "explain", "readme", "describe"
**Common Corrections**: Tone, structure, level of detail
**Key Focus**: What style resonated? What format preferred?
**Approach**: Extract documentation style guide entries

### Advanced Techniques

#### Multi-Session Pattern Detection
Track signals across sessions to identify recurring patterns:
- Query Memory MCP for similar signals in past 7 days
- If same correction appears 3+ times, escalate to HIGH confidence
- Detect conflicting signals and flag for resolution

#### Negative Space Analysis
Learn from what was NOT corrected:
- If user didn't correct a pattern, it's implicitly approved
- Track approval-by-silence for frequently used patterns
- Lower confidence (0.55) but valuable signal

#### Skill Dependency Tracking
When correcting skill A, check impact on skills that depend on it:
- Build dependency graph from skill index
- Warn if update might conflict with downstream skills
- Suggest propagating changes to related skills

#### Conflict Resolution
Handle contradictory signals:
- Newer signals override older (recency bias)
- Higher confidence overrides lower
- If true conflict, ask user to resolve
- Store conflict history for pattern analysis

### Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Over-Learning** | Capturing every small preference | Only persist signals that appear 2+ times or are explicit rules |
| **Under-Confidence** | All learnings at LOW confidence | Explicit "always/never" statements are HIGH; don't downgrade |
| **Eval-Harness Modification** | Attempting to update frozen harness | BLOCK: eval-harness never self-improves |
| **Silent Updates** | Applying changes without preview | ALWAYS show diff and require confirmation for HIGH |
| **Orphan Learnings** | Storing in Memory but not SKILL.md | Write to BOTH: skill file for immediate effect, Memory for aggregation |
| **Version Skip** | Not incrementing x-version | ALWAYS bump version on any skill file change |

### Practical Guidelines

#### Full vs Quick Mode

**Full Mode** (default for manual /reflect):
- Scan entire conversation
- Detect all signal types
- Generate comprehensive diff
- Require approval for each change
- Commit to git with detailed message

**Quick Mode** (/reflect --quick or auto mode):
- Focus on explicit corrections only
- Skip style cues and observations
- Auto-apply MEDIUM/LOW changes
- Batch commit at end of session

#### Decision Points

**When to ask user**:
- Conflicting signals detected
- HIGH confidence change proposed
- Same correction already exists (confirm override)
- Signal maps to multiple skills

**When to auto-apply**:
- reflect-on is enabled
- Confidence is MEDIUM or LOW
- No conflicts detected
- Clear skill mapping

---

## TIER 3: INTEGRATION SECTIONS

### Cross-Skill Coordination

#### Upstream Skills (provide input)
| Skill | When Used Before | What It Provides |
|-------|------------------|------------------|
| intent-analyzer | Before reflection | Parsed user intent for signal context |
| prompt-architect | For constraint classification | HARD/SOFT/INFERRED distinction |

#### Downstream Skills (use output)
| Skill | When Used After | What It Does |
|-------|-----------------|--------------|
| skill-forge | After signal classification | Applies safe SKILL.md updates |
| bootstrap-loop | During Meta-Loop | Aggregates learnings for optimization |

#### Parallel Skills (work together)
| Skill | When Used Together | How They Coordinate |
|-------|-------------------|---------------------|
| memory-manager | During storage phase | Stores in Memory MCP |
| github-integration | During commit phase | Handles git operations |

### MCP Requirements

**Required**:
- **memory-mcp**: Store learnings for cross-session retrieval and Meta-Loop aggregation
  - WHY: Central persistence layer for all learnings
  - Tag: WHO=reflect-skill:{session}, WHY=session-learning

**Optional**:
- **sequential-thinking**: For complex multi-signal analysis
  - WHY: Helps reason through conflicting signals
- **vector-search**: For finding similar past learnings
  - WHY: Detect patterns across sessions

### Input/Output Contracts

```yaml
inputs:
  # Required
  trigger: manual | automatic  # How reflect was invoked

  # Optional
  skill_name: string  # Target specific skill (else detect from session)
  mode: full | quick  # Reflection depth
  auto_apply: boolean  # Skip approval for MEDIUM/LOW (requires reflect-on)

outputs:
  # Always returned
  signals_detected: list[Signal]
  skills_updated: list[string]
  learnings_stored: list[MemoryKey]

  # If changes made
  skill_diffs: dict[skill_name, diff_preview]
  version_changes: dict[skill_name, {old: string, new: string}]

  # If git enabled
  commit_hash: string
  commit_message: string
```

### Recursive Improvement

**Role in Meta-Loop**:
The reflect skill is ITSELF subject to Meta-Loop optimization:
- Store self-reflections about signal detection accuracy
- Track false positive rate (learnings user rejected)
- Track coverage (signals user added manually)

**Eval Harness Integration**:
- reflect skill is NOT part of frozen eval harness
- CAN be improved via bootstrap-loop
- MUST NOT modify eval-harness when reflecting on it

**Memory Namespace**:
- Store at: `skills/tooling/reflect/{project}/{timestamp}`
- Retrieve via: query for x-skill=reflect, WHY=self-improvement

---

## TIER 4: CLOSURE SECTIONS

### Examples

#### Example 1: Manual Reflection After Debugging Session

```
User: /reflect

Claude: Analyzing session for learning signals...

## Session Reflection Report

### Signals Detected
- 2 corrections (HIGH confidence)
- 1 approval (MEDIUM confidence)
- 1 observation (LOW confidence)

### Proposed Updates

**Skill: debug** (v2.1.0 -> v2.1.1)

```diff
+ ## LEARNED PATTERNS
+
+ ### High Confidence [conf:0.90]
+ - ALWAYS check for null pointer exceptions before accessing object properties [ground:user-correction:2026-01-05]
+ - Use structured logging instead of console.log in production code [ground:user-correction:2026-01-05]
+
+ ### Medium Confidence [conf:0.75]
+ - Prefer try-catch blocks around async operations [ground:approval-pattern:2026-01-05]
+
+ ### Low Confidence [conf:0.55]
+ - User may prefer detailed stack traces in error messages [ground:observation:2026-01-05]
```

### Commit Message
reflect(debug): [HIGH] Add null check and structured logging rules

---
[Y] Accept  [N] Reject  [E] Edit with natural language

User: Y

Claude: Updates applied successfully.
- Updated: skills/delivery/debug/SKILL.md (v2.1.0 -> v2.1.1)
- Stored: sessions/reflect/my-project/debug/2026-01-05T10:30:00Z
- Committed: reflect(debug): [HIGH] Add null check and structured logging rules

Confidence: 0.85 (ceiling: observation 0.95)
```

#### Example 2: Automatic Reflection via Stop Hook

```
[Session ending - reflect-on is enabled]

==========================================
   SESSION REFLECTION (Automatic)
==========================================

Detected 3 learning signals across 2 skills.

Skill: code-review
  + [MEDIUM] Prefer early returns over nested conditionals

Skill: tester
  + [LOW] Integration tests should mock external APIs
  + [LOW] Use descriptive test names

Auto-applied 3 MEDIUM/LOW learnings.
Stored in Memory MCP.
Git commit: reflect(code-review,tester): [MEDIUM] Session learnings

Next session will include these patterns.
```

#### Example 3: Targeting Specific Skill

```
User: /reflect code-review

Claude: Reflecting on code-review skill specifically...

### Signals for code-review

Found 4 signals:
1. [HIGH] "Never approve PRs with console.log statements" - user-correction
2. [MEDIUM] Security review phase appreciated - approval
3. [MEDIUM] Diff-only output format works well - approval
4. [LOW] May prefer bullet points over paragraphs - observation

Propose adding to skills/quality/code-review/SKILL.md?
[Y] Accept  [N] Reject  [E] Edit
```

### Troubleshooting

| Problem | Solution |
|---------|----------|
| **No signals detected** | Ensure conversation had corrections or approvals. Trivial sessions may not have learnings. |
| **Skill not found** | Verify skill was invoked via Skill() or /command. Check skill-index.json. |
| **Memory MCP unavailable** | Learnings still applied to skill files. Retry memory storage later. |
| **Git commit failed** | Check git status. Ensure no merge conflicts. Manual commit may be needed. |
| **Conflicting learnings** | User must resolve. Show both versions and ask which to keep. |
| **Permission denied on skill file** | Check file permissions. May need elevated access. |
| **x-version not incrementing** | Ensure YAML frontmatter is valid. Check for parsing errors. |

### Conclusion

The Reflect skill transforms ephemeral session corrections into persistent knowledge by implementing **Loop 1.5** - a per-session micro-learning layer that bridges immediate execution (Loop 1) and long-term optimization (Loop 3).

Key capabilities:
- **Signal Detection**: Automatically identifies corrections, approvals, and patterns
- **Confidence Classification**: VERIX-aligned levels (HIGH/MEDIUM/LOW) prevent overclaiming
- **Safe Updates**: Preview-first approach with approval gates for critical changes
- **Memory Integration**: Feeds Meta-Loop for system-wide optimization
- **Version Control**: Git tracking enables rollback and evolution analysis

By capturing learnings at the session level and persisting them in skill files, the Reflect skill enables a self-improving development experience where corrections compound into expertise over time.

### Completion Verification

- [x] YAML frontmatter with x-version, x-category, x-vcl-compliance
- [x] Overview with philosophy, methodology, value proposition
- [x] Core Principles (5 principles with "In practice" items)
- [x] When to Use with use/don't-use criteria
- [x] Main Workflow with 7 phases, agents, input/output contracts
- [x] Pattern Recognition for different session types
- [x] Advanced Techniques (multi-session, negative space, dependencies, conflicts)
- [x] Common Anti-Patterns table with Problem/Solution
- [x] Practical Guidelines for full/quick modes
- [x] Cross-Skill Coordination (upstream/downstream/parallel)
- [x] MCP Requirements with WHY explanations
- [x] Input/Output Contracts in YAML
- [x] Recursive Improvement integration
- [x] Examples (3 complete scenarios)
- [x] Troubleshooting table
- [x] Conclusion summarizing value
- [x] Completion Verification checklist

Confidence: 0.85 (ceiling: observation 0.95) - New skill created following Skill Forge v3.2 required sections with full Tier 1-4 coverage.

---

## LEARNED PATTERNS

### Low Confidence [conf:0.55]
- Self-test on creation session validates the workflow and demonstrates dogfooding [ground:observation:2026-01-05]
  - Context: User requested immediate test after skill creation
  - Action: Offer to run /reflect on the creation session as final validation step

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:R-F-L]] [[COM:Reflect+Skill+Loop]] [[CLS:ge_skill]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:path:/skills/tooling/reflect]]

[define|neutral] REFLECT_SKILL := Per-session micro-learning that extracts corrections and patterns, updates skill files, and stores in Memory MCP for Meta-Loop aggregation [ground:skill-definition] [conf:0.85] [state:confirmed]

[define|neutral] LOOP_1.5 := Session-level reflection layer between Loop 1 (Execution) and Loop 3 (Meta-Loop) that captures immediate learnings [ground:architecture-design] [conf:0.88] [state:confirmed]

[direct|emphatic] EVAL_HARNESS_FROZEN := Reflect skill MUST NOT modify eval-harness; it is frozen per Bootstrap Loop rules [ground:bootstrap-loop-policy] [conf:0.99] [state:confirmed]

[direct|emphatic] CONFIDENCE_CEILINGS := {HIGH:0.90, MEDIUM:0.75, LOW:0.55}; never exceed observation ceiling (0.95) [ground:verix-spec] [conf:0.95] [state:confirmed]

[commit|confident] <promise>REFLECT_SKILL_VCL_V3.1.1_COMPLIANT</promise> [ground:self-check] [conf:0.88] [state:confirmed]
