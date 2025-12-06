"""
meta_calculus/quantum

Quantum-flavored extensions for meta-calculus:
  - Meta-quantum compatibility testing (meta-time Schrödinger)
  - Multi-calculus state-space diffusion
  - GlobalMOO / pymoo objective wrappers
"""

from .meta_quantum_compatibility import (
    MetaDerivativeConfig,
    QuantumCompatibilityResult,
    DEFAULT_CONFIGS,
    run_meta_quantum_experiment,
    run_detailed_experiment,
    print_compatibility_summary,
    random_hermitian,
    random_state,
    make_meta_rhs,
    make_default_u,
)

from .multi_calculus_state_diffusion import (
    QuantumDiffusionConfig,
    QuantumDiffusionResults,
    run_quantum_flavored_diffusion,
    print_quantum_diffusion_summary,
)

from .quantum_objectives import (
    meta_quantum_globalmoo_objective,
    quantum_diffusion_globalmoo_objective,
    MetaQuantumPymooProblem,
    QuantumDiffusionPymooProblem,
)

__all__ = [
    # Meta-quantum compatibility
    "MetaDerivativeConfig",
    "QuantumCompatibilityResult",
    "DEFAULT_CONFIGS",
    "run_meta_quantum_experiment",
    "run_detailed_experiment",
    "print_compatibility_summary",
    "random_hermitian",
    "random_state",
    "make_meta_rhs",
    "make_default_u",
    # Quantum diffusion
    "QuantumDiffusionConfig",
    "QuantumDiffusionResults",
    "run_quantum_flavored_diffusion",
    "print_quantum_diffusion_summary",
    # Objectives
    "meta_quantum_globalmoo_objective",
    "quantum_diffusion_globalmoo_objective",
    "MetaQuantumPymooProblem",
    "QuantumDiffusionPymooProblem",
]
