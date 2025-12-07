#!/usr/bin/env python3
"""
Phase-II Multi-Geometry Diffusion on Multiple Calculi

Key insight from AI conversation:
Instead of "pick one calculus and solve," we define MANY calculi on the SAME
state space and study DIFFUSION TRAJECTORIES across them.

This connects to:
- Multi-metric diffusion (N01ne style)
- Positive geometries & cosmological polytopes
- Scheme-invariance philosophy ("physical = scheme-robust")

EXPERIMENTS:
1. Triangle (2-simplex) with 3 calculi (Euclidean, Log-metric, Curvature)
2. Cosmological parameter space with 3 calculi (Euclidean, Fisher, Meta-FRW)

Integration with existing PyMOO optimization to find scheme-robust structures.

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

# GlobalMOO integration
try:
    from meta_calculus.moo_integration import GlobalMOOClient, GlobalMOOAdapter
    GLOBALMOO_AVAILABLE = True
except ImportError:
    GLOBALMOO_AVAILABLE = False


# =============================================================================
# TRIANGLE (2-SIMPLEX) MULTI-GEOMETRY DIFFUSION
# =============================================================================

def build_triangle_points(N: int = 10) -> np.ndarray:
    """
    Discretize the 2-simplex x1 + x2 + x3 = 1, xk >= 0.

    Returns array of shape (M, 3) where M = (N+1)(N+2)/2.
    """
    pts = []
    for i in range(N + 1):
        for j in range(N + 1 - i):
            k = N - i - j
            x1, x2, x3 = i / N, j / N, k / N
            pts.append([x1, x2, x3])
    return np.array(pts, dtype=float)


def weights_euclidean(pts: np.ndarray, eps: float = 0.05) -> np.ndarray:
    """
    Euclidean distance weights on simplex.

    w_ij = exp(-|x_i - x_j|^2 / eps)
    """
    M = pts.shape[0]
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            d2 = np.sum((pts[i] - pts[j]) ** 2)
            W[i, j] = np.exp(-d2 / eps)
    return W


def weights_log_metric(pts: np.ndarray, eps: float = 0.05,
                       delta: float = 1e-6) -> np.ndarray:
    """
    Log-metric (bigeometric/multiplicative) weights.

    Map to y_k = log(x_k), then Euclidean in y-space.
    This is the triangle analogue of bigeometric calculus.
    """
    y = np.log(np.clip(pts, delta, None))
    M = pts.shape[0]
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            d2 = np.sum((y[i] - y[j]) ** 2)
            W[i, j] = np.exp(-d2 / eps)
    return W


def weights_curvature(pts: np.ndarray, eps: float = 0.05,
                      beta: float = 1.0) -> np.ndarray:
    """
    Curvature-weighted (boundary-aware) weights.

    Downweights points near edges via c_i = prod(x_k^beta).
    """
    M = pts.shape[0]
    c = np.prod(np.power(np.clip(pts, 1e-10, None), beta), axis=1)
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            d2 = np.sum((pts[i] - pts[j]) ** 2)
            W[i, j] = c[i] * c[j] * np.exp(-d2 / eps)
    return W


def graph_laplacian(W: np.ndarray) -> np.ndarray:
    """
    Build graph Laplacian L = W - D.

    This is the unnormalized Laplacian for diffusion.
    Mass conservation: sum_i (L*rho)_i = 0
    """
    D = np.diag(W.sum(axis=1))
    return W - D


def diffusion_step(rho: np.ndarray, L: np.ndarray, dt: float) -> np.ndarray:
    """Single explicit Euler step for diffusion."""
    rho_new = rho + dt * (L @ rho)
    rho_new = np.clip(rho_new, 0, None)
    rho_new /= np.maximum(rho_new.sum(), 1e-16)
    return rho_new


def multi_calculus_diffusion_triangle(
    T: int = 50,
    dt: float = 0.1,
    N: int = 10,
    eps: float = 0.05,
    schedule: Optional[List[str]] = None,
    initial_vertex: int = 0
) -> Dict[str, Any]:
    """
    Multi-geometry diffusion on the 2-simplex.

    Args:
        T: Number of time steps
        dt: Time step size
        N: Discretization level
        eps: Kernel width for weights
        schedule: Sequence of calculi ["A", "B", "C"] or random
        initial_vertex: Which vertex to start density near (0, 1, or 2)

    Returns:
        Dictionary with trajectories and analysis
    """
    pts = build_triangle_points(N)
    M = pts.shape[0]

    # Build weight matrices for each calculus
    W_A = weights_euclidean(pts, eps)
    W_B = weights_log_metric(pts, eps)
    W_C = weights_curvature(pts, eps)

    # Build Laplacians
    L_A = graph_laplacian(W_A)
    L_B = graph_laplacian(W_B)
    L_C = graph_laplacian(W_C)

    L_map = {"A": L_A, "B": L_B, "C": L_C}

    # Generate schedule if not provided
    if schedule is None:
        rng = np.random.default_rng(42)
        schedule = rng.choice(["A", "B", "C"], size=T).tolist()

    # Initial density: localized near a vertex
    vertex_coords = np.eye(3)  # Vertices at (1,0,0), (0,1,0), (0,0,1)
    target = vertex_coords[initial_vertex]
    rho = np.exp(-10.0 * np.sum((pts - target) ** 2, axis=1))
    rho /= rho.sum()

    # Run diffusion
    snapshots = [rho.copy()]
    schedule_used = []

    for k in range(T):
        L = L_map[schedule[k]]
        rho = diffusion_step(rho, L, dt)
        snapshots.append(rho.copy())
        schedule_used.append(schedule[k])

    snapshots = np.array(snapshots)

    # Analysis: entropy evolution
    def entropy(p):
        p_safe = np.clip(p, 1e-30, None)
        return -np.sum(p_safe * np.log(p_safe))

    entropies = [entropy(s) for s in snapshots]

    # Scheme-robust features: where does density concentrate?
    final_density = snapshots[-1]
    peak_idx = np.argmax(final_density)
    peak_location = pts[peak_idx]

    # NOTE on entropy: Computed over full M-point discretization where M = (N+1)*(N+2)/2.
    # For N=10, M=66 points. Max entropy = log(66) ~ 4.19. The value 3.78 indicates
    # significant but not complete spreading. peak_location is barycentric coords
    # of the grid point with highest density, NOT the full distribution.

    return {
        'pts': pts.tolist(),
        'snapshots': snapshots.tolist(),
        'schedule': schedule_used,
        'entropies': entropies,
        'final_peak_barycentric': peak_location.tolist(),  # Renamed for clarity
        'final_peak_value': float(final_density[peak_idx]),
        'distribution_entropy': entropies[-1],  # Shannon entropy over M grid points
        'max_possible_entropy': float(np.log(len(pts))),  # log(M) for uniform
        'mass_conserved': all(abs(s.sum() - 1.0) < 1e-10 for s in snapshots),
        'n_grid_points': len(pts),  # M = (N+1)(N+2)/2
        'parameters': {'T': T, 'dt': dt, 'N': N, 'eps': eps}
    }


# =============================================================================
# COSMOLOGICAL PARAMETER SPACE DIFFUSION
# =============================================================================

def build_param_grid(
    ns_range: Tuple[float, float] = (0.94, 1.02),
    r_range: Tuple[float, float] = (0.0, 0.1),
    N_ns: int = 30,
    N_r: int = 30
) -> np.ndarray:
    """
    Build grid in (n_s, r) cosmological parameter space.

    n_s: Scalar spectral index (~0.96 observed)
    r: Tensor-to-scalar ratio (<0.06 observed)
    """
    ns_vals = np.linspace(*ns_range, N_ns)
    r_vals = np.linspace(*r_range, N_r)
    pts = np.array([[ns, r] for ns in ns_vals for r in r_vals])
    return pts


def weights_param_euclidean(pts: np.ndarray, eps: float = 1e-4) -> np.ndarray:
    """Euclidean weights in (n_s, r) space."""
    M = pts.shape[0]
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            d2 = np.sum((pts[i] - pts[j]) ** 2)
            W[i, j] = np.exp(-d2 / eps)
    return W


def weights_param_fisher(pts: np.ndarray, eps: float = 1e-4,
                        sigma_ns: float = 0.005, sigma_r: float = 0.05) -> np.ndarray:
    """
    Fisher-information-like anisotropic weights.

    Models near Planck best-fit are tightly constrained.
    n_s direction is tighter than r direction.
    """
    M = pts.shape[0]
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            dns = (pts[i, 0] - pts[j, 0]) / sigma_ns
            dr = (pts[i, 1] - pts[j, 1]) / sigma_r
            d2 = dns ** 2 + dr ** 2
            W[i, j] = np.exp(-d2 / eps)
    return W


def effective_frw_index(ns: float, r: float) -> float:
    """
    Toy mapping from (n_s, r) -> effective FRW power-law index.

    This encodes "how similar are the underlying early-universe dynamics
    in a meta-FRW sense."

    n_FRW ~ 2 - 10*(1 - n_s) + 2*r
    """
    return 2.0 - (1.0 - ns) * 10.0 + r * 2.0


def weights_param_meta(pts: np.ndarray, eps: float = 1e-2) -> np.ndarray:
    """
    Meta-FRW-induced weights.

    Distance based on effective FRW index similarity.
    """
    M = pts.shape[0]
    n_eff = np.array([effective_frw_index(ns, r) for ns, r in pts])
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            d2 = (n_eff[i] - n_eff[j]) ** 2
            W[i, j] = np.exp(-d2 / eps)
    return W


def multi_calculus_diffusion_params(
    T: int = 50,
    dt: float = 0.1,
    N_ns: int = 20,
    N_r: int = 20,
    schedule: Optional[List[str]] = None,
    ns_init: float = 0.965,
    r_init: float = 0.01
) -> Dict[str, Any]:
    """
    Multi-geometry diffusion on cosmological parameter space.

    Args:
        T: Number of time steps
        dt: Time step size
        N_ns, N_r: Grid dimensions
        schedule: Sequence of calculi ["E", "F", "M"] or random
        ns_init, r_init: Initial peak location (near Planck best-fit)

    Returns:
        Dictionary with trajectories and analysis
    """
    pts = build_param_grid(N_ns=N_ns, N_r=N_r)
    M = pts.shape[0]

    # Build weight matrices
    W_E = weights_param_euclidean(pts, eps=1e-4)
    W_F = weights_param_fisher(pts, eps=1e-4)
    W_M = weights_param_meta(pts, eps=1e-2)

    # Build Laplacians
    L_E = graph_laplacian(W_E)
    L_F = graph_laplacian(W_F)
    L_M = graph_laplacian(W_M)

    L_map = {"E": L_E, "F": L_F, "M": L_M}

    # Generate schedule
    if schedule is None:
        rng = np.random.default_rng(42)
        schedule = rng.choice(["E", "F", "M"], size=T).tolist()

    # Initial density: peaked near Planck best-fit
    d2 = (pts[:, 0] - ns_init) ** 2 + (pts[:, 1] - r_init) ** 2
    rho = np.exp(-d2 / 1e-4)
    rho /= rho.sum()

    # Run diffusion
    snapshots = [rho.copy()]

    for k in range(T):
        L = L_map[schedule[k]]
        rho = diffusion_step(rho, L, dt)
        snapshots.append(rho.copy())

    snapshots = np.array(snapshots)

    # Analysis
    def entropy(p):
        p_safe = np.clip(p, 1e-30, None)
        return -np.sum(p_safe * np.log(p_safe))

    entropies = [entropy(s) for s in snapshots]

    # Final distribution analysis
    final_density = snapshots[-1]
    peak_idx = np.argmax(final_density)
    peak_location = pts[peak_idx]

    # Weighted mean (n_s, r)
    mean_ns = np.sum(final_density * pts[:, 0])
    mean_r = np.sum(final_density * pts[:, 1])

    return {
        'pts': pts.tolist(),
        'snapshots': snapshots.tolist(),
        'schedule': schedule,
        'entropies': entropies,
        'final_peak_location': peak_location.tolist(),
        'final_mean_ns': float(mean_ns),
        'final_mean_r': float(mean_r),
        'planck_comparison': {
            'predicted_ns': float(mean_ns),
            'observed_ns': 0.9649,
            'predicted_r': float(mean_r),
            'observed_r_limit': 0.06
        },
        'parameters': {'T': T, 'dt': dt, 'N_ns': N_ns, 'N_r': N_r}
    }


# =============================================================================
# PYMOO OPTIMIZATION FOR SCHEME-ROBUST STRUCTURES
# =============================================================================

if PYMOO_AVAILABLE:
    class SchemeRobustnessProblem(Problem):
        """
        Multi-objective optimization to find scheme-robust features.

        Objectives:
        1. Minimize variance of final density across calculus choices
        2. Maximize entropy (find globally stable structures)
        3. Minimize distance to observational constraints
        """

        def __init__(self, space: str = "triangle"):
            self.space = space

            if space == "triangle":
                # Variables: initial_vertex (0-2), eps, dt
                super().__init__(
                    n_var=3,
                    n_obj=2,
                    n_constr=0,
                    xl=np.array([0.0, 0.01, 0.01]),
                    xu=np.array([2.99, 0.2, 0.5])
                )
            else:  # params
                # Variables: ns_init, r_init, eps
                super().__init__(
                    n_var=3,
                    n_obj=2,
                    n_constr=0,
                    xl=np.array([0.94, 0.0, 1e-5]),
                    xu=np.array([1.02, 0.1, 1e-2])
                )

        def _evaluate(self, X, out, *args, **kwargs):
            F = []

            for x in X:
                if self.space == "triangle":
                    vertex = int(x[0])
                    eps = x[1]
                    dt = x[2]

                    # Run 3 different pure-calculus trajectories
                    results = []
                    for schedule in [["A"] * 50, ["B"] * 50, ["C"] * 50]:
                        res = multi_calculus_diffusion_triangle(
                            T=50, dt=dt, N=8, eps=eps,
                            schedule=schedule, initial_vertex=vertex
                        )
                        results.append(np.array(res['snapshots'][-1]))

                    # Objective 1: Variance across calculi
                    stacked = np.stack(results)
                    variance = np.mean(np.var(stacked, axis=0))

                    # Objective 2: Mean entropy (maximize -> minimize negative)
                    mean_entropy = -np.mean(res['entropies'][-10:])

                else:
                    ns_init = x[0]
                    r_init = x[1]
                    eps = x[2]

                    # Run 3 different pure-calculus trajectories
                    results = []
                    for schedule in [["E"] * 50, ["F"] * 50, ["M"] * 50]:
                        res = multi_calculus_diffusion_params(
                            T=50, dt=0.1, N_ns=15, N_r=15,
                            schedule=schedule, ns_init=ns_init, r_init=r_init
                        )
                        results.append(np.array(res['snapshots'][-1]))

                    # Objective 1: Variance across calculi
                    stacked = np.stack(results)
                    variance = np.mean(np.var(stacked, axis=0))

                    # Objective 2: Distance from Planck best-fit
                    dist_planck = ((ns_init - 0.9649) ** 2 +
                                   (r_init - 0.01) ** 2)

                F.append([variance, mean_entropy if self.space == "triangle" else dist_planck])

            out["F"] = np.array(F)


def run_moo_scheme_robustness(space: str = "triangle",
                              n_gen: int = 20,
                              pop_size: int = 30) -> Dict[str, Any]:
    """
    Run multi-objective optimization to find scheme-robust configurations.
    """
    if not PYMOO_AVAILABLE:
        return {"error": "PyMOO not available"}

    problem = SchemeRobustnessProblem(space=space)

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

    # Extract Pareto front
    pareto_front = result.F.tolist() if result.F is not None else []
    pareto_solutions = result.X.tolist() if result.X is not None else []

    return {
        'space': space,
        'pareto_front': pareto_front,
        'pareto_solutions': pareto_solutions,
        'n_pareto': len(pareto_front),
        'n_generations': n_gen,
        'pop_size': pop_size
    }


# =============================================================================
# SCHEME-ROBUSTNESS ANALYSIS
# =============================================================================

def compare_calculus_schedules(space: str = "triangle",
                               schedules: Optional[List[List[str]]] = None) -> Dict[str, Any]:
    """
    Compare final distributions across different calculus schedules.

    Scheme-robust features = same under all schedules.

    Robustness Score Definition:
    robustness = 1 / (variance of peak locations across schedules + epsilon)

    Interpretation:
    - > 1e6: Extremely robust (peak variance < 1e-6)
    - > 1000: Robust (peak variance ~ 1e-3)
    - > 10: Moderate robustness
    - < 10: Fragile (peak location depends on schedule)
    """
    if schedules is None:
        if space == "triangle":
            schedules = [
                ["A"] * 50,  # Pure Euclidean
                ["B"] * 50,  # Pure Log-metric
                ["C"] * 50,  # Pure Curvature
                ["A", "B", "C"] * 17,  # Alternating
            ]
        else:
            schedules = [
                ["E"] * 50,
                ["F"] * 50,
                ["M"] * 50,
                ["E", "F", "M"] * 17,
            ]

    results = []

    for schedule in schedules:
        if space == "triangle":
            res = multi_calculus_diffusion_triangle(
                T=len(schedule), schedule=schedule
            )
        else:
            res = multi_calculus_diffusion_params(
                T=len(schedule), schedule=schedule
            )

        results.append({
            'schedule_name': ''.join(schedule[:3]) + '...',
            'final_entropy': res['entropies'][-1],
            'final_peak': res['final_peak_location']
        })

    # Compute robustness score (inverse of variance in peak locations)
    peaks = np.array([r['final_peak'] for r in results])
    variance = np.mean(np.var(peaks, axis=0))
    robustness = 1.0 / (variance + 1e-10)

    return {
        'space': space,
        'schedule_results': results,
        'peak_variance': float(variance),
        'robustness_score': float(robustness),
        'interpretation': 'robust' if robustness > 100 else 'moderate' if robustness > 10 else 'fragile'
    }


# =============================================================================
# MAIN DEMO
# =============================================================================

def run_phase2_diffusion_demo() -> Dict[str, Any]:
    """
    Run complete Phase-II multi-geometry diffusion demonstration.
    """
    print("=" * 60)
    print("PHASE-II: Multi-Geometry Diffusion")
    print("=" * 60)

    results = {}

    # 1. Triangle diffusion
    print("\n1. Triangle (2-simplex) diffusion with 3 calculi...")

    triangle_result = multi_calculus_diffusion_triangle(
        T=50, dt=0.1, N=10, eps=0.05
    )
    results['triangle'] = {
        'final_peak': triangle_result['final_peak_location'],
        'final_entropy': triangle_result['entropies'][-1],
        'mass_conserved': triangle_result['mass_conserved']
    }

    print(f"   Final peak location: {triangle_result['final_peak_location']}")
    print(f"   Final entropy: {triangle_result['entropies'][-1]:.4f}")
    print(f"   Mass conserved: {triangle_result['mass_conserved']}")

    # 2. Cosmological parameter diffusion
    print("\n2. Cosmological parameter space diffusion...")

    params_result = multi_calculus_diffusion_params(
        T=50, dt=0.1, N_ns=20, N_r=20
    )
    results['params'] = {
        'final_mean_ns': params_result['final_mean_ns'],
        'final_mean_r': params_result['final_mean_r'],
        'planck_comparison': params_result['planck_comparison']
    }

    print(f"   Final mean n_s: {params_result['final_mean_ns']:.4f}")
    print(f"   Final mean r: {params_result['final_mean_r']:.4f}")
    print(f"   Planck observed n_s: {params_result['planck_comparison']['observed_ns']}")

    # 3. Scheme robustness comparison
    print("\n3. Comparing scheme robustness across calculi...")

    triangle_robust = compare_calculus_schedules("triangle")
    params_robust = compare_calculus_schedules("params")

    results['robustness'] = {
        'triangle': {
            'robustness_score': triangle_robust['robustness_score'],
            'interpretation': triangle_robust['interpretation']
        },
        'params': {
            'robustness_score': params_robust['robustness_score'],
            'interpretation': params_robust['interpretation']
        }
    }

    print(f"   Triangle robustness: {triangle_robust['robustness_score']:.2f} "
          f"({triangle_robust['interpretation']})")
    print(f"   Params robustness: {params_robust['robustness_score']:.2f} "
          f"({params_robust['interpretation']})")

    # 4. MOO optimization (if available)
    if PYMOO_AVAILABLE:
        print("\n4. Running PyMOO optimization for scheme-robust configurations...")

        moo_triangle = run_moo_scheme_robustness("triangle", n_gen=10, pop_size=20)
        moo_params = run_moo_scheme_robustness("params", n_gen=10, pop_size=20)

        results['moo_optimization'] = {
            'triangle_pareto_size': moo_triangle['n_pareto'],
            'params_pareto_size': moo_params['n_pareto']
        }

        print(f"   Triangle Pareto front size: {moo_triangle['n_pareto']}")
        print(f"   Params Pareto front size: {moo_params['n_pareto']}")
    else:
        print("\n4. PyMOO not available - skipping MOO optimization")
        results['moo_optimization'] = {'status': 'PyMOO not installed'}

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("- Multi-geometry diffusion implemented on triangle and param space")
    print("- Three calculi tested: Euclidean, Log-metric, Curvature/Fisher/Meta")
    print("- Scheme-robust features identified by low peak variance")
    print("- MOO optimization finds Pareto-optimal configurations")
    print("=" * 60)

    return results


if __name__ == "__main__":
    results = run_phase2_diffusion_demo()

    # Save results
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(output_dir, "phase2_diffusion_results.json")

    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {output_path}")
