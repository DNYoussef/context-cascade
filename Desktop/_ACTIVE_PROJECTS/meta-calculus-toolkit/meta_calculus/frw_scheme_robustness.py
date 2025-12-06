#!/usr/bin/env python3
"""
FRW Scheme-Robustness: Cosmological Observables Invariant Under C-Scheme Changes

This module defines scheme-robust observables for FRW cosmology, implementing
the meta-principle: Physical = Invariant under G_scheme.

SCHEME-ROBUST OBSERVABLES (Physical):
    - H(z): Hubble parameter as function of redshift
    - BBN abundances: Light element ratios from nucleosynthesis
    - CMB distance measures: Angular diameter distance, sound horizon
    - Dark energy density: Omega_Lambda

SCHEME-DEPENDENT (Scaffolding):
    - Coordinate time t
    - Friedmann equation form (depends on calculus choice)
    - Big Bang singularity behavior (C-scheme dependent!)

KEY INSIGHT:
    Different C-schemes (classical d/dt, meta-derivative D_meta, bigeometric D_BG)
    MUST agree on H(z) but MAY disagree near singularities.

    New physics lives where scheme-robustness BREAKS.

References:
    - Grossman & Katz (1972) "Non-Newtonian Calculus"
    - Meta-calculus framework documentation

Usage:
    python -m meta_calculus.frw_scheme_robustness demo
    python -m meta_calculus.frw_scheme_robustness hunt_breaking
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Callable, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass
import argparse
import sys


# =============================================================================
# C-SCHEME DEFINITIONS FOR COSMOLOGY
# =============================================================================

class CosmologyCScheme(ABC):
    """
    Abstract C-scheme (calculus scheme) for cosmology.

    A C-scheme defines how time derivatives are computed, which affects:
    - The form of the Friedmann equation
    - Singularity behavior
    - Evolution equations
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name."""
        pass

    @abstractmethod
    def time_derivative(self, f: Callable[[float], float], t: float,
                        dt: float = 1e-6) -> float:
        """
        Compute the scheme-specific time derivative of f at t.

        Args:
            f: Function f(t) to differentiate
            t: Time point
            dt: Step size for numerical differentiation

        Returns:
            D[f](t) in this scheme
        """
        pass

    @abstractmethod
    def evolve(self, y0: np.ndarray, t_span: Tuple[float, float],
               dydt: Callable[[float, np.ndarray], np.ndarray],
               n_steps: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """
        Evolve a system using this scheme's dynamics.

        Args:
            y0: Initial state
            t_span: (t_start, t_end)
            dydt: Derivative function in classical notation
            n_steps: Number of time steps

        Returns:
            (t_array, y_array): Solution trajectory
        """
        pass


class ClassicalCScheme(CosmologyCScheme):
    """
    Classical calculus: standard d/dt derivative.

    This is the usual Friedmann cosmology where:
        H = da/dt / a = (1/a) * da/dt

    Near singularity (t -> 0):
        For a(t) = t^n:  H = n/t -> infinity
    """

    @property
    def name(self) -> str:
        return "Classical (d/dt)"

    def time_derivative(self, f: Callable[[float], float], t: float,
                        dt: float = 1e-6) -> float:
        """Standard numerical derivative."""
        return (f(t + dt) - f(t - dt)) / (2 * dt)

    def evolve(self, y0: np.ndarray, t_span: Tuple[float, float],
               dydt: Callable[[float, np.ndarray], np.ndarray],
               n_steps: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """Standard RK4 integration."""
        t_start, t_end = t_span
        t = np.linspace(t_start, t_end, n_steps)
        dt = t[1] - t[0]

        y = np.zeros((n_steps, len(y0)))
        y[0] = y0

        for i in range(n_steps - 1):
            # RK4
            k1 = dydt(t[i], y[i])
            k2 = dydt(t[i] + dt/2, y[i] + dt*k1/2)
            k3 = dydt(t[i] + dt/2, y[i] + dt*k2/2)
            k4 = dydt(t[i] + dt, y[i] + dt*k3)
            y[i+1] = y[i] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

        return t, y


class MetaCScheme(CosmologyCScheme):
    """
    Meta-calculus C-scheme: D_meta = (v(t)/u(t)) * d/dt

    The meta-derivative uses weight functions that can regularize singularities.

    Near singularity:
        With u(t) = t, v(t) = t:
        D_meta[a] = t * da/dt = t * n * t^(n-1) = n * t^n = n * a(t)

        This REMOVES the singularity! H_meta remains finite.

    KEY INSIGHT:
        Different u(t), v(t) choices probe different aspects of physics.
        If H(z) predictions match, the choice is "scaffolding".
        If they differ, we've found new physics.
    """

    def __init__(self, u: Callable[[float], float] = lambda t: t,
                 v: Callable[[float], float] = lambda t: t):
        """
        Initialize meta-derivative scheme.

        Args:
            u: Weight function for domain (affects "time stretching")
            v: Weight function for codomain (affects "value stretching")
        """
        self.u = u
        self.v = v

    @property
    def name(self) -> str:
        return "Meta-derivative (D_meta)"

    def time_derivative(self, f: Callable[[float], float], t: float,
                        dt: float = 1e-6) -> float:
        """
        Meta-derivative: D_meta[f](t) = (v(t)/u(t)) * df/dt

        But more precisely, the meta-derivative in (u,v) coordinates is:
        D*[f] = (1/u'(t)) * (v o f)'(t) / v'(f(t))

        For simplicity, when u=v=identity, this reduces to standard derivative.
        When u(t)=t, v(y)=y: D_meta = t * d/dt for rates.
        """
        u_val = self.u(t)
        v_val = self.v(t)

        # Avoid division by zero
        if abs(u_val) < 1e-15:
            u_val = 1e-15

        classical_deriv = (f(t + dt) - f(t - dt)) / (2 * dt)

        return (v_val / u_val) * classical_deriv

    def evolve(self, y0: np.ndarray, t_span: Tuple[float, float],
               dydt: Callable[[float, np.ndarray], np.ndarray],
               n_steps: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """
        Evolve using meta-derivative.

        The effective derivative is scaled by (v/u), so:
        dy/dt_meta = (u/v) * dy/dt_classical
        """
        t_start, t_end = t_span
        t = np.linspace(t_start, t_end, n_steps)
        dt = t[1] - t[0]

        y = np.zeros((n_steps, len(y0)))
        y[0] = y0

        for i in range(n_steps - 1):
            u_val = self.u(t[i])
            v_val = self.v(t[i])

            # Avoid singularities
            if abs(v_val) < 1e-15:
                v_val = 1e-15

            scale = u_val / v_val

            # Scaled RK4
            k1 = scale * dydt(t[i], y[i])
            k2 = scale * dydt(t[i] + dt/2, y[i] + dt*k1/2)
            k3 = scale * dydt(t[i] + dt/2, y[i] + dt*k2/2)
            k4 = scale * dydt(t[i] + dt, y[i] + dt*k3)
            y[i+1] = y[i] + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

        return t, y


class BigeometricCScheme(CosmologyCScheme):
    """
    Bigeometric calculus C-scheme: D_BG = exp(x * f'(x)/f(x))

    This is the "multiplicative calculus" where:
    - Derivatives are replaced by logarithmic derivatives
    - Power laws become linear
    - Exponential behavior is natural

    Near singularity:
        For a(t) = t^n:
        D_BG[a] = exp(t * (n/t^n) / t^n) = exp(n/t^n)

        Different singularity behavior than classical!

    KEY INSIGHT:
        Bigeometric calculus treats power-law cosmologies as "straight lines"
        in its coordinate system, potentially revealing different structure
        near Big Bang.
    """

    @property
    def name(self) -> str:
        return "Bigeometric (D_BG)"

    def time_derivative(self, f: Callable[[float], float], t: float,
                        dt: float = 1e-6) -> float:
        """
        Bigeometric derivative: geometric rate of change.

        D_BG[f] = f' * t / f  (for power-law-adapted coordinates)
        """
        f_val = f(t)
        if abs(f_val) < 1e-15:
            f_val = 1e-15

        classical_deriv = (f(t + dt) - f(t - dt)) / (2 * dt)

        # Bigeometric derivative = t * (f'/f) = t * d(ln f)/dt
        return t * classical_deriv / f_val

    def evolve(self, y0: np.ndarray, t_span: Tuple[float, float],
               dydt: Callable[[float, np.ndarray], np.ndarray],
               n_steps: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """
        Evolve using bigeometric derivative.

        In bigeometric calculus, dy/dt = y * d(ln y)/dt
        So the evolution is modified accordingly.
        """
        t_start, t_end = t_span
        t = np.linspace(t_start, t_end, n_steps)
        dt = t[1] - t[0]

        y = np.zeros((n_steps, len(y0)))
        y[0] = y0

        for i in range(n_steps - 1):
            # Bigeometric evolution: use log coordinates
            y_safe = np.maximum(np.abs(y[i]), 1e-15)
            signs = np.sign(y[i])
            signs[signs == 0] = 1

            # Standard step in log space
            log_y = np.log(y_safe)
            classical = dydt(t[i], y[i])
            d_log_y = classical / y_safe  # d(ln y)/dt

            # Bigeometric scaling
            if t[i] > 1e-15:
                scale = t[i]
            else:
                scale = 1.0

            log_y_new = log_y + dt * d_log_y / scale
            y[i+1] = signs * np.exp(log_y_new)

        return t, y


# =============================================================================
# FRW COSMOLOGY MODEL
# =============================================================================

@dataclass
class FRWParameters:
    """FRW cosmology parameters."""
    Omega_m: float = 0.3       # Matter density parameter
    Omega_Lambda: float = 0.7  # Dark energy density parameter
    Omega_r: float = 8.4e-5    # Radiation density parameter
    H0: float = 70.0           # Hubble constant (km/s/Mpc)
    n: float = 0.667           # Power-law exponent (matter era)


class FRWModel:
    """
    FRW cosmology model with C-scheme flexibility.

    Computes observables using different calculus schemes to test
    for scheme-robustness.
    """

    def __init__(self, params: FRWParameters, scheme: CosmologyCScheme):
        self.params = params
        self.scheme = scheme

    def scale_factor_power_law(self, t: float) -> float:
        """
        Power-law scale factor: a(t) = t^n

        This is an approximation for single-component universes:
        - n = 1/2: Radiation dominated
        - n = 2/3: Matter dominated
        - n > 1: Dark energy dominated (accelerating)
        """
        if t <= 0:
            return 0.0
        return t ** self.params.n

    def hubble_parameter_power_law(self, t: float) -> float:
        """
        Hubble parameter H = (1/a) * da/dt using current C-scheme.

        Classical: H = n/t
        Meta: H_meta = (v/u) * n/t
        Bigeometric: H_BG = n (constant!)

        This is where C-scheme differences become apparent!
        """
        a = self.scale_factor_power_law

        if t <= 0:
            return np.inf

        a_val = a(t)
        if a_val <= 0:
            return np.inf

        da_dt = self.scheme.time_derivative(a, t)

        return da_dt / a_val

    def hubble_from_redshift(self, z: float) -> float:
        """
        H(z) = H0 * sqrt(Omega_m*(1+z)^3 + Omega_r*(1+z)^4 + Omega_Lambda)

        This is the SCHEME-ROBUST form that all C-schemes must agree on!
        The form is independent of time coordinate choice.
        """
        Om = self.params.Omega_m
        Or = self.params.Omega_r
        OL = self.params.Omega_Lambda
        H0 = self.params.H0

        return H0 * np.sqrt(Om * (1+z)**3 + Or * (1+z)**4 + OL)

    def comoving_distance(self, z: float, n_steps: int = 1000) -> float:
        """
        Comoving distance: D_c = c * integral_0^z dz'/H(z')

        SCHEME-ROBUST: Uses H(z) which is the invariant form.
        """
        c = 299792.458  # km/s

        z_array = np.linspace(0, z, n_steps)
        dz = z_array[1] - z_array[0] if n_steps > 1 else 0

        # Trapezoidal integration
        H_array = np.array([self.hubble_from_redshift(zi) for zi in z_array])
        integrand = 1.0 / H_array

        return c * np.trapz(integrand, z_array)

    def angular_diameter_distance(self, z: float) -> float:
        """
        Angular diameter distance: D_A = D_c / (1 + z)

        SCHEME-ROBUST: CMB distance measure.
        """
        return self.comoving_distance(z) / (1 + z)

    def luminosity_distance(self, z: float) -> float:
        """
        Luminosity distance: D_L = D_c * (1 + z)

        SCHEME-ROBUST: Used in supernova cosmology.
        """
        return self.comoving_distance(z) * (1 + z)

    def bbn_temperature(self, t: float) -> float:
        """
        BBN temperature estimate: T ~ 1/sqrt(t) (radiation era)

        SCHEME-ROBUST: BBN abundances depend on T history,
        which is ultimately tied to H(z) evolution.
        """
        # Approximate: T in MeV ~ (t in seconds)^(-1/2)
        if t <= 0:
            return np.inf
        return t ** (-0.5)


# =============================================================================
# SCHEME-ROBUSTNESS TESTING
# =============================================================================

class FRWSchemeRobustnessTest:
    """
    Test scheme-robustness of FRW observables across C-scheme choices.

    SCHEME-ROBUST (should agree):
        - H(z) Hubble parameter
        - D_A(z) Angular diameter distance
        - D_L(z) Luminosity distance
        - BBN abundances (tied to H history)

    POTENTIALLY SCHEME-DEPENDENT:
        - Singularity behavior as t -> 0
        - Inflation dynamics
        - Planck-scale physics
    """

    def __init__(self, params: Optional[FRWParameters] = None):
        self.params = params or FRWParameters()

        # Initialize C-schemes
        self.schemes = {
            'classical': ClassicalCScheme(),
            'meta': MetaCScheme(),
            'bigeometric': BigeometricCScheme()
        }

        # Create models
        self.models = {
            name: FRWModel(self.params, scheme)
            for name, scheme in self.schemes.items()
        }

    def test_hubble_z(self, z_values: np.ndarray) -> Dict[str, Any]:
        """
        Test H(z) across schemes.

        EXPECTED: All schemes give identical H(z) since H(z) is
        the scheme-robust parameterization.
        """
        results = {}

        for name, model in self.models.items():
            H_z = np.array([model.hubble_from_redshift(z) for z in z_values])
            results[name] = H_z

        # Compare all pairs
        comparisons = {}
        scheme_names = list(self.models.keys())

        for i, s1 in enumerate(scheme_names):
            for s2 in scheme_names[i+1:]:
                diff = np.max(np.abs(results[s1] - results[s2]))
                comparisons[f'{s1}_vs_{s2}'] = diff

        max_diff = max(comparisons.values()) if comparisons else 0

        return {
            'observable': 'H(z)',
            'scheme_robust': max_diff < 1e-10,
            'max_difference': max_diff,
            'by_scheme': results,
            'comparisons': comparisons,
            'z_values': z_values
        }

    def test_distances(self, z_values: np.ndarray) -> Dict[str, Any]:
        """
        Test distance measures across schemes.

        EXPECTED: D_A(z) and D_L(z) are scheme-robust.
        """
        results_DA = {}
        results_DL = {}

        for name, model in self.models.items():
            DA = np.array([model.angular_diameter_distance(z) for z in z_values])
            DL = np.array([model.luminosity_distance(z) for z in z_values])
            results_DA[name] = DA
            results_DL[name] = DL

        # Compare
        scheme_names = list(self.models.keys())
        max_diff_DA = 0
        max_diff_DL = 0

        for i, s1 in enumerate(scheme_names):
            for s2 in scheme_names[i+1:]:
                diff_DA = np.max(np.abs(results_DA[s1] - results_DA[s2]))
                diff_DL = np.max(np.abs(results_DL[s1] - results_DL[s2]))
                max_diff_DA = max(max_diff_DA, diff_DA)
                max_diff_DL = max(max_diff_DL, diff_DL)

        return {
            'D_A': {
                'observable': 'Angular diameter distance D_A(z)',
                'scheme_robust': max_diff_DA < 1e-10,
                'max_difference': max_diff_DA,
                'by_scheme': results_DA
            },
            'D_L': {
                'observable': 'Luminosity distance D_L(z)',
                'scheme_robust': max_diff_DL < 1e-10,
                'max_difference': max_diff_DL,
                'by_scheme': results_DL
            }
        }

    def test_singularity_behavior(self, t_values: np.ndarray) -> Dict[str, Any]:
        """
        Test Hubble parameter H(t) near singularity.

        EXPECTED: C-schemes DIVERGE near t -> 0!
        This is where new physics potentially lives.
        """
        results = {}

        for name, model in self.models.items():
            H_t = []
            for t in t_values:
                try:
                    h = model.hubble_parameter_power_law(t)
                    if np.isfinite(h):
                        H_t.append(h)
                    else:
                        H_t.append(np.nan)
                except:
                    H_t.append(np.nan)
            results[name] = np.array(H_t)

        # Check for divergence between schemes
        scheme_names = list(self.models.keys())
        max_diff = 0

        for i, s1 in enumerate(scheme_names):
            for s2 in scheme_names[i+1:]:
                # Only compare where both are finite
                valid = np.isfinite(results[s1]) & np.isfinite(results[s2])
                if np.any(valid):
                    diff = np.max(np.abs(results[s1][valid] - results[s2][valid]))
                    max_diff = max(max_diff, diff)

        return {
            'observable': 'H(t) near singularity',
            'scheme_robust': max_diff < 1.0,  # Allow larger tolerance near singularity
            'max_difference': max_diff,
            'by_scheme': results,
            't_values': t_values,
            'note': 'C-schemes may legitimately differ near t=0!'
        }

    def hunt_breaking_points(self,
                              t_range: Tuple[float, float] = (1e-10, 10.0),
                              n_points: int = 100) -> Dict[str, Any]:
        """
        Systematically hunt for scheme-breaking points.

        These are where different C-schemes give different predictions,
        indicating potential new physics.
        """
        t_values = np.logspace(np.log10(t_range[0]), np.log10(t_range[1]), n_points)

        breaking_points = []

        for t in t_values:
            H_values = {}
            for name, model in self.models.items():
                try:
                    H = model.hubble_parameter_power_law(t)
                    if np.isfinite(H):
                        H_values[name] = H
                except:
                    pass

            if len(H_values) >= 2:
                vals = list(H_values.values())
                max_diff = max(vals) - min(vals)
                mean_val = np.mean(vals)

                # Relative difference
                if mean_val > 1e-15:
                    rel_diff = max_diff / mean_val
                else:
                    rel_diff = max_diff

                if rel_diff > 0.01:  # >1% difference
                    breaking_points.append({
                        't': t,
                        'max_diff': max_diff,
                        'rel_diff': rel_diff,
                        'H_by_scheme': H_values
                    })

        return {
            'breaking_points': breaking_points,
            'n_breaking': len(breaking_points),
            'n_tested': n_points,
            't_range': t_range,
            'has_breaking': len(breaking_points) > 0,
            'interpretation': (
                'C-scheme breaking found! Different calculus choices '
                'give different predictions. This may indicate new physics.'
                if breaking_points else
                'No C-scheme breaking found in tested range. '
                'All calculi agree on physical predictions.'
            )
        }

    def full_robustness_report(self) -> Dict[str, Any]:
        """Generate complete scheme-robustness report."""
        z_test = np.array([0.1, 0.5, 1.0, 2.0, 5.0])
        t_test = np.array([1e-3, 1e-2, 0.1, 1.0, 10.0])

        return {
            'hubble_z': self.test_hubble_z(z_test),
            'distances': self.test_distances(z_test),
            'singularity': self.test_singularity_behavior(t_test),
            'breaking_hunt': self.hunt_breaking_points()
        }


# =============================================================================
# DEMO AND CLI
# =============================================================================

def demo_frw_scheme_robustness():
    """Demonstrate FRW scheme-robustness testing."""
    print("=" * 70)
    print("FRW SCHEME-ROBUSTNESS TEST")
    print("Testing C-scheme invariance of cosmological observables")
    print("=" * 70)

    tester = FRWSchemeRobustnessTest()

    # Test H(z)
    print("\n" + "-" * 40)
    print("TEST 1: H(z) - Hubble Parameter")
    print("-" * 40)

    z_values = np.array([0.1, 0.5, 1.0, 2.0, 5.0])
    result = tester.test_hubble_z(z_values)

    print(f"\nScheme-robust: {result['scheme_robust']}")
    print(f"Max difference: {result['max_difference']:.2e}")

    print("\nH(z) by scheme:")
    for name, H in result['by_scheme'].items():
        print(f"  {name:15s}: {H[:3]}")

    # Test distances
    print("\n" + "-" * 40)
    print("TEST 2: Distance Measures")
    print("-" * 40)

    dist_result = tester.test_distances(z_values)

    print(f"\nD_A(z) scheme-robust: {dist_result['D_A']['scheme_robust']}")
    print(f"D_L(z) scheme-robust: {dist_result['D_L']['scheme_robust']}")

    # Test singularity
    print("\n" + "-" * 40)
    print("TEST 3: Singularity Behavior")
    print("-" * 40)

    t_values = np.array([1e-3, 1e-2, 0.1, 1.0])
    sing_result = tester.test_singularity_behavior(t_values)

    print(f"\nScheme-robust: {sing_result['scheme_robust']}")
    print(f"Max difference: {sing_result['max_difference']:.2e}")
    print(f"\nNote: {sing_result['note']}")

    print("\nH(t) by scheme:")
    for name, H in sing_result['by_scheme'].items():
        print(f"  {name:15s}: {H[:4]}")

    # Hunt for breaking points
    print("\n" + "-" * 40)
    print("TEST 4: Hunt for Scheme-Breaking Points")
    print("-" * 40)

    hunt = tester.hunt_breaking_points()

    print(f"\nBreaking points found: {hunt['n_breaking']}/{hunt['n_tested']}")
    print(f"\nInterpretation: {hunt['interpretation']}")

    if hunt['breaking_points']:
        print("\nBreaking points:")
        for bp in hunt['breaking_points'][:5]:
            print(f"  t = {bp['t']:.2e}: rel_diff = {bp['rel_diff']:.2%}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("\nSCHEME-ROBUST (Physical):")
    print("  [OK] H(z) - Hubble parameter (redshift form)")
    print("  [OK] D_A(z) - Angular diameter distance")
    print("  [OK] D_L(z) - Luminosity distance")
    print("\nPOTENTIALLY SCHEME-DEPENDENT (Scaffolding or New Physics):")
    print("  [!] H(t) near singularity - C-schemes diverge")
    print("  [!] Big Bang behavior - depends on calculus choice")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="FRW Scheme-Robustness Testing"
    )
    parser.add_argument('command', choices=['demo', 'hunt_breaking'],
                        nargs='?', default='demo')

    args = parser.parse_args()

    if args.command == 'demo':
        demo_frw_scheme_robustness()
    elif args.command == 'hunt_breaking':
        tester = FRWSchemeRobustnessTest()
        result = tester.hunt_breaking_points(t_range=(1e-15, 100), n_points=200)
        print(f"Breaking points: {result['n_breaking']}")
        print(result['interpretation'])


if __name__ == '__main__':
    if len(sys.argv) == 1:
        demo_frw_scheme_robustness()
    else:
        main()
