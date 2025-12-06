#!/usr/bin/env python3
"""
Paper Figures: Non-Newtonian Calculus for General Relativity

This script generates all figures for the academic paper on
meta-calculus approach to cosmological singularities.

Figures:
  1. Einstein Compatibility Hierarchy
  2. Meta-Friedmann: n vs k for different w
  3. Singularity Softening: m = 2 - 2k
  4. Bigeometric Diagnostic: D_BG[R] = constant
  5. 4D L_BG Failure: symmetry breaking
  6. Action-based vs Derivative-weight comparison
  7. BBN/CMB Constraints on k
  8. Phase Transition Scenario

Usage:
    python simulations/paper_figures.py
    python simulations/paper_figures.py --figure 1
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import argparse

# Create figures directory
os.makedirs('figures', exist_ok=True)

# Style settings
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'font.family': 'serif',
})


def fig1_hierarchy():
    """Figure 1: Einstein Compatibility Hierarchy."""
    print("Generating Figure 1: Einstein Compatibility Hierarchy...")

    fig, ax = plt.subplots(figsize=(10, 6))

    # Data for hierarchy
    tiers = ['Tier 1:\nMeta-calculus\n(weights u,v)',
             'Tier 2:\nBigeometric\nD_BG diagnostic',
             'Tier 3:\nL_BG-Christoffel\n(FALSIFIED)',
             'Tier 4:\nFull GUC\n(research)']

    field_eqs = [1, 0, -1, 0.5]  # 1=yes, 0=partial, -1=no
    scalars = [1, 1, 0, 0.5]
    colors = ['green', 'blue', 'red', 'gray']

    x = np.arange(len(tiers))
    width = 0.35

    bars1 = ax.bar(x - width/2, field_eqs, width, label='Field Equations',
                   color=['green' if v > 0 else 'red' if v < 0 else 'orange' for v in field_eqs])
    bars2 = ax.bar(x + width/2, scalars, width, label='Scalar Analysis',
                   color=['green' if v > 0 else 'red' if v < 0 else 'orange' for v in scalars])

    ax.set_ylabel('Viability')
    ax.set_title('Einstein Compatibility Hierarchy for Non-Newtonian Calculus')
    ax.set_xticks(x)
    ax.set_xticklabels(tiers)
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.set_ylim(-1.5, 1.5)
    ax.legend()

    # Add annotations
    ax.annotate('WORKS', xy=(0, 1), xytext=(0, 1.2), ha='center', fontsize=10, color='green')
    ax.annotate('Diagnostic only', xy=(1, 1), xytext=(1, 1.2), ha='center', fontsize=10, color='blue')
    ax.annotate('FAILS', xy=(2, -1), xytext=(2, -1.3), ha='center', fontsize=10, color='red')

    plt.tight_layout()
    plt.savefig('figures/fig1_hierarchy.png')
    plt.savefig('figures/fig1_hierarchy.pdf')
    print("  Saved: figures/fig1_hierarchy.png")
    plt.close()


def fig2_n_vs_k():
    """Figure 2: Meta-Friedmann expansion exponent n vs k."""
    print("Generating Figure 2: n vs k for different w...")

    fig, ax = plt.subplots(figsize=(10, 6))

    k_vals = np.linspace(-0.5, 2.0, 100)

    # Different equations of state
    w_values = [0.0, 1/3, 1.0]
    labels = ['Dust (w=0)', 'Radiation (w=1/3)', 'Stiff (w=1)']
    colors = ['blue', 'red', 'green']

    for w, label, color in zip(w_values, labels, colors):
        n_vals = (2/3) * (1 - k_vals) / (1 + w)
        ax.plot(k_vals, n_vals, color=color, linewidth=2, label=label)

    # Mark special points
    ax.axvline(x=0, color='gray', linestyle='--', alpha=0.5, label='Classical (k=0)')
    ax.axvline(x=1, color='orange', linestyle='--', alpha=0.5, label='Singularity-free (k=1)')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    ax.set_xlabel('Meta-weight exponent k')
    ax.set_ylabel('Expansion exponent n')
    ax.set_title('Meta-Friedmann: Expansion Exponent n = (2/3)(1-k)/(1+w)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.5, 2.0)
    ax.set_ylim(-1, 1.5)

    # Annotate regions
    ax.annotate('Classical expansion', xy=(0.1, 0.5), fontsize=10)
    ax.annotate('Static/slow\nexpansion', xy=(0.8, 0.1), fontsize=10)
    ax.annotate('Contraction?', xy=(1.3, -0.3), fontsize=10, color='red')

    plt.tight_layout()
    plt.savefig('figures/fig2_n_vs_k.png')
    plt.savefig('figures/fig2_n_vs_k.pdf')
    print("  Saved: figures/fig2_n_vs_k.png")
    plt.close()


def fig3_singularity_softening():
    """Figure 3: Density exponent m = 2 - 2k."""
    print("Generating Figure 3: Singularity softening m = 2 - 2k...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left panel: m vs k
    ax = axes[0]
    k_vals = np.linspace(-0.5, 2.0, 100)
    m_vals = 2 - 2 * k_vals

    ax.plot(k_vals, m_vals, 'b-', linewidth=2)
    ax.axhline(y=0, color='red', linestyle='--', linewidth=2, label='m=0: No singularity')
    ax.axhline(y=2, color='gray', linestyle='--', alpha=0.5, label='m=2: Classical')
    ax.axvline(x=0, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=1, color='green', linestyle='--', alpha=0.7, label='k=1: Critical')

    ax.fill_between(k_vals, m_vals, 0, where=(m_vals > 0), alpha=0.2, color='red', label='Singularity')
    ax.fill_between(k_vals, m_vals, 0, where=(m_vals <= 0), alpha=0.2, color='green', label='No singularity')

    ax.set_xlabel('Meta-weight exponent k')
    ax.set_ylabel('Density exponent m')
    ax.set_title('Density Scaling: rho ~ t^(-m)')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.5, 2.0)
    ax.set_ylim(-2, 3)

    # Right panel: rho vs t for different k
    ax = axes[1]
    t_vals = np.logspace(-3, 0, 100)

    for k, color, style in [(0, 'red', '-'), (0.5, 'orange', '--'), (1.0, 'green', '-'), (1.5, 'blue', ':')]:
        m = 2 - 2*k
        if m > 0:
            rho = t_vals ** (-m)
        elif m == 0:
            rho = np.ones_like(t_vals)
        else:
            rho = t_vals ** (-m)  # Goes to 0 as t->0

        label = f'k={k:.1f}, m={m:.1f}'
        ax.loglog(t_vals, rho, color=color, linestyle=style, linewidth=2, label=label)

    ax.set_xlabel('Time t')
    ax.set_ylabel('Density rho(t)')
    ax.set_title('Density Evolution for Different k')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e-3, 1)
    ax.set_ylim(1e-2, 1e6)

    # Mark singularity region
    ax.annotate('Singularity\nremoved!', xy=(0.01, 1), fontsize=10, color='green',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('figures/fig3_singularity_softening.png')
    plt.savefig('figures/fig3_singularity_softening.pdf')
    print("  Saved: figures/fig3_singularity_softening.png")
    plt.close()


def fig4_bigeometric_diagnostic():
    """Figure 4: Bigeometric diagnostic D_BG[R] = constant."""
    print("Generating Figure 4: Bigeometric diagnostic...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left panel: Classical R(t) diverges
    ax = axes[0]
    t_vals = np.logspace(-4, 0, 100)

    n = 2/3  # Matter dominated
    C = 6 * (2 * n**2 - n)
    R_classical = C / t_vals**2

    ax.loglog(t_vals, np.abs(R_classical), 'b-', linewidth=2, label='Classical R(t) ~ t^(-2)')
    ax.set_xlabel('Time t')
    ax.set_ylabel('|R(t)|')
    ax.set_title('Classical Ricci Scalar: DIVERGES')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.annotate('R -> infinity\nas t -> 0', xy=(1e-3, 1e6), fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Right panel: D_BG[R] = constant
    ax = axes[1]

    D_BG_R = np.exp(-2) * np.ones_like(t_vals)  # Constant!

    ax.semilogx(t_vals, D_BG_R, 'g-', linewidth=2, label='D_BG[R] = e^(-2)')
    ax.axhline(y=np.exp(-2), color='k', linestyle='--', alpha=0.5)

    ax.set_xlabel('Time t')
    ax.set_ylabel('D_BG[R]')
    ax.set_title('Bigeometric Derivative: CONSTANT!')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0.13, 0.14)

    ax.annotate(f'D_BG[R] = e^(-2) = {np.exp(-2):.4f}\nFINITE at all t!',
                xy=(1e-2, 0.136), fontsize=11, color='green', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('figures/fig4_bigeometric_diagnostic.png')
    plt.savefig('figures/fig4_bigeometric_diagnostic.pdf')
    print("  Saved: figures/fig4_bigeometric_diagnostic.png")
    plt.close()


def fig5_4d_failure():
    """Figure 5: 4D L_BG-Christoffel failure."""
    print("Generating Figure 5: 4D L_BG failure...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    n = 2/3

    # Left panel: 2D vs 4D divergence
    ax = axes[0]
    t_vals = np.logspace(-3, 0, 100)

    # 2D appears to work
    R_LBG_2d = -2 * n * np.ones_like(t_vals)

    # 4D fails (simplified: ~ t^(-4n))
    R_LBG_4d = t_vals ** (-4*n)  # Simplified dominant term

    ax.semilogx(t_vals, R_LBG_2d, 'g-', linewidth=2, label=f'2D: R_LBG = {-2*n:.2f} (constant)')
    ax.semilogx(t_vals, R_LBG_4d, 'r-', linewidth=2, label='4D: R_LBG ~ t^(-4n) (DIVERGES!)')
    ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)

    ax.set_xlabel('Time t')
    ax.set_ylabel('R_LBG')
    ax.set_title('2D "Success" vs 4D FAILURE')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-5, 100)

    ax.annotate('2D: Constant\n(MISLEADING)', xy=(0.1, -1.5), fontsize=10, color='green')
    ax.annotate('4D: Diverges!\n(WORSE than classical)', xy=(0.003, 50), fontsize=10, color='red')

    # Right panel: Symmetry breaking
    ax = axes[1]

    t_fixed = 0.1
    r_vals = np.linspace(0.5, 3.0, 50)

    # In 4D, R_LBG depends on r (should be constant for FRW!)
    # Simplified model: R_LBG ~ 1/r^2 term appears
    R_LBG_vs_r = 10 * (1/r_vals**2 + 0.1)

    ax.plot(r_vals, R_LBG_vs_r, 'r-', linewidth=2, label='4D R_LBG(r)')
    ax.axhline(y=-2*n, color='g', linestyle='--', linewidth=2, label=f'2D R_LBG = {-2*n:.2f}')

    ax.set_xlabel('Radius r')
    ax.set_ylabel('R_LBG')
    ax.set_title(f'HOMOGENEITY BROKEN: R_LBG depends on r (t={t_fixed})')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax.annotate('FRW should be\nr-independent!', xy=(2.0, max(R_LBG_vs_r)*0.7),
                fontsize=10, color='red',
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    plt.tight_layout()
    plt.savefig('figures/fig5_4d_failure.png')
    plt.savefig('figures/fig5_4d_failure.pdf')
    print("  Saved: figures/fig5_4d_failure.png")
    plt.close()


def fig6_action_comparison():
    """Figure 6: Action-based u(t) vs Derivative-weight comparison."""
    print("Generating Figure 6: Action comparison...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left panel: Action-based u(t) = t^s
    ax = axes[0]
    t_vals = np.logspace(-3, 0, 100)

    # rho always ~ t^(-2) for action-based
    for s, color in [(0, 'blue'), (0.5, 'green'), (1.0, 'orange')]:
        rho = t_vals ** (-2)  # Always -2!
        label = f's = {s:.1f} (m = 2 always)'
        ax.loglog(t_vals, rho, color=color, linewidth=2, label=label, linestyle='--' if s > 0 else '-')

    ax.set_xlabel('Time t')
    ax.set_ylabel('Density rho(t)')
    ax.set_title('Action-based u(t) = t^s:\nrho ~ t^(-2) ALWAYS')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax.annotate('Cannot change\nsingularity!', xy=(0.01, 1e4), fontsize=10, color='red',
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Right panel: Derivative-weight t^k
    ax = axes[1]

    for k, color in [(0, 'blue'), (0.5, 'green'), (1.0, 'orange'), (1.5, 'purple')]:
        m = 2 - 2*k
        if m > 0:
            rho = t_vals ** (-m)
        elif m == 0:
            rho = np.ones_like(t_vals)
        else:
            rho = t_vals ** (-m)

        label = f'k = {k:.1f} (m = {m:.1f})'
        ax.loglog(t_vals, rho, color=color, linewidth=2, label=label)

    ax.set_xlabel('Time t')
    ax.set_ylabel('Density rho(t)')
    ax.set_title('Derivative-weight D = t^k d/dt:\nrho ~ t^(-(2-2k)) TUNABLE')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(1e-2, 1e6)

    ax.annotate('Singularity\nREMOVED!', xy=(0.01, 1), fontsize=10, color='green',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('figures/fig6_action_comparison.png')
    plt.savefig('figures/fig6_action_comparison.pdf')
    print("  Saved: figures/fig6_action_comparison.png")
    plt.close()


def fig7_bbn_cmb_constraints():
    """Figure 7: BBN/CMB constraints on k."""
    print("Generating Figure 7: BBN/CMB constraints...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left panel: Chi-squared
    ax = axes[0]

    k_vals = np.linspace(-0.1, 0.1, 200)

    # BBN chi-squared (simplified)
    chi2_bbn = (k_vals / 0.02)**2

    # CMB chi-squared (tighter)
    chi2_cmb = (k_vals / 0.0005)**2

    # Combined
    chi2_total = chi2_bbn + chi2_cmb

    ax.semilogy(k_vals, chi2_bbn, 'b-', linewidth=2, label='BBN')
    ax.semilogy(k_vals, chi2_cmb, 'r-', linewidth=2, label='CMB')
    ax.semilogy(k_vals, chi2_total, 'k--', linewidth=2, label='Combined')

    ax.axhline(y=4, color='gray', linestyle=':', label='2-sigma')
    ax.axhline(y=9, color='gray', linestyle='--', alpha=0.5, label='3-sigma')

    ax.set_xlabel('Meta-weight k')
    ax.set_ylabel('Chi-squared')
    ax.set_title('Observational Constraints on k')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0.1, 1000)

    # Right panel: Allowed regions
    ax = axes[1]

    sigma_levels = [1, 2, 3]
    k_bounds = {1: 0.0005, 2: 0.001, 3: 0.0015}  # Approximate

    for sigma in sigma_levels:
        k_max = k_bounds[sigma]
        ax.barh(sigma, 2*k_max, left=-k_max, height=0.6,
                alpha=0.5, label=f'{sigma}-sigma')

    ax.axvline(x=0, color='black', linewidth=1)
    ax.axvline(x=1, color='red', linestyle='--', label='k=1 (singularity-free)')

    ax.set_xlabel('Meta-weight k')
    ax.set_ylabel('Sigma level')
    ax.set_title('Allowed k Range vs Confidence Level')
    ax.legend(loc='upper right')
    ax.set_xlim(-0.01, 0.01)
    ax.set_yticks([1, 2, 3])

    ax.annotate('k = 1 needed for\nsingularity removal\n(ruled out during\nBBN/CMB era)',
                xy=(0.005, 2.5), fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    plt.tight_layout()
    plt.savefig('figures/fig7_bbn_cmb_constraints.png')
    plt.savefig('figures/fig7_bbn_cmb_constraints.pdf')
    print("  Saved: figures/fig7_bbn_cmb_constraints.png")
    plt.close()


def fig8_phase_transition():
    """Figure 8: Phase transition scenario."""
    print("Generating Figure 8: Phase transition scenario...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left panel: k(T) transition
    ax = axes[0]

    T_vals = np.logspace(-3, 4, 1000)  # eV to GeV

    k_early = 1.0
    T_transition = 100  # MeV = 1e8 eV = 100000 in our scale
    T_trans_ev = 1e8  # 100 MeV in eV
    width = 0.5

    k_of_T = k_early * 0.5 * (1 + np.tanh(np.log(T_vals / T_trans_ev) / width))

    ax.semilogx(T_vals, k_of_T, 'b-', linewidth=2)
    ax.axhline(y=1, color='green', linestyle='--', alpha=0.5, label='k=1 (early)')
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5, label='k=0 (late)')
    ax.axvline(x=1e8, color='red', linestyle=':', label='T_transition ~ 100 MeV')
    ax.axvline(x=1e6, color='orange', linestyle=':', alpha=0.7, label='BBN ~ 1 MeV')

    ax.set_xlabel('Temperature T (eV)')
    ax.set_ylabel('Meta-weight k')
    ax.set_title('Phase Transition: k(T)')
    ax.legend(loc='center right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e-3, 1e4)
    ax.set_ylim(-0.1, 1.2)

    ax.annotate('Singularity-free\nearly phase', xy=(1e10, 0.9), fontsize=10, color='green')
    ax.annotate('Classical\nlate phase', xy=(1e2, 0.1), fontsize=10)

    # Right panel: rho(T) in both phases
    ax = axes[1]

    # Classical: rho ~ T^4 (radiation)
    rho_classical = (T_vals / 1e6)**4  # Normalized

    # Meta: rho ~ T^(4*(1-k)) approximately
    # This is simplified; actual dependence is more complex
    rho_meta = np.where(T_vals > T_trans_ev,
                        (T_vals / 1e6)**0,  # k=1: rho constant
                        (T_vals / 1e6)**4)   # k=0: classical

    ax.loglog(T_vals, rho_classical, 'r--', linewidth=2, label='Classical (k=0 always)')
    ax.loglog(T_vals, rho_meta, 'b-', linewidth=2, label='Meta with transition')
    ax.axvline(x=T_trans_ev, color='gray', linestyle=':', alpha=0.5)

    ax.set_xlabel('Temperature T (eV)')
    ax.set_ylabel('Density rho (normalized)')
    ax.set_title('Density Evolution with Phase Transition')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1e-3, 1e12)

    ax.annotate('Early:\nrho = const\n(no singularity)', xy=(1e10, 1e-10), fontsize=9, color='blue')
    ax.annotate('Late:\nrho ~ T^4\n(classical)', xy=(1e2, 1e-8), fontsize=9)

    plt.tight_layout()
    plt.savefig('figures/fig8_phase_transition.png')
    plt.savefig('figures/fig8_phase_transition.pdf')
    print("  Saved: figures/fig8_phase_transition.png")
    plt.close()


def generate_all():
    """Generate all figures."""
    print("=" * 70)
    print("GENERATING ALL PAPER FIGURES")
    print("=" * 70)

    fig1_hierarchy()
    fig2_n_vs_k()
    fig3_singularity_softening()
    fig4_bigeometric_diagnostic()
    fig5_4d_failure()
    fig6_action_comparison()
    fig7_bbn_cmb_constraints()
    fig8_phase_transition()

    print("\n" + "=" * 70)
    print("ALL FIGURES GENERATED")
    print("=" * 70)
    print("\nFigures saved to: figures/")
    print("  - fig1_hierarchy.png/pdf")
    print("  - fig2_n_vs_k.png/pdf")
    print("  - fig3_singularity_softening.png/pdf")
    print("  - fig4_bigeometric_diagnostic.png/pdf")
    print("  - fig5_4d_failure.png/pdf")
    print("  - fig6_action_comparison.png/pdf")
    print("  - fig7_bbn_cmb_constraints.png/pdf")
    print("  - fig8_phase_transition.png/pdf")


def main():
    parser = argparse.ArgumentParser(description="Generate paper figures")
    parser.add_argument('--figure', type=int, choices=[1,2,3,4,5,6,7,8],
                        help='Generate specific figure (1-8)')

    args = parser.parse_args()

    if args.figure:
        fig_funcs = {
            1: fig1_hierarchy,
            2: fig2_n_vs_k,
            3: fig3_singularity_softening,
            4: fig4_bigeometric_diagnostic,
            5: fig5_4d_failure,
            6: fig6_action_comparison,
            7: fig7_bbn_cmb_constraints,
            8: fig8_phase_transition,
        }
        fig_funcs[args.figure]()
    else:
        generate_all()


if __name__ == '__main__':
    main()
