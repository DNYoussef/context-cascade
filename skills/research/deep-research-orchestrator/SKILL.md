/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for research workflows [ground:given] [conf:0.95] [state:confirmed]
category: research
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic research processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "research",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["SKILL", "research", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## SKILL-SPECIFIC GUIDANCE

### When to Use This Skill
- Complete research lifecycle from literature review to production (Pipelines A-I)
- Multi-month academic projects requiring 3 quality gates
- NeurIPS/ICML/CVPR submissions with reproducibility requirements
- Research requiring systematic methodology (PRISMA, ACM badging)
- Coordinating 9 pipelines with 15+ specialized agents

### When NOT to Use This Skill
- Quick investigations (<1 week, use researcher skill)
- Single-pipeline workflows (use specific skills)
- Industry projects without academic rigor
- Prototyping without publication goals

### Success Criteria
- [assert|neutral] All 3 Quality Gates passed (Foundations, Development, Production) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Minimum 50 papers reviewed (Pipeline A) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Baseline replicated within +/- 1% (Pipeline D) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Novel method validated (p < 0.05, d >= 0.5) [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Holistic evaluation across 6+ dimensions [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Reproducibility package tested in fresh environments [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Ethics review completed (data bias audit, fairness metrics) [ground:acceptance-criteria] [conf:0.90] [state:provisional]

### Edge Cases & Limitations
- Gate 1 failure: incomplete literature review, missing SOTA benchmarks
- Gate 2 failure: insufficient ablations, statistical power too low
- Gate 3 failure: production infrastructure not validated, monitoring gaps
- Multi-modal data: expand holistic evaluation to modality-specific metrics
- Limited compute: prioritize smaller ablation sets, document constraints

### Critical Guardrails
- NEVER skip Quality Gates (use gate-validation for rigorous checks)
- ALWAYS document full pipeline execution (A through I, no shortcuts)
- NEVER claim production readiness without Gate 3 validation
- ALWAYS coordinate ethics review (ethics-agent) before Gate 1
- NEVER bypass reproducibility requirements (archivist agent mandatory)

### Evidence-Based Validation
- Validate Gate 1: verify 50+ papers, SOTA benchmarks, research gaps
- Validate Gate 2: confirm 5+ ablations, p < 0.05, effect size d >= 0.5
- Validate Gate 3: test production deployment, monitoring, rollback strategies
- Cross-validate pipelines: ensure Pipeline D baseline feeds into Pipeline E
- Verify agent coordination: check memory-mcp state, confirm handoffs logged

---
name: deep-research-orchestrator
description: Meta-orchestrator for complete Deep Research SOP lifecycle managing 3
  phases, 9 pipelines (A-I), and 3 quality gates. Use when starting new research projects,
  conducting systematic ML research, or ensuring rigorous scientific methodology from
  literature review through production deployment. Coordinates all SOP skills and
  agents for end-to-end research execution.
version: 1.1.0
category: research
tags:
- research
- analysis
- planning
author: ruv
cognitive_frame:
  primary: evidential
  secondary: morphological
  rationale: "Research requires rigorous source tracking and concept decomposition"
---

# Deep Research Orchestrator

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Master orchestration skill for the complete Deep Research Standard Operating Procedure (SOP), managing the entire research lifecycle from ideation through production deployment with rigorous quality gates.

## Kanitsal Cerceve Aktivasyonu (Evidential Frame)

Bu arastirma gorevi icin her iddia kaynaklandirilmalidir:

**Kaynak Turleri:**
- **DOGRUDAN (-DI)**: Birincil kaynak, dogrudan inceleme
- **CIKARIM (-mIs)**: Ikincil analiz, cikarim yapildi
- **BILDIRILEN (-mIs)**: Ucuncu taraf bildirimi

**English Application:**
- **[

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/research/SKILL/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "SKILL-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
