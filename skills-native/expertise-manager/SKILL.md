---
name: expertise-manager
description: Manages domain expertise files for Agent Experts-style learning. Handles expertise creation, validation, pre-action loading, and post-build auto-updates. Enables agents to accumulate persistent domain knowledge that improves over time.
---

# Expertise Manager

## Phase 0: Expertise Loading

Before managing expertise:

1. **Detect Domain**: Identify the domain for expertise management
2. **Check Expertise**: Look for `.claude/expertise/meta-expertise.yaml`
3. **Load Context**: If exists, load expertise schema and validation rules
4. **Apply Configuration**: Use meta-expertise for management operations

## Purpose

Enable Agent Experts-style learning in the ruv-sparc three-loop system by managing domain expertise files - persistent mental models that agents read BEFORE acting and auto-update AFTER successful builds.

**Key Innovation**: Agents don't just execute and forget. They execute, learn, and reuse their expertise.

## When to Use This Skill

Activate this skill when:
- Creating a new domain expertise file for a codebase area
- Validating existing expertise against current code
- Loading domain context BEFORE implementation tasks
- Auto-updating expertise AFTER successful Loop 2 builds
- Analyzing expertise accuracy and learning history

**DO NOT** use this skill for:
- Quick one-off tasks (expertise overhead not worth it)
- Non-code tasks (expertise is code-focused)
- Tasks outside defined expertise domains

## MCP Requirements

### Memory MCP (Required)

**Purpose**: Persist expertise across sessions, enable cross-agent knowledge sharing.

**Tools Used**:
- `mcp__memory-mcp__memory_store`: Store expertise state and learning history
- `mcp__memory-mcp__vector_search`: Find relevant expertise for current task

**Activation**:
```bash
claude mcp add memory-mcp npx @modelcontextprotocol/server-memory
```



### Operation 2: Validate Expertise (Pre-Action)

**Command**: `/expertise-validate <domain>`

**Purpose**: Verify expertise file matches current code reality BEFORE acting.

**SOP**:
```javascript
// PHASE 1: LOAD EXPERTISE
const expertise = loadExpertiseFile(domain);
if (!expertise) {
  console.log("No expertise file found. Run /expertise-create first.");
  return;
}

// PHASE 2: RUN VALIDATION RULES
Task("Validation Runner",
  `Validate expertise for ${domain}:

   For each validation_rule in expertise.validation_rules:
   1. file_exists: Check if target path exists
   2. pattern_match: Verify pattern still present in code
   3. import_check: Verify imports still valid
   4. function_signature: Verify function signatures match

   Track: { passed: [], failed: [], skipped: [] }

   Output: .claude/.artifacts/expertise-validation-${domain}.json`,
  "code-analyzer")

// PHASE 3: CHECK FILE LOCATIONS
Task("Location Verifier",
  `Verify file locations for ${domain}:

   Check each path in expertise.file_locations:
   - Does primary directory exist?
   - Do test files exist?
   - Do config files exist?

   Flag any missing/moved files.

   Output: .claude/.artifacts/expertise-locations-${domain}.json`,
  "code-analyzer")

// PHASE 4: DETECT DRIFT
Task("Drift Detector",
  `Detect expertise drift for ${domain}:

   Compare current code against expertise patterns:
   - Are documented patterns still used?
   - Have new patterns emerged?
   - Have entities changed (renamed, moved, deleted)?

   Calculate drift_score: 0.0 (no drift) to 1.0 (major drift)

   Output: .claude/.artifacts/expertise-drift-${domain}.json`,
  "analyst")

// PHASE 5: UPDATE OR FLAG
const validationResult = combineValidationResults();

if (validationResult.drift_score < 0.2) {
  // Expertise is valid - update timestamp
  expertise.last_validated = new Date().toISOString();
  expertise.validation_status = "valid";
  saveExpertiseFile(domain, expertise);

  console.log("Expertise validated. Ready for use.");
} else if (validationResult.drift_score < 0.5) {
  // Minor drift - auto-correct
  await autoCorrectExpertise(domain, validationResult);
  console.log("Expertise auto-corrected. Minor drift resolved.");
} else {
  // Major drift - flag for review
  expertise.validation_status = "stale";
  saveExpertiseFile(domain, expertise);

  console.log("WARNING: Major expertise drift detected.");
  console.log("Run /expertise-refresh to rebuild expertise.");
}
```



### Operation 4: Self-Improve (Post-Build Auto-Update)

**Purpose**: Automatically update expertise after successful Loop 2 builds.

**Trigger**: Loop 2 Step 9 completion with 100% test success

**SOP**:
```javascript
// SELF-IMPROVE HOOK - Runs after successful Loop 2 build

// PHASE 1: IDENTIFY AFFECTED DOMAINS
Task("Domain Identifier",
  `Identify domains affected by this build:

   1. Parse git diff to find changed files
   2. Map changed files to expertise domains
   3. Rank domains by change magnitude

   Output: List of domains needing expertise update`,
  "analyst")

// PHASE 2: EXTRACT LEARNINGS (Per Domain)
for (const domain of affectedDomains) {
  Task(`Learning Extractor (${domain})`,
    `Extract learnings for ${domain} from this build:

     1. New patterns introduced?
        - New files created
        - New functions/classes added
        - New error handling patterns

     2. Existing patterns modified?
        - Refactored code
        - Changed signatures
        - Updated validation logic

     3. Issues discovered and fixed?
        - Bugs fixed
        - Edge cases handled
        - Security improvements

     4. Relationships changed?
        - New imports
        - New dependencies
        - Decoupled components

     Output: .claude/.artifacts/learnings-${domain}.json`,
    "analyst")
}

// PHASE 3: UPDATE EXPERTISE FILES
for (const domain of affectedDomains) {
  Task(`Expertise Updater (${domain})`,
    `Update expertise file for ${domain}:

     1. Load current: .claude/expertise/${domain}.yaml
     2. Load learnings: .claude/.artifacts/learnings-${domain}.json

     3. Update sections:
        - file_locations: Add new files, remove deleted
        - patterns: Document new/changed patterns
        - entities: Update class/function registry
        - known_issues: Add discovered issues, resolve fixed ones
        - relationships: Update dependency graph

     4. Add to learning_history:
        {
          timestamp: now,
          source: "loop2_build",
          learned: "<summary>",
          confidence: 0.9,
          evidence: [files_changed]
        }

     5. Update metadata:
        - last_updated: now
        - update_count++
        - validation_status: "valid"

     6. Save: .claude/expertise/${domain}.yaml

     7. Persist to Memory MCP: expertise/${domain}`,
    "knowledge-manager")
}

// PHASE 4: VALIDATE UPDATES
Task("Update Validator",
  `Validate expertise updates:

   For each updated expertise file:
   1. Run validation rules against current code
   2. Verify all file_locations exist
   3. Confirm patterns match code
   4. Calculate new accuracy_score

   If validation fails:
   - Rollback to previous version
   - Flag for manual review

   Output: Update validation report`,
  "code-analyzer")
```



## Integration with Three-Loop System

### Loop 1 Integration (Planning)

```yaml
# In research-driven-planning SKILL.md
# Add to Phase 2: Research

Task("Expertise Loader",
  `Load relevant expertise for planning:

   1. Identify domains from SPEC.md requirements
   2. For each domain with expertise file:
      - Load .claude/expertise/${domain}.yaml
      - Extract: patterns, known_issues, relationships
   3. Feed into research synthesis

   Benefits:
   - Research builds on existing knowledge
   - Known issues inform pre-mortem
   - Relationships guide architecture`,
  "knowledge-manager")
```

### Loop 2 Integration (Implementation)

```yaml
# In parallel-swarm-implementation SKILL.md
# Add as Step 0: Expertise Loading

## Step 0: Load Domain Expertise (Pre-Action)

Before Queen creates agent+skill matrix:

Task("Expertise Coordinator",
  `Load expertise for all domains in Loop 1 plan:

   1. Parse Loop 1 planning package
   2. Identify all domains involved
   3. For each domain:
      - Run /expertise-validate
      - Load validated expertise into session
   4. Provide expertise context to Queen

   Queen uses expertise to:
   - Know exact file locations (no search thrash)
   - Select agents familiar with domain patterns
   - Apply known issue mitigations
   - Respect existing relationships`,
  "knowledge-manager")

# Add as Step 9.5: Self-Improve

## Step 9.5: Expertise Self-Improve (Post-Build)

After successful build (100% test pass):

Task("Self-Improve Coordinator",
  `Auto-update expertise from build learnings:

   1. Identify domains changed in this build
   2. Extract learnings from changes
   3. Update expertise files
   4. Validate updates against code
   5. Persist to Memory MCP

   This is AUTOMATIC - no human intervention needed.
   Expertise improves with every successful build.`,
  "knowledge-manager")
```

### Loop 3 Integration (Feedback)

```yaml
# In cicd-intelligent-recovery SKILL.md
# Add to Step 8: GitHub Feedback

## Enhanced Failure Pattern Storage

When storing loop3-failure-patterns.json:

Task("Expertise Failure Integrator",
  `Integrate failure patterns into expertise:

   For each failure:
   1. Identify affected domain
   2. Load .claude/expertise/${domain}.yaml
   3. Add to known_issues:
      {
        id: "LOOP3-${failure_id}",
        description: "${root_cause}",
        severity: "${severity}",
        status: "open",
        discovered: now,
        mitigation: "${prevention_strategy}"
      }
   4. Add to learning_history:
      {
        timestamp: now,
        source: "loop3_failure",
        learned: "Failure pattern: ${category}",
        confidence: ${consensus_confidence},
        evidence: [affected_files]
      }
   5. Save expertise file
   6. Persist to Memory MCP

   Next Loop 1 pre-mortem AUTOMATICALLY
   receives this failure knowledge.`,
  "knowledge-manager")
```

--------|---------|----------|----------|
| `expertise/{domain}` | Persisted expertise files | expertise-manager | All agents |
| `expertise/active` | Currently loaded expertise | pre-action hook | Current session |
| `expertise/learnings` | Extracted learnings | self-improve | expertise-manager |
| `expertise/validation` | Validation results | validator | expertise-manager |
| `expertise/history` | Historical expertise versions | archive | recovery |

------|---------|-------|
| `/expertise-create` | Create new domain expertise | `/expertise-create authentication` |
| `/expertise-validate` | Validate expertise against code | `/expertise-validate database` |
| `/expertise-refresh` | Rebuild stale expertise | `/expertise-refresh websocket` |
| `/expertise-list` | List all expertise files | `/expertise-list` |
| `/expertise-show` | Display expertise details | `/expertise-show authentication` |
| `/expertise-diff` | Show expertise drift | `/expertise-diff database` |



## Performance Metrics

- **Pre-Action Time**: <500ms to load and validate expertise
- **Self-Improve Time**: <2min to extract learnings and update
- **Drift Detection Accuracy**: >95% of meaningful changes detected
- **Auto-Correction Success**: >80% of minor drift auto-resolved
- **Knowledge Retention**: 100% persistence across sessions



## Recursive Improvement Integration (v2.1)

### Input/Output Contracts

```yaml
input_contract:
  required:
    - operation: string  # create/validate/load/update
  optional:
    - domain: string
    - expertise_file: path

output_contract:
  required:
    - expertise_state: object
    - status: string
```

### Eval Harness Integration

```yaml
benchmark: expertise-manager-benchmark-v1
  tests:
    - em-001: Load Time
    - em-002: Drift Detection
  minimum_scores:
    load_time: 500ms
    drift_accuracy: 0.95
```

### Memory Namespace

```yaml
namespaces:
  - expertise-manager/domains/{domain}: Domain expertise
  - expertise-manager/validations: Validation history
```

### Cross-Skill Coordination

Works with: **research-driven-planning**, **parallel-swarm-implementation**, **skill-forge**

## Core Principles

### 1. Expertise as Correctable Working Memory, Not Source of Truth
Expertise files are mental models that guide action, not canonical documentation. They capture agent understanding of codebase patterns, file locations, and relationships - understanding that can drift as code evolves. The value lies in validation loops that detect drift and auto-correct, not in the artifact itself. Treat expertise as hypothesis to be continuously validated against code reality, never as immutable truth.

### 2. Pre-Action Loading Prevents Search Thrash
Agents without domain expertise waste time discovering what previous agents already learned - scanning directories, inferring patterns, rediscovering known issues. Loading expertise before action provides agents with accumulated knowledge: exact file locations (no globbing), documented patterns (follow conventions immediately), and known issues (avoid solved problems). This pre-action context transforms agents from discovery mode to execution mode, eliminating redundant exploration.

### 3. Post-Success Auto-Update Creates Learning DNA
Expertise that never updates becomes stale documentation. The innovation is automatic learning after successful builds: detect changed domains, extract new patterns, update expertise files, and validate against current code. This creates self-improving systems where each successful build strengthens agent knowledge for future tasks. Expertise accumulates without manual maintenance, compounding effectiveness across projects.

-----------|--------------|------------------|
| **Treating expertise as static documentation** | Code evolves but expertise doesn't, causing drift. Agents follow outdated patterns, reference moved files, and apply obsolete conventions. Stale expertise is worse than no expertise - it misleads rather than guides. | Enable post-build auto-update hooks. After successful Loop 2 builds, automatically extract learnings, update affected domain expertise, and validate changes. Expertise stays synchronized with code evolution. Set last_validated timestamps and drift_score thresholds. |
| **Skipping pre-action validation** | Loading expertise without validation risks acting on stale information. Agent confidently uses wrong file paths, applies deprecated patterns, and violates current conventions because expertise wasn't verified. | Always run /expertise-validate before loading domain context. Check validation rules, verify file locations exist, detect drift through pattern matching. If drift >0.5, refresh expertise before use. Validation takes <500ms but prevents hours of wasted effort. |
| **Creating expertise for every codebase area** | Expertise has overhead - creation time, validation cost, maintenance burden. Creating expertise for rarely-touched areas wastes resources maintaining knowledge that's seldom used. | Create expertise strategically for high-frequency domains. Focus on areas agents work in repeatedly (authentication, database, API layers). Skip one-off tasks or rarely-modified code. Good rule: create expertise if domain used 3+ times per month. |

---

## Conclusion

Expertise Manager implements Agent Experts-style learning for the three-loop system - agents that don't just execute and forget, but execute, learn, and reuse knowledge. This transforms Claude from stateless execution to stateful intelligence where each task strengthens future performance. The key insight is that expertise files are correctable working memory, not static documentation, with value derived from validation loops rather than initial accuracy.

The system's power emerges through three integrated mechanisms: pre-action loading eliminates search thrash by providing agents with accumulated domain knowledge before they begin work; post-success auto-update creates learning DNA where successful builds automatically strengthen expertise; and validation loops detect drift between expertise and code reality, enabling automatic correction before stale knowledge misleads agents. Together, these mechanisms create self-improving agents that compound effectiveness over time.

Successful implementation requires treating expertise as living mental models that require continuous validation against code reality. The investment pays exponential returns - early tasks spend time creating expertise, but subsequent tasks in the same domains execute faster with fewer mistakes as agents leverage pre-existing knowledge. This is especially powerful in Loop 2 parallel swarms where multiple agents working across domains all benefit from shared expertise, eliminating redundant discovery and ensuring consistent pattern application across the entire codebase.