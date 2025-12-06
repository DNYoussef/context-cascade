"""
meta_calculus/quantum/meta_quantum_compatibility.py

Meta-Quantum Compatibility Explorer

This module implements a small, self-contained test bench for
meta-time Schrodinger equations, mirroring the cosmology meta-Friedmann
simulations featured on the Simulator and Results pages.

It:

    - Builds a random finite-dimensional quantum system (4x4 Hermitian H),
    - Evolves an initial state under:
        * Standard Schrodinger dynamics
        * Several meta-derivative variants in time
    - Measures:
        * Norm drift (||psi||^2 should stay 1 in standard QM)
        * Deviation from the standard trajectory

The output is a dictionary of metrics suitable for:

    - A "Meta-Quantum Compatibility" section on the Simulator page
    - A compact summary on the Meta-Quantum chapter page

Usage:
    from meta_calculus.quantum import run_meta_quantum_experiment

    metrics = run_meta_quantum_experiment(dim=4, t_final=10.0, num_steps=2000)
"""

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

import numpy as np


# ---------------------------------------------------------------------------
# 1. Utilities: random Hermitian H and RK4 integrator
# ---------------------------------------------------------------------------

def random_hermitian(dim: int, seed: Optional[int] = None) -> np.ndarray:
    """Generate a random Hermitian matrix."""
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    H = 0.5 * (A + A.conj().T)
    return H


def random_state(dim: int, seed: Optional[int] = None) -> np.ndarray:
    """Generate a random normalized quantum state."""
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(dim,)) + 1j * rng.normal(size=(dim,))
    v /= np.linalg.norm(v)
    return v


def rk4_step(
    rhs: Callable[[float, np.ndarray], np.ndarray],
    t: float,
    psi: np.ndarray,
    dt: float,
) -> np.ndarray:
    """Classical RK4 step for complex state psi."""
    k1 = rhs(t, psi)
    k2 = rhs(t + 0.5 * dt, psi + 0.5 * dt * k1)
    k3 = rhs(t + 0.5 * dt, psi + 0.5 * dt * k2)
    k4 = rhs(t + dt, psi + dt * k3)
    return psi + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)


# ---------------------------------------------------------------------------
# 2. Meta-derivative families (in time)
# ---------------------------------------------------------------------------

@dataclass
class MetaDerivativeConfig:
    """
    Encodes one family of meta-time derivatives.

    Each family defines a modified RHS for the Schrodinger equation:

        i hbar D_t^{(meta)} psi = H psi

    which we rewrite as an ODE:

        dpsi/dt = F(t, psi).

    The families are chosen to match the "safe" and "breaking" classes
    discussed in the meta-quantum analysis.

    Families:
        - "standard":        Classical Schrodinger (reference)
        - "safe_u":          D_t = (1/u(t)) d/dt  (clock reparametrization)
        - "global_norm":     D_t = (1/u(t))(1 + k||psi||^2) d/dt
        - "log_component":   D_t^{log} psi_j = (1/u(t))(1/psi_j) dpsi_j/dt
        - "power_component": D_t psi_j = (1/u(t))|psi_j|^p dpsi_j/dt
        - "component_k":     D_t psi_j = (1/u(t))(1 + k|psi_j|^2) dpsi_j/dt
    """
    name: str
    kind: str  # "standard", "safe_u", "global_norm", "log_component", "power_component", "component_k"
    params: Dict = field(default_factory=dict)

    # Classification
    level: str = "Q0"  # Q0=classical, Q1=safe clock, Q2=global, Q3=componentwise
    safe: bool = True


# Predefined meta-derivative configurations matching the compatibility hierarchy
DEFAULT_CONFIGS: List[MetaDerivativeConfig] = [
    MetaDerivativeConfig(
        name="Standard Schrodinger",
        kind="standard",
        params={},
        level="Q0",
        safe=True,
    ),
    MetaDerivativeConfig(
        name="Safe Clock (u(t))",
        kind="safe_u",
        params={},
        level="Q1",
        safe=True,
    ),
    MetaDerivativeConfig(
        name="Global Norm (k=0.5)",
        kind="global_norm",
        params={"k": 0.5},
        level="Q2",
        safe=True,
    ),
    MetaDerivativeConfig(
        name="Log Component",
        kind="log_component",
        params={},
        level="Q3",
        safe=False,
    ),
    MetaDerivativeConfig(
        name="Power Component (p=1)",
        kind="power_component",
        params={"p": 1.0},
        level="Q3",
        safe=False,
    ),
    MetaDerivativeConfig(
        name="Componentwise k=0.5",
        kind="component_k",
        params={"k": 0.5},
        level="Q3",
        safe=False,
    ),
]


def make_default_u() -> Callable[[float], float]:
    """Default gently oscillating positive time-weight."""
    def u(t: float) -> float:
        return 1.0 + 0.3 * np.sin(0.7 * t) * np.cos(0.3 * t)
    return u


def make_meta_rhs(
    H: np.ndarray,
    config: MetaDerivativeConfig,
    hbar: float = 1.0,
) -> Callable[[float, np.ndarray], np.ndarray]:
    """
    Build the RHS f(t, psi) = dpsi/dt for a given meta-derivative family.

    The baselines are:

        Standard Schrodinger:
            dpsi/dt = -i H psi / hbar

        Meta families transform this based on the derivative structure.
    """
    # For all families, we'll use the same u(t) unless overridden
    u = config.params.get("u", None)
    if u is None:
        u = make_default_u()

    kind = config.kind
    eps = 1e-10

    if kind == "standard":
        # Reference RHS
        def rhs(t: float, psi: np.ndarray) -> np.ndarray:
            return -1j * H @ psi / hbar
        return rhs

    if kind == "safe_u":
        # D_t psi = (1/u(t)) dpsi/dt => dpsi/dt = -i u(t) H psi / hbar
        def rhs(t: float, psi: np.ndarray) -> np.ndarray:
            return -1j * u(t) * (H @ psi) / hbar
        return rhs

    if kind == "global_norm":
        # D_t psi = (1/u(t)) (1 + k ||psi||^2) dpsi/dt
        # => dpsi/dt = -i u(t) H psi / [hbar (1 + k ||psi||^2)]
        k = config.params.get("k", 0.5)

        def rhs(t: float, psi: np.ndarray) -> np.ndarray:
            norm_sq = float(np.vdot(psi, psi).real)
            denom = 1.0 + k * norm_sq
            return -1j * u(t) * (H @ psi) / (hbar * denom)
        return rhs

    if kind == "log_component":
        # Component-wise "log-like" derivative:
        #   D_t psi_j = (1/u(t)) (1/psi_j) dpsi_j/dt
        # => dpsi_j/dt = -i u(t) psi_j (Hpsi)_j / hbar
        def rhs(t: float, psi: np.ndarray) -> np.ndarray:
            Hp = H @ psi
            return -1j * u(t) * psi * Hp / hbar
        return rhs

    if kind == "power_component":
        # D_t psi_j = (1/u(t)) |psi_j|^p dpsi_j/dt
        # => dpsi_j/dt = -i u(t) (Hpsi)_j / (hbar |psi_j|^p)
        p = config.params.get("p", 1.0)

        def rhs(t: float, psi: np.ndarray) -> np.ndarray:
            Hp = H @ psi
            mag = np.abs(psi) + eps
            return -1j * u(t) * Hp / (hbar * mag**p)
        return rhs

    if kind == "component_k":
        # D_t psi_j = (1/u(t)) (1 + k |psi_j|^2) dpsi_j/dt
        # => dpsi_j/dt = -i u(t) (Hpsi)_j / (hbar (1 + k |psi_j|^2))
        k = config.params.get("k", 0.5)

        def rhs(t: float, psi: np.ndarray) -> np.ndarray:
            Hp = H @ psi
            mag2 = np.abs(psi)**2
            denom = 1.0 + k * mag2
            return -1j * u(t) * Hp / (hbar * denom)
        return rhs

    raise ValueError(f"Unknown meta-derivative kind: {kind}")


# ---------------------------------------------------------------------------
# 3. Core experiment: compare families vs standard Schrodinger
# ---------------------------------------------------------------------------

@dataclass
class QuantumCompatibilityResult:
    """Results from a single meta-derivative family run."""
    name: str
    kind: str
    level: str
    safe: bool
    max_norm_drift: float
    mean_norm_drift: float
    final_norm_drift: float
    max_distance_to_standard: float
    mean_distance_to_standard: float
    final_distance_to_standard: float
    trajectory: Optional[np.ndarray] = None
    norms: Optional[np.ndarray] = None


def run_meta_quantum_experiment(
    dim: int = 4,
    t_final: float = 10.0,
    num_steps: int = 2000,
    configs: Optional[List[MetaDerivativeConfig]] = None,
    seed: Optional[int] = 0,
    store_trajectories: bool = False,
) -> Dict[str, Dict[str, float]]:
    """
    Run the meta-quantum compatibility experiment.

    Parameters
    ----------
    dim : int
        Dimension of the Hilbert space (default: 4).
    t_final : float
        Final physical time.
    num_steps : int
        Number of RK4 steps.
    configs : list of MetaDerivativeConfig, optional
        Meta-derivative families to test. If None, uses DEFAULT_CONFIGS.
    seed : int, optional
        Random seed.
    store_trajectories : bool
        Whether to store full trajectories in results (memory intensive).

    Returns
    -------
    metrics : dict
        Dictionary keyed by family name with:

        {
          'max_norm_drift': float,
          'mean_norm_drift': float,
          'final_norm_drift': float,
          'max_distance_to_standard': float,
          'mean_distance_to_standard': float,
          'final_distance_to_standard': float,
          'level': str,
          'safe': bool,
        }

    These can be plotted as bar charts / heatmaps in the Simulator.
    """
    if configs is None:
        configs = DEFAULT_CONFIGS

    H = random_hermitian(dim, seed=seed)
    psi0 = random_state(dim, seed=seed + 1 if seed is not None else None)

    dt = t_final / num_steps

    # First: compute the standard Schrodinger reference trajectory
    std_config = MetaDerivativeConfig(name="standard", kind="standard", params={})
    std_rhs = make_meta_rhs(H, std_config)
    psi_std = psi0.copy()

    std_traj = [psi_std.copy()]
    for n in range(num_steps):
        t = n * dt
        psi_std = rk4_step(std_rhs, t, psi_std, dt)
        std_traj.append(psi_std.copy())
    std_traj = np.stack(std_traj, axis=0)  # (T+1, dim)

    metrics: Dict[str, Dict[str, float]] = {}

    for cfg in configs:
        rhs = make_meta_rhs(H, cfg)
        psi = psi0.copy()
        traj = [psi.copy()]
        for n in range(num_steps):
            t = n * dt
            psi = rk4_step(rhs, t, psi, dt)
            traj.append(psi.copy())
        traj = np.stack(traj, axis=0)
        norms = np.linalg.norm(traj, axis=1)

        # Norm drift from initial
        norm_drift = np.abs(norms - norms[0])
        max_norm_drift = float(np.max(norm_drift))
        mean_norm_drift = float(np.mean(norm_drift))
        final_norm_drift = float(norm_drift[-1])

        # Distance to standard trajectory
        diff = traj - std_traj
        dists = np.linalg.norm(diff, axis=1)
        max_dist = float(np.max(dists))
        mean_dist = float(np.mean(dists))
        final_dist = float(dists[-1])

        metrics[cfg.name] = {
            "max_norm_drift": max_norm_drift,
            "mean_norm_drift": mean_norm_drift,
            "final_norm_drift": final_norm_drift,
            "max_distance_to_standard": max_dist,
            "mean_distance_to_standard": mean_dist,
            "final_distance_to_standard": final_dist,
            "level": cfg.level,
            "safe": cfg.safe,
        }

    return metrics


def run_detailed_experiment(
    dim: int = 4,
    t_final: float = 10.0,
    num_steps: int = 2000,
    seed: Optional[int] = 0,
) -> List[QuantumCompatibilityResult]:
    """
    Run experiment with full result objects including trajectories.

    Returns list of QuantumCompatibilityResult objects for detailed analysis.
    """
    configs = DEFAULT_CONFIGS
    H = random_hermitian(dim, seed=seed)
    psi0 = random_state(dim, seed=seed + 1 if seed is not None else None)
    dt = t_final / num_steps

    # Standard reference
    std_config = MetaDerivativeConfig(name="standard", kind="standard", params={})
    std_rhs = make_meta_rhs(H, std_config)
    psi_std = psi0.copy()
    std_traj = [psi_std.copy()]
    for n in range(num_steps):
        t = n * dt
        psi_std = rk4_step(std_rhs, t, psi_std, dt)
        std_traj.append(psi_std.copy())
    std_traj = np.stack(std_traj, axis=0)

    results = []
    for cfg in configs:
        rhs = make_meta_rhs(H, cfg)
        psi = psi0.copy()
        traj = [psi.copy()]
        for n in range(num_steps):
            t = n * dt
            psi = rk4_step(rhs, t, psi, dt)
            traj.append(psi.copy())
        traj = np.stack(traj, axis=0)
        norms = np.linalg.norm(traj, axis=1)

        norm_drift = np.abs(norms - norms[0])
        diff = traj - std_traj
        dists = np.linalg.norm(diff, axis=1)

        results.append(QuantumCompatibilityResult(
            name=cfg.name,
            kind=cfg.kind,
            level=cfg.level,
            safe=cfg.safe,
            max_norm_drift=float(np.max(norm_drift)),
            mean_norm_drift=float(np.mean(norm_drift)),
            final_norm_drift=float(norm_drift[-1]),
            max_distance_to_standard=float(np.max(dists)),
            mean_distance_to_standard=float(np.mean(dists)),
            final_distance_to_standard=float(dists[-1]),
            trajectory=traj,
            norms=norms,
        ))

    return results


def print_compatibility_summary(metrics: Dict[str, Dict[str, float]]) -> None:
    """Print a formatted summary of quantum compatibility results."""
    print("=" * 70)
    print("META-QUANTUM COMPATIBILITY RESULTS")
    print("=" * 70)
    print()
    print(f"{'Family':<25} {'Level':<6} {'Safe':<6} {'Max Norm Drift':<15} {'Max Dist':<12}")
    print("-" * 70)

    for name, m in metrics.items():
        safe_str = "Yes" if m.get("safe", True) else "NO"
        level = m.get("level", "?")
        print(f"{name:<25} {level:<6} {safe_str:<6} {m['max_norm_drift']:<15.6f} {m['max_distance_to_standard']:<12.6f}")

    print("=" * 70)


if __name__ == "__main__":
    metrics = run_meta_quantum_experiment()
    print_compatibility_summary(metrics)
