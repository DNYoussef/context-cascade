# Pull Request Template

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## CRITICAL: GITHUB OPERATIONS SAFETY GUARDRAILS

**BEFORE any GitHub operation, validate**:
- [ ] Branch protection rules respected (required reviews, status checks)
- [ ] No force-push to protected branches (main, master, release/*)
- [ ] PR template completed (description, tests, screenshots)
- [ ] CI checks passing (build, lint, test, security scan)
- [ ] Code review approved by domain experts

**NEVER**:
- Merge without passing CI checks
- Delete branches with unmerged commits
- Bypass CODEOWNERS approval requirements
- Commit secrets or sensitive data (use .gitignore + pre-commit hooks)
- Force-push to shared branches

**ALWAYS**:
- Use conventional commits (feat:, fix:, refactor:, docs:)
- Link PRs to issues for traceability
- Update CHANGELOG.md with user-facing changes
- Tag releases with semantic versioning (vX.Y.Z)
- Document breaking changes in PR description

**Evidence-Based Techniques for GitHub Operations**:
- **Program-of-Thought**: Model PR workflow as state machine (draft -> review -> approved -> merged)
- **Retrieval-Augmented**: Query similar PRs for review patterns
- **Chain-of-Thought**: Trace commit history for root cause analysis
- **Self-Consistency**: Apply same review checklist across all PRs


## Description

<!-- Provide a brief description of the changes in this PR -->

## Type of Change

<!-- Mark the relevant option with an "x" -->

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring
- [ ] Configuration change
- [ ] Dependency update

## Related Issues

<!-- Link to related issues using #issue_number -->

Fixes #
Closes #
Related to #

## Changes Made

<!-- List the specific changes made in this PR -->

-
-
-

## Testing

### Test Coverage

- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] E2E tests added/updated
- [ ] Manual testing performed

### Test Results

<!-- Describe the testing performed and results -->

```
# Paste test output here
```

## Screenshots/Videos (if applicable)

<!-- Add screenshots or videos demonstrating the changes -->

## Performance Impact

<!-- Describe any performance implications -->

- [ ] No performance impact
- [ ] Performance improved
- [ ] Performance degraded (explain why this is acceptable)

### Benchmark Results

<!-- If applicable, add benchmark comparisons -->

## Security Considerations

- [ ] No security impact
- [ ] Security review completed
- [ ] Security vulnerabilities addressed

### Security Checklist

- [ ] No sensitive data exposed
- [ ] Input validation implemented
- [ ] Authentication/authorization checked
- [ ] Dependencies scanned for vulnerabilities
- [ ] Secrets properly managed (not hardcoded)

## Breaking Changes

<!-- List any breaking changes and migration instructions -->

## Documentation

- [ ] README updated
- [ ] API documentation updated
- [ ] Code comments added/updated
- [ ] CHANGELOG updated

## Deployment Notes

<!-- Any special deployment considerations -->

- [ ] Database migrations required
- [ ] Environment variables added/changed
- [ ] Configuration changes needed
- [ ] Deployment order matters

### Environment Variables

<!-- List new or changed environment variables -->

```env
# Example
NEW_API_KEY=your-api-key-here
```

## Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added in hard-to-understand areas
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added and passing
- [ ] All CI checks passing
- [ ] Backward compatibility maintained (or breaking changes documented)
- [ ] Reviewed for accessibility (if UI changes)
- [ ] Mobile responsiveness verified (if UI changes)

## Reviewer Guidelines

<!-- Instructions for reviewers -->

### Focus Areas

<!-- Areas that need special attention during review -->

-
-

### Testing Instructions

<!-- Step-by-step testing instructions for reviewers -->

1.
2.
3.

## Post-Merge Actions

<!-- Actions to take after merging -->

- [ ] Deploy to staging
- [ ] Notify team
- [ ] Update project board
- [ ] Close related issues

## Additional Context

<!-- Add any other context about the PR here -->

---

**Estimated Review Time**: <!-- e.g., 30 minutes -->

**Reviewers**: @username1 @username2

**Labels**: <!-- e.g., enhancement, bug, documentation -->

<!--
Template Tips:
- Be concise but thorough
- Include visual aids when helpful
- Reference related work
- Highlight risks or concerns
- Make reviewer's job easier
-->


---
*Promise: `<promise>PULL_REQUEST_TEMPLATE_VERIX_COMPLIANT</promise>`*
