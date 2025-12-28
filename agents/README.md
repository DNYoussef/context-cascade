# Agents Directory

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
  optional:           # MCPs that enhance functionality but aren't required
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
3. **Search by capability** – `rg "capabilities:.*<keyword>" agents` to locate agents with specific skills.  
4. **Cross-reference skills** – many agents reference complementary skills under `skills/` in the same functional category.

---

## Memory-MCP Integration

All 211 agents have access to the Memory-MCP triple-layer storage system for persistent memory across sessions.

### Configuration

Memory-MCP is configured in `identity/memory-mcp-config.json` and provides:

| Capability | Tier | Latency | Purpose |
|------------|------|---------|---------|
| `kv_store` | 1 | <1ms | O(1) preference lookups |
| `vector_search` | 3 | <100ms | Semantic search via embeddings |
| `graph_service` | 4 | <50ms | Entity relationship graphs |
| `event_log` | 5 | <10ms | Temporal event logging |
| `query_router` | - | - | Polyglot tier selection |

### Tagging Protocol (Required)

All memory writes MUST include these tags:

```yaml
WHO: "{agent-type}:{agent-id}"    # e.g., "code-analyzer:601c545c"
WHEN: "{ISO-8601-timestamp}"      # e.g., "2025-12-28T09:47:04.638Z"
PROJECT: "{project-name}"         # e.g., "memory-mcp-triple-system"
WHY: "{purpose}"                  # e.g., "analysis", "implementation", "bugfix"
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
kv_store.set_json('findings:code-analyzer:high:GOD-001', {
    'WHO': 'code-analyzer:601c545c',
    'WHEN': datetime.now().isoformat(),
    'PROJECT': 'my-project',
    'WHY': 'analysis',
    'content': 'Found God Object with 0.26 cohesion',
    'severity': 'high'
})

# Build knowledge graph
graph.add_relationship('finding:GOD-001', 'fixed_by', 'pattern:facade')

# Log event
event_log.log_event(EventType.QUERY_EXECUTED, {
    'agent': 'researcher',
    'query': 'similar issues',
    'results': 5
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
