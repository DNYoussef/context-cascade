"""
Weight functions for path-dependent and information-theoretic meta-calculus.

Weight functions u(x) and v(y) allow the mathematical "ruler" to vary
based on local properties like information content, reliability, or
physical constraints. This enables context-dependent mathematics where
the importance of different regions can be weighted appropriately.
"""

import numpy as np
from typing import Callable, Optional, Union
# Removed unused warnings import

ArrayLike = Union[float, np.ndarray]


def information_weight_qubit(r: ArrayLike) -> ArrayLike:
    """Information weight for a qubit based on its Bloch vector.
    
    For a qubit with Bloch vector r (|r| <= 1):
    - Pure state (|r| = 1): weight = 1 (maximum information)
    - Maximally mixed (r = 0): weight = exp(-ln 2) ~= 0.5 (minimum information)
    
    The weight is u(rho) = exp(-S_vN) where S_vN is the von Neumann entropy.
    
    Args:
        r: Bloch vector magnitude(s), must satisfy |r| <= 1
    
    Returns:
        Information weight u = exp(-S_vN)
    """
    r = np.atleast_1d(np.abs(r))
    r = np.clip(r, 0, 1)  # Ensure physical values
    
    # Von Neumann entropy for qubit: S = -Tr(rho log rho)
    # For rho = (1/2)(I + r*sigma), eigenvalues are (1+/-|r|)/2
    lambda_plus = (1 + r) / 2
    lambda_minus = (1 - r) / 2
    
    # Handle edge cases to avoid log(0)
    S_vN = np.zeros_like(r)
    mask = (r < 1 - 1e-15)  # Not pure state
    
    # Compute entropy only for mixed states
    S_vN[mask] = -(
        lambda_plus[mask] * np.log(lambda_plus[mask] + 1e-100) +
        lambda_minus[mask] * np.log(lambda_minus[mask] + 1e-100)
    )
    
    return np.exp(-S_vN)


def horizon_weight(r: ArrayLike, r_h: float, epsilon: float = 1e-6) -> ArrayLike:
    """Weight function near a black hole horizon.
    
    Suppresses contributions very close to the horizon to regularize
    divergences while preserving physics at finite distances. Uses a
    smooth tanh cutoff to avoid discontinuities.
    
    Args:
        r: Radial coordinate(s)
        r_h: Horizon radius (Schwarzschild radius = 2GM/c^2)
        epsilon: Regularization scale (should be << r_h)
    
    Returns:
        Weight v(r) that vanishes smoothly at r = r_h
    """
    r = np.atleast_1d(r)
    
    # Smooth cutoff using tanh: v(r) = tanh((r-r_h)/epsilon)
    # This gives v(r_h) ~= 0 and v(r >> r_h) ~= 1
    delta = (r - r_h) / epsilon
    weight = np.tanh(delta)
    
    # Ensure weight is zero inside horizon
    weight[r <= r_h] = 0
    
    # Ensure weight is positive outside horizon
    weight = np.maximum(weight, 0)
    
    return weight


def sensor_confidence_weight(sigma: ArrayLike, sigma_ref: float = 1.0) -> ArrayLike:
    """Weight based on measurement uncertainty.
    
    Used in sensor fusion to weight contributions by reliability.
    Sensors with smaller uncertainty get higher weight.
    
    Args:
        sigma: Measurement uncertainty/standard deviation
        sigma_ref: Reference uncertainty scale
    
    Returns:
        Weight u = (sigma_ref/sigma)^2 (inverse variance weighting)
    """
    sigma = np.atleast_1d(sigma)
    
    # Prevent division by zero
    sigma_safe = np.where(sigma <= 0, sigma_ref * 1e-6, sigma)
    
    return (sigma_ref / sigma_safe) ** 2


def decoherence_weight(lambda_k: ArrayLike, lambda_0: float) -> ArrayLike:
    """Weight for decoherence channels in quantum systems.
    
    Suppresses strongly-coupled environment modes to preserve coherence.
    Based on the exponential suppression of coupling to high-energy modes.
    
    Args:
        lambda_k: Coupling strengths to environment modes
        lambda_0: Characteristic energy/coupling scale
    
    Returns:
        Weight v_k = exp(-lambda__k/lambda__0)
    """
    lambda_k = np.atleast_1d(lambda_k)
    
    # Prevent overflow for very large coupling
    ratio = np.clip(lambda_k / lambda_0, 0, 700)
    
    return np.exp(-ratio)


def path_integral_weight(path_action: ArrayLike, 
                        action_scale: float = 1.0,
                        temperature: float = 1.0) -> ArrayLike:
    """Weight based on path integral action.
    
    Implements Boltzmann-like weighting: w = exp(-S[path]/T)
    where S[path] is the action along a path.
    
    Args:
        path_action: Action values along different paths
        action_scale: Characteristic action scale
        temperature: Temperature parameter controlling weight spread
    
    Returns:
        Path weights w = exp(-S/T)
    """
    path_action = np.atleast_1d(path_action)
    
    # Normalize by action scale and temperature
    normalized_action = path_action / (action_scale * temperature)
    
    # Prevent overflow
    normalized_action = np.clip(normalized_action, -700, 700)
    
    return np.exp(-normalized_action)


def information_entropy_weight(probabilities: ArrayLike) -> float:
    """Weight based on Shannon entropy of probability distribution.
    
    Higher entropy (more uncertainty) gives lower weight.
    
    Args:
        probabilities: Probability distribution (must sum to 1)
    
    Returns:
        Weight w = exp(-H) where H is Shannon entropy
    """
    p = np.atleast_1d(probabilities)
    
    # Normalize to ensure sum = 1
    p = p / np.sum(p)
    
    # Remove zero probabilities to avoid log(0)
    p_nonzero = p[p > 1e-100]
    
    # Shannon entropy: H = -Sigma p_i log(p_i)
    H = -np.sum(p_nonzero * np.log(p_nonzero))
    
    return np.exp(-H)


def correlation_weight(x: ArrayLike, y: ArrayLike, 
                      correlation_scale: float = 1.0) -> ArrayLike:
    """Weight based on correlation between variables.
    
    Higher correlation gives higher weight, useful for
    identifying strongly related variables.
    
    Args:
        x, y: Variables to compute correlation
        correlation_scale: Scale factor for weight
    
    Returns:
        Weight based on correlation coefficient
    """
    x = np.atleast_1d(x)
    y = np.atleast_1d(y)
    
    if len(x) != len(y):
        raise ValueError("x and y must have same length")
    
    if len(x) < 2:
        return np.array([1.0])
    
    # Compute correlation coefficient
    corr_coeff = np.corrcoef(x, y)[0, 1]
    
    # Handle NaN correlation (constant variables)
    if np.isnan(corr_coeff):
        corr_coeff = 0.0
    
    # Weight based on absolute correlation
    weight = np.abs(corr_coeff) * correlation_scale
    
    return np.full_like(x, weight)


class Weight:
    """Base class for general weight functions.
    
    Encapsulates both u(x) and v(y) weight functions and provides
    a unified interface for weight evaluation and combination.
    """
    
    def __init__(self, 
                 u_func: Optional[Callable[[ArrayLike], ArrayLike]] = None, 
                 v_func: Optional[Callable[[ArrayLike], ArrayLike]] = None,
                 name: str = "custom"):
        """Initialize weight functions.
        
        Args:
            u_func: Weight function u(x) for independent variable
            v_func: Weight function v(y) for dependent variable
            name: Descriptive name for the weight
        """
        self.u = u_func if u_func is not None else lambda x: np.ones_like(np.asarray(x))
        self.v = v_func if v_func is not None else lambda y: np.ones_like(np.asarray(y))
        self.name = name
    
    def __call__(self, x: ArrayLike = None, y: ArrayLike = None) -> tuple:
        """Evaluate weight functions.
        
        Args:
            x: Independent variable values
            y: Dependent variable values
        
        Returns:
            (u(x), v(y)) tuple of weight values
        """
        u_val = self.u(x) if x is not None else 1.0
        v_val = self.v(y) if y is not None else 1.0
        return u_val, v_val
    
    def combine(self, other: 'Weight', method: str = 'multiply') -> 'Weight':
        """Combine with another weight function.
        
        Args:
            other: Another Weight object
            method: Combination method ('multiply', 'add', 'max', 'min')
        
        Returns:
            New Weight object with combined functions
        """
        if method == 'multiply':
            u_combined = lambda x: self.u(x) * other.u(x)
            v_combined = lambda y: self.v(y) * other.v(y)
        elif method == 'add':
            u_combined = lambda x: self.u(x) + other.u(x)
            v_combined = lambda y: self.v(y) + other.v(y)
        elif method == 'max':
            u_combined = lambda x: np.maximum(self.u(x), other.u(x))
            v_combined = lambda y: np.maximum(self.v(y), other.v(y))
        elif method == 'min':
            u_combined = lambda x: np.minimum(self.u(x), other.u(x))
            v_combined = lambda y: np.minimum(self.v(y), other.v(y))
        else:
            raise ValueError(f"Unknown combination method: {method}")
        
        return Weight(u_combined, v_combined, f"{self.name}_{method}_{other.name}")
    
    def normalize(self, x_domain: ArrayLike = None, y_domain: ArrayLike = None) -> 'Weight':
        """Create normalized version of weight functions.
        
        Args:
            x_domain: Domain for normalizing u(x)
            y_domain: Domain for normalizing v(y)
        
        Returns:
            New Weight object with normalized functions
        """
        if x_domain is not None:
            u_vals = self.u(x_domain)
            u_max = np.max(u_vals) if np.max(u_vals) > 0 else 1.0
            u_normalized = lambda x: self.u(x) / u_max
        else:
            u_normalized = self.u
        
        if y_domain is not None:
            v_vals = self.v(y_domain)
            v_max = np.max(v_vals) if np.max(v_vals) > 0 else 1.0
            v_normalized = lambda y: self.v(y) / v_max
        else:
            v_normalized = self.v
        
        return Weight(u_normalized, v_normalized, f"{self.name}_normalized")
    
    def __repr__(self):
        return f"Weight({self.name})"


class InformationWeight(Weight):
    """Weight based on information-theoretic measures.
    
    Uses entropy and mutual information to weight contributions
    based on their information content.
    """
    
    def __init__(self, 
                 entropy_func: Callable[[ArrayLike], ArrayLike],
                 mutual_info_func: Optional[Callable[[ArrayLike], ArrayLike]] = None,
                 temperature: float = 1.0):
        """Initialize information-based weights.
        
        Args:
            entropy_func: Function computing entropy S(x)
            mutual_info_func: Function computing mutual information I(x;y)
            temperature: Temperature parameter for Boltzmann weighting
        """
        u_func = lambda x: np.exp(-entropy_func(x) / temperature)
        
        if mutual_info_func is not None:
            v_func = lambda y: np.exp(mutual_info_func(y) / temperature)
        else:
            v_func = None
        
        super().__init__(u_func, v_func, "information")
        self.entropy_func = entropy_func
        self.mutual_info_func = mutual_info_func
        self.temperature = temperature


class PathDependentWeight(Weight):
    """Weight that depends on the path taken through configuration space.
    
    Useful for systems where the history or path matters, such as
    hysteretic systems or path integrals in quantum mechanics.
    """
    
    def __init__(self, 
                 path_integral_func: Callable[[ArrayLike], ArrayLike],
                 action_scale: float = 1.0,
                 temperature: float = 1.0):
        """Initialize path-dependent weight.
        
        Args:
            path_integral_func: Function computing path-dependent quantity
                               (e.g., Wilson loop, holonomy, action)
            action_scale: Characteristic scale for the path integral
            temperature: Temperature for Boltzmann weighting
        """
        u_func = lambda x: path_integral_weight(
            path_integral_func(x), action_scale, temperature
        )
        
        super().__init__(u_func=u_func, name="path_dependent")
        self.path_integral_func = path_integral_func
        self.action_scale = action_scale
        self.temperature = temperature


class AdaptiveWeight(Weight):
    """Weight that adapts based on local properties of the data.
    
    Automatically adjusts weighting based on local density,
    gradient magnitude, or other adaptive criteria.
    """
    
    def __init__(self, 
                 adaptation_func: Callable[[ArrayLike], ArrayLike],
                 adaptation_scale: float = 1.0,
                 smoothing_length: float = 0.1):
        """Initialize adaptive weight.
        
        Args:
            adaptation_func: Function that computes adaptation criterion
            adaptation_scale: Scale for the adaptation
            smoothing_length: Length scale for smoothing the adaptation
        """
        def adaptive_u(x):
            x = np.atleast_1d(x)
            adaptation = adaptation_func(x)
            
            # Smooth the adaptation using a Gaussian kernel
            if len(x) > 1 and smoothing_length > 0:
                from scipy.ndimage import gaussian_filter1d
                try:
                    # Sort for smoothing
                    sort_idx = np.argsort(x)
                    adaptation_sorted = adaptation[sort_idx]
                    
                    # Apply Gaussian smoothing
                    sigma = smoothing_length * len(x) / (np.max(x) - np.min(x) + 1e-10)
                    adaptation_smooth = gaussian_filter1d(adaptation_sorted, sigma)
                    
                    # Unsort
                    adaptation[sort_idx] = adaptation_smooth
                except ImportError:
                    # Fallback: simple moving average
                    window = max(1, int(smoothing_length * len(x)))
                    adaptation = np.convolve(adaptation, 
                                           np.ones(window)/window, mode='same')
            
            return adaptation / adaptation_scale
        
        super().__init__(u_func=adaptive_u, name="adaptive")
        self.adaptation_func = adaptation_func
        self.adaptation_scale = adaptation_scale
        self.smoothing_length = smoothing_length


def create_physics_weight(physics_type: str, **kwargs) -> Weight:
    """Factory function for creating physics-specific weights.
    
    Args:
        physics_type: Type of physics ('quantum', 'gravity', 'statistical', 'field')
        **kwargs: Parameters specific to the physics type
    
    Returns:
        Appropriate Weight object for the physics application
    """
    if physics_type == 'quantum':
        # Quantum information weight
        def quantum_entropy(x):
            # Assume x represents some quantum parameter
            # This is a placeholder - real implementation would depend on specific system
            return -np.sum(x * np.log(np.abs(x) + 1e-100), axis=-1)
        
        return InformationWeight(quantum_entropy, **kwargs)
    
    elif physics_type == 'gravity':
        # Gravitational weight near horizons
        r_h = kwargs.get('horizon_radius', 1.0)
        epsilon = kwargs.get('regularization', 1e-6)
        
        u_func = lambda r: horizon_weight(r, r_h, epsilon)
        return Weight(u_func=u_func, name="gravitational")
    
    elif physics_type == 'statistical':
        # Statistical mechanics weight
        temperature = kwargs.get('temperature', 1.0)
        
        def boltzmann_weight(energy):
            return np.exp(-energy / temperature)
        
        return Weight(v_func=boltzmann_weight, name="statistical")
    
    elif physics_type == 'field':
        # Quantum field theory weight
        cutoff = kwargs.get('cutoff_scale', 1.0)
        
        def field_weight(momentum):
            return decoherence_weight(momentum, cutoff)
        
        return Weight(u_func=field_weight, name="field_theory")
    
    else:
        raise ValueError(f"Unknown physics type: {physics_type}")


def test_weight_properties(weight: Weight, 
                          x_test: ArrayLike = None,
                          y_test: ArrayLike = None) -> dict:
    """Test mathematical properties of weight functions.
    
    Args:
        weight: Weight object to test
        x_test: Test points for u(x) (default: linspace)
        y_test: Test points for v(y) (default: linspace)
    
    Returns:
        Dictionary with test results
    """
    if x_test is None:
        x_test = np.linspace(-2, 2, 100)
    if y_test is None:
        y_test = np.linspace(-2, 2, 100)
    
    results = {
        'u_properties': {},
        'v_properties': {},
        'combined_properties': {}
    }
    
    try:
        # Test u(x) properties
        u_vals = weight.u(x_test)
        results['u_properties'] = {
            'min_value': np.min(u_vals),
            'max_value': np.max(u_vals),
            'mean_value': np.mean(u_vals),
            'is_positive': np.all(u_vals >= 0),
            'is_finite': np.all(np.isfinite(u_vals)),
            'monotonicity': _check_monotonicity(u_vals),
            'smoothness': _check_smoothness(u_vals)
        }
        
        # Test v(y) properties
        v_vals = weight.v(y_test)
        results['v_properties'] = {
            'min_value': np.min(v_vals),
            'max_value': np.max(v_vals),
            'mean_value': np.mean(v_vals),
            'is_positive': np.all(v_vals >= 0),
            'is_finite': np.all(np.isfinite(v_vals)),
            'monotonicity': _check_monotonicity(v_vals),
            'smoothness': _check_smoothness(v_vals)
        }
        
        # Combined properties
        u_x, v_y = weight(x_test, y_test)
        results['combined_properties'] = {
            'weight_product_finite': np.all(np.isfinite(u_x * v_y)),
            'weight_ratio_finite': np.all(np.isfinite(v_y / (u_x + 1e-100))),
            'effective_range': np.sum((u_x * v_y) > 0.01 * np.max(u_x * v_y)) / len(u_x)
        }
        
    except Exception as e:
        results['error'] = str(e)
    
    return results


def _check_monotonicity(values: ArrayLike) -> str:
    """Check if values are monotonic."""
    diff = np.diff(values)
    if np.all(diff >= 0):
        return 'increasing'
    elif np.all(diff <= 0):
        return 'decreasing'
    else:
        return 'non_monotonic'


def _check_smoothness(values: ArrayLike) -> float:
    """Check smoothness by computing second derivative magnitude."""
    if len(values) < 3:
        return 0.0
    
    second_diff = np.diff(values, 2)
    return np.mean(np.abs(second_diff))