#!/usr/bin/env python3
"""
Multi-Operator RG: Renormalization Group Interpretation of Multi-Calculus

This module formalizes the insight that multi-calculus diffusion acts like
a joint coarse-graining / RG procedure on solution spaces.

KEY INSIGHT:
    Composing diffusion operators from different calculi:
        P_mix = P_C @ P_B @ P_A

    Acts as a joint coarse-graining that:
        1. Damps modes high-frequency in ANY calculus
        2. Preserves modes smooth in ALL calculi
        3. Has larger spectral gap = faster convergence to stable structure

    This is analogous to multi-scheme renormalization in QFT.

INTERPRETATION:
    - Each calculus = different "RG scheme" (notion of scale/roughness)
    - Joint low-lying eigenmodes = approximate fixed-point directions
    - Scheme-robust observables = relevant operators under RG

Usage:
    python -m meta_calculus.multi_operator_rg flow
    python -m meta_calculus.multi_operator_rg fixed_points
"""

import numpy as np
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass
import argparse
import sys

from .scheme_robust_observables import (
    Calculus, CalculusEnsemble, create_standard_ensemble,
    EuclideanCalculus, LogCalculus, CurvatureWeightedCalculus
)


# =============================================================================
# RG FLOW ON SOLUTION SPACE
# =============================================================================

@dataclass
class RGFlowResult:
    """Result of an RG flow computation."""
    trajectory: np.ndarray       # (n_steps, n_points, n_features)
    eigenvalue_evolution: np.ndarray  # (n_steps, k) eigenvalues at each step
    convergence_rate: float      # How fast the flow converges
    fixed_point_modes: np.ndarray  # Approximate fixed-point eigenmodes
    relevant_count: int          # Number of relevant (slow-decaying) modes


class MultiOperatorRG:
    """
    Multi-Operator RG flow on a solution space.

    Interprets the composition of diffusion operators as an RG step:
        - High-frequency modes (in any calculus) are damped
        - Low-frequency modes (in all calculi) survive
        - Fixed points = stable structure under all calculi

    This provides a principled way to extract physically meaningful
    structure from a space of solutions (cosmologies, amplitudes, etc.)
    """

    def __init__(self, ensemble: CalculusEnsemble,
                 relevance_threshold: float = 0.9):
        """
        Args:
            ensemble: Calculus ensemble for RG analysis
            relevance_threshold: Eigenvalue threshold for "relevant" modes
                                 (modes with |lambda| > threshold are relevant)
        """
        self.ensemble = ensemble
        self.relevance_threshold = relevance_threshold

    def rg_step(self, P_current: np.ndarray, X: np.ndarray) -> np.ndarray:
        """
        Perform one RG step: compose with mixed operator.

        This is the core operation that coarse-grains the state space.
        """
        P_mix = self.ensemble.mixed_operator(X)
        return P_mix @ P_current

    def flow(self, X: np.ndarray, n_steps: int = 10,
             track_eigenvalues: bool = True) -> RGFlowResult:
        """
        Run the RG flow for multiple steps.

        At each step, we track:
            - How the operator evolves
            - How eigenvalues decay
            - What structure survives

        Args:
            X: State space points
            n_steps: Number of RG steps
            track_eigenvalues: Whether to compute eigenvalues at each step

        Returns:
            RGFlowResult with trajectory and diagnostics
        """
        n = len(X)
        P = np.eye(n)  # Start with identity

        eigenvalue_evolution = [] if track_eigenvalues else None

        for step in range(n_steps):
            P = self.rg_step(P, X)

            if track_eigenvalues:
                eigenvalues = np.linalg.eigvals(P)
                eigenvalues = np.sort(np.abs(eigenvalues))[::-1]
                eigenvalue_evolution.append(eigenvalues[:10])

        # Analyze final state
        final_eigenvalues, final_eigenvectors = np.linalg.eig(P)
        idx = np.argsort(-np.abs(final_eigenvalues))
        final_eigenvalues = np.abs(final_eigenvalues[idx])
        final_eigenvectors = final_eigenvectors[:, idx].real

        # Count relevant modes
        relevant_count = np.sum(final_eigenvalues > self.relevance_threshold)

        # Estimate convergence rate from eigenvalue gap
        if len(final_eigenvalues) > 1:
            convergence_rate = 1.0 - final_eigenvalues[1]
        else:
            convergence_rate = 1.0

        return RGFlowResult(
            trajectory=P,  # Final operator (could store all if needed)
            eigenvalue_evolution=np.array(eigenvalue_evolution) if track_eigenvalues else None,
            convergence_rate=convergence_rate,
            fixed_point_modes=final_eigenvectors[:, :relevant_count],
            relevant_count=relevant_count
        )

    def find_fixed_points(self, X: np.ndarray, k: int = 5) -> Dict:
        """
        Find approximate fixed points of the RG flow.

        These are modes that are stable under all calculi, corresponding
        to the "physical" structure of the solution space.

        Returns:
            Dict with:
                - fixed_point_modes: Eigenvectors with eigenvalue ~ 1
                - eigenvalues: Corresponding eigenvalues
                - stability: How stable each mode is
        """
        P_mix = self.ensemble.mixed_operator(X)

        eigenvalues, eigenvectors = np.linalg.eig(P_mix)
        idx = np.argsort(-np.abs(eigenvalues))
        eigenvalues = eigenvalues[idx[:k]]
        eigenvectors = eigenvectors[:, idx[:k]].real

        # Stability = how close eigenvalue is to 1
        stability = 1.0 - np.abs(1.0 - np.abs(eigenvalues))

        return {
            'fixed_point_modes': eigenvectors,
            'eigenvalues': eigenvalues.real,
            'stability': stability,
            'n_relevant': np.sum(np.abs(eigenvalues) > self.relevance_threshold)
        }

    def classify_modes(self, X: np.ndarray, k: int = 10) -> Dict:
        """
        Classify modes as relevant, marginal, or irrelevant.

        In RG language:
            - Relevant: |lambda| ~ 1, survives coarse-graining (physical)
            - Marginal: |lambda| ~ threshold, borderline
            - Irrelevant: |lambda| << 1, washed out (coordinate artifacts)

        Returns:
            Dict with classified modes and their properties
        """
        P_mix = self.ensemble.mixed_operator(X)
        eigenvalues, eigenvectors = np.linalg.eig(P_mix)

        abs_eigenvalues = np.abs(eigenvalues)
        idx = np.argsort(-abs_eigenvalues)

        classification = {
            'relevant': {'eigenvalues': [], 'modes': [], 'indices': []},
            'marginal': {'eigenvalues': [], 'modes': [], 'indices': []},
            'irrelevant': {'eigenvalues': [], 'modes': [], 'indices': []}
        }

        marginal_lower = self.relevance_threshold - 0.1
        marginal_upper = self.relevance_threshold + 0.05

        for i in idx[:k]:
            ev = abs_eigenvalues[i]
            mode = eigenvectors[:, i].real

            if ev > marginal_upper:
                cat = 'relevant'
            elif ev > marginal_lower:
                cat = 'marginal'
            else:
                cat = 'irrelevant'

            classification[cat]['eigenvalues'].append(ev)
            classification[cat]['modes'].append(mode)
            classification[cat]['indices'].append(i)

        # Convert to arrays
        for cat in classification:
            if classification[cat]['eigenvalues']:
                classification[cat]['eigenvalues'] = np.array(classification[cat]['eigenvalues'])
                classification[cat]['modes'] = np.array(classification[cat]['modes']).T

        return classification

    def anomalous_dimensions(self, X: np.ndarray, k: int = 5) -> Dict:
        """
        Compute anomalous dimensions for modes.

        In standard RG, anomalous dimension gamma measures deviation from
        free-field scaling. Here, we define it as deviation from |lambda| = 1.

        gamma_i = -log|lambda_i| / log(2)

        So gamma = 0 means |lambda| = 1 (marginal/fixed point)
           gamma > 0 means |lambda| < 1 (irrelevant, decays)
           gamma < 0 would mean |lambda| > 1 (relevant, grows - but bounded by 1)

        Returns:
            Dict with anomalous dimensions and interpretation
        """
        P_mix = self.ensemble.mixed_operator(X)
        eigenvalues, eigenvectors = np.linalg.eig(P_mix)

        abs_eigenvalues = np.abs(eigenvalues)
        idx = np.argsort(-abs_eigenvalues)[:k]

        eigenvalues_sorted = eigenvalues[idx]
        abs_sorted = abs_eigenvalues[idx]

        # Compute anomalous dimensions
        # Avoid log(0) by clipping
        abs_clipped = np.clip(abs_sorted, 1e-10, 1.0)
        gamma = -np.log(abs_clipped) / np.log(2)

        return {
            'eigenvalues': eigenvalues_sorted.real,
            'abs_eigenvalues': abs_sorted,
            'anomalous_dimensions': gamma,
            'interpretation': [
                'fixed point' if g < 0.01 else
                'marginally irrelevant' if g < 0.1 else
                'irrelevant'
                for g in gamma
            ]
        }


# =============================================================================
# COARSE-GRAINING ANALYSIS
# =============================================================================

class CoarseGrainingAnalysis:
    """
    Analyze how structure evolves under multi-calculus coarse-graining.

    Key questions:
        - What features survive coarse-graining?
        - How do clusters/classifications sharpen or blur?
        - At what "scale" does physical structure emerge?
    """

    def __init__(self, ensemble: CalculusEnsemble):
        self.ensemble = ensemble
        self.rg = MultiOperatorRG(ensemble)

    def feature_survival(self, X: np.ndarray,
                         features: Dict[str, np.ndarray],
                         n_steps: int = 5) -> Dict:
        """
        Track how features survive under RG flow.

        Args:
            X: State space points
            features: Dict of feature_name -> feature_vector
            n_steps: Number of RG steps

        Returns:
            Dict mapping feature names to survival curves
        """
        P = np.eye(len(X))

        survival = {name: [1.0] for name in features}

        for step in range(n_steps):
            P = self.rg.rg_step(P, X)

            for name, f in features.items():
                # Apply P to feature (as if it were a distribution)
                f_coarse = P @ f
                # Measure how much of original structure remains
                f_norm = np.linalg.norm(f)
                if f_norm > 1e-10:
                    correlation = np.abs(np.dot(f, f_coarse)) / (f_norm * np.linalg.norm(f_coarse) + 1e-10)
                else:
                    correlation = 0.0
                survival[name].append(correlation)

        return survival

    def cluster_sharpening(self, X: np.ndarray,
                           labels: np.ndarray,
                           n_steps: int = 5) -> Dict:
        """
        Measure how cluster separation evolves under RG.

        If clusters represent physical classifications, they should
        sharpen (become more separated) under coarse-graining.

        Args:
            X: State space points
            labels: Cluster labels (integer array)
            n_steps: Number of RG steps

        Returns:
            Dict with separation metrics at each step
        """
        unique_labels = np.unique(labels)
        n_clusters = len(unique_labels)

        P = np.eye(len(X))
        separation_history = []

        for step in range(n_steps + 1):
            # Compute inter-cluster vs intra-cluster distances
            # Using the current (coarse-grained) metric

            if step > 0:
                P = self.rg.rg_step(P, X)

            # Effective distances under current operator
            # (Approximate by looking at how P mixes points)
            intra_distances = []
            inter_distances = []

            for i in range(len(X)):
                for j in range(i+1, len(X)):
                    # "Distance" = how differently P treats these points
                    # Low correlation = they're mixed together
                    d = 1.0 - np.abs(np.dot(P[i], P[j]))

                    if labels[i] == labels[j]:
                        intra_distances.append(d)
                    else:
                        inter_distances.append(d)

            mean_intra = np.mean(intra_distances) if intra_distances else 0
            mean_inter = np.mean(inter_distances) if inter_distances else 0

            # Separation ratio: higher = clusters more distinct
            separation = mean_inter / (mean_intra + 1e-10)
            separation_history.append(separation)

        return {
            'separation_by_step': np.array(separation_history),
            'initial_separation': separation_history[0],
            'final_separation': separation_history[-1],
            'sharpening_factor': separation_history[-1] / (separation_history[0] + 1e-10),
            'sharpens': separation_history[-1] > separation_history[0]
        }

    def scale_structure_emergence(self, X: np.ndarray,
                                    structure_detector: Callable[[np.ndarray], float],
                                    n_steps: int = 10) -> Dict:
        """
        Find at what "scale" (RG step) a particular structure emerges.

        Args:
            X: State space points
            structure_detector: Function that measures structure strength
                               Returns higher values when structure is clearer
            n_steps: Number of RG steps

        Returns:
            Dict with structure strength at each scale
        """
        P = np.eye(len(X))
        structure_by_scale = []

        for step in range(n_steps + 1):
            if step > 0:
                P = self.rg.rg_step(P, X)

            # Apply P to get "coarse-grained" point cloud
            X_coarse = P @ X

            strength = structure_detector(X_coarse)
            structure_by_scale.append(strength)

        # Find emergence scale (where structure becomes clear)
        max_strength = max(structure_by_scale)
        emergence_scale = next(
            (i for i, s in enumerate(structure_by_scale) if s > 0.8 * max_strength),
            n_steps
        )

        return {
            'structure_by_scale': np.array(structure_by_scale),
            'emergence_scale': emergence_scale,
            'max_strength': max_strength,
            'final_strength': structure_by_scale[-1]
        }


# =============================================================================
# DEMO AND CLI
# =============================================================================

def demo_rg_flow():
    """Demonstrate RG flow analysis."""
    print("=" * 70)
    print("MULTI-OPERATOR RG FLOW DEMO")
    print("=" * 70)

    # Generate clustered data
    np.random.seed(42)
    n_per_cluster = 15

    centers = np.array([
        [0.5, 0.5, 1.0],
        [2.0, 1.5, 3.0],
        [3.5, 2.5, 6.0]
    ])

    X = []
    labels = []
    for i, c in enumerate(centers):
        cluster = c + 0.2 * np.random.randn(n_per_cluster, 3)
        X.append(cluster)
        labels.extend([i] * n_per_cluster)

    X = np.vstack(X)
    labels = np.array(labels)

    print(f"\nGenerated {len(X)} points in 3 clusters")

    # Create ensemble and RG
    ensemble = create_standard_ensemble(sigma=0.8)
    rg = MultiOperatorRG(ensemble, relevance_threshold=0.9)

    # Run RG flow
    print("\n" + "-" * 40)
    print("RG FLOW ANALYSIS")
    print("-" * 40)

    flow_result = rg.flow(X, n_steps=5)

    print(f"\nConvergence rate: {flow_result.convergence_rate:.4f}")
    print(f"Number of relevant modes: {flow_result.relevant_count}")

    if flow_result.eigenvalue_evolution is not None:
        print("\nEigenvalue evolution (top 3):")
        for step, evs in enumerate(flow_result.eigenvalue_evolution):
            print(f"  Step {step}: {evs[:3]}")

    # Classify modes
    print("\n" + "-" * 40)
    print("MODE CLASSIFICATION")
    print("-" * 40)

    classification = rg.classify_modes(X)
    for cat in ['relevant', 'marginal', 'irrelevant']:
        evs = classification[cat]['eigenvalues']
        n = len(evs) if isinstance(evs, np.ndarray) and len(evs) > 0 else 0
        print(f"\n{cat.capitalize()}: {n} modes")
        if n > 0:
            print(f"  Eigenvalues: {evs[:3]}")

    # Anomalous dimensions
    print("\n" + "-" * 40)
    print("ANOMALOUS DIMENSIONS")
    print("-" * 40)

    anom = rg.anomalous_dimensions(X)
    for i in range(min(5, len(anom['anomalous_dimensions']))):
        gamma = anom['anomalous_dimensions'][i]
        interp = anom['interpretation'][i]
        ev = anom['abs_eigenvalues'][i]
        print(f"  Mode {i}: gamma = {gamma:.4f} ({interp}), |lambda| = {ev:.4f}")

    # Coarse-graining analysis
    print("\n" + "-" * 40)
    print("COARSE-GRAINING ANALYSIS")
    print("-" * 40)

    cg = CoarseGrainingAnalysis(ensemble)

    # Feature survival
    features = {
        'cluster_label': labels.astype(float),
        'coord_0': X[:, 0],
        'noise': np.random.randn(len(X))
    }

    survival = cg.feature_survival(X, features, n_steps=3)
    print("\nFeature survival under RG:")
    for name, curve in survival.items():
        final = curve[-1]
        print(f"  {name:15s}: {curve[0]:.3f} -> {final:.3f} "
              f"({'survives' if final > 0.5 else 'decays'})")

    # Cluster sharpening
    sharpening = cg.cluster_sharpening(X, labels, n_steps=3)
    print(f"\nCluster separation:")
    print(f"  Initial: {sharpening['initial_separation']:.4f}")
    print(f"  Final:   {sharpening['final_separation']:.4f}")
    print(f"  Sharpening factor: {sharpening['sharpening_factor']:.2f}x")
    print(f"  Clusters sharpen: {sharpening['sharpens']}")

    print("\n" + "=" * 70)
    print("KEY INSIGHT: RG flow reveals which structure is 'physical'")
    print("(survives all calculi) vs 'coordinate artifact' (calculus-dependent)")
    print("=" * 70)


def demo_fixed_points():
    """Demonstrate fixed point analysis."""
    print("=" * 70)
    print("FIXED POINT ANALYSIS DEMO")
    print("=" * 70)

    np.random.seed(123)

    # Create data with clear structure
    n = 40
    t = np.linspace(0.5, 2.0, n)
    n_vals = 0.5 + 0.15 * np.random.randn(n)  # Power law exponents
    H_vals = 1.0 / t                           # Hubble
    R_vals = 1.0 / t**2                        # Ricci scalar

    X = np.column_stack([n_vals, H_vals, R_vals])

    print(f"\nGenerated {len(X)} FRW-like solutions")
    print("  n ~ 0.5 (radiation-like)")
    print("  H ~ 1/t")
    print("  R ~ 1/t^2")

    ensemble = create_standard_ensemble(sigma=0.5)
    rg = MultiOperatorRG(ensemble)

    # Find fixed points
    print("\n" + "-" * 40)
    print("FIXED POINTS OF RG FLOW")
    print("-" * 40)

    fp = rg.find_fixed_points(X, k=5)

    print(f"\nNumber of relevant modes: {fp['n_relevant']}")
    print("\nTop 5 modes:")
    for i in range(5):
        ev = fp['eigenvalues'][i]
        stab = fp['stability'][i]
        print(f"  Mode {i}: lambda = {ev:.4f}, stability = {stab:.4f}")

    print("\n" + "=" * 70)
    print("Modes with lambda ~ 1 and high stability are 'physical' degrees of freedom")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Multi-Operator RG Analysis"
    )
    parser.add_argument('command', choices=['flow', 'fixed_points'],
                        nargs='?', default='flow',
                        help="Analysis to run")

    if len(sys.argv) > 1:
        args = parser.parse_args()
    else:
        args = argparse.Namespace(command='flow')

    if args.command == 'flow':
        demo_rg_flow()
    elif args.command == 'fixed_points':
        demo_fixed_points()

    return 0


if __name__ == "__main__":
    sys.exit(main())
