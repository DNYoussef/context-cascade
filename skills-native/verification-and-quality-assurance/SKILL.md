---
name: verification-and-quality-assurance
description: Comprehensive truth scoring, code quality verification, and automatic rollback system with 0.95 accuracy threshold for ensuring high-quality agent outputs and codebase reliability.
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

-----------|---------|----------|
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