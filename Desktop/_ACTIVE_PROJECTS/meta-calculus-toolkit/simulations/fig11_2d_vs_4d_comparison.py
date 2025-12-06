#!/usr/bin/env python3
"""
Figure 11: 2D vs 4D FRW Comparison

This figure demonstrates why the 2D "bigeometric Christoffel" success
is MISLEADING and does NOT extend to 4D.

Key findings:
  - 2D: R_LBG = -2n (constant, finite) - APPEARS to work
  - 4D: R_LBG ~ t^(-4n) (DIVERGES, worse than classical!)
  - 4D: R_LBG depends on r, theta (BREAKS FRW symmetry!)
"""

import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs('figures', exist_ok=True)

plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
})


def ricci_classical_frw(t, n):
    """Classical R(t) = 6(2n^2 - n) / t^2"""
    C = 6 * (2 * n**2 - n)
    return C / (t**2)


def ricci_LBG_2d(n):
    """2D 'L_BG Ricci' = -2n (constant)"""
    return -2 * n


def ricci_LBG_4d(t, r, theta, n):
    """
    4D 'L_BG Ricci' from symbolic computation.

    R_LBG = 2n(n*r^2 + n*r^2*csc^2(theta) + n*csc^2(theta) - 3*r^4*t^(4n)) / (r^4 * t^(4n))

    PROBLEMS:
    1. Diverges like t^(-4n) as t -> 0
    2. Depends on r (breaks homogeneity)
    3. Depends on theta (breaks isotropy)
    """
    sin_th = np.sin(theta)
    if np.abs(sin_th) < 1e-10:
        return np.inf

    csc_sq = 1.0 / (sin_th**2)

    numerator = 2 * n * (
        n * r**2 +
        n * r**2 * csc_sq +
        n * csc_sq -
        3 * r**4 * t**(4*n)
    )
    denominator = r**4 * t**(4*n)

    if denominator == 0:
        return np.inf

    return numerator / denominator


def D_BG_ricci(t, n):
    """
    D_BG[R_classical] = e^(-2)

    This is the CORRECT diagnostic application.
    """
    return np.exp(-2)


def main():
    print("Generating Figure 11: 2D vs 4D Comparison...")

    n = 2/3
    t_vals = np.logspace(-4, 0, 100)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # =========================================================================
    # Panel A: Classical Ricci scalar (reference)
    # =========================================================================
    ax = axes[0, 0]

    R_classical = [ricci_classical_frw(t, n) for t in t_vals]

    ax.loglog(t_vals, np.abs(R_classical), 'b-', linewidth=2)
    ax.set_xlabel('Time t')
    ax.set_ylabel('|R(t)|')
    ax.set_title('(A) Classical Ricci: R ~ t^(-2) (DIVERGES)')
    ax.grid(True, alpha=0.3)
    ax.annotate('R -> infinity\nas t -> 0', xy=(1e-3, 1e6), fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # =========================================================================
    # Panel B: 2D "success" vs 4D failure
    # =========================================================================
    ax = axes[0, 1]

    R_LBG_2d_vals = [ricci_LBG_2d(n)] * len(t_vals)
    R_LBG_4d_vals = [ricci_LBG_4d(t, r=1.0, theta=np.pi/2, n=n) for t in t_vals]

    ax.semilogx(t_vals, R_LBG_2d_vals, 'g-', linewidth=2, label=f'2D: R_LBG = {ricci_LBG_2d(n):.2f} (constant)')
    ax.semilogx(t_vals, R_LBG_4d_vals, 'r-', linewidth=2, label='4D: R_LBG (DIVERGES!)')
    ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)

    ax.set_xlabel('Time t')
    ax.set_ylabel('R_LBG')
    ax.set_title('(B) 2D "Success" vs 4D FAILURE')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-100, 100)

    ax.annotate('2D: Constant (looks good!)', xy=(1e-2, -1.5), fontsize=10, color='green')
    ax.annotate('4D: Still diverges!', xy=(1e-3, 50), fontsize=10, color='red')

    # =========================================================================
    # Panel C: 4D breaks homogeneity (r-dependence)
    # =========================================================================
    ax = axes[1, 0]

    t_fixed = 0.1
    r_vals = np.linspace(0.5, 3.0, 50)

    R_LBG_vs_r = [ricci_LBG_4d(t_fixed, r, np.pi/2, n) for r in r_vals]
    R_classical_fixed = ricci_classical_frw(t_fixed, n)

    ax.plot(r_vals, R_LBG_vs_r, 'r-', linewidth=2, label='R_LBG (4D)')
    ax.axhline(y=R_classical_fixed, color='b', linestyle='--', linewidth=2,
               label=f'R_classical = {R_classical_fixed:.1f}')
    ax.axhline(y=ricci_LBG_2d(n), color='g', linestyle=':', linewidth=2,
               label=f'R_LBG (2D) = {ricci_LBG_2d(n):.2f}')

    ax.set_xlabel('Radius r')
    ax.set_ylabel('R_LBG')
    ax.set_title(f'(C) HOMOGENEITY BROKEN: R_LBG depends on r (t={t_fixed})')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax.annotate('FRW should be\nr-independent!', xy=(2.0, max(R_LBG_vs_r)*0.7),
                fontsize=10, color='red',
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # =========================================================================
    # Panel D: What ACTUALLY works (D_BG diagnostic)
    # =========================================================================
    ax = axes[1, 1]

    D_BG_vals = [D_BG_ricci(t, n) for t in t_vals]

    ax.semilogx(t_vals, D_BG_vals, 'g-', linewidth=2, label='D_BG[R_classical]')
    ax.axhline(y=np.exp(-2), color='k', linestyle='--', linewidth=2,
               label=f'Expected: e^(-2) = {np.exp(-2):.4f}')

    ax.set_xlabel('Time t')
    ax.set_ylabel('D_BG[R]')
    ax.set_title('(D) WHAT WORKS: D_BG as Diagnostic (Constant!)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0.13, 0.14)

    ax.annotate('D_BG[R] = e^(-2)\nFINITE at all t!', xy=(1e-2, 0.136),
                fontsize=11, color='green', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()
    plt.savefig('figures/fig11_2d_vs_4d_comparison.png')
    plt.savefig('figures/fig11_2d_vs_4d_comparison.pdf')
    print("  Saved: figures/fig11_2d_vs_4d_comparison.png")
    plt.close()

    # =========================================================================
    # Summary output
    # =========================================================================
    print("\n" + "=" * 70)
    print("CROSS-AUDIT FINDINGS VISUALIZED")
    print("=" * 70)
    print("\n  Panel A: Classical R ~ t^(-2) diverges (reference)")
    print("\n  Panel B: 2D 'L_BG Christoffel' gives R_LBG = constant (MISLEADING)")
    print("           4D extension STILL DIVERGES like t^(-4n)")
    print("\n  Panel C: 4D R_LBG depends on r (BREAKS FRW HOMOGENEITY)")
    print("           This should be constant in FRW!")
    print("\n  Panel D: D_BG as DIAGNOSTIC is correct")
    print("           D_BG[R_classical] = e^(-2) is finite and constant")
    print("\n" + "=" * 70)
    print("CONCLUSION: Use D_BG as diagnostic, NOT as field equation modifier")
    print("=" * 70)


if __name__ == '__main__':
    main()
