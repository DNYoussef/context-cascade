# Skill Forge - Expertise System Addendum

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Version**: 2.1.0
**Integrates**: expertise-manager, domain-expert

This addendum extends Skill Forge (now 8-phase methodology) with Agent Experts-style learning capabilities. Note: Phase 0 (Expertise Loading) is now integrated into the main SKILL.md as of v2.0.

---

## New Phase 0: Domain Expertise Loading

**Add BEFORE Phase 1 (Intent Archaeology)**

### Purpose

Load and leverage existing domain expertise to inform skill creation. Skills created with expertise context are more accurate and integrate better with the codebase.

### Process

```javascript
// PHASE 0: EXPERTISE CONTEXT LOADING

// 1. Detect domain from skill request
const domain = analyzeDomainFromRequest(skillRequest);

// 2. Check for expertise file
const expertisePath = `.claude/expertise/${domain}.yaml`;

if (fileExists(expertisePath)) {
  console.log(`[EXPERTISE] Found expertise for domain: ${domain}`);

  // 3. Validate expertise is current
  await runCommand('/expertise-validate', domain, '--fix');

  // 4. Load validated expertise
  const expertise = loadYAML(expertisePath);

  // 5. Extract relevant context for skill creation
  const context = {
    fileLocations: expertise.file_locations,
    patterns: expertise.patterns,
    knownIssues: expertise.known_issues,
    routingTemplates: expertise.routing.task_templates,
    trustLevel: expertise.correctability.trust_level
  };

  console.log(`[EXPERTISE] Loaded context:`);
  console.log(`  - Primary path: ${context.fileLocations.primary.path}`);
  console.log(`  - Patterns: ${Object.keys(context.patterns).length}`);
  console.log(`  - Known issues: ${context.knownIssues.length}`);
  console.log(`  - Trust level: ${context.trustLevel}`);

  // 6. Store for use in subsequent phases
  setPhaseContext('expertise', context);
} else {
  console.log(`[EXPERTISE] No expertise file for ${domain}`);
  console.log(`[EXPERTISE] Will generate expertise as side effect`);
  setPhaseContext('generateExpertise', true);
}
```

---

## Enhanced Phase 3: Structural Architecture

**Modify to incorporate expertise context**

When designing skill structure, if expertise is available:

### Use Expertise File Locations

```yaml
# In generated skill
file_context:
  # From expertise.file_locations
  primary_path: "${expertise.file_locations.primary.path}"
  tests_path: "${expertise.file_locations.tests.path}"
  config_path: "${expertise.file_locations.config.path}"
```

### Reference Expertise Patterns

```yaml
# In generated skill methodology
methodology:
  # Reference domain patterns from expertise
  architecture_pattern: "${expertise.patterns.architecture.claim}"
  data_flow: "${expertise.patterns.data_flow.claim}"
  error_handling: "${expertise.patterns.error_handling.claim}"
```

### Incorporate Known Issues

```yaml
# In generated skill guardrails
known_issues:
  # From expertise.known_issues
  ${expertise.known_issues.map(issue => `
  - id: ${issue.id}
    description: ${issue.description}
    mitigation: ${issue.mitigation}
  `)}
```

---

## New Phase 7.5: Expertise Hook Integration

**Add AFTER Phase 7 (Quality Assurance)**

### Add Expertise Hooks to Generated Skill

Every skill created for a domain with expertise should include:

```yaml
# In generated SKILL.md frontmatter
expertise_integration:
  domain: "${domain}"
  requires_expertise: true
  auto_validate: true
  auto_update: true

# In generated SKILL.md hooks section
hooks:
  pre_execution: |
    # Load and validate domain expertise before execution
    if [ -f ".claude/expertise/${domain}.yaml" ]; then
      /expertise-validate ${domain} --fix
      export EXPERTISE_LOADED="true"
      export EXPERTISE_DOMAIN="${domain}"
    fi

  post_execution: |
    # Extract learnings and propose expertise updates
    if [ "$EXPERTISE_LOADED" = "true" ]; then
      /expertise-extract-learnings ${EXPERTISE_DOMAIN}
    fi
```

---

## New Phase 8: Expertise Generation (If No Expertise Exists)

**Run ONLY if generateExpertise flag was set in Phase 0**

### Generate Initial Domain Expertise

When creating a skill for a domain without expertise, generate it:

```javascript
// PHASE 8: EXPERTISE GENERATION (conditional)

if (getPhaseContext('generateExpertise')) {
  console.log(`[EXPERTISE] Generating expertise for domain: ${domain}`);

  // 1. Extract domain knowledge from skill analysis
  const domainKnowledge = {
    fileLocations: getPhaseOutput('structuralArchitecture').fileLocations,
    patterns: getPhaseOutput('structuralArchitecture').patterns,
    entities: getPhaseOutput('intentArchaeology').entities
  };

  // 2. Generate expertise file
  Task("Expertise Generator",
    `Generate initial expertise file for ${domain}:

     File locations:
     ${JSON.stringify(domainKnowledge.fileLocations, null, 2)}

     Patterns:
     ${JSON.stringify(domainKnowledge.patterns, null, 2)}

     Create: .claude/expertise/${domain}.yaml
     Set: validation_status = "needs_validation"
     Set: trust_level = "provisional"`,
    "knowledge-manager");

  // 3. Queue for adversarial validation
  console.log(`[EXPERTISE] Generated expertise queued for validation`);
  console.log(`[EXPERTISE] Run: /expertise-challenge ${domain}`);
}
```

---

## Updated Quality Assurance Phase

Add expertise-specific quality checks:

### Expertise Alignment Check

```yaml
quality_checks:
  - name: expertise_alignment
    description: Verify skill aligns with domain expertise
    checks:
      - skill_uses_expertise_paths: true
      - skill_follows_expertise_patterns: true
      - skill_references_known_issues: true
      - skill_has_expertise_hooks: true
```

### Learning Potential Check

```yaml
quality_checks:
  - name: learning_potential
    description: Verify skill can contribute to expertise learning
    checks:
      - has_pre_execution_hook: true
      - has_post_execution_hook: true
      - tracks_observations: true
      - can_propose_updates: true
```

---

## Integration Summary

| Phase | Addition | Purpose |
|-------|----------|---------|
| 0 (NEW) | Expertise Loading | Load domain context |
| 3 | Expertise in Structure | Use file locations, patterns |
| 5 | Expertise in Instructions | Reference known issues |
| 7 | Expertise Quality Checks | Verify alignment |
| 7.5 (NEW) | Hook Integration | Add expertise hooks |
| 8 (NEW) | Expertise Generation | Create if missing |

---

## Usage Example

```bash
# Creating a skill for authentication domain with expertise
> "Create a skill for validating JWT tokens in our auth system"

[EXPERTISE] Found expertise for domain: authentication
[EXPERTISE] Validated expertise (drift: 0.12)
[EXPERTISE] Loaded context:
  - Primary path: src/auth/
  - Patterns: 4
  - Known issues: 1
  - Trust level: validated

[PHASE 1] Intent Archaeology with expertise context...
[PHASE 2] Use Case Crystallization...
[PHASE 3] Structural Architecture using:
  - File locations from expertise
  - Patterns from expertise
[PHASE 4-7] Standard phases...
[PHASE 7.5] Adding expertise hooks to skill...
[DONE] Skill created with expertise integration
```

---

## Reference

See: `.claude/skills/EXPERTISE-INTEGRATION-MODULE.md` for full integration patterns.


---
*Promise: `<promise>EXPERTISE_ADDENDUM_VERIX_COMPLIANT</promise>`*
