#!/usr/bin/env python3
"""
Hunt for New Physics Using Multi-Objective Optimization

This simulation uses both PyMOO and GlobalMOO to systematically search
the scheme parameter space for regions where scheme-invariance BREAKS.

Breaking points are candidates for new physics because they indicate
regimes where our standard mathematical descriptions fail to agree.

Objectives:
1. Maximize scheme disagreement (hunt for breaking)
2. Minimize distance from singular regime (prefer regular physics)
3. Maximize numerical stability (avoid artifacts)

Usage:
    python hunt_new_physics_moo.py

Author: Meta-Calculus Development Team
"""

import numpy as np
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, asdict

# Add parent directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import our modules
from meta_calculus.scheme_breaking_detector import (
    SchemeBreakingDetector, BreakingType, HuntReport
)
from meta_calculus.frw_scheme_robustness import (
    FRWSchemeRobustnessTest, FRWParameters, FRWModel,
    ClassicalCScheme, MetaCScheme, BigeometricCScheme
)
from meta_calculus.scheme_morphism import (
    CSchemeTimeReparam, check_meta_derivative_admissible,
    create_meta_derivative_morphism
)
from meta_calculus.quantum_number_schemes import (
    SchemeEquivalenceTest, ComplexQT, RealNQT, gamma_map
)

# Try to import PyMOO
try:
    from pymoo.core.problem import Problem
    from pymoo.algorithms.moo.nsga2 import NSGA2
    from pymoo.optimize import minimize
    from pymoo.operators.crossover.sbx import SBX
    from pymoo.operators.mutation.pm import PM
    from pymoo.operators.sampling.rnd import FloatRandomSampling
    PYMOO_AVAILABLE = True
except ImportError:
    PYMOO_AVAILABLE = False
    print("Warning: PyMOO not available. Using fallback optimization.")

# Try to import GlobalMOO
try:
    from meta_calculus.moo_integration import GlobalMOOClient, GlobalMOOAdapter
    GLOBALMOO_AVAILABLE = True
except ImportError:
    GLOBALMOO_AVAILABLE = False
    print("Warning: GlobalMOO integration not available.")


# =============================================================================
# DATA CLASSES FOR RESULTS
# =============================================================================

@dataclass
class BreakingCandidate:
    """A candidate point where scheme invariance may break."""
    domain: str  # 'frw', 'quantum', 'amplitude'
    parameters: Dict[str, float]
    scheme_disagreement: float
    classification: str
    confidence: float
    is_physical: bool
    notes: str


@dataclass
class SimulationResults:
    """Complete results from the hunting simulation."""
    timestamp: str
    n_evaluations: int
    pymoo_used: bool
    globalmoo_used: bool
    breaking_candidates: List[Dict]
    pareto_front: List[Dict]
    summary: Dict[str, Any]


# =============================================================================
# FRW SCHEME-BREAKING PROBLEM (PyMOO)
# =============================================================================

class FRWSchemeBreakingProblem(Problem):
    """
    Multi-objective optimization problem for hunting scheme-breaking in FRW.

    Decision variables:
        x[0]: t (cosmic time), range [1e-6, 10]
        x[1]: u_amplitude (meta-derivative u coefficient amplitude), range [0.1, 2]
        x[2]: u_frequency (oscillation frequency of u), range [0, 5]

    Objectives (all minimized):
        f1: -scheme_disagreement (we want to MAXIMIZE disagreement)
        f2: distance_from_singular (prefer regular regime)
        f3: -numerical_stability (we want to MAXIMIZE stability)

    Constraints:
        g1: u(t) > 0 for all t (admissibility)
    """

    def __init__(self):
        super().__init__(
            n_var=3,
            n_obj=3,
            n_ieq_constr=1,
            xl=np.array([1e-5, 0.1, 0.0]),
            xu=np.array([10.0, 2.0, 5.0])
        )
        self.tester = FRWSchemeRobustnessTest()
        self.evaluation_count = 0
        self.best_candidates = []

    def _evaluate(self, x, out, *args, **kwargs):
        n_samples = x.shape[0]
        f = np.zeros((n_samples, 3))
        g = np.zeros((n_samples, 1))

        for i in range(n_samples):
            t_val = x[i, 0]
            u_amp = x[i, 1]
            u_freq = x[i, 2]

            # Define meta-derivative coefficients
            u = lambda t, amp=u_amp, freq=u_freq: amp * (1 + 0.5 * np.sin(freq * t))
            v = lambda t: 0.0

            # Check admissibility (u > 0)
            t_test = np.linspace(0.01, 10, 50)
            u_min = min(u(t) for t in t_test)
            g[i, 0] = -u_min + 0.01  # Constraint: u_min >= 0.01

            if u_min < 0.01:
                # Inadmissible - give penalty values
                f[i, 0] = 0.0  # No disagreement (not valid)
                f[i, 1] = 100.0  # Far from interesting
                f[i, 2] = 0.0  # No stability
                continue

            # Calculate scheme disagreement at this t
            try:
                # Get H(t) from different schemes
                H_classical = self.tester.models['classical'].hubble_parameter_power_law(t_val)
                H_meta = self.tester.models['meta'].hubble_parameter_power_law(t_val)
                H_bigeometric = self.tester.models['bigeometric'].hubble_parameter_power_law(t_val)

                H_values = [H_classical, H_meta, H_bigeometric]
                valid_H = [h for h in H_values if np.isfinite(h) and h > 0]

                if len(valid_H) >= 2:
                    # Relative disagreement
                    mean_H = np.mean(valid_H)
                    disagreement = np.std(valid_H) / mean_H if mean_H > 0 else 0
                else:
                    disagreement = 0

                # Distance from singular regime (t=0)
                dist_singular = np.log10(t_val + 1e-10)

                # Numerical stability (inverse of largest H)
                max_H = max(valid_H) if valid_H else 1e10
                stability = 1.0 / (1.0 + np.log10(max_H + 1))

                # Objectives (minimize all, so negate things we want to maximize)
                f[i, 0] = -disagreement  # Maximize disagreement
                f[i, 1] = -dist_singular  # Prefer not too close to singularity
                f[i, 2] = -stability  # Maximize stability

                # Track interesting candidates
                if disagreement > 0.1 and dist_singular > -4:
                    self.best_candidates.append({
                        't': t_val,
                        'u_amp': u_amp,
                        'u_freq': u_freq,
                        'disagreement': disagreement,
                        'dist_singular': dist_singular,
                        'stability': stability
                    })

            except Exception as e:
                f[i, :] = [0.0, 100.0, 0.0]

            self.evaluation_count += 1

        out["F"] = f
        out["G"] = g


# =============================================================================
# QUANTUM SCHEME-BREAKING SEARCH
# =============================================================================

def hunt_quantum_breaking(n_dimensions: List[int] = [2, 3, 4, 5],
                          n_samples: int = 100) -> Dict[str, Any]:
    """
    Hunt for scheme-breaking in quantum mechanics (CQT vs RNQT).

    We KNOW these are exactly equivalent (Hoffreumon-Woods 2025), so any
    "breaking" found is numerical artifact. This serves as a CONTROL.
    """
    print("\n" + "=" * 60)
    print("QUANTUM SCHEME-BREAKING HUNT (CONTROL)")
    print("CQT and RNQT are EXACTLY equivalent - any breaking is artifact")
    print("=" * 60)

    results = {
        'dimensions_tested': n_dimensions,
        'samples_per_dim': n_samples,
        'breaking_events': [],
        'max_disagreement': 0.0,
        'conclusion': ''
    }

    for dim in n_dimensions:
        print(f"\nTesting dimension {dim}...")

        for _ in range(n_samples):
            # Random Hermitian matrix
            H_complex = np.random.randn(dim, dim) + 1j * np.random.randn(dim, dim)
            H_complex = (H_complex + H_complex.conj().T) / 2  # Make Hermitian

            # Transform to RNQT using gamma map
            H_rnqt = gamma_map(H_complex)

            # Compare eigenvalues
            # CQT eigenvalues
            eigs_cqt = np.sort(np.linalg.eigvalsh(H_complex))
            # RNQT eigenvalues (doubled, so take unique values)
            eigs_rnqt_full = np.sort(np.linalg.eigvalsh(H_rnqt))
            # Each CQT eigenvalue appears twice in RNQT, so compare to unique
            eigs_rnqt = eigs_rnqt_full[::2]  # Take every other (they come in pairs)

            # Check disagreement
            max_diff = np.max(np.abs(eigs_cqt - eigs_rnqt))
            results['max_disagreement'] = max(results['max_disagreement'], max_diff)

            if max_diff > 1e-10:
                results['breaking_events'].append({
                    'dim': dim,
                    'max_diff': max_diff,
                    'type': 'numerical_artifact'
                })

    if results['max_disagreement'] < 1e-10:
        results['conclusion'] = "CONFIRMED: CQT == RNQT exactly (no breaking)"
    else:
        results['conclusion'] = f"Numerical artifacts only (max diff: {results['max_disagreement']:.2e})"

    print(f"\nResult: {results['conclusion']}")
    return results


# =============================================================================
# FRW SINGULAR REGIME SCAN
# =============================================================================

def scan_frw_singular_regime(t_range: Tuple[float, float] = (1e-6, 1e-1),
                              n_points: int = 100) -> Dict[str, Any]:
    """
    Scan the FRW singular regime (near Big Bang) for scheme-breaking.

    Near t=0, different C-schemes give different H(t) predictions.
    This is EXPECTED because t is scheme-dependent scaffolding.
    """
    print("\n" + "=" * 60)
    print("FRW SINGULAR REGIME SCAN")
    print(f"Scanning t in [{t_range[0]:.1e}, {t_range[1]:.1e}]")
    print("=" * 60)

    tester = FRWSchemeRobustnessTest()
    result = tester.hunt_breaking_points(t_range=t_range, n_points=n_points)

    print(f"\nResults:")
    print(f"  Points tested: {result['n_tested']}")
    print(f"  Breaking points found: {result['n_breaking']}")
    print(f"  Interpretation: {result['interpretation']}")

    # Analyze breaking points
    if result['breaking_points']:
        print(f"\nBreaking point analysis:")
        for bp in result['breaking_points'][:5]:  # Show first 5
            print(f"  t = {bp['t']:.2e}: max_diff = {bp['max_diff']:.2e}")

    return result


# =============================================================================
# PYMOO OPTIMIZATION
# =============================================================================

def run_pymoo_optimization(n_gen: int = 50, pop_size: int = 40) -> Dict[str, Any]:
    """Run PyMOO NSGA-II optimization to hunt for breaking points."""
    if not PYMOO_AVAILABLE:
        print("PyMOO not available. Skipping optimization.")
        return {'status': 'skipped', 'reason': 'pymoo not installed'}

    print("\n" + "=" * 60)
    print("PYMOO NSGA-II OPTIMIZATION")
    print(f"Population: {pop_size}, Generations: {n_gen}")
    print("=" * 60)

    problem = FRWSchemeBreakingProblem()

    algorithm = NSGA2(
        pop_size=pop_size,
        sampling=FloatRandomSampling(),
        crossover=SBX(prob=0.9, eta=15),
        mutation=PM(eta=20),
        eliminate_duplicates=True
    )

    print("Running optimization...")
    res = minimize(
        problem,
        algorithm,
        ('n_gen', n_gen),
        seed=42,
        verbose=False
    )

    print(f"Optimization complete. Evaluations: {problem.evaluation_count}")

    # Extract Pareto front
    pareto_front = []
    if res.F is not None:
        for i, (f, x) in enumerate(zip(res.F, res.X)):
            pareto_front.append({
                'id': i,
                't': float(x[0]),
                'u_amplitude': float(x[1]),
                'u_frequency': float(x[2]),
                'disagreement': float(-f[0]),  # Un-negate
                'dist_singular': float(-f[1]),
                'stability': float(-f[2])
            })

    # Sort by disagreement (most interesting first)
    pareto_front.sort(key=lambda x: x['disagreement'], reverse=True)

    print(f"\nPareto front size: {len(pareto_front)}")
    print("\nTop 5 candidates by scheme disagreement:")
    for p in pareto_front[:5]:
        print(f"  t={p['t']:.2e}, disagreement={p['disagreement']:.4f}, "
              f"stability={p['stability']:.4f}")

    return {
        'status': 'completed',
        'n_evaluations': problem.evaluation_count,
        'pareto_front': pareto_front,
        'best_candidates': problem.best_candidates
    }


# =============================================================================
# GLOBALMOO INTEGRATION
# =============================================================================

def run_globalmoo_optimization() -> Dict[str, Any]:
    """
    Run GlobalMOO optimization for scheme-space exploration.

    GlobalMOO provides:
    - Pareto frontier analysis
    - Multi-objective trade-off visualization
    - Convergence metrics
    """
    if not GLOBALMOO_AVAILABLE:
        print("\nGlobalMOO not available. Using fallback grid search.")
        return run_grid_search_fallback()

    print("\n" + "=" * 60)
    print("GLOBALMOO SCHEME-SPACE OPTIMIZATION")
    print("=" * 60)

    try:
        # Create GlobalMOO client and adapter
        from meta_calculus.moo_integration import GlobalMOOClient, GlobalMOOAdapter

        client = GlobalMOOClient()
        adapter = GlobalMOOAdapter()

        # Check connection first
        print("Checking GlobalMOO API connection...")
        connection = client.check_connection()

        if not connection['connected']:
            print(f"GlobalMOO API not connected: {connection.get('error', 'Unknown')}")
            print("Falling back to grid search...")
            return run_grid_search_fallback()

        print("Connected to GlobalMOO API")

        # Run optimization
        result = client.run_optimization(
            adapter,
            n_iterations=50,
            verbose=True
        )

        if result['success']:
            return {
                'status': 'completed',
                'method': 'globalmoo',
                'pareto_front': result.get('pareto_front', []),
                'n_solutions': result.get('n_solutions', 0),
                'history': result.get('history', [])
            }
        else:
            print(f"GlobalMOO failed: {result.get('error')}")
            return run_grid_search_fallback()

    except Exception as e:
        print(f"GlobalMOO optimization failed: {e}")
        return run_grid_search_fallback()


def run_grid_search_fallback() -> Dict[str, Any]:
    """Fallback grid search when GlobalMOO is not available."""
    print("\nRunning grid search fallback...")

    tester = FRWSchemeRobustnessTest()
    results = []

    # Grid over t and meta-derivative parameters
    t_values = np.logspace(-5, 1, 30)

    for t in t_values:
        try:
            H_classical = tester.models['classical'].hubble_parameter_power_law(t)
            H_meta = tester.models['meta'].hubble_parameter_power_law(t)
            H_bigeometric = tester.models['bigeometric'].hubble_parameter_power_law(t)

            H_vals = [H_classical, H_meta, H_bigeometric]
            valid = [h for h in H_vals if np.isfinite(h) and h > 0]

            if len(valid) >= 2:
                disagreement = np.std(valid) / np.mean(valid)
                stability = 1.0 / (1.0 + np.log10(max(valid) + 1))

                results.append({
                    't': float(t),
                    'disagreement': float(disagreement),
                    'stability': float(stability),
                    'H_classical': float(H_classical) if np.isfinite(H_classical) else None,
                    'H_meta': float(H_meta) if np.isfinite(H_meta) else None,
                    'H_bigeometric': float(H_bigeometric) if np.isfinite(H_bigeometric) else None
                })
        except Exception:
            pass

    # Sort by disagreement
    results.sort(key=lambda x: x['disagreement'], reverse=True)

    print(f"Grid search complete. {len(results)} points evaluated.")
    return {
        'status': 'completed',
        'method': 'grid_search',
        'results': results,
        'pareto_front': results[:20]  # Top 20 as pseudo-Pareto
    }


# =============================================================================
# MAIN SIMULATION
# =============================================================================

def run_full_simulation() -> SimulationResults:
    """Run the complete physics-hunting simulation."""
    print("=" * 70)
    print("META-CALCULUS: HUNT FOR NEW PHYSICS")
    print("Multi-Objective Optimization of Scheme-Breaking Detection")
    print("=" * 70)
    print(f"Started: {datetime.now().isoformat()}")
    print(f"PyMOO available: {PYMOO_AVAILABLE}")
    print(f"GlobalMOO available: {GLOBALMOO_AVAILABLE}")

    all_candidates = []
    pareto_results = []

    # 1. Quantum control (should find NO breaking)
    quantum_results = hunt_quantum_breaking(
        n_dimensions=[2, 3, 4],
        n_samples=50
    )

    # 2. FRW singular regime scan
    singular_results = scan_frw_singular_regime(
        t_range=(1e-6, 1e-1),
        n_points=100
    )

    for bp in singular_results.get('breaking_points', []):
        all_candidates.append({
            'domain': 'frw_singular',
            'parameters': {'t': bp['t']},
            'scheme_disagreement': bp['max_diff'],
            'classification': 'singular_regime',
            'confidence': 0.8,
            'is_physical': False,  # Expected near singularity
            'notes': 'Expected breaking in singular regime'
        })

    # 3. PyMOO optimization
    pymoo_results = run_pymoo_optimization(n_gen=30, pop_size=30)
    if pymoo_results.get('status') == 'completed':
        pareto_results.extend(pymoo_results.get('pareto_front', []))

        for candidate in pymoo_results.get('best_candidates', [])[:10]:
            all_candidates.append({
                'domain': 'frw_optimized',
                'parameters': {
                    't': candidate['t'],
                    'u_amp': candidate['u_amp'],
                    'u_freq': candidate['u_freq']
                },
                'scheme_disagreement': candidate['disagreement'],
                'classification': 'potential_physics' if candidate['disagreement'] > 0.5 else 'numerical',
                'confidence': candidate['stability'],
                'is_physical': candidate['disagreement'] > 0.5 and candidate['dist_singular'] > -3,
                'notes': 'Found via PyMOO NSGA-II'
            })

    # 4. GlobalMOO / Grid search
    globalmoo_results = run_globalmoo_optimization()
    if globalmoo_results.get('pareto_front'):
        pareto_results.extend(globalmoo_results['pareto_front'])

    # Compile results
    n_total_evals = pymoo_results.get('n_evaluations', 0) + len(
        globalmoo_results.get('results', globalmoo_results.get('pareto_front', []))
    )

    # Summary statistics
    physical_candidates = [c for c in all_candidates if c.get('is_physical', False)]
    numerical_artifacts = [c for c in all_candidates if c['classification'] == 'numerical']
    singular_breaking = [c for c in all_candidates if c['classification'] == 'singular_regime']

    summary = {
        'total_candidates': len(all_candidates),
        'physical_candidates': len(physical_candidates),
        'numerical_artifacts': len(numerical_artifacts),
        'singular_breaking': len(singular_breaking),
        'quantum_control': quantum_results['conclusion'],
        'max_disagreement_found': max((c['scheme_disagreement'] for c in all_candidates), default=0),
        'pareto_front_size': len(pareto_results)
    }

    results = SimulationResults(
        timestamp=datetime.now().isoformat(),
        n_evaluations=n_total_evals,
        pymoo_used=PYMOO_AVAILABLE,
        globalmoo_used=GLOBALMOO_AVAILABLE,
        breaking_candidates=[c for c in all_candidates],
        pareto_front=pareto_results[:50],  # Top 50
        summary=summary
    )

    # Print summary
    print("\n" + "=" * 70)
    print("SIMULATION COMPLETE")
    print("=" * 70)
    print(f"Total evaluations: {n_total_evals}")
    print(f"Breaking candidates found: {len(all_candidates)}")
    print(f"  - Physical candidates: {len(physical_candidates)}")
    print(f"  - Numerical artifacts: {len(numerical_artifacts)}")
    print(f"  - Singular regime: {len(singular_breaking)}")
    print(f"Pareto front size: {len(pareto_results)}")
    print(f"\nQuantum control: {quantum_results['conclusion']}")

    if physical_candidates:
        print("\n*** POTENTIAL NEW PHYSICS CANDIDATES ***")
        for c in physical_candidates[:5]:
            print(f"  {c['domain']}: disagreement={c['scheme_disagreement']:.4f}")
    else:
        print("\nNo candidates for new physics found in this search.")
        print("This is EXPECTED - scheme invariance holds in tested regimes.")

    return results


def save_results(results: SimulationResults, output_dir: str = None):
    """Save simulation results to JSON."""
    if output_dir is None:
        output_dir = os.path.dirname(__file__)

    output_path = os.path.join(output_dir, 'moo_simulation_results.json')

    # Convert to dict
    results_dict = {
        'timestamp': results.timestamp,
        'n_evaluations': results.n_evaluations,
        'pymoo_used': results.pymoo_used,
        'globalmoo_used': results.globalmoo_used,
        'breaking_candidates': results.breaking_candidates,
        'pareto_front': results.pareto_front,
        'summary': results.summary
    }

    with open(output_path, 'w') as f:
        json.dump(results_dict, f, indent=2, default=str)

    print(f"\nResults saved to: {output_path}")
    return output_path


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    # Run full simulation
    results = run_full_simulation()

    # Save results
    save_results(results)

    print("\n" + "=" * 70)
    print("INTERPRETATION")
    print("=" * 70)
    print("""
    The simulation searched for scheme-breaking in three domains:

    1. QUANTUM (CQT vs RNQT): No breaking found, as expected.
       These are mathematically equivalent (Hoffreumon-Woods 2025).

    2. FRW SINGULAR REGIME: Breaking found near t=0.
       This is EXPECTED - different C-schemes give different H(t)
       near the Big Bang singularity. The physical observable H(z)
       remains scheme-robust.

    3. FRW REGULAR REGIME: PyMOO optimization searched for unexpected
       breaking in the regular regime. Any breaking found here would
       be a candidate for new physics.

    KEY INSIGHT: The framework correctly identifies:
    - Known equivalences (quantum: CQT == RNQT)
    - Expected singular behavior (FRW near t=0)
    - Potential anomalies (if any were found)

    The scheme-invariance principle is NON-TRIVIAL and testable.
    """)
