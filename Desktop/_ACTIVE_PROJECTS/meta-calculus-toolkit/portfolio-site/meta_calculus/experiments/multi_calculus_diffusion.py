"""
Multi-Calculus Diffusion on the Simplex (Δ²)

This experiment is the geometric / diffusion analogue of the FRW + meta-calculus
work you already have under the "Simulator" and "Results" sections on the site:

    - Instead of modifying the dynamics (like Friedmann or Schrödinger directly),
      we keep the underlying space fixed (the simplex Δ²),
      and change the *calculus* used to define distances and diffusion.

    - Each calculus is realized as an embedding Φ_k of the state space into R^m.
      Euclidean distance in that embedding defines a "metric" / geometry.

    - For each calculus-geometry we build a diffusion operator P_k.

    - We then compare:
        * Single-calculus diffusion using P_k,
        * Naive averaged operator,
        * Multi-calculus trajectories that alternate between {P_k}.

This mirrors the N01ne-style "multi-metric diffusion" idea, but expressed in your
"many calculi on the same geometry" language.

Usage:
    python -m meta_calculus.experiments.multi_calculus_diffusion

Or import and use:
    from meta_calculus.experiments.multi_calculus_diffusion import (
        run_example_experiment,
        run_full_analysis,
    )
"""

from dataclasses import dataclass, field
from typing import Callable, List, Literal, Tuple, Dict, Optional

import numpy as np


# ---------------------------------------------------------------------------
# 1. Simplex sampling utilities
# ---------------------------------------------------------------------------

def sample_simplex_points(
    num_points: int,
    num_clusters: int = 3,
    cluster_spread: float = 0.05,
    noise_fraction: float = 0.2,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Sample points on the 2-simplex Δ^2 with a mixture of clustered + noisy points.

    Each probability vector p satisfies:
        p_i >= 0, sum_i p_i = 1.

    Parameters
    ----------
    num_points : int
        Total number of points to sample.
    num_clusters : int
        Number of cluster centers on the simplex (default: 3, the vertices).
    cluster_spread : float
        Standard deviation of Gaussian noise around cluster centers.
    noise_fraction : float
        Fraction of points that are sampled uniformly on the simplex.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    points : (N, 3) ndarray
        Sampled probability vectors on Δ^2.
    labels : (N,) ndarray
        Cluster labels in {0,1,2,...} or -1 for noise.
    """
    rng = np.random.default_rng(seed)

    # Canonical vertices of Δ^2
    vertices = np.eye(3)
    num_points = int(num_points)
    num_noise = int(noise_fraction * num_points)
    num_cluster_points = num_points - num_noise

    # If num_clusters != 3, we just pick that many random combinations of vertices.
    if num_clusters <= 3:
        centers = vertices[:num_clusters]
    else:
        # simple random convex combinations of vertices as pseudo-centers
        weights = rng.dirichlet(alpha=np.ones(3), size=num_clusters)
        centers = weights

    points = []
    labels = []

    # Clustered points
    for i in range(num_cluster_points):
        k = i % num_clusters
        center = centers[k]

        # Add small Gaussian noise in R^3 then project back to simplex
        noisy = center + rng.normal(scale=cluster_spread, size=3)
        noisy = np.clip(noisy, 1e-8, None)
        noisy /= noisy.sum()

        points.append(noisy)
        labels.append(k)

    # Uniform noise on simplex via Dirichlet
    if num_noise > 0:
        noise_pts = rng.dirichlet(alpha=np.ones(3), size=num_noise)
        points.extend(noise_pts)
        labels.extend([-1] * num_noise)

    points = np.vstack(points)
    labels = np.array(labels, dtype=int)

    return points, labels


# ---------------------------------------------------------------------------
# 2. Calculus embeddings = "metrics" on the state space
# ---------------------------------------------------------------------------

@dataclass
class CalculusEmbedding:
    """
    A calculus embedding Φ: Δ^2 -> R^m.

    This is the "geometric lens" associated with a particular calculus.

    Examples implemented here:
        - 'classical': Φ(p) = p
        - 'log':       Φ(p) = log(p + eps)
        - 'power':     Φ(p) = p^gamma
        - 'curvature': Φ(p) = W^{1/2} p, where W encodes curvature / weights
    """
    name: str
    kind: Literal["classical", "log", "power", "curvature"]
    params: Dict = field(default_factory=dict)

    def __post_init__(self):
        # Set reasonable defaults if not provided
        if self.kind == "log":
            self.params.setdefault("eps", 1e-8)
        elif self.kind == "power":
            self.params.setdefault("gamma", 0.3)  # emphasize mid vs extremes
        elif self.kind == "curvature":
            # If no W provided, just identity weights (no-op)
            W = self.params.get("W", np.eye(3))
            self.params["W"] = np.array(W, dtype=float)

    def embed(self, P: np.ndarray) -> np.ndarray:
        """
        Embed a batch of simplex points P (N x 3) into R^3 using this calculus.

        Parameters
        ----------
        P : (N, 3) ndarray
            Probability vectors on Δ^2.

        Returns
        -------
        Z : (N, 3) ndarray
            Embedded points in R^3 under this calculus.
        """
        if self.kind == "classical":
            # Identity embedding
            return P.copy()

        elif self.kind == "log":
            eps = self.params["eps"]
            return np.log(P + eps)

        elif self.kind == "power":
            gamma = self.params["gamma"]
            return np.power(P, gamma)

        elif self.kind == "curvature":
            W = self.params["W"]
            # W^{1/2} @ p for each p
            # For now assume W is symmetric positive definite
            # Precompute sqrt of W
            eigvals, eigvecs = np.linalg.eigh(W)
            sqrtW = eigvecs @ np.diag(np.sqrt(np.clip(eigvals, 0, None))) @ eigvecs.T
            return (sqrtW @ P.T).T

        else:
            raise ValueError(f"Unknown calculus kind: {self.kind}")


# ---------------------------------------------------------------------------
# 3. Build graph Laplacians and diffusion operators for each calculus
# ---------------------------------------------------------------------------

def pairwise_distances(Z: np.ndarray) -> np.ndarray:
    """
    Compute pairwise Euclidean distances between rows of Z.

    Parameters
    ----------
    Z : (N, d) ndarray

    Returns
    -------
    D : (N, N) ndarray
        Distance matrix.
    """
    # Using (x - y)^2 = x^2 + y^2 - 2 x·y trick
    sq = np.sum(Z**2, axis=1, keepdims=True)
    D2 = sq + sq.T - 2 * (Z @ Z.T)
    D2 = np.maximum(D2, 0.0)
    return np.sqrt(D2)


def build_affinity_and_laplacian(
    Z: np.ndarray,
    sigma: Optional[float] = None,
    normalized: bool = True,
    eps: float = 1e-9,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Build affinity matrix W and (normalized) Laplacian L for embedded points.

    Parameters
    ----------
    Z : (N, d) ndarray
        Embedded points in R^d.
    sigma : float, optional
        Scale for the Gaussian kernel. If None, uses median distance.
    normalized : bool
        Whether to return the normalized Laplacian (I - D^{-1/2} W D^{-1/2})
        or the unnormalized one (D - W).
    eps : float
        Small value to avoid division by zero.

    Returns
    -------
    W : (N, N) ndarray
        Affinity matrix.
    L : (N, N) ndarray
        Graph Laplacian.
    """
    D = pairwise_distances(Z)
    if sigma is None:
        # Median of non-zero distances
        d_flat = D[np.triu_indices_from(D, k=1)]
        d_flat = d_flat[d_flat > 0]
        if len(d_flat) == 0:
            sigma = 1.0
        else:
            sigma = np.median(d_flat)

    W = np.exp(- (D**2) / (sigma**2 + eps))

    # Zero diagonal (no self-loop weight)
    np.fill_diagonal(W, 0.0)

    # Degree matrix
    degrees = np.sum(W, axis=1)
    D_mat = np.diag(degrees)

    if normalized:
        # Normalized Laplacian: L = I - D^{-1/2} W D^{-1/2}
        inv_sqrt_deg = 1.0 / np.sqrt(degrees + eps)
        D_inv_sqrt = np.diag(inv_sqrt_deg)
        I = np.eye(W.shape[0])
        L = I - D_inv_sqrt @ W @ D_inv_sqrt
    else:
        # Unnormalized: L = D - W
        L = D_mat - W

    return W, L


def build_diffusion_operator(
    L: np.ndarray,
    step_size: float = 0.5,
) -> np.ndarray:
    """
    Build a diffusion operator P = I - eta * L.

    For small eta, this approximates heat flow on the graph. If L is a
    normalized Laplacian, then I - eta L is typically a contraction.

    Parameters
    ----------
    L : (N, N) ndarray
        Graph Laplacian.
    step_size : float
        Diffusion step size eta.

    Returns
    -------
    P : (N, N) ndarray
        Diffusion operator.
    """
    I = np.eye(L.shape[0])
    return I - step_size * L


# ---------------------------------------------------------------------------
# 4. Spectral analysis utilities
# ---------------------------------------------------------------------------

def compute_spectral_gap(L: np.ndarray, k: int = 2) -> float:
    """
    Compute the spectral gap (λ₂ - λ₁) of a Laplacian.

    For a normalized Laplacian, λ₁ = 0 (constant eigenvector).
    The spectral gap λ₂ controls the mixing time of diffusion.

    Parameters
    ----------
    L : (N, N) ndarray
        Graph Laplacian.
    k : int
        Number of eigenvalues to compute (need at least 2).

    Returns
    -------
    gap : float
        The spectral gap λ₂ - λ₁.
    """
    # Use full eigendecomposition for small matrices
    eigvals = np.linalg.eigvalsh(L)
    eigvals = np.sort(eigvals)

    if len(eigvals) < 2:
        return 0.0

    # λ₁ should be ~0 for normalized Laplacian, λ₂ is the gap
    return float(eigvals[1] - eigvals[0])


def compute_effective_spectral_gap(
    P_list: List[np.ndarray],
    num_cycles: int = 1,
) -> float:
    """
    Estimate effective spectral gap for the product of diffusion operators
    (one full cycle through all calculi).

    P_eff = P_K @ P_{K-1} @ ... @ P_1

    The effective gap relates to how fast the multi-calculus trajectory converges.

    Parameters
    ----------
    P_list : list of (N, N) ndarray
        Diffusion operators for each calculus.
    num_cycles : int
        Number of complete cycles to compose.

    Returns
    -------
    gap : float
        Effective spectral gap (1 - |λ₂|) of the composed operator.
    """
    N = P_list[0].shape[0]
    P_eff = np.eye(N)

    for _ in range(num_cycles):
        for P in P_list:
            P_eff = P @ P_eff

    # Compute eigenvalues of the composed operator
    eigvals = np.linalg.eigvals(P_eff)
    eigvals_abs = np.abs(eigvals)
    eigvals_sorted = np.sort(eigvals_abs)[::-1]  # descending

    # The largest eigenvalue should be ~1 (stationary),
    # gap is 1 - second largest
    if len(eigvals_sorted) < 2:
        return 0.0

    return float(1.0 - eigvals_sorted[1])


# ---------------------------------------------------------------------------
# 5. Diffusion and multi-calculus trajectories
# ---------------------------------------------------------------------------

def run_diffusion(
    P: np.ndarray,
    f0: np.ndarray,
    num_steps: int,
) -> np.ndarray:
    """
    Run diffusion using a single operator P:

        f^{(t+1)} = P f^{(t)}.

    Parameters
    ----------
    P : (N, N) ndarray
        Diffusion operator.
    f0 : (N,) ndarray
        Initial signal on nodes.
    num_steps : int
        Number of diffusion steps.

    Returns
    -------
    traj : (num_steps+1, N) ndarray
        Trajectory of f over time.
    """
    f = f0.copy()
    traj = [f.copy()]
    for _ in range(num_steps):
        f = P @ f
        traj.append(f.copy())
    return np.vstack(traj)


def run_multi_calculus_trajectory(
    P_list: List[np.ndarray],
    f0: np.ndarray,
    num_steps: int,
    mode: Literal["cyclic", "random"] = "cyclic",
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, List[int]]:
    """
    Run a multi-calculus diffusion trajectory:

        f^{(t+1)} = P_{k_t} f^{(t)},

    where {P_k} are the diffusion operators for different calculi, and k_t is
    chosen either cyclically or randomly.

    Parameters
    ----------
    P_list : list of (N, N) ndarray
        Diffusion operators for different calculi.
    f0 : (N,) ndarray
        Initial signal.
    num_steps : int
        Number of diffusion steps.
    mode : {"cyclic", "random"}
        How to choose the calculus at each step.
    seed : int, optional
        Random seed for "random" mode.

    Returns
    -------
    traj : (num_steps+1, N) ndarray
        Trajectory of f over time.
    calculus_sequence : list of int
        Which calculus was used at each step.
    """
    K = len(P_list)
    f = f0.copy()
    traj = [f.copy()]
    calculus_sequence = []

    rng = np.random.default_rng(seed)

    for t in range(num_steps):
        if mode == "cyclic":
            k = t % K
        elif mode == "random":
            k = rng.integers(low=0, high=K)
        else:
            raise ValueError(f"Unknown mode: {mode}")

        calculus_sequence.append(k)
        P = P_list[k]
        f = P @ f
        traj.append(f.copy())

    return np.vstack(traj), calculus_sequence


def run_averaged_diffusion(
    P_list: List[np.ndarray],
    f0: np.ndarray,
    num_steps: int,
) -> np.ndarray:
    """
    Run diffusion using the naive averaged operator:

        P_avg = (1/K) * sum_k P_k
        f^{(t+1)} = P_avg f^{(t)}

    Parameters
    ----------
    P_list : list of (N, N) ndarray
        Diffusion operators for different calculi.
    f0 : (N,) ndarray
        Initial signal.
    num_steps : int
        Number of diffusion steps.

    Returns
    -------
    traj : (num_steps+1, N) ndarray
        Trajectory of f over time.
    """
    K = len(P_list)
    P_avg = sum(P_list) / K
    return run_diffusion(P_avg, f0, num_steps)


# ---------------------------------------------------------------------------
# 6. Evaluation metrics
# ---------------------------------------------------------------------------

def normalized_entropy(p: np.ndarray, eps: float = 1e-12) -> float:
    """
    Compute normalized entropy H(p)/log(N) for a probability distribution p.

    Parameters
    ----------
    p : (N,) ndarray
        Non-negative weights (not necessarily normalized).
    eps : float
        Small constant for numerical stability.

    Returns
    -------
    h_norm : float
        Normalized entropy in [0,1].
    """
    w = np.abs(p) + eps
    w /= w.sum()
    H = -np.sum(w * np.log(w + eps))
    H_max = np.log(len(w))
    return float(H / (H_max + eps))


def cluster_variance_along_signal(
    f: np.ndarray,
    labels: np.ndarray,
) -> float:
    """
    Compute average within-cluster variance of a scalar signal f, ignoring
    label -1 (noise). Lower is "better" separation along f.

    Parameters
    ----------
    f : (N,) ndarray
        Scalar signal on nodes.
    labels : (N,) ndarray
        Cluster labels, with -1 used for noise.

    Returns
    -------
    var_mean : float
        Mean within-cluster variance.
    """
    unique_labels = sorted(set(labels.tolist()) - {-1})
    if not unique_labels:
        return float("nan")

    vars_ = []
    for c in unique_labels:
        idx = np.where(labels == c)[0]
        if len(idx) < 2:
            continue
        vars_.append(float(np.var(f[idx])))

    if not vars_:
        return float("nan")

    return float(np.mean(vars_))


def silhouette_score_simple(
    Z: np.ndarray,
    labels: np.ndarray,
) -> float:
    """
    Compute a simplified silhouette score for cluster quality.

    Parameters
    ----------
    Z : (N, d) ndarray
        Embedded points.
    labels : (N,) ndarray
        Cluster labels (-1 = noise, ignored).

    Returns
    -------
    score : float
        Mean silhouette score in [-1, 1]. Higher is better.
    """
    unique_labels = sorted(set(labels.tolist()) - {-1})
    if len(unique_labels) < 2:
        return 0.0

    D = pairwise_distances(Z)
    scores = []

    for i in range(len(labels)):
        if labels[i] == -1:
            continue

        # a(i) = mean distance to points in same cluster
        same_cluster = np.where(labels == labels[i])[0]
        same_cluster = same_cluster[same_cluster != i]
        if len(same_cluster) == 0:
            continue
        a_i = np.mean(D[i, same_cluster])

        # b(i) = min over other clusters of mean distance to that cluster
        b_i = float('inf')
        for c in unique_labels:
            if c == labels[i]:
                continue
            other_cluster = np.where(labels == c)[0]
            if len(other_cluster) > 0:
                b_i = min(b_i, np.mean(D[i, other_cluster]))

        if b_i == float('inf'):
            continue

        s_i = (b_i - a_i) / max(a_i, b_i)
        scores.append(s_i)

    if not scores:
        return 0.0

    return float(np.mean(scores))


def find_multi_calculus_invariants(
    P_list: List[np.ndarray],
    threshold: float = 0.1,
) -> np.ndarray:
    """
    Find states (indices) that are approximately fixed points for ALL
    diffusion operators simultaneously.

    P_k f ≈ f for all k

    These are the "scheme-robust" states that survive all calculi.

    Parameters
    ----------
    P_list : list of (N, N) ndarray
        Diffusion operators.
    threshold : float
        Maximum allowed deviation ||P_k f - f|| / ||f|| for each k.

    Returns
    -------
    invariant_scores : (N,) ndarray
        Score for each node indicating how "invariant" it is across all calculi.
        Higher score = more invariant.
    """
    N = P_list[0].shape[0]
    scores = np.ones(N)

    for i in range(N):
        # Unit vector concentrated at node i
        f = np.zeros(N)
        f[i] = 1.0

        max_deviation = 0.0
        for P in P_list:
            Pf = P @ f
            deviation = np.linalg.norm(Pf - f) / (np.linalg.norm(f) + 1e-10)
            max_deviation = max(max_deviation, deviation)

        # Score: inverse of deviation (higher = more invariant)
        scores[i] = 1.0 / (1.0 + max_deviation)

    return scores


# ---------------------------------------------------------------------------
# 7. Full experiment harness
# ---------------------------------------------------------------------------

@dataclass
class ExperimentConfig:
    """Configuration for multi-calculus diffusion experiment."""
    num_points: int = 300
    num_clusters: int = 3
    cluster_spread: float = 0.07
    noise_fraction: float = 0.2
    num_steps: int = 20
    step_size: float = 0.5
    seed: int = 0

    # Curvature weights (can be derived from physics)
    curvature_weights: np.ndarray = field(default_factory=lambda: np.diag([1.0, 1.3, 0.7]))


@dataclass
class ExperimentResults:
    """Results from multi-calculus diffusion experiment."""
    # Points and labels
    points: np.ndarray
    labels: np.ndarray

    # Calculi and operators
    calculi: List[CalculusEmbedding]
    laplacians: List[np.ndarray]
    diffusion_operators: List[np.ndarray]

    # Spectral analysis
    spectral_gaps: Dict[str, float] = field(default_factory=dict)
    effective_gap: float = 0.0

    # Diffusion results
    single_calculus_metrics: Dict[str, Dict[str, float]] = field(default_factory=dict)
    averaged_metrics: Dict[str, float] = field(default_factory=dict)
    multi_cyclic_metrics: Dict[str, float] = field(default_factory=dict)
    multi_random_metrics: Dict[str, float] = field(default_factory=dict)

    # Invariant analysis
    invariant_scores: np.ndarray = field(default_factory=lambda: np.array([]))

    # Trajectories (optional, for visualization)
    trajectories: Dict[str, np.ndarray] = field(default_factory=dict)


def run_full_analysis(config: ExperimentConfig) -> ExperimentResults:
    """
    Run a comprehensive multi-calculus diffusion analysis.

    Parameters
    ----------
    config : ExperimentConfig
        Experiment configuration.

    Returns
    -------
    results : ExperimentResults
        Complete results including metrics, spectral analysis, and invariants.
    """
    rng = np.random.default_rng(config.seed)

    # 1. Sample simplex points + cluster labels
    P, labels = sample_simplex_points(
        num_points=config.num_points,
        num_clusters=config.num_clusters,
        cluster_spread=config.cluster_spread,
        noise_fraction=config.noise_fraction,
        seed=config.seed,
    )
    N = P.shape[0]

    # 2. Define calculi (these correspond to distinct "metrics" / geometries)
    calculi = [
        CalculusEmbedding(name="classical", kind="classical"),
        CalculusEmbedding(name="log", kind="log", params={"eps": 1e-6}),
        CalculusEmbedding(name="power", kind="power", params={"gamma": 0.3}),
        CalculusEmbedding(name="curvature", kind="curvature", params={"W": config.curvature_weights}),
    ]

    # 3. Build diffusion operators and store Laplacians
    P_list = []
    L_list = []
    spectral_gaps = {}

    for calc in calculi:
        Z = calc.embed(P)
        _, L = build_affinity_and_laplacian(Z, normalized=True)
        P_k = build_diffusion_operator(L, step_size=config.step_size)

        P_list.append(P_k)
        L_list.append(L)
        spectral_gaps[calc.name] = compute_spectral_gap(L)

    # 4. Compute effective spectral gap for multi-calculus
    effective_gap = compute_effective_spectral_gap(P_list, num_cycles=1)

    # 5. Initial signal f0: concentrate on cluster 0
    idx_cluster0 = np.where(labels == 0)[0]
    f0 = np.zeros(N)
    if len(idx_cluster0) > 0:
        f0[idx_cluster0] = 1.0
    else:
        f0[rng.integers(low=0, high=N)] = 1.0

    # 6. Run diffusions and compute metrics
    single_calculus_metrics = {}
    trajectories = {}

    for calc, Pk in zip(calculi, P_list):
        traj = run_diffusion(Pk, f0, num_steps=config.num_steps)
        fT = traj[-1]

        single_calculus_metrics[calc.name] = {
            "final_normalized_entropy": normalized_entropy(fT),
            "final_cluster_variance": cluster_variance_along_signal(fT, labels),
            "silhouette_score": silhouette_score_simple(calc.embed(P), labels),
        }
        trajectories[f"single_{calc.name}"] = traj

    # Averaged operator
    traj_avg = run_averaged_diffusion(P_list, f0, config.num_steps)
    fT_avg = traj_avg[-1]
    averaged_metrics = {
        "final_normalized_entropy": normalized_entropy(fT_avg),
        "final_cluster_variance": cluster_variance_along_signal(fT_avg, labels),
    }
    trajectories["averaged"] = traj_avg

    # Multi-calculus (cyclic)
    traj_multi, _ = run_multi_calculus_trajectory(
        P_list, f0, config.num_steps, mode="cyclic", seed=config.seed
    )
    fT_multi = traj_multi[-1]
    multi_cyclic_metrics = {
        "final_normalized_entropy": normalized_entropy(fT_multi),
        "final_cluster_variance": cluster_variance_along_signal(fT_multi, labels),
    }
    trajectories["multi_cyclic"] = traj_multi

    # Multi-calculus (random)
    traj_rand, _ = run_multi_calculus_trajectory(
        P_list, f0, config.num_steps, mode="random", seed=config.seed
    )
    fT_rand = traj_rand[-1]
    multi_random_metrics = {
        "final_normalized_entropy": normalized_entropy(fT_rand),
        "final_cluster_variance": cluster_variance_along_signal(fT_rand, labels),
    }
    trajectories["multi_random"] = traj_rand

    # 7. Find multi-calculus invariants
    invariant_scores = find_multi_calculus_invariants(P_list)

    return ExperimentResults(
        points=P,
        labels=labels,
        calculi=calculi,
        laplacians=L_list,
        diffusion_operators=P_list,
        spectral_gaps=spectral_gaps,
        effective_gap=effective_gap,
        single_calculus_metrics=single_calculus_metrics,
        averaged_metrics=averaged_metrics,
        multi_cyclic_metrics=multi_cyclic_metrics,
        multi_random_metrics=multi_random_metrics,
        invariant_scores=invariant_scores,
        trajectories=trajectories,
    )


def run_example_experiment(
    num_points: int = 300,
    num_steps: int = 20,
    seed: Optional[int] = 0,
) -> Dict[str, Dict[str, float]]:
    """
    Run a small end-to-end experiment (simplified interface).

    Returns a dict of simple scalar metrics that you can send to the
    "Results" page or log from your existing experiment harness.
    """
    config = ExperimentConfig(
        num_points=num_points,
        num_steps=num_steps,
        seed=seed if seed is not None else 0,
    )

    results = run_full_analysis(config)

    # Flatten to simple dict format
    output = {}

    for name, metrics in results.single_calculus_metrics.items():
        output[f"single_{name}"] = metrics

    output["averaged"] = results.averaged_metrics
    output["multi_cyclic"] = results.multi_cyclic_metrics
    output["multi_random"] = results.multi_random_metrics

    # Add spectral info
    output["spectral"] = {
        **{f"gap_{k}": v for k, v in results.spectral_gaps.items()},
        "effective_gap": results.effective_gap,
    }

    return output


def print_results_summary(results: ExperimentResults) -> None:
    """Print a formatted summary of experiment results."""
    print("=" * 60)
    print("MULTI-CALCULUS DIFFUSION EXPERIMENT RESULTS")
    print("=" * 60)

    print("\n--- Spectral Gaps ---")
    for name, gap in results.spectral_gaps.items():
        print(f"  {name}: {gap:.4f}")
    print(f"  effective (multi): {results.effective_gap:.4f}")

    print("\n--- Single-Calculus Diffusion ---")
    for name, metrics in results.single_calculus_metrics.items():
        print(f"  {name}:")
        print(f"    entropy: {metrics['final_normalized_entropy']:.4f}")
        print(f"    cluster_var: {metrics['final_cluster_variance']:.6f}")

    print("\n--- Averaged Operator ---")
    print(f"    entropy: {results.averaged_metrics['final_normalized_entropy']:.4f}")
    print(f"    cluster_var: {results.averaged_metrics['final_cluster_variance']:.6f}")

    print("\n--- Multi-Calculus (Cyclic) ---")
    print(f"    entropy: {results.multi_cyclic_metrics['final_normalized_entropy']:.4f}")
    print(f"    cluster_var: {results.multi_cyclic_metrics['final_cluster_variance']:.6f}")

    print("\n--- Multi-Calculus (Random) ---")
    print(f"    entropy: {results.multi_random_metrics['final_normalized_entropy']:.4f}")
    print(f"    cluster_var: {results.multi_random_metrics['final_cluster_variance']:.6f}")

    print("\n--- Invariant Analysis ---")
    top_invariant = np.argsort(results.invariant_scores)[-5:][::-1]
    print(f"  Most invariant nodes: {top_invariant.tolist()}")
    print(f"  Their scores: {results.invariant_scores[top_invariant].tolist()}")

    print("=" * 60)


# ---------------------------------------------------------------------------
# 8. CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Multi-Calculus Diffusion on Simplex"
    )
    parser.add_argument("--num-points", type=int, default=300)
    parser.add_argument("--num-steps", type=int, default=20)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    config = ExperimentConfig(
        num_points=args.num_points,
        num_steps=args.num_steps,
        seed=args.seed,
    )

    results = run_full_analysis(config)

    if args.verbose:
        print_results_summary(results)
    else:
        # Simple JSON-like output
        metrics = run_example_experiment(
            num_points=args.num_points,
            num_steps=args.num_steps,
            seed=args.seed,
        )
        print("Multi-Calculus Diffusion (Δ²) – Metrics:")
        for k, v in metrics.items():
            print(f"{k}: {v}")
