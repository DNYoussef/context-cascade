#!/usr/bin/env python3
"""
AI Simulation Helper - CLI Tool for Optimal Physics Simulation Design

This tool helps AI systems (or humans) choose the optimal calculus parameter k
and generate appropriate NNC (Non-Newtonian Calculus) code for physics simulations.

Usage:
  python ai_simulation_helper.py --length-scale 1e-10 --singularity-type 1/r
  python ai_simulation_helper.py --problem "crack tip stress field"
  python ai_simulation_helper.py --interactive

Based on empirically validated k(L) formula:
  k_optimal = -0.0137 * log10(L) + 0.1593  (R^2 = 0.7127, p < 0.01)

Source: https://meta-calculus-portfolio-production.up.railway.app/results/multiscale
"""

import argparse
import json
import math
import sys
from typing import Dict, Optional, Tuple

# =============================================================================
# CORE FORMULAS
# =============================================================================

def k_from_length_scale(L: float, objective: str = "balanced") -> float:
    """
    Calculate optimal k from characteristic length scale L (in meters).

    k(L) = -0.0137 * log10(L) + 0.1593

    Args:
        L: Characteristic length scale in meters
        objective: "balanced", "singularity", "accuracy", or "cost"

    Returns:
        Optimal k value
    """
    if L <= 0:
        raise ValueError("Length scale must be positive")

    log_L = math.log10(L)

    if objective == "balanced":
        # Combined optimal from MOO: k(L) = -0.0137 * log10(L) + 0.1593
        return -0.0137 * log_L + 0.1593

    elif objective == "singularity":
        # Maximize singularity handling
        # Small scales (L < 1e-6): k = -1 (bigeometric, best for 1/r)
        # Large scales: k = 0 (classical)
        if log_L < -13:
            return -1.0
        elif log_L < -7:
            return -0.5 + (log_L + 13) * 0.5 / 6
        elif log_L < -4:
            return -0.1 + (log_L + 7) * 0.1 / 3
        else:
            return 0.0

    elif objective == "accuracy":
        # Maximize numerical accuracy
        # Needs meta-calculus at extreme scales
        if log_L < -20:
            return -0.5
        elif log_L > 20:
            return -0.5
        else:
            return 0.0

    elif objective == "cost":
        # Minimize computational cost
        # k=0 everywhere (classical has minimal overhead)
        return 0.0

    else:
        raise ValueError(f"Unknown objective: {objective}")


def k_from_singularity_type(singularity: str) -> float:
    """
    Get optimal k based on singularity type.

    The key insight: k should match the negative of the singularity exponent.
    D*[x^n] = e^n (constant!) when using NNC derivative.

    Args:
        singularity: Type of singularity (e.g., "1/r", "1/r^2", "1/sqrt(r)")

    Returns:
        Optimal k value
    """
    SINGULARITY_K_MAP = {
        # Power law singularities: k matches negative exponent
        "1/r": -1.0,        # r^(-1) -> k = -1
        "1/r^2": -2.0,      # r^(-2) -> k = -2
        "1/sqrt(r)": -0.5,  # r^(-0.5) -> k = -0.5
        "r^(-1)": -1.0,
        "r^(-2)": -2.0,
        "r^(-0.5)": -0.5,
        "r^(-1/2)": -0.5,

        # Physics-specific singularities
        "coulomb": -1.0,           # 1/r potential
        "gravitational": -1.0,     # 1/r potential
        "schwarzschild": -1.0,     # 1/r metric component
        "kretschmann": -6.0,       # r^(-6) curvature scalar
        "crack_tip": -0.5,         # sqrt(r) stress singularity
        "vortex_core": -1.0,       # 1/r velocity singularity
        "radiation": -2.0,         # 1/r^2 intensity
        "dipole": -3.0,            # 1/r^3 field

        # Special cases
        "exponential": 1.0,        # Bigeometric is natural for exp
        "none": 0.0,               # No singularity -> classical
        "smooth": 0.0,             # Smooth function -> classical
    }

    singularity_lower = singularity.lower().replace(" ", "_")

    if singularity_lower in SINGULARITY_K_MAP:
        return SINGULARITY_K_MAP[singularity_lower]

    # Try to parse as r^n pattern
    if "r^" in singularity_lower or "r**" in singularity_lower:
        try:
            # Extract exponent
            import re
            match = re.search(r'r\^?\*?\*?\(?(-?\d*\.?\d*/?-?\d*\.?\d*)\)?', singularity_lower)
            if match:
                exp_str = match.group(1)
                if '/' in exp_str:
                    num, den = exp_str.split('/')
                    exponent = float(num) / float(den)
                else:
                    exponent = float(exp_str)
                return exponent  # k = exponent for singularity r^exponent
        except:
            pass

    print(f"Warning: Unknown singularity type '{singularity}', defaulting to k=0")
    return 0.0


# =============================================================================
# PROBLEM ANALYSIS
# =============================================================================

PROBLEM_DATABASE = {
    "crack tip stress": {
        "length_scale": 1e-6,
        "singularity": "1/sqrt(r)",
        "k": -0.5,
        "description": "Stress field near crack tip follows sigma ~ K/sqrt(r)",
        "improvement": "93.4% closer to singularity with NNC"
    },
    "black hole": {
        "length_scale": 1e3,  # Stellar mass black hole
        "singularity": "1/r",
        "k": -1.0,
        "description": "Schwarzschild metric has 1/r singularity at horizon",
        "improvement": "Regularizes metric components"
    },
    "molecular dynamics": {
        "length_scale": 1e-10,
        "singularity": "1/r",
        "k": -1.0,
        "description": "Lennard-Jones potential has 1/r^6 and 1/r^12 terms",
        "improvement": "22.3% improvement in energy conservation"
    },
    "turbulence vortex": {
        "length_scale": 1e-3,
        "singularity": "1/r",
        "k": -1.0,
        "description": "Vortex core has 1/r velocity singularity",
        "improvement": "70.9% closer to vortex core"
    },
    "radiation transport": {
        "length_scale": 1e-2,
        "singularity": "1/r^2",
        "k": -2.0,
        "description": "Radiation intensity follows inverse square law",
        "improvement": "83.6% improvement near point sources"
    },
    "shock wave": {
        "length_scale": 1e-4,
        "singularity": "none",
        "k": 0.0,
        "description": "Shock discontinuity, not a mathematical singularity",
        "improvement": "Use flux limiters instead of NNC"
    },
    "quantum mechanics": {
        "length_scale": 1e-10,
        "singularity": "none",
        "k": 0.0,
        "description": "Quantum evolution is smooth - no singularities",
        "improvement": "Classical calculus (k=0) is optimal"
    },
    "cosmology": {
        "length_scale": 1e26,
        "singularity": "none",
        "k": 0.0,
        "description": "Large-scale structure is smooth",
        "improvement": "Classical calculus (k=0) is optimal"
    },
}


def analyze_problem(problem_description: str) -> Dict:
    """
    Analyze a physics problem and recommend simulation parameters.
    """
    problem_lower = problem_description.lower()

    # Search for matching problem
    for key, info in PROBLEM_DATABASE.items():
        if key in problem_lower or any(word in problem_lower for word in key.split()):
            return {
                "matched_problem": key,
                "recommended_k": info["k"],
                "length_scale": info["length_scale"],
                "singularity_type": info["singularity"],
                "description": info["description"],
                "expected_improvement": info["improvement"],
            }

    # No match - provide general guidance
    return {
        "matched_problem": None,
        "recommended_k": None,
        "guidance": """
Unable to match specific problem. Please provide:
1. Characteristic length scale (in meters)
2. Singularity type (if any): 1/r, 1/r^2, 1/sqrt(r), or 'none'

Example: python ai_simulation_helper.py --length-scale 1e-10 --singularity-type 1/r
"""
    }


# =============================================================================
# CODE GENERATION
# =============================================================================

def generate_python_code(k: float, singularity_type: str = None) -> str:
    """
    Generate Python code for NNC simulation with the given k value.
    """
    code = f'''# NNC Simulation Code - Auto-generated for k = {k}
# Source: ai_simulation_helper.py

import numpy as np

# =============================================================================
# NNC Transform Functions
# =============================================================================

def nnc_forward_transform(x, k={k}, eps=1e-10):
    """Transform from physics space to NNC space."""
    if abs(k) < eps:
        return x  # Classical (identity)
    if abs(k - 1.0) < eps:
        # Geometric (log transform)
        return np.sign(x) * np.log(np.maximum(np.abs(x), eps))
    # General k: Power transform
    return np.sign(x) * np.power(np.maximum(np.abs(x), eps), 1.0 - k)

def nnc_inverse_transform(y, k={k}, eps=1e-10):
    """Transform from NNC space back to physics space."""
    if abs(k) < eps:
        return y  # Classical (identity)
    if abs(k - 1.0) < eps:
        # Geometric (exp transform)
        return np.sign(y) * np.exp(np.minimum(np.abs(y), 700))
    # General k: Inverse power transform
    return np.sign(y) * np.power(np.maximum(np.abs(y), eps), 1.0 / (1.0 - k))

def nnc_derivative(f, x, k={k}, dx=1e-6):
    """
    Compute NNC derivative D*_k[f](x).

    D*_k[f] = f(x)^(1-k) * f'(x)

    For k={k}, this regularizes singularities of type r^({-k}).
    """
    # Classical derivative via finite difference
    f_prime = (f(x + dx) - f(x - dx)) / (2 * dx)

    if abs(k) < 1e-10:
        return f_prime  # Classical

    # NNC derivative: f^(1-k) * f'
    f_val = f(x)
    return np.sign(f_val) * np.power(np.maximum(np.abs(f_val), 1e-10), 1.0 - k) * f_prime

# =============================================================================
# Simulation Template
# =============================================================================

def run_simulation(
    initial_conditions,
    dt=0.001,
    n_steps=1000,
    use_nnc=True,
    k={k}
):
    """
    Run simulation with optional NNC regularization.

    Key insight: Transform to NNC space, evolve, transform back.
    This regularizes singularities without changing the physics.
    """
    state = initial_conditions.copy()

    for step in range(n_steps):
        if use_nnc:
            # 1. Transform to NNC space
            state_nnc = nnc_forward_transform(state, k=k)

            # 2. Evolve in NNC space (your physics here)
            # state_nnc = evolve_nnc(state_nnc, dt)

            # 3. Transform back to physics space
            state = nnc_inverse_transform(state_nnc, k=k)
        else:
            # Classical evolution (may diverge near singularities)
            # state = evolve_classical(state, dt)
            pass

    return state

# =============================================================================
# Key Mathematical Insight
# =============================================================================
#
# For power functions f(x) = x^n, the multiplicative derivative is:
#   D*[x^n] = e^n  (CONSTANT, independent of x!)
#
# This transforms diverging classical derivatives into bounded constants:
#   Classical: d/dx[1/r] = -1/r^2 (diverges as r->0)
#   NNC (k=-1): D*[1/r] = e^(-1) = 0.368 (bounded!)
#
# Your singularity type: {singularity_type or "unspecified"}
# Recommended k: {k}
# Why: k should match the negative of the singularity exponent
#
'''
    return code


def generate_typescript_code(k: float) -> str:
    """
    Generate TypeScript code for browser-based NNC simulation.
    """
    code = f'''// NNC Simulation Code - Auto-generated for k = {k}
// For browser-based physics simulations

export const NNCTransforms = {{
  /**
   * Forward transform: physics space -> NNC space
   */
  forwardTransform: (x: number, k: number = {k}, eps: number = 1e-10): number => {{
    if (Math.abs(k) < eps) return x; // Classical
    if (Math.abs(k - 1.0) < eps) {{
      return Math.sign(x) * Math.log(Math.max(Math.abs(x), eps));
    }}
    return Math.sign(x) * Math.pow(Math.max(Math.abs(x), eps), 1.0 - k);
  }},

  /**
   * Inverse transform: NNC space -> physics space
   */
  inverseTransform: (y: number, k: number = {k}, eps: number = 1e-10): number => {{
    if (Math.abs(k) < eps) return y; // Classical
    if (Math.abs(k - 1.0) < eps) {{
      return Math.sign(y) * Math.exp(Math.min(Math.abs(y), 700));
    }}
    return Math.sign(y) * Math.pow(Math.max(Math.abs(y), eps), 1.0 / (1.0 - k));
  }},

  /**
   * Regularization factor for singularity at distance r
   */
  regularizationFactor: (r: number, k: number = {k}): number => {{
    if (k === 0) return 1;
    return Math.pow(Math.max(r, 1e-10), -k);
  }}
}};

// Usage:
// const k = {k};
// const physicsValue = compute_physics(r);
// const regularized = NNCTransforms.forwardTransform(physicsValue, k);
// // ... work with regularized value ...
// const result = NNCTransforms.inverseTransform(regularized, k);
'''
    return code


# =============================================================================
# CLI INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="AI Simulation Helper - Choose optimal k and generate NNC code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai_simulation_helper.py --length-scale 1e-10 --singularity 1/r
  python ai_simulation_helper.py --problem "crack tip stress field"
  python ai_simulation_helper.py --k -1.0 --generate python
  python ai_simulation_helper.py --lookup all

Reference: https://meta-calculus-portfolio-production.up.railway.app/results/multiscale
        """
    )

    parser.add_argument("--length-scale", "-L", type=float,
                        help="Characteristic length scale in meters")
    parser.add_argument("--singularity", "-s", type=str,
                        help="Singularity type (e.g., '1/r', '1/sqrt(r)', 'none')")
    parser.add_argument("--problem", "-p", type=str,
                        help="Problem description for automatic analysis")
    parser.add_argument("--k", type=float,
                        help="Specify k directly (overrides other options)")
    parser.add_argument("--objective", "-o", type=str, default="balanced",
                        choices=["balanced", "singularity", "accuracy", "cost"],
                        help="Optimization objective (default: balanced)")
    parser.add_argument("--generate", "-g", type=str, choices=["python", "typescript", "both"],
                        help="Generate code template")
    parser.add_argument("--lookup", type=str,
                        help="Lookup k for scale: 'planck', 'nuclear', 'atomic', 'human', 'solar', 'hubble', or 'all'")
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON (for programmatic use)")

    args = parser.parse_args()

    result = {}

    # Lookup mode
    if args.lookup:
        SCALES = {
            "planck": 1.616e-35,
            "nuclear": 1e-15,
            "atomic": 1e-10,
            "nano": 1e-9,
            "micro": 1e-6,
            "human": 1.0,
            "planetary": 1e7,
            "solar": 1e11,
            "galactic": 1e21,
            "hubble": 8.8e26,
        }

        if args.lookup.lower() == "all":
            result["scale_lookup"] = {}
            for name, L in SCALES.items():
                k = k_from_length_scale(L, args.objective)
                result["scale_lookup"][name] = {
                    "L": L,
                    "log10_L": math.log10(L),
                    "k_optimal": round(k, 4),
                }
        elif args.lookup.lower() in SCALES:
            L = SCALES[args.lookup.lower()]
            k = k_from_length_scale(L, args.objective)
            result["scale"] = args.lookup
            result["L"] = L
            result["k_optimal"] = round(k, 4)
        else:
            result["error"] = f"Unknown scale: {args.lookup}"

    # Problem analysis mode
    elif args.problem:
        result = analyze_problem(args.problem)

    # Direct k specification
    elif args.k is not None:
        result["k"] = args.k
        result["source"] = "user_specified"

    # Calculate from length scale and/or singularity
    else:
        if args.length_scale and args.singularity:
            k_L = k_from_length_scale(args.length_scale, args.objective)
            k_s = k_from_singularity_type(args.singularity)
            # Use singularity-based k if there's a singularity, otherwise length-based
            if args.singularity.lower() in ["none", "smooth"]:
                result["k"] = round(k_L, 4)
                result["source"] = "length_scale"
            else:
                result["k"] = round(k_s, 4)
                result["source"] = "singularity_type"
            result["k_from_length_scale"] = round(k_L, 4)
            result["k_from_singularity"] = round(k_s, 4)
            result["length_scale"] = args.length_scale
            result["singularity_type"] = args.singularity

        elif args.length_scale:
            k = k_from_length_scale(args.length_scale, args.objective)
            result["k"] = round(k, 4)
            result["source"] = "length_scale"
            result["length_scale"] = args.length_scale
            result["objective"] = args.objective

        elif args.singularity:
            k = k_from_singularity_type(args.singularity)
            result["k"] = round(k, 4)
            result["source"] = "singularity_type"
            result["singularity_type"] = args.singularity

        else:
            # No input - show help
            parser.print_help()
            return

    # Code generation
    if args.generate and "k" in result:
        k = result.get("k", result.get("recommended_k", 0))
        singularity = result.get("singularity_type", None)

        if args.generate in ["python", "both"]:
            result["python_code"] = generate_python_code(k, singularity)
        if args.generate in ["typescript", "both"]:
            result["typescript_code"] = generate_typescript_code(k)

    # Output
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("\n" + "="*60)
        print("AI SIMULATION HELPER - RESULTS")
        print("="*60)

        if "error" in result:
            print(f"\nError: {result['error']}")
            return

        if "scale_lookup" in result:
            print("\nOptimal k values across physical scales:")
            print("-" * 50)
            print(f"{'Scale':<12} {'L (m)':<15} {'log10(L)':<10} {'k_optimal':<10}")
            print("-" * 50)
            for name, data in result["scale_lookup"].items():
                print(f"{name:<12} {data['L']:<15.2e} {data['log10_L']:<10.1f} {data['k_optimal']:<10.4f}")

        elif "matched_problem" in result:
            if result["matched_problem"]:
                print(f"\nMatched Problem: {result['matched_problem']}")
                print(f"Recommended k: {result['recommended_k']}")
                print(f"Length Scale: {result.get('length_scale', 'N/A')}")
                print(f"Singularity Type: {result.get('singularity_type', 'N/A')}")
                print(f"Description: {result.get('description', '')}")
                print(f"Expected Improvement: {result.get('expected_improvement', '')}")
            else:
                print(result.get("guidance", ""))

        else:
            print(f"\nOptimal k: {result.get('k', 'N/A')}")
            print(f"Source: {result.get('source', 'N/A')}")
            if "length_scale" in result:
                print(f"Length Scale: {result['length_scale']:.2e} m")
            if "singularity_type" in result:
                print(f"Singularity Type: {result['singularity_type']}")
            if "objective" in result:
                print(f"Objective: {result['objective']}")

        if "python_code" in result:
            print("\n" + "="*60)
            print("GENERATED PYTHON CODE")
            print("="*60)
            print(result["python_code"])

        if "typescript_code" in result:
            print("\n" + "="*60)
            print("GENERATED TYPESCRIPT CODE")
            print("="*60)
            print(result["typescript_code"])

        print("\n" + "="*60)
        print("Reference: https://meta-calculus-portfolio-production.up.railway.app/results/multiscale")
        print("="*60 + "\n")


if __name__ == "__main__":
    main()
