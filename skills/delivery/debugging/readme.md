# Debugging Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.




## When to Use This Skill

- **Production Incidents**: Critical bugs affecting live users requiring rapid diagnosis
- **Intermittent Failures**: Flaky tests, race conditions, or timing-dependent bugs
- **Performance Issues**: Slow endpoints, memory leaks, or CPU spikes
- **Integration Failures**: Third-party API errors, database connectivity issues
- **Regression Analysis**: New bugs introduced by recent changes
- **Complex Stack Traces**: Multi-layered errors spanning multiple services

## When NOT to Use This Skill

- **Feature Development**: Building new functionality (use feature-dev-complete instead)
- **Code Reviews**: Reviewing code quality or architecture (use code-review-assistant)
- **Refactoring**: Restructuring code without fixing bugs (use refactoring skills)
- **Known Issues**: Bugs with clear root cause already identified

## Success Criteria

- [ ] Root cause identified with supporting evidence
- [ ] Fix implemented and tested
- [ ] Regression test added to prevent recurrence
- [ ] All related test suites passing
- [ ] Fix validated in production-like environment
- [ ] Documentation updated with troubleshooting notes
- [ ] Monitoring/alerting adjusted if needed

## Edge Cases to Handle

- **Heisenbugs**: Bugs that disappear when debugger attached
- **Multi-Service Failures**: Cascading errors across microservices
- **Data Corruption**: State inconsistencies requiring rollback
- **Timezone Issues**: Date/time bugs across regions
- **Concurrency Bugs**: Race conditions, deadlocks, or thread safety
- **Memory Corruption**: Pointer errors, buffer overflows in native code

## Guardrails

- **NEVER** deploy debug code or verbose logging to production
- **ALWAYS** reproduce bugs locally before proposing fixes
- **NEVER** fix symptoms without understanding root cause
- **ALWAYS** add regression tests for fixed bugs
- **NEVER** disable tests to make CI pass
- **ALWAYS** verify fixes do not introduce new bugs
- **NEVER** modify production data without backup

## Evidence-Based Validation

- [ ] Bug reproduced consistently with minimal test case
- [ ] Stack traces analyzed with error tracking tools (Sentry, Rollbar)
- [ ] Performance profiled with appropriate tools (Chrome DevTools, py-spy)
- [ ] Fix verified with automated tests
- [ ] Integration tests passing
- [ ] No new errors in application logs
- [ ] Memory/CPU usage within normal bounds

> Systematic debugging methodology for identifying and fixing bugs efficiently

## Quick Start

1. **Report the issue**: Describe symptoms, expected vs actual behavior, and reproduction steps
2. **Run the skill**: The debugging assistant will execute a 5-phase protocol (Symptom ID → Root Cause Analysis → Fix Generation → Validation → Prevention)
3. **Review and apply**: Test the proposed fix and add regression tests to your test suite

## When to Use This Skill

Use this debugging skill when you encounter:

- **Runtime errors**: Exceptions, crashes, or unexpected terminations
- **Logic bugs**: Incorrect output, wrong calculations, or flawed behavior
- **Performance issues**: Slowdowns, memory leaks, or resource exhaustion
- **Integration failures**: Service communication errors or API incompatibilities
- **Race conditions**: Intermittent failures or timing-dependent bugs
- **Test failures**: Failing unit tests, integration tests, or E2E tests that require investigation

**Don't use for**:
- Simple syntax errors (use a linter)
- Typos or obvious mistakes (quick manual fix)
- Feature requests (use feature development workflow)

## Structure Overview

```
debugging/
├── README.md                          # This file - overview and quick start
├── when-debugging-code-use-debugging-assistant/
│   └── skill.md                      # Main skill definition with 5-phase SOP
├── examples/
│   ├── example-1-null-pointer.md     # Basic: Fixing null reference errors
│   ├── example-2-race-condition.md   # Intermediate: Async race condition debugging
│   └── example-3-memory-leak.md      # Advanced: Memory leak investigation
├── references/
│   ├── best-practices.md             # Industry debugging best practices
│   ├── troubleshooting-guide.md      # Common debugging patterns and anti-patterns
│   └── debugging-methodologies.md    # RCA techniques and systematic approaches
└── graphviz/
    └── workflow.dot                   # Visual debugging decision tree
```

## Examples

### Example 1: Null Pointer Exception (Basic)
**Problem**: `TypeError: Cannot read property 'name' of undefined`
**Solution**: Add null safety checks and proper validation
**See**: [examples/example-1-null-pointer.md](examples/example-1-null-pointer.md)

### Example 2: Race Condition (Intermediate)
**Problem**: Intermittent test failures and data corruption
**Solution**: Implement optimistic locking for concurrent updates
**See**: [examples/example-2-race-condition.md](examples/example-2-race-condition.md)

### Example 3: Memory Leak (Advanced)
**Problem**: Continuous memory growth leading to crashes
**Solution**: Proper event listener cleanup and lifecycle management
**See**: [examples/example-3-memory-leak.md](examples/example-3-memory-leak.md)

## 5-Phase Debugging Protocol

The debugging skill follows a systematic SOP:

1. **Symptom Identification** (code-analyzer)
   - Collect error messages, logs, and stack traces
   - Document expected vs actual behavior
   - Establish reproduction steps

2. **Root Cause Analysis** (code-analyzer + coder)
   - Trace execution flow from entry to failure
   - Examine variable states and data transformations
   - Use binary search, hypothesis-driven investigation

3. **Fix Generation** (coder)
   - Generate 2-3 solution approaches
   - Evaluate trade-offs and select optimal fix
   - Implement with clear comments and documentation

4. **Validation Testing** (tester)
   - Create test case reproducing the bug
   - Verify fix resolves issue without regressions
   - Run full test suite and exploratory testing

5. **Regression Prevention** (tester + coder)
   - Add permanent test to test suite
   - Document bug and fix in code/knowledge base
   - Update guidelines to prevent similar issues

## Key Features

- **Systematic approach**: No guessing - follow evidence-based investigation
- **Multi-agent coordination**: Leverage specialized agents (analyzer, coder, tester)
- **Test-driven fixes**: Write tests before fixing to validate solution
- **Knowledge preservation**: Document lessons learned and add regression tests
- **Performance metrics**: Track time to resolution, fix accuracy, regression rate

## Integration

### Memory Coordination
The skill uses Memory MCP for cross-agent communication:
- `debug/[issue-id]/symptoms` - Symptom analysis
- `debug/[issue-id]/root-cause` - RCA findings
- `debug/[issue-id]/fix` - Solution implementation
- `debug/[issue-id]/validation` - Test results
- `debug/[issue-id]/prevention` - Long-term measures

### Hooks Integration
```bash
# Before debugging
npx claude-flow@alpha hooks pre-task --description "Debug: [issue]"

# After fixing
npx claude-flow@alpha hooks post-edit --file "[file]" --memory-key "debug/[id]/fix"

# Session end
npx claude-flow@alpha hooks post-task --task-id "debug-[id]"
```

## Best Practices

**Do**:
- Always reproduce before fixing
- Write tests first (TDD approach)
- Document your reasoning chain
- Consider multiple solutions
- Add regression tests

**Don't**:
- Fix symptoms without understanding root cause
- Skip test validation
- Rush to solutions without analysis
- Leave debugging code in production
- Make unverified assumptions

## Performance Targets

- **Time to Root Cause**: < 30 minutes for typical bugs
- **Fix Accuracy**: > 95% first-attempt success
- **Regression Rate**: < 2% of fixes introduce new issues
- **Test Coverage**: +5-10% coverage per debug session

## Quality Tier: Silver

**File Count**: 10+ files
**Completeness**: README, examples, references, graphviz diagrams
**Validation**: ✅ MECE structure, production-ready components

## Related Skills

- `smart-bug-fix` - AI-powered intelligent debugging with automated fixes
- `functionality-audit` - Sandbox testing for code validation
- `testing-quality` - TDD framework for test creation
- `code-review-assistant` - Multi-agent code review for quality assurance

## References

- [Best Practices](references/best-practices.md) - Industry debugging guidelines
- [Troubleshooting Guide](references/troubleshooting-guide.md) - Common patterns and anti-patterns
- [Debugging Methodologies](references/debugging-methodologies.md) - RCA techniques and frameworks
- [Workflow Diagram](graphviz/workflow.dot) - Visual debugging decision tree


---
*Promise: `<promise>README_VERIX_COMPLIANT</promise>`*
