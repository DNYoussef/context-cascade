# Skill Documentation Audit Protocol v1.0

**Purpose**: Automated audit and improvement of skill documentation completeness.
**Integrated With**: skill-forge Phase 7a, recursive-improvement meta-loop
**Last Updated**: 2025-12-17

---

## Overview

This protocol defines how the meta-loop automatically audits and improves skill documentation. It runs:
1. **During skill creation** (Phase 7a of skill-forge)
2. **Periodically via recursive-improvement** (batch auditing)
3. **On-demand via `/skill-audit` command**

---

## Tier Requirements (from REQUIRED-SECTIONS.md)

### Tier 1: Critical (MUST HAVE - 100% required)
| Section | Detection Pattern | Auto-Generate |
|---------|-------------------|---------------|
| YAML Frontmatter | `^---\s*\n.*?name:` | Yes |
| Overview | `## Overview` | Yes |
| Core Principles | `## Core Principles` or `### Principle \d` | Yes |
| When to Use | `## When to Use` or `**Use When` | Yes |
| Main Workflow | `## Workflow` or `### Phase \d` or `### Step \d` | Yes |

### Tier 2: Essential (REQUIRED - 100% target)
| Section | Detection Pattern | Auto-Generate |
|---------|-------------------|---------------|
| Pattern Recognition | `## .*Type Recognition` or `## Pattern` | Yes |
| Advanced Techniques | `## Advanced` | Yes |
| Anti-Patterns | `## .*Anti-Pattern` or `\| Anti-Pattern` | Yes |
| Practical Guidelines | `## Guidelines` or `## Best Practices` | Yes |

### Tier 3: Integration (REQUIRED - 100% target)
| Section | Detection Pattern | Auto-Generate |
|---------|-------------------|---------------|
| Cross-Skill Coordination | `## Cross-Skill` or `## Integration` | Yes |
| MCP Requirements | `## MCP` or `mcp_servers:` | Partial |
| Input/Output Contracts | `input_contract:` or `output_contract:` | Template |
| Recursive Improvement | `## Recursive Improvement` | Yes |

### Tier 4: Closure (REQUIRED - 100% target)
| Section | Detection Pattern | Auto-Generate |
|---------|-------------------|---------------|
| Examples | `## Example` | Template |
| Troubleshooting | `## Troubleshooting` | Yes |
| Conclusion | `## Conclusion` or `## Summary` | Yes |
| Completion Verification | `## .*Completion` or `- [ ]` | Yes |

---

## Audit Algorithm

```javascript
function auditSkill(skillPath) {
  const content = readFile(skillPath);
  const results = { tier1: {}, tier2: {}, tier3: {}, tier4: {}, missing: [] };

  // Check each section
  for (const [tier, sections] of Object.entries(TIER_REQUIREMENTS)) {
    for (const section of sections) {
      const found = section.patterns.some(p => p.test(content));
      results[tier][section.name] = found;
      if (!found) results.missing.push({ tier, section: section.name });
    }
  }

  // Calculate scores
  results.tier1Score = calcScore(results.tier1);
  results.tier2Score = calcScore(results.tier2);
  results.overallScore = calcOverall(results);
  results.status = determineStatus(results);

  return results;
}

function determineStatus(results) {
  if (results.tier1Score === 100 && results.tier2Score === 100) return 'COMPLETE';
  if (results.tier1Score >= 60 && results.tier2Score >= 50) return 'PARTIAL';
  return 'INCOMPLETE';
}
```

---

## Auto-Generation Templates

### Core Principles Template
```markdown
## Core Principles

[Skill Name] operates on [N] fundamental principles:

### Principle 1: [Domain-Specific Name]
[1-2 sentence explanation based on skill purpose]

In practice:
- [Practical application derived from skill workflow]
- [Another practical application]

### Principle 2: [Domain-Specific Name]
...
```

### Anti-Patterns Template
```markdown
## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **[Derived from skill domain]** | [Common mistake] | [How skill addresses it] |
| **[Another pattern]** | [What goes wrong] | [Correct approach] |
```

### Conclusion Template
```markdown
## Conclusion

[Skill Name] provides [core value proposition from Overview].

Key takeaways:
- [Derived from Core Principles]
- [Derived from Workflow]
- [Derived from When to Use]

Use this skill when [When to Use summary]. Avoid [Anti-Pattern summary].
```

---

## Integration Points

### 1. skill-forge Phase 7a (Post-Creation Audit)
After skill creation, automatically:
1. Run tier compliance check
2. Generate missing sections using templates
3. Insert sections at appropriate locations
4. Re-validate until COMPLETE or max iterations

### 2. recursive-improvement (Batch Audit)
Periodically:
1. Scan all skills in plugin directory
2. Identify INCOMPLETE skills
3. Prioritize by: usage frequency > age > category
4. Generate improvements in batches
5. Track improvement metrics in Memory MCP

### 3. On-Demand via Command
```bash
/skill-audit [skill-name]     # Audit single skill
/skill-audit --all            # Audit all skills
/skill-audit --fix            # Audit and auto-fix
/skill-audit --report         # Generate completeness report
```

---

## Metrics Tracking

Store in Memory MCP with namespace `skill-audit/`:

```yaml
skill-audit/metrics:
  total_skills: 180
  complete: 1
  partial: 22
  incomplete: 157
  avg_score: 36.5
  last_audit: 2025-12-17T16:00:00Z
  improvements_made: 0

skill-audit/history:
  - date: 2025-12-17
    before: { complete: 1, partial: 22, incomplete: 157 }
    after: { complete: X, partial: Y, incomplete: Z }
    sections_added: N
```

---

## Success Criteria

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| Tier 1 compliance | 45% | 100% | Immediate |
| Tier 2 compliance | 20% | 100% | 2 weeks |
| Tier 3 compliance | 35% | 80% | 1 month |
| Tier 4 compliance | 30% | 80% | 1 month |
| COMPLETE skills | 1 | 50+ | 2 weeks |

---

## Enforcement

This protocol is enforced at:
1. **skill-forge Phase 7a** - All new skills must pass audit
2. **recursive-improvement cycle** - Existing skills audited periodically
3. **CI/CD** - PR validation includes audit check
4. **pre-commit hook** - Optional local enforcement

Skills failing Tier 1 compliance CANNOT be marked as production-ready.

---

**Version**: 1.0.0
**Author**: Meta-loop self-improvement
**Triggered By**: Skill consolidation audit revealing 97% missing sections
