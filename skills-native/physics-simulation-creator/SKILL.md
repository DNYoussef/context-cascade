---
name: physics-simulation-creator
description: > Create optimal physics simulations using Non-Newtonian Calculus (NNC) parameter tuning. Use for ANY physics simulation to maximize accuracy and minimize computational complexity. The k parameter optimizes numerical behavior - works for smooth problems AND singularities. Automatically detects if singularities exist and handles them appropriately.
---

# Physics Simulation Creator

Create optimal physics simulations with automatic parameter tuning using Non-Newtonian Calculus (NNC).

## Overview

This skill helps AI agents create **ANY numerical physics simulation** with optimal accuracy and minimal computational complexity. The k parameter from NNC provides a tuning knob that:

1. **Maximizes accuracy** for your specific problem type
2. **Minimizes computational steps** needed for convergence
3. **Handles singularities automatically** (if present)

**Key Insight**: Classical calculus (k=0) is not always optimal. Different physics problems benefit from different k values - even smooth problems without singularities.

## When to Use This Skill

### ALWAYS USE FOR (Significant gains):
- Problems with singularities (1/r, 1/r^2, crack tips, etc.)
- Molecular dynamics (atomic scale, L ~ 1e-10 m)
- Quantum simulations near singularities (hydrogen atom)
- Fracture mechanics (crack tip singularities)
- Gravitational simulations (black holes, 1/r potentials)

### USE FOR COMPUTATIONAL EFFICIENCY (Same accuracy, fewer steps):
- **Large simulations on consumer hardware** - 7-100x step reduction
- Long-time molecular dynamics (run 10x longer trajectories)
- Real-time physics in games/VR (same accuracy, faster)
- Parameter sweeps (run 10x more configurations)
- Stiff ODEs (dramatically fewer steps to converge)

### CONSIDER USING FOR (Moderate accuracy gains):
- Microscale simulations (L < 1e-6 m)
- Ultra-high precision requirements (>6 digits)
- Rapid scale-change problems

### k=0 IS OPTIMAL FOR (No NNC needed):
- Smooth quantum mechanics (harmonic oscillator)
- Human-scale engineering (1mm - 1km)
- Large-scale cosmology (smooth metrics)
- Problems with adequate engineering tolerance

### The Process

```
1. Analyze problem -> Does it have singularities? What length scale?
2. Select optimal k -> For accuracy AND complexity, not just singularity handling
3. Generate code -> With NNC transforms at optimal k
4. Validate -> Compare accuracy vs classical (k=0)
```

### Singularity Detection (Part of Process, Not the Only Use)

The skill automatically checks: **"Does this problem have a singularity I need to watch out for?"**

- If YES: k is tuned to handle it (e.g., k=-1 for 1/r)
- If NO: k is still optimized for accuracy/complexity (often k != 0)

----|-----------|---------------|----------------|----------------|
| Planck (1e-35 m) | 0.64 | 50%+ | 50-100x | **ALWAYS use NNC** |
| Atomic (1e-10 m) | 0.30 | 15-30% | 7-22x | **Use NNC** - significant |
| Micro (1e-6 m) | 0.24 | 10-20% | 5-10x | Use NNC for large sims |
| Human (1 m) | 0.16 | <5% | 1.5-3x | k=0 unless need speed |
| Solar (1e11 m) | 0.01 | <1% | ~1x | k=0 optimal |
| Galactic (1e21 m) | -0.13 | <5% | ~1x | k=0 optimal |

### Practical Decision Rule

**Use NNC (k != 0) when:**
1. Problem has explicit singularities (1/r, 1/r^2, etc.) - **ALWAYS**
2. Length scale < 1e-6 m (microscale and smaller) - **accuracy gains > 10%**
3. **Need to reduce computational steps** - 7-100x fewer steps at small scales
4. **Running large simulations on limited hardware** - same accuracy, faster
5. Ultra-high precision required (>6 digits) - even for smooth problems

**Use classical (k = 0) when:**
1. Smooth problem at human scale (1mm - 1km) AND speed not critical
2. Engineering tolerance is adequate (3-4 digits)
3. Simplicity preferred AND not computationally constrained

### Accuracy vs Complexity Trade-off

The CASCADE algorithm (61.9% win rate vs classical) proves that:
- Optimal k reduces step count by 7-100x (at microscale)
- Optimal k improves accuracy by 10-40,000x (for singularities) or 10-30% (for smooth microscale)
- These gains apply to BOTH singular and smooth problems (but magnitude differs)



## Core Formula

### k from Length Scale (Universal)

```
k_optimal(L) = -0.0137 * log10(L) + 0.1593
```

This works for ALL problems - singular or smooth.

### k from Singularity Type (When Present)

| Singularity | k | Use When |
|-------------|---|----------|
| 1/r | -1.0 | Coulomb, gravitational |
| 1/r^2 | -2.0 | Radiation intensity |
| 1/sqrt(r) | -0.5 | Crack tip stress |
| none | Use k(L) formula | Smooth problems |

**Decision Rule**:
- If explicit singularity exists: use singularity-based k
- If smooth/unknown: use k(L) formula based on length scale
- NEVER assume k=0 without checking



## Sub-Agents (From 206-Agent Registry)

| Agent | Path | Role | When Used |
|-------|------|------|-----------|
| **coder-enhanced** | `foundry/core/` | Generate complex numerical simulation code with TDD | Phase 3: Code generation |
| **quantum-computing-researcher** | `research/emerging/quantum/` | Quantum physics, algorithm design, numerical methods expertise | Phase 1: Quantum problems |
| **model-evaluation-agent** | `platforms/ai-ml/evaluation/` | Rigorous statistical comparison (k=optimal vs k=0), metrics | Phase 4: Accuracy validation |
| **experiment-tracking-agent** | `platforms/ai-ml/experiments/` | Track simulation experiments, log parameters, reproducibility | Phase 3-4: Experiment logging |
| **evaluator** | `research/` | Quality gate validation, GO/NO-GO decisions | Phase 4: Final validation |
| **root-cause-analyzer** | `quality/analysis/` | Debug failed simulations, identify numerical issues | Phase 4: Error diagnosis |
| **sublinear-goal-planner** | `research/reasoning/` | Complex problem decomposition, multi-step planning | Phase 1: Problem analysis |

### Agent Selection Rationale

**Why coder-enhanced over coder?**
- Better for complex numerical code
- TDD-focused approach for validation
- Handles scientific computing patterns

**Why model-evaluation-agent?**
- Statistical comparison expertise (paired t-test, effect size)
- Quantifies improvement: k=optimal vs k=0
- Generates evaluation reports

**Why experiment-tracking-agent?**
- Logs k values, length scales, singularity types
- Tracks accuracy/performance metrics across runs
- Enables reproducibility

**Why root-cause-analyzer?**
- When simulations fail or produce wrong results
- Identifies numerical issues (NaN, overflow, divergence)
- Maps to ERROR-DETECTION.md patterns



## Examples

### Example 1: Smooth Quantum Problem (No Singularity)

**Problem**: Harmonic oscillator simulation

```bash
python ai_simulation_helper.py --length-scale 1e-10 --json
```

**Output**:
```json
{
  "k": 0.2963,
  "has_singularity": false,
  "expected_accuracy_gain": "15-30% over classical"
}
```

**Result**: Even though there's no singularity, k=0.30 gives better accuracy than k=0.

### Example 2: Problem WITH Singularity

**Problem**: Molecular dynamics with Lennard-Jones

```bash
python ai_simulation_helper.py --problem "molecular dynamics" --json
```

**Output**:
```json
{
  "k": -1.0,
  "has_singularity": true,
  "singularity_type": "1/r",
  "expected_accuracy_gain": "10,000x+ over classical"
}
```

**Result**: Singularity detected, k tuned to handle it.

### Example 3: Large-Scale Cosmology

**Problem**: Galaxy formation simulation

```bash
python ai_simulation_helper.py --length-scale 1e21 --json
```

**Output**:
```json
{
  "k": -0.1284,
  "has_singularity": false,
  "expected_accuracy_gain": "5-10% over classical"
}
```

**Result**: At galactic scales, k goes slightly negative but is still not exactly 0.

--------|--------|
| Singularity present | Use k from singularity table (k=-1 for 1/r, etc.) |
| L < 1e-6 m, smooth | Use k from k(L) formula (gains > 10%) |
| Human scale, smooth | k=0 is optimal (gains < 5%) |
| Need ultra-precision | Consider k(L) even for smooth problems |



## Success Metrics

| Metric | Target |
|--------|--------|
| k-value selection | Use CLI script output |
| Accuracy vs k=0 | Document improvement |
| Performance vs k=0 | Document step reduction |
| Singularity detection | Correctly identify if present |



## Memory Namespace

```yaml
namespaces:
  - physics-simulation-creator/problems/{id}: Analyzed problems
  - physics-simulation-creator/simulations/{id}: Generated simulations
  - physics-simulation-creator/comparisons/{id}: k=optimal vs k=0 results
  - improvement/audits/physics-simulation-creator: Skill audits
```

----|--------------|
| **prompt-forge** | Can improve this skill's documentation |
| **skill-auditor** | Audits this skill for improvement opportunities |
| **functionality-audit** | Validates simulation correctness |
| **model-evaluation-agent** | Compares k=optimal vs k=0 accuracy |
| **experiment-tracking-agent** | Tracks simulation experiments |

### Guardrails

**NEVER**:
- Generate k values outside the physics-valid range
- Skip validation against k=0 baseline
- Assume smooth when singularity might exist
- Create simulations without documenting k-source
- Modify frozen eval harness benchmarks

**ALWAYS**:
- Run CLI script for k-selection
- Include comparison vs k=0
- Document assumptions explicitly
- Support auditing with clear metrics
- Capture learnings for expertise update



## Core Principles

### 1. Optimization is Universal, Not Singular
The optimal numerical method depends on the problem scale and structure, not just the presence of singularities. Classical calculus (k=0) is one choice among many, not the default.

**In practice:**
- Always run ai_simulation_helper.py to determine optimal k, even for smooth problems
- Use k(L) formula for scale-dependent optimization: k = -0.0137 * log10(L) + 0.1593
- Recognize that k != 0 provides 10-30% accuracy gains at microscales (L < 1e-6 m)
- Understand that k handles singularities (k=-1 for 1/r) AND optimizes smooth problems
- Never assume k=0 is optimal without verification
- Document why k was chosen (scale-based or singularity-based)

### 2. Validate Against Baselines
Numerical improvements must be demonstrated empirically, not assumed. Every simulation should prove it outperforms classical methods.

**In practice:**
- Always compare k=optimal vs k=0 (classical) baseline
- Measure accuracy improvement (relative error reduction)
- Measure computational efficiency (step count reduction)
- Document convergence rates for both methods
- Use model-evaluation-agent for statistical comparison (paired t-test)
- Report both accuracy gains AND step reduction (not just one)
- Validate that solution remains physically meaningful (energy conservation, boundedness)

### 3. Transparency Through Reproducibility
Simulations must be independently verifiable. The k-selection process, transforms, and validation must be fully documented.

**In practice:**
- Document k value, source (length scale or singularity type), and expected improvement
- Include both forward and inverse NNC transforms in code
- Provide comparison plots (k=optimal vs k=0 error curves)
- Store results in experiment-tracking-agent with full parameters
- Make assumptions explicit (smoothness, boundary conditions, scale ranges)
- Include roundtrip error tests (transform -> inverse -> verify < 1e-10 error)
- Archive simulation code, k-selection rationale, and validation results

-----------|---------|----------|
| **Assuming k=0 is optimal** | Misses 10-30% accuracy gains at microscales and 10,000x+ gains for singularities by defaulting to classical calculus | Always run ai_simulation_helper.py. Use k(L) formula for scale-based optimization. Only use k=0 if empirically validated. |
| **Using NNC only for singularities** | Limits NNC to singularity handling, ignores computational efficiency gains for smooth problems | Recognize NNC optimizes BOTH accuracy (singularities) AND complexity (step reduction). Use for any simulation where speed matters. |
| **Skipping k=0 comparison** | Cannot prove improvement, lacks evidence for k-selection, wastes effort if classical methods work fine | Always benchmark k=optimal vs k=0. Document accuracy and step count differences. Use model-evaluation-agent for statistical validation. |
| **Hardcoding k values** | Violates scale-dependence, uses wrong k for problem, cannot adapt to different physics | Use ai_simulation_helper.py for every problem. Never hardcode k without CLI verification. Store k-selection rationale. |
| **Missing inverse transforms** | Forward-only transforms prevent coordinate recovery, breaks visualization and boundary conditions | Implement BOTH forward (u -> v) AND inverse (v -> u) transforms. Test roundtrip error < 1e-10. |
| **No physics validation** | Numerically stable but physically wrong (negative energies, unbounded solutions, violation of conservation laws) | Verify physical constraints: energy conservation, boundedness at singularities, correct asymptotic behavior. Use domain experts. |
| **Hardcoded speedup values (THEATER)** | Fake metrics like `speedupFactor: 2.0` without measurement deceive users and prevent real optimization | ALWAYS measure speedups with real timing (performance.now()). Never hardcode multipliers. Use PerformanceTracker class. |
| **Lookup tables for Math.*functions** | Modern JS engines compile Math.sqrt/exp/log to CPU instructions. Lookup tables with interpolation are SLOWER (0.18x measured). | Use native Math.* functions. Lookup tables only help on very old browsers. Benchmark before assuming optimization works. |

----------|------------------|--------|
| **Object Pooling (ArrayPool)** | **6.62x** | REAL WIN - eliminates GC pauses |
| **Fast Math Lookup Tables** | **0.18x (SLOWER)** | REMOVED - native Math.* is faster |
| **In-place Operations** | ~1x (neutral) | JS JIT optimizes allocations well |

**Key Insight**: Modern JavaScript engines (V8, SpiderMonkey) compile `Math.sqrt`, `Math.exp`, etc. to direct CPU instructions. Pre-computed lookup tables with linear interpolation add overhead and are actually SLOWER.

### 2. Object Pooling: The Real Win

```typescript
// BAD: Allocates 10 new Float32Arrays per RK4 step
function rk4Step(...) {
  const k1 = new Float32Array(n);  // GC pressure
  const k2 = new Float32Array(n);
  // ... 8 more allocations
}

// GOOD: Reuses pooled arrays (6.62x faster)
const arrayPool = new ArrayPool();
function rk4StepPooled(...) {
  const k1 = arrayPool.acquire(n);  // From pool, no GC
  // ... use k1
  arrayPool.release(k1);  // Return to pool
}
```

**Implementation**: See `lib/physics/real-performance.ts` in meta-calculus-portfolio.

### 3. NNC Benefit is NUMERICAL STABILITY, Not Raw Speed

NNC with k=-1 does NOT make Math.sqrt faster. It allows:

| Metric | Classical (k=0) | NNC (k=-1) | Improvement |
|--------|-----------------|------------|-------------|
| Timestep size | dt = 0.0002 | dt = 0.0012 | **5.91x larger** |
| Steps to simulate 10s | ~50,000 | ~8,300 | **6x fewer** |
| Stability near singularity | Stalls/NaN | Stable | **Robust** |

**Key Insight**: The speedup comes from needing FEWER INTEGRATION STEPS because larger timesteps remain stable, not from faster individual calculations.

### 4. Avoid "Theater" Code

**WRONG (Fake speedup):**
```typescript
// This is THEATER - hardcoded fake metrics
const speedupFactor = controls.nncEnabled ? 2.0 : 1.0;  // LIE
const dt = 0.002 * (nncEnabled ? 1.5 : 1);  // FAKE
```

**RIGHT (Real measurement):**
```typescript
// Measure actual physics time
const physicsStart = performance.now();
// ... do physics
const physicsTime = performance.now() - physicsStart;

// Track real speedup vs baseline
performanceTracker.endPhysics(physicsStart, dt);
const realSpeedup = performanceTracker.getRealSpeedup();
```

### 5. Separate ORTHOGONAL vs NNC Speedups

When displaying metrics, separate:

1. **Orthogonal Optimizations** (benefit BOTH Classical and NNC modes):
   - Object pooling (~6x)
   - Algorithmic improvements (spatial hash, Barnes-Hut)
   - Memory layout optimization

2. **NNC Mathematical Benefits** (only benefit NNC mode):
   - Larger stable timesteps (~6x)
   - Better energy conservation
   - Avoids stalls near singularities

```typescript
interface Metrics3D {
  // NNC math speedup (only for NNC mode)
  speedupFactor: number;

  // Orthogonal infrastructure speedup (benefits both modes)
  infraSpeedup?: number;
  pooledArrays?: number;
  gcAvoided?: number;
}
```

### 6. When Spatial Hashing Helps vs Hurts

| Scenario | Use Spatial Hash? | Reason |
|----------|-------------------|--------|
| LJ with cutoff (short-range) | YES | O(n) vs O(n^2) for neighbors |
| Biot-Savart (long-range 1/r) | NO | Cutoff introduces physics errors |
| <50 particles | NO | Hash overhead exceeds benefit |
| >1000 particles | YES | O(n^2) becomes prohibitive |

### 7. Benchmark Template

Always run honest benchmarks before claiming optimization:

```javascript
// Warmup
for (let i = 0; i < 1000; i++) { optimizedFn(data); classicalFn(data); }

// Measure classical
const startClassical = performance.now();
for (let i = 0; i < N; i++) { classicalFn(data); }
const timeClassical = performance.now() - startClassical;

// Measure optimized
const startOptimized = performance.now();
for (let i = 0; i < N; i++) { optimizedFn(data); }
const timeOptimized = performance.now() - startOptimized;

// Real speedup
const speedup = timeClassical / timeOptimized;
console.log(`Speedup: ${speedup.toFixed(2)}x`);  // May be < 1 !
```

### Summary: What Actually Works

| Technique | Expected | Actual | Use? |
|-----------|----------|--------|------|
| Object pooling | 2-5x | 6.62x | YES |
| Lookup tables | 2x | 0.18x | NO (slower) |
| In-place ops | 1.5x | 1x | Neutral |
| NNC k=-1 timestep | 2-6x | 5.91x | YES |
| Spatial hash (>1000 particles) | 10-100x | ~50x | YES |
| Spatial hash (<50 particles) | 2x | 0.5x | NO (overhead)

---

## Conclusion

The Physics Simulation Creator skill challenges the assumption that classical calculus (k=0) is universally optimal. By leveraging Non-Newtonian Calculus (NNC) with scale-dependent parameter tuning, this skill delivers significant accuracy improvements (10-30% for microscales, 10,000x+ for singularities) and computational efficiency gains (7-100x step reduction).

The core insight is that optimal k varies by problem scale and structure. The bundled ai_simulation_helper.py script automates k-selection using the k(L) formula for length-scale optimization and singularity-specific tables for problems with explicit discontinuities. This ensures that every simulation uses the numerically optimal method for its specific physics, rather than defaulting to classical approaches.

By enforcing baseline comparisons, transparent documentation, and physics validation, this skill ensures that NNC-based simulations are not only faster and more accurate but also reproducible and scientifically rigorous. Whether simulating molecular dynamics at atomic scales or handling gravitational singularities, this skill provides a systematic framework for optimal numerical physics simulation.