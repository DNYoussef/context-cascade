---
name: functionality-audit
description: Validates that code actually works through sandbox testing, execution verification, and systematic debugging. Use this skill after code generation or modification to ensure functionality is genuine rather than assumed. The skill creates isolated test environments, executes code with realistic inputs, identifies bugs through systematic analysis, and applies best practices to fix issues without breaking existing functionality. This ensures code delivers its intended behavior reliably.
---

## Kanitsal Kalite Denetimi (Evidential Quality Audit)

Her bulgu icin olcum gerekli:
- METRIK: Measured value at [location]
- ESIK: Threshold from [quality_standard]
- ETKI: Impact quantified [confidence: X]

## Al-Tahlil al-Sarfi lil-Jawda (Morphological Quality Analysis)

Quality Decomposition:
- DIMENSION: Maintainability/Performance/Security
  - ROOT: Primary quality factor
  - DERIVED: Contributing sub-factors
  - REMEDIATION: Target root, not symptoms

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


# Functionality Audit

This skill validates that code genuinely works as intended through systematic testing in isolated sandbox environments. Rather than assuming code is correct because it looks right or passes cursory checks, the functionality audit actually executes code with realistic inputs, verifies outputs match expectations, and debugs any issues discovered. This transforms theoretical correctness into verified functionality.

## When to Use This Skill

Use the functionality-audit skill after generating or modifying code to verify it works before deployment, when code appears correct but behavior seems off, after integrating code from multiple sources, or before production releases as final validation. The skill is essential when correctness is critical, when code complexity makes visual inspection insufficient, or when debugging existing code that fails intermittently or mysteriously.

## The Importance of Execution Verification

Code that looks correct is not the same as code that works correctly. Syntax can be valid while logic is flawed. Functions can exist while their implementations are broken. Integration points can appear properly connected while producing incorrect results. Execution verification eliminates the gap between apparent correctness and actual functionality.

**Syntax Correctness Versus Semantic Correctness**: Code can parse and compile without errors while implementing the wrong algorithm, making incorrect assumptions about input data, handling edge cases improperly, or producing subtly wrong outputs. Syntax checking validates form but not substance. Semantic correctness requires execution with realistic inputs and careful verification of outputs.

**Static Analysis Limitations**: Static analysis tools check for code smells, common pitfalls, and structural issues, but they cannot verify that code implements its intended behavior correctly. A function might have perfect style and no linting warnings while computing the wrong result. Static analysis is valuable but insufficient for functionality validation.

**The Testing Gap**: Even code with tests may have bugs if tests are incomplete, shallow, or incorrectly specify expected behavior. Tests themselves can be wrong, passing while the code they test is broken. Comprehensive functionality auditing goes beyond running existing tests to creating new test cases that probe behavior systematically and verify outputs carefully.

**Integration Complexity**: Code that works in isolation often fails when integrated with other components because of incorrect interface assumptions, incompatible data formats, race conditions in concurrent code, or dependencies on execution order. Execution verification in realistic environments exposes these integration issues before they cause production failures.

## Sandbox Testing Methodology

The functionality audit uses isolated sandbox environments to test code safely without affecting production systems or development environments.

### Sandbox Creation

Create isolated test environments that replicate production conditions as closely as possible while remaining safe for experimentation. This involves provisioning fresh virtual environments with required dependencies, setting up isolated databases or mock data stores, configuring environment variables and system settings, and ensuring network isolation to prevent unintended external interactions.

Sandboxes should be reproducible so tests run consistently across different executions. Use containerization, virtual machines, or isolated Python environments depending on the technology stack. The goal is a clean slate for each test run that mimics production without production risks.

### Test Case Generation

Generate comprehensive test cases that exercise code through multiple paths including normal operation with typical valid inputs, boundary conditions that test the edges of acceptable inputs, error cases with invalid or malformed inputs, edge cases that expose off-by-one errors or overflow conditions, and stress tests with large datasets or high concurrency if performance matters.

Test cases should be systematically designed to achieve high code coverage while focusing on the most likely sources of bugs. For example, any code that parses external input should be tested with malformed input. Any code that performs calculations should be tested with boundary values. Any code that loops should be tested with empty, single-item, and large collections.

### Execution Monitoring

Execute code in the sandbox while carefully monitoring behavior including standard output and error streams for unexpected messages, return values and exceptions to verify correct results, execution time and resource usage for performance issues, and file system or database state changes for side effects. Comprehensive monitoring reveals not just whether code runs but whether it runs correctly.

Use instrumentation and logging liberally during testing. Add temporary print statements or debug logs to expose intermediate values. Use debugger breakpoints to step through complex logic. The goal is complete transparency into what the code is actually doing during execution.

### Output Verification (Evidence-Backed Template)

Verify that code produces correct outputs by comparing actual results against expected results using precise equality for deterministic functions, range checking or statistical measures for functions with acceptable variance, structural validation for complex outputs like JSON or objects, and assertion checking for invariants that should always hold.

Output verification requires clear specifications of what correct behavior looks like. For functions with complex outputs, define validation logic that checks all important properties rather than just superficial aspects. Subtle bugs often hide in outputs that are mostly right but wrong in small ways.

**Quality Finding Template**:

```markdown
### Quality Finding
- **Dimension**: [Maintainability|Performance|Security|Reliability|Testability]
- **Issue**: [description]
- **Evidence**:
  - Metric: [value] at [location:line]
  - Threshold: [limit] from [standard]
- **Root Cause Analysis**:
  - Surface: [visible_symptom]
  - ROOT: [true_underlying_cause]
- **Impact**: [quantified_effect] [Confidence: 0.0-1.0]
- **Remediation**: [fix targeting root cause]
```

**Example**:

```markdown
### Quality Finding
- **Dimension**: Performance
- **Issue**: Excessive database queries in user fetch loop
- **Evidence**:
  - Metric: 847 queries in src/api/users.js:42
  - Threshold: 1 query per operation (N+1 anti-pattern)
- **Root Cause Analysis**:
  - Surface: Slow page load (4.2s)
  - ROOT: Unbatched queries inside loop iteration
- **Impact**: 4x page load degradation [Confidence: 0.95]
- **Remediation**: Replace loop with single JOIN query or batch loader
```

### Failure Analysis

When tests fail, perform systematic analysis to understand why. Examine the exact failure mode and error messages, trace execution backwards from the failure point, identify the first point where actual behavior diverges from expected behavior, and determine the root cause rather than just symptoms. Effective debugging starts with precise understanding of what went wrong and why.

Avoid jumping to conclusions or applying fixes before understanding root causes. A hasty fix for a symptom often leaves the underlying bug in place or creates new problems. Take time to understand failures deeply before attempting repairs.

## Systematic Debugging Workflow

When functionality audits reveal bugs, follow this systematic debugging workflow to fix issues reliably without introducing new problems.

### Step 1: Reproduce the Bug Reliably

Before attempting any fix, ensure the bug can be reproduced consistently. Create a minimal test case that reliably triggers the failure. Strip away unnecessary complexity to isolate the bug. Document the exact sequence of inputs or conditions needed to reproduce the issue. Reliable reproduction is essential for verifying that fixes actually work.

If a bug cannot be reproduced reliably, it may be a race condition, memory corruption, or other non-deterministic issue requiring specialized debugging techniques like stress testing under various conditions or memory sanitizers.

### Step 2: Understand the Bug's Cause

Investigate why the bug occurs by tracing through the code execution path that leads to the failure, examining variable values and state at key points, identifying incorrect assumptions or logic errors, and understanding what the code should do versus what it actually does. Root cause understanding prevents superficial fixes that mask problems rather than solving them.

Use debugging tools like breakpoints, watch expressions, and stack traces to inspect program state. Add logging to expose hidden behavior. Draw diagrams of data flow if it helps clarify complex logic. The investment in understanding pays off in better fixes.

### Step 3: Design the Fix

Before writing code, design the fix carefully by determining what needs to change to eliminate the bug, considering whether the fix might introduce new bugs, checking if similar bugs exist elsewhere in the codebase, and planning how to test that the fix works without breaking other functionality.

Good fixes address root causes rather than symptoms. They are localized to avoid widespread changes that increase risk. They include test cases that would have caught the original bug. They consider edge cases that might reveal additional problems.

### Step 4: Implement Using Best Practices

Implement the fix following coding best practices from the prompting-principles skill including clear, readable code that makes the fix obvious, comprehensive comments explaining why the change was necessary, proper error handling for edge cases related to the bug, and validation of assumptions that were incorrect in the buggy version.

The fixed code should be noticeably better than the original, not just "less broken." If the fix feels like a hack or workaround, reconsider whether it addresses the root cause or just papers over symptoms.

### Step 5: Verify the Fix

Test the fixed code thoroughly to confirm the bug no longer occurs, verify that the fix does not break existing functionality through regression testing, test edge cases related to the bug, and validate that the fix works under the same conditions where the original bug occurred.

Verification should be more comprehensive than the original functionality audit because fixes can introduce new bugs. Pay special attention to interactions with other code that might be affected by the changes.

### Step 6: Document the Fix

Document what bug was fixed, why it occurred, how the fix addresses the root cause, what testing was performed to verify the fix, and any risks or side effects of the change. Good documentation helps future maintainers understand the code's evolution and prevents reintroduction of fixed bugs.

Documentation should be written for someone who was not involved in the original bug investigation. Explain enough context that the fix makes sense without requiring archaeological research into commit histories.

## Integration with Sandbox Tools

The functionality audit integrates with various sandbox and testing tools depending on the technology stack.

### Python Sandbox Testing

For Python code, use virtual environments with venv or conda to isolate dependencies, pytest for test execution and assertion checking, unittest.mock for mocking external dependencies, coverage.py for measuring test coverage, and pdb debugger for interactive debugging when tests fail.

Python's rich ecosystem of testing tools makes comprehensive functionality audits straightforward. Leverage these tools rather than reinventing testing infrastructure.

### JavaScript Sandbox Testing

For JavaScript code, use Node.js isolated environments or browser sandboxes, Jest or Mocha for test frameworks, testing-library for component testing if applicable, Istanbul for coverage measurement, and debugger statements or Chrome DevTools for debugging.

JavaScript's asynchronous nature requires careful attention to timing and promises during testing. Ensure tests properly handle async operations and do not produce false positives from incomplete async resolution.

### Containerized Testing

For complex applications, use Docker containers to create reproducible test environments, docker-compose for multi-service applications, isolated networks for testing distributed systems, and volume mounts to access test results and logs. Containerized testing provides the highest fidelity to production environments while maintaining isolation.

Containers add complexity but enable testing of applications that require specific system configurations, databases, or external services. The investment in containerized testing infrastructure pays off for serious applications.

### Cloud-Based Sandboxes

For applications that integrate with cloud services, use provider-specific testing tools like AWS SAM for Lambda functions, Google Cloud emulators for Firebase and other services, or Azure DevTest Labs for Azure resources. Cloud sandboxes allow testing of cloud-specific functionality without incurring production costs or risks.

Mock cloud services when possible to keep tests fast and deterministic. Use real cloud sandboxes for integration testing where mocking would miss important behavior.

## Debugging Techniques from Best Practices

Apply proven debugging techniques when functionality audits reveal issues.

### Binary Search Debugging

When a bug's location is unclear, use binary search to narrow down the problem space. Test halfway through the code to determine if the bug is in the first or second half. Recursively subdivide until the buggy section is isolated. This technique quickly focuses attention on the relevant code when the bug's location is not obvious.

Binary search debugging is especially valuable in large codebases or when dealing with regressions where the bug was recently introduced but the triggering commit is unknown.

### Rubber Duck Debugging

Explain the code's intended behavior and actual behavior to someone else, or even to an inanimate object like a rubber duck. The act of explaining often reveals the bug because it forces explicit articulation of assumptions and logic that may contain errors. If no other person is available, write out the explanation in prose.

Rubber duck debugging surfaces mental blind spots where the developer thinks code does one thing but it actually does another. The verbalization process breaks through these blind spots.

### Hypothesis-Driven Debugging

Form explicit hypotheses about what might be causing the bug, design experiments or test cases that would confirm or refute each hypothesis, systematically test hypotheses starting with the most likely, and eliminate possibilities until the root cause is identified.

Hypothesis-driven debugging transforms bug fixing from random trial-and-error into systematic scientific investigation. Document tested hypotheses and results to avoid repeating failed approaches.

### Differential Debugging

Compare the buggy code against working code including older versions before the bug was introduced, similar code in other parts of the system that works correctly, or reference implementations from documentation or tutorials. Identifying what changed or what is different often illuminates the source of bugs.

Differential debugging is particularly effective for regressions where code previously worked but now fails. The delta between working and broken versions directly points to the problem.

### Logging and Instrumentation

Add extensive logging to expose program state during execution including input values at function entry, intermediate computation results, conditional branch paths taken, and output values before return. Comprehensive logging makes the invisible visible, revealing exactly what the code is doing.

Temporary debug logging can be removed after debugging, but consider retaining some strategic logging permanently to aid future debugging. Well-placed production logging dramatically reduces debugging time when issues arise.

## Output Report Structure

The functionality audit produces a structured report that communicates findings and tracks progress.

### Execution Summary

Begin the report with an executive summary stating how many test cases were run, what percentage passed versus failed, overall assessment of code quality, and critical issues requiring immediate attention. The summary gives stakeholders quick insight into code functionality without requiring them to read detailed results.

### Detailed Test Results

For each test case, document the test case description and inputs, expected behavior, actual behavior, whether the test passed or failed, and if failed, specific error messages or stack traces. Detailed results support debugging and provide evidence for claims about code quality.

Structure test results to make patterns visible. Group failures by type or location to reveal systemic issues rather than isolated bugs.

### Identified Bugs

List all bugs discovered during testing with clear descriptions of each bug's behavior, root cause if identified, severity assessment, recommended fix, and testing needed to verify the fix. This list becomes the debugging roadmap that guides remediation work.

Prioritize bugs by severity and impact. Critical bugs that cause crashes or data corruption demand immediate attention. Minor bugs that affect edge cases can be deferred.

### Remediation Tracking

As bugs are fixed, update the report to track progress including marking bugs as fixed, recording fix dates and implementers, noting what testing confirmed the fix, and tracking remaining bugs. Progress tracking ensures bugs do not slip through cracks and provides evidence of quality improvement.

### Testing Recommendations

Conclude with recommendations for additional testing including test cases that should be added to prevent regressions, areas of code that need more comprehensive testing, suggestions for improving test infrastructure, and proposals for ongoing continuous testing. These recommendations ensure that functionality validation becomes part of the development process rather than a one-time activity.

## Integration with Claude Code Workflow

The functionality-audit skill integrates with Claude Code as part of a comprehensive quality assurance workflow.

### Invocation Context

Claude Code invokes functionality-audit after generating or modifying code by providing paths to code files to test, description of expected behavior, available test data or inputs, and any known issues or concerns. Clear context enables targeted testing rather than blind exploration.

### Execution and Reporting

The skill creates sandboxes, generates test cases, executes tests, analyzes failures, and packages results into a comprehensive report. It reports progress through testing phases and flags critical issues immediately for user awareness.

The skill may request clarifications about expected behavior if specifications are ambiguous. It escalates questions promptly rather than making assumptions that might lead to false positives or negatives in testing.

### Feedback Loop with Other Skills

Functionality audit findings feed into other quality skills. Bugs discovered during testing might reveal theater that was missed by theater-detection-audit. Code that works but is poorly structured provides input to style-audit for improvement. The three audit skills together create a comprehensive quality improvement pipeline.

## Working with the Functionality Audit Skill

To use this skill effectively, provide clear specifications of expected code behavior, representative test data or inputs, any known edge cases or problem areas, and information about dependencies or external systems the code interacts with. The more context provided, the more thorough and accurate the functionality testing becomes.

The skill will systematically test code, identify bugs, debug issues using best practices, and produce a comprehensive report. It transforms code from "possibly correct" to "verified correct" through rigorous execution validation. When combined with theater-detection-audit and style-audit, it ensures code is genuine, functional, and well-crafted before deployment.
## Core Principles

Functionality Audit operates on 3 fundamental principles:

### Principle 1: Execution Over Assumption
Code that looks correct is not the same as code that works correctly. Syntax validation, static analysis, and visual inspection are insufficient for verifying functionality.

In practice:
- Every code change is executed in isolated sandbox environments with realistic inputs
- Outputs are verified against precise specifications, not assumptions about correctness
- Edge cases and boundary conditions are systematically tested, not just happy paths
- Integration behavior is validated under production-like conditions

### Principle 2: Systematic Root Cause Analysis
Bugs are symptoms of underlying problems. Superficial fixes that address symptoms without understanding root causes leave problems in place or create new issues.

In practice:
- Failures trigger methodical investigation to trace execution backwards from the failure point
- Hypotheses about bug causes are formed and tested systematically before applying fixes
- Minimal reproducible test cases are created to isolate bugs from surrounding complexity
- Fixes are designed to eliminate root causes, validated through comprehensive testing

### Principle 3: Comprehensive Verification Feedback Loop
Testing and fixing are iterative processes. Each bug discovered and fixed improves understanding of system behavior and reveals additional areas requiring validation.

In practice:
- Test results feed directly into debugging workflows with detailed failure analysis
- Fixed code undergoes more thorough testing than original implementations to prevent regressions
- Patterns from discovered bugs inform generation of new test cases for similar vulnerabilities
- Documentation captures the evolution from buggy to verified code for future maintainers

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Approval Without Execution** | Assuming code works because it "looks right" or passes linting without running it | Execute code in sandboxes with realistic inputs before approval; require output verification |
| **Shallow Testing** | Testing only happy paths or using incomplete test cases that miss edge conditions | Generate comprehensive test suites covering normal operation, boundaries, errors, edge cases, and stress scenarios |
| **Symptom-Based Fixes** | Applying quick patches that address visible failures without understanding underlying causes | Perform root cause analysis before implementing fixes; trace execution to identify where actual behavior diverges from expected |
| **Theater Testing** | Tests that use mocks everywhere or validate against other mock data rather than real behavior | Use minimal mocking; test against real integrations in sandbox environments; verify outputs match production specifications |
| **Incomplete Verification** | Checking that code runs without errors but not verifying correctness of outputs or side effects | Validate outputs with precise equality checks, structural validation, and invariant assertions; monitor side effects like file/database changes |
| **Manual-Only Testing** | Relying on one-time manual verification without automated regression prevention | Create automated test suites from manual test cases; integrate testing into development workflow |

## Conclusion

Functionality Audit transforms code quality assurance from a superficial checking exercise into rigorous validation that code genuinely works as intended. By executing code in isolated sandbox environments and systematically verifying behavior against specifications, this skill eliminates the dangerous gap between apparent correctness and actual functionality. The combination of comprehensive test case generation, careful output verification, and systematic debugging workflows ensures that bugs are not just found but understood and properly fixed.

Use this skill whenever code correctness is critical, particularly after generating or modifying complex logic, integrating code from multiple sources, or before production releases. The skill is essential when visual inspection is insufficient due to code complexity, when debugging mysterious failures that only occur under specific conditions, or when establishing confidence that new code will behave correctly in production environments.

The systematic approach embodied in functionality-audit - from sandbox creation through test execution to root cause analysis and verified fixes - creates a repeatable quality process that catches bugs early and prevents regressions. When integrated with theater-detection-audit to ensure code is genuine and style-audit to ensure maintainability, functionality-audit completes a comprehensive quality pipeline that delivers production-ready code with verified behavior, not just syntactically correct placeholders.

---

## Changelog

### v1.1.0 (2025-12-19)
- Added cognitive frame: evidential (primary) + morphological (secondary)
- Added Turkish/Arabic cognitive frame activation headers
- Added evidence-backed Quality Finding Template with metrics, thresholds, and root cause analysis
- Added example quality finding demonstrating N+1 query detection
- Enhanced output verification section with structured reporting format
- Rationale: Quality auditing requires metric-backed findings decomposed to root causes