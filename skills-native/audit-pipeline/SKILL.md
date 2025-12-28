---
name: audit-pipeline
description: Skill for audit-pipeline
---

# Audit Pipeline - Complete Code Quality Workflow

## Cognitive Frame Activation

### Kanitsal Kalite Hatti (Evidential Quality Pipeline)

Her bulgu icin metrik kaniti gereklidir:
- **Finding**: [description of quality issue]
- **Evidence**: [metric: value at location]
- **Standard**: [threshold from reference]
- **Impact**: [quantified effect on quality score]
- **Confidence**: [0.0-1.0]

Every quality finding MUST include:
1. **Metric evidence**: Concrete measurement (complexity=13, coverage=60%, lines=72)
2. **Location evidence**: Exact file path and line number [file:line]
3. **Standard reference**: Documented threshold (NASA limit, WCAG level, OWASP category)
4. **Impact quantification**: Quality score delta, risk level, maintainability cost

### Al-Tahlil al-Sarfi lil-Jawda (Morphological Quality Analysis)

Root Cause Decomposition - Every quality issue has layers:

```
DIMENSION: [Maintainability | Performance | Security | Reliability]
  SURFACE: [visible symptom in code]
    - Location: [file:line]
    - Metric: [measurement]
  ROOT: [underlying cause]
    - Pattern: [anti-pattern name]
    - Origin: [design decision, knowledge gap, time pressure]
  DERIVED: [contributing factors]
    - Technical debt
    - Missing tests
    - Unclear requirements
  REMEDIATION: [target the root cause]
    - Fix: [address root, not symptom]
    - Prevent: [process change to avoid recurrence]
```

**Example Decomposition**:
```
DIMENSION: Maintainability
  SURFACE: God Object with 26 methods
    - Location: src/UserService.js:1-450
    - Metric: methods=26 (threshold=15), lines=450 (threshold=250)
  ROOT: Single Responsibility Principle violation
    - Pattern: God Object anti-pattern
    - Origin: Feature additions without refactoring
  DERIVED:
    - Missing abstraction for authentication logic
    - Missing abstraction for data validation
    - Missing abstraction for error handling
  REMEDIATION:
    - Fix: Extract AuthService, ValidationService, ErrorHandler
    - Prevent: Code review gate at 15 methods, refactoring sprint every 3 months
```

## Purpose
Execute a comprehensive 3-phase code quality audit that systematically transforms code from prototype to production-ready by eliminating theater, verifying functionality through sandbox testing with Codex iteration, and polishing style to meet professional standards.

## The 3-Phase Pipeline

This orchestrator runs three audit skills in the optimal sequence:

### Phase 1: Theater Detection Audit
**Finds**: Mock data, hardcoded responses, TODO markers, stub functions, placeholder code
**Goal**: Identify all "fake" implementations that need to be completed
**Skill**: `theater-detection-audit`

### Phase 2: Functionality Audit (with Codex Sandbox)
**Validates**: Code actually works through execution testing
**Method**: Sandbox testing + Codex iteration loop for fixes
**Skill**: `functionality-audit` + `codex-auto`
**Goal**: Verify and fix functionality using Codex's Full Auto mode for iterative debugging

### Phase 3: Style & Quality Audit
**Polishes**: Code organization, naming, documentation, best practices
**Goal**: Production-grade code quality and maintainability
**Skill**: `style-audit`

## Why This Order Matters

**1. Theater First** - No point testing or polishing fake code
- Identifies what's real vs. placeholder
- Provides roadmap for completion
- Ensures subsequent phases test actual functionality

**2. Functionality Second** - Must work before polishing
- Validates real implementations
- Uses Codex sandbox for safe iterative testing
- Fixes bugs before style improvements
- Ensures refactoring won't break working code

**3. Style Last** - Polish after functionality is verified
- Refactors with confidence (tests prove it works)
- Improves maintainability of working code
- Final production-ready state

## Usage

### Complete Pipeline (All 3 Phases)
```bash
/audit-pipeline
```

### With Specific Target
```bash
/audit-pipeline "Audit the src/api directory and prepare for production"
```

### With Configuration
```bash
/audit-pipeline "Audit entire codebase, use Codex for functionality fixes, apply strict style rules"
```

## What Happens in Each Phase

### Phase 1: Theater Detection
```
1. Scans codebase for theater patterns
2. Identifies:
   - Mock/fake data
   - Hardcoded responses
   - TODO/FIXME markers
   - Stub functions
   - Commented-out production code
3. Produces report with locations and priorities
4. Optionally: Completes theater with real implementations
```

**Output**: Theater audit report + completion roadmap



### Phase 3: Style & Quality Audit
```
1. Runs automated linters (pylint, eslint, etc.)
2. Manual style review
3. Security & performance analysis
4. Documentation review
5. Refactors for:
   - Clarity and readability
   - Best practices
   - Maintainability
   - Team standards
6. Verifies functionality preserved after refactoring
```

**Output**: Style audit report + polished code



## Quality Finding Template (Evidence + Root Cause)

Every finding from the audit pipeline MUST use this structure:

```yaml
finding:
  id: "QUAL-001"
  phase: "theater | functionality | style"

  # EVIDENTIAL FRAME (Turkish)
  evidence:
    metric: "[measurement with unit]"
    location: "[file:line-range]"
    standard: "[reference threshold]"
    impact: "[quantified effect]"
    confidence: 0.95
    code_snippet: |
      [context showing the issue]

  # MORPHOLOGICAL FRAME (Arabic)
  root_cause:
    dimension: "Maintainability | Performance | Security | Reliability"
    surface:
      symptom: "[visible issue]"
      location: "[file:line]"
      metric: "[measurement]"
    root:
      cause: "[underlying problem]"
      pattern: "[anti-pattern name]"
      origin: "[why it happened]"
    derived:
      - "[contributing factor 1]"
      - "[contributing factor 2]"
    remediation:
      fix: "[address root cause]"
      prevent: "[process change]"
      validation: "[how to verify fix]"
```

**Complete Example**:
```yaml
finding:
  id: "QUAL-042"
  phase: "functionality"

  evidence:
    metric: "test_coverage=60% (lines), 0% (branches)"
    location: "src/payment/processor.js:1-150"
    standard: "Required: 80% line coverage, 70% branch coverage"
    impact: "-20 quality points, HIGH risk in production"
    confidence: 1.0
    code_snippet: |
      120: function processRefund(orderId, amount) {
      121:   if (amount > 0 && amount <= order.total) {
      122:     // Refund logic - NO TESTS
      123:     return stripe.refund(orderId, amount);
      124:   }
      125: }

  root_cause:
    dimension: Reliability
    surface:
      symptom: "Missing test coverage for refund edge cases"
      location: "src/payment/processor.js:120-125"
      metric: "0% branch coverage (4 branches untested)"
    root:
      cause: "Test-after development pattern"
      pattern: "Untested critical path"
      origin: "Time pressure during payment feature sprint"
    derived:
      - "No test-driven development discipline"
      - "Missing edge case documentation"
      - "No pre-commit coverage gate"
    remediation:
      fix: "Add test cases: zero amount, negative amount, amount > total, stripe API failure"
      prevent: "Enforce TDD for payment code, pre-commit hook blocks <80% coverage"
      validation: "Coverage report shows 100% branch coverage, all edge cases documented"
```

## Pipeline Configuration

### Default Behavior
- Runs all 3 phases sequentially
- Uses Codex Full Auto for functionality fixes
- Applies standard linting rules
- Produces comprehensive report
- **NEW**: All findings use evidential + morphological template

### Customization Options

**Skip Phases** (if some already done):
```bash
/audit-pipeline --skip-theater  # Start from functionality
/audit-pipeline --skip-style    # Just theater + functionality
```

**Codex Integration Level**:
```bash
/audit-pipeline --codex-mode=off          # Manual fixes only
/audit-pipeline --codex-mode=assisted     # Codex suggests, you approve
/audit-pipeline --codex-mode=auto         # Full Auto (default)
```

**Strictness Level**:
```bash
/audit-pipeline --strict         # Fail on any issues
/audit-pipeline --lenient        # Warning mode, no blocks
```

## Output Report

The pipeline produces a comprehensive report:

```markdown
# Code Quality Audit Pipeline Report

## Executive Summary
- **Theater Instances Found**: 15
- **Theater Completed**: 15/15
- **Functionality Tests**: 247 total
  - Passed: 241
  - Failed: 6 (fixed by Codex in 12 iterations)
- **Style Issues Found**: 89
- **Style Issues Fixed**: 89/89
- **Overall Quality**: Production Ready ✓

## Phase 1: Theater Detection
[Detailed findings...]

## Phase 2: Functionality Audit
[Test results, Codex iterations, fixes applied...]

## Phase 3: Style Audit
[Style improvements, refactorings, final metrics...]

## Before vs After Metrics
- Code Quality Score: 45% → 95%
- Test Coverage: 60% → 92%
- Maintainability Index: C → A
- Technical Debt: 12 weeks → 2 days

## Production Readiness: ✓ APPROVED
```

## Integration with Workflow

### Pre-Production Checklist
```bash
# Run before deploying to production
/audit-pipeline "Complete pre-production audit for release v2.0"
```

### Code Review Preparation
```bash
# Clean up before PR
/audit-pipeline "Audit feature branch before code review"
```

### Legacy Code Modernization
```bash
# Transform legacy code
/audit-pipeline "Modernize legacy authentication module"
```

### Post-Prototype Hardening
```bash
# After rapid prototyping
/audit-pipeline "Harden prototype for production deployment"
```

## Codex Sandbox Iteration Loop (Phase 2 Detail)

The functionality audit phase uses Codex's Full Auto mode in a sophisticated iteration loop:

```
For each test failure:
  1. Capture error details and context
  2. Spawn codex-auto in sandbox:
     - Network disabled (security)
     - CWD only (isolation)
     - Full Auto mode (autonomous)
  3. Codex analyzes and fixes
  4. Re-run tests in sandbox
  5. If still failing:
     - Repeat with new context
     - Max 5 iterations per issue
  6. If passing:
     - Validate no regressions
     - Apply fix to main codebase
  7. Document fix in audit report
```

**Safety Features**:
- Sandboxed execution prevents damage
- Iteration limit prevents infinite loops
- Regression testing after each fix
- Human approval for major changes (optional)

## Success Criteria

Pipeline succeeds when:
✅ All theater identified and completed
✅ All functionality tests passing
✅ All style issues resolved
✅ No regressions introduced
✅ Code meets production standards

## When to Use

### Perfect For:
✅ Pre-production quality gates
✅ Legacy code modernization
✅ Post-prototype hardening
✅ Comprehensive code reviews
✅ Continuous quality improvement

### Not Needed When:
❌ Code already production-ready
❌ Only minor changes made
❌ Individual phases already complete

## Related Skills

- **theater-detection-audit**: Run phase 1 alone
- **functionality-audit**: Run phase 2 alone
- **style-audit**: Run phase 3 alone
- **codex-auto**: Used internally for fixes
- **root-cause-analyzer**: For deep debugging

## Time Estimates

- **Small project** (< 1K lines): 5-10 minutes
- **Medium project** (1K-10K lines): 15-30 minutes
- **Large project** (10K-50K lines): 30-60 minutes
- **Very large project** (50K+ lines): 1-3 hours

Times include Codex iteration loops and style refactoring.



**Remember**: This pipeline transforms code from "it works on my machine" to "it's production-ready". Use it before every major release!

See `docs/agents/audit-pipeline-guide.md` for complete documentation.