#!/usr/bin/env python3
"""
Multi-Metric Diffusion for Meta-Cosmology (Gaps 4-6)

This module implements multi-metric diffusion operators on the space
of meta-cosmology solutions, inspired by the multi-metric trajectory
approach from diffusion geometry.

KEY IDEA:
  Same solution space, multiple metrics -> each gives different "view"
  Multi-metric trajectories (composing operators) reveal invariant structure

GAPS COVERED:
  Gap 4: Distance functions (classical, log/bigeometric, meta-weighted)
  Gap 5: Diffusion operators (graph Laplacians from each metric)
  Gap 6: Multi-metric trajectories (operator composition)

CONNECTION TO EXISTING CODE:
  Uses model_comparison.py for solution generation (n_action_based, etc.)
  Uses bbn_cmb_constraints.py for physical constraints

Usage:
    python -m meta_calculus.multi_metric distances --metric classical
    python -m meta_calculus.multi_metric laplacian --metric log --sigma 0.1
    python -m meta_calculus.multi_metric trajectory --sequence classical,log,meta
    python -m meta_calculus.multi_metric eigenmodes --n-solutions 50
"""

import numpy as np
from typing import Tuple, Dict, List, Optional, Callable
from scipy import linalg
import argparse
import sys

# Import from existing modules
from .model_comparison import n_action_based, n_derivative_weight
from .bbn_cmb_constraints import MetaFriedmannBBN


# =============================================================================
# SOLUTION REPRESENTATION
# =============================================================================

class CosmologicalSolution:
    """
    Represents a meta-cosmology solution with parameters (n, s, k, w).

    Features are computed at a time grid for distance calculations.
    """

    def __init__(self, n: float, s: float, k: float, w: float,
                 t_grid: np.ndarray = None):
        """
        Initialize solution.

        Args:
            n: Expansion exponent a(t) ~ t^n
            s: Action-based weight exponent
            k: Derivative weight exponent
            w: Equation of state
            t_grid: Time grid for feature evaluation (default: logspace)
        """
        self.n = n
        self.s = s
        self.k = k
        self.w = w

        if t_grid is None:
            self.t_grid = np.logspace(-2, 2, 20)  # t from 0.01 to 100
        else:
            self.t_grid = t_grid

        # Compute derived quantities
        self.m = 2 - 2 * k  # Density exponent

    def scale_factor(self, t: np.ndarray = None) -> np.ndarray:
        """a(t) = t^n"""
        if t is None:
            t = self.t_grid
        return t**self.n

    def hubble(self, t: np.ndarray = None) -> np.ndarray:
        """H(t) = n/t"""
        if t is None:
            t = self.t_grid
        return self.n / t

    def density(self, t: np.ndarray = None, rho_0: float = 1.0) -> np.ndarray:
        """rho(t) = rho_0 * t^(-m) where m = 2 - 2k"""
        if t is None:
            t = self.t_grid
        return rho_0 * t**(-self.m)

    def curvature_scalar(self, t: np.ndarray = None) -> np.ndarray:
        """
        Ricci scalar R for FRW.

        R = 6 * (H_dot + 2H^2) = 6 * (-n/t^2 + 2n^2/t^2)
          = 6 * n * (2n - 1) / t^2
        """
        if t is None:
            t = self.t_grid
        return 6 * self.n * (2 * self.n - 1) / t**2

    def feature_vector(self) -> np.ndarray:
        """
        Compute feature vector for distance calculations.

        Returns:
            Concatenated array of [a(t), H(t), rho(t)] at all t_grid points
        """
        a = self.scale_factor()
        H = self.hubble()
        rho = self.density()
        return np.concatenate([a, H, rho])

    def log_feature_vector(self) -> np.ndarray:
        """
        Compute log-transformed feature vector (bigeometric).

        Returns:
            log of feature vector (for positive quantities)
        """
        a = self.scale_factor()
        H = self.hubble()
        rho = self.density()

        # Avoid log(0) or log(negative)
        a = np.maximum(a, 1e-30)
        H = np.maximum(H, 1e-30)
        rho = np.maximum(rho, 1e-30)

        return np.concatenate([np.log(a), np.log(H), np.log(rho)])

    def meta_weighted_feature_vector(self, k_weight: float = None) -> np.ndarray:
        """
        Compute meta-weighted feature vector.

        Weights each time slice by t^k.
        """
        if k_weight is None:
            k_weight = self.k

        weights = self.t_grid**k_weight

        a = self.scale_factor() * weights
        H = self.hubble() * weights
        rho = self.density() * weights

        return np.concatenate([a, H, rho])


def generate_solution_ensemble(n_solutions: int = 100,
                               seed: int = None) -> List[CosmologicalSolution]:
    """
    Generate an ensemble of cosmological solutions.

    Samples from parameter ranges consistent with BBN/CMB constraints.

    Args:
        n_solutions: Number of solutions to generate
        seed: Random seed

    Returns:
        List of CosmologicalSolution objects
    """
    if seed is not None:
        np.random.seed(seed)

    solutions = []

    # Parameter ranges (within observational constraints)
    s_range = (-0.04, 0.04)  # BBN: |s| < 0.05
    k_range = (-0.02, 0.02)  # CMB: |k| < 0.03
    w_range = (-0.5, 0.9)    # Physical EOS

    attempts = 0
    max_attempts = n_solutions * 10

    while len(solutions) < n_solutions and attempts < max_attempts:
        attempts += 1

        s = np.random.uniform(*s_range)
        k = np.random.uniform(*k_range)
        w = np.random.uniform(*w_range)

        # Skip pathological cases
        if abs(w + 1) < 0.1:  # Near de Sitter
            continue

        # Compute n from action-based model
        try:
            n = n_action_based(s, w)
        except:
            continue

        if np.isnan(n) or n <= 0:
            continue

        sol = CosmologicalSolution(n, s, k, w)
        solutions.append(sol)

    return solutions


# =============================================================================
# DISTANCE FUNCTIONS (Gap 4)
# =============================================================================

class DistanceFunction:
    """
    Base class for distance functions on solution space.
    """

    def distance(self, sol1: CosmologicalSolution,
                 sol2: CosmologicalSolution) -> float:
        """Compute distance between two solutions."""
        raise NotImplementedError

    def distance_matrix(self, solutions: List[CosmologicalSolution]) -> np.ndarray:
        """
        Compute pairwise distance matrix.

        Args:
            solutions: List of solutions

        Returns:
            N x N distance matrix
        """
        N = len(solutions)
        D = np.zeros((N, N))

        for i in range(N):
            for j in range(i+1, N):
                d = self.distance(solutions[i], solutions[j])
                D[i, j] = d
                D[j, i] = d

        return D


class ClassicalDistance(DistanceFunction):
    """
    Euclidean distance on raw features.

    d_classical(X_i, X_j) = || X_i - X_j ||_2
    """

    def distance(self, sol1: CosmologicalSolution,
                 sol2: CosmologicalSolution) -> float:
        X1 = sol1.feature_vector()
        X2 = sol2.feature_vector()
        return np.linalg.norm(X1 - X2)


class LogDistance(DistanceFunction):
    """
    Euclidean distance on log-transformed features (bigeometric).

    d_log(X_i, X_j) = || log(X_i) - log(X_j) ||_2

    Makes power-law differences look linear.
    """

    def distance(self, sol1: CosmologicalSolution,
                 sol2: CosmologicalSolution) -> float:
        X1 = sol1.log_feature_vector()
        X2 = sol2.log_feature_vector()
        return np.linalg.norm(X1 - X2)


class MetaWeightedDistance(DistanceFunction):
    """
    Meta-weighted distance.

    d_meta(X_i, X_j; k) = || t^k * (X_i - X_j) ||_2

    Early times down-weighted for k > 0.
    """

    def __init__(self, k_weight: float = 0.5):
        """
        Args:
            k_weight: Weight exponent
        """
        self.k_weight = k_weight

    def distance(self, sol1: CosmologicalSolution,
                 sol2: CosmologicalSolution) -> float:
        X1 = sol1.meta_weighted_feature_vector(self.k_weight)
        X2 = sol2.meta_weighted_feature_vector(self.k_weight)
        return np.linalg.norm(X1 - X2)


class CurvatureWeightedDistance(DistanceFunction):
    """
    Curvature-weighted distance.

    d_curv(X_i, X_j) = sum_t |R_i(t)|^(-1) * |X_i(t) - X_j(t)|^2

    Emphasizes differences in low-curvature regions.
    """

    def distance(self, sol1: CosmologicalSolution,
                 sol2: CosmologicalSolution) -> float:
        R1 = np.abs(sol1.curvature_scalar())
        R2 = np.abs(sol2.curvature_scalar())

        # Harmonic mean of curvatures as weight
        R_mean = 2 / (1/np.maximum(R1, 1e-10) + 1/np.maximum(R2, 1e-10))
        weights = 1.0 / np.maximum(R_mean, 1e-10)

        X1 = sol1.feature_vector()
        X2 = sol2.feature_vector()

        # Reshape to apply weights (assuming 3 fields * n_times)
        n_times = len(sol1.t_grid)
        diff = X1 - X2
        diff_reshaped = diff.reshape(3, n_times)

        weighted_diff = np.sqrt(weights) * diff_reshaped
        return np.linalg.norm(weighted_diff)


class ParameterDistance(DistanceFunction):
    """
    Distance in parameter space (n, s, k, w).

    d_param = || (n1-n2, s1-s2, k1-k2, w1-w2) ||_2
    """

    def distance(self, sol1: CosmologicalSolution,
                 sol2: CosmologicalSolution) -> float:
        params1 = np.array([sol1.n, sol1.s, sol1.k, sol1.w])
        params2 = np.array([sol2.n, sol2.s, sol2.k, sol2.w])
        return np.linalg.norm(params1 - params2)


DISTANCE_FUNCTIONS = {
    'classical': ClassicalDistance,
    'log': LogDistance,
    'meta': MetaWeightedDistance,
    'curvature': CurvatureWeightedDistance,
    'parameter': ParameterDistance,
}


# =============================================================================
# DIFFUSION OPERATORS (Gap 5)
# =============================================================================

class DiffusionOperator:
    """
    Graph Laplacian-based diffusion operator.

    From distance matrix D, construct:
      1. Kernel: K_ij = exp(-D_ij^2 / (2 sigma^2))
      2. Degree: D_ii = sum_j K_ij
      3. Laplacian: L = D - K (unnormalized)
      4. Random walk: P = D^(-1) K
    """

    def __init__(self, distance_matrix: np.ndarray, sigma: float = None):
        """
        Initialize from distance matrix.

        Args:
            distance_matrix: N x N symmetric distance matrix
            sigma: Kernel bandwidth (default: median distance)
        """
        self.D_dist = distance_matrix
        self.N = distance_matrix.shape[0]

        # Auto-select sigma as median of positive distances
        if sigma is None:
            positive_dists = distance_matrix[distance_matrix > 0]
            if len(positive_dists) > 0:
                sigma = np.median(positive_dists)
            else:
                sigma = 1.0

        self.sigma = sigma

        # Build kernel
        self.K = np.exp(-distance_matrix**2 / (2 * sigma**2))
        np.fill_diagonal(self.K, 0)  # No self-loops

        # Degree matrix
        self.degrees = np.sum(self.K, axis=1)
        self.D_degree = np.diag(self.degrees)

        # Laplacians
        self.L_unnorm = self.D_degree - self.K  # Unnormalized
        self.L_rw = np.eye(self.N) - np.diag(1/np.maximum(self.degrees, 1e-10)) @ self.K

        # Random walk matrix
        self.P = np.diag(1/np.maximum(self.degrees, 1e-10)) @ self.K

    def laplacian(self, normalized: bool = True) -> np.ndarray:
        """
        Return graph Laplacian.

        Args:
            normalized: If True, return random-walk normalized L_rw

        Returns:
            N x N Laplacian matrix
        """
        if normalized:
            return self.L_rw
        else:
            return self.L_unnorm

    def diffusion_matrix(self, t: int = 1) -> np.ndarray:
        """
        Return t-step diffusion matrix P^t.

        Args:
            t: Number of diffusion steps

        Returns:
            N x N diffusion matrix
        """
        return np.linalg.matrix_power(self.P, t)

    def eigendecomposition(self, n_modes: int = 10) -> Tuple[np.ndarray, np.ndarray]:
        """
        Compute eigenvalues and eigenvectors of Laplacian.

        Args:
            n_modes: Number of smallest eigenvalues/vectors

        Returns:
            (eigenvalues, eigenvectors) tuple
        """
        # Use symmetric normalized Laplacian for numerical stability
        D_inv_sqrt = np.diag(1/np.sqrt(np.maximum(self.degrees, 1e-10)))
        L_sym = np.eye(self.N) - D_inv_sqrt @ self.K @ D_inv_sqrt

        eigenvalues, eigenvectors = linalg.eigh(L_sym)

        # Sort by eigenvalue
        idx = np.argsort(eigenvalues)
        eigenvalues = eigenvalues[idx[:n_modes]]
        eigenvectors = eigenvectors[:, idx[:n_modes]]

        return eigenvalues, eigenvectors

    def diffusion_coordinates(self, n_dims: int = 3, t: int = 1) -> np.ndarray:
        """
        Compute diffusion map coordinates.

        Phi_i = (sqrt(lambda_1)^t * phi_1(i), sqrt(lambda_2)^t * phi_2(i), ...)

        Args:
            n_dims: Number of embedding dimensions
            t: Diffusion time

        Returns:
            N x n_dims coordinate matrix
        """
        eigenvalues, eigenvectors = self.eigendecomposition(n_dims + 1)

        # Skip the trivial eigenvalue (lambda_0 = 0)
        eigenvalues = eigenvalues[1:]
        eigenvectors = eigenvectors[:, 1:]

        # Diffusion coordinates
        weights = np.sqrt(np.maximum(eigenvalues, 0))**t
        coords = eigenvectors * weights

        return coords


# =============================================================================
# MULTI-METRIC TRAJECTORIES (Gap 6)
# =============================================================================

class MultiMetricTrajectory:
    """
    Multi-metric diffusion trajectory.

    Compose operators from different metrics:
      T = L_1 @ L_2 @ ... @ L_M

    Or alternating diffusion:
      T = P_1^t1 @ P_2^t2 @ ... @ P_M^tM
    """

    def __init__(self, solutions: List[CosmologicalSolution]):
        """
        Initialize with solution ensemble.

        Args:
            solutions: List of cosmological solutions
        """
        self.solutions = solutions
        self.N = len(solutions)
        self.operators = {}

    def add_metric(self, name: str, distance_func: DistanceFunction,
                   sigma: float = None):
        """
        Add a metric and compute its diffusion operator.

        Args:
            name: Name for this metric
            distance_func: DistanceFunction instance
            sigma: Kernel bandwidth
        """
        D = distance_func.distance_matrix(self.solutions)
        op = DiffusionOperator(D, sigma=sigma)
        self.operators[name] = op

    def trajectory_operator(self, sequence: List[str],
                            use_laplacian: bool = True) -> np.ndarray:
        """
        Compute trajectory operator from metric sequence.

        Args:
            sequence: List of metric names, e.g., ['classical', 'log', 'meta']
            use_laplacian: If True, multiply Laplacians; if False, multiply P

        Returns:
            N x N trajectory operator matrix
        """
        T = np.eye(self.N)

        for name in sequence:
            if name not in self.operators:
                raise ValueError(f"Unknown metric: {name}")

            op = self.operators[name]

            if use_laplacian:
                T = T @ op.laplacian(normalized=True)
            else:
                T = T @ op.P

        return T

    def diffusion_distance(self, sequence: List[str],
                           i: int, j: int, t: int = 1) -> float:
        """
        Diffusion distance between solutions i and j under trajectory.

        Args:
            sequence: Metric sequence
            i, j: Solution indices
            t: Diffusion time

        Returns:
            Diffusion distance
        """
        T = self.trajectory_operator(sequence, use_laplacian=False)
        T_t = np.linalg.matrix_power(T, t)

        return np.linalg.norm(T_t[i, :] - T_t[j, :])

    def trajectory_eigenanalysis(self, sequence: List[str],
                                  n_modes: int = 5) -> Dict:
        """
        Eigenanalysis of trajectory operator.

        Args:
            sequence: Metric sequence
            n_modes: Number of modes to compute

        Returns:
            Dictionary with eigenvalues, eigenvectors, spectral gap
        """
        T = self.trajectory_operator(sequence, use_laplacian=True)

        eigenvalues, eigenvectors = linalg.eig(T)

        # Sort by magnitude
        idx = np.argsort(np.abs(eigenvalues))
        eigenvalues = eigenvalues[idx[:n_modes]]
        eigenvectors = eigenvectors[:, idx[:n_modes]]

        # Spectral gap
        if len(eigenvalues) >= 2:
            spectral_gap = np.abs(eigenvalues[1]) - np.abs(eigenvalues[0])
        else:
            spectral_gap = 0.0

        return {
            'eigenvalues': eigenvalues,
            'eigenvectors': eigenvectors,
            'spectral_gap': spectral_gap,
            'sequence': sequence,
        }

    def compare_trajectories(self, trajectories: List[List[str]],
                              n_modes: int = 5) -> List[Dict]:
        """
        Compare multiple trajectory sequences.

        Args:
            trajectories: List of metric sequences
            n_modes: Number of modes for each

        Returns:
            List of eigenanalysis results
        """
        results = []
        for seq in trajectories:
            analysis = self.trajectory_eigenanalysis(seq, n_modes)
            results.append(analysis)
        return results


# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_distances(args):
    """Compute and display distance statistics."""
    print("=" * 70)
    print(f"DISTANCE ANALYSIS (metric: {args.metric})")
    print("=" * 70)

    # Generate solutions
    print(f"\n  Generating {args.n_solutions} solutions...")
    solutions = generate_solution_ensemble(args.n_solutions, seed=42)
    print(f"  Generated {len(solutions)} valid solutions")

    # Create distance function
    if args.metric == 'meta':
        dist_func = MetaWeightedDistance(k_weight=args.k_weight)
    else:
        dist_func = DISTANCE_FUNCTIONS[args.metric]()

    # Compute distance matrix
    print(f"\n  Computing distance matrix...")
    D = dist_func.distance_matrix(solutions)

    # Statistics
    positive_D = D[D > 0]
    print(f"\n  Distance statistics:")
    print(f"    Min:    {positive_D.min():.4f}")
    print(f"    Max:    {positive_D.max():.4f}")
    print(f"    Mean:   {positive_D.mean():.4f}")
    print(f"    Median: {np.median(positive_D):.4f}")
    print(f"    Std:    {positive_D.std():.4f}")

    # Nearest neighbors
    print(f"\n  Nearest neighbor distances (first 5 solutions):")
    for i in range(min(5, len(solutions))):
        row = D[i, :]
        row[i] = float('inf')  # Exclude self
        nn_idx = np.argmin(row)
        nn_dist = row[nn_idx]
        print(f"    Sol {i}: nearest = Sol {nn_idx}, distance = {nn_dist:.4f}")


def cmd_laplacian(args):
    """Compute and analyze Laplacian."""
    print("=" * 70)
    print(f"LAPLACIAN ANALYSIS (metric: {args.metric})")
    print("=" * 70)

    # Generate solutions
    solutions = generate_solution_ensemble(args.n_solutions, seed=42)

    # Create distance and operator
    if args.metric == 'meta':
        dist_func = MetaWeightedDistance(k_weight=0.5)
    else:
        dist_func = DISTANCE_FUNCTIONS[args.metric]()

    D = dist_func.distance_matrix(solutions)
    op = DiffusionOperator(D, sigma=args.sigma)

    # Eigendecomposition
    eigenvalues, eigenvectors = op.eigendecomposition(n_modes=10)

    print(f"\n  Kernel bandwidth sigma = {op.sigma:.4f}")
    print(f"\n  Smallest eigenvalues:")
    for i, ev in enumerate(eigenvalues):
        print(f"    lambda_{i} = {ev:.6f}")

    if len(eigenvalues) >= 2:
        gap = eigenvalues[1] - eigenvalues[0]
        print(f"\n  Spectral gap (lambda_1 - lambda_0) = {gap:.6f}")

    # Diffusion coordinates
    coords = op.diffusion_coordinates(n_dims=3, t=1)
    print(f"\n  Diffusion coordinate ranges:")
    for d in range(3):
        print(f"    Dim {d+1}: [{coords[:, d].min():.4f}, {coords[:, d].max():.4f}]")


def cmd_trajectory(args):
    """Compute multi-metric trajectory."""
    print("=" * 70)
    print("MULTI-METRIC TRAJECTORY ANALYSIS")
    print("=" * 70)

    # Parse sequence
    sequence = [m.strip() for m in args.sequence.split(',')]
    print(f"\n  Trajectory sequence: {' -> '.join(sequence)}")

    # Generate solutions
    solutions = generate_solution_ensemble(args.n_solutions, seed=42)

    # Build multi-metric
    mmt = MultiMetricTrajectory(solutions)

    for metric in set(sequence):
        if metric == 'meta':
            dist_func = MetaWeightedDistance(k_weight=0.5)
        elif metric in DISTANCE_FUNCTIONS:
            dist_func = DISTANCE_FUNCTIONS[metric]()
        else:
            print(f"  Unknown metric: {metric}")
            return 1

        mmt.add_metric(metric, dist_func)
        print(f"  Added metric: {metric}")

    # Trajectory analysis
    result = mmt.trajectory_eigenanalysis(sequence, n_modes=5)

    print(f"\n  Trajectory operator eigenvalues:")
    for i, ev in enumerate(result['eigenvalues']):
        print(f"    lambda_{i} = {ev:.6f}")

    print(f"\n  Spectral gap = {result['spectral_gap']:.6f}")


def cmd_eigenmodes(args):
    """Compare eigenmodes across metrics."""
    print("=" * 70)
    print("EIGENMODE COMPARISON ACROSS METRICS")
    print("=" * 70)

    # Generate solutions
    solutions = generate_solution_ensemble(args.n_solutions, seed=42)

    metrics = ['classical', 'log', 'parameter']
    print(f"\n  Comparing metrics: {', '.join(metrics)}")

    results = []
    for metric in metrics:
        dist_func = DISTANCE_FUNCTIONS[metric]()
        D = dist_func.distance_matrix(solutions)
        op = DiffusionOperator(D)
        eigenvalues, _ = op.eigendecomposition(n_modes=5)

        results.append({
            'metric': metric,
            'eigenvalues': eigenvalues,
            'spectral_gap': eigenvalues[1] - eigenvalues[0] if len(eigenvalues) >= 2 else 0,
        })

    print(f"\n  {'Metric':<12} {'lambda_0':<12} {'lambda_1':<12} {'Spectral Gap':<12}")
    print("  " + "-" * 50)

    for r in results:
        ev = r['eigenvalues']
        print(f"  {r['metric']:<12} {ev[0]:<12.6f} {ev[1]:<12.6f} {r['spectral_gap']:<12.6f}")


def cmd_compare_trajectories(args):
    """Compare different trajectory sequences."""
    print("=" * 70)
    print("TRAJECTORY SEQUENCE COMPARISON")
    print("=" * 70)

    # Generate solutions
    solutions = generate_solution_ensemble(args.n_solutions, seed=42)

    # Build multi-metric with all distance functions
    mmt = MultiMetricTrajectory(solutions)
    for name, cls in DISTANCE_FUNCTIONS.items():
        if name == 'meta':
            mmt.add_metric(name, MetaWeightedDistance(k_weight=0.5))
        else:
            mmt.add_metric(name, cls())

    # Trajectories to compare
    trajectories = [
        ['classical'],
        ['log'],
        ['classical', 'log'],
        ['classical', 'log', 'classical'],
        ['classical', 'log', 'meta'],
        ['log', 'classical', 'log'],
    ]

    print(f"\n  {'Trajectory':<35} {'Spectral Gap':<15}")
    print("  " + "-" * 50)

    for seq in trajectories:
        try:
            result = mmt.trajectory_eigenanalysis(seq, n_modes=3)
            seq_str = ' -> '.join(seq)
            print(f"  {seq_str:<35} {result['spectral_gap']:<15.6f}")
        except Exception as e:
            print(f"  {' -> '.join(seq):<35} ERROR: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Multi-Metric Diffusion for Meta-Cosmology",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # distances command
    dist_parser = subparsers.add_parser('distances',
        help='Compute distance statistics')
    dist_parser.add_argument('--metric', type=str, default='classical',
        choices=list(DISTANCE_FUNCTIONS.keys()))
    dist_parser.add_argument('--n-solutions', type=int, default=50)
    dist_parser.add_argument('--k-weight', type=float, default=0.5,
        help='Weight exponent for meta metric')
    dist_parser.set_defaults(func=cmd_distances)

    # laplacian command
    lap_parser = subparsers.add_parser('laplacian',
        help='Compute and analyze Laplacian')
    lap_parser.add_argument('--metric', type=str, default='classical',
        choices=list(DISTANCE_FUNCTIONS.keys()))
    lap_parser.add_argument('--n-solutions', type=int, default=50)
    lap_parser.add_argument('--sigma', type=float, default=None)
    lap_parser.set_defaults(func=cmd_laplacian)

    # trajectory command
    traj_parser = subparsers.add_parser('trajectory',
        help='Compute multi-metric trajectory')
    traj_parser.add_argument('--sequence', type=str, default='classical,log',
        help='Comma-separated metric sequence')
    traj_parser.add_argument('--n-solutions', type=int, default=50)
    traj_parser.set_defaults(func=cmd_trajectory)

    # eigenmodes command
    eigen_parser = subparsers.add_parser('eigenmodes',
        help='Compare eigenmodes across metrics')
    eigen_parser.add_argument('--n-solutions', type=int, default=50)
    eigen_parser.set_defaults(func=cmd_eigenmodes)

    # compare-trajectories command
    comp_parser = subparsers.add_parser('compare-trajectories',
        help='Compare different trajectory sequences')
    comp_parser.add_argument('--n-solutions', type=int, default=50)
    comp_parser.set_defaults(func=cmd_compare_trajectories)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
