---
name: code-review-assistant
description: Comprehensive PR review using multi-agent swarm with specialized reviewers for security, performance, style, tests, and documentation. Provides detailed feedback with auto-fix suggestions and merge readiness assessment.
---

## Kanitsal Kod Incelemesi (Evidential Code Review)

Her bulgu icin kaynak belirtilmeli:
- **DOGRUDAN**: Kod satirinda goruldu [file:line]
- **STIL_KURALI**: Style guide referansi [rule_id]
- **EN_IYI_PRATIK**: Best practice citation [reference]

Every review comment MUST cite:
1. **Code location**: [file:line] with surrounding context
2. **Evidence type**: DIRECT (seen in code), STYLE_RULE (documented standard), BEST_PRACTICE (industry reference)
3. **Reference source**: Style guide section, security advisory, performance benchmark

## Keigo Wakugumi (Hierarchical Organization)

Rejisutaa Shurui (Severity Levels):
- **SONKEIGO (CRITICAL)**: Architecture-level issues (security vulnerabilities, data loss risks)
- **TEINEIGO (MAJOR)**: Module-level issues (performance bottlenecks, maintainability problems)
- **CASUAL (MINOR)**: Function-level improvements (code style, readability)
- **NIT**: Line-level suggestions (formatting, naming)

Review findings are organized hierarchically:
1. System-level concerns (architecture, security, data integrity)
2. Component-level issues (modules, services, APIs)
3. Implementation details (functions, algorithms)
4. Surface-level polish (style, naming, comments)

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


# Code Review Assistant

## Purpose

Automated comprehensive code review using specialized multi-agent swarm for PRs.

## Specialist Agent

I am a code review coordinator managing specialized review agents.

**Methodology** (Multi-Agent Swarm Review Pattern):
1. Initialize review swarm with specialized agents
2. Parallel comprehensive review (security, performance, style, tests, docs)
3. Run complete quality audit pipeline
4. Aggregate findings with severity ranking
5. Generate fix suggestions with Codex
6. Assess merge readiness with quality gates
7. Create detailed review comment

**Review Agents** (5 specialists):
- **Security Reviewer**: Vulnerabilities, unsafe patterns, secrets
- **Performance Analyst**: Bottlenecks, optimization opportunities
- **Style Reviewer**: Code style, best practices, maintainability
- **Test Specialist**: Test coverage, quality, edge cases
- **Documentation Reviewer**: Comments, API docs, README updates

## Input Contract

```yaml
input:
  pr_number: number (required) or
  changed_files: array[string] (file paths)
  focus_areas: array[enum] (default: all)
    - security
    - performance
    - style
    - tests
    - documentation
  suggest_fixes: boolean (default: true)
  auto_merge_if_passing: boolean (default: false)
```

## Output Contract

```yaml
output:
  review_summary:
    overall_score: number (0-100)
    merge_ready: boolean
    blocking_issues: number
    warnings: number
    suggestions: number
  detailed_reviews:
    security: object
    performance: object
    style: object
    tests: object
    documentation: object
  fix_suggestions: array[code_change]
  merge_decision: enum[approve, request_changes, needs_work]
```

### Review Finding Template (Evidence-Based)

Every finding MUST use this structure:

```yaml
finding:
  issue: "[description of problem]"
  evidence:
    location: "[file:line]"
    code_snippet: |
      [5 lines before]
      > [problematic line(s)]
      [5 lines after]
    evidence_type: "DIRECT | STYLE_RULE | BEST_PRACTICE"
  reference:
    source: "[style_guide | security_advisory | benchmark | standard]"
    citation: "[specific section or rule ID]"
    url: "[optional reference link]"
  severity: "CRITICAL | MAJOR | MINOR | NIT"
  scope: "ARCHITECTURE | MODULE | FUNCTION | LINE"
  confidence: number (0.0-1.0)
  suggested_fix: |
    [specific code change or approach]
```

**Example**:
```yaml
finding:
  issue: "SQL injection vulnerability in user query"
  evidence:
    location: "src/api/users.js:42"
    code_snippet: |
      40: app.get('/users', (req, res) => {
      41:   const userId = req.query.id;
      > 42:   const sql = `SELECT * FROM users WHERE id = ${userId}`;
      43:   db.query(sql, (err, results) => {
      44:     res.json(results);
    evidence_type: "DIRECT"
  reference:
    source: "OWASP Top 10 2021"
    citation: "A03:2021 - Injection"
    url: "https://owasp.org/Top10/A03_2021-Injection/"
  severity: "CRITICAL"
  scope: "FUNCTION"
  confidence: 1.0
  suggested_fix: |
    Use parameterized queries:
    const sql = 'SELECT * FROM users WHERE id = ?';
    db.query(sql, [userId], (err, results) => {
```

## Execution Flow

```bash
#!/bin/bash
set -e

PR_NUMBER="$1"
FOCUS_AREAS="${2:-security,performance,style,tests,documentation}"
SUGGEST_FIXES="${3:-true}"

REVIEW_DIR="pr-review-$PR_NUMBER"
mkdir -p "$REVIEW_DIR"

echo "================================================================"
echo "Code Review Assistant: PR #$PR_NUMBER"
echo "================================================================"

# PHASE 1: PR Information Gathering
echo "[1/8] Gathering PR information..."
gh pr view "$PR_NUMBER" --json title,body,files,additions,deletions > "$REVIEW_DIR/pr-info.json"

PR_TITLE=$(cat "$REVIEW_DIR/pr-info.json" | jq -r '.title')
CHANGED_FILES=$(cat "$REVIEW_DIR/pr-info.json" | jq -r '.files[].path' | tr '\n' ' ')

echo "PR: $PR_TITLE"
echo "Files changed: $(echo $CHANGED_FILES | wc -w)"

# Checkout PR branch
gh pr checkout "$PR_NUMBER"

# PHASE 2: Initialize Review Swarm
echo "[2/8] Initializing multi-agent review swarm..."
npx claude-flow coordination swarm-init \
  --topology mesh \
  --max-agents 5 \
  --strategy specialized

# Spawn specialized review agents
npx claude-flow automation auto-agent \
  --task "Comprehensive code review of PR#$PR_NUMBER focusing on: $FOCUS_AREAS" \
  --strategy optimal \
  --max-agents 5

# PHASE 3: Parallel Specialized Reviews
echo "[3/8] Executing specialized reviews in parallel..."

# Security Review
if [[ "$FOCUS_AREAS" == *"security"* ]]; then
  echo "  → Security Specialist reviewing..."
  npx claude-flow security-scan . \
    --deep true \
    --check-secrets true \
    --output "$REVIEW_DIR/security-review.json" &
  SEC_PID=$!
fi

# Performance Review
if [[ "$FOCUS_AREAS" == *"performance"* ]]; then
  echo "  → Performance Analyst reviewing..."
  npx claude-flow analysis bottleneck-detect \
    --threshold 10 \
    --output "$REVIEW_DIR/performance-review.json" &
  PERF_PID=$!
fi

# Style Review
if [[ "$FOCUS_AREAS" == *"style"* ]]; then
  echo "  → Style Reviewer checking..."
  npx claude-flow style-audit . \
    --fix false \
    --output "$REVIEW_DIR/style-review.json" &
  STYLE_PID=$!
fi

# Test Review
if [[ "$FOCUS_AREAS" == *"tests"* ]]; then
  echo "  → Test Specialist analyzing..."
  npx claude-flow test-coverage . \
    --detailed true \
    --output "$REVIEW_DIR/test-review.json" &
  TEST_PID=$!
fi

# Documentation Review
if [[ "$FOCUS_AREAS" == *"documentation"* ]]; then
  echo "  → Documentation Reviewer checking..."
  # Check for README updates, JSDoc comments, etc.
  npx claude-flow docs-checker . \
    --output "$REVIEW_DIR/docs-review.json" &
  DOCS_PID=$!
fi

# Wait for all reviews to complete
wait $SEC_PID $PERF_PID $STYLE_PID $TEST_PID $DOCS_PID 2>/dev/null || true

# PHASE 4: Complete Quality Audit
echo "[4/8] Running complete quality audit..."
npx claude-flow audit-pipeline . \
  --phase all \
  --model codex-auto \
  --output "$REVIEW_DIR/quality-audit.json"

# PHASE 5: Aggregate Review Findings
echo "[5/8] Aggregating review findings..."
cat > "$REVIEW_DIR/aggregated-review.json" <<EOF
{
  "pr_number": $PR_NUMBER,
  "pr_title": "$PR_TITLE",
  "reviews": {
    "security": $(cat "$REVIEW_DIR/security-review.json" 2>/dev/null || echo "{}"),
    "performance": $(cat "$REVIEW_DIR/performance-review.json" 2>/dev/null || echo "{}"),
    "style": $(cat "$REVIEW_DIR/style-review.json" 2>/dev/null || echo "{}"),
    "tests": $(cat "$REVIEW_DIR/test-review.json" 2>/dev/null || echo "{}"),
    "documentation": $(cat "$REVIEW_DIR/docs-review.json" 2>/dev/null || echo "{}"),
    "quality_audit": $(cat "$REVIEW_DIR/quality-audit.json")
  }
}
EOF

# Calculate scores
SECURITY_SCORE=$(cat "$REVIEW_DIR/security-review.json" 2>/dev/null | jq '.score // 100')
PERF_SCORE=$(cat "$REVIEW_DIR/performance-review.json" 2>/dev/null | jq '.score // 100')
STYLE_SCORE=$(cat "$REVIEW_DIR/style-review.json" 2>/dev/null | jq '.quality_score // 100')
TEST_SCORE=$(cat "$REVIEW_DIR/test-review.json" 2>/dev/null | jq '.coverage_percent // 100')
QUALITY_SCORE=$(cat "$REVIEW_DIR/quality-audit.json" | jq '.overall_score // 100')

OVERALL_SCORE=$(echo "($SECURITY_SCORE + $PERF_SCORE + $STYLE_SCORE + $TEST_SCORE + $QUALITY_SCORE) / 5" | bc)

# PHASE 6: Generate Fix Suggestions
if [ "$SUGGEST_FIXES" = "true" ]; then
  echo "[6/8] Generating fix suggestions with Codex..."

  # Collect all issues
  ISSUES=$(cat "$REVIEW_DIR/aggregated-review.json" | jq '[.reviews[] | .issues? // [] | .[]]')

  if [ "$(echo $ISSUES | jq 'length')" -gt 0 ]; then
    codex --reasoning-mode "Suggest fixes for code review issues" \
      --context "$REVIEW_DIR/aggregated-review.json" \
      --output "$REVIEW_DIR/fix-suggestions.md"
  fi
fi

# PHASE 7: Assess Merge Readiness
echo "[7/8] Assessing merge readiness..."

CRITICAL_SECURITY=$(cat "$REVIEW_DIR/security-review.json" 2>/dev/null | jq '.critical_issues // 0')
TESTS_PASSING=$(cat "$REVIEW_DIR/quality-audit.json" | jq '.functionality_audit.all_passed // false')

MERGE_READY="false"
MERGE_DECISION="request_changes"

if [ "$CRITICAL_SECURITY" -eq 0 ] && [ "$TESTS_PASSING" = "true" ] && [ "$OVERALL_SCORE" -ge 80 ]; then
  MERGE_READY="true"
  if [ "$OVERALL_SCORE" -ge 90 ]; then
    MERGE_DECISION="approve"
  else
    MERGE_DECISION="approve_with_suggestions"
  fi
fi

# PHASE 8: Create Review Comment
echo "[8/8] Creating review comment..."

cat > "$REVIEW_DIR/review-comment.md" <<EOF
# Automated Code Review (Evidence-Based)

**Overall Score**: $OVERALL_SCORE/100
**Merge Ready**: $([ "$MERGE_READY" = "true" ] && echo "Yes" || echo "No")

## Review Summary

| Category | Score | Status |
|----------|-------|--------|
| Security | $SECURITY_SCORE/100 | $([ "$SECURITY_SCORE" -ge 80 ] && echo "PASS" || echo "FAIL") |
| Performance | $PERF_SCORE/100 | $([ "$PERF_SCORE" -ge 80 ] && echo "PASS" || echo "FAIL") |
| Style | $STYLE_SCORE/100 | $([ "$STYLE_SCORE" -ge 80 ] && echo "PASS" || echo "FAIL") |
| Tests | $TEST_SCORE/100 | $([ "$TEST_SCORE" -ge 80 ] && echo "PASS" || echo "FAIL") |
| Quality | $QUALITY_SCORE/100 | $([ "$QUALITY_SCORE" -ge 80 ] && echo "PASS" || echo "FAIL") |

## TEINEIGO (MAJOR) - Module-Level Issues

### Performance Review
$(cat "$REVIEW_DIR/performance-review.json" 2>/dev/null | jq -r '.major_issues // [] | map("#### " + .issue + "\n- **Evidence**: [" + .file + ":" + (.line|tostring) + "]\n- **Reference**: " + .benchmark + "\n- **Severity**: MAJOR\n- **Scope**: MODULE\n\n**Suggested Fix**: " + .suggested_fix) | join("\n\n")' || echo "No performance bottlenecks detected")

### Test Coverage
- **Test Coverage**: $TEST_SCORE%
- **All Tests Passing**: $([ "$TESTS_PASSING" = "true" ] && echo "Yes" || echo "No")
- **Missing Tests**: $(cat "$REVIEW_DIR/test-review.json" 2>/dev/null | jq -r '.missing_tests // [] | join(", ")' || echo "None")

## NIT - Line-Level Suggestions

$(cat "$REVIEW_DIR/style-review.json" 2>/dev/null | jq -r '.nits // [] | map("- " + .issue + " [" + .file + ":" + (.line|tostring) + "]") | join("\n")' || echo "No nits")

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


🤖 Generated by Claude Code Review Assistant
EOF

# Post review comment
gh pr comment "$PR_NUMBER" --body-file "$REVIEW_DIR/review-comment.md"

# Approve or request changes
if [ "$MERGE_DECISION" = "approve" ]; then
  gh pr review "$PR_NUMBER" --approve --body "Code review passed! Overall score: $OVERALL_SCORE/100 ✅"
elif [ "$MERGE_DECISION" = "approve_with_suggestions" ]; then
  gh pr review "$PR_NUMBER" --approve --body "Approved with suggestions. See detailed review comment. Score: $OVERALL_SCORE/100 ✅"
else
  gh pr review "$PR_NUMBER" --request-changes --body "Please address review findings before merging. Score: $OVERALL_SCORE/100"
fi

echo ""
echo "================================================================"
echo "Code Review Complete!"
echo "================================================================"
echo ""
echo "Overall Score: $OVERALL_SCORE/100"
echo "Merge Ready: $MERGE_READY"
echo "Decision: $MERGE_DECISION"
echo ""
echo "Review artifacts in: $REVIEW_DIR/"
echo "Review comment posted to PR #$PR_NUMBER"
echo ""
```

## Integration Points

### Cascades
- Part of `/github-automation-workflow` cascade
- Used by `/pr-quality-gate` cascade
- Invoked by `/review-pr` command

### Commands
- Uses: `/swarm-init`, `/auto-agent`, `/security-scan`
- Uses: `/bottleneck-detect`, `/style-audit`, `/test-coverage`
- Uses: `/audit-pipeline`, `/codex-reasoning`
- Uses GitHub CLI: `gh pr view`, `gh pr checkout`, `gh pr comment`, `gh pr review`

### Other Skills
- Invokes: `quick-quality-check`, `smart-bug-fix` (if issues)
- Output to: `merge-decision-maker`, `pr-enhancer`

## Usage Example

```bash
# Review PR with all checks
code-review-assistant 123

# Review focusing on security
code-review-assistant 123 security

# Review with auto-merge
code-review-assistant 123 "security,tests" true --auto-merge true
```

## Failure Modes

- **PR not found**: Verify PR number and repository access
- **Critical security issues**: Block merge, escalate to security team
- **Tests failing**: Request changes, provide fix suggestions
- **GitHub CLI not authenticated**: Guide user to authenticate
-----------|---------|----------|
| **Approval Without Execution** | Approving code based on reading alone without running tests or seeing actual output | ALWAYS require passing CI/CD, local execution, or sandbox testing before approval |
| **Nitpicking Style Over Substance** | Focusing on minor formatting issues while missing critical security vulnerabilities or logic errors | Use automated linters for style; human reviewers focus on security, logic, architecture |
| **Sequential Review Bottleneck** | Running reviews one-by-one (security -> performance -> docs) causing 8+ hour delays | Run all specialized reviews in PARALLEL using swarm coordination (2 hours total) |

## Conclusion

Code Review Assistant transforms PR review from a subjective, sequential bottleneck into an objective, parallel quality gate. By coordinating 5 specialized reviewers (security, performance, style, tests, docs) in parallel and requiring evidence-based validation, it achieves comprehensive coverage in 4 hours vs 8+ hours sequential. The system enforces the critical rule that code is NEVER approved without execution proof - all tests must pass, security scans must complete, and performance profiling must show acceptable metrics before merge approval. This multi-agent approach catches issues that single-reviewer processes miss while maintaining fast turnaround through parallelization.

Use this skill when you need thorough PR review with multiple quality dimensions evaluated simultaneously. The automated checks (lint, test, coverage, build) act as a blocking gate - human review only begins after automation passes. The result is high-confidence merge decisions backed by concrete evidence rather than assumptions.

---

## Changelog

### v1.1.0 (2025-12-19)
- **COGNITIVE LENSING APPLIED**: Added evidential (Turkish) + hierarchical (Japanese) cognitive frames
- **EVIDENTIAL FRAME**: Every finding now requires citation with [file:line], evidence type (DIRECT/STYLE_RULE/BEST_PRACTICE), and reference source
- **HIERARCHICAL FRAME**: Findings organized by severity (SONKEIGO/CRITICAL, TEINEIGO/MAJOR, CASUAL/MINOR, NIT) and scope (ARCHITECTURE, MODULE, FUNCTION, LINE)
- **NEW TEMPLATE**: Added structured Review Finding Template with evidence, reference, severity, scope, and confidence fields
- **REVIEW OUTPUT**: Updated review comment format to display findings hierarchically (critical -> major -> minor -> nits)
- **RATIONALE**: Code review requires evidence-backed findings organized by severity for clear prioritization and actionable feedback

### v1.0.0 (Initial)
- Multi-agent swarm review system with 5 specialized reviewers
- Parallel review execution (security, performance, style, tests, docs)
- Automated fix suggestions with Codex
- Merge readiness assessment with quality gates
- GitHub PR integration via gh CLI