# FORMAT COMPLIANCE AUDIT: ruv-sparc vs Anthropic Official Specs

**Audit Date**: 2025-12-30
**Auditor**: Claude Code (Opus 4.5)
**Scope**: Skills, Agents, Plugins formatting compliance

---

## EXECUTIVE SUMMARY

| Component | Official Format | Current Format | Compliant? | Severity |
|-----------|-----------------|----------------|------------|----------|
| **Skills** | Simple YAML frontmatter | Extended VERIX notation | PARTIAL | MEDIUM |
| **Agents** | Simple YAML frontmatter | Extended with RBAC/budget | PARTIAL | MEDIUM |
| **plugin.json** | Specific schema | Custom schema | NO | HIGH |
| **ZIP packaging** | NOT for Claude Code | N/A (not used) | N/A | N/A |

**KEY FINDING**: Skills are NOT supposed to be ZIP files. ZIPs are only for Claude.ai web and Claude Desktop, NOT Claude Code CLI. Your current directory-based SKILL.md approach is CORRECT.

---

## 1. SKILLS FORMAT COMPARISON

### OFFICIAL ANTHROPIC FORMAT (from code.claude.com/docs/en/skills.md)

```yaml
---
name: skill-name
description: When to use this skill
allowed-tools: Read, Write, Bash
---

# Skill Title

Your skill content, instructions, and guidance here.
No special notation required.
```

**Required fields**: `name`, `description`
**Optional fields**: `allowed-tools`
**Content**: Plain markdown

### CURRENT ruv-sparc FORMAT

```yaml
---
name: feature-dev-complete
version: 1.1.0
description: |
  [assert|neutral] Complete feature development lifecycle... [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- feature
- development
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "..."
    second_order: "..."
    third_order: "..."
---

/*============================================================================*/
/* FEATURE-DEV-COMPLETE SKILL :: VERILINGUA x VERIX EDITION                  */
/*============================================================================*/

[define|neutral] SKILL := {...} [ground:given] [conf:1.0] [state:confirmed]
```

### DISCREPANCIES

| Field | Official | Current | Issue |
|-------|----------|---------|-------|
| `name` | Required | Present | OK |
| `description` | Plain text | VERIX notation | MAY NOT PARSE |
| `allowed-tools` | Official field | NOT USED | Missing |
| `version` | NOT in spec | Present | EXTRA FIELD |
| `category` | NOT in spec | Present | EXTRA FIELD |
| `tags` | NOT in spec | Present | EXTRA FIELD |
| `author` | NOT in spec | Present | EXTRA FIELD |
| `cognitive_frame` | NOT in spec | Present | EXTRA FIELD |
| Content | Plain markdown | VERIX notation + /* */ comments | MAY NOT PARSE |

---

## 2. AGENTS/SUBAGENTS FORMAT COMPARISON

### OFFICIAL ANTHROPIC FORMAT (from code.claude.com/docs/en/sub-agents.md)

```yaml
---
name: subagent-name
description: When to use this subagent
tools: Read, Write, Edit, Bash
model: sonnet
permissionMode: default
skills: skill1, skill2
---

Your subagent's system prompt goes here. This text defines the role,
capabilities, and approach to solving problems.
```

**Required fields**: `name`, `description`
**Optional fields**: `tools`, `model`, `permissionMode`, `skills`
**Content**: System prompt in plain text

### CURRENT ruv-sparc FORMAT

```yaml
---
name: "specification"
type: "general"
color: "#4A90D9"
description: |
  [assert|neutral] specification agent... [ground:given] [conf:0.85]
capabilities:
  - general_tasks
priority: "medium"
identity:
  agent_id: "specification-20251229"
  role: "agent"
  role_confidence: 0.85
  role_reasoning: "[ground:capability-analysis] [conf:0.85]"
rbac:
  allowed_tools: [Read, Write, Edit, Bash]
  denied_tools: []
  path_scopes: [src/**, tests/**]
  api_access: [memory-mcp]
budget:
  max_tokens_per_session: 200000
  max_cost_per_day: 30
  currency: "USD"
metadata:
  category: "delivery"
  version: "1.0.0"
  verix_compliant: true
  created_at: "2025-12-29T09:17:48.704751"
---
```

### DISCREPANCIES

| Field | Official | Current | Issue |
|-------|----------|---------|-------|
| `name` | Required | Present | OK |
| `description` | Plain text | VERIX notation | MAY NOT PARSE |
| `tools` | Official field | NOT USED (uses rbac.allowed_tools) | WRONG FIELD NAME |
| `model` | Official field | NOT USED | Missing |
| `permissionMode` | Official field | NOT USED | Missing |
| `skills` | Official field | NOT USED | Missing |
| `type` | NOT in spec | Present | EXTRA FIELD |
| `color` | NOT in spec | Present | EXTRA FIELD |
| `capabilities` | NOT in spec | Present | EXTRA FIELD |
| `priority` | NOT in spec | Present | EXTRA FIELD |
| `identity` | NOT in spec | Present | EXTRA FIELD |
| `rbac` | NOT in spec | Present | EXTRA FIELD |
| `budget` | NOT in spec | Present | EXTRA FIELD |
| `metadata` | NOT in spec | Present | EXTRA FIELD |

---

## 3. PLUGIN.JSON FORMAT COMPARISON

### OFFICIAL ANTHROPIC FORMAT (from code.claude.com/docs/en/plugins-reference.md)

```json
{
  "name": "plugin-name",
  "description": "Brief description",
  "version": "1.0.0",
  "author": {"name": "Your Name"},
  "commands": ["./commands/"],
  "agents": "./agents/",
  "skills": "./skills/",
  "hooks": "./hooks/hooks.json",
  "mcpServers": "./mcp-config.json",
  "lspServers": "./.lsp.json"
}
```

### CURRENT ruv-sparc FORMAT

```json
{
  "name": "context-cascade",
  "version": "3.0.0",
  "description": "...",
  "author": {...},
  "license": "Apache-2.0",
  "repository": "...",
  "homepage": "...",
  "keywords": [...],
  "claudeCode": {
    "minVersion": "1.0.0",
    "compatibility": "2024.01+"
  },
  "contents": {
    "playbooks": {...},
    "skills": {...},
    "agents": {...},
    "commands": {...},
    "mcpServers": {...}
  },
  "features": [...],
  "installation": {...},
  "documentation": {...},
  "maintainers": [...]
}
```

### DISCREPANCIES

| Field | Official | Current | Issue |
|-------|----------|---------|-------|
| `name` | Required | Present | OK |
| `description` | Required | Present | OK |
| `version` | Required | Present | OK |
| `author` | Required | Present | OK |
| `commands` | Path string | NOT PRESENT (embedded in contents) | WRONG FORMAT |
| `agents` | Path string | NOT PRESENT (embedded in contents) | WRONG FORMAT |
| `skills` | Path string | NOT PRESENT (embedded in contents) | WRONG FORMAT |
| `hooks` | Path string | NOT PRESENT | Missing |
| `mcpServers` | Path string | NOT PRESENT (embedded in contents) | WRONG FORMAT |
| `claudeCode` | NOT in spec | Present | EXTRA FIELD |
| `contents` | NOT in spec | Present | EXTRA FIELD |
| `features` | NOT in spec | Present | EXTRA FIELD |
| `installation` | NOT in spec | Present | EXTRA FIELD |
| `documentation` | NOT in spec | Present | EXTRA FIELD |

---

## 4. WHAT IS CORRECT IN CURRENT SYSTEM

1. **Directory Structure**: Using directories with SKILL.md files (NOT ZIPs) is CORRECT
2. **Agent Location**: Agents in `agents/` directory is CORRECT
3. **Plugin Location**: `.claude-plugin/plugin.json` location is CORRECT
4. **CLAUDE.md**: Multiple CLAUDE.md files in hierarchy is CORRECT
5. **Markdown Format**: Using markdown for skills/agents is CORRECT

---

## 5. WHAT NEEDS FIXING

### CRITICAL (Will likely break with official tooling)

1. **plugin.json schema**: Completely wrong structure
   - Must use `"commands": "./commands/"` not `contents.commands`
   - Must use `"agents": "./agents/"` not `contents.agents`
   - Must use `"skills": "./skills/"` not `contents.skills`

### HIGH (May cause parsing issues)

2. **Agent field names**:
   - Rename `rbac.allowed_tools` to `tools`
   - Add `model` field if needed
   - Remove or namespace custom fields

3. **Skill field names**:
   - Add `allowed-tools` if restricting tool access
   - Consider moving custom fields to a `custom:` namespace

### MEDIUM (May cause confusion but won't break)

4. **VERIX notation in descriptions**:
   - Official parser expects plain text descriptions
   - Move VERIX notation to content body, not frontmatter

5. **Extra metadata fields**:
   - Consider prefixing with `x-` for custom extensions
   - Example: `x-cognitive-frame`, `x-verix-compliant`

---

## 6. MIGRATION PLAN

### Phase 1: plugin.json Fix (IMMEDIATE)

```json
{
  "name": "context-cascade",
  "description": "Context-saving nested plugin architecture",
  "version": "3.0.0",
  "author": {"name": "DNYoussef"},
  "commands": "./commands/",
  "agents": "./agents/",
  "skills": "./skills/",
  "hooks": "./hooks/hooks.json",
  "mcpServers": "./.mcp.json",
  "x-claudeCode": {
    "minVersion": "1.0.0"
  },
  "x-contents": {
    "playbooks": {"count": 30},
    "skills": {"count": 196},
    "agents": {"count": 211},
    "commands": {"count": 223}
  }
}
```

### Phase 2: Agent Field Standardization

Transform from:
```yaml
rbac:
  allowed_tools: [Read, Write, Edit, Bash]
```

To:
```yaml
tools: Read, Write, Edit, Bash
x-rbac:
  denied_tools: []
  path_scopes: [src/**, tests/**]
```

### Phase 3: Skill Field Standardization

Transform from:
```yaml
description: |
  [assert|neutral] Complete feature... [ground:given] [conf:0.95]
```

To:
```yaml
description: Complete feature development lifecycle from research to deployment
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
x-verix:
  assertion: "[assert|neutral] Complete feature... [ground:given] [conf:0.95]"
```

### Phase 4: Content Cleanup

- Move /* */ comment blocks to proper markdown
- Keep VERIX notation in body content (optional extension)
- Ensure descriptions are plain text for parsing

---

## 7. RISK ASSESSMENT

| If Not Fixed | Risk Level | Impact |
|--------------|------------|--------|
| plugin.json schema | HIGH | Plugin may not load with official tooling |
| Wrong field names | MEDIUM | Agents may not inherit correct tools |
| VERIX in descriptions | LOW | Descriptions may display with notation |
| Extra metadata | LOW | Ignored by parser, no functional impact |

---

## 8. RECOMMENDATION

**Option A: Full Compliance Migration** (Recommended if using official marketplace)
- Reformat all 196 skills, 211 agents, and plugin.json
- Estimated effort: High (automated script possible)
- Benefit: Full compatibility with Anthropic tooling

**Option B: Hybrid Approach** (Recommended for private use)
- Fix plugin.json to official schema
- Add official fields (`tools`, `allowed-tools`) alongside custom fields
- Keep custom extensions with `x-` prefix
- Benefit: Works with official tooling while preserving custom features

**Option C: Keep As-Is** (Not recommended)
- Risk breaking with future Anthropic updates
- May not work with plugin marketplace
- Custom tooling required to process files

---

## APPENDIX: Official Documentation Sources

1. Skills: https://code.claude.com/docs/en/skills.md
2. Subagents: https://code.claude.com/docs/en/sub-agents.md
3. Plugins: https://code.claude.com/docs/en/plugins.md
4. Plugins Reference: https://code.claude.com/docs/en/plugins-reference.md
5. Memory (CLAUDE.md): https://code.claude.com/docs/en/memory.md

---

*Audit conducted using Claude Code Opus 4.5 with web search verification*
