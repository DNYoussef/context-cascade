"""
meta_calculus/quantum/quantum_objectives.py

Quantum Objective Functions for GlobalMOO + pymoo

This module wraps the quantum simulations in a multi-objective style
analogous to the cosmology + GlobalMOO/pymoo interface:

    1) Meta-Quantum Compatibility (meta-time Schrodinger):
       - Objectives: minimize norm drift, minimize distance to standard QM,
         and optionally penalize meta-derivative complexity.

    2) Multi-Calculus State-Space Diffusion (Δ² / diagonal qutrits):
       - Objectives: maximize cluster preservation, control entropy (not too
         mixed, not too sharp), and minimize sensitivity to calculus choice.

The design is:

    - "GlobalMOO-style" objective wrappers:
        * return a dict with named scalar objectives
        * easy to serialize to JSON and send to GlobalMOO

    - "pymoo-style" Problem classes:
        * expose vector-valued f(x) suitable for pymoo algorithms

Usage:
    # GlobalMOO style
    payload = meta_quantum_globalmoo_objective(x)

    # pymoo style
    from meta_calculus.quantum.quantum_objectives import MetaQuantumPymooProblem
    problem = MetaQuantumPymooProblem()
"""

from dataclasses import dataclass
from typing import Callable, Dict, Optional, Tuple, List

import numpy as np

from meta_calculus.quantum.meta_quantum_compatibility import (
    MetaDerivativeConfig,
    make_meta_rhs,
    random_hermitian,
    random_state,
    rk4_step,
)


# ---------------------------------------------------------------------------
# 1. Meta-Quantum Compatibility Objectives
# ---------------------------------------------------------------------------

@dataclass
class MetaQuantumParameterization:
    """
    Parameterization of the meta-time Schrodinger families that we expose
    to GlobalMOO/pymoo as a search space.

    The idea is: x = (a_u, w_u, k_global, p_power) controls:

        u(t)      = 1 + a_u * sin(w_u * t)
        global k  = coupling in the "global_norm" family
        power p   = exponent in the "power_component" family

    We then measure:
        - norm drift and distance to standard for these families.

    This mirrors the FRW 'calculus parameters' -> 'compatibility metrics'
    structure from the cosmology experiments.
    """

    a_u: float        # amplitude of u(t) modulation
    w_u: float        # frequency of u(t) modulation
    k_global: float   # global_norm "k"
    p_power: float    # power_component "p"

    def make_u(self) -> Callable[[float], float]:
        """
        Build the time-weight function u(t) = 1 + a_u * sin(w_u t),
        but clamp amplitude to keep u(t) positive.
        """
        a = float(self.a_u)
        w = float(self.w_u)

        # Limit amplitude to avoid negative u(t)
        if abs(a) >= 0.9:
            a = 0.9 * np.sign(a)

        def u(t: float) -> float:
            return 1.0 + a * np.sin(w * t)

        return u


def meta_quantum_globalmoo_objective(
    x: np.ndarray,
    dim: int = 4,
    t_final: float = 10.0,
    num_steps: int = 2000,
    seed: Optional[int] = 0,
) -> Dict:
    """
    GlobalMOO-style objective function for the meta-quantum compatibility
    experiment.

    Parameters
    ----------
    x : (4,) ndarray
        Decision vector [a_u, w_u, k_global, p_power].
    dim, t_final, num_steps, seed : as in run_meta_quantum_experiment.

    Returns
    -------
    payload : dict
        {
          "params": { ... },
          "objectives": {
             "norm_drift_global_norm": ...,
             "distance_global_norm": ...,
             "norm_drift_power": ...,
             "distance_power": ...,
             "complexity_penalty": ...
          },
          "metadata": { ... }
        }

    The "objectives" dict is what you typically pass on to GlobalMOO.
    """
    x = np.asarray(x, dtype=float).ravel()
    if x.size != 4:
        raise ValueError("Expected x with 4 parameters: [a_u, w_u, k_global, p_power].")

    a_u, w_u, k_global, p_power = x.tolist()
    param = MetaQuantumParameterization(a_u=a_u, w_u=w_u,
                                        k_global=k_global, p_power=p_power)
    u = param.make_u()

    H = random_hermitian(dim, seed=seed)
    psi0 = random_state(dim, seed=seed + 1 if seed is not None else None)
    dt = t_final / num_steps

    # Standard reference
    std_cfg = MetaDerivativeConfig(name="standard", kind="standard", params={})
    std_rhs = make_meta_rhs(H, std_cfg)
    psi_std = psi0.copy()
    std_traj = [psi_std.copy()]
    for n in range(num_steps):
        t = n * dt
        psi_std = rk4_step(std_rhs, t, psi_std, dt)
        std_traj.append(psi_std.copy())
    std_traj = np.stack(std_traj, axis=0)

    # global_norm / power_component families with this u, k, p
    cfg_global = MetaDerivativeConfig(
        name="global_norm_k", kind="global_norm", params={"u": u, "k": k_global}
    )
    cfg_power = MetaDerivativeConfig(
        name="power_component", kind="power_component", params={"u": u, "p": p_power}
    )

    def eval_family(cfg: MetaDerivativeConfig) -> Tuple[float, float]:
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
        max_norm_drift = float(np.max(norm_drift))

        diff = traj - std_traj
        dists = np.linalg.norm(diff, axis=1)
        max_dist = float(np.max(dists))

        return max_norm_drift, max_dist

    max_norm_global, max_dist_global = eval_family(cfg_global)
    max_norm_power, max_dist_power = eval_family(cfg_power)

    # Complexity penalty: prefer small |k|, |p|, |a_u|, |w_u|
    complexity_penalty = (
        abs(k_global) +
        abs(p_power) +
        0.5 * abs(a_u) +
        0.1 * abs(w_u)
    )

    payload = {
        "params": {
            "a_u": a_u,
            "w_u": w_u,
            "k_global": k_global,
            "p_power": p_power,
        },
        "objectives": {
            # All are to be MINIMIZED
            "norm_drift_global_norm": max_norm_global,
            "distance_global_norm": max_dist_global,
            "norm_drift_power": max_norm_power,
            "distance_power": max_dist_power,
            "complexity_penalty": complexity_penalty,
        },
        "metadata": {
            "dim": dim,
            "t_final": t_final,
            "num_steps": num_steps,
        },
    }
    return payload


# ---------------------------------------------------------------------------
# 2. Quantum State Diffusion Objectives (Δ² / diagonal qutrits)
# ---------------------------------------------------------------------------

@dataclass
class QuantumDiffusionParameterization:
    """
    Parameters controlling the multi-calculus diffusion experiment:

        gamma_power  : power exponent in the power calculus embedding
        w1, w2, w3   : curvature weights on the simplex vertices
        step_size    : diffusion step size (shared by all calculi)

    x = [gamma_power, w1, w2, w3, step_size].
    """

    gamma_power: float
    w1: float
    w2: float
    w3: float
    step_size: float


def quantum_diffusion_globalmoo_objective(
    x: np.ndarray,
    num_points: int = 300,
    num_steps: int = 20,
    seed: Optional[int] = 0,
) -> Dict:
    """
    GlobalMOO-style objective for the quantum-flavored multi-calculus diffusion
    on the simplex (diagonal qutrit density matrices).

    Parameters
    ----------
    x : (5,) ndarray
        Decision vector [gamma_power, w1, w2, w3, step_size].
    num_points, num_steps, seed : forwarded to the diffusion experiment.

    Returns
    -------
    payload : dict
        {
          "params": {...},
          "objectives": {
             "multi_var": ...,
             "multi_entropy_targeted": ...,
             "robustness_variance": ...
          },
          "metadata": {...}
        }

    All objectives are to be MINIMIZED.
    """
    x = np.asarray(x, dtype=float).ravel()
    if x.size != 5:
        raise ValueError("Expected x with 5 parameters: [gamma_power, w1, w2, w3, step_size].")

    gamma_power, w1, w2, w3, step_size = x.tolist()

    # Clamp step_size to a reasonable positive range
    if step_size <= 0:
        step_size = 1e-3
    if step_size > 1.0:
        step_size = 1.0

    from meta_calculus.experiments.multi_calculus_diffusion import (
        sample_simplex_points,
        CalculusEmbedding,
        build_affinity_and_laplacian,
        build_diffusion_operator,
        run_diffusion,
        run_multi_calculus_trajectory,
        normalized_entropy,
        cluster_variance_along_signal,
    )

    P, labels = sample_simplex_points(
        num_points=num_points,
        num_clusters=3,
        cluster_spread=0.07,
        noise_fraction=0.2,
        seed=seed,
    )
    N = P.shape[0]

    W_curv = np.diag([w1, w2, w3])

    calculi = [
        CalculusEmbedding(name="classical", kind="classical"),
        CalculusEmbedding(name="log", kind="log", params={"eps": 1e-6}),
        CalculusEmbedding(name="power", kind="power", params={"gamma": gamma_power}),
        CalculusEmbedding(name="curvature", kind="curvature", params={"W": W_curv}),
    ]

    P_list = []
    for calc in calculi:
        Z = calc.embed(P)
        _, L = build_affinity_and_laplacian(Z, normalized=True)
        P_k = build_diffusion_operator(L, step_size=step_size)
        P_list.append(P_k)

    rng = np.random.default_rng(seed)
    idx_cluster0 = np.where(labels == 0)[0]
    f0 = np.zeros(N)
    if len(idx_cluster0) > 0:
        f0[idx_cluster0] = 1.0
    else:
        f0[rng.integers(low=0, high=N)] = 1.0

    # Single-calculus diffusion
    single_metrics = {}
    for calc, Pk in zip(calculi, P_list):
        traj = run_diffusion(Pk, f0, num_steps=num_steps)
        fT = traj[-1]
        single_metrics[calc.name] = {
            "entropy": normalized_entropy(fT),
            "variance": cluster_variance_along_signal(fT, labels),
        }

    # Multi-calculus (cyclic)
    traj_cyc, _ = run_multi_calculus_trajectory(
        P_list=P_list,
        f0=f0,
        num_steps=num_steps,
        mode="cyclic",
        seed=seed,
    )
    fT_cyc = traj_cyc[-1]
    multi_entropy = normalized_entropy(fT_cyc)
    multi_var = cluster_variance_along_signal(fT_cyc, labels)

    # Robustness: how much cluster variance varies across calculi vs multi
    var_values = [m["variance"] for m in single_metrics.values()]
    var_values.append(multi_var)
    var_values = np.array(var_values, dtype=float)
    robustness_variance = float(np.nanstd(var_values))

    # Entropy target: we don't want entropy too low (no diffusion) or too high
    # (everything washed out). Aim for a moderate target, say 0.6.
    entropy_target = 0.6
    multi_entropy_targeted = float((multi_entropy - entropy_target) ** 2)

    payload = {
        "params": {
            "gamma_power": gamma_power,
            "w1": w1,
            "w2": w2,
            "w3": w3,
            "step_size": step_size,
        },
        "objectives": {
            # All minimized:
            # 1) want small multi-calculus cluster variance (clear cluster structure)
            "multi_var": float(multi_var),
            # 2) want multi-calculus entropy near target
            "multi_entropy_targeted": multi_entropy_targeted,
            # 3) want outcomes to be robust across calculi
            "robustness_variance": robustness_variance,
        },
        "metadata": {
            "num_points": num_points,
            "num_steps": num_steps,
        },
    }
    return payload


# ---------------------------------------------------------------------------
# 3. pymoo Problem Classes (optional, depends on pymoo being installed)
# ---------------------------------------------------------------------------

try:
    from pymoo.core.problem import ElementwiseProblem

    class MetaQuantumPymooProblem(ElementwiseProblem):
        """
        pymoo-compatible problem for meta-quantum compatibility.

        Decision variables x = [a_u, w_u, k_global, p_power].
        Objectives (all minimized):

            f1 = norm_drift_global_norm
            f2 = distance_global_norm
            f3 = norm_drift_power
            f4 = distance_power
            f5 = complexity_penalty
        """

        def __init__(
            self,
            dim: int = 4,
            t_final: float = 10.0,
            num_steps: int = 2000,
            seed: Optional[int] = 0,
        ):
            self._dim = dim
            self._t_final = t_final
            self._num_steps = num_steps
            self._seed = seed

            # Reasonable variable bounds
            xl = np.array([-0.9, 0.0, -2.0, -2.0], dtype=float)  # a_u, w_u, k, p
            xu = np.array([0.9, 3.0, 2.0, 2.0], dtype=float)

            super().__init__(n_var=4, n_obj=5, n_constr=0, xl=xl, xu=xu)

        def _evaluate(self, x, out, *args, **kwargs):
            payload = meta_quantum_globalmoo_objective(
                x,
                dim=self._dim,
                t_final=self._t_final,
                num_steps=self._num_steps,
                seed=self._seed,
            )
            objs = payload["objectives"]
            f1 = objs["norm_drift_global_norm"]
            f2 = objs["distance_global_norm"]
            f3 = objs["norm_drift_power"]
            f4 = objs["distance_power"]
            f5 = objs["complexity_penalty"]
            out["F"] = np.array([f1, f2, f3, f4, f5], dtype=float)

    class QuantumDiffusionPymooProblem(ElementwiseProblem):
        """
        pymoo-compatible problem for multi-calculus quantum state diffusion.

        Decision variables x = [gamma_power, w1, w2, w3, step_size].
        Objectives (all minimized):

            f1 = multi_var
            f2 = multi_entropy_targeted
            f3 = robustness_variance
        """

        def __init__(
            self,
            num_points: int = 300,
            num_steps: int = 20,
            seed: Optional[int] = 0,
        ):
            self._num_points = num_points
            self._num_steps = num_steps
            self._seed = seed

            # Bounds
            xl = np.array([0.1, 0.1, 0.1, 0.1, 0.01], dtype=float)
            xu = np.array([2.0, 3.0, 3.0, 3.0, 1.0], dtype=float)

            super().__init__(n_var=5, n_obj=3, n_constr=0, xl=xl, xu=xu)

        def _evaluate(self, x, out, *args, **kwargs):
            payload = quantum_diffusion_globalmoo_objective(
                x,
                num_points=self._num_points,
                num_steps=self._num_steps,
                seed=self._seed,
            )
            objs = payload["objectives"]
            f1 = objs["multi_var"]
            f2 = objs["multi_entropy_targeted"]
            f3 = objs["robustness_variance"]
            out["F"] = np.array([f1, f2, f3], dtype=float)

except ImportError:
    # pymoo is optional; if not installed, we simply skip the Problem classes.
    MetaQuantumPymooProblem = None
    QuantumDiffusionPymooProblem = None


if __name__ == "__main__":
    # Test GlobalMOO-style objectives
    print("Testing Meta-Quantum GlobalMOO objective...")
    x_qm = np.array([0.3, 1.0, 0.5, 1.0])
    payload_qm = meta_quantum_globalmoo_objective(x_qm, num_steps=500)
    print(f"Params: {payload_qm['params']}")
    print(f"Objectives: {payload_qm['objectives']}")

    print("\nTesting Quantum Diffusion GlobalMOO objective...")
    x_diff = np.array([0.3, 1.0, 1.3, 0.7, 0.5])
    payload_diff = quantum_diffusion_globalmoo_objective(x_diff)
    print(f"Params: {payload_diff['params']}")
    print(f"Objectives: {payload_diff['objectives']}")
