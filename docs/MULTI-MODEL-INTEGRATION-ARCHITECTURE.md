# Multi-Model Integration Architecture for Context Cascade

## Executive Summary

This document outlines a comprehensive architecture for integrating Gemini CLI, Codex CLI, and LLM Council patterns into the Context Cascade system, while optimizing MCP context usage through CLI-based invocation.

**Key Insight**: Each model has distinct strengths that complement Claude:
- **Gemini**: Online research (Google Search grounding), 1M token context
- **Codex**: Autonomous sandbox execution, debugging, auditing
- **Claude**: Complex reasoning, comprehensive documentation, multi-step tasks

By routing tasks to optimal models and using Memory-MCP for coordination, we achieve LLM Council-style consensus without 58k+ token MCP overhead.

---

## 1. Research Findings Summary

### Gemini CLI Capabilities
```bash
# Installation
npm install -g @google/gemini-cli

# Basic usage
gemini "Your prompt here"
gemini "@file.ts Analyze this code"
gemini -o json "Query" > output.json

# Key features
- 1M token context window (vs Claude's 200k)
- Google Search grounding (real-time info)
- 70+ extensions (Figma, Stripe, etc.)
- MCP support via: gemini mcp add <name> <command>
- Session resume: gemini --resume latest
```

### Codex CLI Capabilities
```bash
# Full auto mode (sandboxed)
codex --full-auto "Build REST API with tests"
# Equivalent to: codex -a on-failure -s workspace-write

# Key features
- Autonomous execution (no approval needed)
- Sandbox isolation (no network, CWD only)
- Iterative test-fix loops
- GPT-5-Codex optimized for agentic coding
```

### LLM Council Pattern (Karpathy)
```
Stage 1: COLLECT - All models answer independently
Stage 2: RANK - Models cross-review (anonymized)
Stage 3: SYNTHESIZE - Chairman model produces final answer
```
- Reduces hallucination through consensus
- Different model perspectives catch errors
- OpenRouter for multi-provider routing

---

## 2. Integration Architecture

### Option A: Pre-Agent Layer (RECOMMENDED)

Route to optimal model BEFORE spawning Claude agents:

```
User Request
    |
    v
[Intent Analyzer]
    |
    +---> Research? ---> Gemini CLI (Google Search grounding)
    |                         |
    |                         v
    |                   [Store in Memory-MCP]
    |                         |
    +---> Audit/Debug? ---> Codex CLI (sandbox execution)
    |                         |
    |                         v
    |                   [Store in Memory-MCP]
    |                         |
    +---> Complex/Multi-step? ---> Claude Agents
    |                                   |
    |                                   v
    |                           [Read from Memory-MCP]
    |
    v
[Final Output]
```

**Implementation**:
```bash
# In pre-task hook or skill
function route_to_model() {
  case "$TASK_TYPE" in
    "research"|"search"|"current_events")
      gemini -o json "$PROMPT" | store_to_memory
      ;;
    "debug"|"audit"|"sandbox_test")
      codex --full-auto "$PROMPT" --context "$FILES"
      ;;
    *)
      # Default to Claude agents
      ;;
  esac
}
```

### Option B: Model-Locked Agents

Map specific agent types to external models:

| Agent Type | Model | Rationale |
|------------|-------|-----------|
| researcher | Gemini | Google Search grounding |
| auditor | Codex | Sandbox execution |
| code-analyzer | Codex | Debugging strengths |
| literature-synthesis | Gemini | 1M context for papers |
| coder | Claude | Complex multi-file edits |
| reviewer | Claude | Nuanced code review |

**Implementation**:
```yaml
# In agent definition
agent: researcher
model_override: gemini
invocation: |
  gemini -o json "@{context_files}" "{prompt}" | \
    jq '.content' | \
    memory_store "research/{task_id}" --namespace research
```

### Option C: LLM Council Consensus (For Critical Decisions)

Use all three models + voting for high-stakes decisions:

```
                    +---> Claude ---> Response A
                    |
User Query --------+---> Gemini ---> Response B
                    |
                    +---> Codex ----> Response C
                    |
                    v
             [Cross-Review via Memory-MCP]
                    |
                    v
             [Chairman (Claude) Synthesizes]
                    |
                    v
              Final Answer
```

**Implementation using DAA tools**:
```javascript
// Use existing DAA consensus mechanism
mcp__ruv-swarm__daa_consensus --agents="claude,gemini,codex" \
  --proposal="{\"query\": \"$QUERY\", \"threshold\": 0.67}"

// Store votes in memory
memory_store "council/votes/{query_id}" \
  --value "{claude: A, gemini: B, codex: C}"

// Chairman synthesis
gemini -o json "Synthesize these responses: $VOTES" | \
  memory_store "council/final/{query_id}"
```

---

## 3. CLI-Based Context Savings

### The Problem
Always-on MCPs consume context even when unused:
- flow-nexus: 58k tokens
- ruv-swarm: 15.5k tokens
- playwright: 14.5k tokens

### The Solution: Terminal CLI Invocation

**Pattern 1: Direct CLI (Zero MCP Cost)**
```bash
# Instead of loading 15.5k token ruv-swarm MCP
npx claude-flow swarm "Build API" --topology=hierarchical

# Instead of loading 58k token flow-nexus MCP
npx flow-nexus sandbox create --name test-env
```

**Pattern 2: Hybrid (Load Only When Needed)**
```bash
# Enable MCP for workflow
claude mcp add ruv-swarm npx ruv-swarm mcp start

# Do multi-agent work...

# Disable when done
claude mcp remove ruv-swarm
```

**Pattern 3: Memory-MCP as Central Hub**
```
Gemini CLI --> Memory-MCP <-- Claude Agents
                  ^
                  |
              Codex CLI
```

All models read/write to Memory-MCP, but only Memory-MCP (~1.2k tokens) stays loaded.

---

## 4. Memory-MCP Coordination Protocol

### Namespace Structure for Multi-Model
```
multi-model/
  gemini/
    research/{task_id}       # Gemini research results
    search/{query_hash}      # Cached search results
  codex/
    audit/{task_id}          # Audit results
    fixes/{finding_id}       # Applied fixes
  council/
    votes/{query_id}         # Model votes
    final/{query_id}         # Synthesized answer
  coordination/
    handoff/{from}/{to}      # Model handoff state
```

### Tagging Protocol (WHO/WHEN/PROJECT/WHY)
```json
{
  "WHO": "gemini-cli:research",
  "WHEN": "2025-12-28T15:00:00Z",
  "PROJECT": "context-cascade",
  "WHY": "literature-synthesis",
  "MODEL": "gemini-2.5-pro",
  "TOKENS_USED": 45000,
  "GROUNDING": "google-search"
}
```

### Cross-Model Communication Flow
```javascript
// Gemini stores research
gemini -o json "Research best practices for auth" | \
  memory_store "multi-model/gemini/research/auth-001" \
    --tags '{"WHO":"gemini","WHY":"research"}'

// Claude agent reads research
const research = memory_retrieve("multi-model/gemini/research/auth-001")
Task("Coder", `Implement auth using: ${research.content}`, "coder")

// Codex audits implementation
codex --full-auto "Audit auth implementation" --context src/auth/

// Claude reviews audit
const audit = memory_retrieve("multi-model/codex/audit/auth-001")
Task("Reviewer", `Review audit findings: ${audit.findings}`, "reviewer")
```

---

## 5. Implementation Plan

### Phase 1: CLI Wrappers (Week 1)
```bash
# scripts/multi-model/gemini-research.sh
#!/bin/bash
QUERY="$1"
TASK_ID="${2:-$(uuidgen)}"

# Execute Gemini research
RESULT=$(gemini -o json "$QUERY")

# Store to Memory-MCP
echo "$RESULT" | jq -c '{
  content: .content,
  sources: .sources,
  model: "gemini-2.5-pro",
  timestamp: now | todate
}' | memory_store "multi-model/gemini/research/$TASK_ID"

echo "Research stored: multi-model/gemini/research/$TASK_ID"
```

```bash
# scripts/multi-model/codex-audit.sh
#!/bin/bash
TASK="$1"
CONTEXT="$2"
TASK_ID="${3:-$(uuidgen)}"

# Execute Codex audit
codex --full-auto "$TASK" --context "$CONTEXT" \
  --sandbox true --max-iterations 5 \
  > /tmp/codex-result-$TASK_ID.md

# Store to Memory-MCP
cat /tmp/codex-result-$TASK_ID.md | memory_store \
  "multi-model/codex/audit/$TASK_ID" \
  --tags '{"WHO":"codex","WHY":"audit"}'

echo "Audit stored: multi-model/codex/audit/$TASK_ID"
```

### Phase 2: Skill Integration (Week 2)

Create new skills that invoke external models:

```yaml
# skills/multi-model/gemini-research/SKILL.md
---
name: gemini-research
description: Use Gemini CLI for research with Google Search grounding
allowed-tools: Bash, Read, Write, TodoWrite
---

## When to Use
- Real-time information needed
- Large document analysis (>200k tokens)
- Need Google Search grounding

## Invocation
bash scripts/multi-model/gemini-research.sh "$QUERY" "$TASK_ID"

## Output
Stored in Memory-MCP: multi-model/gemini/research/{task_id}
```

### Phase 3: Agent Router Enhancement (Week 3)

Update agent-selector to consider model strengths:

```javascript
// In agent-selector skill
function selectOptimalAgent(task) {
  const taskType = analyzeTaskType(task);

  // Route to external models for their strengths
  if (taskType.needsRealtimeSearch) {
    return { model: 'gemini', script: 'gemini-research.sh' };
  }
  if (taskType.needsSandboxExecution) {
    return { model: 'codex', script: 'codex-audit.sh' };
  }
  if (taskType.needsLargeContext && taskType.tokens > 150000) {
    return { model: 'gemini', script: 'gemini-megacontext.sh' };
  }

  // Default to Claude agents
  return { model: 'claude', agent: selectClaudeAgent(task) };
}
```

### Phase 4: LLM Council Integration (Week 4)

Implement consensus for critical decisions:

```javascript
// skills/multi-model/llm-council/SKILL.md
async function runCouncil(query, options = {}) {
  const { threshold = 0.67, chairman = 'claude' } = options;

  // Stage 1: Collect responses
  const responses = await Promise.all([
    bash(`gemini -o json "${query}"`),
    bash(`codex --full-auto "${query}" --sandbox true`),
    // Claude responds inline
  ]);

  // Stage 2: Cross-review (anonymized)
  const reviews = await crossReview(responses);

  // Stage 3: Synthesize (chairman)
  const final = await synthesize(reviews, chairman);

  // Store decision
  memory_store(`council/decisions/${Date.now()}`, {
    query, responses, reviews, final,
    consensus: calculateConsensus(reviews)
  });

  return final;
}
```

---

## 6. Context Budget Analysis

### Before Multi-Model Optimization
```
Context Budget: 200,000 tokens

Always-on MCPs:      -111,100 tokens (55.5%)
System prompts:       -38,000 tokens (19%)
Available for work:    50,900 tokens (25.5%)
```

### After Optimization (Current)
```
Context Budget: 200,000 tokens

Core MCPs:             -2,700 tokens (1.4%)
System prompts:       -38,000 tokens (19%)
Available for work:   159,300 tokens (79.6%)
```

### With Multi-Model CLI Routing
```
Context Budget: 200,000 tokens

Core MCPs:             -2,700 tokens (1.4%)  [memory + sequential-thinking]
System prompts:       -38,000 tokens (19%)
Available for work:   159,300 tokens (79.6%)

PLUS: External model capacity
- Gemini: +1,000,000 tokens (separate context)
- Codex: Unlimited (sandbox execution)
- Council: 3x perspectives on critical decisions
```

**Effective Expansion**: 5x+ capacity through multi-model routing

---

## 7. Recommended Integration Strategy

### Immediate (This Week)
1. Create CLI wrapper scripts for Gemini/Codex
2. Define Memory-MCP namespaces for multi-model
3. Test basic research -> Claude handoff

### Short-term (Next 2 Weeks)
1. Create gemini-research and codex-audit skills
2. Update agent-selector with model routing
3. Implement cross-model memory coordination

### Medium-term (Month 1)
1. Full LLM Council integration for critical decisions
2. Auto-routing based on task analysis
3. Metrics tracking for model performance

### Long-term (Quarter 1)
1. Fine-tune routing based on success rates
2. Custom model combinations per domain
3. Expertise system integration (which model for which domain)

---

## 8. Quick Reference

### When to Use Each Model

| Task Type | Best Model | Reason |
|-----------|------------|--------|
| Real-time search | Gemini | Google Search grounding |
| Large codebase analysis | Gemini | 1M token context |
| Autonomous prototyping | Codex | --full-auto sandbox |
| Iterative debugging | Codex | Test-fix-retest loop |
| Complex multi-file edits | Claude | Superior reasoning |
| Code review | Claude | Nuanced evaluation |
| Critical decisions | Council | Consensus reduces errors |
| Documentation | Claude | Comprehensive output |

### CLI Quick Commands
```bash
# Gemini research
gemini "Current best practices for X" | memory_store research/X

# Codex audit
codex --full-auto "Audit src/ for bugs" --sandbox true

# Council decision
./scripts/multi-model/council.sh "Should we use approach A or B?"
```

### Memory Keys
```
multi-model/gemini/research/{task_id}
multi-model/codex/audit/{task_id}
multi-model/council/decisions/{timestamp}
multi-model/handoff/{from}/{to}/{task_id}
```

---

## Sources

- [LLM Council by Andrej Karpathy](https://medium.com/@meshuggah22/andrej-karpathys-llm-council-when-ensemble-learning-meets-large-language-models-e3312fd02064)
- [Karpathy's LLM Council Explained](https://www.analyticsvidhya.com/blog/2025/12/llm-council-by-andrej-karpathy/)
- [VentureBeat: Karpathy's AI Council](https://venturebeat.com/ai/a-weekend-vibe-code-hack-by-andrej-karpathy-quietly-sketches-the-missing)
- [Building AI Council Architecture](https://skillwisor.com/2025/11/30/building-an-ai-council-a-deep-dive-into-the-llm-council-architecture/)
