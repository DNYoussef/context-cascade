---
name: skill-forge-sop
description: Agent-orchestrated 7-phase SOP for building production-grade Claude Code skills
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: foundry/skill-forge
x-vcl-compliance: v3.1.1
---

### L1 Improvement
- Reframed the enhanced Skill Forge SOP into an English-first structure with explicit triggers, outputs, and confidence ceilings.
- Preserved all original agent prompts, task breakdowns, and examples in the appendix for fidelity.
- Clarified memory namespaces, deliverables, and sequencing to enable execution without VCL knowledge.

## STANDARD OPERATING PROCEDURE

### Purpose
Run the enhanced 7-phase Skill Forge workflow with coordinated agents to turn intent into production-ready skills.

### Trigger Conditions
- Engage when a new skill requires full agent-orchestrated execution (researcher → reviewer flow).
- Defer to `SKILL.md` for legacy baseline or `quick-reference.md` for short checklists.

### Execution Phases (summary)
1. **Intent Archaeology (researcher, 10–15 min)**
   - Extract true intent, hidden assumptions, and success metrics.
   - Output: `phase1-intent-analysis.json`.
2. **Use Case Crystallization (analyst, 10–15 min)**
   - Produce 3–5 concrete examples with I/O schemas and coverage matrix.
   - Output: `phase2-use-cases.json`.
3. **Structural Architecture (architect, 15–20 min)**
   - Define progressive disclosure, resources, and SKILL.md outline.
   - Output: `phase3-architecture.json`.
4. **Content Implementation (coder, 20–30 min)**
   - Write SKILL.md in imperative voice with workflows and examples.
   - Output: completed `SKILL.md`.
5. **Resource Development (coder, 20–40 min)**
   - Build scripts, references, assets, and GraphViz diagrams.
   - Outputs: `scripts/`, `references/`, `assets/`, `{skill}-process.dot`.
6. **Validation Testing (tester, 15–25 min)**
   - Validate structure, functionality, clarity, and anti-patterns; generate report.
   - Output: `validation-report.json`.
7. **Quality Review (reviewer, 10–15 min)**
   - Assess readiness and decide approve/warn/revise.
   - Output: `final-review.json`.

### Coordination & Memory
- Namespace: `skill-forge/[phase]/[output-type]` (or `coordination/skill-forge/phase{N}/*` in quick ref).
- Use hooks to manage sessions and persist context between agents.

### Output Format
- Phase status with agent, duration, deliverable, and risks.
- Memory keys used, hooks invoked, and pending tasks.
- Confidence statement using ceiling syntax: `Confidence: X.XX (ceiling: TYPE Y.YY)` (ceilings: inference/report 0.70; research 0.85; observation/definition 0.95).

### Validation Checklist
- [ ] All seven phases executed or queued with deliverables.
- [ ] Memory namespaces populated; handoffs documented.
- [ ] SKILL.md plus supporting resources produced.
- [ ] Validation report completed; decision recorded.
- [ ] Confidence statement present with explicit ceiling.

Confidence: 0.70 (ceiling: inference 0.70) - Enhanced SOP rewritten to English-first format while preserving full agent prompts and timings in the appendix.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

- Full legacy content (including all agent prompts and detailed steps) is preserved at `resources/legacy/skill-enhanced-legacy.md`. Reference it whenever VCL/VERIX markers or verbatim text are required.
- Keep user-facing outputs in pure English; use the legacy file only for internal compliance checks.
