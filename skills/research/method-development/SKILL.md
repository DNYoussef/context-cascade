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

name: method-development
description: Develop novel machine learning methods with rigorous ablation studies
  for Deep Research SOP Pipeline D. Use after baseline replication passes Quality
  Gate 1, when creating new algorithms, proposing modifications to existing methods,
  or conducting systematic experimental validation. Includes architectural innovation,
  hyperparameter optimization, and component-wise ablation analysis leading to Quality
  Gate 2.
version: 1.0.0
category: research
tags:
- research
- analysis
- planning
author: ruv
---

# Method Development

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Systematically develop and validate novel machine learning methods through controlled experimentation, ablation studies, and architectural innovation following Deep Research SOP Pipeline D.

## Overview

**Purpose**: Develop novel ML methods with rigorous experimental validation after baseline replication

**When to Use**:
- Quality Gate 1 (baseline replication) has APPROVED status
- Proposing architectural modifications to baseline methods
- Developing new training algorithms or optimization strategies
- Creating novel model components or attention mechanisms
- Systematic hyperparameter optimization required
- Ablation studies needed to validate design choices

**Quality Gate**: Leads to Quality Gate 2 (Model & Evaluation Validation)

**Prerequisites**:
- Baseline replication completed with ±1% tolerance (Quality Gate 1 passed)
- Baseline reproducibility package available
- Statistical analysis framework in place
- Docker environment configured
- GPU resources allocated (4-8 GPUs recommended)

**Outputs**:
- Novel method implementation with complete codebase
- Ablation study results (minimum 5 components tested)
- Performance comparison vs. baseline (statistical significance)
- Architectural diagrams and design documentation
- Hyperparameter sensitivity analysis
- Quality Gate 2 checklist (model validation requirements)

**Time Estimate**: 3-7 days (varies by complexity)
- Phase 1 (Architecture Design): 4-8 hours
- Phase 2 (Prototype Implementation): 1-2 days
- Phase 3 (Ablation Studies): 2-3 days
- Phase 4 (Optimization): 1-2 days
- Phase 5 (Comparative Evaluation): 4-8 hours
- Phase 6 (Documentation): 2-4 hours
- Phase 7 (Gate 2 Validation): 2-4 hours

**Agents Used**: system-architect, coder, tester, ethics-agent, reviewer, archivist, evaluator

---

## Quick Start

### 1. Prerequisites Check
```bash
# Verify baseline replication passed Gate 1
npx claude-flow@alpha memory retrieve --key "sop/gate-1/status"

# Load baseline reproducibility package
cd baseline-replication-package/
docker build -t baseline:latest .

# Verify baseline results
python scripts/verify_baseline_results.py --tolerance 0.01
```

### 2. Initialize Method Development
```bash
# Run architecture design workflow
npx claude-flow@alpha hooks pre-task \
  --description "Method development: Novel attention mechanism"

# Create method development workspace
mkdir -p novel-method/{src,experiments,ablations,docs}
cd novel-method/
```

### 3. Design Novel Architecture
```bash
# Invoke system-architect agent
# Document architectural decisions
# Create comparison diagrams (baseline vs. novel)
```

### 4. Run Ablation Studies
```bash
# Minimum 5 component ablations required
python scripts/run_ablations.py \
  --components "attention,normalization,residual,activation,pooling" \
  --baseline baseline:latest \
  --runs 3 \
  --seeds 42,123,456
```

### 5. Statistical Validation
```bash
# Compare novel method vs. baseline
python scripts/statistical_comparison.py \
  --method novel-method \
  --baseline baseline \
  --test paired-ttest \
  --significance 0.05
```

### 6. Quality Gate 2 Validation
```bash
# Validate Gate 2 requirements
npx claude-flow@alpha sparc run evaluator \
  "/validate-gate-2 --pipeline E --method novel-method"
```

---

## Detailed Instructions

### Phase 1: Architecture Design (4-8 hours)

**Agent**: system-

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
