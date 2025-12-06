"""
Meta-Calculus Experiments Module

This module contains experimental validations of the meta-calculus framework,
including scheme-robustness tests and multi-geometry analyses.

Key Experiments:
    - Experiment Q-A: A-scheme invariance of meta-time evolution
    - Experiment Q-B: Multi-geometry diffusion on quantum states
"""

from .quantum_scheme_experiments import (
    ExperimentQA,
    ExperimentQB,
    ComplexQHO,
    RealNQTQHO,
    demo_experiment_qa,
    demo_experiment_qb,
    run_all_experiments
)

__all__ = [
    'ExperimentQA',
    'ExperimentQB',
    'ComplexQHO',
    'RealNQTQHO',
    'demo_experiment_qa',
    'demo_experiment_qb',
    'run_all_experiments'
]
