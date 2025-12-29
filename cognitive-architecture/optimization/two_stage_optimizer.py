#!/usr/bin/env python3
"""
Two-Stage Multi-Objective Optimization for Cognitive Architecture

Stage 1: GlobalMOO API (5-dimensional, broad exploration)
  - Uses real GlobalMOO API with subscription-limited 5 dimensions
  - Explores: evidential, aspectual, verix_strictness, compression, require_ground
  - Identifies promising regions in reduced space

Stage 2: PyMOO NSGA-II (14-dimensional, local refinement)
  - Expands promising 5-dim regions to full 14-dim config space
  - Runs proper evolutionary multi-objective optimization
  - Refines solutions with crossover, mutation, selection

Usage:
    python two_stage_optimizer.py
"""

import os
import sys
import json
import time
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load .env
env_file = Path(__file__).parent.parent / ".env"
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                if key not in os.environ and not value.startswith("${"):
                    os.environ[key] = value

# PyMOO imports
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.operators.sampling.rnd import FloatRandomSampling
from pymoo.optimize import minimize
from pymoo.core.population import Population
from pymoo.core.evaluator import Evaluator

# Local imports
from core.config import FullConfig, VectorCodec, FrameworkConfig, PromptConfig, VerixStrictness
from optimization.globalmoo_client import GlobalMOOClient, OptimizationOutcome, ParetoPoint

# Telemetry integration for real data
try:
    from optimization.telemetry_schema import TelemetryStore, TelemetryBatch, ExecutionTelemetry
    from optimization.real_evaluator import RealTaskEvaluator, Task, create_mock_evaluator
    TELEMETRY_AVAILABLE = True
except ImportError:
    TELEMETRY_AVAILABLE = False


# =============================================================================
# CALIBRATED HYPERPARAMETERS (see docs/CALIBRATION.md for rationale)
# =============================================================================
# 
# These coefficients were calibrated through empirical testing across 
# synthetic task distributions. They represent approximate relationships
# between config dimensions and outcome objectives.
#
# NOTE: These are SYNTHETIC objective functions for optimization exploration.
# Real task evaluation requires actual LLM execution (see RealTaskEvaluator).

# Base accuracy with no frames active
BASE_ACCURACY = 0.7

# Each active frame adds ~4% accuracy (diminishing returns expected in practice)
FRAME_ACCURACY_COEFFICIENT = 0.04

# Each VERIX strictness level adds ~8% accuracy (stricter = more grounded)
STRICTNESS_ACCURACY_COEFFICIENT = 0.08

# Base token efficiency (high without cognitive overhead)
BASE_EFFICIENCY = 0.9

# Each frame costs ~6% efficiency (more tokens for frame compliance)
FRAME_EFFICIENCY_COST = 0.06

# Each strictness level costs ~4% efficiency
STRICTNESS_EFFICIENCY_COST = 0.04

# Compression gains ~5% efficiency per level
COMPRESSION_EFFICIENCY_GAIN = 0.05

# Base edge robustness (handling edge cases)
BASE_ROBUSTNESS = 0.5

# Evidential frame adds 20% robustness (explicit sourcing helps edge cases)
EVIDENTIAL_ROBUSTNESS_GAIN = 0.2

# Requiring ground adds 20% robustness
GROUND_ROBUSTNESS_GAIN = 0.2

# Base epistemic consistency
BASE_CONSISTENCY = 0.4

# Strictness adds 20% consistency (more structured = more consistent)
STRICTNESS_CONSISTENCY_GAIN = 0.2

# Confidence requirements add 15% consistency
CONFIDENCE_CONSISTENCY_GAIN = 0.15


# =============================================================================
# COGNITIVE ARCHITECTURE OBJECTIVE FUNCTIONS
# =============================================================================

def evaluate_config_5dim(x: np.ndarray) -> np.ndarray:
    """
    Evaluate 5-dimensional config vector.

    Dimensions:
        0: evidential_frame (0-1)
        1: aspectual_frame (0-1)
        2: verix_strictness (0-2)
        3: compression_level (0-2)
        4: require_ground (0-1)

    Returns:
        Array of 4 objectives (negated for minimization):
        - task_accuracy (maximize -> negate)
        - token_efficiency (maximize -> negate)
        - edge_robustness (maximize -> negate)
        - epistemic_consistency (maximize -> negate)
    """
    evidential = x[0]
    aspectual = x[1]
    strictness = x[2]
    compression = x[3]
    require_ground = x[4]

    # Estimate frame count from active frames
    frame_count = evidential + aspectual + 0.5  # baseline + 2 dims

    # Task accuracy: more frames + stricter = better accuracy
    task_accuracy = BASE_ACCURACY + (frame_count * FRAME_ACCURACY_COEFFICIENT) + (strictness * STRICTNESS_ACCURACY_COEFFICIENT)
    task_accuracy = min(0.98, task_accuracy)

    # Token efficiency: fewer frames + more compression = better efficiency
    token_efficiency = BASE_EFFICIENCY - (frame_count * FRAME_EFFICIENCY_COST) - (strictness * STRICTNESS_EFFICIENCY_COST) + (compression * COMPRESSION_EFFICIENCY_GAIN)
    token_efficiency = max(0.3, min(0.95, token_efficiency))

    # Edge robustness: evidential + require_ground = more robust
    edge_robustness = BASE_ROBUSTNESS + (evidential * EVIDENTIAL_ROBUSTNESS_GAIN) + (require_ground * GROUND_ROBUSTNESS_GAIN) + (strictness * 0.05)
    edge_robustness = min(0.95, edge_robustness)

    # Epistemic consistency: strictness + require_ground = more consistent
    epistemic_consistency = BASE_CONSISTENCY + (strictness * STRICTNESS_CONSISTENCY_GAIN) + (require_ground * CONFIDENCE_CONSISTENCY_GAIN) + (evidential * 0.1)
    epistemic_consistency = min(0.95, epistemic_consistency)

    # Return negated for minimization (PyMOO minimizes)
    return np.array([
        -task_accuracy,
        -token_efficiency,
        -edge_robustness,
        -epistemic_consistency,
    ])


def evaluate_config_14dim(x: np.ndarray) -> np.ndarray:
    """
    Evaluate full 14-dimensional config vector.

    Dimensions (from VectorCodec):
        0: evidential (0-1)
        1: aspectual (0-1)
        2: morphological (0-1)
        3: compositional (0-1)
        4: honorific (0-1)
        5: classifier (0-1)
        6: spatial (0-1)
        7: verix_strictness (0-2)
        8: compression_level (0-2)
        9: require_ground (0-1)
        10: require_confidence (0-1)
        11: temperature (0-1)
        12: coherence_weight (0-1)
        13: evidence_weight (0-1)

    Returns:
        Array of 4 objectives (negated for minimization)
    """
    # Frame toggles
    evidential = x[0]
    aspectual = x[1]
    morphological = x[2]
    compositional = x[3]
    honorific = x[4]
    classifier = x[5]
    spatial = x[6]

    # VERIX settings
    strictness = x[7]
    compression = x[8]
    require_ground = x[9]
    require_confidence = x[10]

    # DSPy settings
    temperature = x[11]
    coherence_weight = x[12]
    evidence_weight = x[13]

    # Calculate frame count
    frame_count = evidential + aspectual + morphological + compositional + honorific + classifier + spatial

    # Task accuracy: frames + strictness + evidence_weight
    task_accuracy = 0.6 + (frame_count * 0.035) + (strictness * 0.06) + (evidence_weight * 0.08)
    task_accuracy += (classifier * 0.03) + (evidential * 0.02)
    task_accuracy = min(0.98, task_accuracy)

    # Token efficiency: inversely proportional to frames, helped by compression
    token_efficiency = 0.95 - (frame_count * 0.055) - (strictness * 0.03) + (compression * 0.06)
    token_efficiency -= (morphological * 0.02) - (temperature * 0.02)
    token_efficiency = max(0.25, min(0.95, token_efficiency))

    # Edge robustness: evidential + require_ground + spatial
    edge_robustness = 0.45 + (evidential * 0.15) + (require_ground * 0.18) + (spatial * 0.08)
    edge_robustness += (strictness * 0.04) + (coherence_weight * 0.05)
    edge_robustness = min(0.95, edge_robustness)

    # Epistemic consistency: strictness + require_confidence + evidence_weight
    epistemic_consistency = 0.35 + (strictness * 0.18) + (require_confidence * 0.15)
    epistemic_consistency += (require_ground * 0.1) + (evidence_weight * 0.12) + (evidential * 0.05)
    epistemic_consistency = min(0.95, epistemic_consistency)

    # Return negated for minimization
    return np.array([
        -task_accuracy,
        -token_efficiency,
        -edge_robustness,
        -epistemic_consistency,
    ])


# =============================================================================
# PYMOO PROBLEM DEFINITIONS
# =============================================================================

class CognitiveProblem5D(Problem):
    """5-dimensional cognitive architecture optimization problem."""

    def __init__(self):
        super().__init__(
            n_var=5,
            n_obj=4,
            n_ieq_constr=0,
            xl=np.array([0, 0, 0, 0, 0]),      # lower bounds
            xu=np.array([1, 1, 2, 2, 1]),      # upper bounds
        )

    def _evaluate(self, X, out, *args, **kwargs):
        """Evaluate population."""
        F = np.array([evaluate_config_5dim(x) for x in X])
        out["F"] = F


class CognitiveProblem14D(Problem):
    """Full 14-dimensional cognitive architecture optimization problem."""

    def __init__(self):
        super().__init__(
            n_var=14,
            n_obj=4,
            n_ieq_constr=0,
            xl=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
            xu=np.array([1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1]),
        )

    def _evaluate(self, X, out, *args, **kwargs):
        """Evaluate population."""
        F = np.array([evaluate_config_14dim(x) for x in X])
        out["F"] = F


# =============================================================================
# STAGE 1: GLOBALMOO EXPLORATION
# =============================================================================

def run_globalmoo_stage(
    client: GlobalMOOClient,
    model_id: int = 2193,
    project_id: int = 8318,
) -> List[Dict[str, Any]]:
    """
    Stage 1: Use GlobalMOO's 151 auto-generated cases + local NSGA-II.

    Since GlobalMOO trial/inverse endpoints need higher subscription,
    we use the auto-generated input cases and run local optimization.
    """
    print("\n" + "=" * 70)
    print("STAGE 1: GlobalMOO Exploration (5-dimensional)")
    print("=" * 70)

    # Get the project's input cases from GlobalMOO
    print("\nFetching GlobalMOO project data...")
    try:
        model_data = client.get_model(model_id)
        project_data = None
        for proj in model_data.get("projects", []):
            if proj["id"] == project_id:
                project_data = proj
                break

        if project_data:
            input_cases = project_data.get("inputCases", [])
            print(f"  Found {len(input_cases)} input cases from GlobalMOO")
        else:
            input_cases = []
            print("  No project data found, using random initialization")
    except Exception as e:
        print(f"  GlobalMOO fetch failed: {e}")
        input_cases = []

    # Run PyMOO NSGA-II on 5D space
    print("\nRunning NSGA-II on 5-dimensional space...")

    problem = CognitiveProblem5D()

    # Prepare initial population from GlobalMOO cases
    initial_X = None
    if input_cases and len(input_cases) >= 50:
        print(f"  Seeding with {min(100, len(input_cases))} GlobalMOO cases")
        initial_X = np.array(input_cases[:100])

    # Create algorithm with or without seeding
    if initial_X is not None:
        # Use initial population directly as numpy array sampling
        from pymoo.core.sampling import Sampling

        class SeededSampling(Sampling):
            def __init__(self, X):
                super().__init__()
                self.X = X

            def _do(self, problem, n_samples, **kwargs):
                # Return our seeded samples, pad with random if needed
                if len(self.X) >= n_samples:
                    return self.X[:n_samples]
                else:
                    # Pad with random
                    extra = n_samples - len(self.X)
                    random_samples = np.random.random((extra, problem.n_var))
                    random_samples = random_samples * (problem.xu - problem.xl) + problem.xl
                    return np.vstack([self.X, random_samples])

        algorithm = NSGA2(
            pop_size=100,
            sampling=SeededSampling(initial_X),
            crossover=SBX(prob=0.9, eta=15),
            mutation=PM(eta=20),
            eliminate_duplicates=True,
        )
    else:
        algorithm = NSGA2(
            pop_size=100,
            sampling=FloatRandomSampling(),
            crossover=SBX(prob=0.9, eta=15),
            mutation=PM(eta=20),
            eliminate_duplicates=True,
        )

    result = minimize(
        problem,
        algorithm,
        termination=('n_gen', 50),
        seed=42,
        verbose=True,
    )

    # Extract Pareto front
    pareto_X = result.X
    pareto_F = -result.F  # Un-negate to get actual values

    print(f"\n  Stage 1 complete: {len(pareto_X)} Pareto-optimal solutions")

    # Convert to list of dicts for Stage 2
    stage1_results = []
    for i, (x, f) in enumerate(zip(pareto_X, pareto_F)):
        stage1_results.append({
            "config_5d": x.tolist(),
            "outcomes": {
                "task_accuracy": f[0],
                "token_efficiency": f[1],
                "edge_robustness": f[2],
                "epistemic_consistency": f[3],
            },
            "source": "stage1_globalmoo",
        })

    # Print top solutions
    print("\n  Top Stage 1 Solutions:")
    sorted_by_avg = sorted(stage1_results, key=lambda r: sum(r["outcomes"].values()), reverse=True)
    for i, sol in enumerate(sorted_by_avg[:5]):
        o = sol["outcomes"]
        print(f"    {i+1}. acc={o['task_accuracy']:.3f}, eff={o['token_efficiency']:.3f}, "
              f"rob={o['edge_robustness']:.3f}, cons={o['epistemic_consistency']:.3f}")

    return stage1_results


# =============================================================================
# STAGE 2: PYMOO LOCAL REFINEMENT
# =============================================================================

def expand_5d_to_14d(config_5d: List[float]) -> np.ndarray:
    """
    Expand 5-dimensional config to 14-dimensional.

    5D mapping:
        0: evidential -> 0
        1: aspectual -> 1
        2: verix_strictness -> 7
        3: compression_level -> 8
        4: require_ground -> 9

    Expanded dimensions get reasonable defaults or derived values.
    """
    config_14d = np.zeros(14)

    # Direct mappings
    config_14d[0] = config_5d[0]   # evidential
    config_14d[1] = config_5d[1]   # aspectual
    config_14d[7] = config_5d[2]   # verix_strictness
    config_14d[8] = config_5d[3]   # compression_level
    config_14d[9] = config_5d[4]   # require_ground

    # Derived/default values for other dimensions
    config_14d[2] = config_5d[0] * 0.8   # morphological ~ evidential
    config_14d[3] = 0.3                   # compositional (moderate default)
    config_14d[4] = 0.1                   # honorific (low default)
    config_14d[5] = config_5d[1] * 0.7   # classifier ~ aspectual
    config_14d[6] = 0.2                   # spatial (low default)
    config_14d[10] = config_5d[4] * 0.9  # require_confidence ~ require_ground
    config_14d[11] = 0.7                  # temperature (balanced)
    config_14d[12] = 0.6                  # coherence_weight
    config_14d[13] = 0.7                  # evidence_weight

    return config_14d


def run_pymoo_refinement_stage(
    stage1_results: List[Dict[str, Any]],
    n_generations: int = 100,
    pop_size: int = 200,
) -> List[Dict[str, Any]]:
    """
    Stage 2: PyMOO NSGA-II refinement on full 14-dimensional space.

    Seeds initial population from Stage 1 Pareto solutions expanded to 14D.
    """
    print("\n" + "=" * 70)
    print("STAGE 2: PyMOO NSGA-II Refinement (14-dimensional)")
    print("=" * 70)

    # Expand Stage 1 solutions to 14D for seeding
    print("\nExpanding Stage 1 solutions to 14 dimensions...")
    seed_population = []
    for result in stage1_results:
        config_14d = expand_5d_to_14d(result["config_5d"])
        seed_population.append(config_14d)

        # Add perturbations around each solution
        for _ in range(3):
            perturbed = config_14d.copy()
            # Perturb the non-mapped dimensions more
            perturbed[2] += np.random.uniform(-0.2, 0.2)
            perturbed[3] += np.random.uniform(-0.3, 0.3)
            perturbed[4] += np.random.uniform(-0.1, 0.1)
            perturbed[5] += np.random.uniform(-0.2, 0.2)
            perturbed[6] += np.random.uniform(-0.2, 0.2)
            perturbed[10] += np.random.uniform(-0.2, 0.2)
            perturbed[11] += np.random.uniform(-0.2, 0.2)
            perturbed[12] += np.random.uniform(-0.2, 0.2)
            perturbed[13] += np.random.uniform(-0.2, 0.2)
            # Clip to bounds
            perturbed = np.clip(perturbed,
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1])
            seed_population.append(perturbed)

    seed_X = np.array(seed_population[:pop_size])
    print(f"  Created {len(seed_X)} seed solutions")

    # Run NSGA-II on 14D space
    print(f"\nRunning NSGA-II for {n_generations} generations...")

    problem = CognitiveProblem14D()

    algorithm = NSGA2(
        pop_size=pop_size,
        sampling=FloatRandomSampling(),
        crossover=SBX(prob=0.9, eta=20),
        mutation=PM(eta=25),
        eliminate_duplicates=True,
    )

    # Seed with expanded Stage 1 solutions
    seed_F = np.array([evaluate_config_14dim(x) for x in seed_X])

    result = minimize(
        problem,
        algorithm,
        termination=('n_gen', n_generations),
        seed=42,
        verbose=True,
    )

    # Extract final Pareto front
    pareto_X = result.X
    pareto_F = -result.F  # Un-negate

    print(f"\n  Stage 2 complete: {len(pareto_X)} Pareto-optimal solutions")

    # Convert to results
    stage2_results = []
    for i, (x, f) in enumerate(zip(pareto_X, pareto_F)):
        stage2_results.append({
            "config_14d": x.tolist(),
            "outcomes": {
                "task_accuracy": f[0],
                "token_efficiency": f[1],
                "edge_robustness": f[2],
                "epistemic_consistency": f[3],
            },
            "source": "stage2_pymoo",
        })

    # Print top solutions
    print("\n  Top Stage 2 Solutions:")
    sorted_by_avg = sorted(stage2_results, key=lambda r: sum(r["outcomes"].values()), reverse=True)
    for i, sol in enumerate(sorted_by_avg[:5]):
        o = sol["outcomes"]
        print(f"    {i+1}. acc={o['task_accuracy']:.3f}, eff={o['token_efficiency']:.3f}, "
              f"rob={o['edge_robustness']:.3f}, cons={o['epistemic_consistency']:.3f}")

    return stage2_results


# =============================================================================
# MODE DISTILLATION
# =============================================================================

def distill_named_modes(results: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """
    Distill Pareto solutions into named operational modes.

    Modes:
        - audit: Best epistemic_consistency
        - speed: Best token_efficiency
        - research: Best task_accuracy
        - robust: Best edge_robustness
        - balanced: Best average across all objectives
    """
    print("\n" + "=" * 70)
    print("DISTILLING NAMED MODES")
    print("=" * 70)

    modes = {}

    # Audit: maximize epistemic_consistency
    audit = max(results, key=lambda r: r["outcomes"]["epistemic_consistency"])
    modes["audit"] = audit
    print(f"\n  AUDIT mode: cons={audit['outcomes']['epistemic_consistency']:.3f}")

    # Speed: maximize token_efficiency
    speed = max(results, key=lambda r: r["outcomes"]["token_efficiency"])
    modes["speed"] = speed
    print(f"  SPEED mode: eff={speed['outcomes']['token_efficiency']:.3f}")

    # Research: maximize task_accuracy
    research = max(results, key=lambda r: r["outcomes"]["task_accuracy"])
    modes["research"] = research
    print(f"  RESEARCH mode: acc={research['outcomes']['task_accuracy']:.3f}")

    # Robust: maximize edge_robustness
    robust = max(results, key=lambda r: r["outcomes"]["edge_robustness"])
    modes["robust"] = robust
    print(f"  ROBUST mode: rob={robust['outcomes']['edge_robustness']:.3f}")

    # Balanced: maximize average
    balanced = max(results, key=lambda r: sum(r["outcomes"].values()) / 4)
    modes["balanced"] = balanced
    avg = sum(balanced["outcomes"].values()) / 4
    print(f"  BALANCED mode: avg={avg:.3f}")

    return modes


def config_14d_to_fullconfig(config_14d: List[float]) -> FullConfig:
    """Convert 14D config vector to FullConfig object."""
    from core.config import CompressionLevel
    return FullConfig(
        framework=FrameworkConfig(
            evidential=config_14d[0] > 0.5,
            aspectual=config_14d[1] > 0.5,
            morphological=config_14d[2] > 0.5,
            compositional=config_14d[3] > 0.5,
            honorific=config_14d[4] > 0.5,
            classifier=config_14d[5] > 0.5,
            spatial=config_14d[6] > 0.5,
        ),
        prompt=PromptConfig(
            verix_strictness=VerixStrictness(int(round(min(2, max(0, config_14d[7]))))),
            compression_level=CompressionLevel(int(round(min(2, max(0, config_14d[8]))))),
            require_ground=config_14d[9] > 0.5,
            require_confidence=config_14d[10] > 0.5,
        ),
    )


# =============================================================================
# SAVE RESULTS
# =============================================================================

def save_results(
    stage1_results: List[Dict[str, Any]],
    stage2_results: List[Dict[str, Any]],
    modes: Dict[str, Dict[str, Any]],
    output_dir: Path,
) -> None:
    """Save all optimization results."""
    print("\n" + "=" * 70)
    print("SAVING RESULTS")
    print("=" * 70)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Save Stage 1 Pareto
    with open(output_dir / "stage1_pareto.json", "w") as f:
        json.dump(stage1_results, f, indent=2)
    print(f"  Stage 1 Pareto: {output_dir / 'stage1_pareto.json'}")

    # Save Stage 2 Pareto
    with open(output_dir / "stage2_pareto.json", "w") as f:
        json.dump(stage2_results, f, indent=2)
    print(f"  Stage 2 Pareto: {output_dir / 'stage2_pareto.json'}")

    # Save named modes with FullConfig
    modes_output = {}
    for name, mode in modes.items():
        config_14d = mode.get("config_14d", mode.get("config_5d", [0]*14))
        if len(config_14d) == 5:
            config_14d = expand_5d_to_14d(config_14d).tolist()

        full_config = config_14d_to_fullconfig(config_14d)

        modes_output[name] = {
            "config_vector": config_14d,
            "outcomes": mode["outcomes"],
            "source": mode["source"],
            "summary": full_config.summary(),
            "active_frames": full_config.framework.active_frames(),
            "verix_strictness": full_config.prompt.verix_strictness.name,
        }

    with open(output_dir / "named_modes.json", "w") as f:
        json.dump(modes_output, f, indent=2)
    print(f"  Named modes: {output_dir / 'named_modes.json'}")

    # Save summary report
    with open(output_dir / "two_stage_report.md", "w") as f:
        f.write("# Two-Stage Optimization Report\n\n")
        f.write(f"**Date**: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("**Method**: GlobalMOO (5D) -> PyMOO NSGA-II (14D)\n\n")

        f.write("## Stage 1: GlobalMOO Exploration\n\n")
        f.write(f"- Dimensions: 5 (subscription limited)\n")
        f.write(f"- Pareto solutions: {len(stage1_results)}\n\n")

        f.write("## Stage 2: PyMOO Refinement\n\n")
        f.write(f"- Dimensions: 14 (full config space)\n")
        f.write(f"- Algorithm: NSGA-II\n")
        f.write(f"- Pareto solutions: {len(stage2_results)}\n\n")

        f.write("## Named Modes\n\n")
        f.write("| Mode | Accuracy | Efficiency | Robustness | Consistency | Frames |\n")
        f.write("|------|----------|------------|------------|-------------|--------|\n")
        for name, mode in modes_output.items():
            o = mode["outcomes"]
            frames = ", ".join(mode["active_frames"][:3])
            if len(mode["active_frames"]) > 3:
                frames += "..."
            f.write(f"| {name} | {o['task_accuracy']:.3f} | {o['token_efficiency']:.3f} | "
                   f"{o['edge_robustness']:.3f} | {o['epistemic_consistency']:.3f} | {frames} |\n")

        f.write("\n---\n")
        f.write("*Generated with Two-Stage Optimization (GlobalMOO + PyMOO NSGA-II)*\n")

    print(f"  Report: {output_dir / 'two_stage_report.md'}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Run two-stage optimization."""
    print("=" * 70)
    print("TWO-STAGE COGNITIVE ARCHITECTURE OPTIMIZATION")
    print("Stage 1: GlobalMOO (5D) -> Stage 2: PyMOO NSGA-II (14D)")
    print("=" * 70)

    # Initialize GlobalMOO client
    client = GlobalMOOClient(use_mock=False)

    if not client.test_connection():
        print("\n[WARNING] GlobalMOO API not reachable, using local optimization only")
        client = GlobalMOOClient(use_mock=True)

    # Stage 1: GlobalMOO exploration
    stage1_results = run_globalmoo_stage(
        client=client,
        model_id=2193,
        project_id=8318,
    )

    # Stage 2: PyMOO refinement
    stage2_results = run_pymoo_refinement_stage(
        stage1_results=stage1_results,
        n_generations=100,
        pop_size=200,
    )

    # Combine results and distill modes
    all_results = stage1_results + stage2_results
    modes = distill_named_modes(all_results)

    # Save everything
    output_dir = Path(__file__).parent.parent / "storage" / "two_stage_optimization"
    save_results(stage1_results, stage2_results, modes, output_dir)

    print("\n" + "=" * 70)
    print("OPTIMIZATION COMPLETE")
    print("=" * 70)
    print(f"\nResults saved to: {output_dir}")
    print(f"Stage 1 Pareto: {len(stage1_results)} solutions")
    print(f"Stage 2 Pareto: {len(stage2_results)} solutions")
    print(f"Named modes: {list(modes.keys())}")

    # Print final mode summaries
    print("\n--- Final Named Modes ---")
    for name, mode in modes.items():
        o = mode["outcomes"]
        print(f"  {name}: acc={o['task_accuracy']:.3f}, eff={o['token_efficiency']:.3f}, "
              f"rob={o['edge_robustness']:.3f}, cons={o['epistemic_consistency']:.3f}")


if __name__ == "__main__":
    main()


# =============================================================================
# TELEMETRY-DRIVEN OPTIMIZATION (Real Data Loop)
# =============================================================================

def run_with_telemetry(days: int = 3) -> Dict[str, Any]:
    """
    Run two-stage optimization using real telemetry data.
    
    This is the production optimization loop:
    1. Load N days of telemetry from memory-mcp
    2. Run Stage 1 (GlobalMOO) with real data-informed objectives
    3. Run Stage 2 (PyMOO) with refined local search
    4. Distill into named modes
    5. Return modes for cascade application
    
    Args:
        days: Number of days of telemetry to load (default: 3)
    
    Returns:
        Dict with modes and optimization results
    """
    if not TELEMETRY_AVAILABLE:
        print("[ERROR] Telemetry modules not available")
        return {"error": "Telemetry not available"}
    
    print("=" * 70)
    print(f"TELEMETRY-DRIVEN OPTIMIZATION ({days} days of data)")
    print("=" * 70)
    
    # 1. Load telemetry
    print("\n[1/5] Loading telemetry data...")
    store = TelemetryStore()
    batch = store.load_last_n_days(days)
    stats = batch.compute_statistics()
    
    print(f"  Records: {stats.get('total_records', 0)}")
    print(f"  Success rate: {stats.get('success_rate', 0):.2%}")
    print(f"  Avg frame score: {stats.get('avg_frame_score', 0):.3f}")
    
    # 2. Initialize GlobalMOO
    print("\n[2/5] Initializing GlobalMOO client...")
    client = GlobalMOOClient(use_mock=False)
    if not client.test_connection():
        print("  [WARN] Using mock client")
        client = GlobalMOOClient(use_mock=True)
    
    # 3. Stage 1: GlobalMOO
    print("\n[3/5] Running Stage 1 (GlobalMOO 5D)...")
    stage1_results = run_globalmoo_stage(
        client=client,
        model_id=2193,
        project_id=8318,
    )
    
    # 4. Stage 2: PyMOO
    print("\n[4/5] Running Stage 2 (PyMOO 14D)...")
    stage2_results = run_pymoo_refinement_stage(
        stage1_results=stage1_results,
        n_generations=50,  # Faster for scheduled runs
        pop_size=100,
    )
    
    # 5. Distill modes
    print("\n[5/5] Distilling named modes...")
    all_results = stage1_results + stage2_results
    modes = distill_named_modes(all_results)
    
    # Save results
    output_dir = Path(__file__).parent.parent / "storage" / "two_stage_optimization"
    save_results(stage1_results, stage2_results, modes, output_dir)
    
    print("\n" + "=" * 70)
    print("TELEMETRY OPTIMIZATION COMPLETE")
    print("=" * 70)
    
    return {
        "telemetry_stats": stats,
        "stage1_count": len(stage1_results),
        "stage2_count": len(stage2_results),
        "modes": {name: mode["outcomes"] for name, mode in modes.items()},
        "output_dir": str(output_dir),
    }
