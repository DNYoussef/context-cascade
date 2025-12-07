#!/usr/bin/env python3
"""
Phase-II Numerical Relativity Scheme Invariance

Tests scheme-invariance across numerical relativity formulations:
- ADM (Arnowitt-Deser-Misner)
- BSSN (Baumgarte-Shapiro-Shibata-Nakamura)
- Generalized Harmonic Gauge (GHG)

Key insight from AI conversation:
Physical invariants (gravitational wave strain, ADM mass, angular momentum,
horizon areas) should be approximately scheme-invariant up to discretization error.

3+1 decomposition:
ds^2 = -alpha^2 dt^2 + gamma_ij (dx^i + beta^i dt)(dx^j + beta^j dt)

CURRENT STATUS: Structural placeholder with correct invariance testing pattern.
The evolution is trivial by design - needs real ADM/BSSN steps for physics.

VERSION: Phase-II (extracted from AI conversation analysis)
Author: Meta-Calculus Development Team
"""

import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Tuple, Any, Callable, Optional
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# PyMOO integration
try:
    from pymoo.core.problem import Problem
    from pymoo.algorithms.moo.nsga2 import NSGA2
    from pymoo.optimize import minimize
    from pymoo.operators.sampling.rnd import FloatRandomSampling
    PYMOO_AVAILABLE = True
except ImportError:
    PYMOO_AVAILABLE = False


# =============================================================================
# 3+1 FORMALISM BASICS
# =============================================================================

@dataclass
class ADMVariables:
    """ADM formulation variables."""
    gamma: np.ndarray  # 3-metric (N x 3 x 3)
    K: np.ndarray  # Extrinsic curvature (N x 3 x 3)
    alpha: np.ndarray  # Lapse (N,)
    beta: np.ndarray  # Shift (N x 3)


@dataclass
class BSSNVariables:
    """BSSN formulation variables."""
    phi: np.ndarray  # Conformal factor (or chi = exp(-4*phi))
    gamma_tilde: np.ndarray  # Conformal metric
    K: np.ndarray  # Trace of extrinsic curvature
    A_tilde: np.ndarray  # Traceless part of extrinsic curvature
    Gamma_tilde: np.ndarray  # Conformal connection functions


@dataclass
class NRConfig:
    """Configuration for numerical relativity simulation."""
    formulation: str  # 'ADM', 'BSSN', or 'GHG'
    gauge: Dict[str, float]  # Gauge parameters
    resolution: int  # Grid points
    domain_size: float  # Physical domain size
    cfl: float  # CFL number


# =============================================================================
# METRIC AND GAUGE CHOICES
# =============================================================================

def schwarzschild_3metric_isotropic(r: np.ndarray, M: float = 1.0) -> np.ndarray:
    r"""
    Schwarzschild 3-metric in isotropic coordinates.

    ds^2_3 = psi^4 * (dr^2 + r^2 d\Omega^2)

    where psi = 1 + M/(2r)
    """
    psi = 1.0 + M / (2.0 * r + 1e-10)
    psi4 = psi ** 4

    # Return diagonal metric components (assuming spherical symmetry)
    return psi4 * np.ones_like(r)


def lapse_1plus_log(alpha: np.ndarray, K: np.ndarray, f: float = 2.0) -> np.ndarray:
    """
    1+log slicing: d_t alpha = -f * alpha * K

    Popular gauge choice for black hole simulations.
    """
    return -f * alpha * K


def shift_gamma_driver(beta: np.ndarray, B: np.ndarray,
                       Gamma_tilde: np.ndarray, eta: float = 2.0) -> np.ndarray:
    """
    Gamma-driver shift condition:
    d_t beta^i = 3/4 * B^i
    d_t B^i = d_t Gamma_tilde^i - eta * B^i
    """
    return 0.75 * B  # Simplified


# =============================================================================
# NR SIMULATION INTERFACE
# =============================================================================

def run_nr_simulation(config: NRConfig,
                      T_final: float = 100.0,
                      M: float = 1.0) -> Dict[str, Any]:
    """
    Run numerical relativity simulation.

    WARNING: STRUCTURAL PLACEHOLDER ONLY!
    ===========================================
    This does NOT integrate Einstein equations.
    The "evolution" returns static/random data.
    Convergence tests will NOT show expected order.
    Use only to verify interface/invariance structure.

    For real NR, integrate with external codes (SpEC, Einstein Toolkit, etc.).

    Args:
        config: NR configuration
        T_final: Final simulation time
        M: Mass parameter

    Returns:
        Dictionary with waveforms and invariants
    """
    N = config.resolution
    t = np.linspace(0, T_final, 1000)
    r = np.linspace(0.1, config.domain_size, N)

    # Placeholder: trivial evolution (no actual dynamics)
    if config.formulation == 'ADM':
        # ADM: evolve gamma_ij and K_ij
        metric_evolution = schwarzschild_3metric_isotropic(r, M)

    elif config.formulation == 'BSSN':
        # BSSN: conformal decomposition
        psi = 1.0 + M / (2.0 * r + 1e-10)
        phi = np.log(psi) / 4.0  # Conformal factor
        metric_evolution = np.ones_like(r)  # Flat conformal metric

    elif config.formulation == 'GHG':
        # Generalized Harmonic: constraint damping
        metric_evolution = schwarzschild_3metric_isotropic(r, M)

    else:
        raise ValueError(f"Unknown formulation: {config.formulation}")

    # Placeholder waveforms (would come from Psi_4 extraction)
    h_plus = 0.1 * M / (r[-1]) * np.sin(2 * np.pi * t / T_final)
    h_cross = 0.1 * M / (r[-1]) * np.cos(2 * np.pi * t / T_final)

    # Physical invariants
    M_ADM = M * (1.0 + 0.001 * np.random.randn())  # Should be M
    J = 0.8 * M ** 2 * (1.0 + 0.001 * np.random.randn())  # Angular momentum
    A_horizon = 16 * np.pi * M ** 2  # Horizon area (Schwarzschild)

    # Constraint violations (should be small)
    H_constraint = config.resolution ** (-2) * np.random.exponential(0.01)
    M_constraint = config.resolution ** (-2) * np.random.exponential(0.01)

    return {
        't': t.tolist(),
        'r': r.tolist(),
        'h_plus': h_plus.tolist(),
        'h_cross': h_cross.tolist(),
        'M_ADM': float(M_ADM),
        'J': float(J),
        'A_horizon': float(A_horizon),
        'H_constraint': float(H_constraint),
        'M_constraint': float(M_constraint),
        'formulation': config.formulation,
        'resolution': config.resolution
    }


# =============================================================================
# SCHEME INVARIANCE TESTING
# =============================================================================

def compare_waveforms(data1: Dict, data2: Dict) -> float:
    """
    Compare gravitational waveforms between two simulations.

    Returns normalized L2 difference.
    """
    t1 = np.array(data1['t'])
    t2 = np.array(data2['t'])
    h1 = np.array(data1['h_plus'])
    h2 = np.array(data2['h_plus'])

    # Interpolate to common time grid
    t_common = np.linspace(max(t1[0], t2[0]), min(t1[-1], t2[-1]), 500)
    h1_interp = np.interp(t_common, t1, h1)
    h2_interp = np.interp(t_common, t2, h2)

    # Normalized difference
    norm = max(np.linalg.norm(h1_interp), 1e-16)
    diff = np.linalg.norm(h1_interp - h2_interp) / norm

    return float(diff)


def scheme_invariance_nr(config_1: NRConfig,
                         config_2: NRConfig,
                         T_final: float = 100.0,
                         M: float = 1.0) -> Tuple[float, Dict]:
    """
    Test scheme invariance between two NR formulations.

    Args:
        config_1, config_2: Two NR configurations
        T_final: Final time
        M: Mass parameter

    Returns:
        invariance_penalty, detailed_results
    """
    data_1 = run_nr_simulation(config_1, T_final, M)
    data_2 = run_nr_simulation(config_2, T_final, M)

    # Compare waveforms
    wf_diff = compare_waveforms(data_1, data_2)

    # Compare physical invariants
    M_diff = abs(data_1['M_ADM'] - data_2['M_ADM'])
    J_diff = abs(data_1['J'] - data_2['J'])
    A_diff = abs(data_1['A_horizon'] - data_2['A_horizon'])

    # Total penalty
    penalty = wf_diff + M_diff / M + J_diff / (M ** 2) + A_diff / (16 * np.pi * M ** 2)

    return float(penalty), {
        'formulations': (config_1.formulation, config_2.formulation),
        'waveform_diff': wf_diff,
        'M_ADM_diff': M_diff,
        'J_diff': J_diff,
        'A_horizon_diff': A_diff,
        'total_penalty': float(penalty),
        'data_1': {k: v for k, v in data_1.items() if k not in ['t', 'r', 'h_plus', 'h_cross']},
        'data_2': {k: v for k, v in data_2.items() if k not in ['t', 'r', 'h_plus', 'h_cross']}
    }


def full_scheme_comparison(resolution: int = 100,
                           domain_size: float = 50.0,
                           M: float = 1.0) -> Dict[str, Any]:
    """
    Compare all three formulations: ADM, BSSN, GHG.
    """
    formulations = ['ADM', 'BSSN', 'GHG']
    configs = {}

    for form in formulations:
        configs[form] = NRConfig(
            formulation=form,
            gauge={'alpha_f': 2.0, 'beta_eta': 2.0},
            resolution=resolution,
            domain_size=domain_size,
            cfl=0.5
        )

    # Run all simulations
    results = {}
    for form, config in configs.items():
        results[form] = run_nr_simulation(config, T_final=100.0, M=M)

    # Pairwise comparisons
    comparisons = []
    for i, form1 in enumerate(formulations):
        for j, form2 in enumerate(formulations):
            if i >= j:
                continue

            penalty, details = scheme_invariance_nr(
                configs[form1], configs[form2], M=M
            )
            comparisons.append({
                'pair': (form1, form2),
                'penalty': penalty,
                'waveform_diff': details['waveform_diff'],
                'M_ADM_diff': details['M_ADM_diff']
            })

    # Summary
    max_penalty = max(c['penalty'] for c in comparisons)
    mean_penalty = np.mean([c['penalty'] for c in comparisons])

    return {
        'formulations': formulations,
        'resolution': resolution,
        'domain_size': domain_size,
        'M': M,
        'comparisons': comparisons,
        'max_penalty': float(max_penalty),
        'mean_penalty': float(mean_penalty),
        'invariants': {
            form: {
                'M_ADM': results[form]['M_ADM'],
                'J': results[form]['J'],
                'A_horizon': results[form]['A_horizon'],
                'constraints': results[form]['H_constraint'] + results[form]['M_constraint']
            }
            for form in formulations
        }
    }


# =============================================================================
# PYMOO OPTIMIZATION
# =============================================================================

if PYMOO_AVAILABLE:
    class NRSchemeOptimization(Problem):
        """
        Multi-objective optimization for NR configurations.

        Objectives:
        1. Minimize scheme invariance penalty
        2. Minimize constraint violations
        3. Minimize runtime/cost (proportional to resolution^3)
        """

        def __init__(self):
            super().__init__(
                n_var=3,  # resolution, domain_size, cfl
                n_obj=3,
                n_constr=0,
                xl=np.array([20, 20.0, 0.1]),
                xu=np.array([200, 100.0, 0.9])
            )

        def _evaluate(self, X, out, *args, **kwargs):
            F = []

            for x in X:
                resolution = int(x[0])
                domain_size = x[1]
                cfl = x[2]

                # Run comparison
                result = full_scheme_comparison(
                    resolution=resolution,
                    domain_size=domain_size
                )

                # Objectives
                f1 = result['mean_penalty']  # Scheme invariance
                f2 = np.mean([inv['constraints']
                             for inv in result['invariants'].values()])  # Constraints
                f3 = (resolution / 100) ** 3  # Cost proxy

                F.append([f1, f2, f3])

            out["F"] = np.array(F)


def optimize_nr_config(n_gen: int = 10, pop_size: int = 20) -> Dict[str, Any]:
    """Run MOO for optimal NR configuration."""
    if not PYMOO_AVAILABLE:
        return {"error": "PyMOO not available"}

    problem = NRSchemeOptimization()

    algorithm = NSGA2(
        pop_size=pop_size,
        sampling=FloatRandomSampling()
    )

    result = minimize(
        problem,
        algorithm,
        ('n_gen', n_gen),
        verbose=False
    )

    return {
        'pareto_front': result.F.tolist() if result.F is not None else [],
        'pareto_solutions': result.X.tolist() if result.X is not None else [],
        'n_pareto': len(result.F) if result.F is not None else 0
    }


# =============================================================================
# CONVERGENCE TESTING
# =============================================================================

def convergence_test(formulation: str = 'BSSN',
                     resolutions: List[int] = [50, 100, 200],
                     M: float = 1.0) -> Dict[str, Any]:
    """
    Test convergence of a formulation as resolution increases.

    Expect: error ~ dx^p where p is the convergence order.

    WARNING: DIAGNOSTIC ONLY
    ========================
    Since run_nr_simulation is a PLACEHOLDER (no actual Einstein evolution),
    the "errors" are random noise, NOT convergent numerical solutions.
    The extracted convergence order will be ~0, NOT the expected ~2.

    This test structure is correct; the physics is missing.
    A real implementation would show p ~ 2 for BSSN with standard finite differences.
    """
    results = []

    for res in resolutions:
        config = NRConfig(
            formulation=formulation,
            gauge={'alpha_f': 2.0, 'beta_eta': 2.0},
            resolution=res,
            domain_size=50.0,
            cfl=0.5
        )

        data = run_nr_simulation(config, M=M)
        results.append({
            'resolution': res,
            'dx': 50.0 / res,
            'M_ADM': data['M_ADM'],
            'H_constraint': data['H_constraint'],
            'M_ADM_error': abs(data['M_ADM'] - M) / M
        })

    # Extract convergence order
    if len(results) >= 2:
        dx = np.array([r['dx'] for r in results])
        error = np.array([r['M_ADM_error'] for r in results])

        # Fit log(error) = log(C) + p * log(dx)
        if np.all(error > 0) and np.all(dx > 0):
            log_dx = np.log(dx)
            log_error = np.log(error + 1e-16)
            p, log_C = np.polyfit(log_dx, log_error, 1)
            convergence_order = p
        else:
            convergence_order = 0.0
    else:
        convergence_order = 0.0

    return {
        'formulation': formulation,
        'resolutions': resolutions,
        'results': results,
        'convergence_order': float(convergence_order),
        'expected_order': 2.0 if formulation == 'BSSN' else 1.0,
        'note': 'Placeholder simulation - real convergence needs actual evolution'
    }


# =============================================================================
# MAIN DEMO
# =============================================================================

def run_phase2_nr_demo() -> Dict[str, Any]:
    """
    Run complete Phase-II numerical relativity demonstration.
    """
    print("=" * 60)
    print("PHASE-II: Numerical Relativity Scheme Invariance")
    print("=" * 60)

    results = {}

    # 1. Full scheme comparison
    print("\n1. Comparing ADM vs BSSN vs GHG formulations...")

    comparison = full_scheme_comparison(resolution=100, M=1.0)
    results['scheme_comparison'] = comparison

    print(f"   Formulations: {comparison['formulations']}")
    print(f"   Max penalty: {comparison['max_penalty']:.4e}")
    print(f"   Mean penalty: {comparison['mean_penalty']:.4e}")

    for comp in comparison['comparisons']:
        print(f"   {comp['pair']}: penalty = {comp['penalty']:.4e}")

    # 2. Physical invariants
    print("\n2. Physical invariants across formulations...")

    for form, inv in comparison['invariants'].items():
        print(f"   {form}: M_ADM = {inv['M_ADM']:.4f}, J = {inv['J']:.4f}")

    # 3. Convergence test
    print("\n3. Convergence test for BSSN formulation...")

    conv_test = convergence_test('BSSN', [50, 100, 200])
    results['convergence'] = conv_test

    print(f"   Resolutions tested: {conv_test['resolutions']}")
    print(f"   Convergence order: {conv_test['convergence_order']:.2f}")
    print(f"   Expected order: {conv_test['expected_order']:.1f}")

    # 4. MOO optimization (if available)
    if PYMOO_AVAILABLE:
        print("\n4. Running PyMOO optimization for optimal NR config...")

        moo_result = optimize_nr_config(n_gen=5, pop_size=10)
        results['moo_optimization'] = moo_result

        print(f"   Pareto front size: {moo_result['n_pareto']}")
    else:
        print("\n4. PyMOO not available - skipping optimization")
        results['moo_optimization'] = {'status': 'PyMOO not installed'}

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("- ADM, BSSN, GHG formulations compared")
    print("- Physical invariants (M_ADM, J, A) extracted")
    print("- Convergence scaling tested")
    print("- NOTE: Placeholder evolution - needs real Einstein solver")
    print("=" * 60)

    return results


if __name__ == "__main__":
    results = run_phase2_nr_demo()

    # Save results
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "phase2_nr_results.json")

    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {output_path}")
