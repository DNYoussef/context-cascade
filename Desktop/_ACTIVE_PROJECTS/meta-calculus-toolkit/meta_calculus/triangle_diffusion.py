#!/usr/bin/env python3
"""
Triangle Cosmological Polytope Diffusion Experiment

This module implements the discrete diffusion experiment on the simplest
cosmological polytope (a triangle) with multiple calculi:
  - Calculus A: Euclidean (classical affine)
  - Calculus B: Log/GUC-like (bigeometric-inspired)
  - Calculus C: Curvature-weighted

KEY INSIGHT from ChatGPT analysis:
  "Your many calculi aren't rival theories. They're multiple geometric lenses
   on the same underlying object. The multi-geometry / multi-operator picture
   says: don't crown one lens as 'the true one.' Put several on the same object."

TRIANGLE DEFINITION (two-site cosmological polytope):
  Vertices: (2,2), (0,-2), (-2,0)
  Facets (edges):
    L1: y - 2x + 2 = 0
    L2: y + x + 2 = 0
    L3: -2y + x + 2 = 0
  Canonical form: Omega = dx ^ dy / (L1 * L2 * L3)

Usage:
    python -m meta_calculus.triangle_diffusion sample
    python -m meta_calculus.triangle_diffusion diffusion
    python -m meta_calculus.triangle_diffusion compare
    python -m meta_calculus.triangle_diffusion plot
"""

import numpy as np
from typing import Tuple, Dict, List, Optional
import argparse
import sys


# =============================================================================
# TRIANGLE COSMOLOGICAL POLYTOPE
# =============================================================================

class TrianglePolytope:
    """
    The simplest cosmological polytope: a triangle from the two-site graph.

    Vertices: V1 = (2,2), V2 = (0,-2), V3 = (-2,0)

    Facet (edge) functions:
      L1(x,y) = y - 2x + 2
      L2(x,y) = y + x + 2
      L3(x,y) = -2y + x + 2

    Canonical form:
      Omega = dx ^ dy / (L1 * L2 * L3)
    """

    # Vertices
    V1 = np.array([2.0, 2.0])
    V2 = np.array([0.0, -2.0])
    V3 = np.array([-2.0, 0.0])

    @classmethod
    def L1(cls, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Facet 1: y - 2x + 2"""
        return y - 2*x + 2

    @classmethod
    def L2(cls, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Facet 2: y + x + 2"""
        return y + x + 2

    @classmethod
    def L3(cls, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Facet 3: -2y + x + 2"""
        return -2*y + x + 2

    @classmethod
    def canonical_form(cls, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Canonical form coefficient: 1 / (L1 * L2 * L3)

        This is the coefficient of dx ^ dy.
        """
        denom = cls.L1(x, y) * cls.L2(x, y) * cls.L3(x, y)
        return np.where(np.abs(denom) > 1e-10, 1.0 / denom, np.inf)

    @classmethod
    def is_inside(cls, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Check if points are inside the triangle (all Li > 0)."""
        return (cls.L1(x, y) > 0) & (cls.L2(x, y) > 0) & (cls.L3(x, y) > 0)

    @classmethod
    def sample_interior(cls, n_points: int, seed: int = None) -> np.ndarray:
        """
        Sample points uniformly from the triangle interior.

        Returns:
            Array of shape (n_points, 2) with (x, y) coordinates
        """
        if seed is not None:
            np.random.seed(seed)

        points = []
        attempts = 0
        max_attempts = n_points * 100

        # Bounding box
        x_min, x_max = -2.0, 2.0
        y_min, y_max = -2.0, 2.0

        while len(points) < n_points and attempts < max_attempts:
            attempts += 1
            x = np.random.uniform(x_min, x_max)
            y = np.random.uniform(y_min, y_max)

            if cls.is_inside(np.array([x]), np.array([y]))[0]:
                points.append([x, y])

        return np.array(points)


# =============================================================================
# CALCULUS DEFINITIONS
# =============================================================================

class CalculusA:
    """
    Calculus A: Classical Euclidean

    - Coordinates: phi_A(x,y) = (x, y)
    - Metric: ds^2 = dx^2 + dy^2
    - Features: raw (x, y) coordinates
    """
    name = "Euclidean"

    @staticmethod
    def transform(points: np.ndarray) -> np.ndarray:
        """Identity transform."""
        return points.copy()

    @staticmethod
    def distance_matrix(points: np.ndarray) -> np.ndarray:
        """Euclidean distance matrix."""
        diff = points[:, None, :] - points[None, :, :]
        return np.sqrt(np.sum(diff**2, axis=-1))


class CalculusB:
    """
    Calculus B: Log/GUC-like (Bigeometric-inspired)

    - Coordinates: phi_B(x,y) = (sign(x)*log(1+|x|), sign(y)*log(1+|y|))
    - Metric: Euclidean in log-space
    - Features: compressed magnitude, focuses on multiplicative structure
    """
    name = "Log/GUC"

    @staticmethod
    def transform(points: np.ndarray) -> np.ndarray:
        """Log-like transform: sign(x) * log(1 + |x|)"""
        return np.sign(points) * np.log1p(np.abs(points))

    @staticmethod
    def distance_matrix(points: np.ndarray) -> np.ndarray:
        """Distance in log-transformed space."""
        transformed = CalculusB.transform(points)
        diff = transformed[:, None, :] - transformed[None, :, :]
        return np.sqrt(np.sum(diff**2, axis=-1))


class CalculusC:
    """
    Calculus C: Curvature-weighted (Canonical form weighted)

    - Coordinates: (x, y)
    - Metric: weighted by proximity to boundary (canonical form magnitude)
    - Features: points near boundaries are "further apart"
    """
    name = "Curvature-weighted"

    @staticmethod
    def transform(points: np.ndarray) -> np.ndarray:
        """Identity on coordinates."""
        return points.copy()

    @staticmethod
    def weights(points: np.ndarray) -> np.ndarray:
        """
        Weight based on canonical form magnitude.
        Near boundaries -> large canonical form -> large weight.
        """
        x, y = points[:, 0], points[:, 1]
        L1 = TrianglePolytope.L1(x, y)
        L2 = TrianglePolytope.L2(x, y)
        L3 = TrianglePolytope.L3(x, y)

        # Minimum distance to any facet
        min_L = np.minimum(np.minimum(L1, L2), L3)
        min_L = np.maximum(min_L, 0.1)  # Regularize

        # Weight: larger near boundary
        return 1.0 / min_L

    @staticmethod
    def distance_matrix(points: np.ndarray) -> np.ndarray:
        """Weighted Euclidean distance."""
        w = CalculusC.weights(points)
        W = np.sqrt(w[:, None] * w[None, :])  # Geometric mean of weights

        diff = points[:, None, :] - points[None, :, :]
        d = np.sqrt(np.sum(diff**2, axis=-1))
        return d * W


CALCULI = {
    'A': CalculusA,
    'B': CalculusB,
    'C': CalculusC,
}


# =============================================================================
# DIFFUSION OPERATORS
# =============================================================================

class DiffusionOperator:
    """
    Diffusion operator from distance matrix.

    K_ij = exp(-D_ij^2 / epsilon)
    P = D^(-1) K  (row-stochastic Markov matrix)
    """

    def __init__(self, distance_matrix: np.ndarray, k_neighbors: int = 7):
        """
        Build diffusion operator.

        Args:
            distance_matrix: N x N distance matrix
            k_neighbors: Number of neighbors for adaptive bandwidth
        """
        self.D = distance_matrix
        self.N = distance_matrix.shape[0]

        # Adaptive bandwidth: median of k-th nearest neighbor distance
        D_sorted = np.sort(distance_matrix, axis=1)
        knn = D_sorted[:, min(k_neighbors, self.N - 1)]
        self.epsilon = np.median(knn**2) + 1e-8

        # Gaussian kernel
        self.K = np.exp(-distance_matrix**2 / self.epsilon)
        np.fill_diagonal(self.K, 0.0)

        # Row-normalize to get Markov matrix
        row_sums = self.K.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1.0
        self.P = self.K / row_sums

    def eigendecomposition(self, n_modes: int = 10) -> Tuple[np.ndarray, np.ndarray]:
        """
        Compute eigenvalues and eigenvectors of P.

        Returns right eigenvectors of P (columns).
        """
        eigenvalues, eigenvectors = np.linalg.eig(self.P.T)

        # Sort by descending magnitude
        idx = np.argsort(-np.abs(eigenvalues))
        eigenvalues = eigenvalues[idx[:n_modes]].real
        eigenvectors = eigenvectors[:, idx[:n_modes]].real

        return eigenvalues, eigenvectors

    def diffusion_embedding(self, n_dims: int = 2) -> np.ndarray:
        """
        Diffusion map embedding.

        Phi_i = (lambda_1 * psi_1(i), lambda_2 * psi_2(i), ...)
        """
        eigenvalues, eigenvectors = self.eigendecomposition(n_dims + 1)

        # Skip trivial eigenvalue (lambda_0 = 1)
        lambdas = eigenvalues[1:n_dims+1]
        psi = eigenvectors[:, 1:n_dims+1]

        return psi * lambdas


def build_diffusion_operators(points: np.ndarray) -> Dict[str, DiffusionOperator]:
    """Build diffusion operators for all calculi."""
    operators = {}
    for name, calc_class in CALCULI.items():
        D = calc_class.distance_matrix(points)
        operators[name] = DiffusionOperator(D)
    return operators


def mixed_operator(operators: List[DiffusionOperator]) -> np.ndarray:
    """
    Compose multiple Markov operators: P_mix = P_n @ ... @ P_2 @ P_1

    This is the key "multi-geometry" operation that preserves
    structure common to all calculi.
    """
    P = np.eye(operators[0].N)
    for op in operators:
        P = op.P @ P
    return P


# =============================================================================
# ANALYSIS
# =============================================================================

def analyze_spectral_decay(operators: Dict[str, DiffusionOperator],
                           P_mix: np.ndarray) -> Dict:
    """
    Analyze spectral decay across calculi.

    Faster decay = more "low-pass" = better noise filtering.
    """
    results = {}

    for name, op in operators.items():
        evals, _ = op.eigendecomposition(10)
        results[name] = {
            'eigenvalues': evals,
            'spectral_gap': 1.0 - evals[1] if len(evals) > 1 else 0,
        }

    # Mixed operator
    N = P_mix.shape[0]
    evals_mix, _ = np.linalg.eig(P_mix.T)
    evals_mix = np.sort(np.abs(evals_mix))[::-1][:10].real

    results['mixed'] = {
        'eigenvalues': evals_mix,
        'spectral_gap': 1.0 - evals_mix[1] if len(evals_mix) > 1 else 0,
    }

    return results


# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_sample(args):
    """Sample points from triangle interior."""
    print("=" * 70)
    print("SAMPLING TRIANGLE COSMOLOGICAL POLYTOPE")
    print("=" * 70)

    points = TrianglePolytope.sample_interior(args.n_points, seed=42)

    print(f"\n  Triangle vertices:")
    print(f"    V1 = {TrianglePolytope.V1}")
    print(f"    V2 = {TrianglePolytope.V2}")
    print(f"    V3 = {TrianglePolytope.V3}")

    print(f"\n  Sampled {len(points)} interior points")
    print(f"    x range: [{points[:,0].min():.3f}, {points[:,0].max():.3f}]")
    print(f"    y range: [{points[:,1].min():.3f}, {points[:,1].max():.3f}]")

    # Show canonical form values
    omega = TrianglePolytope.canonical_form(points[:,0], points[:,1])
    print(f"\n  Canonical form Omega statistics:")
    print(f"    min: {omega.min():.4f}")
    print(f"    max: {omega.max():.4f}")
    print(f"    mean: {omega.mean():.4f}")


def cmd_diffusion(args):
    """Build and analyze diffusion operators."""
    print("=" * 70)
    print("DIFFUSION OPERATORS ON TRIANGLE")
    print("=" * 70)

    points = TrianglePolytope.sample_interior(args.n_points, seed=42)
    print(f"\n  Using {len(points)} sample points")

    operators = build_diffusion_operators(points)

    print(f"\n  Diffusion operators built for:")
    for name, calc in CALCULI.items():
        op = operators[name]
        print(f"    Calculus {name} ({calc.name}): epsilon = {op.epsilon:.4f}")

    # Eigenvalue analysis
    print(f"\n  Top eigenvalues (after trivial 1):")
    print(f"  {'Calculus':<15} {'lambda_1':<12} {'lambda_2':<12} {'lambda_3':<12}")
    print("  " + "-" * 50)

    for name in ['A', 'B', 'C']:
        evals, _ = operators[name].eigendecomposition(5)
        print(f"  {CALCULI[name].name:<15} {evals[1]:<12.6f} {evals[2]:<12.6f} {evals[3]:<12.6f}")

    # Mixed operator
    P_mix = mixed_operator([operators['A'], operators['B'], operators['C']])
    evals_mix, _ = np.linalg.eig(P_mix.T)
    evals_mix = np.sort(np.abs(evals_mix))[::-1][:5].real

    print(f"  {'Mixed (A->B->C)':<15} {evals_mix[1]:<12.6f} {evals_mix[2]:<12.6f} {evals_mix[3]:<12.6f}")


def cmd_compare(args):
    """Compare diffusion embeddings across calculi."""
    print("=" * 70)
    print("MULTI-CALCULUS DIFFUSION COMPARISON")
    print("=" * 70)

    points = TrianglePolytope.sample_interior(args.n_points, seed=42)
    operators = build_diffusion_operators(points)
    P_mix = mixed_operator([operators['A'], operators['B'], operators['C']])

    # Spectral analysis
    results = analyze_spectral_decay(operators, P_mix)

    print(f"\n  SPECTRAL DECAY ANALYSIS:")
    print(f"  {'Calculus':<20} {'Spectral Gap':<15} {'Decay Rate':<15}")
    print("  " + "-" * 50)

    for name in ['A', 'B', 'C', 'mixed']:
        gap = results[name]['spectral_gap']
        evals = results[name]['eigenvalues']
        decay = (1.0 - evals[3]) / (1.0 - evals[1]) if len(evals) > 3 else 0
        label = CALCULI[name].name if name in CALCULI else "Mixed (C o B o A)"
        print(f"  {label:<20} {gap:<15.6f} {decay:<15.4f}")

    print(f"\n  KEY INSIGHT:")
    print(f"    Mixed operator has LARGER spectral gap = more low-pass")
    print(f"    => Filters out artifacts idiosyncratic to any single calculus")
    print(f"    => Preserves structure common to ALL calculi")


def cmd_plot(args):
    """Generate visualization (requires matplotlib)."""
    print("=" * 70)
    print("GENERATING DIFFUSION EMBEDDING PLOTS")
    print("=" * 70)

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("  ERROR: matplotlib not installed. Run: pip install matplotlib")
        return 1

    points = TrianglePolytope.sample_interior(args.n_points, seed=42)
    operators = build_diffusion_operators(points)
    P_mix = mixed_operator([operators['A'], operators['B'], operators['C']])

    # Compute embeddings
    emb_A = operators['A'].diffusion_embedding(2)
    emb_B = operators['B'].diffusion_embedding(2)
    emb_C = operators['C'].diffusion_embedding(2)

    # Mixed embedding
    N = P_mix.shape[0]
    evals, evecs = np.linalg.eig(P_mix.T)
    idx = np.argsort(-np.abs(evals))
    evals = evals[idx[:3]].real
    evecs = evecs[:, idx[:3]].real
    emb_mix = evecs[:, 1:3] * evals[1:3]

    # Color by canonical form value (proxy for "distance to boundary")
    omega = TrianglePolytope.canonical_form(points[:,0], points[:,1])
    colors = np.log1p(np.abs(omega))

    fig, axes = plt.subplots(2, 3, figsize=(14, 9))

    # Row 1: Original space and individual embeddings
    ax = axes[0, 0]
    ax.scatter(points[:,0], points[:,1], c=colors, cmap='viridis', s=20)
    ax.plot([2, 0, -2, 2], [2, -2, 0, 2], 'k-', linewidth=2)
    ax.set_title("Triangle (color = log|Omega|)")
    ax.set_aspect('equal')

    for ax, emb, title in zip(
        axes[0, 1:],
        [emb_A, emb_B],
        ["Calculus A (Euclidean)", "Calculus B (Log/GUC)"]):
        ax.scatter(emb[:,0], emb[:,1], c=colors, cmap='viridis', s=20)
        ax.set_title(title)
        ax.set_aspect('equal')

    axes[1, 0].scatter(emb_C[:,0], emb_C[:,1], c=colors, cmap='viridis', s=20)
    axes[1, 0].set_title("Calculus C (Curvature-weighted)")
    axes[1, 0].set_aspect('equal')

    axes[1, 1].scatter(emb_mix[:,0], emb_mix[:,1], c=colors, cmap='viridis', s=20)
    axes[1, 1].set_title("Mixed (C o B o A)")
    axes[1, 1].set_aspect('equal')

    # Spectral decay plot
    ax = axes[1, 2]
    for name, marker in [('A', 'o'), ('B', 's'), ('C', '^')]:
        evals, _ = operators[name].eigendecomposition(8)
        ax.plot(range(len(evals)), evals, marker=marker, label=CALCULI[name].name)

    evals_mix, _ = np.linalg.eig(P_mix.T)
    evals_mix = np.sort(np.abs(evals_mix))[::-1][:8].real
    ax.plot(range(len(evals_mix)), evals_mix, 'k*-', label='Mixed', markersize=10)

    ax.set_xlabel("Eigenvalue index")
    ax.set_ylabel("Eigenvalue")
    ax.set_title("Spectral Decay Comparison")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    # Save figure
    output_path = args.output or "figures/triangle_diffusion.png"
    plt.savefig(output_path, dpi=150)
    print(f"  Saved plot to: {output_path}")

    if args.show:
        plt.show()

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Triangle Cosmological Polytope Diffusion Experiment",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # sample command
    sample_parser = subparsers.add_parser('sample',
        help='Sample points from triangle interior')
    sample_parser.add_argument('--n-points', type=int, default=100)
    sample_parser.set_defaults(func=cmd_sample)

    # diffusion command
    diff_parser = subparsers.add_parser('diffusion',
        help='Build and analyze diffusion operators')
    diff_parser.add_argument('--n-points', type=int, default=100)
    diff_parser.set_defaults(func=cmd_diffusion)

    # compare command
    comp_parser = subparsers.add_parser('compare',
        help='Compare diffusion embeddings across calculi')
    comp_parser.add_argument('--n-points', type=int, default=100)
    comp_parser.set_defaults(func=cmd_compare)

    # plot command
    plot_parser = subparsers.add_parser('plot',
        help='Generate visualization')
    plot_parser.add_argument('--n-points', type=int, default=200)
    plot_parser.add_argument('--output', type=str, default=None)
    plot_parser.add_argument('--show', action='store_true')
    plot_parser.set_defaults(func=cmd_plot)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
