"""
Quantum-Classical Transition using Meta-Calculus.

This module implements the meta-calculus approach to the quantum-classical
transition, where a scale-dependent generator smoothly interpolates between
quantum (additive) and classical (multiplicative) regimes.

Key Features:
- Modified Schrodinger equation with meta-calculus corrections
- Energy spectrum modifications in quantum dots
- Transition probability calculations
- Experimental predictions for STM spectroscopy
"""

import numpy as np
from typing import Tuple, Optional, Callable, Dict
# Removed unused imports

try:
    from ..core import ScaleDependent, MetaDerivative, Identity, Power
except ImportError:
    from meta_calculus.core import ScaleDependent, MetaDerivative, Identity, Power


class QuantumClassicalTransition:
    """Meta-calculus framework for quantum-classical transitions.
    
    Implements the scale-dependent generator approach where quantum
    and classical physics are unified through a single mathematical
    framework that transitions smoothly between regimes.
    """
    
    def __init__(self, 
                 scale_length: float = 1e-7,
                 energy_scale: float = 1e-3,
                 n_cutoff: float = 100):
        """Initialize quantum-classical transition system.
        
        Args:
            scale_length: Characteristic length scale ℓ (meters)
            energy_scale: Characteristic energy scale (eV)
            n_cutoff: Cutoff for quantum number corrections
        """
        self.scale_length = scale_length
        self.energy_scale = energy_scale
        self.n_cutoff = n_cutoff
        
        # Create scale-dependent generator
        self.alpha = ScaleDependent(scale_length)
        
        # Energy-dependent beta generator
        self.beta = self._create_energy_generator()
        
        # Meta-derivative operator
        self.meta_d = MetaDerivative(self.alpha, self.beta)
    
    def _create_energy_generator(self) -> Callable:
        """Create energy-dependent beta generator.
        
        beta(E) = E + (hbaromega/E_c) * ln(1 + E/hbaromega)
        
        This provides logarithmic corrections at high energies.
        """
        def beta_energy(E):
            E = np.asarray(E)
            hbar_omega = self.energy_scale
            E_c = self.energy_scale * self.n_cutoff
            
            # Avoid division by zero
            E_safe = np.where(np.abs(E) < 1e-100, 1e-100, E)
            
            # Logarithmic correction term
            correction = (hbar_omega / E_c) * np.log(1 + np.abs(E_safe) / hbar_omega)
            
            return E_safe + correction
        
        def beta_energy_derivative(E):
            E = np.asarray(E)
            hbar_omega = self.energy_scale
            E_c = self.energy_scale * self.n_cutoff
            
            E_safe = np.where(np.abs(E) < 1e-100, 1e-100, E)
            
            # d/dE [E + (hbaromega/E_c) * ln(1 + E/hbaromega)]
            correction_deriv = (hbar_omega / E_c) / (hbar_omega + np.abs(E_safe))
            
            return 1 + correction_deriv
        
        # Create custom generator
        from ..core import Custom
        return Custom(beta_energy, beta_energy_derivative, name="energy_dependent")
    
    def modified_hamiltonian(self, H_classical: np.ndarray, 
                           position_scale: float = None) -> np.ndarray:
        """Compute modified Hamiltonian with meta-calculus corrections.
        
        H_eff = H * [1 + delta(n/n_c)] * [alpha'(x)/alpha'_classical(x)]
        
        Args:
            H_classical: Classical Hamiltonian matrix
            position_scale: Characteristic position scale
            
        Returns:
            Modified Hamiltonian with meta-calculus corrections
        """
        if position_scale is None:
            position_scale = self.scale_length
        
        # For harmonic oscillator: H = hbaromega(a†a + 1/2)
        # Eigenvalues are E_n = hbaromega(n + 1/2)
        
        # Extract quantum numbers from diagonal elements
        eigenvals = np.diag(H_classical)
        n_quantum = eigenvals / self.energy_scale - 0.5
        
        # Correction factor delta(n/n_c)
        n_ratio = n_quantum / self.n_cutoff
        correction_factor = np.exp(-n_ratio**2) * (1 + n_ratio**2 * np.tanh(n_ratio))
        
        # Scale-dependent correction
        x_typical = position_scale
        alpha_prime_ratio = (self.alpha.derivative(x_typical) / 
                           x_typical)  # alpha'(x) / alpha'_classical(x) where alpha'_classical = 1
        
        # Apply corrections to Hamiltonian
        H_modified = H_classical.copy()
        for i in range(len(eigenvals)):
            H_modified[i, i] *= (1 + correction_factor[i]) * alpha_prime_ratio
        
        return H_modified
    
    def energy_spectrum_corrections(self, n_levels: int = 200) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Calculate energy spectrum corrections for quantum dot.
        
        Args:
            n_levels: Number of energy levels to compute
            
        Returns:
            (n, E_classical, E_modified, relative_deviation)
        """
        n = np.arange(1, n_levels + 1)
        
        # Classical harmonic oscillator energies
        E_classical = self.energy_scale * (n + 0.5)
        
        # Meta-calculus corrections
        n_ratio = n / self.n_cutoff
        
        # Correction term: deltaE_n/E_n
        delta_factor = 0.5 * np.exp(-n_ratio**2) * (1 + n_ratio**2 * np.tanh(n_ratio))
        
        # Modified energies
        E_modified = E_classical * (1 + delta_factor)
        
        # Relative deviation
        relative_deviation = (E_modified - E_classical) / E_classical
        
        return n, E_classical, E_modified, relative_deviation
    
    def find_maximum_deviation(self, n_max: int = 500) -> Tuple[int, float]:
        """Find quantum number with maximum energy deviation.
        
        Args:
            n_max: Maximum quantum number to search
            
        Returns:
            (n_max_deviation, max_deviation)
        """
        n, _, _, deviations = self.energy_spectrum_corrections(n_max)
        
        max_idx = np.argmax(np.abs(deviations))
        n_max_dev = n[max_idx]
        max_dev = deviations[max_idx]
        
        return n_max_dev, max_dev
    
    def transition_probability(self, n_initial: int, n_final: int,
                             time: float = 1.0) -> float:
        """Calculate modified transition probability between energy levels.
        
        Uses meta-calculus corrections to the time evolution operator.
        
        Args:
            n_initial: Initial quantum number
            n_final: Final quantum number
            time: Evolution time
            
        Returns:
            Transition probability |<n_f|U(t)|n_i>|^2
        """
        # Get energy corrections
        n_max = max(n_initial, n_final) + 10
        n, E_classical, E_modified, _ = self.energy_spectrum_corrections(n_max)
        
        if n_initial >= len(E_modified) or n_final >= len(E_modified):
            return 0.0
        
        # Energy difference with corrections
        E_i = E_modified[n_initial - 1] if n_initial > 0 else 0
        E_f = E_modified[n_final - 1] if n_final > 0 else 0
        
        # Modified time evolution
        # In meta-calculus: dt* = alpha'(t) dt
        # For simplicity, assume alpha'(t) ~= 1 + small corrections
        alpha_prime_correction = 1 + 0.01 * np.exp(-time / (self.scale_length * 1e7))
        
        effective_time = time * alpha_prime_correction
        
        # Transition amplitude (simplified)
        if n_initial == n_final:
            # Diagonal element
            phase = np.exp(-1j * E_i * effective_time / (6.582e-16))  # hbar in eV*s
            return np.abs(phase)**2
        else:
            # Off-diagonal transitions (perturbative)
            coupling = 0.01 * self.energy_scale  # Weak coupling
            delta_E = E_f - E_i
            
            if abs(delta_E) < 1e-100:
                return 0.0
            
            # First-order perturbation theory
            amplitude = (coupling / delta_E) * (
                np.exp(-1j * E_f * effective_time / (6.582e-16)) - 
                np.exp(-1j * E_i * effective_time / (6.582e-16))
            )
            
            return np.abs(amplitude)**2
    
    def coherence_time(self, n_quantum: int, 
                      decoherence_rate: float = 1e-12) -> float:
        """Calculate modified coherence time with meta-calculus corrections.
        
        Args:
            n_quantum: Quantum number
            decoherence_rate: Base decoherence rate (1/s)
            
        Returns:
            Modified coherence time (seconds)
        """
        # Meta-calculus correction to decoherence
        n_ratio = n_quantum / self.n_cutoff
        
        # Decoherence suppression in quantum regime
        suppression_factor = np.exp(-n_ratio**2)
        
        # Modified decoherence rate
        gamma_modified = decoherence_rate * (1 - 0.5 * suppression_factor)
        
        # Coherence time
        return 1.0 / gamma_modified if gamma_modified > 0 else np.inf
    
    def experimental_signature(self, energy_resolution: float = 2e-6) -> Dict:
        """Calculate experimental signatures for STM spectroscopy.
        
        Args:
            energy_resolution: Energy resolution in eV
            
        Returns:
            Dictionary with experimental predictions
        """
        # Find optimal measurement parameters
        n_max_dev, max_deviation = self.find_maximum_deviation()
        
        # Energy scale for the deviation
        energy_deviation = max_deviation * self.energy_scale
        
        # Signal-to-noise ratio
        snr = energy_deviation / energy_resolution
        
        # Measurement feasibility
        measurable = snr > 3.0  # 3sigma detection threshold
        
        # Optimal quantum numbers for measurement
        n, _, _, deviations = self.energy_spectrum_corrections(200)
        significant_deviations = n[np.abs(deviations) > 0.001]  # > 0.1%
        
        return {
            'max_deviation_n': n_max_dev,
            'max_deviation_percent': max_deviation * 100,
            'energy_deviation_eV': energy_deviation,
            'signal_to_noise_ratio': snr,
            'measurable': measurable,
            'required_resolution_eV': energy_deviation / 3.0,
            'optimal_n_range': (significant_deviations[0], significant_deviations[-1]),
            'measurement_time_estimate': self._estimate_measurement_time(snr)
        }
    
    def _estimate_measurement_time(self, snr: float) -> float:
        """Estimate measurement time for given signal-to-noise ratio.
        
        Args:
            snr: Signal-to-noise ratio
            
        Returns:
            Estimated measurement time in seconds
        """
        # Typical STM measurement parameters
        base_time = 1.0  # 1 second base measurement
        
        # Time scales as 1/SNR^2 for shot noise limited measurements
        if snr > 0:
            return base_time / snr**2
        else:
            return np.inf
    
    def plot_energy_spectrum(self, n_max: int = 150, 
                           save_path: Optional[str] = None):
        """Plot energy spectrum with meta-calculus corrections.
        
        Args:
            n_max: Maximum quantum number to plot
            save_path: Path to save the plot (optional)
        """
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("Matplotlib not available for plotting")
            return
        
        n, E_classical, E_modified, deviations = self.energy_spectrum_corrections(n_max)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Energy spectrum
        ax1.plot(n, E_classical * 1000, 'b-', label='Classical', linewidth=2)
        ax1.plot(n, E_modified * 1000, 'r--', label='Meta-calculus', linewidth=2)
        ax1.set_xlabel('Quantum number n')
        ax1.set_ylabel('Energy (meV)')
        ax1.set_title('Energy Spectrum: Classical vs Meta-Calculus')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Relative deviations
        ax2.plot(n, deviations * 100, 'g-', linewidth=2)
        ax2.axhline(0, color='k', linestyle=':', alpha=0.5)
        ax2.set_xlabel('Quantum number n')
        ax2.set_ylabel('Relative deviation (%)')
        ax2.set_title('Meta-Calculus Energy Corrections')
        ax2.grid(True, alpha=0.3)
        
        # Mark maximum deviation
        n_max_dev, max_dev = self.find_maximum_deviation(n_max)
        ax2.plot(n_max_dev, max_dev * 100, 'ro', markersize=8, 
                label=f'Max: {max_dev*100:.2f}% at n={n_max_dev}')
        ax2.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def generate_stm_protocol(self) -> Dict:
        """Generate detailed STM measurement protocol.
        
        Returns:
            Dictionary with experimental protocol details
        """
        exp_sig = self.experimental_signature()
        
        protocol = {
            'sample_preparation': {
                'material': 'GaAs quantum dot',
                'size': f'{self.scale_length*1e9:.0f} nm diameter',
                'confinement_energy': f'{self.energy_scale*1000:.1f} meV',
                'temperature': '4.2 K (liquid helium)',
                'magnetic_field': '0 T (zero field)'
            },
            
            'stm_parameters': {
                'tip_material': 'Tungsten or PtIr',
                'bias_voltage_range': f'+/-{self.energy_scale*2:.3f} V',
                'current_setpoint': '10 pA',
                'energy_resolution': f'{exp_sig["required_resolution_eV"]*1e6:.1f} mueV',
                'spatial_resolution': f'{self.scale_length*1e9/10:.1f} nm'
            },
            
            'measurement_sequence': {
                'step_1': 'Locate quantum dot using topographic imaging',
                'step_2': f'Position tip over dot center (+/-{self.scale_length*1e9/20:.1f} nm)',
                'step_3': f'Record dI/dV spectrum from n={exp_sig["optimal_n_range"][0]} to n={exp_sig["optimal_n_range"][1]}',
                'step_4': f'Integration time: {exp_sig["measurement_time_estimate"]:.1f} s per point',
                'step_5': 'Repeat at multiple tip positions for statistics'
            },
            
            'data_analysis': {
                'peak_identification': 'Fit Gaussian peaks to dI/dV spectrum',
                'energy_extraction': 'Extract peak positions with mueV precision',
                'deviation_calculation': 'Compare with harmonic oscillator model',
                'significance_test': f'Require SNR > 3 (current: {exp_sig["signal_to_noise_ratio"]:.1f})'
            },
            
            'expected_results': {
                'maximum_deviation': f'{exp_sig["max_deviation_percent"]:.2f}%',
                'optimal_quantum_number': exp_sig['max_deviation_n'],
                'measurability': 'Yes' if exp_sig['measurable'] else 'No',
                'required_improvements': [] if exp_sig['measurable'] else [
                    f'Improve energy resolution to {exp_sig["required_resolution_eV"]*1e6:.1f} mueV',
                    'Reduce thermal broadening (lower temperature)',
                    'Minimize vibrational noise'
                ]
            }
        }
        
        return protocol


class QuantumDotSpectrum:
    """Specialized class for quantum dot spectroscopy calculations.
    
    Provides detailed calculations for experimental quantum dot
    measurements with meta-calculus corrections.
    """
    
    def __init__(self, 
                 dot_radius: float = 50e-9,
                 material: str = 'GaAs',
                 confinement_strength: float = 1.5e-3):
        """Initialize quantum dot spectrum calculator.
        
        Args:
            dot_radius: Quantum dot radius (meters)
            material: Semiconductor material
            confinement_strength: Confinement energy scale (eV)
        """
        self.dot_radius = dot_radius
        self.material = material
        self.confinement_strength = confinement_strength
        
        # Material properties
        self.material_properties = self._get_material_properties(material)
        
        # Create quantum-classical transition system
        self.qc_system = QuantumClassicalTransition(
            scale_length=dot_radius,
            energy_scale=confinement_strength,
            n_cutoff=100
        )
    
    def _get_material_properties(self, material: str) -> Dict:
        """Get material-specific properties.
        
        Args:
            material: Material name
            
        Returns:
            Dictionary with material properties
        """
        properties = {
            'GaAs': {
                'effective_mass': 0.067,  # m*/m_e
                'dielectric_constant': 12.9,
                'band_gap': 1.424,  # eV at 300K
                'lattice_constant': 5.653e-10  # meters
            },
            'InAs': {
                'effective_mass': 0.023,
                'dielectric_constant': 15.15,
                'band_gap': 0.354,
                'lattice_constant': 6.058e-10
            },
            'Si': {
                'effective_mass': 0.26,
                'dielectric_constant': 11.68,
                'band_gap': 1.12,
                'lattice_constant': 5.431e-10
            }
        }
        
        return properties.get(material, properties['GaAs'])
    
    def calculate_confinement_energy(self) -> float:
        """Calculate quantum confinement energy.
        
        Returns:
            Confinement energy in eV
        """
        # Particle in a box model: E = hbar^2pi^2/(2m*L^2)
        hbar = 1.055e-34  # J*s
        m_e = 9.109e-31   # kg
        eV_to_J = 1.602e-19
        
        m_eff = self.material_properties['effective_mass'] * m_e
        L = 2 * self.dot_radius
        
        E_confinement = (hbar**2 * np.pi**2) / (2 * m_eff * L**2)
        
        return E_confinement / eV_to_J  # Convert to eV
    
    def thermal_broadening(self, temperature: float = 4.2) -> float:
        """Calculate thermal broadening of energy levels.
        
        Args:
            temperature: Temperature in Kelvin
            
        Returns:
            Thermal broadening FWHM in eV
        """
        k_B = 8.617e-5  # eV/K
        return 2.35 * k_B * temperature  # FWHM = 2.35 * sigma for Gaussian
    
    def lifetime_broadening(self, n_quantum: int) -> float:
        """Calculate lifetime broadening for given quantum state.
        
        Args:
            n_quantum: Quantum number
            
        Returns:
            Lifetime broadening in eV
        """
        # Estimate from meta-calculus coherence time
        coherence_time = self.qc_system.coherence_time(n_quantum)
        hbar_eV = 6.582e-16  # eV*s
        
        return hbar_eV / coherence_time if coherence_time > 0 else 0
    
    def total_linewidth(self, n_quantum: int, temperature: float = 4.2) -> float:
        """Calculate total linewidth including all broadening mechanisms.
        
        Args:
            n_quantum: Quantum number
            temperature: Temperature in Kelvin
            
        Returns:
            Total linewidth FWHM in eV
        """
        thermal = self.thermal_broadening(temperature)
        lifetime = self.lifetime_broadening(n_quantum)
        instrumental = 1e-6  # 1 mueV instrumental broadening
        
        # Add in quadrature
        return np.sqrt(thermal**2 + lifetime**2 + instrumental**2)
    
    def detection_probability(self, n_quantum: int, 
                            measurement_time: float = 1.0) -> float:
        """Calculate probability of detecting energy level deviation.
        
        Args:
            n_quantum: Quantum number
            measurement_time: Measurement time in seconds
            
        Returns:
            Detection probability (0-1)
        """
        # Get energy deviation
        n, _, _, deviations = self.qc_system.energy_spectrum_corrections(n_quantum + 10)
        if n_quantum >= len(deviations):
            return 0.0
        
        deviation = abs(deviations[n_quantum - 1])
        energy_deviation = deviation * self.confinement_strength
        
        # Total linewidth
        linewidth = self.total_linewidth(n_quantum)
        
        # Signal-to-noise ratio
        snr = energy_deviation / linewidth
        
        # Detection probability (assuming Gaussian statistics)
        # P = 1 - exp(-SNR^2/2) for SNR >> 1
        if snr > 0.1:
            return 1 - np.exp(-snr**2 / 2)
        else:
            return snr**2 / 2  # Small SNR approximation
    
    def optimize_measurement_conditions(self) -> Dict:
        """Optimize experimental conditions for maximum sensitivity.
        
        Returns:
            Dictionary with optimized conditions
        """
        # Find optimal quantum number
        n_max_dev, max_dev = self.qc_system.find_maximum_deviation()
        
        # Optimize temperature
        temperatures = np.linspace(0.3, 10, 50)  # 0.3K to 10K
        detection_probs = []
        
        for T in temperatures:
            linewidth = self.thermal_broadening(T)
            energy_dev = max_dev * self.confinement_strength
            snr = energy_dev / linewidth
            prob = 1 - np.exp(-snr**2 / 2) if snr > 0.1 else snr**2 / 2
            detection_probs.append(prob)
        
        optimal_temp_idx = np.argmax(detection_probs)
        optimal_temp = temperatures[optimal_temp_idx]
        
        return {
            'optimal_quantum_number': n_max_dev,
            'optimal_temperature_K': optimal_temp,
            'maximum_detection_probability': detection_probs[optimal_temp_idx],
            'required_energy_resolution_eV': max_dev * self.confinement_strength / 3,
            'measurement_feasibility': detection_probs[optimal_temp_idx] > 0.9,
            'recommended_conditions': {
                'temperature': f'{optimal_temp:.1f} K',
                'measurement_time': '10-100 seconds per spectrum',
                'tip_stability': '< 0.1 Å drift',
                'vibration_isolation': '< 0.01 Å RMS'
            }
        }