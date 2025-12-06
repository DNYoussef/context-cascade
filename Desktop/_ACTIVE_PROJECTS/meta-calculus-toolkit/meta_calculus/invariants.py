#!/usr/bin/env python3
"""
Multi-Calculus Invariant Detection (Gap 7)

This module detects quantities that remain invariant across different
calculus choices (classical, bigeometric, meta-weighted).

KEY CONCEPT:
  A quantity I is a multi-calculus invariant if:
    forall calculus C: I(solution; C) = I(solution; classical)

  Invariants are the "true" physical observables that don't depend on
  how we parametrize or measure the solution.

INVARIANT CANDIDATES:
  - Singularity type (removable, essential)
  - Expansion regime (accelerating, decelerating)
  - Asymptotic behavior (de Sitter, flat, collapsing)
  - Topology (horizon existence)
  - Conservation laws (where defined)

METHODS:
  1. Variance across calculi (low variance = invariant)
  2. Correlation analysis (high correlation = invariant)
  3. PCA on features from all calculi (first PC = invariant mode)

Usage:
    python -m meta_calculus.invariants compute --n-solutions 50
    python -m meta_calculus.invariants score --feature singularity
    python -m meta_calculus.invariants consensus
    python -m meta_calculus.invariants pca --n-solutions 100
"""

import numpy as np
from typing import Tuple, Dict, List, Optional, Callable
from scipy import stats
import argparse
import sys

# Import from existing modules
from .model_comparison import n_action_based, n_derivative_weight, density_exponent_toy
from .multi_metric import (
    CosmologicalSolution, generate_solution_ensemble
)


# =============================================================================
# CALCULUS DEFINITIONS
# =============================================================================

class Calculus:
    """
    Base class representing a calculus choice.

    Each calculus provides:
      - A way to compute derivatives
      - A way to transform features
      - A way to interpret singularities
    """

    def __init__(self, name: str):
        self.name = name

    def transform_time(self, t: np.ndarray) -> np.ndarray:
        """Transform time coordinate."""
        return t

    def transform_density(self, rho: np.ndarray, t: np.ndarray) -> np.ndarray:
        """Transform density profile."""
        return rho

    def transform_scale(self, a: np.ndarray, t: np.ndarray) -> np.ndarray:
        """Transform scale factor."""
        return a

    def singularity_type(self, sol: CosmologicalSolution) -> str:
        """Classify singularity type in this calculus."""
        raise NotImplementedError


class ClassicalCalculus(Calculus):
    """
    Standard calculus with d/dt derivatives.
    """

    def __init__(self):
        super().__init__("classical")

    def transform_time(self, t: np.ndarray) -> np.ndarray:
        return t

    def transform_density(self, rho: np.ndarray, t: np.ndarray) -> np.ndarray:
        return rho

    def transform_scale(self, a: np.ndarray, t: np.ndarray) -> np.ndarray:
        return a

    def singularity_type(self, sol: CosmologicalSolution) -> str:
        """
        In classical calculus:
          - m > 0: density diverges (essential singularity)
          - m = 0: density constant (removable)
          - m < 0: density vanishes (no singularity)
        """
        m = 2 - 2 * sol.k  # Standard density exponent

        if m > 0:
            return "essential"
        elif abs(m) < 1e-10:
            return "removable"
        else:
            return "none"


class BigeometricCalculus(Calculus):
    """
    Bigeometric (multiplicative) calculus.

    In this calculus, power laws become linear.
    Uses log-derivatives: D_bg[f] = d(log f) / d(log t)
    """

    def __init__(self):
        super().__init__("bigeometric")

    def transform_time(self, t: np.ndarray) -> np.ndarray:
        """Transform to log-time."""
        return np.log(np.maximum(t, 1e-30))

    def transform_density(self, rho: np.ndarray, t: np.ndarray) -> np.ndarray:
        """Transform to log-density."""
        return np.log(np.maximum(rho, 1e-30))

    def transform_scale(self, a: np.ndarray, t: np.ndarray) -> np.ndarray:
        """Transform to log-scale."""
        return np.log(np.maximum(a, 1e-30))

    def singularity_type(self, sol: CosmologicalSolution) -> str:
        """
        In bigeometric calculus:
          - log(rho) = -m * log(t) + const
          - The "singularity" is at log(t) -> -inf (t -> 0)
          - In log-space, this is always a linear divergence
          - Classification based on the slope -m
        """
        m = 2 - 2 * sol.k

        if m > 1:
            return "strong_divergence"  # Fast divergence in log-space
        elif m > 0:
            return "weak_divergence"    # Slow divergence
        elif abs(m) < 1e-10:
            return "constant"            # No divergence
        else:
            return "vanishing"           # log(rho) -> -inf means rho -> 0


class MetaCalculus(Calculus):
    """
    Meta-calculus with D_meta = t^k d/dt.

    Time is stretched/compressed near t=0 based on k.
    """

    def __init__(self, k: float = 0.5):
        super().__init__(f"meta_k{k}")
        self.k = k

    def transform_time(self, t: np.ndarray) -> np.ndarray:
        """Transform to meta-time tau = t^(1-k) / (1-k)."""
        if abs(self.k - 1) < 1e-10:
            return np.log(np.maximum(t, 1e-30))
        else:
            return t**(1 - self.k) / (1 - self.k)

    def transform_density(self, rho: np.ndarray, t: np.ndarray) -> np.ndarray:
        """
        In meta-calculus, density exponent changes:
        rho ~ t^(-m) where m = 2 - 2k
        """
        # The actual density values don't change, but their interpretation does
        return rho

    def transform_scale(self, a: np.ndarray, t: np.ndarray) -> np.ndarray:
        return a

    def singularity_type(self, sol: CosmologicalSolution) -> str:
        """
        In meta-calculus with weight k:
          - Effective density exponent is m = 2 - 2k
          - For k >= 1: m <= 0, singularity is removed
          - For k < 1: m > 0, singularity still present but softer
        """
        m_eff = 2 - 2 * self.k

        if m_eff <= 0:
            return "removed"
        elif m_eff < 1:
            return "softened"
        elif m_eff < 2:
            return "mild"
        else:
            return "strong"


CALCULI = {
    'classical': ClassicalCalculus(),
    'bigeometric': BigeometricCalculus(),
    'meta_0.3': MetaCalculus(0.3),
    'meta_0.5': MetaCalculus(0.5),
    'meta_0.8': MetaCalculus(0.8),
    'meta_1.0': MetaCalculus(1.0),
}


# =============================================================================
# FEATURE COMPUTATION
# =============================================================================

class FeatureComputer:
    """
    Compute features for a solution under different calculi.
    """

    def __init__(self, calculi: List[Calculus] = None):
        """
        Initialize with list of calculi.

        Args:
            calculi: List of Calculus objects (default: all defined)
        """
        if calculi is None:
            calculi = [ClassicalCalculus(), BigeometricCalculus(),
                       MetaCalculus(0.5), MetaCalculus(1.0)]
        self.calculi = calculi

    def compute_feature(self, sol: CosmologicalSolution,
                        feature_name: str) -> Dict[str, float]:
        """
        Compute a named feature under all calculi.

        Args:
            sol: Cosmological solution
            feature_name: One of 'singularity', 'expansion', 'density_exp', etc.

        Returns:
            Dictionary mapping calculus name to feature value
        """
        results = {}

        for calc in self.calculi:
            if feature_name == 'singularity':
                # Encode singularity type as number
                sing_type = calc.singularity_type(sol)
                value = self._encode_singularity(sing_type)

            elif feature_name == 'expansion':
                # Is expansion accelerating (n > 1)?
                value = 1.0 if sol.n > 1 else 0.0

            elif feature_name == 'density_exp':
                # Effective density exponent
                if calc.name == 'classical':
                    value = 2.0  # Always 2 for action-based
                elif calc.name == 'bigeometric':
                    value = 2 - 2 * sol.k  # Same formula, different interpretation
                elif 'meta' in calc.name:
                    value = 2 - 2 * calc.k  # Depends on meta-weight, not solution's k
                else:
                    value = 2 - 2 * sol.k

            elif feature_name == 'hubble_deviation':
                # Deviation from classical Hubble rate
                n_classical = 2.0 / 3.0 / (1 + sol.w) if sol.w != -1 else float('inf')
                value = (sol.n - n_classical) / max(n_classical, 1e-10)

            elif feature_name == 'asymptotic':
                # Late-time behavior
                if sol.n > 1:
                    value = 1.0  # Accelerating
                elif abs(sol.n - 1) < 0.1:
                    value = 0.5  # Coasting
                elif sol.n > 0:
                    value = 0.0  # Decelerating
                else:
                    value = -1.0  # Collapsing

            else:
                value = float('nan')

            results[calc.name] = value

        return results

    def _encode_singularity(self, sing_type: str) -> float:
        """Encode singularity type as numeric value."""
        encoding = {
            'essential': 2.0,
            'strong_divergence': 1.8,
            'strong': 1.5,
            'weak_divergence': 1.2,
            'mild': 1.0,
            'softened': 0.5,
            'removable': 0.0,
            'constant': 0.0,
            'removed': -0.5,
            'vanishing': -1.0,
            'none': -1.0,
        }
        return encoding.get(sing_type, float('nan'))

    def feature_matrix(self, solutions: List[CosmologicalSolution],
                       feature_names: List[str]) -> np.ndarray:
        """
        Compute feature matrix for all solutions and all calculi.

        Args:
            solutions: List of solutions
            feature_names: List of feature names

        Returns:
            Array of shape (n_solutions, n_calculi, n_features)
        """
        n_sol = len(solutions)
        n_calc = len(self.calculi)
        n_feat = len(feature_names)

        matrix = np.zeros((n_sol, n_calc, n_feat))

        for i, sol in enumerate(solutions):
            for f_idx, feat in enumerate(feature_names):
                feat_values = self.compute_feature(sol, feat)
                for c_idx, calc in enumerate(self.calculi):
                    matrix[i, c_idx, f_idx] = feat_values[calc.name]

        return matrix


# =============================================================================
# INVARIANT DETECTION
# =============================================================================

class InvariantDetector:
    """
    Detect invariants across calculi.
    """

    def __init__(self, feature_computer: FeatureComputer = None):
        """
        Initialize detector.

        Args:
            feature_computer: FeatureComputer instance
        """
        self.fc = feature_computer or FeatureComputer()

    def variance_score(self, solutions: List[CosmologicalSolution],
                       feature_name: str) -> Dict:
        """
        Compute variance of feature across calculi.

        Low variance = likely invariant.

        Args:
            solutions: List of solutions
            feature_name: Feature to analyze

        Returns:
            Dictionary with variance statistics
        """
        # Compute feature for all solutions and calculi
        variances = []

        for sol in solutions:
            feat_values = self.fc.compute_feature(sol, feature_name)
            values = list(feat_values.values())
            var = np.var(values)
            variances.append(var)

        variances = np.array(variances)

        # Invariance score: 1 - normalized variance
        max_var = np.max(variances) if np.max(variances) > 0 else 1.0
        scores = 1.0 - variances / max_var

        return {
            'feature': feature_name,
            'mean_variance': np.mean(variances),
            'max_variance': np.max(variances),
            'mean_invariance_score': np.mean(scores),
            'min_invariance_score': np.min(scores),
            'n_perfect_invariants': np.sum(variances < 1e-10),
            'n_solutions': len(solutions),
        }

    def correlation_matrix(self, solutions: List[CosmologicalSolution],
                           feature_name: str) -> np.ndarray:
        """
        Compute correlation matrix of feature across calculi.

        High correlation = calculi agree = likely invariant.

        Args:
            solutions: List of solutions
            feature_name: Feature to analyze

        Returns:
            Correlation matrix (n_calculi x n_calculi)
        """
        n_calc = len(self.fc.calculi)
        n_sol = len(solutions)

        # Collect feature values
        values = np.zeros((n_sol, n_calc))

        for i, sol in enumerate(solutions):
            feat_dict = self.fc.compute_feature(sol, feature_name)
            for j, calc in enumerate(self.fc.calculi):
                values[i, j] = feat_dict[calc.name]

        # Compute correlation
        corr = np.corrcoef(values.T)

        return corr

    def pca_analysis(self, solutions: List[CosmologicalSolution],
                     feature_names: List[str]) -> Dict:
        """
        PCA on features from all calculi.

        First PC represents invariant mode if it explains most variance.

        Args:
            solutions: List of solutions
            feature_names: Features to include

        Returns:
            Dictionary with PCA results
        """
        # Build feature matrix
        matrix = self.fc.feature_matrix(solutions, feature_names)
        n_sol, n_calc, n_feat = matrix.shape

        # Flatten calculi and features into single feature vector
        X = matrix.reshape(n_sol, n_calc * n_feat)

        # Standardize
        X_mean = np.mean(X, axis=0)
        X_std = np.std(X, axis=0)
        X_std[X_std < 1e-10] = 1.0
        X_norm = (X - X_mean) / X_std

        # SVD for PCA
        U, S, Vt = np.linalg.svd(X_norm, full_matrices=False)

        # Explained variance
        explained_var = S**2 / np.sum(S**2)

        return {
            'explained_variance': explained_var[:min(10, len(explained_var))],
            'cumulative_variance': np.cumsum(explained_var)[:10],
            'first_pc_explains': explained_var[0],
            'n_components_90': np.argmax(np.cumsum(explained_var) >= 0.9) + 1,
            'components': Vt[:5],  # First 5 principal components
        }

    def consensus_features(self, solutions: List[CosmologicalSolution],
                           feature_names: List[str],
                           threshold: float = 0.9) -> List[str]:
        """
        Find features with high invariance score (consensus across calculi).

        Args:
            solutions: List of solutions
            feature_names: Candidate features
            threshold: Minimum invariance score

        Returns:
            List of invariant feature names
        """
        invariant_features = []

        for feat in feature_names:
            result = self.variance_score(solutions, feat)
            if result['mean_invariance_score'] >= threshold:
                invariant_features.append(feat)

        return invariant_features


# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_compute(args):
    """Compute features across calculi."""
    print("=" * 70)
    print("FEATURE COMPUTATION ACROSS CALCULI")
    print("=" * 70)

    # Generate solutions
    solutions = generate_solution_ensemble(args.n_solutions, seed=42)
    print(f"\n  Generated {len(solutions)} solutions")

    # Compute features
    fc = FeatureComputer()
    feature_names = ['singularity', 'expansion', 'density_exp', 'asymptotic']

    print(f"\n  Features: {', '.join(feature_names)}")
    print(f"  Calculi: {', '.join(c.name for c in fc.calculi)}")

    # Show example for first solution
    sol = solutions[0]
    print(f"\n  Example (Solution 0: n={sol.n:.4f}, k={sol.k:.4f}):")

    for feat in feature_names:
        values = fc.compute_feature(sol, feat)
        print(f"\n    {feat}:")
        for calc_name, val in values.items():
            print(f"      {calc_name}: {val:.4f}")


def cmd_score(args):
    """Compute invariance score for a feature."""
    print("=" * 70)
    print(f"INVARIANCE SCORE: {args.feature}")
    print("=" * 70)

    solutions = generate_solution_ensemble(args.n_solutions, seed=42)
    detector = InvariantDetector()

    result = detector.variance_score(solutions, args.feature)

    print(f"\n  Feature: {result['feature']}")
    print(f"  Solutions analyzed: {result['n_solutions']}")
    print(f"\n  Variance across calculi:")
    print(f"    Mean variance: {result['mean_variance']:.6f}")
    print(f"    Max variance:  {result['max_variance']:.6f}")
    print(f"\n  Invariance score (1 = perfect invariant, 0 = varies):")
    print(f"    Mean score: {result['mean_invariance_score']:.4f}")
    print(f"    Min score:  {result['min_invariance_score']:.4f}")
    print(f"\n  Perfect invariants (variance < 1e-10): {result['n_perfect_invariants']}")

    if result['mean_invariance_score'] > 0.9:
        print("\n  CONCLUSION: This feature is likely INVARIANT")
    elif result['mean_invariance_score'] > 0.5:
        print("\n  CONCLUSION: This feature is PARTIALLY INVARIANT")
    else:
        print("\n  CONCLUSION: This feature is CALCULUS-DEPENDENT")


def cmd_consensus(args):
    """Find consensus features across calculi."""
    print("=" * 70)
    print("CONSENSUS FEATURE DETECTION")
    print("=" * 70)

    solutions = generate_solution_ensemble(args.n_solutions, seed=42)
    detector = InvariantDetector()

    feature_names = ['singularity', 'expansion', 'density_exp', 'asymptotic', 'hubble_deviation']

    print(f"\n  Analyzing {len(feature_names)} candidate features...")
    print(f"  Threshold: {args.threshold}")

    print(f"\n  {'Feature':<20} {'Mean Score':<15} {'Status':<15}")
    print("  " + "-" * 50)

    for feat in feature_names:
        result = detector.variance_score(solutions, feat)
        score = result['mean_invariance_score']
        status = "INVARIANT" if score >= args.threshold else "VARIES"
        print(f"  {feat:<20} {score:<15.4f} {status:<15}")

    # Find consensus
    consensus = detector.consensus_features(solutions, feature_names, args.threshold)
    print(f"\n  Consensus invariants: {', '.join(consensus) if consensus else 'None'}")


def cmd_correlation(args):
    """Show correlation matrix for a feature."""
    print("=" * 70)
    print(f"CORRELATION ANALYSIS: {args.feature}")
    print("=" * 70)

    solutions = generate_solution_ensemble(args.n_solutions, seed=42)
    detector = InvariantDetector()

    corr = detector.correlation_matrix(solutions, args.feature)

    calc_names = [c.name for c in detector.fc.calculi]

    print(f"\n  Correlation matrix ({args.feature}):\n")
    print("  " + " " * 15 + " ".join(f"{n[:10]:>12}" for n in calc_names))

    for i, name in enumerate(calc_names):
        row = "  " + f"{name[:14]:<15}"
        row += " ".join(f"{corr[i, j]:>12.4f}" for j in range(len(calc_names)))
        print(row)

    # Average off-diagonal correlation
    n = len(calc_names)
    off_diag = (np.sum(corr) - n) / (n * n - n)
    print(f"\n  Mean off-diagonal correlation: {off_diag:.4f}")

    if off_diag > 0.9:
        print("  Interpretation: High agreement - likely invariant")
    elif off_diag > 0.5:
        print("  Interpretation: Moderate agreement")
    else:
        print("  Interpretation: Low agreement - calculus-dependent")


def cmd_pca(args):
    """PCA analysis to find invariant modes."""
    print("=" * 70)
    print("PCA ANALYSIS FOR INVARIANT DETECTION")
    print("=" * 70)

    solutions = generate_solution_ensemble(args.n_solutions, seed=42)
    detector = InvariantDetector()

    feature_names = ['singularity', 'expansion', 'density_exp', 'asymptotic']

    result = detector.pca_analysis(solutions, feature_names)

    print(f"\n  Features: {', '.join(feature_names)}")
    print(f"  Calculi: {len(detector.fc.calculi)}")
    print(f"  Solutions: {len(solutions)}")

    print(f"\n  Explained variance by PC:")
    for i, var in enumerate(result['explained_variance'][:5]):
        print(f"    PC{i+1}: {var*100:6.2f}%  (cumulative: {result['cumulative_variance'][i]*100:6.2f}%)")

    print(f"\n  First PC explains: {result['first_pc_explains']*100:.2f}% of variance")
    print(f"  Components for 90%: {result['n_components_90']}")

    if result['first_pc_explains'] > 0.7:
        print("\n  INTERPRETATION:")
        print("    First PC dominates -> strong invariant structure")
        print("    Most variation is in a single invariant direction")
    elif result['first_pc_explains'] > 0.4:
        print("\n  INTERPRETATION:")
        print("    First PC explains moderate variance")
        print("    Mixed invariant and calculus-dependent structure")
    else:
        print("\n  INTERPRETATION:")
        print("    Variance spread across many components")
        print("    Features are mostly calculus-dependent")


def main():
    parser = argparse.ArgumentParser(
        description="Multi-Calculus Invariant Detection",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # compute command
    comp_parser = subparsers.add_parser('compute',
        help='Compute features across calculi')
    comp_parser.add_argument('--n-solutions', type=int, default=50)
    comp_parser.set_defaults(func=cmd_compute)

    # score command
    score_parser = subparsers.add_parser('score',
        help='Compute invariance score for feature')
    score_parser.add_argument('--feature', type=str, default='singularity',
        choices=['singularity', 'expansion', 'density_exp', 'asymptotic', 'hubble_deviation'])
    score_parser.add_argument('--n-solutions', type=int, default=50)
    score_parser.set_defaults(func=cmd_score)

    # consensus command
    cons_parser = subparsers.add_parser('consensus',
        help='Find consensus features')
    cons_parser.add_argument('--n-solutions', type=int, default=50)
    cons_parser.add_argument('--threshold', type=float, default=0.8)
    cons_parser.set_defaults(func=cmd_consensus)

    # correlation command
    corr_parser = subparsers.add_parser('correlation',
        help='Show correlation matrix')
    corr_parser.add_argument('--feature', type=str, default='singularity')
    corr_parser.add_argument('--n-solutions', type=int, default=50)
    corr_parser.set_defaults(func=cmd_correlation)

    # pca command
    pca_parser = subparsers.add_parser('pca',
        help='PCA analysis for invariant detection')
    pca_parser.add_argument('--n-solutions', type=int, default=100)
    pca_parser.set_defaults(func=cmd_pca)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
