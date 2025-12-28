---
name: holistic-evaluation
description: Comprehensive multi-dimensional model evaluation across accuracy, fairness, robustness, efficiency, interpretability, and safety for Deep Research SOP Pipeline E. Use after method development when Quality Gate 2 validation is required, ensuring models meet production-ready standards across 6+ evaluation dimensions before deployment.
---

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


# Holistic Evaluation

Systematically evaluate machine learning models across 6+ critical dimensions following Deep Research SOP Pipeline E, ensuring comprehensive assessment beyond simple accuracy metrics.

## Overview

**Purpose**: Comprehensive model evaluation across multiple dimensions for production readiness

**When to Use**:
- Method development complete (novel method implemented)
- Quality Gate 2 validation required
- Before model deployment to production
- Regulatory compliance evaluation needed (EU AI Act, FDA)
- Fairness, safety, and robustness assessment required
- Model comparison across multiple dimensions

**Quality Gate**: Required for Quality Gate 2 APPROVED status

**Prerequisites**:
- Trained model checkpoint available
- Method development completed
- Test datasets prepared (standard + adversarial + fairness)
- Evaluation framework installed (sklearn, fairness-indicators, etc.)
- Ethics review initiated

**Outputs**:
- Holistic evaluation report across 6+ dimensions
- Fairness metrics (demographic parity, equalized odds, etc.)
- Robustness analysis (adversarial, distribution shift)
- Efficiency metrics (latency, throughput, memory, energy)
- Interpretability analysis (SHAP, attention visualizations)
- Safety evaluation (harmful outputs, bias, privacy)
- Quality Gate 2 validation checklist

**Time Estimate**: 2-5 days
- Phase 1 (Accuracy Evaluation): 4-8 hours
- Phase 2 (Fairness Evaluation): 1 day
- Phase 3 (Robustness Testing): 1-2 days
- Phase 4 (Efficiency Profiling): 4-8 hours
- Phase 5 (Interpretability Analysis): 4-8 hours
- Phase 6 (Safety Evaluation): 1 day
- Phase 7 (Synthesis & Gate 2): 2-4 hours

**Agents Used**: tester, ethics-agent, archivist, evaluator

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Detailed Instructions

### Phase 1: Accuracy Evaluation (4-8 hours)

**Agent**: tester

**Objectives**:
1. Evaluate standard metrics across test sets
2. Measure performance on challenging subsets
3. Compare with baselines and SOTA methods
4. Statistical significance testing

**Steps**:

#### 1.1 Standard Metrics Evaluation
```bash
# Evaluate on standard test set
python scripts/evaluate_accuracy.py \
  --model experiments/results/best_checkpoint.pth \
  --dataset test \
  --metrics "accuracy,precision,recall,f1,auc" \
  --output experiments/results/holistic_evaluation/accuracy/
```

**Expected Metrics** (classification example):
- Accuracy: Overall correctness
- Precision: Positive prediction quality
- Recall: Positive class coverage
- F1 Score: Harmonic mean of precision/recall
- AUC-ROC: Classifier discrimination ability

#### 1.2 Per-Class Performance
```bash
# Analyze per-class metrics
python scripts/per_class_analysis.py \
  --model experiments/results/best_checkpoint.pth \
  --dataset test \
  --output experiments/results/holistic_evaluation/accuracy/per_class.json
```

**Identify**:
- Worst-performing classes (bottom 10%)
- Confusion matrix patterns
- Class imbalance effects

#### 1.3 Error Analysis
```bash
# Systematic error analysis
python scripts/error_analysis.py \
  --predictions experiments/results/holistic_evaluation/accuracy/predictions.json \
  --dataset test \
  --error-types "false_positives,false_negatives,high_confidence_errors" \
  --output experiments/results/holistic_evaluation/accuracy/error_analysis/
```

**Deliverable**: Accuracy evaluation report with error analysis

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


### Phase 3: Robustness Testing (1-2 days)

**Agent**: tester

**Objectives**:
1. Adversarial robustness evaluation
2. Out-of-distribution (OOD) detection
3. Distribution shift resilience
4. Uncertainty calibration

**Steps**:

#### 3.1 Adversarial Robustness (White-Box)
```python
# FGSM, PGD, C&W attacks
from foolbox import PyTorchModel
from foolbox.attacks import FGSM, PGD, CarliniWagnerL2Attack

fmodel = PyTorchModel(model, bounds=(0, 1))

# Fast Gradient Sign Method (FGSM)
attack = FGSM()
adversarial_examples = attack(fmodel, images, labels, epsilons=[0.01, 0.03, 0.05])

# Projected Gradient Descent (PGD)
attack = PGD()
adversarial_examples = attack(fmodel, images, labels, epsilons=[0.01, 0.03, 0.05])

# Report robust accuracy
python scripts/adversarial_eval.py \
  --model experiments/results/best_checkpoint.pth \
  --attacks "fgsm,pgd,cw" \
  --epsilons "0.01,0.03,0.05,0.1" \
  --output experiments/results/holistic_evaluation/robustness/adversarial/
```

**Expected Results**:
```
Adversarial Robustness Results
==============================
Clean Accuracy: 87.5%

FGSM (ε=0.03): 62.3% (-25.2%)
PGD (ε=0.03):  45.8% (-41.7%)
C&W (ε=0.03):  38.1% (-49.4%)

Conclusion: Model vulnerable to white-box adversarial attacks.
Recommendation: Consider adversarial training.
```

#### 3.2 Out-of-Distribution (OOD) Detection
```bash
# Test on OOD datasets (e.g., CIFAR-10 trained on ImageNet tested)
python scripts/ood_detection.py \
  --model experiments/results/best_checkpoint.pth \
  --in-distribution ImageNet \
  --out-distributions "Places365,iNaturalist,Textures" \
  --metrics "auroc,fpr_at_tpr95" \
  --output experiments/results/holistic_evaluation/robustness/ood/
```

**Metrics**:
- AUROC: Area under ROC curve (higher = better OOD detection)
- FPR@95%TPR: False positive rate when TPR=95% (lower = better)

#### 3.3 Distribution Shift Resilience
```bash
# Test on corrupted data (Gaussian noise, blur, weather effects)
python scripts/distribution_shift_eval.py \
  --model experiments/results/best_checkpoint.pth \
  --corruptions "gaussian_noise,shot_noise,motion_blur,fog,snow" \
  --severities 1,2,3,4,5 \
  --output experiments/results/holistic_evaluation/robustness/corruption/
```

#### 3.4 Uncertainty Calibration
```python
# Expected Calibration Error (ECE)
from netcal.metrics import ECE

ece = ECE(bins=15)
calibration_error = ece.measure(confidences, predictions, ground_truth)
print(f"Expected Calibration Error: {calibration_error:.4f}")
# Target: ECE < 0.05

# Reliability diagrams
python scripts/plot_calibration.py \
  --predictions experiments/results/holistic_evaluation/robustness/predictions.json \
  --output experiments/results/holistic_evaluation/robustness/calibration.pdf
```

**Deliverable**: Robustness evaluation report

--------|------------|----------|-----|-----|-----
1          |  12.3      | 0.5      | 12.2| 13.1| 13.8
8          |  45.2      | 1.2      | 45.0| 47.3| 48.9
16         |  78.5      | 2.1      | 78.1| 81.8| 84.2
32         |  142.7     | 3.5      | 142.0| 148.5| 152.3
```

#### 4.2 Throughput Measurement
```bash
# Queries per second (QPS)
python scripts/measure_throughput.py \
  --model experiments/results/best_checkpoint.pth \
  --duration 60 \
  --batch-size 32 \
  --device cuda \
  --output experiments/results/holistic_evaluation/efficiency/throughput.json
```

#### 4.3 Memory Profiling
```python
# GPU memory profiling
import torch

torch.cuda.reset_peak_memory_stats()
model.eval()
with torch.no_grad():
    output = model(input_batch)
peak_memory = torch.cuda.max_memory_allocated() / 1024**3  # GB
print(f"Peak GPU Memory: {peak_memory:.2f} GB")

# CPU memory profiling
from memory_profiler import profile
@profile
def inference():
    model(input_batch)
```

#### 4.4 Energy Consumption
```bash
# Estimate CO2 emissions and energy usage
pip install carbontracker

python scripts/energy_profiling.py \
  --model experiments/results/best_checkpoint.pth \
  --iterations 1000 \
  --output experiments/results/holistic_evaluation/efficiency/energy.json
```

#### 4.5 Model Compression Analysis
```bash
# Compare full vs. quantized vs. pruned models
python scripts/compression_comparison.py \
  --full-model experiments/results/best_checkpoint.pth \
  --quantized experiments/results/quantized_model.pth \
  --pruned experiments/results/pruned_model.pth \
  --metrics "size,latency,accuracy" \
  --output experiments/results/holistic_evaluation/efficiency/compression.json
```

**Deliverable**: Efficiency profiling report

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


### Phase 6: Safety Evaluation (1 day)

**Agent**: ethics-agent

**Objectives**:
1. Harmful output detection
2. Bias amplification analysis
3. Privacy leakage testing (membership inference)
4. Adversarial prompt testing (for LLMs)
5. Dual-use risk assessment

**Steps**:

#### 6.1 Harmful Output Detection
Coordinate with ethics-agent:
```bash
npx claude-flow@alpha sparc run ethics-agent \
  "/safety-eval --model experiments/results/best_checkpoint.pth --adversarial-testing"
```

**Test Categories**:
- Toxic language generation
- Hate speech propagation
- Misinformation amplification
- Harmful stereotypes

#### 6.2 Bias Amplification
```python
# Test if model amplifies biases present in training data
python scripts/bias_amplification_test.py \
  --model experiments/results/best_checkpoint.pth \
  --baseline-bias 0.15  # Bias level in training data \
  --output experiments/results/holistic_evaluation/safety/bias_amplification.json

# Expected: Model bias ≤ Baseline bias (no amplification)
```

#### 6.3 Privacy Leakage (Membership Inference)
```bash
# Membership inference attack
python scripts/membership_inference_attack.py \
  --model experiments/results/best_checkpoint.pth \
  --train-data train_dataset \
  --test-data test_dataset \
  --output experiments/results/holistic_evaluation/safety/privacy.json
```

**Metrics**:
- Attack Accuracy: Should be ≈50% (random guess) for privacy-preserving models
- Attack AUC: Should be ≈0.5

#### 6.4 Adversarial Prompt Testing (LLMs)
```bash
# Test with adversarial prompts (jailbreak attempts)
python scripts/adversarial_prompt_testing.py \
  --model experiments/results/best_checkpoint.pth \
  --prompt-categories "jailbreak,prompt_injection,context_manipulation" \
  --output experiments/results/holistic_evaluation/safety/adversarial_prompts.json
```

#### 6.5 Dual-Use Risk Assessment
Coordinate with ethics-agent:
```bash
npx claude-flow@alpha sparc run ethics-agent \
  "/assess-risks --component deployment --gate 3 --focus dual-use"
```

**Deliverable**: Safety evaluation report

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Integration with Deep Research SOP

### Pipeline Integration
- **Pipeline E (Holistic Evaluation)**: This skill implements comprehensive model evaluation
- **Prerequisite**: Method development complete
- **Next Step**: Archival and reproducibility packaging (Gate 3) if APPROVED

### Quality Gates
- **Gate 2**: This skill is REQUIRED for Gate 2 validation
- **Gate 3**: Holistic evaluation report included in reproducibility package

### Agent Coordination
```
Flow: tester → ethics-agent → archivist → evaluator

Phase 1-5: tester performs accuracy, robustness, efficiency, interpretability evaluations
Phase 2, 6: ethics-agent conducts fairness and safety evaluations
Phase 7: evaluator synthesizes results and validates Gate 2
archivist: Stores holistic evaluation report in reproducibility package
```

### Memory Coordination
```bash
# Store evaluation results for future reference
npx claude-flow@alpha memory store \
  --key "sop/holistic-evaluation/results" \
  --value "$(cat experiments/results/holistic_evaluation/summary.json)"

# Retrieve baseline evaluation for comparison
npx claude-flow@alpha memory retrieve \
  --key "sop/baseline-replication/evaluation"
```

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Related Skills and Commands

### Prerequisites
- `method-development` - Must complete before holistic evaluation

### Next Steps (after Gate 2 APPROVED)
- `reproducibility-audit` - Audit reproducibility before archival
- `deployment-readiness` - Prepare model for production deployment

### Related Commands
- `/validate-gate-2` - Gate 2 validation (evaluator agent)
- `/assess-risks` - Ethics and safety review (ethics-agent)
- `/safety-eval` - Safety-specific evaluation (ethics-agent)

### Parallel Skills
- Can run in parallel with literature synthesis (no dependencies)

## When to Use This Skill

Use this skill when:
- Code quality issues are detected (violations, smells, anti-patterns)
- Audit requirements mandate systematic review (compliance, release gates)
- Review needs arise (pre-merge, production hardening, refactoring preparation)
- Quality metrics indicate degradation (test coverage drop, complexity increase)
- Theater detection is needed (mock data, stubs, incomplete implementations)

## When NOT to Use This Skill

Do NOT use this skill for:
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Third-party libraries (focus on application code)

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

## Edge Cases and Limitations

Handle these edge cases carefully:
- **Empty Files**: May trigger false positives - verify intent (stub vs intentional)
- **Generated Code**: Skip or flag as low priority (auto-generated files)
- **Third-Party Libraries**: Exclude from analysis (vendor/, node_modules/)
- **Domain-Specific Patterns**: What looks like violation may be intentional (DSLs)
- **Legacy Code**: Balance ideal standards with pragmatic technical debt management

## Quality Analysis Guardrails

CRITICAL RULES - ALWAYS FOLLOW:
- **NEVER approve code without evidence**: Require actual execution, not assumptions
- **ALWAYS provide line numbers**: Every finding MUST include file:line reference
- **VALIDATE findings against multiple perspectives**: Cross-check with complementary tools
- **DISTINGUISH symptoms from root causes**: Report underlying issues, not just manifestations
- **AVOID false confidence**: Flag uncertain findings as "needs manual review"
- **PRESERVE context**: Show surrounding code (5 lines before/after minimum)
- **TRACK false positives**: Learn from mistakes to improve detection accuracy

## Evidence-Based Validation

Use multiple validation perspectives:
1. **Static Analysis**: Code structure, patterns, metrics (connascence, complexity)
2. **Dynamic Analysis**: Execution behavior, test results, runtime characteristics
3. **Historical Analysis**: Git history, past bug patterns, change frequency
4. **Peer Review**: Cross-validation with other quality skills (functionality-audit, theater-detection)
5. **Domain Expertise**: Leverage .claude/expertise/{domain}.yaml if available

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

## Integration with Quality Pipeline

This skill integrates with:
- **Pre-Phase**: Load domain expertise (.claude/expertise/{domain}.yaml)
- **Parallel Skills**: functionality-audit, theater-detection-audit, style-audit
- **Post-Phase**: Store findings in Memory MCP with WHO/WHEN/PROJECT/WHY tags
- **Feedback Loop**: Learnings feed dogfooding-system for continuous improvement


## Appendix

### Example Holistic Evaluation Summary

```
Model: Multi-Scale Attention ResNet-50
Date: 2025-11-01
Evaluator: tester + ethics-agent + evaluator

┌─────────────────────┬─────────────┬──────────┬──────────────────┐
│ Dimension           │ Metric      │ Value    │ Status           │
├─────────────────────┼─────────────┼──────────┼──────────────────┤
│ Accuracy            │ Test Acc    │ 87.5%    │ ✅ PASS (>85%)   │
│ Fairness            │ Dem. Parity │ 8.2%     │ ✅ PASS (<10%)   │
│ Robustness (Adv)    │ PGD ε=0.03  │ 45.8%    │ ⚠️  CONDITIONAL  │
│ Robustness (OOD)    │ AUROC       │ 0.82     │ ✅ PASS (>0.80)  │
│ Efficiency (Latency)│ Batch=32    │ 142.7ms  │ ✅ PASS (<200ms) │
│ Interpretability    │ SHAP        │ Complete │ ✅ PASS          │
│ Safety              │ Harmful Out │ 0.02%    │ ✅ PASS (<0.05%) │
└─────────────────────┴─────────────┴──────────┴──────────────────┘

Overall: CONDITIONAL APPROVAL
- Proceed to Gate 3 with adversarial robustness mitigation plan
- Deploy only in non-adversarial environments without mitigation
- Monitor fairness metrics in production
```
## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| **Accuracy-Only Validation** | Evaluating only test accuracy ignores fairness gaps, adversarial vulnerability, safety risks, and efficiency constraints. A 90% accurate model may have 30% accuracy on minority groups, collapse under small perturbations, or generate harmful outputs. Leads to production failures and reputational damage. | Evaluate all 6 dimensions (accuracy, fairness, robustness, efficiency, interpretability, safety) with quantitative thresholds. Require PASS status on ALL critical dimensions before Gate 2 approval. Document trade-offs explicitly in evaluation report. |
| **Subjective Gate Decisions** | Gate 2 decisions based on intuition ("model looks good") without statistical validation fail under academic peer review and regulatory audit. Cannot defend approval decisions when challenged. Leads to reproducibility failures and rejected publications. | Implement rigorous statistical validation: multiple comparison correction (Bonferroni), effect size calculation (Cohen's d >= 0.5 for medium effects), power analysis (1-beta >= 0.8). Require 2+ confirming signals before flagging violations. Store all evidence in Memory MCP with WHO/WHEN/PROJECT/WHY tags. |
| **One-Size-Fits-All Thresholds** | Applying generic thresholds (e.g., "accuracy > 90%") across all domains ignores context. Medical diagnosis requires 99%+ sensitivity to avoid false negatives, while recommendation systems tolerate lower accuracy for speed. Generic thresholds lead to either over-engineering or under-validation. | Define domain-specific thresholds based on use case requirements. Medical AI: ECE < 0.01, adversarial robustness > 80%. Consumer apps: latency < 100ms, throughput > 500 QPS. Document rationale for threshold selection in evaluation report. Coordinate with ethics-agent for high-risk domains. |

---

## Conclusion

Holistic evaluation transforms model validation from a narrow accuracy check into a comprehensive production-readiness assessment spanning six critical dimensions. By requiring quantitative evidence across accuracy, fairness, robustness, efficiency, interpretability, and safety, this skill ensures that models deployed to production meet rigorous standards comparable to FDA medical device approval or EU AI Act compliance. The integration with Quality Gate 2 in the Deep Research SOP provides a systematic GO/NO-GO decision framework backed by statistical rigor, preventing the deployment of models that excel in lab benchmarks while failing in real-world scenarios.

The value of holistic evaluation extends beyond risk mitigation - it enables informed trade-off decisions. A model evaluation revealing 87.5% accuracy, 8.2% fairness gaps, and 45.8% adversarial robustness under PGD attacks provides actionable intelligence: deploy in non-adversarial environments with fairness monitoring, while developing adversarial training for high-risk scenarios. This transparency prevents the dangerous illusion of universally optimal models and enables deployment strategies tailored to specific contexts and risk profiles.

For production ML systems, holistic evaluation is not optional - it is the difference between responsible deployment and catastrophic failure. Models passing Gate 2 validation have been systematically evaluated against production-ready standards, with documented evidence, statistical validation, and clear deployment recommendations. This rigorous evaluation framework ensures that ML systems deployed from Deep Research SOP meet or exceed academic publication standards and regulatory compliance requirements.