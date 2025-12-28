---
name: sop-dogfooding-quality-detection
description: 3-part dogfooding workflow Phase 1 - Run Connascence analysis, store results in Memory-MCP with WHO/WHEN/PROJECT/WHY tagging. 30-60 seconds execution time.
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


# SOP: Dogfooding Quality Detection

**Loop 1 of 3-Part System**: Code Quality Detection → Memory Storage

**Purpose**: Automatically detect code quality violations and store findings for cross-session learning

**Timeline**: 30-60 seconds

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


## Phase 1: Pre-Analysis Health Check (5 sec)

**Agent**: `code-analyzer`

**Prompt**:
```javascript
await Task("Code Quality Checker", `
Check system health:
1. Verify Connascence Analyzer MCP is operational
   Command: cd C:\\Users\\17175\\Desktop\\connascence && python -m mcp.cli health-check
   Expected: {"status": "healthy"}

2. Verify Memory-MCP ChromaDB accessible
   Command: python -c "from src.indexing.vector_indexer import VectorIndexer; vi = VectorIndexer(); print('OK')"
   Expected: "OK"

3. Confirm target project exists
   Path: <project-directory>
   Check: Directory contains .py, .js, .ts files

Report status: READY or BLOCKED
`, "code-analyzer");
```

**MCP Tools Used**:
- `mcp__connascence-analyzer__health_check`

**Success Criteria**:
- Connascence returns "healthy"
- ChromaDB initialized
- Target has code files

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


## Phase 3: Store in Memory-MCP (10-20 sec)

**Agent**: `code-analyzer`

**Prompt**:
```javascript
await Task("Memory Storage Agent", `
Store Connascence results in Memory-MCP with proper tagging.

Input JSON: C:\\Users\\17175\\metrics\\dogfooding\\<project>_<timestamp>.json

Script: node C:\\Users\\17175\\scripts\\store-connascence-results.js --project <name> --file <json-path>

Apply WHO/WHEN/PROJECT/WHY Protocol:

WHO:
- agent: "code-analyzer"
- agent_category: "code-quality"

WHEN:
- timestamp_iso: "<ISO-8601>"
- timestamp_unix: <unix-timestamp>
- timestamp_readable: "YYYY-MM-DD HH:MM:SS UTC"

PROJECT:
- project: "<project-name>"

WHY:
- intent: "code-quality-improvement"

ADDITIONAL:
- severity: "critical|high|medium|low"
- fix_category: "god-object|parameter-bomb|etc"
- violations_count: <number>
- platform: "windows|linux|mac"

Store via: VectorIndexer + EmbeddingPipeline
Collection: memory_chunks
Embedding: 384-dimensional (sentence-transformers)
`, "code-analyzer");
```

**Script**: `C:\Users\17175\scripts\store-connascence-results.js`

**MCP Tools Used**:
- `mcp__memory-mcp__memory_store` (via VectorIndexer)

**Node.js Script Logic**:
```javascript
// store-connascence-results.js
const { VectorIndexer } = require('../Desktop/memory-mcp-triple-system/src/indexing/vector_indexer');
const { EmbeddingPipeline } = require('../Desktop/memory-mcp-triple-system/src/indexing/embedding_pipeline');

// Load results JSON
const results = JSON.parse(fs.readFileSync(args.file));

// Generate text summary
const text = `
# Connascence Analysis: ${results.project}
Timestamp: ${results.timestamp}
Files Analyzed: ${results.files_analyzed}
Total Violations: ${results.total_violations}

CRITICAL (NASA Compliance):
- Parameter Bombs: ${results.violations.parameter_bomb}
- Deep Nesting: ${results.violations.deep_nesting}

Violations by Type:
${JSON.stringify(results.violations, null, 2)}
`;

// Create metadata
const metadata = {
  agent: "code-analyzer",
  agent_category: "code-quality",
  timestamp_iso: new Date().toISOString(),
  timestamp_unix: Math.floor(Date.now() / 1000),
  timestamp_readable: new Date().toUTCString(),
  project: results.project,
  intent: "code-quality-improvement",
  severity: results.critical_count > 0 ? "critical" : "medium",
  violations_count: results.total_violations
};

// Store in ChromaDB
const indexer = new VectorIndexer();
const embedder = new EmbeddingPipeline();
const embedding = embedder.encode_single(text);

indexer.collection.add({
  ids: [`dogfooding-${Date.now()}`],
  embeddings: [embedding.tolist()],
  documents: [text],
  metadatas: [metadata]
});
```

**Success Criteria**:
- Data stored in ChromaDB
- Metadata tags applied correctly
- Searchable via `vector_search`

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


## Phase 5: Dashboard Update & Coordination (5 sec)

**Agent**: `code-analyzer`

**Prompt**:
```javascript
await Task("Metrics Coordinator", `
Update Grafana dashboard and notify completion.

Actions:
1. Insert analysis record into SQLite DB
   DB: C:\\Users\\17175\\metrics\\dogfooding\\dogfooding.db
   Table: violations
   Columns: project, timestamp, file_count, total_violations, critical_count, high_count, medium_count

2. Trigger dashboard refresh
   Endpoint: http://localhost:3000/api/datasources/proxy/1/refresh

3. Send MCP coordination hook
   Command: npx claude-flow@alpha hooks post-task --task-id "quality-detection-<timestamp>" --status "complete" --violations "<count>"

4. Prepare next phase trigger
   Set flag: READY_FOR_PATTERN_RETRIEVAL=true

Store completion status in memory: dogfooding/quality-detection/status
`, "code-analyzer");
```

**MCP Tools Used**:
- Claude Flow hooks system

**Bash Commands**:
```bash
# Update SQLite DB
sqlite3 C:\Users\17175\metrics\dogfooding\dogfooding.db \
  "INSERT INTO violations (project, timestamp, total_violations) VALUES ('<project>', '<timestamp>', <count>)"

# Trigger hook
npx claude-flow@alpha hooks post-task --task-id "qd-<timestamp>" --status "complete"
```

**Success Criteria**:
- Database updated
- Dashboard refreshed
- Hook notification sent
- Ready for Phase 2 (pattern retrieval)

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


## Metrics Tracked

1. **Analysis Duration**: Seconds (target: <30s)
2. **Violations Detected**: Count by type
3. **Files Analyzed**: Total count
4. **Storage Success Rate**: Percentage (target: 100%)
5. **Dashboard Update Status**: Success/Fail

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


## Quick Reference

```bash
# Single project
C:\Users\17175\scripts\dogfood-quality-check.bat memory-mcp

# All projects
C:\Users\17175\scripts\dogfood-quality-check.bat all

# Expected outputs:
# 1. JSON: metrics/dogfooding/<project>_<timestamp>.json
# 2. Summary: metrics/dogfooding/summary_<timestamp>.txt
# 3. Memory-MCP storage confirmation
# 4. Dashboard update
```

**Total Duration**: 30-60 seconds
**Agents**: `code-analyzer` (primary), `reviewer` (secondary)
**Tools**: Connascence Analyzer MCP, Memory-MCP, Bash, SQLite
**Output**: Violations detected + stored with metadata + dashboard updated

## Core Principles

SOP Dogfooding Quality Detection operates on 3 fundamental principles:

### Principle 1: Automated Learning from Real Usage
Quality improvement comes from analyzing the code you actually write, not synthetic examples. Self-dogfooding catches real-world violations.

In practice:
- Connascence analysis runs on production codebases (memory-mcp, terminal-manager, trader-ai)
- Violations detected in actual agent-generated code (not test fixtures)
- Memory MCP stores findings with WHO/WHEN/PROJECT/WHY tags for cross-session learning

### Principle 2: NASA-Grade Compliance as Non-Negotiable
Certain quality standards (parameter limits, nesting depth) are grounded in human cognitive science. These thresholds are not subjective preferences.

In practice:
- Parameter Bombs (>6 params) flagged as CRITICAL - NASA research shows human working memory limit
- Deep Nesting (>4 levels) flagged as CRITICAL - exceeds human comprehension capacity
- These violations block merges regardless of "it works" arguments

### Principle 3: Continuous Improvement Through Feedback Loops
Quality detection is only valuable if it feeds back into code generation to prevent repeat violations. Detection without correction is theater.

In practice:
- Phase 1 detects violations, Phase 2 retrieves fix patterns from Memory MCP
- Phase 3 applies fixes with sandbox testing (dogfooding-continuous-improvement)
- Dashboard tracks violation trends over time (are we improving?)

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Analysis Without Storage** | Running Connascence analysis but not storing results in Memory MCP - no cross-session learning | ALWAYS store findings with WHO/WHEN/PROJECT/WHY tags - enables pattern retrieval in Phase 2 |
| **Ignoring NASA Compliance** | Treating Parameter Bombs and Deep Nesting as "suggestions" rather than blockers | Flag NASA violations (>6 params, >4 nesting) as CRITICAL - these are cognitive science limits |
| **Detection Without Action** | Detecting violations but never applying fixes - quality metrics don't improve | Always follow detection (Phase 1) with pattern retrieval (Phase 2) and fix application (Phase 3) |

## Conclusion

SOP Dogfooding Quality Detection closes the loop on AI code quality by automatically analyzing agent-generated code, detecting violations grounded in cognitive science (NASA parameter/nesting limits), and storing findings in Memory MCP for cross-session learning. This enables the dogfooding cycle where Phase 1 detects issues in real codebases, Phase 2 retrieves proven fix patterns from past successes, and Phase 3 applies corrections with sandbox validation. The result is continuous quality improvement - violation rates decrease over time as the system learns from its own mistakes.

Use this skill as the first phase of the 3-part dogfooding system when you need to audit code quality on production codebases and build a knowledge base of violations and fixes. The 30-60 second execution time makes it suitable for post-generation quality gates. For the complete improvement cycle including fix application, use sop-dogfooding-continuous-improvement which orchestrates all three phases.

## Core Principles (Additional)

### Principle 4: False Positives Undermine Trust - Validation Threshold 2+ Signals
Quality detection that flags non-issues as violations trains teams to ignore warnings, eroding trust in the entire system. The 2+ confirming signals threshold (static + dynamic, or static + historical, etc.) reduces false positive rate to <5%, ensuring findings are actionable rather than noise.

In practice:
- Connascence analysis provides static signal (code structure metrics)
- Test execution provides dynamic signal (runtime behavior)
- Git history provides historical signal (frequently changed files correlate with quality issues)
- Findings require agreement from 2+ perspectives before flagging as violation
- Uncertain findings tagged "needs manual review" rather than auto-flagged as violations

### Principle 5: Detection Without Context Is Noise
A Parameter Bomb (14 params) might be a genuine violation in business logic but intentional in a CLI argument parser. Context-aware detection considers domain patterns before flagging violations, reducing false positives and focusing remediation efforts on actual technical debt.

In practice:
- Leverage .claude/expertise/{domain}.yaml when available (domain-specific patterns documented)
- Exclude generated code (build artifacts flagged as low priority)
- Exclude third-party libraries (vendor/ and node_modules/ skipped)
- DSL-specific patterns recognized (e.g., test fixtures often have many parameters intentionally)

### Principle 6: Continuous Detection Enables Continuous Improvement
One-time quality audits capture point-in-time state but do not prevent quality degradation. Continuous detection (daily cycles, post-commit hooks, pre-merge gates) catches violations as they are introduced, enabling immediate remediation before violations multiply.

In practice:
- Daily dogfooding cycles analyze active projects (memory-mcp, terminal-manager, trader-ai)
- Post-commit hooks trigger analysis on modified files (targeted rather than full codebase scan)
- Pre-merge CI gates block PRs with new critical violations (prevents quality regression)
- Dashboard tracks violation trends (are we improving or regressing over time?)

## Common Anti-Patterns (Additional)

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **"One-Time Audit"** | Running Connascence analysis once during "quality sprint", then never again. New code introduces violations that accumulate unnoticed until next sporadic audit. | Continuous detection - daily cycles for active projects, pre-merge gates for all PRs, post-commit hooks for immediate feedback. Quality is maintained through ongoing vigilance, not periodic cleanups. |
| **"Alert Fatigue from False Positives"** | Detection system flags 100+ violations with 30% false positive rate. Teams ignore warnings, treating all findings as noise. Real issues buried in false alarms. | Validation threshold 2+ confirming signals. Accept lower sensitivity to achieve <5% false positive rate. Better to miss 10% of violations than flag 30% non-issues - trust is more valuable than completeness. |
| **"Context-Blind Detection"** | Flagging Parameter Bombs in CLI parsers, Deep Nesting in test fixtures, God Objects in generated ORM models. Teams waste time investigating "violations" that are actually appropriate for context. | Context-aware detection - check .claude/expertise/{domain}.yaml, exclude generated code, recognize DSL patterns. Detection tuned to domain specifics prevents wasted investigation effort. |

## Conclusion (Extended)

SOP Dogfooding Quality Detection provides the foundation for continuous quality improvement by automatically analyzing agent-generated code, detecting violations grounded in cognitive science (NASA parameter/nesting limits), and storing findings in Memory MCP for cross-session learning. The 30-60 second execution time includes Connascence analysis (15-30s), Memory MCP storage (10-20s), and summary generation (5s), making it suitable for post-generation quality gates and pre-merge CI checks.

Use this skill as the entry point into the 3-part dogfooding system when you need to audit code quality on production codebases and build institutional memory of violation patterns. Detection operates on real code (not synthetic test cases), catches violations in agent-generated output, and enables data-driven quality improvement by tracking which violation types are most common and trending over time. Integration with Memory MCP closes the loop - Phase 1 detects issues, Phase 2 retrieves proven fix patterns, Phase 3 applies corrections with safety validation.

Success requires treating detection as continuous rather than one-time - quality degrades without ongoing monitoring. Teams that run daily detection cycles experience continuous improvement as violation rates decrease over time through automated remediation. The validation threshold (2+ confirming signals) and context awareness (<5% false positive rate) ensure findings are actionable and teams trust the system enough to act on recommendations. The result is systematic quality improvement driven by empirical evidence rather than subjective code review.