---
name: llm-council
description: Facilitate council-style deliberation among specialized models with structured prompts, evidence gates, and explicit confidence ceilings.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: orchestration
x-vcl-compliance: v3.2.0
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

## STANDARD OPERATING PROCEDURE

### Purpose
Run council deliberations that collect diverse model opinions, enforce evidence-backed synthesis, and prevent overconfident consensus.

### Trigger Conditions
- **Positive:** multi-model debate, comparative reasoning, adjudication of conflicting outputs, need for weighted synthesis with evidence.
- **Negative:** single-model answers, pure prompt polishing (route to prompt-architect), or skill creation (route to skill-forge).

### Guardrails
- **Skill-Forge structure-first:** maintain `SKILL.md`, `examples/`, `tests/`; add `resources/` and `references/` or log remediation tasks.
- **Prompt-Architect hygiene:** define intent and constraints per council question; capture HARD/SOFT/INFERRED assumptions; output pure English with explicit ceilings.
- **Council safety:** assign roles (proposer, challenger, judge), enforce registry agents, timebox rounds, and ensure hook latency budgets.
- **Adversarial validation:** require dissenting review, cross-check citations, and COV on synthesis steps; capture evidence.
- **MCP tagging:** store council transcripts with WHO=`llm-council-{session}` and WHY=`skill-execution`.

### Execution Playbook
1. **Intent & scope:** define the question, success metric, and constraints; confirm inferred items.
2. **Panel setup:** select specialists, assign roles, and set scoring criteria; configure timeboxes.
3. **Deliberation rounds:** gather proposals, run adversarial critiques, and request evidence per claim.
4. **Synthesis:** weigh arguments, resolve conflicts, and produce a grounded recommendation with alternatives.
5. **Validation loop:** check evidence integrity, run COV on synthesis, and record telemetry.
6. **Delivery:** provide recommendation, rationale, dissent, risks, and confidence ceiling.

### Output Format
- Question, constraints, and panel composition.
- Round summaries (proposals, critiques, evidence).
- Synthesis with chosen path, alternatives, and risk notes.
- **Confidence:** `X.XX (ceiling: TYPE Y.YY) - rationale`.

### Validation Checklist
- Structure-first assets present or planned; examples/tests updated or ticketed.
- Roles/timeboxes enforced; evidence cited; registry-only agents used; hooks within budget.
- Adversarial and COV results captured with MCP tags; confidence ceiling declared; English-only output.

### Completion Definition
Council run is complete when a recommendation (or documented stalemate) is delivered with evidence, dissent captured, risks owned, and MCP log persisted.

Confidence: 0.70 (ceiling: inference 0.70) - Council orchestration rewritten with skill-forge scaffolding and prompt-architect constraint and confidence discipline.
