# Agent Creator - Expertise System Addendum

**Version**: 2.1.0
**Integrates**: expertise-manager, domain-expert

This addendum extends the 5-Phase Agent Creation Methodology (v2.0) with expertise-aware agent design. Note: Phase 0 is now integrated into the main SKILL.md as of v2.0.

---

## New Phase 0: Domain Expertise Loading

**Add BEFORE Phase 1 (Initial Analysis)**

### Purpose

Agents created with expertise context have embedded domain knowledge - they "know" the codebase structure, patterns, and known issues before they start.

### Process

```javascript
// PHASE 0: EXPERTISE LOADING

// 1. Identify primary domain for agent
const domain = identifyAgentDomain(agentRequest);

// 2. Check for expertise
const expertisePath = `.claude/expertise/${domain}.yaml`;

if (fileExists(expertisePath)) {
  console.log(`[EXPERTISE] Loading domain expertise for agent`);

  // 3. Validate expertise
  await runCommand('/expertise-validate', domain, '--fix');

  // 4. Load expertise
  const expertise = loadYAML(expertisePath);

  // 5. Extract agent-relevant context
  const agentContext = {
    // Where things are
    fileLocations: expertise.file_locations,

    // How things work
    patterns: expertise.patterns,

    // What to avoid
    knownIssues: expertise.known_issues,

    // How to route tasks
    routingTemplates: expertise.routing.task_templates,

    // Domain relationships
    dependencies: expertise.relationships.depends_on,
    dependents: expertise.relationships.depended_by
  };

  // 6. Store for embedding in agent
  setAgentContext('expertise', agentContext);

  console.log(`[EXPERTISE] Agent will have embedded knowledge of:`);
  console.log(`  - ${Object.keys(expertise.file_locations).length} file locations`);
  console.log(`  - ${Object.keys(expertise.patterns).length} patterns`);
  console.log(`  - ${expertise.known_issues.length} known issues`);
  console.log(`  - ${expertise.routing.task_templates.length} task templates`);
} else {
  console.log(`[EXPERTISE] No expertise for ${domain}`);
  console.log(`[EXPERTISE] Agent will operate in discovery mode`);
  setAgentContext('discoveryMode', true);
}
```

---

## Enhanced Phase 2: Expertise Extraction

**Integrate expertise into cognitive framework**

### Add Domain Knowledge Section

```markdown
## Domain Knowledge (From Expertise)

I have embedded knowledge of the ${domain} domain:

### File Locations I Know
- Primary source: ${expertise.file_locations.primary.path}
- Tests: ${expertise.file_locations.tests.path}
- Config: ${expertise.file_locations.config.path}
${expertise.file_locations.additional.map(a => `- ${a.purpose}: ${a.path}`).join('\n')}

### Patterns I Follow
- Architecture: ${expertise.patterns.architecture.claim}
- Data Flow: ${expertise.patterns.data_flow.claim}
- Error Handling: ${expertise.patterns.error_handling.claim}

### Issues I Avoid
${expertise.known_issues.map(i => `
- **${i.id}**: ${i.description}
  - Severity: ${i.severity}
  - Mitigation: ${i.mitigation}
`).join('\n')}

### Dependencies I Respect
${expertise.relationships.depends_on.map(d => `
- ${d.domain}: ${d.reason} (${d.coupling} coupling)
`).join('\n')}

This knowledge comes from `.claude/expertise/${domain}.yaml` and is validated against current code before each action.
```

---

## Enhanced Agent Frontmatter

**Add expertise integration metadata**

```yaml
---
name: "${agent_name}"
type: "${agent_type}"
description: "${description}"

# NEW: Expertise Integration
expertise_integration:
  primary_domain: "${domain}"
  secondary_domains: []
  load_on_init: true
  validate_before_action: true
  propose_updates_after: true

  # Embedded from expertise at creation time
  embedded_knowledge:
    file_locations: true
    patterns: true
    known_issues: true
    routing_templates: true

mcp_servers:
  required:
    - memory-mcp  # For expertise persistence
  optional: []
  auto_enable: true

hooks:
  pre: |
    # Load and validate domain expertise
    DOMAIN="${domain}"
    if [ -f ".claude/expertise/${DOMAIN}.yaml" ]; then
      /expertise-validate ${DOMAIN} --fix
      export EXPERTISE_LOADED="true"
      export EXPERTISE_DOMAIN="${DOMAIN}"
    fi

  post: |
    # Extract learnings and propose updates
    if [ "$EXPERTISE_LOADED" = "true" ]; then
      /expertise-extract-learnings ${EXPERTISE_DOMAIN}
    fi
---
```

---

## Enhanced Phase 3: System Prompt Construction

**Add expertise references to system prompt**

### Agent Identity with Expertise

```markdown
# ${agent_name}

## Core Identity

I am a **${role}** specialized in **${domain}** with embedded domain expertise.

## My Domain Knowledge

Unlike generic agents, I have **pre-loaded knowledge** of this codebase:

### I Know Where Things Are
${FILE_LOCATIONS_FROM_EXPERTISE}

### I Know How Things Work
${PATTERNS_FROM_EXPERTISE}

### I Know What To Avoid
${KNOWN_ISSUES_FROM_EXPERTISE}

### I Know How To Route Tasks
${ROUTING_TEMPLATES_FROM_EXPERTISE}

## How I Use This Knowledge

1. **Before Acting**: I validate my expertise against current code
2. **During Action**: I use known locations and patterns (no search thrash)
3. **After Action**: I extract learnings to update expertise

This makes me more efficient and accurate than an agent starting from scratch.
```

---

## New Phase 4.5: Expertise Validation

**Add after Phase 4 (Testing & Validation)**

### Validate Agent Uses Expertise Correctly

```yaml
validation_checks:
  expertise_usage:
    - agent_references_file_locations: true
    - agent_follows_documented_patterns: true
    - agent_avoids_known_issues: true
    - agent_has_pre_action_hook: true
    - agent_has_post_action_hook: true

  learning_capability:
    - can_extract_learnings: true
    - can_propose_updates: true
    - tracks_observations: true
```

---

## Discovery Mode Agent

**When no expertise exists**

If domain has no expertise file, create agent in discovery mode:

```markdown
## Discovery Mode

I am operating in **discovery mode** for the ${domain} domain.

### My First Task
Before executing domain-specific work, I will:
1. Discover domain structure (files, patterns, entities)
2. Generate initial expertise file
3. Queue for adversarial validation

### Discovery Process
1. Scan for ${domain}-related files
2. Extract patterns from code
3. Document key entities
4. Create: `.claude/expertise/${domain}.yaml`
5. Report: "Expertise generated, run /expertise-challenge ${domain}"

### After Discovery
Once expertise exists, future agents will have embedded knowledge and can work more efficiently.
```

---

## Agent Types with Expertise

### Domain Expert Agent (Inherits from domain-expert.md)

```yaml
# For agents specialized in a single domain
base_agent: domain-expert
expertise:
  primary: ${domain}
  embedded: true

capabilities:
  - expertise_loading
  - pre_action_validation
  - learning_extraction
  - update_proposal
```

### Multi-Domain Agent

```yaml
# For agents spanning multiple domains
expertise:
  domains:
    - primary: ${main_domain}
    - secondary:
        - ${domain2}
        - ${domain3}

  load_strategy: "on_demand"  # Load expertise when domain is accessed

  routing:
    # Use expertise routing templates when available
    use_expertise_templates: true
```

---

## Integration Summary

| Phase | Addition | Purpose |
|-------|----------|---------|
| 0 (NEW) | Expertise Loading | Load domain context |
| 1 | Expertise in Analysis | Domain knowledge informs research |
| 2 | Expertise in Extraction | Embed domain knowledge |
| 3 | Expertise in Prompt | Reference expertise in identity |
| 4 | Expertise in Testing | Validate correct usage |
| 4.5 (NEW) | Expertise Validation | Check expertise integration |

---

## Usage Example

```bash
# Creating an agent for authentication domain
> "Create a security analyst agent for our auth system"

[PHASE 0] Loading domain expertise...
[EXPERTISE] Found expertise for: authentication
[EXPERTISE] Validated (trust_level: validated)
[EXPERTISE] Agent will know:
  - 5 file locations
  - 4 patterns
  - 1 known issue
  - 2 routing templates

[PHASE 1] Initial Analysis with expertise context...
  - Skipping file discovery (known from expertise)
  - Focusing on security-specific patterns

[PHASE 2] Expertise Extraction...
  - Embedding file locations in agent identity
  - Embedding patterns in methodology
  - Adding known issues to guardrails

[PHASE 3] System Prompt Construction...
  - Agent has "I know where things are" section
  - Agent has "I know how things work" section
  - Agent has expertise validation hooks

[PHASE 4] Testing...
  - Verifying agent references expertise correctly

[DONE] Agent created with embedded domain expertise
```

---

## Reference

See: `.claude/skills/EXPERTISE-INTEGRATION-MODULE.md` for full integration patterns.
See: `agents/foundry/expertise/domain-expert.md` for base domain expert agent.
