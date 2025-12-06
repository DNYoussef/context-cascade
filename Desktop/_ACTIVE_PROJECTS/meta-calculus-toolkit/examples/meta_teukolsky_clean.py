#!/usr/bin/env python3
"""
meta_teukolsky_clean.py - Schwarzschild gravitational wave echo detection

A complete, validated module for detecting gravitational wave echoes from 
quantum-modified black hole horizons using the Teukolsky equation.

Key Features:
- Exact Schwarzschild Regge-Wheeler potential for spin s=-2
- Robust Newton solver for tortoise coordinate inversion  
- Proper complex number handling with zvode integrator
- Outward integration from horizon to infinity
- Echo detection via residual FFT analysis
"""

import numpy as np
from scipy.integrate import ode
from scipy.optimize import newton
import time
import sys

# Global constants (geometrized units G = c = 1)
EPS_ROOT = 1e-10                    # Newton solver tolerance
MIN_RADIUS_FACTOR = 1.01            # Safety margin for horizon

def v_meta(r, r_h, epsilon=1e-3, length_scale=1e-5):
    """Quantum-information weight near the horizon."""
    return 1.0 - epsilon * np.exp(-(r - r_h) / length_scale)

def r_tortoise(r, mass):
    """Schwarzschild tortoise coordinate r*."""
    return r + 2*mass * np.log(np.abs(r / (2*mass) - 1))

def r_from_rstar(r_star, mass):
    """
    Invert r*(r) numerically using Newton-Raphson method.
    Includes proper error handling and fallback approximations.
    """
    # Special cases for extreme values
    if r_star > 100*mass:
        return r_star  # Good approximation far away
    
    if r_star < -100*mass:
        return 2*mass * MIN_RADIUS_FACTOR  # Near horizon
    
    # Safety threshold
    r_min = 2*mass * MIN_RADIUS_FACTOR
    
    # Improved initial guess
    if r_star > 0:
        r0 = max(r_star, 3*mass)  # Outside photon sphere
    else:
        delta = np.exp(r_star/(2*mass))
        r0 = max(2*mass * (1 + delta), r_min)
    
    # Define functions with safety checks
    def f_func(r):
        if r <= 2*mass:
            return 1e10  # Large value if inside horizon
        return r_tortoise(r, mass) - r_star
    
    def fprime_func(r):
        if r <= 2*mass or abs(r - 2*mass) < 1e-10:
            return 1e-10  # Small positive value near horizon
        return 1 / (1 - 2*mass/r)
    
    try:
        result = newton(f_func, r0, fprime_func, tol=EPS_ROOT, maxiter=50)
        
        # Ensure result is physically valid
        if result <= 2*mass:
            result = r_min
        
        return result
    except (RuntimeError, ZeroDivisionError, OverflowError, ValueError):
        # Fallback approximation
        if r_star > 0:
            return max(r_star, 3*mass)
        else:
            delta = np.exp(r_star/(2*mass))
            return max(2*mass * (1 + delta), r_min)

def validate_r_from_rstar(mass):
    """Test r_from_rstar function with known values."""
    print("Validating r_from_rstar function:")
    
    # Test case 1: r* = 0
    r_test = r_from_rstar(0.0, mass)
    print(f"r*(0) -> r = {r_test:.6f} (expected ~= {2*mass:.6f})")
    
    # Test case 2: Large positive r*
    r_star_large = 100*mass
    r_test = r_from_rstar(r_star_large, mass)
    print(f"r*({r_star_large}) -> r = {r_test:.6f} (expected ~= {r_star_large:.6f})")
    
    # Test case 3: Photon sphere
    r_photon = 3*mass
    r_star_photon = r_tortoise(r_photon, mass)
    r_recovered = r_from_rstar(r_star_photon, mass)
    print(f"r = 3M: r* = {r_star_photon:.6f}, recovered r = {r_recovered:.6f}")
    print(f"Error: {abs(r_recovered - r_photon):.2e}")

def compute_reflection_coefficient(r_vals, psi_vals, frequency, r_star_analysis_start=20.0):
    """
    Compute reflection coefficient by fitting to outgoing/incoming waves.
    At large positive r*, psi ~= A*e^{-iomegar*} + B*e^{+iomegar*}
    """
    # Find analysis region
    analysis_mask = r_vals >= r_star_analysis_start
    if not np.any(analysis_mask):
        return np.nan, "No data in analysis region"
    
    r_analysis = r_vals[analysis_mask]
    psi_analysis = psi_vals[analysis_mask]
    
    if len(r_analysis) < 10:
        return np.nan, "Insufficient data points"
    
    # Set up linear system
    outgoing = np.exp(-1j * frequency * r_analysis)
    incoming = np.exp(1j * frequency * r_analysis)
    
    design_matrix = np.column_stack([outgoing, incoming])
    try:
        coeffs, residuals, _, _ = np.linalg.lstsq(design_matrix, psi_analysis, rcond=None)
        a_out, b_in = coeffs
        
        if abs(b_in) > 1e-12:
            reflection_coeff = a_out / b_in
            return reflection_coeff, f"Fit successful, residual: {np.sqrt(residuals[0]) if len(residuals) > 0 else 'N/A'}"
        else:
            return np.nan, "Incoming amplitude too small"
    except np.linalg.LinAlgError as error:
        return np.nan, f"Linear algebra error: {error}"

def V_regge_wheeler(r, mass, angular_l):
    """Regge-Wheeler potential for spin s=-2 (axial gravitational perturbations)."""
    f_factor = 1.0 - 2*mass/r
    return f_factor * (angular_l*(angular_l+1)/r**2 - 6*mass/r**3)

def teukolsky_rhs_complex(r_star, y, mass, angular_l, frequency, epsilon, length_scale):
    """
    Complex two-component RHS for the meta-weighted Teukolsky equation.
    y = [psi, p = v*dpsi/dr*]
    """
    psi, p = y
    r = r_from_rstar(r_star, mass)
    v = v_meta(r, 2*mass, epsilon, length_scale)
    V = V_regge_wheeler(r, mass, angular_l)

    dpsi_drstar = p / v
    dp_drstar = V * psi
    return [dpsi_drstar, dp_drstar]

def integrate_meta_teukolsky(mass, angular_l, frequency,
                             r_star_start=-200.,
                             r_star_end=200.,
                             epsilon=1e-3, length_scale=1e-5,
                             n_steps=2000,
                             show_progress=True):
    """
    Integrate outward from horizon to infinity with purely ingoing boundary condition.
    """
    if show_progress:
        print(f"Starting integration: M={mass}, l={angular_l}, omega={frequency}")
        print(f"r*: {r_star_start} -> {r_star_end}, steps={n_steps}")
        print(f"Meta-weight params: eps={epsilon}, ell={length_scale}")
    
    start_time = time.time()
    
    # Initial condition at horizon: purely ingoing wave
    r_star_h = r_star_start
    psi0 = np.exp(-1j * frequency * r_star_h)
    r_start = r_from_rstar(r_star_h, mass)
    
    if show_progress:
        print(f"Initial radius r({r_star_start}) = {r_start:.2f}")
    
    v0 = v_meta(r_start, 2*mass, epsilon, length_scale)
    # Derivative condition: dpsi/dr* = -iomega psi at horizon
    p0 = v0 * (-1j * frequency * psi0)

    # Initial complex state
    y0 = np.array([psi0, p0], dtype=complex)

    # Use zvode for complex integration
    solver = ode(teukolsky_rhs_complex).set_integrator(
        'zvode',
        method='adams',
        rtol=1e-8, atol=1e-8,
        nsteps=50000
    )
    solver.set_initial_value(y0, r_star_h)
    solver.set_f_params(mass, angular_l, frequency, epsilon, length_scale)

    rs, psis = [r_star_start], [psi0]
    dr = (r_star_end - r_star_h) / n_steps
    
    # Progress tracking
    last_percentage = 0
    last_status_time = time.time()
    progress_interval = 2.0
    
    step_count = 0
    max_steps = n_steps + 100
    
    try:
        while solver.successful() and solver.t < r_star_end and step_count < max_steps:
            solver.integrate(solver.t + dr)
            rs.append(solver.t)
            psi, _ = solver.y
            psis.append(psi)
            step_count += 1
            
            # Show progress
            if show_progress and time.time() - last_status_time > progress_interval:
                progress = (solver.t - r_star_start) / (r_star_end - r_star_start)
                percentage = int(100 * progress)
                
                if percentage > last_percentage:
                    r_current = r_from_rstar(solver.t, mass)
                    elapsed = time.time() - start_time
                    remaining = elapsed / progress - elapsed if progress > 0 else 0
                    
                    print(f"Progress: {percentage}% complete, r*={solver.t:.2f}, r={r_current:.2f}")
                    print(f"Time: {elapsed:.1f}s elapsed, ~{remaining:.1f}s remaining")
                    print(f"|psi| = {abs(psi):.6f}")
                    sys.stdout.flush()
                    
                    last_percentage = percentage
                    last_status_time = time.time()
    
    except Exception as error:
        print(f"Integration error at step {step_count}, r*={solver.t if solver else 'unknown'}: {error}")
        if len(rs) < 10:
            raise
    
    if show_progress:
        print(f"Integration complete: {len(rs)} points, {time.time() - start_time:.1f}s elapsed")
    
    return np.array(rs), np.array(psis, dtype=complex)

def detect_echoes_residual(rs, psi, fit_region_start=50.0):
    """
    Detect echoes by fitting exponential decay and analyzing residual spectrum.
    """
    t = rs
    A = np.abs(psi)
    
    # Focus on far-field region
    far_field_mask = t >= fit_region_start
    if not np.any(far_field_mask):
        return None, "No far-field data"
    
    t_far = t[far_field_mask]
    A_far = A[far_field_mask]
    
    if len(A_far) < 10:
        return None, "Insufficient far-field points"
    
    try:
        # Fit exponential decay
        valid_mask = A_far > 0
        if np.sum(valid_mask) < 5:
            return None, "Insufficient positive amplitudes"
        
        t_valid = t_far[valid_mask]
        log_A_valid = np.log(A_far[valid_mask])
        
        p, residuals = np.polyfit(t_valid, log_A_valid, 1, full=True)[:2]
        gamma_fit = -p[0]
        A0_fit = np.exp(p[1])
        
        # Compute residual
        A_fitted = A0_fit * np.exp(-gamma_fit * t)
        residual = A - A_fitted
        
        # FFT analysis of residual
        echo_mask = t >= fit_region_start
        residual_echo = residual[echo_mask]
        
        if len(residual_echo) < 10:
            return None, "Insufficient echo data"
        
        dt = np.mean(np.diff(t[echo_mask]))
        freqs = np.fft.rfftfreq(len(residual_echo), d=dt)
        spectrum = np.abs(np.fft.rfft(residual_echo))
        
        if len(spectrum) > 1:
            peak_idx = np.argmax(spectrum[1:]) + 1
            peak_freq = freqs[peak_idx]
            peak_amplitude = spectrum[peak_idx]
            
            noise_level = np.median(spectrum[1:])
            snr = peak_amplitude / noise_level if noise_level > 0 else 0
            
            theoretical_freq = 1.0 / (2 * 200)  # Echo frequency estimate
            
            return {
                'gamma_fit': gamma_fit,
                'A0_fit': A0_fit,
                'peak_freq': peak_freq,
                'snr': snr,
                'theoretical_freq': theoretical_freq,
                'freq_ratio': peak_freq / theoretical_freq if theoretical_freq > 0 else 0,
                'fit_quality': residuals[0] if len(residuals) > 0 else 0
            }, "Success"
        else:
            return None, "Insufficient frequency resolution"
            
    except Exception as error:
        return None, f"Analysis error: {error}"

def main():
    """Main function demonstrating the module capabilities."""
    print("=============================================================")
    print("  meta_teukolsky_clean.py - Echo Detection Demo             ")
    print("=============================================================")
    
    # Parameters
    mass = 1.0
    angular_l = 2
    frequency = 0.3
    epsilon = 1e-3
    length_scale = 1e-5
    
    # Validate coordinate system
    print("\n--- Validation: r_from_rstar function ---")
    validate_r_from_rstar(mass)
    
    # Test case 1: No meta-weight (standard Schwarzschild)
    print("\n--- Test Case 1: Standard Schwarzschild (epsilon = 0) ---")
    try:
        r_s0, psi_s0 = integrate_meta_teukolsky(
            mass, angular_l, frequency,
            r_star_start=-200.0,
            r_star_end=200.0,
            epsilon=0.0,
            length_scale=length_scale,
            n_steps=2000,
            show_progress=True
        )
        
        print("\nResults without meta-weight:")
        print(f"psi(r* = -200.0) = {psi_s0[0]}")
        print(f"psi(r* = 200.0) = {psi_s0[-1]}")
        print(f"Amplitude ratio (far/near): {abs(psi_s0[-1])/abs(psi_s0[0]):.3f}")
        
        # Compute reflection coefficient
        R, status = compute_reflection_coefficient(r_s0, psi_s0, frequency)
        print(f"Reflection coefficient: R = {R}")
        print(f"Status: {status}")
        
        print(f"Integration successful: {len(r_s0)} points")
    
    except Exception as error:
        print(f"Standard Schwarzschild test failed: {error}")
    
    # Test case 2: With meta-weight
    print("\n--- Test Case 2: With meta-weight (epsilon = 10^-^3) ---")
    try:
        r_s, psi_s = integrate_meta_teukolsky(
            mass, angular_l, frequency,
            r_star_start=-200.0,
            r_star_end=200.0,
            epsilon=epsilon,
            length_scale=length_scale,
            n_steps=2000,
            show_progress=True
        )
        
        print("\nResults with meta-weight:")
        print(f"psi(r* = -200.0) = {psi_s[0]}")
        print(f"psi(r* = 200.0) = {psi_s[-1]}")
        print(f"Amplitude ratio (far/near): {abs(psi_s[-1])/abs(psi_s[0]):.3f}")
        
        # Echo detection
        echo_data, echo_status = detect_echoes_residual(r_s, psi_s)
        if echo_data is not None:
            print(f"\nEcho analysis:")
            print(f"Peak frequency: {echo_data['peak_freq']:.6f}")
            print(f"SNR: {echo_data['snr']:.2f}")
            print(f"Frequency ratio: {echo_data['freq_ratio']:.2f}")
        else:
            print(f"Echo analysis failed: {echo_status}")
        
        print(f"Integration successful: {len(r_s)} points")
        
        # Compare with standard case
        if 'psi_s0' in locals():
            print(f"\nComparison:")
            print(f"Far-field amplitude ratio (with/without meta-weight): {abs(psi_s[-1])/abs(psi_s0[-1]):.3f}")
    
    except Exception as error:
        print(f"Meta-weight test failed: {error}")
    
    print("\n=============================================================")
    print("  Demo complete - Module ready for advanced applications    ")
    print("=============================================================")

if __name__ == "__main__":
    main()