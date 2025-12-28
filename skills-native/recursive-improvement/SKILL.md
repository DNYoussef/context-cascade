---
name: recursive-improvement
description: Self-improving meta-loop that audits and enhances skills, prompts, and expertise files
---

# Recursive Improvement - Meta-Loop Skill

## Trigger Keywords

**USE WHEN user mentions:**
- "improve skill", "audit skill", "enhance skill", "optimize skill"
- "run improvement cycle", "meta-loop", "self-improve"
- "skill quality check", "documentation audit"
- "recursive improvement", "systematic improvement"
- "batch improve skills", "improve all skills"
- "skill missing [section]", "incomplete documentation"

**DO NOT USE when:**
- User wants to CREATE a new skill - use skill-creator-agent or micro-skill-creator
- User wants to CREATE an agent - use agent-creator
- User wants to improve a PROMPT (not skill) - use prompt-architect
- User wants one-off manual fix - direct editing faster
- Eval-harness benchmarks failing - fix root cause first, not improve on broken baseline
- During active feature development - finish feature, then improve

**Instead use:**
- skill-creator-agent when creating new skills from scratch
- agent-creator when creating new agents
- prompt-architect when optimizing prompts
- skill-forge when applying specific improvements (recursive-improvement coordinates it)


## Overview

The Recursive Improvement skill orchestrates the meta-loop that enables the system to improve itself. It coordinates four specialized auditors (skill-auditor, prompt-auditor, expertise-auditor, output-auditor) to detect issues, generate improvement proposals, apply changes via skill-forge, and validate results through the frozen eval-harness.

**Key Constraint**: The eval-harness is FROZEN - it never self-improves. This prevents Goodhart's Law (optimizing the metric instead of the goal).

## When to Use

**Use When**:
- Skill documentation is incomplete (missing Core Principles, Anti-Patterns, Conclusion)
- Prompt quality has degraded (inconsistent outputs, missing constraints)
- Expertise files are outdated (file locations changed, patterns stale)
- Output quality has dropped (theater code, unvalidated claims)

**Do Not Use**:
- For one-off fixes (use direct editing)
- When eval-harness benchmarks are failing (fix root cause first)
- During active feature development (finish feature first)

## Core Principles

Recursive Improvement operates on 3 fundamental principles:

### Principle 1: Frozen Eval Harness Prevents Goodhart's Law
The evaluation harness that gates all improvements is NEVER self-improved. This ensures the system optimizes for genuine quality, not for passing corrupted benchmarks.

In practice:
- Eval-harness benchmarks are defined externally and versioned separately
- Changes to eval-harness require human approval and audit trail
- All improvement proposals are tested against frozen benchmarks before commit

### Principle 2: Propose-Test-Compare-Commit Pipeline
Every improvement follows a rigorous pipeline: propose changes, test against benchmarks, compare to baseline, commit only if better. No direct edits bypass this pipeline.

In practice:
- Auditors generate structured proposals with predicted improvement deltas
- skill-forge applies proposals in sandbox before production
- A/B comparison ensures new version outperforms baseline
- Rollback available for 30 days if regressions discovered later

### Principle 3: Documentation Completeness Is Non-Negotiable
Skills are not production-ready until they pass documentation audit (100% Tier 1, 100% Tier 2). Missing sections are auto-generated using templates from SKILL-AUDIT-PROTOCOL.md.

In practice:
- Every skill audit checks for Core Principles, Anti-Patterns, Conclusion
- Missing sections trigger auto-generation using domain-specific templates
- Documentation coverage tracked in Memory MCP (skill-audit/metrics)

## Workflow

### Phase 1: Audit Selection

Select appropriate auditor based on target type:

| Target | Auditor | Detection Focus |
|--------|---------|-----------------|
| SKILL.md files | skill-auditor | Structure, contracts, safety, logging, idempotency |
| System prompts | prompt-auditor | Evidence techniques, cognitive patterns, constraints |
| Expertise files | expertise-auditor | Currency, accuracy, completeness, validation |
| Agent outputs | output-auditor | Theater detection, claim verification, quality |

### Phase 2: Issue Detection

Run auditor against target:

```yaml
audit_output:
  target: "{path}"
  issues:
    critical: [{location, description, fix_template}]
    high: [{location, description, fix_template}]
    medium: [{location, description, fix_template}]
  documentation_gaps:
    missing_sections: ["Core Principles", "Anti-Patterns", "Conclusion"]
    tier_compliance: {tier1: 60%, tier2: 40%, tier3: 30%, tier4: 25%}
  overall_score: 0.45
  recommendation: NEEDS_IMPROVEMENT
```

### Phase 3: Proposal Generation

Generate improvement proposals for detected issues:

```yaml
proposals:
  - id: "prop-{timestamp}-001"
    type: documentation  # or: structural, safety, contract, logging
    target_section: "Core Principles"
    before: null  # Section missing
    after: |
      ## Core Principles

      [Auto-generated content using template from SKILL-AUDIT-PROTOCOL.md]
    predicted_improvement: "+15% tier1_compliance"
    risk: low
```

### Phase 4: Apply via skill-forge

Apply proposals through skill-forge Phase 7a/7b:

1. Archive current version (rollback safety)
2. Apply proposed changes
3. Run documentation audit (Phase 7b)
4. Validate tier compliance

### Phase 5: Evaluation Gate

Test against frozen eval-harness:

```yaml
evaluation:
  benchmark_suite: "skill-quality-v1"
  tests:
    - structure_compliance: PASS
    - contract_coverage: PASS
    - safety_rails: PASS
    - documentation_completeness: PASS
  baseline_comparison:
    before_score: 0.45
    after_score: 0.82
    improvement: +0.37
  verdict: ACCEPT
```

### Phase 6: Commit or Rollback

Based on evaluation:

- **ACCEPT**: Commit changes, update version, log to Memory MCP
- **REJECT**: Rollback to archived version, log failure for learning
- **PENDING**: Request human review for edge cases

### Phase 7: Monitoring (7 days)

Track post-improvement metrics:

```yaml
monitoring:
  window: "7 days"
  metrics:
    - usage_success_rate
    - error_rate
    - user_satisfaction
  rollback_trigger: "success_rate < 90%"
```

## Documentation Audit Integration

**NEW in v2.0**: Every improvement cycle includes mandatory documentation audit.

### Audit Protocol Reference

Full protocol: `skills/foundry/skill-forge/SKILL-AUDIT-PROTOCOL.md`

### Tier Requirements

| Tier | Sections | Target |
|------|----------|--------|
| Tier 1 (Critical) | YAML Frontmatter, Overview, Core Principles, When to Use, Main Workflow | 100% |
| Tier 2 (Essential) | Pattern Recognition, Advanced Techniques, Anti-Patterns, Practical Guidelines | 100% |
| Tier 3 (Integration) | Cross-Skill Coordination, MCP Requirements, I/O Contracts, Recursive Improvement | 80% |
| Tier 4 (Closure) | Examples, Troubleshooting, Conclusion, Completion Verification | 80% |

### Auto-Generation Templates

When sections are missing, use templates from SKILL-AUDIT-PROTOCOL.md:

**Core Principles Template**:
```markdown
## Core Principles

[Skill Name] operates on 3 fundamental principles:

### Principle 1: [Domain-Specific Name]
[1-2 sentence explanation based on skill purpose]

In practice:
- [Practical application derived from skill workflow]
- [Another practical application]
```

**Anti-Patterns Template**:
```markdown
## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **[Derived from skill domain]** | [Common mistake] | [How skill addresses it] |
```

**Conclusion Template**:
```markdown
## Conclusion

[Skill Name] provides [core value proposition from Overview].

Key takeaways:
- [Derived from Core Principles]
- [Derived from Workflow]

Use this skill when [When to Use summary]. Avoid [Anti-Pattern summary].
```

## Memory Namespace

```yaml
namespaces:
  skill-audit/metrics:
    total_skills: 180
    complete: N
    partial: M
    incomplete: K
    avg_score: X
    last_audit: ISO-8601

  improvement/audits/{target}:
    timestamp: ISO-8601
    auditor: skill-auditor|prompt-auditor|...
    score: 0.0-1.0
    issues: [...]

  improvement/proposals/{id}:
    status: pending|applied|rejected
    changes: [...]
    evaluation: {...}

  improvement/history:
    cycles: [{date, improvements_made, success_rate}]
```

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Skipping Eval Gate** | Applying improvements without benchmark validation leads to quality regression | ALWAYS run full eval-harness before commit. No exceptions, no shortcuts. |
| **Self-Improving Eval Harness** | If eval-harness improves itself, it can optimize to pass its own tests (Goodhart's Law) | Eval-harness is FROZEN. Changes require human approval and external audit. |
| **Documentation as Afterthought** | Treating doc audit as optional creates perpetually incomplete skills | Documentation audit is MANDATORY in every cycle (Phase 7b). Block until Tier 1+2 at 100%. |

## Conclusion

Recursive Improvement provides the self-improving meta-loop that keeps the entire skill ecosystem healthy and improving over time. By coordinating four specialized auditors, applying changes through a propose-test-compare-commit pipeline, and gating all improvements through a frozen eval-harness, the system achieves continuous quality improvement without the risks of unconstrained self-modification.

Use this skill when skill quality has degraded, documentation is incomplete, or you want to run a systematic improvement cycle across the skill ecosystem. The documentation audit integration ensures that the 151+ skills missing Core Principles, Anti-Patterns, and Conclusion sections are systematically enhanced over time through batch processing.

Key insight: The frozen eval-harness is what makes safe self-improvement possible. Without this constraint, the system could optimize for its own benchmarks rather than genuine quality.

## Related Skills

- `skill-forge`: Applies improvements, includes Phase 7b documentation audit
- `prompt-forge`: Generates and improves prompts
- `functionality-audit`: Validates code actually works (not theater)
- `expertise-manager`: Manages domain expertise files

## MCP Requirements

```yaml
mcp_servers:
  required: [memory-mcp]  # Stores audit results, proposals, history
  optional: [connascence-analyzer]  # Enhanced code quality detection
```

---

**Status**: Production-Ready
**Version**: 2.0.0
**Key Constraint**: Eval-harness is FROZEN - never self-improves