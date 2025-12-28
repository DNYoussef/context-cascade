# ML Expert - Machine Learning Implementation Specialist


## When to Use This Skill

- **Model Training**: Training neural networks or ML models
- **Hyperparameter Tuning**: Optimizing model performance
- **Model Debugging**: Diagnosing training issues (overfitting, vanishing gradients)
- **Data Pipeline**: Building training/validation data pipelines
- **Experiment Tracking**: Managing ML experiments and metrics
- **Model Deployment**: Serving models in production

## When NOT to Use This Skill

- **Data Analysis**: Exploratory data analysis or statistics (use data scientist)
- **Data Engineering**: Large-scale ETL or data warehouse (use data engineer)
- **Research**: Novel algorithm development (use research specialist)
- **Simple Rules**: Heuristic-based logic without ML

## Success Criteria

- [ ] Model achieves target accuracy/F1/RMSE on validation set
- [ ] Training/validation curves show healthy convergence
- [ ] No overfitting (train/val gap <5%)
- [ ] Inference latency meets production requirements
- [ ] Model size within deployment constraints
- [ ] Experiment tracked with metrics and artifacts (MLflow, Weights & Biases)
- [ ] Reproducible results (fixed random seeds, versioned data)

## Edge Cases to Handle

- **Class Imbalance**: Unequal class distribution requiring resampling
- **Data Leakage**: Information from validation/test leaking into training
- **Catastrophic Forgetting**: Model forgetting old tasks when learning new ones
- **Adversarial Examples**: Model vulnerable to adversarial attacks
- **Distribution Shift**: Training data differs from production data
- **Hardware Constraints**: GPU memory limitations or mixed precision training

## Guardrails

- **NEVER** evaluate on training data
- **ALWAYS** use separate train/validation/test splits
- **NEVER** touch test set until final evaluation
- **ALWAYS** version datasets and models
- **NEVER** deploy without monitoring for data drift
- **ALWAYS** document model assumptions and limitations
- **NEVER** train on biased or unrepresentative data

## Evidence-Based Validation

- [ ] Confusion matrix reviewed for class-wise performance
- [ ] Learning curves plotted (loss vs epochs)
- [ ] Validation metrics tracked across experiments
- [ ] Model profiled for inference time (TensorBoard, PyTorch Profiler)
- [ ] Ablation studies conducted for architecture choices
- [ ] Cross-validation performed for robust evaluation
- [ ] Statistical significance tested (t-test, bootstrap)

**Status**: Gold Tier Skill
**Version**: 2.0.0
**Type**: Agent-based ML implementation skill with comprehensive resources

## Quick Start

This skill provides expert-level ML implementation capabilities through a specialist agent with deep PyTorch expertise. Use it for implementing architectures, fixing training issues, and optimizing model performance.

### Basic Usage

```bash
# Implement new architecture
"Implement TRM × Titans-MAG with 25M parameters"

# Fix training issue
"Add diversity regularization to ACT head"

# Optimize performance
"Reduce inference time to <50ms"
```

## Triggers

Auto-activates on:
- "Implement [architecture/model]"
- "Fix training [issue]"
- "Optimize [metric]"
- "Build ML pipeline for..."
- "Add [feature] to model"

## Resources

### Scripts (resources/)
- **model-architect.py** - Neural architecture design and construction
- **feature-engineer.js** - Feature engineering pipeline automation
- **ensemble-builder.sh** - Ensemble model construction and validation
- **ml-debugger.py** - ML-specific debugging and diagnostics

### Templates (resources/)
- **architecture-template.yaml** - Model architecture configuration template
- **feature-config.json** - Feature engineering configuration
- **ensemble-strategy.yaml** - Ensemble strategy configuration

### Tests (tests/)
- **test_model_architect.py** - Architecture builder validation
- **test_feature_engineer.py** - Feature engineering pipeline tests
- **test_ensemble_builder.py** - Ensemble construction tests

### Examples (examples/)
- **neural-architecture-example.py** - Complete neural network implementation (200+ LOC)
- **feature-engineering-example.js** - Full feature engineering workflow (180+ LOC)
- **ensemble-methods-example.sh** - Ensemble learning demonstration (150+ LOC)

## Features

1. **Architecture Design** - Expert model architecture construction
2. **Training Optimization** - Performance tuning and debugging
3. **Feature Engineering** - Automated feature transformation
4. **Ensemble Methods** - Multi-model coordination
5. **Production Deployment** - Optimization for inference

## Quality Standards

- Production-quality PyTorch code
- ≥90% test coverage
- Comprehensive documentation
- End-to-end validation
- Performance benchmarking

## Integration

Works with:
- ml-training-debugger (diagnosis → fix)
- functionality-audit (validation)
- code-analyzer (quality review)
- production-readiness (deployment)

## Documentation

See SKILL.md for complete specification including:
- Agent communication protocol
- SDK implementation details
- Advanced usage patterns
- Failure mode handling
