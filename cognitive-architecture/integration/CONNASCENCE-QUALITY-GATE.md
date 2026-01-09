# Connascence Quality Gate Integration

## Overview

The Connascence Analyzer (7-Analyzer Suite) is available as an MCP server for quality validation within the cognitive architecture.

## MCP Server Status

**Enabled**: Yes (in `~/.claude/settings.local.json`)
**Location**: `D:\Projects\connascence`

## The 7 Core Analyzers

| # | Analyzer | Purpose | Key Metrics |
|---|----------|---------|-------------|
| 1 | Connascence | 9 coupling types detection | CoN/CoT/CoM/CoP/CoA/CoE/CoT2/CoV/CoI |
| 2 | NASA Safety | Power of 10 rules compliance | 10 rules, >95% required |
| 3 | MECE | Duplication detection | >80% uniqueness threshold |
| 4 | Clarity Linter | Cognitive load analysis | Complexity metrics |
| 5 | Six Sigma | Quality metrics | DPMO <6210, Sigma >=4.0 |
| 6 | Theater Detection | Fake quality prevention | <20% theater risk |
| 7 | Safety Violations | God objects, parameter bombs | 0 critical violations |

## Integration with FrozenHarness

### Current Architecture

```
FrozenHarness.grade(artifact_path)
    |
    v
[CLI Evaluator] OR [Heuristics]
    |
    v
{task_accuracy, token_efficiency, edge_robustness, epistemic_consistency}
```

### Extended Architecture (with Connascence)

```
FrozenHarness.grade(artifact_path)
    |
    v
[CLI Evaluator] OR [Heuristics]
    |
    v
{metrics}
    |
    +---> [Optional: Connascence MCP Call]
    |          |
    |          v
    |     {connascence_score, nasa_compliance, theater_risk}
    |
    v
{combined_metrics}
```

## Invocation via MCP

When connascence-analyzer MCP is available, use tools:
- `connascence_analyze_file` - Analyze a single file
- `connascence_analyze_directory` - Analyze directory
- `connascence_get_sarif` - Get SARIF-format report

## Quality Thresholds

| Metric | Pass Threshold | Action if Failed |
|--------|----------------|------------------|
| Sigma Level | >= 4.0 | Block/Escalate |
| DPMO | <= 6,210 | Warning |
| NASA Compliance | >= 95% | Block/Escalate |
| MECE Score | >= 80% | Warning |
| Theater Risk | < 20% | Block/Escalate |
| Critical Violations | 0 | Block |

## Integration Points

### 1. Loop 2 Quality Validation

In `ralph_iteration_complete()`, after harness grading:

```python
# Optional connascence analysis
if policy.get("connascence_enabled", False):
    from integration.connascence_bridge import analyze_artifact
    connascence_result = analyze_artifact(artifact_path)
    harness_metrics["connascence"] = connascence_result
```

### 2. Pre-Merge Quality Gate

Before merging optimization changes:

```bash
# Use claude-dev-cli quality gate
claude-dev quality gate src/ --strict
```

### 3. Session Reflection

In `/reflect` skill, capture quality metrics:

```python
# Store quality metrics in session learnings
learning = {
    "signal_type": "quality_check",
    "metrics": {
        "sigma_level": 4.2,
        "theater_risk": 0.12,
        "nasa_compliance": 0.98
    }
}
```

## Memory MCP Storage Format

```json
{
  "WHO": "connascence-analyzer:quality-gate",
  "WHEN": "2026-01-09T12:00:00Z",
  "PROJECT": "cognitive-architecture",
  "WHY": "quality-validation",
  "x-analyzer": "connascence",
  "x-sigma-level": "4.2",
  "x-theater-risk": "0.12",
  "x-nasa-compliance": "0.98",
  "x-violations-count": "3"
}
```

## CLI Commands

```bash
# Full analysis
claude-dev quality analyze cognitive-architecture/ --profile strict

# Six Sigma report
claude-dev quality sigma cognitive-architecture/

# Theater detection only
claude-dev quality violations cognitive-architecture/ --analyzer theater

# Quality gate for CI/CD
claude-dev quality gate cognitive-architecture/ --strict && echo "PASS" || echo "FAIL"
```

## Status

- [x] Connascence MCP server exists and is enabled
- [x] Quality metrics defined (Six Sigma thresholds)
- [x] Storage format documented (WHO/WHEN/PROJECT/WHY)
- [x] CLI integration available via claude-dev-cli
- [ ] Optional: Deep FrozenHarness integration (deferred - adds coupling)

## Notes

The connascence analyzer is intentionally kept as a separate MCP server rather than deeply integrated into FrozenHarness. This maintains:

1. **Separation of Concerns** - Evaluation vs. quality analysis
2. **Modularity** - Can disable/enable independently
3. **Performance** - Optional analysis only when needed
4. **Flexibility** - Can use different analyzers for different projects
