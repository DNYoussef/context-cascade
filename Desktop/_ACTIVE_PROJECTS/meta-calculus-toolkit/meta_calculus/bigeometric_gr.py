#!/usr/bin/env python3
"""
Bigeometric General Relativity Module

This module implements bigeometric calculus applied to GR solutions.

STATUS:
  - PROVEN: Bigeometric derivatives of classical GR solutions
  - SPECULATIVE: Bigeometric field equations (see docs/BIGEOMETRIC_EINSTEIN_AUDIT.md)

Usage:
  python -m meta_calculus.bigeometric_gr --help
  python -m meta_calculus.bigeometric_gr frw --n 0.667 --t-range 1e-6 1
  python -m meta_calculus.bigeometric_gr schwarzschild --r-range 1e-3 10
  python -m meta_calculus.bigeometric_gr validate
"""

import numpy as np
import argparse
import sys
from typing import Callable, Tuple, List, Dict, Optional
import json


# =============================================================================
# CORE BIGEOMETRIC CALCULUS (VERIFIED CORRECT)
# =============================================================================

def bigeometric_derivative(f: Callable[[float], float], x: float, h: float = 1e-8) -> float:
    """
    Compute bigeometric derivative D_BG[f](x) = exp(x * f'(x) / f(x))

    This is the standard Grossman bigeometric derivative formula.
    VERIFIED CORRECT per Grossman & Katz (1972).

    Args:
        f: Function to differentiate (must be positive at x)
        x: Point of evaluation (must be positive)
        h: Step size for numerical derivative

    Returns:
        D_BG[f](x) or nan if undefined
    """
    if x <= 0:
        return float('nan')

    f_x = f(x)
    if f_x <= 0:
        return float('nan')

    # Central difference for f'(x)
    f_prime = (f(x + h) - f(x - h)) / (2 * h)

    # Bigeometric derivative
    elasticity = x * f_prime / f_x
    return np.exp(elasticity)


def bigeometric_derivative_array(f_vals: np.ndarray, x_vals: np.ndarray) -> np.ndarray:
    """
    Compute bigeometric derivative from arrays using ratio formula.

    D_BG ~ (f(x*h) / f(x))^(1/(h-1)) as h -> 1

    Args:
        f_vals: Array of function values (must be positive)
        x_vals: Array of x values (must be positive, logarithmically spaced)

    Returns:
        Array of D_BG values (length = len(x_vals) - 1)
    """
    D_BG = []
    for i in range(len(x_vals) - 1):
        x = x_vals[i]
        x_next = x_vals[i + 1]

        h_mult = x_next / x
        if abs(h_mult - 1.0) < 1e-10:
            continue

        if f_vals[i] <= 0 or f_vals[i + 1] <= 0:
            D_BG.append(float('nan'))
            continue

        f_ratio = f_vals[i + 1] / f_vals[i]
        D_BG_val = f_ratio ** (1.0 / (h_mult - 1.0))
        D_BG.append(D_BG_val)

    return np.array(D_BG)


# =============================================================================
# FRW COSMOLOGY (VERIFIED CORRECT)
# =============================================================================

class FRWCosmology:
    """
    Flat FRW cosmology with scale factor a(t) = t^n.

    All calculations here are VERIFIED CORRECT classical GR results.
    """

    def __init__(self, n: float):
        """
        Initialize FRW cosmology.

        Args:
            n: Power law exponent for scale factor
               n = 1/2: radiation-dominated
               n = 2/3: matter-dominated
        """
        self.n = n
        self.C = 6.0 * (2.0 * n**2 - n)  # Ricci scalar coefficient

    def scale_factor(self, t: float) -> float:
        """Scale factor a(t) = t^n"""
        if t <= 0:
            return float('nan')
        return t ** self.n

    def hubble_parameter(self, t: float) -> float:
        """Hubble parameter H = a'/a = n/t"""
        if t <= 0:
            return float('nan')
        return self.n / t

    def ricci_scalar(self, t: float) -> float:
        """
        Ricci scalar R(t) = 6(a''/a + (a'/a)^2) = C/t^2

        For a(t) = t^n:
          R(t) = 6(2n^2 - n) / t^2

        VERIFIED: Standard GR derivation
        """
        if t <= 0:
            return float('nan')
        return self.C / (t ** 2)

    def ricci_scalar_derivative(self, t: float) -> float:
        """Classical derivative dR/dt = -2C/t^3"""
        if t <= 0:
            return float('nan')
        return -2.0 * self.C / (t ** 3)

    def d_bg_ricci(self, t: float) -> float:
        """
        Bigeometric derivative of Ricci scalar.

        For R(t) = C/t^2 = C * t^(-2):
          D_BG[R] = exp(-2) ~ 0.1353

        This is the power law theorem: D_BG[t^n] = e^n
        Here n = -2, so D_BG[R] = e^(-2)

        VERIFIED CORRECT
        """
        return bigeometric_derivative(self.ricci_scalar, t)

    def d_bg_ricci_analytical(self) -> float:
        """
        Analytical result: D_BG[R] = e^(-2)

        Independent of n (the cosmology exponent) because R ~ t^(-2) always.
        """
        return np.exp(-2)

    def energy_density(self, t: float, G: float = 1.0) -> float:
        """
        Energy density from Friedmann equation:
        rho = 3H^2 / (8*pi*G) = 3n^2 / (8*pi*G*t^2)
        """
        if t <= 0:
            return float('nan')
        H = self.hubble_parameter(t)
        return 3.0 * H**2 / (8.0 * np.pi * G)

    def d_bg_energy_density(self, t: float, G: float = 1.0) -> float:
        """
        Bigeometric derivative of energy density.

        rho ~ t^(-2), so D_BG[rho] = e^(-2)
        """
        return bigeometric_derivative(lambda t: self.energy_density(t, G), t)

    def run_analysis(self, t_values: np.ndarray) -> Dict:
        """
        Run complete FRW analysis.

        Args:
            t_values: Array of time values to analyze

        Returns:
            Dictionary with all computed quantities
        """
        results = {
            'n': self.n,
            'C': self.C,
            't': t_values.tolist(),
            'a': [],
            'H': [],
            'R': [],
            'dR_dt': [],
            'D_BG_R_numerical': [],
            'D_BG_R_analytical': self.d_bg_ricci_analytical(),
        }

        for t in t_values:
            results['a'].append(self.scale_factor(t))
            results['H'].append(self.hubble_parameter(t))
            results['R'].append(self.ricci_scalar(t))
            results['dR_dt'].append(self.ricci_scalar_derivative(t))
            results['D_BG_R_numerical'].append(self.d_bg_ricci(t))

        # Compute error
        D_BG_numerical = np.array(results['D_BG_R_numerical'])
        D_BG_expected = results['D_BG_R_analytical']
        valid_mask = ~np.isnan(D_BG_numerical)

        if np.any(valid_mask):
            rel_error = np.abs(D_BG_numerical[valid_mask] - D_BG_expected) / D_BG_expected
            results['mean_relative_error'] = float(np.mean(rel_error))
            results['max_relative_error'] = float(np.max(rel_error))
        else:
            results['mean_relative_error'] = float('nan')
            results['max_relative_error'] = float('nan')

        return results


# =============================================================================
# SCHWARZSCHILD SPACETIME (VERIFIED CORRECT)
# =============================================================================

class SchwarzschildSpacetime:
    """
    Schwarzschild black hole spacetime.

    All calculations here are VERIFIED CORRECT classical GR results.
    """

    def __init__(self, M: float = 1.0):
        """
        Initialize Schwarzschild spacetime.

        Args:
            M: Black hole mass (in geometric units G=c=1)
        """
        self.M = M
        self.r_s = 2.0 * M  # Schwarzschild radius

    def kretschmann_scalar(self, r: float) -> float:
        """
        Kretschmann scalar K = R_abcd R^abcd = 48 M^2 / r^6

        VERIFIED: Standard GR result
        """
        if r <= 0:
            return float('nan')
        return 48.0 * self.M**2 / (r ** 6)

    def d_bg_kretschmann(self, r: float) -> float:
        """
        Bigeometric derivative of Kretschmann scalar.

        For K ~ r^(-6): D_BG[K] = e^(-6) ~ 0.00248

        VERIFIED: Power law theorem
        """
        return bigeometric_derivative(self.kretschmann_scalar, r)

    def d_bg_kretschmann_analytical(self) -> float:
        """Analytical result: D_BG[K] = e^(-6)"""
        return np.exp(-6)

    def tidal_force(self, r: float) -> float:
        """
        Radial tidal force ~ M/r^3
        """
        if r <= 0:
            return float('nan')
        return self.M / (r ** 3)

    def d_bg_tidal(self, r: float) -> float:
        """D_BG[tidal] = e^(-3) ~ 0.0498"""
        return bigeometric_derivative(self.tidal_force, r)

    def run_analysis(self, r_values: np.ndarray) -> Dict:
        """Run complete Schwarzschild analysis."""
        results = {
            'M': self.M,
            'r_s': self.r_s,
            'r': r_values.tolist(),
            'K': [],
            'D_BG_K_numerical': [],
            'D_BG_K_analytical': self.d_bg_kretschmann_analytical(),
            'tidal': [],
            'D_BG_tidal_numerical': [],
            'D_BG_tidal_analytical': np.exp(-3),
        }

        for r in r_values:
            results['K'].append(self.kretschmann_scalar(r))
            results['D_BG_K_numerical'].append(self.d_bg_kretschmann(r))
            results['tidal'].append(self.tidal_force(r))
            results['D_BG_tidal_numerical'].append(self.d_bg_tidal(r))

        return results


# =============================================================================
# HAWKING RADIATION (VERIFIED CORRECT)
# =============================================================================

class HawkingRadiation:
    """
    Hawking radiation properties.

    All calculations are VERIFIED CORRECT.
    """

    def temperature(self, M: float) -> float:
        """
        Hawking temperature T ~ 1/M (in natural units)

        Full formula: T = hbar * c^3 / (8 * pi * k_B * G * M)
        We use T = 1/M in geometric units.
        """
        if M <= 0:
            return float('nan')
        return 1.0 / M

    def d_bg_temperature(self, M: float) -> float:
        """D_BG[T] = e^(-1) ~ 0.368"""
        return bigeometric_derivative(self.temperature, M)

    def evaporation_time(self, M: float) -> float:
        """Evaporation timescale t_evap ~ M^3"""
        if M <= 0:
            return float('nan')
        return M ** 3

    def d_bg_evaporation_time(self, M: float) -> float:
        """D_BG[t_evap] = e^3 ~ 20.09"""
        return bigeometric_derivative(self.evaporation_time, M)


# =============================================================================
# VALIDATION SUITE
# =============================================================================

def run_validation_suite() -> Dict:
    """
    Run complete validation of bigeometric GR calculations.

    Returns:
        Dictionary with all test results
    """
    results = {
        'tests': [],
        'summary': {}
    }

    tolerance = 1e-4

    # Test 1: FRW Ricci scalar (matter-dominated)
    frw_matter = FRWCosmology(n=2/3)
    t_vals = np.logspace(-6, 0, 100)
    D_BG_R = [frw_matter.d_bg_ricci(t) for t in t_vals]
    D_BG_R_mean = np.nanmean(D_BG_R)
    expected = np.exp(-2)
    rel_error = abs(D_BG_R_mean - expected) / expected

    results['tests'].append({
        'name': 'FRW_matter_Ricci',
        'n': 2/3,
        'computed': D_BG_R_mean,
        'expected': expected,
        'rel_error': rel_error,
        'passed': rel_error < tolerance
    })

    # Test 2: FRW Ricci scalar (radiation-dominated)
    frw_rad = FRWCosmology(n=1/2)
    D_BG_R = [frw_rad.d_bg_ricci(t) for t in t_vals]
    D_BG_R_mean = np.nanmean(D_BG_R)
    rel_error = abs(D_BG_R_mean - expected) / expected

    results['tests'].append({
        'name': 'FRW_radiation_Ricci',
        'n': 1/2,
        'computed': D_BG_R_mean,
        'expected': expected,
        'rel_error': rel_error,
        'passed': rel_error < tolerance
    })

    # Test 3: Schwarzschild Kretschmann
    schwarz = SchwarzschildSpacetime(M=1.0)
    r_vals = np.logspace(-6, 0, 100)
    D_BG_K = [schwarz.d_bg_kretschmann(r) for r in r_vals]
    D_BG_K_mean = np.nanmean(D_BG_K)
    expected_K = np.exp(-6)
    rel_error_K = abs(D_BG_K_mean - expected_K) / expected_K

    results['tests'].append({
        'name': 'Schwarzschild_Kretschmann',
        'computed': D_BG_K_mean,
        'expected': expected_K,
        'rel_error': rel_error_K,
        'passed': rel_error_K < tolerance
    })

    # Test 4: Hawking temperature
    hawking = HawkingRadiation()
    M_vals = np.logspace(-3, 3, 100)
    D_BG_T = [hawking.d_bg_temperature(M) for M in M_vals]
    D_BG_T_mean = np.nanmean(D_BG_T)
    expected_T = np.exp(-1)
    rel_error_T = abs(D_BG_T_mean - expected_T) / expected_T

    results['tests'].append({
        'name': 'Hawking_temperature',
        'computed': D_BG_T_mean,
        'expected': expected_T,
        'rel_error': rel_error_T,
        'passed': rel_error_T < tolerance
    })

    # Summary
    passed = sum(1 for t in results['tests'] if t['passed'])
    total = len(results['tests'])
    results['summary'] = {
        'passed': passed,
        'total': total,
        'all_passed': passed == total
    }

    return results


# =============================================================================
# CLI INTERFACE
# =============================================================================

def print_banner():
    """Print CLI banner."""
    print("=" * 70)
    print("BIGEOMETRIC GENERAL RELATIVITY MODULE")
    print("Applying bigeometric calculus to GR solutions")
    print("=" * 70)


def cmd_frw(args):
    """FRW cosmology analysis."""
    print_banner()
    print(f"\nFRW Cosmology Analysis")
    print(f"  Scale factor: a(t) = t^{args.n}")
    print(f"  Time range: [{args.t_range[0]}, {args.t_range[1]}]")
    print("-" * 70)

    frw = FRWCosmology(n=args.n)
    t_vals = np.logspace(np.log10(args.t_range[0]), np.log10(args.t_range[1]), args.points)

    results = frw.run_analysis(t_vals)

    print(f"\nRicci scalar coefficient C = 6(2n^2 - n) = {results['C']:.4f}")
    print(f"\nSample results:")
    print(f"{'t':>12} {'R(t)':>15} {'dR/dt':>15} {'D_BG[R]':>12}")
    print("-" * 56)

    for i in range(0, len(t_vals), max(1, len(t_vals)//10)):
        print(f"{t_vals[i]:>12.2e} {results['R'][i]:>15.4e} {results['dR_dt'][i]:>15.4e} {results['D_BG_R_numerical'][i]:>12.6f}")

    print("-" * 56)
    print(f"\nAnalytical D_BG[R] = e^(-2) = {results['D_BG_R_analytical']:.6f}")
    print(f"Mean numerical D_BG[R]      = {np.nanmean(results['D_BG_R_numerical']):.6f}")
    print(f"Mean relative error         = {results['mean_relative_error']:.2e}")

    print("\n" + "=" * 70)
    print("KEY RESULT: Classical Ricci scalar R ~ 1/t^2 DIVERGES as t -> 0")
    print("            Bigeometric derivative D_BG[R] = e^(-2) is CONSTANT")
    print("=" * 70)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to: {args.output}")


def cmd_schwarzschild(args):
    """Schwarzschild analysis."""
    print_banner()
    print(f"\nSchwarzschild Spacetime Analysis")
    print(f"  Black hole mass: M = {args.M}")
    print(f"  Radius range: [{args.r_range[0]}, {args.r_range[1]}] r_s")
    print("-" * 70)

    schwarz = SchwarzschildSpacetime(M=args.M)
    r_vals = np.logspace(np.log10(args.r_range[0]), np.log10(args.r_range[1]), args.points)

    results = schwarz.run_analysis(r_vals)

    print(f"\nSchwarzschild radius r_s = {results['r_s']}")
    print(f"\nSample results:")
    print(f"{'r':>12} {'K(r)':>15} {'D_BG[K]':>12}")
    print("-" * 42)

    for i in range(0, len(r_vals), max(1, len(r_vals)//10)):
        print(f"{r_vals[i]:>12.2e} {results['K'][i]:>15.4e} {results['D_BG_K_numerical'][i]:>12.6f}")

    print("-" * 42)
    print(f"\nAnalytical D_BG[K] = e^(-6) = {results['D_BG_K_analytical']:.6f}")
    print(f"Mean numerical D_BG[K]      = {np.nanmean(results['D_BG_K_numerical']):.6f}")

    print("\n" + "=" * 70)
    print("KEY RESULT: Kretschmann scalar K ~ 1/r^6 DIVERGES as r -> 0")
    print("            Bigeometric derivative D_BG[K] = e^(-6) is CONSTANT")
    print("=" * 70)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to: {args.output}")


def cmd_validate(args):
    """Run validation suite."""
    print_banner()
    print("\nRunning Validation Suite")
    print("-" * 70)

    results = run_validation_suite()

    for test in results['tests']:
        status = "PASS" if test['passed'] else "FAIL"
        print(f"\n  Test: {test['name']}")
        print(f"    Computed: {test['computed']:.8f}")
        print(f"    Expected: {test['expected']:.8f}")
        print(f"    Rel Error: {test['rel_error']:.2e}")
        print(f"    Status: {status}")

    print("\n" + "-" * 70)
    print(f"Summary: {results['summary']['passed']}/{results['summary']['total']} tests passed")

    if results['summary']['all_passed']:
        print("\nALL TESTS PASSED - Bigeometric calculations verified")
    else:
        print("\nSOME TESTS FAILED - Review calculations")

    print("=" * 70)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to: {args.output}")

    return 0 if results['summary']['all_passed'] else 1


def cmd_power_law(args):
    """Test power law theorem."""
    print_banner()
    print(f"\nPower Law Theorem Test: D_BG[x^n] = e^n")
    print("-" * 70)

    x_vals = np.logspace(-3, 1, 100)

    print(f"{'n':>8} {'Expected e^n':>15} {'Computed':>15} {'Rel Error':>12}")
    print("-" * 52)

    for n in args.n_values:
        f = lambda x, n=n: x ** n
        D_BG_vals = [bigeometric_derivative(f, x) for x in x_vals]
        computed = np.nanmean(D_BG_vals)
        expected = np.exp(n)
        rel_error = abs(computed - expected) / expected if expected != 0 else float('inf')

        print(f"{n:>8.2f} {expected:>15.6f} {computed:>15.6f} {rel_error:>12.2e}")

    print("=" * 70)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Bigeometric General Relativity Module",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m meta_calculus.bigeometric_gr frw --n 0.667
  python -m meta_calculus.bigeometric_gr schwarzschild --M 1.0
  python -m meta_calculus.bigeometric_gr validate
  python -m meta_calculus.bigeometric_gr power-law -n -6 -3 -2 -1 0.5 1 2 3
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # FRW command
    frw_parser = subparsers.add_parser('frw', help='FRW cosmology analysis')
    frw_parser.add_argument('--n', type=float, default=2/3,
                           help='Scale factor exponent (default: 2/3 for matter)')
    frw_parser.add_argument('--t-range', nargs=2, type=float, default=[1e-6, 1.0],
                           help='Time range [t_min, t_max]')
    frw_parser.add_argument('--points', type=int, default=100,
                           help='Number of sample points')
    frw_parser.add_argument('--output', '-o', type=str,
                           help='Output JSON file')
    frw_parser.set_defaults(func=cmd_frw)

    # Schwarzschild command
    schwarz_parser = subparsers.add_parser('schwarzschild', help='Schwarzschild analysis')
    schwarz_parser.add_argument('--M', type=float, default=1.0,
                               help='Black hole mass')
    schwarz_parser.add_argument('--r-range', nargs=2, type=float, default=[1e-3, 10.0],
                               help='Radius range [r_min, r_max]')
    schwarz_parser.add_argument('--points', type=int, default=100,
                               help='Number of sample points')
    schwarz_parser.add_argument('--output', '-o', type=str,
                               help='Output JSON file')
    schwarz_parser.set_defaults(func=cmd_schwarzschild)

    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Run validation suite')
    validate_parser.add_argument('--output', '-o', type=str,
                                help='Output JSON file')
    validate_parser.set_defaults(func=cmd_validate)

    # Power law command
    powerlaw_parser = subparsers.add_parser('power-law', help='Test power law theorem')
    powerlaw_parser.add_argument('-n', '--n-values', nargs='+', type=float,
                                default=[-6, -3, -2, -1, -0.5, 0.5, 1, 2, 3],
                                help='Power law exponents to test')
    powerlaw_parser.set_defaults(func=cmd_power_law)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
