---
name: testing-quality
description: Testing quality assessment for test suite health, coverage analysis, and test effectiveness. Use when auditing test quality, improving test coverage, or assessing test reliability and maintainability. --- # Testing Quality Assessment and improvement of test suite quality, coverage, and effectiveness. ## Phase 0: Expertise Loading ```yaml
---

# Testing Quality

Assessment and improvement of test suite quality, coverage, and effectiveness.

## Phase 0: Expertise Loading

```yaml
expertise_check:
  domain: testing-quality
  file: .claude/expertise/testing-quality.yaml

  if_exists:
    - Load quality metrics
    - Load coverage thresholds
    - Apply assessment criteria

  if_not_exists:
    - Flag discovery mode
    - Document patterns learned
```

## When to Use This Skill

Use testing-quality when:
- Auditing test suite health
- Analyzing test coverage gaps
- Assessing test reliability
- Improving test maintainability
- Identifying flaky tests

## Quality Dimensions

| Dimension | Metrics |
|-----------|---------|
| Coverage | Line, branch, function |
| Reliability | Flake rate, consistency |
| Speed | Execution time, parallelization |
| Maintainability | Complexity, duplication |

## Quality Metrics

### Coverage Analysis
```yaml
metrics:
  line_coverage: ">= 80%"
  branch_coverage: ">= 75%"
  function_coverage: ">= 80%"
  critical_path_coverage: "100%"
```

### Test Health
```yaml
metrics:
  flaky_test_rate: "< 1%"
  test_execution_time: "< 5 min"
  test_to_code_ratio: ">= 1:1"
  assertion_density: ">= 2 per test"
```

## Anti-Patterns

```yaml
anti_patterns:
  - Flaky tests (non-deterministic)
  - Test interdependence
  - Over-mocking
  - Missing assertions
  - Slow tests in CI
  - Commented-out tests
```

## MCP Requirements

- **claude-flow**: For orchestration
- **Bash**: For coverage tools

## Recursive Improvement Integration (v2.1)

### Eval Harness Integration

```yaml
benchmark: testing-quality-benchmark-v1
  tests:
    - tq-001: Coverage analysis accuracy
    - tq-002: Anti-pattern detection
  minimum_scores:
    analysis_accuracy: 0.90
    detection_rate: 0.85
```

### Memory Namespace

```yaml
namespaces:
  - testing-quality/audits/{id}: Quality audits
  - testing-quality/metrics: Health metrics
  - improvement/audits/testing-quality: Skill audits
```

### Uncertainty Handling

```yaml
confidence_check:
  if confidence >= 0.8:
    - Proceed with assessment
  if confidence 0.5-0.8:
    - Confirm scope
  if confidence < 0.5:
    - Ask for test suite details
```

### Cross-Skill Coordination

Works with: **testing**, **code-review-assistant**, **functionality-audit**

-----------|---------|----------|
| **Coverage Theater** | High coverage percentage from tests that execute code but don't validate behavior (missing assertions) | Measure assertion density (>= 2 per test); review tests for meaningful validations; require tests to fail when code is broken |
| **Flaky Test Tolerance** | Accepting non-deterministic tests and re-running until they pass rather than fixing root causes | Enforce <1% flaky rate; investigate any flakiness immediately; isolate tests to eliminate interdependence |
| **Over-Mocking** | Tests that mock everything and validate only that mocks are called, not actual behavior | Use mocks sparingly for external dependencies only; test real integrations in sandboxes; validate outputs not just call counts |
| **Slow Test Accumulation** | Test suite execution time growing unbounded as tests are added without optimization | Set execution time budgets (<5 min); parallelize tests; identify and optimize slow tests; separate unit from integration |
| **Test Interdependence** | Tests that must run in specific order or share state, making them fragile and hard to debug | Ensure tests can run independently in any order; use test fixtures for setup; clean up state after each test |
| **Commented-Out Tests** | Disabling failing tests rather than fixing them or the code they validate | Never allow commented tests in codebase; either fix test/code or delete test entirely; track test deletions with justification |

## Conclusion

Testing Quality assessment provides systematic evaluation of test suite health beyond simple coverage metrics, examining reliability, speed, maintainability, and effectiveness. By measuring test quality across multiple dimensions and identifying anti-patterns like flakiness, over-mocking, and slow execution, this skill helps teams build test suites that actually catch bugs and provide confidence in code correctness rather than creating false security through coverage theater.

Use this skill when auditing test suite health as part of quality initiatives, when analyzing why tests are being skipped or ignored due to flakiness or slow execution, when test coverage numbers are high but bugs still reach production, or when improving test maintainability to reduce technical debt. The skill is essential for establishing trust in automated testing and ensuring that test investments deliver real value through early bug detection rather than just checking a coverage box.

The multi-dimensional assessment - coverage analysis, reliability metrics, speed optimization, and maintainability evaluation - creates a comprehensive view of test suite quality that guides targeted improvements. The identification of specific anti-patterns (flaky tests, over-mocking, interdependence) with concrete metrics enables prioritized remediation rather than vague calls for "better testing." When combined with functionality-audit for execution verification and verification-quality for quality gates, testing-quality ensures that test suites are not just comprehensive but genuinely effective at preventing defects from reaching production.

## Core Principles

1. **Multi-Dimensional Assessment** - Test quality cannot be measured by coverage alone. Evaluate across coverage, reliability, speed, and maintainability dimensions for comprehensive quality understanding.

2. **Evidence-Based Metrics** - Use quantitative thresholds (80% line coverage, <1% flake rate, <5 min execution) validated through static and dynamic analysis rather than subjective assessment.

3. **Continuous Improvement Loop** - Quality assessment feeds the dogfooding system for self-improvement. Patterns detected in test suite health inform better testing practices across the codebase.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|--------------|-----------------|
| **Coverage Theater** - Achieving high coverage percentage without testing meaningful scenarios | Coverage number becomes vanity metric, critical paths remain untested, false confidence in quality | Focus on critical path coverage (100%), verify assertions test actual behavior, use branch coverage not just line coverage |
| **Ignoring Flaky Tests** - Tolerating non-deterministic test failures | Developers ignore CI failures, real bugs get missed, trust in automation erodes | Track flake rate (<1% threshold), quarantine flaky tests, fix or delete them, never merge with flaky tests |
| **Test Code Neglect** - Treating test code as second-class citizen without quality standards | Unmaintainable test suite, high duplication, unclear test intent, hard to debug failures | Apply same quality standards to test code, refactor test helpers, document test patterns, review test code rigorously |

## Conclusion

The testing quality skill enables systematic assessment of test suite health across multiple dimensions beyond simple coverage metrics. By evaluating coverage adequacy, test reliability, execution speed, and code maintainability, teams gain comprehensive understanding of their testing effectiveness. The integration with the recursive improvement system ensures quality assessments feed continuous self-improvement through the dogfooding cycle, creating a feedback loop that elevates testing practices organization-wide.

Effective quality assessment requires looking beyond vanity metrics to evidence-based evaluation of what tests actually validate. Avoiding anti-patterns like coverage theater or tolerating flaky tests ensures the test suite provides genuine confidence rather than false assurance. By maintaining quality standards for test code itself and continuously improving through the assessment-feedback-improvement loop, teams build test suites that catch bugs reliably, execute quickly, and remain maintainable as codebases evolve. This systematic approach transforms testing from a compliance exercise into a strategic quality advantage.