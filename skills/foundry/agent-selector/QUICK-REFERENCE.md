# Agent Selector - Quick Reference v2.1.0

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Intelligent agent selection from 203-agent registry using semantic matching and capability analysis.

## Agent Registry Overview

| Category | Count | Description |
|----------|-------|-------------|
| delivery | 20+ | Implementation & deployment |
| foundry | 15+ | Core creation & building |
| operations | 20+ | System & workflow ops |
| orchestration | 15+ | Coordination & routing |
| platforms | 15+ | Platform-specific |
| quality | 25+ | Testing & validation |
| research | 20+ | Analysis & investigation |
| security | 15+ | Security & compliance |
| specialists | 30+ | Domain experts |
| tooling | 25+ | Tool & utility agents |

**Total: 211 agents**

## Selection Process

```
1. PARSE    -> Extract task intent & keywords
2. ANALYZE  -> Determine complexity, domain, tools needed
3. QUERY    -> Build semantic search vector
4. MATCH    -> Find agents by capability
5. RANK     -> Score candidates (0-1)
6. SELECT   -> Return best fit(s)
```

## Quick Commands

```bash
# Single agent selection
Select agent for: [task description]

# Multi-agent ensemble
Select agents (ensemble) for: [complex task]

# Category-constrained
Select [category] agent for: [task]
```

## Scoring Weights

| Factor | Weight | Description |
|--------|--------|-------------|
| Semantic Match | 0.4 | Description alignment |
| Capability Match | 0.3 | Tool/skill overlap |
| Domain Match | 0.2 | Category fit |
| History Score | 0.1 | Past performance |

## Common Selections

| Task Type | Recommended Agent(s) |
|-----------|---------------------|
| Code implementation | coder, implementer |
| Code review | reviewer, code-reviewer |
| Testing | tester, qa-engineer |
| Architecture | system-architect, designer |
| Security audit | security-auditor, penetration-tester |
| Documentation | technical-writer, documenter |
| Bug fix | debugger, bug-hunter |
| Performance | performance-engineer, optimizer |

## Ensemble Patterns

**Code Quality Triad:**
- coder + tester + reviewer

**Full Stack:**
- frontend-dev + backend-dev + devops-engineer

**Security Review:**
- security-auditor + penetration-tester + compliance-checker

## Output Format

```yaml
selection:
  primary_agent: agent-name
  confidence: 0.85
  reasoning: "Selected because..."
  alternatives:
    - agent: alt-1
      confidence: 0.72
    - agent: alt-2
      confidence: 0.68
```

## Related Skills

- **expertise-manager** - Domain expertise loading
- **parallel-swarm-implementation** - Uses selected agents
- **research-driven-planning** - Informs selection criteria


---
*Promise: `<promise>QUICK_REFERENCE_VERIX_COMPLIANT</promise>`*
