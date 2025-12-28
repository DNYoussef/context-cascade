---
name: improvement-pipeline
description: Executable implementation of the Propose -> Test -> Compare -> Commit -> Rollback pipeline for recursive self-improvement. Provides concrete commands and workflows for each stage.
---

# Improvement Pipeline (Executable Stages)

## Purpose

Provide concrete, executable implementation for each stage of the improvement pipeline:

```
PROPOSE -> TEST -> COMPARE -> COMMIT -> MONITOR -> ROLLBACK
```

Each stage has:
- Clear inputs and outputs
- Executable commands
- Validation checks
- Failure handling



## Stage 2: TEST

Run evaluation harness on proposed changes.

### Input
```yaml
test_input:
  proposal_id: "prop-1734567890123"
  candidate_content: "{content with changes applied}"
  benchmark_suite: "prompt-generation-benchmark-v1 | skill-generation-benchmark-v1"
  regression_suite: "prompt-forge-regression-v1 | skill-forge-regression-v1"
```

### Process

```javascript
async function runTests(proposal, candidateContent) {
  const results = {
    proposal_id: proposal.id,
    timestamp: new Date().toISOString(),
    benchmarks: {},
    regressions: {},
    human_gates: []
  };

  // 1. Determine which test suites to run
  const benchmarks = getBenchmarksForTarget(proposal.target);
  const regressions = getRegressionsForTarget(proposal.target);

  // 2. Run benchmark suite
  for (const benchmark of benchmarks) {
    const benchResult = await runBenchmark(benchmark, candidateContent);
    results.benchmarks[benchmark.id] = {
      status: benchResult.score >= benchmark.minimum ? 'PASS' : 'FAIL',
      score: benchResult.score,
      minimum: benchmark.minimum,
      tasks: benchResult.task_results
    };
  }

  // 3. Run regression tests
  for (const regression of regressions) {
    const regResult = await runRegressionSuite(regression, candidateContent);
    results.regressions[regression.id] = {
      status: regResult.failed === 0 ? 'PASS' : 'FAIL',
      passed: regResult.passed,
      failed: regResult.failed,
      failed_tests: regResult.failed_tests
    };
  }

  // 4. Check human gates
  results.human_gates = checkHumanGates(proposal);

  return results;
}

function getBenchmarksForTarget(target) {
  if (target.includes('prompt-forge')) {
    return [{ id: 'prompt-generation-benchmark-v1', minimum: 0.7 }];
  }
  if (target.includes('skill-forge') || target.includes('SKILL.md')) {
    return [{ id: 'skill-generation-benchmark-v1', minimum: 0.75 }];
  }
  if (target.includes('expertise')) {
    return [{ id: 'expertise-generation-benchmark-v1', minimum: 0.8 }];
  }
  return [];
}
```

### Output
```yaml
test_results:
  proposal_id: "prop-1734567890123"
  timestamp: "2025-12-15T10:35:00Z"

  benchmarks:
    skill-generation-benchmark-v1:
      status: "PASS"
      score: 0.87
      minimum: 0.75
      tasks:
        sg-001:
          name: "Micro-Skill Generation"
          scores:
            functionality: 0.85
            contract_compliance: 0.90
            error_coverage: 0.86
        sg-002:
          name: "Complex Skill Generation"
          scores:
            functionality: 0.88
            structure_compliance: 0.87
            safety_coverage: 0.85

  regressions:
    skill-forge-regression-v1:
      status: "PASS"
      passed: 4
      failed: 0
      failed_tests: []

  human_gates: []  # None triggered
```

### Validation
```yaml
test_validation:
  benchmark_check:
    - all_benchmarks_run: true
    - all_scores_recorded: true

  regression_check:
    - all_tests_run: true
    - failure_details_captured: true

  gate_check:
    - all_gates_evaluated: true
```



## Stage 4: COMMIT

Apply changes and create version entry.

### Input
```yaml
commit_input:
  proposal_id: "prop-1734567890123"
  target: "{file path}"
  new_content: "{content with changes applied}"
  comparison_result: "{from Stage 3}"
```

### Process

```javascript
async function commitChanges(proposal, target, newContent, comparison) {
  const commit = {
    id: `commit-${Date.now()}`,
    proposal_id: proposal.id,
    timestamp: new Date().toISOString(),
    target,
    actions: []
  };

  // 1. Archive current version
  const archivePath = getArchivePath(target);
  const currentVersion = await getCurrentVersion(target);
  await writeFile(
    `${archivePath}/SKILL-v${currentVersion}.md`,
    await readFile(target)
  );
  commit.actions.push({
    action: 'archive',
    path: `${archivePath}/SKILL-v${currentVersion}.md`
  });

  // 2. Apply new content
  await writeFile(target, newContent);
  commit.actions.push({
    action: 'update',
    path: target
  });

  // 3. Increment version
  const newVersion = incrementVersion(currentVersion);
  await updateVersionInFile(target, newVersion);
  commit.actions.push({
    action: 'version_bump',
    from: currentVersion,
    to: newVersion
  });

  // 4. Update changelog
  const changelogEntry = formatChangelogEntry(proposal, comparison, newVersion);
  await appendToChangelog(target, changelogEntry);
  commit.actions.push({
    action: 'changelog_update',
    entry: changelogEntry
  });

  // 5. Store commit record in memory
  await storeInMemory(`improvement/commits/${commit.id}`, {
    ...commit,
    proposal,
    comparison
  });

  return commit;
}

function formatChangelogEntry(proposal, comparison, version) {
  return `
## v${version} (${new Date().toISOString().split('T')[0]})

**Proposal**: ${proposal.id}
**Improvement**: ${comparison.reason}

**Changes**:
${proposal.changes.map(c => `- ${c.section}: ${c.rationale}`).join('\n')}

**Metrics**:
${Object.entries(comparison.delta)
  .map(([k, v]) => `- ${k}: ${v.baseline} -> ${v.candidate} (${v.percent_change})`)
  .join('\n')}
`;
}
```

### Output
```yaml
commit_result:
  id: "commit-1734567890456"
  proposal_id: "prop-1734567890123"
  timestamp: "2025-12-15T10:45:00Z"
  target: ".claude/skills/skill-forge/SKILL.md"

  actions:
    - action: "archive"
      path: ".claude/skills/skill-forge/.archive/SKILL-v1.0.0.md"
    - action: "update"
      path: ".claude/skills/skill-forge/SKILL.md"
    - action: "version_bump"
      from: "1.0.0"
      to: "1.1.0"
    - action: "changelog_update"
      entry: "## v1.1.0..."

  status: "SUCCESS"
```

### Validation
```yaml
commit_validation:
  pre_commit:
    - archive_exists: "Verify archive created"
    - backup_verified: "Can restore from archive"

  post_commit:
    - file_updated: "Target file has new content"
    - version_incremented: "Version number updated"
    - changelog_appended: "Changelog has new entry"
    - memory_stored: "Commit record in memory"
```



## Stage 6: ROLLBACK

Restore previous version if regressions detected.

### Input
```yaml
rollback_input:
  commit_id: "commit-1734567890456"
  reason: "regression_detected | manual_request"
  evidence: "{alert details or user request}"
```

### Process

```javascript
async function rollback(commitId, reason, evidence) {
  const commit = await retrieveFromMemory(`improvement/commits/${commitId}`);
  if (!commit) throw new Error(`Commit not found: ${commitId}`);

  const rollback = {
    id: `rollback-${Date.now()}`,
    commit_id: commitId,
    target: commit.target,
    timestamp: new Date().toISOString(),
    reason,
    evidence,
    actions: []
  };

  // 1. Find archived version
  const archivePath = getArchivePath(commit.target);
  const previousVersion = decrementVersion(commit.actions
    .find(a => a.action === 'version_bump').to);
  const archiveFile = `${archivePath}/SKILL-v${previousVersion}.md`;

  // 2. Verify archive exists
  if (!await fileExists(archiveFile)) {
    rollback.status = 'FAILED';
    rollback.error = `Archive not found: ${archiveFile}`;
    return rollback;
  }

  // 3. Restore archived content
  const archivedContent = await readFile(archiveFile);
  await writeFile(commit.target, archivedContent);
  rollback.actions.push({
    action: 'restore',
    from: archiveFile,
    to: commit.target
  });

  // 4. Update changelog
  const rollbackEntry = `
## ROLLBACK to v${previousVersion} (${new Date().toISOString().split('T')[0]})

**Rolled back from**: ${commit.actions.find(a => a.action === 'version_bump').to}
**Reason**: ${reason}
**Evidence**: ${JSON.stringify(evidence)}
`;
  await appendToChangelog(commit.target, rollbackEntry);
  rollback.actions.push({
    action: 'changelog_update',
    entry: rollbackEntry
  });

  // 5. Mark commit as rolled back
  commit.rolled_back = true;
  commit.rollback_id = rollback.id;
  await storeInMemory(`improvement/commits/${commitId}`, commit);

  // 6. Store rollback record
  await storeInMemory(`improvement/rollbacks/${rollback.id}`, rollback);

  // 7. Cancel monitoring
  const monitor = await retrieveFromMemory(`improvement/monitors/${commitId}`);
  if (monitor) {
    monitor.status = 'CANCELLED_ROLLBACK';
    await storeInMemory(`improvement/monitors/${commitId}`, monitor);
  }

  rollback.status = 'SUCCESS';
  rollback.restored_version = previousVersion;

  return rollback;
}
```

### Output
```yaml
rollback_result:
  id: "rollback-1734567890789"
  commit_id: "commit-1734567890456"
  target: ".claude/skills/skill-forge/SKILL.md"
  timestamp: "2025-12-15T15:00:00Z"

  reason: "regression_detected"
  evidence:
    alert_type: "REGRESSION"
    metric: "clarity"
    baseline: 0.85
    current: 0.75
    delta: -0.10

  actions:
    - action: "restore"
      from: ".claude/skills/skill-forge/.archive/SKILL-v1.0.0.md"
      to: ".claude/skills/skill-forge/SKILL.md"
    - action: "changelog_update"
      entry: "## ROLLBACK to v1.0.0..."

  status: "SUCCESS"
  restored_version: "1.0.0"
```

### Validation
```yaml
rollback_validation:
  pre_rollback:
    - archive_exists: "Verify archived version available"
    - target_accessible: "Can write to target file"

  post_rollback:
    - content_restored: "File matches archive"
    - changelog_updated: "Rollback documented"
    - commit_marked: "Commit flagged as rolled back"
    - monitor_cancelled: "Monitoring stopped"
```



## Memory Namespaces

| Namespace | Purpose | Retention |
|-----------|---------|-----------|
| `improvement/proposals/{id}` | Pending proposals | Until resolved |
| `improvement/commits/{id}` | Committed changes | Permanent |
| `improvement/rollbacks/{id}` | Rollback events | Permanent |
| `improvement/monitors/{id}` | Active monitoring | 30 days |
| `improvement/pipelines/{id}` | Full pipeline runs | 90 days |
| `improvement/pending/{id}` | Awaiting human review | Until resolved |

## Core Principles

### 1. Every Stage Has Clear Contracts
Each pipeline stage must have explicit inputs, outputs, and validation criteria to enable debugging and rollback.

**In practice**:
- Define JSON schemas for inputs and outputs at each stage boundary
- Validate inputs before processing and outputs before proceeding to next stage
- Store intermediate results in memory with versioned namespaces
- Log all decisions with rationale for audit trail
- Make stages idempotent: running twice produces same result

### 2. Test Before Commit, Monitor After Commit
Automated evaluation gates changes before they are applied, continuous monitoring detects delayed regressions.

**In practice**:
- Run eval harness on candidate changes before committing
- Reject proposals that fail benchmarks or regressions immediately
- Set up 7-day monitoring window after commit to catch delayed issues
- Define alert thresholds: 3% regression triggers warning, 10% triggers rollback consideration
- Archive baseline versions to enable instant rollback

### 3. Rollback is a First-Class Operation
Rollback must be as easy and reliable as deployment to enable confident experimentation.

**In practice**:
- Archive every version before applying changes
- Verify archives are restorable during commit (pre-validation)
- Document rollback trigger conditions: regression detected, manual request, failed monitoring
- Make rollback single-command: restore archive, update changelog, cancel monitoring
- Track rollback events as learning opportunities, not failures

-----------|---------|----------|
| **Skipping Baseline Comparison** | Deploying changes without comparing candidate vs baseline hides regressions and prevents measuring actual improvement | Always run COMPARE stage. Calculate deltas for all metrics. Reject if average delta is negative. Log comparison results for trend analysis. |
| **Manual Rollback Procedures** | Complex rollback steps discourage experimentation and slow incident response when production breaks | Automate rollback: single function call restores archive, updates changelog, cancels monitoring. Test rollback in staging. Make rollback safer than staying broken. |
| **Ignoring Delayed Regressions** | Committing changes and moving on without monitoring allows subtle bugs to compound over time | Set up automatic monitoring for 7 days post-commit. Define alert thresholds. Link monitoring to rollback consideration. Store monitoring results in memory. |
| **Proposal Overload** | Batching too many changes into one proposal makes it impossible to isolate which change caused a regression | Limit proposals to 5 changes maximum. Break large refactors into incremental proposals. Run separate test cycles for unrelated changes. |
| **Missing Validation Gates** | Allowing incomplete proposals (missing rationale, no predicted improvement) into the pipeline creates low-quality change churn | Validate proposal structure before processing. Require rationale, predicted improvement, risk assessment. Reject malformed proposals early. |
| **Lost Context on Rollback** | Rolling back without documenting why loses valuable learning and risks repeating the same mistake | Append rollback entry to changelog with reason and evidence. Store rollback record in memory. Link to original commit. Schedule post-mortem to prevent recurrence. |

---

## Conclusion

The improvement pipeline transforms chaotic ad-hoc changes into a disciplined, auditable process. By requiring clear contracts at every stage, gating changes with automated testing, and treating rollback as a first-class operation, teams can iterate rapidly without sacrificing stability.

The pipeline's power comes from its staged architecture: PROPOSE creates concrete diffs, TEST validates objectively, COMPARE decides quantitatively, COMMIT applies safely, MONITOR detects delays, and ROLLBACK recovers instantly. Each stage is independently testable, debuggable, and improvable.

Remember: the goal is not perfection on the first try, but safe experimentation with fast feedback loops. The pipeline reduces the cost of failure, making it rational to try bold improvements. When rollback is easy, teams take smarter risks. When monitoring is automatic, regressions are caught early. When every stage is validated, the pipeline becomes a competitive advantage - not overhead, but infrastructure that enables velocity.