/*============================================================================*/
/* WHEN-DEVELOPING-ML-MODELS-USE-ML-EXPERT SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: when-developing-ml-models-use-ml-expert
version: 1.0.0
description: |
  [assert|neutral] Specialized ML model development, training, and deployment workflow [ground:given] [conf:0.95] [state:confirmed]
category: machine-learning
tags:
- ml
- training
- deployment
- model-development
- neural-networks
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute when-developing-ml-models-use-ml-expert workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic machine-learning processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "when-developing-ml-models-use-ml-expert",
  category: "machine-learning",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["when-developing-ml-models-use-ml-expert", "machine-learning", "workflow"],
  context: "user needs when-developing-ml-models-use-ml-expert capability"
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


# ML Expert - Machine Learning Model Development

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Overview

Specialized workflow for ML model development, training, and deployment. Supports various architectures (CNNs, RNNs, Transformers) with distributed training capabilities.

## When to Use

- Developing new ML models
- Training neural networks
- Model optimization
- Production deployment
- Transfer learning
- Fine-tuning existing models

## Phase 1: Data Preparation (10 min)

### Objective
Clean, preprocess, and prepare training data

### Agent: ML-Developer

**Step 1.1: Load and Analyze Data**
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv('dataset.csv')

# Analyze
analysis = {
    'shape': data.shape,
    'columns': data.columns.tolist(),
    'dtypes': data.dtypes.to_dict(),
    'missing': data.isnull().sum().to_dict(),
    'stats': data.describe().to_dict()
}

# Store analysis
await memory.store('ml-expert/data-analysis', analysis)
```

**Step 1.2: Data Cleaning**
```python
# Handle missing values
data = data.fillna(data.mean())

# Remove duplicates
data = data.drop_duplicates()

# Handle outliers
from scipy import stats
z_scores = np.abs(stats.zscore(data.select_dtypes(include=

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
  pattern: "skills/machine-learning/when-developing-ml-models-use-ml-expert/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "when-developing-ml-models-use-ml-expert-{session_id}",
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

[commit|confident] <promise>WHEN_DEVELOPING_ML_MODELS_USE_ML_EXPERT_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
