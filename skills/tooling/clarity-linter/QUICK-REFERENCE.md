# Clarity Linter – Quick Reference (v3.2.0)

Purpose: run a rubric-driven clarity audit, deliver focused fixes, and gate changes with evidence and confidence ceilings.

## Triggers
- Use for readability/cognitive-load audits, thin-helper detection, naming and call-depth issues.
- Do not use for security/performance-only scans or generic lint (route elsewhere).

## 3-Phase Execution (Prompt Architect framing)
1. **Metrics Collection** (code-analyzer)
   - AST + call depth, indirection layers, duplication/naming, comment density.
   - Store raw metrics in memory with WHO/WHY/PROJECT tags.
2. **Rubric Evaluation** (reviewer)
   - Score five dimensions: indirection, function size/cohesion, call depth, duplication vs DRY, explanation quality.
   - Verdict: ACCEPT ≥0.80, REFINE 0.60–0.79, REJECT <0.60.
3. **Fix Generation** (coder + analyst)
   - Produce minimal diffs with rationale and rollback notes.
   - Rerun metrics; report deltas and confidence.

## Inputs (minimum)
- `target`: file|directory path.
- `policy`: strict|standard|lenient (default standard).
- Flags: `auto_fix`, `report_format` (md|json), `min_score_threshold` (default 0.60).

## Outputs
- Metrics snapshot + rubric scores + verdict.
- Top violations with evidence and proposed/applied patches.
- Risks, follow-ups, and memory keys used.
- Confidence line: `Confidence: X.XX (ceiling: TYPE Y.YY)`.

## Validation Checklist
- Metrics collected and stored.
- Rubric applied with evidence per issue.
- Re-run metrics after fixes; no regressions.
- Confidence ceiling stated; harness hash logged if used.

## Quick Commands
```bash
# Lint a file
default: clarity-linter --target path/to/file --report-format markdown

# Lint a directory with strict policy
clarity-linter --target src/ --policy strict --auto-fix false
```

Related skills: connascence-analyzer (coupling), code-review-assistant (PR focus), performance-testing-agent (performance).

Confidence: 0.70 (ceiling: inference 0.70) – Quick reference rewritten to Skill Forge/P.A. structure.
