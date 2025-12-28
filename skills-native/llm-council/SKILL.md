---
name: llm-council
description: Multi-model consensus using Karpathy LLM Council pattern for critical decisions
allowed-tools: Bash, Read, Write, TodoWrite
---

# LLM Council Skill

## Purpose

Run 3-stage multi-model consensus for critical decisions where:
- Single-model hallucination risk is unacceptable
- Multiple perspectives improve decision quality
- High-stakes choices need validation

## Architecture (Karpathy Pattern)

```
STAGE 1: COLLECT
  +---> Claude ---> Response A
  |
Query --+---> Gemini ---> Response B
  |
  +---> Codex ----> Response C

STAGE 2: RANK
  Each model reviews others (anonymized)
  Produces rankings with rationale

STAGE 3: SYNTHESIZE
  Chairman aggregates rankings
  Produces final answer with consensus score
```

## When to Use

### Perfect For:
- Architecture decisions
- Technology selection
- Critical bug triage
- Security assessment
- High-risk deployments
- Contentious design choices

### Don't Use When:
- Simple, low-risk decisions
- Time-critical responses
- Single correct answer exists
- Cost is a concern (3x API usage)

## Usage

### Basic Council
```bash
/llm-council "Should we use microservices or monolith for this system?"
```

### With Threshold
```bash
/llm-council "Which auth approach is best?" --threshold 0.75
```

### With Chairman Override
```bash
/llm-council "Architecture decision" --chairman gemini
```

## Command Pattern

```bash
bash scripts/multi-model/llm-council.sh "<query>" "<threshold>" "<chairman>"
```

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| threshold | 0.67 | Minimum consensus score |
| chairman | claude | Model that synthesizes final answer |
| models | [claude, gemini, codex] | Participating models |

## Consensus Scoring

- **>0.80**: Strong consensus - proceed with confidence
- **0.67-0.80**: Moderate consensus - consider minority views
- **<0.67**: Weak consensus - escalate to human review

## Memory Integration

Results stored to Memory-MCP:
- Key: `multi-model/council/decisions/{query_id}`
- Tags: WHO=llm-council, WHY=consensus-decision

## Output Format

```json
{
  "query": "Original question",
  "final_answer": {
    "synthesis": "Combined answer...",
    "chairman": "claude"
  },
  "consensus_score": 0.85,
  "responses": {
    "claude": "...",
    "gemini": "...",
    "codex": "..."
  },
  "rankings": [
    {"model": "A", "rank": 1, "rationale": "..."}
  ]
}
```

## Failure Modes

### Deadlock (No Consensus)
- All models disagree
- Consensus < threshold
- Action: Store for human review

### Model Unavailable
- One model times out
- Action: Continue with 2 models (2/3 quorum)

### Chairman Failure
- Synthesis fails
- Action: Fallback to highest-ranked response

## Integration Examples

### Architecture Decision
```javascript
const decision = await runCouncil(
  "Microservices vs Monolith for our scale?",
  { threshold: 0.75 }
);

if (decision.consensus_score >= 0.75) {
  proceed(decision.final_answer);
} else {
  escalateToHuman(decision);
}
```

### Security Assessment
```javascript
const assessment = await runCouncil(
  "Is this authentication approach secure?",
  { threshold: 0.80 }
);
// Higher threshold for security decisions
```

## Sources

- [LLM Council by Andrej Karpathy](https://github.com/karpathy/llm-council)
- [VentureBeat Analysis](https://venturebeat.com/ai/a-weekend-vibe-code-hack-by-andrej-karpathy-quietly-sketches-the-missing)
