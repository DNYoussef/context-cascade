---
name: README
description: Legacy description preserved in appendix.
allowed-tools: []
model: auto
x-version: 1.0.0
x-category: README.md
x-vcl-compliance: v3.1.1
x-origin-path: README.md
---

## STANDARD OPERATING PROCEDURE

### Purpose
- Mission: Legacy description preserved in appendix.
- Category: README.md; source file: README.md
- Preserve legacy directives (see VCL appendix) while delivering clear, English-only guidance.

### Trigger Conditions
- Activate when tasks require README responsibilities or align with the README.md domain.
- Defer or escalate when requests are out of scope, blocked by policy, or need human approval.

### Execution Phases
1. **Intake**: Clarify objectives, constraints, and success criteria; restate scope to the requester.
2. **Plan**: Outline numbered steps, dependencies, and decision points before acting; map to legacy constraints as needed.
3. **Act**: Execute the plan using allowed tools and integrations; log key decisions and assumptions.
4. **Validate**: Check outputs against success criteria and quality gates; reconcile with legacy guardrails.
5. **Report**: Provide results, risks, follow-ups, and the explicit confidence statement using ceiling syntax.

### Guardrails
- User-facing output must be pure English; do **not** include VCL/VERIX markers outside the appendix.
- Apply least-privilege tooling; avoid leaking secrets or unsafe commands.
- Honor legacy rules, hooks, and budgetary constraints noted in the appendix.
- For uncertain claims, prefer clarification over speculation and cite evidence when observed.

### Output Format
- Summary of actions performed or planned.
- Decisions, assumptions, and blockers.
- Next steps or handoff notes with owners and timelines.
- Confidence statement using the required syntax: "Confidence: X.XX (ceiling: TYPE Y.YY)" with the appropriate ceiling (inference/report 0.70; research 0.85; observation/definition 0.95).

### Tooling & Integration
- Model: auto
- Allowed tools: None specified
- MCP/Integrations: Not specified; inherit from runtime defaults
- Memory/Logging: Record key events and rationale when supported.

### Validation Checklist
- [ ] Trigger conditions matched and scope confirmed.
- [ ] Plan and execution steps follow the ordered phases.
- [ ] Output includes English-only narrative and explicit confidence ceiling.
- [ ] Legacy constraints reviewed and applied where relevant.


## VCL COMPLIANCE APPENDIX (Internal Reference)

[[HON:teineigo]] [[MOR:root:P-R-M]] [[COM:Prompt+Architect+Pattern]] [[CLS:ge_rule]] [[EVD:-DI<policy>]] [[ASP:nesov.]] [[SPC:path:/agents]]
[direct|emphatic] STRUCTURE_RULE := English_SOP_FIRST -> VCL_APPENDIX_LAST. [ground:prompt-architect-SKILL] [conf:0.88] [state:confirmed]
[direct|emphatic] CEILING_RULE := {inference:0.70, report:0.70, research:0.85, observation:0.95, definition:0.95}; confidence statements MUST include ceiling syntax. [ground:prompt-architect-SKILL] [conf:0.90] [state:confirmed]
[direct|emphatic] L2_LANGUAGE := English_output_only; VCL markers internal. [ground:system-policy] [conf:0.99] [state:confirmed]

### Legacy Reference
<details>
<summary>Legacy content (verbatim)</summary>
<pre># Agents Directory

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Status:** 211 agents organised into ten functional categories
**Last reorganised:** 2025-11-26
**Common format:** Every agent uses Markdown with YAML front matter (name, type, phase, category, capabilities, tools, MCP servers, hooks, quality gates, artifact contracts).

**Recent additions (2025-11-26):**
- `specialists/finance/quant-analyst.md` - Quantitative trading and signal calibration
- `specialists/finance/risk-manager.md` - Risk quantification and compliance
- `specialists/finance/market-data-specialist.md` - Real-time market data integration

---

## Quick Category Overview

| Category | Description | Agent count | Example agents |
|----------|-------------|-------------|----------------|
| delivery | Feature and product implementation specialists covering architecture, backend, frontend, and SPARC execution | 18 | `delivery/development/backend/dev-backend-api.md`, `delivery/architecture/system-design/arch-system-design.md` |
| foundry | Agent creation, templates, registries, and base specialists that support building new automations | 19 | `foundry/core/base-template-generator.md`, `foundry/templates/skill-boilerplate-generator.md` |
| operations | DevOps, infrastructure, performance, and monitoring agents that keep systems healthy | 28 | `operations/devops/ci-cd/ops-cicd-github.md`, `operations/infrastructure/terraform/terraform-provisioner.md` |
| orchestration | Goal planners, swarm coordinators, and consensus agents for multi-agent workflows | 21 | `orchestration/consensus/byzantine-coordinator.md`, `orchestration/swarm/hierarchical-coordinator.md` |
| platforms | Data, ML, neural, Flow Nexus, and platform service agents | 44 | `platforms/ai-ml/automl/automl-optimizer.md`, `platforms/flow-nexus/multi-model-orchestrator.md` |
| quality | Analysis, audit, testing, and verification agents | 18 | `quality/analysis/code-analyzer.md`, `quality/testing/test-orchestrator.md` |
| research | Research, reasoning, emerging tech, and discovery agents | 11 | `research/archivist.md`, `research/emerging/arvr/ar-vr-developer.md` |
| security | Compliance, pentest, container, and cloud security specialists | 5 | `security/compliance/soc-compliance-auditor.md`, `security/pentest/penetration-testing-agent.md` |
| specialists | Domain specialists for business, industry, finance, and vertical workflows | 18 | `specialists/business/business-analyst.md`, `specialists/finance/quant-analyst.md`, `specialists/supply-chain/logistics-optimizer.md` |
| tooling | Documentation, GitHub, and knowledge tooling agents | 24 | `tooling/documentation/api-docs/docs-api-openapi.md`, `tooling/github/pr-manager.md` |

Totals include nested directories; for example `platforms/ai-ml/*` contributes to the platforms count.

---

## Directory Layout

```
agents/
  delivery/                 # Architecture, development, SPARC execution
  foundry/                  # Core, templates, registries, agent builders
  operations/               # DevOps, infrastructure, monitoring, optimization
  orchestration/            # Coordinators, consensus, goal planners, swarm agents
  platforms/                # Flow Nexus, AI/ML, database, neural services
  quality/                  # Analysis, audits, testing specialists
  research/                 # Research cores, reasoning, emerging technology scouts
  security/                 # Compliance, security, penetration testing
  specialists/              # Business, industry, finance, and other domain experts
    business/               # Business analyst, marketing, sales, product management
    finance/                # Quant analyst, risk manager, market data specialist
    supply-chain/           # Logistics, inventory, procurement
  tooling/                  # Documentation, GitHub, productivity tooling
  registry/                 # (moved to foundry/registry)
```

Each category folder preserves the prior domain structure (for example `delivery/development/backend/*`).

---

## Agent File Structure

Every agent Markdown file starts with YAML metadata followed by usage documentation. Typical sections include:

```
---
name: agent-name
type: coordinator | coder | analyst | optimizer | researcher | specialist
phase: planning | development | testing | deployment | maintenance
category: delivery
description: Short mission statement
capabilities: [...]
tools_required: [...]
mcp_servers:
  required:           # MCPs that MUST be enabled for this agent to function
    - memory-mcp      # Always required for cross-session memory
  optional:           # MCPs that enhance functionality but aren&#x27;t required
    - ruv-swarm       # For swarm coordination
    - flow-nexus      # For cloud features
  auto_enable: true   # If true, Claude Code will prompt to enable missing MCPs
hooks:
  pre: |
    # commands...
  post: |
    # commands...
quality_gates: [...]
artifact_contracts: [...]
---

# Agent Title

## When to use
...
```

---

## Finding the Right Agent

1. **Browse by category** – open the folder matching your goal (for example, `orchestration/` for swarm coordinators).  
2. **Use the registry** – `foundry/registry/registry.json` lists canonical agent metadata for automation.  
3. **Search by capability** – `rg &quot;capabilities:.*&lt;keyword&gt;&quot; agents` to locate agents with specific skills.  
4. **Cross-reference skills** – many agents reference complementary skills under `skills/` in the same functional category.

---

## Memory-MCP Integration

All 211 agents have access to the Memory-MCP triple-layer storage system for persistent memory across sessions.

### Configuration

Memory-MCP is configured in `identity/memory-mcp-config.json` and provides:

| Capability | Tier | Latency | Purpose |
|------------|------|---------|---------|
| `kv_store` | 1 | &lt;1ms | O(1) preference lookups |
| `vector_search` | 3 | &lt;100ms | Semantic search via embeddings |
| `graph_service` | 4 | &lt;50ms | Entity relationship graphs |
| `event_log` | 5 | &lt;10ms | Temporal event logging |
| `query_router` | - | - | Polyglot tier selection |

### Tagging Protocol (Required)

All memory writes MUST include these tags:

```yaml
WHO: &quot;{agent-type}:{agent-id}&quot;    # e.g., &quot;code-analyzer:601c545c&quot;
WHEN: &quot;{ISO-8601-timestamp}&quot;      # e.g., &quot;2025-12-28T09:47:04.638Z&quot;
PROJECT: &quot;{project-name}&quot;         # e.g., &quot;memory-mcp-triple-system&quot;
WHY: &quot;{purpose}&quot;                  # e.g., &quot;analysis&quot;, &quot;implementation&quot;, &quot;bugfix&quot;
```

### Memory Namespaces

| Namespace | Pattern | Used For |
|-----------|---------|----------|
| agents | `agents/{category}/{type}/{project}/{timestamp}` | Agent-specific memories |
| swarm | `swarm/{coordination-type}/{task-id}` | Swarm coordination state |
| expertise | `expertise/{domain}` | Domain expertise files |
| findings | `findings/{agent-type}/{severity}` | Code analysis findings |
| decisions | `decisions/{project}/{decision-id}` | Decision records |

### Access Levels by Role

| Role | Operations | Namespaces |
|------|------------|------------|
| admin | All | All |
| developer | set, get, delete, search, log_event | agents/*, swarm/*, findings/* |
| reviewer | get, search, query_by_date | agents/*, findings/*, decisions/* |
| coordinator | All | swarm/*, agents/* |
| analyst | get, search, query_by_date, find_path | All (read) |

### Example Usage

```python
# Store a finding
kv_store.set_json(&#x27;findings:code-analyzer:high:GOD-001&#x27;, {
    &#x27;WHO&#x27;: &#x27;code-analyzer:601c545c&#x27;,
    &#x27;WHEN&#x27;: datetime.now().isoformat(),
    &#x27;PROJECT&#x27;: &#x27;my-project&#x27;,
    &#x27;WHY&#x27;: &#x27;analysis&#x27;,
    &#x27;content&#x27;: &#x27;Found God Object with 0.26 cohesion&#x27;,
    &#x27;severity&#x27;: &#x27;high&#x27;
})

# Build knowledge graph
graph.add_relationship(&#x27;finding:GOD-001&#x27;, &#x27;fixed_by&#x27;, &#x27;pattern:facade&#x27;)

# Log event
event_log.log_event(EventType.QUERY_EXECUTED, {
    &#x27;agent&#x27;: &#x27;researcher&#x27;,
    &#x27;query&#x27;: &#x27;similar issues&#x27;,
    &#x27;results&#x27;: 5
})
```

### Agent YAML Configuration

Ensure agents declare memory-mcp in their frontmatter:

```yaml
mcp_servers:
  required:
    - memory-mcp      # Cross-session memory (always required)
  optional:
    - ruv-swarm       # Swarm coordination
  auto_enable: true

rbac:
  api_access:
    - memory-mcp      # Required for memory operations
```

---

## Updating or Adding Agents

1. Place new agents inside the category that matches their primary function.  
2. Follow the YAML + documentation structure above; keep hooks and quality gates up to date.  
3. Update this README and any relevant taxonomy docs (see `docs/agent-taxonomy/`) with counts and locations.  
4. Regenerate `foundry/registry/registry.json` if the agent should appear in the programmatic registry.

This organisation mirrors the skills directory, making it easier to align agents, skills, and SOPs by functional area.


---
*Promise: `&lt;promise&gt;README_VERIX_COMPLIANT&lt;/promise&gt;`*
</pre>
</details>

