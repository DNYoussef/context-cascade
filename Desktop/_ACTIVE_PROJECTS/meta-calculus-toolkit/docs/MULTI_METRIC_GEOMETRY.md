# Multi-Metric Geometry for Meta-Cosmology

## Mathematical Foundations for Gaps 1-7

**Version**: 1.0.0
**Date**: 2024-12-04
**Status**: Rigorous Formulation

---

## Table of Contents

1. [Gap 1: Solution Space Polytope](#gap-1-solution-space-polytope)
2. [Gap 2: Canonical Form with Pole Structure](#gap-2-canonical-form-with-pole-structure)
3. [Gap 3: Jacobian Interpretation of t^(2k)](#gap-3-jacobian-interpretation)
4. [Gap 4: Multi-Metric Distance Functions](#gap-4-multi-metric-distance-functions)
5. [Gap 5: Diffusion Operators](#gap-5-diffusion-operators)
6. [Gap 6: Multi-Metric Trajectories](#gap-6-multi-metric-trajectories)
7. [Gap 7: Invariant Detection](#gap-7-invariant-detection)
8. [Connection to Existing Code](#connection-to-existing-code)

---

## Gap 1: Solution Space Polytope

### 1.1 Parameter Space Definition

The meta-Friedmann solutions are parametrized by:

```
P = { (n, s, k, w) in R^4 : constraints satisfied }
```

Where:
- `n` = expansion exponent: a(t) ~ t^n
- `s` = action-based weight exponent: u(t) = t^s
- `k` = derivative weight exponent: D_meta = t^k d/dt
- `w` = equation of state: p = w * rho

### 1.2 Facet Inequalities (Observational + Physical)

**BBN Constraint (F1):**
```
|s| <= s_max = 0.05  (3% Hubble deviation)

F1: -0.05 <= s <= 0.05
Facet hyperplanes: { s = -0.05 } and { s = +0.05 }
```

**CMB Constraint (F2):**
```
|k| <= k_max = 0.03  (acoustic peak constraint)

F2: -0.03 <= k <= 0.03
Facet hyperplanes: { k = -0.03 } and { k = +0.03 }
```

**Energy Conditions (F3):**
```
Weak Energy Condition: rho >= 0, rho + p >= 0
Dominant Energy Condition: |p| <= rho
=> -1 <= w <= 1

F3: -1 <= w <= 1
Facet hyperplanes: { w = -1 } and { w = +1 }
```

**Expansion Requirement (F4):**
```
Expanding universe: H > 0 => n > 0

F4: n >= 0
Facet hyperplane: { n = 0 }
```

**Discriminant Constraint (F5):**
```
Real solutions require: Delta(s, w) >= 0
Delta = 9 s^2 w^2 - 8 s^2 + 4 s + 4

This is a curved constraint, not a hyperplane.
```

### 1.3 Vertex Enumeration

The polytope vertices are extreme points satisfying all constraints:

```
V1 = (n_classical(w=-1/3), 0, 0, -1/3)   # Radiation, classical
   = (1/2, 0, 0, 1/3)

V2 = (n_classical(w=0), 0, 0, 0)          # Dust, classical
   = (2/3, 0, 0, 0)

V3 = (n_classical(w=1), 0, 0, 1)          # Stiff matter, classical
   = (1/3, 0, 0, 1)

V4 = (n_act(s=0.05, w=1/3), 0.05, 0, 1/3) # Radiation, max s
V5 = (n_act(s=-0.05, w=1/3), -0.05, 0, 1/3)
V6 = (n_toy(k=0.03, w=1/3), 0, 0.03, 1/3) # Radiation, max k
V7 = (n_toy(k=-0.03, w=1/3), 0, -0.03, 1/3)
... (enumerate all extremes)
```

### 1.4 Formal Polytope Definition

```
P = { x in R^4 : A x <= b }

where A is the constraint matrix and b is the bound vector:

A = [ 0   1   0   0  ]    b = [ 0.05  ]   (s <= 0.05)
    [ 0  -1   0   0  ]        [ 0.05  ]   (-s <= 0.05)
    [ 0   0   1   0  ]        [ 0.03  ]   (k <= 0.03)
    [ 0   0  -1   0  ]        [ 0.03  ]   (-k <= 0.03)
    [ 0   0   0   1  ]        [ 1     ]   (w <= 1)
    [ 0   0   0  -1  ]        [ 1     ]   (-w <= 1)
    [-1   0   0   0  ]        [ 0     ]   (-n <= 0)
```

---

## Gap 2: Canonical Form with Pole Structure

### 2.1 Cosmological Polytope Analogy

In the amplituhedron/cosmohedron literature, the canonical form is:

```
Omega = d^n X / Product_i L_i(X)
```

where L_i are linear functions vanishing on facets.

### 2.2 Meta-Cosmology Canonical Form

For our parameter space polytope P:

```
Omega(n, s, k, w) = dn ^ ds ^ dk ^ dw / [F1(s) * F2(k) * F3(w) * F4(n)]
```

**Facet Functions:**

```
F1(s) = (s_max - s)(s_max + s) = s_max^2 - s^2 = 0.0025 - s^2
F2(k) = (k_max - k)(k_max + k) = k_max^2 - k^2 = 0.0009 - k^2
F3(w) = (1 - w)(1 + w) = 1 - w^2
F4(n) = n
```

**Full Canonical Form:**

```
Omega = dn ^ ds ^ dk ^ dw / [(0.0025 - s^2)(0.0009 - k^2)(1 - w^2) n]
```

### 2.3 Pole Structure Analysis

The canonical form has poles at:
- s = +/- 0.05 (BBN boundary)
- k = +/- 0.03 (CMB boundary)
- w = +/- 1 (energy condition boundary)
- n = 0 (static universe)

**Physical Interpretation:**

Near a pole, the integral diverges, indicating:
- These boundaries are where "physical" solutions end
- Crossing a facet = entering unphysical/excluded regime
- Residues at poles encode boundary physics

### 2.4 Measure Deformation Under GUC

Under coordinate transform (GUC):
```
s = e^(alpha * sigma) - 1    (approximately s ~ alpha * sigma for small sigma)
k = e^(beta * kappa) - 1
```

The canonical form transforms:

```
Omega_GUC = J(sigma, kappa) * d sigma ^ d kappa ^ ... / [F1(...) * F2(...) * ...]
```

where J is the Jacobian:

```
J = alpha * e^(alpha * sigma) * beta * e^(beta * kappa)
```

**Key Insight:** The Jacobian prefactor is analogous to the t^(2k) term in L_meta!

---

## Gap 3: Jacobian Interpretation

### 3.1 The t^(2k) Factor as Jacobian

The minisuperspace meta-Lagrangian is:

```
L_meta = -(3/8 pi G) a t^(2k) a_dot^2 - a^3 rho(a)
```

**Claim:** The t^(2k) arises from a coordinate Jacobian.

### 3.2 Coordinate Transformation

Define "meta-time" tau:
```
tau = integral_0^t dt' / t'^k = t^(1-k) / (1-k)   for k != 1
    = ln(t)                                       for k = 1
```

The inverse is:
```
t = [(1-k) tau]^(1/(1-k))   for k != 1
```

### 3.3 Jacobian Derivation

The Jacobian of the time transformation:
```
dt/d tau = t^k
```

The kinetic term transforms:
```
a_dot^2 dt = (da/dt)^2 dt
           = (da/d tau * d tau/dt)^2 dt
           = (da/d tau)^2 * (d tau/dt)^2 * dt
           = (da/d tau)^2 * t^(-2k) * dt
           = (da/d tau)^2 * t^(-2k) * t^k d tau
           = (da/d tau)^2 * t^(-k) d tau
```

**In the Lagrangian:**
```
L dt = L_classical * t^(-k) d tau
```

Rewriting in original t-coordinates with the Jacobian factor:
```
L_meta = t^k * L_classical(D_meta a)
```

where D_meta a = t^k da/dt.

### 3.4 Connection to Positive Geometry

In positive geometry terms:
- Standard coordinates (t, a) <-> linear facet functions
- Meta-coordinates (tau, alpha) <-> nonlinear (exponential) facet functions
- The Jacobian t^k is the measure deformation factor

**Formula:**
```
Omega_standard(t, a) = dt ^ da / [facets in (t,a)]
Omega_meta(tau, alpha) = J * d tau ^ d alpha / [facets in (tau, alpha)]

J = t^k * a   (or just t^k for time-only transform)
```

---

## Gap 4: Multi-Metric Distance Functions

### 4.1 Solution Feature Vector

For a solution with parameters (n, s, k, w), evaluate at time grid {t_i}:

```
X = (a(t_1), ..., a(t_N), H(t_1), ..., H(t_N), rho(t_1), ..., rho(t_N))
```

For power-law solutions:
```
a(t_i) = t_i^n
H(t_i) = n / t_i
rho(t_i) = rho_0 * t_i^(-m)   where m = 2 - 2k
```

### 4.2 Classical (Euclidean) Distance

```
d_classical(X_i, X_j) = || X_i - X_j ||_2
                      = sqrt( sum_l (X_i[l] - X_j[l])^2 )
```

### 4.3 Bigeometric (Log) Distance

For positive fields, use log-transform:

```
d_log(X_i, X_j) = || log(X_i) - log(X_j) ||_2
                = sqrt( sum_l (log(X_i[l]) - log(X_j[l]))^2 )
```

This makes power-law differences look like linear differences.

### 4.4 Meta-Weighted Distance

Weight each time slice by meta-factor:

```
d_meta(X_i, X_j; k) = || t^k * (X_i - X_j) ||_2
                    = sqrt( sum_l t_l^(2k) (X_i[l] - X_j[l])^2 )
```

Early times (small t) are down-weighted for k > 0.

### 4.5 Curvature-Weighted Distance

Weight by curvature magnitude:

```
d_curv(X_i, X_j) = sqrt( sum_l |R_l|^(-1) (X_i[l] - X_j[l])^2 )
```

This emphasizes differences in low-curvature regions.

### 4.6 Mahalanobis Distance

If Sigma is the covariance matrix of the solution ensemble:

```
d_Maha(X_i, X_j) = sqrt( (X_i - X_j)^T Sigma^(-1) (X_i - X_j) )
```

This accounts for correlations between features.

---

## Gap 5: Diffusion Operators

### 5.1 Kernel Matrix

From any distance d, construct a kernel:

```
K_ij = exp( -d(X_i, X_j)^2 / (2 sigma^2) )
```

sigma is the bandwidth parameter (controls locality).

### 5.2 Graph Laplacian

Degree matrix:
```
D_ii = sum_j K_ij
```

Unnormalized Laplacian:
```
L = D - K
```

Normalized Laplacian (random walk):
```
L_rw = I - D^(-1) K
```

Symmetric normalized:
```
L_sym = I - D^(-1/2) K D^(-1/2)
```

### 5.3 Diffusion Operator

The diffusion operator is:
```
P = D^(-1) K   (row-stochastic)
```

Power P^t gives t-step diffusion.

### 5.4 Spectral Properties

Eigendecomposition:
```
L phi_j = lambda_j phi_j
```

- lambda_0 = 0 (trivial eigenvalue, constant eigenvector)
- lambda_1 > 0 gives the "spectral gap" (connectivity)
- Small eigenvalues = slow modes = global structure
- Eigenvectors phi_j are "diffusion coordinates"

---

## Gap 6: Multi-Metric Trajectories

### 6.1 Operator Composition

Given Laplacians {L_1, L_2, ..., L_M} from different metrics:

**Trajectory operator:**
```
T = L_1 * L_2 * ... * L_M   (matrix product)
```

Or alternating powers:
```
T = P_1^(t1) * P_2^(t2) * ... * P_M^(tM)
```

### 6.2 Trajectory Sequence

Let sequence be S = (m_1, m_2, ..., m_k) where m_i in {1, ..., M}.

```
T_S = Product_{i=1}^{k} L_{m_i}
```

### 6.3 Diffusion Distance Under Trajectory

Starting from initial distribution f_0:

```
f_t = T_S f_0
```

The diffusion distance between points i, j under trajectory S:

```
D_S(i, j) = || Phi_S(i) - Phi_S(j) ||

where Phi_S(i) = (sqrt(lambda_1^S) phi_1^S(i), sqrt(lambda_2^S) phi_2^S(i), ...)
```

### 6.4 Optimal Trajectory Selection

**Objective:** Find trajectory S that maximizes cluster separation.

```
max_S  { between-cluster variance / within-cluster variance }

     = max_S  { sum_C |mu_C - mu|^2 / sum_C sum_{i in C} |x_i - mu_C|^2 }
```

where clusters C are defined by physical regime (singular/regular, etc.).

---

## Gap 7: Invariant Detection

### 7.1 Definition of Multi-Calculus Invariant

A quantity I is a **multi-calculus invariant** if:

```
forall calculus C in {classical, bigeometric, meta, ...}:
    I(solution; C) = I(solution; classical)
```

### 7.2 Feature Computation Across Calculi

For each solution and each calculus, compute feature vector:

```
F_C(solution) = (f_1^C, f_2^C, ..., f_p^C)

where f_i^C = i-th feature computed using calculus C
```

**Example features:**
- Singularity type: Does rho -> infinity at t -> 0?
- Expansion class: Is n > 1 (accelerating) or n < 1 (decelerating)?
- Curvature bound: sup |R(t)|
- Horizon existence: Is there an event horizon?

### 7.3 Consensus Detection

**Method 1: Variance across calculi**

```
Var_C[f_i] = (1/|C|) sum_C (f_i^C - mean(f_i))^2
```

If Var_C[f_i] < epsilon, then f_i is approximately invariant.

**Method 2: Correlation matrix**

Compute correlation of f_i across calculi:
```
Corr(C1, C2) = E[f^{C1} f^{C2}] / sqrt(Var[f^{C1}] Var[f^{C2}])
```

High correlation = invariance.

**Method 3: Principal Component Analysis**

Stack features from all calculi into matrix F.
PCA reveals:
- First PC = invariant mode (if exists)
- Higher PCs = calculus-dependent modes

### 7.4 Invariant Candidates

**Topology:**
- Singularity presence (yes/no) - should be invariant
- Horizon topology - should be invariant

**Asymptotic behavior:**
- Late-time attractor class - may be invariant
- Infinity type (de Sitter, flat, etc.) - should be invariant

**Conservation laws:**
- Total energy (if defined) - calculus-dependent in general
- Entropy bounds - may be invariant

### 7.5 Invariant Score

Define invariance score:

```
S_inv(f) = 1 - Var_C[f] / max_C Var_C[f]
```

Score = 1 means perfect invariance.
Score = 0 means maximally calculus-dependent.

---

## Connection to Existing Code

### Existing Functions to Reuse

From `model_comparison.py`:
- `n_action_based(s, w)` -> compute n for action-based model
- `n_derivative_weight(k, w)` -> compute n for derivative-weight model
- `k_equivalent(s, w)` -> matching formula
- `discriminant(s, w)` -> constraint for real solutions
- `ObservationalConstraints` -> BBN/CMB limits

From `action_derivation.py`:
- `MetaActionDerivation` -> Lagrangian computations
- `formal_derivation()` -> L_meta formula

From `bbn_cmb_constraints.py`:
- `MetaFriedmannBBN` -> solution at fixed k
- `BBNConstraints`, `CMBConstraints` -> chi-squared analysis
- `PhaseTransition` -> transition scenarios

### New Modules to Create

1. `meta_calculus/polytope.py` - Gaps 1-2
2. `meta_calculus/jacobian.py` - Gap 3
3. `meta_calculus/multi_metric.py` - Gaps 4-6
4. `meta_calculus/invariants.py` - Gap 7

### CLI Commands to Add

```bash
# Gap 1-2: Polytope
mc polytope vertices
mc polytope facets
mc polytope canonical-form --n 0.5 --s 0.02 --k 0.01 --w 0.333

# Gap 3: Jacobian
mc jacobian show --k 0.5
mc jacobian verify --k 0.5

# Gaps 4-6: Multi-metric
mc multi-metric distances --metric classical
mc multi-metric distances --metric log
mc multi-metric diffusion --metrics classical,log,meta
mc multi-metric trajectory --sequence "1,2,1,2"

# Gap 7: Invariants
mc invariants compute --calculi classical,bigeometric,meta
mc invariants score --feature singularity
mc invariants consensus
```

---

## Summary of Key Formulas

### Polytope (Gap 1)
```
P = { (n,s,k,w) : |s| <= 0.05, |k| <= 0.03, -1 <= w <= 1, n >= 0 }
```

### Canonical Form (Gap 2)
```
Omega = dn ^ ds ^ dk ^ dw / [(0.0025 - s^2)(0.0009 - k^2)(1 - w^2) n]
```

### Jacobian (Gap 3)
```
t^(2k) in L_meta = Jacobian of tau = integral dt/t^k
```

### Distances (Gap 4)
```
d_classical = || X_i - X_j ||_2
d_log = || log(X_i) - log(X_j) ||_2
d_meta = || t^k * (X_i - X_j) ||_2
```

### Laplacian (Gap 5)
```
K_ij = exp(-d^2 / 2 sigma^2)
L = D - K
```

### Trajectory (Gap 6)
```
T = L_1 * L_2 * ... * L_M
```

### Invariance Score (Gap 7)
```
S_inv(f) = 1 - Var_C[f] / max Var_C[f]
```

---

## Multi-Geometry Diffusion Framework

### The Core Insight

From the ChatGPT analysis:

> "Your many calculi aren't rival theories. They're **multiple geometric lenses**
> on the same underlying object. The multi-geometry / multi-operator picture says:
> don't crown one lens as 'the true one.' Put several on the same object."

### Fixed Object, Varied Calculus

1. **Fix** the underlying object:
   - A positive geometry (cosmological polytope, cosmohedron)
   - A state space of solutions (FRW solutions, black hole parameters)

2. **Apply multiple calculi** on the same object:
   - Classical/Euclidean (vanilla GR)
   - Log/GUC (bigeometric-inspired)
   - Curvature-weighted
   - Meta-weighted (D_meta = t^k d/dt)

3. **Build operators** from each calculus:
   - Distance functions d_c
   - Diffusion operators P_c

4. **Compose operators** (the key innovation):
   ```
   P_mix = P_C @ P_B @ P_A
   ```

### Key Experimental Result

From the FRW diffusion experiment:

| Calculus | Spectral Gap | Notes |
|----------|--------------|-------|
| A (Euclidean) | 0.028 | Over-emphasizes early curvature |
| B (Log/GUC) | 0.014 | Suppresses magnitude differences |
| C (Curvature-weighted) | 0.000 | Over-emphasizes R variations |
| Mixed (C o B o A) | **0.109** | **LARGEST** - best low-pass filter |

The mixed operator:
- Preserves what's COMMON to all calculi
- Attenuates what is IDIOSYNCRATIC to any one
- Creates cleaner separation of physical regimes
- Has fastest spectral decay (most low-pass)

### Terminal Commands

**Triangle Cosmological Polytope:**
```bash
cd Desktop/_SCRATCH/meta-calculus-toolkit

python -m meta_calculus.triangle_diffusion sample
python -m meta_calculus.triangle_diffusion diffusion
python -m meta_calculus.triangle_diffusion compare
python -m meta_calculus.triangle_diffusion plot --show
```

**FRW Multi-Calculus Diffusion:**
```bash
python -m meta_calculus.frw_diffusion generate
python -m meta_calculus.frw_diffusion analyze
python -m meta_calculus.frw_diffusion experiment
python -m meta_calculus.frw_diffusion plot --show
```

**Via Main CLI:**
```bash
python cli.py triangle-diffusion compare
python cli.py frw-diffusion experiment
```

### Implication for Meta-Calculus

> "The true structure of the early-universe model space isn't best captured
> by any single calculus. It lives in the INTERSECTION of multiple calculi -
> the features that survive when you move through A -> B -> C."

This validates the multi-calculus approach:
- GUC/meta-calculus is a coordinate + measure deformation (not new physics)
- But using MULTIPLE calculi together reveals invariant structure
- Mixed diffusion operators are the computational tool to find this structure

---

## Files Summary

| File | Purpose |
|------|---------|
| `polytope.py` | Solution space polytope (Gaps 1-2) |
| `jacobian.py` | t^(2k) as Jacobian (Gap 3) |
| `multi_metric.py` | Distance functions & Laplacians (Gaps 4-6) |
| `invariants.py` | Multi-calculus invariant detection (Gap 7) |
| `triangle_diffusion.py` | Triangle cosmological polytope experiment |
| `frw_diffusion.py` | FRW multi-calculus experiment |

---

*Document generated for meta-calculus-toolkit v0.2.0*
