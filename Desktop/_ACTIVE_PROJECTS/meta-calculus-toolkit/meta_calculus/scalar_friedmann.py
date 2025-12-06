#!/usr/bin/env python3
"""
Scalar-Level Meta-Friedmann Equations

This module implements the CORRECT scalar-level application of meta-calculus
to FRW cosmology, as documented in SCALAR_FRIEDMANN_META_CALCULUS.md.

TWO TOY MODELS:

1. Naive Bigeometric (D_BG) Replacement:
   - Demonstrates FAILURE: overconstrains to n = 0
   - Kept for pedagogical purposes

2. Meta-Friedmann with Weight W(t) = t^k:
   - WORKS consistently
   - n = (2/3) * (1 - k) / (1 + w)
   - m = 2 - 2k (density exponent)
   - k = 0 recovers classical FRW
   - k >= 1 softens/removes singularity

Usage:
    python -m meta_calculus.scalar_friedmann naive --w 0.333 --n 0.5
    python -m meta_calculus.scalar_friedmann meta --k 0.5 --w 0.333
    python -m meta_calculus.scalar_friedmann compare --w 0.333
    python -m meta_calculus.scalar_friedmann singularity --k 0.5 1.0 1.5
"""

import numpy as np
from typing import Callable, Optional, List, Tuple
import argparse
import sys


# =============================================================================
# CONSTANTS
# =============================================================================

# Gravitational constant (geometric units, or set to 1)
G = 1.0

# Common equation of state values
W_RADIATION = 1.0 / 3.0
W_DUST = 0.0
W_DARK_ENERGY = -1.0


# =============================================================================
# CLASSICAL FRW (REFERENCE)
# =============================================================================

class ClassicalFRW:
    """
    Classical flat FRW cosmology for comparison.

    Equations:
        (a_dot / a)^2 = (8 pi G / 3) rho
        a_ddot / a = -(4 pi G / 3)(rho + 3p)

    Power-law solution a(t) = t^n:
        n = 2 / (3(1 + w))
        rho ~ t^(-2)
    """

    def __init__(self, w: float):
        """
        Initialize with equation of state p = w * rho.

        Args:
            w: Equation of state parameter (0 = dust, 1/3 = radiation)
        """
        self.w = w
        self.n = self.expansion_exponent()
        self.m = 2.0  # Density always scales as t^(-2) classically

    def expansion_exponent(self) -> float:
        """Classical expansion exponent n = 2 / (3(1 + w))."""
        if self.w == -1:
            return float('inf')  # de Sitter
        return 2.0 / (3.0 * (1.0 + self.w))

    def scale_factor(self, t: float) -> float:
        """a(t) = t^n (normalized)."""
        if t <= 0:
            return 0.0
        return t ** self.n

    def hubble(self, t: float) -> float:
        """H = a_dot / a = n / t."""
        if t <= 0:
            return float('inf')
        return self.n / t

    def density(self, t: float, rho_0: float = 1.0) -> float:
        """rho(t) = rho_0 * t^(-2)."""
        if t <= 0:
            return float('inf')
        return rho_0 * t ** (-self.m)

    def acceleration(self, t: float) -> float:
        """a_ddot / a = n(n-1) / t^2."""
        if t <= 0:
            return float('inf')
        return self.n * (self.n - 1) / (t ** 2)

    def summary(self) -> dict:
        """Return summary of classical model."""
        return {
            'model': 'Classical FRW',
            'w': self.w,
            'n': self.n,
            'm': self.m,
            'density_at_t0': 'infinity (singularity)',
            'expansion': f'a(t) ~ t^{self.n:.4f}',
            'density': f'rho(t) ~ t^(-{self.m:.1f})',
        }


# =============================================================================
# TOY MODEL A: NAIVE BIGEOMETRIC (FAILS)
# =============================================================================

class NaiveBigeometricFRW:
    """
    Naive bigeometric replacement in Friedmann equations.

    This demonstrates WHY naive D_BG substitution FAILS.

    BG-Friedmann: m = 2n
    BG-Acceleration: n = 0 (overconstrained!)

    The only consistent power-law solution is static (n = 0).
    """

    def __init__(self, w: float, n_attempt: float = 0.5):
        """
        Initialize with attempted expansion exponent.

        Args:
            w: Equation of state parameter
            n_attempt: Attempted expansion exponent (will show inconsistency)
        """
        self.w = w
        self.n_attempt = n_attempt
        self.n_forced = 0.0  # What acceleration equation forces

    def D_BG_scale_factor(self) -> float:
        """D_BG[a] = e^n for a = t^n."""
        return np.exp(self.n_attempt)

    def D_BG_squared_scale_factor(self) -> float:
        """D_BG^2[a] = D_BG[e^n] = 1."""
        return 1.0

    def density_exponent_from_friedmann(self) -> float:
        """From BG-Friedmann: m = 2n."""
        return 2.0 * self.n_attempt

    def n_from_acceleration(self) -> float:
        """
        From BG-Acceleration equation:
        Matching powers gives n = 0.

        This is the FAILURE: acceleration equation forces n = 0.
        """
        return 0.0  # Always!

    def is_consistent(self) -> bool:
        """Check if Friedmann and Acceleration are consistent."""
        return abs(self.n_attempt) < 1e-10  # Only n = 0 works

    def D_BG_density(self) -> float:
        """D_BG[rho] = e^(-m) for rho ~ t^(-m)."""
        m = self.density_exponent_from_friedmann()
        return np.exp(-m)

    def demonstrate_failure(self) -> dict:
        """Show the inconsistency between equations."""
        m = self.density_exponent_from_friedmann()
        n_accel = self.n_from_acceleration()

        return {
            'model': 'Naive Bigeometric FRW',
            'w': self.w,
            'n_attempted': self.n_attempt,
            'n_from_friedmann': f'any (m = 2n = {m:.2f})',
            'n_from_acceleration': n_accel,
            'consistent': self.is_consistent(),
            'conclusion': 'FAILS: Acceleration forces n = 0 (static universe)',
            'D_BG_a': self.D_BG_scale_factor(),
            'D_BG_rho': self.D_BG_density(),
            'insight': 'rho diverges but D_BG[rho] is finite',
        }


# =============================================================================
# TOY MODEL B: META-FRIEDMANN WITH WEIGHT W(t) = t^k (WORKS)
# =============================================================================

class MetaFriedmann:
    """
    Meta-calculus Friedmann equations with weight W(t) = t^k.

    This is the CORRECT scalar-level application.

    Meta-derivative: D_meta[f] = t^k * f'(t)

    Results:
        n = (2/3) * (1 - k) / (1 + w)
        m = 2 - 2k (density exponent)

    Key features:
        - k = 0: recover classical FRW
        - k = 1: density is constant (no singularity!)
        - k > 1: density vanishes at t = 0
    """

    def __init__(self, k: float, w: float):
        """
        Initialize meta-Friedmann model.

        Args:
            k: Meta-weight exponent (W(t) = t^k)
            w: Equation of state parameter
        """
        self.k = k
        self.w = w
        self.n = self.expansion_exponent()
        self.m = self.density_exponent()

    def expansion_exponent(self) -> float:
        """n = (2/3) * (1 - k) / (1 + w)."""
        if self.w == -1:
            return float('inf')
        return (2.0 / 3.0) * (1.0 - self.k) / (1.0 + self.w)

    def density_exponent(self) -> float:
        """m = 2 - 2k."""
        return 2.0 - 2.0 * self.k

    def classical_n(self) -> float:
        """Classical exponent for comparison."""
        if self.w == -1:
            return float('inf')
        return 2.0 / (3.0 * (1.0 + self.w))

    def scale_factor(self, t: float) -> float:
        """a(t) = t^n."""
        if t <= 0:
            if self.n > 0:
                return 0.0
            elif self.n < 0:
                return float('inf')
            else:
                return 1.0
        return t ** self.n

    def density(self, t: float, rho_0: float = 1.0) -> float:
        """rho(t) = rho_0 * t^(-m) where m = 2 - 2k."""
        if t <= 0:
            if self.m > 0:
                return float('inf')
            elif self.m < 0:
                return 0.0
            else:
                return rho_0
        return rho_0 * t ** (-self.m)

    def meta_hubble(self, t: float) -> float:
        """D_meta[a] / a = n * t^(k-1)."""
        if t <= 0:
            if self.k > 1:
                return 0.0
            elif self.k < 1:
                return float('inf')
            else:
                return self.n
        return self.n * t ** (self.k - 1)

    def meta_acceleration(self, t: float) -> float:
        """D_meta^2[a] / a = n(n + k - 1) * t^(2k-2)."""
        if t <= 0:
            if self.k > 1:
                return 0.0
            elif self.k < 1:
                return float('inf')
            else:
                return self.n * (self.n + self.k - 1)
        return self.n * (self.n + self.k - 1) * t ** (2 * self.k - 2)

    def density_behavior_at_t0(self) -> str:
        """Describe density behavior as t -> 0."""
        if self.m > 0:
            return f'rho -> infinity (diverges like t^(-{self.m:.2f}))'
        elif self.m == 0:
            return 'rho -> constant (FINITE!)'
        else:
            return f'rho -> 0 (vanishes like t^({abs(self.m):.2f}))'

    def singularity_status(self) -> str:
        """Is there a density singularity at t = 0?"""
        if self.k >= 1:
            return 'NO SINGULARITY (k >= 1)'
        else:
            return f'SINGULARITY (k = {self.k} < 1)'

    def summary(self) -> dict:
        """Return summary of meta-Friedmann model."""
        return {
            'model': 'Meta-Friedmann',
            'k': self.k,
            'w': self.w,
            'n': self.n,
            'n_classical': self.classical_n(),
            'n_ratio': self.n / self.classical_n() if self.classical_n() != 0 else None,
            'm': self.m,
            'expansion': f'a(t) ~ t^{self.n:.4f}',
            'density': f'rho(t) ~ t^(-{self.m:.2f})',
            'density_at_t0': self.density_behavior_at_t0(),
            'singularity': self.singularity_status(),
        }


# =============================================================================
# COMPARISON AND ANALYSIS
# =============================================================================

def compare_models(w: float, k_values: List[float]) -> dict:
    """
    Compare classical, naive BG, and meta-Friedmann models.

    Args:
        w: Equation of state
        k_values: List of meta-weight exponents to compare

    Returns:
        Comparison dictionary
    """
    classical = ClassicalFRW(w)
    naive = NaiveBigeometricFRW(w, n_attempt=classical.n)
    meta_models = [MetaFriedmann(k, w) for k in k_values]

    comparison = {
        'equation_of_state': w,
        'classical': classical.summary(),
        'naive_bigeometric': naive.demonstrate_failure(),
        'meta_friedmann': [m.summary() for m in meta_models],
    }

    return comparison


def analyze_singularity_softening(k_values: List[float], w: float = W_RADIATION) -> List[dict]:
    """
    Analyze how increasing k softens the singularity.

    Args:
        k_values: Meta-weight exponents to analyze
        w: Equation of state

    Returns:
        List of analysis results
    """
    results = []
    for k in k_values:
        model = MetaFriedmann(k, w)
        results.append({
            'k': k,
            'n': model.n,
            'm': model.m,
            'density_t0': model.density_behavior_at_t0(),
            'singularity': model.singularity_status(),
        })
    return results


# =============================================================================
# CLI
# =============================================================================

def cmd_classical(args):
    """Show classical FRW results."""
    print("=" * 70)
    print("CLASSICAL FRW COSMOLOGY")
    print("=" * 70)

    for w, name in [(W_RADIATION, "Radiation"), (W_DUST, "Dust")]:
        model = ClassicalFRW(w)
        summary = model.summary()

        print(f"\n  {name} (w = {w:.3f}):")
        print(f"    Expansion: n = {model.n:.4f}")
        print(f"    Density:   m = {model.m:.1f} (rho ~ t^(-2))")
        print(f"    Singularity: YES (rho -> infinity at t = 0)")


def cmd_naive(args):
    """Demonstrate naive bigeometric failure."""
    print("=" * 70)
    print("NAIVE BIGEOMETRIC FRW (DEMONSTRATES FAILURE)")
    print("=" * 70)

    w = args.w
    n_attempt = args.n

    model = NaiveBigeometricFRW(w, n_attempt)
    result = model.demonstrate_failure()

    print(f"\n  Equation of state: w = {w:.3f}")
    print(f"  Attempted expansion: n = {n_attempt:.4f}")
    print()
    print("  BG-FRIEDMANN EQUATION:")
    print(f"    D_BG[a] = e^n = {model.D_BG_scale_factor():.4f}")
    print(f"    Implies: m = 2n = {model.density_exponent_from_friedmann():.4f}")
    print()
    print("  BG-ACCELERATION EQUATION:")
    print(f"    D_BG^2[a] = 1")
    print(f"    Matching powers: n = 0 (FORCED!)")
    print()
    print("  RESULT: " + result['conclusion'])
    print()
    print("  INSIGHT: Even though rho diverges, D_BG[rho] is finite:")
    print(f"    D_BG[rho] = e^(-m) = {model.D_BG_density():.6f}")
    print()
    print("  => Naive bigeometric replacement is INCONSISTENT")
    print("     for nontrivial power-law expansion.")


def cmd_meta(args):
    """Run meta-Friedmann model."""
    print("=" * 70)
    print("META-FRIEDMANN COSMOLOGY")
    print(f"Weight W(t) = t^k, k = {args.k}")
    print("=" * 70)

    model = MetaFriedmann(args.k, args.w)
    classical = ClassicalFRW(args.w)

    summary = model.summary()

    print(f"\n  Parameters:")
    print(f"    Meta-weight exponent: k = {args.k:.4f}")
    print(f"    Equation of state:    w = {args.w:.4f}")
    print()
    print(f"  RESULTS:")
    print(f"    Expansion exponent:   n = {model.n:.6f}")
    print(f"    Classical would give: n = {classical.n:.6f}")
    print(f"    Ratio (n / n_classical): {model.n / classical.n if classical.n != 0 else 'N/A':.4f}")
    print()
    print(f"    Density exponent:     m = {model.m:.4f}")
    print(f"    Density behavior:     {summary['density']}")
    print(f"    At t = 0:            {summary['density_at_t0']}")
    print()
    print(f"  SINGULARITY: {summary['singularity']}")

    # Show time evolution
    print("\n  TIME EVOLUTION:")
    print(f"  {'t':>10} {'a(t)':>12} {'rho(t)':>12} {'H_meta':>12}")
    print("  " + "-" * 50)

    for t in [1e-4, 1e-3, 1e-2, 0.1, 1.0, 10.0]:
        a = model.scale_factor(t)
        rho = model.density(t)
        H = model.meta_hubble(t)

        a_str = f"{a:.4e}" if abs(a) < 1e6 and abs(a) > 1e-6 else f"{a:.2e}"
        rho_str = f"{rho:.4e}" if rho < 1e6 and rho > 1e-6 else f"{rho:.2e}"
        H_str = f"{H:.4e}" if abs(H) < 1e6 and abs(H) > 1e-6 else f"{H:.2e}"

        print(f"  {t:>10.4f} {a_str:>12} {rho_str:>12} {H_str:>12}")


def cmd_compare(args):
    """Compare all models."""
    print("=" * 70)
    print("MODEL COMPARISON")
    print(f"Equation of state: w = {args.w:.3f}")
    print("=" * 70)

    classical = ClassicalFRW(args.w)
    k_values = [0.0, 0.5, 1.0, 1.5, 2.0]

    print("\n  EXPANSION EXPONENT n:")
    print(f"  {'Model':<25} {'k':<8} {'n':<12} {'Ratio':<10}")
    print("  " + "-" * 55)
    print(f"  {'Classical':<25} {'N/A':<8} {classical.n:<12.4f} {'1.0000':<10}")

    for k in k_values:
        meta = MetaFriedmann(k, args.w)
        ratio = meta.n / classical.n if classical.n != 0 else float('inf')
        print(f"  {'Meta-Friedmann':<25} {k:<8.2f} {meta.n:<12.4f} {ratio:<10.4f}")

    print("\n  DENSITY EXPONENT m:")
    print(f"  {'Model':<25} {'k':<8} {'m':<12} {'At t=0':<20}")
    print("  " + "-" * 65)
    print(f"  {'Classical':<25} {'N/A':<8} {classical.m:<12.1f} {'infinity':<20}")

    for k in k_values:
        meta = MetaFriedmann(k, args.w)
        behavior = 'infinity' if meta.m > 0 else ('constant' if meta.m == 0 else 'zero')
        print(f"  {'Meta-Friedmann':<25} {k:<8.2f} {meta.m:<12.2f} {behavior:<20}")

    print("\n  SINGULARITY STATUS:")
    print("    Classical: ALWAYS singular (rho -> infinity)")
    print("    Meta k < 1: Singular (but weaker)")
    print("    Meta k = 1: NO SINGULARITY (density finite)")
    print("    Meta k > 1: NO SINGULARITY (density -> 0)")


def cmd_singularity(args):
    """Analyze singularity softening."""
    print("=" * 70)
    print("SINGULARITY SOFTENING ANALYSIS")
    print("=" * 70)

    k_values = args.k_values
    w = args.w

    print(f"\n  Equation of state: w = {w:.3f}")
    print(f"  Analyzing k values: {k_values}")

    results = analyze_singularity_softening(k_values, w)

    print(f"\n  {'k':<8} {'n':<12} {'m':<12} {'Density at t=0':<30}")
    print("  " + "-" * 65)

    for r in results:
        print(f"  {r['k']:<8.2f} {r['n']:<12.4f} {r['m']:<12.2f} {r['density_t0']:<30}")

    print("\n  INTERPRETATION:")
    for r in results:
        if r['m'] > 0:
            print(f"    k = {r['k']}: Singularity (weaker than classical)")
        elif r['m'] == 0:
            print(f"    k = {r['k']}: NO SINGULARITY - density is CONSTANT")
        else:
            print(f"    k = {r['k']}: NO SINGULARITY - density VANISHES at t=0")


def main():
    parser = argparse.ArgumentParser(
        description="Scalar-Level Meta-Friedmann Equations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python -m meta_calculus.scalar_friedmann classical
    python -m meta_calculus.scalar_friedmann naive --w 0.333 --n 0.5
    python -m meta_calculus.scalar_friedmann meta --k 0.5 --w 0.333
    python -m meta_calculus.scalar_friedmann compare --w 0.333
    python -m meta_calculus.scalar_friedmann singularity --k 0.5 1.0 1.5
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # classical command
    classical_parser = subparsers.add_parser('classical', help='Show classical FRW')
    classical_parser.set_defaults(func=cmd_classical)

    # naive command
    naive_parser = subparsers.add_parser('naive', help='Demonstrate naive BG failure')
    naive_parser.add_argument('--w', type=float, default=W_RADIATION,
                              help='Equation of state (default: 1/3 = radiation)')
    naive_parser.add_argument('--n', type=float, default=0.5,
                              help='Attempted expansion exponent')
    naive_parser.set_defaults(func=cmd_naive)

    # meta command
    meta_parser = subparsers.add_parser('meta', help='Run meta-Friedmann model')
    meta_parser.add_argument('--k', type=float, required=True,
                             help='Meta-weight exponent')
    meta_parser.add_argument('--w', type=float, default=W_RADIATION,
                             help='Equation of state (default: 1/3 = radiation)')
    meta_parser.set_defaults(func=cmd_meta)

    # compare command
    compare_parser = subparsers.add_parser('compare', help='Compare all models')
    compare_parser.add_argument('--w', type=float, default=W_RADIATION,
                                help='Equation of state')
    compare_parser.set_defaults(func=cmd_compare)

    # singularity command
    sing_parser = subparsers.add_parser('singularity', help='Analyze singularity softening')
    sing_parser.add_argument('--k', dest='k_values', nargs='+', type=float,
                             default=[0.0, 0.5, 1.0, 1.5, 2.0],
                             help='Meta-weight exponents to analyze')
    sing_parser.add_argument('--w', type=float, default=W_RADIATION,
                             help='Equation of state')
    sing_parser.set_defaults(func=cmd_singularity)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
