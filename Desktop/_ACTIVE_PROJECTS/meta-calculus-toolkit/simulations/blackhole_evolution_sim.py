"""
Simulation 1: Black Hole Evolution (Formation to Evaporation)
Uses meta_calculus.applications.black_holes.BlackHoleEvolution

Tests NNC hypothesis that bigeometric derivative D_BG[T_H] = e^(-1) regularizes
Hawking temperature divergence and conserves information via multiplicative entropy.
"""
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from meta_calculus.applications.black_holes import BlackHoleEvolution
from meta_calculus.core.derivatives import BigeometricDerivative
from simulations.utils.validation import (
    check_constant_derivative,
    check_conservation,
    check_no_divergence,
    generate_validation_report
)
from simulations.utils.plotting import (
    plot_classical_vs_nnc,
    plot_evolution,
    plot_conservation
)


class BlackHoleEvolutionSim:
    """
    Comprehensive black hole evolution simulation testing singularity regularization.

    Uses existing BlackHoleEvolution from meta_calculus.applications.black_holes.
    """

    def __init__(self, M_initial=1.0, epsilon=1e-3, units='planck', n_points=1000):
        """
        Initialize simulation.

        Args:
            M_initial: Initial black hole mass (Planck masses)
            epsilon: Quantum correction parameter
            units: Unit system ('planck', 'solar', 'geometric')
            n_points: Number of time points for evolution
        """
        self.M_initial = M_initial
        self.epsilon = epsilon
        self.units = units
        self.n_points = n_points

        # Initialize black hole system
        self.bh_system = BlackHoleEvolution(M_initial, epsilon, units=units)
        self.D_BG = BigeometricDerivative()

        self.results = {}
        self.validation = {}

    def run(self, save_output=True):
        """Execute simulation and collect results."""
        print("Running Simulation 1: Black Hole Evolution")
        print("=" * 60)
        print(f"Initial mass: {self.M_initial} ({self.units} units)")
        print(f"Quantum correction: epsilon = {self.epsilon}")
        print(f"Evolution points: {self.n_points}")
        print()

        # Step 1: Evolve black hole system
        print("[1/5] Evolving black hole system...")
        t_evap = self.bh_system.evaporation_time()
        t_final = 0.95 * t_evap  # Evolve to 95% evaporation

        t, M, S_star_bh, S_star_rad, S_star_quantum = self.bh_system.evolve(
            t_final=t_final,
            n_points=self.n_points
        )

        print(f"    Evaporation time: {t_evap:.6e} s")
        print(f"    Evolved to: t = {t_final:.6e} s ({t_final/t_evap*100:.1f}% of evaporation)")

        # Step 2: Compute observables
        print("[2/5] Computing observables...")

        # Schwarzschild radius
        r_s = np.array([self.bh_system.schwarzschild_radius(m) for m in M])

        # Hawking temperature
        T_H = np.array([self.bh_system.hawking_temperature(m) for m in M])

        # Bekenstein-Hawking entropy
        S_BH = np.array([self.bh_system.bekenstein_hawking_entropy(m) for m in M])

        print(f"    Initial temperature: {T_H[0]:.6e} K")
        print(f"    Final temperature: {T_H[-1]:.6e} K")
        print(f"    Initial entropy: {S_BH[0]:.6e} J/K")

        # Step 3: Compute classical derivatives (diverge)
        print("[3/5] Computing classical derivatives...")

        # dT/dM = -hbar*c^3/(8*pi*G*k_B) * (1/M^2)
        # Diverges as M -> 0
        hbar = self.bh_system.unit_factors['hbar']
        c = self.bh_system.unit_factors['c']
        G = self.bh_system.unit_factors['G']
        k_B = self.bh_system.unit_factors['k_B']

        dT_dM_classical = -(hbar * c**3) / (8 * np.pi * G * k_B) * (1 / M**2)

        print(f"    Classical dT/dM at M_initial: {dT_dM_classical[0]:.6e}")
        print(f"    Classical dT/dM at M_final: {dT_dM_classical[-1]:.6e} (diverging)")

        # Step 4: Compute bigeometric derivatives (constant)
        print("[4/5] Computing bigeometric derivatives...")

        # D_BG[T_H(M)] for T_H = 1/M
        # Expected: e^(-1) = 0.3679
        T_func = lambda m: self.bh_system.hawking_temperature(m)
        D_BG_T = self.D_BG(T_func, M)

        expected_D_BG = np.exp(-1)  # e^(-1) for T ~ M^(-1)

        print(f"    Expected D_BG[T_H]: {expected_D_BG:.6f} (e^(-1))")
        print(f"    Computed D_BG[T_H] mean: {np.mean(D_BG_T):.6f}")
        print(f"    Computed D_BG[T_H] std: {np.std(D_BG_T):.6e}")

        # Step 5: Check conservation
        print("[5/5] Checking information conservation...")

        conservation = self.bh_system.conservation_check(
            t, S_star_bh, S_star_rad, S_star_quantum
        )

        print(f"    Conservation quality: {conservation['conservation_quality']}")
        print(f"    Max relative error: {conservation['max_relative_error']:.6e}")

        # Store results
        self.results = {
            't': t,
            't_normalized': t / t_evap,
            'M': M,
            'M_normalized': M / self.M_initial,
            'r_s': r_s,
            'T_H': T_H,
            'S_BH': S_BH,
            'S_star_bh': S_star_bh,
            'S_star_rad': S_star_rad,
            'S_star_quantum': S_star_quantum,
            'dT_dM_classical': dT_dM_classical,
            'D_BG_T': D_BG_T,
            'expected_D_BG': expected_D_BG,
            'conservation': conservation,
            'parameters': {
                'M_initial': self.M_initial,
                'epsilon': self.epsilon,
                'units': self.units,
                't_evap': t_evap
            }
        }

        if save_output:
            self.save_results()

        return self.results

    def validate(self):
        """Check validation criteria."""
        print("\nValidation:")
        print("-" * 60)

        validation = {}

        # Criterion 1: D_BG[T_H] constant to 1%
        pass1, stats1 = check_constant_derivative(
            self.results['D_BG_T'],
            self.results['expected_D_BG'],
            rtol=0.01
        )
        validation['D_BG_constant'] = stats1
        print(f"  [{'PASS' if pass1 else 'FAIL'}] D_BG[T_H] constant to 1%")
        print(f"      Mean: {stats1['mean']:.6f}, Expected: {stats1['expected']:.6f}")
        print(f"      Variation: {stats1['rel_variation']:.6f}")

        # Criterion 2: Information conserved to 1e-6
        S_total = (self.results['S_star_bh'] *
                   self.results['S_star_rad'] *
                   self.results['S_star_quantum'])
        pass2, stats2 = check_conservation(S_total, rtol=1e-6)
        validation['conservation'] = stats2
        print(f"  [{'PASS' if pass2 else 'FAIL'}] Information conserved to 1e-6")
        print(f"      Quality: {stats2['conservation_quality']}")
        print(f"      Relative error: {stats2['rel_error']:.6e}")

        # Criterion 3: No divergences in NNC
        pass3, stats3 = check_no_divergence(self.results['D_BG_T'])
        validation['no_divergence'] = stats3
        print(f"  [{'PASS' if pass3 else 'FAIL'}] No numerical divergences")
        print(f"      Max value: {stats3['max_value']:.6e}")

        # Criterion 4: Temperature evolution smooth
        dT_dt = np.gradient(self.results['T_H'], self.results['t'])
        pass4, stats4 = check_no_divergence(dT_dt, threshold=1e15)
        validation['smooth_evolution'] = stats4
        print(f"  [{'PASS' if pass4 else 'FAIL'}] Smooth temperature evolution")

        all_pass = pass1 and pass2 and pass3 and pass4

        self.validation = validation

        return validation, all_pass

    def save_results(self):
        """Save results to .npz file."""
        output_dir = Path(__file__).parent / "output"
        output_dir.mkdir(exist_ok=True)

        output_path = output_dir / "blackhole_evolution.npz"

        # Flatten conservation dict for saving
        conservation_flat = {
            f'conservation_{k}': v for k, v in self.results['conservation'].items()
        }

        # Flatten parameters dict
        params_flat = {
            f'param_{k}': v for k, v in self.results['parameters'].items()
            if not isinstance(v, str)
        }

        np.savez(
            output_path,
            t=self.results['t'],
            t_normalized=self.results['t_normalized'],
            M=self.results['M'],
            M_normalized=self.results['M_normalized'],
            r_s=self.results['r_s'],
            T_H=self.results['T_H'],
            S_BH=self.results['S_BH'],
            S_star_bh=self.results['S_star_bh'],
            S_star_rad=self.results['S_star_rad'],
            S_star_quantum=self.results['S_star_quantum'],
            dT_dM_classical=self.results['dT_dM_classical'],
            D_BG_T=self.results['D_BG_T'],
            expected_D_BG=self.results['expected_D_BG'],
            **conservation_flat,
            **params_flat
        )

        print(f"\nResults saved to: {output_path}")

    def plot_results(self):
        """Generate publication-quality plots."""
        plot_dir = Path(__file__).parent / "plots"
        plot_dir.mkdir(exist_ok=True)

        print("\nGenerating plots...")

        # Plot 1: Classical vs NNC derivatives
        plot_classical_vs_nnc(
            self.results['M_normalized'],
            self.results['dT_dM_classical'],
            self.results['D_BG_T'],
            xlabel='M / M_initial',
            ylabel='Derivative',
            title='Hawking Temperature Derivative',
            expected_nnc=self.results['expected_D_BG'],
            save_path=plot_dir / 'blackhole_derivative_comparison.png'
        )

        # Plot 2: Evolution
        observables = {
            'Mass (M/M_0)': self.results['M_normalized'],
            'Temperature (K)': self.results['T_H'],
            'Entropy (J/K)': self.results['S_BH']
        }
        plot_evolution(
            self.results['t_normalized'],
            observables,
            title='Black Hole Evolution',
            save_path=plot_dir / 'blackhole_evolution.png'
        )

        # Plot 3: Conservation
        S_total = (self.results['S_star_bh'] *
                   self.results['S_star_rad'] *
                   self.results['S_star_quantum'])
        plot_conservation(
            self.results['t_normalized'],
            S_total,
            title='Multiplicative Entropy Conservation',
            rtol=1e-6,
            save_path=plot_dir / 'blackhole_conservation.png'
        )

        print("Plots saved to:", plot_dir)


def main():
    """Run simulation with default parameters."""
    print("\n" + "=" * 80)
    print("SIMULATION 1: BLACK HOLE EVOLUTION")
    print("Testing NNC singularity regularization")
    print("=" * 80 + "\n")

    # Default parameters
    params = {
        'M_initial': 1.0,  # Planck masses
        'epsilon': 1e-3,   # Quantum correction
        'units': 'planck',
        'n_points': 1000
    }

    sim = BlackHoleEvolutionSim(**params)
    results = sim.run(save_output=True)
    validation, success = sim.validate()

    # Generate plots
    sim.plot_results()

    # Final report
    report = generate_validation_report(validation, "Black Hole Evolution")
    print(report)

    return results, validation


if __name__ == "__main__":
    results, validation = main()
