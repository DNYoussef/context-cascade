---
name: when-reviewing-pull-request-orchestrate-comprehensive-code-review
description: | Use when conducting comprehensive code review for pull requests across multiple quality dimensions. Orchestrates 12-15 specialized reviewer agents across 4 phases using star topology coordination. Covers automated checks, parallel specialized reviews (quality, security, performance, architecture, documentation), integration analysis, and final merge recommendation in a 4-hour workflow.
---

# Code Review Orchestration Workflow

Comprehensive code review workflow orchestrating 12-15 specialized reviewers across automated checks, parallel expert reviews, integration analysis, and final approval recommendation. Designed for thorough quality validation across security, performance, architecture, testing, and documentation dimensions in a systematic 4-hour process.

## Overview

This SOP implements a multi-dimensional code review process using star topology coordination where a central PR manager orchestrates specialized reviewers operating in parallel. The workflow emphasizes both thoroughness and efficiency by running automated checks first (gate 1), then parallelizing specialized human-centric reviews, followed by integration impact analysis, and finally synthesizing all findings into actionable recommendations.

The star pattern enables each specialist to focus deeply on their domain while the coordinator ensures comprehensive coverage and prevents conflicting feedback. Memory coordination allows reviewers to reference findings from other specialists, creating a holistic review experience.

## Trigger Conditions

Use this workflow when:
- Reviewing pull requests requiring comprehensive quality validation
- Changes span multiple quality dimensions (code, security, performance, architecture)
- Need systematic review from multiple specialist perspectives
- PR introduces significant functionality or architectural changes
- Merge decision requires evidence-based go/no-go recommendation
- Team wants consistent, repeatable review process
- Code review SLA is within 4 hours (business hours)

## Orchestrated Agents (15 Total)

### Coordination Agent
- **`pr-manager`** - PR coordination, review orchestration, findings aggregation, author notification

### Automated Check Agents (Phase 1)
- **`code-analyzer`** - Linting, static analysis, code complexity metrics
- **`tester`** - Test execution, test suite validation
- **`qa-engineer`** - Coverage analysis, test quality assessment

### Specialized Review Agents (Phase 2)
- **`code-analyzer`** - Code quality, readability, maintainability, DRY, SOLID principles
- **`security-manager`** - Security vulnerabilities, OWASP compliance, secrets scanning, auth/auth
- **`performance-analyzer`** - Performance regressions, algorithmic efficiency, resource optimization
- **`system-architect`** - Architectural consistency, design patterns, scalability, integration fit
- **`api-documentation-specialist`** - Code documentation, API docs, comments, examples
- **`style-auditor`** - Code style consistency, formatting standards
- **`dependency-analyzer`** - Dependency audit, outdated packages, security vulnerabilities
- **`test-coverage-reviewer`** - Coverage metrics, uncovered code paths, edge case testing
- **`documentation-reviewer`** - README updates, changelog, migration guides

### Integration Analysis Agents (Phase 3)
- **`system-integrator`** - Integration impact, breaking changes, backward compatibility
- **`devops-engineer`** - Deployment impact, infrastructure changes, rollback planning
- **`code-reviewer`** - Risk assessment, blast radius analysis

## Workflow Phases

### Phase 1: Automated Checks (30 Minutes, Parallel Gate)

**Duration**: 30 minutes
**Execution Mode**: Parallel automated validation (fast fail-fast gate)
**Agents**: `code-analyzer`, `tester`, `qa-engineer`, `pr-manager`

**Process**:

1. **Initialize Review Swarm**
   ```bash
   PR_ID="$1"  # e.g., "repo-name/pulls/123"
   PR_NUMBER=$(echo $PR_ID | cut -d'/' -f3)

   npx claude-flow hooks pre-task --description "Code review: PR #${PR_NUMBER}"
   npx claude-flow swarm init --topology star --max-agents 15 --strategy specialized
   npx claude-flow agent spawn --type pr-manager
   ```

   **PR Manager** retrieves PR metadata:
   - Changed files and line counts
   - Commit history and messages
   - Branch comparison (base vs head)
   - PR description and labels
   - Author and reviewers assigned

   **Memory Storage**:
   ```bash
   npx claude-flow memory store --key "code-review/${PR_ID}/metadata" \
     --value '{"pr_number": "'"${PR_NUMBER}"'", "files_changed": 15, "lines_added": 342, "lines_deleted": 78}'
   ```

2. **Run Automated Checks in Parallel**
   ```bash
   npx claude-flow task orchestrate --strategy parallel --max-agents 4
   ```

   Spawn all automated check agents concurrently:

   **Linting Check** (Code Analyzer):
   ```bash
   npx claude-flow agent spawn --type code-analyzer --focus "linting"

   # Run linting
   npm run lint  # ESLint for JS/TS
   # or
   pylint src/  # Python
   # or
   rubocop  # Ruby
   ```

   Checks:
   - Code style violations (max line length, indentation)
   - Unused variables and imports
   - Type errors (TypeScript)
   - Deprecated API usage
   - Code complexity warnings

   **Memory Pattern**: `code-review/${PR_ID}/phase-1/code-analyzer/lint-results`

   **Test Execution** (Tester):
   ```bash
   npx claude-flow agent spawn --type tester --focus "test-execution"

   # Run test suite
   npm test  # Jest/Mocha
   # or
   pytest  # Python
   # or
   rspec  # Ruby
   ```

   Validates:
   - All unit tests passing
   - All integration tests passing
   - All E2E tests passing (if applicable)
   - No flaky test failures
   - Test execution time within limits

   **Memory Pattern**: `code-review/${PR_ID}/phase-1/tester/test-results`

   **Coverage Analysis** (QA Engineer):
   ```bash
   npx claude-flow agent spawn --type tester --focus "coverage"

   # Generate coverage report
   npm run test:coverage
   ```

   Checks:
   - Overall coverage > 80%
   - New code coverage > 90%
   - No critical paths uncovered
   - Coverage delta (did coverage decrease?)
   - Untested branches and conditions

   **Memory Pattern**: `code-review/${PR_ID}/phase-1/qa-engineer/coverage-report`

   **Build Validation** (Code Analyzer):
   ```bash
   # Clean build validation
   npm run build
   # or
   python setup.py build
   ```

   Validates:
   - Clean build (no errors, no warnings)
   - Type checking passes (TypeScript, mypy)
   - No broken dependencies
   - Bundle size within limits (for frontend)
   - No circular dependencies

   **Memory Pattern**: `code-review/${PR_ID}/phase-1/code-analyzer/build-status`

3. **Evaluate Gate 1 Results**
   ```bash
   npx claude-flow memory retrieve --pattern "code-review/${PR_ID}/phase-1/*/results"
   ```

   **PR Manager** aggregates automated results:
   - Lint: PASS/FAIL (violations count)
   - Tests: PASS/FAIL (passed/failed/skipped)
   - Coverage: PASS/FAIL (percentage, delta)
   - Build: PASS/FAIL (errors/warnings)

   **Decision Logic**:
   ```javascript
   if (lintFailed || testsFailed || buildFailed) {
     // Request fixes from author
     await notifyAuthor({
       status: 'CHANGES_REQUESTED',
       message: 'Automated checks failed. Please fix before review continues.',
       details: summarizeFailures()
     });

     // Store feedback and stop review
     await memory_store(`code-review/${PR_ID}/phase-1/automated-feedback`);
     return; // Stop review until fixed
   }

   // All automated checks passed, proceed to Phase 2
   await notifyAuthor({
     status: 'IN_REVIEW',
     message: 'Automated checks passed. Proceeding with specialized reviews.'
   });
   ```

**Outputs**:
- Automated check results (pass/fail for each)
- Test execution report
- Coverage report with delta
- Build status

**Success Criteria**:
- [ ] All linting checks passing
- [ ] All tests passing (100% of test suite)
- [ ] Code coverage meets thresholds
- [ ] Build successful with no errors



### Phase 3: Integration Analysis (1 Hour, Sequential Impact Assessment)

**Duration**: 1 hour
**Execution Mode**: Sequential end-to-end impact analysis
**Agents**: `tester`, `devops-engineer`, `product-manager`, `code-reviewer`

**Process**:

1. **Integration Testing**
   ```bash
   npx claude-flow agent spawn --type tester --focus "integration-impact"
   ```

   **QA Engineer** tests:
   - Does this change break existing functionality?
   - Are all integration tests passing?
   - Does it integrate properly with related modules?
   - Any unexpected side effects or regressions?

   Run integration test suite:
   ```bash
   npm run test:integration
   ```

   **Findings**:
   - Integration tests: 45/45 passing
   - No regressions detected
   - New functionality integrates cleanly

   **Memory Pattern**: `code-review/${PR_ID}/phase-3/tester/integration-tests`

2. **Deployment Impact Assessment**
   ```bash
   npx claude-flow memory retrieve --key "code-review/${PR_ID}/metadata"
   npx claude-flow agent spawn --type cicd-engineer --focus "deployment-impact"
   ```

   **DevOps Engineer** evaluates:
   - Infrastructure changes needed? (new services, scaling)
   - Database migrations required? (schema changes)
   - Configuration updates needed? (env vars, secrets)
   - Backward compatibility maintained? (can rollback safely)
   - Rollback plan clear and tested?

   **Findings**:
   ```json
   {
     "infrastructure_changes": ["Add Redis cache for session storage"],
     "database_migrations": ["Add index on users.email for faster lookups"],
     "config_updates": ["Add REDIS_URL environment variable"],
     "backward_compatible": true,
     "rollback_complexity": "LOW",
     "deployment_risk": "MEDIUM"
   }
   ```

   **Memory Pattern**: `code-review/${PR_ID}/phase-3/devops-engineer/deployment-impact`

3. **User Impact Assessment**
   ```bash
   npx claude-flow agent spawn --type planner --focus "user-impact"
   ```

   **Product Manager** assesses:
   - Does this improve user experience?
   - Any user-facing changes? (UI/UX)
   - Consistent with design system?
   - Analytics/tracking updated?
   - Feature flags needed?

   **Findings**:
   ```json
   {
     "user_facing_changes": ["New export functionality in dashboard"],
     "ux_impact": "POSITIVE",
     "design_system_compliant": true,
     "analytics_updated": false,
     "feature_flag_recommended": true
   }
   ```

   **Memory Pattern**: `code-review/${PR_ID}/phase-3/product-manager/user-impact`

4. **Risk Assessment**
   ```bash
   npx claude-flow memory retrieve --pattern "code-review/${PR_ID}/phase-3/*"
   npx claude-flow agent spawn --type reviewer --focus "risk-analysis"
   ```

   **Code Reviewer** analyzes:
   - What's the blast radius of this change? (how many users/services affected)
   - Worst-case failure scenario? (data loss, downtime, security breach)
   - Do we have rollback procedures? (tested and documented)
   - Should this be feature-flagged? (gradual rollout)
   - Is monitoring and alerting adequate? (can detect issues quickly)

   **Risk Matrix**:
   ```json
   {
     "blast_radius": "MEDIUM (affects 30% of users)",
     "worst_case_scenario": "Temporary export failures (no data loss)",
     "rollback_available": true,
     "rollback_tested": false,
     "feature_flag_needed": true,
     "monitoring_adequate": true,
     "overall_risk": "MEDIUM",
     "recommendation": "CONDITIONAL_APPROVE (add feature flag + test rollback)"
   }
   ```

   **Memory Pattern**: `code-review/${PR_ID}/phase-3/code-reviewer/risk-analysis`

**Outputs**:
- Integration test results
- Deployment impact report
- User impact assessment
- Risk analysis with mitigation recommendations

**Success Criteria**:
- [ ] Integration tests passing
- [ ] Deployment plan documented
- [ ] User impact understood
- [ ] Risk assessment complete with mitigation


   🤖 Generated by Claude Code Review System | [View Full Report](link)
   ```

   **Memory Storage**:
   ```bash
   npx claude-flow memory store --key "code-review/${PR_ID}/phase-4/author-notification"
   npx claude-flow hooks post-task --task-id "code-review-${PR_ID}" --export-report true
   ```

4. **Execute Decision Actions**

   Based on decision, take appropriate GitHub actions:

   **If APPROVE**:
   ```bash
   # Add approval label
   gh pr edit ${PR_NUMBER} --add-label "approved"

   # Add approval review
   gh pr review ${PR_NUMBER} --approve --body "✅ All quality checks passed. Ready to merge."

   # Queue for merge (if auto-merge enabled)
   gh pr merge ${PR_NUMBER} --auto --squash
   ```

   **If REQUEST_CHANGES**:
   ```bash
   # Add changes-requested label
   gh pr edit ${PR_NUMBER} --add-label "changes-requested" --remove-label "approved"

   # Request changes
   gh pr review ${PR_NUMBER} --request-changes --body "${REVIEW_COMMENT_MARKDOWN}"

   # Assign back to author
   gh pr edit ${PR_NUMBER} --add-assignee ${AUTHOR_USERNAME}

   # Schedule follow-up review
   npx claude-flow memory store --key "code-review/${PR_ID}/follow-up/scheduled" --value "true"
   ```

   **If REJECT**:
   ```bash
   # Add rejected label
   gh pr edit ${PR_NUMBER} --add-label "rejected"

   # Provide detailed explanation
   gh pr review ${PR_NUMBER} --request-changes --body "${DETAILED_REJECTION_REASON}"

   # Suggest alternative approaches
   gh pr comment ${PR_NUMBER} --body "Consider these alternative approaches: ${ALTERNATIVES}"
   ```

5. **Finalize Review Session**
   ```bash
   npx claude-flow hooks session-end --export-metrics true
   npx claude-flow hooks post-task --task-id "pr-${PR_ID}"
   ```

**Outputs**:
- Final review summary (comprehensive report)
- Merge decision (Approve/Request Changes/Reject)
- Author notification (GitHub comment)
- GitHub labels and status updated

**Success Criteria**:
- [ ] Final summary generated and comprehensive
- [ ] Decision clear and justified
- [ ] Author notified with actionable feedback
- [ ] GitHub PR status updated appropriately



## Scripts & Automation

### Pre-Review Initialization

```bash
#!/bin/bash
# Initialize code review workflow

PR_NUMBER="$1"
REPO="$2"  # e.g., "owner/repo"
PR_ID="${REPO}/pulls/${PR_NUMBER}"

# Fetch PR metadata via GitHub API
PR_DATA=$(gh pr view ${PR_NUMBER} --json number,title,author,files,additions,deletions)

# Setup coordination
npx claude-flow hooks pre-task --description "Code review: PR #${PR_NUMBER}"

# Initialize star topology swarm (central coordinator + specialists)
npx claude-flow swarm init --topology star --max-agents 15 --strategy specialized

# Store PR metadata
npx claude-flow memory store --key "code-review/${PR_ID}/metadata" --value "${PR_DATA}"

echo "✅ Code review initialized: PR #${PR_NUMBER}"
```

### Automated Check Gate

```bash
#!/bin/bash
# Execute Phase 1 automated checks (gate)

PR_ID="$1"

echo "🤖 Running automated checks..."

# Run checks in parallel
npx claude-flow task orchestrate --strategy parallel --max-agents 4 << EOF
  lint: npm run lint
  test: npm test
  coverage: npm run test:coverage
  build: npm run build
EOF

# Aggregate results
LINT_STATUS=$(npx claude-flow memory retrieve --key "code-review/${PR_ID}/phase-1/code-analyzer/lint-results" | jq -r '.status')
TEST_STATUS=$(npx claude-flow memory retrieve --key "code-review/${PR_ID}/phase-1/tester/test-results" | jq -r '.status')
COVERAGE_OK=$(npx claude-flow memory retrieve --key "code-review/${PR_ID}/phase-1/qa-engineer/coverage-report" | jq -r '.meets_threshold')
BUILD_STATUS=$(npx claude-flow memory retrieve --key "code-review/${PR_ID}/phase-1/code-analyzer/build-status" | jq -r '.status')

# Check if all passed
if [ "$LINT_STATUS" = "PASS" ] && [ "$TEST_STATUS" = "PASS" ] && [ "$COVERAGE_OK" = "true" ] && [ "$BUILD_STATUS" = "PASS" ]; then
  echo "✅ All automated checks passed. Proceeding to specialist reviews."
  exit 0
else
  echo "❌ Automated checks failed. Requesting fixes from author."
  gh pr review ${PR_NUMBER} --request-changes --body "Automated checks failed. Please fix before review continues."
  exit 1
fi
```

### Parallel Specialist Review

```bash
#!/bin/bash
# Execute Phase 2 specialist reviews in parallel

PR_ID="$1"

echo "👥 Spawning specialist reviewers..."

# Spawn all reviewers concurrently via Claude Flow
npx claude-flow task orchestrate --strategy parallel --max-agents 10 << EOF
  code_quality: Review code quality (readability, maintainability, best practices)
  security: Review security vulnerabilities (OWASP Top 10, secrets, auth)
  performance: Review performance (algorithms, resource usage, optimizations)
  architecture: Review architecture consistency (patterns, integration, scalability)
  documentation: Review documentation completeness (code docs, API docs, changelog)
  style: Review code style consistency
  dependencies: Review dependency security and updates
  test_coverage: Review test coverage gaps
  external_docs: Review README and migration guides
  integration: Review integration fit with existing codebase
EOF

# Wait for all reviews to complete
npx claude-flow task status --wait

echo "✅ All specialist reviews complete."
```

### Final Decision Script

```bash
#!/bin/bash
# Generate final decision and notify author

PR_ID="$1"
PR_NUMBER=$(echo $PR_ID | cut -d'/' -f3)

# Retrieve all review data
npx claude-flow memory retrieve --pattern "code-review/${PR_ID}/**" > "/tmp/${PR_ID}-reviews.json"

# Count issues by severity
CRITICAL_COUNT=$(jq '[.. | .severity? | select(. == "CRITICAL")] | length' /tmp/${PR_ID}-reviews.json)
HIGH_COUNT=$(jq '[.. | .severity? | select(. == "HIGH")] | length' /tmp/${PR_ID}-reviews.json)
BLOCKING_COUNT=$((CRITICAL_COUNT + HIGH_COUNT))

# Determine decision
if [ $CRITICAL_COUNT -gt 0 ] || [ $BLOCKING_COUNT -gt 5 ]; then
  DECISION="REJECT"
elif [ $BLOCKING_COUNT -gt 0 ]; then
  DECISION="REQUEST_CHANGES"
else
  DECISION="APPROVE"
fi

echo "📊 Review Decision: ${DECISION}"
echo "   Critical Issues: ${CRITICAL_COUNT}"
echo "   High-Severity Issues: ${HIGH_COUNT}"

# Notify author via GitHub
case $DECISION in
  APPROVE)
    gh pr review ${PR_NUMBER} --approve --body "✅ All quality checks passed. Ready to merge."
    gh pr edit ${PR_NUMBER} --add-label "approved"
    ;;
  REQUEST_CHANGES)
    gh pr review ${PR_NUMBER} --request-changes --body-file "/tmp/${PR_ID}-summary.md"
    gh pr edit ${PR_NUMBER} --add-label "changes-requested"
    ;;
  REJECT)
    gh pr review ${PR_NUMBER} --request-changes --body-file "/tmp/${PR_ID}-rejection.md"
    gh pr edit ${PR_NUMBER} --add-label "rejected"
    ;;
esac

# Finalize session
npx claude-flow hooks post-task --task-id "code-review-${PR_ID}" --export-metrics true
```



## Usage Examples

### Example 1: Small Feature PR (Simple)

```bash
# Feature: Add email validation to registration form
PR_NUMBER=245
PR_ID="acme-app/pulls/245"

# Initialize review
./init-review.sh ${PR_NUMBER} "acme/acme-app"

# Phase 1: Automated checks (5 minutes)
./automated-checks.sh ${PR_ID}
# Output: All checks passed

# Phase 2: Specialist reviews (30 minutes - small PR)
./specialist-reviews.sh ${PR_ID}
# Output: 3 minor issues (all LOW severity)

# Phase 3: Integration analysis (10 minutes)
# Output: No integration concerns, backward compatible

# Phase 4: Final decision
./final-decision.sh ${PR_ID}
# Decision: ✅ APPROVE
# Output: "All quality checks passed. 3 minor suggestions for future consideration."
```

### Example 2: Large Refactoring PR (Complex)

```bash
# Refactoring: Migrate from REST to GraphQL
PR_NUMBER=312
PR_ID="acme-app/pulls/312"

# Initialize review
./init-review.sh ${PR_NUMBER} "acme/acme-app"

# Phase 1: Automated checks (10 minutes)
./automated-checks.sh ${PR_ID}
# Output: All checks passed, coverage 94%

# Phase 2: Specialist reviews (2 hours)
./specialist-reviews.sh ${PR_ID}
# Output: 15 findings
#   - 1 HIGH/SECURITY (authentication flow changed, needs verification)
#   - 2 HIGH/PERFORMANCE (N+1 queries in new resolvers)
#   - 3 MAJOR/ARCHITECTURE (GraphQL schema design concerns)
#   - 9 MEDIUM/LOW (documentation, minor improvements)

# Phase 3: Integration analysis (1 hour)
# Output: Breaking changes for API clients, migration guide needed
# Risk: HIGH (affects all API consumers)

# Phase 4: Final decision
./final-decision.sh ${PR_ID}
# Decision: ⏸️ REQUEST CHANGES
# Output: "3 blocking issues (security + performance). Add feature flag for gradual rollout. Provide migration guide for API clients."
```

### Example 3: Security Patch PR (Critical)

```bash
# Security: Fix SQL injection vulnerability
PR_NUMBER=418
PR_ID="acme-app/pulls/418"

# Initialize expedited review
./init-review.sh ${PR_NUMBER} "acme/acme-app"

# Phase 1: Automated checks (5 minutes)
./automated-checks.sh ${PR_ID}
# Output: All checks passed

# Phase 2: Focus on security review (30 minutes)
npx claude-flow agent spawn --type security-manager --focus "comprehensive-audit"
# Output: Vulnerability fixed correctly, no new issues introduced

# Phase 3: Integration analysis (15 minutes)
# Output: Backward compatible, zero downtime deployment

# Phase 4: Fast-track approval
./final-decision.sh ${PR_ID}
# Decision: ✅ APPROVE (EXPEDITED)
# Output: "Security fix verified. No regressions. Approved for immediate merge and deployment."

# Deploy immediately
gh pr merge ${PR_NUMBER} --admin --squash
```



## Quality Checklist

Before considering code review complete, verify:

- [ ] **Phase 1**: All automated checks passing (lint, tests, coverage, build)
- [ ] **Phase 2**: All specialist reviews completed, findings categorized
- [ ] **Phase 3**: Integration impact analyzed, deployment plan documented
- [ ] **Phase 4**: Final decision made, author notified, GitHub status updated

**Memory Verification**:
- [ ] `code-review/${PR_ID}/metadata` - PR information
- [ ] `code-review/${PR_ID}/phase-1/*` - Automated check results
- [ ] `code-review/${PR_ID}/phase-2/*` - Specialist review findings
- [ ] `code-review/${PR_ID}/phase-3/*` - Integration analysis
- [ ] `code-review/${PR_ID}/phase-4/final-summary` - Comprehensive report

**Feedback Quality**:
- [ ] All feedback is specific (file, line, issue clearly identified)
- [ ] All feedback is actionable (how to fix provided)
- [ ] All feedback is constructive (not just criticism, but improvement suggestions)
- [ ] Severity is appropriate (not overstating or understating issues)

## !! SKILL COMPLETION VERIFICATION (MANDATORY) !!

**After invoking this skill, you MUST complete ALL items below before proceeding:**

### Completion Checklist

- [ ] **Agent Spawning**: Did you spawn at least 1 agent via Task()?
  - Example: `Task("Agent Name", "Task description", "agent-type-from-registry")`

- [ ] **Agent Registry Validation**: Is your agent from the registry?
  - Registry location: `claude-code-plugins/ruv-sparc-three-loop-system/agents/`
  - Valid categories: delivery, foundry, operations, orchestration, platforms, quality, research, security, specialists, tooling
  - NOT valid: Made-up agent names

- [ ] **TodoWrite Called**: Did you call TodoWrite with 5+ todos?
  - Example: `TodoWrite({ todos: [8-10 items covering all work] })`

- [ ] **Work Delegation**: Did you delegate to agents (not do work yourself)?
  - CORRECT: Agents do the implementation via Task()
  - WRONG: You write the code directly after reading skill

### Correct Pattern After Skill Invocation

```javascript
// After Skill("<skill-name>") is invoked:
[Single Message - ALL in parallel]:
  Task("Agent 1", "Description of task 1...", "agent-type-1")
  Task("Agent 2", "Description of task 2...", "agent-type-2")
  Task("Agent 3", "Description of task 3...", "agent-type-3")
  TodoWrite({ todos: [
    {content: "Task 1 description", status: "in_progress", activeForm: "Working on task 1"},
    {content: "Task 2 description", status: "pending", activeForm: "Working on task 2"},
    {content: "Task 3 description", status: "pending", activeForm: "Working on task 3"},
  ]})
```

### Wrong Pattern (DO NOT DO THIS)

```javascript
// WRONG - Reading skill and then doing work yourself:
Skill("<skill-name>")
// Then you write all the code yourself without Task() calls
// This defeats the purpose of the skill system!
```

**The skill is NOT complete until all checklist items are checked.**

## Core Principles

### 1. Automated Gates Before Human Review
**Principle**: Fast-failing automated checks (linting, tests, coverage, build) must pass before expensive specialist reviews begin. No human should review code that fails basic quality gates.

**In practice**:
- Phase 1 runs automated checks in parallel completing within 30 minutes
- Linting violations, test failures, or build errors trigger immediate author notification
- Phase 2 specialist reviews only begin after all Phase 1 checks pass green
- Automated gate prevents wasted reviewer time analyzing code with obvious defects
- Author fixes issues and re-submits triggering fresh Phase 1 run before review resumes

### 2. Parallel Specialist Reviews for Comprehensive Coverage
**Principle**: Code quality requires evaluation across multiple dimensions (security, performance, architecture, documentation) by domain experts reviewing concurrently.

**In practice**:
- Star topology spawns 10 specialist reviewers in parallel during Phase 2
- Each specialist focuses deeply on their domain without distraction from other concerns
- Security reviewer analyzes OWASP Top 10 vulnerabilities and auth/auth correctness
- Performance reviewer identifies algorithmic inefficiencies and resource leaks
- Architecture reviewer validates design patterns and integration consistency
- Findings from all specialists aggregate into comprehensive assessment

### 3. Risk-Based Decision Making with Evidence
**Principle**: Merge decisions must be deterministic based on severity-weighted findings, not subjective gut feel. Evidence drives recommendations.

**In practice**:
- Critical severity issues automatically block merge requiring fixes before approval
- High severity issues (security, performance regressions) request changes with specific remediation
- Medium severity issues conditionally approve with recommendations to address
- Low severity issues approve with suggestions for future improvement
- Decision logic codified in deterministic algorithm ensuring consistency across PRs

----------|---------|----------|
| **Skipping Automated Checks** | Proceeding directly to human review without automated validation wastes specialist time reviewing code with linting violations, failing tests, or broken builds. | Implement mandatory Phase 1 automated gate. No specialist reviews begin until all automated checks pass. Author must fix issues before review proceeds. Enforce with CI/CD pipeline checks. |
| **Single Reviewer Bottleneck** | One generalist reviewer attempts to evaluate all quality dimensions (code, security, performance, architecture) resulting in shallow review missing domain-specific issues. | Deploy star topology with 10 specialist reviewers operating in parallel. Each reviewer focuses deeply on their domain expertise. Aggregate findings into comprehensive assessment covering all dimensions. |
| **Merge Without Risk Assessment** | Approving PRs based solely on code quality without analyzing deployment impact, integration risk, or rollback complexity leads to production incidents. | Add Phase 3 integration analysis evaluating deployment impact, database migrations, backward compatibility, and rollback procedures. Risk assessment informs merge decision and deployment strategy (feature flags, gradual rollout). |

-----------|---------|----------|
| **Skipping Automated Checks** | Proceeding directly to human review without automated validation wastes specialist time reviewing code with linting violations, failing tests, or broken builds. | Implement mandatory Phase 1 automated gate. No specialist reviews begin until all automated checks pass. Author must fix issues before review proceeds. Enforce with CI/CD pipeline checks. |
| **Single Reviewer Bottleneck** | One generalist reviewer attempts to evaluate all quality dimensions (code, security, performance, architecture) resulting in shallow review missing domain-specific issues. | Deploy star topology with 10 specialist reviewers operating in parallel. Each reviewer focuses deeply on their domain expertise. Aggregate findings into comprehensive assessment covering all dimensions. |
| **Merge Without Risk Assessment** | Approving PRs based solely on code quality without analyzing deployment impact, integration risk, or rollback complexity leads to production incidents. | Add Phase 3 integration analysis evaluating deployment impact, database migrations, backward compatibility, and rollback procedures. Risk assessment informs merge decision and deployment strategy (feature flags, gradual rollout). |

## Conclusion

Comprehensive code review orchestration transforms manual, inconsistent review processes into systematic workflows that evaluate PRs across security, performance, architecture, documentation, and integration dimensions within 4 hours. The star topology coordination pattern enables 10+ specialists to review concurrently while maintaining coherence through centralized PR manager aggregation. Automated gates prevent wasted human effort by fast-failing obvious defects before expensive specialist reviews begin.

The workflow's effectiveness stems from balancing speed with thoroughness - Phase 1 automated checks complete in 30 minutes providing immediate feedback, while Phase 2 parallel specialist reviews achieve comprehensive coverage without sequential bottlenecks. The deterministic decision logic in Phase 4 eliminates subjective merge decisions, basing recommendations on severity-weighted findings rather than gut feel. This consistency builds team confidence that review quality remains high regardless of which specialists are available.

Memory coordination enables specialists to reference findings from other reviewers, preventing duplicate work and creating holistic assessments. The security reviewer can reference performance issues when evaluating authentication flows, while the architecture reviewer considers deployment complexity identified by DevOps analysis. This cross-referencing elevates individual specialist insights into collective intelligence greater than sum of parts. Teams implementing this workflow should resist the temptation to skip phases or compress timelines during crunch periods - the 4-hour duration reflects realistic minimum time for thorough multi-dimensional analysis. Rushing reviews surfaces as production incidents that cost far more than modest PR review delays.