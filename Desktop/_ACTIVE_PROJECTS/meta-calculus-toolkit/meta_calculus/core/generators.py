"""
Generator functions for meta-calculus transformations.

This module provides alpha (argument) and beta (value) generator functions that
transform standard calculus into alternative mathematical frameworks where
different types of relationships become linear.
"""

import numpy as np
from abc import ABC, abstractmethod
from typing import Union, Callable, Optional
import warnings

ArrayLike = Union[float, np.ndarray]


class Generator(ABC):
    """Abstract base class for all generator functions."""
    
    @abstractmethod
    def __call__(self, x: ArrayLike) -> ArrayLike:
        """Apply the generator transformation."""
        pass
    
    @abstractmethod
    def derivative(self, x: ArrayLike) -> ArrayLike:
        """Compute the derivative of the generator."""
        pass
    
    @abstractmethod
    def inverse(self, y: ArrayLike) -> ArrayLike:
        """Compute the inverse transformation."""
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"


class AlphaGenerator(Generator):
    """Base class for alpha (argument) generators."""
    pass


class BetaGenerator(Generator):
    """Base class for beta (value) generators."""
    pass


# Concrete generator implementations

class Identity(AlphaGenerator, BetaGenerator):
    """Identity generator: alpha(x) = x
    
    This is the classical calculus generator that leaves coordinates unchanged.
    Used as the default when no transformation is needed.
    """
    
    def __call__(self, x: ArrayLike) -> ArrayLike:
        return np.asarray(x, dtype=float)
    
    def derivative(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x)
        return np.ones_like(x, dtype=float)
    
    def inverse(self, y: ArrayLike) -> ArrayLike:
        return np.asarray(y, dtype=float)


class Exponential(AlphaGenerator, BetaGenerator):
    """Exponential generator: alpha(x) = exp(x)
    
    Transforms exponential relationships into linear ones.
    Useful for growth/decay processes and multiplicative phenomena.
    """
    
    def __call__(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        # Prevent overflow for very large x
        x_clipped = np.clip(x, -700, 700)
        if not np.array_equal(x, x_clipped):
            warnings.warn("Input clipped to prevent overflow in exponential", RuntimeWarning)
        return np.exp(x_clipped)
    
    def derivative(self, x: ArrayLike) -> ArrayLike:
        return self(x)  # d/dx exp(x) = exp(x)
    
    def inverse(self, y: ArrayLike) -> ArrayLike:
        y = np.asarray(y, dtype=float)
        # Handle negative and zero values
        y_safe = np.where(y <= 0, 1e-100, y)
        return np.log(y_safe)


class Log(AlphaGenerator, BetaGenerator):
    """Logarithmic generator: alpha(x) = ln(x)
    
    Transforms power law relationships into linear ones.
    Useful for scaling relationships and multiplicative processes.
    """
    
    def __call__(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        # Handle negative and zero values
        x_safe = np.where(x <= 0, 1e-100, np.abs(x))
        result = np.log(x_safe)
        # Preserve sign for negative inputs
        return np.where(x < 0, -result, result)
    
    def derivative(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        x_safe = np.where(np.abs(x) < 1e-100, 1e-100, x)
        return 1.0 / x_safe
    
    def inverse(self, y: ArrayLike) -> ArrayLike:
        y = np.asarray(y, dtype=float)
        return np.exp(y)


class Power(AlphaGenerator, BetaGenerator):
    """Power generator: alpha(x) = x^p
    
    Transforms polynomial relationships with specific powers.
    Generalizes square, cube, and other power transformations.
    """
    
    def __init__(self, p: float):
        if p == 0:
            raise ValueError("Power p cannot be zero")
        self.p = p
    
    def __call__(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        if self.p == int(self.p) and int(self.p) % 2 == 1:
            # Odd integer powers preserve sign
            return np.sign(x) * np.abs(x) ** self.p
        else:
            # Even powers or non-integer powers
            x_safe = np.where(x < 0, 0, x)  # Handle negative values
            return x_safe ** self.p
    
    def derivative(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        if self.p == 1:
            return np.ones_like(x)
        
        if self.p == int(self.p) and int(self.p) % 2 == 1:
            # Odd integer powers
            return self.p * np.abs(x) ** (self.p - 1)
        else:
            # Even powers or non-integer powers
            x_safe = np.where(x <= 0, 1e-100, x)
            return self.p * x_safe ** (self.p - 1)
    
    def inverse(self, y: ArrayLike) -> ArrayLike:
        y = np.asarray(y, dtype=float)
        if self.p == int(self.p) and int(self.p) % 2 == 1:
            # Odd integer powers preserve sign
            return np.sign(y) * np.abs(y) ** (1.0 / self.p)
        else:
            # Even powers or non-integer powers
            y_safe = np.where(y < 0, 0, y)
            return y_safe ** (1.0 / self.p)
    
    def __repr__(self):
        return f"Power(p={self.p})"


class Reciprocal(AlphaGenerator, BetaGenerator):
    """Reciprocal generator: alpha(x) = 1/x
    
    Transforms harmonic relationships and inverse proportionalities.
    Useful for physical laws with inverse dependencies.
    """
    
    def __call__(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        x_safe = np.where(np.abs(x) < 1e-100, 1e-100, x)
        return 1.0 / x_safe
    
    def derivative(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        x_safe = np.where(np.abs(x) < 1e-100, 1e-100, x)
        return -1.0 / (x_safe ** 2)
    
    def inverse(self, y: ArrayLike) -> ArrayLike:
        return self(y)  # 1/(1/x) = x


class Sqrt(AlphaGenerator, BetaGenerator):
    """Square root generator: alpha(x) = sqrtx
    
    Transforms quadratic relationships into linear ones.
    Commonly used in physics for energy-momentum relationships.
    """
    
    def __call__(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        # Handle negative values by taking sqrt of absolute value
        return np.sqrt(np.abs(x))
    
    def derivative(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        x_safe = np.where(np.abs(x) < 1e-100, 1e-100, np.abs(x))
        return 0.5 / np.sqrt(x_safe)
    
    def inverse(self, y: ArrayLike) -> ArrayLike:
        y = np.asarray(y, dtype=float)
        return y ** 2


class ScaleDependent(AlphaGenerator):
    """Scale-dependent generator for quantum-classical transitions.
    
    alpha(x; ℓ) = x*exp(-x^2/ℓ^2) + sign(x)*ℓ*exp(|x|/ℓ)*[1 - exp(-x^2/ℓ^2)]
    
    For |x| << ℓ: alpha(x;ℓ) ~= x (quantum/additive regime)
    For |x| >> ℓ: alpha(x;ℓ) ~= sign(x)*ℓ*exp(|x|/ℓ) (classical/multiplicative regime)
    
    This generator smoothly interpolates between quantum and classical physics
    at the characteristic scale ℓ.
    """
    
    def __init__(self, scale: float):
        if scale <= 0:
            raise ValueError("Scale must be positive")
        self.scale = scale
    
    def __call__(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        x_scaled = x / self.scale
        exp_factor = np.exp(-x_scaled**2)
        
        # Quantum part: x * exp(-x^2/ℓ^2)
        quantum_part = x * exp_factor
        
        # Classical part: sign(x) * ℓ * exp(|x|/ℓ) * [1 - exp(-x^2/ℓ^2)]
        # Clip to prevent overflow
        abs_x_scaled = np.clip(np.abs(x_scaled), 0, 700)
        classical_part = (np.sign(x) * self.scale * 
                         np.exp(abs_x_scaled) * (1 - exp_factor))
        
        return quantum_part + classical_part
    
    def derivative(self, x: ArrayLike) -> ArrayLike:
        x = np.asarray(x, dtype=float)
        x_scaled = x / self.scale
        exp_factor = np.exp(-x_scaled**2)
        
        # d/dx of quantum part: exp(-x^2/ℓ^2) * (1 - 2x^2/ℓ^2)
        dquantum = exp_factor * (1 - 2 * x_scaled**2)
        
        # d/dx of classical part
        abs_x_scaled = np.clip(np.abs(x_scaled), 0, 700)
        sign_x = np.sign(x)
        
        # First term: sign(x) * exp(|x|/ℓ) * (1 - exp(-x^2/ℓ^2))
        term1 = sign_x * np.exp(abs_x_scaled) * (1 - exp_factor)
        
        # Second term: sign(x) * ℓ * sign(x) * (1/ℓ) * exp(|x|/ℓ) * (1 - exp(-x^2/ℓ^2))
        term2 = np.exp(abs_x_scaled) * (1 - exp_factor)
        
        # Third term: sign(x) * ℓ * exp(|x|/ℓ) * 2x/ℓ^2 * exp(-x^2/ℓ^2)
        term3 = sign_x * self.scale * np.exp(abs_x_scaled) * (2 * x / self.scale**2) * exp_factor
        
        dclassical = term1 + term2 + term3
        
        return dquantum + dclassical
    
    def inverse(self, y: ArrayLike) -> ArrayLike:
        """Numerical inverse using root finding."""
        from scipy.optimize import brentq
        # OptimizeError doesn't exist in newer scipy versions, use ValueError instead
        OptimizeError = ValueError
        
        y = np.asarray(y, dtype=float)
        result = np.zeros_like(y)
        
        for i, yi in enumerate(np.atleast_1d(y)):
            if abs(yi) < 1e-10:
                result.flat[i] = 0
            else:
                # Define function to find root of
                def f(x):
                    return self(x) - yi
                
                # Search bounds
                x_max = 10 * self.scale
                
                try:
                    if yi > 0:
                        result.flat[i] = brentq(f, 0, x_max, xtol=1e-12)
                    else:
                        result.flat[i] = brentq(f, -x_max, 0, xtol=1e-12)
                except (OptimizeError, ValueError):
                    # Fallback to approximate inverse
                    if abs(yi) < self.scale:
                        # Quantum regime: alpha ~= x
                        result.flat[i] = yi
                    else:
                        # Classical regime: alpha ~= ℓ*exp(|x|/ℓ)
                        result.flat[i] = np.sign(yi) * self.scale * np.log(abs(yi) / self.scale)
        
        return result.reshape(y.shape)
    
    def __repr__(self):
        return f"ScaleDependent(scale={self.scale})"


class Custom(AlphaGenerator, BetaGenerator):
    """Custom generator from user-supplied functions.
    
    Allows users to define their own generator functions with
    custom transformation, derivative, and inverse functions.
    """
    
    def __init__(self, 
                 func: Callable[[ArrayLike], ArrayLike], 
                 deriv: Callable[[ArrayLike], ArrayLike], 
                 inv: Optional[Callable[[ArrayLike], ArrayLike]] = None,
                 name: str = "custom"):
        self.func = func
        self.deriv = deriv
        self.inv = inv if inv is not None else lambda y: y
        self.name = name
    
    def __call__(self, x: ArrayLike) -> ArrayLike:
        return self.func(x)
    
    def derivative(self, x: ArrayLike) -> ArrayLike:
        return self.deriv(x)
    
    def inverse(self, y: ArrayLike) -> ArrayLike:
        return self.inv(y)
    
    def __repr__(self):
        return f"Custom({self.name})"


# Utility functions for generator selection

def select_generator_pair(data_x: ArrayLike, data_y: ArrayLike, 
                         candidates: list = None) -> tuple:
    """Automatically select the best (alpha, beta) generator pair for given data.
    
    Uses the straight-line test to find generators that make the relationship
    between x and y as linear as possible in transformed coordinates.
    
    Args:
        data_x: Independent variable data
        data_y: Dependent variable data  
        candidates: List of generator classes to test
        
    Returns:
        (best_alpha, best_beta, r_squared): Best generator pair and fit quality
    """
    if candidates is None:
        candidates = [Identity, Exponential, Log, Power(2), Power(0.5), Reciprocal]
    
    best_r2 = -np.inf
    best_pair = (Identity(), Identity())
    
    for alpha_class in candidates:
        for beta_class in candidates:
            try:
                alpha = alpha_class() if not hasattr(alpha_class, 'p') else alpha_class
                beta = beta_class() if not hasattr(beta_class, 'p') else beta_class
                
                # Transform data
                x_trans = alpha(data_x)
                y_trans = beta(data_y)
                
                # Fit line and compute R^2
                if len(x_trans) > 2:
                    coeffs = np.polyfit(x_trans, y_trans, 1)
                    y_pred = coeffs[0] * x_trans + coeffs[1]
                    ss_res = np.sum((y_trans - y_pred) ** 2)
                    ss_tot = np.sum((y_trans - np.mean(y_trans)) ** 2)
                    r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
                    
                    if r2 > best_r2:
                        best_r2 = r2
                        best_pair = (alpha, beta)
                        
            except (ValueError, RuntimeWarning, OverflowError):
                continue
    
    return best_pair[0], best_pair[1], best_r2


def test_generator_properties(generator: Generator, 
                            test_points: ArrayLike = None) -> dict:
    """Test mathematical properties of a generator function.
    
    Args:
        generator: Generator to test
        test_points: Points to test (default: logarithmic spacing)
        
    Returns:
        Dictionary with test results
    """
    if test_points is None:
        test_points = np.logspace(-3, 3, 100)
    
    results = {
        'monotonicity': True,
        'continuity': True,
        'inverse_accuracy': 0.0,
        'derivative_accuracy': 0.0,
        'numerical_stability': True
    }
    
    try:
        # Test function evaluation
        y = generator(test_points)
        
        # Test monotonicity (for positive test points)
        pos_points = test_points[test_points > 0]
        if len(pos_points) > 1:
            y_pos = generator(pos_points)
            results['monotonicity'] = np.all(np.diff(y_pos) >= 0) or np.all(np.diff(y_pos) <= 0)
        
        # Test continuity (no large jumps)
        if len(y) > 1:
            relative_jumps = np.abs(np.diff(y)) / (np.abs(y[:-1]) + 1e-10)
            results['continuity'] = np.all(relative_jumps < 10)
        
        # Test inverse accuracy
        try:
            x_recovered = generator.inverse(y)
            inverse_error = np.mean(np.abs(x_recovered - test_points) / (np.abs(test_points) + 1e-10))
            results['inverse_accuracy'] = inverse_error
        except:
            results['inverse_accuracy'] = np.inf
        
        # Test derivative accuracy (numerical vs analytical)
        try:
            h = 1e-8
            numerical_deriv = (generator(test_points + h) - generator(test_points - h)) / (2 * h)
            analytical_deriv = generator.derivative(test_points)
            deriv_error = np.mean(np.abs(numerical_deriv - analytical_deriv) / 
                                (np.abs(analytical_deriv) + 1e-10))
            results['derivative_accuracy'] = deriv_error
        except:
            results['derivative_accuracy'] = np.inf
        
        # Test numerical stability
        extreme_points = np.array([-1e10, -1e-10, 0, 1e-10, 1e10])
        try:
            y_extreme = generator(extreme_points)
            results['numerical_stability'] = np.all(np.isfinite(y_extreme))
        except:
            results['numerical_stability'] = False
            
    except Exception as e:
        results['error'] = str(e)
    
    return results