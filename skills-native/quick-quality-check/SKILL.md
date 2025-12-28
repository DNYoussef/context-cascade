---
name: quick-quality-check
description: Lightning-fast quality check using parallel command execution. Runs theater detection, linting, security scan, and basic tests in parallel for instant feedback on code quality.
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


# Quick Quality Check

## Purpose

Run a fast, comprehensive quality check on code in under 30 seconds using parallel execution.

## Specialist Agent

I am a quality assurance specialist focused on rapid feedback loops.

**Methodology** (Parallel Execution Pattern):
1. Spawn swarm with optimal topology for speed
2. Execute independent checks in parallel
3. Aggregate results in real-time
4. Provide instant actionable feedback
5. Prioritize findings by severity

**Checks Performed** (parallel):
- Theater detection (mocks, TODOs, placeholders)
- Style audit (linting, formatting)
- Security scan (vulnerabilities, unsafe patterns)
- Basic test execution
- Token usage analysis

**Output**: Unified quality report with severity-ranked issues

## Input Contract

```yaml
input:
  path: string (file or directory path, required)
  parallel: boolean (default: true)
  quick_mode: boolean (skip deep analysis, default: true)
```

## Output Contract

```yaml
output:
  quality_score: number (0-100)
  issues:
    critical: array[issue]
    high: array[issue]
    medium: array[issue]
    low: array[issue]
  execution_time: number (seconds)
  checks_run: array[string]
```

## Execution Flow

```bash
# Initialize swarm for parallel execution
npx claude-flow coordination swarm-init --topology mesh --max-agents 5

# Spawn specialized agents in parallel
npx claude-flow automation auto-agent --task "Quick quality assessment" --strategy optimal

# Execute all checks in parallel
parallel ::: \
  "npx claude-flow theater-detect '$path' --output theater.json" \
  "npx claude-flow style-audit '$path' --quick --output style.json" \
  "npx claude-flow security-scan '$path' --fast --output security.json" \
  "npx claude-flow test-coverage '$path' --quick --output tests.json" \
  "npx claude-flow analysis token-usage --time-range 1h --output tokens.json"

# Aggregate results
npx claude-flow merge-reports theater.json style.json security.json tests.json tokens.json \
  --output quality-report.json \
  --prioritize severity

# Display summary
cat quality-report.json | jq '.summary'
```

## Integration Points

### Cascades
- Part of `/production-readiness` cascade
- Used by `/code-review-assistant` cascade
- Invoked by `/quick-check` command

### Commands
- Combines: `/theater-detect`, `/style-audit`, `/security-scan`, `/test-coverage`, `/token-usage`
- Uses: `/swarm-init`, `/auto-agent`, `/parallel-execute`

### Other Skills
- Input to `deep-code-audit` skill
- Used by `pre-commit-check` skill
- Part of `continuous-quality` skill

## Usage Example

```bash
# Quick check current directory
quick-quality-check .

# Quick check specific file
quick-quality-check src/api/users.js

# Quick check with detailed output
quick-quality-check src/ --detailed
```

## Failure Modes

- **Insufficient resources**: Reduce parallelism, run sequentially
- **Tests failing**: Flag but continue other checks
- **Security issues found**: Escalate to detailed security review
- **Poor quality score**: Trigger `deep-code-audit` skill
-----------|---------|----------|
| **Deep Analysis in Quick Check** | Running comprehensive analysis (full security audit, 100% coverage) instead of quick scan causing 5+ minute delays | Use quick mode flags (--quick, --fast) - deep analysis belongs in pre-commit or CI/CD |
| **Blocking on Non-Critical Issues** | Failing quality check for minor style violations or low-priority warnings | Only fail on critical/high severity - flag medium/low as warnings that don't block |
| **No Prioritization** | Showing all 50+ findings in flat list without ranking | Always sort by severity (critical first) and provide counts (3 critical, 12 high, 35 low) |

## Conclusion

Quick Quality Check provides instant quality feedback (under 30 seconds) by running 5 independent checks in parallel and aggregating results with severity ranking. This enables developers to catch critical issues (theater code, security vulnerabilities, broken builds) before committing, rather than discovering them hours later in CI/CD. The key insight is parallelization - because checks are independent (theater detection doesn't need security scan results), they can run concurrently on separate agents and complete in the time of the slowest check (typically 20-30 seconds).

Use this skill when you need fast quality feedback during active development - before git commit, during code review, or as a pre-push hook. The quick mode skips deep analysis (full coverage reports, comprehensive security audits) in favor of speed, making it suitable for tight feedback loops. For thorough analysis, use the comprehensive code review workflow instead.