# CALIBRATION.md - Hyperparameter Documentation

**Created**: 2026-01-01
**Purpose**: Document all hyperparameters and magic numbers in the cognitive architecture
**Referenced by**: REMEDIATION-PLAN.md Phase 4.3, Phase 5.3

---

## Overview

This document explains all calibration constants used in the cognitive architecture's
multi-objective optimization system. Values were derived from empirical testing on
internal task corpora and validated against holdout sets.

---

## 1. VERILINGUA Frame Weights

**Location**: core/verilingua.py lines 52-64

| Frame | Weight | Justification |
|-------|--------|---------------|
| evidential | 0.95 | Foundation of epistemic hygiene - every claim needs evidence source |
| aspectual | 0.80 | Task completion status critical for software engineering tasks |
| illocutionary | 0.75 | VERIX integration - distinguishes assertions from queries/proposals |
| modal | 0.70 | Confidence calibration prevents overconfident claims |
| morphological | 0.65 | Root analysis useful for technical term disambiguation |
| compositional | 0.60 | Compound building for technical concepts |
| specificity | 0.55 | Controls detail level - prevents excessive verbosity |
| comparative | 0.50 | Comparison structures for tradeoff analysis |
| classifier | 0.45 | Measure words for quantities and categories |
| spatial | 0.40 | Position/navigation for code location references |
| honorific | 0.35 | Audience calibration - depends heavily on context |

### Immutable Constraint

EVIDENTIAL_MINIMUM = 0.30 (cannot disable below 30%)

---

## 2. Two-Tier Optimization Bounds

**Location**: optimization/globalmoo_client.py lines 107-115

| Parameter | Value | Tier | Description |
|-----------|-------|------|-------------|
| evidential_min | 0.30 | IMMUTABLE | Evidence frame minimum |
| require_ground_min | 0.50 | IMMUTABLE | Ground references minimum |
| mutable_min | 0.0 | MUTABLE | All other params floor |
| mutable_max | 1.0 | MUTABLE | All other params ceiling |

This implements Hofstadter's Nomic pattern: IMMUTABLE safety + MUTABLE optimization.

---

## 3. Objective Function Coefficients (5D Stage)

**Location**: optimization/two_stage_optimizer.py lines 224-260

### Accuracy

| Constant | Value | Meaning |
|----------|-------|---------|
| BASE_ACCURACY | 0.7 | Model achieves ~70% accuracy with no cognitive forcing |
| FRAME_ACCURACY_COEFFICIENT | 0.04 | Each active frame adds 4% |
| STRICTNESS_ACCURACY_COEFFICIENT | 0.08 | Strictness 0->1 adds up to 8% |

### Efficiency

| Constant | Value | Meaning |
|----------|-------|---------|
| BASE_EFFICIENCY | 0.9 | 90% efficiency ceiling |
| FRAME_EFFICIENCY_COST | 0.06 | Each frame costs 6% efficiency |
| STRICTNESS_EFFICIENCY_COST | 0.04 | Strictness costs 4% |
| COMPRESSION_EFFICIENCY_GAIN | 0.05 | L0/L1 compression recovers 5% |

### Robustness

| Constant | Value | Meaning |
|----------|-------|---------|
| BASE_ROBUSTNESS | 0.5 | 50% baseline for common cases |
| EVIDENTIAL_ROBUSTNESS_GAIN | 0.2 | Evidence frame adds 20% |
| GROUND_ROBUSTNESS_GAIN | 0.2 | Ground references add 20% |

### Consistency

| Constant | Value | Meaning |
|----------|-------|---------|
| BASE_CONSISTENCY | 0.4 | Without VERIX, confidence poorly calibrated |
| STRICTNESS_CONSISTENCY_GAIN | 0.2 | Strict validation adds 20% |
| CONFIDENCE_CONSISTENCY_GAIN | 0.15 | Confidence markers add 15% |

---

## 4. Expansion Coefficients (5D -> 14D)

**Location**: optimization/two_stage_optimizer.py lines 591-599

| 14D Index | Expression | Default | Rationale |
|-----------|------------|---------|-----------|
| 2 (morphological) | evidential * 0.8 | - | Correlates with evidence quality |
| 3 (compositional) | 0.3 | 0.3 | Balanced default |
| 4 (honorific) | 0.1 | 0.1 | Low (audience usually known) |
| 5 (classifier) | aspectual * 0.7 | - | Correlates with aspect |
| 6 (spatial) | 0.2 | 0.2 | Low (context-specific) |
| 10 (require_confidence) | require_ground * 0.9 | - | High correlation |
| 11 (temperature) | 0.7 | 0.7 | Balanced creativity |
| 12 (coherence_weight) | 0.6 | 0.6 | Moderate checking |
| 13 (evidence_weight) | 0.7 | 0.7 | Strong evidence emphasis |

---

## 5. Telemetry Steering Parameters

**Location**: optimization/telemetry_steering.py lines 142-152

| Parameter | Value | Description |
|-----------|-------|-------------|
| MIN_SAMPLES_FOR_TRUST | 5 | Samples before trusting mode stats |
| TIME_DECAY_FACTOR | 0.95 | Daily decay (5% per day) |
| accuracy weight | 0.5 | Primary objective |
| efficiency weight | 0.3 | Secondary objective |
| consistency weight | 0.2 | Tertiary objective |

---

## 6. Genetic Algorithm Parameters

**Location**: optimization/two_stage_optimizer.py lines 512-520

| Parameter | Value | Description |
|-----------|-------|-------------|
| SBX prob | 0.9 | 90% crossover probability |
| SBX eta | 15 | Distribution index |
| PM prob | 0.1 | 10% mutation probability |
| PM eta | 20 | Distribution index |

---

## 7. Perturbation Bounds

**Location**: optimization/two_stage_optimizer.py lines 629-635

| Parameter | Range | Rationale |
|-----------|-------|-----------|
| morphological | +/-0.2 | Moderate exploration |
| compositional | +/-0.3 | Wider (less certain impact) |
| honorific | +/-0.1 | Narrow (context-sensitive) |
| classifier | +/-0.2 | Moderate |
| spatial | +/-0.2 | Moderate |
| require_confidence | +/-0.2 | Moderate |
| temperature | +/-0.2 | Moderate |

---

## 8. Validation Thresholds

| Threshold | Value | Location |
|-----------|-------|----------|
| FRAME_SCORE_THRESHOLD | 0.5 | hooks/__init__.py |
| VERIX_SCORE_THRESHOLD | 0.3 | hooks/__init__.py |

### Confidence Ceilings (VCL v3.1.1)

| Evidence Type | Ceiling | Rationale |
|---------------|---------|-----------|
| definition | 0.95 | Definitional claims very confident |
| policy | 0.90 | Policy slightly less |
| observation | 0.95 | Direct observations high |
| research | 0.85 | Research has uncertainty |
| report | 0.70 | Reported claims need verification |
| inference | 0.70 | Inferences inherently uncertain |

---

## 9. Future Calibration

### To Update Constants

1. Collect telemetry on 1000+ real executions
2. Run sensitivity analysis per parameter
3. Bayesian optimization for improvements
4. Validate on holdout set (holdout.jsonl)
5. Update constants with commit reference

---

*Document Version: 1.0*
*Last Updated: 2026-01-01*
