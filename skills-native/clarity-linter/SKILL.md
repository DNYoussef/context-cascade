---
name: clarity-linter
description: Machine-readable code clarity auditing with cognitive load optimization. 3-phase SOP - Metrics Collection (code-analyzer) -> Rubric Evaluation (reviewer) -> Fix Generation (coder + analyst). Detects thin helpers, excessive indirection, call chain depth, poor naming, and comment issues.
---

# Clarity Linter

## Phase 0: Expertise Loading

Before linting for clarity:

1. **Detect Domain**: Identify codebase language and patterns
2. **Check Expertise**: Look for `.claude/expertise/clarity-${lang}.yaml`
3. **Load Context**: If exists, load clarity thresholds and naming conventions
4. **Apply Configuration**: Use expertise for context-aware linting

**Purpose**: Evaluate code clarity and cognitive load using machine-readable rubric with weighted scoring

**Timeline**: 35-105 seconds (Metrics 10-30s + Evaluation 5-15s + Fixes 20-60s)

**Integration**: Runs alongside connascence-analyzer in dogfooding quality detection cycles



## When to Use This Skill

Activate this skill when:
- Code quality audit focused on **readability and cognitive load** (not just coupling)
- Detecting thin helpers that add useless indirection
- Analyzing call chain depth and excessive layering
- Evaluating function size and cohesion
- Identifying poor naming patterns that hide complexity
- Checking comment density (over-commented vs under-explained)
- Complementing connascence analysis with clarity-specific patterns

**DO NOT** use this skill for:
- Pure coupling analysis (use connascence-analyzer)
- Security vulnerabilities (use security-testing-agent)
- Performance bottlenecks (use performance-testing-agent)
- Quick lint checks (use quick-quality-check)



## SOP Phase 1: Metrics Collection (10-30 sec)

**Objective**: Collect code metrics for clarity rubric evaluation

**Agent**: `code-analyzer`

**Prompt**:
```javascript
await Task("Clarity Metrics Collector", `
Collect code clarity metrics for rubric evaluation.

Target: <target-path>
Rubric: .claude/skills/clarity-linter/.artifacts/clarity_rubric.json

Metrics to Collect (per function):
1. func_lines: Non-comment, non-blank lines in function body
2. nesting_depth: Maximum nesting depth of control structures
3. is_trivial_expression: Single simple expression or statement
4. is_single_call_forwarder: Single call that forwards parameters verbatim
5. call_count: How many other functions call this function
6. name_semantic_score: 0-1 heuristic of domain meaning in function name
   - 1.0: Rich domain meaning (e.g., 'is_valid_email', 'calculate_compound_interest')
   - 0.5: Moderate meaning (e.g., 'process_data', 'handle_request')
   - 0.1: Generic/vague (e.g., 'do_thing', 'helper', 'util')
7. comment_density: Comment lines / total lines inside function
8. local_domain_spread: 0-1 measure of unrelated concerns touched (0=cohesive, 1=scattered)

Metrics to Collect (per file):
1. thin_helper_count: Count of functions meeting thin helper criteria
2. avg_func_length: Average function length across file
3. avg_nesting_depth: Average nesting depth across file
4. max_call_chain_depth: Estimated max call depth from public entrypoints

Metrics to Collect (per project):
1. max_project_call_chain_depth: Max call chain across whole project
2. duplicate_block_count: Duplicated code blocks >5 lines
3. duplicate_block_details: List of duplications with locations

Output Format (JSON):
{
  "timestamp": "ISO8601",
  "target": "<path>",
  "functions": [
    {
      "file": "path/to/file.py",
      "name": "function_name",
      "line": 42,
      "metrics": {
        "func_lines": 15,
        "nesting_depth": 2,
        "is_trivial_expression": false,
        "is_single_call_forwarder": false,
        "call_count": 3,
        "name_semantic_score": 0.7,
        "comment_density": 0.12,
        "local_domain_spread": 0.3
      }
    }
  ],
  "files": [...],
  "project": {...}
}

Save to: .claude/.artifacts/clarity-metrics-<timestamp>.json

Use hooks for coordination:
npx claude-flow@alpha hooks pre-task --description "clarity metrics collection"
npx claude-flow@alpha hooks post-task --task-id "clarity-metrics"
`, "code-analyzer");
```

**MCP Tools Used**:
- `mcp__memory-mcp__memory_store` (optional: cache results for faster re-runs)

**Bash Commands**:
```bash
# Navigate to target
cd <target-path>

# Analyze with AST parsing (example for Python)
python -c "
import ast
import json
# ... AST analysis to collect metrics ...
with open('.claude/.artifacts/clarity-metrics.json', 'w') as f:
    json.dump(metrics, f, indent=2)
"
```

**Success Criteria**:
- All functions analyzed
- Metrics JSON generated
- No parse errors
- All required metrics present



## SOP Phase 3: Fix Generation & Reporting (20-60 sec)

**Objective**: Generate auto-fixes and human-readable reports

**Agents**: `coder` (auto-fixes) + `analyst` (reports)

**Prompt for Coder** (if auto_fix enabled):
```javascript
await Task("Clarity Fix Generator", `
Generate auto-fix PRs for high-confidence clarity violations.

Evaluation: .claude/.artifacts/clarity-evaluation-<timestamp>.json

Auto-Fix Strategy (by check_id):

1. THIN_HELPER_SIZE / THIN_HELPER_SINGLE_CALL:
   - Inline the helper function at its call site(s)
   - Remove the helper function definition
   - Confidence: HIGH (safe if called ≤3 times)

2. PASS_THROUGH_WRAPPER:
   - Replace wrapper calls with direct calls to underlying function
   - Remove wrapper function
   - Confidence: HIGH (safe if no side effects)

3. SOFT_TOO_LONG_FUNCTION:
   - Identify logical substeps (by code blocks or comments)
   - Extract 2-3 well-named helper functions
   - Confidence: MEDIUM (requires semantic understanding)

4. LOW_COHESION_FUNCTION:
   - Split function by domain concerns
   - Extract separate functions per concern
   - Confidence: MEDIUM (requires domain knowledge)

5. OVERCOMMENTED_FUNCTION:
   - Remove obvious/redundant comments
   - Keep only "why" and non-obvious explanations
   - Confidence: LOW (subjective - suggest only, don't auto-apply)

6. UNDEREXPLAINED_COMPLEX_FUNCTION:
   - Add docstring with purpose, invariants, design decisions
   - Confidence: LOW (requires context - suggest only)

For each HIGH confidence violation:
  Generate git diff patch with before/after
  Include in PR: file path, line numbers, check_id, explanation

Output Format (JSON):
{
  "auto_fixes": [
    {
      "file": "path/to/file.py",
      "violation_id": "THIN_HELPER_SINGLE_CALL",
      "function": "wrapper_func",
      "confidence": "HIGH",
      "diff": "--- a/path/to/file.py\n+++ b/path/to/file.py\n@@ -10,5 +10,1 @@\n-def wrapper_func(x):\n-    return actual_func(x)\n...",
      "explanation": "Inlined wrapper_func at its single call site (line 42). Removed unnecessary indirection."
    }
  ],
  "suggested_fixes": [
    {
      "file": "path/to/file.py",
      "violation_id": "SOFT_TOO_LONG_FUNCTION",
      "function": "process_request",
      "confidence": "MEDIUM",
      "suggestion": "Consider extracting validation logic (lines 45-58) into 'validate_request_params' helper."
    }
  ]
}

Save to: .claude/.artifacts/clarity-fixes-<timestamp>.json
`, "coder");
```

**Prompt for Analyst**:
```javascript
await Task("Clarity Report Generator", `
Generate human-readable clarity audit report.

Evaluation: .claude/.artifacts/clarity-evaluation-<timestamp>.json
Metrics: .claude/.artifacts/clarity-metrics-<timestamp>.json
Fixes: .claude/.artifacts/clarity-fixes-<timestamp>.json

Report Structure (Markdown):

# Code Clarity Audit Report

**Generated**: <timestamp>
**Target**: <target-path>
**Overall Score**: <score> / 1.0
**Verdict**: <ACCEPT | REFINE | REJECT>

## Executive Summary

- **Functions Analyzed**: <count>
- **Files Analyzed**: <count>
- **Total Violations**: <count>
  - Critical: <count>
  - Warning: <count>
  - Info: <count>

## Dimension Scores

| Dimension | Weight | Score | Status |
|-----------|--------|-------|--------|
| Thin Helpers & Indirection | 25% | 0.85 | ✅ |
| Function Size & Cohesion | 25% | 0.60 | ⚠️ |
| Indirection & Call Depth | 20% | 0.75 | ✅ |
| Duplication vs DRY | 15% | 0.90 | ✅ |
| Comments & Explanation | 15% | 0.55 | ⚠️ |
| **Overall** | 100% | **0.73** | **REFINE** |

## Top Violations

### 1. SOFT_TOO_LONG_FUNCTION (5 occurrences)

**Impact**: -0.50 total score impact
**Severity**: Info

**Examples**:
- \`process_request\` (path/to/file.py:42) - 45 lines
- \`handle_data\` (path/to/file.py:108) - 52 lines

**Suggested Fix**: Extract logical substeps into well-named helpers.

### 2. THIN_HELPER_SINGLE_CALL (3 occurrences)

**Impact**: -0.45 total score impact
**Severity**: Warning

**Auto-Fixes Available**: 3 PRs generated

...

## Metrics Summary

### Call Chain Analysis
- Max call chain depth (project): 5 levels
- Max call chain depth (file): 4 levels
- Files with deep chains: 2

### Naming Quality
- High semantic score (>0.7): 85%
- Medium semantic score (0.4-0.7): 12%
- Low semantic score (<0.4): 3%

### Comment Density Distribution
- Overcommented (>0.35): 2 functions
- Well-documented (0.05-0.35): 78 functions
- Underdocumented (<0.05): 12 functions

## Recommendations

1. **Refactor long functions** (5 instances)
   - Priority: High
   - Effort: 2-3 hours
   - Expected improvement: +0.15 score

2. **Inline thin helpers** (3 instances)
   - Priority: High
   - Effort: 30 minutes
   - Auto-fix available: Yes
   - Expected improvement: +0.10 score

3. **Add documentation to complex functions** (12 instances)
   - Priority: Medium
   - Effort: 1-2 hours
   - Expected improvement: +0.08 score

## Next Steps

- [ ] Review and apply auto-fix PRs (3 available)
- [ ] Manual refactoring for medium-confidence violations
- [ ] Re-run clarity-linter after changes
- [ ] Target score: ≥0.8 (ACCEPT threshold)



## Integration with Dogfooding Cycle

**Clarity Linter** complements **Connascence Analyzer** in the 3-phase dogfooding system:

### Phase 1: Quality Detection (30-60s total)
```
Run in Parallel:
  ├─ sop-dogfooding-quality-detection (connascence violations)
  └─ clarity-linter (cognitive load violations)
```

### Phase 2: Pattern Retrieval (10-30s)
```
sop-dogfooding-pattern-retrieval searches Memory-MCP for:
  ├─ Past connascence fixes (coupling patterns)
  └─ Past clarity fixes (indirection/naming/size patterns)
```

### Phase 3: Continuous Improvement (60-120s)
```
sop-dogfooding-continuous-improvement applies:
  ├─ Connascence auto-fixes (God Objects → delegation)
  └─ Clarity auto-fixes (thin helpers → inlining)
```

**Combined Benefits**:
- Connascence: Detects coupling (God Objects, Parameter Bombs, etc.)
- Clarity: Detects cognitive load (thin helpers, long functions, poor naming)
- Together: Comprehensive code quality (coupling + clarity)

----|-------------|--------|
| Phase 1: Metrics Collection | 10-30s | 100-500 functions/sec |
| Phase 2: Rubric Evaluation | 5-15s | 5000 checks/sec |
| Phase 3: Fix Generation | 20-60s | 10-30 fixes/minute |
| **Total** | **35-105s** | **Complete audit in <2 min** |

**Accuracy Targets**:
- Precision: ≥90% (violations are real clarity issues)
- Recall: ≥80% (finds most clarity problems)
- Auto-fix safety: 100% (no breakage from HIGH confidence fixes)



## Artifacts Reference

1. **clarity_rubric.json**: Machine-readable scoring rubric (see .artifacts/)
2. **clarity-metrics-<timestamp>.json**: Collected metrics
3. **clarity-evaluation-<timestamp>.json**: Rubric evaluation results
4. **clarity-fixes-<timestamp>.json**: Auto-fix PRs + suggestions
5. **clarity-audit-report-<timestamp>.md**: Human-readable report



**END OF CLARITY-LINTER SKILL SOP**



## !! SKILL COMPLETION VERIFICATION (MANDATORY) !!

**After invoking this skill, you MUST complete ALL items below before proceeding:**

### Completion Checklist

- [ ] **Agent Spawning**: Did you spawn at least 1 agent via Task()?
  - Example: `Task("Agent Name", "Task description", "agent-type-from-registry")`

- [ ] **Agent Registry Validation**: Is your agent from the registry?
  - Registry location: `claude-code-plugins/ruv-sparc-three-loop-system/agents/`
  - Valid categories: delivery, foundry, operations, orchestration, platforms, quality, research, security, specialists, tooling
  - NOT valid: Made-up agent names

- [ ] **TodoWrite Called**: Did you call TodoWrite with 5+ todos?
  - Example: `TodoWrite({ todos: [8-10 items covering all work] })`

- [ ] **Work Delegation**: Did you delegate to agents (not do work yourself)?
  - CORRECT: Agents do the implementation via Task()
  - WRONG: You write the code directly after reading skill

### Correct Pattern After Skill Invocation

```javascript
// After Skill("<skill-name>") is invoked:
[Single Message - ALL in parallel]:
  Task("Agent 1", "Description of task 1...", "agent-type-1")
  Task("Agent 2", "Description of task 2...", "agent-type-2")
  Task("Agent 3", "Description of task 3...", "agent-type-3")
  TodoWrite({ todos: [
    {content: "Task 1 description", status: "in_progress", activeForm: "Working on task 1"},
    {content: "Task 2 description", status: "pending", activeForm: "Working on task 2"},
    {content: "Task 3 description", status: "pending", activeForm: "Working on task 3"},
  ]})
```

### Wrong Pattern (DO NOT DO THIS)

```javascript
// WRONG - Reading skill and then doing work yourself:
Skill("<skill-name>")
// Then you write all the code yourself without Task() calls
// This defeats the purpose of the skill system!
```

**The skill is NOT complete until all checklist items are checked.**

## Core Principles

### 1. Cognitive Load is Measurable
Code clarity is not subjective. Indirection, nesting depth, function size, and naming quality can be quantified through machine-readable rubrics with weighted scoring.

**In practice:**
- Use clarity_rubric.json with 5 dimensions (25% thin helpers, 25% size/cohesion, 20% call depth, 15% duplication, 15% comments)
- Collect objective metrics: func_lines, nesting_depth, call_count, name_semantic_score, comment_density
- Score 0-1 per dimension based on threshold violations (SOFT_TOO_LONG_FUNCTION > 40 lines)
- Aggregate to overall score with weights (0.8+ ACCEPT, 0.6-0.79 REFINE, <0.6 REJECT)
- Track improvement over time (average score trend, violations by type)
- Use statistical validation (metrics collection on 100-500 functions/sec)

### 2. Indirection is Only Valuable When Semantic
Adding layers of abstraction without adding meaning increases cognitive load. Thin helpers that forward calls or wrap trivial expressions are clarity violations.

**In practice:**
- Detect thin helpers: <=3 lines + trivial expression + low semantic name score
- Identify pass-through wrappers: single call forwarder + no value-add
- Score naming quality: 1.0 for domain meaning (validate_email), 0.1 for generic (do_thing, helper)
- Count call depth (max 4 levels per file, 6 levels per project)
- Auto-fix HIGH confidence violations: inline thin helpers, remove wrappers
- Require semantic justification for abstraction layers

### 3. Fixes Must Be Safe and Evidence-Based
Auto-fixes should only apply to high-confidence, mechanical transformations. Complex refactorings require human judgment.

**In practice:**
- HIGH confidence (auto-apply): Inline thin helper called <=3 times, remove pass-through wrapper
- MEDIUM confidence (suggest only): Extract substeps from long function, split low-cohesion function
- LOW confidence (suggest only): Adjust comment density, add documentation to complex functions
- All auto-fixes tested for correctness (no breakage from inlining)
- Suggested fixes include rationale and expected improvement
- Track auto-fix success rate (no regressions allowed)

-----------|---------|----------|
| **Creating thin helpers for "clean code"** | Adds useless indirection, hides complexity instead of reducing it, increases call depth | Inline helpers <=3 lines with trivial logic. Only extract if semantic value added (meaningful name, reusable abstraction). |
| **Over-abstracting for "DRY"** | Creates God Objects, parameter bombs, excessive indirection to avoid 2 lines of duplication | Allow intentional duplication for clarity. Extract only when pattern is genuine, reusable, and semantically cohesive. |
| **Ignoring cognitive load metrics** | Code "looks clean" but has 8-level nesting, 72-line functions, 14-parameter methods | Enforce NASA coding standards: max 4 nesting levels, 50 lines per function, 6 parameters per method. Measure objectively. |
| **Auto-fixing without validation** | Breaks functionality, introduces bugs, loses semantic meaning during mechanical refactoring | Only auto-fix HIGH confidence violations (inline, remove wrapper). Suggest MEDIUM/LOW confidence fixes. Test all changes. |
| **Confusing comments with clarity** | Over-commented code (comment_density > 0.35) hides poor naming and structure | Good code self-documents. Use comments for "why", not "what". If comments explain code, improve code instead. |
| **Skipping baseline comparison** | Cannot prove improvement, may make code worse while chasing metrics | Always compare before/after scores. Track improvement delta. Validate that refactoring improves clarity, not just metrics. |

---

## Conclusion

The Clarity Linter skill operationalizes code clarity through machine-readable rubrics that quantify cognitive load across five dimensions: thin helpers, function size, call depth, duplication, and comments. By collecting objective metrics and applying weighted scoring, this skill transforms subjective code review into evidence-based quality assessment.

The emphasis on indirection as the primary clarity violation challenges the "clean code" assumption that more abstraction is always better. Thin helpers, pass-through wrappers, and excessive call depth increase cognitive load without reducing complexity. The skill detects these patterns automatically and provides high-confidence auto-fixes (inlining, wrapper removal) alongside lower-confidence suggestions (extracting substeps, splitting cohesion).

By integrating with the dogfooding cycle (Phase 1: quality detection, Phase 2: pattern retrieval, Phase 3: continuous improvement), the Clarity Linter enables systematic code quality improvement with pattern learning across projects. The combination of objective metrics, safe auto-fixes, and transparent reporting makes code clarity measurable, improvable, and auditable - transforming it from an art into an engineering discipline.