---
name: sop-dogfooding-pattern-retrieval
description: 3-part dogfooding workflow Phase 2 - Query Memory-MCP for similar past fixes using vector search, rank patterns, optionally apply transformations. 10-30 seconds execution time.
---

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


# SOP: Dogfooding Pattern Retrieval

**Loop 2 of 3-Part System**: Pattern Retrieval → Application

**Purpose**: Query Memory-MCP for similar successful fixes and apply best practices

**Timeline**: 10-30 seconds

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Phase 1: Identify Fix Context (5 sec)

**Agent**: `code-analyzer`

**Prompt**:
```javascript
await Task("Context Analyzer", `
Extract violation context for semantic search.

Input from Phase 1 (Quality Detection):
- Violation type: <type> (e.g., "God Object", "Parameter Bomb")
- File path: <path>
- Violation details: <details> (e.g., "26 methods", "10 parameters")
- Severity: <critical|high|medium|low>

Formulate semantic search query:

Examples:
- "How to fix God Object with 26 methods"
- "Refactor Parameter Bomb with 10 parameters to meet NASA limit"
- "Reduce Deep Nesting from 6 levels to 4"
- "Extract Magic Literals to named constants"
- "Break long function into smaller methods"

Query Construction Rules:
1. Include violation type
2. Include quantitative metric (e.g., "26 methods")
3. Include desired outcome (e.g., "to 4 levels")
4. Use natural language (for better embedding similarity)

Store query: dogfooding/pattern-retrieval/query-<timestamp>
`, "code-analyzer");
```

**Success Criteria**:
- Query formulated with context
- Violation type + metrics included
- Natural language phrasing

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Phase 3: Analyze Retrieved Patterns (5-10 sec)

**Agent**: `code-analyzer` + `reviewer`

**Prompt**:
```javascript
await Task("Pattern Analyzer", `
Analyze top 3 retrieved patterns for applicability.

Input: C:\\Users\\17175\\metrics\\dogfooding\\retrievals\\query-<timestamp>.json

For each pattern:
1. Extract transformation type:
   - Delegation Pattern (God Object → separate classes)
   - Config Object Pattern (Parameter Bomb → object param)
   - Early Return Pattern (Deep Nesting → guard clauses)
   - Extract Method Pattern (Long Function → smaller functions)
   - Named Constant Pattern (Magic Literal → const)
   - Extract Function Pattern (Duplicate Code → DRY)

2. Assess context similarity:
   - Same violation type? (YES/NO)
   - Similar complexity? (e.g., both 20+ methods)
   - Same language? (Python, TypeScript, etc.)
   - Similar domain? (web server, data processing, etc.)

3. Extract improvement metrics:
   - Before state (e.g., "26 methods")
   - After state (e.g., "12 methods")
   - Improvement percentage (e.g., "54% reduction")
   - Side effects (e.g., "None", "Required dependency injection")

4. Check success indicators:
   - Tests still passing after fix?
   - Code quality score improved?
   - No new violations introduced?

Output analysis report for top 3 patterns.
`, "code-analyzer");
```

**Pattern Type Examples**:

**1. Delegation Pattern** (God Object fix):
```javascript
// Before: 26 methods
class Processor {
  process() {...}
  validate() {...}
  transform() {...}
  save() {...}
  // ... 22 more methods
}

// After: 12 methods (54% reduction)
class Processor {
  constructor() {
    this.validator = new Validator(); // 5 methods
    this.transformer = new Transformer(); // 6 methods
    this.storage = new Storage(); // 3 methods
  }
  process() {
    this.validator.validate(...);
    this.transformer.transform(...);
    this.storage.save(...);
  }
}
```

**2. Config Object Pattern** (Parameter Bomb fix):
```javascript
// Before: 10 parameters (violates NASA limit of 6)
function request(url, method, headers, body, timeout, retries, cache, auth, proxy, debug) {...}

// After: 1 parameter
function request(config) {
  const { url, method, headers, body, timeout, retries, cache, auth, proxy, debug } = config;
  ...
}
```

**Success Criteria**:
- Transformation type identified
- Context similarity assessed
- Improvement metrics extracted
- Applicability determined

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Phase 5: Apply Pattern (OPTIONAL, 10-30 sec)

**Agent**: `coder`

**Prompt**:
```javascript
await Task("Pattern Applicator", `
Apply selected pattern transformation to target code.

⚠️ SAFETY RULES CRITICAL ⚠️
See: C:\\Users\\17175\\docs\\DOGFOODING-SAFETY-RULES.md

MANDATORY STEPS:

1. Backup original file
   Command: cp <file> <file>.backup-<timestamp>

2. Parse target code (AST)
   Tool: @babel/parser or python ast module

3. Apply transformation
   Pattern: <selected-transformation>
   Target: <file-path>

4. Write transformed code

5. Run tests (CRITICAL)
   Command: npm test (or pytest)

6. If tests FAIL:
   ROLLBACK: mv <file>.backup-<timestamp> <file>
   ABORT: Do NOT commit changes

7. If tests PASS:
   Proceed to verification

Script: node C:\\Users\\17175\\scripts\\apply-fix-pattern.js --input best-pattern-<timestamp>.json --file <target> --rank 1

NEVER skip testing! ALWAYS rollback on failure!
`, "coder");
```

**Script**: `C:\Users\17175\scripts\apply-fix-pattern.js`

**Transformation Strategies**:

**Strategy 1: Delegation** (God Object):
```javascript
// AST transformation
function applyDelegation(ast, methodsToExtract) {
  // 1. Identify methods to extract
  // 2. Create new class definitions
  // 3. Move methods to new classes
  // 4. Add dependency injection in constructor
  // 5. Update method calls to use delegates
}
```

**Strategy 2: Config Object** (Parameter Bomb):
```javascript
// AST transformation
function applyConfigObject(ast, functionNode) {
  // 1. Find function with >6 params
  // 2. Create config object type/interface
  // 3. Replace params with single config param
  // 4. Add destructuring in function body
  // 5. Update all call sites
}
```

**Safety Checks**:
```bash
# Before transformation
git stash push -u -m "pre-pattern-application-<timestamp>"

# Apply transformation
node apply-fix-pattern.js --file <target> --pattern <id>

# Test
npm test

# If tests fail
if [ $? -ne 0 ]; then
  echo "ROLLBACK: Tests failed"
  git stash pop
  exit 1
fi

# If tests pass
git stash drop
git add <file>
git commit -m "Applied <pattern> - <improvement>"
```

**Success Criteria**:
- Transformation applied successfully
- Tests pass (100% required)
- No new violations introduced
- Code quality improved

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Error Handling

### If No Patterns Found:

**Agent**: `code-analyzer`

```javascript
await Task("Fallback Search", `
No patterns found. Broaden search.

Strategies:
1. Remove quantitative metrics from query
   Before: "God Object with 26 methods"
   After: "God Object refactoring"

2. Search by category only
   Query: "code quality improvement"

3. Increase result limit
   From: --limit 5
   To: --limit 10

4. Check total vector count in Memory-MCP
   Command: python -c "from src.indexing.vector_indexer import VectorIndexer; vi = VectorIndexer(); print(f'Total vectors: {vi.collection.count()}')"

5. If count is 0:
   ERROR: Memory-MCP has no stored patterns
   Action: Run Phase 1 (Quality Detection) first to populate data

Store "no patterns found" event for analysis.
`, "code-analyzer");
```

### If Pattern Application Fails:

**Agent**: `coder`

```javascript
await Task("Failure Handler", `
Pattern application failed. Execute rollback and analysis.

Immediate Actions:
1. Rollback changes
   Command: git checkout <file>

2. Verify rollback
   Command: git diff <file> (should be empty)

3. Re-run tests
   Command: npm test (should pass)

Root Cause Analysis:
1. Why did transformation fail?
   - Syntax error in generated code?
   - Tests failed due to logic change?
   - New violations introduced?

2. Record failure in Memory-MCP
   Metadata:
   {
     intent: "pattern-application-failure",
     pattern_id: "<id>",
     failure_reason: "<reason>",
     transformation: "<type>",
     DO_NOT_APPLY: true
   }

3. Update pattern success_rate
   Decrement on failure

4. Alert user
   Message: "Pattern application failed: <reason>. Changes rolled back. Tests passing."

Never leave codebase in broken state!
`, "coder");
```

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Integration with 3-Part System

**Current Phase**: Phase 2 (Pattern Retrieval)

**Triggered By**:
- `sop-dogfooding-quality-detection` - After violations detected

**Triggers Next**:
- `sop-dogfooding-continuous-improvement` - Full cycle execution

**Works With**:
- `memory-mcp` - Vector search
- `code-analyzer` agent - Pattern analysis
- `coder` agent - Pattern application
- `reviewer` agent - Ranking and selection

-----------|---------|----------|
| **"No Results? Give Up"** | Vector search returns zero results because query is too specific (e.g., "God Object with exactly 26 methods"). Fallback strategies not attempted. | Broaden search progressively: (1) remove quantitative metrics, (2) search by category only, (3) increase result limit 5 -> 10. Search "God Object refactoring" if "God Object with 26 methods" fails. |
| **"Top Result Is Best"** | Applying highest similarity pattern without considering success rate or context match. High similarity (0.95) but low success rate (0.40) means pattern is semantically similar but unreliable. | Use ranking algorithm that combines similarity, success rate, context match, and recency. Pattern with similarity 0.80 + success rate 0.90 beats pattern with similarity 0.95 + success rate 0.40. |
| **"Apply Without Testing"** | Retrieving pattern, applying transformation, skipping sandbox testing because "pattern worked before". Context differences cause breakage in current codebase. | NEVER skip sandbox testing in Phase 5. Pattern application is optional - use retrieval results to inform manual fixes if automatic application is high-risk. Retrieval provides guidance, not guarantee. |

## Conclusion

SOP Dogfooding Pattern Retrieval bridges quality detection (Phase 1) and automated correction (Phase 3) by querying Memory MCP for proven fix patterns based on semantic similarity, historical success rates, and context matching. The 10-30 second execution time includes vector search (5-10s), pattern analysis (5-10s), ranking (5s), and optional AST-based fix application (10-30s). Retrieval outputs include similarity scores, success rates, transformation types, and recommendations - enabling informed decisions about which fixes to apply.

Use this skill as Phase 2 of the 3-part dogfooding system when you have violations detected (from sop-dogfooding-quality-detection) and need proven fix patterns to address them. The skill can operate standalone for manual fix guidance or integrate with sop-dogfooding-continuous-improvement for fully automated correction. Pattern ranking prevents low-quality fixes from being applied - only patterns with 70%+ success rates and 0.70+ similarity scores are recommended for automatic application.

Cross-session learning through Memory MCP means fix quality improves over time as successful patterns accumulate higher success rates and failed patterns are excluded. Teams that use pattern retrieval systematically avoid rediscovering solutions and benefit from institutional memory spanning months or years of past fixes. The result is faster remediation (patterns retrieved in 10-30 seconds vs hours of research) with higher success rates (proven patterns vs experimental approaches).