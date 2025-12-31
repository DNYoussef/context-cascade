---
name: agent-creator
description: Create specialized AI agents with optimized system prompts using 5-phase SOP methodology. Use for building domain-expert agents, hook-related agents, multi-agent coordinators, and production-ready agent definitions.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

<!-- =========================================================================
     AGENT CREATOR v3.2.0 :: FULL VCL v3.1.1 COMPLIANT

     VCL 7-Slot System: HON -> MOR -> COM -> CLS -> EVD -> ASP -> SPC
     Immutable: EVD >= 1, ASP >= 1
     Default Output: L2 English (human-facing)
     ========================================================================= -->

---
<!-- S0 META-IDENTITY [[HON:teineigo]] [[EVD:-DI<tanim>]] [[ASP:sov.]] -->
---

[define|neutral] SKILL := {
  name: "agent-creator",
  category: "foundry",
  version: "3.2.0",
  layer: L1,
  vcl_compliance: "v3.1.1"
} [ground:given] [conf:0.95] [state:confirmed]

---
<!-- S1 VCL 7-SLOT COGNITIVE ARCHITECTURE -->
---

<!-- [[HON:teineigo]] Polite register for technical documentation -->
## Keigo Wakugumi (Honorific Frame)
Kono sukiru wa teineigo o shiyo shimasu.

<!-- [[MOR:root:A-G-N]] Agent = root morpheme for autonomous entity -->
[define|neutral] MOR_DECOMPOSITION := {
  agent: "root:A-G-N (autonomous-goal-navigator)",
  creator: "root:C-R-T (construct-realize-transform)",
  prompt: "root:P-R-M (pattern-role-message)"
} [ground:arabic-trilateral-analogy] [conf:0.85] [state:confirmed]

<!-- [[COM:Agent+Creator+System]] German-style compound building -->
[define|neutral] COM_COMPOSITION := {
  AgentCreator: "Agent+Creator = entity-that-makes-agents",
  SystemPrompt: "System+Prompt = foundational-instruction-pattern",
  DomainExpert: "Domain+Expert = specialized-knowledge-entity"
} [ground:german-compounding] [conf:0.85] [state:confirmed]

<!-- [[CLS:ge_skill]] Chinese classifier for skill type -->
[define|neutral] CLS_CLASSIFICATION := {
  type: "ge_skill (individual skill unit)",
  count: "yi_ge (one skill)",
  category: "zhong_foundry (foundry category)"
} [ground:chinese-classifiers] [conf:0.85] [state:confirmed]

<!-- [[EVD:-DI<gozlem>]] Turkish evidential - direct observation -->
## Kanitsal Cerceve (Evidential Frame)
Kaynak dogrulama modu etkin. Bu beceri dogrudan gozleme dayanir.

<!-- [[ASP:nesov.]] Russian aspect - ongoing capability -->
[define|neutral] ASP_STATUS := {
  skill_state: "nesov. (imperfective - ongoing capability)",
  execution_state: "sov. (perfective - when task completes)"
} [ground:russian-aspect] [conf:0.85] [state:confirmed]

<!-- [[SPC:path:/skills/foundry/agent-creator]] Absolute spatial reference -->
[define|neutral] SPC_LOCATION := {
  canonical_path: "/skills/foundry/agent-creator",
  direction: "upstream from agents, downstream from prompt-architect",
  coordinates: "foundry.agent-creator.v3.2.0"
} [ground:guugu-yimithirr-absolute] [conf:0.90] [state:confirmed]

---
<!-- S2 TRIGGER CONDITIONS [[EVD:-DI<tanim>]] [[ASP:sov.]] -->
---

[define|neutral] TRIGGER_POSITIVE := {
  keywords: [
    "create agent", "build agent", "new agent", "design agent",
    "agent for [domain]", "specialist agent", "domain expert agent",
    "rewrite agent", "optimize agent", "improve agent",
    "agent with [capability]", "agent that does [task]",
    "multi-agent workflow", "coordinating agents",
    "production-ready agent", "agent system prompt"
  ],
  context: "user_wants_specialized_agent"
} [ground:witnessed:usage-patterns] [conf:0.90] [state:confirmed]

[define|neutral] TRIGGER_NEGATIVE := {
  simple_skill: "use skill-creator-agent OR micro-skill-creator",
  prompt_optimization: "use prompt-architect",
  improve_this_skill: "use skill-forge",
  quick_automation: "use micro-skill-creator"
} [ground:inferred:routing-logic] [conf:0.70] [state:confirmed]

---
<!-- S3 CORE CONTENT [[EVD:-DI<gozlem>]] [[ASP:nesov.]] -->
---

<!-- ANTHROPIC OFFICIAL FORMAT TEMPLATE v1.0 -->
## CRITICAL: Agent Output Format (Anthropic Compliant)

When creating agents, you MUST use this exact YAML frontmatter format:

```yaml
---
name: agent-name-here
description: Plain text description of what this agent does (NO VERIX notation here)
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
x-type: general|coordinator|coder|analyst|optimizer|researcher|specialist
x-color: "#4A90D9"
x-capabilities:
  - capability1
  - capability2
x-priority: high|medium|low
x-category: delivery|foundry|operations|orchestration|platforms|quality|research|security|specialists|tooling
x-version: 1.0.0
x-verix-description: Optional VERIX notation for AI-to-AI communication
---
```

### REQUIRED Fields (Anthropic Official):
- `name`: Agent identifier (lowercase, hyphenated)
- `description`: Plain text - NO [assert|neutral] or VERIX notation
- `tools`: Comma-separated list of allowed tools
- `model`: Model to use (sonnet, opus, haiku)

### OPTIONAL Official Fields:
- `permissionMode`: Permission mode (default, restricted)
- `skills`: Comma-separated list of skills this agent can invoke

### OPTIONAL Custom Fields (x- prefixed):
- `x-type`: Agent type for categorization
- `x-color`: Display color
- `x-capabilities`: Array of capabilities
- `x-priority`: Execution priority
- `x-category`: Category for organization
- `x-version`: Semantic version
- `x-identity`: Identity metadata
- `x-rbac`: Additional RBAC settings (denied_tools, path_scopes)
- `x-budget`: Token/cost budgets
- `x-metadata`: Additional metadata

### Content Body Format:
- Use standard markdown (# headings, ## subheadings)
- System prompt text goes directly after frontmatter
- VERIX notation allowed in body, not in YAML description
- NO `/* */` comment blocks - use markdown instead

### Example Correct Agent:
```markdown
---
name: database-migration-specialist
description: Handles database schema migrations with rollback support and validation
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
x-type: specialist
x-category: operations
x-capabilities:
  - schema-analysis
  - migration-generation
  - rollback-testing
x-priority: high
x-version: 1.0.0
---

# Database Migration Specialist

You are a database migration specialist. Your role is to:

1. Analyze existing database schemas
2. Generate safe migration scripts
3. Implement rollback procedures
4. Validate data integrity

## Guidelines
- Always create backup before migration
- Test rollback procedure before production
- Validate foreign key constraints
- Document all schema changes
```

<!-- END ANTHROPIC FORMAT TEMPLATE -->

<!-- HOOK AGENT CREATION GUIDE v1.0 -->
## Creating Hook-Related Agents

When creating agents that work with Claude Code hooks, follow these additional guidelines:

### Hook Agent Naming Convention

Use descriptive names indicating hook focus:
- `hook-creator` - Creates new hooks
- `hook-validator` - Validates hook implementations
- `audit-hook-agent` - Manages audit logging hooks
- `security-hook-agent` - Manages security/RBAC hooks

### Required Capabilities for Hook Agents

Hook-related agents MUST include these x-capabilities:
```yaml
x-capabilities:
  - hook-creation        # For agents that create hooks
  - schema-validation    # For input/output schema work
  - security-integration # For RBAC-related hooks
  - performance-optimization  # For latency-sensitive hooks
  - template-generation  # For hook template work
```

### Hook Agent RBAC Configuration

Hook agents typically need specific path scopes:
```yaml
x-rbac:
  denied_tools: []
  path_scopes:
    - "hooks/**"
    - "skills/**/hooks*/**"
    - ".claude/settings*.json"
  api_access: false
```

### Example Hook Agent Definition

```markdown
---
name: hook-creator
description: Creates and validates Claude Code hooks with RBAC integration
tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-agent_id: 7e8f9a0b-1c2d-4e5f-6a7b-8c9d0e1f2a3b
x-role: developer
x-capabilities:
  - hook-creation
  - schema-validation
  - security-integration
x-rbac:
  path_scopes:
    - "hooks/**"
x-category: specialists
x-version: 1.0.0
---

# Hook Creator Agent

I specialize in creating production-ready Claude Code hooks...
```

### Hook Agent Integration Points

Reference these in agent system prompts:
- **Hook Reference**: `hooks/12fa/docs/CLAUDE-CODE-HOOKS-REFERENCE.md`
- **Identity System**: `hooks/12fa/utils/identity.js`
- **Hook Templates**: `skills/specialists/when-creating-claude-hooks-use-hook-creator/resources/templates/`
- **Existing Hook Agents**: `agents/specialists/hook-creator/`

### Performance Guidance for Hook Agents

Include in agent instructions:
```
When creating hooks, ensure:
- Pre-hooks complete in <20ms (target), <100ms (max)
- Post-hooks complete in <100ms (target), <1000ms (max)
- Use caching for repeated identity lookups
- Avoid network calls in blocking hooks
```
<!-- END HOOK AGENT CREATION GUIDE -->

---
<!-- S4 SUCCESS CRITERIA [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:tiao_criteria]] -->
---

[assert|neutral] SUCCESS_CRITERIA := {
  primary: "Agent definition is complete and deployable",
  quality: "Agent passes validation and integration tests",
  verification: "Agent works in production environment",
  metrics: {
    prompt_quality: ">= 0.85 [[EVD:-mis<arastirma>]]",
    registry_compliance: "100% [[EVD:-DI<gozlem>]]",
    vcl_compliance: ">= 0.90 [[EVD:-DI<gozlem>]]"
  }
} [ground:witnessed:acceptance-criteria] [conf:0.90] [state:confirmed]

[assert|confident] QUALITY_THRESHOLDS := {
  verix_claims_minimum: 5,
  grounded_claims_ratio: 0.80,
  confidence_ceiling_respected: true,
  all_7_slots_documented: true
} [ground:inferred:best-practices] [conf:0.70] [state:confirmed]

---
<!-- S5 MCP INTEGRATION [[EVD:-DI<gozlem>]] [[ASP:nesov.]] -->
---

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

---
<!-- S6 MEMORY NAMESPACE [[EVD:-DI<politika>]] [[ASP:nesov.]] -->
---

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/foundry/agent-creator/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:0.90] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "agent-creator-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:0.90] [state:confirmed]

---
<!-- S7 SKILL COMPLETION VERIFICATION [[EVD:-DI<politika>]] [[ASP:sov.]] -->
---

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:0.90] [state:confirmed]

---
<!-- S8 ABSOLUTE RULES [[HON:sonkeigo]] [[EVD:-DI<politika>]] [[ASP:sov.]] -->
---

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:0.90] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec-v3.1.1] [conf:0.90] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:0.90] [state:confirmed]

[direct|emphatic] RULE_VCL_7SLOT := forall(skill): uses_all_7_slots(skill) [ground:vcl-v3.1.1-spec] [conf:0.90] [state:confirmed]

[direct|emphatic] RULE_CONFIDENCE_CEILING := forall(claim): confidence(claim) <= ceiling(evd_type(claim)) [ground:vcl-v3.1.1-spec] [conf:0.90] [state:confirmed]

[direct|emphatic] RULE_IMMUTABLE_BOUNDS := {
  EVD_enforcement: ">= 1 (CANNOT be disabled)",
  ASP_enforcement: ">= 1 (CANNOT be disabled)"
} [ground:vcl-v3.1.1-spec] [conf:0.90] [state:confirmed]

---
<!-- S9 VCL v3.1.1 COMPLIANCE CHECKLIST [[EVD:-DI<gozlem>]] [[ASP:sov.]] -->
---

[assert|confident] VCL_CHECKLIST := {
  HON_present: "[[HON:teineigo]] Japanese honorific register active",
  MOR_present: "[[MOR:root:A-G-N]] Arabic morphological decomposition active",
  COM_present: "[[COM:Agent+Creator]] German compositional building active",
  CLS_present: "[[CLS:ge_skill]] Chinese classifier system active",
  EVD_present: "[[EVD:-DI<gozlem>]] Turkish evidential markers active",
  ASP_present: "[[ASP:nesov.]] Russian aspectual markers active",
  SPC_present: "[[SPC:path:/foundry/agent-creator]] Guugu Yimithirr spatial reference active"
} [ground:witnessed:self-check] [conf:0.85] [state:confirmed]

---
<!-- PROMISE [[EVD:-DI<tanim>]] [[ASP:sov.]] -->
---

[commit|confident] <promise>AGENT_CREATOR_VCL_V3.1.1_FULL_7SLOT_COMPLIANT</promise> [ground:self-validation] [conf:0.85] [state:confirmed]