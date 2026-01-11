# Smart Bug Fix - Resources

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.




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

This directory contains production-ready scripts, templates, and utilities for intelligent debugging and automated bug fixing.

## Directory Structure

```
resources/
├── README.md                    # This file
├── scripts/                     # Production debugging scripts
│   ├── bug-detector.py         # Automated bug pattern detection (350+ lines)
│   ├── root-cause-analyzer.js  # Stack trace & RCA analysis (320+ lines)
│   ├── fix-generator.sh        # AI-powered fix suggestions (280+ lines)
│   └── regression-validator.py # Regression testing validation (300+ lines)
└── templates/                   # Configuration templates
    ├── bug-report.yaml         # Structured bug documentation
    ├── fix-workflow.json       # Debugging process template
    └── regression-tests.yaml   # Test generation config
```

## Scripts Overview

### bug-detector.py
**Purpose**: Automated detection of common bug patterns across codebases.

**Features**:
- Pattern matching for 50+ common bug types
- Static analysis integration (AST parsing)
- Multi-language support (Python, JavaScript, TypeScript)
- Confidence scoring for each detection
- Integration with Claude-Flow memory for pattern learning

**Usage**:
```bash
python resources/scripts/bug-detector.py \
  --path src/ \
  --languages python,javascript \
  --output bug-detection-report.json
```

**Detection Categories**:
1. **Memory Issues**: Leaks, dangling pointers, buffer overflows
2. **Concurrency**: Race conditions, deadlocks, thread safety
3. **Logic Errors**: Off-by-one, null pointer, type mismatches
4. **Security**: SQL injection, XSS, CSRF vulnerabilities
5. **Performance**: N+1 queries, inefficient algorithms
6. **Integration**: API contract violations, broken dependencies

### root-cause-analyzer.js
**Purpose**: Deep stack trace analysis and root cause identification using 5 Whys methodology.

**Features**:
- Stack trace parsing (all major languages)
- Call graph reconstruction
- Variable state tracking
- Timeline reconstruction for intermittent bugs
- Multi-model reasoning (Claude RCA + Codex analysis)

**Usage**:
```bash
node resources/scripts/root-cause-analyzer.js \
  --error-log logs/error.log \
  --source-path src/ \
  --depth deep \
  --output rca-report.md
```

**Analysis Techniques**:
1. **5 Whys**: Recursive questioning to find root cause
2. **Fishbone Diagram**: Categorize contributing factors
3. **Timeline Analysis**: Reconstruct event sequence
4. **Dependency Mapping**: Identify integration failures
5. **State Tracking**: Variable mutations leading to failure

### fix-generator.sh
**Purpose**: AI-powered fix generation with multi-model reasoning and automated validation.

**Features**:
- Integration with Claude, Codex, and Gemini models
- Alternative fix approaches (3+ solutions per bug)
- Sandbox testing before applying fixes
- Automatic rollback on test failures
- Git integration for safe patching

**Usage**:
```bash
bash resources/scripts/fix-generator.sh \
  --bug-id BUG-123 \
  --rca-report rca-report.md \
  --context-path src/api/ \
  --max-attempts 5
```

**Fix Workflow**:
1. **Analyze RCA**: Parse root cause findings
2. **Generate Alternatives**: 3+ fix approaches using multi-model
3. **Rank Solutions**: Score by safety, complexity, impact
4. **Apply Fix**: Implement in sandbox environment
5. **Validate**: Run tests + regression checks
6. **Iterate**: Refine if tests fail (max 5 iterations)

### regression-validator.py
**Purpose**: Comprehensive regression testing to ensure fixes don't introduce new bugs.

**Features**:
- Automated test generation from fix context
- Diff-based test discovery
- Mutation testing for fix robustness
- Performance regression detection
- Visual regression testing (for UI changes)

**Usage**:
```bash
python resources/scripts/regression-validator.py \
  --before-fix git:HEAD~1 \
  --after-fix git:HEAD \
  --test-suite tests/ \
  --coverage-threshold 90 \
  --output regression-report.json
```

**Validation Checks**:
1. **Existing Tests**: All prior tests still pass
2. **New Edge Cases**: Fix handles boundary conditions
3. **Performance**: No degradation (&gt;10% threshold)
4. **Integration**: APIs/contracts remain compatible
5. **Security**: No new vulnerabilities introduced

## Templates

### bug-report.yaml
Structured bug report template with all necessary metadata for automated processing.

**Sections**:
- Bug identification (ID, severity, priority)
- Environment details (OS, runtime, dependencies)
- Reproduction steps (detailed workflow)
- Expected vs actual behavior
- Error logs and stack traces
- Related issues and context

### fix-workflow.json
Configurable debugging workflow with phase definitions and validation gates.

**Phases**:
1. Detection & Triage
2. Root Cause Analysis
3. Fix Generation
4. Testing & Validation
5. Deployment & Monitoring

### regression-tests.yaml
Configuration for automated regression test generation.

**Configuration**:
- Test discovery rules
- Coverage thresholds
- Performance baselines
- Integration test scenarios
- Mutation testing parameters

## Integration with Claude Code Skills

These resources are designed to integrate seamlessly with:
- `functionality-audit` - Validation after fixes
- `theater-detection-audit` - Ensure real implementation
- `code-review-assistant` - Pre-merge review
- `performance-analysis` - Performance impact assessment

## Memory Integration

All scripts store findings and patterns in Claude-Flow memory:

```bash
# Bug detector stores patterns
npx claude-flow memory store \
  --key "bugs/patterns/$(date +%Y%m%d)" \
  --value "$(cat bug-detection-report.json)"

# RCA stores root causes
npx claude-flow memory store \
  --key "rca/findings/BUG-123" \
  --value "$(cat rca-report.md)"

# Fix generator stores successful solutions
npx claude-flow memory store \
  --key "fixes/successful/BUG-123" \
  --value "$(cat fix-implementation.json)"
```

## Best Practices

1. **Always run bug-detector.py first** to identify known patterns
2. **Use deep RCA depth for complex/intermittent bugs**
3. **Generate 3+ alternative fixes** for critical issues
4. **Run full regression suite** before merging fixes
5. **Store all findings in memory** for pattern learning
6. **Use sandbox environments** for all fix testing
7. **Integrate with CI/CD** for automated validation

## Dependencies

### Python Scripts
```bash
pip install -r resources/requirements.txt
```

### Node.js Scripts
```bash
npm install --prefix resources/
```

### System Requirements
- Python 3.9+
- Node.js 18+
- Git 2.30+
- Docker (for sandbox testing)

## License

MIT License - Part of Claude Code Skills Suite


---
*Promise: `<promise>README_VERIX_COMPLIANT</promise>`*
