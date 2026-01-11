# Required SKILL.md Sections (v2.3)

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



This document defines the MANDATORY sections every skill must include to be considered complete.

## Purpose

Skills missing these sections are incomplete and prone to the same documentation gaps discovered during the landing-page-generator v2.0 enhancement. Following this checklist ensures skills are fully documented from the start.

---

## Section Tiers

### Tier 1: Critical (MUST HAVE)

| Section | Purpose | Format |
|---------|---------|--------|
| **YAML Frontmatter** | Discoverability, version, triggers | `---\nname:\nversion:\ndescription:\ntriggers:\n---` |
| **Overview** | Philosophy, methodology, value proposition | 2-4 paragraphs explaining WHY the skill exists |
| **Core Principles** | Fundamental operating principles | 3-5 principles with "In practice:" bullets |
| **When to Use** | Clear activation criteria | "Use When:" + "Do Not Use When:" bullets |
| **Main Workflow** | The core procedure | Phases with Purpose, Agent, Input/Output contracts |

### Tier 2: Essential (REQUIRED)

| Section | Purpose | Format |
|---------|---------|--------|
| **Pattern Recognition** | Different input types/variations | Named patterns with characteristics + key focus |
| **Advanced Techniques** | Sophisticated approaches | Audience optimization, multi-model, edge cases |
| **Common Anti-Patterns** | What to avoid | Table: Anti-Pattern - Problem - Solution |
| **Practical Guidelines** | Decision guidance | Full vs quick mode, checkpoints, trade-offs |

### Tier 3: Integration (REQUIRED)

| Section | Purpose | Format |
|---------|---------|--------|
| **Cross-Skill Coordination** | Ecosystem integration | Upstream/Downstream/Parallel skills |
| **MCP Requirements** | Dependencies with rationale | Required/Optional with WHY explanations |
| **Input/Output Contracts** | Clear interfaces | YAML with required/optional params |
| **Recursive Improvement** | Meta-loop integration | Role, eval harness, memory namespace |

### Tier 4: Closure (REQUIRED)

| Section | Purpose | Format |
|---------|---------|--------|
| **Examples** | Concrete usage | 2-3 full scenarios with Task() calls |
| **Troubleshooting** | Issue resolution | Table: Issue - Solution |
| **Conclusion** | Summary and takeaways | 2-3 paragraphs reinforcing key principles |
| **Completion Verification** | Final checklist | Checkbox list of completion criteria |

---

## Phase 7 Validation Checklist

Before considering ANY skill complete, verify:

### Tier 1 Checklist
- [ ] YAML frontmatter has full description (not just name)
- [ ] Overview explains philosophy and methodology
- [ ] Core Principles section has 3-5 principles with practical guidance
- [ ] When to Use has clear use/don't-use criteria
- [ ] Main Workflow has detailed phases with contracts

### Tier 2 Checklist
- [ ] Pattern Recognition covers different input types
- [ ] Advanced Techniques includes sophisticated approaches
- [ ] Common Anti-Patterns has problem-solution tables
- [ ] Practical Guidelines includes decision guides

### Tier 3 Checklist
- [ ] Cross-Skill Coordination documents ecosystem integration
- [ ] MCP Requirements explains WHY each is needed
- [ ] Input/Output Contracts are clearly specified in YAML
- [ ] Recursive Improvement Integration is documented

### Tier 4 Checklist
- [ ] Examples include 2-3 concrete scenarios
- [ ] Troubleshooting addresses common issues
- [ ] Conclusion summarizes skill value
- [ ] Completion Verification checklist is present

---

## Example Section Templates

### Core Principles Template

```markdown
## Core Principles

[Skill Name] operates on [N] fundamental principles:

### Principle 1: [Principle Name]

[1-2 sentence explanation of the principle]

In practice:
- [Practical application 1]
- [Practical application 2]
- [Practical application 3]

### Principle 2: [Principle Name]
...
```

### Pattern Recognition Template

```markdown
## [Domain] Type Recognition

Different [input types] require different approaches:

### [Pattern Name 1]
**Patterns**: "[trigger word 1]", "[trigger word 2]"
**Common characteristics**:
- [Characteristic 1]
- [Characteristic 2]

**Key focus**:
- [What to focus on for this pattern]

**Approach**: [Framework or methodology to use]

### [Pattern Name 2]
...
```

### Anti-Patterns Template

```markdown
## Common Anti-Patterns

Avoid these common mistakes:

### [Category] Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **[Name]** | [What goes wrong] | [How to fix] |
| **[Name]** | [What goes wrong] | [How to fix] |
```

### Cross-Skill Coordination Template

```markdown
## Cross-Skill Coordination

[Skill Name] works with other skills in the ecosystem:

### Upstream Skills (provide input)

| Skill | When to Use First | What It Provides |
|-------|------------------|------------------|
| `skill-name` | [Condition] | [What it provides] |

### Downstream Skills (use output)

| Skill | When to Use After | What It Does |
|-------|------------------|--------------|
| `skill-name` | [Condition] | [What it does] |

### Parallel Skills (run alongside)

| Skill | When to Run Together | How They Coordinate |
|-------|---------------------|---------------------|
| `skill-name` | [Condition] | [Coordination method] |
```

---

## Quality Standards

| Metric | Minimum | Target |
|--------|---------|--------|
| Tier 1 sections | 100% | 100% |
| Tier 2 sections | 100% | 100% |
| Tier 3 sections | 100% | 100% |
| Tier 4 sections | 100% | 100% |
| Core Principles | 3 | 5 |
| Pattern Types | 2 | 4-6 |
| Anti-Pattern Tables | 1 | 3-4 |
| Examples | 2 | 3 |

**Skills missing ANY Tier 1 or Tier 2 section are INCOMPLETE and must be enhanced.**

---

## Enforcement

This checklist is enforced at:
1. **Phase 7 Validation** - Skill-forge checks for all sections
2. **Skill Auditor** - Audits existing skills for completeness
3. **CI/CD** - Automated validation before merge

When skill-forge creates a skill, it MUST generate ALL sections. If time-constrained, generate skeleton sections with TODO markers that can be filled in iteratively.

---

**Last Updated**: 2025-12-17
**Version**: 2.3.0
**Triggered By**: Landing-page-generator v2.0 enhancement revealed missing sections


---
*Promise: `<promise>REQUIRED_SECTIONS_VERIX_COMPLIANT</promise>`*
