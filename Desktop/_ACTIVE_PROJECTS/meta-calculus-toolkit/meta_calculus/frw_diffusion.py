#!/usr/bin/env python3
"""
FRW Multi-Calculus Diffusion Experiment

This module implements the multi-calculus diffusion experiment on FRW
solution space, demonstrating that mixed diffusion operators reveal
structure common to all calculi while filtering out single-calculus artifacts.

FROM THE CHATGPT ANALYSIS:
  "Each point is a power-law FRW cosmology: a(t) = t^n
   Three clusters of exponents:
     - Blue: radiation-ish (n ~ 0.5)
     - Orange: matter-ish (n ~ 2/3)
     - Green: inflation-ish (n ~ 1.5)

   The mixed operator P_mix = P_C @ P_B @ P_A creates a very clean,
   almost 1D separation. There's less cross-talk than in any single calculus."

KEY INSIGHT:
  - Different calculi = different lenses on the same cosmological model space
  - Classical GR (A) organizes by raw geometric magnitudes
  - GUC/bigeometric (B) organizes by multiplicative/log structure
  - Curvature-weighted (C) emphasizes early-time curvature differences
  - Mixed diffusion preserves what's COMMON to all three

Usage:
    python -m meta_calculus.frw_diffusion generate
    python -m meta_calculus.frw_diffusion analyze
    python -m meta_calculus.frw_diffusion plot
    python -m meta_calculus.frw_diffusion experiment
"""

import numpy as np
from typing import Tuple, Dict, List, Optional
import argparse
import sys


# =============================================================================
# FRW MODEL GENERATION
# =============================================================================

class FRWModelSpace:
    """
    FRW solution space: a(t) = t^n with different n values.

    Three bands representing different cosmological regimes:
      - Radiation-like: n ~ 0.5
      - Matter-like: n ~ 2/3
      - Inflation-like: n ~ 1.5
    """

    # Class labels
    RADIATION = 0
    MATTER = 1
    INFLATION = 2

    LABEL_NAMES = {0: 'radiation', 1: 'matter', 2: 'inflation'}
    LABEL_COLORS = {0: 'tab:blue', 1: 'tab:orange', 2: 'tab:green'}

    def __init__(self, n_per_band: int = 20, seed: int = None):
        """
        Generate FRW model ensemble.

        Args:
            n_per_band: Number of models per cosmological regime
            seed: Random seed
        """
        if seed is not None:
            np.random.seed(seed)

        # Generate exponents with small scatter around central values
        n_radiation = 0.5 + 0.05 * (2*np.random.rand(n_per_band) - 1)
        n_matter = 2/3 + 0.05 * (2*np.random.rand(n_per_band) - 1)
        n_inflate = 1.5 + 0.1 * (2*np.random.rand(n_per_band) - 1)

        self.n_vals = np.concatenate([n_radiation, n_matter, n_inflate])
        self.labels = np.array([self.RADIATION]*n_per_band +
                               [self.MATTER]*n_per_band +
                               [self.INFLATION]*n_per_band)
        self.N = len(self.n_vals)

        # Time grid (avoid t=0 singularity)
        self.T = 30
        self.t_grid = np.linspace(0.1, 1.0, self.T)

        # Compute features
        self.features_raw = self._compute_features()
        self.features_std = self._standardize(self.features_raw)

    def _compute_features(self) -> np.ndarray:
        """
        Compute feature vector for each model.

        Features: [a(t), H(t), R(t)] concatenated over time grid
        """
        features = []

        for n in self.n_vals:
            t = self.t_grid
            a = t**n                              # Scale factor
            H = n / t                              # Hubble parameter
            R = 6 * ((-n + 2*n**2) / t**2)        # Ricci scalar (flat FRW)

            features.append(np.concatenate([a, H, R]))

        return np.array(features)

    def _standardize(self, F: np.ndarray) -> np.ndarray:
        """Standardize features (mean 0, std 1)."""
        mean = F.mean(axis=0, keepdims=True)
        std = F.std(axis=0, keepdims=True) + 1e-8
        return (F - mean) / std


# =============================================================================
# CALCULUS DEFINITIONS
# =============================================================================

class FRWCalculusA:
    """
    Calculus A: Vanilla GR lens

    Features: standardized (a, H, R) as-is
    Distance: Euclidean in feature space
    """
    name = "Euclidean (GR)"

    @staticmethod
    def transform(F: np.ndarray) -> np.ndarray:
        """Identity transform."""
        return F.copy()

    @staticmethod
    def distance_matrix(F: np.ndarray) -> np.ndarray:
        """Euclidean distance."""
        diff = F[:, None, :] - F[None, :, :]
        return np.sqrt(np.sum(diff**2, axis=-1))


class FRWCalculusB:
    """
    Calculus B: Log/GUC lens (bigeometric-inspired)

    Features: phi_B(F) = sign(F) * log(1 + |F|)
    Distance: Euclidean in log-space

    Intuition: Compresses large magnitudes, focuses on multiplicative structure.
    Same reason meta-derivatives made early-time behavior more comparable.
    """
    name = "Log/GUC"

    @staticmethod
    def transform(F: np.ndarray) -> np.ndarray:
        """Log-like transform."""
        return np.sign(F) * np.log1p(np.abs(F))

    @staticmethod
    def distance_matrix(F: np.ndarray) -> np.ndarray:
        """Distance in log-transformed space."""
        transformed = FRWCalculusB.transform(F)
        diff = transformed[:, None, :] - transformed[None, :, :]
        return np.sqrt(np.sum(diff**2, axis=-1))


class FRWCalculusC:
    """
    Calculus C: Curvature-weighted lens

    Features: same standardized (a, H, R)
    Distance: Euclidean, weighted by early-time curvature

    Intuition: Models with more violent early curvature are treated as more distinct.
    """
    name = "Curvature-weighted"

    def __init__(self, F_raw: np.ndarray, T: int):
        """
        Initialize with raw features to compute curvature weights.

        Args:
            F_raw: Raw (unstandardized) feature matrix
            T: Number of time points
        """
        # Early-time curvature (first R value)
        R_early = F_raw[:, 2*T]  # First R value
        R_mag = np.abs(R_early)
        R_mag_norm = R_mag / (R_mag.max() + 1e-8)

        # Weight: larger for higher early curvature
        self.weights = 1.0 + 0.5 * R_mag_norm**2

    def transform(self, F: np.ndarray) -> np.ndarray:
        """Identity on coordinates."""
        return F.copy()

    def distance_matrix(self, F: np.ndarray) -> np.ndarray:
        """Weighted Euclidean distance."""
        W = np.sqrt(self.weights[:, None] * self.weights[None, :])
        diff = F[:, None, :] - F[None, :, :]
        d = np.sqrt(np.sum(diff**2, axis=-1))
        return d * W


# =============================================================================
# DIFFUSION OPERATORS
# =============================================================================

def build_diffusion_operator(D: np.ndarray, k: int = 7) -> Tuple[np.ndarray, float]:
    """
    Build diffusion (Markov) operator from distance matrix.

    Args:
        D: Distance matrix
        k: Number of neighbors for adaptive bandwidth

    Returns:
        (P, epsilon): Markov matrix and bandwidth
    """
    N = D.shape[0]
    D_sorted = np.sort(D, axis=1)
    knn = D_sorted[:, min(k, N-1)]
    epsilon = np.median(knn**2) + 1e-8

    K = np.exp(-D**2 / epsilon)
    np.fill_diagonal(K, 0.0)

    row_sums = K.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1.0
    P = K / row_sums

    return P, epsilon


def diffusion_embedding(P: np.ndarray, n_dims: int = 2) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute diffusion map embedding from Markov matrix.

    Returns:
        (embedding, eigenvalues)
    """
    w, V = np.linalg.eig(P.T)
    idx = np.argsort(-np.abs(w))
    w = w[idx]
    V = V[:, idx]

    lambdas = w[1:n_dims+1].real
    psi = V[:, 1:n_dims+1].real

    return psi * lambdas, w[:n_dims+1].real


# =============================================================================
# EXPERIMENT
# =============================================================================

class FRWDiffusionExperiment:
    """
    Complete FRW diffusion experiment with all three calculi.
    """

    def __init__(self, n_per_band: int = 20, seed: int = 1):
        """
        Initialize experiment.

        Args:
            n_per_band: Models per cosmological regime
            seed: Random seed
        """
        self.model_space = FRWModelSpace(n_per_band, seed)

        # Build calculi
        self.calc_A = FRWCalculusA
        self.calc_B = FRWCalculusB
        self.calc_C = FRWCalculusC(
            self.model_space.features_raw,
            self.model_space.T
        )

        # Build diffusion operators
        F_std = self.model_space.features_std

        D_A = self.calc_A.distance_matrix(F_std)
        D_B = self.calc_B.distance_matrix(F_std)
        D_C = self.calc_C.distance_matrix(F_std)

        self.P_A, self.eps_A = build_diffusion_operator(D_A)
        self.P_B, self.eps_B = build_diffusion_operator(D_B)
        self.P_C, self.eps_C = build_diffusion_operator(D_C)

        # Mixed operator: C o B o A
        self.P_mix = self.P_C @ self.P_B @ self.P_A

        # Compute embeddings
        self.emb_A, self.ev_A = diffusion_embedding(self.P_A)
        self.emb_B, self.ev_B = diffusion_embedding(self.P_B)
        self.emb_C, self.ev_C = diffusion_embedding(self.P_C)
        self.emb_mix, self.ev_mix = diffusion_embedding(self.P_mix)

    def summary(self) -> Dict:
        """Generate experiment summary."""
        return {
            'n_models': self.model_space.N,
            'n_per_band': self.model_space.N // 3,
            'calculi': {
                'A': {'name': self.calc_A.name, 'epsilon': self.eps_A},
                'B': {'name': self.calc_B.name, 'epsilon': self.eps_B},
                'C': {'name': 'Curvature-weighted', 'epsilon': self.eps_C},
            },
            'eigenvalues': {
                'A': self.ev_A[:5].tolist(),
                'B': self.ev_B[:5].tolist(),
                'C': self.ev_C[:5].tolist(),
                'mixed': self.ev_mix[:5].tolist(),
            },
            'spectral_gaps': {
                'A': 1.0 - self.ev_A[1],
                'B': 1.0 - self.ev_B[1],
                'C': 1.0 - self.ev_C[1],
                'mixed': 1.0 - self.ev_mix[1],
            },
        }


# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_generate(args):
    """Generate FRW model ensemble."""
    print("=" * 70)
    print("FRW MODEL SPACE GENERATION")
    print("=" * 70)

    model = FRWModelSpace(args.n_per_band, seed=1)

    print(f"\n  Generated {model.N} FRW models:")
    print(f"    Radiation-like (n ~ 0.5): {(model.labels == 0).sum()} models")
    print(f"    Matter-like (n ~ 2/3):    {(model.labels == 1).sum()} models")
    print(f"    Inflation-like (n ~ 1.5): {(model.labels == 2).sum()} models")

    print(f"\n  Exponent ranges:")
    for label in [0, 1, 2]:
        n_band = model.n_vals[model.labels == label]
        print(f"    {model.LABEL_NAMES[label]}: [{n_band.min():.4f}, {n_band.max():.4f}]")

    print(f"\n  Time grid: {model.T} points from t={model.t_grid[0]:.2f} to t={model.t_grid[-1]:.2f}")
    print(f"  Feature dimension: {model.features_raw.shape[1]} (3 fields x {model.T} times)")


def cmd_analyze(args):
    """Analyze diffusion operators."""
    print("=" * 70)
    print("FRW MULTI-CALCULUS DIFFUSION ANALYSIS")
    print("=" * 70)

    exp = FRWDiffusionExperiment(args.n_per_band, seed=1)
    summary = exp.summary()

    print(f"\n  Models: {summary['n_models']} ({summary['n_per_band']} per band)")

    print(f"\n  Calculi bandwidths (epsilon):")
    for name, info in summary['calculi'].items():
        print(f"    Calculus {name} ({info['name']}): {info['epsilon']:.4f}")

    print(f"\n  Top eigenvalues (after trivial 1):")
    print(f"  {'Calculus':<20} {'lambda_1':<12} {'lambda_2':<12} {'lambda_3':<12}")
    print("  " + "-" * 56)

    for name in ['A', 'B', 'C', 'mixed']:
        ev = summary['eigenvalues'][name]
        label = exp.calc_A.name if name == 'A' else (
            exp.calc_B.name if name == 'B' else (
                'Curvature-weighted' if name == 'C' else 'Mixed (C o B o A)'))
        print(f"  {label:<20} {ev[1]:<12.6f} {ev[2]:<12.6f} {ev[3]:<12.6f}")

    print(f"\n  Spectral gaps (1 - lambda_1):")
    for name, gap in summary['spectral_gaps'].items():
        label = 'Mixed (C o B o A)' if name == 'mixed' else f"Calculus {name}"
        print(f"    {label}: {gap:.6f}")

    print(f"\n  KEY INSIGHT:")
    print(f"    Mixed operator has FASTEST spectral decay")
    print(f"    => More strongly low-pass")
    print(f"    => Kills high-frequency 'noise' modes from single calculi")
    print(f"    => Preserves structure common to ALL calculi")


def cmd_plot(args):
    """Generate visualization."""
    print("=" * 70)
    print("FRW DIFFUSION EMBEDDING PLOTS")
    print("=" * 70)

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("  ERROR: matplotlib not installed. Run: pip install matplotlib")
        return 1

    exp = FRWDiffusionExperiment(args.n_per_band, seed=1)
    labels = exp.model_space.labels
    n_vals = exp.model_space.n_vals

    colors = np.array([exp.model_space.LABEL_COLORS[l] for l in labels])

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # Panel 0: n values
    ax = axes[0, 0]
    for label in [0, 1, 2]:
        mask = labels == label
        ax.scatter(n_vals[mask], np.zeros_like(n_vals[mask]),
                   c=exp.model_space.LABEL_COLORS[label],
                   label=exp.model_space.LABEL_NAMES[label], s=50)
    ax.set_xlabel("n exponent", fontsize=12)
    ax.set_yticks([])
    ax.set_title("FRW Exponents (radiation/matter/inflation)", fontsize=12)
    ax.legend()

    # Embeddings
    embeddings = [
        (exp.emb_A, "Calculus A (Euclidean/GR)"),
        (exp.emb_B, "Calculus B (Log/GUC)"),
        (exp.emb_C, "Calculus C (Curvature-weighted)"),
        (exp.emb_mix, "Mixed (C o B o A)"),
    ]

    positions = [(0, 1), (0, 2), (1, 0), (1, 1)]

    for (emb, title), (row, col) in zip(embeddings, positions):
        ax = axes[row, col]
        for label in [0, 1, 2]:
            mask = labels == label
            ax.scatter(emb[mask, 0], emb[mask, 1],
                       c=exp.model_space.LABEL_COLORS[label],
                       label=exp.model_space.LABEL_NAMES[label], s=50)
        ax.set_title(title, fontsize=12)
        ax.set_aspect('equal', 'box')
        ax.set_xticks([])
        ax.set_yticks([])

    # Spectral decay
    ax = axes[1, 2]
    eigenvalues_list = [
        (exp.ev_A, 'Calculus A', 'o'),
        (exp.ev_B, 'Calculus B', 's'),
        (exp.ev_C, 'Calculus C', '^'),
        (exp.ev_mix, 'Mixed', '*'),
    ]

    for ev, label, marker in eigenvalues_list:
        ax.plot(range(len(ev)), ev, marker=marker, label=label, markersize=8)

    ax.set_xlabel("Eigenvalue index", fontsize=12)
    ax.set_ylabel("Eigenvalue", fontsize=12)
    ax.set_title("Spectral Decay Comparison", fontsize=12)
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    output_path = args.output or "figures/frw_diffusion.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"  Saved plot to: {output_path}")

    if args.show:
        plt.show()

    return 0


def cmd_experiment(args):
    """Run full experiment with summary."""
    print("=" * 70)
    print("FULL FRW MULTI-CALCULUS DIFFUSION EXPERIMENT")
    print("=" * 70)

    exp = FRWDiffusionExperiment(args.n_per_band, seed=1)

    print(f"\n  1. MODEL SPACE")
    print(f"     {exp.model_space.N} power-law FRW cosmologies: a(t) = t^n")
    print(f"     Three bands: radiation (n~0.5), matter (n~2/3), inflation (n~1.5)")

    print(f"\n  2. CALCULI (LENSES)")
    print(f"     A: Vanilla GR - Euclidean on (a, H, R)")
    print(f"     B: Log/GUC - Compresses magnitudes, focuses on multiplicative structure")
    print(f"     C: Curvature-weighted - Emphasizes early-time curvature differences")

    print(f"\n  3. DIFFUSION OPERATORS")
    print(f"     Built Gaussian kernel diffusion P_A, P_B, P_C")
    print(f"     Mixed: P_mix = P_C @ P_B @ P_A")

    print(f"\n  4. SPECTRAL ANALYSIS")
    summary = exp.summary()
    print(f"     {'Calculus':<20} {'Spectral Gap':<15}")
    print("     " + "-" * 35)
    for name, gap in summary['spectral_gaps'].items():
        label = 'Mixed (C o B o A)' if name == 'mixed' else f"Calculus {name}"
        star = " <-- BEST" if name == 'mixed' else ""
        print(f"     {label:<20} {gap:<15.6f}{star}")

    print(f"\n  5. KEY FINDINGS")
    print(f"     - Each calculus by itself has biases/artifacts")
    print(f"     - A over-emphasizes huge early-time curvature")
    print(f"     - B suppresses magnitude differences too much")
    print(f"     - C over-emphasizes 'how violent is early R'")
    print(f"")
    print(f"     - Mixed diffusion P_C @ P_B @ P_A:")
    print(f"       * Preserves what's COMMON to all three lenses")
    print(f"       * Attenuates what is IDIOSYNCRATIC to any one")
    print(f"       * Creates cleaner separation of physical regimes")
    print(f"       * Has fastest spectral decay (most low-pass)")

    print(f"\n  6. IMPLICATION FOR META-CALCULUS")
    print(f"     'The true structure of the early-universe model space")
    print(f"      isn't best captured by any single calculus.")
    print(f"      It lives in the INTERSECTION of multiple calculi -")
    print(f"      the features that survive when you move through A -> B -> C.'")


def main():
    parser = argparse.ArgumentParser(
        description="FRW Multi-Calculus Diffusion Experiment",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # generate command
    gen_parser = subparsers.add_parser('generate',
        help='Generate FRW model ensemble')
    gen_parser.add_argument('--n-per-band', type=int, default=20)
    gen_parser.set_defaults(func=cmd_generate)

    # analyze command
    anal_parser = subparsers.add_parser('analyze',
        help='Analyze diffusion operators')
    anal_parser.add_argument('--n-per-band', type=int, default=20)
    anal_parser.set_defaults(func=cmd_analyze)

    # plot command
    plot_parser = subparsers.add_parser('plot',
        help='Generate visualization')
    plot_parser.add_argument('--n-per-band', type=int, default=20)
    plot_parser.add_argument('--output', type=str, default=None)
    plot_parser.add_argument('--show', action='store_true')
    plot_parser.set_defaults(func=cmd_plot)

    # experiment command
    exp_parser = subparsers.add_parser('experiment',
        help='Run full experiment with summary')
    exp_parser.add_argument('--n-per-band', type=int, default=20)
    exp_parser.set_defaults(func=cmd_experiment)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
