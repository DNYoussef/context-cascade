/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for quality workflows [ground:given] [conf:0.95] [state:confirmed]
category: quality
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic quality processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "quality",
  version: "1.0.0",
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
  keywords: ["SKILL", "quality", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# SKILL: connascence-quality-gate

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## METADATA
- **Name**: Connascence Quality Gate
- **Category**: quality
- **Version**: 1.0.0
- **Triggers**: "quality gate", "code audit", "connascence check", "perfect code", "code quality loop"
- **Dependencies**: ralph-loop, connascence-analyzer
- **MCP Servers**: memory-mcp (optional)

## PURPOSE

Integrates the Connascence Safety Analyzer with the Ralph Wiggum persistence loop to create an automated code quality feedback system. Code is audited after each change, and the loop continues until all quality issues are resolved.

## WHEN TO USE

- After completing any code task to verify quality
- During TDD/refactoring loops to ensure code stays clean
- Before marking a task as complete
- When user wants "perfect" code with no violations

## CORE CONCEPT

```
Write Code -> Audit -> Issues Found? -> Fix -> Repeat
                 |
                 v (No Issues)
            Mark Complete
```

## STANDARD OPERATING PROCEDURE

### Phase 1: Initialize Quality Loop (30s)

1. **Setup State**
   ```bash
   mkdir -p ~/.claude/connascence-audit
   mkdir -p ~/.claude/ralph-wiggum
   ```

2. **Configure Loop**
   ```yaml
   # ~/.claude/ralph-wiggum/loop-state.md
   ---
   session_id: quality-gate-{timestamp}
   active: true
   iteration: 0
   max_iterations: 25
   quality_gate: true
   completion_promise: "CODE_QUALITY_PASSED"
   ---
   {original task prompt}
   ```

3. **Enable Hooks**
   - PostToolUse:Write/Edit runs connascence audit
   - Stop hook checks quality gate before allowing exit

### Phase 2: Development Loop (iterative)

For each iteration:

1. **Write/Edit Code**
   - Implement feature or fix
   - Save changes to file

2. **Automatic Audit** (triggered by hook)
   ```python
   from analyzer.core import ConnascenceAnalyzer
   analyzer = ConnascenceAnalyzer()
   result = analyzer.analyze_path(file_path, policy='strict-core')
   ```

3. **Quality Check**
   - CRITICAL violations: MUST fix immediately
   - HIGH violations: Max 3 allowed
   - MEDIUM/LOW: Recommendations only

4. **Feedback Loop**
   - If issues found: Show violations, continue loop
   - If clean: Allow completion promise

### Phase 3: Completion (when quality passes)

1. **All checks pass**:
   ```
   <promise>CODE_QUALITY_PASSED</promise>
   ```

2. **Quality Gate verified**:
   - No critical violations
   - Max 3 high violations
   - Connascence score > 80%

## INTEGRATION COMMANDS

### Start Quality Gate Loop

```bash
/ralph-loop "Implement {feature} with production-quality code.

QUALITY REQUIREMENTS:
- No critical connascence violations
- Max 3 high-severity issues
- All tests must pass

The Connascence Safety Analyzer will audit your code after each change.
Fix all issues before completing.

Output <promise>CODE_QUALITY_PASSED</promise> when quality gate passes." \
  --completion-promise "CODE_QUALITY_PASSED" \
  --max-iterations 25 \
  --quality-gate true
```

### Manual Audit

```bash
cd D:/Projects/connascence
python -c "
from analyzer.core import ConnascenceAnalyzer
analyzer = ConnascenceAnalyzer()
result = analyzer.analyze_path('path/to/file.py', policy='strict-core')
print(f'Violations: {len(result.get(\"violations\", []))}')
"
```

### View Audit Results

```bash
cat ~/.claude/connascence-audit/latest-results.json | jq .
cat ~/.claude/connascence-audit/pending-issues.md
```

## QUALITY THRESHOLDS

| Severity | Threshold | Blocking |
|----------|-----------|----------|
| CRITICAL | 0 allowed | YES |
| HIGH | Max 3 | YES (if > 3) |
| MEDIUM | Unlimited | NO |
| LOW | Unlimited | NO |

## VIOLATION TYPES CHECKED

The Connascence Safety Analyzer detects:

1. **CoM (Connascence of Meaning)**: Magic literals
2. **CoP (Connascence of Position)**: Parameter bombs (>4 params)
3. **CoA (Connascence of Algorithm)**: Duplicated logic
4. **God Objects**: Classes with >15 methods
5. **NASA Rule Violations**: Deep nesting, long functions
6. **Cyc

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
  pattern: "skills/quality/SKILL/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "SKILL-{session_id}",
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

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
