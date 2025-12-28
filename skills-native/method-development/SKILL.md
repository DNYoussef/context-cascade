---
name: method-development
description: Develop novel machine learning methods with rigorous ablation studies for Deep Research SOP Pipeline D. Use after baseline replication passes Quality Gate 1, when creating new algorithms, proposing modifications to existing methods, or conducting systematic experimental validation. Includes architectural innovation, hyperparameter optimization, and component-wise ablation analysis leading to Quality Gate 2.
---

for Deep Research SOP Pipeline D. Use after baseline replication passes Quality
  Gate 1, when creating new algorithms, proposing modifications to existing methods,
  or conducting systematic experimental validation. Includes architectural innovation,
  hyperparameter optimization, and component-wise ablation analysis leading to Quality
  Gate 2.
- research
- analysis
- planning


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



### Phase 2: Prototype Implementation (1-2 days)

**Agent**: coder

**Objectives**:
1. Implement novel architecture in PyTorch/TensorFlow
2. Maintain code quality (100% test coverage)
3. Enable deterministic mode for reproducibility
4. Create modular, ablation-ready codebase

**Steps**:

#### 2.1 Project Setup
```bash
# Initialize project structure
mkdir -p src/{models,layers,utils,config}
mkdir -p tests/{unit,integration,ablation}
mkdir -p experiments/{configs,scripts,results}

# Copy baseline code as starting point
cp -r ../baseline-replication-package/src/* src/

# Initialize Git repository with DVC
git init
dvc init
```

#### 2.2 Novel Component Implementation
Invoke coder agent with:
```
Implement the following novel components:

1. Multi-Scale Attention (src/layers/attention.py)
   - Support 3 scales: local, medium, global
   - Efficient implementation using sparse matrices
   - Deterministic mode with fixed seeds

2. Pre-Norm Residual Blocks (src/layers/residual.py)
   - Layer normalization before residual connection
   - Optional dropout for regularization

3. [Other novel components...]

Requirements:
- Type hints for all functions
- Docstrings with complexity analysis
- Unit tests achieving 100% coverage
- Ablation flags for each component
```

**Code Quality Standards**:
```python
# Example: Multi-scale attention with ablation support
class MultiScaleAttention(nn.Module):
    """
    Multi-scale attention mechanism with local, medium, and global receptive fields.

    Computational Complexity:
    - Time: O(n * k) where n=sequence_length, k=num_scales
    - Space: O(n * d) where d=embedding_dimension

    Args:
        embed_dim: Embedding dimension
        num_heads: Number of attention heads per scale
        num_scales: Number of scales (default: 3)
        ablate_scales: Disable specific scales for ablation (default: None)

    Example:
        >>> attn = MultiScaleAttention(embed_dim=512, num_heads=8)
        >>> # Ablation: disable global scale
        >>> attn_ablated = MultiScaleAttention(embed_dim=512, num_heads=8,
        ...                                     ablate_scales=['global'])
    """
    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        num_scales: int = 3,
        ablate_scales: Optional[List[str]] = None
    ):
        super().__init__()
        self.ablate_scales = ablate_scales or []
        # Implementation...
```

#### 2.3 Integration with Baseline
```bash
# Ensure backward compatibility
python tests/integration/test_baseline_equivalence.py \
  --novel-model src/models/novel_model.py \
  --baseline-model ../baseline-replication-package/src/models/baseline.py \
  --ablate-all-novel  # Should match baseline when all novel components disabled
```

**Deliverable**: Implemented novel method codebase

#### 2.4 Test Suite Development
Invoke tester agent with:
```
Create comprehensive test suite covering:

1. Unit Tests (tests/unit/)
   - Each novel component in isolation
   - Edge cases and boundary conditions
   - Numerical stability tests

2. Integration Tests (tests/integration/)
   - Novel model end-to-end training
   - Gradient flow validation
   - Memory profiling

3. Ablation Tests (tests/ablation/)
   - Each component can be disabled via flags
   - Ablated model runs without errors
   - Ablation results logged correctly

Target: 100% code coverage
```

**Deliverable**: Complete test suite with coverage report



### Phase 4: Hyperparameter Optimization (1-2 days)

**Agent**: coder

**Objectives**:
1. Optimize hyperparameters for novel method
2. Conduct sensitivity analysis
3. Document optimal configuration
4. Compare with baseline hyperparameters

**Steps**:

#### 4.1 Hyperparameter Search Space
```python
# Define search space in experiments/configs/hparam_search.yaml
search_space:
  learning_rate:
    type: log_uniform
    min: 1e-5
    max: 1e-2

  attention_heads:
    type: choice
    values: [4, 8, 16, 32]

  num_layers:
    type: int_uniform
    min: 6
    max: 24

  dropout:
    type: uniform
    min: 0.0
    max: 0.5

  # [Continue for all tunable hyperparameters]
```

#### 4.2 Bayesian Optimization
```bash
# Run Bayesian optimization with Optuna
python experiments/scripts/optimize_hyperparameters.py \
  --search-space experiments/configs/hparam_search.yaml \
  --n-trials 100 \
  --sampler TPE \
  --pruner MedianPruner \
  --output experiments/results/hparam_optimization/
```

#### 4.3 Sensitivity Analysis
```bash
# Analyze hyperparameter sensitivity
python scripts/sensitivity_analysis.py \
  --optimization-results experiments/results/hparam_optimization/ \
  --method sobol \
  --output docs/sensitivity_analysis.pdf
```

**Deliverable**: Optimal hyperparameter configuration



### Phase 6: Documentation (2-4 hours)

**Agent**: archivist

**Objectives**:
1. Document novel method architecture
2. Create architectural diagrams
3. Write method card (similar to model card)
4. Prepare for Quality Gate 2

**Steps**:

#### 6.1 Method Card Creation
Coordinate with archivist agent:
```bash
npx claude-flow@alpha sparc run archivist \
  "Create method card for novel architecture following Mitchell et al. 2019 template"
```

**Method Card Sections**:
1. **Method Details**: Architecture, components, design rationale
2. **Intended Use**: Task types, domains, limitations
3. **Performance**: Metrics, comparisons, ablation results
4. **Training**: Hyperparameters, optimization, data requirements
5. **Computational Requirements**: GPU, memory, latency
6. **Ethical Considerations**: Bias, fairness, dual-use risks
7. **Caveats and Recommendations**: Known issues, best practices

#### 6.2 Architectural Diagrams
Create diagrams showing:
- High-level architecture comparison (baseline vs. novel)
- Novel component details (attention mechanism, residual blocks, etc.)
- Information flow diagrams
- Computational graph

**Tools**: draw.io, GraphViz, or LaTeX TikZ

#### 6.3 Reproducibility Documentation
```markdown
# Reproducibility Guide

## Environment Setup
\`\`\`bash
# Docker image
docker pull novel-method:v1.0

# Or build from source
docker build -t novel-method:v1.0 -f Dockerfile .
\`\`\`

## Training from Scratch
\`\`\`bash
python train.py \
  --config experiments/configs/optimal_hparams.yaml \
  --seed 42 \
  --deterministic \
  --output experiments/results/reproduction/
\`\`\`

## Expected Results
- Test Accuracy: 0.875 ± 0.003
- Training Time: ~48 hours on 4x V100 GPUs
- Final Checkpoint: experiments/results/reproduction/checkpoint_epoch_100.pth
\`\`\`
```

**Deliverable**: Complete documentation package



## Integration with Deep Research SOP

### Pipeline Integration
- **Pipeline D (Method Development)**: This skill implements the complete method development phase
- **Prerequisite**: Baseline replication (Quality Gate 1 APPROVED)
- **Next Step**: Holistic evaluation (Quality Gate 2 APPROVED required)

### Quality Gates
- **Gate 1**: Must pass before invoking this skill
- **Gate 2**: Validation performed in Phase 7 of this skill
- **Gate 3**: Archival and deployment (requires Gate 2 APPROVED)

### Agent Coordination
```
Flow: system-architect → coder → tester → reviewer → ethics-agent → archivist → evaluator

Phase 1: system-architect designs novel architecture
Phase 2: coder implements with 100% test coverage
Phase 3: tester runs ablation studies
Phase 4: coder optimizes hyperparameters
Phase 5: tester performs comparative evaluation
Phase 6: archivist creates documentation
Phase 7: evaluator validates Gate 2 + ethics-agent reviews safety/ethics
```

### Memory Coordination
All agents store/retrieve via Memory MCP:
```bash
# Store architectural decisions
npx claude-flow@alpha memory store \
  --key "sop/method-development/architecture" \
  --value "$(cat docs/architecture.md)"

# Retrieve baseline results for comparison
npx claude-flow@alpha memory retrieve \
  --key "sop/baseline-replication/results"
```



## Related Skills and Commands

### Prerequisites
- `baseline-replication` - Must complete before invoking this skill

### Next Steps (after Gate 2 APPROVED)
- `holistic-evaluation` - Comprehensive model evaluation across multiple dimensions
- `reproducibility-audit` - Audit reproducibility package before archival

### Related Commands
- `/validate-gate-2` - Gate 2 validation (evaluator agent)
- `/assess-risks` - Ethics review for models (ethics-agent)
- `/init-model-card` - Create model card (archivist agent)

### Parallel Skills
- `literature-synthesis` - Can run in parallel to gather SOTA comparisons



## Appendix

### Example Ablation Study Results

```
Ablation Study: Multi-Scale Attention Mechanism
================================================

Configuration: ResNet-50 + Multi-Scale Attention on ImageNet

| Ablation                  | Accuracy | Δ from Full | p-value | Significant |
|---------------------------|----------|-------------|---------|-------------|
| Full Model                | 0.875    | -           | -       | -           |
| Ablate Local Scale        | 0.868    | -0.7%       | 0.032   | Yes         |
| Ablate Medium Scale       | 0.871    | -0.4%       | 0.156   | No          |
| Ablate Global Scale       | 0.852    | -2.3%       | 0.001   | Yes         |
| Ablate All (Baseline)     | 0.850    | -2.5%       | <0.001  | Yes         |

Conclusion: Global scale is critical (+2.3% over baseline), local scale contributes moderately (+0.7%), medium scale is non-significant.

Recommendation: Keep global and local scales, consider removing medium scale to reduce computational cost.
```

### Example Method Card Template

```markdown
# Method Card: Multi-Scale Attention ResNet

## Method Details
**Architecture**: ResNet-50 with Multi-Scale Attention
**Novel Components**:
- Multi-Scale Attention (local, medium, global)
- Pre-Norm Residual Blocks
**Design Rationale**: Improve long-range dependency modeling while maintaining computational efficiency

## Intended Use
**Tasks**: Image classification, object detection
**Domains**: Computer vision, medical imaging
**Limitations**: Requires GPU with ≥16GB memory

## Performance
**ImageNet Accuracy**: 87.5% (±0.3%)
**Baseline Comparison**: +2.5% over ResNet-50
**Latency**: 45.2ms per image (batch=32)

## Training
**Hyperparameters**: lr=1e-4, batch=256, epochs=100
**Optimizer**: AdamW with cosine annealing
**Data**: ImageNet-1k (1.28M images)

## Computational Requirements
**GPUs**: 4x V100 (16GB each)
**Training Time**: 48 hours
**Memory**: 8.4GB per GPU

## Ethical Considerations
**Bias**: Evaluated on Balanced Faces dataset, demographic parity within 2%
**Fairness**: No disparate impact detected (p > 0.05)
**Dual-Use**: Standard image classification, low dual-use risk

## Caveats
- Requires deterministic mode for reproducibility (may impact performance by ~1%)
- Not tested on extremely high-resolution images (>2048px)
- Best performance with batch size ≥32
```
## Core Principles

Method Development operates on 3 fundamental principles:

### Principle 1: Ablation-Driven Validation
Every novel component must justify its inclusion through controlled ablation studies showing statistically significant performance impact (p < 0.05). This prevents architectural complexity without empirical benefit.

In practice:
- Minimum 5 component ablations isolate individual contributions
- Effect sizes (Cohen's d >= 0.5) verify practical significance beyond statistical significance
- Interaction effects tested through combinatorial ablations

### Principle 2: Baseline Superiority with Statistical Rigor
Novel methods must demonstrably outperform replicated baselines with proper statistical validation, multiple comparison corrections, and sufficient statistical power (1-beta >= 0.8).

In practice:
- Paired t-tests with Bonferroni correction for multiple metrics
- 95% confidence intervals reported for all performance claims
- Minimum 3 independent runs with different random seeds

### Principle 3: Reproducibility by Design
All method development includes deterministic implementation, comprehensive documentation, and validated reproducibility packages to enable independent verification and future research.

In practice:
- Docker containers with pinned dependencies for environment reproducibility
- Deterministic mode with fixed seeds for algorithmic reproducibility
- Method cards documenting architecture, training, and computational requirements

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Skipping Baseline Replication** | Comparing to reported baseline results without replication introduces confounds and prevents fair evaluation | Complete Quality Gate 1 baseline replication (±1% tolerance) before method development |
| **Insufficient Ablations** | Testing <5 components or skipping combinatorial ablations fails to isolate contributions and identify synergies | Run minimum 5 individual ablations plus key combinations, apply Bonferroni correction |
| **Cherry-Picking Results** | Reporting only best runs or metrics inflates apparent performance and harms reproducibility | Report all runs with median/mean appropriately, include full result distributions |

## Conclusion

Method Development provides a rigorous framework for developing and validating novel machine learning methods with academic-level experimental rigor. By enforcing ablation studies, statistical validation, and reproducibility standards, this skill ensures that novel methods represent genuine scientific contributions rather than engineering artifacts.

Use this skill after baseline replication (Quality Gate 1) when proposing architectural innovations, developing new training algorithms, or conducting systematic experimental validation for publication. The 7-phase workflow (architecture design, implementation, ablation studies, optimization, evaluation, documentation, Gate 2 validation) ensures comprehensive development while the guardrails prevent common pitfalls like p-hacking, cherry-picking, and insufficient statistical power. The result is publication-ready research with validated claims and reproducible results.