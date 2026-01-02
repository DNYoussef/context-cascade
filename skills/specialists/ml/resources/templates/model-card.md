# Model Card Template (Skill-Forge Aligned)

## Overview
- **Model name:**
- **Owners:**
- **Purpose:**
- **Stage:** prototype | ready-for-deployment
- **Source skill:** ml | ml-expert | ml-training-debugger

## Data
- **Datasets:** (source, version, license, collection notes)
- **Splits:** (train/val/test ratios, stratification rationale)
- **Preprocessing:** (normalization, augmentation, feature engineering)
- **Bias/Privacy considerations:**

## Model
- **Architecture:** (layers, parameters, special blocks)
- **Loss/Optimizer/Scheduler:**
- **Hyperparameters:** (learning rate, batch size, epochs, regularization)
- **Initialization/Seeds:**

## Training
- **Hardware:** (GPU/CPU, memory)
- **Runtime:**
- **Checkpoints:** (location, retention policy)
- **Reproducibility:** (seeds, configs, determinism flags)

## Evaluation
- **Metrics:** (with split and variance)
- **Robustness:** (class imbalance, drift sensitivity, adversarial probes)
- **Safety:** (PII handling, prompt/feature injection mitigations if applicable)

## Deployment
- **Artifacts:** (weights, tokenizer/preprocessor, config)
- **Interfaces:** (API/schema expectations)
- **Latency/Memory targets:**
- **Monitoring plan:** (drift, quality, cost)
- **Rollback strategy:**

## Risks & Limitations
- Known failure modes and mitigations.

## Confidence
Confidence: X.XX (ceiling: TYPE Y.YY) - rationale.
