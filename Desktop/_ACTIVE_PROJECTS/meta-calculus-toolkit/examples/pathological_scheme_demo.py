#!/usr/bin/env python3
"""
Pathological Scheme Demo: Controlled Failure Examples

This script demonstrates cases where scheme invariance BREAKS, providing
concrete examples of:

1. INADMISSIBLE C-SCHEMES: Meta-derivatives where u(t) vanishes
2. SINGULAR BREAKING: Near Big Bang where C-schemes diverge
3. ANOMALY-LIKE OBSTRUCTIONS: Where transformations fail axiom checks

These examples show that the framework is NON-TRIVIAL: not every
transformation is in G_scheme, and breaking can be detected.

Usage:
    python pathological_scheme_demo.py

Author: Meta-Calculus Development Team
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Tuple, Dict, Any
import sys
import os

# Add parent directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from meta_calculus.scheme_morphism import (
    CSchemeTimeReparam,
    create_meta_derivative_morphism,
    check_meta_derivative_admissible,
    AdmissibilityAxiom
)
from meta_calculus.frw_scheme_robustness import (
    ClassicalCScheme, MetaCScheme, BigeometricCScheme,
    FRWParameters, FRWModel, FRWSchemeRobustnessTest
)


# =============================================================================
# DEMO 1: INADMISSIBLE META-DERIVATIVES
# =============================================================================

def demo_inadmissible_meta_derivatives():
    """
    Demonstrate meta-derivatives that FAIL admissibility.

    Key insight: When u(t) vanishes or goes negative, the coordinate
    transformation tau(t) = integral(u(s)ds) is not invertible.
    Therefore, no admissible pullback to standard calculus exists.
    """
    print("\n" + "=" * 70)
    print("DEMO 1: INADMISSIBLE META-DERIVATIVES")
    print("=" * 70)

    # Case 1: u(t) = t - 5 (vanishes at t=5)
    print("\n--- Case 1: u(t) = t - 5 (vanishes at t=5) ---")
    u_bad1 = lambda t: t - 5
    v_bad1 = lambda t: 0.0

    morphism1 = create_meta_derivative_morphism(u_bad1, v_bad1, (0, 10))
    report1 = morphism1.check_c_scheme_admissibility()

    print(f"Admissible: {report1.is_admissible}")
    print(f"Confidence: {report1.overall_confidence:.2f}")
    for v in report1.verifications:
        print(f"  {v}")

    # Case 2: u(t) = sin(t) (vanishes at t = n*pi)
    print("\n--- Case 2: u(t) = sin(t) (vanishes at t = 0, pi, 2pi, ...) ---")
    u_bad2 = lambda t: np.sin(t)
    v_bad2 = lambda t: 0.0

    morphism2 = create_meta_derivative_morphism(u_bad2, v_bad2, (0.1, 10))
    report2 = morphism2.check_c_scheme_admissibility()

    print(f"Admissible: {report2.is_admissible}")
    print(f"Confidence: {report2.overall_confidence:.2f}")

    # Case 3: u(t) = exp(-t^2) (goes to zero as t -> infinity)
    print("\n--- Case 3: u(t) = exp(-t^2) (asymptotically zero) ---")
    u_marginal = lambda t: np.exp(-t**2)
    v_marginal = lambda t: 0.0

    # This is technically admissible on finite domain (u > 0)
    # but numerically problematic for large t
    morphism3 = create_meta_derivative_morphism(u_marginal, v_marginal, (0, 3))
    report3 = morphism3.check_c_scheme_admissibility()

    print(f"Admissible on (0,3): {report3.is_admissible}")
    print(f"Note: u becomes very small (u(3) = {u_marginal(3):.2e})")

    # Contrast: Admissible case
    print("\n--- Contrast: ADMISSIBLE u(t) = 1 + 0.5*cos(t) ---")
    u_good = lambda t: 1 + 0.5 * np.cos(t)  # Always > 0.5
    v_good = lambda t: 0.1 * t

    is_admissible = check_meta_derivative_admissible(u_good, v_good, (0, 10))
    print(f"Admissible: {is_admissible}")

    return {
        'case1_inadmissible': not report1.is_admissible,
        'case2_inadmissible': not report2.is_admissible,
        'case3_marginal': report3.is_admissible,
        'good_case_admissible': is_admissible
    }


# =============================================================================
# DEMO 2: SINGULAR REGIME BREAKING
# =============================================================================

def demo_singular_breaking():
    """
    Demonstrate scheme breaking near the Big Bang singularity.

    Key insight: Different C-schemes give different predictions for H(t)
    near t=0, but this is EXPECTED because we're probing singular regime.

    The physical question: Is this breaking numerical artifact, expected
    singular behavior, or genuine new physics?
    """
    print("\n" + "=" * 70)
    print("DEMO 2: SINGULAR REGIME BREAKING")
    print("=" * 70)

    tester = FRWSchemeRobustnessTest()

    # Test at progressively smaller times (approaching singularity)
    time_scales = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]

    print("\nH(t) comparison across C-schemes near t=0:")
    print("-" * 60)
    print(f"{'t':<12} {'Classical':<15} {'Meta':<15} {'Bigeometric':<15}")
    print("-" * 60)

    breaking_data = []

    for t in time_scales:
        # Power-law model: a(t) = t^n, H(t) = n/t (classical)
        # Other schemes give different H(t) by construction

        H_classical = tester.models['classical'].hubble_parameter_power_law(t)
        H_meta = tester.models['meta'].hubble_parameter_power_law(t)
        H_bigeometric = tester.models['bigeometric'].hubble_parameter_power_law(t)

        # Calculate relative spread
        H_values = [H_classical, H_meta, H_bigeometric]
        mean_H = np.mean([h for h in H_values if np.isfinite(h)])
        spread = np.std([h for h in H_values if np.isfinite(h)]) / mean_H if mean_H > 0 else 0

        print(f"{t:<12.1e} {H_classical:<15.2e} {H_meta:<15.2e} {H_bigeometric:<15.2e}")

        breaking_data.append({
            't': t,
            'H_classical': H_classical,
            'H_meta': H_meta,
            'H_bigeometric': H_bigeometric,
            'relative_spread': spread
        })

    print("-" * 60)

    # Hunt for breaking points
    print("\nHunting for breaking points in singular regime...")
    result = tester.hunt_breaking_points(t_range=(1e-5, 1e-1), n_points=50)

    print(f"\nResults:")
    print(f"  Points tested: {result['n_tested']}")
    print(f"  Breaking points found: {result['n_breaking']}")
    print(f"  Interpretation: {result['interpretation']}")

    # Key insight
    print("\n" + "=" * 60)
    print("INTERPRETATION:")
    print("=" * 60)
    print("""
    H(t) differs across C-schemes by CONSTRUCTION. This is expected!

    For power-law a(t) = t^n:
      - Classical: H = n/t (diverges as t -> 0)
      - Meta: H_meta depends on u(t), v(t) choice
      - Bigeometric: H_BG = n (constant for power law!)

    The scheme-ROBUST observable is H(z), not H(t).
    H(z) is defined via redshift, independent of time coordinate.

    This demonstrates that:
    1. C-scheme breaking in singular regime is EXPECTED
    2. Physical observables (H(z), BBN, CMB) remain robust
    3. Time coordinate t is scheme-dependent scaffolding
    """)

    return {
        'breaking_data': breaking_data,
        'hunt_result': result
    }


# =============================================================================
# DEMO 3: PHYSICAL VS ARTIFACT BREAKING
# =============================================================================

def demo_physical_vs_artifact():
    """
    Demonstrate how to distinguish:
    1. Numerical artifacts (roundoff, integration error)
    2. Expected singular behavior (t -> 0)
    3. Potential new physics (unexpected breaking in regular regime)

    This is the core of the scheme-breaking detector.
    """
    print("\n" + "=" * 70)
    print("DEMO 3: CLASSIFYING BREAKING EVENTS")
    print("=" * 70)

    from meta_calculus.scheme_breaking_detector import (
        BreakingClassifier, BreakingType
    )

    classifier = BreakingClassifier()

    # Test cases
    cases = [
        {
            'name': 'Numerical noise',
            'difference': 1e-14,
            'relative_difference': 1e-14,
            'is_near_singularity': False,
            'is_regular_regime': True,
            'expected_type': BreakingType.NONE
        },
        {
            'name': 'Small numerical artifact',
            'difference': 1e-7,
            'relative_difference': 1e-6,
            'is_near_singularity': False,
            'is_regular_regime': True,
            'expected_type': BreakingType.NUMERICAL
        },
        {
            'name': 'Singular regime behavior',
            'difference': 100.0,
            'relative_difference': 0.5,
            'is_near_singularity': True,
            'is_regular_regime': False,
            'expected_type': BreakingType.SINGULAR
        },
        {
            'name': 'Potential new physics (!)',
            'difference': 0.1,
            'relative_difference': 0.1,
            'is_near_singularity': False,
            'is_regular_regime': True,
            'expected_type': BreakingType.PHYSICAL
        },
    ]

    print("\nClassification Results:")
    print("-" * 70)

    results = []
    for case in cases:
        btype, confidence = classifier.classify(
            difference=case['difference'],
            relative_difference=case['relative_difference'],
            is_near_singularity=case['is_near_singularity'],
            is_regular_regime=case['is_regular_regime']
        )

        correct = (btype == case['expected_type'])
        status = "[PASS]" if correct else "[FAIL]"

        print(f"\n{status} {case['name']}:")
        print(f"  Input: diff={case['difference']:.1e}, rel={case['relative_difference']:.1e}")
        print(f"  Classified as: {btype.value}")
        print(f"  Expected: {case['expected_type'].value}")
        print(f"  Confidence: {confidence:.2f}")

        results.append({
            'name': case['name'],
            'classified_as': btype,
            'expected': case['expected_type'],
            'correct': correct,
            'confidence': confidence
        })

    print("-" * 70)

    # Summary
    n_correct = sum(1 for r in results if r['correct'])
    print(f"\nSummary: {n_correct}/{len(results)} classifications correct")

    return results


# =============================================================================
# DEMO 4: PULLBACK VISUALIZATION
# =============================================================================

def demo_pullback_visualization():
    """
    Visualize the pullback from meta-derivative to standard calculus.

    Shows:
    1. How tau(t) = integral(u(s)ds) reparametrizes time
    2. When the pullback is well-defined (u > 0)
    3. When it breaks (u <= 0)
    """
    print("\n" + "=" * 70)
    print("DEMO 4: PULLBACK VISUALIZATION")
    print("=" * 70)

    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Case A: Admissible (u > 0 always)
    u_admissible = lambda t: 1 + 0.3 * np.sin(t)
    v_admissible = lambda t: 0.0

    morphism_a = create_meta_derivative_morphism(
        u_admissible, v_admissible, (0, 10)
    )

    t_vals = np.linspace(0.1, 10, 100)
    pullback_a = morphism_a.compute_pullback_to_standard(t_vals)

    axes[0, 0].plot(t_vals, [u_admissible(t) for t in t_vals], 'b-', linewidth=2)
    axes[0, 0].axhline(y=0, color='r', linestyle='--', label='u = 0 (boundary)')
    axes[0, 0].fill_between(t_vals, 0, [u_admissible(t) for t in t_vals],
                            alpha=0.3, color='green', label='u > 0 (admissible)')
    axes[0, 0].set_xlabel('t')
    axes[0, 0].set_ylabel('u(t)')
    axes[0, 0].set_title('ADMISSIBLE: u(t) = 1 + 0.3*sin(t)')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].plot(t_vals, pullback_a['tau_values'], 'b-', linewidth=2)
    axes[0, 1].set_xlabel('t')
    axes[0, 1].set_ylabel('tau(t)')
    axes[0, 1].set_title('tau(t) = integral u(s) ds (monotonic)')
    axes[0, 1].grid(True, alpha=0.3)

    # Case B: Inadmissible (u crosses zero)
    u_inadmissible = lambda t: np.sin(t - 3)  # Crosses zero at t=3
    v_inadmissible = lambda t: 0.0

    morphism_b = create_meta_derivative_morphism(
        u_inadmissible, v_inadmissible, (0, 10)
    )

    u_vals_bad = [u_inadmissible(t) for t in t_vals]
    tau_vals_bad = [morphism_b.compute_tau(t) for t in t_vals]

    axes[1, 0].plot(t_vals, u_vals_bad, 'r-', linewidth=2)
    axes[1, 0].axhline(y=0, color='k', linestyle='--', linewidth=2)
    axes[1, 0].fill_between(t_vals, 0, u_vals_bad,
                            where=[u > 0 for u in u_vals_bad],
                            alpha=0.3, color='green', label='u > 0')
    axes[1, 0].fill_between(t_vals, 0, u_vals_bad,
                            where=[u <= 0 for u in u_vals_bad],
                            alpha=0.3, color='red', label='u <= 0 (BREAKS)')
    axes[1, 0].set_xlabel('t')
    axes[1, 0].set_ylabel('u(t)')
    axes[1, 0].set_title('INADMISSIBLE: u(t) = sin(t-3)')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].plot(t_vals, tau_vals_bad, 'r-', linewidth=2)
    axes[1, 1].set_xlabel('t')
    axes[1, 1].set_ylabel('tau(t)')
    axes[1, 1].set_title('tau(t) NOT monotonic -> NOT invertible!')
    axes[1, 1].grid(True, alpha=0.3)

    # Mark the problem region
    zero_crossings = [t for i, t in enumerate(t_vals[:-1])
                      if u_vals_bad[i] * u_vals_bad[i+1] < 0]
    for zc in zero_crossings:
        axes[1, 0].axvline(x=zc, color='purple', linestyle=':', linewidth=2,
                           label=f'Zero at t~{zc:.1f}' if zc == zero_crossings[0] else '')
        axes[1, 1].axvline(x=zc, color='purple', linestyle=':', linewidth=2)

    plt.tight_layout()
    plt.suptitle('Pullback to Standard Calculus: Admissible vs Inadmissible',
                 y=1.02, fontsize=14, fontweight='bold')

    # Save figure
    output_path = os.path.join(
        os.path.dirname(__file__),
        'pathological_pullback_demo.png'
    )
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\nFigure saved to: {output_path}")

    plt.show()

    return {
        'admissible_report': morphism_a.check_c_scheme_admissibility(),
        'inadmissible_report': morphism_b.check_c_scheme_admissibility()
    }


# =============================================================================
# DEMO 5: ANOMALY-LIKE OBSTRUCTION
# =============================================================================

def demo_anomaly_obstruction():
    """
    Demonstrate how an anomaly-like obstruction manifests in our framework.

    Scenario: Try to transform between schemes where the path integral
    measure would pick up a nontrivial Jacobian.

    In practice: Create a transformation that LOOKS admissible but
    fails expectation preservation due to "hidden" nonlocality.
    """
    print("\n" + "=" * 70)
    print("DEMO 5: ANOMALY-LIKE OBSTRUCTION")
    print("=" * 70)

    from meta_calculus.scheme_morphism import (
        GammaMorphism, GSchemeObstruction, classify_anomaly_as_obstruction
    )

    # Example 1: Chiral anomaly (conceptual)
    print("\n--- Example 1: Chiral U(1) Anomaly ---")
    obstruction = classify_anomaly_as_obstruction(
        "Chiral U(1) rotation",
        classical_invariant=True,
        quantum_invariant=False
    )
    if obstruction:
        print(obstruction)

    # Example 2: Conformal anomaly (conceptual)
    print("\n--- Example 2: Conformal/Trace Anomaly ---")
    obstruction2 = classify_anomaly_as_obstruction(
        "Weyl rescaling",
        classical_invariant=True,
        quantum_invariant=False
    )
    if obstruction2:
        print(obstruction2)

    # Example 3: No anomaly (Gamma map CQT <-> RNQT)
    print("\n--- Example 3: Gamma Map (No Anomaly) ---")
    obstruction3 = classify_anomaly_as_obstruction(
        "Gamma: CQT <-> RNQT",
        classical_invariant=True,
        quantum_invariant=True  # Proven in Hoffreumon-Woods 2025
    )
    if obstruction3:
        print(obstruction3)
    else:
        print("No obstruction: Gamma is in G_scheme")

    # Verify Gamma is fully admissible
    print("\n--- Verifying Gamma Admissibility ---")
    gamma = GammaMorphism()

    # Create test observables (2x2 Hermitian)
    H1 = np.array([[1, 1j], [-1j, 2]])
    H2 = np.array([[0, 1], [1, 0]]) + 0j  # Pauli X
    H3 = np.array([[1, 0], [0, -1]]) + 0j  # Pauli Z

    # Create test states
    psi1 = np.array([1, 0]) + 0j
    psi2 = np.array([1, 1]) / np.sqrt(2) + 0j
    psi3 = np.array([1, 1j]) / np.sqrt(2)

    report = gamma.check_admissibility(
        test_observables=[H1, H2, H3],
        test_states=[psi1, psi2, psi3]
    )

    print(report.summary())

    return {
        'chiral_obstruction': obstruction,
        'conformal_obstruction': obstruction2,
        'gamma_no_obstruction': obstruction3 is None,
        'gamma_report': report
    }


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Run all demos."""
    print("=" * 70)
    print("PATHOLOGICAL SCHEME DEMO")
    print("Demonstrating Controlled Failures in Scheme Invariance Framework")
    print("=" * 70)

    results = {}

    # Demo 1
    results['inadmissible'] = demo_inadmissible_meta_derivatives()

    # Demo 2
    results['singular'] = demo_singular_breaking()

    # Demo 3
    results['classification'] = demo_physical_vs_artifact()

    # Demo 4 (visualization)
    try:
        results['pullback'] = demo_pullback_visualization()
    except Exception as e:
        print(f"\nNote: Visualization demo skipped (may require display): {e}")
        results['pullback'] = None

    # Demo 5
    results['anomaly'] = demo_anomaly_obstruction()

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("""
    This demo showed:

    1. INADMISSIBLE META-DERIVATIVES: When u(t) vanishes, the pullback
       to standard calculus breaks. These are NOT in G_scheme.

    2. SINGULAR BREAKING: Near t=0, different C-schemes give different H(t).
       This is EXPECTED because t is scheme-dependent. H(z) remains robust.

    3. BREAKING CLASSIFICATION: The framework distinguishes:
       - Numerical artifacts (tiny differences)
       - Singular behavior (expected near singularities)
       - Potential new physics (unexpected regular-regime breaking)

    4. PULLBACK VISUALIZATION: The coordinate transformation tau(t)
       shows exactly when and why admissibility fails.

    5. ANOMALY CONNECTION: Quantum anomalies are G_scheme obstructions
       where measure invariance fails despite classical invariance.

    KEY TAKEAWAY: The scheme-invariance framework is NON-TRIVIAL.
    Not every transformation is admissible, and breaking has physical meaning.
    """)

    return results


if __name__ == "__main__":
    results = main()
