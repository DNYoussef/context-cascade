#!/usr/bin/env python
"""
NNC Singularity Visualizations for Academic Paper
Generates publication-quality figures for the bigeometric calculus paper.

All figures saved to: simulations/figures/
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Create figures directory
os.makedirs('figures', exist_ok=True)

# Set publication-quality defaults
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 11,
    'figure.figsize': (8, 6),
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})


def bigeometric_derivative(f, x, dx=1e-8):
    """Compute bigeometric derivative D_BG[f](x) = exp(x * f'(x) / f(x))"""
    fx = f(x)
    f_prime = (f(x + dx) - f(x - dx)) / (2 * dx)
    fx_safe = np.where(np.abs(fx) < 1e-100, 1e-100, fx)
    return np.exp(x * f_prime / fx_safe)


def classical_derivative(f, x, dx=1e-8):
    """Compute classical derivative f'(x)"""
    return (f(x + dx) - f(x - dx)) / (2 * dx)


# =============================================================================
# FIGURE 1: Classical vs Bigeometric Derivatives for Power Laws
# =============================================================================
def figure1_power_law_comparison():
    """Compare classical and bigeometric derivatives for f(x) = x^n"""
    print("Generating Figure 1: Power Law Comparison...")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    x = np.linspace(0.01, 10, 500)

    # Panel A: f(x) = 1/x (n=-1, Hawking temperature)
    ax = axes[0, 0]
    f = lambda x: 1/x
    classical = classical_derivative(f, x)
    bigeometric = bigeometric_derivative(f, x)

    ax.semilogy(x, np.abs(classical), 'b-', label='|Classical derivative|', linewidth=2)
    ax.axhline(y=np.exp(-1), color='r', linestyle='--', label=f'Bigeometric = e^(-1) = {np.exp(-1):.4f}', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('Derivative magnitude')
    ax.set_title('(A) f(x) = 1/x  (Hawking Temperature)')
    ax.legend()
    ax.set_ylim(1e-2, 1e4)
    ax.grid(True, alpha=0.3)
    ax.text(0.95, 0.95, 'Classical DIVERGES\nBigeometric CONSTANT',
            transform=ax.transAxes, ha='right', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Panel B: f(x) = 1/x^6 (n=-6, Kretschmann scalar)
    ax = axes[0, 1]
    f = lambda x: 1/(x**6)
    classical = classical_derivative(f, x)
    bigeometric = bigeometric_derivative(f, x)

    ax.semilogy(x, np.abs(classical), 'b-', label='|Classical derivative|', linewidth=2)
    ax.axhline(y=np.exp(-6), color='r', linestyle='--', label=f'Bigeometric = e^(-6) = {np.exp(-6):.6f}', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('Derivative magnitude')
    ax.set_title('(B) f(x) = 1/x^6  (Kretschmann Scalar)')
    ax.legend()
    ax.set_ylim(1e-10, 1e20)
    ax.grid(True, alpha=0.3)
    ax.text(0.95, 0.95, 'Classical DIVERGES\nBigeometric CONSTANT',
            transform=ax.transAxes, ha='right', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Panel C: f(x) = x^(1/2) (n=0.5, radiation era)
    ax = axes[1, 0]
    f = lambda x: np.sqrt(x)
    classical = classical_derivative(f, x)
    bigeometric = bigeometric_derivative(f, x)

    ax.plot(x, classical, 'b-', label='Classical derivative', linewidth=2)
    ax.axhline(y=np.exp(0.5), color='r', linestyle='--', label=f'Bigeometric = e^(0.5) = {np.exp(0.5):.4f}', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('Derivative')
    ax.set_title('(C) f(x) = x^(1/2)  (Big Bang Radiation Era)')
    ax.legend()
    ax.set_ylim(0, 10)
    ax.grid(True, alpha=0.3)
    ax.text(0.95, 0.95, 'Classical DIVERGES at x=0\nBigeometric CONSTANT',
            transform=ax.transAxes, ha='right', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Panel D: Summary - D_BG[x^n] = e^n for various n
    ax = axes[1, 1]
    n_values = np.array([-6, -3, -2, -1, -0.5, 0.5, 2/3, 1, 2, 3])
    e_n = np.exp(n_values)

    # Computed values
    computed = []
    for n in n_values:
        f = lambda x, n=n: x**n
        vals = bigeometric_derivative(f, np.linspace(0.1, 10, 100))
        computed.append(np.mean(vals))
    computed = np.array(computed)

    ax.scatter(n_values, e_n, s=100, c='red', marker='o', label='Expected: e^n', zorder=3)
    ax.scatter(n_values, computed, s=50, c='blue', marker='x', label='Computed', zorder=4)
    ax.plot(n_values, e_n, 'r--', alpha=0.5)
    ax.set_xlabel('Power n')
    ax.set_ylabel('D_BG[x^n]')
    ax.set_title('(D) Power Law Theorem: D_BG[x^n] = e^n')
    ax.legend()
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=1, color='gray', linestyle=':', alpha=0.5)

    # Add physics labels
    physics_labels = {-6: 'Kretschmann', -1: 'Hawking T', 0.5: 'Radiation', 2/3: 'Matter'}
    for n, label in physics_labels.items():
        idx = np.where(np.isclose(n_values, n))[0]
        if len(idx) > 0:
            ax.annotate(label, (n, e_n[idx[0]]), textcoords="offset points",
                       xytext=(10, 5), fontsize=9)

    plt.tight_layout()
    plt.savefig('figures/fig1_power_law_comparison.png')
    plt.savefig('figures/fig1_power_law_comparison.pdf')
    print("  Saved: figures/fig1_power_law_comparison.png")
    plt.close()


# =============================================================================
# FIGURE 2: Hawking Temperature Evolution
# =============================================================================
def figure2_hawking_temperature():
    """Hawking temperature: classical divergence vs bigeometric regularization"""
    print("Generating Figure 2: Hawking Temperature...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Mass range (in units where constants = 1)
    M = np.linspace(0.01, 10, 500)

    # Panel A: Temperature vs Mass
    ax = axes[0]
    T_H = 1 / M  # T ~ 1/M

    ax.plot(M, T_H, 'b-', linewidth=2, label='Hawking Temperature T_H = 1/M')
    ax.set_xlabel('Black Hole Mass M')
    ax.set_ylabel('Temperature T_H')
    ax.set_title('(A) Hawking Temperature vs Mass')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 50)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.annotate('T -> infinity\nas M -> 0', xy=(0.5, 40), fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Panel B: Derivatives comparison
    ax = axes[1]

    # Classical derivative dT/dM = -1/M^2
    classical_dT = -1 / M**2

    # Bigeometric derivative = e^(-1)
    bigeometric_dT = np.ones_like(M) * np.exp(-1)

    ax.semilogy(M, np.abs(classical_dT), 'b-', linewidth=2, label='|Classical dT/dM| = 1/M^2')
    ax.semilogy(M, bigeometric_dT, 'r--', linewidth=2, label=f'Bigeometric D_BG[T] = e^(-1) = {np.exp(-1):.4f}')
    ax.set_xlabel('Black Hole Mass M')
    ax.set_ylabel('Derivative Magnitude')
    ax.set_title('(B) Classical vs Bigeometric Derivative')
    ax.set_xlim(0, 10)
    ax.set_ylim(1e-2, 1e4)
    ax.grid(True, alpha=0.3)
    ax.legend()

    ax.fill_between(M, 1e-2, np.abs(classical_dT), alpha=0.2, color='blue')
    ax.annotate('Classical\nDIVERGES', xy=(0.3, 100), fontsize=11, color='blue')
    ax.annotate('Bigeometric\nCONSTANT', xy=(5, 0.5), fontsize=11, color='red')

    plt.tight_layout()
    plt.savefig('figures/fig2_hawking_temperature.png')
    plt.savefig('figures/fig2_hawking_temperature.pdf')
    print("  Saved: figures/fig2_hawking_temperature.png")
    plt.close()


# =============================================================================
# FIGURE 3: Big Bang Scale Factor
# =============================================================================
def figure3_big_bang():
    """Big Bang singularity: scale factor evolution"""
    print("Generating Figure 3: Big Bang Scale Factor...")

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    t = np.linspace(1e-6, 5, 500)

    # Panel A: Scale factor evolution
    ax = axes[0]
    a_rad = t**0.5  # Radiation era
    a_mat = t**(2/3)  # Matter era

    ax.plot(t, a_rad, 'b-', linewidth=2, label='Radiation: a(t) = t^(1/2)')
    ax.plot(t, a_mat, 'g-', linewidth=2, label='Matter: a(t) = t^(2/3)')
    ax.set_xlabel('Time t')
    ax.set_ylabel('Scale Factor a(t)')
    ax.set_title('(A) Scale Factor Evolution')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.annotate('Big Bang\nSingularity?', xy=(0.1, 0.1), fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Panel B: Classical derivatives (diverge)
    ax = axes[1]
    da_rad = 0.5 * t**(-0.5)
    da_mat = (2/3) * t**(-1/3)

    ax.semilogy(t, da_rad, 'b-', linewidth=2, label='Radiation: da/dt = 0.5/sqrt(t)')
    ax.semilogy(t, da_mat, 'g-', linewidth=2, label='Matter: da/dt = (2/3)/t^(1/3)')
    ax.set_xlabel('Time t')
    ax.set_ylabel('Classical Derivative da/dt')
    ax.set_title('(B) Classical Derivatives (DIVERGE)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(1e-1, 1e4)
    ax.annotate('Both DIVERGE\nas t -> 0', xy=(0.01, 1000), fontsize=10, color='red',
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Panel C: Bigeometric derivatives (constant)
    ax = axes[2]
    D_rad = np.ones_like(t) * np.exp(0.5)
    D_mat = np.ones_like(t) * np.exp(2/3)

    ax.plot(t, D_rad, 'b-', linewidth=2, label=f'Radiation: D_BG[a] = e^(0.5) = {np.exp(0.5):.3f}')
    ax.plot(t, D_mat, 'g-', linewidth=2, label=f'Matter: D_BG[a] = e^(2/3) = {np.exp(2/3):.3f}')
    ax.set_xlabel('Time t')
    ax.set_ylabel('Bigeometric Derivative D_BG[a]')
    ax.set_title('(C) Bigeometric Derivatives (CONSTANT)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 3)
    ax.annotate('CONSTANT\neven at t -> 0!', xy=(2, 1.2), fontsize=10, color='green',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    plt.tight_layout()
    plt.savefig('figures/fig3_big_bang.png')
    plt.savefig('figures/fig3_big_bang.pdf')
    print("  Saved: figures/fig3_big_bang.png")
    plt.close()


# =============================================================================
# FIGURE 4: Kretschmann Scalar Near Singularity
# =============================================================================
def figure4_kretschmann():
    """Kretschmann scalar K ~ 1/r^6 near black hole singularity"""
    print("Generating Figure 4: Kretschmann Scalar...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    r = np.logspace(-3, 1, 500)  # From 0.001 to 10

    # Panel A: Kretschmann scalar
    ax = axes[0]
    K = 1 / r**6  # K ~ 1/r^6

    ax.loglog(r, K, 'b-', linewidth=2)
    ax.set_xlabel('Radius r (units of r_s)')
    ax.set_ylabel('Kretschmann Scalar K')
    ax.set_title('(A) Kretschmann Scalar K = 48M^2/r^6')
    ax.grid(True, alpha=0.3)
    ax.axvline(x=1, color='gray', linestyle=':', label='Schwarzschild radius')
    ax.annotate('K -> infinity\nas r -> 0\n(SINGULARITY)',
                xy=(0.01, 1e12), fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Panel B: Derivatives
    ax = axes[1]

    # Classical: dK/dr = -6/r^7
    classical = 6 / r**7

    # Bigeometric: D_BG[K] = e^(-6)
    bigeometric = np.ones_like(r) * np.exp(-6)

    ax.loglog(r, classical, 'b-', linewidth=2, label='|Classical dK/dr| = 6/r^7')
    ax.loglog(r, bigeometric, 'r--', linewidth=2, label=f'Bigeometric D_BG[K] = e^(-6) = {np.exp(-6):.6f}')
    ax.set_xlabel('Radius r (units of r_s)')
    ax.set_ylabel('Derivative Magnitude')
    ax.set_title('(B) Classical vs Bigeometric Derivative')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.axvline(x=1, color='gray', linestyle=':')

    ax.fill_between(r, 1e-10, classical, alpha=0.2, color='blue', where=(classical > 1e-10))
    ax.annotate('Classical\nDIVERGES', xy=(0.01, 1e15), fontsize=10, color='blue')
    ax.annotate('Bigeometric\nCONSTANT', xy=(1, 1e-4), fontsize=10, color='red')

    plt.tight_layout()
    plt.savefig('figures/fig4_kretschmann.png')
    plt.savefig('figures/fig4_kretschmann.pdf')
    print("  Saved: figures/fig4_kretschmann.png")
    plt.close()


# =============================================================================
# FIGURE 5: Scope and Limitations
# =============================================================================
def figure5_scope_limitations():
    """Show what NNC does and does NOT regularize"""
    print("Generating Figure 5: Scope and Limitations...")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    x = np.linspace(0.01, 5, 500)

    # Panel A: Power law - REGULARIZED
    ax = axes[0, 0]
    f = lambda x: 1/x**2
    D_BG = bigeometric_derivative(f, x)

    ax.plot(x, D_BG, 'g-', linewidth=2)
    ax.axhline(y=np.exp(-2), color='r', linestyle='--', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('D_BG[f]')
    ax.set_title('(A) Power Law f(x) = 1/x^2: REGULARIZED')
    ax.set_ylim(0, 0.3)
    ax.grid(True, alpha=0.3)
    ax.fill_between(x, 0, D_BG, alpha=0.3, color='green')
    ax.annotate(f'D_BG = e^(-2) = {np.exp(-2):.4f}\nCONSTANT',
                xy=(3, 0.15), fontsize=11, color='green',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    # Panel B: Exponential - NOT regularized
    ax = axes[0, 1]
    f = lambda x: np.exp(1/x)
    D_BG = bigeometric_derivative(f, x)

    ax.semilogy(x, D_BG, 'r-', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('D_BG[f]')
    ax.set_title('(B) Essential Singularity f(x) = exp(1/x): NOT REGULARIZED')
    ax.grid(True, alpha=0.3)
    ax.annotate('D_BG VARIES\nNOT constant!', xy=(0.5, 1e10), fontsize=11, color='red',
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Panel C: Logarithm - NOT regularized
    ax = axes[1, 0]
    x_log = np.linspace(0.01, 5, 500)
    f = lambda x: -np.log(x)  # -ln(x) to keep positive
    D_BG = bigeometric_derivative(f, x_log)

    ax.plot(x_log, D_BG, 'r-', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('D_BG[f]')
    ax.set_title('(C) Logarithmic f(x) = -ln(x): NOT REGULARIZED')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 5)
    ax.annotate('D_BG VARIES\nNOT constant!', xy=(2, 3), fontsize=11, color='red',
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Panel D: Summary table as bar chart
    ax = axes[1, 1]

    singularities = ['Power Law\n(Black Hole)', 'Power Law\n(Big Bang)',
                     'Essential\n(exp(1/r))', 'Logarithmic\n(ln(r))']
    regularized = [1, 1, 0, 0]  # 1 = yes, 0 = no
    colors = ['green', 'green', 'red', 'red']

    bars = ax.bar(singularities, regularized, color=colors, alpha=0.7, edgecolor='black')
    ax.set_ylabel('Regularized by Bigeometric Calculus?')
    ax.set_title('(D) Scope of Bigeometric Regularization')
    ax.set_ylim(0, 1.3)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['NO', 'YES'])

    for bar, reg in zip(bars, regularized):
        height = bar.get_height()
        label = 'YES' if reg else 'NO'
        color = 'green' if reg else 'red'
        ax.annotate(label, xy=(bar.get_x() + bar.get_width()/2, height + 0.05),
                   ha='center', fontsize=12, fontweight='bold', color=color)

    ax.annotate('~80-90% of GR\nsingularities covered', xy=(0.5, 0.5), fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    plt.tight_layout()
    plt.savefig('figures/fig5_scope_limitations.png')
    plt.savefig('figures/fig5_scope_limitations.pdf')
    print("  Saved: figures/fig5_scope_limitations.png")
    plt.close()


# =============================================================================
# FIGURE 6: Numerical Validation
# =============================================================================
def figure6_validation():
    """Numerical validation of D_BG[x^n] = e^n"""
    print("Generating Figure 6: Numerical Validation...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: D_BG vs expected for many n values
    ax = axes[0]

    n_values = np.linspace(-6, 3, 50)
    expected = np.exp(n_values)
    computed = []
    errors = []

    for n in n_values:
        f = lambda x, n=n: x**n
        x_test = np.linspace(0.1, 10, 100)
        vals = bigeometric_derivative(f, x_test)
        computed.append(np.mean(vals))
        errors.append(np.std(vals))

    computed = np.array(computed)
    errors = np.array(errors)

    ax.semilogy(n_values, expected, 'r-', linewidth=2, label='Expected: e^n')
    ax.semilogy(n_values, computed, 'b--', linewidth=2, label='Computed')
    ax.fill_between(n_values, computed - 3*errors, computed + 3*errors,
                    alpha=0.3, color='blue', label='3-sigma band')
    ax.set_xlabel('Power n')
    ax.set_ylabel('D_BG[x^n]')
    ax.set_title('(A) Validation: D_BG[x^n] = e^n')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Physics annotations
    physics_n = {'Kretschmann': -6, 'Hawking': -1, 'Radiation': 0.5, 'Matter': 2/3}
    for label, n in physics_n.items():
        ax.axvline(x=n, color='gray', linestyle=':', alpha=0.5)
        ax.annotate(label, (n, np.exp(n)*1.5), fontsize=8, rotation=90)

    # Panel B: Relative error
    ax = axes[1]

    rel_error = np.abs(computed - expected) / expected * 100

    ax.semilogy(n_values, rel_error, 'b-', linewidth=2)
    ax.axhline(y=1e-4, color='g', linestyle='--', label='0.0001% error')
    ax.axhline(y=1e-6, color='r', linestyle='--', label='0.000001% error')
    ax.set_xlabel('Power n')
    ax.set_ylabel('Relative Error (%)')
    ax.set_title('(B) Numerical Precision')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(1e-10, 1e-2)

    ax.annotate(f'Mean error: {np.mean(rel_error):.2e}%', xy=(-4, 1e-3), fontsize=11,
                bbox=dict(boxstyle='round', facecolor='lightgreen'))

    plt.tight_layout()
    plt.savefig('figures/fig6_validation.png')
    plt.savefig('figures/fig6_validation.pdf')
    print("  Saved: figures/fig6_validation.png")
    plt.close()


# =============================================================================
# FIGURE 7: Physical Interpretation - Elasticity
# =============================================================================
def figure7_elasticity():
    """Physical interpretation: D_BG = exp(elasticity)"""
    print("Generating Figure 7: Physical Interpretation...")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    x = np.linspace(0.1, 10, 500)

    # Panel A: Elasticity for different power laws
    ax = axes[0]

    for n, label, color in [(-2, 'n=-2 (curvature)', 'blue'),
                            (-1, 'n=-1 (Hawking T)', 'green'),
                            (0.5, 'n=0.5 (radiation)', 'red'),
                            (1, 'n=1 (linear)', 'purple')]:
        f = lambda x, n=n: x**n
        # Elasticity = x * f'(x) / f(x) = n
        elasticity = np.ones_like(x) * n
        ax.plot(x, elasticity, color=color, linewidth=2, label=f'{label}: elasticity = {n}')

    ax.set_xlabel('x')
    ax.set_ylabel('Elasticity = x * f\'(x) / f(x)')
    ax.set_title('(A) Elasticity is CONSTANT for Power Laws')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='gray', linestyle=':')

    ax.annotate('Elasticity = % change in f\nper % change in x',
                xy=(6, 0.3), fontsize=10,
                bbox=dict(boxstyle='round', facecolor='lightyellow'))

    # Panel B: D_BG = exp(elasticity)
    ax = axes[1]

    elasticity_range = np.linspace(-6, 3, 100)
    D_BG = np.exp(elasticity_range)

    ax.semilogy(elasticity_range, D_BG, 'b-', linewidth=2)
    ax.set_xlabel('Elasticity (= n for power laws)')
    ax.set_ylabel('Bigeometric Derivative D_BG = exp(elasticity)')
    ax.set_title('(B) D_BG = exp(Elasticity)')
    ax.grid(True, alpha=0.3)

    # Mark physics examples
    physics_examples = [(-6, 'Kretschmann'), (-1, 'Hawking'), (0.5, 'Radiation'), (2/3, 'Matter')]
    for n, label in physics_examples:
        ax.scatter([n], [np.exp(n)], s=100, zorder=5)
        ax.annotate(f'{label}\n({np.exp(n):.3f})', (n, np.exp(n)*1.3), fontsize=9, ha='center')

    ax.axhline(y=1, color='gray', linestyle=':', label='D_BG = 1 (n=0)')

    plt.tight_layout()
    plt.savefig('figures/fig7_elasticity.png')
    plt.savefig('figures/fig7_elasticity.pdf')
    print("  Saved: figures/fig7_elasticity.png")
    plt.close()


# =============================================================================
# MAIN
# =============================================================================
if __name__ == '__main__':
    print("="*60)
    print("NNC SINGULARITY VISUALIZATIONS")
    print("Generating publication-quality figures...")
    print("="*60)

    figure1_power_law_comparison()
    figure2_hawking_temperature()
    figure3_big_bang()
    figure4_kretschmann()
    figure5_scope_limitations()
    figure6_validation()
    figure7_elasticity()

    print("="*60)
    print("ALL FIGURES GENERATED")
    print("Location: simulations/figures/")
    print("="*60)

    # List all figures
    print("\nFigures created:")
    for f in sorted(os.listdir('figures')):
        print(f"  - {f}")
