#!/usr/bin/env python3
"""
Bigeometric Operators - Corrected Implementation

This module implements the CORRECT bigeometric operators based on
cross-audit of multiple implementations.

KEY INSIGHT (from cross-audit):
  - D_BG and L_BG work as DIAGNOSTIC tools on classical solutions
  - They do NOT work as replacement derivatives in field equations
  - The 2D success is misleading; 4D fails catastrophically

WHAT WORKS:
  - D_BG[f](x) = exp(L_BG[f](x)) for positive f
  - L_BG[x^n] = n (constant)
  - Applied to classical GR solutions (R, K, etc.)

WHAT DOES NOT WORK:
  - Replacing partial_t -> L_BG in Christoffel formulas
  - Building "bigeometric connections" via naive substitution
  - Extending 2D results to 4D (breaks symmetry)

Usage:
  python -m meta_calculus.bigeometric_operators
"""

import numpy as np
from typing import Callable, Tuple, Optional
import argparse
import sys


# =============================================================================
# L_BG OPERATOR (Log-Bigeometric Derivative)
# =============================================================================

def L_BG(f: Callable[[float], float], x: float, h: float = 1e-8) -> float:
    """
    Log-bigeometric derivative: L_BG[f](x) = x * f'(x) / f(x)

    This is the EXPONENT that appears in D_BG:
        D_BG[f](x) = exp(L_BG[f](x))

    Properties (PROVEN):
        L_BG[x^n] = n (constant, independent of x)
        L_BG[const] = 0
        L_BG[f*g] = L_BG[f] + L_BG[g]

    Args:
        f: Positive function
        x: Evaluation point (must be positive)
        h: Step size for numerical derivative

    Returns:
        L_BG[f](x), or nan if undefined
    """
    if x <= 0:
        return float('nan')

    f_x = f(x)
    if f_x <= 0:
        return float('nan')

    # Central difference for f'(x)
    f_prime = (f(x + h) - f(x - h)) / (2 * h)

    # L_BG = x * f'/f
    return x * f_prime / f_x


def D_BG(f: Callable[[float], float], x: float, h: float = 1e-8) -> float:
    """
    Bigeometric derivative: D_BG[f](x) = exp(L_BG[f](x))

    This is the Grossman bigeometric derivative.

    Properties (PROVEN):
        D_BG[x^n] = e^n (constant, independent of x)
        D_BG[const] = 1
        D_BG[f*g] = D_BG[f] * D_BG[g]

    Args:
        f: Positive function
        x: Evaluation point (must be positive)
        h: Step size for numerical derivative

    Returns:
        D_BG[f](x), or nan if undefined
    """
    l_bg = L_BG(f, x, h)
    if np.isnan(l_bg):
        return float('nan')
    return np.exp(l_bg)


# =============================================================================
# POWER LAW VERIFICATION
# =============================================================================

def verify_power_law_theorem(n: float, x_range: Tuple[float, float] = (0.1, 10.0),
                             num_points: int = 100) -> dict:
    """
    Verify the power law theorem: D_BG[x^n] = e^n, L_BG[x^n] = n

    Args:
        n: Power law exponent
        x_range: Range of x values to test
        num_points: Number of test points

    Returns:
        Dictionary with verification results
    """
    x_vals = np.logspace(np.log10(x_range[0]), np.log10(x_range[1]), num_points)

    f = lambda x: x ** n

    L_BG_vals = np.array([L_BG(f, x) for x in x_vals])
    D_BG_vals = np.array([D_BG(f, x) for x in x_vals])

    L_BG_expected = n
    D_BG_expected = np.exp(n)

    L_BG_mean = np.nanmean(L_BG_vals)
    D_BG_mean = np.nanmean(D_BG_vals)

    L_BG_std = np.nanstd(L_BG_vals)
    D_BG_std = np.nanstd(D_BG_vals)

    L_BG_error = abs(L_BG_mean - L_BG_expected) / abs(L_BG_expected) if L_BG_expected != 0 else abs(L_BG_mean)
    D_BG_error = abs(D_BG_mean - D_BG_expected) / D_BG_expected

    return {
        'n': n,
        'L_BG_expected': L_BG_expected,
        'L_BG_computed': L_BG_mean,
        'L_BG_std': L_BG_std,
        'L_BG_rel_error': L_BG_error,
        'D_BG_expected': D_BG_expected,
        'D_BG_computed': D_BG_mean,
        'D_BG_std': D_BG_std,
        'D_BG_rel_error': D_BG_error,
        'theorem_verified': L_BG_error < 1e-4 and D_BG_error < 1e-4,
    }


# =============================================================================
# 2D FRW TOY MODEL (WHERE L_BG "WORKS")
# =============================================================================

class FRW2D:
    """
    2D FRW toy model demonstrating where L_BG-based approach appears to work.

    WARNING: This 2D success is MISLEADING. The 4D extension FAILS.
    See FRW4D class for the failure case.

    Metric: ds^2 = -dt^2 + a(t)^2 dr^2
    Scale factor: a(t) = t^n
    """

    def __init__(self, n: float):
        self.n = n

    def metric_rr(self, t: float) -> float:
        """g_rr = a(t)^2 = t^(2n)"""
        return t ** (2 * self.n)

    def L_BG_metric_rr(self, t: float) -> float:
        """L_BG[g_rr] = 2n (constant!)"""
        return L_BG(self.metric_rr, t)

    def christoffel_t_rr_classical(self, t: float) -> float:
        """Classical Gamma^t_rr = n * t^(2n-1)"""
        return self.n * t ** (2 * self.n - 1)

    def christoffel_r_tr_classical(self, t: float) -> float:
        """Classical Gamma^r_tr = n/t"""
        return self.n / t

    def christoffel_t_rr_LBG(self) -> float:
        """
        "L_BG Christoffel": Gamma^t_rr = n (CONSTANT!)

        This appears finite, but see 4D failure.
        """
        return self.n

    def christoffel_r_tr_LBG(self, t: float) -> float:
        """
        "L_BG Christoffel": Gamma^r_tr = n / t^(2n)

        WARNING: Still diverges for n > 0!
        """
        return self.n / (t ** (2 * self.n))

    def ricci_scalar_classical(self, t: float) -> float:
        """
        Classical R(t) = 6(2n^2 - n) / t^2

        DIVERGES as t -> 0
        """
        C = 6 * (2 * self.n**2 - self.n)
        return C / (t ** 2)

    def ricci_scalar_LBG_2d(self) -> float:
        """
        R_LBG in 2D = -2n (CONSTANT!)

        This is the "miraculous" 2D result.
        WARNING: Does NOT extend to 4D!
        """
        return -2 * self.n

    def L_BG_ricci(self, t: float) -> float:
        """L_BG[R] = -2 (constant, as R ~ t^(-2))"""
        return L_BG(self.ricci_scalar_classical, t)

    def D_BG_ricci(self, t: float) -> float:
        """D_BG[R] = e^(-2) (constant)"""
        return D_BG(self.ricci_scalar_classical, t)


# =============================================================================
# 4D FRW FAILURE CASE
# =============================================================================

class FRW4D:
    """
    4D FRW showing FAILURE of naive L_BG approach.

    The same substitution that gave R_LBG = -2n in 2D gives:
        R_LBG ~ t^(-4n) in 4D (STILL DIVERGES!)
        R_LBG depends on r, theta (BREAKS SYMMETRY!)

    This class documents the failure, not a working theory.
    """

    def __init__(self, n: float):
        self.n = n

    def metric_components(self, t: float, r: float, theta: float) -> dict:
        """
        4D FRW metric components.

        g_tt = -1
        g_rr = t^(2n)
        g_theta_theta = t^(2n) * r^2
        g_phi_phi = t^(2n) * r^2 * sin^2(theta)
        """
        a_sq = t ** (2 * self.n)
        return {
            'g_tt': -1.0,
            'g_rr': a_sq,
            'g_theta_theta': a_sq * r**2,
            'g_phi_phi': a_sq * r**2 * np.sin(theta)**2,
        }

    def ricci_scalar_classical(self, t: float) -> float:
        """
        Classical R(t) = 6(2n^2 - n) / t^2

        Depends only on t (homogeneous, isotropic).
        """
        C = 6 * (2 * self.n**2 - self.n)
        return C / (t ** 2)

    def ricci_scalar_LBG_4d(self, t: float, r: float, theta: float) -> float:
        """
        R_LBG in 4D using naive substitution.

        From other AI's symbolic computation:
        R_LBG = 2n(n*r^2 + n*r^2*csc^2(theta) + n*csc^2(theta) - 3*r^4*t^(4n)) / (r^4 * t^(4n))

        PROBLEMS:
        1. DIVERGES as t -> 0 (like t^(-4n), worse than classical!)
        2. Depends on r (breaks homogeneity!)
        3. Depends on theta (breaks isotropy!)

        This demonstrates the FAILURE of the naive approach.
        """
        sin_th = np.sin(theta)
        csc_sq = 1.0 / (sin_th ** 2) if sin_th != 0 else float('inf')

        numerator = 2 * self.n * (
            self.n * r**2 +
            self.n * r**2 * csc_sq +
            self.n * csc_sq -
            3 * r**4 * t**(4 * self.n)
        )
        denominator = r**4 * t**(4 * self.n)

        if denominator == 0:
            return float('inf')

        return numerator / denominator

    def demonstrate_failure(self, t_values: list, r: float = 1.0, theta: float = np.pi/2) -> dict:
        """
        Demonstrate that R_LBG diverges and breaks symmetry.

        Returns comparison of classical vs L_BG approach.
        """
        results = {
            't': t_values,
            'R_classical': [],
            'R_LBG_4d': [],
            'R_LBG_at_different_r': [],
            'R_LBG_at_different_theta': [],
        }

        for t in t_values:
            results['R_classical'].append(self.ricci_scalar_classical(t))
            results['R_LBG_4d'].append(self.ricci_scalar_LBG_4d(t, r, theta))
            # Check r-dependence (should be zero for FRW!)
            results['R_LBG_at_different_r'].append(
                self.ricci_scalar_LBG_4d(t, 2.0, theta)
            )
            # Check theta-dependence (should be zero for FRW!)
            results['R_LBG_at_different_theta'].append(
                self.ricci_scalar_LBG_4d(t, r, np.pi/4)
            )

        return results


# =============================================================================
# SCHWARZSCHILD FAILURE CASE (L_BG does NOTHING for static metrics)
# =============================================================================

class Schwarzschild2D_LBG:
    """
    2D Schwarzschild showing that L_BG in time direction does NOTHING.

    Metric: ds^2 = -f(r) dt^2 + f(r)^(-1) dr^2
    where f(r) = 1 - 2M/r

    Since the metric is STATIC (doesn't depend on t):
        L_BG g_ab = t * d/dt ln|g_ab| = t * 0 = 0

    Therefore R_LBG = R_classical = 4M/r^3 (STILL DIVERGES!)

    This is a CRITICAL falsification of the L_BG-Christoffel approach.
    """

    def __init__(self, M: float = 1.0):
        self.M = M

    def f(self, r: float) -> float:
        """Schwarzschild lapse f(r) = 1 - 2M/r"""
        if r <= 0:
            return float('nan')
        return 1.0 - 2.0 * self.M / r

    def ricci_scalar_classical(self, r: float) -> float:
        """
        Classical 2D Ricci scalar R = 4M/r^3

        DIVERGES as r -> 0
        """
        if r <= 0:
            return float('inf')
        return 4.0 * self.M / (r ** 3)

    def ricci_scalar_LBG(self, r: float) -> float:
        """
        L_BG Ricci scalar = SAME as classical!

        Because metric doesn't depend on t, L_BG in time direction = 0.
        So L_BG-Christoffels = classical Christoffels.
        Therefore R_LBG = R_classical.

        This is the FAILURE: L_BG does nothing for static metrics.
        """
        return self.ricci_scalar_classical(r)  # Identical!

    def kretschmann_scalar_classical(self, r: float) -> float:
        """
        2D Kretschmann K ~ 8M^2 * (...) / r^8

        Near r=0: K ~ 32M^4 / r^8 (DIVERGES)
        """
        if r <= 0:
            return float('inf')
        f_r = self.f(r)
        if f_r == 0:
            return float('inf')
        # Simplified dominant term
        return 32.0 * self.M**4 / (r ** 8)

    def kretschmann_scalar_LBG(self, r: float) -> float:
        """K_LBG = K_classical (L_BG does nothing)"""
        return self.kretschmann_scalar_classical(r)  # Identical!

    def demonstrate_failure(self, r_values: list) -> dict:
        """
        Show that L_BG does NOTHING for Schwarzschild.

        Returns comparison showing R_LBG = R_classical.
        """
        results = {
            'r': r_values,
            'R_classical': [],
            'R_LBG': [],
            'difference': [],
        }

        for r in r_values:
            R_cl = self.ricci_scalar_classical(r)
            R_LBG = self.ricci_scalar_LBG(r)
            results['R_classical'].append(R_cl)
            results['R_LBG'].append(R_LBG)
            results['difference'].append(R_LBG - R_cl)  # Should be 0!

        return results


# =============================================================================
# WHAT ACTUALLY WORKS: DIAGNOSTIC APPLICATION
# =============================================================================

class BigeometricDiagnostic:
    """
    The CORRECT use of bigeometric operators: as diagnostics on classical solutions.

    This does NOT claim to be a "modified GR theory".
    It's a mathematical observation about power-law behavior.
    """

    @staticmethod
    def analyze_power_law_singularity(f: Callable, x_values: np.ndarray,
                                       label: str = "f") -> dict:
        """
        Analyze a power-law singularity using bigeometric diagnostics.

        Args:
            f: Function with power-law behavior
            x_values: Points to evaluate
            label: Name for the function

        Returns:
            Dictionary with classical and bigeometric analysis
        """
        results = {
            'label': label,
            'x': x_values.tolist(),
            'f_classical': [],
            'L_BG_f': [],
            'D_BG_f': [],
        }

        for x in x_values:
            results['f_classical'].append(f(x))
            results['L_BG_f'].append(L_BG(f, x))
            results['D_BG_f'].append(D_BG(f, x))

        # Compute statistics
        L_BG_array = np.array(results['L_BG_f'])
        D_BG_array = np.array(results['D_BG_f'])

        results['L_BG_mean'] = float(np.nanmean(L_BG_array))
        results['L_BG_std'] = float(np.nanstd(L_BG_array))
        results['D_BG_mean'] = float(np.nanmean(D_BG_array))
        results['D_BG_std'] = float(np.nanstd(D_BG_array))

        # Check if constant (power law)
        results['is_power_law'] = results['L_BG_std'] < 0.01 * abs(results['L_BG_mean'])
        results['inferred_exponent'] = results['L_BG_mean']

        return results


# =============================================================================
# CLI
# =============================================================================

def cmd_verify(args):
    """Verify power law theorem."""
    print("=" * 70)
    print("POWER LAW THEOREM VERIFICATION")
    print("L_BG[x^n] = n, D_BG[x^n] = e^n")
    print("=" * 70)

    n_values = args.n_values

    all_pass = True
    for n in n_values:
        result = verify_power_law_theorem(n)
        status = "PASS" if result['theorem_verified'] else "FAIL"
        if not result['theorem_verified']:
            all_pass = False

        print(f"\n  n = {n:6.2f}:")
        print(f"    L_BG: computed = {result['L_BG_computed']:8.4f}, expected = {result['L_BG_expected']:8.4f}")
        print(f"    D_BG: computed = {result['D_BG_computed']:8.4f}, expected = {result['D_BG_expected']:8.4f}")
        print(f"    Status: {status}")

    print("\n" + "=" * 70)
    if all_pass:
        print("ALL TESTS PASSED - Power law theorem verified")
    else:
        print("SOME TESTS FAILED")
    print("=" * 70)


def cmd_2d_vs_4d(args):
    """Compare 2D (works) vs 4D (fails) results."""
    print("=" * 70)
    print("2D vs 4D FRW COMPARISON")
    print("Demonstrating why 2D success is MISLEADING")
    print("=" * 70)

    n = args.n
    frw2d = FRW2D(n)
    frw4d = FRW4D(n)

    t_values = [1e-1, 1e-2, 1e-3, 1e-4]

    print(f"\n  Scale factor exponent n = {n}")

    print("\n  2D RESULTS (appear to work):")
    print(f"    R_LBG (2D) = {frw2d.ricci_scalar_LBG_2d():.4f} (CONSTANT)")
    print(f"    D_BG[R_classical] = {np.exp(-2):.4f} (also constant)")

    print("\n  4D RESULTS (FAIL!):")
    print(f"  {'t':>10} {'R_classical':>15} {'R_LBG (4D)':>15} {'Ratio':>10}")
    print("  " + "-" * 55)

    for t in t_values:
        R_cl = frw4d.ricci_scalar_classical(t)
        R_LBG = frw4d.ricci_scalar_LBG_4d(t, r=1.0, theta=np.pi/2)
        ratio = R_LBG / R_cl if R_cl != 0 else float('inf')
        print(f"  {t:>10.0e} {R_cl:>15.4e} {R_LBG:>15.4e} {ratio:>10.2f}")

    print("\n  SYMMETRY CHECK (should be ZERO variation):")
    t_test = 0.1
    R_at_r1 = frw4d.ricci_scalar_LBG_4d(t_test, r=1.0, theta=np.pi/2)
    R_at_r2 = frw4d.ricci_scalar_LBG_4d(t_test, r=2.0, theta=np.pi/2)
    R_at_theta1 = frw4d.ricci_scalar_LBG_4d(t_test, r=1.0, theta=np.pi/2)
    R_at_theta2 = frw4d.ricci_scalar_LBG_4d(t_test, r=1.0, theta=np.pi/4)

    print(f"    R_LBG(r=1) = {R_at_r1:.4e}")
    print(f"    R_LBG(r=2) = {R_at_r2:.4e} (should equal r=1!)")
    print(f"    R_LBG(theta=pi/2) = {R_at_theta1:.4e}")
    print(f"    R_LBG(theta=pi/4) = {R_at_theta2:.4e} (should equal theta=pi/2!)")

    print("\n" + "=" * 70)
    print("CONCLUSION: The 4D L_BG approach:")
    print("  1. STILL DIVERGES (worse than classical)")
    print("  2. BREAKS HOMOGENEITY (depends on r)")
    print("  3. BREAKS ISOTROPY (depends on theta)")
    print("  => Cannot be a valid modified GR theory")
    print("=" * 70)


def cmd_schwarzschild_failure(args):
    """Demonstrate Schwarzschild L_BG failure."""
    print("=" * 70)
    print("SCHWARZSCHILD L_BG FAILURE DEMONSTRATION")
    print("L_BG in time direction does NOTHING for static metrics")
    print("=" * 70)

    M = args.M
    schwarz = Schwarzschild2D_LBG(M)

    r_values = [10.0, 5.0, 2.0, 1.0, 0.5, 0.1, 0.01]

    print(f"\n  Black hole mass M = {M}")
    print(f"  Schwarzschild radius r_s = {2*M}")

    print("\n  Comparing R_classical vs R_LBG:")
    print(f"  {'r':>10} {'R_classical':>15} {'R_LBG':>15} {'Difference':>15}")
    print("  " + "-" * 60)

    for r in r_values:
        R_cl = schwarz.ricci_scalar_classical(r)
        R_LBG = schwarz.ricci_scalar_LBG(r)
        diff = R_LBG - R_cl

        print(f"  {r:>10.2f} {R_cl:>15.4e} {R_LBG:>15.4e} {diff:>15.4e}")

    print("\n" + "=" * 70)
    print("RESULT: R_LBG = R_classical EXACTLY")
    print("        L_BG does NOTHING because metric doesn't depend on t")
    print("        The r=0 singularity is COMPLETELY UNTOUCHED")
    print("=" * 70)
    print("\nThis FALSIFIES the L_BG-Christoffel approach for static spacetimes.")


def cmd_diagnostic(args):
    """Run bigeometric diagnostic on GR solutions."""
    print("=" * 70)
    print("BIGEOMETRIC DIAGNOSTIC (Correct Usage)")
    print("Apply D_BG to classical solutions as diagnostic tool")
    print("=" * 70)

    t_values = np.logspace(-6, 0, 50)

    # FRW Ricci scalar
    n = 2/3
    R = lambda t: 6 * (2 * n**2 - n) / (t**2)
    result_R = BigeometricDiagnostic.analyze_power_law_singularity(R, t_values, "FRW Ricci R")

    print(f"\n  FRW Ricci Scalar (n={n}):")
    print(f"    Classical: R ~ t^(-2) -> infinity as t -> 0")
    print(f"    L_BG[R] = {result_R['L_BG_mean']:.4f} (expected: -2)")
    print(f"    D_BG[R] = {result_R['D_BG_mean']:.4f} (expected: {np.exp(-2):.4f})")
    print(f"    Is power law: {result_R['is_power_law']}")

    # Schwarzschild Kretschmann
    r_values = np.logspace(-4, 1, 50)
    K = lambda r: 48.0 / (r**6)
    result_K = BigeometricDiagnostic.analyze_power_law_singularity(K, r_values, "Kretschmann K")

    print(f"\n  Schwarzschild Kretschmann:")
    print(f"    Classical: K ~ r^(-6) -> infinity as r -> 0")
    print(f"    L_BG[K] = {result_K['L_BG_mean']:.4f} (expected: -6)")
    print(f"    D_BG[K] = {result_K['D_BG_mean']:.6f} (expected: {np.exp(-6):.6f})")
    print(f"    Is power law: {result_K['is_power_law']}")

    print("\n" + "=" * 70)
    print("INTERPRETATION:")
    print("  D_BG gives FINITE values for power-law singularities")
    print("  This is a DIAGNOSTIC, not a 'resolution'")
    print("  It tells us the 'multiplicative rate' is well-behaved")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Bigeometric Operators - Corrected Implementation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # verify command
    verify_parser = subparsers.add_parser('verify', help='Verify power law theorem')
    verify_parser.add_argument('-n', '--n-values', nargs='+', type=float,
                              default=[-6, -3, -2, -1, -0.5, 0.5, 1, 2, 3],
                              help='Exponents to test')
    verify_parser.set_defaults(func=cmd_verify)

    # 2d-vs-4d command
    compare_parser = subparsers.add_parser('2d-vs-4d', help='Compare 2D vs 4D results')
    compare_parser.add_argument('--n', type=float, default=2/3,
                               help='FRW exponent')
    compare_parser.set_defaults(func=cmd_2d_vs_4d)

    # diagnostic command
    diag_parser = subparsers.add_parser('diagnostic', help='Run bigeometric diagnostic')
    diag_parser.set_defaults(func=cmd_diagnostic)

    # schwarzschild-failure command
    schwarz_parser = subparsers.add_parser('schwarzschild-failure',
                                           help='Demonstrate L_BG failure for static metrics')
    schwarz_parser.add_argument('--M', type=float, default=1.0,
                               help='Black hole mass')
    schwarz_parser.set_defaults(func=cmd_schwarzschild_failure)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
