"""
Integration and fundamental theorems for meta-calculus.

Implements meta-integration and verifies the fundamental theorems
of calculus in the transformed coordinate system. This module provides
the integration capabilities that complement the meta-derivative operations.
"""

import numpy as np
from scipy.integrate import simpson, cumulative_trapezoid, quad
from scipy.optimize import minimize_scalar
from typing import Callable, Tuple, Optional, Union
try:
    from .generators import AlphaGenerator, BetaGenerator, Identity
    from .derivatives import MetaDerivative
except ImportError:
    from meta_calculus.core.generators import AlphaGenerator, BetaGenerator, Identity
    from meta_calculus.core.derivatives import MetaDerivative

ArrayLike = Union[float, np.ndarray]


class MetaIntegral:
    """Compute integrals in the meta-calculus framework.
    
    The meta-integral transforms according to:
    integral f dx* = integral u(x) * beta(f(x)) * alpha'(x) dx
    
    This generalizes classical integration to alternative mathematical
    frameworks where the integration measure is modified by the generators
    and weight functions.
    """
    
    def __init__(self, 
                 alpha: AlphaGenerator, 
                 beta: BetaGenerator,
                 u: Optional[Callable[[ArrayLike], ArrayLike]] = None):
        """Initialize meta-integral operator.
        
        Args:
            alpha: Generator for independent variable transformation
            beta: Generator for dependent variable transformation
            u: Weight function for independent variable (default: unity)
        """
        self.alpha = alpha
        self.beta = beta
        self.u = u if u is not None else lambda x: np.ones_like(np.asarray(x))
    
    def integrate(self, f: Callable[[ArrayLike], ArrayLike], 
                  a: float, b: float, 
                  n_points: int = 1000,
                  method: str = 'simpson') -> float:
        """Compute the definite meta-integral integral[a,b] f dx*.
        
        Args:
            f: Function to integrate
            a, b: Integration bounds
            n_points: Number of points for numerical integration
            method: Integration method ('simpson', 'trapezoid', 'adaptive')
            
        Returns:
            Value of the meta-integral
        """
        if method == 'adaptive':
            return self._adaptive_integrate(f, a, b)
        
        # Create integration grid
        x = np.linspace(a, b, n_points)
        
        # Evaluate function and transformations
        fx = f(x)
        beta_fx = self.beta(fx)
        alpha_prime = self.alpha.derivative(x)
        u_x = self.u(x)
        
        # Integrand in standard coordinates: u(x) * beta(f(x)) * alpha'(x)
        integrand = u_x * beta_fx * alpha_prime
        
        # Numerical integration
        if method == 'simpson':
            return simpson(integrand, x=x)
        elif method == 'trapezoid':
            return np.trapz(integrand, x=x)
        else:
            raise ValueError(f"Unknown integration method: {method}")
    
    def _adaptive_integrate(self, f: Callable, a: float, b: float) -> float:
        """Adaptive integration using scipy.integrate.quad.
        
        Args:
            f: Function to integrate
            a, b: Integration bounds
            
        Returns:
            Adaptive integration result
        """
        def integrand(x):
            fx = f(x)
            beta_fx = self.beta(fx)
            alpha_prime = self.alpha.derivative(x)
            u_x = self.u(x)
            return u_x * beta_fx * alpha_prime
        
        try:
            result, _ = quad(integrand, a, b, limit=100)
            return result
        except Exception as e:
            # Fallback to fixed-grid integration
            print(f"Adaptive integration failed: {e}. Using Simpson's rule.")
            return self.integrate(f, a, b, method='simpson')
    
    def cumulative(self, f: Callable[[ArrayLike], ArrayLike], 
                   x: ArrayLike) -> ArrayLike:
        """Compute cumulative meta-integral F(x) = integral[x0,x] f dt*.
        
        Args:
            f: Function to integrate
            x: Points at which to evaluate cumulative integral
            
        Returns:
            Cumulative integral values
        """
        x = np.asarray(x)
        
        # Evaluate function and transformations
        fx = f(x)
        beta_fx = self.beta(fx)
        alpha_prime = self.alpha.derivative(x)
        u_x = self.u(x)
        
        # Integrand
        integrand = u_x * beta_fx * alpha_prime
        
        # Cumulative integration
        F = cumulative_trapezoid(integrand, x=x, initial=0)
        
        return F
    
    def mean_value(self, f: Callable, a: float, b: float) -> float:
        """Compute the meta-calculus mean value of f over [a,b].
        
        The mean value in meta-calculus is:
        <f>* = (integral[a,b] f dx*) / (integral[a,b] 1 dx*)
        
        Args:
            f: Function to average
            a, b: Integration bounds
            
        Returns:
            Meta-calculus mean value
        """
        numerator = self.integrate(f, a, b)
        denominator = self.integrate(lambda x: np.ones_like(x), a, b)
        
        return numerator / denominator if denominator != 0 else 0
    
    def variance(self, f: Callable, a: float, b: float) -> float:
        """Compute the meta-calculus variance of f over [a,b].
        
        Var*[f] = <f^2>* - <f>*^2
        
        Args:
            f: Function to compute variance for
            a, b: Integration bounds
            
        Returns:
            Meta-calculus variance
        """
        mean_f = self.mean_value(f, a, b)
        mean_f_squared = self.mean_value(lambda x: f(x)**2, a, b)
        
        return mean_f_squared - mean_f**2
    
    def moment(self, f: Callable, a: float, b: float, 
              order: int, center: Optional[float] = None) -> float:
        """Compute the nth meta-calculus moment of f.
        
        Args:
            f: Function to compute moment for
            a, b: Integration bounds
            order: Moment order (1, 2, 3, ...)
            center: Center point (default: mean value)
            
        Returns:
            nth meta-calculus moment
        """
        if center is None:
            center = self.mean_value(f, a, b)
        
        def moment_func(x):
            return (f(x) - center) ** order
        
        return self.mean_value(moment_func, a, b)


def verify_fundamental_theorem_I(
    f: Callable[[ArrayLike], ArrayLike],
    alpha: AlphaGenerator,
    beta: BetaGenerator,
    a: float,
    b: float,
    n_points: int = 1000,
    u: Optional[Callable] = None
) -> Tuple[float, float, float]:
    """Verify the first fundamental theorem of meta-calculus.
    
    If F is an antiderivative of f in meta-calculus, then:
    integral[a,b] f dx* = F*(b) - F*(a)
    
    Args:
        f: Function to test
        alpha, beta: Generator functions
        a, b: Integration bounds
        n_points: Number of points for numerical integration
        u: Weight function
        
    Returns:
        (integral_value, F_b_minus_F_a, relative_error)
    """
    # Compute integral directly
    meta_int = MetaIntegral(alpha, beta, u)
    integral_value = meta_int.integrate(f, a, b, n_points)
    
    # Compute via antiderivative using cumulative integral
    x = np.linspace(a, b, n_points)
    F = meta_int.cumulative(f, x)
    F_b_minus_F_a = F[-1] - F[0]
    
    # Compute error
    relative_error = abs(integral_value - F_b_minus_F_a) / (abs(integral_value) + 1e-10)
    
    return integral_value, F_b_minus_F_a, relative_error


def verify_fundamental_theorem_II(
    F: Callable[[ArrayLike], ArrayLike],
    alpha: AlphaGenerator,
    beta: BetaGenerator,
    x: ArrayLike,
    tol: float = 1e-6,
    u: Optional[Callable] = None,
    v: Optional[Callable] = None
) -> Tuple[ArrayLike, ArrayLike, float]:
    """Verify the second fundamental theorem of meta-calculus.
    
    If F is differentiable, then:
    D*/dx* [integral[a,x] f dt*] = f(x)
    
    Args:
        F: Antiderivative function
        alpha, beta: Generator functions
        x: Points at which to verify
        tol: Tolerance for verification
        u, v: Weight functions
        
    Returns:
        (meta_derivative_of_integral, original_function, max_error)
    """
    x = np.asarray(x)
    
    # Compute meta-derivative of F
    meta_deriv = MetaDerivative(alpha, beta, u, v)
    dF_dx_star = meta_deriv(F, x)
    
    # For verification, we need to know what f should be
    # We use numerical differentiation as ground truth
    dx = np.mean(np.diff(x)) if len(x) > 1 else 1e-8
    f_numerical = np.gradient(F(x), x)
    
    # Transform to get f in original coordinates
    # This is the inverse of the meta-derivative transformation
    fx = F(x)
    alpha_prime = alpha.derivative(x)
    beta_prime = beta.derivative(fx)
    u_x = u(x) if u is not None else np.ones_like(x)
    v_fx = v(fx) if v is not None else np.ones_like(fx)
    
    # f = (u/v) * (alpha'/beta') * (classical derivative)
    f_original = (u_x / v_fx) * (alpha_prime / beta_prime) * f_numerical
    
    # Compute error
    max_error = np.max(np.abs(dF_dx_star - f_original))
    
    return dF_dx_star, f_original, max_error


def straight_line_test(
    f: Callable[[ArrayLike], ArrayLike],
    alpha: AlphaGenerator,
    beta: BetaGenerator,
    x_range: Tuple[float, float],
    expected_slope: float,
    expected_intercept: float,
    n_points: int = 100,
    tol: float = 0.01
) -> Tuple[bool, float, float, float]:
    """Test if a function becomes linear in (alpha,beta) coordinates.
    
    This is the key diagnostic for choosing appropriate generators.
    A good choice of generators will make the relationship linear.
    
    Args:
        f: Function to test
        alpha, beta: Generator functions
        x_range: (x_min, x_max) for testing
        expected_slope: Expected slope in (alpha,beta) plane
        expected_intercept: Expected intercept in (alpha,beta) plane
        n_points: Number of test points
        tol: Tolerance for linearity
        
    Returns:
        (is_linear, fitted_slope, fitted_intercept, r_squared)
    """
    # Generate test points
    x = np.linspace(x_range[0], x_range[1], n_points)
    
    # Transform to (alpha,beta) coordinates
    alpha_x = alpha(x)
    beta_fx = beta(f(x))
    
    # Remove any non-finite values
    finite_mask = np.isfinite(alpha_x) & np.isfinite(beta_fx)
    alpha_x = alpha_x[finite_mask]
    beta_fx = beta_fx[finite_mask]
    
    if len(alpha_x) < 3:
        return False, np.nan, np.nan, 0.0
    
    # Fit line in transformed coordinates
    coeffs = np.polyfit(alpha_x, beta_fx, 1)
    fitted_slope, fitted_intercept = coeffs
    
    # Compute R^2 to measure linearity
    y_pred = fitted_slope * alpha_x + fitted_intercept
    ss_res = np.sum((beta_fx - y_pred) ** 2)
    ss_tot = np.sum((beta_fx - np.mean(beta_fx)) ** 2)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
    
    # Check if linear within tolerance
    slope_error = abs(fitted_slope - expected_slope) / (abs(expected_slope) + 1e-10)
    intercept_error = abs(fitted_intercept - expected_intercept) / (abs(expected_intercept) + 1e-10)
    
    is_linear = (r_squared > (1 - tol) and 
                slope_error < tol and 
                intercept_error < tol)
    
    return is_linear, fitted_slope, fitted_intercept, r_squared


def optimize_generators(
    f: Callable[[ArrayLike], ArrayLike],
    x_data: ArrayLike,
    generator_candidates: list = None,
    linearity_weight: float = 1.0,
    smoothness_weight: float = 0.1
) -> Tuple[AlphaGenerator, BetaGenerator, float]:
    """Automatically optimize generator selection for maximum linearity.
    
    Args:
        f: Function to linearize
        x_data: Input data points
        generator_candidates: List of generator classes to try
        linearity_weight: Weight for linearity in optimization
        smoothness_weight: Weight for smoothness in optimization
        
    Returns:
        (best_alpha, best_beta, quality_score)
    """
    if generator_candidates is None:
        from .generators import Identity, Exponential, Log, Power, Reciprocal, Sqrt
        generator_candidates = [
            Identity, Exponential, Log, 
            lambda: Power(2), lambda: Power(0.5), lambda: Power(3),
            Reciprocal, Sqrt
        ]
    
    best_score = -np.inf
    best_pair = (Identity(), Identity())
    
    y_data = f(x_data)
    
    for alpha_gen in generator_candidates:
        for beta_gen in generator_candidates:
            try:
                # Create generator instances
                alpha = alpha_gen() if callable(alpha_gen) else alpha_gen
                beta = beta_gen() if callable(beta_gen) else beta_gen
                
                # Transform data
                x_trans = alpha(x_data)
                y_trans = beta(y_data)
                
                # Check for finite values
                finite_mask = (np.isfinite(x_trans) & np.isfinite(y_trans))
                if np.sum(finite_mask) < 3:
                    continue
                
                x_trans = x_trans[finite_mask]
                y_trans = y_trans[finite_mask]
                
                # Compute linearity score (R^2)
                if len(x_trans) > 2:
                    coeffs = np.polyfit(x_trans, y_trans, 1)
                    y_pred = coeffs[0] * x_trans + coeffs[1]
                    ss_res = np.sum((y_trans - y_pred) ** 2)
                    ss_tot = np.sum((y_trans - np.mean(y_trans)) ** 2)
                    r_squared = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
                    
                    # Compute smoothness score (inverse of second derivative magnitude)
                    if len(y_trans) > 2:
                        second_deriv = np.abs(np.diff(y_trans, 2))
                        smoothness = 1.0 / (1.0 + np.mean(second_deriv))
                    else:
                        smoothness = 1.0
                    
                    # Combined score
                    score = linearity_weight * r_squared + smoothness_weight * smoothness
                    
                    if score > best_score:
                        best_score = score
                        best_pair = (alpha, beta)
                        
            except (ValueError, RuntimeWarning, OverflowError, ZeroDivisionError):
                continue
    
    return best_pair[0], best_pair[1], best_score


def integration_convergence_test(
    meta_int: MetaIntegral,
    f: Callable,
    a: float, b: float,
    n_points_list: list = None
) -> dict:
    """Test convergence of meta-integration with increasing resolution.
    
    Args:
        meta_int: MetaIntegral object to test
        f: Function to integrate
        a, b: Integration bounds
        n_points_list: List of point counts to test
        
    Returns:
        Dictionary with convergence analysis
    """
    if n_points_list is None:
        n_points_list = [100, 200, 500, 1000, 2000, 5000]
    
    results = []
    errors = []
    
    for n_points in n_points_list:
        try:
            result = meta_int.integrate(f, a, b, n_points)
            results.append(result)
        except Exception as e:
            results.append(np.nan)
    
    # Compute convergence errors (assuming last result is most accurate)
    if len(results) > 1 and np.isfinite(results[-1]):
        reference = results[-1]
        errors = [abs(r - reference) for r in results[:-1]]
    
    # Estimate convergence rate
    convergence_rate = np.nan
    if len(errors) > 2:
        # Fit power law: error ∝ n^(-p)
        valid_errors = [(n, e) for n, e in zip(n_points_list[:-1], errors) if e > 0]
        if len(valid_errors) > 2:
            n_vals, error_vals = zip(*valid_errors)
            log_n = np.log(n_vals)
            log_error = np.log(error_vals)
            convergence_rate = -np.polyfit(log_n, log_error, 1)[0]
    
    return {
        'n_points': n_points_list,
        'results': results,
        'errors': errors,
        'convergence_rate': convergence_rate,
        'final_result': results[-1] if results else np.nan,
        'relative_precision': errors[-1] / abs(results[-1]) if len(errors) > 0 and results[-1] != 0 else np.nan
    }


def compare_integration_methods(
    meta_int: MetaIntegral,
    f: Callable,
    a: float, b: float,
    methods: list = None
) -> dict:
    """Compare different integration methods for meta-calculus.
    
    Args:
        meta_int: MetaIntegral object
        f: Function to integrate
        a, b: Integration bounds
        methods: List of methods to compare
        
    Returns:
        Dictionary comparing method performance
    """
    if methods is None:
        methods = ['simpson', 'trapezoid', 'adaptive']
    
    results = {}
    
    for method in methods:
        try:
            import time
            start_time = time.time()
            
            if method == 'adaptive':
                result = meta_int._adaptive_integrate(f, a, b)
            else:
                result = meta_int.integrate(f, a, b, method=method)
            
            end_time = time.time()
            
            results[method] = {
                'result': result,
                'time': end_time - start_time,
                'success': True
            }
            
        except Exception as e:
            results[method] = {
                'result': np.nan,
                'time': np.nan,
                'success': False,
                'error': str(e)
            }
    
    # Compute relative differences
    if len([r for r in results.values() if r['success']]) > 1:
        values = [r['result'] for r in results.values() if r['success']]
        reference = np.mean(values)
        
        for method in results:
            if results[method]['success']:
                results[method]['relative_error'] = (
                    abs(results[method]['result'] - reference) / 
                    (abs(reference) + 1e-10)
                )
    
    return results


class MetaIntegralSolver:
    """Advanced solver for meta-calculus integration problems.
    
    Provides high-level interface for solving complex integration
    problems with automatic method selection and error control.
    """
    
    def __init__(self, 
                 alpha: AlphaGenerator, 
                 beta: BetaGenerator,
                 u: Optional[Callable] = None,
                 rtol: float = 1e-8,
                 atol: float = 1e-12):
        """Initialize meta-integral solver.
        
        Args:
            alpha, beta: Generator functions
            u: Weight function
            rtol: Relative tolerance
            atol: Absolute tolerance
        """
        self.meta_int = MetaIntegral(alpha, beta, u)
        self.rtol = rtol
        self.atol = atol
    
    def solve(self, f: Callable, a: float, b: float,
              auto_method: bool = True) -> dict:
        """Solve integration problem with automatic method selection.
        
        Args:
            f: Function to integrate
            a, b: Integration bounds
            auto_method: Whether to automatically select best method
            
        Returns:
            Dictionary with solution and diagnostics
        """
        if auto_method:
            # Test different methods and select best
            methods_results = compare_integration_methods(
                self.meta_int, f, a, b
            )
            
            # Select method with best accuracy/speed tradeoff
            best_method = self._select_best_method(methods_results)
            result = methods_results[best_method]['result']
            
            return {
                'result': result,
                'method_used': best_method,
                'all_methods': methods_results,
                'convergence_test': integration_convergence_test(
                    self.meta_int, f, a, b
                )
            }
        else:
            # Use adaptive method
            result = self.meta_int.integrate(f, a, b, method='adaptive')
            return {'result': result, 'method_used': 'adaptive'}
    
    def _select_best_method(self, methods_results: dict) -> str:
        """Select best integration method based on accuracy and speed."""
        successful_methods = {
            method: results for method, results in methods_results.items()
            if results['success']
        }
        
        if not successful_methods:
            return 'simpson'  # Fallback
        
        # Score based on accuracy and speed
        best_score = -np.inf
        best_method = list(successful_methods.keys())[0]
        
        for method, results in successful_methods.items():
            # Higher score for lower relative error and faster time
            accuracy_score = 1.0 / (results.get('relative_error', 1.0) + 1e-10)
            speed_score = 1.0 / (results['time'] + 1e-10)
            
            # Combined score (favor accuracy over speed)
            score = 0.8 * accuracy_score + 0.2 * speed_score
            
            if score > best_score:
                best_score = score
                best_method = method
        
        return best_method