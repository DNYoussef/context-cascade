# Release Notes Template

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


## Version {{VERSION}}

**Release Date**: {{DATE}}

---

## 🎯 Highlights

{{HIGHLIGHTS}}

---

## 💥 Breaking Changes

{{BREAKING_CHANGES}}

**Migration Guide**: See [MIGRATION.md](./MIGRATION.md) for upgrade instructions.

---

## 🚀 New Features

{{FEATURES}}

---

## ✨ Enhancements

{{ENHANCEMENTS}}

---

## 🐛 Bug Fixes

{{BUG_FIXES}}

---

## ⚡ Performance Improvements

{{PERFORMANCE}}

---

## 📚 Documentation

{{DOCUMENTATION}}

---

## 🔒 Security

{{SECURITY}}

---

## 🛠️ Technical Details

### Supported Platforms
- Linux (x64, arm64)
- macOS (x64, arm64)
- Windows (x64, arm64)

### Dependencies
{{DEPENDENCIES}}

### Known Issues
{{KNOWN_ISSUES}}

---

## 📦 Installation

### npm
```bash
npm install {{PACKAGE_NAME}}@{{VERSION}}
```

### yarn
```bash
yarn add {{PACKAGE_NAME}}@{{VERSION}}
```

### pnpm
```bash
pnpm add {{PACKAGE_NAME}}@{{VERSION}}
```

### Docker
```bash
docker pull {{DOCKER_IMAGE}}:{{VERSION}}
```

---

## 🔄 Upgrade Instructions

### From {{PREVIOUS_VERSION}} to {{VERSION}}

1. Update package version
2. Run migration scripts if needed
3. Update configuration files
4. Test thoroughly before production deployment

See [MIGRATION.md](./MIGRATION.md) for detailed instructions.

---

## 👥 Contributors

{{CONTRIBUTORS}}

---

## 📊 Release Statistics

- **Commits**: {{COMMIT_COUNT}}
- **Pull Requests**: {{PR_COUNT}}
- **Contributors**: {{CONTRIBUTOR_COUNT}}
- **Files Changed**: {{FILES_CHANGED}}

---

## 🔗 Links

- [Full Changelog]({{CHANGELOG_URL}})
- [Documentation]({{DOCS_URL}})
- [GitHub Release]({{GITHUB_RELEASE_URL}})
- [Migration Guide]({{MIGRATION_URL}})

---

**Need Help?** Open an issue on [GitHub]({{ISSUES_URL}}) or join our [community]({{COMMUNITY_URL}}).


---
*Promise: `<promise>RELEASE_NOTES_VERIX_COMPLIANT</promise>`*
