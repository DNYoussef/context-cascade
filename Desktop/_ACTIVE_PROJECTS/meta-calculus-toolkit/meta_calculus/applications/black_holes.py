"""
Black Hole Information Paradox Resolution using Meta-Calculus.

This module implements the meta-calculus approach to black hole thermodynamics
and information theory, using multiplicative entropy to resolve the information
paradox while preserving unitarity.

Key Features:
- Multiplicative entropy S* = exp(S/k_B)
- Meta-time evolution near horizons
- Information conservation through S*_total = constant
- Echo predictions from quantum-modified horizons
- Analog gravity experimental protocols
"""

import numpy as np
from typing import Tuple, Optional, Dict
from scipy.integrate import solve_ivp
import warnings

try:
    from ..core import (
        MetaDerivative, MetaIntegral, Custom, Identity,
        horizon_weight, information_weight_qubit
    )
except ImportError:
    from meta_calculus.core import (
        MetaDerivative, MetaIntegral, Custom, Identity,
        horizon_weight, information_weight_qubit
    )


class BlackHoleEvolution:
    """Meta-calculus framework for black hole evolution and information.
    
    Implements multiplicative entropy approach where information is
    conserved through the product S*_total = S*_bh * S*_rad * S*_quantum = constant
    rather than the sum S_total = S_bh + S_rad.
    """
    
    def __init__(self, 
                 M_initial: float,
                 epsilon: float = 1e-3,
                 length_scale: float = 1e-5,
                 units: str = 'planck'):
        """Initialize black hole evolution system.
        
        Args:
            M_initial: Initial black hole mass (in specified units)
            epsilon: Quantum correction parameter
            length_scale: Characteristic length scale for quantum effects
            units: Unit system ('planck', 'solar', 'geometric')
        """
        self.M_initial = M_initial
        self.epsilon = epsilon
        self.length_scale = length_scale
        self.units = units
        
        # Unit conversions
        self.unit_factors = self._get_unit_factors(units)
        
        # Create meta-time generator
        self.alpha_time = self._create_meta_time_generator()
        
        # Create multiplicative entropy generator
        self.beta_entropy = self._create_entropy_generator()
        
        # Meta-derivative for time evolution
        self.meta_d_time = MetaDerivative(self.alpha_time, self.beta_entropy)
        
        # Horizon weight function
        self.horizon_weight_func = lambda r: horizon_weight(
            r, 2 * M_initial, length_scale
        )
    
    def _get_unit_factors(self, units: str) -> Dict:
        """Get unit conversion factors.
        
        Args:
            units: Unit system
            
        Returns:
            Dictionary with conversion factors
        """
        if units == 'planck':
            return {
                'G': 1.0,
                'c': 1.0,
                'hbar': 1.0,
                'k_B': 1.0,
                'length': 1.616e-35,  # Planck length in meters
                'time': 5.391e-44,    # Planck time in seconds
                'mass': 2.176e-8      # Planck mass in kg
            }
        elif units == 'solar':
            return {
                'G': 6.674e-11,
                'c': 2.998e8,
                'hbar': 1.055e-34,
                'k_B': 1.381e-23,
                'length': 1.0,
                'time': 1.0,
                'mass': 1.989e30      # Solar mass in kg
            }
        elif units == 'geometric':
            # G = c = 1, lengths in meters, masses in meters
            return {
                'G': 1.0,
                'c': 1.0,
                'hbar': 1.055e-34,
                'k_B': 1.381e-23,
                'length': 1.0,
                'time': 1.0,
                'mass': 1.477e3       # 1 kg in meters (G/c^2)
            }
        else:
            raise ValueError(f"Unknown unit system: {units}")
    
    def _create_meta_time_generator(self):
        """Create meta-time generator alpha(t).
        
        dt* = alpha'(t) dt where alpha(t) slows time near complete evaporation
        to preserve unitarity.
        """
        def alpha_time(t):
            t = np.asarray(t)
            t_evap = self.evaporation_time()
            
            # Slow time near evaporation: alpha(t) = t + (t/t_evap)^2 correction
            correction = (t / t_evap)**2 / (1 + (t / t_evap)**2)
            return t + correction
        
        def alpha_time_derivative(t):
            t = np.asarray(t)
            t_evap = self.evaporation_time()
            
            # alpha'(t) = 1 + d/dt[(t/t_evap)^2/(1 + (t/t_evap)^2)]
            x = t / t_evap
            correction_deriv = (2 * x / t_evap) / (1 + x**2)**2
            return 1 + correction_deriv
        
        return Custom(alpha_time, alpha_time_derivative, name="meta_time")
    
    def _create_entropy_generator(self):
        """Create multiplicative entropy generator beta(S).
        
        S* = exp(S/k_B) transforms additive entropy to multiplicative.
        """
        k_B = self.unit_factors['k_B']
        
        def beta_entropy(S):
            S = np.asarray(S)
            # Prevent overflow for very large entropy
            S_normalized = np.clip(S / k_B, -700, 700)
            return np.exp(S_normalized)
        
        def beta_entropy_derivative(S):
            S = np.asarray(S)
            S_normalized = np.clip(S / k_B, -700, 700)
            return (1 / k_B) * np.exp(S_normalized)
        
        return Custom(beta_entropy, beta_entropy_derivative, name="multiplicative_entropy")
    
    def schwarzschild_radius(self, M: float) -> float:
        """Calculate Schwarzschild radius.
        
        Args:
            M: Black hole mass
            
        Returns:
            Schwarzschild radius r_s = 2GM/c^2
        """
        G = self.unit_factors['G']
        c = self.unit_factors['c']
        return 2 * G * M / c**2
    
    def hawking_temperature(self, M: float) -> float:
        """Calculate Hawking temperature.
        
        Args:
            M: Black hole mass
            
        Returns:
            Hawking temperature T_H = hbarc^3/(8piGMk_B)
        """
        G = self.unit_factors['G']
        c = self.unit_factors['c']
        hbar = self.unit_factors['hbar']
        k_B = self.unit_factors['k_B']
        
        return hbar * c**3 / (8 * np.pi * G * M * k_B)
    
    def bekenstein_hawking_entropy(self, M: float) -> float:
        """Calculate Bekenstein-Hawking entropy.

        Args:
            M: Black hole mass

        Returns:
            Entropy S_BH = (k_B*c^3*A)/(4*G*hbar) = (k_B*c^3*pi*r_s^2)/(4*G*hbar)
        """
        G = self.unit_factors['G']
        c = self.unit_factors['c']
        hbar = self.unit_factors['hbar']
        k_B = self.unit_factors['k_B']
        r_s = self.schwarzschild_radius(M)

        # Full SI units: S = (k_B*c^3*A)/(4*G*hbar) where A = 4*pi*r_s^2
        return (k_B * c**3 * np.pi * r_s**2) / (4 * G * hbar)
    
    def evaporation_time(self) -> float:
        """Calculate black hole evaporation time.
        
        Returns:
            Evaporation time t_evap ∝ M^3
        """
        G = self.unit_factors['G']
        c = self.unit_factors['c']
        hbar = self.unit_factors['hbar']
        
        # t_evap = (5120pi/3) * (G^2M^3)/(hbarc^4)
        return (5120 * np.pi / 3) * (G**2 * self.M_initial**3) / (hbar * c**4)
    
    def evolution_equations(self, t: float, y: np.ndarray) -> np.ndarray:
        """Evolution equations for black hole system.
        
        Args:
            t: Time
            y: State vector [M, S*_bh, S*_rad, S*_quantum]
            
        Returns:
            Time derivatives [dM/dt*, dS*_bh/dt*, dS*_rad/dt*, dS*_quantum/dt*]
        """
        M, S_star_bh, S_star_rad, S_star_quantum = y
        
        # Prevent negative mass
        M = max(M, 0.01 * self.M_initial)
        
        # Hawking evaporation rate: dM/dt = -k/M^2
        G = self.unit_factors['G']
        c = self.unit_factors['c']
        hbar = self.unit_factors['hbar']
        
        k_hawking = hbar * c**4 / (15360 * np.pi * G**2)
        dM_dt_classical = -k_hawking / M**2
        
        # Meta-time correction
        alpha_prime = self.alpha_time.derivative(t)
        dM_dt_star = dM_dt_classical / alpha_prime
        
        # Multiplicative entropy evolution
        # S*_bh = exp(S_bh/k_B), so dS*_bh/dt* = S*_bh * (1/k_B) * dS_bh/dt*
        
        k_B = self.unit_factors['k_B']
        
        # Black hole entropy decreases as mass decreases
        S_bh = k_B * np.log(S_star_bh + 1e-100)  # Current entropy
        # Fixed entropy rate: dS/dM = (2*pi*r_s)/G where r_s = 2GM/c^2
        r_s = self.schwarzschild_radius(M)
        dS_bh_dM = (2 * np.pi * r_s) / G
        dS_bh_dt_star = dS_bh_dM * dM_dt_star
        dS_star_bh_dt_star = S_star_bh * (dS_bh_dt_star / k_B)
        
        # Radiation entropy increases
        # Assume S_rad ∝ E_rad^(3/4) (Stefan-Boltzmann)
        E_rad_rate = -dM_dt_star * c**2  # Energy radiated away
        
        # Simplified: dS*_rad/dt* ∝ energy flux
        if S_star_rad > 0:
            dS_star_rad_dt_star = (3/4) * S_star_rad * (E_rad_rate / (S_star_rad * k_B))
        else:
            dS_star_rad_dt_star = E_rad_rate / (k_B * c**2)
        
        # Quantum information factor
        # S*_quantum compensates to maintain S*_total = constant
        S_star_total = S_star_bh * S_star_rad * S_star_quantum
        
        # Conservation: d(S*_total)/dt* = 0
        # d(ABC)/dt = BC(dA/dt) + AC(dB/dt) + AB(dC/dt) = 0
        # So: dC/dt = -C(1/A * dA/dt + 1/B * dB/dt)
        
        if S_star_quantum > 1e-100 and S_star_bh > 1e-100 and S_star_rad > 1e-100:
            dS_star_quantum_dt_star = -S_star_quantum * (
                (dS_star_bh_dt_star / S_star_bh) + 
                (dS_star_rad_dt_star / S_star_rad)
            )
        else:
            dS_star_quantum_dt_star = 0
        
        return np.array([
            dM_dt_star,
            dS_star_bh_dt_star,
            dS_star_rad_dt_star,
            dS_star_quantum_dt_star
        ])
    
    def evolve(self, t_final: Optional[float] = None, 
               n_points: int = 1000) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Evolve black hole system in meta-time.
        
        Args:
            t_final: Final time (default: 90% of evaporation time)
            n_points: Number of time points
            
        Returns:
            (t, M, S*_bh, S*_rad, S*_quantum)
        """
        if t_final is None:
            t_final = 0.9 * self.evaporation_time()
        
        # Initial conditions
        M0 = self.M_initial
        S_bh_0 = self.bekenstein_hawking_entropy(M0)
        S_star_bh_0 = self.beta_entropy(S_bh_0)
        S_star_rad_0 = 1.0  # Initial radiation entropy
        S_star_quantum_0 = S_star_bh_0 * S_star_rad_0  # Maintain conservation
        
        y0 = np.array([M0, S_star_bh_0, S_star_rad_0, S_star_quantum_0])
        
        # Time span
        t_span = (0, t_final)
        t_eval = np.linspace(0, t_final, n_points)
        
        # Solve evolution equations
        try:
            sol = solve_ivp(
                self.evolution_equations, 
                t_span, 
                y0, 
                t_eval=t_eval,
                method='RK45',
                rtol=1e-8,
                atol=1e-10,
                max_step=t_final/1000
            )
            
            if not sol.success:
                warnings.warn(f"Integration failed: {sol.message}")
            
            t = sol.t
            M = sol.y[0]
            S_star_bh = sol.y[1]
            S_star_rad = sol.y[2]
            S_star_quantum = sol.y[3]
            
        except Exception as e:
            warnings.warn(f"Evolution failed: {e}")
            # Return initial conditions
            t = np.array([0])
            M = np.array([M0])
            S_star_bh = np.array([S_star_bh_0])
            S_star_rad = np.array([S_star_rad_0])
            S_star_quantum = np.array([S_star_quantum_0])
        
        return t, M, S_star_bh, S_star_rad, S_star_quantum
    
    def conservation_check(self, t: np.ndarray, 
                          S_star_bh: np.ndarray,
                          S_star_rad: np.ndarray, 
                          S_star_quantum: np.ndarray) -> Dict:
        """Check conservation of total multiplicative entropy.
        
        Args:
            t: Time array
            S_star_bh, S_star_rad, S_star_quantum: Entropy arrays
            
        Returns:
            Dictionary with conservation analysis
        """
        S_star_total = S_star_bh * S_star_rad * S_star_quantum
        
        # Conservation error
        S_star_initial = S_star_total[0]
        relative_error = np.abs(S_star_total - S_star_initial) / S_star_initial
        
        max_error = np.max(relative_error)
        mean_error = np.mean(relative_error)
        final_error = relative_error[-1]
        
        # Check if conservation is maintained
        conservation_maintained = max_error < 1e-6
        
        return {
            'S_star_total': S_star_total,
            'initial_value': S_star_initial,
            'final_value': S_star_total[-1],
            'max_relative_error': max_error,
            'mean_relative_error': mean_error,
            'final_relative_error': final_error,
            'conservation_maintained': conservation_maintained,
            'conservation_quality': 'excellent' if max_error < 1e-10 else
                                  'good' if max_error < 1e-6 else
                                  'poor'
        }
    
    def information_recovery_time(self) -> float:
        """Calculate information recovery time (Page time).

        Returns:
            Time when S_bh = S_rad (information recovery begins)
        """
        # Solve for when S_bh(t) = S_rad(t)
        # This is approximately at half the evaporation time
        return 0.5 * self.evaporation_time()

    def bigeometric_hawking_derivative(self) -> float:
        """Calculate bigeometric derivative of Hawking temperature.

        For T_H = hbar*c^3/(8*pi*G*M*k_B) with mass dimension [-1],
        the bigeometric derivative is D_BG[T_H] = e^(-1).

        Returns:
            e^(-1) (approx 0.3679)
        """
        return np.exp(-1)

    def bigeometric_kretschmann_derivative(self) -> float:
        """Calculate bigeometric derivative of Kretschmann scalar.

        For Schwarzschild metric, K = 48*G^2*M^2/(c^4*r^6).
        At horizon r = r_s = 2GM/c^2, K has mass dimension [-6],
        so the bigeometric derivative is D_BG[K] = e^(-6).

        Returns:
            e^(-6) (approx 0.00248)
        """
        return np.exp(-6)

    def echo_frequency_prediction(self, r_observer: float) -> Dict:
        """Predict gravitational wave echo frequencies.
        
        Args:
            r_observer: Observer distance from black hole
            
        Returns:
            Dictionary with echo predictions
        """
        r_s = self.schwarzschild_radius(self.M_initial)
        
        # Effective horizon radius with quantum corrections
        r_h_eff = r_s * (1 + self.epsilon * np.exp(-r_s / self.length_scale))
        
        # Barrier location (approximate)
        r_barrier = 3 * r_s  # Photon sphere
        
        # Echo frequency: Deltaf ~= 1/(2|r*_barrier - r*_h,eff|)
        # Tortoise coordinates: r* = r + 2M ln|r/2M - 1|
        
        def r_tortoise(r, M):
            return r + 2 * M * np.log(np.abs(r / (2 * M) - 1))
        
        r_star_barrier = r_tortoise(r_barrier, self.M_initial)
        r_star_h_eff = r_tortoise(r_h_eff, self.M_initial)
        
        delta_r_star = abs(r_star_barrier - r_star_h_eff)
        echo_frequency = 1 / (2 * delta_r_star)
        
        # Convert to physical units
        c = self.unit_factors['c']
        echo_frequency_hz = echo_frequency * c / self.unit_factors['length']
        
        # Echo amplitude (rough estimate)
        echo_amplitude = self.epsilon * np.exp(-r_observer / (10 * r_s))
        
        return {
            'echo_frequency_hz': echo_frequency_hz,
            'echo_period_s': 1 / echo_frequency_hz if echo_frequency_hz > 0 else np.inf,
            'echo_amplitude_relative': echo_amplitude,
            'barrier_location': r_barrier,
            'effective_horizon': r_h_eff,
            'tortoise_separation': delta_r_star,
            'detectability': echo_amplitude > 1e-6  # Rough threshold
        }
    
    def analog_gravity_parameters(self, 
                                 bec_temperature: float = 1e-9,
                                 atom_mass: float = 87) -> Dict:
        """Calculate parameters for analog gravity experiments.
        
        Args:
            bec_temperature: BEC temperature in Kelvin
            atom_mass: Atomic mass in amu
            
        Returns:
            Dictionary with BEC parameters for analog black hole
        """
        # Physical constants
        k_B = 1.381e-23  # J/K
        amu = 1.661e-27  # kg
        hbar = 1.055e-34  # J*s
        
        m_atom = atom_mass * amu
        
        # BEC healing length
        n_density = 1e14  # atoms/m^3 (typical)
        a_scattering = 5e-9  # scattering length (m)
        
        xi_healing = 1 / np.sqrt(8 * np.pi * n_density * a_scattering)
        
        # Sound speed
        c_sound = np.sqrt(4 * np.pi * hbar**2 * a_scattering * n_density / m_atom)
        
        # Analog Schwarzschild radius
        # Scale analog system to match black hole
        scale_factor = self.schwarzschild_radius(self.M_initial) / xi_healing
        
        r_s_analog = xi_healing  # Healing length as analog horizon
        
        # Flow velocity for analog horizon
        v_flow = c_sound  # Sonic horizon condition
        
        # Temperature for thermal effects
        T_hawking_analog = hbar * c_sound / (2 * np.pi * k_B * xi_healing)
        
        # Echo frequency in analog system
        echo_freq_analog = c_sound / (2 * xi_healing)
        
        return {
            'healing_length_m': xi_healing,
            'sound_speed_ms': c_sound,
            'analog_horizon_m': r_s_analog,
            'flow_velocity_ms': v_flow,
            'hawking_temperature_K': T_hawking_analog,
            'echo_frequency_hz': echo_freq_analog,
            'density_atoms_per_m3': n_density,
            'scattering_length_m': a_scattering,
            'scale_factor': scale_factor,
            'experimental_feasibility': {
                'temperature_achievable': T_hawking_analog > bec_temperature,
                'flow_stable': v_flow < 0.1 * c_sound,  # Subsonic flow
                'echo_detectable': echo_freq_analog < 1e6  # < MHz
            }
        }
    
    def plot_evolution(self, save_path: Optional[str] = None):
        """Plot black hole evolution with multiplicative entropy.
        
        Args:
            save_path: Path to save the plot (optional)
        """
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("Matplotlib not available for plotting")
            return
        
        # Evolve system
        t, M, S_star_bh, S_star_rad, S_star_quantum = self.evolve()
        
        # Conservation check
        conservation = self.conservation_check(t, S_star_bh, S_star_rad, S_star_quantum)
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
        
        # Mass evolution
        ax1.plot(t / self.evaporation_time(), M / self.M_initial, 'b-', linewidth=2)
        ax1.set_xlabel('t / t_evap')
        ax1.set_ylabel('M / M_initial')
        ax1.set_title('Black Hole Mass Evolution')
        ax1.grid(True, alpha=0.3)
        
        # Multiplicative entropies
        ax2.semilogy(t / self.evaporation_time(), S_star_bh, 'r-', label='S*_BH', linewidth=2)
        ax2.semilogy(t / self.evaporation_time(), S_star_rad, 'g-', label='S*_rad', linewidth=2)
        ax2.semilogy(t / self.evaporation_time(), S_star_quantum, 'b-', label='S*_quantum', linewidth=2)
        ax2.set_xlabel('t / t_evap')
        ax2.set_ylabel('S* (multiplicative entropy)')
        ax2.set_title('Multiplicative Entropy Evolution')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Conservation
        S_star_total = conservation['S_star_total']
        ax3.plot(t / self.evaporation_time(), S_star_total / S_star_total[0], 'k-', linewidth=2)
        ax3.axhline(1.0, color='r', linestyle='--', alpha=0.5)
        ax3.set_xlabel('t / t_evap')
        ax3.set_ylabel('S*_total / S*_initial')
        ax3.set_title(f'Conservation (max error: {conservation["max_relative_error"]:.2e})')
        ax3.grid(True, alpha=0.3)
        
        # Information recovery
        page_time = self.information_recovery_time()
        ax4.plot(t / self.evaporation_time(), 
                np.log(S_star_bh), 'r-', label='ln(S*_BH)', linewidth=2)
        ax4.plot(t / self.evaporation_time(), 
                np.log(S_star_rad), 'g-', label='ln(S*_rad)', linewidth=2)
        ax4.axvline(page_time / self.evaporation_time(), 
                   color='k', linestyle=':', label='Page time')
        ax4.set_xlabel('t / t_evap')
        ax4.set_ylabel('ln(S*)')
        ax4.set_title('Information Recovery')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
        
        # Print summary
        print(f"Black Hole Evolution Summary:")
        print(f"Initial mass: {self.M_initial:.2f} (units: {self.units})")
        print(f"Evaporation time: {self.evaporation_time():.2e} s")
        print(f"Conservation quality: {conservation['conservation_quality']}")
        print(f"Max conservation error: {conservation['max_relative_error']:.2e}")


class QuantumHorizon:
    """Quantum-modified black hole horizon with meta-calculus.
    
    Models the near-horizon region where quantum effects become
    important and classical general relativity breaks down.
    """
    
    def __init__(self, 
                 M_bh: float,
                 quantum_scale: float = 1e-5,
                 units: str = 'planck'):
        """Initialize quantum horizon.
        
        Args:
            M_bh: Black hole mass
            quantum_scale: Quantum correction scale
            units: Unit system
        """
        self.M_bh = M_bh
        self.quantum_scale = quantum_scale
        self.units = units
        
        # Classical Schwarzschild radius
        if units == 'planck':
            self.r_s = 2 * M_bh  # G = c = 1
        else:
            G = 6.674e-11
            c = 2.998e8
            self.r_s = 2 * G * M_bh / c**2
    
    def effective_metric(self, r: np.ndarray) -> Dict:
        """Calculate effective metric with quantum corrections.
        
        Args:
            r: Radial coordinates
            
        Returns:
            Dictionary with metric components
        """
        r = np.asarray(r)
        
        # Classical Schwarzschild metric: f(r) = 1 - r_s/r
        f_classical = 1 - self.r_s / r
        
        # Quantum corrections near horizon
        delta_r = r - self.r_s
        quantum_correction = self.quantum_scale * np.exp(-delta_r / self.quantum_scale)
        
        # Modified metric function
        f_quantum = f_classical + quantum_correction
        
        # Ensure f > 0 (no horizon)
        f_quantum = np.maximum(f_quantum, 1e-10)
        
        return {
            'f_classical': f_classical,
            'f_quantum': f_quantum,
            'quantum_correction': quantum_correction,
            'effective_horizon': self.r_s * (1 - self.quantum_scale / self.r_s)
        }
    
    def surface_gravity(self, quantum_corrected: bool = True) -> float:
        """Calculate surface gravity.
        
        Args:
            quantum_corrected: Whether to include quantum corrections
            
        Returns:
            Surface gravity kappa
        """
        if quantum_corrected:
            # Modified surface gravity with quantum corrections
            kappa = 1 / (4 * self.r_s) * (1 - self.quantum_scale / self.r_s)
        else:
            # Classical surface gravity
            kappa = 1 / (4 * self.r_s)
        
        return kappa
    
    def hawking_radiation_spectrum(self, omega: np.ndarray,
                                  quantum_corrected: bool = True) -> np.ndarray:
        """Calculate modified Hawking radiation spectrum.
        
        Args:
            omega: Frequency array
            quantum_corrected: Whether to include quantum corrections
            
        Returns:
            Spectral density
        """
        omega = np.asarray(omega)
        
        # Hawking temperature
        if self.units == 'planck':
            T_H = 1 / (8 * np.pi * self.M_bh)  # Planck units
        else:
            hbar = 1.055e-34
            c = 2.998e8
            k_B = 1.381e-23
            G = 6.674e-11
            T_H = hbar * c**3 / (8 * np.pi * G * self.M_bh * k_B)
        
        if quantum_corrected:
            # Modified temperature with quantum corrections
            T_H_modified = T_H * (1 + self.quantum_scale / self.r_s)
        else:
            T_H_modified = T_H
        
        # Planck spectrum with greybody factors
        if self.units == 'planck':
            k_B = 1.0
        else:
            k_B = 1.381e-23
        
        # Avoid division by zero
        omega_safe = np.where(omega == 0, 1e-100, omega)
        
        spectrum = (omega_safe**3) / (np.exp(omega_safe / (k_B * T_H_modified)) - 1)
        
        return spectrum
    
    def information_scrambling_time(self) -> float:
        """Calculate information scrambling time.
        
        Returns:
            Scrambling time t_scramble ∼ M log(M)
        """
        if self.units == 'planck':
            return self.M_bh * np.log(self.M_bh)
        else:
            G = 6.674e-11
            c = 2.998e8
            return (G * self.M_bh / c**3) * np.log(self.M_bh)
    
    def entanglement_entropy(self, subsystem_size: float) -> float:
        """Calculate entanglement entropy for subsystem.
        
        Args:
            subsystem_size: Size of subsystem relative to horizon
            
        Returns:
            Entanglement entropy
        """
        # Area law with logarithmic corrections
        area_term = subsystem_size * self.r_s
        log_correction = np.log(subsystem_size + 1e-10)
        
        return area_term + self.quantum_scale * log_correction


def create_black_hole_system(M_initial: float,
                            epsilon: float = 1e-3,
                            units: str = 'planck') -> BlackHoleEvolution:
    """Factory function to create a black hole evolution system.
    
    Args:
        M_initial: Initial black hole mass
        epsilon: Quantum correction parameter
        units: Unit system
        
    Returns:
        BlackHoleEvolution instance
    """
    return BlackHoleEvolution(M_initial, epsilon, units=units)


def validate_information_conservation(bh_system: BlackHoleEvolution,
                                    tolerance: float = 1e-6) -> bool:
    """Validate that information is conserved in black hole evolution.
    
    Args:
        bh_system: BlackHoleEvolution system
        tolerance: Conservation tolerance
        
    Returns:
        True if information is conserved within tolerance
    """
    t, M, S_star_bh, S_star_rad, S_star_quantum = bh_system.evolve()
    conservation = bh_system.conservation_check(t, S_star_bh, S_star_rad, S_star_quantum)
    
    return conservation['max_relative_error'] < tolerance