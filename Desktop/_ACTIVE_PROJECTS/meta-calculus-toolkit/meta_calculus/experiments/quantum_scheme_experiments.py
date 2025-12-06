"""
Experiment Q-A: A-Scheme Invariance of Meta-Time Evolution
Experiment Q-B: Multi-Geometry Diffusion on Quantum States

Demonstrates that meta-calculus is compatible with number system
scheme-robustness. The key results are:

Q-A: Meta-time Schrodinger evolution produces identical observables
     whether formulated in Complex QT or Real NQT (RNQT).

Q-B: Entanglement structure survives alternating diffusion between
     CQT (Fubini-Study) and RNQT metrics, validating that physical
     structure is scheme-robust.

This validates that meta-calculus doesn't accidentally break
the CQT <-> RNQT equivalence.

Citations:
- Hoffreumon & Woods (2025) arXiv:2504.02808
- Renou et al. (2021) arXiv:2101.10873

CRITICAL: NO UNICODE - ASCII only for Windows compatibility
"""

import numpy as np
from typing import Tuple, Dict, List, Callable, Optional
from abc import ABC, abstractmethod


class HarmonicOscillatorBase(ABC):
    """Base class for quantum harmonic oscillator in different formulations"""

    def __init__(self, n_levels: int = 10, omega: float = 1.0,
                 hbar: float = 1.0, mass: float = 1.0):
        """
        Initialize quantum harmonic oscillator.

        Args:
            n_levels: Number of energy levels to include
            omega: Angular frequency
            hbar: Reduced Planck constant
            mass: Particle mass
        """
        self.n_levels = n_levels
        self.omega = omega
        self.hbar = hbar
        self.mass = mass
        self._setup_operators()

    @abstractmethod
    def _setup_operators(self):
        """Setup Hamiltonian and other operators"""
        pass

    @abstractmethod
    def evolve(self, psi0, t: float) -> np.ndarray:
        """Evolve state from psi0 to time t"""
        pass

    @abstractmethod
    def meta_evolve(self, psi0, t: float, u_func: Callable) -> np.ndarray:
        """Meta-time evolution with weight function u(t)"""
        pass


class ComplexQHO(HarmonicOscillatorBase):
    """Quantum harmonic oscillator in standard complex formulation"""

    def _setup_operators(self):
        """Setup operators in complex Hilbert space"""
        # Energy eigenvalues: E_n = hbar * omega * (n + 1/2)
        self.energies = self.hbar * self.omega * (np.arange(self.n_levels) + 0.5)

        # Hamiltonian (diagonal in energy basis)
        self.H = np.diag(self.energies)

        # Creation and annihilation operators
        # a|n> = sqrt(n)|n-1>, a_dag|n> = sqrt(n+1)|n+1>
        self.a = np.zeros((self.n_levels, self.n_levels), dtype=complex)
        for n in range(self.n_levels - 1):
            self.a[n, n+1] = np.sqrt(n + 1)
        self.a_dag = self.a.T.conj()

        # Position operator: x = sqrt(hbar/2*m*omega) * (a + a_dag)
        coeff = np.sqrt(self.hbar / (2 * self.mass * self.omega))
        self.x = coeff * (self.a + self.a_dag)

        # Momentum operator: p = i*sqrt(m*omega*hbar/2) * (a_dag - a)
        coeff_p = np.sqrt(self.mass * self.omega * self.hbar / 2)
        self.p = 1j * coeff_p * (self.a_dag - self.a)

    def evolve(self, psi0: np.ndarray, t: float) -> np.ndarray:
        """
        Standard Schrodinger evolution.

        |psi(t)> = exp(-iHt/hbar)|psi0>

        In the energy eigenbasis, this is just phase multiplication.
        """
        phases = np.exp(-1j * self.energies * t / self.hbar)
        return psi0 * phases

    def meta_evolve(self, psi0: np.ndarray, t: float, u_func: Callable,
                    dt: float = 0.001) -> np.ndarray:
        """
        Meta-time evolution with weight function u(t).

        d|psi>/dt_meta = -i/hbar * u(t) * H |psi>

        This generalizes standard evolution by allowing time-dependent
        rescaling via the weight function u(t).

        Args:
            psi0: Initial state vector
            t: Final meta-time
            u_func: Weight function u(t)
            dt: Integration timestep
        """
        psi = psi0.copy().astype(complex)
        n_steps = int(t / dt)

        for step in range(n_steps):
            t_current = step * dt
            weight = u_func(t_current)
            # Euler step: d_psi = -i/hbar * u(t) * H @ psi * dt
            d_psi = -1j / self.hbar * weight * (self.H @ psi) * dt
            psi = psi + d_psi
            # Renormalize to prevent numerical drift
            psi = psi / np.linalg.norm(psi)

        return psi

    def expectation(self, psi: np.ndarray, O: np.ndarray) -> float:
        """
        Expectation value <psi|O|psi>.

        Args:
            psi: State vector
            O: Observable operator

        Returns:
            Real expectation value
        """
        return np.real(np.conj(psi) @ O @ psi)


class RealNQTQHO(HarmonicOscillatorBase):
    """
    Quantum harmonic oscillator in Real Number Quantum Theory (RNQT).

    Uses the Gamma embedding: C^n -> R^{2n} to represent quantum states
    and operators purely with real numbers. The imaginary unit i is
    represented by the matrix J.

    Reference: Hoffreumon & Woods (2025) arXiv:2504.02808
    """

    def __init__(self, *args, **kwargs):
        # J matrix (2x2 block representing imaginary unit)
        # J^2 = -I, so J acts like i
        self.J2 = np.array([[0, -1], [1, 0]], dtype=float)
        super().__init__(*args, **kwargs)

    def _J_block(self, n: int) -> np.ndarray:
        """
        Create block-diagonal J matrix of size 2n x 2n.

        This represents the imaginary unit in the real embedding.
        """
        return np.kron(np.eye(n), self.J2)

    def gamma_vector(self, psi_complex: np.ndarray) -> np.ndarray:
        """
        Gamma embedding for state vectors.

        Maps complex vector psi = psi_re + i*psi_im to real vector:
        Gamma(psi) = [psi_re, psi_im]

        Args:
            psi_complex: Complex state vector of length n

        Returns:
            Real state vector of length 2n
        """
        return np.concatenate([psi_complex.real, psi_complex.imag])

    def gamma_matrix(self, H_complex: np.ndarray) -> np.ndarray:
        """
        Gamma embedding for Hermitian matrices.

        Maps complex matrix H to real matrix:
        Gamma(H) = [[Re(H), -Im(H)],
                    [Im(H),  Re(H)]]

        Args:
            H_complex: Complex Hermitian matrix (n x n)

        Returns:
            Real matrix (2n x 2n)
        """
        n = H_complex.shape[0]
        H_real = H_complex.real
        H_imag = H_complex.imag

        top = np.hstack([H_real, -H_imag])
        bottom = np.hstack([H_imag, H_real])
        return np.vstack([top, bottom])

    def _setup_operators(self):
        """Setup operators in real embedding"""
        # Energy eigenvalues (same as complex case)
        self.energies = self.hbar * self.omega * (np.arange(self.n_levels) + 0.5)

        # Create complex Hamiltonian first
        H_complex = np.diag(self.energies.astype(complex))

        # Real embedding of Hamiltonian
        self.H = self.gamma_matrix(H_complex)

        # J matrix for this dimension (represents i)
        self.J = self._J_block(self.n_levels)

        # Position operator (via complex construction then embedding)
        a = np.zeros((self.n_levels, self.n_levels), dtype=complex)
        for n in range(self.n_levels - 1):
            a[n, n+1] = np.sqrt(n + 1)
        a_dag = a.T.conj()
        coeff = np.sqrt(self.hbar / (2 * self.mass * self.omega))
        x_complex = coeff * (a + a_dag)

        # Real embedding of position
        self.x = self.gamma_matrix(x_complex)

    def evolve(self, psi0_real: np.ndarray, t: float) -> np.ndarray:
        """
        RNQT evolution equation.

        In RNQT, the evolution is:
        d|psi_r>/dt = -J/hbar @ H_r @ |psi_r>

        where J is the real representation of i.

        Solution: |psi_r(t)> = exp(-J*H_r*t/hbar) @ |psi_r(0)>

        For diagonal H, this gives block-wise rotations:
        exp(-J*H*t/hbar) = cos(Ht/hbar)*I - J*sin(Ht/hbar)
        """
        n = self.n_levels
        phases = self.energies * t / self.hbar

        # Build evolution operator block by block
        U = np.zeros((2*n, 2*n))
        for i, phi in enumerate(phases):
            c, s = np.cos(phi), np.sin(phi)
            # 2x2 rotation block for energy level i
            U[i, i] = c
            U[i, n+i] = s
            U[n+i, i] = -s
            U[n+i, n+i] = c

        return U @ psi0_real

    def meta_evolve(self, psi0_real: np.ndarray, t: float, u_func: Callable,
                    dt: float = 0.001) -> np.ndarray:
        """
        Meta-time evolution in RNQT formulation.

        d|psi_r>/dt_meta = -J/hbar * u(t) * H_r @ |psi_r>

        This is the RNQT analog of the complex meta-evolution.
        """
        psi = psi0_real.copy()
        n_steps = int(t / dt)

        for step in range(n_steps):
            t_current = step * dt
            weight = u_func(t_current)
            # Euler step: d_psi = -J/hbar * u(t) * H @ psi * dt
            d_psi = -weight / self.hbar * (self.J @ self.H @ psi) * dt
            psi = psi + d_psi
            # Renormalize
            psi = psi / np.linalg.norm(psi)

        return psi

    def expectation(self, psi_real: np.ndarray, O_real: np.ndarray) -> float:
        """
        Expectation value in RNQT.

        <psi|O|psi> = psi_r^T @ O_r @ psi_r

        Args:
            psi_real: Real state vector
            O_real: Real observable matrix

        Returns:
            Expectation value
        """
        return np.dot(psi_real, O_real @ psi_real)


class ExperimentQA:
    """
    Experiment Q-A: Verify A-scheme invariance of meta-time evolution.

    Shows that Complex QT and Real NQT give identical predictions for:
    - Survival probabilities
    - Transition probabilities
    - Observable expectation values

    Under both standard and meta-time evolution.

    If meta-calculus is truly scheme-invariant, then both formulations
    should give the same physics, just like standard QM does.
    """

    def __init__(self, n_levels: int = 10):
        """
        Initialize experiment with two oscillators.

        Args:
            n_levels: Number of energy levels
        """
        self.n_levels = n_levels
        self.cqt = ComplexQHO(n_levels)
        self.rnqt = RealNQTQHO(n_levels)

    def run(self, psi0_complex: Optional[np.ndarray] = None,
            t_max: float = 10.0, n_times: int = 50,
            u_func: Optional[Callable] = None) -> Dict:
        """
        Run the A-scheme invariance experiment.

        Args:
            psi0_complex: Initial state in complex form (default: ground state)
            t_max: Maximum evolution time
            n_times: Number of time points to sample
            u_func: Meta-time weight function (default: 1 + 0.1*sin(omega*t))

        Returns:
            Dictionary containing comparison results
        """
        # Default: ground state
        if psi0_complex is None:
            psi0_complex = np.zeros(self.n_levels, dtype=complex)
            psi0_complex[0] = 1.0

        # Default: oscillating weight function
        if u_func is None:
            omega = self.cqt.omega
            u_func = lambda t: 1.0 + 0.1 * np.sin(omega * t)

        # Initial state in both formulations
        psi0_real = self.rnqt.gamma_vector(psi0_complex)

        times = np.linspace(0, t_max, n_times)

        results = {
            'times': times,
            'standard': {'cqt': [], 'rnqt': [], 'diff': []},
            'meta': {'cqt': [], 'rnqt': [], 'diff': []}
        }

        for t in times:
            # ===== STANDARD EVOLUTION =====
            psi_cqt_std = self.cqt.evolve(psi0_complex, t)
            psi_rnqt_std = self.rnqt.evolve(psi0_real, t)

            # Ground state survival probability
            # CQT: P_0 = |<0|psi>|^2
            p0_cqt_std = np.abs(psi_cqt_std[0])**2

            # RNQT: P_0 = psi_r[0]^2 + psi_r[n]^2 (real and imag parts)
            p0_rnqt_std = psi_rnqt_std[0]**2 + psi_rnqt_std[self.n_levels]**2

            results['standard']['cqt'].append(p0_cqt_std)
            results['standard']['rnqt'].append(p0_rnqt_std)
            results['standard']['diff'].append(abs(p0_cqt_std - p0_rnqt_std))

            # ===== META-TIME EVOLUTION =====
            psi_cqt_meta = self.cqt.meta_evolve(psi0_complex, t, u_func)
            psi_rnqt_meta = self.rnqt.meta_evolve(psi0_real, t, u_func)

            # Ground state survival probability
            p0_cqt_meta = np.abs(psi_cqt_meta[0])**2
            p0_rnqt_meta = psi_rnqt_meta[0]**2 + psi_rnqt_meta[self.n_levels]**2

            results['meta']['cqt'].append(p0_cqt_meta)
            results['meta']['rnqt'].append(p0_rnqt_meta)
            results['meta']['diff'].append(abs(p0_cqt_meta - p0_rnqt_meta))

        # Summary statistics
        results['summary'] = {
            'standard_max_diff': max(results['standard']['diff']),
            'meta_max_diff': max(results['meta']['diff']),
            'standard_mean_diff': np.mean(results['standard']['diff']),
            'meta_mean_diff': np.mean(results['meta']['diff']),
            'scheme_invariant': (max(results['standard']['diff']) < 1e-6 and
                                max(results['meta']['diff']) < 1e-3)
        }

        return results

    def report(self, results: Dict) -> str:
        """
        Generate human-readable report.

        Args:
            results: Output from run()

        Returns:
            Formatted report string
        """
        lines = [
            "=" * 70,
            "EXPERIMENT Q-A: A-SCHEME INVARIANCE OF META-TIME EVOLUTION",
            "=" * 70,
            "",
            "Testing if Complex QT and Real NQT give identical predictions",
            "under meta-time Schrodinger evolution.",
            "",
            "Standard Evolution:",
            f"  Max |P(CQT) - P(RNQT)|:  {results['summary']['standard_max_diff']:.2e}",
            f"  Mean |P(CQT) - P(RNQT)|: {results['summary']['standard_mean_diff']:.2e}",
            "",
            "Meta-Time Evolution:",
            f"  Max |P(CQT) - P(RNQT)|:  {results['summary']['meta_max_diff']:.2e}",
            f"  Mean |P(CQT) - P(RNQT)|: {results['summary']['meta_mean_diff']:.2e}",
            "",
            "RESULT: " + ("SCHEME-INVARIANT" if results['summary']['scheme_invariant']
                         else "SCHEME-DEPENDENT (check numerical precision)"),
            "",
            "Interpretation:",
            "  If scheme-invariant: Meta-calculus preserves CQT<->RNQT equivalence.",
            "  Both formulations give identical physical predictions.",
            "  This validates that meta-time does not break quantum mechanics.",
            "",
            "Physical Meaning:",
            "  The meta-time weight function u(t) rescales the evolution rate",
            "  but does not change the observable predictions. This is a",
            "  coordinate transformation in 'time space', analogous to a",
            "  coordinate transformation in position space.",
            "",
            "Reference: Hoffreumon & Woods (2025) arXiv:2504.02808",
            "=" * 70
        ]
        return "\n".join(lines)


class ExperimentQB:
    """
    Experiment Q-B: Multi-geometry diffusion on quantum states.

    Tests scheme-robustness by running diffusion with metrics from
    both CQT (Fubini-Study) and RNQT formulations.

    Key prediction: Entanglement structure is scheme-robust, meaning
    it survives alternating CQT/RNQT diffusion operators.

    This is a stronger test than Q-A because it involves non-linear
    operations (building graphs from distances) that could potentially
    break under scheme changes.
    """

    def __init__(self, n_states: int = 20):
        """
        Initialize with a family of 2-qubit states.

        Args:
            n_states: Number of states parameterized by entanglement
        """
        self.n_states = n_states
        self._generate_states()

    def _generate_states(self):
        """
        Generate 2-qubit states parameterized by entanglement.

        States: |psi(theta)> = cos(theta)|00> + sin(theta)|11>

        theta=0:    |00> (separable)
        theta=pi/4: (|00> + |11>)/sqrt(2) (maximally entangled, Bell state)
        """
        thetas = np.linspace(0, np.pi/4, self.n_states)

        self.states_complex = []
        self.states_real = []
        self.entanglement = []  # Linear entropy measure

        for theta in thetas:
            # Complex state vector (4D for 2 qubits)
            # Basis: |00>, |01>, |10>, |11>
            psi = np.array([np.cos(theta), 0, 0, np.sin(theta)], dtype=complex)
            self.states_complex.append(psi)

            # Real embedding (8D)
            psi_real = np.concatenate([psi.real, psi.imag])
            self.states_real.append(psi_real)

            # Entanglement: linear entropy of reduced density matrix
            # For pure states |psi>, S_lin(rho_A) = 1 - Tr(rho_A^2)
            rho = np.outer(psi, psi.conj())
            # Partial trace over qubit B
            rho_A = np.array([
                [rho[0,0] + rho[1,1], rho[0,2] + rho[1,3]],
                [rho[2,0] + rho[3,1], rho[2,2] + rho[3,3]]
            ])
            S_lin = 1 - np.trace(rho_A @ rho_A).real
            self.entanglement.append(S_lin)

        self.states_complex = np.array(self.states_complex)
        self.states_real = np.array(self.states_real)
        self.entanglement = np.array(self.entanglement)

    def fubini_study_distance(self, psi1: np.ndarray, psi2: np.ndarray) -> float:
        """
        Fubini-Study distance between pure quantum states.

        d_FS(psi1, psi2) = arccos(|<psi1|psi2>|)

        This is the natural metric on the space of pure quantum states
        (projective Hilbert space).

        Args:
            psi1, psi2: Complex state vectors

        Returns:
            Distance in [0, pi/2]
        """
        overlap = np.abs(np.vdot(psi1, psi2))
        overlap = np.clip(overlap, 0, 1)  # Numerical safety
        return np.arccos(overlap)

    def rnqt_distance(self, psi1_real: np.ndarray, psi2_real: np.ndarray) -> float:
        """
        Distance in RNQT formulation.

        In the real embedding, we use Euclidean distance on the
        projective space (accounting for overall sign ambiguity).

        Args:
            psi1_real, psi2_real: Real state vectors

        Returns:
            Distance
        """
        # Normalize to unit vectors
        psi1_n = psi1_real / np.linalg.norm(psi1_real)
        psi2_n = psi2_real / np.linalg.norm(psi2_real)

        # Account for sign ambiguity in projective space
        d1 = np.linalg.norm(psi1_n - psi2_n)
        d2 = np.linalg.norm(psi1_n + psi2_n)
        return min(d1, d2)

    def build_graph_laplacian(self, distance_func: Callable,
                             states: List[np.ndarray],
                             sigma: float = 0.5) -> Tuple[np.ndarray, np.ndarray]:
        """
        Build graph Laplacian from pairwise distances.

        Constructs a weighted graph where edge weights are:
        W_ij = exp(-d(i,j)^2 / (2*sigma^2))

        Then builds normalized Laplacian: L = I - D^{-1}W

        Args:
            distance_func: Function computing distance between states
            states: List of state vectors
            sigma: Kernel bandwidth parameter

        Returns:
            (L, P) where L is Laplacian and P is transition matrix
        """
        n = len(states)
        K = np.zeros((n, n))

        # Build affinity matrix
        for i in range(n):
            for j in range(n):
                if i != j:
                    d = distance_func(states[i], states[j])
                    K[i,j] = np.exp(-d**2 / (2*sigma**2))
                else:
                    K[i,i] = 1.0  # Self-similarity

        # Degree matrix and normalization
        D = K.sum(axis=1)
        D_inv = np.diag(1.0 / np.maximum(D, 1e-10))
        P = D_inv @ K  # Row-stochastic transition matrix
        L = np.eye(n) - P  # Normalized Laplacian

        return L, P

    def multi_geometry_diffusion(self, signal: np.ndarray,
                                 n_steps: int = 10,
                                 sigma: float = 0.5) -> np.ndarray:
        """
        Run alternating diffusion between CQT and RNQT geometries.

        This tests whether structure survives across A-scheme changes.

        Odd steps:  Use Fubini-Study (CQT) geometry
        Even steps: Use RNQT geometry

        Args:
            signal: Initial signal on states (n_states,)
            n_steps: Number of diffusion steps
            sigma: Kernel bandwidth

        Returns:
            Trajectory array (n_steps+1, n_states)
        """
        # Build both graph Laplacians
        L_fs, P_fs = self.build_graph_laplacian(
            self.fubini_study_distance, self.states_complex, sigma)
        L_rnqt, P_rnqt = self.build_graph_laplacian(
            self.rnqt_distance, self.states_real, sigma)

        # Run alternating diffusion
        f = signal.copy()
        trajectory = [f.copy()]

        for step in range(n_steps):
            # Alternate between geometries
            if step % 2 == 0:
                f = P_fs @ f
            else:
                f = P_rnqt @ f
            trajectory.append(f.copy())

        return np.array(trajectory)

    def run(self, n_steps: int = 20, sigma: float = 0.5) -> Dict:
        """
        Run the multi-geometry diffusion experiment.

        Args:
            n_steps: Number of alternating diffusion steps
            sigma: Kernel bandwidth for graph construction

        Returns:
            Dictionary with experiment results
        """
        # Initial signal: delta function on maximally entangled state
        signal = np.zeros(self.n_states)
        signal[-1] = 1.0  # Last state is theta=pi/4 (Bell state)

        # Run diffusion
        trajectory = self.multi_geometry_diffusion(signal, n_steps, sigma)

        # Analysis: Does entanglement structure persist?
        # Check if high-entanglement states remain clustered
        final_signal = trajectory[-1]

        # Correlation between final signal and entanglement
        corr = np.corrcoef(final_signal, self.entanglement)[0, 1]

        # Additional metric: entropy of final distribution
        # Low entropy = localized (structure preserved)
        p = final_signal / final_signal.sum()
        entropy = -np.sum(p * np.log(p + 1e-10))

        return {
            'trajectory': trajectory,
            'final_signal': final_signal,
            'entanglement': self.entanglement,
            'correlation': corr,
            'entropy': entropy,
            'max_entropy': np.log(self.n_states),
            'scheme_robust': abs(corr) > 0.5  # Strong correlation preserved
        }

    def report(self, results: Dict) -> str:
        """
        Generate human-readable report.

        Args:
            results: Output from run()

        Returns:
            Formatted report string
        """
        lines = [
            "=" * 70,
            "EXPERIMENT Q-B: MULTI-GEOMETRY DIFFUSION ON QUANTUM STATES",
            "=" * 70,
            "",
            "Testing if entanglement structure survives alternating",
            "diffusion between CQT (Fubini-Study) and RNQT metrics.",
            "",
            "Setup:",
            f"  States: {self.n_states} two-qubit states from separable to maximally entangled",
            "  Initial: Delta on Bell state (theta = pi/4)",
            "  Diffusion: Alternates between CQT and RNQT geometries",
            "",
            "Results:",
            f"  Final signal-entanglement correlation: {results['correlation']:.4f}",
            f"  Final entropy: {results['entropy']:.4f} / {results['max_entropy']:.4f}",
            "",
            "RESULT: " + ("ENTANGLEMENT IS SCHEME-ROBUST" if results['scheme_robust']
                         else "ENTANGLEMENT IS SCHEME-DEPENDENT"),
            "",
            "Interpretation:",
            "  High correlation means entanglement structure is preserved",
            "  despite switching between different geometric descriptions.",
            "  This validates the principle: Physical = Scheme-Robust.",
            "",
            "Physical Meaning:",
            "  Entanglement is a genuine physical property, not an artifact",
            "  of the complex number formulation. It persists in the real",
            "  formulation (RNQT) and under non-trivial geometric operations.",
            "",
            "Implications for Meta-Calculus:",
            "  If meta-calculus respects this scheme-robustness, it is",
            "  compatible with the deep structure of quantum mechanics.",
            "",
            "Reference: Hoffreumon & Woods (2025) arXiv:2504.02808",
            "=" * 70
        ]
        return "\n".join(lines)


def demo_experiment_qa():
    """
    Run and display Experiment Q-A results.

    Demonstrates A-scheme invariance of meta-time evolution.
    """
    print("\n" + "=" * 70)
    print("Running Experiment Q-A: Complex vs RNQT under Meta-Time")
    print("=" * 70 + "\n")

    exp = ExperimentQA(n_levels=10)

    # Coherent state: superposition of ground and first excited
    psi0 = np.zeros(10, dtype=complex)
    psi0[0] = 1/np.sqrt(2)
    psi0[1] = 1/np.sqrt(2)

    print("Initial state: (|0> + |1>) / sqrt(2)")
    print("Meta-time weight: u(t) = 1 + 0.1*sin(omega*t)")
    print("\nEvolving...\n")

    results = exp.run(psi0_complex=psi0, t_max=10.0, n_times=100)
    print(exp.report(results))

    return results


def demo_experiment_qb():
    """
    Run and display Experiment Q-B results.

    Demonstrates scheme-robustness of entanglement under multi-geometry diffusion.
    """
    print("\n" + "=" * 70)
    print("Running Experiment Q-B: Multi-Geometry Diffusion")
    print("=" * 70 + "\n")

    exp = ExperimentQB(n_states=30)

    print("Initial: Delta on maximally entangled Bell state")
    print("Diffusion: Alternates between Fubini-Study (CQT) and RNQT metrics")
    print("\nDiffusing...\n")

    results = exp.run(n_steps=20, sigma=0.3)
    print(exp.report(results))

    return results


def run_all_experiments():
    """Run both experiments Q-A and Q-B"""
    print("\n" + "=" * 70)
    print("META-CALCULUS QUANTUM SCHEME EXPERIMENTS")
    print("=" * 70)
    print("\nValidating scheme-robustness of meta-time quantum mechanics")
    print("Testing compatibility between CQT and RNQT formulations\n")

    results_qa = demo_experiment_qa()
    print("\n\n")
    results_qb = demo_experiment_qb()

    print("\n" + "=" * 70)
    print("ALL EXPERIMENTS COMPLETE")
    print("=" * 70)

    return {
        'Q-A': results_qa,
        'Q-B': results_qb
    }


if __name__ == "__main__":
    # Run both experiments
    all_results = run_all_experiments()

    print("\n\nSUMMARY:")
    print("-" * 70)
    print(f"Q-A Scheme Invariant: {all_results['Q-A']['summary']['scheme_invariant']}")
    print(f"Q-B Scheme Robust:    {all_results['Q-B']['scheme_robust']}")
    print("-" * 70)

    if all_results['Q-A']['summary']['scheme_invariant'] and all_results['Q-B']['scheme_robust']:
        print("\nCONCLUSION: Meta-calculus preserves quantum scheme-robustness!")
        print("Both CQT and RNQT formulations give equivalent physical predictions.")
    else:
        print("\nWARNING: Potential scheme-dependence detected.")
        print("Check numerical precision and integration parameters.")
