---
name: verification-and-quality-assurance
description: Comprehensive truth scoring, code quality verification, and automatic rollback system with 0.95 accuracy threshold for ensuring high-quality agent outputs and codebase reliability.
allowed-tools: Read, Glob, Grep, Task, TodoWrite
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


# Verification & Quality Assurance Skill

## What This Skill Does

This skill provides a comprehensive verification and quality assurance system that ensures code quality and correctness through:

- **Truth Scoring**: Real-time reliability metrics (0.0-1.0 scale) for code, agents, and tasks
- **Verification Checks**: Automated code correctness, security, and best practices validation
- **Automatic Rollback**: Instant reversion of changes that fail verification (default threshold: 0.95)
- **Quality Metrics**: Statistical analysis with trends, confidence intervals, and improvement tracking
- **CI/CD Integration**: Export capabilities for continuous integration pipelines
- **Real-time Monitoring**: Live dashboards and watch modes for ongoing verification

## Prerequisites

- Claude Flow installed (`npx claude-flow@alpha`)
- Git repository (for rollback features)
- Node.js 18+ (for dashboard features)

## Quick Start

```bash
# View current truth scores
npx claude-flow@alpha truth

# Run verification check
npx claude-flow@alpha verify check

# Verify specific file with custom threshold
npx claude-flow@alpha verify check --file src/app.js --threshold 0.98

# Rollback last failed verification
npx claude-flow@alpha verify rollback --last-good
```

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


## Complete Guide

### Truth Scoring System

#### View Truth Metrics

Display comprehensive quality and reliability metrics for your codebase and agent tasks.

**Basic Usage:**
```bash
# View current truth scores (default: table format)
npx claude-flow@alpha truth

# View scores for specific time period
npx claude-flow@alpha truth --period 7d

# View scores for specific agent
npx claude-flow@alpha truth --agent coder --period 24h

# Find files/tasks below threshold
npx claude-flow@alpha truth --threshold 0.8
```

**Output Formats:**
```bash
# Table format (default)
npx claude-flow@alpha truth --format table

# JSON for programmatic access
npx claude-flow@alpha truth --format json

# CSV for spreadsheet analysis
npx claude-flow@alpha truth --format csv

# HTML report with visualizations
npx claude-flow@alpha truth --format html --export report.html
```

**Real-time Monitoring:**
```bash
# Watch mode with live updates
npx claude-flow@alpha truth --watch

# Export metrics automatically
npx claude-flow@alpha truth --export .claude-flow/metrics/truth-$(date +%Y%m%d).json
```

#### Truth Score Dashboard

Example dashboard output:
```
📊 Truth Metrics Dashboard
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Overall Truth Score: 0.947 ✅
Trend: ↗️ +2.3% (7d)

Top Performers:
  verification-agent   0.982 ⭐
  code-analyzer       0.971 ⭐
  test-generator      0.958 ✅

Needs Attention:
  refactor-agent      0.821 ⚠️
  docs-generator      0.794 ⚠️

Recent Tasks:
  task-456  0.991 ✅  "Implement auth"
  task-455  0.967 ✅  "Add tests"
  task-454  0.743 ❌  "Refactor API"
```

#### Metrics Explained

**Truth Scores (0.0-1.0):**
- `1.0-0.95`: Excellent ⭐ (production-ready)
- `0.94-0.85`: Good ✅ (acceptable quality)
- `0.84-0.75`: Warning ⚠️ (needs attention)
- `<0.75`: Critical ❌ (requires immediate action)

**Trend Indicators:**
- ↗️ Improving (positive trend)
- → Stable (consistent performance)
- ↘️ Declining (quality regression detected)

**Statistics:**
- **Mean Score**: Average truth score across all measurements
- **Median Score**: Middle value (less affected by outliers)
- **Standard Deviation**: Consistency of scores (lower = more consistent)
- **Confidence Interval**: Statistical reliability of measurements

### Verification Checks

#### Run Verification

Execute comprehensive verification checks on code, tasks, or agent outputs.

**File Verification:**
```bash
# Verify single file
npx claude-flow@alpha verify check --file src/app.js

# Verify directory recursively
npx claude-flow@alpha verify check --directory src/

# Verify with auto-fix enabled
npx claude-flow@alpha verify check --file src/utils.js --auto-fix

# Verify current working directory
npx claude-flow@alpha verify check
```

**Task Verification:**
```bash
# Verify specific task output
npx claude-flow@alpha verify check --task task-123

# Verify with custom threshold
npx claude-flow@alpha verify check --task task-456 --threshold 0.99

# Verbose output for debugging
npx claude-flow@alpha verify check --task task-789 --verbose
```

**Batch Verification:**
```bash
# Verify multiple files in parallel
npx claude-flow@alpha verify batch --files "*.js" --parallel

# Verify with pattern matching
npx claude-flow@alpha verify batch --pattern "src/**/*.ts"

# Integration test suite
npx claude-flow@alpha verify integration --test-suite full
```

#### Verification Criteria

The verification system evaluates:

1. **Code Correctness**
   - Syntax validation
   - Type checking (TypeScript)
   - Logic flow analysis
   - Error handling completeness

2. **Best Practices**
   - Code style adherence
   - SOLID principles
   - Design patterns usage
   - Modularity and reusability

3. **Security**
   - Vulnerability scanning
   - Secret detection
   - Input validation
   - Authentication/authorization checks

4. **Performance**
   - Algorithmic complexity
   - Memory usage patterns
   - Database query optimization
   - Bundle size impact

5. **Documentation**
   - JSDoc/TypeDoc completeness
   - README accuracy
   - API documentation
   - Code comments quality

#### JSON Output for CI/CD

```bash
# Get structured JSON output
npx claude-flow@alpha verify check --json > verification.json

# Example JSON structure:
{
  "overallScore": 0.947,
  "passed": true,
  "threshold": 0.95,
  "checks": [
    {
      "name": "code-correctness",
      "score": 0.98,
      "passed": true
    },
    {
      "name": "security",
      "score": 0.91,
      "passed": false,
      "issues": [...]
    }
  ]
}
```

### Automatic Rollback

#### Rollback Failed Changes

Automatically revert changes that fail verification checks.

**Basic Rollback:**
```bash
# Rollback to last known good state
npx claude-flow@alpha verify rollback --last-good

# Rollback to specific commit
npx claude-flow@alpha verify rollback --to-commit abc123

# Interactive rollback with preview
npx claude-flow@alpha verify rollback --interactive
```

**Smart Rollback:**
```bash
# Rollback only failed files (preserve good changes)
npx claude-flow@alpha verify rollback --selective

# Rollback with automatic backup
npx claude-flow@alpha verify rollback --backup-first

# Dry-run mode (preview without executing)
npx claude-flow@alpha verify rollback --dry-run
```

**Rollback Performance:**
- Git-based rollback: <1 second
- Selective file rollback: <500ms
- Backup creation: Automatic before rollback

### Verification Reports

#### Generate Reports

Create detailed verification reports with metrics and visualizations.

**Report Formats:**
```bash
# JSON report
npx claude-flow@alpha verify report --format json

# HTML report with charts
npx claude-flow@alpha verify report --export metrics.html --format html

# CSV for data analysis
npx claude-flow@alpha verify report --format csv --export metrics.csv

# Markdown summary
npx claude-flow@alpha verify report --format markdown
```

**Time-based Reports:**
```bash
# Last 24 hours
npx claude-flow@alpha verify report --period 24h

# Last 7 days
npx claude-flow@alpha verify report --period 7d

# Last 30 days with trends
npx claude-flow@alpha verify report --period 30d --include-trends

# Custom date range
npx claude-flow@alpha verify report --from 2025-01-01 --to 2025-01-31
```

**Report Content:**
- Overall truth scores
- Per-agent performance metrics
- Task completion quality
- Verification pass/fail rates
- Rollback frequency
- Quality improvement trends
- Statistical confidence intervals

### Interactive Dashboard

#### Launch Dashboard

Run interactive web-based verification dashboard with real-time updates.

```bash
# Launch dashboard on default port (3000)
npx claude-flow@alpha verify dashboard

# Custom port
npx claude-flow@alpha verify dashboard --port 8080

# Export dashboard data
npx claude-flow@alpha verify dashboard --export

# Dashboard with auto-refresh
npx claude-flow@alpha verify dashboard --refresh 5s
```

**Dashboard Features:**
- Real-time truth score updates (WebSocket)
- Interactive charts and graphs
- Agent performance comparison
- Task history timeline
- Rollback history viewer
- Export to PDF/HTML
- Filter by time period/agent/score

### Configuration

#### Default Configuration

Set verification preferences in `.claude-flow/config.json`:

```json
{
  "verification": {
    "threshold": 0.95,
    "autoRollback": true,
    "gitIntegration": true,
    "hooks": {
      "preCommit": true,
      "preTask": true,
      "postEdit": true
    },
    "checks": {
      "codeCorrectness": true,
      "security": true,
      "performance": true,
      "documentation": true,
      "bestPractices": true
    }
  },
  "truth": {
    "defaultFormat": "table",
    "defaultPeriod": "24h",
    "warningThreshold": 0.85,
    "criticalThreshold": 0.75,
    "autoExport": {
      "enabled": true,
      "path": ".claude-flow/metrics/truth-daily.json"
    }
  }
}
```

#### Threshold Configuration

**Adjust verification strictness:**
```bash
# Strict mode (99% accuracy required)
npx claude-flow@alpha verify check --threshold 0.99

# Lenient mode (90% acceptable)
npx claude-flow@alpha verify check --threshold 0.90

# Set default threshold
npx claude-flow@alpha config set verification.threshold 0.98
```

**Per-environment thresholds:**
```json
{
  "verification": {
    "thresholds": {
      "production": 0.99,
      "staging": 0.95,
      "development": 0.90
    }
  }
}
```

### Integration Examples

#### CI/CD Integration

**GitHub Actions:**
```yaml
name: Quality Verification

on: [push, pull_request]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install Dependencies
        run: npm install

      - name: Run Verification
        run: |
          npx claude-flow@alpha verify check --json > verification.json

      - name: Check Truth Score
        run: |
          score=$(jq '.overallScore' verification.json)
          if (( $(echo "$score < 0.95" | bc -l) )); then
            echo "Truth score too low: $score"
            exit 1
          fi

      - name: Upload Report
        uses: actions/upload-artifact@v3
        with:
          name: verification-report
          path: verification.json
```

**GitLab CI:**
```yaml
verify:
  stage: test
  script:
    - npx claude-flow@alpha verify check --threshold 0.95 --json > verification.json
    - |
      score=$(jq '.overallScore' verification.json)
      if [ $(echo "$score < 0.95" | bc) -eq 1 ]; then
        echo "Verification failed with score: $score"
        exit 1
      fi
  artifacts:
    paths:
      - verification.json
    reports:
      junit: verification.json
```

#### Swarm Integration

Run verification automatically during swarm operations:

```bash
# Swarm with verification enabled
npx claude-flow@alpha swarm --verify --threshold 0.98

# Hive Mind with auto-rollback
npx claude-flow@alpha hive-mind --verify --rollback-on-fail

# Training pipeline with verification
npx claude-flow@alpha train --verify --threshold 0.99
```

#### Pair Programming Integration

Enable real-time verification during collaborative development:

```bash
# Pair with verification
npx claude-flow@alpha pair --verify --real-time

# Pair with custom threshold
npx claude-flow@alpha pair --verify --threshold 0.97 --auto-fix
```

### Advanced Workflows

#### Continuous Verification

Monitor codebase continuously during development:

```bash
# Watch directory for changes
npx claude-flow@alpha verify watch --directory src/

# Watch with auto-fix
npx claude-flow@alpha verify watch --directory src/ --auto-fix

# Watch with notifications
npx claude-flow@alpha verify watch --notify --threshold 0.95
```

#### Monitoring Integration

Send metrics to external monitoring systems:

```bash
# Export to Prometheus
npx claude-flow@alpha truth --format json | \
  curl -X POST https://pushgateway.example.com/metrics/job/claude-flow \
  -d @-

# Send to DataDog
npx claude-flow@alpha verify report --format json | \
  curl -X POST "https://api.datadoghq.com/api/v1/series?api_key=${DD_API_KEY}" \
  -H "Content-Type: application/json" \
  -d @-

# Custom webhook
npx claude-flow@alpha truth --format json | \
  curl -X POST https://metrics.example.com/api/truth \
  -H "Content-Type: application/json" \
  -d @-
```

#### Pre-commit Hooks

Automatically verify before commits:

```bash
# Install pre-commit hook
npx claude-flow@alpha verify install-hook --pre-commit

# .git/hooks/pre-commit example:
#!/bin/bash
npx claude-flow@alpha verify check --threshold 0.95 --json > /tmp/verify.json

score=$(jq '.overallScore' /tmp/verify.json)
if (( $(echo "$score < 0.95" | bc -l) )); then
  echo "❌ Verification failed with score: $score"
  echo "Run 'npx claude-flow@alpha verify check --verbose' for details"
  exit 1
fi

echo "✅ Verification passed with score: $score"
```

### Performance Metrics

**Verification Speed:**
- Single file check: <100ms
- Directory scan: <500ms (per 100 files)
- Full codebase analysis: <5s (typical project)
- Truth score calculation: <50ms

**Rollback Speed:**
- Git-based rollback: <1s
- Selective file rollback: <500ms
- Backup creation: <2s

**Dashboard Performance:**
- Initial load: <1s
- Real-time updates: <100ms latency (WebSocket)
- Chart rendering: 60 FPS

### Troubleshooting

#### Common Issues

**Low Truth Scores:**
```bash
# Get detailed breakdown
npx claude-flow@alpha truth --verbose --threshold 0.0

# Check specific criteria
npx claude-flow@alpha verify check --verbose

# View agent-specific issues
npx claude-flow@alpha truth --agent <agent-name> --format json
```

**Rollback Failures:**
```bash
# Check git status
git status

# View rollback history
npx claude-flow@alpha verify rollback --history

# Manual rollback
git reset --hard HEAD~1
```

**Verification Timeouts:**
```bash
# Increase timeout
npx claude-flow@alpha verify check --timeout 60s

# Verify in batches
npx claude-flow@alpha verify batch --batch-size 10
```

### Exit Codes

Verification commands return standard exit codes:

- `0`: Verification passed (score ≥ threshold)
- `1`: Verification failed (score < threshold)
- `2`: Error during verification (invalid input, system error)

### Related Commands

- `npx claude-flow@alpha pair` - Collaborative development with verification
- `npx claude-flow@alpha train` - Training with verification feedback
- `npx claude-flow@alpha swarm` - Multi-agent coordination with quality checks
- `npx claude-flow@alpha report` - Generate comprehensive project reports

### Best Practices

1. **Set Appropriate Thresholds**: Use 0.99 for critical code, 0.95 for standard, 0.90 for experimental
2. **Enable Auto-rollback**: Prevent bad code from persisting
3. **Monitor Trends**: Track improvement over time, not just current scores
4. **Integrate with CI/CD**: Make verification part of your pipeline
5. **Use Watch Mode**: Get immediate feedback during development
6. **Export Metrics**: Track quality metrics in your monitoring system
7. **Review Rollbacks**: Understand why changes were rejected
8. **Train Agents**: Use verification feedback to improve agent performance

### Additional Resources

- Truth Scoring Algorithm: See `/docs/truth-scoring.md`
- Verification Criteria: See `/docs/verification-criteria.md`
- Integration Examples: See `/examples/verification/`
- API Reference: See `/docs/api/verification.md`
## Core Principles

Verification and Quality Assurance operates on 3 fundamental principles:

### Principle 1: Quantified Quality Through Truth Scoring
Quality is measurable through statistical reliability metrics that provide objective assessment of code correctness and agent performance.

In practice:
- Truth scores (0.0-1.0 scale) quantify code quality, agent reliability, and task completion accuracy
- Multiple verification perspectives (static analysis, dynamic testing, security scanning) contribute to composite scores
- Statistical confidence intervals indicate reliability of measurements rather than single-point estimates
- Trend analysis tracks quality improvement or degradation over time, not just current state

### Principle 2: Automated Quality Gates with Instant Rollback
Quality thresholds should be enforced automatically with immediate reversion of changes that fail verification rather than allowing bad code to persist.

In practice:
- Default 0.95 truth score threshold blocks merges of code below quality standards
- Git-based rollback (<1 second) instantly reverts failed changes to last known good state
- Selective rollback preserves good changes while reverting only failed files
- Pre-commit hooks prevent low-quality code from entering version control

### Principle 3: Continuous Quality Monitoring with Real-Time Feedback
Quality verification is not a one-time gate but a continuous process providing real-time feedback during development.

In practice:
- Watch mode monitors directories for changes and runs verification automatically
- Live dashboards display truth scores, verification status, and quality trends with WebSocket updates
- Integration with CI/CD pipelines ensures every commit undergoes comprehensive verification
- Export capabilities send metrics to external monitoring systems for alerting and long-term trend analysis

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Manual-Only Verification** | Relying on developers to remember to run verification checks before committing | Install pre-commit hooks that automatically verify changes; integrate verification into CI/CD pipeline |
| **Ignoring Low Scores** | Seeing truth scores below threshold but merging anyway due to deadlines or "it looks fine" | Enforce quality gates strictly; use automatic rollback for failed verification; track exceptions with explicit justification |
| **One-Dimensional Quality Metrics** | Focusing only on test coverage or only on linting while ignoring security, performance, or documentation | Use comprehensive verification criteria covering correctness, security, performance, best practices, and documentation |
| **Late-Stage Verification** | Running verification only at PR submission, creating merge delays and context loss | Enable watch mode during development for immediate feedback; run verification continuously, not just at checkpoints |
| **Ignoring Quality Trends** | Focusing only on current scores without noticing gradual quality degradation | Track trends over time; set alerts for declining quality metrics; review quality reports regularly |
| **Overly Lenient Thresholds** | Setting thresholds too low (e.g., 0.75) allowing low-quality code to pass | Use strict thresholds (0.95-0.99) for production code; adjust thresholds based on criticality and risk tolerance |

## Conclusion

Verification and Quality Assurance with truth scoring and automatic rollback transforms code quality from a subjective judgment into an objective, measurable, and enforceable standard. By quantifying quality through statistical reliability metrics and automatically blocking or reverting changes that fall below thresholds, this skill ensures that only high-quality code enters the codebase while providing developers with clear, actionable feedback for improvement.

Use this skill as a continuous quality monitoring system throughout the development lifecycle, not just at release gates. The combination of truth scoring for quantified quality assessment, comprehensive verification checks across multiple dimensions, and instant rollback for failed changes creates a safety net that catches quality issues early while maintaining development velocity. The real-time feedback through watch mode and live dashboards enables developers to fix issues immediately rather than discovering them days later during code review.

The integration with CI/CD pipelines, pre-commit hooks, and external monitoring systems means verification becomes an automatic part of the development workflow rather than a manual step that gets skipped under pressure. When combined with functionality-audit for execution verification, theater-detection for placeholder elimination, and code-review for human oversight, this skill completes a comprehensive quality ecosystem that delivers production-ready code with measurable confidence in its correctness, security, and reliability.