"""
Shared plotting utilities for NNC simulations.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server environments
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Publication-quality settings
rcParams['font.size'] = 12
rcParams['font.family'] = 'serif'
rcParams['axes.labelsize'] = 14
rcParams['axes.titlesize'] = 16
rcParams['xtick.labelsize'] = 12
rcParams['ytick.labelsize'] = 12
rcParams['legend.fontsize'] = 12
rcParams['figure.dpi'] = 100  # Lower for faster rendering, increase for publication


def plot_classical_vs_nnc(x, classical, nnc, xlabel, ylabel,
                           title, expected_nnc=None, save_path=None):
    """
    Plot classical (divergent) vs NNC (regularized) results.

    Args:
        x: Independent variable
        classical: Classical results (may diverge)
        nnc: NNC results (regularized)
        xlabel, ylabel, title: Plot labels
        expected_nnc: Expected NNC value (constant line)
        save_path: Path to save figure
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Classical result
    finite_mask = np.isfinite(classical)
    if np.any(finite_mask):
        ax1.semilogy(x[finite_mask], np.abs(classical[finite_mask]),
                     'b-', linewidth=2, label='Classical')
        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(f'{ylabel} (absolute value)')
        ax1.set_title(f'{title} - Classical (Diverges)')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
    else:
        ax1.text(0.5, 0.5, 'All values divergent', ha='center', va='center',
                 transform=ax1.transAxes)
        ax1.set_title(f'{title} - Classical (Diverges)')

    # NNC result
    ax2.plot(x, nnc, 'r-', linewidth=2, label='NNC (Regularized)')
    if expected_nnc is not None:
        ax2.axhline(expected_nnc, color='k', linestyle='--',
                    label=f'Expected: {expected_nnc:.4f}')
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel)
    ax2.set_title(f'{title} - NNC (Regularized)')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {save_path}")

    plt.close()


def plot_evolution(t, observables_dict, title, save_path=None):
    """
    Plot time evolution of multiple observables.

    Args:
        t: Time array
        observables_dict: {name: values} dictionary
        title: Plot title
        save_path: Path to save figure
    """
    n_obs = len(observables_dict)
    fig, axes = plt.subplots(n_obs, 1, figsize=(10, 4*n_obs))

    if n_obs == 1:
        axes = [axes]

    for ax, (name, values) in zip(axes, observables_dict.items()):
        ax.plot(t, values, linewidth=2)
        ax.set_xlabel('Time')
        ax.set_ylabel(name)
        ax.grid(True, alpha=0.3)

    axes[0].set_title(title)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {save_path}")

    plt.close()


def plot_conservation(t, conserved_quantity, title, rtol=1e-6, save_path=None):
    """
    Plot conservation of a quantity over time.

    Args:
        t: Time array
        conserved_quantity: Values of conserved quantity
        title: Plot title
        rtol: Relative tolerance for conservation
        save_path: Path to save figure
    """
    initial = conserved_quantity[0]
    relative_error = (conserved_quantity - initial) / initial

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Absolute values
    ax1.plot(t, conserved_quantity, 'b-', linewidth=2)
    ax1.axhline(initial, color='k', linestyle='--', alpha=0.5,
                label=f'Initial: {initial:.6e}')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Conserved Quantity')
    ax1.set_title(title)
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # Relative error
    ax2.semilogy(t, np.abs(relative_error) + 1e-20, 'r-', linewidth=2)
    ax2.axhline(rtol, color='k', linestyle='--',
                label=f'Tolerance: {rtol:.1e}')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Relative Error')
    ax2.set_title('Conservation Error')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_ylim([1e-12, 1e-2])

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {save_path}")

    plt.close()


def plot_phase_diagram(x, y, z, xlabel, ylabel, zlabel, title, save_path=None):
    """
    Plot 3D phase diagram.

    Args:
        x, y, z: Coordinate arrays
        xlabel, ylabel, zlabel: Axis labels
        title: Plot title
        save_path: Path to save figure
    """
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, z, linewidth=2)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {save_path}")

    plt.close()
