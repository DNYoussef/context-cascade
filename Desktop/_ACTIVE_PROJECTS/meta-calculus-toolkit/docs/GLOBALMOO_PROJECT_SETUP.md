# Global MOO Project Setup for Meta-Calculus

## Project Configuration

Use these settings when creating your Global MOO project:

### Project Name
```
MetaCalculus_FRW_Optimization
```

### Input Variables: 4

| # | Name | Type  | Min   | Max  | Description                    |
|---|------|-------|-------|------|--------------------------------|
| 1 | n    | Float | 0.3   | 1.5  | Expansion exponent a(t) = t^n  |
| 2 | s    | Float | -0.05 | 0.05 | Action weight (BBN bounded)    |
| 3 | k    | Float | -0.03 | 0.03 | Meta-weight (CMB bounded)      |
| 4 | w    | Float | -0.5  | 0.5  | Equation of state              |

### Output Variables: 5

| # | Name                   | Type     | Target | Description                        |
|---|------------------------|----------|--------|------------------------------------|
| 1 | chi2_total             | Minimize | 0.0    | Observational fit (BBN + CMB)      |
| 2 | neg_spectral_gap_mixed | Minimize | -1.0   | Negative spectral gap (maximize)   |
| 3 | neg_invariance_score   | Minimize | -1.0   | Negative invariance (maximize)     |
| 4 | neg_min_individual_gap | Minimize | -1.0   | Worst individual gap (maximize)    |
| 5 | fragility              | Minimize | 0.0    | Solution sensitivity               |

**Note**: Outputs 2-4 are negated because Global MOO minimizes. Negating converts maximization to minimization.

---

## Step-by-Step Setup

### 1. Create Project
- Go to app.globalmoo.com
- Click "Create Project"
- Set **Input variables**: 4
- Set input bounds as shown above
- Name: `MetaCalculus_FRW_Optimization`

### 2. Configure Outputs
After project creation, add 5 output objectives as shown above.

### 3. Generate Initial Samples

Run this to generate initial data for Global MOO:

```bash
cd C:\Users\17175\Desktop\_ACTIVE_PROJECTS\meta-calculus-toolkit
python -m meta_calculus.moo_integration export-template > globalmoo_config.json
```

This creates 15 evaluated sample points to initialize the surrogate model.

### 4. Upload Initial Samples

From the exported JSON, extract the `initial_samples.samples` array and upload to Global MOO.

---

## Evaluation Function

When Global MOO requests an evaluation, use this Python code:

```python
from meta_calculus.moo_integration import PhysicsOracle

oracle = PhysicsOracle(n_solutions=30, sigma=0.5)

def evaluate_for_globalmoo(n, s, k, w):
    """Evaluate parameters for Global MOO API."""
    result = oracle.evaluate(n, s, k, w, compute_fragility=False)

    if not result['feasible']:
        # Return penalty values for infeasible points
        return [1000.0, 0.0, 0.0, 0.0, 100.0]

    obj = result['objectives']
    return [
        obj['chi2_total'],
        obj['neg_spectral_gap_mixed'],
        obj['neg_invariance_score'],
        obj['neg_min_individual_gap'],
        obj['fragility'],
    ]

# Example usage
outputs = evaluate_for_globalmoo(0.67, 0.0, 0.0, 0.0)
print(outputs)
# [0.0, -0.999999, -1.0, -0.96, 0.0]
```

---

## Using the Colab Notebook

The Colab notebook at: https://colab.research.google.com/drive/1uM7fAx2mMEj_hBAejnGCBenup_KdLIrK

Can be used to:
1. Install the meta-calculus toolkit
2. Run evaluations in the cloud
3. Submit results back to Global MOO

### Colab Setup Code

```python
# Install meta-calculus
!git clone https://github.com/meta-calculus/meta-calculus.git
%cd meta-calculus
!pip install -e .

# Install pymoo as backup
!pip install pymoo

# Test the physics oracle
from meta_calculus.moo_integration import PhysicsOracle, GlobalMOOAdapter

oracle = PhysicsOracle()
adapter = GlobalMOOAdapter(oracle)

# Generate sample data
samples = adapter.export_sample_data(n_samples=20)
print(f"Generated {samples['n_samples']} samples")

# Show configuration
config = adapter.generate_api_config()
print(json.dumps(config, indent=2))
```

---

## Constraints (Auto-Enforced)

The tight bounds ensure >90% of samples are feasible:

| Constraint | Expression   | Reason           |
|------------|--------------|------------------|
| BBN bound  | |s| <= 0.05  | Nucleosynthesis  |
| CMB bound  | |k| <= 0.03  | Cosmic microwave |
| Energy     | -1 <= w <= 1 | Physical         |
| Expansion  | n >= 0       | Physical         |

---

## Expected Results

Based on pymoo optimization (40 generations, pop=40):

**Best Observational Fit**:
- n=0.486, s=-0.009, k=0.0, w=0.249
- chi2 = 8.76e-11 (excellent)

**Best Structure Clarity**:
- n=0.481, s=-0.038, k=-0.015, w=0.199
- spectral_gap = 0.99999996

**Sweet Spot** (balanced):
- n ~ 0.49, s ~ -0.001, k ~ 0, w ~ 0.25
- All objectives near optimal

---

## API Key

Your API key is configured in the code:
```
gq8bbjzNZzJPsDaEzB4YWqzJKvSst2H7rL9R6JHfsUYm9Arc
```

Make sure this matches what's shown in your Global MOO account settings.

---

## Troubleshooting

### "API connection failed"
- Verify the API endpoint URL (check Global MOO docs)
- Ensure API key is active
- Check network/firewall settings

### "No feasible solutions"
- Bounds may be too tight
- Try widening s and k ranges slightly

### "Optimizer stuck"
- Increase number of initial samples
- Try different random seed
- Use pymoo as fallback

---

## Contact

For Global MOO support: https://globalmoo.com/support/
For meta-calculus issues: https://github.com/meta-calculus/meta-calculus/issues
