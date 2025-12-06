"""
Core components of the meta-calculus framework.

This module provides the fundamental mathematical tools for meta-calculus:
- Generator functions (alpha, beta) for coordinate transformations
- Meta-derivatives for generalized differentiation
- Weight functions for information-theoretic and path-dependent calculus
- Meta-integration and fundamental theorem verification

The meta-calculus framework enables alternative mathematical formulations
where complex relationships become linear, making previously intractable
problems solvable.
"""

# Generator functions
from .generators import (
    # Abstract base classes
    Generator, AlphaGenerator, BetaGenerator,
    
    # Concrete implementations
    Identity, Exponential, Log, Power, Reciprocal, Sqrt,
    ScaleDependent, Custom,
    
    # Utility functions
    select_generator_pair, test_generator_properties
)

# Meta-derivatives
from .derivatives import (
    MetaDerivative, StarDerivative, AdaptiveMetaDerivative,
    verify_derivative_accuracy, compare_derivative_methods
)

# Weight functions
from .weights import (
    # Base classes
    Weight, InformationWeight, PathDependentWeight, AdaptiveWeight,
    
    # Specific weight functions
    information_weight_qubit, horizon_weight,
    sensor_confidence_weight, decoherence_weight,
    path_integral_weight, information_entropy_weight,
    correlation_weight,
    
    # Factory and utility functions
    create_physics_weight, test_weight_properties
)

# Integration and fundamental theorems
from .integration import (
    MetaIntegral, MetaIntegralSolver,
    verify_fundamental_theorem_I, verify_fundamental_theorem_II,
    straight_line_test, optimize_generators,
    integration_convergence_test, compare_integration_methods
)

# Version information
__version__ = "0.1.0"

# Export all public components
__all__ = [
    # Generators
    'Generator', 'AlphaGenerator', 'BetaGenerator',
    'Identity', 'Exponential', 'Log', 'Power', 'Reciprocal', 'Sqrt',
    'ScaleDependent', 'Custom',
    'select_generator_pair', 'test_generator_properties',
    
    # Derivatives
    'MetaDerivative', 'StarDerivative', 'AdaptiveMetaDerivative',
    'verify_derivative_accuracy', 'compare_derivative_methods',
    
    # Weights
    'Weight', 'InformationWeight', 'PathDependentWeight', 'AdaptiveWeight',
    'information_weight_qubit', 'horizon_weight',
    'sensor_confidence_weight', 'decoherence_weight',
    'path_integral_weight', 'information_entropy_weight',
    'correlation_weight', 'create_physics_weight', 'test_weight_properties',
    
    # Integration
    'MetaIntegral', 'MetaIntegralSolver',
    'verify_fundamental_theorem_I', 'verify_fundamental_theorem_II',
    'straight_line_test', 'optimize_generators',
    'integration_convergence_test', 'compare_integration_methods'
]


def quick_start_example():
    """Demonstrate basic meta-calculus usage.
    
    This function provides a simple example of how to use the
    meta-calculus framework for transforming an exponential
    relationship into a linear one.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    
    print("Meta-Calculus Quick Start Example")
    print("=" * 40)
    
    # Create test data: exponential relationship
    x = np.linspace(0, 2, 100)
    f = lambda x: 3 * np.exp(2 * x)
    y = f(x)
    
    # Classical approach: y vs x (exponential)
    print("1. Classical coordinates (x, y):")
    print(f"   Relationship: y = 3 * exp(2x)")
    print(f"   This is nonlinear and difficult to analyze")
    
    # Meta-calculus approach: transform to linear coordinates
    alpha = Identity()  # Keep x unchanged
    beta = Log()        # Transform y to ln(y)
    
    # Transform coordinates
    x_trans = alpha(x)
    y_trans = beta(y)
    
    # Fit line in transformed coordinates
    coeffs = np.polyfit(x_trans, y_trans, 1)
    slope, intercept = coeffs
    
    print(f"\n2. Meta-calculus coordinates (x, ln(y)):")
    print(f"   Transformed relationship: ln(y) = {slope:.3f}x + {intercept:.3f}")
    print(f"   Expected: ln(y) = 2x + ln(3) = 2x + {np.log(3):.3f}")
    print(f"   Error in slope: {abs(slope - 2):.6f}")
    print(f"   Error in intercept: {abs(intercept - np.log(3)):.6f}")
    
    # Verify linearity
    is_linear, fitted_slope, fitted_intercept, r_squared = straight_line_test(
        f, alpha, beta, (0, 2), expected_slope=2, expected_intercept=np.log(3)
    )
    
    print(f"\n3. Linearity verification:")
    print(f"   R^2 = {r_squared:.8f}")
    print(f"   Is linear? {is_linear}")
    
    # Meta-derivative example
    meta_d = MetaDerivative(alpha, beta)
    df_dx_star = meta_d(f, np.array([0.5, 1.0, 1.5]))
    
    print(f"\n4. Meta-derivative at x = [0.5, 1.0, 1.5]:")
    print(f"   D*f/dx* = {df_dx_star}")
    print(f"   In (x, ln y) coordinates, this should be constant = 2")
    
    # Meta-integration example
    meta_int = MetaIntegral(alpha, beta)
    integral_result = meta_int.integrate(lambda x: np.ones_like(x), 0, 1)
    
    print(f"\n5. Meta-integration integral[0,1] 1 dx*:")
    print(f"   Result: {integral_result:.6f}")
    print(f"   This represents: integral[0,1] e^1 dx = e ~= {np.e:.6f}")
    
    print(f"\nMeta-calculus successfully linearized the exponential relationship!")
    
    return {
        'original_data': (x, y),
        'transformed_data': (x_trans, y_trans),
        'linearity_test': (is_linear, r_squared),
        'meta_derivative': df_dx_star,
        'meta_integral': integral_result
    }


def validate_framework():
    """Validate the meta-calculus framework with comprehensive tests.
    
    This function runs a series of validation tests to ensure
    the mathematical framework is working correctly.
    """
    import numpy as np
    
    print("Meta-Calculus Framework Validation")
    print("=" * 40)
    
    validation_results = {
        'generators': {},
        'derivatives': {},
        'weights': {},
        'integration': {},
        'fundamental_theorems': {}
    }
    
    # Test 1: Generator properties
    print("\n1. Testing Generator Properties...")
    
    generators_to_test = [
        Identity(), Exponential(), Log(), Power(2), 
        Reciprocal(), Sqrt(), ScaleDependent(1e-7)
    ]
    
    for gen in generators_to_test:
        test_points = np.logspace(-2, 2, 50)
        if isinstance(gen, Log):
            test_points = test_points[test_points > 0]  # Log needs positive inputs
        
        results = test_generator_properties(gen, test_points)
        validation_results['generators'][gen.__class__.__name__] = results
        
        print(f"   {gen.__class__.__name__}: ", end="")
        if results.get('numerical_stability', False) and results.get('inverse_accuracy', 1) < 0.01:
            print("✓ PASS")
        else:
            print("[X] FAIL")
    
    # Test 2: Meta-derivative accuracy
    print("\n2. Testing Meta-Derivative Accuracy...")
    
    # Test with known analytical derivative
    f = lambda x: x**2
    analytical_deriv = lambda x: 2*x
    
    alpha = Identity()
    beta = Identity()
    meta_d = MetaDerivative(alpha, beta)
    
    x_test = np.linspace(0.1, 2, 20)
    accuracy_results = verify_derivative_accuracy(
        meta_d, f, analytical_deriv, x_test
    )
    
    validation_results['derivatives']['accuracy'] = accuracy_results
    
    if accuracy_results['passes_tolerance']:
        print("   Classical derivative recovery: ✓ PASS")
    else:
        print(f"   Classical derivative recovery: [X] FAIL (error: {accuracy_results['max_relative_error']:.2e})")
    
    # Test 3: Weight function properties
    print("\n3. Testing Weight Functions...")
    
    # Test qubit information weight
    r_values = np.linspace(0, 1, 50)
    qubit_weights = information_weight_qubit(r_values)
    
    weight_test_passed = (
        np.all(qubit_weights >= 0) and  # Non-negative
        np.all(qubit_weights <= 1) and  # Bounded
        abs(qubit_weights[0] - np.exp(-np.log(2))) < 1e-10 and  # Mixed state
        abs(qubit_weights[-1] - 1.0) < 1e-10  # Pure state
    )
    
    validation_results['weights']['qubit'] = weight_test_passed
    
    if weight_test_passed:
        print("   Qubit information weight: ✓ PASS")
    else:
        print("   Qubit information weight: [X] FAIL")
    
    # Test 4: Integration convergence
    print("\n4. Testing Integration Convergence...")
    
    meta_int = MetaIntegral(Identity(), Identity())
    f_simple = lambda x: x**2  # integralx^2 dx = x^3/3
    
    convergence_results = integration_convergence_test(
        meta_int, f_simple, 0, 1, [100, 500, 1000, 2000]
    )
    
    expected_result = 1/3  # integral[0,1] x^2 dx = 1/3
    final_error = abs(convergence_results['final_result'] - expected_result)
    
    validation_results['integration']['convergence'] = convergence_results
    
    if final_error < 1e-6 and convergence_results['convergence_rate'] > 1:
        print(f"   Integration convergence: ✓ PASS (error: {final_error:.2e})")
    else:
        print(f"   Integration convergence: [X] FAIL (error: {final_error:.2e})")
    
    # Test 5: Fundamental Theorem I
    print("\n5. Testing Fundamental Theorem I...")
    
    f_test = lambda x: np.sin(x)
    integral_val, antideriv_val, ftc_error = verify_fundamental_theorem_I(
        f_test, Identity(), Identity(), 0, np.pi
    )
    
    validation_results['fundamental_theorems']['ftc_i'] = {
        'integral': integral_val,
        'antiderivative': antideriv_val,
        'error': ftc_error
    }
    
    if ftc_error < 1e-6:
        print(f"   Fundamental Theorem I: ✓ PASS (error: {ftc_error:.2e})")
    else:
        print(f"   Fundamental Theorem I: [X] FAIL (error: {ftc_error:.2e})")
    
    # Test 6: Straight-line test
    print("\n6. Testing Straight-Line Diagnostic...")
    
    # Exponential function should be linear in (x, ln y) coordinates
    f_exp = lambda x: np.exp(2*x + 1)
    is_linear, slope, intercept, r_squared = straight_line_test(
        f_exp, Identity(), Log(), (0, 2), 
        expected_slope=2, expected_intercept=1
    )
    
    validation_results['fundamental_theorems']['straight_line'] = {
        'is_linear': is_linear,
        'r_squared': r_squared,
        'slope_error': abs(slope - 2),
        'intercept_error': abs(intercept - 1)
    }
    
    if is_linear and r_squared > 0.999:
        print(f"   Straight-line test: ✓ PASS (R^2 = {r_squared:.6f})")
    else:
        print(f"   Straight-line test: [X] FAIL (R^2 = {r_squared:.6f})")
    
    # Summary
    print(f"\n" + "=" * 40)
    print("Validation Summary:")
    
    total_tests = 0
    passed_tests = 0
    
    # Count generator tests
    for gen_name, results in validation_results['generators'].items():
        total_tests += 1
        if results.get('numerical_stability', False) and results.get('inverse_accuracy', 1) < 0.01:
            passed_tests += 1
    
    # Count other tests
    test_checks = [
        validation_results['derivatives']['accuracy']['passes_tolerance'],
        validation_results['weights']['qubit'],
        final_error < 1e-6 and convergence_results['convergence_rate'] > 1,
        ftc_error < 1e-6,
        is_linear and r_squared > 0.999
    ]
    
    for check in test_checks:
        total_tests += 1
        if check:
            passed_tests += 1
    
    print(f"Tests passed: {passed_tests}/{total_tests}")
    print(f"Success rate: {100*passed_tests/total_tests:.1f}%")
    
    if passed_tests == total_tests:
        print("🎉 All tests passed! Framework is ready for use.")
    else:
        print("[!]  Some tests failed. Please check implementation.")
    
    return validation_results


# Convenience function for common use cases
def create_quantum_classical_system(scale_length: float = 1e-7):
    """Create a meta-calculus system for quantum-classical transitions.
    
    Args:
        scale_length: Characteristic length scale for the transition
        
    Returns:
        Tuple of (alpha_generator, meta_derivative, meta_integral)
    """
    alpha = ScaleDependent(scale_length)
    beta = Identity()  # Keep energy/field values unchanged initially
    
    meta_d = MetaDerivative(alpha, beta)
    meta_int = MetaIntegral(alpha, beta)
    
    return alpha, meta_d, meta_int


def create_information_weighted_system(entropy_func: callable):
    """Create a meta-calculus system with information-theoretic weighting.
    
    Args:
        entropy_func: Function that computes entropy S(x)
        
    Returns:
        Tuple of (weight, meta_derivative, meta_integral)
    """
    weight = InformationWeight(entropy_func)
    alpha = Identity()
    beta = Identity()
    
    meta_d = MetaDerivative(alpha, beta, weight.u, weight.v)
    meta_int = MetaIntegral(alpha, beta, weight.u)
    
    return weight, meta_d, meta_int


# Module-level constants
PLANCK_LENGTH = 1.616e-35  # meters
PLANCK_ENERGY = 1.956e9    # joules
PLANCK_TIME = 5.391e-44    # seconds

# Common scale lengths for different physics
SCALES = {
    'planck': PLANCK_LENGTH,
    'atomic': 1e-10,        # Angstrom
    'mesoscopic': 1e-7,     # 100 nm
    'classical': 1.0,       # meter
    'cosmological': 1e26    # Hubble length
}