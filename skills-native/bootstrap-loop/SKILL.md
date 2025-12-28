---
name: bootstrap-loop
description: Orchestrates the recursive self-improvement cycle where Prompt Forge improves Skill Forge, Skill Forge improves Prompt Forge, and both audit/improve everything else. All changes gated by frozen eval harness.
---

# Bootstrap Loop (Recursive Self-Improvement Orchestrator)

## Purpose

Orchestrate the recursive improvement cycle:

```
+------------------+         +------------------+
|   PROMPT FORGE   |-------->|   SKILL FORGE    |
| (Meta-Prompt)    |<--------|   (Meta-Skill)   |
+------------------+         +------------------+
         |                            |
         |   Improved tools audit     |
         |   and improve everything   |
         v                            v
+--------------------------------------------------+
|              AUDITOR AGENTS                       |
|  [Prompt] [Skill] [Expertise] [Output]           |
+--------------------------------------------------+
         |                            |
         |   All changes gated by     |
         v                            v
+--------------------------------------------------+
|              EVAL HARNESS (FROZEN)               |
|  Benchmarks | Regression Tests | Human Gates     |
+--------------------------------------------------+
```

**CRITICAL**: The eval harness does NOT self-improve. It is the anchor that prevents Goodhart's Law.

## When to Use

- Running a recursive improvement cycle
- Improving meta-tools (Prompt Forge, Skill Forge)
- Auditing and improving system-wide prompts/skills
- Measuring improvement over time

## MCP Requirements

### memory-mcp (Required)

**Purpose**: Store proposals, test results, version history, metrics

**Activation**:
```bash
claude mcp add memory-mcp npx @modelcontextprotocol/server-memory
```



## Cycle Protocol

### Full Cycle Execution

```javascript
async function runBootstrapCycle(target, options = {}) {
  const cycle = {
    id: `cycle-${Date.now()}`,
    target,
    timestamp: new Date().toISOString(),
    phases: {},
    result: null
  };

  // Phase 1: Analyze
  cycle.phases.analyze = await runPhase('analyze', target, {
    agent: 'prompt-auditor',
    action: `Analyze ${target} for improvement opportunities`
  });

  // Phase 2: Propose
  cycle.phases.propose = await runPhase('propose', target, {
    agent: 'prompt-forge',
    input: cycle.phases.analyze.output,
    action: 'Generate improvement proposals'
  });

  // Check if any proposals generated
  if (cycle.phases.propose.proposals.length === 0) {
    cycle.result = 'NO_PROPOSALS';
    return cycle;
  }

  // Phase 3: Apply
  cycle.phases.apply = await runPhase('apply', target, {
    agent: 'skill-forge',
    input: cycle.phases.propose.proposals,
    action: 'Apply improvements, generate new version'
  });

  // Archive current version before testing
  await archiveVersion(target, cycle.id);

  // Phase 4: Evaluate
  cycle.phases.evaluate = await runPhase('evaluate', target, {
    tool: 'eval-harness',
    candidate: cycle.phases.apply.output,
    benchmarks: getRelevantBenchmarks(target),
    regressions: getRelevantRegressions(target)
  });

  // Phase 5: Decide
  cycle.phases.decide = decideOnResults(cycle.phases.evaluate);

  // Phase 6: Commit or Rollback
  if (cycle.phases.decide.verdict === 'ACCEPT') {
    await commitVersion(target, cycle.phases.apply.output, cycle.id);
    cycle.result = 'ACCEPTED';
  } else {
    await rollbackVersion(target, cycle.id);
    cycle.result = 'REJECTED';
    cycle.rejection_reason = cycle.phases.decide.reason;
  }

  // Store cycle results
  await storeInMemory(`improvement/cycles/${cycle.id}`, cycle);

  return cycle;
}
```

### Decision Logic

```javascript
function decideOnResults(evalResults) {
  const decision = {
    verdict: null,
    reason: null,
    details: {}
  };

  // Check regression tests (must ALL pass)
  if (evalResults.regressions.failed > 0) {
    decision.verdict = 'REJECT';
    decision.reason = `Regression test failed: ${evalResults.regressions.failed_tests.join(', ')}`;
    return decision;
  }

  // Check benchmarks (must meet minimum)
  for (const [benchmark, result] of Object.entries(evalResults.benchmarks)) {
    if (!result.minimum_met) {
      decision.verdict = 'REJECT';
      decision.reason = `Benchmark ${benchmark} below minimum: ${result.score} < ${result.minimum}`;
      return decision;
    }
  }

  // Check for improvement (must be positive)
  if (evalResults.improvement_delta < 0) {
    decision.verdict = 'REJECT';
    decision.reason = `No improvement detected: delta = ${evalResults.improvement_delta}`;
    return decision;
  }

  // Check human gates
  if (evalResults.human_gates_triggered.length > 0) {
    decision.verdict = 'PENDING_HUMAN_REVIEW';
    decision.reason = `Human review required: ${evalResults.human_gates_triggered.join(', ')}`;
    return decision;
  }

  // All checks passed
  decision.verdict = 'ACCEPT';
  decision.reason = `All checks passed. Improvement: +${evalResults.improvement_delta}%`;
  decision.details = {
    benchmark_scores: evalResults.benchmarks,
    regression_passed: evalResults.regressions.passed,
    improvement: evalResults.improvement_delta
  };

  return decision;
}
```



## Multi-Agent Coordination

### Auditor Disagreement Handling

```yaml
disagreement_protocol:
  threshold: 3  # 3+ auditors disagree = human review

  process:
    - step: "Collect all auditor assessments"
    - step: "Identify disagreements"
    - step: "If disagreements > threshold: trigger human gate"
    - step: "Log disagreement details for learning"

  example:
    prompt_auditor: "APPROVE - clarity improved"
    skill_auditor: "REJECT - contract violation introduced"
    expertise_auditor: "NEUTRAL - no expertise impact"
    output_auditor: "REJECT - premature coherence detected"

    verdict: "HUMAN_REVIEW - 2 REJECT, 1 APPROVE, 1 NEUTRAL"
```

### Consensus Requirements

```yaml
consensus:
  for_auto_accept:
    - "All regression tests pass"
    - "All benchmarks meet minimum"
    - "Improvement delta > 0"
    - "No auditor REJECT votes"
    - "No human gates triggered"

  for_auto_reject:
    - "Any regression test fails"
    - "Any benchmark below minimum"
    - "Improvement delta < 0"

  for_human_review:
    - "Auditor disagreement > threshold"
    - "Novel pattern detected"
    - "Breaking change detected"
    - "High-risk change detected"
```



## Anti-Patterns

### NEVER:

1. **Skip eval harness** - Every change must pass
2. **Modify eval during cycle** - Keep eval frozen per cycle
3. **Auto-commit on disagreement** - Human review required
4. **Skip archiving** - Always archive before apply
5. **Run concurrent cycles on same target** - Sequential only

### ALWAYS:

1. **Archive before apply**
2. **Run full eval harness**
3. **Log all decisions**
4. **Track metrics over time**
5. **Respect human gates**

--------|---------|-----------|
| `improvement/cycles/{id}` | Full cycle details | 90 days |
| `improvement/proposals/{id}` | Pending proposals | Until resolved |
| `improvement/commits/{id}` | Committed changes | Permanent |
| `improvement/rollbacks/{id}` | Rollback events | Permanent |
| `improvement/metrics` | Aggregate metrics | Permanent |



**Status**: Production-Ready
**Version**: 1.0.0
**Key Constraint**: All changes gated by frozen eval harness
**Safety**: Eval harness NEVER self-improves

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Skipping eval harness** | Changes applied without validation, regressions introduced, quality degrades over time | NEVER skip eval harness. Every change must pass benchmarks and regression tests. Auto-reject on any regression test failure. |
| **Modifying eval during cycle** | Moving goalposts, Goodhart's Law takes effect, metrics become meaningless | Freeze eval harness per cycle. New benchmarks require human approval. Eval harness never self-improves. |
| **Auto-commit on disagreement** | Auditor disagreement signals risk, auto-commit bypasses validation, introduces breaking changes | Trigger human review when 3+ auditors disagree. Require consensus for auto-accept. Respect auditor REJECT votes. |
| **No archiving before apply** | Cannot rollback on regression, lost version history, no recovery path | Always archive previous version before applying changes. Maintain 90-day retention. Test rollback protocol quarterly. |
| **Concurrent cycles on same target** | Race conditions, conflicting changes, version chaos, merge conflicts | Run cycles sequentially on same target. Queue proposals, process one at a time. Lock target during cycle. |
| **Ignoring human gates** | Breaking changes deployed without review, high-risk changes bypass validation | Respect human gate triggers (novel patterns, breaking changes, high-risk). Pause for manual approval. |

---

## Conclusion

The Bootstrap Loop orchestrates recursive self-improvement with rigorous safeguards against Goodhart's Law and runaway optimization. By treating the eval harness as an immutable anchor, requiring multi-agent consensus for improvements, and maintaining comprehensive version history with rollback capabilities, this skill enables safe, evidence-based evolution of the meta-tools (Prompt Forge and Skill Forge) and all downstream skills and prompts.

The recursive improvement cycle - where Prompt Forge improves Skill Forge, Skill Forge improves Prompt Forge, and both audit everything else - creates a positive feedback loop for continuous quality improvement. However, this loop is carefully bounded by frozen evaluation criteria, transparent decision logging, and automatic rollback on regression. The result is a self-improving system that gets better over time without drifting from its core objectives.

Whether improving a single skill prompt or orchestrating a full audit of 196 skills, the Bootstrap Loop ensures that changes are validated, versioned, and reversible. The combination of automated improvement with human oversight at critical decision points strikes the balance between efficiency and safety, enabling rapid iteration without sacrificing quality or stability.