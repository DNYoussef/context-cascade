"""
meta_calculus/quantum/multi_calculus_state_diffusion.py

Quantum-Flavored Multi-Calculus Diffusion

This wraps the generic Δ^2 multi-calculus diffusion experiment and
reinterprets it as acting on diagonal qutrit density matrices:

    - Each point p = (p1, p2, p3) in Δ^2 represents rho = diag(p1, p2, p3)
    - Different CalculusEmbedding choices define different "metrics"
      on the space of diagonal states.
    - Diffusion operators approximate a kind of coarse-grained
      quantum state mixing under each calculus.

The metrics mirror the classical cosmology simulator, but now on a
"quantum state space" instead of FRW parameter space.

Usage:
    from meta_calculus.quantum import run_quantum_flavored_diffusion

    metrics = run_quantum_flavored_diffusion(num_points=300, num_steps=20)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import numpy as np

# Import the general Δ^2 diffusion machinery
from meta_calculus.experiments.multi_calculus_diffusion import (
    sample_simplex_points,
    CalculusEmbedding,
    build_affinity_and_laplacian,
    build_diffusion_operator,
    run_diffusion,
    run_multi_calculus_trajectory,
    run_averaged_diffusion,
    normalized_entropy,
    cluster_variance_along_signal,
    silhouette_score_simple,
    compute_spectral_gap,
    compute_effective_spectral_gap,
    find_multi_calculus_invariants,
)


@dataclass
class QuantumDiffusionConfig:
    """Configuration for quantum-flavored diffusion experiment."""
    num_points: int = 300
    num_clusters: int = 3
    cluster_spread: float = 0.07
    noise_fraction: float = 0.2
    num_steps: int = 20
    step_size: float = 0.5
    seed: int = 0

    # Calculus parameters
    log_eps: float = 1e-6
    power_gamma: float = 0.3

    # Curvature weights - can be tied to physics constraints
    curvature_weights: np.ndarray = field(default_factory=lambda: np.diag([1.0, 1.3, 0.7]))


@dataclass
class QuantumDiffusionResults:
    """Results from quantum-flavored diffusion experiment."""
    # Points and labels (interpreted as diagonal density matrices)
    points: np.ndarray  # (N, 3) - each row is diag(rho)
    labels: np.ndarray

    # Calculi and operators
    calculi: List[CalculusEmbedding]
    diffusion_operators: List[np.ndarray]

    # Spectral analysis
    spectral_gaps: Dict[str, float] = field(default_factory=dict)
    effective_gap: float = 0.0

    # Diffusion results
    single_calculus_metrics: Dict[str, Dict[str, float]] = field(default_factory=dict)
    averaged_metrics: Dict[str, float] = field(default_factory=dict)
    multi_cyclic_metrics: Dict[str, float] = field(default_factory=dict)
    multi_random_metrics: Dict[str, float] = field(default_factory=dict)

    # Invariant analysis (scheme-robust quantum states)
    invariant_scores: np.ndarray = field(default_factory=lambda: np.array([]))

    # Trajectories for visualization
    trajectories: Dict[str, np.ndarray] = field(default_factory=dict)


def run_quantum_flavored_diffusion(
    num_points: int = 300,
    num_steps: int = 20,
    seed: Optional[int] = 0,
) -> Dict[str, Dict[str, float]]:
    """
    Run the Δ^2 multi-calculus diffusion experiment and interpret it
    as diffusion on diagonal qutrit density matrices.

    We:
        - Sample clustered points p on the simplex (as in FRW experiments),
        - Define 4 calculi / metrics:
            * classical (identity embedding)
            * log (ratio-sensitive)
            * power (emphasize mid vs extremes)
            * curvature-weighted (slot in FRW-based weights)
        - Build diffusion operators for each,
        - Run:
            * single-calculus diffusion,
            * multi-calculus cyclic trajectory,
            * multi-calculus random trajectory.

    We then measure:
        - final_normalized_entropy: how spread out the signal is
        - final_cluster_variance: how well cluster structure survives

    These are direct analogues of "scheme robustness" on the cosmology side.

    Parameters
    ----------
    num_points : int
        Number of quantum states to sample.
    num_steps : int
        Number of diffusion steps.
    seed : int, optional
        Random seed.

    Returns
    -------
    results : dict
        Dictionary of metrics per method.
    """
    P, labels = sample_simplex_points(
        num_points=num_points,
        num_clusters=3,
        cluster_spread=0.07,
        noise_fraction=0.2,
        seed=seed,
    )
    N = P.shape[0]

    # Example curvature weights; you can tie W_curv to FRW / meta-Friedmann
    # constraints or scheme-robustness scores.
    W_curv = np.diag([1.0, 1.3, 0.7])

    calculi = [
        CalculusEmbedding(name="classical", kind="classical"),
        CalculusEmbedding(name="log", kind="log", params={"eps": 1e-6}),
        CalculusEmbedding(name="power", kind="power", params={"gamma": 0.3}),
        CalculusEmbedding(name="curvature", kind="curvature", params={"W": W_curv}),
    ]

    P_list = []
    spectral_gaps = {}
    for calc in calculi:
        Z = calc.embed(P)
        _, L = build_affinity_and_laplacian(Z, normalized=True)
        P_k = build_diffusion_operator(L, step_size=0.5)
        P_list.append(P_k)
        spectral_gaps[calc.name] = compute_spectral_gap(L)

    # Effective spectral gap for multi-calculus
    effective_gap = compute_effective_spectral_gap(P_list, num_cycles=1)

    # Initial signal: emphasize cluster 0 (think of it as one "phase" or sector)
    rng = np.random.default_rng(seed)
    idx_cluster0 = np.where(labels == 0)[0]
    f0 = np.zeros(N)
    if len(idx_cluster0) > 0:
        f0[idx_cluster0] = 1.0
    else:
        f0[rng.integers(low=0, high=N)] = 1.0

    results: Dict[str, Dict[str, float]] = {}

    # Single-calculus diffusion
    for calc, Pk in zip(calculi, P_list):
        traj = run_diffusion(Pk, f0, num_steps=num_steps)
        fT = traj[-1]
        results[f"single_{calc.name}"] = {
            "final_normalized_entropy": normalized_entropy(fT),
            "final_cluster_variance": cluster_variance_along_signal(fT, labels),
            "silhouette_score": silhouette_score_simple(calc.embed(P), labels),
            "spectral_gap": spectral_gaps[calc.name],
        }

    # Averaged operator
    traj_avg = run_averaged_diffusion(P_list, f0, num_steps)
    fT_avg = traj_avg[-1]
    results["averaged"] = {
        "final_normalized_entropy": normalized_entropy(fT_avg),
        "final_cluster_variance": cluster_variance_along_signal(fT_avg, labels),
    }

    # Multi-calculus: cyclic
    traj_cyc, _ = run_multi_calculus_trajectory(
        P_list=P_list,
        f0=f0,
        num_steps=num_steps,
        mode="cyclic",
        seed=seed,
    )
    fT_cyc = traj_cyc[-1]
    results["multi_cyclic"] = {
        "final_normalized_entropy": normalized_entropy(fT_cyc),
        "final_cluster_variance": cluster_variance_along_signal(fT_cyc, labels),
        "effective_spectral_gap": effective_gap,
    }

    # Multi-calculus: random
    traj_rand, _ = run_multi_calculus_trajectory(
        P_list=P_list,
        f0=f0,
        num_steps=num_steps,
        mode="random",
        seed=seed,
    )
    fT_rand = traj_rand[-1]
    results["multi_random"] = {
        "final_normalized_entropy": normalized_entropy(fT_rand),
        "final_cluster_variance": cluster_variance_along_signal(fT_rand, labels),
    }

    # Add spectral info as a separate key
    results["spectral"] = {
        **{f"gap_{k}": v for k, v in spectral_gaps.items()},
        "effective_gap": effective_gap,
    }

    return results


def run_full_quantum_diffusion_analysis(
    config: QuantumDiffusionConfig,
) -> QuantumDiffusionResults:
    """
    Run comprehensive quantum-flavored diffusion analysis.

    Parameters
    ----------
    config : QuantumDiffusionConfig
        Experiment configuration.

    Returns
    -------
    results : QuantumDiffusionResults
        Complete results object.
    """
    P, labels = sample_simplex_points(
        num_points=config.num_points,
        num_clusters=config.num_clusters,
        cluster_spread=config.cluster_spread,
        noise_fraction=config.noise_fraction,
        seed=config.seed,
    )
    N = P.shape[0]

    calculi = [
        CalculusEmbedding(name="classical", kind="classical"),
        CalculusEmbedding(name="log", kind="log", params={"eps": config.log_eps}),
        CalculusEmbedding(name="power", kind="power", params={"gamma": config.power_gamma}),
        CalculusEmbedding(name="curvature", kind="curvature", params={"W": config.curvature_weights}),
    ]

    P_list = []
    L_list = []
    spectral_gaps = {}

    for calc in calculi:
        Z = calc.embed(P)
        _, L = build_affinity_and_laplacian(Z, normalized=True)
        P_k = build_diffusion_operator(L, step_size=config.step_size)
        P_list.append(P_k)
        L_list.append(L)
        spectral_gaps[calc.name] = compute_spectral_gap(L)

    effective_gap = compute_effective_spectral_gap(P_list, num_cycles=1)

    # Initial signal
    rng = np.random.default_rng(config.seed)
    idx_cluster0 = np.where(labels == 0)[0]
    f0 = np.zeros(N)
    if len(idx_cluster0) > 0:
        f0[idx_cluster0] = 1.0
    else:
        f0[rng.integers(low=0, high=N)] = 1.0

    single_calculus_metrics = {}
    trajectories = {}

    for calc, Pk in zip(calculi, P_list):
        traj = run_diffusion(Pk, f0, num_steps=config.num_steps)
        fT = traj[-1]
        single_calculus_metrics[calc.name] = {
            "final_normalized_entropy": normalized_entropy(fT),
            "final_cluster_variance": cluster_variance_along_signal(fT, labels),
            "silhouette_score": silhouette_score_simple(calc.embed(P), labels),
        }
        trajectories[f"single_{calc.name}"] = traj

    # Averaged
    traj_avg = run_averaged_diffusion(P_list, f0, config.num_steps)
    fT_avg = traj_avg[-1]
    averaged_metrics = {
        "final_normalized_entropy": normalized_entropy(fT_avg),
        "final_cluster_variance": cluster_variance_along_signal(fT_avg, labels),
    }
    trajectories["averaged"] = traj_avg

    # Multi-calculus cyclic
    traj_cyc, _ = run_multi_calculus_trajectory(
        P_list, f0, config.num_steps, mode="cyclic", seed=config.seed
    )
    fT_cyc = traj_cyc[-1]
    multi_cyclic_metrics = {
        "final_normalized_entropy": normalized_entropy(fT_cyc),
        "final_cluster_variance": cluster_variance_along_signal(fT_cyc, labels),
    }
    trajectories["multi_cyclic"] = traj_cyc

    # Multi-calculus random
    traj_rand, _ = run_multi_calculus_trajectory(
        P_list, f0, config.num_steps, mode="random", seed=config.seed
    )
    fT_rand = traj_rand[-1]
    multi_random_metrics = {
        "final_normalized_entropy": normalized_entropy(fT_rand),
        "final_cluster_variance": cluster_variance_along_signal(fT_rand, labels),
    }
    trajectories["multi_random"] = traj_rand

    # Find invariants
    invariant_scores = find_multi_calculus_invariants(P_list)

    return QuantumDiffusionResults(
        points=P,
        labels=labels,
        calculi=calculi,
        diffusion_operators=P_list,
        spectral_gaps=spectral_gaps,
        effective_gap=effective_gap,
        single_calculus_metrics=single_calculus_metrics,
        averaged_metrics=averaged_metrics,
        multi_cyclic_metrics=multi_cyclic_metrics,
        multi_random_metrics=multi_random_metrics,
        invariant_scores=invariant_scores,
        trajectories=trajectories,
    )


def print_quantum_diffusion_summary(results: Dict[str, Dict[str, float]]) -> None:
    """Print formatted summary of quantum diffusion results."""
    print("=" * 60)
    print("QUANTUM STATE-SPACE DIFFUSION RESULTS")
    print("=" * 60)

    if "spectral" in results:
        print("\n--- Spectral Gaps ---")
        for k, v in results["spectral"].items():
            print(f"  {k}: {v:.4f}")

    print("\n--- Single-Calculus Diffusion ---")
    for name, metrics in results.items():
        if name.startswith("single_"):
            calc_name = name.replace("single_", "")
            print(f"  {calc_name}:")
            print(f"    entropy: {metrics['final_normalized_entropy']:.4f}")
            print(f"    cluster_var: {metrics['final_cluster_variance']:.6f}")

    if "averaged" in results:
        print("\n--- Averaged Operator ---")
        print(f"    entropy: {results['averaged']['final_normalized_entropy']:.4f}")
        print(f"    cluster_var: {results['averaged']['final_cluster_variance']:.6f}")

    if "multi_cyclic" in results:
        print("\n--- Multi-Calculus (Cyclic) ---")
        print(f"    entropy: {results['multi_cyclic']['final_normalized_entropy']:.4f}")
        print(f"    cluster_var: {results['multi_cyclic']['final_cluster_variance']:.6f}")

    if "multi_random" in results:
        print("\n--- Multi-Calculus (Random) ---")
        print(f"    entropy: {results['multi_random']['final_normalized_entropy']:.4f}")
        print(f"    cluster_var: {results['multi_random']['final_cluster_variance']:.6f}")

    print("=" * 60)


if __name__ == "__main__":
    metrics = run_quantum_flavored_diffusion()
    print_quantum_diffusion_summary(metrics)
