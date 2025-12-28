---
name: ml-expert
description: '**Version**: 1.0.0'
---

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

**Version**: 1.0.0
**Type**: Agent-based skill with SDK implementation
**Domain**: Machine learning model implementation, training, and optimization

## Description

Implement machine learning solutions including model architectures, training pipelines, optimization strategies, and performance improvements. This skill spawns a specialist ML implementation agent with deep expertise in PyTorch, deep learning architectures, training techniques, and production ML systems.

Use this skill when implementing new ML models, fixing training issues, optimizing performance, implementing research papers, or building production ML pipelines.

## Triggers

This skill activates when users request:
- "Implement this ML architecture"
- "Fix the training code"
- "Optimize model performance"
- "Implement [paper/technique]"
- "Build a training pipeline for..."
- "Add [feature] to the model"
- "Improve inference speed"

## Skill Architecture

### Skill Layer (Lightweight)
The skill handles:
1. **Detection**: Identify ML implementation requests
2. **Context Gathering**: Collect requirements, existing code, constraints
3. **Agent Spawning**: Invoke ML expert specialist with context
4. **Result Processing**: Validate and format implementation

### Agent Layer (Specialist)
The ML expert agent handles:
1. **Architecture Design**: Create model structures following best practices
2. **Implementation**: Write production-quality PyTorch code
3. **Optimization**: Apply performance improvements and best practices
4. **Validation**: Ensure correctness through testing

## Communication Protocol

### Skill → Agent Context Package
```json
{
  "task": "Implement TRM × Titans-MAG architecture",
  "requirements": {
    "model_type": "transformer",
    "parameters": "25M target",
    "features": ["sliding_window_attention", "long_term_memory", "ACT"],
    "framework": "pytorch",
    "constraints": {
      "vram": "6GB",
      "inference_speed": "real-time"
    }
  },
  "existing_code": {
    "files": ["model.py", "config.py"],
    "status": "partial_implementation"
  },
  "reference_materials": {
    "papers": ["TRM.pdf", "Titans-MAG.pdf"],
    "implementations": ["reference_model.py"]
  }
}
```

### Agent → Skill Results
```json
{
  "status": "implementation_complete",
  "deliverables": {
    "code_files": [
      {
        "path": "src/model/titans_mag.py",
        "description": "Titans-MAG backbone implementation",
        "loc": 350,
        "tested": true
      }
    ],
    "tests": [
      {
        "path": "tests/test_model.py",
        "coverage": 95,
        "all_passing": true
      }
    ],
    "documentation": {
      "architecture_diagram": "docs/architecture.md",
      "usage_examples": "examples/train.py"
    }
  },
  "performance_metrics": {
    "parameter_count": "25.6M",
    "inference_time": "45ms (GPU)",
    "vram_usage": "5.2GB"
  },
  "validation": {
    "unit_tests": "48/48 passing",
    "integration_tests": "12/12 passing",
    "manual_verification": "Forward/backward pass successful"
  }
}
```

## Agent Spawning Logic

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
import asyncio

async def execute_ml_expert(context: dict):
    """Spawn ML implementation specialist agent."""

    # Load specialist agent prompt
    with open('agents/ml-expert-specialist.prompt', 'r') as f:
        specialist_prompt = f.read()

    # Configure agent with write permissions (plan mode for safety)
    options = ClaudeAgentOptions(
        model='claude-sonnet-4-5',
        system_prompt=specialist_prompt,
        permission_mode='plan',  # Show intent before editing
        allowed_tools=['Read', 'Write', 'Edit', 'Bash', 'Grep'],
        setting_sources=['project']
    )

    client = ClaudeSDKClient(options)

    try:
        await client.connect()

        # Format task for agent
        task = f"""Implement ML solution:

Requirements: {context['requirements']}

Existing code: {context['existing_code']}

Reference materials: {context['reference_materials']}

Deliver production-quality implementation with tests and documentation."""

        await client.query(task)

        # Collect implementation results
        results = []
        async for message in client.receive_messages():
            if message.type == 'assistant':
                results.append(message.content)

        return parse_implementation(results)

    finally:
        await client.disconnect()
```

## Resources

### Scripts
- `scripts/init_model_template.py` - Generate model boilerplate
- `scripts/test_model.py` - Model testing utilities
- `scripts/profile_performance.py` - Performance profiling
- `scripts/validate_architecture.py` - Architecture validation

### References
- `references/pytorch-best-practices.md` - PyTorch coding standards
- `references/architecture-patterns.md` - Common ML architecture patterns
- `references/optimization-techniques.md` - Training optimization guide
- `references/testing-guide.md` - ML testing best practices

### Templates
- `templates/model_template.py` - Base model class template
- `templates/trainer_template.py` - Training loop template
- `templates/config_template.py` - Configuration dataclass template

### Custom Tools
- `create_model_skeleton()` - Generate model file structure
- `add_tests()` - Create test cases for model components
- `benchmark_model()` - Performance benchmarking

## Usage Examples

### Example 1: Implement New Architecture
```
User: "Implement the TRM × Titans-MAG architecture from these papers with 25M parameters"

Skill gathers:
- Paper PDFs with architecture details
- Target parameter count constraint
- PyTorch as framework
- GPU memory constraint (6GB)

Agent implements:
- Titans-MAG backbone (sliding window attention, LMM, MAG gate)
- TRM wrapper (multi-pass reasoning)
- ACT head (adaptive computation)
- Full model integration
- Unit tests (95% coverage)
- Usage examples
- Architecture documentation

Deliverables:
- src/model/titans_mag.py (350 LOC)
- src/model/trm_wrapper.py (180 LOC)
- src/model/act_head.py (120 LOC)
- src/model/full_model.py (200 LOC)
- tests/test_*.py (48 tests, all passing)
- docs/architecture.md
```

### Example 2: Fix Training Issue
```
User: "The ACT head has variance=0 issue. Add diversity regularization."

Skill gathers:
- Current ACT head implementation
- Diagnosis from ml-training-debugger skill
- Recommended fix (diversity loss)

Agent implements:
- Modify compute_act_loss() method
- Add diversity regularization term
- Update docstrings
- Add test for variance>0
- Verify training runs without warning

Deliverables:
- Modified src/model/act_head.py
- New test: tests/test_act_diversity.py
- Validation: Warning eliminated in training
```

### Example 3: Optimize Performance
```
User: "Model inference is too slow. Optimize for real-time performance."

Skill gathers:
- Current model code
- Profiling results
- Performance requirements (< 100ms)

Agent optimizes:
- Enable gradient checkpointing
- Fuse operations where possible
- Use torch.compile() for JIT optimization
- Optimize tensor operations
- Add caching for repeated computations

Deliverables:
- Optimized model code
- Performance benchmarks (45ms → 28ms)
- Memory usage reduced (6.2GB → 5.2GB)
- All tests still passing
```

## Quality Standards

The ML expert agent must:
- ✅ Write production-quality, well-documented code
- ✅ Follow PyTorch best practices and idioms
- ✅ Include comprehensive tests (≥90% coverage)
- ✅ Verify all implementations work end-to-end
- ✅ Provide usage examples and documentation
- ✅ Optimize for readability and maintainability

## Integration with Other Skills

This skill works with:
- **ml-training-debugger** - Implements fixes from diagnoses
- **code-analyzer** - Reviews implementation quality
- **functionality-audit** - Validates implementations work
- **style-audit** - Ensures code style compliance

## Failure Modes and Escalation

If the agent cannot implement the solution:
1. Clarify ambiguous requirements with user
2. Request additional reference materials
3. Implement partial solution with clear TODOs
4. Escalate if task exceeds ML expertise scope

The agent should NEVER:
- Write code without understanding requirements
- Implement untested functionality
- Make breaking changes to existing APIs
- Commit directly without validation

## Testing

Test the skill with:
1. New model implementation (TRM × Titans-MAG)
2. Bug fix implementation (ACT diversity loss)
3. Performance optimization (inference speed)
4. Research paper implementation
5. Production pipeline creation

## Documentation

- Agent system prompt: `agents/ml-expert-specialist.prompt`
- SDK implementation: `index.py`
- Process visualization: `ml-expert-process.dot`
- Testing guide: `tests/README.md`

## Core Principles

1. **Reproducibility is Non-Negotiable**: Machine learning experiments must be fully reproducible, meaning identical code with identical data and identical random seeds produces identical results within numerical precision. This requires fixing all sources of randomness (PyTorch, NumPy, CUDA), versioning datasets with checksums, and documenting environment details (GPU type, CUDA version, library versions). Reproducibility isn't just about scientific rigor - it's the foundation for debugging training issues, validating performance claims, and enabling collaborative research. Every model implementation should include a reproducibility checklist covering random seeds, data versioning, environment specifications, and validation procedures.

2. **Separate Model Architecture from Training Concerns**: Clean ML code separates what the model computes (forward pass, loss calculation) from how it's trained (optimization, learning rate scheduling, checkpointing). The model class should be a pure mathematical transformation with no references to optimizers, data loaders, or training loops. Training logic belongs in separate trainer classes that handle optimization, logging, and experiment management. This separation enables testing model components independently, swapping training strategies without touching model code, and reusing architectures across different training regimes. A model that can only be used within a specific training script is poorly architected.

3. **Performance Optimization Follows Correctness**: The sequence must be: implement correctly, verify mathematically, profile systematically, then optimize bottlenecks. Never optimize prematurely based on assumptions about what's slow. Use PyTorch Profiler or TensorBoard to identify actual bottlenecks (often data loading, not compute). Common optimizations include mixed precision training (torch.amp), gradient checkpointing for memory, torch.compile() for JIT optimization, and efficient data pipelines with prefetching. But these come after correctness is verified with unit tests, gradient checks, and validation that training curves match expected behavior.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|--------------|-----------------|
| **Training Without Validation Split** | Using only training loss to evaluate model performance leads to overfitting where the model memorizes training data but fails on unseen data. Without a validation set, you cannot detect when training should stop, cannot tune hyperparameters reliably, and cannot diagnose whether poor performance is due to underfitting or overfitting. | Always split data into train/validation/test sets before training begins (70/15/15 or 80/10/10). Monitor both training and validation loss every epoch. Use validation loss for early stopping and hyperparameter tuning. Only touch the test set once for final evaluation after all model decisions are finalized. Implement stratified splits for classification to maintain class balance. |
| **Ignoring Data Leakage** | Data leakage occurs when information from validation/test sets influences training, such as fitting scalers on entire datasets before splitting, using future information in time series, or data augmentation applied before splitting. This inflates validation metrics artificially and leads to models that fail catastrophically in production on truly unseen data. | Perform all data preprocessing after train/test split. For scalers/normalizers, fit only on training data then transform validation/test. For time series, use strict temporal splits with no future data in training. Apply data augmentation only to training set. Use cross-validation to validate that results are stable across different splits. Document preprocessing steps with explicit split boundaries. |
| **Deploying Without Monitoring** | Models degrade silently in production due to data drift (input distribution changes), concept drift (relationship between inputs/outputs changes), or system changes (preprocessing bugs, API changes). Without monitoring, you won't detect when model performance degrades until users complain or business metrics suffer. | Implement monitoring for input statistics (mean, std, quantiles) to detect data drift. Track prediction distributions to catch concept drift. Log model confidence scores to identify uncertain predictions. Set up alerts for anomalous inputs or prediction patterns. Periodically evaluate on fresh labeled data to measure real-world performance. Plan for model retraining cadence based on drift detection. |

## Conclusion

The ML Expert skill provides comprehensive machine learning implementation capabilities through specialized agent-based workflows. By separating architecture design, implementation, optimization, and validation concerns, this skill enables rapid development of production-quality ML systems while maintaining correctness and reproducibility.

Success with this skill requires balancing mathematical rigor with engineering pragmatism. The agent spawning architecture ensures that ML expertise is applied systematically - from implementing novel architectures from research papers to debugging training failures and optimizing inference performance. The quality standards enforced by this skill (comprehensive testing, documentation, performance validation) reflect the reality that ML code must be held to the same standards as production software, not treated as experimental scripts.

Whether implementing cutting-edge architectures like TRM and Titans-MAG, fixing subtle training issues like ACT variance collapse, or optimizing models for real-time inference, this skill provides the expertise and tooling to deliver robust ML solutions. The integration with ml-training-debugger creates a complete workflow from implementation through diagnosis to production deployment, ensuring that ML systems are not just mathematically correct but operationally reliable.