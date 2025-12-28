# Physics Simulation Creator - Quick Reference

## TL;DR: Optimize Physics Simulations

**Use NNC (k != 0) when:**
- Singularities present (1/r, 1/r^2, etc.) - **ALWAYS**
- Length scale < 1e-6 m - **10%+ accuracy gain**
- **Need fewer steps** - 7-100x reduction for large sims on consumer hardware
- Ultra-high precision needed

**Use classical (k = 0) when:**
- Smooth problem at human scale AND speed not critical
- Engineering tolerance adequate AND not hardware-constrained

---

## Step 1: Get Optimal k (ALWAYS DO THIS)

```bash
python ai_simulation_helper.py --length-scale YOUR_SCALE --json
```

Or if you know the problem type:
```bash
python ai_simulation_helper.py --problem "YOUR PROBLEM" --json
```

---

## Step 2: Check Output

**Smooth problem** (no singularity):
```json
{"k": 0.2963, "has_singularity": false}
```
Still use k=0.30, NOT k=0!

**Singular problem**:
```json
{"k": -1.0, "has_singularity": true, "singularity_type": "1/r"}
```
Use k=-1.0 to handle singularity.

---

## k-Value Quick Lookup

| Scale | k | Accuracy Gain | Step Reduction | Use NNC? |
|-------|---|---------------|----------------|----------|
| Planck (1e-35 m) | 0.64 | 50%+ | 50-100x | **YES** |
| Atomic (1e-10 m) | 0.30 | 15-30% | 7-22x | **YES** |
| Micro (1e-6 m) | 0.24 | 10-20% | 5-10x | YES (large sims) |
| Human (1 m) | 0.16 | <5% | 1.5-3x | NO (unless need speed) |
| Solar (1e11 m) | 0.01 | <1% | ~1x | NO |
| Galactic (1e21 m) | -0.13 | <5% | ~1x | NO |

| Singularity | k | Accuracy Gain | Override scale k? |
|-------------|---|---------------|-------------------|
| 1/r | -1.0 | 1000-40,000x | **YES - always** |
| 1/r^2 | -2.0 | 1000-40,000x | **YES - always** |
| 1/sqrt(r) | -0.5 | 100-1000x | **YES - always** |

---

## Core Formula

```
k = -0.0137 * log10(L) + 0.1593
```

Where L = length scale in meters.

---

## Decision Tree

```
START: Physics Simulation
  |
  v
[Get length scale L]
  |
  v
[Run CLI: --length-scale L --json]
  |
  v
[Check output: has_singularity?]
  |
  +-- NO --> Use k from output (often != 0)
  |
  +-- YES --> Use singularity-based k
              (overrides length-scale k)
```

---

## Key Mindset

| Situation | Recommendation |
|-----------|----------------|
| Has singularity | **Always use NNC** (k from singularity type) |
| L < 1e-6 m, no singularity | **Use NNC** (k from scale, gains > 10%) |
| Human scale, smooth | **k=0 usually fine** (gains < 5%) |
| Ultra-high precision | **Use NNC** even if smooth |

---

## Code Template

```python
k = 0.30  # From CLI - NOT hardcoded 0!

def nnc_forward(x, k=k):
    return np.sign(x) * np.power(np.abs(x) + 1e-10, 1.0 - k)

def nnc_inverse(y, k=k):
    return np.sign(y) * np.power(np.abs(y) + 1e-10, 1.0 / (1.0 - k))
```

---

## Validation Checklist

- [ ] Ran CLI script (even for smooth problems)
- [ ] Got k value from output
- [ ] Compared accuracy vs k=0 baseline
- [ ] Documented improvement metrics
