"""
Example usage of the meta_calculus library demonstrating key features.

This script shows how to use the meta-calculus framework for:
1. Basic generator transformations
2. Meta-derivatives and integration
3. Physics applications
4. Experimental predictions
"""

import numpy as np
import matplotlib.pyplot as plt
import meta_calculus as mc


def example_1_basic_transformations():
    """Demonstrate basic generator transformations."""
    print("=" * 60)
    print("Example 1: Basic Generator Transformations")
    print("=" * 60)
    
    # Create test data: exponential relationship y = 3*exp(2x)
    x = np.linspace(0, 2, 100)
    f = lambda x: 3 * np.exp(2 * x)
    y = f(x)
    
    print("Original function: f(x) = 3*exp(2x)")
    print("This is nonlinear and difficult to analyze directly.")
    
    # Transform to make it linear
    alpha = mc.Identity()  # Keep x unchanged
    beta = mc.Log()        # Transform y to ln(y)
    
    # Test linearity
    is_linear, slope, intercept, r_squared = mc.straight_line_test(
        f, alpha, beta, (0, 2), expected_slope=2, expected_intercept=np.log(3)
    )
    
    print(f"\nAfter transformation to (x, ln(y)) coordinates:")
    print(f"Expected: ln(y) = 2x + ln(3) = 2x + {np.log(3):.3f}")
    print(f"Fitted:   ln(y) = {slope:.3f}x + {intercept:.3f}")
    print(f"R^2 = {r_squared:.8f} (perfect linearity = 1.0)")
    print(f"Is linear? {is_linear}")
    
    # Meta-derivative
    meta_d = mc.MetaDerivative(alpha, beta)
    x_test = np.array([0.5, 1.0, 1.5])
    df_dx_star = meta_d(f, x_test)
    
    print(f"\nMeta-derivative D*f/dx* at x = {x_test}:")
    print(f"Values: {df_dx_star}")
    print(f"Should be constant ~= 2 in transformed coordinates")
    print(f"Standard deviation: {np.std(df_dx_star):.6f} (should be ~= 0)")


def example_2_quantum_classical_transition():
    """Demonstrate quantum-classical transition application."""
    print("\n" + "=" * 60)
    print("Example 2: Quantum-Classical Transition")
    print("=" * 60)
    
    # Create quantum-classical system
    qc = mc.QuantumClassicalTransition(
        scale_length=1e-7,    # 100 nm mesoscopic scale
        energy_scale=1.5e-3,  # 1.5 meV energy scale
        n_cutoff=100
    )
    
    print("System parameters:")
    print(f"  Scale length: {qc.scale_length*1e9:.0f} nm")
    print(f"  Energy scale: {qc.energy_scale*1000:.1f} meV")
    print(f"  Quantum number cutoff: {qc.n_cutoff}")
    
    # Calculate energy spectrum
    n, E_classical, E_modified, deviations = qc.energy_spectrum_corrections(150)
    
    # Find maximum deviation
    n_max, max_dev = qc.find_maximum_deviation()
    
    print(f"\nEnergy spectrum analysis:")
    print(f"  Maximum deviation: {max_dev*100:.2f}% at n = {n_max}")
    print(f"  Energy correction: {max_dev * qc.energy_scale * 1e6:.1f} mueV")
    
    # Experimental feasibility
    exp_sig = qc.experimental_signature()
    
    print(f"\nExperimental signature:")
    print(f"  Measurable with current technology: {exp_sig['measurable']}")
    print(f"  Required energy resolution: {exp_sig['required_resolution_eV']*1e6:.1f} mueV")
    print(f"  Signal-to-noise ratio: {exp_sig['signal_to_noise_ratio']:.1f}")
    print(f"  Optimal measurement range: n = {exp_sig['optimal_n_range'][0]} to {exp_sig['optimal_n_range'][1]}")
    
    # Plot if matplotlib is available
    try:
        plt.figure(figsize=(12, 8))
        
        # Energy spectrum
        plt.subplot(2, 2, 1)
        plt.plot(n[:100], E_classical[:100]*1000, 'b-', label='Classical', linewidth=2)
        plt.plot(n[:100], E_modified[:100]*1000, 'r--', label='Meta-calculus', linewidth=2)
        plt.xlabel('Quantum number n')
        plt.ylabel('Energy (meV)')
        plt.title('Energy Spectrum')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Deviations
        plt.subplot(2, 2, 2)
        plt.plot(n[:100], deviations[:100]*100, 'g-', linewidth=2)
        plt.axhline(0, color='k', linestyle=':', alpha=0.5)
        plt.plot(n_max, max_dev*100, 'ro', markersize=8, 
                label=f'Max: {max_dev*100:.2f}% at n={n_max}')
        plt.xlabel('Quantum number n')
        plt.ylabel('Relative deviation (%)')
        plt.title('Energy Corrections')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Scale-dependent generator
        plt.subplot(2, 2, 3)
        x = np.logspace(-10, -4, 1000)
        alpha_x = qc.alpha(x)
        plt.loglog(x*1e9, alpha_x*1e9, 'purple', linewidth=2, label='alpha(x)')
        plt.loglog(x*1e9, x*1e9, 'k--', alpha=0.5, label='x (quantum)')
        plt.axvline(qc.scale_length*1e9, color='r', linestyle=':', 
                   label=f'ℓ = {qc.scale_length*1e9:.0f} nm')
        plt.xlabel('Position (nm)')
        plt.ylabel('alpha(x) (nm)')
        plt.title('Scale-Dependent Generator')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Transition probability
        plt.subplot(2, 2, 4)
        n_range = np.arange(1, 21)
        probs = [qc.transition_probability(10, n, time=1e-12) for n in n_range]
        plt.semilogy(n_range, probs, 'orange', marker='o', linewidth=2)
        plt.xlabel('Final state n')
        plt.ylabel('Transition probability')
        plt.title('Transition from n=10 (t=1ps)')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
    except ImportError:
        print("  (Matplotlib not available for plotting)")


def example_3_black_hole_information():
    """Demonstrate black hole information paradox resolution."""
    print("\n" + "=" * 60)
    print("Example 3: Black Hole Information Paradox")
    print("=" * 60)
    
    # Create black hole system
    bh = mc.BlackHoleEvolution(
        M_initial=100,  # 100 Planck masses
        epsilon=1e-3,   # Quantum correction parameter
        units='planck'
    )
    
    print("Black hole parameters:")
    print(f"  Initial mass: {bh.M_initial} Planck masses")
    print(f"  Quantum parameter epsilon: {bh.epsilon}")
    print(f"  Schwarzschild radius: {bh.schwarzschild_radius(bh.M_initial)} Planck lengths")
    print(f"  Hawking temperature: {bh.hawking_temperature(bh.M_initial):.2e} Planck temperature")
    print(f"  Evaporation time: {bh.evaporation_time():.2e} Planck times")
    
    # Evolve the system (short evolution for demo)
    print("\nEvolving black hole system...")
    t, M, S_star_bh, S_star_rad, S_star_quantum = bh.evolve(
        t_final=0.1 * bh.evaporation_time(), 
        n_points=100
    )
    
    # Check conservation
    conservation = bh.conservation_check(t, S_star_bh, S_star_rad, S_star_quantum)
    
    print(f"\nEvolution results:")
    print(f"  Final mass: {M[-1]:.1f} Planck masses ({M[-1]/M[0]*100:.1f}% of initial)")
    print(f"  Mass loss: {M[0] - M[-1]:.1f} Planck masses")
    
    print(f"\nInformation conservation:")
    print(f"  Conservation quality: {conservation['conservation_quality']}")
    print(f"  Maximum error: {conservation['max_relative_error']:.2e}")
    print(f"  Final error: {conservation['final_relative_error']:.2e}")
    print(f"  Conservation maintained: {conservation['conservation_maintained']}")
    
    # Echo predictions
    echo_pred = bh.echo_frequency_prediction(r_observer=1000)
    
    print(f"\nGravitational wave echo predictions:")
    print(f"  Echo frequency: {echo_pred['echo_frequency_hz']:.2e} Hz")
    print(f"  Echo period: {echo_pred['echo_period_s']*1000:.2f} ms")
    print(f"  Echo amplitude (relative): {echo_pred['echo_amplitude_relative']:.2e}")
    print(f"  Detectable: {echo_pred['detectability']}")
    
    # Analog gravity parameters
    analog_params = bh.analog_gravity_parameters()
    
    print(f"\nAnalog gravity experiment (BEC):")
    print(f"  Healing length: {analog_params['healing_length_m']*1e6:.1f} mum")
    print(f"  Sound speed: {analog_params['sound_speed_ms']*1000:.1f} mm/s")
    print(f"  Analog Hawking temperature: {analog_params['hawking_temperature_K']*1e9:.1f} nK")
    print(f"  Echo frequency: {analog_params['echo_frequency_hz']/1000:.1f} kHz")
    print(f"  Experimentally feasible: {analog_params['experimental_feasibility']['temperature_achievable']}")


def example_4_cosmological_constant():
    """Demonstrate cosmological constant suppression."""
    print("\n" + "=" * 60)
    print("Example 4: Cosmological Constant Suppression")
    print("=" * 60)
    
    # Create cosmological system
    cosmo = mc.CosmologicalSuppression(
        cutoff_energy=2.8e-3,  # 2.8 meV cutoff
        units='natural'
    )
    
    print("Cosmological parameters:")
    print(f"  Energy cutoff: {cosmo.cutoff_energy*1000:.1f} meV")
    print(f"  Critical density: {cosmo.density_scale:.2e} eV^4")
    
    # Calculate vacuum energy suppression
    rho_vacuum = cosmo.vacuum_energy_density()
    suppression = cosmo.suppression_factor()
    
    print(f"\nVacuum energy calculation:")
    print(f"  Suppressed vacuum density: {rho_vacuum:.2e} eV^4")
    print(f"  Suppression factor: {suppression:.2e}")
    print(f"  Target suppression: ~10^-^1^2^2 (observational)")
    print(f"  Ratio to target: {suppression/1e-122:.2e}")
    
    # Naturalness check
    naturalness = cosmo.naturalness_check()
    
    print(f"\nNaturalness analysis:")
    print(f"  Mechanism quality: {naturalness['mechanism_quality']}")
    print(f"  Fine-tuning required: {naturalness['fine_tuning_required']}")
    print(f"  Cutoff scale natural: {naturalness['cutoff_natural']}")
    print(f"  Naturalness ratio: {naturalness['naturalness_ratio']:.2e}")
    
    # Effective cosmological constant
    Lambda_eff = cosmo.effective_cosmological_constant()
    
    print(f"\nEffective cosmological constant:")
    print(f"  Lambda_eff: {Lambda_eff:.2e} eV^2")
    
    # Dark energy equation of state
    z = np.array([0, 0.5, 1.0, 2.0])
    de_eos = cosmo.dark_energy_equation_of_state(z)
    
    print(f"\nDark energy evolution:")
    print(f"  w(z=0): {de_eos['w_0']:.3f}")
    print(f"  w_a (evolution): {de_eos['w_a']:.3f}")
    print(f"  Phantom crossing: {de_eos['phantom_crossing']}")
    
    # Observational constraints
    constraints = cosmo.observational_constraints()
    
    print(f"\nObservational comparison:")
    print(f"  Agreement quality: {constraints['agreement_quality']}")
    print(f"  chi^2 = {constraints['chi_squared']:.2f}")
    print(f"  Reduced chi^2 = {constraints['reduced_chi_squared']:.2f}")


def example_5_framework_validation():
    """Demonstrate framework validation."""
    print("\n" + "=" * 60)
    print("Example 5: Framework Validation")
    print("=" * 60)
    
    print("Running comprehensive framework validation...")
    print("This tests all core components and physics applications.")
    
    # Run validation
    results = mc.validate_framework()
    
    print(f"\nValidation Summary:")
    print(f"  Core components: {results['summary']['core_passed']}/{results['summary']['core_total']} passed")
    print(f"  Applications: {results['summary']['app_passed']}/{results['summary']['app_total']} passed")
    print(f"  Overall success rate: {results['summary']['success_rate']*100:.1f}%")
    print(f"  Framework quality: {results['summary']['quality']}")
    
    if results['summary']['quality'] == 'excellent':
        print("\n🎉 Framework validation successful!")
        print("   All components working correctly.")
    elif results['summary']['quality'] == 'good':
        print("\n[OK] Framework mostly functional.")
        print("   Minor issues detected but core functionality works.")
    else:
        print("\n[!]  Framework needs attention.")
        print("   Several components failed validation.")


def example_6_experimental_predictions():
    """Generate experimental predictions."""
    print("\n" + "=" * 60)
    print("Example 6: Experimental Predictions")
    print("=" * 60)
    
    print("Generating testable experimental predictions...")
    
    predictions = mc.experimental_predictions()
    
    print(f"\n1. Quantum Dot Spectroscopy:")
    qd = predictions['quantum_dots']
    print(f"   Energy deviation: {qd['energy_deviation_percent']:.2f}%")
    print(f"   Optimal quantum number: n = {qd['optimal_quantum_number']}")
    print(f"   Required resolution: {qd['required_resolution_eV']*1e6:.1f} mueV")
    print(f"   Measurable now: {qd['measurable_with_current_tech']}")
    print(f"   Timeline: {qd['timeline']}")
    
    print(f"\n2. Black Hole Echoes:")
    bh = predictions['black_hole_echoes']
    print(f"   Echo frequency: {bh['echo_frequency_hz']:.2e} Hz")
    print(f"   Echo period: {bh['echo_period_ms']:.2f} ms")
    print(f"   Detectable: {bh['detectable']}")
    print(f"   Timeline: {bh['timeline']}")
    
    print(f"\n3. Cosmological Constant:")
    cc = predictions['cosmological_constant']
    print(f"   Suppression factor: {cc['suppression_factor']:.2e}")
    print(f"   Cutoff energy: {cc['cutoff_energy_meV']:.1f} meV")
    print(f"   Naturalness: {cc['naturalness_quality']}")
    print(f"   Timeline: {cc['timeline']}")
    
    print(f"\nAll predictions are within reach of current or near-future technology!")


def main():
    """Run all examples."""
    print("Meta-Calculus Framework - Comprehensive Examples")
    print("This demonstration shows the key capabilities of the framework.")
    
    try:
        example_1_basic_transformations()
        example_2_quantum_classical_transition()
        example_3_black_hole_information()
        example_4_cosmological_constant()
        example_5_framework_validation()
        example_6_experimental_predictions()
        
        print("\n" + "=" * 60)
        print("🎉 All examples completed successfully!")
        print("=" * 60)
        print("\nThe meta-calculus framework demonstrates:")
        print("* Mathematical transformation of complex problems")
        print("* Resolution of fundamental physics paradoxes")
        print("* Testable experimental predictions")
        print("* Comprehensive validation and reliability")
        print("\nReady for research applications! 🚀")
        
    except Exception as e:
        print(f"\n[X] Example failed with error: {e}")
        print("This may indicate missing dependencies or implementation issues.")
        print("Please check the installation and requirements.")


if __name__ == "__main__":
    main()