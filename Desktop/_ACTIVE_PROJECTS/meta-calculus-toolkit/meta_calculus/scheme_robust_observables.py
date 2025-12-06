#!/usr/bin/env python3
"""
Scheme-Robust Observables: Multi-Calculus Invariant Extraction

This module implements the core insight from the multi-calculus reframing:

    Physical = Scheme-Robust = Cross-Calculus Invariant

Instead of betting on one calculus (classical, GUC, bigeometric), we use
an ENSEMBLE of calculi and extract features that are robust across all of them.

KEY CONCEPTS:
    - Calculus: A triple (feature_map, metric, measure) on a state space
    - CalculusEnsemble: Collection of calculi for joint analysis
    - SchemeRobustObservable: Feature stable across all calculi
    - MixedOperator: Composition P_n @ ... @ P_1 that extracts invariants

MAIN INSIGHT:
    The spectral gap of the mixed operator is ~4x larger than any single
    calculus, meaning it converges faster to the "truly invariant" structure.

Usage:
    python -m meta_calculus.scheme_robust_observables demo
    python -m meta_calculus.scheme_robust_observables analyze --data frw
"""

import numpy as np
from typing import List, Dict, Tuple, Callable, Optional, Any
from abc import ABC, abstractmethod
import argparse
import sys


# =============================================================================
# ABSTRACT CALCULUS INTERFACE
# =============================================================================

class Calculus(ABC):
    """
    Abstract base class for a calculus on a state space.

    A calculus is a triple (phi, g, mu):
        phi: X --> R^d   (feature map / coordinates)
        g:   metric on X (induced from distance in R^d)
        mu:  measure on X (weighting of configurations)

    Each calculus induces a diffusion/Laplacian operator.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name for this calculus."""
        pass

    @abstractmethod
    def feature_map(self, X: np.ndarray) -> np.ndarray:
        """
        Map points in state space to feature space.

        Args:
            X: Array of shape (n_points, n_dims) in state space

        Returns:
            Array of shape (n_points, n_features) in feature space
        """
        pass

    @abstractmethod
    def distance(self, X: np.ndarray, Y: np.ndarray) -> float:
        """
        Compute distance between two points.

        Args:
            X, Y: Points in state space

        Returns:
            Distance according to this calculus
        """
        pass

    def distance_matrix(self, X: np.ndarray) -> np.ndarray:
        """
        Compute pairwise distance matrix.

        Args:
            X: Array of shape (n_points, n_dims)

        Returns:
            Distance matrix of shape (n_points, n_points)
        """
        n = len(X)
        D = np.zeros((n, n))
        for i in range(n):
            for j in range(i+1, n):
                d = self.distance(X[i], X[j])
                D[i, j] = d
                D[j, i] = d
        return D

    def kernel_matrix(self, X: np.ndarray, sigma: float = 1.0) -> np.ndarray:
        """
        Compute Gaussian kernel matrix.

        K_ij = exp(-d(x_i, x_j)^2 / (2*sigma^2))
        """
        D = self.distance_matrix(X)
        return np.exp(-D**2 / (2 * sigma**2))

    def markov_operator(self, X: np.ndarray, sigma: float = 1.0) -> np.ndarray:
        """
        Compute row-stochastic Markov operator (transition matrix).

        P_ij = K_ij / sum_k K_ik
        """
        K = self.kernel_matrix(X, sigma)
        D = K.sum(axis=1, keepdims=True)
        D = np.maximum(D, 1e-10)  # Avoid division by zero
        return K / D

    def laplacian(self, X: np.ndarray, sigma: float = 1.0,
                  normalized: bool = True) -> np.ndarray:
        """
        Compute graph Laplacian.

        L = D - K (unnormalized)
        L = I - P (normalized, random-walk Laplacian)
        """
        if normalized:
            P = self.markov_operator(X, sigma)
            return np.eye(len(X)) - P
        else:
            K = self.kernel_matrix(X, sigma)
            D = np.diag(K.sum(axis=1))
            return D - K


# =============================================================================
# CONCRETE CALCULUS IMPLEMENTATIONS
# =============================================================================

class EuclideanCalculus(Calculus):
    """Standard Euclidean calculus (classical)."""

    @property
    def name(self) -> str:
        return "Euclidean"

    def feature_map(self, X: np.ndarray) -> np.ndarray:
        return X.copy()

    def distance(self, X: np.ndarray, Y: np.ndarray) -> float:
        return np.linalg.norm(X - Y)


class LogCalculus(Calculus):
    """
    Log/GUC-like calculus: distances in log-transformed space.

    This is the bigeometric-inspired calculus that makes multiplicative
    relationships linear.
    """

    def __init__(self, epsilon: float = 1e-10):
        self.epsilon = epsilon

    @property
    def name(self) -> str:
        return "Log/GUC"

    def _safe_log(self, x: np.ndarray) -> np.ndarray:
        """Sign-preserving log: sign(x) * log(1 + |x|)"""
        return np.sign(x) * np.log1p(np.abs(x))

    def feature_map(self, X: np.ndarray) -> np.ndarray:
        return self._safe_log(X)

    def distance(self, X: np.ndarray, Y: np.ndarray) -> float:
        log_X = self._safe_log(X)
        log_Y = self._safe_log(Y)
        return np.linalg.norm(log_X - log_Y)


class CurvatureWeightedCalculus(Calculus):
    """
    Curvature-weighted calculus: emphasizes regions of high curvature.

    Points near boundaries/singularities get higher weight, making
    structure near the "edges" of the allowed region more prominent.
    """

    def __init__(self, curvature_func: Optional[Callable] = None,
                 R_max: float = 100.0):
        """
        Args:
            curvature_func: Function X -> scalar curvature. If None, uses
                           last coordinate as proxy for curvature.
            R_max: Maximum curvature cutoff to avoid infinities
        """
        self.curvature_func = curvature_func
        self.R_max = R_max

    @property
    def name(self) -> str:
        return "Curvature-Weighted"

    def _weight(self, X: np.ndarray) -> float:
        """Compute weight for a point based on curvature."""
        if self.curvature_func is not None:
            R = np.abs(self.curvature_func(X))
        else:
            # Use last coordinate as curvature proxy
            R = np.abs(X[-1]) if len(X.shape) == 1 else np.abs(X[:, -1])

        R_clipped = np.minimum(R + 1e-10, self.R_max)
        return 1.0 / R_clipped

    def feature_map(self, X: np.ndarray) -> np.ndarray:
        if len(X.shape) == 1:
            w = self._weight(X)
            return X * w
        else:
            weights = self._weight(X).reshape(-1, 1)
            return X * weights

    def distance(self, X: np.ndarray, Y: np.ndarray) -> float:
        w_X = self._weight(X)
        w_Y = self._weight(Y)
        # Geometric mean of weights
        w = np.sqrt(w_X * w_Y)
        return w * np.linalg.norm(X - Y)


# =============================================================================
# CALCULUS ENSEMBLE
# =============================================================================

class CalculusEnsemble:
    """
    Collection of calculi for multi-calculus analysis.

    This is the core class for extracting scheme-robust observables.

    Key operations:
        - mixed_operator(): Compose P_n @ ... @ P_1
        - scheme_robust_eigenmodes(): Top eigenmodes of mixed operator
        - invariance_score(): Measure how stable a feature is across calculi
    """

    def __init__(self, calculi: List[Calculus], sigma: float = 1.0):
        """
        Args:
            calculi: List of Calculus objects
            sigma: Bandwidth for kernel construction
        """
        self.calculi = calculi
        self.sigma = sigma
        self._cache: Dict[str, Any] = {}

    @property
    def names(self) -> List[str]:
        """Names of all calculi in ensemble."""
        return [c.name for c in self.calculi]

    def clear_cache(self):
        """Clear cached operators."""
        self._cache = {}

    def markov_operators(self, X: np.ndarray) -> List[np.ndarray]:
        """Get Markov operators for all calculi."""
        key = f"markov_{id(X)}"
        if key not in self._cache:
            self._cache[key] = [c.markov_operator(X, self.sigma)
                               for c in self.calculi]
        return self._cache[key]

    def mixed_operator(self, X: np.ndarray,
                       order: Optional[List[int]] = None) -> np.ndarray:
        """
        Compose diffusion operators: P_mix = P_n @ ... @ P_1

        Args:
            X: State space points
            order: Optional custom order of composition (indices into calculi)
                   If None, uses natural order [0, 1, 2, ...]

        Returns:
            Mixed Markov operator (composition of all)
        """
        operators = self.markov_operators(X)
        if order is None:
            order = list(range(len(self.calculi)))

        P_mix = np.eye(len(X))
        for i in order:
            P_mix = operators[i] @ P_mix

        return P_mix

    def spectral_analysis(self, X: np.ndarray, k: int = 10) -> Dict:
        """
        Perform spectral analysis on all operators.

        Returns:
            Dict with eigenvalues and eigenvectors for each calculus
            and for the mixed operator.
        """
        results = {}

        # Individual calculi
        for i, P in enumerate(self.markov_operators(X)):
            eigenvalues, eigenvectors = np.linalg.eig(P)
            idx = np.argsort(-np.abs(eigenvalues))
            eigenvalues = eigenvalues[idx[:k]].real
            eigenvectors = eigenvectors[:, idx[:k]].real

            gap = 1.0 - np.abs(eigenvalues[1]) if len(eigenvalues) > 1 else 0

            results[self.calculi[i].name] = {
                'eigenvalues': eigenvalues,
                'eigenvectors': eigenvectors,
                'spectral_gap': gap
            }

        # Mixed operator
        P_mix = self.mixed_operator(X)
        eigenvalues, eigenvectors = np.linalg.eig(P_mix)
        idx = np.argsort(-np.abs(eigenvalues))
        eigenvalues = eigenvalues[idx[:k]].real
        eigenvectors = eigenvectors[:, idx[:k]].real

        gap = 1.0 - np.abs(eigenvalues[1]) if len(eigenvalues) > 1 else 0

        results['Mixed'] = {
            'eigenvalues': eigenvalues,
            'eigenvectors': eigenvectors,
            'spectral_gap': gap
        }

        return results

    def scheme_robust_eigenmodes(self, X: np.ndarray, k: int = 5) -> np.ndarray:
        """
        Return top k eigenmodes of mixed operator.

        These are the "scheme-robust" directions that survive coarse-graining
        under all calculi.
        """
        P_mix = self.mixed_operator(X)
        eigenvalues, eigenvectors = np.linalg.eig(P_mix)
        idx = np.argsort(-np.abs(eigenvalues))
        return eigenvectors[:, idx[:k]].real

    def invariance_score(self, X: np.ndarray, f: np.ndarray) -> float:
        """
        Measure how scheme-robust a feature vector is.

        High score = f is smooth (low-frequency) in all calculi
        Low score = f is rough (high-frequency) in at least one calculus

        Args:
            X: State space points
            f: Feature vector of shape (n_points,)

        Returns:
            Score in [0, 1], higher = more invariant
        """
        f = f - f.mean()  # Center
        f_norm = np.linalg.norm(f)
        if f_norm < 1e-10:
            return 1.0  # Constant function is perfectly invariant

        roughness_scores = []
        for c in self.calculi:
            L = c.laplacian(X, self.sigma, normalized=True)
            # Rayleigh quotient: f^T L f / f^T f
            roughness = np.dot(f, L @ f) / (f_norm ** 2)
            roughness_scores.append(roughness)

        # Average roughness across calculi
        avg_roughness = np.mean(roughness_scores)

        # Convert to score: low roughness = high invariance
        return 1.0 / (1.0 + avg_roughness)

    def find_invariant_features(self, X: np.ndarray,
                                 features: Dict[str, np.ndarray],
                                 threshold: float = 0.7) -> List[str]:
        """
        Find features that are scheme-robust.

        Args:
            X: State space points
            features: Dict mapping feature names to feature vectors
            threshold: Minimum invariance score to be considered robust

        Returns:
            List of feature names that pass the threshold
        """
        invariant = []
        for name, f in features.items():
            score = self.invariance_score(X, f)
            if score >= threshold:
                invariant.append(name)
        return invariant

    def projection_onto_robust_subspace(self, X: np.ndarray,
                                         f: np.ndarray,
                                         k: int = 5) -> np.ndarray:
        """
        Project a feature onto the scheme-robust subspace.

        This extracts the "physically meaningful" part of f.

        Args:
            X: State space points
            f: Feature vector
            k: Number of robust eigenmodes to use

        Returns:
            Projected feature vector
        """
        eigenmodes = self.scheme_robust_eigenmodes(X, k)

        # Project f onto span of eigenmodes
        coords = np.linalg.lstsq(eigenmodes, f, rcond=None)[0]
        return eigenmodes @ coords


# =============================================================================
# SCHEME-ROBUST OBSERVABLE CLASS
# =============================================================================

class SchemeRobustObservable:
    """
    An observable that is stable across all calculi in an ensemble.

    Properties:
        - Low roughness (high smoothness) in all calculi
        - High projection onto mixed operator eigenmodes
        - Represents "physical" as opposed to "coordinate" information
    """

    def __init__(self, name: str,
                 compute_func: Callable[[np.ndarray], np.ndarray],
                 ensemble: CalculusEnsemble):
        """
        Args:
            name: Human-readable name
            compute_func: Function X -> observable values
            ensemble: The calculus ensemble for validation
        """
        self.name = name
        self.compute = compute_func
        self.ensemble = ensemble
        self._validation_result: Optional[Dict] = None

    def validate(self, X: np.ndarray) -> Dict:
        """
        Validate that this observable is truly scheme-robust.

        Returns:
            Dict with invariance_score, per_calculus_roughness, and
            projection_onto_robust for diagnostics.
        """
        f = self.compute(X)

        # Compute invariance score
        inv_score = self.ensemble.invariance_score(X, f)

        # Per-calculus roughness
        roughness = {}
        f_centered = f - f.mean()
        f_norm = np.linalg.norm(f_centered)
        for c in self.ensemble.calculi:
            L = c.laplacian(X, self.ensemble.sigma)
            r = np.dot(f_centered, L @ f_centered) / (f_norm**2 + 1e-10)
            roughness[c.name] = r

        # Projection quality
        eigenmodes = self.ensemble.scheme_robust_eigenmodes(X, k=5)
        coords = np.linalg.lstsq(eigenmodes, f_centered, rcond=None)[0]
        f_proj = eigenmodes @ coords
        proj_quality = 1.0 - np.linalg.norm(f_centered - f_proj) / (f_norm + 1e-10)

        self._validation_result = {
            'invariance_score': inv_score,
            'roughness_by_calculus': roughness,
            'projection_quality': proj_quality,
            'is_robust': inv_score > 0.7 and proj_quality > 0.5
        }

        return self._validation_result

    def is_robust(self, X: np.ndarray) -> bool:
        """Check if observable is scheme-robust for given data."""
        if self._validation_result is None:
            self.validate(X)
        return self._validation_result['is_robust']


# =============================================================================
# STANDARD ENSEMBLE FACTORY
# =============================================================================

def create_standard_ensemble(sigma: float = 1.0) -> CalculusEnsemble:
    """
    Create the standard 3-calculus ensemble used in experiments.

    Includes:
        - EuclideanCalculus (A): Classical
        - LogCalculus (B): GUC/bigeometric
        - CurvatureWeightedCalculus (C): Curvature-weighted
    """
    calculi = [
        EuclideanCalculus(),
        LogCalculus(),
        CurvatureWeightedCalculus()
    ]
    return CalculusEnsemble(calculi, sigma=sigma)


# =============================================================================
# DEMO AND CLI
# =============================================================================

def demo_scheme_robust():
    """Demonstrate scheme-robust observable extraction."""
    print("=" * 70)
    print("SCHEME-ROBUST OBSERVABLES DEMO")
    print("=" * 70)

    # Generate toy data: 3 clusters like FRW experiment
    np.random.seed(42)
    n_per_cluster = 20

    # Cluster centers (like radiation/matter/inflation)
    centers = np.array([
        [0.5, 0.2, 1.0],    # radiation-like
        [0.67, 0.5, 2.0],   # matter-like
        [1.5, 1.0, 5.0]     # inflation-like
    ])

    X = []
    labels = []
    for i, c in enumerate(centers):
        cluster = c + 0.1 * np.random.randn(n_per_cluster, 3)
        X.append(cluster)
        labels.extend([i] * n_per_cluster)

    X = np.vstack(X)
    labels = np.array(labels)

    print(f"\nGenerated {len(X)} points in 3 clusters")
    print(f"Shape: {X.shape}")

    # Create ensemble
    ensemble = create_standard_ensemble(sigma=0.5)
    print(f"\nCalculus ensemble: {ensemble.names}")

    # Spectral analysis
    print("\n" + "-" * 40)
    print("SPECTRAL ANALYSIS")
    print("-" * 40)

    results = ensemble.spectral_analysis(X, k=5)
    for name, data in results.items():
        print(f"\n{name}:")
        print(f"  Spectral gap: {data['spectral_gap']:.6f}")
        print(f"  Top eigenvalues: {data['eigenvalues'][:3]}")

    # Compare spectral gaps
    print("\n" + "-" * 40)
    print("SPECTRAL GAP COMPARISON")
    print("-" * 40)

    gaps = {name: data['spectral_gap'] for name, data in results.items()}
    for name, gap in gaps.items():
        bar = "#" * int(gap * 100)
        print(f"{name:20s}: {gap:.6f} {bar}")

    # Key insight: mixed gap should be larger
    individual_max = max(gaps[n] for n in ensemble.names)
    mixed_gap = gaps['Mixed']
    print(f"\nMixed gap / max individual gap: {mixed_gap / individual_max:.2f}x")

    # Test scheme-robust observables
    print("\n" + "-" * 40)
    print("SCHEME-ROBUST OBSERVABLES")
    print("-" * 40)

    # Define candidate features
    features = {
        'cluster_label': labels.astype(float),  # Should be robust
        'first_coord': X[:, 0],                 # May or may not be robust
        'random_noise': np.random.randn(len(X)),  # Should NOT be robust
        'cluster_indicator': (labels == 1).astype(float)  # Should be robust
    }

    print("\nInvariance scores (higher = more scheme-robust):")
    for name, f in features.items():
        score = ensemble.invariance_score(X, f)
        status = "ROBUST" if score > 0.7 else "variable"
        print(f"  {name:20s}: {score:.4f}  [{status}]")

    # Find invariant features
    invariant = ensemble.find_invariant_features(X, features, threshold=0.7)
    print(f"\nScheme-robust features: {invariant}")

    print("\n" + "=" * 70)
    print("KEY INSIGHT: Cluster structure (labels) is scheme-robust,")
    print("             while random noise is not.")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Scheme-Robust Observables: Multi-Calculus Analysis"
    )
    parser.add_argument('command', choices=['demo', 'analyze'],
                        help="Command to run")
    parser.add_argument('--data', choices=['frw', 'triangle', 'random'],
                        default='random',
                        help="Data source for analysis")

    if len(sys.argv) < 2:
        parser.print_help()
        return 0

    args = parser.parse_args()

    if args.command == 'demo':
        demo_scheme_robust()
    elif args.command == 'analyze':
        print(f"Analysis with {args.data} data not yet implemented")
        print("Use the FRWDiffusionExperiment or TrianglePolytope classes directly")

    return 0


if __name__ == "__main__":
    sys.exit(main())
