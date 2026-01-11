---

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

name: Bug Report
about: Create a report to help us improve
title: '[BUG] '
labels: bug, needs-triage
assignees: ''
---

# Bug Report

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Bug Description

<!-- A clear and concise description of the bug -->

## Steps to Reproduce

<!-- Detailed steps to reproduce the behavior -->

1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior

<!-- What you expected to happen -->

## Actual Behavior

<!-- What actually happened -->

## Screenshots/Videos

<!-- If applicable, add screenshots or videos to help explain the problem -->

## Environment

<!-- Please complete the following information -->

**Platform:**
- OS: [e.g., Windows 11, macOS 13.0, Ubuntu 22.04]
- Browser: [e.g., Chrome 120, Firefox 121, Safari 17]
- Version: [e.g., v2.1.0]

**Runtime:**
- Node.js: [e.g., v18.19.0]
- npm/yarn: [e.g., npm 10.2.3]
- Other relevant versions:

## Error Messages/Logs

<!-- Include any relevant error messages or logs -->

```
Paste error messages or logs here
```

## Code Snippet

<!-- If applicable, provide a minimal code example that reproduces the bug -->

```javascript
// Your code here
```

## Severity/Impact

<!-- Select one -->

- [ ] Critical - Application crashes or data loss
- [ ] High - Major functionality broken
- [ ] Medium - Feature partially broken
- [ ] Low - Minor issue or cosmetic problem

## Frequency

<!-- How often does this occur? -->

- [ ] Always (100%)
- [ ] Frequently (>50%)
- [ ] Sometimes (10-50%)
- [ ] Rarely (<10%)
- [ ] Once

## Workaround

<!-- Is there a workaround available? If yes, describe it -->

## Additional Context

<!-- Add any other context about the problem here -->

## Possible Solution

<!-- If you have suggestions on how to fix the bug, describe them here -->

## Related Issues/PRs

<!-- Link to related issues or PRs -->

## Checklist

- [ ] I have searched existing issues to ensure this is not a duplicate
- [ ] I have included all relevant information above
- [ ] I have provided steps to reproduce
- [ ] I have included error messages/logs
- [ ] I have specified the environment details
- [ ] I can reproduce this bug consistently

---

<!--
For maintainers:
- Assign appropriate labels
- Set milestone if applicable
- Assign to relevant team member
- Add to project board
-->


---
*Promise: `<promise>ISSUE_TEMPLATE_BUG_VERIX_COMPLIANT</promise>`*
