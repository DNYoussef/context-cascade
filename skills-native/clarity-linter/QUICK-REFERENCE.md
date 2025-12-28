# Clarity Linter - Quick Reference v2.1.0

## Purpose
Machine-readable code clarity auditing with cognitive load optimization.

## 3-Phase SOP

```
Phase 1: METRICS COLLECTION (code-analyzer)
  |-> Parse AST & control flow
  |-> Measure call chain depth
  |-> Count indirection layers
  |-> Analyze naming quality
  |-> Check comment coverage

Phase 2: RUBRIC EVALUATION (reviewer)
  |-> Apply clarity rubric
  |-> Score each metric
  |-> Identify issues
  |-> Rank by severity

Phase 3: FIX GENERATION (coder + analyst)
  |-> Generate fix suggestions
  |-> Estimate cognitive load reduction
  |-> Prioritize by impact/effort
  |-> Output SARIF report
```

## Clarity Metrics

| Metric | Target | Critical |
|--------|--------|----------|
| Call Chain Depth | <= 3 | > 5 |
| Indirection Layers | <= 2 | > 4 |
| Function Length | <= 25 LOC | > 50 LOC |
| Cyclomatic Complexity | <= 10 | > 20 |
| Naming Score | >= 0.8 | < 0.5 |
| Comment Ratio | 10-20% | < 5% or > 40% |

## Issue Categories

| Category | Description | Priority |
|----------|-------------|----------|
| Thin Helpers | Functions that just wrap another call | Medium |
| Excessive Indirection | Too many abstraction layers | High |
| Deep Call Chains | A calls B calls C calls D... | High |
| Poor Naming | Unclear variable/function names | Medium |
| Missing Comments | Complex logic without explanation | Low |
| Over-Commenting | Obvious code with verbose comments | Low |

## Quick Commands

```bash
# Lint single file
Use clarity-linter on: [file path]

# Lint directory
Use clarity-linter on: [directory path]

# With specific focus
Use clarity-linter focusing on: [call-chains|naming|indirection]
```

## Rubric Reference

Located at: `.artifacts/clarity_rubric.json`

```json
{
  "thin_helpers": {
    "threshold": 1,
    "severity": "medium",
    "description": "Function body is single line call"
  },
  "call_chain_depth": {
    "threshold": 3,
    "severity": "high",
    "description": "Call depth exceeds threshold"
  }
}
```

## SARIF Output Format

```json
{
  "runs": [{
    "tool": { "name": "clarity-linter" },
    "results": [{
      "ruleId": "CLAR-001",
      "level": "warning",
      "message": { "text": "..." },
      "locations": [{ "uri": "file.ts", "line": 42 }]
    }]
  }]
}
```

## Fix Patterns

| Issue | Fix Pattern |
|-------|-------------|
| Thin Helper | Inline the call |
| Deep Chain | Extract intermediate variables |
| Excessive Indirection | Flatten abstractions |
| Poor Naming | Rename with semantic meaning |
| Missing Comments | Add why-not-what comments |

## Cognitive Load Estimation

```
Total Load = sum(
  call_chain_depth * 2.0,
  indirection_layers * 1.5,
  cyclomatic_complexity * 1.0,
  (1 - naming_score) * 1.5
)

Rating:
  0-10:  Low (good)
  11-20: Medium (acceptable)
  21-30: High (needs work)
  30+:   Critical (urgent refactor)
```

## Related Skills

- **connascence-analyzer** - Coupling analysis (complementary)
- **code-review-assistant** - PR review with clarity checks
- **style-audit** - Style consistency (separate concern)
