#!/usr/bin/env python3
"""
Jacobian Interpretation of Meta-Calculus (Gap 3)

This module shows how the t^(2k) factor in L_meta arises as a Jacobian
from coordinate transformation, connecting to positive geometry.

KEY INSIGHT:
  The minisuperspace meta-Lagrangian:
    L_meta = -(3/8 pi G) a t^(2k) a_dot^2 - a^3 rho(a)

  The t^(2k) factor is the Jacobian from:
    - Standard time t
    - Meta-time tau = integral dt / t^k = t^(1-k) / (1-k)

CONNECTION TO POSITIVE GEOMETRY:
  In positive geometry terms:
    - Standard coordinates (t, a) -> linear facet functions
    - Meta-coordinates (tau, alpha) -> nonlinear facet functions
    - Jacobian t^k = measure deformation factor
    - GUC is a coordinate change, NOT a new geometry

Usage:
    python -m meta_calculus.jacobian show
    python -m meta_calculus.jacobian verify --k 0.5
    python -m meta_calculus.jacobian transform --k 0.5 --t 1.0
    python -m meta_calculus.jacobian compare
"""

import numpy as np
from typing import Tuple, Dict, Callable
import argparse
import sys


# =============================================================================
# COORDINATE TRANSFORMATIONS
# =============================================================================

class MetaTimeTransform:
    """
    Coordinate transformation from standard time t to meta-time tau.

    tau = integral_0^t dt' / t'^k
        = t^(1-k) / (1-k)   for k != 1
        = ln(t)             for k = 1

    Inverse:
    t = [(1-k) tau]^(1/(1-k))   for k != 1
    t = exp(tau)                 for k = 1
    """

    def __init__(self, k: float):
        """
        Initialize with meta-weight exponent k.

        Args:
            k: Meta-weight exponent
        """
        self.k = k

    def tau_of_t(self, t: float) -> float:
        """
        Convert standard time t to meta-time tau.

        Args:
            t: Standard cosmic time (must be > 0)

        Returns:
            Meta-time tau
        """
        if t <= 0:
            return float('-inf') if self.k < 1 else float('inf')

        if abs(self.k - 1.0) < 1e-10:
            # k = 1: tau = ln(t)
            return np.log(t)
        else:
            # k != 1: tau = t^(1-k) / (1-k)
            return t**(1 - self.k) / (1 - self.k)

    def t_of_tau(self, tau: float) -> float:
        """
        Convert meta-time tau to standard time t.

        Args:
            tau: Meta-time

        Returns:
            Standard cosmic time t
        """
        if abs(self.k - 1.0) < 1e-10:
            # k = 1: t = exp(tau)
            return np.exp(tau)
        else:
            # k != 1: t = [(1-k) tau]^(1/(1-k))
            arg = (1 - self.k) * tau
            if arg <= 0:
                return float('nan')
            return arg**(1 / (1 - self.k))

    def dt_dtau(self, t: float) -> float:
        """
        Jacobian dt/d(tau) = t^k.

        This is the key factor appearing in L_meta.
        """
        return t**self.k

    def dtau_dt(self, t: float) -> float:
        """
        Inverse Jacobian d(tau)/dt = t^(-k).
        """
        return t**(-self.k)

    def verify_inverse(self, t_test: float = 1.0) -> Dict:
        """
        Verify that tau(t(tau)) = tau and t(tau(t)) = t.

        Returns:
            Dictionary with verification results
        """
        tau = self.tau_of_t(t_test)
        t_recovered = self.t_of_tau(tau)

        tau_test = 1.0
        t_from_tau = self.t_of_tau(tau_test)
        tau_recovered = self.tau_of_t(t_from_tau)

        return {
            't_original': t_test,
            'tau': tau,
            't_recovered': t_recovered,
            't_error': abs(t_test - t_recovered),
            'tau_original': tau_test,
            't_from_tau': t_from_tau,
            'tau_recovered': tau_recovered,
            'tau_error': abs(tau_test - tau_recovered),
            'verified': (abs(t_test - t_recovered) < 1e-10 and
                        abs(tau_test - tau_recovered) < 1e-10),
        }


# =============================================================================
# JACOBIAN IN LAGRANGIAN
# =============================================================================

class JacobianInLagrangian:
    """
    Show how the Jacobian appears in the meta-Lagrangian.

    Standard Lagrangian (in t):
        L = -(3/8 pi G) a a_dot^2 - a^3 rho

    In meta-time tau:
        a_dot = da/dt = da/d(tau) * d(tau)/dt = a'(tau) * t^(-k)

        L dt = L_standard dt
             = -(3/8 pi G) a (a'(tau) t^(-k))^2 dt - a^3 rho dt
             = -(3/8 pi G) a a'^2 t^(-2k) t^k d(tau) - a^3 rho t^k d(tau)
             = [-(3/8 pi G) a a'^2 t^(-k) - a^3 rho t^k] d(tau)

    Rewriting in t with D_meta = t^k d/dt:
        L_meta = -(3/8 pi G) a t^(2k) (D_meta a / t^k)^2 - a^3 rho
               = -(3/8 pi G) a t^(2k) a_dot^2 - a^3 rho

    The t^(2k) IS the Jacobian factor!
    """

    def __init__(self, k: float):
        """
        Initialize with meta-weight k.

        Args:
            k: Meta-weight exponent
        """
        self.k = k
        self.transform = MetaTimeTransform(k)

    def classical_lagrangian(self, a: float, a_dot: float, rho: float) -> float:
        """
        Classical FRW Lagrangian.

        L = -(3/8 pi G) a a_dot^2 - a^3 rho
        """
        G = 1.0  # Geometric units
        return -(3.0 / (8.0 * np.pi * G)) * a * a_dot**2 - a**3 * rho

    def meta_lagrangian(self, a: float, a_dot: float, t: float, rho: float) -> float:
        """
        Meta-Lagrangian with t^(2k) factor.

        L_meta = -(3/8 pi G) a t^(2k) a_dot^2 - a^3 rho
        """
        G = 1.0
        jacobian_factor = t**(2 * self.k)
        return -(3.0 / (8.0 * np.pi * G)) * a * jacobian_factor * a_dot**2 - a**3 * rho

    def lagrangian_in_metatime(self, a: float, a_prime: float, tau: float, rho: float) -> float:
        """
        Lagrangian expressed in meta-time tau.

        a_prime = da/d(tau)

        L_tau = -(3/8 pi G) a a_prime^2 - a^3 rho * (dt/d tau)
        """
        t = self.transform.t_of_tau(tau)
        G = 1.0
        dt_dtau = self.transform.dt_dtau(t)

        # In meta-time, the kinetic term has no extra factor
        # but the potential term picks up dt/d(tau) = t^k
        kinetic = -(3.0 / (8.0 * np.pi * G)) * a * a_prime**2
        potential = -a**3 * rho * dt_dtau

        return kinetic + potential

    def verify_equivalence(self, t: float = 1.0, n: float = 0.5) -> Dict:
        """
        Verify L_meta(t) = L_tau(tau) after coordinate change.

        For a = t^n:
            a_dot = n t^(n-1)
            a_prime = da/d(tau) = a_dot * dt/d(tau) = n t^(n-1) * t^k = n t^(n-1+k)

        Returns:
            Dictionary with verification
        """
        # Power-law solution
        a = t**n
        a_dot = n * t**(n - 1)
        rho = 1.0  # Arbitrary normalization

        # Meta-Lagrangian in t
        L_meta = self.meta_lagrangian(a, a_dot, t, rho)

        # Convert to meta-time
        tau = self.transform.tau_of_t(t)
        dt_dtau = self.transform.dt_dtau(t)
        a_prime = a_dot * dt_dtau  # da/d(tau)

        # Lagrangian in meta-time (times d(tau))
        L_tau = self.lagrangian_in_metatime(a, a_prime, tau, rho)

        # L_meta dt = L_tau d(tau)
        # L_meta = L_tau * (d tau / dt) = L_tau * t^(-k)
        L_meta_from_tau = L_tau * t**(-self.k)

        return {
            'k': self.k,
            't': t,
            'tau': tau,
            'a': a,
            'a_dot': a_dot,
            'a_prime': a_prime,
            'L_meta': L_meta,
            'L_tau': L_tau,
            'L_meta_from_tau': L_meta_from_tau,
            'equivalence_error': abs(L_meta - L_meta_from_tau),
            'verified': abs(L_meta - L_meta_from_tau) < 1e-10 * abs(L_meta),
        }


# =============================================================================
# GUC INTERPRETATION
# =============================================================================

class GUCInterpretation:
    """
    Interpretation in terms of Generalized Uniformly Weighted Calculus (GUC).

    GUC defines:
        D_w[f] = (v/u) * f'

    For meta-calculus with weight t^k:
        u(t) = 1, v(t) = t^k
        D_meta[f] = t^k * df/dt

    This is equivalent to:
        - Coordinate change t -> tau = t^(1-k)/(1-k)
        - Jacobian factor t^k in measure

    KEY INSIGHT from positive geometry:
        GUC = coordinate + measure deformation
        NOT a new geometry/polytope
        Same underlying structure, different parametrization
    """

    def __init__(self, k: float):
        """
        Initialize GUC with weight exponent k.

        Args:
            k: Exponent in D_meta = t^k d/dt
        """
        self.k = k

    def u_weight(self, t: float) -> float:
        """Weight function u(t) = 1 in standard GUC notation."""
        return 1.0

    def v_weight(self, t: float) -> float:
        """Weight function v(t) = t^k in standard GUC notation."""
        return t**self.k

    def meta_derivative(self, f: Callable, t: float, h: float = 1e-6) -> float:
        """
        Compute meta-derivative D_meta[f](t) = t^k * f'(t).

        Args:
            f: Function to differentiate
            t: Point of evaluation
            h: Step size for numerical derivative

        Returns:
            Meta-derivative value
        """
        # Central difference
        f_prime = (f(t + h) - f(t - h)) / (2 * h)
        return self.v_weight(t) * f_prime

    def jacobian_factor(self, t: float) -> float:
        """
        The Jacobian factor t^(2k) appearing in L_meta.

        This arises from:
            dt = t^k d(tau)
            dt^2 in kinetic term -> t^(2k) d(tau)^2

        In Lagrangian written in t but with D_meta:
            a_dot^2 dt = (D_meta a / t^k)^2 dt
            The t^(2k) compensates to give D_meta a properly.
        """
        return t**(2 * self.k)

    def connection_to_positive_geometry(self) -> str:
        """
        Explain connection to positive geometry / cosmological polytope.
        """
        return f"""
CONNECTION TO POSITIVE GEOMETRY
==============================

For the triangle (simplest cosmological polytope):

  Standard coordinates (x, y):
    Omega = dx ^ dy / [L1(x,y) * L2(x,y) * L3(x,y)]

  Under GUC-like transform x = exp(alpha * u), y = exp(beta * v):
    Omega_GUC = J * du ^ dv / [L1(phi) * L2(phi) * L3(phi)]

    where J = alpha * beta * exp(alpha*u + beta*v)
          is the Jacobian prefactor

For meta-cosmology with k = {self.k}:

  Standard time t:
    L = -(3/8 pi G) a a_dot^2 - a^3 rho

  With D_meta = t^k d/dt:
    L_meta = -(3/8 pi G) a t^(2k) a_dot^2 - a^3 rho

    The t^(2k) IS the Jacobian from t -> tau coordinate change!

KEY INSIGHT:
  - GUC does NOT create a new polytope/geometry
  - It gives a DEFORMED CHART + DEFORMED MEASURE on the same polytope
  - The combinatorics and topology remain unchanged
  - Only the coordinates and measure are transformed
  - This matches what we found in FRW: changing to meta-derivatives
    doesn't change which spacetime solution you have, just how you
    parametrize and weight it.

CONSEQUENCE:
  For genuinely new physics, you need more than GUC:
    - New action terms
    - New constraints
    - Different boundary conditions

  But GUC is EXCELLENT for finding "good coordinates" where
  structure is simpler (e.g., power-law divergences become constant).
"""


# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_show(args):
    """Show the Jacobian interpretation."""
    print("=" * 70)
    print("JACOBIAN INTERPRETATION OF t^(2k) IN L_meta")
    print("=" * 70)

    print("""
1. MINISUPERSPACE META-LAGRANGIAN

   L_meta = -(3/8 pi G) a t^(2k) a_dot^2 - a^3 rho(a)

   The t^(2k) factor is NOT arbitrary - it is a JACOBIAN.

2. COORDINATE TRANSFORMATION

   Standard time: t
   Meta-time:     tau = integral_0^t dt' / t'^k
                      = t^(1-k) / (1-k)    for k != 1
                      = ln(t)              for k = 1

   Inverse:       t = [(1-k) tau]^(1/(1-k))

3. JACOBIAN DERIVATION

   dt/d(tau) = t^k

   The kinetic term transforms:
     a_dot^2 dt = (da/d(tau) * d(tau)/dt)^2 dt
                = (da/d(tau))^2 * t^(-2k) * dt
                = (da/d(tau))^2 * t^(-2k) * t^k d(tau)
                = (da/d(tau))^2 * t^(-k) d(tau)

   Rewriting in t with the measure factor:
     L_meta = t^k * L_classical(D_meta a)
            = -(3/8 pi G) a t^(2k) a_dot^2 - a^3 rho

4. PHYSICAL MEANING

   Near t = 0:
     - d(tau) = dt / t^k -> large d(tau) for small dt (if k > 0)
     - Time "slows down" near the singularity
     - This is the regularization mechanism

   For k >= 1:
     - tau(t=0) is finite (= 0)
     - The singularity is a finite point in meta-time
     - Density rho ~ t^(-(2-2k)) is finite or zero at t=0
""")


def cmd_verify(args):
    """Verify Jacobian equivalence."""
    print("=" * 70)
    print(f"VERIFYING JACOBIAN INTERPRETATION (k = {args.k})")
    print("=" * 70)

    # Coordinate transform verification
    print("\n  COORDINATE TRANSFORM VERIFICATION:")
    transform = MetaTimeTransform(args.k)
    result = transform.verify_inverse(args.t)

    print(f"    t -> tau -> t:")
    print(f"      t = {result['t_original']:.6f}")
    print(f"      tau = {result['tau']:.6f}")
    print(f"      t recovered = {result['t_recovered']:.6f}")
    print(f"      Error = {result['t_error']:.2e}")

    print(f"    tau -> t -> tau:")
    print(f"      tau = {result['tau_original']:.6f}")
    print(f"      t = {result['t_from_tau']:.6f}")
    print(f"      tau recovered = {result['tau_recovered']:.6f}")
    print(f"      Error = {result['tau_error']:.2e}")

    print(f"    Verified: {result['verified']}")

    # Lagrangian equivalence
    print("\n  LAGRANGIAN EQUIVALENCE:")
    lagr = JacobianInLagrangian(args.k)
    lag_result = lagr.verify_equivalence(t=args.t, n=0.5)

    print(f"    L_meta(t) = {lag_result['L_meta']:.6f}")
    print(f"    L_tau(tau) -> L_meta = {lag_result['L_meta_from_tau']:.6f}")
    print(f"    Error = {lag_result['equivalence_error']:.2e}")
    print(f"    Verified: {lag_result['verified']}")


def cmd_transform(args):
    """Show coordinate transformation at a point."""
    print("=" * 70)
    print(f"COORDINATE TRANSFORMATION (k = {args.k})")
    print("=" * 70)

    transform = MetaTimeTransform(args.k)

    t = args.t
    tau = transform.tau_of_t(t)
    dt_dtau = transform.dt_dtau(t)
    dtau_dt = transform.dtau_dt(t)

    print(f"\n  Standard time:     t = {t:.6f}")
    print(f"  Meta-time:         tau = {tau:.6f}")
    print(f"\n  Jacobian factors:")
    print(f"    dt/d(tau) = t^k = {dt_dtau:.6f}")
    print(f"    d(tau)/dt = t^(-k) = {dtau_dt:.6f}")
    print(f"\n  Lagrangian factor:")
    print(f"    t^(2k) = {t**(2*args.k):.6f}")

    if args.k > 0:
        print(f"\n  Near t = 0:")
        print(f"    dt/d(tau) -> 0 (time slows)")
        print(f"    d(tau)/dt -> infinity (meta-time speeds up)")
    elif args.k < 0:
        print(f"\n  Near t = 0:")
        print(f"    dt/d(tau) -> infinity")
        print(f"    d(tau)/dt -> 0")


def cmd_compare(args):
    """Compare different k values."""
    print("=" * 70)
    print("JACOBIAN COMPARISON ACROSS k VALUES")
    print("=" * 70)

    print(f"\n  At t = 1.0:")
    print(f"  {'k':<10} {'tau(t=1)':<12} {'t^(2k)':<12} {'m = 2-2k':<12} {'Singularity':<15}")
    print("  " + "-" * 60)

    for k in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25]:
        transform = MetaTimeTransform(k)
        tau = transform.tau_of_t(1.0)
        jacobian = 1.0**(2*k)
        m = 2 - 2*k

        if k >= 1:
            sing = "REMOVED"
        elif k > 0.5:
            sing = "Weakened"
        elif k > 0:
            sing = "Slightly softer"
        else:
            sing = "Classical"

        print(f"  {k:<10.2f} {tau:<12.4f} {jacobian:<12.4f} {m:<12.2f} {sing:<15}")

    print("\n  Near t = 0.01:")
    print(f"  {'k':<10} {'tau':<12} {'t^(2k)':<12} {'rho ~ t^(-m)':<15}")
    print("  " + "-" * 50)

    t_small = 0.01
    for k in [0.0, 0.5, 1.0]:
        transform = MetaTimeTransform(k)
        tau = transform.tau_of_t(t_small)
        jacobian = t_small**(2*k)
        m = 2 - 2*k
        rho = t_small**(-m)

        print(f"  {k:<10.2f} {tau:<12.4f} {jacobian:<12.6f} {rho:<15.2e}")


def cmd_guc(args):
    """Show GUC interpretation and positive geometry connection."""
    print("=" * 70)
    print("GUC INTERPRETATION AND POSITIVE GEOMETRY")
    print("=" * 70)

    guc = GUCInterpretation(args.k)
    print(guc.connection_to_positive_geometry())


def main():
    parser = argparse.ArgumentParser(
        description="Jacobian Interpretation of Meta-Calculus",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # show command
    show_parser = subparsers.add_parser('show',
        help='Show Jacobian interpretation')
    show_parser.set_defaults(func=cmd_show)

    # verify command
    verify_parser = subparsers.add_parser('verify',
        help='Verify Jacobian equivalence')
    verify_parser.add_argument('--k', type=float, default=0.5)
    verify_parser.add_argument('--t', type=float, default=1.0)
    verify_parser.set_defaults(func=cmd_verify)

    # transform command
    trans_parser = subparsers.add_parser('transform',
        help='Show coordinate transformation')
    trans_parser.add_argument('--k', type=float, default=0.5)
    trans_parser.add_argument('--t', type=float, default=1.0)
    trans_parser.set_defaults(func=cmd_transform)

    # compare command
    comp_parser = subparsers.add_parser('compare',
        help='Compare different k values')
    comp_parser.set_defaults(func=cmd_compare)

    # guc command
    guc_parser = subparsers.add_parser('guc',
        help='Show GUC and positive geometry connection')
    guc_parser.add_argument('--k', type=float, default=0.5)
    guc_parser.set_defaults(func=cmd_guc)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
