# Meta-Loop Multi-Model Integration

## Overview

This document describes how the Ralph Wiggum Multi-Model persistence loop integrates with the recursive improvement meta-loop system.

## Architecture

```
META-LOOP RECURSIVE IMPROVEMENT PIPELINE
========================================

              +---> PROMPT FORGE (Meta-Prompt)
              |          |
              |          v
FOUNDRY ------+---> SKILL FORGE (Meta-Skill) <-- Ralph Multi-Model
              |          |                            |
              |          v                            |
              +---> AGENT CREATOR                     |
                         |                            |
                         v                            |
                 AUDITOR AGENTS (4 types) <-----------+
                         |
                         v
    +--------------------+--------------------+
    |                    |                    |
    v                    v                    v
PROMPT-AUDITOR    SKILL-AUDITOR    EXPERTISE-AUDITOR
    |                    |                    |
    v                    v                    v
    +--------------------+--------------------+
                         |
                         v
              IMPROVEMENT PROPOSAL
                         |
                         v
    ==========================================
    |     EVAL HARNESS (FROZEN - NEVER       |
    |         SELF-IMPROVES)                  |
    ==========================================
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
    BENCHMARK        REGRESSION       HUMAN GATES
    TESTS            TESTS
        |                |                |
        +----------------+----------------+
                         |
                         v
                 COMPARE BASELINE
                         |
            +------------+------------+
            |                         |
            v                         v
        ACCEPT                    REJECT
            |                         |
            v                         v
        COMMIT                   LOG FAILURE
            |
            v
        MONITOR (7 days)
            |
            v
    ROLLBACK if regression
```

## Ralph Multi-Model Integration Points

### 1. PROPOSE Phase (Auditor-Driven)

When auditors detect issues, Ralph Multi-Model can be used for implementation:

```yaml
integration_point: PROPOSE
trigger: Auditor detects improvement opportunity
action: |
  ralph-multimodel.sh "
    Implement improvement proposal:
    - Target: {target_file}
    - Change: {proposed_change}
    - Rationale: {rationale}
    Output <promise>IMPLEMENTED</promise> when done
  "
routing:
  - If research needed: Gemini (search, megacontext)
  - If code generation: Claude or Codex
  - If testing needed: Codex (full-auto)
```

### 2. TEST Phase (Eval Harness)

Ralph Multi-Model runs tests using Codex for autonomous iteration:

```yaml
integration_point: TEST
trigger: Implementation complete
action: |
  CODEX_MODE=full-auto ralph-multimodel.sh "
    Run eval harness tests:
    - Benchmark suite: {benchmark_id}
    - Regression tests: {regression_suite}
    Fix any failures automatically
    Output <promise>ALL_TESTS_PASS</promise>
  "
routing:
  - Test execution: Codex (full-auto with iteration)
  - Failure analysis: Claude (reasoning)
  - Fix generation: Codex (yolo)
```

### 3. COMPARE Phase (Baseline Comparison)

Use LLM Council for consensus on improvement quality:

```yaml
integration_point: COMPARE
trigger: Tests pass
action: |
  USE_COUNCIL=true ralph-multimodel.sh "
    Compare baseline vs candidate:
    - Baseline metrics: {baseline}
    - Candidate metrics: {candidate}
    - Provide consensus recommendation
    Output <promise>VERDICT:{ACCEPT|REJECT}</promise>
  "
routing:
  - Analysis: Gemini (megacontext for full comparison)
  - Consensus: LLM Council
```

### 4. MONITOR Phase (7-Day Window)

Use Gemini for real-time monitoring alerts:

```yaml
integration_point: MONITOR
trigger: Commit accepted
duration: 7 days
action: |
  ralph-multimodel.sh "
    Monitor deployed change:
    - Search for error reports (Gemini search)
    - Analyze metrics trend
    - Alert if regression detected
    Output <promise>MONITOR_COMPLETE</promise> after 7 days
  "
routing:
  - Real-time search: Gemini
  - Metrics analysis: Claude
  - Alert generation: Claude
```

## Model Selection Matrix for Meta-Loop

| Meta-Loop Phase | Primary Model | Fallback | Rationale |
|-----------------|---------------|----------|-----------|
| Auditor Analysis | Claude | Gemini | Deep reasoning needed |
| Proposal Generation | Claude | - | Complex multi-step |
| Implementation | Codex (yolo) | Claude | Autonomous iteration |
| Test Execution | Codex (full-auto) | Claude | Test-fix loops |
| Test Fixing | Codex (full-auto) | Claude | Autonomous fixes |
| Baseline Comparison | Gemini (megacontext) | Claude | Full codebase view |
| Consensus Decision | LLM Council | Claude | Multi-perspective |
| Monitoring | Gemini (search) | Claude | Real-time info |
| Rollback | Claude | - | Critical operation |

## Configuration

### Environment Variables

```bash
# Meta-loop + Ralph integration
export META_LOOP_USE_RALPH=true
export RALPH_MAX_ITERATIONS=50
export RALPH_COMPLETION_PROMISE="PHASE_COMPLETE"
export USE_COUNCIL_FOR_DECISIONS=true
export CODEX_MODE_DEFAULT=full-auto
```

### Hook Integration

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "bash .claude/hooks/multi-model/model-router-pretool.sh \"$TOOL_NAME\" \"$TOOL_INPUT\""
      }
    ],
    "meta-loop-propose": [
      {
        "type": "command",
        "command": "bash scripts/multi-model/ralph-multimodel.sh \"$PROPOSAL\""
      }
    ]
  }
}
```

## Memory Namespace Integration

```yaml
namespaces:
  meta-loop:
    proposals/{id}:
      description: Improvement proposals
      ralph_integration: true

    implementations/{id}:
      description: Ralph execution results
      source: multi-model/codex/yolo/*

    test-results/{id}:
      description: Eval harness results
      source: multi-model/codex/audit/*

    comparisons/{id}:
      description: Baseline vs candidate
      source: multi-model/council/decisions/*

    monitoring/{id}:
      description: 7-day monitoring data
      source: multi-model/gemini/search/*
```

## Workflow Example

### Complete Meta-Loop Cycle with Ralph Multi-Model

```bash
# 1. Auditor detects issue
prompt-auditor.sh analyze skill-forge/SKILL.md
# Output: Proposal to improve error handling

# 2. Ralph implements with multi-model routing
ralph-multimodel.sh "
  Implement proposal:
  - Add error handling to skill-forge
  - Research best practices (Gemini)
  - Implement changes (Codex yolo)
  - Run tests until pass (Codex full-auto)
  Output <promise>IMPLEMENTED</promise>
"

# 3. Eval harness tests
CODEX_MODE=full-auto ralph-multimodel.sh "
  Run eval harness:
  - skill-generation-benchmark-v1
  - skill-forge-regression-v1
  Output <promise>TESTS_PASS</promise>
"

# 4. Compare with council consensus
USE_COUNCIL=true ralph-multimodel.sh "
  Compare metrics:
  - Before: success_rate=0.85
  - After: success_rate=0.90
  Provide consensus verdict
  Output <promise>VERDICT:ACCEPT</promise>
"

# 5. Commit if accepted
git add -A && git commit -m "Improve skill-forge error handling (+5% success rate)"

# 6. Monitor for 7 days
ralph-multimodel.sh "
  Monitor deployment:
  - Check error logs daily (Gemini search)
  - Compare metrics to baseline
  - Alert if regression
  Output <promise>MONITOR_COMPLETE</promise>
"
```

## Safety Constraints

1. **Eval Harness Never Self-Improves**: Ralph cannot modify eval harness
2. **Human Gates**: Council decisions flagged for human review if confidence < 0.80
3. **Rollback Always Available**: 90-day archive of previous versions
4. **Codex Sandbox for Risky Changes**: Use `CODEX_MODE=sandbox` for experimental improvements

## Metrics Tracked

| Metric | Target | Source |
|--------|--------|--------|
| Improvement acceptance rate | >60% | meta-loop/comparisons |
| Ralph completion rate | >90% | ralph-wiggum/loop-state |
| Model routing accuracy | >85% | multi-model/routing-state |
| Test auto-fix success | >80% | multi-model/codex/audit |
| Council consensus rate | >75% | multi-model/council/decisions |
