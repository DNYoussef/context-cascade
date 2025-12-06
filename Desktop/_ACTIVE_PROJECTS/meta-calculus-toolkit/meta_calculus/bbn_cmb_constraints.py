#!/usr/bin/env python3
"""
BBN and CMB Constraints on Meta-Friedmann Parameter k

This module analyzes observational constraints on the meta-weight
parameter k from Big Bang Nucleosynthesis and CMB observations.

KEY PHYSICS:
  - BBN occurs at t ~ 1-1000 seconds, T ~ 0.1-10 MeV
  - CMB decoupling at t ~ 380,000 years, T ~ 0.26 eV
  - Both are sensitive to expansion rate H(t) and density rho(t)

META-FRIEDMANN EFFECTS:
  - Expansion exponent: n = (2/3) * (1-k) / (1+w)
  - Density exponent: m = 2 - 2k
  - rho(t) ~ t^(-m)

CONSTRAINTS:
  - BBN: Helium-4 abundance Y_p ~ 0.245 +/- 0.003
  - BBN: Deuterium D/H ~ 2.5e-5
  - CMB: Acoustic peak positions
  - CMB: Damping tail

Usage:
    python -m meta_calculus.bbn_cmb_constraints analyze
    python -m meta_calculus.bbn_cmb_constraints bounds --sigma 2
    python -m meta_calculus.bbn_cmb_constraints phase-transition
"""

import numpy as np
from typing import Tuple, Dict, List, Optional
import argparse
import sys


# =============================================================================
# PHYSICAL CONSTANTS (natural units where applicable)
# =============================================================================

# Temperatures in MeV
T_BBN_START = 10.0      # MeV - weak freeze-out
T_BBN_END = 0.01        # MeV - end of nucleosynthesis
T_CMB = 0.26e-3         # MeV (0.26 eV) - CMB decoupling

# Times (approximate, radiation dominated)
# t ~ 1 second at T ~ 1 MeV
T_1_MEV_TIME = 1.0      # seconds

# Observed abundances
Y_P_OBSERVED = 0.245    # Helium-4 mass fraction
Y_P_ERROR = 0.003       # 1-sigma error
D_H_OBSERVED = 2.5e-5   # Deuterium to hydrogen ratio
D_H_ERROR = 0.3e-5      # 1-sigma error

# Radiation equation of state
W_RADIATION = 1.0 / 3.0


# =============================================================================
# META-FRIEDMANN COSMOLOGY
# =============================================================================

class MetaFriedmannBBN:
    """
    Meta-Friedmann cosmology for BBN analysis.

    In meta-Friedmann with weight W(t) = t^k:
      n = (2/3) * (1-k) / (1+w)
      m = 2 - 2k
      rho ~ t^(-m)
      H = n/t

    For radiation (w = 1/3):
      n = (1/2) * (1-k)
      m = 2 - 2k
    """

    def __init__(self, k: float):
        """
        Initialize with meta-weight exponent.

        Args:
            k: Meta-weight exponent (k=0 is classical)
        """
        self.k = k
        self.w = W_RADIATION
        self.n = self.expansion_exponent()
        self.m = self.density_exponent()

    def expansion_exponent(self) -> float:
        """n = (2/3) * (1-k) / (1+w) for radiation: n = (1-k)/2."""
        return (2.0 / 3.0) * (1.0 - self.k) / (1.0 + self.w)

    def density_exponent(self) -> float:
        """m = 2 - 2k."""
        return 2.0 - 2.0 * self.k

    def hubble_ratio(self, k_ref: float = 0.0) -> float:
        """
        Ratio of Hubble parameter to classical (k=0).

        H(k) / H(0) = n(k) / n(0) = (1-k)

        For k > 0: expansion is SLOWER
        For k < 0: expansion is FASTER
        """
        n_classical = 0.5  # radiation, k=0
        return self.n / n_classical

    def density_ratio_at_fixed_T(self, k_ref: float = 0.0) -> float:
        """
        Ratio of density at fixed temperature.

        Since T ~ 1/a and a ~ t^n, we have t ~ T^(-1/n).
        At fixed T: rho(k) / rho(0) = (t(k)/t(0))^(-m(k)+m(0))

        This is complex; simplified version assumes t is the same.
        """
        # At same cosmic time:
        # rho(k)/rho(0) = t^(-m(k)) / t^(-m(0)) = t^(m(0)-m(k)) = t^(2k)
        # At BBN (t ~ 1 sec), this gives ~ 1 for small k
        return 1.0  # First order, more detailed below

    def freeze_out_temperature_shift(self) -> float:
        """
        Estimate shift in weak freeze-out temperature.

        Freeze-out occurs when Gamma_weak ~ H.
        Gamma_weak ~ G_F^2 T^5
        H ~ T^2 / M_Pl (in classical)

        With meta-Friedmann, H is modified by factor (1-k).
        Freeze-out: T_f^3 ~ H / G_F^2 ~ (1-k) * T^2 / M_Pl / G_F^2

        Leading to: T_f(k) / T_f(0) ~ (1-k)^(1/3)
        """
        if self.k >= 1:
            return 0.0  # No freeze-out in static universe
        return (1.0 - self.k) ** (1.0 / 3.0)

    def helium_abundance_estimate(self) -> float:
        """
        Estimate Helium-4 abundance Y_p.

        Y_p depends on neutron-to-proton ratio at freeze-out:
        n/p ~ exp(-Delta_m / T_f)

        where Delta_m ~ 1.3 MeV is the neutron-proton mass difference.

        Higher T_f -> more neutrons -> more He-4
        Lower T_f -> fewer neutrons -> less He-4

        Classical Y_p ~ 0.245 corresponds to T_f ~ 0.8 MeV.
        """
        # Classical freeze-out temperature
        T_f_classical = 0.8  # MeV

        # Meta-modified freeze-out
        T_f_ratio = self.freeze_out_temperature_shift()
        T_f_meta = T_f_classical * T_f_ratio

        if T_f_meta <= 0:
            return 0.0

        # Neutron-proton mass difference
        delta_m = 1.293  # MeV

        # n/p ratio at freeze-out
        np_ratio_classical = np.exp(-delta_m / T_f_classical)
        np_ratio_meta = np.exp(-delta_m / T_f_meta)

        # Y_p ~ 2 * (n/p) / (1 + n/p) for complete conversion
        # Simplified: Y_p ~ 2 * n/p for small n/p
        Y_p_classical = 0.245

        # Scale by ratio of n/p
        Y_p_meta = Y_p_classical * (np_ratio_meta / np_ratio_classical)

        # Clamp to physical range
        return max(0.0, min(1.0, Y_p_meta))

    def expansion_rate_during_bbn(self) -> float:
        """
        Expansion rate factor during BBN relative to classical.

        H(k) / H(0) = (1-k) at fixed cosmic time
        """
        return 1.0 - self.k


# =============================================================================
# CONSTRAINT ANALYSIS
# =============================================================================

class BBNConstraints:
    """
    Analyze BBN constraints on meta-weight k.
    """

    def __init__(self):
        """Initialize with observed values."""
        self.Y_p_obs = Y_P_OBSERVED
        self.Y_p_err = Y_P_ERROR
        self.D_H_obs = D_H_OBSERVED
        self.D_H_err = D_H_ERROR

    def chi_squared_helium(self, k: float) -> float:
        """
        Chi-squared for Helium-4 abundance.

        Args:
            k: Meta-weight exponent

        Returns:
            Chi-squared value
        """
        model = MetaFriedmannBBN(k)
        Y_p_pred = model.helium_abundance_estimate()

        chi2 = ((Y_p_pred - self.Y_p_obs) / self.Y_p_err) ** 2
        return chi2

    def chi_squared_expansion(self, k: float) -> float:
        """
        Chi-squared from expansion rate constraint.

        BBN constrains |delta_H / H| < 0.1 (roughly).
        delta_H / H = -k for meta-Friedmann.
        """
        # Constraint: |k| < 0.1 at 2-sigma
        k_limit = 0.1
        k_err = k_limit / 2.0  # 2-sigma

        chi2 = (k / k_err) ** 2
        return chi2

    def total_chi_squared(self, k: float) -> float:
        """Total chi-squared from all BBN constraints."""
        chi2_He = self.chi_squared_helium(k)
        chi2_H = self.chi_squared_expansion(k)
        return chi2_He + chi2_H

    def find_bounds(self, sigma: float = 2.0) -> Tuple[float, float]:
        """
        Find bounds on k at given sigma level.

        Args:
            sigma: Number of standard deviations

        Returns:
            (k_min, k_max) bounds
        """
        # Delta chi2 for given sigma (1 parameter)
        delta_chi2 = sigma ** 2

        # Scan k values
        k_values = np.linspace(-0.5, 0.5, 1000)
        chi2_values = [self.total_chi_squared(k) for k in k_values]

        # Find minimum
        chi2_min = min(chi2_values)
        k_best = k_values[chi2_values.index(chi2_min)]

        # Find bounds where chi2 = chi2_min + delta_chi2
        threshold = chi2_min + delta_chi2

        k_allowed = [k for k, chi2 in zip(k_values, chi2_values) if chi2 <= threshold]

        if len(k_allowed) == 0:
            return (0.0, 0.0)

        return (min(k_allowed), max(k_allowed))

    def summary(self, sigma: float = 2.0) -> Dict:
        """Generate summary of BBN constraints."""
        k_min, k_max = self.find_bounds(sigma)

        # Best fit (minimum chi2)
        k_values = np.linspace(-0.3, 0.3, 100)
        chi2_values = [self.total_chi_squared(k) for k in k_values]
        k_best = k_values[np.argmin(chi2_values)]
        chi2_best = min(chi2_values)

        return {
            'k_best': k_best,
            'chi2_min': chi2_best,
            'k_min': k_min,
            'k_max': k_max,
            'sigma': sigma,
            'constraint': f'{k_min:.3f} < k < {k_max:.3f} ({sigma:.0f}-sigma)',
        }


class CMBConstraints:
    """
    Analyze CMB constraints on meta-weight k.

    CMB is sensitive to:
    1. Expansion history (affects acoustic peak positions)
    2. Matter-radiation equality (affects peak heights)
    3. Damping scale (affects small-scale power)
    """

    def __init__(self):
        """Initialize CMB constraint analysis."""
        # Acoustic scale constraint
        # theta_* = r_s(z_*) / D_A(z_*)
        # Planck measures theta_* to 0.03%
        self.theta_rel_err = 0.0003

        # Effective number of relativistic species
        # N_eff = 3.046 +/- 0.2
        self.N_eff_obs = 3.046
        self.N_eff_err = 0.2

    def delta_N_eff_from_k(self, k: float) -> float:
        """
        Effective change in N_eff from meta-weight k.

        Modified expansion rate H(k) = (1-k) * H(0) can be
        recast as change in radiation content:

        H^2 ~ rho_rad ~ N_eff

        So: delta_N_eff / N_eff ~ 2 * delta_H / H = -2k
        """
        return -2.0 * k * self.N_eff_obs

    def chi_squared_N_eff(self, k: float) -> float:
        """Chi-squared from N_eff constraint."""
        delta_N = self.delta_N_eff_from_k(k)
        chi2 = (delta_N / self.N_eff_err) ** 2
        return chi2

    def acoustic_scale_shift(self, k: float) -> float:
        """
        Relative shift in acoustic scale from meta-weight.

        theta_* depends on integral of c_s / H from early times.
        Modified H -> modified theta_*.

        Roughly: delta_theta / theta ~ -k * (some order-1 factor)
        """
        # Simplified: acoustic scale shifts proportionally to k
        return -k * 0.5  # Order of magnitude estimate

    def chi_squared_acoustic(self, k: float) -> float:
        """Chi-squared from acoustic scale constraint."""
        delta_theta = self.acoustic_scale_shift(k)
        chi2 = (delta_theta / self.theta_rel_err) ** 2
        return chi2

    def total_chi_squared(self, k: float) -> float:
        """Total chi-squared from CMB constraints."""
        return self.chi_squared_N_eff(k) + self.chi_squared_acoustic(k)

    def find_bounds(self, sigma: float = 2.0) -> Tuple[float, float]:
        """Find bounds on k from CMB at given sigma level."""
        delta_chi2 = sigma ** 2

        k_values = np.linspace(-0.2, 0.2, 1000)
        chi2_values = [self.total_chi_squared(k) for k in k_values]

        chi2_min = min(chi2_values)
        threshold = chi2_min + delta_chi2

        k_allowed = [k for k, chi2 in zip(k_values, chi2_values) if chi2 <= threshold]

        if len(k_allowed) == 0:
            return (0.0, 0.0)

        return (min(k_allowed), max(k_allowed))

    def summary(self, sigma: float = 2.0) -> Dict:
        """Generate summary of CMB constraints."""
        k_min, k_max = self.find_bounds(sigma)

        return {
            'k_min': k_min,
            'k_max': k_max,
            'sigma': sigma,
            'constraint': f'{k_min:.4f} < k < {k_max:.4f} ({sigma:.0f}-sigma)',
            'note': 'CMB provides tighter constraints than BBN',
        }


class CombinedConstraints:
    """Combined BBN + CMB constraints on k."""

    def __init__(self):
        """Initialize combined analysis."""
        self.bbn = BBNConstraints()
        self.cmb = CMBConstraints()

    def total_chi_squared(self, k: float) -> float:
        """Combined chi-squared."""
        return self.bbn.total_chi_squared(k) + self.cmb.total_chi_squared(k)

    def find_bounds(self, sigma: float = 2.0) -> Tuple[float, float]:
        """Find combined bounds on k."""
        delta_chi2 = sigma ** 2

        k_values = np.linspace(-0.1, 0.1, 1000)
        chi2_values = [self.total_chi_squared(k) for k in k_values]

        chi2_min = min(chi2_values)
        threshold = chi2_min + delta_chi2

        k_allowed = [k for k, chi2 in zip(k_values, chi2_values) if chi2 <= threshold]

        if len(k_allowed) == 0:
            return (0.0, 0.0)

        return (min(k_allowed), max(k_allowed))

    def summary(self, sigma: float = 2.0) -> Dict:
        """Generate combined summary."""
        k_min, k_max = self.find_bounds(sigma)

        bbn_summary = self.bbn.summary(sigma)
        cmb_summary = self.cmb.summary(sigma)

        return {
            'combined': {
                'k_min': k_min,
                'k_max': k_max,
                'sigma': sigma,
                'constraint': f'{k_min:.4f} < k < {k_max:.4f} ({sigma:.0f}-sigma)',
            },
            'bbn': bbn_summary,
            'cmb': cmb_summary,
            'interpretation': self._interpret(k_min, k_max),
        }

    def _interpret(self, k_min: float, k_max: float) -> str:
        """Interpret the constraint."""
        if k_max < 0.01:
            return "k must be very close to 0; classical GR preferred"
        elif k_max < 0.05:
            return "Small deviations allowed; marginal singularity softening possible"
        elif k_max < 0.1:
            return "Moderate k allowed; significant early-universe modification possible"
        else:
            return "Large k allowed; major departures from classical cosmology possible"


# =============================================================================
# PHASE TRANSITION ANALYSIS
# =============================================================================

class PhaseTransition:
    """
    Analyze phase transition from meta-phase (k > 0) to classical (k = 0).

    Scenario: Early universe has k > 0 (singularity softening),
    transitions to k = 0 (classical) before BBN.
    """

    def __init__(self, k_early: float, T_transition: float):
        """
        Initialize phase transition model.

        Args:
            k_early: Meta-weight in early phase
            T_transition: Temperature of transition (MeV)
        """
        self.k_early = k_early
        self.T_transition = T_transition

    def k_of_T(self, T: float) -> float:
        """
        k as function of temperature.

        Simple model: step function at T_transition.
        Could be smoothed for more realistic treatment.
        """
        if T > self.T_transition:
            return self.k_early
        else:
            return 0.0

    def k_of_T_smooth(self, T: float, width: float = 0.1) -> float:
        """
        Smoothed transition using tanh.

        Args:
            T: Temperature (MeV)
            width: Width of transition (in log T)
        """
        x = np.log(T / self.T_transition) / width
        # Interpolate from k_early (high T) to 0 (low T)
        return self.k_early * 0.5 * (1.0 + np.tanh(x))

    def is_bbn_safe(self) -> bool:
        """Check if transition happens before BBN."""
        return self.T_transition > T_BBN_START

    def early_density_behavior(self) -> str:
        """Describe early-time density behavior."""
        m_early = 2.0 - 2.0 * self.k_early

        if m_early > 0:
            return f"rho ~ t^(-{m_early:.2f}) (still diverges, but weaker)"
        elif m_early == 0:
            return "rho = constant (NO SINGULARITY)"
        else:
            return f"rho ~ t^({-m_early:.2f}) (vanishes at t=0)"

    def summary(self) -> Dict:
        """Summarize phase transition scenario."""
        return {
            'k_early': self.k_early,
            'k_late': 0.0,
            'T_transition': self.T_transition,
            'T_transition_MeV': f'{self.T_transition:.1f} MeV',
            'bbn_safe': self.is_bbn_safe(),
            'early_behavior': self.early_density_behavior(),
            'late_behavior': 'Classical GR (k=0)',
            'viable': self.is_bbn_safe(),
        }


# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_analyze(args):
    """Analyze BBN/CMB constraints on k."""
    print("=" * 70)
    print("BBN AND CMB CONSTRAINTS ON META-WEIGHT k")
    print("=" * 70)

    print("\n  META-FRIEDMANN COSMOLOGY:")
    print("    Expansion exponent: n = (1-k)/2  (radiation)")
    print("    Density exponent:   m = 2 - 2k")
    print("    Density:            rho ~ t^(-m)")

    print("\n  BBN CONSTRAINTS:")
    bbn = BBNConstraints()
    bbn_sum = bbn.summary(sigma=2.0)
    print(f"    Best fit k: {bbn_sum['k_best']:.4f}")
    print(f"    Chi2 min:   {bbn_sum['chi2_min']:.2f}")
    print(f"    2-sigma:    {bbn_sum['constraint']}")

    print("\n  CMB CONSTRAINTS:")
    cmb = CMBConstraints()
    cmb_sum = cmb.summary(sigma=2.0)
    print(f"    2-sigma:    {cmb_sum['constraint']}")
    print(f"    Note:       {cmb_sum['note']}")

    print("\n  COMBINED CONSTRAINTS:")
    combined = CombinedConstraints()
    comb_sum = combined.summary(sigma=2.0)
    print(f"    2-sigma:    {comb_sum['combined']['constraint']}")
    print(f"    Interpretation: {comb_sum['interpretation']}")

    print("\n  SINGULARITY SOFTENING VIABILITY:")
    k_max = comb_sum['combined']['k_max']
    m_at_kmax = 2.0 - 2.0 * k_max
    print(f"    Maximum allowed k: {k_max:.4f}")
    print(f"    Density exponent at k_max: m = {m_at_kmax:.4f}")
    if k_max >= 1.0:
        print("    -> Full singularity removal (k >= 1) IS allowed")
    elif k_max > 0:
        print(f"    -> Partial softening: rho ~ t^(-{m_at_kmax:.3f}) instead of t^(-2)")
    else:
        print("    -> No softening allowed; classical k=0 required")


def cmd_bounds(args):
    """Show constraints at various sigma levels."""
    print("=" * 70)
    print("CONSTRAINT BOUNDS AT VARIOUS SIGMA LEVELS")
    print("=" * 70)

    combined = CombinedConstraints()

    print(f"\n  {'Sigma':<10} {'k_min':<12} {'k_max':<12} {'m_max':<12} {'Singularity?':<15}")
    print("  " + "-" * 60)

    for sigma in [1.0, 2.0, 3.0]:
        k_min, k_max = combined.find_bounds(sigma)
        m_max = 2.0 - 2.0 * k_max

        if k_max >= 1.0:
            sing = "REMOVED"
        elif k_max > 0.5:
            sing = "Weak (m < 1)"
        elif k_max > 0:
            sing = f"Softened (m={m_max:.2f})"
        else:
            sing = "Classical"

        print(f"  {sigma:<10.1f} {k_min:<12.4f} {k_max:<12.4f} {m_max:<12.4f} {sing:<15}")

    print("\n  PHYSICAL MEANING:")
    print("    m = 2: Classical Big Bang (rho -> infinity)")
    print("    m = 1: rho ~ 1/t (still diverges, slower)")
    print("    m = 0: rho = constant (NO SINGULARITY)")
    print("    m < 0: rho -> 0 as t -> 0")


def cmd_phase_transition(args):
    """Analyze phase transition scenarios."""
    print("=" * 70)
    print("PHASE TRANSITION SCENARIOS")
    print("Early meta-phase (k > 0) transitioning to classical (k = 0)")
    print("=" * 70)

    # Various scenarios
    scenarios = [
        (1.0, 100.0, "Full singularity removal, transition at 100 MeV"),
        (1.0, 10.0, "Full removal, transition at 10 MeV (after BBN start!)"),
        (0.5, 100.0, "Partial softening (m=1), transition at 100 MeV"),
        (0.5, 1000.0, "Partial softening, early transition at 1 GeV"),
    ]

    print(f"\n  {'k_early':<10} {'T_trans (MeV)':<15} {'BBN Safe?':<12} {'Early rho':<25}")
    print("  " + "-" * 65)

    for k_early, T_trans, description in scenarios:
        pt = PhaseTransition(k_early, T_trans)
        summary = pt.summary()

        safe = "YES" if summary['bbn_safe'] else "NO"
        early = summary['early_behavior'][:24]

        print(f"  {k_early:<10.2f} {T_trans:<15.1f} {safe:<12} {early:<25}")

    print("\n  VIABLE SCENARIOS:")
    print("    - k_early = 1.0, T_transition > 10 MeV: Singularity-free early phase")
    print("    - k_early = 0.5, T_transition > 10 MeV: Softened singularity")
    print("    - Must transition BEFORE BBN (T > 10 MeV) to preserve abundances")

    print("\n  OBSERVATIONAL SIGNATURES:")
    print("    - Primordial gravitational waves modified")
    print("    - Possible relic abundance changes")
    print("    - Modified reheating after inflation")


def cmd_helium(args):
    """Show Helium-4 abundance vs k."""
    print("=" * 70)
    print("HELIUM-4 ABUNDANCE vs META-WEIGHT k")
    print("=" * 70)

    print(f"\n  Observed: Y_p = {Y_P_OBSERVED} +/- {Y_P_ERROR}")

    print(f"\n  {'k':<10} {'Y_p':<12} {'Delta Y_p':<12} {'Sigma':<10}")
    print("  " + "-" * 45)

    for k in np.linspace(-0.2, 0.2, 9):
        model = MetaFriedmannBBN(k)
        Y_p = model.helium_abundance_estimate()
        delta = Y_p - Y_P_OBSERVED
        sigma = abs(delta) / Y_P_ERROR

        print(f"  {k:<10.2f} {Y_p:<12.4f} {delta:<+12.4f} {sigma:<10.1f}")


def main():
    parser = argparse.ArgumentParser(
        description="BBN and CMB Constraints on Meta-Friedmann",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # analyze command
    analyze_parser = subparsers.add_parser('analyze',
        help='Full constraint analysis')
    analyze_parser.set_defaults(func=cmd_analyze)

    # bounds command
    bounds_parser = subparsers.add_parser('bounds',
        help='Show bounds at various sigma levels')
    bounds_parser.set_defaults(func=cmd_bounds)

    # phase-transition command
    phase_parser = subparsers.add_parser('phase-transition',
        help='Analyze phase transition scenarios')
    phase_parser.set_defaults(func=cmd_phase_transition)

    # helium command
    helium_parser = subparsers.add_parser('helium',
        help='Show Helium abundance vs k')
    helium_parser.set_defaults(func=cmd_helium)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
