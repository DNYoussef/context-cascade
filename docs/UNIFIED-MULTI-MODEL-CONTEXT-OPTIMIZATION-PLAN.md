# Unified Multi-Model & Context Optimization Plan

## Executive Summary

This plan combines:
1. **MCP Context Optimization** - Reduce 111k tokens to 2.7k (97% reduction)
2. **Multi-Model Integration** - Gemini, Codex, LLM Council patterns
3. **Memory-MCP Coordination** - Cross-model communication via shared memory
4. **Meta-Loop Integration** - Self-improvement pipeline compatibility

---

## PART 1: RESEARCH FINDINGS

### 1.1 Internal System Architecture

**Agent Coordination Pattern**:
```
Agents --> Memory-MCP Namespaces --> Other Agents
              |
              v
         swarm/{agent-type}/{scope}
```

- No direct agent-to-agent messaging
- 30-second heartbeat cycles for state sync
- Three topologies: Hierarchical, Mesh, Hive Mind
- Byzantine fault tolerance (2f+1 voting)

**Meta-Loop Pipeline**:
```
PROPOSE (4 auditors) --> TEST (frozen eval) --> COMPARE --> COMMIT --> MONITOR --> ROLLBACK
```

- Frozen eval harness prevents Goodhart's Law
- 90-day rollback window
- Prompt Forge <-> Skill Forge mutual improvement

### 1.2 MCP Status Analysis

| Category | MCPs | Tokens | Status |
|----------|------|--------|--------|
| REMOVED | filesystem, fetch | 10k | Native tools replace |
| CORE | memory-mcp, sequential-thinking | 2.7k | Always-on |
| UNIQUE | DAA, swarm topology | 15.5k | Keep situational |
| UNIQUE | Neural, E2B sandboxes | 58k | Needs modular split |
| PARTIAL | focused-changes, toc | 2.4k | Some overlap |

### 1.3 External Model Capabilities

| Model | Strengths | CLI Command | Context |
|-------|-----------|-------------|---------|
| Gemini | Search grounding, extensions | `gemini "query"` | 1M tokens |
| Codex | Sandbox execution, debugging | `codex --full-auto` | Unlimited |
| Claude | Reasoning, multi-step | Native | 200k tokens |

### 1.4 LLM Council Pattern

```
Stage 1: COLLECT   - All models answer independently
Stage 2: RANK      - Cross-review (anonymized)
Stage 3: SYNTHESIZE - Chairman produces final
```

---

## PART 2: SPECIFICATIONS

### 2.1 CLI Wrapper Scripts

**Spec: gemini-research.sh**
```yaml
name: gemini-research
purpose: Execute Gemini CLI and store results in Memory-MCP
inputs:
  - query: string (required)
  - task_id: string (optional, auto-generated)
  - output_format: json|text (default: json)
outputs:
  - memory_key: multi-model/gemini/research/{task_id}
  - stdout: JSON with content, sources, timestamp
behavior:
  - Execute gemini -o json "{query}"
  - Parse response
  - Store to Memory-MCP with WHO/WHEN/PROJECT/WHY tags
  - Return memory key for downstream agents
error_handling:
  - Retry 3x on timeout
  - Fall back to Claude research if Gemini unavailable
```

**Spec: codex-audit.sh**
```yaml
name: codex-audit
purpose: Execute Codex CLI in sandbox and store audit results
inputs:
  - task: string (required)
  - context: file path or directory (required)
  - max_iterations: int (default: 5)
  - sandbox: boolean (default: true)
outputs:
  - memory_key: multi-model/codex/audit/{task_id}
  - stdout: Markdown audit report
behavior:
  - Execute codex --full-auto "{task}" --context "{context}"
  - Capture stdout/stderr
  - Parse results into structured format
  - Store to Memory-MCP
constraints:
  - Network DISABLED (sandbox)
  - CWD only access
  - Max 5 iterations by default
```

**Spec: llm-council.sh**
```yaml
name: llm-council
purpose: Run 3-stage consensus across Claude, Gemini, Codex
inputs:
  - query: string (required)
  - threshold: float (default: 0.67)
  - chairman: claude|gemini (default: claude)
outputs:
  - memory_key: multi-model/council/decisions/{timestamp}
  - stdout: Final synthesized answer
stages:
  1_collect:
    - Parallel: gemini, codex, claude respond
    - Store: council/responses/{query_id}/{model}
  2_rank:
    - Each model reviews others (anonymized)
    - Store: council/reviews/{query_id}/{reviewer}
  3_synthesize:
    - Chairman aggregates reviews
    - Produce final answer
    - Store: council/final/{query_id}
```

### 2.2 Memory-MCP Namespace Schema

```yaml
namespaces:
  multi-model:
    gemini:
      research/{task_id}:
        content: string
        sources: array
        model: string
        tokens_used: int
        timestamp: ISO8601
      search/{query_hash}:
        cached: boolean
        ttl: 3600
    codex:
      audit/{task_id}:
        findings: array
        severity_counts: object
        files_analyzed: array
        fixes_applied: array
      sandbox/{session_id}:
        commands: array
        files_created: array
        test_results: object
    council:
      responses/{query_id}/{model}:
        content: string
        confidence: float
      reviews/{query_id}/{reviewer}:
        rankings: array
        rationale: string
      final/{query_id}:
        answer: string
        consensus_score: float
        dissenting: array
    coordination:
      handoff/{from}/{to}/{task_id}:
        context: string
        artifacts: array
        next_action: string
```

### 2.3 Skill Specifications

**Skill: gemini-research**
```yaml
name: gemini-research
description: Use Gemini CLI for research with Google Search grounding
allowed-tools: Bash, Read, Write, TodoWrite, WebFetch
triggers:
  - "search for"
  - "find current"
  - "research online"
  - "latest information"
routing:
  pre_check: Is real-time info needed? Is context >150k tokens?
  if_yes: Route to this skill
  if_no: Use Claude researcher agent
memory_integration:
  write_to: multi-model/gemini/research/{task_id}
  tags: {WHO: gemini-cli, WHY: research}
```

**Skill: codex-audit**
```yaml
name: codex-audit
description: Use Codex CLI for sandboxed auditing and debugging
allowed-tools: Bash, Read, Write, TodoWrite, Glob, Grep
triggers:
  - "audit code"
  - "debug in sandbox"
  - "fix tests automatically"
  - "prototype quickly"
routing:
  pre_check: Needs autonomous iteration? Needs sandbox isolation?
  if_yes: Route to this skill
  if_no: Use Claude code-analyzer agent
memory_integration:
  write_to: multi-model/codex/audit/{task_id}
  tags: {WHO: codex-cli, WHY: audit}
```

**Skill: llm-council**
```yaml
name: llm-council
description: Multi-model consensus for critical decisions
allowed-tools: Bash, Read, Write, TodoWrite
triggers:
  - "get consensus"
  - "multiple perspectives"
  - "critical decision"
  - "reduce hallucination"
phases:
  collect: Parallel model invocation
  rank: Cross-review with anonymization
  synthesize: Chairman aggregation
memory_integration:
  write_to: multi-model/council/decisions/{timestamp}
  tags: {WHO: llm-council, WHY: consensus}
```

### 2.4 Agent Router Enhancement Spec

```yaml
enhancement: model-aware-routing
location: skills/orchestration/agent-selector/SKILL.md
changes:
  - Add model_override field to routing decisions
  - Check task characteristics for model affinity
  - Integrate with Memory-MCP for model performance history

routing_logic:
  if:
    - task.needs_realtime_search: true
    - task.context_tokens > 150000
  then:
    model: gemini
    script: gemini-research.sh

  elif:
    - task.needs_sandbox: true
    - task.type in [audit, debug, prototype]
  then:
    model: codex
    script: codex-audit.sh

  elif:
    - task.criticality == high
    - task.type == decision
  then:
    model: council
    script: llm-council.sh

  else:
    model: claude
    agent: select_from_registry(task)
```

---

## PART 3: PRE-MORTEM ANALYSIS

### 3.1 What Could Go Wrong

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Gemini API rate limits | Medium | High | Implement caching, fallback to Claude |
| Codex sandbox breaks | Low | Medium | Catch errors, retry with constraints |
| Memory-MCP sync delays | Medium | Medium | Add heartbeat checks, timeout handling |
| Model disagreement in council | High | Low | Use threshold voting, chairman tiebreak |
| CLI scripts fail on Windows | Medium | High | Test on Windows, use cross-platform syntax |
| Context overflow despite optimization | Low | High | Monitor token usage, alert thresholds |
| External models return garbage | Medium | Medium | Validate outputs before storing |
| Coordination deadlocks | Low | High | Implement timeouts, dead letter queues |

### 3.2 Failure Mode Analysis

**Failure Mode 1: Gemini Unavailable**
```
Trigger: API error, rate limit, auth failure
Detection: Non-zero exit code from gemini CLI
Response:
  1. Log error to multi-model/errors/gemini/{timestamp}
  2. Fall back to Claude researcher agent
  3. Mark task as "degraded_execution"
  4. Continue with reduced capability
```

**Failure Mode 2: Codex Sandbox Escape**
```
Trigger: Code tries to access outside CWD
Detection: Permission denied errors
Response:
  1. Terminate sandbox immediately
  2. Log attempt to security/violations/{timestamp}
  3. Alert user
  4. Do not store results
```

**Failure Mode 3: Council Deadlock**
```
Trigger: All models return different answers, no consensus
Detection: Consensus score < threshold after N rounds
Response:
  1. Log deadlock to council/deadlocks/{query_id}
  2. Request human intervention
  3. Store all perspectives for manual review
  4. Do not auto-proceed
```

**Failure Mode 4: Memory-MCP Corruption**
```
Trigger: Concurrent writes, invalid JSON
Detection: Parse errors on read
Response:
  1. Rollback to last known good state
  2. Retry write with exponential backoff
  3. Log corruption event
  4. Alert if repeated
```

### 3.3 Success Criteria

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| Context reduction | 97%+ | Before/after token count |
| Multi-model routing accuracy | >90% | Correct model for task type |
| Council consensus rate | >80% | Decisions reaching threshold |
| Memory-MCP write success | >99.5% | Successful stores / attempts |
| End-to-end latency | <30s | Task submission to result |
| Cross-model handoff success | >95% | Clean handoffs / total |

---

## PART 4: IMPLEMENTATION STEPS

### Phase 1: Foundation (Day 1)

**Step 1.1: Create CLI Wrapper Scripts**
- [ ] Create `scripts/multi-model/gemini-research.sh`
- [ ] Create `scripts/multi-model/codex-audit.sh`
- [ ] Create `scripts/multi-model/llm-council.sh`
- [ ] Test each script independently
- [ ] Audit with Connascence analyzer

**Step 1.2: Define Memory Namespaces**
- [ ] Create namespace schema in Memory-MCP
- [ ] Test write/read operations
- [ ] Verify cross-model access
- [ ] Document namespace conventions

### Phase 2: Skill Creation (Day 2)

**Step 2.1: Create Multi-Model Skills**
- [ ] Create `skills/multi-model/gemini-research/SKILL.md`
- [ ] Create `skills/multi-model/codex-audit/SKILL.md`
- [ ] Create `skills/multi-model/llm-council/SKILL.md`
- [ ] Validate YAML frontmatter
- [ ] Test skill invocation

**Step 2.2: Update Agent Selector**
- [ ] Add model_override routing logic
- [ ] Implement task characteristic analysis
- [ ] Add fallback handling
- [ ] Test routing decisions

### Phase 3: Integration (Day 3)

**Step 3.1: Hook Integration**
- [ ] Update PreToolUse hook for model routing
- [ ] Update PostToolUse hook for result storage
- [ ] Add Memory-MCP tagging enforcement
- [ ] Test hook execution flow

**Step 3.2: Coordinator Integration**
- [ ] Update hierarchical-coordinator for multi-model
- [ ] Add external model support to mesh-coordinator
- [ ] Implement council pattern in hive-mind

### Phase 4: Testing & Validation (Day 4)

**Step 4.1: Unit Tests**
- [ ] Test each CLI wrapper script
- [ ] Test each skill independently
- [ ] Test routing logic
- [ ] Test memory operations

**Step 4.2: Integration Tests**
- [ ] Test Gemini -> Claude handoff
- [ ] Test Codex -> Claude handoff
- [ ] Test full Council workflow
- [ ] Test failure recovery

**Step 4.3: Quality Audit**
- [ ] Run Connascence analyzer on all new code
- [ ] Fix any violations
- [ ] Document quality metrics

### Phase 5: Documentation & Deployment (Day 5)

**Step 5.1: Documentation**
- [ ] Update CLAUDE.md with multi-model section
- [ ] Create quick reference guide
- [ ] Document troubleshooting steps
- [ ] Update skill trigger index

**Step 5.2: Deployment**
- [ ] Commit all changes
- [ ] Push to GitHub
- [ ] Verify hook enforcement active
- [ ] Monitor for issues

---

## PART 5: EXECUTION PLAYBOOK ROUTING

| Phase | Tasks | Playbook | Skills | Agents |
|-------|-------|----------|--------|--------|
| 1.1 | CLI scripts | simple-feature-implementation | sparc-methodology | coder |
| 1.2 | Memory namespaces | database-design | agentdb-memory-patterns | data-steward |
| 2.1 | Multi-model skills | skill-creation | skill-creator-agent | skill-creator |
| 2.2 | Agent selector | refactoring-technical-debt | code-review-assistant | reviewer |
| 3.1 | Hook integration | infrastructure | cicd-intelligent-recovery | devops |
| 3.2 | Coordinator update | three-loop-system | cascade-orchestrator | hierarchical-coordinator |
| 4.1 | Unit tests | testing-quality | testing-quality | tester |
| 4.2 | Integration tests | e2e-testing | functionality-audit | e2e-tester |
| 4.3 | Quality audit | comprehensive-review | clarity-linter, connascence | code-analyzer |
| 5.1 | Documentation | comprehensive-documentation | documentation | technical-writer |
| 5.2 | Deployment | production-deployment | deployment-readiness | release-engineer |

---

## PART 6: MONITORING & ROLLBACK

### Metrics to Track

```yaml
metrics:
  context_usage:
    before: 111100
    target: 2700
    alert_threshold: 10000

  model_routing:
    gemini_invocations: counter
    codex_invocations: counter
    council_invocations: counter
    fallback_count: counter

  memory_operations:
    writes_per_minute: gauge
    read_latency_p99: histogram
    failures: counter

  quality:
    connascence_violations: gauge
    audit_pass_rate: gauge
```

### Rollback Procedure

```bash
# If issues detected:

# 1. Disable new skills
claude mcp remove gemini-research
claude mcp remove codex-audit

# 2. Restore previous agent-selector
git checkout HEAD~1 -- skills/orchestration/agent-selector/SKILL.md

# 3. Disable hooks
mv .claude/hooks/multi-model-router.sh .claude/hooks/multi-model-router.sh.disabled

# 4. Clear problematic memory
memory_delete "multi-model/*" --namespace coordination

# 5. Monitor for stability
bash .claude/hooks/enforcement/analyze-compliance.sh
```

---

## APPENDIX: File Locations

| Component | Path |
|-----------|------|
| CLI Scripts | `scripts/multi-model/` |
| Skills | `skills/multi-model/` |
| Memory Schema | `docs/MEMORY-NAMESPACE-SCHEMA.yaml` |
| This Plan | `docs/UNIFIED-MULTI-MODEL-CONTEXT-OPTIMIZATION-PLAN.md` |
| MCP Analysis | `docs/MCP-CONTEXT-OPTIMIZATION-ANALYSIS.md` |
| Integration Arch | `docs/MULTI-MODEL-INTEGRATION-ARCHITECTURE.md` |
