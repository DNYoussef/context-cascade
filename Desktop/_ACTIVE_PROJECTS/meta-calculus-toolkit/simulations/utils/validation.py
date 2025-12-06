"""
Statistical validation utilities for NNC simulations.
"""
import numpy as np


def check_constant_derivative(D_values, expected_value, rtol=0.01):
    """
    Check if bigeometric derivative is constant.

    Args:
        D_values: Array of derivative values
        expected_value: Expected constant value (e^n)
        rtol: Relative tolerance (default 1%)

    Returns:
        (is_constant, stats_dict)
    """
    D_values = np.asarray(D_values)

    mean_D = np.mean(D_values)
    std_D = np.std(D_values)
    rel_variation = std_D / mean_D if mean_D != 0 else np.inf

    # Check 1: Small variation
    is_constant_variation = rel_variation < rtol

    # Check 2: Close to expected value
    rel_error = np.abs(mean_D - expected_value) / expected_value
    is_correct_value = rel_error < rtol

    stats = {
        'mean': mean_D,
        'std': std_D,
        'rel_variation': rel_variation,
        'expected': expected_value,
        'rel_error': rel_error,
        'passes_variation': is_constant_variation,
        'passes_value': is_correct_value,
        'overall_pass': is_constant_variation and is_correct_value
    }

    return stats['overall_pass'], stats


def check_conservation(values, rtol=1e-6):
    """
    Check if conserved quantity remains constant.

    Args:
        values: Time series of conserved quantity
        rtol: Relative tolerance

    Returns:
        (is_conserved, stats_dict)
    """
    values = np.asarray(values)

    initial = values[0]
    final = values[-1]
    max_deviation = np.max(np.abs(values - initial))
    rel_error = max_deviation / np.abs(initial) if initial != 0 else np.inf

    is_conserved = rel_error < rtol

    stats = {
        'initial': initial,
        'final': final,
        'max_deviation': max_deviation,
        'rel_error': rel_error,
        'conservation_quality': (
            'excellent' if rel_error < 1e-10 else
            'good' if rel_error < 1e-6 else
            'poor'
        ),
        'passes': is_conserved
    }

    return is_conserved, stats


def check_no_divergence(values, threshold=1e10):
    """
    Check that values remain finite (no divergence).

    Args:
        values: Array of numerical values
        threshold: Maximum allowed value

    Returns:
        (is_finite, stats_dict)
    """
    values = np.asarray(values)

    has_nan = np.any(np.isnan(values))
    has_inf = np.any(np.isinf(values))
    max_value = np.max(np.abs(values[np.isfinite(values)])) if np.any(np.isfinite(values)) else np.inf
    exceeds_threshold = max_value > threshold

    is_finite = not (has_nan or has_inf or exceeds_threshold)

    stats = {
        'has_nan': has_nan,
        'has_inf': has_inf,
        'max_value': max_value,
        'threshold': threshold,
        'exceeds_threshold': exceeds_threshold,
        'passes': is_finite
    }

    return is_finite, stats


def compare_classical_vs_nnc(classical_values, nnc_values):
    """
    Compare classical (divergent) vs NNC (regularized) results.

    Args:
        classical_values: Classical calculation results
        nnc_values: NNC calculation results

    Returns:
        comparison_dict
    """
    classical_values = np.asarray(classical_values)
    nnc_values = np.asarray(nnc_values)

    # Classical divergence
    classical_diverges = np.any(np.isinf(classical_values)) or np.max(np.abs(classical_values[np.isfinite(classical_values)])) > 1e10

    # NNC regularization
    nnc_finite = np.all(np.isfinite(nnc_values))
    nnc_max = np.max(np.abs(nnc_values))
    classical_max = np.max(np.abs(classical_values[np.isfinite(classical_values)])) if np.any(np.isfinite(classical_values)) else np.inf

    comparison = {
        'classical_diverges': classical_diverges,
        'nnc_finite': nnc_finite,
        'classical_max': classical_max,
        'nnc_max': nnc_max,
        'regularization_achieved': classical_diverges and nnc_finite,
        'suppression_factor': classical_max / nnc_max if nnc_max != 0 and np.isfinite(classical_max) else np.inf
    }

    return comparison


def generate_validation_report(validation_results, simulation_name):
    """
    Generate formatted validation report.

    Args:
        validation_results: Dictionary of validation results
        simulation_name: Name of simulation

    Returns:
        Formatted report string
    """
    report = []
    report.append(f"\nValidation Report: {simulation_name}")
    report.append("=" * 60)

    for criterion, result in validation_results.items():
        if isinstance(result, dict) and 'passes' in result:
            status = "PASS" if result['passes'] else "FAIL"
            report.append(f"  [{status}] {criterion}")
            for key, value in result.items():
                if key != 'passes':
                    if isinstance(value, float):
                        report.append(f"      {key}: {value:.6e}")
                    else:
                        report.append(f"      {key}: {value}")
        elif isinstance(result, bool):
            status = "PASS" if result else "FAIL"
            report.append(f"  [{status}] {criterion}")

    all_pass = all(
        v['passes'] if isinstance(v, dict) and 'passes' in v else v
        for v in validation_results.values()
    )
    report.append("-" * 60)
    report.append(f"Overall: {'SUCCESS' if all_pass else 'PARTIAL SUCCESS'}")

    return "\n".join(report)
