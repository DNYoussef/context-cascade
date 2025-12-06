"""
Meta-Calculus Experiments

Numerical experiments for testing meta-calculus hypotheses.

Available experiments:
    - multi_calculus_diffusion: Diffusion on simplex with multiple calculi
"""

from .multi_calculus_diffusion import (
    CalculusEmbedding,
    ExperimentConfig,
    ExperimentResults,
    run_example_experiment,
    run_full_analysis,
    sample_simplex_points,
)

__all__ = [
    "CalculusEmbedding",
    "ExperimentConfig",
    "ExperimentResults",
    "run_example_experiment",
    "run_full_analysis",
    "sample_simplex_points",
]
