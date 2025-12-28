---
name: smart-bug-fix
description: Intelligent bug fixing workflow combining root cause analysis, multi-model reasoning, Codex auto-fix, and comprehensive testing. Uses RCA agent, Codex iteration, and validation to systematically fix bugs.
---

# Smart Bug Fix

## Kanitsal Hata Ayiklama (Evidential Debugging)

Every bug hypothesis requires evidence. The evidential frame ensures no fix is applied without proof of causation.

**Evidence Requirements**:
- **GOZLEM** (Observation): Bug observed with concrete reproduction steps
- **HIPOTEZ** (Hypothesis): Theory X based on evidence Y
- **DOGRULAMA** (Verification): Fix verified by test results Z
- **RED** (Rejection): Hypothesis rejected due to counter-evidence W

**Example**:
```
GOZLEM: API timeout after 30s under load (reproduction: 1000 concurrent requests)
HIPOTEZ: Database connection pool exhausted (evidence: pool size=10, active=10, waiting=990)
DOGRULAMA: Increased pool to 100, timeout resolved (evidence: 0 timeouts in 10k requests)
```

## Al-Itar al-Sarfi li-Tahlil al-Sabab (Root Cause Morphology)

Symptoms are composed of causes. Decompose systematically using the "Why Chain" until the root is reached.

**Morphological Decomposition**:
- **SYMPTOM**: Observable error or behavior (surface manifestation)
- **CAUSE-1**: Immediate cause (why-1: "Why did this symptom occur?")
- **CAUSE-2**: Deeper cause (why-2: "Why did cause-1 occur?")
- **ROOT**: True root cause (why-N: "Why did cause-(N-1) occur?" until no further "why" exists)

**Example**:
```
SYMPTOM: Login fails on Firefox
CAUSE-1: JWT token not in cookie (why-1)
CAUSE-2: SameSite=Strict blocks cross-site cookies (why-2)
ROOT: Auth server on different subdomain than app (why-3 - architectural root)
```

**NASA 5 Whys Integration**:
The morphological frame is implemented through the 5 Whys methodology:
1. Why-1: Immediate cause (technical layer)
2. Why-2: Systemic cause (design layer)
3. Why-3: Process cause (architectural layer)
4. Why-4: Cultural cause (organizational layer)
5. Why-5: Root cause (foundational layer)

## When to Use This Skill

- **Domain-Specific Work**: Tasks requiring specialized domain knowledge
- **Complex Problems**: Multi-faceted challenges needing systematic approach
- **Best Practice Implementation**: Following industry-standard methodologies
- **Quality-Critical Work**: Production code requiring high standards
- **Team Collaboration**: Coordinated work following shared processes

## When NOT to Use This Skill

- **Outside Domain**: Tasks outside this skill specialty area
- **Incompatible Tech Stack**: Technologies not covered by this skill
- **Simple Tasks**: Trivial work not requiring specialized knowledge
- **Exploratory Work**: Experimental code without production requirements

## Success Criteria

- [ ] Implementation complete and functional
- [ ] Tests passing with adequate coverage
- [ ] Code reviewed and approved
- [ ] Documentation updated
- [ ] Performance benchmarks met
- [ ] Security considerations addressed
- [ ] Deployed or integrated successfully

## Edge Cases to Handle

- **Legacy Integration**: Working with older codebases or deprecated APIs
- **Missing Dependencies**: Unavailable libraries or external services
- **Version Conflicts**: Dependency version incompatibilities
- **Data Issues**: Malformed input or edge case data
- **Concurrency**: Race conditions or synchronization challenges
- **Error Handling**: Graceful degradation and recovery

## Guardrails

- **NEVER** skip testing to ship faster
- **ALWAYS** follow domain-specific best practices
- **NEVER** commit untested or broken code
- **ALWAYS** document complex logic and decisions
- **NEVER** hardcode sensitive data or credentials
- **ALWAYS** validate input and handle errors gracefully
- **NEVER** deploy without reviewing changes

## Evidence-Based Validation

- [ ] Automated tests passing
- [ ] Code linter/formatter passing
- [ ] Security scan completed
- [ ] Performance within acceptable range
- [ ] Manual testing completed
- [ ] Peer review approved
- [ ] Documentation reviewed

## Purpose

Systematically debug and fix bugs using root cause analysis, multi-model reasoning, and automated testing.

## Specialist Agent

I am a debugging specialist using systematic problem-solving methodology.

**Methodology** (Root Cause + Fix + Validate Pattern):
1. Deep root cause analysis (5 Whys, inverse reasoning)
2. Multi-model reasoning for fix approaches
3. Codex auto-fix in isolated sandbox
4. Comprehensive testing with iteration
5. Regression validation
6. Performance impact analysis

**Models Used**:
- **Claude (RCA)**: Deep root cause analysis
- **Codex (Fix)**: Rapid fix implementation
- **Claude (Validation)**: Comprehensive testing
- **Gemini (Context)**: Large codebase analysis if needed

**Output**: Fixed code with test validation and impact analysis

## Input Contract

```yaml
input:
  bug_description: string (required)
  context_path: string (directory or file, required)
  reproduction_steps: string (optional)
  error_logs: string (optional)
  depth: enum[shallow, normal, deep] (default: deep)
```

## Output Contract

```yaml
output:
  root_cause: object
    identified: string
    contributing_factors: array[string]
    evidence: array[string]
  fix_applied: object
    changes: array[file_change]
    reasoning: string
    alternatives_considered: array[string]
  validation: object
    tests_passed: boolean
    regression_check: boolean
    performance_impact: string
  confidence: number (0-1)
```

## Evidential Output Template

All bug fixes MUST follow this evidence-based structure:

```markdown
### Bug Analysis Output

**Symptom**: [observable_error_or_behavior]

**Reproduction**: [step_by_step_reproduction] [VERIFIED|INTERMITTENT|NOT_REPRODUCIBLE]

**Why-Chain** (Morphological Decomposition):
- **Why-1** (Immediate): [technical_cause]
  - EVIDENCE: [log_entry | metric | stack_trace | observation]
  - CONFIDENCE: [0.0-1.0]

- **Why-2** (Systemic): [design_cause]
  - EVIDENCE: [code_inspection | architecture_diagram | dependency_analysis]
  - CONFIDENCE: [0.0-1.0]

- **Why-3** (Architectural): [process_or_architectural_cause]
  - EVIDENCE: [system_design | configuration | infrastructure_analysis]
  - CONFIDENCE: [0.0-1.0]

- **ROOT CAUSE**: [foundational_cause]
  - EVIDENCE: [comprehensive_analysis_supporting_root_diagnosis]
  - CONFIDENCE: [0.0-1.0]

**Hypotheses Tested**:
1. **HIPOTEZ-1**: [hypothesis_description]
   - Evidence For: [supporting_evidence]
   - Evidence Against: [counter_evidence]
   - Status: [VERIFIED|REJECTED]

2. **HIPOTEZ-2**: [hypothesis_description]
   - Evidence For: [supporting_evidence]
   - Evidence Against: [counter_evidence]
   - Status: [VERIFIED|REJECTED]

**Fix Applied**:
- **Approach**: [fix_strategy]
- **Files Changed**: [list_of_modified_files]
- **Rationale**: [why_this_fix_addresses_root_cause]

**Verification** (DOGRULAMA):
- **Tests Before Fix**: [failure_count] failures, [error_logs]
  - EVIDENCE: [test_output_or_logs]

- **Tests After Fix**: [success_count] passing, [regression_check]
  - EVIDENCE: [test_output_or_logs]

- **Performance Impact**: [before_vs_after_metrics]
  - EVIDENCE: [benchmark_results | profiling_data]

**Confidence Score**: [0.0-1.0]
- Based on: [evidence_quality | reproduction_reliability | test_coverage]
```

**Example Output**:

```markdown
### Bug Analysis Output

**Symptom**: API returns 504 Gateway Timeout under load

**Reproduction**: Send 1000 concurrent POST /api/users requests [VERIFIED]

**Why-Chain**:
- **Why-1**: Database connection timeout after 30s
  - EVIDENCE: PostgreSQL logs show "connection pool exhausted"
  - CONFIDENCE: 0.95

- **Why-2**: Connection pool size (10) < concurrent request load (1000)
  - EVIDENCE: Config shows max_connections=10, connection_wait_queue=990
  - CONFIDENCE: 0.90

- **ROOT CAUSE**: Initial pool sizing based on dev load (10 users), not production load (1000 users)
  - EVIDENCE: Config comments show "set for local dev", no load testing performed
  - CONFIDENCE: 0.85

**Hypotheses Tested**:
1. **HIPOTEZ-1**: Slow query causing timeouts
   - Evidence For: Some queries take 5-10s
   - Evidence Against: Timeouts occur even on fast queries (<100ms)
   - Status: REJECTED

2. **HIPOTEZ-2**: Connection pool exhaustion
   - Evidence For: Pool=10, wait_queue=990, timeouts correlate with pool saturation
   - Evidence Against: None
   - Status: VERIFIED

**Fix Applied**:
- Approach: Increased pool from 10 to 100 connections
- Files Changed: config/database.yml
- Rationale: Pool size now matches production concurrency requirements

**Verification**:
- Tests Before: 990/1000 requests timeout (99% failure)
  - EVIDENCE: Load test logs show 504 errors

- Tests After: 0/10000 requests timeout (0% failure)
  - EVIDENCE: Load test logs show all 200 OK

- Performance Impact: P99 latency 30000ms -> 150ms (200x improvement)
  - EVIDENCE: New Relic metrics before/after deployment

**Confidence Score**: 0.90
- Based on: High-quality evidence (logs + metrics), 100% reproduction, comprehensive load testing
```

## Execution Flow

```bash
#!/bin/bash
set -e

BUG_DESC="$1"
CONTEXT_PATH="$2"

echo "=== Smart Bug Fix Workflow ==="

# PHASE 1: Root Cause Analysis
echo "[1/6] Performing deep root cause analysis..."
npx claude-flow agent-rca "$BUG_DESC" \
  --context "$CONTEXT_PATH" \
  --depth deep \
  --output rca-report.md

# PHASE 2: Context Analysis (if large codebase)
LOC=$(find "$CONTEXT_PATH" -name "*.js" -o -name "*.ts" | xargs wc -l | tail -1 | awk '{print $1}')
if [ "$LOC" -gt 10000 ]; then
  echo "[2/6] Large codebase detected - analyzing with Gemini MegaContext..."
  gemini "Analyze patterns related to: $BUG_DESC" \
    --files "$CONTEXT_PATH" \
    --model gemini-2.0-flash \
    --output context-analysis.md
else
  echo "[2/6] Standard codebase - skipping mega-context analysis"
fi

# PHASE 3: Alternative Solutions (multi-model reasoning)
echo "[3/6] Generating fix approaches..."
# Claude approach (from RCA)
CLAUDE_FIX=$(cat rca-report.md | grep "Solution" -A 10)

# Codex alternative approach
codex --reasoning-mode "Alternative approaches to fix: $BUG_DESC" \
  --context rca-report.md \
  --output codex-alternatives.md

# PHASE 4: Implement Fix with Codex Auto
echo "[4/6] Implementing fix with Codex Auto..."
codex --full-auto "Fix bug: $BUG_DESC based on RCA findings" \
  --context rca-report.md \
  --context "$CONTEXT_PATH" \
  --sandbox true \
  --network-disabled \
  --output fix-implementation/

# PHASE 5: Comprehensive Testing with Iteration
echo "[5/6] Testing fix with Codex iteration..."
npx claude-flow functionality-audit fix-implementation/ \
  --model codex-auto \
  --max-iterations 5 \
  --sandbox true \
  --regression-check true \
  --output test-results.json

# Check if tests passed
TESTS_PASSED=$(cat test-results.json | jq '.all_passed')
if [ "$TESTS_PASSED" != "true" ]; then
  echo "⚠️ Tests failed after 5 iterations - escalating to user"
  exit 1
fi

# PHASE 6: Performance Impact Analysis
echo "[6/6] Analyzing performance impact..."
npx claude-flow analysis performance-report \
  --compare-before-after \
  --export performance-impact.json

# Display summary
echo ""
echo "================================================================"
echo "Bug Fix Complete!"
echo "================================================================"
echo ""
echo "Root Cause: $(cat rca-report.md | grep 'Primary Root Cause' -A 2 | tail -1)"
echo "Tests: ✓ All passing"
echo "Regression: ✓ No regressions detected"
echo "Performance Impact: $(cat performance-impact.json | jq '.impact_summary')"
echo ""
echo "Files changed:"
find fix-implementation/ -name "*.js" -o -name "*.ts" | head -10
echo ""
```

## Integration Points

### Cascades
- Part of `/bug-triage-workflow` cascade
- Used by `/production-incident-response` cascade
- Invoked by `/fix-bug` command

### Commands
- Uses: `/agent-rca`, `/gemini-megacontext`, `/codex-auto`, `/functionality-audit`
- Chains with: `/style-audit`, `/performance-report`

### Other Skills
- Input to `regression-validator` skill
- Used by `incident-response` skill
- Integrates with `code-review-assistant`

## Advanced Features

### Automatic RCA Depth Selection

```javascript
function selectRCADepth(bugDescription, errorLogs) {
  if (errorLogs.includes("intermittent") || errorLogs.includes("race condition")) {
    return "deep"; // Complex issues need deep analysis
  } else if (errorLogs.includes("TypeError") || errorLogs.includes("undefined")) {
    return "normal"; // Common errors need normal analysis
  } else {
    return "shallow"; // Simple issues
  }
}
```

### Multi-Model Fix Approach

```yaml
fix_strategy:
  1. Claude RCA → Deep understanding
  2. Codex alternatives → Multiple approaches
  3. Codex auto-fix → Rapid implementation
  4. Claude validation → Comprehensive testing
```

### Codex Iteration Loop

```
Test → FAIL → Codex fix → Test → FAIL → Codex fix → Test → PASS → Apply
↑                                                                    ↓
└────────────────── Max 5 iterations ──────────────────────────────┘
```

## Usage Example

```bash
# Fix bug with description
smart-bug-fix "API timeout under load" src/api/

# Fix with reproduction steps
smart-bug-fix "Login fails on Firefox" src/auth/ \
  --reproduction-steps "1. Open Firefox 2. Try login 3. See error"

# Fix with error logs
smart-bug-fix "Database connection fails" src/db/ \
  --error-logs "logs/error.log"
```

## Failure Modes

- **RCA inconclusive**: Request more context, run additional diagnostics
- **Codex fix fails tests**: Try alternative approach, escalate if max iterations reached
- **Regression detected**: Rollback fix, analyze conflicting requirements
- **Performance degradation**: Optimize fix, consider alternative approach

## Core Principles

Smart Bug Fix operates on 3 fundamental principles:

### Principle 1: Root Cause Over Symptoms
Never patch surface symptoms - invest time in deep root cause analysis using 5 Whys and inverse reasoning. Fixing the underlying issue prevents the bug from reappearing in new forms.

In practice:
- Use RCA agent to perform systematic 5 Whys analysis before implementing fixes
- Identify contributing factors beyond the immediate cause
- Document evidence trail showing how diagnosis was reached

### Principle 2: Validate Through Iteration
Fixes must prove themselves through automated testing with Codex iteration loops. No fix is complete until tests pass and regressions are ruled out.

In practice:
- Run comprehensive testing with max 5 Codex auto-fix iterations
- Enable regression checking to ensure fix doesn't break existing functionality
- Measure performance impact before declaring fix complete

### Principle 3: Alternative Approaches
Generate multiple fix strategies using multi-model reasoning (Claude RCA + Codex alternatives). The first solution is rarely the optimal one.

In practice:
- Compare Claude's RCA-derived solution with Codex alternatives
- Evaluate trade-offs between fixes (complexity, performance, maintainability)
- Choose approach with best long-term viability, not fastest implementation

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Quick Patching** | Fixing symptoms without understanding root cause leads to recurring bugs | Always perform deep RCA before implementing fixes |
| **Single-Attempt Fixes** | First fix fails, give up and escalate prematurely | Use Codex iteration loop (max 5 attempts) before escalating |
| **Ignoring Regressions** | Fix solves bug A but breaks feature B unknowingly | Enable regression checking in functionality audit |
| **Performance Blindness** | Fix works but degrades system performance | Analyze performance impact before declaring success |
| **Manual Testing Only** | Relying on manual verification allows bugs to slip through | Use automated test suite with comprehensive coverage |
| **Skipping Context Analysis** | Fixing bugs in isolation without understanding broader system impact | Analyze large codebases with Gemini MegaContext for patterns |

## Conclusion

Smart Bug Fix transforms debugging from an art into a systematic science. By combining root cause analysis, multi-model reasoning, and automated iteration, this skill ensures bugs are not just patched but truly solved - with evidence of correctness through passing tests and regression validation.

Use this skill when bugs matter - production incidents, recurring issues, or complex failures requiring deep investigation. The RCA-first methodology prevents the whack-a-mole anti-pattern where surface fixes create new bugs elsewhere. The Codex iteration loop provides resilience, automatically recovering from initial implementation failures.

The result is a repeatable process that goes from bug report to validated fix with high confidence. When bugs cannot afford to recur, Smart Bug Fix provides the systematic rigor that manual debugging lacks.

## Changelog

### v1.1.0 (2025-12-19)
- Applied cognitive lensing with evidential (Turkish) and morphological (Arabic) frames
- Added "Kanitsal Hata Ayiklama" (Evidential Debugging) section requiring evidence for all hypotheses
- Added "Al-Itar al-Sarfi li-Tahlil al-Sabab" (Root Cause Morphology) section for systematic symptom decomposition
- Introduced structured Evidential Output Template with:
  - Why-Chain decomposition (Why-1 through ROOT with evidence and confidence scores)
  - Hypothesis testing protocol (GOZLEM, HIPOTEZ, DOGRULAMA, RED)
  - Comprehensive verification requirements (before/after evidence)
  - Confidence scoring based on evidence quality
- Integrated NASA 5 Whys methodology into morphological frame (technical -> systemic -> architectural -> cultural -> foundational)
- Added detailed example outputs demonstrating evidence-based bug analysis
- Enhanced cognitive_frame metadata in YAML frontmatter

### v1.0.0 (Initial Release)
- Root cause analysis using 5 Whys and inverse reasoning
- Multi-model reasoning (Claude RCA + Codex alternatives)
- Codex auto-fix with iteration loops (max 5 attempts)
- Comprehensive testing and regression validation
- Performance impact analysis
- Integration with bug-triage-workflow and production-incident-response cascades