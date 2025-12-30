# MIGRATION MASTER PLAN: Anthropic Format Compliance

## ULTRATHINK SEQUENTIAL ANALYSIS

---

### THOUGHT 1: Problem Decomposition

**What are we actually solving?**

The ruv-sparc-three-loop-system plugin has 660+ components that deviate from Anthropic's official Claude Code specifications. The deviations fall into three categories:

1. **Structural** - Wrong JSON schema in plugin.json
2. **Field-level** - Wrong/missing YAML frontmatter fields
3. **Content-level** - VERIX notation in places expecting plain text

**Why does this matter?**

- Official Claude Code tooling may fail to parse non-compliant files
- Plugin marketplace submission will be rejected
- Future Anthropic updates may break functionality
- Other developers cannot use standard tools with this plugin

**What's the scope?**

| Component | Count | Files Affected |
|-----------|-------|----------------|
| plugin.json | 1 | 1 file |
| Skills | 196 | 196 SKILL.md files |
| Agents | 211 | 211 .md files |
| Commands | 223 | ~223 .md files |
| TOTAL | 631 | ~631 files |

---

### THOUGHT 2: Constraint Analysis

**Hard Constraints (Cannot Violate)**

1. Must preserve ALL existing functionality
2. Must maintain backward compatibility with custom tooling
3. Cannot lose VERIX/VERILINGUA metadata (valuable for advanced features)
4. Must be reversible (rollback capability)
5. ASCII-only (no Unicode) - Windows compatibility

**Soft Constraints (Should Respect)**

1. Minimize manual intervention
2. Complete in single automated run
3. Preserve git history readability
4. Keep file sizes reasonable

**Trade-offs Identified**

| Trade-off | Option A | Option B | Decision |
|-----------|----------|----------|----------|
| Metadata preservation | Delete custom fields | Namespace with x- | **Option B** |
| Description format | Strip VERIX entirely | Move to x-verix field | **Option B** |
| Content format | Remove /* */ comments | Convert to markdown | **Option B** |
| Validation | Strict official only | Hybrid validation | **Hybrid** |

---

### THOUGHT 3: Dependency Graph Analysis

**Migration Order Dependencies**

```
Phase 0: Backup
    |
    v
Phase 1: plugin.json (no dependencies)
    |
    v
Phase 2: Skills (depends on Phase 1 for validation)
    |
    v
Phase 3: Agents (depends on Phase 2 - agents reference skills)
    |
    v
Phase 4: Commands (depends on Phase 3 - commands reference agents)
    |
    v
Phase 5: Validation (depends on all prior phases)
    |
    v
Phase 6: Documentation update
```

**Why this order?**

1. plugin.json defines WHERE to find components - fix first
2. Skills are referenced BY agents - fix before agents
3. Agents are referenced BY commands - fix before commands
4. Validation needs all components fixed to verify
5. Documentation describes the final state

---

### THOUGHT 4: Transformation Rules Definition

**RULE SET 1: plugin.json Transformation**

```
INPUT:
{
  "contents": {
    "skills": {"count": 196},
    "agents": {"count": 211},
    "commands": {"count": 223}
  },
  "claudeCode": {...}
}

OUTPUT:
{
  "skills": "./skills/",
  "agents": "./agents/",
  "commands": "./commands/",
  "hooks": "./hooks/hooks.json",
  "mcpServers": "./.mcp.json",
  "x-contents": {"count": {...}},
  "x-claudeCode": {...}
}
```

**RULE SET 2: Skill YAML Transformation**

```
INPUT FIELDS:
- name (keep)
- version (move to x-version)
- description with VERIX (extract plain text, move VERIX to x-verix)
- category (move to x-category)
- tags (move to x-tags)
- author (move to x-author)
- cognitive_frame (move to x-cognitive-frame)

OUTPUT FIELDS:
- name (required)
- description (plain text only)
- allowed-tools (ADD - derive from content analysis or default)
- x-version (preserved)
- x-category (preserved)
- x-tags (preserved)
- x-author (preserved)
- x-cognitive-frame (preserved)
- x-verix (preserved assertion)
```

**RULE SET 3: Agent YAML Transformation**

```
INPUT FIELDS:
- name (keep)
- type (move to x-type)
- color (move to x-color)
- description with VERIX (extract plain text)
- capabilities (move to x-capabilities)
- priority (move to x-priority)
- identity (move to x-identity)
- rbac.allowed_tools (RENAME to tools)
- rbac.* other (move to x-rbac)
- budget (move to x-budget)
- metadata (move to x-metadata)

OUTPUT FIELDS:
- name (required)
- description (plain text only)
- tools (from rbac.allowed_tools, comma-separated string)
- model (ADD - default "sonnet" or derive from context)
- x-type (preserved)
- x-color (preserved)
- x-capabilities (preserved)
- x-priority (preserved)
- x-identity (preserved)
- x-rbac (preserved minus allowed_tools)
- x-budget (preserved)
- x-metadata (preserved)
- x-verix (preserved assertion)
```

**RULE SET 4: Content Body Transformation**

```
INPUT:
/*============================================================================*/
/* SKILL NAME :: VERILINGUA x VERIX EDITION                                   */
/*============================================================================*/

[define|neutral] SKILL := {...} [ground:given]

OUTPUT:
# SKILL NAME

> VERILINGUA x VERIX EDITION

<!-- x-verix: [define|neutral] SKILL := {...} [ground:given] -->

```

---

### THOUGHT 5: Risk Mitigation Strategy

**Risk 1: Data Loss**
- Mitigation: Full backup before any changes
- Mitigation: Git commit before migration
- Mitigation: Preserve all data in x- namespaced fields

**Risk 2: Script Errors**
- Mitigation: Dry-run mode first
- Mitigation: Process one file at a time with error handling
- Mitigation: Detailed logging of all changes

**Risk 3: Broken References**
- Mitigation: Validate all skill/agent references after migration
- Mitigation: Keep original names unchanged
- Mitigation: Update any hardcoded paths

**Risk 4: Partial Migration**
- Mitigation: Transaction-like approach (all or nothing per phase)
- Mitigation: Checkpoint files between phases
- Mitigation: Resume capability if interrupted

**Risk 5: Future Incompatibility**
- Mitigation: x- prefix is standard for extensions
- Mitigation: Document all custom fields
- Mitigation: Version the migration format

---

### THOUGHT 6: Validation Strategy

**Level 1: Syntax Validation**
- YAML frontmatter parses correctly
- JSON is valid
- No syntax errors in markdown

**Level 2: Schema Validation**
- All required fields present (name, description)
- Official fields have correct types
- x- fields preserved correctly

**Level 3: Reference Validation**
- All skill references resolve
- All agent references resolve
- All command references resolve

**Level 4: Functional Validation**
- Plugin loads in Claude Code
- Skills activate on triggers
- Agents spawn correctly

**Validation Script Output**
```
VALIDATION REPORT
=================
Phase 1 (plugin.json): PASS
Phase 2 (Skills): 196/196 PASS
Phase 3 (Agents): 211/211 PASS
Phase 4 (Commands): 223/223 PASS
Phase 5 (References): ALL RESOLVED
Phase 6 (Functional): MANUAL TEST REQUIRED

Total: 631/631 files compliant
```

---

### THOUGHT 7: Execution Plan

**PHASE 0: PREPARATION (5 minutes)**

```bash
# Step 0.1: Create backup
git add -A
git commit -m "pre-migration checkpoint"
git tag pre-migration-v3.0.0

# Step 0.2: Create backup directory
mkdir -p .migration-backup
cp -r . .migration-backup/

# Step 0.3: Verify backup
diff -rq . .migration-backup/ | head -20
```

**PHASE 1: PLUGIN.JSON (2 minutes)**

```bash
# Step 1.1: Transform plugin.json
node scripts/migrate-plugin-json.js

# Step 1.2: Validate
node scripts/validate-plugin-json.js
```

**PHASE 2: SKILLS (10 minutes)**

```bash
# Step 2.1: Dry run
node scripts/migrate-skills.js --dry-run

# Step 2.2: Execute
node scripts/migrate-skills.js

# Step 2.3: Validate
node scripts/validate-skills.js
```

**PHASE 3: AGENTS (10 minutes)**

```bash
# Step 3.1: Dry run
node scripts/migrate-agents.js --dry-run

# Step 3.2: Execute
node scripts/migrate-agents.js

# Step 3.3: Validate
node scripts/validate-agents.js
```

**PHASE 4: COMMANDS (5 minutes)**

```bash
# Step 4.1: Analyze (commands may already be compliant)
node scripts/analyze-commands.js

# Step 4.2: Migrate if needed
node scripts/migrate-commands.js

# Step 4.3: Validate
node scripts/validate-commands.js
```

**PHASE 5: FULL VALIDATION (5 minutes)**

```bash
# Step 5.1: Run full validation suite
node scripts/validate-all.js

# Step 5.2: Generate report
node scripts/generate-compliance-report.js
```

**PHASE 6: COMMIT AND TAG (2 minutes)**

```bash
# Step 6.1: Commit changes
git add -A
git commit -m "feat: migrate to Anthropic official format compliance"

# Step 6.2: Tag release
git tag v3.1.0-compliant

# Step 6.3: Update version
npm version minor
```

---

### THOUGHT 8: Rollback Procedure

**If Migration Fails at Any Phase**

```bash
# Option 1: Git reset (preferred)
git reset --hard pre-migration-v3.0.0
git tag -d pre-migration-v3.0.0

# Option 2: Restore from backup
rm -rf agents/ skills/ commands/ .claude-plugin/
cp -r .migration-backup/agents/ .
cp -r .migration-backup/skills/ .
cp -r .migration-backup/commands/ .
cp -r .migration-backup/.claude-plugin/ .

# Option 3: Partial rollback (single phase)
node scripts/rollback-phase.js --phase 2  # Rollback skills only
```

**Rollback Validation**

```bash
# Verify rollback success
node scripts/validate-original-format.js
git diff --stat pre-migration-v3.0.0
```

---

### THOUGHT 9: Post-Migration Tasks

1. **Update CLAUDE.md** - Document new x- field conventions
2. **Update README.md** - Note format compliance
3. **Update CHANGELOG.md** - Document migration
4. **Notify Users** - If public plugin, announce breaking changes
5. **Test Integration** - Verify with Claude Code CLI
6. **Archive Backup** - Keep .migration-backup for 30 days

---

### THOUGHT 10: Success Criteria

| Criterion | Measurement | Target |
|-----------|-------------|--------|
| All files parse | YAML/JSON validation | 100% |
| Official fields present | Schema validation | 100% |
| Custom data preserved | x- field count | = original custom field count |
| Plugin loads | Claude Code test | Success |
| Skills activate | Trigger test | 100% of tested skills |
| Agents spawn | Task test | 100% of tested agents |
| No data loss | Diff analysis | 0 fields lost |
| Rollback works | Rollback test | Success |

---

## IMPLEMENTATION FILES TO CREATE

Based on this analysis, we need to create:

1. `scripts/migration/migrate-plugin-json.js`
2. `scripts/migration/migrate-skills.js`
3. `scripts/migration/migrate-agents.js`
4. `scripts/migration/migrate-commands.js`
5. `scripts/migration/validate-all.js`
6. `scripts/migration/rollback-phase.js`
7. `scripts/migration/generate-compliance-report.js`

---

## ESTIMATED TIMELINE

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Phase 0: Preparation | 5 min | 5 min |
| Phase 1: plugin.json | 2 min | 7 min |
| Phase 2: Skills | 10 min | 17 min |
| Phase 3: Agents | 10 min | 27 min |
| Phase 4: Commands | 5 min | 32 min |
| Phase 5: Validation | 5 min | 37 min |
| Phase 6: Commit | 2 min | 39 min |
| **TOTAL** | **~40 min** | Automated |

---

## NEXT STEP

Create the migration scripts starting with `migrate-plugin-json.js`.

**Ready to proceed?**
