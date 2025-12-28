---
name: debugging
description: Systematic debugging methodology using a 5-phase protocol. Use when troubleshooting code failures, investigating bugs, or analyzing unexpected behavior. Applies 10 proven debugging techniques including binary search, rubber duck, hypothesis-driven, and differential debugging.
---

# Debugging - Systematic Code Investigation


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

Systematic debugging through proven methodologies and comprehensive error analysis.

## When to Use This Skill

Use when code fails or produces unexpected results, investigating intermittent bugs, analyzing production errors, or debugging complex race conditions and edge cases.

## 5-Phase Debugging Protocol

### Phase 1: Reproduce Reliably
- Create minimal test case that triggers the bug
- Document exact sequence of inputs/conditions
- Verify bug occurs consistently
- Strip away unnecessary complexity

### Phase 2: Understand Root Cause
- Trace execution path leading to failure
- Examine variable values and state
- Identify incorrect assumptions
- Understand what code should do vs. what it does

### Phase 3: Design the Fix
- Determine changes needed to eliminate bug
- Consider impact on other functionality
- Check for similar bugs elsewhere
- Plan testing strategy

### Phase 4: Implement Using Best Practices
- Write clear, readable code
- Add comprehensive comments
- Handle edge cases properly
- Validate assumptions

### Phase 5: Verify the Fix
- Confirm bug no longer occurs
- Run regression tests
- Test edge cases
- Validate under original conditions

## 10 Debugging Methodologies

1. **Binary Search Debugging** - Divide and conquer to isolate bug location
2. **Rubber Duck Debugging** - Explain code to surface blind spots
3. **Hypothesis-Driven** - Form and test explicit hypotheses
4. **Differential Debugging** - Compare working vs. broken code
5. **Logging and Instrumentation** - Add extensive debug output
6. **Breakpoint Analysis** - Step through code with debugger
7. **Stack Trace Analysis** - Work backwards from failure point
8. **State Inspection** - Examine program state at key points
9. **Input Validation** - Test with boundary and edge case inputs
10. **Isolation Testing** - Test components independently

## Integration with Tools

- **Python**: pdb, pytest, coverage.py
- **JavaScript**: Chrome DevTools, debugger statements
- **Go**: delve debugger, race detector
- **General**: GDB, Valgrind, memory sanitizers

## Automation Scripts

This skill includes production-ready automation scripts in `resources/scripts/`:

1. **binary-search-debug.js** - Automated binary search debugging
   - Bisect through git commits to find bug introduction point
   - Bisect through code lines to isolate problematic code
   - Generate comprehensive debug reports with statistics
   - Usage: `node binary-search-debug.js --mode commits --start <hash> --end <hash> --test "npm test"`

2. **log-analyzer.py** - Intelligent log file analysis
   - Parse multiple log formats (Apache, nginx, syslog, JSON, custom)
   - Detect error patterns and temporal distributions
   - Identify anomalies (error bursts, repeating errors)
   - Generate JSON reports with actionable insights
   - Usage: `python log-analyzer.py --file app.log --format custom --output report.json`

3. **stack-trace-analyzer.py** - Stack trace intelligence
   - Multi-language support (Python, JavaScript, Java, Ruby)
   - Automatic root cause categorization
   - Pattern detection across multiple traces
   - Smart recommendations based on error types
   - Usage: `python stack-trace-analyzer.py --input error.log` or `cat trace.txt | python stack-trace-analyzer.py --stdin`

4. **debug-session-recorder.sh** - Debug session management
   - Record complete debugging sessions with metadata
   - Capture system snapshots at key points
   - Log commands and test results automatically
   - Generate comprehensive markdown reports
   - Usage: `./debug-session-recorder.sh start --issue BUG-123` then `./debug-session-recorder.sh stop`

## Templates

Production-ready templates in `resources/templates/`:

1. **debug-config.template.json** - VS Code/IDE debug configurations
   - Python (current file, pytest, remote)
   - Node.js (current file, Jest, attach, Docker)
   - Go (debug, test)
   - Browser (Chrome DevTools)
   - Multi-language compound configurations

2. **logging-config.template.py** - Comprehensive logging setup
   - JSON structured logging
   - Multiple handlers (console, rotating file)
   - Performance tracking context manager
   - Function call decorator
   - Error context capture

3. **debug-checklist.template.md** - Systematic debugging checklist
   - 10-phase debugging workflow
   - Problem definition and reproduction
   - Hypothesis formation and testing
   - Root cause analysis
   - Solution design and implementation
   - Prevention and lessons learned

## Test Suite

Comprehensive tests in `tests/` directory:

1. **test-binary-search-debug.js** - 15+ test cases for binary search debugger
2. **test-log-analyzer.py** - 12+ test cases for log analysis
3. **test-stack-trace-analyzer.py** - 18+ test cases for stack trace analysis

Run tests:
```bash
# JavaScript tests
cd tests && npm test

# Python tests
python tests/test-log-analyzer.py
python tests/test-stack-trace-analyzer.py
```

## Quick Start Examples

### Binary Search Debugging
```bash
# Find commit that introduced bug
node resources/scripts/binary-search-debug.js \
  --mode commits \
  --start HEAD~10 \
  --end HEAD \
  --test "npm test"

# Find exact line causing issue
node resources/scripts/binary-search-debug.js \
  --mode code \
  --file src/buggy.js \
  --test "node test-script.js"
```

### Log Analysis
```bash
# Analyze application logs
python resources/scripts/log-analyzer.py \
  --file /var/log/app.log \
  --format custom \
  --output analysis-report.json

# Analyze JSON logs
python resources/scripts/log-analyzer.py \
  --file logs/production.json \
  --format json
```

### Stack Trace Analysis
```bash
# From file
python resources/scripts/stack-trace-analyzer.py --input crash.log

# From clipboard
python resources/scripts/stack-trace-analyzer.py --clipboard

# From stdin (pipe)
cat error.txt | python resources/scripts/stack-trace-analyzer.py --stdin
```

### Debug Session Recording
```bash
# Start session
./resources/scripts/debug-session-recorder.sh start --issue PROJ-456

# Log commands during debugging
./resources/scripts/debug-session-recorder.sh log-command "pytest -vv tests/test_auth.py"

# Capture snapshot
./resources/scripts/debug-session-recorder.sh snapshot

# Stop and generate report
./resources/scripts/debug-session-recorder.sh stop
./resources/scripts/debug-session-recorder.sh report PROJ-456-20240115-103045
```

## Core Principles

1. **Reproduce Before Fixing** - Always create a minimal, reliable reproduction case before attempting fixes. This validates the bug exists and provides a test for verifying the fix.

2. **Evidence-Driven Investigation** - Base conclusions on concrete evidence (stack traces, logs, profiler data, debugger inspection) rather than assumptions or guesses about root causes.

3. **Systematic Elimination** - Use structured methodologies (binary search, hypothesis testing, differential debugging) to systematically narrow down the problem space rather than random code changes.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|--------------|-----------------|
| **Shotgun Debugging** - Making random code changes hoping to fix the bug | Creates new bugs, obscures root cause, wastes time on ineffective changes | Use systematic debugging methodologies (Phase 1-5 protocol), form explicit hypotheses before changing code |
| **Ignoring Reproduction** - Attempting to fix bugs without reliable reproduction | Fixes may not address actual issue, cannot verify fix effectiveness, bug likely to return | Invest time in Phase 1 (Reproduce Reliably), create automated test that triggers bug consistently |
| **Symptom Fixing** - Addressing surface-level errors without understanding root cause | Masks underlying problem, bug manifests differently later, technical debt accumulates | Use Phase 2 (Understand Root Cause), trace execution to find why code behaves incorrectly, not just where it fails |

## Conclusion

The debugging skill provides a comprehensive framework for investigating and resolving code failures through systematic methodology rather than trial-and-error. By following the 5-phase protocol (Reproduce, Understand, Design, Implement, Verify) and leveraging 10 proven debugging techniques, developers can efficiently identify root causes and implement lasting fixes. The included automation scripts (binary search debugger, log analyzer, stack trace analyzer, session recorder) accelerate common debugging workflows while maintaining rigor.

Successful debugging requires discipline to reproduce bugs reliably, patience to understand root causes deeply, and systematic thinking to eliminate problem spaces methodically. The skill emphasizes evidence-based investigation through actual execution traces, profiler data, and debugger inspection rather than assumptions. By adding regression tests for every fixed bug and avoiding anti-patterns like shotgun debugging or symptom fixing, teams build more robust codebases while continuously improving their debugging capabilities. This systematic approach transforms debugging from a frustrating struggle into a structured problem-solving process with predictable outcomes.

## Core Principles

Debugging operates on 3 fundamental principles:

### Principle 1: Reproducibility First
A bug that cannot be reproduced cannot be reliably fixed. Invest time upfront to create minimal test cases that trigger failures consistently before attempting diagnosis.

In practice:
- Strip away unnecessary code/data to create minimal reproduction cases
- Document exact sequence of inputs and environmental conditions
- Verify bug occurs consistently (not intermittently) before proceeding to fix

### Principle 2: Evidence-Based Diagnosis
Form explicit hypotheses about root causes and test them systematically. Avoid guessing - use stack traces, logs, breakpoints, and state inspection to gather evidence.

In practice:
- Use 10 debugging methodologies (binary search, differential, hypothesis-driven)
- Analyze stack traces with automated tools to identify error patterns
- Instrument code with structured logging to capture execution flow

### Principle 3: Prevention Through Regression Tests
Every fixed bug should be immortalized as a regression test. This prevents the same bug from recurring and documents the expected behavior.

In practice:
- Add automated tests covering the exact failure scenario before fixing
- Run full regression suite to ensure fix doesn't introduce new bugs
- Update monitoring/alerting to catch similar issues in production

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Shotgun Debugging** | Making random changes hoping to fix the bug wastes time and introduces new issues | Use hypothesis-driven debugging: form testable hypotheses, gather evidence systematically |
| **Fixing Symptoms** | Patching surface symptoms without understanding root cause allows bugs to recur | Always perform Phase 2 (Understand Root Cause) before implementing fixes |
| **Print Statement Debugging** | Excessive print statements clutter code and provide poor observability | Use structured logging (JSON format) with appropriate log levels and context |
| **Skipping Reproduction** | Attempting to fix bugs without reliable reproduction leads to ineffective fixes | Always complete Phase 1 (Reproduce Reliably) with minimal test case |
| **Disabling Tests** | Disabling failing tests to make CI pass hides real bugs | Add regression tests for bugs, never disable tests without fixing underlying issues |
| **Production Debugging** | Debugging directly in production risks data corruption and downtime | Reproduce locally or in staging, use production logs/metrics for diagnosis only |

## Conclusion

Debugging transforms from frustrating trial-and-error into systematic investigation when guided by the 5-phase protocol and 10 proven methodologies. By prioritizing reproducibility, gathering evidence through instrumentation, and preventing recurrence with regression tests, this skill ensures bugs are truly solved, not just temporarily suppressed.

Use this skill when facing production incidents requiring rapid diagnosis, intermittent failures like race conditions, or complex stack traces spanning multiple services. The included automation scripts (binary search debugger, log analyzer, stack trace analyzer, session recorder) accelerate investigation by automating tedious analysis tasks.

The result is a repeatable process that goes from bug report to validated fix with high confidence and comprehensive regression protection. When bugs cannot afford to recur, systematic debugging provides the rigor that ad-hoc approaches lack.

## Core Principles

Debugging operates on 3 fundamental principles:

### Principle 1: Reproduce First, Diagnose Second

You cannot fix what you cannot reliably reproduce. Intermittent bugs must be made deterministic before investigation.

In practice:
- Create minimal test case that triggers the bug consistently with exact sequence of inputs
- Document environmental conditions (OS, browser, data state) required for reproduction
- Strip away unnecessary complexity until you have the simplest failing case
- If bug is intermittent, add logging/instrumentation until patterns emerge that enable reliable reproduction

### Principle 2: Understand Root Cause Before Fixing

Fixing symptoms without understanding root cause leads to incomplete fixes and recurring issues.

In practice:
- Trace execution path from symptom back to actual cause using stack traces, debuggers, and logging
- Distinguish between the failure point (where error surfaces) and root cause (why error occurred)
- Form explicit hypothesis about what is wrong, then test hypothesis with targeted experiments
- Check for similar bugs elsewhere in codebase once root cause is understood

### Principle 3: Verify Fixes Under Original Failure Conditions

A fix that works in your test environment may still fail in production under original conditions.

In practice:
- Run regression tests that reproduce original failure and verify fix eliminates it
- Test edge cases and boundary conditions, not just the happy path
- Validate fix under production-like environment (same data, load, configuration)
- Add automated test that would have caught this bug to prevent regression

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Debugging by Print Statement Alone** | Adding print/console.log everywhere creates noise without systematic investigation | Use actual debugger with breakpoints and variable inspection; add logging strategically at decision points, not randomly |
| **Fixing Symptoms Not Causes** | Changing code to make error disappear without understanding why error occurred in first place | Use stack traces to trace error back to root cause; form hypothesis about what's wrong; test hypothesis; only fix after understanding |
| **Skipping Reproduction Step** | Attempting to debug intermittent bug without first making it reproducible | Invest time in reliable reproduction (seeded data, controlled timing, logging); cannot fix what you cannot reproduce consistently |
| **Shotgun Debugging** | Making multiple changes simultaneously hoping something fixes it | Change one variable at a time; test after each change; track what was changed and outcome; use binary search to isolate failure point |
| **Disabling Tests to Make CI Green** | Commenting out failing tests rather than fixing bug or test | Never disable tests without removing them entirely; either fix the bug, fix the test, or delete test with documented justification |
| **Deploying Debug Code** | Leaving verbose logging, debugger statements, or debug flags in production code | Use feature flags for debug modes; strip debug statements before deployment; run linters that catch debugger statements; review before merge |

## Conclusion

Systematic debugging through the 5-phase protocol - Reproduce Reliably, Understand Root Cause, Design Fix, Implement with Best Practices, Verify Fix - transforms bug investigation from frustrating trial-and-error into methodical problem-solving. By combining 10 proven debugging methodologies (binary search, rubber duck, hypothesis-driven, differential, logging, breakpoint analysis, stack trace analysis, state inspection, input validation, isolation testing) with production-ready automation scripts, this skill provides both strategic approach and tactical tools for rapid bug resolution.

The automation scripts - binary-search-debug.js for bisecting commits and code lines, log-analyzer.py for intelligent log pattern detection, stack-trace-analyzer.py for multi-language root cause categorization, and debug-session-recorder.sh for comprehensive session management - accelerate debugging by automating tedious investigation steps. The comprehensive templates for debug configurations, logging setup, and systematic checklists ensure consistency and completeness across debugging sessions.

Use this skill when investigating production incidents requiring rapid diagnosis, troubleshooting intermittent failures like flaky tests or race conditions, analyzing performance issues such as memory leaks or CPU spikes, debugging integration failures with third-party services, conducting regression analysis for bugs introduced by recent changes, or untangling complex stack traces spanning multiple services. The skill is essential for maintaining production systems where quick diagnosis and reliable fixes are critical to user experience and business continuity. The combination of systematic methodology, proven techniques, and automation tools enables debugging efficiency while ensuring fixes address root causes rather than just masking symptoms.