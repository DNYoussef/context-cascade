---
name: skill-builder
description: Skill for skill-builder
---

## Phase 0: Expertise Loading


# Skill Builder

## What This Skill Does

Creates production-ready Claude Code Skills with proper YAML frontmatter, progressive disclosure architecture, and complete file/folder structure. This skill guides you through building skills that Claude can autonomously discover and use across all surfaces (Claude.ai, Claude Code, SDK, API).

## Prerequisites

- Claude Code 2.0+ or Claude.ai with Skills support
- Basic understanding of Markdown and YAML
- Text editor or IDE

## Quick Start

### Creating Your First Skill

```bash
# 1. Create skill directory (MUST be at top level, NOT in subdirectories!)
mkdir -p ~/.claude/skills/my-first-skill

# 2. Create SKILL.md with proper format
cat > ~/.claude/skills/my-first-skill/SKILL.md << 'EOF'


# My First Skill

## What This Skill Does
[Your instructions here]

## Quick Start
[Basic usage]
EOF

# 3. Verify skill is detected
# Restart Claude Code or refresh Claude.ai
```


name: "Skill Name"                    # REQUIRED: Max 64 chars
description: "What this skill does    # REQUIRED: Max 1024 chars
and when Claude should use it."       # Include BOTH what & when

# ✅ CORRECT: Simple string
name: "API Builder"
description: "Creates REST APIs with Express and TypeScript."

# ✅ CORRECT: Multi-line description
name: "Full-Stack Generator"
description: "Generates full-stack applications with React frontend and Node.js backend. Use when starting new projects or scaffolding applications."

# ✅ CORRECT: Special characters quoted
name: "JSON:API Builder"
description: "Creates JSON:API compliant endpoints: pagination, filtering, relationships."

# ❌ WRONG: Missing quotes with special chars
name: API:Builder  # YAML parse error!

# ❌ WRONG: Extra fields (ignored but discouraged)
name: "My Skill"
description: "My description"
version: "1.0.0"       # NOT part of spec
author: "Me"           # NOT part of spec
tags: ["dev", "api"]   # NOT part of spec


### 📂 Directory Structure

#### Minimal Skill (Required)
```
~/.claude/skills/                    # Personal skills location
└── my-skill/                        # Skill directory (MUST be at top level!)
    └── SKILL.md                     # REQUIRED: Main skill file
```

**IMPORTANT**: Skills MUST be directly under `~/.claude/skills/[skill-name]/`.
Claude Code does NOT support nested subdirectories or namespaces!

#### Full-Featured Skill (Recommended)
```
~/.claude/skills/
└── my-skill/                        # Top-level skill directory
        ├── SKILL.md                 # REQUIRED: Main skill file
        ├── README.md                # Optional: Human-readable docs
        ├── scripts/                 # Optional: Executable scripts
        │   ├── setup.sh
        │   ├── validate.js
        │   └── deploy.py
        ├── resources/               # Optional: Supporting files
        │   ├── templates/
        │   │   ├── api-template.js
        │   │   └── component.tsx
        │   ├── examples/
        │   │   └── sample-output.json
        │   └── schemas/
        │       └── config-schema.json
        └── docs/                    # Optional: Additional documentation
            ├── ADVANCED.md
            ├── TROUBLESHOOTING.md
            └── API_REFERENCE.md
```

#### Skills Locations

**Personal Skills** (available across all projects):
```
~/.claude/skills/
└── [your-skills]/
```
- **Path**: `~/.claude/skills/` or `$HOME/.claude/skills/`
- **Scope**: Available in all projects for this user
- **Version Control**: NOT committed to git (outside repo)
- **Use Case**: Personal productivity tools, custom workflows

**Project Skills** (team-shared, version controlled):
```
<project-root>/.claude/skills/
└── [team-skills]/
```
- **Path**: `.claude/skills/` in project root
- **Scope**: Available only in this project
- **Version Control**: SHOULD be committed to git
- **Use Case**: Team workflows, project-specific tools, shared knowledge


name: "API Builder"                   # 11 chars
description: "Creates REST APIs..."   # ~50 chars


### 📝 SKILL.md Content Structure

#### Recommended 4-Level Structure

```markdown


# Your Skill Name

## Level 1: Overview (Always Read First)
Brief 2-3 sentence description of the skill.

## Prerequisites
- Requirement 1
- Requirement 2

## What This Skill Does
1. Primary function
2. Secondary function
3. Key benefit



## Level 3: Detailed Instructions (For Deep Work)

### Step-by-Step Guide

#### Step 1: Initial Setup
```bash
# Commands
```
Expected output:
```
Success message
```

#### Step 2: Configuration
- Configuration option 1
- Configuration option 2

#### Step 3: Execution
- Run the main command
- Verify results

### Advanced Options

#### Option 1: Custom Configuration
```bash
# Advanced usage
```

#### Option 2: Integration
```bash
# Integration steps
```



### 🎨 Content Best Practices

#### Writing Effective Descriptions

**Front-Load Keywords**:
```yaml
# ✅ GOOD: Keywords first
description: "Generate TypeScript interfaces from JSON schema. Use when converting schemas, creating types, or building API clients."

# ❌ BAD: Keywords buried
description: "This skill helps developers who need to work with JSON schemas by providing a way to generate TypeScript interfaces."
```

**Include Trigger Conditions**:
```yaml
# ✅ GOOD: Clear "when" clause
description: "Debug React performance issues using Chrome DevTools. Use when components re-render unnecessarily, investigating slow updates, or optimizing bundle size."

# ❌ BAD: No trigger conditions
description: "Helps with React performance debugging."
```

**Be Specific**:
```yaml
# ✅ GOOD: Specific technologies
description: "Create Express.js REST endpoints with Joi validation, Swagger docs, and Jest tests. Use when building new APIs or adding endpoints."

# ❌ BAD: Too generic
description: "Build API endpoints with proper validation and testing."
```

#### Progressive Disclosure Writing

**Keep Level 1 Brief** (Overview):
```markdown
## What This Skill Does
Creates production-ready React components with TypeScript, hooks, and tests in 3 steps.
```

**Level 2 for Common Paths** (Quick Start):
```markdown
## Quick Start
```bash
# Most common use case (80% of users)
generate-component MyComponent
```
```

**Level 3 for Details** (Step-by-Step):
```markdown
## Step-by-Step Guide

### Creating a Basic Component
1. Run generator
2. Choose template
3. Customize options
[Detailed explanations]
```

**Level 4 for Edge Cases** (Reference):
```markdown
## Advanced Configuration
For complex scenarios like HOCs, render props, or custom hooks, see [ADVANCED.md](docs/ADVANCED.md).
```



### 🔗 File References and Navigation

Claude can navigate to referenced files automatically. Use these patterns:

#### Markdown Links
```markdown
See [Advanced Configuration](docs/ADVANCED.md) for complex scenarios.
See [Troubleshooting Guide](docs/TROUBLESHOOTING.md) if you encounter errors.
```

#### Relative File Paths
```markdown
Use the template located at `resources/templates/api-template.js`
See examples in `resources/examples/basic-usage/`
```

#### Inline File Content
```markdown
## Example Configuration
See `resources/examples/config.json`:
```json
{
  "option": "value"
}
```
```

**Best Practice**: Keep SKILL.md lean (~2-5KB). Move lengthy content to separate files and reference them. Claude will load only what's needed.

`
- [ ] Contains `name` field (max 64 chars)
- [ ] Contains `description` field (max 1024 chars)
- [ ] Description includes "what" and "when"
- [ ] Ends with `---`
- [ ] No YAML syntax errors

**File Structure**:
- [ ] SKILL.md exists in skill directory
- [ ] Directory is DIRECTLY in `~/.claude/skills/[skill-name]/` or `.claude/skills/[skill-name]/`
- [ ] Uses clear, descriptive directory name
- [ ] **NO nested subdirectories** (Claude Code requires top-level structure)

**Content Quality**:
- [ ] Level 1 (Overview) is brief and clear
- [ ] Level 2 (Quick Start) shows common use case
- [ ] Level 3 (Details) provides step-by-step guide
- [ ] Level 4 (Reference) links to advanced content
- [ ] Examples are concrete and runnable
- [ ] Troubleshooting section addresses common issues

**Progressive Disclosure**:
- [ ] Core instructions in SKILL.md (~2-5KB)
- [ ] Advanced content in separate docs/
- [ ] Large resources in resources/ directory
- [ ] Clear navigation between levels

**Testing**:
- [ ] Skill appears in Claude's skill list
- [ ] Description triggers on relevant queries
- [ ] Instructions are clear and actionable
- [ ] Scripts execute successfully (if included)
- [ ] Examples work as documented


name: "My Basic Skill"
description: "One sentence what. One sentence when to use."

name: "My Intermediate Skill"
description: "Detailed what with key features. When to use with specific triggers: scaffolding, generating, building."

name: "My Advanced Skill"
description: "Comprehensive what with all features and integrations. Use when [trigger 1], [trigger 2], or [trigger 3]. Supports [technology stack]."


## Quick Start (60 seconds)

### Installation
```bash
./scripts/install.sh
```

### First Use
```bash
./scripts/quickstart.sh
```

Expected output:
```
✓ Setup complete
✓ Configuration validated
→ Ready to use
```



## Step-by-Step Guide

### 1. Initial Setup
[Detailed steps]

### 2. Core Workflow
[Main procedures]

### 3. Integration
[Integration steps]



## Scripts Reference

| Script | Purpose | Usage |
|--------|---------|-------|
| `install.sh` | Install dependencies | `./scripts/install.sh` |
| `generate.sh` | Generate code | `./scripts/generate.sh [name]` |
| `validate.sh` | Validate output | `./scripts/validate.sh` |
| `deploy.sh` | Deploy to environment | `./scripts/deploy.sh [env]` |



## Troubleshooting

### Issue: Installation Failed
**Symptoms**: Error during `install.sh`
**Cause**: Missing dependencies
**Solution**:
```bash
# Install prerequisites
npm install -g required-package
./scripts/install.sh --force
```

### Issue: Validation Errors
**Symptoms**: Validation script fails
**Solution**: See [Troubleshooting Guide](docs/TROUBLESHOOTING.md)



**Created**: 2025-10-19
**Category**: Advanced
**Difficulty**: Intermediate
**Estimated Time**: 15-30 minutes
```


name: "README Generator"
description: "Generate comprehensive README.md files for GitHub repositories. Use when starting new projects, documenting code, or improving existing READMEs."

name: "React Component Generator"
description: "Generate React functional components with TypeScript, hooks, tests, and Storybook stories. Use when creating new components, scaffolding UI, or following component architecture patterns."


## Learn More

### Official Resources
- [Anthropic Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
- [GitHub Skills Repository](https://github.com/anthropics/skills)
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)

### Community
- [Skills Marketplace](https://github.com/anthropics/skills) - Browse community skills
- [Anthropic Discord](https://discord.gg/anthropic) - Get help from community

### Advanced Topics
- Multi-file skills with complex navigation
- Skills that spawn other skills
- Integration with MCP tools
- Dynamic skill generation



## !! SKILL COMPLETION VERIFICATION (MANDATORY) !!

**After invoking this skill, you MUST complete ALL items below before proceeding:**

### Completion Checklist

- [ ] **Agent Spawning**: Did you spawn at least 1 agent via Task()?
- [ ] **Agent Registry Validation**: Is your agent from the registry?
- [ ] **TodoWrite Called**: Did you call TodoWrite with 5+ todos?
- [ ] **Work Delegation**: Did you delegate to agents (not do work yourself)?

### Correct Pattern
```javascript
[Single Message - ALL in parallel]:
  Task("Agent 1", "Task description", "agent-type")
  Task("Agent 2", "Task description", "agent-type")
  TodoWrite({ todos: [5-10 items] })
```

**Remember: Skill() -> Task() -> TodoWrite() - ALWAYS**

## Recursive Improvement Integration (v2.1)

### Eval Harness Integration

benchmark: skill_builder-benchmark-v1
  tests:
    - skill_builder-001: Basic functionality
    - skill_builder-002: Edge case handling
  minimum_scores:
    functionality: 0.85
    safety: 0.90

### Memory Namespace

namespaces:
  - skill-builder/artifacts: Skill artifacts
  - skill-builder/metrics: Performance tracking
  - improvement/audits/skill-builder: Audits

### Uncertainty Handling

confidence_check:
  if confidence >= 0.8: Proceed
  if confidence 0.5-0.8: Present options
  if confidence < 0.5: Ask questions

### Cross-Skill Coordination

Works with: **agent-creator,skill-forge,micro-skill-creator**



## Core Principles

### 1. Progressive Disclosure Architecture
Skills must scale to 100+ without context penalty. Use a 3-level hierarchy: Level 1 (metadata: name + description, ~200 chars) loads at startup for autonomous matching; Level 2 (SKILL.md body, 1-10KB) loads only when skill triggers; Level 3+ (referenced files) loads on-demand as Claude navigates. This enables installing 100+ skills with only ~6KB baseline context, loading full instructions only for active skills.

### 2. Autonomous Discoverability Through Description Design
The description field is loaded into Claude's system prompt and drives autonomous skill matching. Front-load trigger keywords, include both WHAT the skill does and WHEN to use it, and be specific about technologies. Example: "Generate TypeScript interfaces from JSON schema. Use when converting schemas, creating types, or building API clients." Good descriptions enable Claude to select the right skill without human intervention.

### 3. Progressive Complexity with Graceful Degradation
Structure SKILL.md content in 4 levels: Overview (always read first), Quick Start (fast onboarding), Detailed Instructions (deep work), and Reference (rarely needed). Users consume only what they need. Keep core instructions lean (2-5KB) and move advanced content to separate docs. Complex skills should work for both novices (guided flow) and experts (quick reference) without forcing either to wade through irrelevant content.

-----------|--------------|------------------|
| **Vague descriptions without trigger conditions** (e.g., "Helps with API development") | Claude cannot autonomously match skills without clear WHEN clauses. Generic descriptions compete with every similar skill, causing match failures. | Include explicit trigger conditions: "Generate OpenAPI 3.0 documentation from Express.js routes. Use when creating API docs, documenting endpoints, or building API specifications." Front-load keywords Claude will search for. |
| **Nested skill directories** (.claude/skills/category/my-skill/) | Claude Code only scans top-level directories under .claude/skills/. Nested structures are invisible to skill detection, causing skills to never load. | Keep all skills directly under .claude/skills/[skill-name]/ with SKILL.md at the root. No subdirectories, no namespaces, no categories. Flat structure is required. |
| **Kitchen sink SKILL.md files** (50KB+ with every detail) | Massive skill files burden context on every invocation, slow Claude's processing, and create cognitive overload. Users cannot find relevant information in walls of text. | Keep SKILL.md under 5KB with core instructions only. Move advanced topics, examples, and reference material to separate docs/ files. Link with markdown references. Claude loads files only when needed. |



## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Nested Subdirectories** | Creating skills at paths like ~/.claude/skills/category/subcategory/my-skill/. Claude Code requires top-level structure (skills MUST be directly under ~/.claude/skills/[skill-name]/). Nested skills are silently ignored and never loaded. | Always create skills at top level: ~/.claude/skills/my-skill/SKILL.md. No subdirectories or namespaces. If you need organization, use naming conventions (api-docs-generator, api-testing-framework) not folder hierarchies. |
| **Bloated SKILL.md Files** | Embedding 50KB of examples, schemas, and references directly in SKILL.md. Loads entire content into context when skill triggers, consuming 10-50KB context per skill vs 2-5KB for lean skills. Multiplied across active skills, bloats context by 5-10x. | Keep SKILL.md lean (2-5KB): overview, quick start, step-by-step guide. Move advanced content to docs/ (linked via markdown), large resources to resources/ (referenced by path), schemas to resources/schemas/ (loaded on-demand). Claude navigates to files only when needed. |
| **Generic Descriptions** | Writing descriptions without trigger keywords or "when" clauses. "A tool for API development" matches poorly vs specific queries. Reduces autonomous discovery by 70%+, requiring users to manually invoke skills Claude should have auto-selected. | Front-load keywords: "Generate OpenAPI 3.0 docs from Express.js routes." Add "when" clause: "Use when creating API docs, documenting endpoints, building API specs." Use technology names (OpenAPI, Express.js) not generic terms (API tool). Test by searching for relevant queries. |

-----------|---------|----------|
| **Vague Descriptions Without Triggers** | Writing generic descriptions like "Helps with API development" without clear WHEN clauses. Claude cannot autonomously match skills without explicit trigger conditions. Skill rarely triggers on relevant queries. | Include explicit trigger conditions in description: "Generate OpenAPI 3.0 docs from Express routes. Use when creating API docs, documenting endpoints, building specs." Front-load keywords Claude searches for. Test description by searching for relevant queries. |
| **Nested Skill Directories** | Creating skills at paths like ~/.claude/skills/category/subcategory/my-skill/. Claude Code requires top-level structure - nested skills are silently ignored and never loaded. | Always create skills directly under ~/.claude/skills/[skill-name]/SKILL.md. No subdirectories or namespaces. If organization needed, use naming conventions (api-docs-generator, api-testing-framework) not folder hierarchies. Flat structure is non-negotiable. |
| **Bloated SKILL.md Files** | Embedding 50KB of examples, schemas, references directly in SKILL.md. Entire content loads into context when skill triggers, consuming 10-50KB per skill vs 2-5KB for lean skills. Multiplied across active skills, bloats context 5-10x. | Keep SKILL.md lean (2-5KB): overview, quick start, step-by-step guide. Move advanced content to docs/ (linked markdown), resources to resources/ (referenced by path), schemas to resources/schemas/ (loaded on-demand). Claude navigates files only when needed. |

---

## Conclusion

Skill Builder transforms the process of creating Claude Code skills from guesswork into systematic engineering. By codifying the official specification (YAML frontmatter, progressive disclosure, directory structure) and best practices (keyword-rich descriptions, lean SKILL.md, on-demand file loading), this skill ensures every created skill meets production standards for discovery, context efficiency, and usability.

The progressive disclosure architecture is the key innovation that enables Claude Code to scale to 100+ skills without context collapse. By loading only metadata at startup (6KB for 100 skills), full content on trigger (2-5KB per active skill), and referenced files on-demand (variable), the system maintains low context overhead while providing deep functionality when needed. Violating this architecture through bloated SKILL.md files or nested directories breaks the scaling properties.

Use this skill whenever creating new skills for Claude Code. Follow the 3-level structure religiously: lean metadata for discovery, concise SKILL.md for core instructions, referenced files for advanced content. Optimize descriptions for autonomous matching by front-loading keywords and including explicit "when" clauses. Validate YAML compliance before deployment. Skills built with this methodology integrate seamlessly into the Claude Code ecosystem and scale efficiently across 100+ skill libraries.