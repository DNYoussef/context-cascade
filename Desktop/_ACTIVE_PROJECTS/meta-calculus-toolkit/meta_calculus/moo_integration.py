#!/usr/bin/env python3
"""
Multi-Objective Optimization Integration for Meta-Calculus

This module provides the interface between the meta-calculus toolkit and
multi-objective optimization engines (Global MOO, pymoo, etc.).

DESIGN PRINCIPLES (from critical analysis):
    1. Optimize FOR cross-calculus consistency, not OVER calculus types
    2. Physical structure = what survives all calculi (scheme-robust)
    3. Pareto frontier is for exploration, not validation
    4. Fragile solutions should be discarded
    5. Always maintain physical interpretability

KEY INSIGHT:
    We use MOO to find parameters (n, s, k, w) where ALL calculi agree
    that physical structure is clear, NOT to find "the best calculus."

Usage:
    # Standalone evaluation
    python -m meta_calculus.moo_integration evaluate --n 0.67 --s 0.01 --k 0.02 --w 0.0

    # Demo with pymoo (if installed)
    python -m meta_calculus.moo_integration pymoo

    # Run Global MOO optimization (requires API key)
    python -m meta_calculus.moo_integration globalmoo

    # Export for Global MOO API
    python -m meta_calculus.moo_integration export-template

    # Run both optimizers and compare
    python -m meta_calculus.moo_integration compare
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Any, Callable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import argparse
import sys
import json
import warnings
import os
import time

# Global MOO API Configuration
# SDK: pip install globalmoo-sdk
# Docs: https://globalmoo.gitbook.io/globalmoo-documentation
GLOBALMOO_API_KEY = os.environ.get(
    'GLOBALMOO_API_KEY',
    'gq8bbjzNZzJPsDaEzB4YWqzJKvSst2H7rL9R6JHfsUYm9Arc'
)
GLOBALMOO_API_URL = os.environ.get(
    'GLOBALMOO_API_URL',
    'https://app.globalmoo.com/api/'  # Official endpoint from SDK docs
)


# =============================================================================
# OBJECTIVE DEFINITIONS
# =============================================================================

@dataclass
class ObjectiveSpec:
    """Specification for a single objective."""
    name: str
    direction: str  # 'minimize' or 'maximize'
    description: str
    target: Optional[float] = None  # For match-target objectives
    weight: float = 1.0  # Relative importance
    bounds: Tuple[float, float] = (-np.inf, np.inf)


@dataclass
class ConstraintSpec:
    """Specification for a constraint."""
    name: str
    type: str  # 'equality', 'inequality_le', 'inequality_ge'
    description: str
    bound: float = 0.0


# Standard objectives for scheme-robust optimization
STANDARD_OBJECTIVES = [
    ObjectiveSpec(
        name='chi2_total',
        direction='minimize',
        description='Total chi-squared for observational fit (BBN + CMB)',
        bounds=(0, 1000)
    ),
    ObjectiveSpec(
        name='neg_spectral_gap_mixed',
        direction='minimize',  # Minimizing negative = maximizing gap
        description='Negative spectral gap of mixed diffusion operator',
        bounds=(-1, 0)
    ),
    ObjectiveSpec(
        name='neg_invariance_score',
        direction='minimize',  # Minimizing negative = maximizing invariance
        description='Negative cross-calculus invariance score',
        bounds=(-1, 0)
    ),
    ObjectiveSpec(
        name='neg_min_individual_gap',
        direction='minimize',  # Maximize the worst individual gap
        description='Negative of minimum spectral gap across individual calculi',
        bounds=(-1, 0)
    ),
    ObjectiveSpec(
        name='fragility',
        direction='minimize',
        description='Sensitivity of objectives to parameter perturbations',
        bounds=(0, 100)
    ),
]

# Standard constraints (polytope bounds)
STANDARD_CONSTRAINTS = [
    ConstraintSpec('s_upper', 'inequality_le', '|s| <= 0.05 (BBN)', 0.05),
    ConstraintSpec('s_lower', 'inequality_ge', 's >= -0.05 (BBN)', -0.05),
    ConstraintSpec('k_upper', 'inequality_le', '|k| <= 0.03 (CMB)', 0.03),
    ConstraintSpec('k_lower', 'inequality_ge', 'k >= -0.03 (CMB)', -0.03),
    ConstraintSpec('w_upper', 'inequality_le', 'w <= 1.0 (energy)', 1.0),
    ConstraintSpec('w_lower', 'inequality_ge', 'w >= -1.0 (energy)', -1.0),
    ConstraintSpec('n_lower', 'inequality_ge', 'n >= 0 (expansion)', 0.0),
]


# =============================================================================
# PHYSICS ORACLE (Black-box evaluator)
# =============================================================================

class PhysicsOracle:
    """
    Black-box evaluator for meta-calculus physics objectives.

    This class wraps the meta-calculus simulator and multi-calculus analysis
    to provide objective values for a given parameter set.

    CRITICAL: All objectives are formulated for MINIMIZATION.
    To maximize something (e.g., spectral gap), we return its negative.
    """

    def __init__(self, n_solutions: int = 30, sigma: float = 0.5,
                 seed: Optional[int] = None):
        """
        Args:
            n_solutions: Number of FRW solutions per evaluation
            sigma: Bandwidth for diffusion kernels
            seed: Random seed for reproducibility
        """
        self.n_solutions = n_solutions
        self.sigma = sigma
        self.seed = seed

        # Lazy imports to avoid circular dependencies
        self._ensemble = None
        self._bbn = None

    def _get_ensemble(self):
        """Lazy load calculus ensemble."""
        if self._ensemble is None:
            from .scheme_robust_observables import create_standard_ensemble
            self._ensemble = create_standard_ensemble(sigma=self.sigma)
        return self._ensemble

    def _get_bbn_constraints(self):
        """Lazy load BBN constraint calculator."""
        if self._bbn is None:
            try:
                from .bbn_cmb_constraints import BBNConstraints, CMBConstraints
                self._bbn = {'bbn': BBNConstraints(), 'cmb': CMBConstraints()}
            except ImportError:
                self._bbn = {'bbn': None, 'cmb': None}
        return self._bbn

    def check_constraints(self, n: float, s: float, k: float, w: float) -> Dict:
        """
        Check if parameters satisfy hard constraints.

        Returns:
            Dict with 'feasible' bool and 'violations' list
        """
        violations = []

        if abs(s) > 0.05:
            violations.append(f's={s:.4f} violates |s| <= 0.05')
        if abs(k) > 0.03:
            violations.append(f'k={k:.4f} violates |k| <= 0.03')
        if w < -1.0 or w > 1.0:
            violations.append(f'w={w:.4f} violates -1 <= w <= 1')
        if n < 0:
            violations.append(f'n={n:.4f} violates n >= 0')

        # Check discriminant for real solutions
        discriminant = 9*s**2*w**2 - 8*s**2 + 4*s + 4
        if discriminant < 0:
            violations.append(f'discriminant={discriminant:.4f} < 0')

        return {
            'feasible': len(violations) == 0,
            'violations': violations
        }

    def generate_solution_cloud(self, n: float, s: float, k: float,
                                 w: float) -> np.ndarray:
        """
        Generate a cloud of FRW solutions near the given parameters.

        Returns:
            Array of shape (n_solutions, n_features) with features:
            [a_representative, H_representative, R_representative]
        """
        if self.seed is not None:
            np.random.seed(self.seed)

        # Generate solutions with small perturbations
        n_vals = n + 0.05 * (2*np.random.rand(self.n_solutions) - 1)
        n_vals = np.clip(n_vals, 0.1, 2.0)

        # Compute representative features for each n
        # For a(t) = t^n at representative time t=1:
        # a = 1, H = n, R ~ n(n-1) (simplified Ricci scalar)
        a_vals = np.ones(self.n_solutions)  # a(1) = 1
        H_vals = n_vals  # H = n at t=1
        R_vals = n_vals * (n_vals - 1)  # Simplified curvature proxy

        return np.column_stack([a_vals, H_vals, R_vals])

    def compute_chi2(self, k: float) -> Tuple[float, float]:
        """
        Compute observational chi-squared values.

        Returns:
            (chi2_bbn, chi2_cmb)
        """
        constraints = self._get_bbn_constraints()

        chi2_bbn = 0.0
        chi2_cmb = 0.0

        if constraints['bbn'] is not None:
            try:
                chi2_bbn = constraints['bbn'].total_chi_squared(k)
            except Exception:
                chi2_bbn = 100.0 * abs(k)  # Fallback penalty

        if constraints['cmb'] is not None:
            try:
                chi2_cmb = constraints['cmb'].total_chi_squared(k)
            except Exception:
                chi2_cmb = 100.0 * abs(k)  # Fallback penalty

        # Simple proxy if modules not available
        if constraints['bbn'] is None and constraints['cmb'] is None:
            # Penalty increases with |k|
            chi2_bbn = 10.0 * k**2 / 0.03**2
            chi2_cmb = 10.0 * k**2 / 0.03**2

        return chi2_bbn, chi2_cmb

    def compute_spectral_analysis(self, X: np.ndarray) -> Dict:
        """
        Compute spectral gaps for all calculi and mixed operator.

        Returns:
            Dict with spectral gaps and invariance metrics
        """
        ensemble = self._get_ensemble()

        results = ensemble.spectral_analysis(X, k=5)

        # Extract spectral gaps
        gaps = {}
        for name, data in results.items():
            gaps[name] = data['spectral_gap']

        # Compute invariance score using cluster labels
        # For now, use first eigenmode as proxy for cluster structure
        if 'Mixed' in results:
            eigenvector = results['Mixed']['eigenvectors'][:, 0]
            invariance = ensemble.invariance_score(X, eigenvector)
        else:
            invariance = 0.5  # Default

        return {
            'gaps': gaps,
            'invariance_score': invariance,
            'gap_mixed': gaps.get('Mixed', 0.0),
            'gap_min_individual': min(
                g for name, g in gaps.items() if name != 'Mixed'
            ) if len(gaps) > 1 else 0.0
        }

    def compute_fragility(self, n: float, s: float, k: float, w: float,
                          base_objectives: Dict[str, float],
                          delta: float = 0.01) -> float:
        """
        Measure sensitivity of objectives to parameter perturbations.

        Fragile solutions change dramatically with small parameter changes.
        Robust solutions are stable.

        Returns:
            Fragility score (lower = more robust)
        """
        perturbations = [
            (n + delta, s, k, w),
            (n - delta, s, k, w),
            (n, s + delta, k, w),
            (n, s - delta, k, w),
            (n, s, k + delta, w),
            (n, s, k - delta, w),
            (n, s, k, w + delta),
            (n, s, k, w - delta),
        ]

        max_change = 0.0
        for p_n, p_s, p_k, p_w in perturbations:
            # Skip infeasible perturbations
            check = self.check_constraints(p_n, p_s, p_k, p_w)
            if not check['feasible']:
                continue

            try:
                perturbed = self._evaluate_core(p_n, p_s, p_k, p_w)
                for key in base_objectives:
                    if key in perturbed:
                        base_val = base_objectives[key]
                        pert_val = perturbed[key]
                        if abs(base_val) > 1e-10:
                            change = abs(pert_val - base_val) / abs(base_val)
                            max_change = max(max_change, change)
            except Exception:
                pass

        return max_change

    def _evaluate_core(self, n: float, s: float, k: float,
                        w: float) -> Dict[str, float]:
        """Core evaluation without fragility (to avoid recursion)."""
        # Generate solution cloud
        X = self.generate_solution_cloud(n, s, k, w)

        # Observational fit
        chi2_bbn, chi2_cmb = self.compute_chi2(k)
        chi2_total = chi2_bbn + chi2_cmb

        # Spectral analysis
        spectral = self.compute_spectral_analysis(X)

        return {
            'chi2_total': chi2_total,
            'chi2_bbn': chi2_bbn,
            'chi2_cmb': chi2_cmb,
            'neg_spectral_gap_mixed': -spectral['gap_mixed'],
            'neg_invariance_score': -spectral['invariance_score'],
            'neg_min_individual_gap': -spectral['gap_min_individual'],
        }

    def evaluate(self, n: float, s: float, k: float, w: float,
                 compute_fragility: bool = True) -> Dict[str, Any]:
        """
        Full evaluation of a parameter set.

        Args:
            n: Expansion exponent
            s: Action weight exponent
            k: Meta-weight exponent
            w: Equation of state

        Returns:
            Dict with all objective values and metadata
        """
        # Check constraints first
        constraint_check = self.check_constraints(n, s, k, w)

        if not constraint_check['feasible']:
            # Return penalty values for infeasible solutions
            return {
                'feasible': False,
                'violations': constraint_check['violations'],
                'objectives': {
                    'chi2_total': 1000.0,
                    'neg_spectral_gap_mixed': 0.0,
                    'neg_invariance_score': 0.0,
                    'neg_min_individual_gap': 0.0,
                    'fragility': 100.0,
                }
            }

        # Core evaluation
        core = self._evaluate_core(n, s, k, w)

        # Fragility (optional, expensive)
        if compute_fragility:
            fragility = self.compute_fragility(n, s, k, w, core)
        else:
            fragility = 0.0

        return {
            'feasible': True,
            'violations': [],
            'objectives': {
                'chi2_total': core['chi2_total'],
                'neg_spectral_gap_mixed': core['neg_spectral_gap_mixed'],
                'neg_invariance_score': core['neg_invariance_score'],
                'neg_min_individual_gap': core['neg_min_individual_gap'],
                'fragility': fragility,
            },
            'details': {
                'chi2_bbn': core['chi2_bbn'],
                'chi2_cmb': core['chi2_cmb'],
                'spectral_gap_mixed': -core['neg_spectral_gap_mixed'],
                'invariance_score': -core['neg_invariance_score'],
            }
        }


# =============================================================================
# GLOBAL MOO ADAPTER
# =============================================================================

class GlobalMOOAdapter:
    """
    Adapter for Global MOO API integration.

    This class formats our physics oracle for the Global MOO API.
    It handles the translation between our internal representations
    and the JSON-based API format.
    """

    def __init__(self, oracle: Optional[PhysicsOracle] = None):
        self.oracle = oracle or PhysicsOracle()

        # Parameter bounds (tight for 90%+ feasibility)
        self.input_specs = [
            {'name': 'n', 'min': 0.3, 'max': 1.5, 'type': 'float'},
            {'name': 's', 'min': -0.05, 'max': 0.05, 'type': 'float'},
            {'name': 'k', 'min': -0.03, 'max': 0.03, 'type': 'float'},
            {'name': 'w', 'min': -0.5, 'max': 0.5, 'type': 'float'},
        ]

        # Output specifications
        self.output_specs = [
            {'name': 'chi2_total', 'target': 0.0, 'type': 'minimize'},
            {'name': 'neg_spectral_gap_mixed', 'target': -1.0, 'type': 'minimize'},
            {'name': 'neg_invariance_score', 'target': -1.0, 'type': 'minimize'},
            {'name': 'neg_min_individual_gap', 'target': -1.0, 'type': 'minimize'},
            {'name': 'fragility', 'target': 0.0, 'type': 'minimize'},
        ]

    def input_to_params(self, inputs: List[float]) -> Dict[str, float]:
        """Convert input array to parameter dict."""
        return {
            'n': inputs[0],
            's': inputs[1],
            'k': inputs[2],
            'w': inputs[3],
        }

    def params_to_input(self, params: Dict[str, float]) -> List[float]:
        """Convert parameter dict to input array."""
        return [params['n'], params['s'], params['k'], params['w']]

    def evaluate_for_api(self, inputs: List[float]) -> List[float]:
        """
        Evaluate inputs and return outputs in API format.

        Args:
            inputs: [n, s, k, w]

        Returns:
            [chi2, neg_gap_mix, neg_inv, neg_gap_min, fragility]
        """
        params = self.input_to_params(inputs)
        result = self.oracle.evaluate(**params)

        obj = result['objectives']
        return [
            obj['chi2_total'],
            obj['neg_spectral_gap_mixed'],
            obj['neg_invariance_score'],
            obj['neg_min_individual_gap'],
            obj['fragility'],
        ]

    def generate_api_config(self) -> Dict:
        """Generate configuration JSON for Global MOO API."""
        return {
            'model_name': 'MetaCalculus_FRW_Optimization',
            'description': 'Multi-objective optimization for meta-calculus cosmology',
            'inputs': {
                'count': len(self.input_specs),
                'specs': self.input_specs,
            },
            'outputs': {
                'count': len(self.output_specs),
                'specs': self.output_specs,
            },
            'constraints': [
                {'name': 's_bound', 'input': 's', 'min': -0.05, 'max': 0.05},
                {'name': 'k_bound', 'input': 'k', 'min': -0.03, 'max': 0.03},
            ],
            'notes': [
                'All objectives are for MINIMIZATION',
                'Negative values indicate maximization targets',
                'Tight bounds ensure >90% feasibility',
            ]
        }

    def export_sample_data(self, n_samples: int = 20) -> Dict:
        """
        Generate sample input/output pairs for API initialization.

        Global MOO needs initial samples to build its surrogate model.
        """
        np.random.seed(42)

        samples = []
        for _ in range(n_samples):
            # Sample within tight bounds
            n = np.random.uniform(0.3, 1.5)
            s = np.random.uniform(-0.04, 0.04)
            k = np.random.uniform(-0.025, 0.025)
            w = np.random.uniform(-0.4, 0.4)

            inputs = [n, s, k, w]
            try:
                outputs = self.evaluate_for_api(inputs)
                samples.append({
                    'inputs': inputs,
                    'outputs': outputs,
                })
            except Exception as e:
                warnings.warn(f"Failed to evaluate sample: {e}")

        return {
            'n_samples': len(samples),
            'samples': samples,
        }


# =============================================================================
# GLOBAL MOO API CLIENT (Using Official SDK)
# =============================================================================

class GlobalMOOClient:
    """
    Client for Global MOO API using the official SDK.

    This client wraps the globalmoo-sdk package to provide optimization
    capabilities for meta-calculus physics problems.

    SDK Installation: pip install globalmoo-sdk
    API Documentation: https://globalmoo.gitbook.io/globalmoo-documentation
    """

    def __init__(self, api_key: Optional[str] = None,
                 base_url: Optional[str] = None,
                 debug: bool = False):
        """
        Initialize the Global MOO client.

        Args:
            api_key: API key for authentication. Defaults to GLOBALMOO_API_KEY.
            base_url: Base URL for API. Defaults to GLOBALMOO_API_URL.
            debug: Enable debug logging.
        """
        self.api_key = api_key or GLOBALMOO_API_KEY
        self.base_url = base_url or GLOBALMOO_API_URL
        self.debug = debug
        self._client = None
        self._model = None
        self._project = None
        self._trial = None
        self._objective = None

    def _get_client(self):
        """Lazy initialization of SDK client."""
        if self._client is None:
            try:
                from globalmoo.client import Client
                from globalmoo.credentials import Credentials

                credentials = Credentials(
                    api_key=self.api_key,
                    base_uri=self.base_url
                )
                self._client = Client(credentials=credentials, debug=self.debug)
            except ImportError:
                raise ImportError(
                    "globalmoo-sdk not installed. Install with: pip install globalmoo-sdk"
                )
        return self._client

    def check_connection(self) -> Dict:
        """Verify API connection and authentication."""
        try:
            client = self._get_client()
            # Try to read models as a connection test
            from globalmoo.request.read_models import ReadModels
            result = client.execute_request(ReadModels())
            return {'connected': True, 'models': len(result) if result else 0}
        except Exception as e:
            return {'connected': False, 'error': str(e)}

    def create_model(self, name: str = "MetaCalculus_FRW",
                     description: str = "Meta-calculus FRW cosmology multi-objective optimization") -> Dict:
        """Create a new model in Global MOO."""
        client = self._get_client()
        from globalmoo.request.create_model import CreateModel

        # Note: Global MOO requires description >= 8 chars
        self._model = client.execute_request(CreateModel(
            name=name,
            description=description
        ))
        return {'model_id': self._model.id, 'name': name}

    def create_project(self, model_id: Optional[str] = None,
                       name: str = "FRW_Optimization") -> Dict:
        """
        Create a project with meta-calculus input specifications.

        Args:
            model_id: Model ID to associate with. Uses last created if None.
            name: Project name.

        Returns:
            Project info including generated input cases.
        """
        client = self._get_client()
        from globalmoo.request.create_project import CreateProject

        if model_id is None and self._model is not None:
            model_id = self._model.id
        elif model_id is None:
            raise ValueError("No model ID. Create a model first.")

        # Meta-calculus input specifications
        self._project = client.execute_request(CreateProject(
            model_id=model_id,
            name=name,
            input_count=4,  # n, s, k, w
            minimums=[0.3, -0.05, -0.03, -0.5],
            maximums=[1.5, 0.05, 0.03, 0.5],
            input_types=["float", "float", "float", "float"],
            categories=[]
        ))

        return {
            'project_id': self._project.id,
            'input_cases': self._project.input_cases,
            'n_cases': len(self._project.input_cases)
        }

    def evaluate_and_load_outputs(self, adapter: 'GlobalMOOAdapter',
                                   project_id: Optional[str] = None) -> Dict:
        """
        Evaluate input cases and load output results.

        Args:
            adapter: GlobalMOOAdapter for physics evaluation.
            project_id: Project ID. Uses last created if None.

        Returns:
            Trial info.
        """
        client = self._get_client()
        from globalmoo.request.load_output_cases import LoadOutputCases

        if project_id is None and self._project is not None:
            project_id = self._project.id
        elif project_id is None:
            raise ValueError("No project ID. Create a project first.")

        # Evaluate each input case using physics oracle
        input_cases = self._project.input_cases
        output_cases = []

        for case in input_cases:
            # case is [n, s, k, w]
            outputs = adapter.evaluate_for_api(case)
            output_cases.append(outputs)

        # Load outputs to Global MOO
        self._trial = client.execute_request(LoadOutputCases(
            project_id=project_id,
            output_count=5,  # chi2, neg_gap, neg_inv, neg_min_gap, fragility
            output_cases=output_cases
        ))

        return {
            'trial_id': self._trial.id,
            'n_outputs': len(output_cases)
        }

    def configure_objectives(self, trial_id: Optional[str] = None) -> Dict:
        """
        Configure optimization objectives.

        All objectives are set for minimization (negatives for maximization targets).
        """
        client = self._get_client()
        from globalmoo.request.load_objectives import LoadObjectives
        from globalmoo.enums.objective_type import ObjectiveType

        if trial_id is None and self._trial is not None:
            trial_id = self._trial.id
        elif trial_id is None:
            raise ValueError("No trial ID. Load outputs first.")

        # Use first input/output as initial point
        initial_input = self._project.input_cases[0]
        initial_output = [0.0, -0.9, -0.9, -0.9, 0.0]  # Reasonable starting point

        # Objective targets (all minimize)
        # chi2 -> 0, neg_gap -> -1, neg_inv -> -1, neg_min_gap -> -1, fragility -> 0
        objectives = [0.0, -1.0, -1.0, -1.0, 0.0]

        # Note: Global MOO requires minimum_bounds < 0 and maximum_bounds > 0
        self._objective = client.execute_request(LoadObjectives(
            trial_id=trial_id,
            desired_l1_norm=0.0,
            objectives=objectives,
            objective_types=[ObjectiveType.PERCENT] * 5,
            initial_input=initial_input,
            initial_output=initial_output,
            minimum_bounds=[-1000.0, -1.0, -1.0, -1.0, -100.0],
            maximum_bounds=[1000.0, 1.0, 1.0, 1.0, 100.0]
        ))

        return {'objective_id': self._objective.id}

    def run_optimization(self, adapter: 'GlobalMOOAdapter',
                         n_iterations: int = 50,
                         verbose: bool = True) -> Dict:
        """
        Run a complete optimization loop using Global MOO SDK.

        This method handles the full workflow:
        1. Create model and project
        2. Evaluate initial cases
        3. Configure objectives
        4. Run inverse optimization loop
        5. Return results

        Args:
            adapter: GlobalMOOAdapter for evaluation
            n_iterations: Number of optimization iterations
            verbose: Print progress updates

        Returns:
            Dict with optimization results
        """
        if verbose:
            print("=" * 70)
            print("GLOBAL MOO OPTIMIZATION (Official SDK)")
            print("=" * 70)
            print(f"API Key: {self.api_key[:12]}...")
            print(f"API URL: {self.base_url}")
            print(f"Iterations: {n_iterations}")

        results_history = []

        try:
            # Step 1: Create model
            if verbose:
                print("\n1. Creating model...")
            model_info = self.create_model(f"MetaCalculus_{int(time.time())}")
            if verbose:
                print(f"   Model ID: {model_info['model_id']}")

            # Step 2: Create project
            if verbose:
                print("\n2. Creating project...")
            project_info = self.create_project()
            if verbose:
                print(f"   Project ID: {project_info['project_id']}")
                print(f"   Input cases: {project_info['n_cases']}")

            # Step 3: Evaluate and load outputs
            if verbose:
                print("\n3. Evaluating initial cases...")
            trial_info = self.evaluate_and_load_outputs(adapter)
            if verbose:
                print(f"   Trial ID: {trial_info['trial_id']}")

            # Step 4: Configure objectives
            if verbose:
                print("\n4. Configuring objectives...")
            obj_info = self.configure_objectives()
            if verbose:
                print(f"   Objective ID: {obj_info['objective_id']}")

            # Step 5: Run inverse optimization loop
            if verbose:
                print(f"\n5. Running optimization ({n_iterations} iterations)...")

            client = self._get_client()
            from globalmoo.request.suggest_inverse import SuggestInverse
            from globalmoo.request.load_inversed_output import LoadInversedOutput

            for i in range(n_iterations):
                try:
                    # Get suggested input
                    inverse = client.execute_request(SuggestInverse(
                        objective_id=self._objective.id
                    ))

                    # Evaluate the suggested input
                    next_input = inverse.input
                    next_output = adapter.evaluate_for_api(next_input)

                    # Submit result
                    inverse = client.execute_request(LoadInversedOutput(
                        inverse_id=inverse.id,
                        output=next_output
                    ))

                    results_history.append({
                        'iteration': i + 1,
                        'input': next_input,
                        'output': next_output,
                    })

                    if verbose and (i + 1) % 10 == 0:
                        print(f"   Iteration {i+1}/{n_iterations}")

                    # Check stopping condition
                    if hasattr(inverse, 'should_stop') and inverse.should_stop():
                        if verbose:
                            print(f"   Converged at iteration {i+1}")
                        break

                except Exception as e:
                    if verbose:
                        print(f"   Warning at iteration {i+1}: {e}")
                    continue

            if verbose:
                print(f"\nOptimization complete!")
                print(f"Total evaluations: {len(results_history)}")

            # Extract best solutions from history
            pareto_front = self._extract_pareto_front(results_history)

            return {
                'success': True,
                'n_iterations': len(results_history),
                'n_solutions': len(pareto_front),
                'pareto_front': pareto_front,
                'history': results_history,
                'model_id': model_info['model_id'],
                'project_id': project_info['project_id'],
            }

        except Exception as e:
            if verbose:
                print(f"\nError: {e}")
                print("Falling back to pymoo...")

            return {
                'success': False,
                'error': str(e),
                'fallback': 'Use pymoo instead',
                'history': results_history,
            }

    def _extract_pareto_front(self, history: List[Dict]) -> List[Dict]:
        """Extract non-dominated solutions from optimization history."""
        if not history:
            return []

        # Convert to arrays for Pareto analysis
        inputs = np.array([h['input'] for h in history])
        outputs = np.array([h['output'] for h in history])

        # Find non-dominated solutions
        n = len(outputs)
        is_dominated = np.zeros(n, dtype=bool)

        for i in range(n):
            for j in range(n):
                if i != j:
                    # j dominates i if j is better in all objectives
                    if np.all(outputs[j] <= outputs[i]) and np.any(outputs[j] < outputs[i]):
                        is_dominated[i] = True
                        break

        pareto_indices = np.where(~is_dominated)[0]

        # Format Pareto solutions
        pareto_front = []
        for idx in pareto_indices:
            x = inputs[idx]
            f = outputs[idx]
            pareto_front.append({
                'params': {'n': x[0], 's': x[1], 'k': x[2], 'w': x[3]},
                'objectives': {
                    'chi2_total': f[0],
                    'spectral_gap_mixed': -f[1],  # Convert back
                    'invariance_score': -f[2],
                    'min_individual_gap': -f[3],
                    'fragility': f[4] if len(f) > 4 else 0.0,
                }
            })

        return pareto_front


# =============================================================================
# PYMOO ADAPTER (Alternative to Global MOO)
# =============================================================================

class PymooAdapter:
    """
    Adapter for pymoo optimization library.

    This provides a fallback if Global MOO is not available,
    using the open-source pymoo library.
    """

    def __init__(self, oracle: Optional[PhysicsOracle] = None):
        self.oracle = oracle or PhysicsOracle()

    def create_problem(self):
        """Create a pymoo Problem instance."""
        try:
            from pymoo.core.problem import Problem
        except ImportError:
            raise ImportError(
                "pymoo not installed. Install with: pip install pymoo"
            )

        oracle = self.oracle

        class MetaCalculusProblem(Problem):
            def __init__(self):
                super().__init__(
                    n_var=4,
                    n_obj=5,
                    n_constr=0,  # Constraints built into bounds
                    xl=np.array([0.3, -0.05, -0.03, -0.5]),
                    xu=np.array([1.5, 0.05, 0.03, 0.5]),
                )
                self.oracle = oracle

            def _evaluate(self, x, out, *args, **kwargs):
                f = np.zeros((len(x), 5))
                for i, row in enumerate(x):
                    n, s, k, w = row
                    result = self.oracle.evaluate(n, s, k, w,
                                                   compute_fragility=False)
                    obj = result['objectives']
                    f[i, 0] = obj['chi2_total']
                    f[i, 1] = obj['neg_spectral_gap_mixed']
                    f[i, 2] = obj['neg_invariance_score']
                    f[i, 3] = obj['neg_min_individual_gap']
                    f[i, 4] = obj['fragility']
                out["F"] = f

        return MetaCalculusProblem()

    def run_optimization(self, n_gen: int = 50, pop_size: int = 40,
                         verbose: bool = True) -> Dict:
        """
        Run multi-objective optimization with NSGA-II.

        Returns:
            Dict with Pareto-optimal solutions and their objectives
        """
        try:
            from pymoo.algorithms.moo.nsga2 import NSGA2
            from pymoo.optimize import minimize
            from pymoo.termination import get_termination
        except ImportError:
            raise ImportError(
                "pymoo not installed. Install with: pip install pymoo"
            )

        problem = self.create_problem()

        algorithm = NSGA2(pop_size=pop_size)
        termination = get_termination("n_gen", n_gen)

        if verbose:
            print(f"Running NSGA-II: {n_gen} generations, pop_size={pop_size}")

        result = minimize(
            problem,
            algorithm,
            termination,
            seed=42,
            verbose=verbose
        )

        # Extract Pareto front
        pareto_solutions = []
        for i, (x, f) in enumerate(zip(result.X, result.F)):
            pareto_solutions.append({
                'id': i,
                'params': {'n': x[0], 's': x[1], 'k': x[2], 'w': x[3]},
                'objectives': {
                    'chi2_total': f[0],
                    'spectral_gap_mixed': -f[1],  # Convert back to positive
                    'invariance_score': -f[2],
                    'min_individual_gap': -f[3],
                    'fragility': f[4],
                }
            })

        return {
            'n_solutions': len(pareto_solutions),
            'pareto_front': pareto_solutions,
            'algorithm': 'NSGA-II',
            'n_generations': n_gen,
        }


# =============================================================================
# CLI AND DEMOS
# =============================================================================

def demo_evaluation():
    """Demonstrate single evaluation."""
    print("=" * 70)
    print("META-CALCULUS MOO EVALUATION DEMO")
    print("=" * 70)

    oracle = PhysicsOracle(n_solutions=30, sigma=0.5, seed=42)

    # Test points
    test_cases = [
        (0.67, 0.0, 0.0, 0.0, "Standard matter-like (baseline)"),
        (0.5, 0.02, 0.01, 0.33, "Radiation-like with small meta-weight"),
        (1.0, -0.03, 0.02, -0.5, "Accelerating with negative EoS"),
        (0.67, 0.1, 0.05, 0.0, "INFEASIBLE: s and k too large"),
    ]

    for n, s, k, w, description in test_cases:
        print(f"\n{description}")
        print(f"  Parameters: n={n}, s={s}, k={k}, w={w}")

        result = oracle.evaluate(n, s, k, w, compute_fragility=False)

        if result['feasible']:
            obj = result['objectives']
            det = result.get('details', {})
            print(f"  Feasible: YES")
            print(f"  chi2_total: {obj['chi2_total']:.4f}")
            print(f"  spectral_gap_mixed: {-obj['neg_spectral_gap_mixed']:.4f}")
            print(f"  invariance_score: {-obj['neg_invariance_score']:.4f}")
        else:
            print(f"  Feasible: NO")
            print(f"  Violations: {result['violations']}")


def demo_pymoo():
    """Demonstrate optimization with pymoo."""
    print("=" * 70)
    print("META-CALCULUS PYMOO OPTIMIZATION DEMO")
    print("=" * 70)

    try:
        adapter = PymooAdapter()
        result = adapter.run_optimization(n_gen=20, pop_size=20, verbose=True)

        print(f"\n{'='*70}")
        print(f"Found {result['n_solutions']} Pareto-optimal solutions")
        print(f"{'='*70}")

        # Show top 5 by spectral gap
        sorted_solutions = sorted(
            result['pareto_front'],
            key=lambda x: x['objectives']['spectral_gap_mixed'],
            reverse=True
        )

        print("\nTop 5 by spectral gap:")
        for sol in sorted_solutions[:5]:
            p = sol['params']
            o = sol['objectives']
            print(f"  n={p['n']:.3f}, s={p['s']:.4f}, k={p['k']:.4f}, w={p['w']:.3f}")
            print(f"    gap={o['spectral_gap_mixed']:.4f}, inv={o['invariance_score']:.4f}, chi2={o['chi2_total']:.2f}")

    except ImportError as e:
        print(f"Error: {e}")
        print("Install pymoo with: pip install pymoo")


def export_globalmoo_template():
    """Export configuration for Global MOO API."""
    adapter = GlobalMOOAdapter()

    config = adapter.generate_api_config()
    samples = adapter.export_sample_data(n_samples=15)

    output = {
        'config': config,
        'initial_samples': samples,
    }

    print(json.dumps(output, indent=2))


def demo_globalmoo(n_iterations: int = 30):
    """Demonstrate Global MOO optimization."""
    print("=" * 70)
    print("GLOBAL MOO OPTIMIZATION DEMO")
    print("=" * 70)

    client = GlobalMOOClient()
    adapter = GlobalMOOAdapter()

    # Check connection first
    print("\nChecking API connection...")
    connection = client.check_connection()

    if not connection['connected']:
        print(f"API connection failed: {connection.get('error', 'Unknown error')}")
        print("\nFalling back to pymoo for demonstration...")
        print("(Global MOO API may require registration at globalmoo.com)")
        demo_pymoo()
        return

    print(f"Connected to Global MOO API")

    # Run optimization
    result = client.run_optimization(
        adapter,
        n_iterations=n_iterations,
        verbose=True
    )

    if result['success']:
        print_pareto_analysis(result['pareto_front'], "Global MOO")
    else:
        print(f"\nOptimization failed: {result.get('error')}")
        print("Falling back to pymoo...")
        demo_pymoo()


def print_pareto_analysis(pareto_front: List[Dict], optimizer_name: str):
    """Print analysis of Pareto frontier solutions."""
    if not pareto_front:
        print("No Pareto solutions found.")
        return

    print(f"\n{'='*70}")
    print(f"{optimizer_name} PARETO FRONTIER ANALYSIS")
    print(f"{'='*70}")
    print(f"Total solutions: {len(pareto_front)}")

    # Sort by different objectives
    by_gap = sorted(pareto_front, key=lambda x: x['objectives']['spectral_gap_mixed'], reverse=True)
    by_inv = sorted(pareto_front, key=lambda x: x['objectives']['invariance_score'], reverse=True)
    by_chi2 = sorted(pareto_front, key=lambda x: x['objectives']['chi2_total'])

    print("\n--- TOP 3 BY SPECTRAL GAP (structure clarity) ---")
    for i, sol in enumerate(by_gap[:3]):
        p = sol['params']
        o = sol['objectives']
        print(f"  {i+1}. n={p['n']:.4f}, s={p['s']:.5f}, k={p['k']:.5f}, w={p['w']:.4f}")
        print(f"     gap={o['spectral_gap_mixed']:.4f}, inv={o['invariance_score']:.4f}, chi2={o['chi2_total']:.2f}")

    print("\n--- TOP 3 BY INVARIANCE SCORE (scheme robustness) ---")
    for i, sol in enumerate(by_inv[:3]):
        p = sol['params']
        o = sol['objectives']
        print(f"  {i+1}. n={p['n']:.4f}, s={p['s']:.5f}, k={p['k']:.5f}, w={p['w']:.4f}")
        print(f"     gap={o['spectral_gap_mixed']:.4f}, inv={o['invariance_score']:.4f}, chi2={o['chi2_total']:.2f}")

    print("\n--- TOP 3 BY OBSERVATIONAL FIT (lowest chi2) ---")
    for i, sol in enumerate(by_chi2[:3]):
        p = sol['params']
        o = sol['objectives']
        print(f"  {i+1}. n={p['n']:.4f}, s={p['s']:.5f}, k={p['k']:.5f}, w={p['w']:.4f}")
        print(f"     gap={o['spectral_gap_mixed']:.4f}, inv={o['invariance_score']:.4f}, chi2={o['chi2_total']:.2f}")

    # Find "sweet spot" solutions (good on all objectives)
    print("\n--- SWEET SPOT SOLUTIONS (balanced trade-off) ---")
    # Rank by average percentile across objectives
    def compute_score(sol):
        o = sol['objectives']
        # Higher is better for gap and invariance, lower is better for chi2
        gap_score = o['spectral_gap_mixed']
        inv_score = o['invariance_score']
        chi2_score = 1.0 / (1.0 + o['chi2_total'])  # Invert chi2
        return gap_score + inv_score + chi2_score

    by_balanced = sorted(pareto_front, key=compute_score, reverse=True)
    for i, sol in enumerate(by_balanced[:3]):
        p = sol['params']
        o = sol['objectives']
        score = compute_score(sol)
        print(f"  {i+1}. n={p['n']:.4f}, s={p['s']:.5f}, k={p['k']:.5f}, w={p['w']:.4f}")
        print(f"     gap={o['spectral_gap_mixed']:.4f}, inv={o['invariance_score']:.4f}, chi2={o['chi2_total']:.2f}")
        print(f"     balance_score={score:.4f}")


def compare_optimizers(n_gen_pymoo: int = 30, n_iter_globalmoo: int = 30):
    """Run both optimizers and compare results."""
    print("=" * 70)
    print("OPTIMIZER COMPARISON: PYMOO vs GLOBAL MOO")
    print("=" * 70)

    results = {}

    # Run pymoo
    print("\n--- Running pymoo (NSGA-II) ---")
    try:
        pymoo_adapter = PymooAdapter()
        pymoo_result = pymoo_adapter.run_optimization(
            n_gen=n_gen_pymoo,
            pop_size=30,
            verbose=True
        )
        results['pymoo'] = pymoo_result
        print(f"pymoo found {pymoo_result['n_solutions']} Pareto solutions")
    except Exception as e:
        print(f"pymoo failed: {e}")
        results['pymoo'] = None

    # Run Global MOO
    print("\n--- Running Global MOO ---")
    try:
        client = GlobalMOOClient()
        adapter = GlobalMOOAdapter()

        connection = client.check_connection()
        if connection['connected']:
            globalmoo_result = client.run_optimization(
                adapter,
                n_iterations=n_iter_globalmoo,
                verbose=True
            )
            results['globalmoo'] = globalmoo_result
            print(f"Global MOO found {globalmoo_result['n_solutions']} Pareto solutions")
        else:
            print(f"Global MOO not available: {connection.get('error')}")
            results['globalmoo'] = None
    except Exception as e:
        print(f"Global MOO failed: {e}")
        results['globalmoo'] = None

    # Compare results
    print("\n" + "=" * 70)
    print("COMPARISON SUMMARY")
    print("=" * 70)

    if results['pymoo'] and results['pymoo']['pareto_front']:
        print_pareto_analysis(results['pymoo']['pareto_front'], "PYMOO")

    if results['globalmoo'] and results['globalmoo'].get('success') and results['globalmoo']['pareto_front']:
        print_pareto_analysis(results['globalmoo']['pareto_front'], "GLOBAL MOO")

    # Find consensus solutions (appear in both)
    if results['pymoo'] and results['globalmoo'] and results['globalmoo'].get('success'):
        print("\n--- CONSENSUS ANALYSIS ---")
        pymoo_params = set()
        for sol in results['pymoo']['pareto_front']:
            p = sol['params']
            # Round to 2 decimal places for comparison
            key = (round(p['n'], 2), round(p['s'], 3), round(p['k'], 3), round(p['w'], 2))
            pymoo_params.add(key)

        consensus_count = 0
        for sol in results['globalmoo']['pareto_front']:
            p = sol['params']
            key = (round(p['n'], 2), round(p['s'], 3), round(p['k'], 3), round(p['w'], 2))
            if key in pymoo_params:
                consensus_count += 1

        print(f"Solutions in similar regions: {consensus_count}")
        print("(Similar = same params rounded to 2-3 decimal places)")

    return results


def save_results(results: Dict, filename: str = "moo_results.json"):
    """Save optimization results to file."""
    output_path = os.path.join(
        os.path.dirname(__file__),
        '..',
        'results',
        filename
    )

    # Ensure results directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"Results saved to: {output_path}")
    return output_path


def run_full_optimization(n_gen: int = 50, save: bool = True):
    """Run complete optimization workflow."""
    print("=" * 70)
    print("META-CALCULUS FULL OPTIMIZATION RUN")
    print("=" * 70)
    print(f"Using pymoo with {n_gen} generations")

    # Run pymoo (always available)
    adapter = PymooAdapter()
    result = adapter.run_optimization(n_gen=n_gen, pop_size=40, verbose=True)

    # Print analysis
    print_pareto_analysis(result['pareto_front'], "PYMOO NSGA-II")

    # Save results
    if save:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"moo_results_{timestamp}.json"
        save_results(result, filename)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Multi-Objective Optimization for Meta-Calculus"
    )
    parser.add_argument('command', nargs='?', default='demo',
                        choices=['demo', 'evaluate', 'pymoo', 'globalmoo',
                                 'compare', 'export-template', 'full'],
                        help="Command to run")
    parser.add_argument('--n', type=float, default=0.67, help="Expansion exponent")
    parser.add_argument('--s', type=float, default=0.0, help="Action weight")
    parser.add_argument('--k', type=float, default=0.0, help="Meta-weight")
    parser.add_argument('--w', type=float, default=0.0, help="Equation of state")
    parser.add_argument('--gen', type=int, default=50, help="Number of generations/iterations")
    parser.add_argument('--no-save', action='store_true', help="Don't save results")

    args = parser.parse_args()

    if args.command == 'demo':
        demo_evaluation()
    elif args.command == 'evaluate':
        oracle = PhysicsOracle()
        result = oracle.evaluate(args.n, args.s, args.k, args.w)
        print(json.dumps(result, indent=2, default=str))
    elif args.command == 'pymoo':
        demo_pymoo()
    elif args.command == 'globalmoo':
        demo_globalmoo(n_iterations=args.gen)
    elif args.command == 'compare':
        compare_optimizers(n_gen_pymoo=args.gen, n_iter_globalmoo=args.gen)
    elif args.command == 'export-template':
        export_globalmoo_template()
    elif args.command == 'full':
        run_full_optimization(n_gen=args.gen, save=not args.no_save)

    return 0


if __name__ == "__main__":
    sys.exit(main())
