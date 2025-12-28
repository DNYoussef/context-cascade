---
name: sop-code-review
description: Comprehensive code review workflow coordinating quality, security, performance, and documentation reviewers. 4-hour timeline for thorough multi-agent review.
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


# SOP: Code Review Workflow

Comprehensive code review using specialized reviewers for different quality aspects.

## Timeline: 4 Hours

**Phases**:
1. Automated Checks (30 min)
2. Specialized Reviews (2 hours)
3. Integration Review (1 hour)
4. Final Approval (30 min)

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


## Phase 2: Specialized Reviews (2 hours)

### Parallel Expert Reviews

**Sequential coordination of parallel reviews**:

```javascript
// Spawn specialized reviewers in parallel
const [codeQuality, security, performance, architecture, docs] = await Promise.all([
  Task("Code Quality Reviewer", `
Review for code quality:

**Readability**:
- Clear, descriptive names (variables, functions, classes)
- Appropriate function/method length (< 50 lines)
- Logical code organization
- Minimal cognitive complexity

**Maintainability**:
- DRY principle (no code duplication)
- SOLID principles followed
- Clear separation of concerns
- Proper error handling

**Best Practices**:
- Following language idioms
- Proper use of design patterns
- Appropriate comments (why, not what)
- No code smells (magic numbers, long parameter lists)

Store review: code-review/${prId}/quality-review
Rating: 1-5 stars
`, "code-analyzer"),

  Task("Security Reviewer", `
Review for security issues:

**Authentication & Authorization**:
- Proper authentication checks
- Correct authorization rules
- No privilege escalation risks
- Secure session management

**Data Security**:
- Input validation (prevent injection attacks)
- Output encoding (prevent XSS)
- Sensitive data encryption
- No hardcoded secrets or credentials

**Common Vulnerabilities** (OWASP Top 10):
- SQL Injection prevention
- XSS prevention
- CSRF protection
- Secure dependencies (no known vulnerabilities)

Store review: code-review/${prId}/security-review
Severity: Critical/High/Medium/Low for each finding
`, "security-manager"),

  Task("Performance Reviewer", `
Review for performance issues:

**Algorithmic Efficiency**:
- Appropriate time complexity (no unnecessary O(n²))
- Efficient data structures chosen
- No unnecessary iterations
- Lazy loading where appropriate

**Resource Usage**:
- No memory leaks
- Proper cleanup (connections, files, timers)
- Efficient database queries (avoid N+1)
- Batch operations where possible

**Optimization Opportunities**:
- Caching potential
- Parallelization opportunities
- Database index needs
- API call optimization

Store review: code-review/${prId}/performance-review
Impact: High/Medium/Low for each finding
`, "perf-analyzer"),

  Task("Architecture Reviewer", `
Review for architectural consistency:

**Design Patterns**:
- Follows established patterns in codebase
- Appropriate abstraction level
- Proper dependency injection
- Clean architecture principles

**Integration**:
- Fits well with existing code
- No unexpected side effects
- Backward compatibility maintained
- API contracts respected

**Scalability**:
- Design supports future growth
- No hardcoded limits
- Stateless where possible
- Horizontally scalable

Store review: code-review/${prId}/architecture-review
Concerns: Blocker/Major/Minor for each finding
`, "system-architect"),

  Task("Documentation Reviewer", `
Review documentation:

**Code Documentation**:
- Public APIs documented (JSDoc/docstring)
- Complex logic explained
- Non-obvious behavior noted
- Examples provided where helpful

**External Documentation**:
- README updated (if needed)
- API docs updated (if API changed)
- Migration guide (if breaking changes)
- Changelog updated

**Tests as Documentation**:
- Test names are descriptive
- Test coverage demonstrates usage
- Edge cases documented in tests

Store review: code-review/${prId}/docs-review
Completeness: 0-100%
`, "api-docs")
]);

// Aggregate all reviews
await Task("Review Aggregator", `
Aggregate specialized reviews:
- Quality: ${codeQuality}
- Security: ${security}
- Performance: ${performance}
- Architecture: ${architecture}
- Documentation: ${docs}

Identify:
- Blocking issues (must fix before merge)
- High-priority suggestions
- Nice-to-have improvements

Generate summary
Store: code-review/${prId}/aggregated-review
`, "reviewer");
```

**Deliverables**:
- 5 specialized reviews completed
- Issues categorized by severity
- Aggregated review summary

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


## Phase 4: Final Approval (30 minutes)

### Review Summary & Decision

**Sequential Finalization**:

```javascript
// Step 1: Generate Final Summary
await Task("Review Coordinator", `
Generate final review summary:

**Automated Checks**: ✅ All passing
**Quality Review**: ${qualityScore}/5
**Security Review**: ${securityIssues} issues (${criticalCount} critical)
**Performance Review**: ${perfIssues} issues (${highImpactCount} high-impact)
**Architecture Review**: ${archConcerns} concerns (${blockerCount} blockers)
**Documentation Review**: ${docsCompleteness}% complete
**Integration Tests**: ${integrationStatus}
**Deployment Impact**: ${deploymentImpact}
**User Impact**: ${userImpact}
**Risk Level**: ${riskLevel}

**Blocking Issues**:
${listBlockingIssues()}

**Recommendations**:
${generateRecommendations()}

**Overall Decision**: ${decision} (Approve/Request Changes/Reject)

Store final summary: code-review/${prId}/final-summary
`, "pr-manager");

// Step 2: Author Notification
await Task("Notification Agent", `
Notify PR author:
- Review complete
- Summary of findings
- Action items (if any)
- Next steps

Send notification
Store: code-review/${prId}/author-notification
`, "pr-manager");

// Step 3: Decision Actions
if (decision === 'Approve') {
  await Task("Merge Coordinator", `
Approved for merge:
- Add "approved" label
- Update PR status
- Queue for merge (if auto-merge enabled)
- Notify relevant teams

Store: code-review/${prId}/merge-approval
`, "pr-manager");
} else if (decision === 'Request Changes') {
  await Task("Feedback Coordinator", `
Request changes:
- Create detailed feedback comment
- Label as "changes-requested"
- Assign back to author
- Schedule follow-up review

Store: code-review/${prId}/change-request
`, "pr-manager");
} else {
  await Task("Rejection Handler", `
Reject PR:
- Create detailed explanation
- Suggest alternative approaches
- Label as "rejected"
- Close PR (or request fundamental rework)

Store: code-review/${prId}/rejection
`, "pr-manager");
}
```

**Deliverables**:
- Final review summary
- Author notification
- Decision and next steps

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


## Review Guidelines

### What Reviewers Should Focus On

**DO Review**:
- Logic correctness
- Edge case handling
- Error handling robustness
- Security vulnerabilities
- Performance implications
- Code clarity and maintainability
- Test coverage and quality
- API design and contracts
- Documentation completeness

**DON'T Nitpick**:
- Personal style preferences (use automated linting)
- Minor variable naming (unless truly confusing)
- Trivial formatting (use automated formatting)
- Subjective "better" ways (unless significantly better)

### Giving Feedback

**Effective Feedback**:
- ✅ "This function has O(n²) complexity. Consider using a hash map for O(n)."
- ✅ "This input isn't validated. Add validation to prevent SQL injection."
- ✅ "This error isn't logged. Add error logging for debugging."

**Ineffective Feedback**:
- ❌ "I don't like this."
- ❌ "This could be better."
- ❌ "Change this." (without explanation)

**Tone**:
- Be respectful and constructive
- Assume good intent
- Ask questions rather than make demands
- Suggest, don't dictate (unless security/critical issue)

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


## Usage

```javascript
// Invoke this SOP skill for a PR
Skill("sop-code-review")

// Or execute with specific PR
Task("Code Review Orchestrator", `
Execute comprehensive code review for PR #${prNumber}
Repository: ${repoName}
Author: ${authorName}
Changes: ${changesSummary}
`, "pr-manager")
```

## Core Principles

SOP Code Review operates on 3 fundamental principles:

### Principle 1: Specialized Expertise Over Generalist Review
No single reviewer has deep expertise across all quality dimensions (security, performance, architecture, documentation). Specialization ensures thoroughness.

In practice:
- Security Reviewer focuses exclusively on OWASP Top 10, auth/authz, secret detection
- Performance Analyst evaluates algorithmic complexity, resource usage, optimization opportunities
- Architecture Reviewer assesses design patterns, API contracts, scalability

### Principle 2: Automated Gates Before Human Review
Human review is expensive (4 hours). Automated checks (linting, tests, coverage, build) must pass before humans invest time.

In practice:
- Phase 1 runs automated checks in parallel - all must pass to proceed to Phase 2
- If lint/test/coverage/build fails, request author fixes immediately (stop review)
- Only code that passes automation gates receives human review (saves 50% reviewer time)

### Principle 3: Risk-Based Approval Decisions
Not all changes carry equal risk. Merge decisions must consider blast radius, rollback difficulty, and user impact - not just code quality score.

In practice:
- Integration review (Phase 3) assesses deployment impact and backward compatibility
- Risk analysis considers worst-case failure scenarios and monitoring adequacy
- High-risk changes may require feature flags even if all reviews pass

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Human Review Before Automation** | Reviewers waste time finding lint errors and test failures that automation should catch | ALWAYS run automated checks first (Phase 1) - only proceed to human review if all pass |
| **Single Generalist Reviewer** | One reviewer tries to evaluate security, performance, architecture, docs - misses specialized issues | Use 5 specialized reviewers in parallel (Phase 2) - security-manager, perf-analyzer, system-architect, etc. |
| **Approval Without Risk Assessment** | Approving based on code quality alone without considering deployment impact and rollback strategy | Always include integration review (Phase 3) assessing deployment impact, user impact, risk level before final approval |

## Conclusion

SOP Code Review provides comprehensive PR review through a 4-phase workflow that balances automation efficiency with human expertise. Phase 1 automated checks (lint, tests, coverage, build) act as a blocking gate - human review only begins after automation passes, saving 50% reviewer time. Phase 2 spawns 5 specialized reviewers in parallel (security, performance, style, tests, docs) providing depth that generalist review misses. Phase 3 integration review assesses real-world deployment risk beyond just code quality. Phase 4 generates actionable summary with severity-ranked findings and merge recommendation.

Use this skill when you need production-grade PR review with both automated validation and multi-dimensional human assessment. The 4-hour timeline (vs 8+ hours sequential) makes it suitable for critical PRs requiring security audit, performance validation, and architecture consistency checks. For simpler changes, use quick-quality-check instead. For changes already merged that need post-hoc analysis, use code-review-assistant.