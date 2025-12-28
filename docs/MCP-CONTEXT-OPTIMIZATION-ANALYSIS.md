# MCP Context Optimization Analysis

## Executive Summary

This analysis examines the claude-flow MCP ecosystem to identify:
1. Which MCPs are **unique** (still provide value not available natively)
2. Which MCPs are **outdated** (redundant with Claude Code native tools)
3. How **CLI-based invocation** can save context vs always-on MCPs

**Key Finding**: We achieved 97% context reduction by strategic MCP management - from 111k tokens (55% of context) to 2.7k tokens (1.4%) at startup.

---

## 1. Current MCP Architecture

### Always-On (Core) MCPs - 2.7k tokens

| MCP | Tokens | Purpose | Verdict |
|-----|--------|---------|---------|
| memory-mcp | 1,200 | Cross-session persistence, vector search | KEEP - No native equivalent |
| sequential-thinking | 1,500 | Complex reasoning chains | KEEP - Unique meta-cognition |

### Situational MCPs (Load on Demand)

| MCP | Tokens | Purpose | Verdict |
|-----|--------|---------|---------|
| ruv-swarm | 15,500 | Multi-agent coordination, DAA | UNIQUE - Keep situational |
| playwright | 14,500 | Browser automation, E2E testing | UNIQUE - No native equivalent |
| flow-nexus | 58,000 | Neural training, sandboxes, GitHub | SPLIT NEEDED - Monolithic |
| agentic-payments | 6,600 | Payment mandates, transactions | UNIQUE - Domain-specific |
| focused-changes | 1,800 | Change tracking, root cause | PARTIALLY OUTDATED |
| toc | 613 | Table of contents generation | OUTDATED - Scripting does this |

### Removed MCPs (Confirmed Redundant)

| MCP | Tokens | Replaced By |
|-----|--------|-------------|
| filesystem | 9,200 | Native: Read, Write, Edit, Glob, Grep |
| fetch | 826 | Native: WebFetch |

---

## 2. Unique vs Outdated Analysis

### UNIQUE - These MCPs Provide Capabilities Not Available Natively

#### DAA (Distributed Autonomous Agents) - 8 tools
```
daa_agent_create      - Dynamic agent creation at runtime
daa_capability_match  - Intelligent task-capability matching
daa_communication     - Inter-agent message passing
daa_consensus         - Byzantine fault-tolerant voting
daa_fault_tolerance   - Automatic failure recovery
daa_lifecycle_manage  - Agent lifecycle orchestration
```

**Why unique**: Claude Code's Task tool spawns subagents, but:
- No native consensus mechanism between agents
- No Byzantine fault tolerance
- No automatic capability matching
- Subagents don't communicate directly (only through parent)

#### Swarm Coordination - 12 tools
```
swarm_init           - Multi-topology support (hierarchical, mesh, hive)
topology_optimize    - Auto-optimize based on task shape
load_balance         - Dynamic task distribution
coordination_sync    - Agent state synchronization
swarm_scale          - Auto-scaling based on workload
```

**Why unique**: Task tool parallelism is flat; these provide:
- Hierarchical command structures (Queen-Worker)
- Mesh networking (peer-to-peer gossip)
- Dynamic topology switching

#### Neural Training - 15 tools
```
neural_train         - Distributed neural network training
wasm_optimize        - WASM SIMD acceleration
ensemble_create      - Model ensembles
transfer_learn       - Transfer learning workflows
```

**Why unique**: No native ML training capabilities in Claude Code.

#### E2B Sandboxes (in flow-nexus)
```
sandbox_create       - Cloud execution environments
sandbox_execute      - Isolated code execution
sandbox_stream       - Real-time output streaming
```

**Why unique**: Claude Code runs locally; these provide cloud isolation.

### OUTDATED - Redundant with Native Claude Code

| Tool Category | MCP Tool | Native Replacement |
|--------------|----------|-------------------|
| File read | filesystem.read | Read tool |
| File write | filesystem.write | Write tool |
| File edit | filesystem.edit | Edit tool |
| File search | filesystem.glob | Glob tool |
| Content search | filesystem.grep | Grep tool |
| Web fetch | fetch.get | WebFetch tool |
| TOC generation | toc.generate | Grep + scripting |
| Change tracking | focused-changes | git diff + LSP |

### PARTIALLY OUTDATED - Keep for Specific Use Cases

| MCP | Native Overlap | Unique Value |
|-----|----------------|--------------|
| focused-changes | git diff | Root cause analysis graphs |
| memory-mcp (some) | Task persistence | Vector search, knowledge graphs |

---

## 3. CLI-Based vs Always-On Context Savings

### The Problem

Always-on MCPs consume context tokens even when unused:
- Tool definitions loaded at startup
- Schema descriptions in every request
- Accumulated overhead per interaction

### The Solution: CLI Invocation Patterns

#### Pattern 1: One-Shot CLI Execution (Zero Context Cost)

Instead of loading MCP for single operation:
```bash
# Direct CLI execution - no MCP context needed
npx claude-flow swarm "Build REST API" --agents=3 --topology=hierarchical

# Get results without MCP loaded
npx claude-flow mcp tools --category=swarm
```

**Savings**: 15.5k tokens per session when only needed once

#### Pattern 2: Dynamic MCP Loading

Enable only when needed, disable after:
```bash
# Enable for workflow
claude mcp add ruv-swarm npx ruv-swarm mcp start

# Do work with MCP tools...

# Disable when done
claude mcp remove ruv-swarm
```

**Savings**: Context freed after MCP removed

#### Pattern 3: Sub-Module MCP Split (Recommended for flow-nexus)

Current flow-nexus: 58,000 tokens (monolithic)

Proposed split:
```
flow-nexus-swarm    -  7,000 tokens  (swarm tools only)
flow-nexus-neural   - 12,000 tokens  (ML training only)
flow-nexus-sandbox  -  6,000 tokens  (E2B only)
flow-nexus-github   -  2,000 tokens  (repo analysis only)
flow-nexus-workflow -  5,000 tokens  (workflow automation)
flow-nexus-platform - 15,000 tokens  (user auth, rarely needed)
```

**Savings**: Load only what's needed = 43k-51k token savings

---

## 4. Context Budget Analysis

### Before Optimization (All MCPs Always-On)
```
Total Available:     200,000 tokens
MCP Overhead:       -111,100 tokens (55.5%)
System Prompts:      -38,000 tokens (19%)
Available for Work:   50,900 tokens (25.5%)
```

### After Optimization (Current State)
```
Total Available:     200,000 tokens
Core MCPs:            -2,700 tokens (1.4%)
System Prompts:      -38,000 tokens (19%)
Available for Work:  159,300 tokens (79.6%)
```

### Optimal State (With CLI Patterns)
```
Total Available:     200,000 tokens
Core MCPs:            -2,700 tokens (1.4%)  [memory + sequential-thinking]
System Prompts:      -38,000 tokens (19%)
Available for Work:  159,300 tokens (79.6%)

+ Situational on-demand:
  ruv-swarm via CLI: 0 tokens (until enabled)
  flow-nexus-swarm: 7,000 tokens (when needed)
```

---

## 5. Recommendations

### Immediate Actions

1. **Keep current core MCPs** (memory-mcp, sequential-thinking)
   - Essential for session persistence and reasoning
   - Low token cost (2.7k total)

2. **Use CLI for one-off swarm operations**
   ```bash
   npx claude-flow swarm "task" --topology=hierarchical
   ```
   Instead of enabling ruv-swarm MCP for single use

3. **Request flow-nexus modularization**
   - Split into focused sub-packages
   - Each sub-module independently installable

### Architecture Changes

1. **Implement MCP Lazy Loading Hook**
   ```javascript
   // In pre-tool hook
   if (toolNeedsSwarm && !mcpEnabled('ruv-swarm')) {
     exec('claude mcp add ruv-swarm npx ruv-swarm mcp start');
   }
   ```

2. **Create CLI Wrappers for Common Operations**
   ```bash
   # scripts/swarm-task.sh
   npx claude-flow swarm "$1" --topology="${2:-hierarchical}"
   # No MCP needed, direct CLI
   ```

3. **Deprecate Redundant Tools**
   - Remove toc MCP (use Grep + scripting)
   - Remove filesystem MCP (already done)
   - Evaluate focused-changes vs native git

### Long-Term Strategy

| Phase | Action | Context Savings |
|-------|--------|-----------------|
| Now | Use CLI for one-off swarm | 15.5k per session |
| Q1 | Split flow-nexus into modules | 43-51k per session |
| Q2 | Auto-load/unload based on task | Dynamic optimization |
| Q3 | Upstream redundant tool removal | Permanent reduction |

---

## 6. MCP Tool-to-Native Mapping

### File Operations (REMOVED - Use Native)

| MCP Tool | Native Tool | Notes |
|----------|-------------|-------|
| filesystem.read_file | Read | Identical functionality |
| filesystem.write_file | Write | Identical functionality |
| filesystem.edit_file | Edit | Native has better diff support |
| filesystem.list_files | Glob | Native supports patterns |
| filesystem.search_content | Grep | Native supports regex |

### Web Operations (REMOVED - Use Native)

| MCP Tool | Native Tool | Notes |
|----------|-------------|-------|
| fetch.get | WebFetch | Native handles redirects |
| fetch.post | WebFetch | Native has AI processing |

### Swarm Operations (KEEP - Unique)

| MCP Tool | Native Equivalent | Gap |
|----------|-------------------|-----|
| swarm_init | Task (parallel) | No topology control |
| daa_consensus | None | No voting mechanism |
| daa_communication | Task results | No peer-to-peer |
| topology_optimize | None | No auto-optimization |

### Neural Operations (KEEP - Unique)

| MCP Tool | Native Equivalent | Gap |
|----------|-------------------|-----|
| neural_train | None | No ML training |
| wasm_optimize | None | No WASM acceleration |
| neural_predict | None | No inference runtime |

---

## 7. Summary

### What's Unique (Keep)
- DAA consensus mechanisms
- Swarm topology management
- Neural training orchestration
- E2B cloud sandboxes
- Cross-session vector memory

### What's Outdated (Remove/Removed)
- Filesystem operations (native Read/Write/Edit/Glob/Grep)
- Web fetch (native WebFetch)
- TOC generation (scripting)

### Context Optimization Strategy
1. **Default**: Only core MCPs (2.7k tokens)
2. **On-demand**: CLI invocation for one-off tasks
3. **Temporary**: Dynamic MCP enable/disable for workflows
4. **Future**: Request modular MCP packages from maintainers

### Achieved Savings
- **Before**: 111.1k tokens (55.5% of context)
- **After**: 2.7k tokens (1.4% of context)
- **Savings**: 108.4k tokens (97% reduction)
