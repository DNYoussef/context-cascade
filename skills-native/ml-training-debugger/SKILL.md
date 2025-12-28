---
name: ml-training-debugger
description: '**Version**: 1.0.0'
---

# ML Training Debugger


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
**Domain**: Machine learning training diagnostics

## Description

Diagnose machine learning training failures including loss divergence, mode collapse, gradient issues, architecture problems, and optimization failures. This skill spawns a specialist ML debugging agent that systematically analyzes training artifacts to identify root causes and propose evidence-based fixes.

Use this skill when encountering training failures, when loss curves exhibit pathological behavior, when models produce degenerate outputs, when experiencing GPU memory issues, or when hyperparameter tuning produces inconsistent results.

## Triggers

This skill activates when users request:
- "Debug my training run"
- "Why is my loss diverging?"
- "Model outputs are all the same token"
- "Training failed at epoch X"
- "Help diagnose mode collapse"
- "Why are gradients exploding/vanishing?"
- "Model not learning anything"

## Skill Architecture

### Skill Layer (Lightweight)
The skill handles:
1. **Detection**: Identify ML training debugging requests
2. **Context Gathering**: Collect training logs, loss curves, model code
3. **Agent Spawning**: Invoke ML debugging specialist with context
4. **Result Processing**: Format diagnosis and fixes for user

### Agent Layer (Specialist)
The ML debugging agent handles:
1. **Systematic Analysis**: Apply debugging methodology to artifacts
2. **Root Cause Identification**: Diagnose underlying issues
3. **Fix Prioritization**: Rank solutions by impact
4. **Evidence-Based Recommendations**: Propose fixes with reasoning

## Communication Protocol

### Skill → Agent Context Package
```json
{
  "task": "Diagnose training failure",
  "artifacts": {
    "training_logs": "path/to/logs.txt",
    "loss_curves": "path/to/losses.csv",
    "model_code": ["model.py", "trainer.py"],
    "error_messages": ["error1.txt"],
    "config": "config.yaml"
  },
  "symptoms": [
    "Loss diverged at epoch 7",
    "Mode collapse to single token",
    "Gradient norm exploded"
  ],
  "constraints": {
    "max_analysis_time": "5 minutes",
    "output_format": "structured_diagnosis"
  }
}
```

### Agent → Skill Results
```json
{
  "status": "diagnosis_complete",
  "root_causes": [
    {
      "issue": "Learning rate too high for Muon optimizer",
      "severity": "critical",
      "evidence": ["grad_norm spike at step 24590", "loss increased 15% in epoch 7"],
      "fix": "Reduce muon_lr from 1e-2 to 5e-3",
      "confidence": 0.95
    }
  ],
  "quick_fixes": ["Reduce LR by 50%", "Enable gradient clipping"],
  "analysis_artifacts": {
    "gradient_analysis": "path/to/grad_analysis.md",
    "loss_visualization": "path/to/loss_plot.png"
  }
}
```

## Agent Spawning Logic

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
import asyncio

async def execute_ml_debugger(context: dict):
    """Spawn ML debugging specialist agent."""

    # Load specialist agent prompt
    with open('agents/ml-debugger-specialist.prompt', 'r') as f:
        specialist_prompt = f.read()

    # Configure agent
    options = ClaudeAgentOptions(
        model='claude-sonnet-4-5',
        system_prompt=specialist_prompt,
        permission_mode='default',  # Read-only for safety
        allowed_tools=['Read', 'Grep', 'Bash'],  # Analysis tools only
        setting_sources=['project']
    )

    client = ClaudeSDKClient(options)

    try:
        await client.connect()

        # Format task for agent
        task = f"""Diagnose ML training failure:

Symptoms: {context['symptoms']}

Artifacts available:
- Training logs: {context['artifacts']['training_logs']}
- Loss curves: {context['artifacts']['loss_curves']}
- Model code: {', '.join(context['artifacts']['model_code'])}

Perform systematic analysis and provide structured diagnosis."""

        await client.query(task)

        # Collect diagnosis
        diagnosis = []
        async for message in client.receive_messages():
            if message.type == 'assistant':
                diagnosis.append(message.content)

        return parse_diagnosis(diagnosis)

    finally:
        await client.disconnect()
```

## Resources

### Scripts
- `scripts/analyze_loss_curve.py` - Loss curve analysis and visualization
- `scripts/check_gradients.py` - Gradient flow analysis
- `scripts/count_parameters.py` - Model parameter counting and distribution
- `scripts/profile_memory.py` - GPU memory profiling

### References
- `references/common-failure-modes.md` - Catalog of ML training failures
- `references/debugging-checklist.md` - Systematic debugging workflow
- `references/fix-templates.md` - Code templates for common fixes

### Custom Tools
- `extract_training_metrics()` - Parse logs for key metrics
- `visualize_loss_curve()` - Generate loss/gradient plots
- `analyze_architecture()` - Check model architecture balance

## Usage Examples

### Example 1: Loss Divergence
```
User: "My model was training fine until epoch 7, then loss started increasing. Help debug this."

Skill gathers:
- Training logs from epochs 1-10
- Loss curve data
- trainer.py and model.py
- Hyperparameter config

Agent diagnoses:
- Root cause: Learning rate too high for curriculum transition
- Evidence: Loss increased 15% at epoch 7, gradient norm spiked
- Fix: Reduce learning rate by 50%, add cosine annealing
- Confidence: 95%
```

### Example 2: Mode Collapse
```
User: "Model only outputs colons (::::) regardless of input. What's wrong?"

Skill gathers:
- Model checkpoint
- Inference test logs
- Training loss history
- Model architecture code

Agent diagnoses:
- Root cause: Embedding layer has 79% of params, transformer underparameterized
- Evidence: Training loss decreased but model has no capacity to learn patterns
- Fix: Rebalance architecture (50% embeddings, 50% transformers)
- Confidence: 90%
```

### Example 3: Gradient Issues
```
User: "Getting warning 'var(): degrees of freedom is <= 0' during training"

Skill gathers:
- Full error traceback
- Gradient statistics from logs
- ACT head implementation code

Agent diagnoses:
- Root cause: ACT variance = 0 (all tokens use same halting steps)
- Evidence: Warning appears in ACT loss computation
- Fix: Add diversity regularization to ACT loss
- Confidence: 98%
```

## Result Processing

The skill processes agent diagnosis into user-friendly format:

1. **Extract Root Causes**: Parse structured diagnosis
2. **Prioritize Fixes**: Rank by impact and confidence
3. **Format Recommendations**: Present as actionable steps
4. **Include Evidence**: Show supporting data/logs
5. **Generate Visualizations**: Create loss plots, gradient heatmaps

## Quality Standards

The ML debugging agent must:
- ✅ Identify root cause with >80% confidence or request more data
- ✅ Provide evidence from actual artifacts (not speculation)
- ✅ Propose fixes with expected impact and reasoning
- ✅ Complete analysis within 5 minutes for typical cases
- ✅ Handle missing artifacts gracefully (work with available data)

## Integration with Other Skills

This skill can be used in conjunction with:
- **ml-expertise** skill for implementing fixes
- **code-analyzer** skill for architecture review
- **functionality-audit** skill for validating fixes

## Failure Modes and Escalation

If the agent cannot diagnose the issue:
1. Request additional artifacts (specific logs, config files)
2. Provide partial diagnosis with lower confidence
3. Suggest alternative debugging approaches
4. Escalate to user with specific questions

The agent should NEVER:
- Guess at root causes without evidence
- Propose fixes that could corrupt training state
- Modify code directly (read-only mode)

## Testing

Test the skill with:
1. Real Phase 1 training failure (loss divergence at epoch 7)
2. Synthetic mode collapse scenario
3. Architecture imbalance case (79% embedding params)
4. Gradient explosion/vanishing cases
5. Missing artifacts scenario

## Documentation

- Agent system prompt: `agents/ml-debugger-specialist.prompt`
- SDK implementation: `index.py`
- Process visualization: `ml-training-debugger-process.dot`
- Testing guide: `tests/README.md`

## Core Principles

1. **Systematic Diagnosis Over Random Fixes**: Machine learning debugging requires systematic analysis of training artifacts rather than throwing random fixes at the problem. The methodology is: gather evidence (loss curves, gradient statistics, model outputs), form hypotheses (learning rate too high, architecture imbalance, data issues), test hypotheses against evidence, then propose targeted fixes with expected impact. Random fixes like "try a different optimizer" or "add more layers" waste compute resources and make it impossible to understand what actually works. Instead, analyze gradient norms to detect exploding/vanishing gradients, examine loss curves to identify divergence patterns, profile memory usage to find bottlenecks, and inspect model outputs to detect mode collapse or degenerate behaviors. Each diagnosis should be supported by concrete evidence from logs, metrics, or code analysis.

2. **Root Causes vs Symptoms**: Training failures manifest as symptoms (high validation loss, mode collapse, NaN gradients) but require identifying root causes for effective fixes. High validation loss could be caused by insufficient model capacity, poor hyperparameters, data quality issues, or architectural problems - treating the symptom without diagnosing the cause leads to ineffective solutions. Mode collapse to repeated tokens suggests architectural imbalance or loss function issues, not just "add dropout". NaN gradients indicate numerical instability from exploding gradients, learning rate too high, or overflow in loss calculations. The debugging process must trace symptoms back to root causes through systematic elimination: verify data pipeline correctness, check architecture parameter balance, validate hyperparameter ranges, then analyze training dynamics.

3. **Evidence-Based Confidence Levels**: Diagnoses should include confidence levels based on evidence quality. High confidence (>90%) requires direct evidence from logs/metrics confirming the diagnosis, such as gradient norm spike at exact epoch where loss diverged. Medium confidence (70-90%) requires circumstantial evidence like architectural patterns known to cause similar issues. Low confidence (<70%) requires requesting more data or proposing multiple hypotheses. Never present speculative diagnoses as certain - explicitly state confidence and reasoning. This enables users to prioritize fixes appropriately and understand which solutions are likely to work versus which are exploratory.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|--------------|-----------------|
| **Blindly Applying Common Fixes** | Suggesting "reduce learning rate" or "add batch normalization" without analyzing actual training artifacts wastes time and compute. These generic fixes might address symptoms temporarily but miss the root cause. Reducing learning rate might mask architectural problems that will resurface later. Adding batch norm without understanding why gradients are unstable introduces complexity without solving the underlying issue. | Analyze training logs systematically: plot loss curves to identify when divergence started, examine gradient norms across layers to pinpoint instability, profile forward/backward passes to find bottlenecks, inspect model outputs to detect degenerate behaviors. Use this evidence to form specific hypotheses, then propose targeted fixes with expected impact ("Gradient norm spiked 10x at epoch 7 when curriculum changed, suggesting learning rate too high for new data distribution. Reduce by 50% and add cosine annealing"). |
| **Ignoring Data Pipeline Validation** | Assuming training failures are always model/hyperparameter issues when data pipeline bugs (incorrect normalization, batch construction errors, label corruption) are common causes. Data issues manifest as models that don't learn (loss doesn't decrease), learn nonsensical patterns (high training accuracy but random validation accuracy), or exhibit sudden performance drops (preprocessor changed). | Validate data pipeline before debugging model: inspect batches visually to verify correctness, check label distributions match expectations, verify augmentation produces sensible outputs, test preprocessing code with known inputs, validate that train/validation splits have no overlap. Implement data versioning with checksums to detect silent corruption. Add data quality assertions in training loop (check for NaN/Inf, verify value ranges, validate batch shapes). |
| **Proposing Fixes Without Expected Impact** | Suggesting changes without explaining what they should fix and how to verify success makes debugging iterative instead of convergent. "Try adding dropout" doesn't specify where, why, or what metrics should improve. This leads to endless experimentation without learning what works. | Every fix proposal should include: (1) what root cause it addresses with evidence, (2) what metrics should improve (expected validation accuracy increase, gradient norm stabilization), (3) how to verify the fix worked (loss curve shape change, gradient statistics), (4) what to try next if it doesn't work. Example: "Add gradient clipping (max_norm=1.0) to stabilize exploding gradients. Expected: gradient norm stays below 5.0, loss decreases smoothly. Verify with gradient norm logging. If ineffective, indicates learning rate still too high - try reducing by additional 50%." |

## Conclusion

The ML Training Debugger skill provides systematic diagnostic capabilities for machine learning training failures through specialized agent-based workflows. By applying structured debugging methodologies to training artifacts, this skill enables rapid identification of root causes and targeted fixes that address underlying issues rather than masking symptoms.

Success with this skill requires discipline in evidence gathering, hypothesis formation, and confidence calibration. The agent spawning architecture ensures that debugging expertise is applied systematically across all training failure modes - from loss divergence to mode collapse to gradient instabilities. The integration with ml-expert skill creates a complete workflow where diagnoses directly inform implementation fixes, validated through functionality audit.

The value of this skill emerges most clearly during critical training failures where compute time is expensive and deadlines are tight. Rather than spending days trying random fixes, systematic diagnosis identifies root causes within minutes to hours, enabling targeted solutions that actually work. The quality standards enforced - evidence-based reasoning, confidence levels, expected impact statements - ensure that debugging is a learning process that builds understanding rather than trial-and-error that accumulates technical debt.

Whether diagnosing subtle issues like ACT variance collapse or obvious failures like loss divergence, this skill provides the methodology, tooling, and expertise to debug machine learning training efficiently and effectively. The agent-based architecture enables scaling this expertise across teams, ensuring that debugging knowledge is captured systematically rather than lost when individuals leave projects.