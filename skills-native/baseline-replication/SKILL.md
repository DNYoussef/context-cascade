---
name: baseline-replication
description: "Replicate published ML baseline experiments with exact reproducibility\ \ (\xB11% tolerance) for Deep Research SOP Pipeline D. Use when validating baselines,\ \ reproducing experiments, verifying published results, or preparing for novel method\ \ development."
---

\ (\xB11% tolerance) for Deep Research SOP Pipeline D. Use when validating baselines,\
  \ reproducing experiments, verifying published results, or preparing for novel method\
  \ development."
## Quick Start (30 minutes)

### Basic Replication
```bash
# 1. Specify baseline to replicate
BASELINE_PAPER="BERT: Pre-training of Deep Bidirectional Transformers (Devlin et al., 2019)"
BASELINE_CODE="https://github.com/google-research/bert"
TARGET_METRIC="Accuracy on SQuAD 2.0"
PUBLISHED_RESULT=0.948

# 2. Run replication workflow
./scripts/replicate-baseline.sh \
  --paper "$BASELINE_PAPER" \
  --code "$BASELINE_CODE" \
  --metric "$TARGET_METRIC" \
  --expected "$PUBLISHED_RESULT"

# 3. Review results
cat output/baseline-bert/replication-report.md
```

Expected output:
```
✓ Paper analyzed: Extracted 47 hyperparameters
✓ Dataset validated: SQuAD 2.0 matches baseline
✓ Implementation complete: 12 BERT layers, 110M parameters
✓ Training complete: 3 epochs, 26.3 GPU hours
✓ Results validated: 0.945 vs 0.948 (within ±1% tolerance)
✓ Reproducibility verified: 3/3 fresh reproductions successful
→ Quality Gate 1: APPROVED
```

### Phase 2: Dataset Validation (20 minutes)

#### Coordinate with data-steward Agent
```bash
# Validate dataset matches baseline specs
./scripts/validate-dataset.sh \
  --dataset "SQuAD 2.0" \
  --splits "train:130k,dev:12k" \
  --preprocessing "WordPiece tokenization, max_length=384"
```

**data-steward checks**:
- Exact dataset version (v2.0, not v1.1)
- Sample counts match (training: 130,319 examples)
- Data splits match (80/10/10 vs 90/10)
- Preprocessing matches (lower-casing, accent stripping)
- Checksum validation (SHA256 hashes)

**Output**: `dataset-validation-report.md`

### Phase 4: Experiment Execution (4-8 hours)

#### Coordinate with tester Agent
```bash
# Run experiments with monitoring
./scripts/run-experiments.sh \
  --implementation baseline-bert-implementation.py \
  --config config/bert-squad.yaml \
  --gpus 4 \
  --monitor true
```

**tester executes**:
1. **Environment Setup**:
   ```bash
   # Create deterministic environment
   docker build -t baseline-bert:v1.0 -f Dockerfile .
   docker run --gpus all -v $(pwd):/workspace baseline-bert:v1.0
   ```

2. **Training with Monitoring**:
   ```python
   # Log training curves
   from torch.utils.tensorboard import SummaryWriter
   writer = SummaryWriter('logs/baseline-bert')

   for epoch in range(3):
       for batch in dataloader:
           loss = model(batch)
           writer.add_scalar('Loss/train', loss, global_step)
           writer.add_scalar('LR', optimizer.param_groups[0]['lr'], global_step)
   ```

3. **Checkpoint Saving**:
   ```python
   # Save best checkpoint
   torch.save({
       'epoch': epoch,
       'model_state_dict': model.state_dict(),
       'optimizer_state_dict': optimizer.state_dict(),
       'loss': loss,
       'accuracy': accuracy
   }, 'checkpoints/best-model.pt')
   ```

**Output**:
- `training.log` - Complete training logs
- `best-model.pt` - Best checkpoint
- `metrics.json` - All evaluation metrics

### Phase 6: Reproducibility Packaging (30 minutes)

#### Coordinate with archivist Agent
```bash
# Create complete reproducibility package
./scripts/create-repro-package.sh \
  --name baseline-bert \
  --code baseline-bert-implementation.py \
  --model best-model.pt \
  --env requirements.txt
```

**archivist creates**:
```
baseline-bert-repro.tar.gz
├── README.md                    # ≤5 steps to reproduce
├── requirements.txt             # Exact versions
├── Dockerfile                   # Exact environment
├── src/
│   ├── baseline-bert-implementation.py
│   ├── data_loader.py
│   └── train.py
├── data/
│   └── download_instructions.txt
├── models/
│   └── best-model.pt
├── logs/
│   └── training.log
├── results/
│   ├── metrics.json
│   └── comparison.csv
└── MANIFEST.txt                 # SHA256 checksums
```

**README.md (≤5 steps)**:
```markdown
# BERT SQuAD 2.0 Baseline Reproduction

## Quick Reproduction (3 steps)

1. Build Docker environment:
   ```bash
   docker build -t bert-squad:v1.0 .
   ```

2. Download SQuAD 2.0 dataset:
   ```bash
   ./download_data.sh
   ```

3. Run training:
   ```bash
   docker run --gpus all -v $(pwd):/workspace bert-squad:v1.0 python src/train.py
   ```

Expected result: 0.945 ± 0.001 accuracy (within ±1% of published 0.948)
```

#### Test Reproducibility
```bash
# Fresh Docker reproduction
./scripts/test-reproducibility.sh --package baseline-bert-repro.tar.gz --runs 3
```

**Output**: 3 successful reproductions with deterministic results

## Advanced Features

### Multi-Baseline Comparison
```bash
# Compare multiple baselines simultaneously
./scripts/compare-baselines.sh \
  --baselines "bert-base,roberta-base,electra-base" \
  --dataset "SQuAD 2.0" \
  --metrics "accuracy,f1,em"
```

### Ablation Study Integration
```bash
# Once baseline validated, run ablations
./scripts/run-ablations.sh \
  --baseline baseline-bert \
  --ablations "no-warmup,no-weight-decay,smaller-lr"
```

### Continuous Validation
```bash
# Set up monitoring for baseline drift
./scripts/setup-monitoring.sh \
  --baseline baseline-bert \
  --schedule "weekly" \
  --alert-threshold 0.02
```

## Output Files

| File | Description | Size |
|------|-------------|------|
| `baseline-{method}-specification.md` | Extracted methodology | ~5KB |
| `dataset-validation-report.md` | Dataset validation results | ~2KB |
| `baseline-{method}-implementation.py` | Clean implementation | ~10KB |
| `baseline-{method}-implementation_test.py` | Unit tests | ~5KB |
| `training.log` | Complete training logs | ~100MB |
| `best-model.pt` | Best checkpoint | ~400MB |
| `metrics.json` | All evaluation metrics | ~1KB |
| `baseline-{method}-comparison.md` | Results comparison | ~3KB |
| `baseline-{method}-comparison.csv` | Metrics table | ~1KB |
| `baseline-{method}-repro.tar.gz` | Reproducibility package | ~450MB |
| `gate-1-validation-checklist.md` | Quality Gate 1 evidence | ~3KB |

## Related Skills

- **method-development** - Develop novel methods after baseline validation
- **holistic-evaluation** - Run HELM + CheckList evaluations (Pipeline E)
- **gate-validation** - Quality Gate approval workflow
- **reproducibility-audit** - Test reproducibility packages
- **literature-synthesis** - PRISMA systematic reviews

**Created**: 2025-11-01
**Version**: 1.0.0
**Category**: Deep Research SOP
**Pipeline**: D (Method Development)
**Quality Gate**: 1 (Baseline Validation)
**Estimated Time**: 8-12 hours (first baseline), 4-6 hours (subsequent)
## Core Principles

Baseline Replication operates on 3 fundamental principles:

### Principle 1: Exact Reproducibility (+-1% Tolerance)
All baseline replications must match published results within +-1% statistical tolerance using identical hyperparameters, datasets, and deterministic settings. This validates that baselines are understood and provides a fair comparison foundation.

In practice:
- All 47+ hyperparameters extracted from paper, code, and supplements
- Deterministic mode enforced (torch.use_deterministic_algorithms(True))
- 3 independent runs with identical results verify determinism
- Statistical validation with paired t-tests confirms tolerance

### Principle 2: Fresh Environment Reproducibility
Reproducibility packages must work in completely fresh Docker environments without cached dependencies, manual interventions, or undocumented setup steps. This ensures true reproducibility rather than "works on my machine" artifacts.

In practice:
- Docker containers with pinned dependencies (pip freeze, conda export)
- 3 successful fresh reproductions from scratch required
- README with 5 steps max to reproduce results
- SHA256 checksums verify dataset integrity

### Principle 3: Complete Documentation Before Novel Development
No novel method development proceeds without Quality Gate 1 baseline validation. This prevents building on misunderstood foundations and ensures fair performance comparisons.

In practice:
- Baseline specification document with all hyperparameters
- Reproducibility package tested independently
- Statistical comparison report (reproduced vs published)
- Quality Gate 1 APPROVED status before method-development skill

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Skipping Baseline Replication** | Comparing novel methods to reported baseline results without replication introduces confounds (different hardware, frameworks, datasets) | Complete full baseline replication with +-1% validation before claiming improvements |
| **Ignoring Non-Determinism** | Running experiments without fixed seeds produces variance across runs, making +-1% tolerance impossible to verify | Force deterministic mode, test with 3 identical runs, document any remaining variance sources |
| **Incomplete Hyperparameter Extraction** | Missing hyperparameters like learning rate schedule or warmup steps causes silent performance gaps | Extract all 47+ hyperparameters from paper + code + supplements, contact authors for missing details |

## Conclusion

Baseline Replication provides rigorous methodology for reproducing published ML results with exact reproducibility (+-1% tolerance), establishing validated foundations for novel method development. By enforcing deterministic implementations, fresh environment testing, and complete documentation, this skill ensures baselines are understood rather than assumed.

Use this skill before developing novel methods (Deep Research SOP Pipeline D prerequisite), when validating SOTA claims, or when preparing reproducibility packages for publication. The 7-phase workflow (paper analysis, dataset validation, implementation, experiments, validation, packaging, Quality Gate 1) produces independently verified baseline implementations with statistical confidence. The result is fair performance comparisons and solid foundations for research contributions.

---