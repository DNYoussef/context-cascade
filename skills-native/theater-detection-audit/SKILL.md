---
name: theater-detection-audit
description: Performs comprehensive audits to detect placeholder code, mock data, TODO markers, and incomplete implementations in codebases. Use this skill when you need to find all instances of "theater" in code such as hardcoded mock responses, stub functions, commented-out production logic, or fake data that needs to be replaced with real implementations. The skill systematically identifies these instances, reads their full context, and completes them with production-quality code.
---

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


# Theater Detection Audit

This skill helps identify and eliminate "theater" in codebases, which refers to code that appears to work but uses fake data, mock responses, stub implementations, or other non-production placeholders. Theater is common during rapid development but must be systematically removed before production deployment. This skill provides a comprehensive audit and completion workflow.

## When to Use This Skill

Use the theater-detection-audit skill when preparing code for production deployment and need to ensure all mocks are replaced, when taking over a codebase and want to understand what is real versus placeholder, when code reviews reveal inconsistent data or suspicious simplicity, or after rapid prototyping phases where shortcuts were taken for speed. The skill is particularly valuable before major releases, during code quality initiatives, or when hardening systems for production use.

## Understanding Code Theater

Code theater takes many forms, all of which create the illusion of functionality without the substance. Recognizing these patterns is the first step in systematic elimination.

**Mock Data and Hardcoded Responses**: Code that returns fixed data instead of fetching from databases, APIs, or user input represents one of the most common forms of theater. This might look like a function that always returns the same user object, an API client that returns sample JSON instead of making real requests, or database queries that return hardcoded arrays. The danger is that this code appears to work during development but fails completely with real data or production conditions.

**TODO and FIXME Markers**: Comments like TODO, FIXME, HACK, or XXX indicate incomplete implementations where the developer acknowledges shortcuts but intended to return later. These markers often accompany placeholder logic that needs replacement. The presence of these markers signals areas requiring careful review and completion before production deployment.

**Stub Functions and Empty Implementations**: Functions that exist but do nothing, or that return default values without real logic, create the appearance of complete interfaces while lacking actual functionality. This is common when building out APIs or class structures before implementing business logic. Stub functions are valuable during development but must be completed before the code can be considered production-ready.

**Commented-Out Production Logic**: Sections of code that are commented out often represent incomplete transitions where developers tried to implement real functionality but fell back to simpler approaches. The commented sections might contain the actual production logic that should be active. This pattern indicates uncertainty or unfinished work that needs resolution.

**Simplified Error Handling**: Error handling that always succeeds, or that catches exceptions but does nothing with them, creates the illusion that code is robust when it actually silently fails. Production code needs comprehensive error detection, logging, and appropriate responses to failure conditions. Oversimplified error handling is a form of theater that hides problems rather than addressing them.

**Test Mode Conditionals**: Code that checks for test flags and behaves completely differently in test versus production modes can hide theater behind conditional logic. While some environmental variation is legitimate, excessive differences between test and production behavior indicate that tests are not validating real functionality. The production path should be what gets tested, not a separate simplified path.

## Audit Methodology

The theater detection audit follows a systematic methodology to ensure comprehensive identification of all placeholder code.

### Phase 1: Pattern-Based Detection

Begin by scanning the codebase for common theater patterns using multiple detection strategies. Search for explicit markers including TODO, FIXME, HACK, XXX, TEMP, STUB, and MOCK in comments. Look for suspicious constant values such as hardcoded user IDs, sample email addresses, fixed timestamps, or test data structures. Identify stub functions that have minimal or no implementation, empty function bodies, immediate return of default values, or commented-out function bodies. Find mock patterns including variables or functions with "mock", "fake", "dummy", or "test" in their names, hardcoded API responses, and simplified database queries that return fixed data.

Create a comprehensive list of all detected instances with file paths, line numbers, the pattern that triggered detection, and immediate code context. This list becomes the audit report that drives the completion phase.

### Phase 2: Contextual Analysis

For each detected instance, read the full file context to understand the intended functionality, what the real implementation should do, what dependencies or data sources it should use, and what error conditions need handling. Theater often exists because the real implementation is complex or depends on external systems that were not yet available during development. Understanding the context reveals what production code needs to look like.

Analyze the surrounding code to determine whether the theater instance is isolated or part of a larger pattern, whether completing it requires changes to other parts of the codebase, what tests exist and whether they validate real behavior, and what edge cases the production implementation must handle. Contextual analysis transforms detection from a simple pattern match into deep understanding of what needs to be built.

### Phase 3: Dependency Mapping

Map out the dependencies and relationships between theater instances. Some placeholders depend on other placeholders, creating chains that must be resolved in the correct order. For example, a mock API client might be used by multiple stub functions. Completing the API client enables completing all the functions that depend on it.

Create a dependency graph that shows which theater instances block completion of others, what external systems or data sources need to be integrated, what authentication or configuration is required, and what order of implementation minimizes rework. Dependency mapping ensures systematic elimination rather than ad hoc fixes that create new problems.

### Phase 4: Risk Assessment

Assess the risk level of each theater instance based on how critical the functionality is to system operation, how likely the placeholder is to cause production failures, how visible the functionality is to end users, and what the impact would be if it fails. High-risk theater such as authentication bypasses or payment processing mocks demands immediate attention, while low-risk theater such as optional feature flags can be prioritized lower.

Risk assessment helps prioritize completion work and ensures critical theater is eliminated before less important instances. It also helps communicate to stakeholders why certain completions are urgent versus deferred.

## Completion Workflow

After identifying and analyzing theater, follow this workflow to complete each instance with production code.

### Step 1: Understand Intended Behavior

For each theater instance, determine what the code should actually do in production. This involves reading specifications, consulting with product owners or architects, examining similar implementations elsewhere in the codebase, and understanding user stories or requirements that this code fulfills. Clear understanding of intended behavior is essential before writing production code.

Document the intended behavior in detail including normal operation paths, edge cases and error conditions, input validation requirements, output format specifications, and performance or scalability considerations. This documentation guides implementation and serves as the basis for testing.

### Step 2: Design Production Implementation

Design the production implementation before writing code. Consider what external systems or data sources to integrate with, what authentication or authorization is required, how to handle errors and failures gracefully, what logging or monitoring to include, how to make the code testable and maintainable, and what performance characteristics are needed.

Good design prevents hasty implementations that simply replace one problem with another. Production code should be robust, secure, efficient, and maintainable, not just "not fake." Take time in the design phase to ensure quality.

### Step 3: Implement with Best Practices

Write the production implementation following coding best practices including proper error handling with specific exception types and meaningful error messages, input validation to prevent invalid data from causing failures, comprehensive logging of important operations and errors, security considerations such as authentication and input sanitization, code clarity with descriptive variable names and helpful comments, and appropriate abstraction to keep the code maintainable.

Production implementations should feel substantially more sophisticated than the theater they replace. The difference should be obvious when reviewing the completed code. If the production code looks suspiciously similar to the theater, probe deeper to ensure real functionality is present.

### Step 4: Test Thoroughly

Develop comprehensive tests that validate the production implementation including unit tests for individual functions and methods, integration tests that verify interaction with external systems, edge case tests for boundary conditions and error scenarios, and load tests for performance-critical code. Tests should fail against the theater implementation but pass against the production code, proving that real functionality has been added.

Testing reveals whether the implementation actually works under realistic conditions or just appears to work. Invest significant effort in testing because this is where remaining theater is exposed. If tests are shallow or mocked out, they become theater themselves, creating a false sense of completeness.

### Step 5: Review and Refine

Conduct thorough code reviews of the completed implementations focusing on whether the code actually implements the intended functionality, if error handling is comprehensive and appropriate, whether security implications have been addressed, if the code is maintainable and well-documented, and whether tests adequately validate behavior. Code review often catches assumptions or shortcuts that the original implementer missed.

Be especially vigilant for new theater introduced during completion. Developers sometimes replace obvious theater with subtler forms when they lack time or information to implement complete solutions. The review should verify that the completion is genuine, not just better-disguised theater.

### Step 6: Update Documentation

Update all documentation to reflect the completed production implementations including API documentation if interfaces changed, architectural documentation if patterns were established, deployment documentation if new dependencies were added, and test documentation describing what is now validated. Documentation ensures that the work of eliminating theater is preserved and that future developers understand what the code actually does.

Outdated documentation that describes mock behavior while the code is now production-ready is its own form of theater, creating confusion about system capabilities. Keep documentation synchronized with code changes.

## Audit Reporting

The theater detection audit produces a comprehensive report that serves multiple purposes including tracking completion progress, communicating findings to stakeholders, and providing an implementation roadmap.

### Report Structure

Structure the audit report with an executive summary stating how many theater instances were found, overall risk assessment, and estimated effort to complete all items. Include detailed findings with a complete list of theater instances including location, pattern type, risk level, and brief description. Provide dependency analysis showing which theater instances are related and what order of completion is recommended. Conclude with a completion roadmap that phases work by priority and shows estimated timelines.

The report should be clear and actionable, allowing both technical and non-technical stakeholders to understand the scope of theater in the codebase and the plan for elimination.

### Tracking Completion Progress

As theater instances are completed, update the audit report to track progress including marking instances as completed, recording completion dates and implementers, noting any complications or deviations from the plan, and tracking how much theater remains. Progress tracking maintains momentum and ensures that completion work does not stall partway through.

Regular progress reviews help identify blockers early and allow for resource reallocation if certain completions are proving more difficult than expected. The goal is systematic elimination of all theater, not just the easy instances.

### Handling Deferred Theater

In some cases, theater cannot be immediately completed because external systems are not available, requirements are unclear, or resources are limited. For deferred theater, document explicitly why completion is deferred, when it is expected to be addressed, what risks the continued presence of theater creates, and what mitigation strategies are in place.

Deferred theater should be tracked carefully to prevent it from being forgotten. Each deferred item should have a clear path to eventual completion rather than becoming permanent fixture.

## Integration with Claude Code Workflow

This skill is designed to be invoked by the main Claude Code instance when conducting code quality audits or preparing for production deployment. The integration follows a specific protocol.

### Invocation Context

Claude Code invokes the theater-detection-audit skill by providing paths to the codebase or specific directories to audit, any known areas of concern to investigate closely, the programming languages in use, and output format preferences for the audit report. The skill expects these inputs to be clearly specified so it can target its audit appropriately.

The skill is computationally intensive because it must scan potentially large codebases and read many files. Provide clear scope boundaries to make the audit tractable. For very large codebases, consider auditing in phases rather than all at once.

### Skill Execution

The skill executes the audit methodology systematically, reporting progress through phase checkpoints, alerting to particularly high-risk findings immediately, maintaining a running count of detected instances, and flagging cases where manual review is recommended. Progress reporting ensures that Claude Code and the user understand that the audit is working and can see findings as they emerge.

The skill may need to ask clarifying questions about intent or requirements when analyzing ambiguous cases. It should escalate these questions promptly rather than making unfounded assumptions about intended behavior.

### Result Packaging

The skill packages its results as a structured audit report in the requested format, a prioritized list of theater instances to complete, code snippets showing each detected instance with context, and recommendations for completion order based on dependencies and risk. These packaged results allow Claude Code to present findings clearly and enable follow-on work to complete the identified theater.

Results should be actionable and specific. Generic findings like "contains mocks" are less valuable than detailed reports showing exactly where each mock is, what it should be replaced with, and why it matters.

## Working with the Theater Detection Audit Skill

To use this skill effectively, provide clear scope for the audit including what directories or files to examine, any known problem areas to investigate closely, what kinds of theater are most concerning, and how detailed the audit report should be. The more context provided, the more targeted and valuable the audit becomes.

The skill will systematically scan, analyze, and report on theater in the codebase, providing a comprehensive view of what needs to be completed before production deployment. It will prioritize findings by risk and dependency, and provide clear guidance on completion order and approach.

This skill is particularly valuable as part of a larger code quality workflow where theater detection feeds into functionality audits and style audits, creating a comprehensive quality improvement pipeline. Together, these audit skills help transform prototype code into production-ready systems.
## Core Principles

Theater Detection Audit operates on 3 fundamental principles:

### Principle 1: Distinguish Appearance from Reality
Code that appears to work through mock data, stub implementations, or hardcoded responses creates dangerous illusions of functionality that fail in production.

In practice:
- Pattern-based detection identifies explicit markers (TODO, FIXME, MOCK), suspicious constants, and stub functions
- Contextual analysis examines surrounding code to determine if implementations are genuine or placeholders
- Risk assessment prioritizes theater based on criticality to system operation and likelihood of production failure
- Dependency mapping reveals chains where mock data flows through multiple components

### Principle 2: Systematic Completion Over Ad Hoc Fixes
Theater must be eliminated systematically through proper production implementations, not replaced with subtler forms of theater through hasty fixes.

In practice:
- Each theater instance triggers understanding of intended behavior from specifications and requirements
- Production implementations are designed before coding to ensure robustness, security, and error handling
- Comprehensive testing validates that completed code works under realistic conditions, not just mocked scenarios
- Code reviews verify that completions are genuine functionality, not better-disguised theater

### Principle 3: Documentation as Quality Assurance
Theater often persists because intended behavior is unclear, dependencies are missing, or requirements are ambiguous. Clear documentation prevents recurrence.

In practice:
- Audit reports explicitly document every theater instance with location, pattern type, and completion requirements
- Deferred theater is tracked with clear justification, expected completion timeline, and risk mitigation
- Completed implementations include updated documentation showing what changed and why
- Progress tracking ensures theater elimination is systematic, not partial or abandoned mid-effort

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Ignoring TODO Comments** | Treating TODO markers as documentation rather than technical debt requiring resolution | Systematically catalog all TODO/FIXME markers; prioritize by risk; track completion progress |
| **Mock Proliferation** | Adding more mocks to support development velocity without plans to replace with real implementations | Limit mock usage to external dependencies; require completion plans for all mocks; audit mock coverage pre-release |
| **Partial Completion** | Replacing obvious theater (hardcoded response) with subtler theater (simplified logic missing error handling) | Require comprehensive implementation including edge cases, error handling, security, and logging - not just basic functionality |
| **Theater in Tests** | Tests that validate against mock data or stub implementations rather than testing real behavior | Minimize test mocking; validate tests fail against theater but pass against production code; test real integrations in sandboxes |
| **Deferred Forever** | Theater marked for future completion but never actually addressed due to lack of tracking | Maintain explicit deferred theater registry with justifications, timelines, and owners; review quarterly; block releases on high-risk items |
| **Documentation Drift** | Leaving documentation describing mock behavior after code is completed with production logic | Update all documentation (API docs, architecture diagrams, deployment guides) when completing theater; validate consistency |

## Conclusion

Theater Detection Audit addresses one of the most dangerous quality issues in software development: code that appears to work during development but fails in production because it relies on fake data, stub implementations, or placeholder logic. By systematically identifying all forms of theater - from explicit TODO markers to subtle mock data patterns - and driving their completion with production-quality implementations, this skill transforms prototype code into production-ready systems.

Use this skill before production deployments to ensure all mocks have been replaced, when taking over codebases to understand what is real versus placeholder, during code quality initiatives to eliminate accumulated technical debt, or after rapid prototyping phases where shortcuts were taken for development speed. The skill is essential for hardening systems before release, particularly in domains where failures have serious consequences like financial transactions, healthcare systems, or security infrastructure.

The systematic methodology - pattern detection, contextual analysis, dependency mapping, risk assessment, and tracked completion - creates a repeatable process for eliminating theater rather than leaving it to chance discovery. The integration with functionality-audit and style-audit creates a comprehensive quality pipeline where theater detection ensures implementations are genuine, functionality-audit verifies they work correctly, and style-audit ensures they are maintainable. Together, these skills establish confidence that code is production-ready, not just development-ready.