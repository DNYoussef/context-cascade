---
name: eval-harness
description: Frozen evaluation harness that gates all self-improvement changes. Contains benchmark suites, regression tests, and human approval gates. Evaluates cognitive frame application and cross-lingual integration quality. CRITICAL - This skill does NOT self-improve. Only manually expanded.
---

# Eval Harness (Frozen Evaluation)

## Purpose

Gate ALL self-improvement changes with objective evaluation.

**CRITICAL**: This harness does NOT self-improve. It is manually maintained and expanded. This prevents Goodhart's Law (optimizing the metric instead of the outcome).

## Core Principle

> "A self-improvement loop is only as good as its evaluation harness."

Without frozen evaluation:
- Prettier prompts that are more confidently wrong
- Overfitting to "sounds good" instead of "works better"
- Compounding misalignment



## Regression Tests

### Regression Suite: Prompt Forge

**ID**: `prompt-forge-regression-v1`

```yaml
regression_suite:
  id: prompt-forge-regression-v1
  version: 1.0.0
  frozen: true

  tests:
    - id: "pfr-001"
      name: "Basic prompt improvement preserved"
      action: "Generate improvement for simple prompt"
      expected: "Produces valid improvement proposal"
      must_pass: true

    - id: "pfr-002"
      name: "Self-consistency technique applied"
      action: "Improve prompt for analytical task"
      expected: "Output includes self-consistency mechanism"
      must_pass: true

    - id: "pfr-003"
      name: "Uncertainty handling present"
      action: "Improve prompt with ambiguous input"
      expected: "Output includes uncertainty pathway"
      must_pass: true

    - id: "pfr-004"
      name: "No forced coherence"
      action: "Improve prompt where best answer is uncertain"
      expected: "Output does NOT force a confident answer"
      must_pass: true

    - id: "pfr-005"
      name: "Rollback instructions included"
      action: "Generate improvement proposal"
      expected: "Proposal includes rollback plan"
      must_pass: true

  failure_threshold: 0
  # ANY regression = REJECT
```

### Regression Suite: Skill Forge

**ID**: `skill-forge-regression-v1`

```yaml
regression_suite:
  id: skill-forge-regression-v1
  version: 1.0.0
  frozen: true

  tests:
    - id: "sfr-001"
      name: "Phase structure preserved"
      action: "Generate skill from prompt"
      expected: "Output has 7-phase structure"
      must_pass: true

    - id: "sfr-002"
      name: "Contract specification present"
      action: "Generate skill"
      expected: "Output has input/output contract"
      must_pass: true

    - id: "sfr-003"
      name: "Error handling included"
      action: "Generate skill"
      expected: "Output has error handling section"
      must_pass: true

    - id: "sfr-004"
      name: "Test cases generated"
      action: "Generate skill"
      expected: "Output includes test cases"
      must_pass: true

  failure_threshold: 0
```

### Regression Suite: Cognitive Lensing

**ID**: `cognitive-lensing-regression-v1`

```yaml
regression_suite:
  id: cognitive-lensing-regression-v1
  version: 1.0.0
  frozen: true

  tests:
    - id: "clr-001"
      name: "Goal analysis preserved"
      action: "Run frame selection on task"
      expected: "All three goal orders analyzed (1st, 2nd, 3rd)"
      must_pass: true

    - id: "clr-002"
      name: "Checklist followed"
      action: "Select frame for ambiguous task"
      expected: "Checklist completed before selection"
      must_pass: true

    - id: "clr-003"
      name: "Multi-lingual activation included"
      action: "Apply frame to prompt"
      expected: "Native language activation section present"
      must_pass: true

    - id: "clr-004"
      name: "English output maintained"
      action: "Generate frame-enhanced output"
      expected: "Final output is in English with markers"
      must_pass: true

    - id: "clr-005"
      name: "Frame selection logged"
      action: "Complete frame selection"
      expected: "Selection stored in memory-mcp with WHO/WHEN/PROJECT/WHY"
      must_pass: true

    - id: "clr-006"
      name: "Backward compatibility"
      action: "Run prompt without frame selection"
      expected: "Standard processing works when frame not selected"
      must_pass: true

  failure_threshold: 0
```



## Evaluation Protocol

### Run Evaluation

```javascript
async function runEvaluation(proposal) {
  const results = {
    proposal_id: proposal.id,
    timestamp: new Date().toISOString(),
    benchmarks: {},
    regressions: {},
    human_gates: [],
    verdict: null
  };

  // 1. Run benchmark suites
  for (const suite of getRelevantBenchmarks(proposal)) {
    results.benchmarks[suite.id] = await runBenchmark(suite, proposal);
  }

  // 2. Run regression tests
  for (const suite of getRelevantRegressions(proposal)) {
    results.regressions[suite.id] = await runRegressions(suite, proposal);
  }

  // 3. Check human gates
  results.human_gates = checkHumanGates(proposal, results);

  // 4. Determine verdict
  if (anyRegressionFailed(results.regressions)) {
    results.verdict = "REJECT";
    results.reason = "Regression test failed";
  } else if (anyBenchmarkBelowMinimum(results.benchmarks)) {
    results.verdict = "REJECT";
    results.reason = "Benchmark below minimum threshold";
  } else if (results.human_gates.length > 0) {
    results.verdict = "PENDING_HUMAN_REVIEW";
    results.reason = `Requires approval: ${results.human_gates.join(', ')}`;
  } else {
    results.verdict = "ACCEPT";
    results.reason = "All checks passed";
  }

  return results;
}
```

### Evaluation Output

```yaml
evaluation_result:
  proposal_id: "prop-123"
  timestamp: "2025-12-15T10:30:00Z"

  benchmarks:
    prompt-generation-benchmark-v1:
      status: "PASS"
      scores:
        clarity: 0.85
        completeness: 0.82
        precision: 0.79
      minimum_met: true

  regressions:
    prompt-forge-regression-v1:
      status: "PASS"
      passed: 5
      failed: 0
      details: []

  human_gates:
    triggered: []
    pending: []

  verdict: "ACCEPT"
  reason: "All benchmarks passed, no regressions, no human gates triggered"

  improvement_delta:
    baseline: 0.78
    candidate: 0.82
    delta: +0.04
    significant: true
```



## Anti-Patterns

### NEVER:

1. **Auto-expand eval harness** - Only manual expansion
2. **Lower thresholds to pass** - Thresholds only go up
3. **Skip regressions** - Every change runs full regression
4. **Ignore human gates** - Gates exist for good reasons
5. **Modify frozen benchmarks** - Create new versions instead

### ALWAYS:

1. **Run full evaluation** - No partial runs
2. **Log all results** - Audit trail required
3. **Respect timeouts** - Timeout = REJECT
4. **Document decisions** - Why ACCEPT or REJECT
5. **Archive results** - 90-day retention minimum



**Status**: Production-Ready (FROZEN)
**Version**: 1.1.0
**Key Constraint**: This skill does NOT self-improve
**Expansion**: Manual only, with human approval



## Anti-Patterns (Enhanced)

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Self-Improving Eval** | Allowing the eval harness to modify itself creates a feedback loop where improvements optimize for passing tests, not real quality gains | Freeze the eval harness. Only expand through manual approval. Version all benchmarks. Prevent automated threshold adjustments. |
| **Lowering Thresholds to Pass** | When improvements fail to meet standards, lowering the bar instead of improving the work erodes quality over time | Thresholds can only increase. If a proposal fails, improve the proposal or reject it. Track threshold changes in audit log. |
| **Skipping Regressions for Small Changes** | Even minor changes can introduce unexpected side effects - skipping validation creates compounding risk | Run full regression suite on every change, no exceptions. Automate regression execution to remove friction. Treat any regression failure as a hard block. |
| **Ignoring Human Gate Timeouts** | Allowing proposals to proceed when human reviewers do not respond undermines the gate's purpose | Timeouts default to REJECT, not ACCEPT. If reviewers are unavailable, the change waits or is withdrawn. Log timeout events for capacity planning. |
| **Metric Manipulation** | Optimizing for specific benchmark tasks instead of general capability (e.g., memorizing test cases) | Use holdout test sets that are not visible during training. Rotate benchmarks periodically. Add adversarial examples. Measure transfer learning to unseen tasks. |
| **Approval Fatigue** | Over-triggering human gates for low-risk changes causes reviewers to rubber-stamp approvals | Calibrate gate triggers to balance false positives vs false negatives. Track approval rates and adjust thresholds. Provide reviewers with rich context to make informed decisions. |

---

## Conclusion

The eval harness is the foundation of trustworthy self-improvement systems. By freezing evaluation criteria, requiring objective measurement before subjective judgment, and invoking human gates for uncertainty, teams prevent the insidious drift toward superficial improvements that look good on paper but fail in practice.

Goodhart's Law warns us: "When a measure becomes a target, it ceases to be a good measure." The eval harness resists this by remaining immutable - improvements must adapt to the harness, not the other way around. This asymmetry is not a limitation but a feature: it forces rigorous engineering instead of metric gaming.

Remember: a self-improvement loop is only as good as its evaluation harness. Invest in comprehensive benchmarks, regression tests, and human oversight. Treat the harness as infrastructure - boring, reliable, and never exciting. When the harness is solid, you can innovate with confidence knowing that regressions will be caught before they reach production.