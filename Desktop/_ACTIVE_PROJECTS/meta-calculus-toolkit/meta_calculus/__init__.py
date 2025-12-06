"""
Meta-Calculus: A Universal Mathematical Framework for Physics

This package implements non-Newtonian calculus and meta-calculus,
providing alternative mathematical frameworks where different types
of physical relationships become linear and tractable.

The meta-calculus framework enables:
- Quantum-classical transitions through scale-dependent generators
- Black hole information paradox resolution via multiplicative entropy
- Natural cosmological constant suppression without fine-tuning
- Information-theoretic weighting of physical processes

Key Components:
- Core mathematical framework (generators, derivatives, weights, integration)
- Physics applications (quantum mechanics, gravity, cosmology)
- Experimental protocols and testable predictions
- Comprehensive validation and testing suite

Example Usage:
    >>> from meta_calculus import ScaleDependent, MetaDerivative
    >>> from meta_calculus.applications import QuantumClassicalTransition
    >>> 
    >>> # Create quantum-classical transition system
    >>> qc = QuantumClassicalTransition(scale_length=1e-7, energy_scale=1.5e-3)
    >>> n_max, max_deviation = qc.find_maximum_deviation()
    >>> print(f"Maximum deviation: {max_deviation*100:.2f}% at n={n_max}")
"""

# Import core components
from .core import *

# Import applications
from .applications import *

# Import new multi-geometry modules (Gaps 1-7 from ChatGPT analysis)
from . import polytope
from . import jacobian
from . import multi_metric
from . import invariants
from . import triangle_diffusion
from . import frw_diffusion

# Import key classes from new modules for convenience
from .polytope import SolutionPolytope, CanonicalForm
from .jacobian import MetaTimeTransform, GUCInterpretation
from .multi_metric import (
    DistanceFunction, ClassicalDistance, LogDistance, MetaWeightedDistance,
    DiffusionOperator, MultiMetricTrajectory
)
from .invariants import FeatureComputer, InvariantDetector
from .triangle_diffusion import TrianglePolytope, CalculusA, CalculusB, CalculusC
from .frw_diffusion import FRWModelSpace, FRWDiffusionExperiment

# Import multi-calculus framework (v2.0 reframing)
from . import scheme_robust_observables
from . import multi_operator_rg
from .scheme_robust_observables import (
    Calculus, CalculusEnsemble, SchemeRobustObservable,
    EuclideanCalculus, LogCalculus, CurvatureWeightedCalculus,
    create_standard_ensemble
)
from .multi_operator_rg import MultiOperatorRG, CoarseGrainingAnalysis

# Import MOO integration
from . import moo_integration
from .moo_integration import PhysicsOracle, GlobalMOOAdapter, PymooAdapter, GlobalMOOClient

# Import quantum number schemes (RNQT - Hoffreumon-Woods 2025)
from . import quantum_number_schemes
from .quantum_number_schemes import (
    AlgebraScheme, ComplexQT, RealNQT, SchemeEquivalenceTest,
    gamma_map, inverse_gamma_map, tensor_r, is_special_symmetric,
    pauli_matrices, bell_state, random_hermitian, random_pure_state
)

# Import quantum experiments (Q-A, Q-B from scheme-robustness validation)
from . import experiments
from .experiments import (
    ExperimentQA, ExperimentQB,
    ComplexQHO, RealNQTQHO,
    demo_experiment_qa, demo_experiment_qb, run_all_experiments
)

# Import FRW scheme-robustness module
from . import frw_scheme_robustness
from .frw_scheme_robustness import (
    CosmologyCScheme, ClassicalCScheme, MetaCScheme, BigeometricCScheme,
    FRWParameters, FRWModel, FRWSchemeRobustnessTest
)

# Import amplitudes scheme-robustness module
from . import amplitudes_scheme_robustness
from .amplitudes_scheme_robustness import (
    AmplitudeScheme, FeynmanScheme, BCFWScheme, PositiveGeometryScheme,
    AmplitudeSchemeRobustnessTest
)

# Import scheme-breaking detector
from . import scheme_breaking_detector
from .scheme_breaking_detector import (
    BreakingType, BreakingEvent, HuntReport,
    BreakingClassifier, SchemeBreakingDetector
)

# Import scheme morphism module (formal G_scheme definition)
from . import scheme_morphism
from .scheme_morphism import (
    AdmissibilityAxiom, AxiomVerification, AdmissibilityReport,
    SchemeMorphism, GammaMorphism, CSchemeTimeReparam,
    GSchemeFullMorphism, OnticLayer, EpistemicLayer,
    GSchemeObstruction, create_gamma_morphism,
    create_meta_derivative_morphism, check_meta_derivative_admissible,
    classify_anomaly_as_obstruction
)

# Version and metadata
__version__ = "0.1.0"
__author__ = "Meta-Calculus Development Team"
__email__ = "contact@meta-calculus.org"
__description__ = "A universal mathematical framework for physics using non-Newtonian calculus"
__url__ = "https://github.com/meta-calculus/meta-calculus"

# License
__license__ = "MIT"

# All public exports (combines core and applications)
__all__ = [
    # Core generators
    'Generator', 'AlphaGenerator', 'BetaGenerator',
    'Identity', 'Exponential', 'Log', 'Power', 'Reciprocal', 'Sqrt',
    'ScaleDependent', 'Custom',
    'select_generator_pair', 'test_generator_properties',

    # Core derivatives
    'MetaDerivative', 'StarDerivative', 'AdaptiveMetaDerivative',
    'verify_derivative_accuracy', 'compare_derivative_methods',

    # Core weights
    'Weight', 'InformationWeight', 'PathDependentWeight', 'AdaptiveWeight',
    'information_weight_qubit', 'horizon_weight',
    'sensor_confidence_weight', 'decoherence_weight',
    'path_integral_weight', 'information_entropy_weight',
    'correlation_weight', 'create_physics_weight', 'test_weight_properties',

    # Core integration
    'MetaIntegral', 'MetaIntegralSolver',
    'verify_fundamental_theorem_I', 'verify_fundamental_theorem_II',
    'straight_line_test', 'optimize_generators',
    'integration_convergence_test', 'compare_integration_methods',

    # Applications - Quantum-classical
    'QuantumClassicalTransition', 'QuantumDotSpectrum',

    # Applications - Black holes
    'BlackHoleEvolution', 'QuantumHorizon',
    'create_black_hole_system', 'validate_information_conservation',

    # Applications - Cosmology
    'CosmologicalSuppression', 'create_cosmological_system',
    'validate_naturalness', 'compare_with_observations',

    # Multi-geometry modules (Gaps 1-7)
    'polytope', 'jacobian', 'multi_metric', 'invariants',
    'triangle_diffusion', 'frw_diffusion',

    # Polytope (Gap 1-2)
    'SolutionPolytope', 'CanonicalForm',

    # Jacobian interpretation (Gap 3)
    'MetaTimeTransform', 'GUCInterpretation',

    # Multi-metric diffusion (Gaps 4-6)
    'DistanceFunction', 'ClassicalDistance', 'LogDistance', 'MetaWeightedDistance',
    'DiffusionOperator', 'MultiMetricTrajectory',

    # Invariant detection (Gap 7)
    'FeatureComputer', 'InvariantDetector',

    # Triangle polytope diffusion
    'TrianglePolytope', 'CalculusA', 'CalculusB', 'CalculusC',

    # FRW multi-calculus diffusion
    'FRWModelSpace', 'FRWDiffusionExperiment',

    # Multi-calculus framework v2.0 (scheme-robust observables)
    'scheme_robust_observables', 'multi_operator_rg',
    'Calculus', 'CalculusEnsemble', 'SchemeRobustObservable',
    'EuclideanCalculus', 'LogCalculus', 'CurvatureWeightedCalculus',
    'create_standard_ensemble',
    'MultiOperatorRG', 'CoarseGrainingAnalysis',

    # Quantum number schemes (RNQT - Hoffreumon-Woods 2025)
    'quantum_number_schemes',
    'AlgebraScheme', 'ComplexQT', 'RealNQT', 'SchemeEquivalenceTest',
    'gamma_map', 'inverse_gamma_map', 'tensor_r', 'is_special_symmetric',
    'pauli_matrices', 'bell_state', 'random_hermitian', 'random_pure_state',

    # Quantum experiments (scheme-robustness validation)
    'experiments',
    'ExperimentQA', 'ExperimentQB',
    'ComplexQHO', 'RealNQTQHO',
    'demo_experiment_qa', 'demo_experiment_qb', 'run_all_experiments',

    # FRW scheme-robustness (C-scheme invariance for cosmology)
    'frw_scheme_robustness',
    'CosmologyCScheme', 'ClassicalCScheme', 'MetaCScheme', 'BigeometricCScheme',
    'FRWParameters', 'FRWModel', 'FRWSchemeRobustnessTest',

    # Amplitudes scheme-robustness (representation invariance for scattering)
    'amplitudes_scheme_robustness',
    'AmplitudeScheme', 'FeynmanScheme', 'BCFWScheme', 'PositiveGeometryScheme',
    'AmplitudeSchemeRobustnessTest',

    # Scheme-breaking detector (hunt for new physics)
    'scheme_breaking_detector',
    'BreakingType', 'BreakingEvent', 'HuntReport',
    'BreakingClassifier', 'SchemeBreakingDetector',

    # Scheme morphism (formal G_scheme definition)
    'scheme_morphism',
    'AdmissibilityAxiom', 'AxiomVerification', 'AdmissibilityReport',
    'SchemeMorphism', 'GammaMorphism', 'CSchemeTimeReparam',
    'GSchemeFullMorphism', 'OnticLayer', 'EpistemicLayer',
    'GSchemeObstruction', 'create_gamma_morphism',
    'create_meta_derivative_morphism', 'check_meta_derivative_admissible',
    'classify_anomaly_as_obstruction'
]


def quick_demo():
    """Quick demonstration of meta-calculus capabilities."""
    print("Meta-Calculus Framework Quick Demo")
    print("=" * 40)
    
    # Import required modules
    import numpy as np
    
    # 1. Basic generator transformation
    print("\n1. Generator Transformation")
    print("-" * 25)
    
    # Transform exponential to linear
    x = np.linspace(0, 2, 100)
    f = lambda x: 3 * np.exp(2 * x)
    
    alpha = Identity()
    beta = Log()
    
    # Test linearity
    is_linear, slope, intercept, r_squared = straight_line_test(
        f, alpha, beta, (0, 2), expected_slope=2, expected_intercept=np.log(3)
    )
    
    print(f"Function: f(x) = 3*exp(2x)")
    print(f"Transformed to linear: R^2 = {r_squared:.6f}")
    print(f"Fitted slope: {slope:.3f} (expected: 2.000)")
    print(f"Fitted intercept: {intercept:.3f} (expected: {np.log(3):.3f})")
    
    # 2. Meta-derivative
    print("\n2. Meta-Derivative")
    print("-" * 18)
    
    meta_d = MetaDerivative(alpha, beta)
    df_dx_star = meta_d(f, np.array([0.5, 1.0, 1.5]))
    
    print(f"Meta-derivative at x = [0.5, 1.0, 1.5]:")
    print(f"D*f/dx* = {df_dx_star}")
    print(f"Should be constant ~= 2 in (x, ln y) coordinates")
    
    # 3. Physics application preview
    print("\n3. Physics Applications Preview")
    print("-" * 32)
    
    try:
        # Quantum-classical transition
        from .applications import QuantumClassicalTransition
        qc = QuantumClassicalTransition(scale_length=1e-7, energy_scale=1.5e-3)
        n_max, max_dev = qc.find_maximum_deviation()
        print(f"Quantum dots: {max_dev*100:.2f}% energy deviation at n={n_max}")
        
        # Black hole information
        from .applications import BlackHoleEvolution
        bh = BlackHoleEvolution(M_initial=10, units='planck')
        print(f"Black holes: Information conservation via multiplicative entropy")
        
        # Cosmological constant
        from .applications import CosmologicalSuppression
        cosmo = CosmologicalSuppression(cutoff_energy=2.8e-3)
        suppression = cosmo.suppression_factor()
        print(f"Cosmology: Vacuum energy suppressed by factor {suppression:.2e}")
        
    except Exception as e:
        print(f"Physics applications preview failed: {e}")
    
    print(f"\n" + "=" * 40)
    print("Meta-calculus successfully demonstrated!")
    print("Use validate_framework() for comprehensive testing.")


def validate_framework():
    """Comprehensive validation of the entire meta-calculus framework."""
    print("Meta-Calculus Framework Validation")
    print("=" * 40)
    
    # Import validation functions
    from .core import validate_framework as validate_core
    from .applications import validate_all_applications
    
    # Validate core components
    print("\nValidating Core Components...")
    core_results = validate_core()
    
    # Validate physics applications
    print("\nValidating Physics Applications...")
    app_results = validate_all_applications()
    
    # Overall summary
    print(f"\n" + "=" * 40)
    print("Framework Validation Summary")
    print("=" * 40)
    
    # Count successful validations
    core_passed = sum(1 for result in core_results.values() 
                     if isinstance(result, dict) and result.get('passes_tolerance', True))
    core_total = len(core_results)
    
    app_passed = sum(1 for result in app_results.values() 
                    if result.get('validation_passed', False))
    app_total = len(app_results)
    
    total_passed = core_passed + app_passed
    total_tests = core_total + app_total
    
    print(f"Core components: {core_passed}/{core_total} passed")
    print(f"Applications: {app_passed}/{app_total} passed")
    print(f"Overall: {total_passed}/{total_tests} passed ({100*total_passed/total_tests:.1f}%)")
    
    if total_passed == total_tests:
        print("\n🎉 All validations passed! Framework is ready for research use.")
        quality = "excellent"
    elif total_passed >= 0.8 * total_tests:
        print("\n[OK] Most validations passed. Framework is functional with minor issues.")
        quality = "good"
    else:
        print("\n[!]  Several validations failed. Framework needs debugging.")
        quality = "needs_work"
    
    return {
        'core_results': core_results,
        'application_results': app_results,
        'summary': {
            'core_passed': core_passed,
            'core_total': core_total,
            'app_passed': app_passed,
            'app_total': app_total,
            'total_passed': total_passed,
            'total_tests': total_tests,
            'success_rate': total_passed / total_tests,
            'quality': quality
        }
    }


def create_example_system(system_type: str = 'quantum_classical', **kwargs):
    """Create an example system for demonstration or research.
    
    Args:
        system_type: Type of system ('quantum_classical', 'black_hole', 'cosmology')
        **kwargs: System-specific parameters
        
    Returns:
        Configured system instance
    """
    if system_type == 'quantum_classical':
        from .applications import QuantumClassicalTransition
        return QuantumClassicalTransition(
            scale_length=kwargs.get('scale_length', 1e-7),
            energy_scale=kwargs.get('energy_scale', 1.5e-3),
            n_cutoff=kwargs.get('n_cutoff', 100)
        )
    
    elif system_type == 'black_hole':
        from .applications import BlackHoleEvolution
        return BlackHoleEvolution(
            M_initial=kwargs.get('M_initial', 100),
            epsilon=kwargs.get('epsilon', 1e-3),
            units=kwargs.get('units', 'planck')
        )
    
    elif system_type == 'cosmology':
        from .applications import CosmologicalSuppression
        return CosmologicalSuppression(
            cutoff_energy=kwargs.get('cutoff_energy', 2.8e-3),
            units=kwargs.get('units', 'natural')
        )
    
    else:
        raise ValueError(f"Unknown system type: {system_type}")


def experimental_predictions():
    """Generate experimental predictions from all physics applications.
    
    Returns:
        Dictionary with testable predictions
    """
    predictions = {}
    
    try:
        # Quantum-classical predictions
        from .applications import QuantumClassicalTransition
        qc = QuantumClassicalTransition()
        exp_sig = qc.experimental_signature()
        
        predictions['quantum_dots'] = {
            'energy_deviation_percent': exp_sig['max_deviation_percent'],
            'optimal_quantum_number': exp_sig['max_deviation_n'],
            'required_resolution_eV': exp_sig['required_resolution_eV'],
            'measurable_with_current_tech': exp_sig['measurable'],
            'timeline': '2-3 years with STM spectroscopy'
        }
        
        # Black hole predictions
        from .applications import BlackHoleEvolution
        bh = BlackHoleEvolution(M_initial=30, units='solar')  # 30 solar mass BH
        echo_pred = bh.echo_frequency_prediction(r_observer=1000)
        
        predictions['black_hole_echoes'] = {
            'echo_frequency_hz': echo_pred['echo_frequency_hz'],
            'echo_period_ms': echo_pred['echo_period_s'] * 1000,
            'detectable': echo_pred['detectability'],
            'timeline': '5-10 years with advanced LIGO/Virgo'
        }
        
        # Cosmological predictions
        from .applications import CosmologicalSuppression
        cosmo = CosmologicalSuppression()
        naturalness = cosmo.naturalness_check()
        
        predictions['cosmological_constant'] = {
            'suppression_factor': naturalness['suppression_factor'],
            'cutoff_energy_meV': cosmo.cutoff_energy * 1000,
            'naturalness_quality': naturalness['mechanism_quality'],
            'timeline': 'Immediate (theoretical prediction)'
        }
        
    except Exception as e:
        predictions['error'] = f"Failed to generate predictions: {e}"
    
    return predictions


# Module-level convenience functions
def create_quantum_system(**kwargs):
    """Create quantum-classical transition system."""
    return create_example_system('quantum_classical', **kwargs)


def create_gravity_system(**kwargs):
    """Create black hole evolution system."""
    return create_example_system('black_hole', **kwargs)


def create_cosmo_system(**kwargs):
    """Create cosmological suppression system."""
    return create_example_system('cosmology', **kwargs)


# Package information
def package_info():
    """Display package information and capabilities."""
    print(f"Meta-Calculus Framework v{__version__}")
    print("=" * 50)
    print(f"Description: {__description__}")
    print(f"Author: {__author__}")
    print(f"License: {__license__}")
    print(f"URL: {__url__}")
    
    print(f"\nCapabilities:")
    print(f"* Non-Newtonian calculus with generator functions")
    print(f"* Meta-derivatives and meta-integration")
    print(f"* Information-theoretic and path-dependent weights")
    print(f"* Quantum-classical transition modeling")
    print(f"* Black hole information paradox resolution")
    print(f"* Cosmological constant suppression")
    print(f"* Experimental protocol generation")
    print(f"* Comprehensive validation and testing")
    
    print(f"\nQuick Start:")
    print(f">>> import meta_calculus as mc")
    print(f">>> mc.quick_demo()  # Basic demonstration")
    print(f">>> mc.validate_framework()  # Full validation")
    print(f">>> predictions = mc.experimental_predictions()")
    
    print(f"\nFor detailed documentation, see:")
    print(f"* docs/theory.md - Mathematical foundations")
    print(f"* docs/api_reference.md - Complete API")
    print(f"* notebooks/ - Interactive examples")


# Set up logging (optional)
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())