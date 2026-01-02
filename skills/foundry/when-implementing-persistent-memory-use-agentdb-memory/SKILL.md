---
name: agentdb-memory
description: Apply AgentDB persistent memory patterns for durable context storage, retrieval, and lifecycle management.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: agentdb
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

### L1 Improvement
- Rewrote the memory guidance into Skill Forge required sections with explicit contracts and validation steps.
- Added prompt-architect constraint capture, confidence ceilings, and safety controls for data retention.

## STANDARD OPERATING PROCEDURE

### Purpose
Design persistent memory strategies with AgentDB, covering namespaces, retention policies, retrieval contracts, and safety/privacy requirements.

### Trigger Conditions
- Positive: implementing long-term memory, audit trails, or context recall for agents/workflows using AgentDB.
- Negative/reroute: ephemeral caches or non-AgentDB storage solutions; vector search tuning (agentdb-vector-search).

### Guardrails
- Define retention, encryption, and access controls before enabling writes.
- Separate memory namespaces per project/session; tag writes for traceability.
- Include data minimization and deletion workflows; avoid storing secrets in plain text.
- Maintain English outputs with explicit confidence ceilings.

### Execution Phases
1. **Planning**: Capture use case, sensitivity, retention needs, and constraints; classify HARD/SOFT/INFERRED.
2. **Schema & Namespaces**: Define record schema, namespace patterns, tags (WHO/WHY/WHEN/PROJECT), and indexing needs.
3. **Write/Read Paths**: Specify APIs for writes, retrieval, and pruning; include rate/size limits and error handling.
4. **Validation**: Test CRUD operations, access controls, and retention enforcement; log results with ceilings.
5. **Operations**: Document monitoring, backup/restore, and incident response for memory misuse.

### Pattern Recognition
- Conversation memory → chunk + summarize with time decay.
- Audit/history → append-only with strong access control and integrity checks.
- Feature store → schema evolution and validation pipelines.

### Advanced Techniques
- Use tiered storage (hot/warm/cold) with TTL policies.
- Apply summarization to reduce footprint while preserving evidence.
- Add anomaly detection on access patterns for security.

### Common Anti-Patterns
- Storing sensitive data without encryption or retention limits.
- Mixing unrelated contexts in one namespace causing leakage.
- No deletion/rotation plan.

### Practical Guidelines
- Standardize tags: WHO=agentdb-memory-{session}, WHY=skill-execution, WHEN=timestamp, PROJECT=name.
- Document maximum record sizes and throttling behavior.
- Provide fallback behavior when reads miss (e.g., regenerate or request input).

### Cross-Skill Coordination
- Upstream: prompt-architect for clarity on memory scope; skill-builder for scaffolding.
- Parallel: agentdb-vector-search for retrieval, agentdb-optimization for performance.
- Downstream: agent-creator/agent-selector using memory configs; recursive-improvement to refine retention.

### MCP Requirements
- Requires AgentDB memory MCP with proper credentials and permissions; tag writes as above for auditability.

### Input/Output Contracts
```yaml
inputs:
  use_case: string  # required
  sensitivity: string  # required data classification
  retention: string  # required policy
  constraints: list[string]  # optional
outputs:
  memory_plan: file  # schema, namespace, and policy definitions
  validation_report: file  # access/retention tests
  runbook: summary  # monitoring, backup, and deletion steps
```

### Recursive Improvement
- Feed incidents or retrieval misses into recursive-improvement to adjust schemas, retention, or access controls.

### Examples
- Configure long-term memory for customer support agents with redaction and TTL policies.
- Set up audit-friendly memory for deployment history with access controls and backups.

### Troubleshooting
- Retrieval misses → verify namespaces/tags, reindex, or adjust queries.
- Storage bloat → enable TTL, summarize, or archive cold data.
- Access issues → audit permissions and rotate credentials.

### Completion Verification
- [ ] Schema, namespaces, and tagging defined.
- [ ] Retention, encryption, and deletion policies documented and tested.
- [ ] Confidence ceilings stated for reliability/safety claims.
- [ ] Runbook provided for monitoring and incidents.

Confidence: 0.70 (ceiling: inference 0.70) - AgentDB memory SOP rewritten with Skill Forge cadence and prompt-architect ceilings.
