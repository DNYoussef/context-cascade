#!/usr/bin/env python3
"""
Model Comparison: Action-Based u(t) vs Derivative-Weight t^k

This module provides the rigorous comparison between:
1. Action-based meta-GR with u(t) = t^s
2. Derivative-weight meta-Friedmann with D_meta = t^k d/dt

KEY RESULTS:
  - Action-based: n_act(s,w) from quadratic equation
  - Derivative-weight: n_toy(k,w) = (2/3)(1-k)/(1+w)
  - Matching: k_equiv(s,w) = 1 - (3/2)(1+w) n_act(s,w)
  - CRITICAL: Even when n matches, rho scaling DIFFERS!

BBN/CMB CONSTRAINTS:
  - Action-based: |s| < 0.05-0.1
  - Derivative-weight: |k| < 0.03-0.05

Usage:
    python -m meta_calculus.model_comparison n-comparison --w 0.333
    python -m meta_calculus.model_comparison matching --s 0.5 --w 0
    python -m meta_calculus.model_comparison constraints
"""

import numpy as np
from typing import Tuple, Dict, Optional
import argparse
import sys


# =============================================================================
# ACTION-BASED META-GR: n_act(s, w)
# =============================================================================

def discriminant(s: float, w: float) -> float:
    """
    Discriminant of the quadratic for n_act(s, w).

    Delta(s, w) = 9*s^2*w^2 - 8*s^2 + 4*s + 4

    Must be >= 0 for real solutions.
    """
    return 9 * s**2 * w**2 - 8 * s**2 + 4 * s + 4


def n_action_based(s: float, w: float) -> float:
    """
    Expansion exponent from action-based meta-GR.

    From the quadratic:
        3(1+w)n^2 + (3ws + 2s - 2)n + s(s-1) = 0

    Physical branch (+ root, reduces to classical at s=0):
        n_act = [-(3ws + 2s - 2) + sqrt(Delta)] / [6(1+w)]

    Args:
        s: Weight exponent in u(t) = t^s
        w: Equation of state p = w * rho

    Returns:
        Expansion exponent n
    """
    if w == -1:
        return float('inf')  # de Sitter limit

    Delta = discriminant(s, w)

    if Delta < 0:
        return float('nan')  # No real solution

    numerator = -(3*w*s + 2*s - 2) + np.sqrt(Delta)
    denominator = 6 * (1 + w)

    return numerator / denominator


def n_action_based_expansion(s: float, w: float) -> Dict:
    """
    Taylor expansion of n_act(s, w) for small s.

    For radiation (w=1/3):
        n = 1/2 - s/4 - s^2/4 + O(s^3)

    For dust (w=0):
        n = 2/3 - s/6 - 3s^2/8 + O(s^3)
    """
    # Coefficients from Taylor expansion
    if abs(w - 1/3) < 1e-10:
        # Radiation
        n0 = 0.5
        n1 = -0.25
        n2 = -0.25
    elif abs(w) < 1e-10:
        # Dust
        n0 = 2/3
        n1 = -1/6
        n2 = -3/8
    else:
        # General case - numerical differentiation
        h = 1e-6
        n0 = n_action_based(0, w)
        n1 = (n_action_based(h, w) - n_action_based(-h, w)) / (2*h)
        n2 = (n_action_based(h, w) - 2*n0 + n_action_based(-h, w)) / h**2 / 2

    return {
        'n0': n0,
        'n1': n1,
        'n2': n2,
        'expansion': f'n = {n0:.4f} + {n1:.4f}*s + {n2:.4f}*s^2 + O(s^3)',
    }


def allowed_s_range(w: float) -> Tuple[float, float]:
    """
    Find allowed range of s where Delta >= 0.

    For dust (w=0): -0.5 <= s <= 1
    For radiation (w=1/3): approximately -0.52 <= s <= 1.09
    """
    # Solve Delta(s, w) = 0
    # 9*w^2*s^2 - 8*s^2 + 4*s + 4 = 0
    # (9*w^2 - 8)*s^2 + 4*s + 4 = 0

    a = 9*w**2 - 8
    b = 4
    c = 4

    if abs(a) < 1e-10:
        # Linear case
        s_bound = -c / b
        return (-np.inf, s_bound) if s_bound > 0 else (s_bound, np.inf)

    disc = b**2 - 4*a*c

    if disc < 0:
        return (-np.inf, np.inf)  # All s allowed

    s1 = (-b - np.sqrt(disc)) / (2*a)
    s2 = (-b + np.sqrt(disc)) / (2*a)

    if a < 0:
        return (min(s1, s2), max(s1, s2))
    else:
        # Check which interval has Delta >= 0
        s_test = (s1 + s2) / 2
        if discriminant(s_test, w) >= 0:
            return (min(s1, s2), max(s1, s2))
        else:
            return (-np.inf, min(s1, s2))  # or (max(s1, s2), inf)


# =============================================================================
# DERIVATIVE-WEIGHT META-FRIEDMANN: n_toy(k, w)
# =============================================================================

def n_derivative_weight(k: float, w: float) -> float:
    """
    Expansion exponent from derivative-weight toy model.

    n_toy(k, w) = (2/3) * (1-k) / (1+w)

    Args:
        k: Weight exponent in D_meta = t^k d/dt
        w: Equation of state

    Returns:
        Expansion exponent n
    """
    if w == -1:
        return float('inf')
    return (2/3) * (1 - k) / (1 + w)


def density_exponent_toy(k: float) -> float:
    """
    Density exponent for derivative-weight model.

    m = 2 - 2k
    rho ~ t^(-m)
    """
    return 2 - 2*k


# =============================================================================
# MODEL MATCHING
# =============================================================================

def k_equivalent(s: float, w: float) -> float:
    """
    Find k such that n_toy(k, w) = n_act(s, w).

    k_equiv = 1 - (3/2) * (1+w) * n_act(s, w)

    This makes the expansion exponents match, but
    THE DENSITY SCALING WILL STILL DIFFER!
    """
    n_act = n_action_based(s, w)

    if np.isnan(n_act):
        return float('nan')

    return 1 - (3/2) * (1 + w) * n_act


def compare_at_matched_n(s: float, w: float) -> Dict:
    """
    Compare models at matched expansion exponent.

    Shows that even when n matches, rho scaling differs.
    """
    n_act = n_action_based(s, w)
    k_eq = k_equivalent(s, w)
    n_toy = n_derivative_weight(k_eq, w)

    # Density exponents
    m_action = 2.0  # Always 2 for action-based!
    m_toy = density_exponent_toy(k_eq)

    return {
        's': s,
        'w': w,
        'n_action': n_act,
        'k_equivalent': k_eq,
        'n_toy': n_toy,
        'n_match': abs(n_act - n_toy) < 1e-10,
        'm_action': m_action,
        'm_toy': m_toy,
        'rho_action': f't^(-{m_action:.2f})',
        'rho_toy': f't^(-{m_toy:.2f})',
        'rho_match': abs(m_action - m_toy) < 1e-10,
    }


# =============================================================================
# HUBBLE RATE DEVIATIONS
# =============================================================================

def hubble_deviation_action(s: float, w: float) -> float:
    """
    Fractional deviation of Hubble rate from classical.

    delta_H / H = (n_act - n_classical) / n_classical

    For small s (radiation): delta_H/H ~ -s/2
    """
    n_act = n_action_based(s, w)
    n_classical = n_action_based(0, w)

    if n_classical == 0:
        return float('inf')

    return (n_act - n_classical) / n_classical


def hubble_deviation_toy(k: float) -> float:
    """
    Fractional deviation of Hubble rate for toy model.

    delta_H / H = -k  (exactly, for any w)
    """
    return -k


# =============================================================================
# BBN/CMB CONSTRAINTS
# =============================================================================

class ObservationalConstraints:
    """
    BBN and CMB constraints on s and k.

    From Planck 2018 + BAO:
        N_eff = 2.99 +/- 0.17

    From BBN + Planck (G_BBN):
        G_BBN / G_0 = 0.99 (+0.06, -0.05) at 2-sigma
        => |delta_H / H| < 3%
    """

    # Observational limits
    DELTA_H_LIMIT_BBN = 0.03      # 3% from BBN
    DELTA_H_LIMIT_CONSERVATIVE = 0.05  # 5% conservative

    @classmethod
    def max_s_from_bbn(cls, w: float = 1/3) -> float:
        """
        Maximum |s| consistent with BBN for action-based model.

        For radiation: delta_H/H ~ -s/2
        => |s| < 2 * delta_H_limit
        """
        # Use Taylor expansion for small s
        # delta_H/H = n1 * s / n0 (approximately)
        expansion = n_action_based_expansion(0, w)
        n0 = expansion['n0']
        n1 = expansion['n1']

        # |n1 * s / n0| < delta_H_limit
        # |s| < delta_H_limit * n0 / |n1|

        s_max = cls.DELTA_H_LIMIT_BBN * abs(n0 / n1)
        return s_max

    @classmethod
    def max_k_from_bbn(cls) -> float:
        """
        Maximum |k| consistent with BBN for derivative-weight model.

        delta_H/H = -k exactly
        => |k| < delta_H_limit
        """
        return cls.DELTA_H_LIMIT_BBN

    @classmethod
    def summary(cls) -> Dict:
        """Generate constraint summary."""
        return {
            'action_based': {
                'radiation_s_max': cls.max_s_from_bbn(1/3),
                'dust_s_max': cls.max_s_from_bbn(0),
                'limit_type': 'BBN (3%)',
            },
            'derivative_weight': {
                'k_max': cls.max_k_from_bbn(),
                'limit_type': 'BBN (3%)',
            },
            'conservative': {
                'action_s_max_rad': cls.DELTA_H_LIMIT_CONSERVATIVE * 2,  # ~0.1
                'derivative_k_max': cls.DELTA_H_LIMIT_CONSERVATIVE,      # ~0.05
            },
            'references': [
                'Planck 2018: N_eff = 2.99 +/- 0.17',
                'BBN+Planck: G_BBN/G_0 = 0.99 (+0.06, -0.05)',
            ],
        }


# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_n_comparison(args):
    """Compare n values across both models."""
    print("=" * 70)
    print("EXPANSION EXPONENT COMPARISON: n_act(s,w) vs n_toy(k,w)")
    print("=" * 70)

    w = args.w
    w_name = "radiation" if abs(w - 1/3) < 0.01 else "dust" if abs(w) < 0.01 else f"w={w}"

    print(f"\n  Equation of state: w = {w:.4f} ({w_name})")

    # Classical values
    n_classical = n_action_based(0, w)
    print(f"  Classical n: {n_classical:.4f}")

    # Allowed s range
    s_min, s_max = allowed_s_range(w)
    print(f"\n  Allowed s range: [{s_min:.4f}, {s_max:.4f}]")

    # Taylor expansion
    expansion = n_action_based_expansion(0, w)
    print(f"\n  Taylor expansion for small s:")
    print(f"    {expansion['expansion']}")

    # Table
    print(f"\n  ACTION-BASED n_act(s, w={w:.3f}):")
    print(f"  {'s':<10} {'n_act':<12} {'delta_H/H':<12}")
    print("  " + "-" * 35)

    for s in [-0.25, -0.1, -0.05, 0, 0.05, 0.1, 0.25, 0.5]:
        if s_min <= s <= s_max:
            n = n_action_based(s, w)
            dH = hubble_deviation_action(s, w)
            print(f"  {s:<10.2f} {n:<12.4f} {dH:<+12.4f}")

    print(f"\n  DERIVATIVE-WEIGHT n_toy(k, w={w:.3f}):")
    print(f"  {'k':<10} {'n_toy':<12} {'delta_H/H':<12} {'m (rho exp)':<12}")
    print("  " + "-" * 50)

    for k in [-0.1, -0.05, 0, 0.05, 0.1, 0.25, 0.5, 1.0]:
        n = n_derivative_weight(k, w)
        dH = hubble_deviation_toy(k)
        m = density_exponent_toy(k)
        print(f"  {k:<10.2f} {n:<12.4f} {dH:<+12.4f} {m:<12.2f}")


def cmd_matching(args):
    """Show model matching at given s, w."""
    print("=" * 70)
    print(f"MODEL MATCHING: s = {args.s}, w = {args.w}")
    print("=" * 70)

    result = compare_at_matched_n(args.s, args.w)

    print(f"\n  ACTION-BASED (u(t) = t^s):")
    print(f"    s = {result['s']:.4f}")
    print(f"    n_action = {result['n_action']:.4f}")
    print(f"    rho ~ {result['rho_action']}")

    print(f"\n  EQUIVALENT DERIVATIVE-WEIGHT:")
    print(f"    k_equiv = {result['k_equivalent']:.4f}")
    print(f"    n_toy = {result['n_toy']:.4f}")
    print(f"    rho ~ {result['rho_toy']}")

    print(f"\n  COMPARISON:")
    print(f"    Expansion n matches: {result['n_match']}")
    print(f"    Density exponent matches: {result['rho_match']}")

    if not result['rho_match']:
        print(f"\n  CRITICAL DIFFERENCE:")
        print(f"    Action-based: rho ~ t^(-2) ALWAYS")
        print(f"    Derivative-weight: rho ~ t^(-{result['m_toy']:.2f})")
        print(f"    => Different early-time thermodynamics!")
        print(f"    => Different BBN predictions!")


def cmd_constraints(args):
    """Show BBN/CMB constraints on s and k."""
    print("=" * 70)
    print("BBN/CMB CONSTRAINTS ON META-COSMOLOGY PARAMETERS")
    print("=" * 70)

    constraints = ObservationalConstraints.summary()

    print("\n  OBSERVATIONAL INPUTS:")
    for ref in constraints['references']:
        print(f"    - {ref}")

    print("\n  ACTION-BASED META-GR (u(t) = t^s):")
    print(f"    Radiation: |s| < {constraints['action_based']['radiation_s_max']:.3f}")
    print(f"    Dust:      |s| < {constraints['action_based']['dust_s_max']:.3f}")

    print("\n  DERIVATIVE-WEIGHT (D_meta = t^k d/dt):")
    print(f"    Any w:     |k| < {constraints['derivative_weight']['k_max']:.3f}")

    print("\n  CONSERVATIVE BOUNDS (5% tolerance):")
    print(f"    Action s:  |s| < {constraints['conservative']['action_s_max_rad']:.2f}")
    print(f"    Deriv. k:  |k| < {constraints['conservative']['derivative_k_max']:.2f}")

    print("\n  IMPLICATIONS:")
    print("    - Both models must be VERY close to classical during BBN/CMB")
    print("    - Singularity removal (k >= 1) requires PHASE TRANSITION")
    print("    - Meta-phase must end BEFORE T ~ 100 MeV")

    print("\n  KEY DIFFERENCE:")
    print("    Action-based: rho ~ t^(-2) always (no singularity softening)")
    print("    Derivative-weight: rho ~ t^(-(2-2k)) (CAN soften singularity)")
    print("    => Only derivative-weight can remove singularity!")


def cmd_discriminant(args):
    """Show discriminant analysis for action-based model."""
    print("=" * 70)
    print("DISCRIMINANT ANALYSIS: Delta(s, w)")
    print("=" * 70)

    print("\n  Discriminant: Delta = 9*s^2*w^2 - 8*s^2 + 4*s + 4")
    print("  Must have Delta >= 0 for real n_act")

    for w, name in [(0, "Dust"), (1/3, "Radiation")]:
        s_min, s_max = allowed_s_range(w)
        print(f"\n  {name} (w = {w:.3f}):")
        print(f"    Allowed s: [{s_min:.4f}, {s_max:.4f}]")

        print(f"    {'s':<10} {'Delta':<12} {'Valid?':<10}")
        print("    " + "-" * 35)

        for s in np.linspace(s_min - 0.1, s_max + 0.1, 9):
            D = discriminant(s, w)
            valid = "YES" if D >= 0 else "NO"
            print(f"    {s:<10.3f} {D:<12.4f} {valid:<10}")


def main():
    parser = argparse.ArgumentParser(
        description="Model Comparison: Action-Based vs Derivative-Weight",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # n-comparison command
    n_parser = subparsers.add_parser('n-comparison',
        help='Compare expansion exponents')
    n_parser.add_argument('--w', type=float, default=1/3,
        help='Equation of state')
    n_parser.set_defaults(func=cmd_n_comparison)

    # matching command
    match_parser = subparsers.add_parser('matching',
        help='Show model matching at given s, w')
    match_parser.add_argument('--s', type=float, required=True,
        help='Action-based weight exponent')
    match_parser.add_argument('--w', type=float, default=0,
        help='Equation of state')
    match_parser.set_defaults(func=cmd_matching)

    # constraints command
    const_parser = subparsers.add_parser('constraints',
        help='Show BBN/CMB constraints')
    const_parser.set_defaults(func=cmd_constraints)

    # discriminant command
    disc_parser = subparsers.add_parser('discriminant',
        help='Show discriminant analysis')
    disc_parser.set_defaults(func=cmd_discriminant)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
