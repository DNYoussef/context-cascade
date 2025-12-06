# Scheme-Invariance Framework: A Meta-Theory of Physics

## Executive Summary

Physical laws are not equations in a specific mathematical language.
Physical laws are **equivalence classes** of models under scheme transformations.

What survives under G_scheme is physics. What changes is scaffolding.

---

## Critical Distinction: Ontic vs Epistemic Layers

This framework is structured in TWO LAYERS that must never be confused:

### LAYER 1 (ONTIC - The World)

This layer captures **what exists** independently of how we describe it:

1. **Least Action Principle**: Physical trajectories satisfy delta S[q;s] = 0
2. **Scheme Invariance**: Physical observables satisfy O(q,s) = O(g.q, g.s) for all g in G_scheme

Quantities that are scheme-invariant are **REAL** (ontic). They exist regardless of
our mathematical description.

### LAYER 2 (EPISTEMIC - Our Descriptions)

This layer captures **how we choose to describe** physical reality:

1. **Information Parsimony**: Among equivalent schemes, prefer argmin I[s]
2. **Coding Conventions**: Complexity depends on programming language, numerical stack

Quantities in Layer 2 are **PRAGMATIC** (epistemic). They are human choices for
convenience, NOT statements about reality.

**CRITICAL RULE**: Layer 2 is used ONLY AFTER Layer 1 establishes physical equivalence.
Never use information criteria to determine physical content!

---

## 1. The Two-Axis Scheme Space

### 1.1 Definition

A **scheme** is a pair s = (A, C) where:

- **A-scheme (Algebra)**: Choice of number system and representation
- **C-scheme (Calculus)**: Choice of differential/evolution structure

### 1.2 A-Scheme Examples

| A-Scheme | State Space | Composition | Example |
|----------|-------------|-------------|---------|
| A1: Complex QT | C^n | Kronecker tensor_K | Standard QM |
| A2: Real NQT | R^{2n} (Gamma embedding) | tensor_r | Hoffreumon-Woods 2025 |
| A3: Kahler | Real symplectic manifold | Kahler structure | Geometric QM |
| A4: Quaternionic | H^n | Quaternionic tensor | Extended QM |

### 1.3 C-Scheme Examples

| C-Scheme | Derivative | Domain | Example |
|----------|------------|--------|---------|
| C1: Classical | d/dt | Standard analysis | Newton, Schrodinger |
| C2: Meta-time | D_meta = (v/u) * d/dt | Weighted evolution | Meta-calculus |
| C3: Bigeometric | D_BG = exp(x*f'/f) | Scale-invariant | Power-law singularities |
| C4: Multi-operator | Alternating L_1, L_2, ... | Diffusion bundles | N01ne intelligence |

---

## 2. The Scheme Groupoid G_scheme

### 2.1 Definition

G_scheme is a **groupoid** (not arbitrary transformations!) of **admissible** morphisms
between schemes:

```
g: (q, s) --> (q', s')
```

where q' is the description of the same physical situation in scheme s'.

### 2.2 The Five Admissibility Axioms

A transformation g is IN G_scheme iff it satisfies ALL of:

| Axiom | Requirement | Why It Matters |
|-------|-------------|----------------|
| **preserves_spectrum** | Eigenvalues of observables unchanged | Physical measurements are eigenvalues |
| **preserves_expectations** | <psi\|O\|psi>_s = <g.psi\|g.O\|g.psi>_{g.s} | Probabilities must agree |
| **is_local** | No nonlocal functional dependence | Causality preservation |
| **is_invertible** | Bijective transformation | Can always go back |
| **is_smooth** | Differentiable in relevant domain | Well-defined calculus |

If a transformation FAILS any axiom, it is NOT in G_scheme. Period.

**Key Insight**: This prevents trivialization. Not "anything goes" - only tame,
physically sensible transformations count.

### 2.3 The Pullback Theorem for C-Schemes

For meta-derivatives D_meta f(t) = u(t)f'(t) + v(t)f(t):

**Theorem**: When u(t) > 0 and smooth throughout the domain, define:

```
tau(t) = integral_0^t u(s) ds
```

Then D_meta is **equivalent** to the standard derivative d/dtau under this
coordinate reparametrization.

**Corollary**: Admissible C-schemes are EXACTLY those obtainable from standard
calculus via smooth, invertible coordinate transformations.

**Implication**: If u(t) vanishes or goes negative, the meta-derivative is
NOT ADMISSIBLE. It either represents new physics or an invalid artifact.

### 2.4 A-Scheme Transformations

| Transformation | Maps | Preserves |
|----------------|------|-----------|
| Gamma map | C-Hilbert --> R-SY_n | Eigenvalues, probabilities |
| Inverse Gamma | R-SY_n --> C-Hilbert | All observables |
| tensor_K <--> tensor_r | Kronecker <--> RNQT | Multipartite correlations |
| Kahler embedding | C^n --> Real Kahler | Symplectic structure |

### 2.5 C-Scheme Transformations

| Transformation | Maps | Preserves (in regime) |
|----------------|------|----------------------|
| Classical <--> Meta | d/dt <--> D_meta | Observables when u(t) ~ constant |
| Classical <--> Bigeometric | d/dt <--> D_BG | Power-law behavior |
| Metric swap | Euclidean <--> Log | Diffusion fixed points |

### 2.6 Composition Rules

G_scheme forms a groupoid (not group) because:
- Not all transformations are composable
- Some have restricted domains
- Inverses exist within domains

---

## 3. The Invariance Principle

### 3.1 Formal Statement

**Definition**: An observable O is **scheme-robust** iff:

```
O(q_phys, s) = O(g . q_phys, g . s)
```

for all allowed g in G_scheme, where q_phys satisfies delta S[q; s] = 0.

### 3.2 The Meta-Invariance Principle

> **Physical content = scheme-robust observables.**
> **Mathematical scaffolding = scheme-dependent features.**

### 3.3 Domain-Specific Invariants

#### FRW Cosmology

| Scheme-Robust (Physical) | Scheme-Dependent (Scaffolding) |
|--------------------------|--------------------------------|
| H(z) Hubble parameter | Coordinate time t |
| BBN abundances | Friedmann equation form |
| CMB distance measures | Singularity at t=0 (maybe) |
| Dark energy density | Calculus used |

#### Quantum Mechanics

| Scheme-Robust (Physical) | Scheme-Dependent (Scaffolding) |
|--------------------------|--------------------------------|
| Probabilities (real) | Complex amplitudes |
| Interference patterns | Literal i symbol |
| Entanglement correlations | Hilbert space dimension |
| Observable spectra | Tensor product choice |
| Unitarity | Phase conventions |

#### Scattering Amplitudes

| Scheme-Robust (Physical) | Scheme-Dependent (Scaffolding) |
|--------------------------|--------------------------------|
| Factorization on poles | Loop integral representation |
| Soft/collinear limits | Regularization scheme |
| Positivity constraints | Feynman diagram sum |
| Locality/causality | Specific coordinates |

---

## 4. The Three-Layer Structure

### 4.1 Layer 1: Dynamical Stationarity (Least Action)

For fixed scheme s, physical trajectories satisfy:

```
delta S[q; s] = 0
```

This is the standard variational principle on configuration space Q.

### 4.2 Layer 2: Scheme Invariance

Among all schemes in S, physical observables satisfy:

```
O(q, s) = O(g.q, g.s) for all g in G_scheme
```

This identifies the physically meaningful quantities.

### 4.3 Layer 3: Information Parsimony

Among equivalent schemes [s] = {g.s : g in G_scheme}, prefer:

```
argmin I[s] subject to A[s] = 0
```

where:
- A[s] = action/misfit term (prediction quality)
- I[s] = information/complexity term (MDL, entropy)

This is NOT physics but EPISTEMOLOGY: how we choose representations.

### 4.4 Unified Principle

```
Physical law = {
  Dynamics: delta S[q;s] = 0 on Q,
  Invariance: O fixed under G_scheme on S,
  Selection: Pareto-optimal I[s] among equivalent schemes
}
```

---

## 5. Anomalies as G_scheme Obstructions

### 5.1 The Anomaly Connection

In QFT, **anomalies** arise when:
1. You try to make a symmetry transformation on fields
2. Classically, the action is invariant
3. BUT: The path integral measure picks up a nontrivial Jacobian

In our language:
1. You WANT g: s -> s' to be in G_scheme (the transformation looks admissible)
2. BUT: The quantum theory says NO - the measure isn't invariant
3. THEREFORE: g is NOT in G_scheme; the transformation is **obstructed**

**Key Insight**: Anomalies ARE cohomological obstructions to extending scheme
transformations from classical to quantum.

### 5.2 Classification of Obstructions

| Type | Classical | Quantum | Status |
|------|-----------|---------|--------|
| **No Obstruction** | Invariant | Invariant | g is in G_scheme |
| **Quantum Anomaly** | Invariant | NOT Invariant | g obstructed by measure |
| **Classical Breaking** | NOT Invariant | N/A | g not even classical morphism |
| **Explicit Breaking** | Invariant | Small violation | Approximate symmetry |

### 5.3 Implications for Scheme-Robustness

When we test scheme-robustness and find BREAKING, we ask:
1. Is this a quantum anomaly? (measure obstruction)
2. Is this new physics? (real physical effect)
3. Is this an invalid scheme? (mathematical artifact)

The framework provides a unified language for all three cases.

---

## 6. Where New Physics Lives

### 6.1 The Key Insight

If two descriptions are exactly equivalent under G_scheme transformations,
there is NO new physics in choosing between them.

**New physics lives where scheme-robustness BREAKS.**

### 6.2 Search Strategy

Use GlobalMOO and multi-operator diffusion to hunt for:

1. **Regimes where FRW with different calculi give incompatible predictions**
   - Near Big Bang singularity
   - During inflation
   - At Planck density

2. **Quantum scenarios where RNQT and CQT diverge**
   - With additional meta-constraints
   - At Planck-scale discreteness
   - With VE-based cutoffs

3. **Amplitude boundaries where positive geometries break**
   - Non-planar limits
   - Massive external states
   - Gravitational corrections

### 6.3 Detection Methodology

```python
def detect_scheme_breaking(observable, schemes, regime):
    """
    Test if observable is scheme-robust in given regime.

    Returns:
        (is_robust, max_deviation, breaking_point)
    """
    predictions = {}
    for s in schemes:
        q_phys = solve_dynamics(s, regime)
        predictions[s] = compute_observable(observable, q_phys, s)

    deviations = pairwise_differences(predictions)
    max_dev = max(deviations)

    if max_dev > tolerance:
        breaking_point = find_where_deviation_peaks(predictions)
        return (False, max_dev, breaking_point)
    else:
        return (True, max_dev, None)
```

---

## 7. Connection to GlobalMOO

### 7.1 GlobalMOO as Scheme-Space Explorer

GlobalMOO is solving:

```
minimize (A[s], I[s]) over s in S
```

where:
- A[s] = misfit to data or reference theory
- I[s] = complexity/description-length of scheme

### 7.2 Pareto Interpretation

- All schemes on A=0 contour are physically equivalent
- Pareto front along that contour = "best" representations
- Complex QM beats RNQT on I[s] (simpler) with same A[s] (equivalent)

### 7.3 Implementation

```python
class SchemeSpaceOptimizer:
    """
    Multi-objective optimizer for scheme selection.
    """
    def __init__(self, schemes, observables, data):
        self.schemes = schemes
        self.observables = observables
        self.data = data

    def action_functional(self, scheme):
        """Misfit between predictions and data."""
        preds = self.predict(scheme)
        return divergence(preds, self.data)

    def info_functional(self, scheme):
        """Complexity measure of scheme."""
        return (
            code_length(scheme.equations) +
            numerical_conditioning(scheme) +
            sparsity_penalty(scheme)
        )

    def optimize(self):
        """Find Pareto-optimal schemes."""
        return globalmoo.solve(
            objectives=[self.action_functional, self.info_functional],
            space=self.schemes
        )
```

---

## 8. Paper Outline

### Title Options

1. "Scheme-Robustness as a Unifying Principle: From Imaginary Numbers to Meta-Calculus"
2. "Physical Laws as Equivalence Classes: A Meta-Theory of Representation Independence"
3. "The Meta-Gauge Group: Invariance Under Mathematical Representation Changes"

### Abstract

We propose that physical laws are best understood not as equations in a specific
mathematical language, but as equivalence classes under a groupoid G_scheme of
allowed representation transformations. Recent work showing that Real Number
Quantum Theory (RNQT) is experimentally indistinguishable from standard Complex
Quantum Theory provides a striking example: the imaginary unit i is scheme-dependent
scaffolding, while probabilities and interference are scheme-robust physics.

We formalize this into a two-axis framework where A-schemes (algebraic representations)
and C-schemes (calculus choices) form a groupoid, and define "physical" as whatever
is invariant under this groupoid. We show this principle unifies:

1. The RNQT vs CQT equivalence (Hoffreumon-Woods 2025)
2. Meta-calculus approaches to singularities (our prior work)
3. Positive geometry formulations of amplitudes

Crucially, new physics lives precisely where scheme-robustness breaks. We outline
a systematic search strategy using multi-objective optimization to hunt for
these breaking points.

### Sections

1. Introduction: The Problem of Mathematical Language
2. Background: From Gauge Invariance to Scheme Invariance
3. The Two-Axis Scheme Space (A, C)
4. G_scheme as a Groupoid
5. Case Study: RNQT vs CQT
6. Case Study: Meta-Calculus and Cosmological Singularities
7. Case Study: Positive Geometries and Amplitudes
8. The Three-Layer Principle (Action, Invariance, Information)
9. Hunting for Scheme-Breaking: A Search Strategy
10. Discussion: Implications for Quantum Gravity
11. Conclusion

### Key Citations

- Hoffreumon & Woods (2025) arXiv:2504.02808
- Renou et al. (2021) arXiv:2101.10873
- Chen et al. (2021) Nature s41586-021-04160-4
- Grossman & Katz (1972) Non-Newtonian Calculus
- Arkani-Hamed et al. (Amplituhedron papers)
- N01ne (multi-metric intelligence)

---

## 9. Implementation Roadmap

### Phase 1: Formalization (Week 1-2)

- [ ] Create scheme_groupoid.py with G_scheme definition
- [ ] Implement A-scheme transformations (Gamma, tensor_r, etc.)
- [ ] Implement C-scheme transformations (derivative swaps)
- [ ] Add invariance testing framework

### Phase 2: Upgrade Experiments (Week 3-4)

- [ ] Upgrade FRW experiments to (A,C) two-axis tests
- [ ] Upgrade QM experiments (Q-A, Q-B) to include A-scheme variations
- [ ] Add amplitude/positive geometry experiments
- [ ] Integrate with GlobalMOO for Pareto analysis

### Phase 3: Hunt for Breaking Points (Week 5-6)

- [ ] Systematic scan of FRW parameter space for scheme-breaking
- [ ] Test QM with Planck-scale constraints
- [ ] Probe positive geometry boundaries
- [ ] Document any genuine breaking points found

### Phase 4: Paper (Week 7-8)

- [ ] Draft conceptual paper
- [ ] Include worked examples from Phases 1-3
- [ ] Submit to arXiv

---

## 10. Key Equations Summary

### Scheme Definition
```
s = (A, C) in S
```

### G_scheme Action
```
g: (q, s) --> (q', s')
```

### Scheme-Robust Observable
```
O(q, s) = O(g.q, g.s) for all g in G_scheme
```

### Least Action (Layer 1)
```
delta S[q; s] = 0
```

### Information Parsimony (Layer 3)
```
I[s] = L_model(s) + L_data|s
```

### Meta-Principle
```
Physical = Invariant under G_scheme AND Pareto-optimal in I[s]
```

---

## 11. The One-Sentence Summary

> Physical laws are equivalence classes under scheme transformations;
> new physics lives where this equivalence breaks;
> preferred formulations minimize information subject to equivalence.

---

*Document Version: 1.0*
*Last Updated: 2025-12-06*
*Based on synthesis of RNQT (Hoffreumon-Woods 2025), meta-calculus, and positive geometries*
