---
name: ml
description: Machine Learning development workflow with experiment tracking, hyperparameter optimization, and MLOps integration
---

# ML Development Skill


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

Comprehensive machine learning development workflow with enterprise-grade experiment tracking, automated hyperparameter optimization, model registry management, and production MLOps pipelines.

## Overview

This Gold-tier skill provides a complete ML development lifecycle with:
- **Experiment Tracking**: MLflow/W&B integration for reproducible experiments
- **Hyperparameter Optimization**: Optuna/Ray Tune for automated tuning
- **Model Registry**: Centralized model versioning and deployment
- **MLOps Pipeline**: Production-ready model serving and monitoring

## Quick Start

```bash
# Initialize ML project
npx claude-flow sparc run ml "Create ML project for image classification"

# Track experiment
python resources/scripts/experiment-tracker.py --config experiment-config.yaml

# Optimize hyperparameters
node resources/scripts/hyperparameter-tuner.js --space hyperparameter-space.json

# Deploy model
bash resources/scripts/model-registry.sh deploy production latest
```

## Workflow Phases

### 1. Experiment Design
- Define hypothesis and metrics
- Configure experiment tracking
- Set up data pipelines
- Validate data quality

### 2. Model Development
- Implement model architecture
- Configure training pipeline
- Set up validation strategy
- Enable experiment logging

### 3. Hyperparameter Optimization
- Define search space
- Select optimization algorithm
- Run distributed trials
- Analyze results

### 4. Model Evaluation
- Comprehensive metrics analysis
- Cross-validation
- Error analysis
- Model interpretability

### 5. Model Deployment
- Register model in registry
- Create deployment pipeline
- Set up monitoring
- Enable A/B testing

## Resources

### Scripts
- `experiment-tracker.py`: MLflow/W&B experiment tracking with auto-logging
- `hyperparameter-tuner.js`: Distributed hyperparameter optimization
- `model-registry.sh`: Model versioning and deployment automation
- `ml-ops.py`: End-to-end MLOps pipeline orchestration

### Templates
- `experiment-config.yaml`: Experiment configuration template
- `hyperparameter-space.json`: Hyperparameter search space definition
- `model-card.md`: Model documentation template

## Examples

### 1. Experiment Tracking
150-line example showing MLflow integration with auto-logging, artifact tracking, and metric visualization.

### 2. Hyperparameter Optimization
250-line example demonstrating Optuna-based distributed hyperparameter tuning with pruning and parallel trials.

### 3. MLOps Pipeline
300-line example implementing complete MLOps workflow with model registry, CI/CD, and monitoring.

## Best Practices

1. **Reproducibility**
   - Track all experiment parameters
   - Version control data and code
   - Use deterministic random seeds
   - Document environment dependencies

2. **Experiment Organization**
   - Use hierarchical experiment structure
   - Tag experiments meaningfully
   - Archive failed experiments
   - Maintain experiment runbooks

3. **Model Management**
   - Semantic versioning for models
   - Comprehensive model cards
   - Automated model testing
   - Deployment staging (dev/staging/prod)

4. **Performance Optimization**
   - Distributed training for large models
   - Mixed precision training
   - Efficient data loading
   - Model compression techniques

5. **Monitoring & Observability**
   - Real-time metric tracking
   - Data drift detection
   - Model performance degradation alerts
   - Resource utilization monitoring

## Integration Points

- **Data**: AgentDB for vector search, PostgreSQL for metadata
- **Compute**: Flow Nexus sandboxes for distributed training
- **CI/CD**: Automated model testing and deployment
- **Memory**: Store experiment insights in Memory MCP

## Advanced Features

- **AutoML**: Automated architecture search and feature engineering
- **Distributed Training**: Multi-GPU and multi-node training
- **Model Compression**: Quantization, pruning, distillation
- **Federated Learning**: Privacy-preserving distributed training
- **Continuous Training**: Automated retraining on new data

## Troubleshooting

### Common Issues
1. **Out of Memory**: Reduce batch size, enable gradient checkpointing
2. **Slow Training**: Use mixed precision, optimize data pipeline
3. **Poor Convergence**: Adjust learning rate, check data quality
4. **Deployment Failures**: Validate model compatibility, test inference

### Debug Mode
```bash
# Enable verbose logging
export ML_DEBUG=1
python resources/scripts/experiment-tracker.py --debug
```

## Performance Metrics

- **Experiment Setup**: 2-5 minutes
- **Hyperparameter Optimization**: 30min - 6 hours (depending on search space)
- **Model Deployment**: 5-10 minutes
- **Full MLOps Pipeline**: 1-2 hours

## Support

For issues or questions:
- Check examples directory for reference implementations
- Review test files for usage patterns
- Consult MLflow/Optuna documentation
- Use `functionality-audit` skill for validation



## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Training on test data** | Inflates accuracy metrics, model fails in production due to overfitting to test distribution | Use strict train/val/test splits. Never touch test set until final evaluation. Use cross-validation on training data only. |
| **Ignoring class imbalance** | Model achieves high accuracy by predicting majority class, fails on minority classes | Apply class weights, resampling (SMOTE), or stratified sampling. Evaluate with F1-score, precision-recall curves, not just accuracy. |
| **Deploying without monitoring** | Model degrades silently as production data drifts from training distribution | Implement data drift detection (KL divergence, PSI). Monitor prediction confidence distributions. Set up automated alerts for performance degradation. |
| **Hyperparameter tuning on test set** | Leaks test information into model selection, overestimates generalization | Tune hyperparameters only on validation set. Reserve test set for final evaluation after all decisions are made. |
| **No experiment tracking** | Cannot reproduce results or compare experiments, wastes time re-running experiments | Use MLflow/W&B from day one. Track all hyperparameters, metrics, and artifacts. Tag experiments with meaningful names. |
| **Premature optimization** | Spending weeks optimizing model before validating basic approach works | Start with simple baseline (logistic regression, small network). Validate approach works. Then optimize. |

---

## Conclusion

Machine learning development requires a rigorous engineering mindset that balances scientific accuracy with production pragmatism. The ML Development Skill provides a comprehensive workflow that treats reproducibility, evidence-based validation, and production readiness as first-class requirements, not afterthoughts.

By integrating experiment tracking (MLflow/W&B), automated hyperparameter optimization (Optuna), and production MLOps pipelines from the start, this skill ensures that models are not only accurate but also deployable, maintainable, and scientifically rigorous. The emphasis on statistical validation, data quality, and monitoring prevents common pitfalls like overfitting, data leakage, and silent production failures.

Whether you are training a simple classifier or building a complex multi-model pipeline, this skill enforces best practices that scale from research prototypes to production systems. The three core principles - reproducibility first, evidence-based validation, and production readiness - guide every phase of the ML lifecycle, from initial data exploration to continuous model improvement in production.