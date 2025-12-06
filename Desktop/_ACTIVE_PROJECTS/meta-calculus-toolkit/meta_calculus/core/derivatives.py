"""
Meta-derivatives for non-Newtonian calculus.

Implements the Grossman Unified Calculus (GUC) derivative operators:

1. GEOMETRIC DERIVATIVE: D_G[f](a) = exp(f'(a) / f(a))
   - Measures MULTIPLICATIVE rates of change
   - Exponentials become "linear" (constant derivative)

2. BIGEOMETRIC DERIVATIVE: D_BG[f](a) = exp(a * f'(a) / f(a))
   - Measures scale-invariant changes
   - Power functions become "linear" (constant derivative)
   - Example: D_BG[x^n] = e^n (independent of x!)

3. META-DERIVATIVE: D_hat[f](a) = (v(a) / u(a)) * f'(a)
   - Weighted classical derivative
   - Changes how we MEASURE intervals (not arithmetic)

4. UNIFIED DERIVATIVE: D*_w[f](a) = (v(f(a)) / u(a)) * beta([D f-bar](a-bar))
   - Full GUC combining NNC + meta-calculus
   - Transforms: f-bar(t) = beta^-1(f(alpha(t))), a-bar = alpha^-1(a)

This module provides the core differentiation capabilities for meta-calculus,
allowing computation of derivatives in transformed coordinate systems.

Reference: UNIFIED_CALCULUS_TEXTBOOK.md (Grossman synthesis)
"""

import numpy as np
from typing import Callable, Optional, Union
try:
    from .generators import AlphaGenerator, BetaGenerator, Identity
except ImportError:
    from meta_calculus.core.generators import AlphaGenerator, BetaGenerator, Identity

ArrayLike = Union[float, np.ndarray]


class GeometricDerivative:
    """Compute geometric derivatives (alpha=I, beta=exp).

    The geometric derivative measures MULTIPLICATIVE rates of change:

    D_G[f](a) = lim_{x->a} [f(x)/f(a)]^{1/(x-a)}

    EXPLICIT FORMULA:
    D_G[f](a) = exp(f'(a) / f(a))

    Key Property:
    - Exponential functions have CONSTANT geometric derivative
    - D_G[e^{kx}] = e^k (independent of x)

    Mathematical Basis:
    - Transform: f-bar(t) = ln(f(t))
    - Differentiate: [D f-bar](a) = f'(a)/f(a)
    - Transform back: D_G[f](a) = exp(f'(a)/f(a))
    """

    def __init__(self, epsilon: float = 1e-100):
        """Initialize geometric derivative operator.

        Args:
            epsilon: Safety threshold for division by zero
        """
        self.epsilon = epsilon

    def __call__(self, f: Callable[[ArrayLike], ArrayLike],
                 x: ArrayLike,
                 dx: Optional[float] = None,
                 method: str = 'central') -> ArrayLike:
        """Compute the geometric derivative of f at points x.

        Args:
            f: Function to differentiate (must be positive)
            x: Points at which to evaluate the derivative
            dx: Spacing for numerical differentiation (auto if None)
            method: Differentiation method ('central', 'forward', 'backward')

        Returns:
            Geometric derivative values: exp(f'(x) / f(x))
        """
        x = np.atleast_1d(x).astype(float)

        # Compute classical derivative numerically
        df_dx = self._numerical_derivative(f, x, dx, method)

        # Evaluate function at x
        fx = f(x)

        # Handle potential division by zero
        fx_safe = np.where(np.abs(fx) < self.epsilon, self.epsilon, fx)

        # Compute geometric derivative: exp(f'(x) / f(x))
        geo_deriv = np.exp(df_dx / fx_safe)

        return geo_deriv

    def _numerical_derivative(self, f: Callable, x: ArrayLike,
                            dx: Optional[float] = None,
                            method: str = 'central') -> ArrayLike:
        """Compute numerical derivative using specified method.

        Args:
            f: Function to differentiate
            x: Points for differentiation
            dx: Step size (auto-computed if None)
            method: Differentiation method

        Returns:
            Numerical derivative values
        """
        x = np.asarray(x)

        # Auto-compute step size if not provided
        if dx is None:
            if len(x) > 1:
                dx = np.mean(np.abs(np.diff(x))) * 0.01
            else:
                dx = np.abs(x[0]) * 1e-8 if x[0] != 0 else 1e-8

        if method == 'central':
            return (f(x + dx) - f(x - dx)) / (2 * dx)
        elif method == 'forward':
            return (f(x + dx) - f(x)) / dx
        elif method == 'backward':
            return (f(x) - f(x - dx)) / dx
        else:
            raise ValueError(f"Unknown differentiation method: {method}")


class BigeometricDerivative:
    """Compute bigeometric derivatives (alpha=exp, beta=exp).

    The bigeometric derivative measures SCALE-INVARIANT rates of change:

    D_BG[f](a) = lim_{x->a} [f(x)/f(a)]^{1/ln(x/a)}

    EXPLICIT FORMULA:
    D_BG[f](a) = exp(a * f'(a) / f(a))

    The expression a * f'(a) / f(a) is called the ELASTICITY.
    The bigeometric derivative exp(elasticity) is called the RESILIENCY.

    CRITICAL PROPERTY - Scale Invariance:
    - Power functions have CONSTANT bigeometric derivative
    - D_BG[x^n] = e^n (independent of x!)
    - Example: D_BG[x^3] = e^3 for all x > 0

    Physics Application:
    - Power-law singularities f(r) ~ r^n appear as "linear" in bigeometric calculus
    - The singularity is "tamed" - derivative remains finite even as r -> 0

    Mathematical Basis:
    - Transform: f-bar(t) = ln(f(exp(t)))
    - For f(x) = x^n: f-bar(t) = ln(exp(nt)) = nt
    - Differentiate: [D f-bar](ln(a)) = n
    - Transform back: D_BG[f](a) = exp(n)
    """

    def __init__(self, epsilon: float = 1e-100):
        """Initialize bigeometric derivative operator.

        Args:
            epsilon: Safety threshold for division by zero
        """
        self.epsilon = epsilon

    def __call__(self, f: Callable[[ArrayLike], ArrayLike],
                 x: ArrayLike,
                 dx: Optional[float] = None,
                 method: str = 'central') -> ArrayLike:
        """Compute the bigeometric derivative of f at points x.

        Args:
            f: Function to differentiate (must be positive on positive domain)
            x: Points at which to evaluate the derivative (must be positive)
            dx: Spacing for numerical differentiation (auto if None)
            method: Differentiation method ('central', 'forward', 'backward')

        Returns:
            Bigeometric derivative values: exp(x * f'(x) / f(x))
        """
        x = np.atleast_1d(x).astype(float)

        # Compute classical derivative numerically
        df_dx = self._numerical_derivative(f, x, dx, method)

        # Evaluate function at x
        fx = f(x)

        # Handle potential division by zero
        fx_safe = np.where(np.abs(fx) < self.epsilon, self.epsilon, fx)

        # Compute bigeometric derivative: exp(x * f'(x) / f(x))
        # This is the ELASTICITY formula
        elasticity = x * df_dx / fx_safe
        bigeo_deriv = np.exp(elasticity)

        return bigeo_deriv

    def _numerical_derivative(self, f: Callable, x: ArrayLike,
                            dx: Optional[float] = None,
                            method: str = 'central') -> ArrayLike:
        """Compute numerical derivative using specified method.

        Args:
            f: Function to differentiate
            x: Points for differentiation
            dx: Step size (auto-computed if None)
            method: Differentiation method

        Returns:
            Numerical derivative values
        """
        x = np.asarray(x)

        # Auto-compute step size if not provided
        if dx is None:
            if len(x) > 1:
                dx = np.mean(np.abs(np.diff(x))) * 0.01
            else:
                dx = np.abs(x[0]) * 1e-8 if x[0] != 0 else 1e-8

        if method == 'central':
            return (f(x + dx) - f(x - dx)) / (2 * dx)
        elif method == 'forward':
            return (f(x + dx) - f(x)) / dx
        elif method == 'backward':
            return (f(x) - f(x - dx)) / dx
        else:
            raise ValueError(f"Unknown differentiation method: {method}")


class MetaDerivative:
    """Compute meta-derivatives (weighted classical derivatives).

    The meta-derivative uses weight functions to change how we MEASURE:

    [D-hat f](a) = (v(a) / u(a)) * f'(a)

    This is fundamentally different from NNC:
    - NNC: Changes the ARITHMETIC STRUCTURE (how we add/subtract)
    - Meta-Calculus: Changes the WEIGHTING (density of contributions)

    Weight Functions:
    - u(x): Weight for independent variable (argument density)
    - v(y): Weight for dependent variable (value density)

    Meta-Uniform Functions:
    - Functions with constant meta-derivative
    - Form: f(x) = b * W(x) + c
    - Where W(x) = integral_0^x (u(t)/v(t)) dt

    When to Use:
    - Measuring contributions with non-uniform density
    - Integrating with respect to non-standard measures
    - Modeling systems with spatially-varying properties

    Mathematical Basis:
    - Meta-measure: mu[r,s] = integral_r^s u(x) dx
    - Meta-change: C[r,s]f = integral_r^s v(x)*f'(x) dx
    - Meta-derivative: D-hat[f](a) = lim_{x->a} C[a,x]f / mu[a,x]
    """

    def __init__(self,
                 u: Optional[Callable[[ArrayLike], ArrayLike]] = None,
                 v: Optional[Callable[[ArrayLike], ArrayLike]] = None,
                 epsilon: float = 1e-100):
        """Initialize meta-derivative operator.

        Args:
            u: Weight function for independent variable (default: unity)
            v: Weight function for dependent variable (default: unity)
            epsilon: Safety threshold for division by zero
        """
        self.u = u if u is not None else lambda x: np.ones_like(np.asarray(x))
        self.v = v if v is not None else lambda y: np.ones_like(np.asarray(y))
        self.epsilon = epsilon

    def __call__(self, f: Callable[[ArrayLike], ArrayLike],
                 x: ArrayLike,
                 dx: Optional[float] = None,
                 method: str = 'central') -> ArrayLike:
        """Compute the meta-derivative of f at points x.

        Args:
            f: Function to differentiate
            x: Points at which to evaluate the derivative
            dx: Spacing for numerical differentiation (auto if None)
            method: Differentiation method ('central', 'forward', 'backward')

        Returns:
            Meta-derivative values: (v(x) / u(x)) * f'(x)
        """
        x = np.atleast_1d(x).astype(float)

        # Compute classical derivative numerically
        df_dx = self._numerical_derivative(f, x, dx, method)

        # Compute weight functions at x (NOT at f(x) - this is meta, not NNC)
        u_x = self.u(x)
        v_x = self.v(x)

        # Handle potential division by zero
        u_x_safe = np.where(np.abs(u_x) < self.epsilon, self.epsilon, u_x)

        # Compute meta-derivative: (v(x) / u(x)) * f'(x)
        meta_deriv = (v_x / u_x_safe) * df_dx

        return meta_deriv

    def _numerical_derivative(self, f: Callable, x: ArrayLike,
                            dx: Optional[float] = None,
                            method: str = 'central') -> ArrayLike:
        """Compute numerical derivative using specified method.

        Args:
            f: Function to differentiate
            x: Points for differentiation
            dx: Step size (auto-computed if None)
            method: Differentiation method

        Returns:
            Numerical derivative values
        """
        x = np.asarray(x)

        # Auto-compute step size if not provided
        if dx is None:
            if len(x) > 1:
                dx = np.mean(np.abs(np.diff(x))) * 0.01
            else:
                dx = np.abs(x[0]) * 1e-8 if x[0] != 0 else 1e-8

        if method == 'central':
            return (f(x + dx) - f(x - dx)) / (2 * dx)
        elif method == 'forward':
            return (f(x + dx) - f(x)) / dx
        elif method == 'backward':
            return (f(x) - f(x - dx)) / dx
        else:
            raise ValueError(f"Unknown differentiation method: {method}")


class UnifiedDerivative:
    """Compute Grossman Unified Calculus (GUC) derivatives.

    The unified derivative combines NNC (non-Newtonian calculus) with meta-calculus:

    [D*_w f](a) = (v(f(a)) / u(a)) * [D*f](a)

    where [D*f](a) is the pure NNC star-derivative.

    FULLY EXPANDED FORM:
    [D*_w f](a) = (v(f(a)) / u(a)) * beta([D f-bar](a-bar))

    where:
    - f-bar(t) = beta^{-1}(f(alpha(t)))
    - a-bar = alpha^{-1}(a)
    - [D f-bar](a-bar) is the classical derivative of the transformed function

    Components:
    - alpha: Generator for argument arithmetic (how we measure changes in x)
    - beta: Generator for value arithmetic (how we measure changes in f(x))
    - u(x): Weight function for arguments (meta-measure density)
    - v(y): Weight function for values (meta-change density)

    Special Cases:
    - Classical: alpha=I, beta=I, u=1, v=1 -> f'(a)
    - Geometric: alpha=I, beta=exp, u=1, v=1 -> exp(f'(a)/f(a))
    - Bigeometric: alpha=exp, beta=exp, u=1, v=1 -> exp(a*f'(a)/f(a))
    - Meta: alpha=I, beta=I, u(x), v(x) -> (v(a)/u(a))*f'(a)

    Mathematical Basis:
    The star-derivative transforms to classical coordinates:
    1. Apply alpha^{-1} to argument: a -> a-bar
    2. Compose with beta^{-1} for values: f -> f-bar
    3. Differentiate classically: [D f-bar](a-bar)
    4. Transform back via beta: D*[f](a) = beta([D f-bar](a-bar))
    5. Apply meta-weights: (v(f(a)) / u(a)) * D*[f](a)
    """

    def __init__(self,
                 alpha: AlphaGenerator,
                 beta: BetaGenerator,
                 u: Optional[Callable[[ArrayLike], ArrayLike]] = None,
                 v: Optional[Callable[[ArrayLike], ArrayLike]] = None,
                 epsilon: float = 1e-100):
        """Initialize unified derivative operator.

        Args:
            alpha: Generator for independent variable transformation
            beta: Generator for dependent variable transformation
            u: Weight function for independent variable (default: unity)
            v: Weight function for dependent variable (default: unity)
            epsilon: Safety threshold for division by zero
        """
        self.alpha = alpha
        self.beta = beta
        self.u = u if u is not None else lambda x: np.ones_like(np.asarray(x))
        self.v = v if v is not None else lambda y: np.ones_like(np.asarray(y))
        self.epsilon = epsilon

    def __call__(self, f: Callable[[ArrayLike], ArrayLike],
                 x: ArrayLike,
                 dx: Optional[float] = None,
                 method: str = 'central') -> ArrayLike:
        """Compute the unified derivative of f at points x.

        Args:
            f: Function to differentiate
            x: Points at which to evaluate the derivative
            dx: Spacing for numerical differentiation (auto if None)
            method: Differentiation method ('central', 'forward', 'backward')

        Returns:
            Unified derivative values
        """
        x = np.atleast_1d(x).astype(float)

        # Compute classical derivative numerically
        df_dx = self._numerical_derivative(f, x, dx, method)

        # Evaluate function at x
        fx = f(x)

        # Compute generator derivatives
        alpha_prime = self.alpha.derivative(x)
        beta_prime = self.beta.derivative(fx)

        # Compute weight functions
        # NOTE: v is evaluated at f(x), not at x (this is the GUC formula)
        u_x = self.u(x)
        v_fx = self.v(fx)

        # Handle potential division by zero
        alpha_prime_safe = np.where(np.abs(alpha_prime) < self.epsilon,
                                    self.epsilon, alpha_prime)
        u_x_safe = np.where(np.abs(u_x) < self.epsilon,
                           self.epsilon, u_x)

        # Compute GUC derivative:
        # [D*_w f](a) = (v(f(a)) / u(a)) * beta'(f(a)) * f'(a) / alpha'(a)
        unified_deriv = (v_fx / u_x_safe) * beta_prime * df_dx / alpha_prime_safe

        return unified_deriv

    def _numerical_derivative(self, f: Callable, x: ArrayLike,
                            dx: Optional[float] = None,
                            method: str = 'central') -> ArrayLike:
        """Compute numerical derivative using specified method.

        Args:
            f: Function to differentiate
            x: Points for differentiation
            dx: Step size (auto-computed if None)
            method: Differentiation method

        Returns:
            Numerical derivative values
        """
        x = np.asarray(x)

        # Auto-compute step size if not provided
        if dx is None:
            if len(x) > 1:
                dx = np.mean(np.abs(np.diff(x))) * 0.01
            else:
                dx = np.abs(x[0]) * 1e-8 if x[0] != 0 else 1e-8

        if method == 'central':
            return (f(x + dx) - f(x - dx)) / (2 * dx)
        elif method == 'forward':
            return (f(x + dx) - f(x)) / dx
        elif method == 'backward':
            return (f(x) - f(x - dx)) / dx
        else:
            raise ValueError(f"Unknown differentiation method: {method}")

    def higher_order(self, f: Callable, x: ArrayLike, order: int = 2,
                    dx: Optional[float] = None) -> ArrayLike:
        """Compute higher-order unified derivatives.

        Args:
            f: Function to differentiate
            x: Points for differentiation
            order: Order of derivative (2, 3, 4, ...)
            dx: Step size

        Returns:
            Higher-order unified derivative values
        """
        if order < 1:
            raise ValueError("Order must be at least 1")
        if order == 1:
            return self(f, x, dx)

        # Recursive computation of higher derivatives
        def unified_f(xi):
            return self(f, xi, dx)

        # Create new unified derivative operator for the next order
        unified_deriv_next = UnifiedDerivative(self.alpha, self.beta, self.u, self.v, self.epsilon)
        return unified_deriv_next.higher_order(unified_f, x, order - 1, dx)

    def gradient(self, f: Callable, x: ArrayLike,
                variables: Optional[list] = None) -> ArrayLike:
        """Compute unified gradient for multivariable functions.

        Args:
            f: Multivariable function f(x1, x2, ..., xn)
            x: Point at which to evaluate gradient
            variables: List of variable indices to differentiate

        Returns:
            Unified gradient vector
        """
        x = np.atleast_1d(x)
        if variables is None:
            variables = list(range(len(x)))

        gradient = np.zeros(len(variables))

        for i, var_idx in enumerate(variables):
            # Create partial derivative function
            def partial_f(xi):
                x_temp = x.copy()
                x_temp[var_idx] = xi
                return f(x_temp)

            # Compute partial unified derivative
            gradient[i] = self(partial_f, x[var_idx])

        return gradient

    def chain_rule(self, g: Callable, f: Callable, x: ArrayLike) -> ArrayLike:
        """Apply unified calculus chain rule.

        Args:
            g: Outer function
            f: Inner function
            x: Points for evaluation

        Returns:
            Chain rule result
        """
        # Compute D*_w f at x
        df_dx_unified = self(f, x)

        # Evaluate f at x
        fx = f(x)

        # Compute D*_w g at y = f(x)
        dg_dy_unified = self(g, fx)

        return dg_dy_unified * df_dx_unified


class StarDerivative(UnifiedDerivative):
    """Simplified star-derivative without weight functions (pure NNC).

    D*f/dx* = beta'(f(x)) * f'(x) / alpha'(x)

    This is the pure non-Newtonian calculus derivative,
    focusing purely on the arithmetic transformations.

    Equivalent to UnifiedDerivative with u=1, v=1.
    """

    def __init__(self, alpha: AlphaGenerator, beta: BetaGenerator, epsilon: float = 1e-100):
        """Initialize star derivative with unity weights.

        Args:
            alpha: Generator for independent variable transformation
            beta: Generator for dependent variable transformation
            epsilon: Safety threshold for division by zero
        """
        super().__init__(alpha, beta, u=None, v=None, epsilon=epsilon)


class AdaptiveMetaDerivative(UnifiedDerivative):
    """Unified derivative with adaptive step size selection.

    Automatically adjusts the numerical differentiation step size
    to optimize accuracy while maintaining numerical stability.
    """

    def __init__(self, alpha: AlphaGenerator, beta: BetaGenerator,
                 u: Optional[Callable] = None, v: Optional[Callable] = None,
                 rtol: float = 1e-8, atol: float = 1e-12, epsilon: float = 1e-100):
        """Initialize adaptive unified derivative.

        Args:
            alpha, beta: Generator functions
            u, v: Weight functions
            rtol: Relative tolerance for step size adaptation
            atol: Absolute tolerance for step size adaptation
            epsilon: Safety threshold for division by zero
        """
        super().__init__(alpha, beta, u, v, epsilon)
        self.rtol = rtol
        self.atol = atol

    def __call__(self, f: Callable, x: ArrayLike,
                 dx: Optional[float] = None) -> ArrayLike:
        """Compute unified derivative with adaptive step size.

        Args:
            f: Function to differentiate
            x: Points for evaluation
            dx: Initial step size guess

        Returns:
            Unified derivative with optimized accuracy
        """
        x = np.atleast_1d(x).astype(float)
        result = np.zeros_like(x)

        for i, xi in enumerate(x):
            result[i] = self._adaptive_derivative_point(f, xi, dx)

        return result

    def _adaptive_derivative_point(self, f: Callable, x: float,
                                 dx_initial: Optional[float] = None) -> float:
        """Compute adaptive derivative at a single point.

        Uses Richardson extrapolation and error estimation to
        find the optimal step size.
        """
        if dx_initial is None:
            dx_initial = abs(x) * 1e-8 if x != 0 else 1e-8

        # Try multiple step sizes
        step_sizes = [dx_initial * (0.5 ** i) for i in range(5)]
        derivatives = []

        for dx in step_sizes:
            try:
                # Use central difference
                deriv_classical = (f(x + dx) - f(x - dx)) / (2 * dx)

                # Transform to unified derivative
                fx = f(x)
                alpha_prime = self.alpha.derivative(x)
                beta_prime = self.beta.derivative(fx)
                u_x = self.u(x)
                v_fx = self.v(fx)

                # Safe division
                alpha_prime_safe = alpha_prime if abs(alpha_prime) > self.epsilon else self.epsilon
                u_x_safe = u_x if abs(u_x) > self.epsilon else self.epsilon

                unified_deriv = (v_fx / u_x_safe) * beta_prime * deriv_classical / alpha_prime_safe
                derivatives.append(unified_deriv)

            except (OverflowError, ZeroDivisionError, ValueError):
                derivatives.append(np.nan)

        # Find the most stable result
        valid_derivatives = [d for d in derivatives if np.isfinite(d)]

        if len(valid_derivatives) >= 2:
            # Use Richardson extrapolation between the two smallest step sizes
            return self._richardson_extrapolation(valid_derivatives[:2])
        elif len(valid_derivatives) == 1:
            return valid_derivatives[0]
        else:
            # Fallback to standard method
            return super().__call__(f, np.array([x]))[0]

    def _richardson_extrapolation(self, derivatives: list) -> float:
        """Apply Richardson extrapolation to improve accuracy.

        For central differences with step sizes h and h/2:
        f'(x) ~= (4*D(h/2) - D(h)) / 3
        """
        if len(derivatives) >= 2:
            D_h = derivatives[1]  # Larger step size
            D_h2 = derivatives[0]  # Smaller step size
            return (4 * D_h2 - D_h) / 3
        else:
            return derivatives[0]


def verify_derivative_accuracy(deriv_operator,
                             f: Callable,
                             analytical_derivative: Callable,
                             x_test: ArrayLike,
                             rtol: float = 1e-6) -> dict:
    """Verify accuracy of derivative computation.

    Args:
        deriv_operator: Derivative operator to test (any class from this module)
        f: Function to differentiate
        analytical_derivative: Known analytical derivative
        x_test: Test points
        rtol: Relative tolerance for accuracy check

    Returns:
        Dictionary with accuracy metrics
    """
    x_test = np.atleast_1d(x_test)

    # Compute numerical derivative using operator
    numerical = deriv_operator(f, x_test)

    # Compute analytical derivative
    analytical = analytical_derivative(x_test)

    # Compute error metrics
    absolute_error = np.abs(numerical - analytical)
    relative_error = absolute_error / (np.abs(analytical) + 1e-100)

    return {
        'max_absolute_error': np.max(absolute_error),
        'max_relative_error': np.max(relative_error),
        'mean_absolute_error': np.mean(absolute_error),
        'mean_relative_error': np.mean(relative_error),
        'passes_tolerance': np.all(relative_error < rtol),
        'numerical_values': numerical,
        'analytical_values': analytical,
        'errors': absolute_error
    }


def compare_derivative_methods(f: Callable, x: ArrayLike,
                             alpha: AlphaGenerator, beta: BetaGenerator,
                             methods: list = None) -> dict:
    """Compare different numerical differentiation methods.

    Args:
        f: Function to differentiate
        x: Test points
        alpha, beta: Generator functions
        methods: List of methods to compare

    Returns:
        Dictionary comparing method performance
    """
    if methods is None:
        methods = ['central', 'forward', 'backward']

    results = {}

    for method in methods:
        unified_deriv = UnifiedDerivative(alpha, beta)
        try:
            result = unified_deriv(f, x, method=method)
            results[method] = {
                'values': result,
                'success': True,
                'max_value': np.max(np.abs(result)),
                'stability': np.std(result) / (np.mean(np.abs(result)) + 1e-100)
            }
        except Exception as e:
            results[method] = {
                'values': None,
                'success': False,
                'error': str(e)
            }

    return results
