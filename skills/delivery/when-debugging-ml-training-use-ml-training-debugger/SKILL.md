/*============================================================================*/
/* WHEN-DEBUGGING-ML-TRAINING-USE-ML-TRAINING-DEBUGGER SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-debugging-ml-training-use-ml-training-debugger
version: 1.0.0
description: |
  [assert|neutral] Debug ML training issues and optimize performance including loss divergence, overfitting, and slow convergence [ground:given] [conf:0.95] [state:confirmed]
category: machine-learning
tags:
- debugging
- ml
- training
- optimization
- troubleshooting
author: ruv
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute when-debugging-ml-training-use-ml-training-debugger workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic machine-learning processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-debugging-ml-training-use-ml-training-debugger",
  category: "machine-learning",
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
  keywords: ["when-debugging-ml-training-use-ml-training-debugger", "machine-learning", "workflow"],
  context: "user needs when-debugging-ml-training-use-ml-training-debugger capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

## When NOT to Use This Skill

- Simple data preprocessing without model training
- Statistical analysis that does not require ML models
- Rule-based systems without learning components
- Operations that do not involve model training or inference

## Success Criteria
- [assert|neutral] Model training convergence: Loss decreasing consistently [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Validation accuracy: Meeting or exceeding baseline targets [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Training time: Within expected bounds for dataset size [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] GPU utilization: >80% during training [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Model export success: 100% successful saves [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Inference latency: <100ms for real-time applications [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Edge Cases & Error Handling

- **GPU Memory Overflow**: Reduce batch size, use gradient accumulation, or mixed precision
- **Divergent Training**: Implement learning rate scheduling, gradient clipping
- **Data Pipeline Failures**: Validate data integrity, handle missing/corrupted files
- **Version Mismatches**: Lock dependency versions, use containerization
- **Checkpoint Corruption**: Save multiple checkpoints, validate before loading
- **Distributed Training Failures**: Handle node failures, implement fault tolerance

## Guardrails & Safety
- [assert|emphatic] NEVER: train on unvalidated or uncleaned data [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: validate model outputs before deployment [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: implement reproducibility (random seeds, version pinning) [ground:policy] [conf:0.98] [state:confirmed]
- [assert|emphatic] NEVER: expose training data in model artifacts or logs [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: monitor for bias and fairness issues [ground:policy] [conf:0.98] [state:confirmed]
- [assert|neutral] ALWAYS: implement model versioning and rollback capabilities [ground:policy] [conf:0.98] [state:confirmed]

## Evidence-Based Validation

- Verify hardware availability: Check GPU/TPU status before training
- Validate data quality: Run data integrity checks and statistics
- Monitor training: Track loss curves, gradients, and metrics
- Test model performance: Evaluate on held-out test set
- Benchmark inference: Measure latency and throughput under load


# ML Training Debugger - Diagnose and Fix Training Issues

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Systematic debugging workflow for ML training issues including loss divergence, overfitting, slow convergence, gradient problems, and performance optimization.

## When to Use

- Training loss becomes NaN or infinite
- Severe overfitting (train >> val performance)
- Training not converging
- Gradient vanishing/exploding
- Poor validation accuracy
- Training too slow

## Phase 1: Diagnose Issue (8 min)

### Objective
Identify the specific training problem

### Agent: ML-Developer

**Step 1.1: Analyze Training Curves**
```python
import json
import numpy as np

# Load training history
with open('training_history.json', 'r') as f:
    history = json.load(f)

# Diagnose issues
diagnosis = {
    'loss_divergence': check_loss_divergence(history['loss']),
    'overfitting': check_overfitting(history['loss'], history['val_loss']),
    'slow_convergence': check_convergence_rate(history['loss']),
    'gradient_issues': check_gradient_health(history),
    'nan_values': any(np.isnan(history['loss']))
}

def check_loss_divergence(losses):
    # Loss increasing over time
    if len(losses) > 10:
        recent_trend = np.mean(losses[-5:]) > np.mean(losses[-10:-5])
      

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
  pattern: "skills/machine-learning/when-debugging-ml-training-use-ml-training-debugger/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-debugging-ml-training-use-ml-training-debugger-{session_id}",
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

[commit|confident] <promise>WHEN_DEBUGGING_ML_TRAINING_USE_ML_TRAINING_DEBUGGER_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
