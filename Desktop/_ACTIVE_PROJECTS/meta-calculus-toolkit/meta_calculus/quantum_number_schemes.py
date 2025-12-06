#!/usr/bin/env python3
"""
Real Number Quantum Theory (RNQT): Scheme-Independent Formulation

This module implements the Real Number Quantum Theory (RNQT) from
Hoffreumon & Woods (2025) arXiv:2504.02808, demonstrating that quantum
mechanics can be formulated entirely with real numbers.

KEY INSIGHT:
    Quantum theory's predictions are independent of the number system
    (real vs complex vs quaternion) used to represent states and observables.
    Observable predictions are "scheme-robust" - they depend only on the
    algebraic structure, not the specific number field.

MAIN RESULTS:
    1. The Gamma map embeds complex Hermitian into real symmetric matrices
    2. The tensor_r composition rule preserves quantum structure in R
    3. Complex QT and Real NQT give IDENTICAL experimental predictions
    4. Scheme independence: observables are always real-valued

CONNECTIONS TO META-CALCULUS:
    - Scheme-robust observables (this module extends that concept)
    - Number system choice is analogous to calculus choice
    - Physical predictions are invariant across schemes

References:
    - Hoffreumon & Woods (2025) "Real Number Quantum Theory" arXiv:2504.02808
    - Renou et al. (2021) "Quantum theory based on real numbers" arXiv:2101.10873
    - Stueckelberg (1960) "Quantum theory in real Hilbert space"

Usage:
    python -m meta_calculus.quantum_number_schemes demo
    python -m meta_calculus.quantum_number_schemes compare --state bell
"""

import numpy as np
from typing import Tuple, Dict, List, Callable, Optional, Any
from abc import ABC, abstractmethod
import argparse
import sys


# =============================================================================
# CORE REAL NUMBER QUANTUM THEORY STRUCTURES
# =============================================================================

# The J matrix: Real representation of imaginary unit i
# J^2 = -I, making it act like i but with real entries
J = np.array([[0, -1], [1, 0]], dtype=float)

# The I2 matrix: 2x2 identity (used in Kronecker products)
I2 = np.array([[1, 0], [0, 1]], dtype=float)


def is_hermitian(H: np.ndarray, tol: float = 1e-10) -> bool:
    """Check if complex matrix is Hermitian: H = H^dagger."""
    if not np.iscomplexobj(H):
        # Real matrix is Hermitian iff symmetric
        return np.allclose(H, H.T, atol=tol)
    return np.allclose(H, H.conj().T, atol=tol)


def is_special_symmetric(M: np.ndarray, tol: float = 1e-10) -> bool:
    """
    Check if M is in SY_n(R): special symmetric matrices.

    The Gamma map I2 tensor Re(H) + J tensor Im(H) produces a matrix
    with a specific block structure. For an n x n Hermitian H,
    Gamma(H) is 2n x 2n and can be viewed as blocks indexed by pairs (i,a)
    where i in {1,...,n} and a in {0,1}.

    The key property: M is real and symmetric, arising from Gamma map.

    Args:
        M: Real matrix of size 2n x 2n
        tol: Numerical tolerance

    Returns:
        True if M is real and symmetric (image of Gamma)
    """
    if not np.isrealobj(M):
        return False

    # Must be symmetric
    if not np.allclose(M, M.T, atol=tol):
        return False

    # Dimension must be even
    n = M.shape[0]
    if n % 2 != 0:
        return False

    # That's the key structural requirement for Gamma image
    # The full characterization is subtle, but real + symmetric is necessary
    return True


def gamma_map(H: np.ndarray) -> np.ndarray:
    """
    Gamma map: Herm_n(C) --> SY_{2n}(R).

    Maps complex Hermitian H to real symmetric matrix:
        Gamma(H) = I2 tensor Re(H) + J tensor Im(H)

    Where tensor is Kronecker product, I2 = [[1,0],[0,1]], J = [[0,-1],[1,0]].

    The resulting 2n x 2n matrix is real and symmetric.

    KEY PROPERTY: Eigenvalues of Gamma(H) are eigenvalues of H (doubled).

    Args:
        H: Complex Hermitian matrix of size n x n

    Returns:
        Real symmetric matrix of size 2n x 2n

    Example:
        >>> H = np.array([[1, 1+2j], [1-2j, 3]])  # Hermitian
        >>> S = gamma_map(H)  # 4x4 real symmetric
        >>> np.linalg.eigvalsh(H)  # [complex eigenvalues]
        >>> np.linalg.eigvalsh(S)  # [same values, each appearing twice]
    """
    assert is_hermitian(H), "Input must be Hermitian"

    Re_H = np.real(H)
    Im_H = np.imag(H)

    # Gamma(H) = I2 tensor Re(H) + J tensor Im(H)
    result = np.kron(I2, Re_H) + np.kron(J, Im_H)

    assert is_special_symmetric(result), "Gamma output must be special symmetric"

    return result


def inverse_gamma_map(S: np.ndarray) -> np.ndarray:
    """
    Inverse Gamma map: SY_{2n}(R) --> Herm_n(C).

    Extract complex Hermitian from real symmetric matrix.

    For S = Gamma(H) = I2 tensor Re(H) + J tensor Im(H), the structure is:
        I2 tensor Re(H) = [[Re(H), 0], [0, Re(H)]]
        J tensor Im(H)  = [[0, -Im(H)], [Im(H), 0]]
        S = [[Re(H), -Im(H)], [Im(H), Re(H)]]

    So we can extract:
        Re(H) = S[:n, :n]  (top-left block)
        Im(H) = S[n:, :n]  (bottom-left block)

    Args:
        S: Real special symmetric matrix of size 2n x 2n

    Returns:
        Complex Hermitian matrix of size n x n
    """
    assert is_special_symmetric(S), "Input must be special symmetric"

    n_total = S.shape[0]
    n = n_total // 2

    # Extract n x n blocks from 2n x 2n matrix
    # S = [[A, B], [C, D]] where A = Re(H), C = Im(H)
    Re_H = S[:n, :n]  # Top-left block
    Im_H = S[n:, :n]  # Bottom-left block

    # Reconstruct H = Re(H) + i*Im(H)
    H = Re_H + 1j * Im_H

    assert is_hermitian(H), "Inverse Gamma output must be Hermitian"

    return H


def tensor_r(S: np.ndarray, T: np.ndarray) -> np.ndarray:
    """
    Alternative tensor product for RNQT: tensor_r.

    This is the KEY innovation of RNQT. While standard Kronecker product
    S tensor T doesn't preserve the special symmetric structure, tensor_r does.

    KEY PROPERTY:
        If S = Gamma(H1) and T = Gamma(H2), then
        tensor_r(S, T) = Gamma(H1 tensor H2)

        Meaning: tensor_r is compatible with Gamma map!

    Implementation: Since we know S = Gamma(H1) and T = Gamma(H2),
    we can extract H1, H2, compute H1 tensor H2, then Gamma map back.

    Args:
        S, T: Special symmetric real matrices (from Gamma map)

    Returns:
        Special symmetric real matrix (composite state)

    Example:
        >>> # Two-qubit state from tensor product
        >>> H1 = np.array([[1, 0], [0, -1]])  # sigma_z
        >>> H2 = np.array([[0, 1], [1, 0]])   # sigma_x
        >>> S1 = gamma_map(H1)
        >>> S2 = gamma_map(H2)
        >>> S12_r = tensor_r(S1, S2)  # Composite in RNQT
        >>> S12_c = gamma_map(np.kron(H1, H2))  # Composite in CQT
        >>> np.allclose(S12_r, S12_c)  # True!
    """
    # Extract the underlying complex Hermitian matrices
    H1 = inverse_gamma_map(S)
    H2 = inverse_gamma_map(T)

    # Compute complex Kronecker product
    H12 = np.kron(H1, H2)

    # Gamma map back to real representation
    result = gamma_map(H12)

    return result


# =============================================================================
# ALGEBRA SCHEMES: ABSTRACT INTERFACE FOR NUMBER SYSTEM CHOICE
# =============================================================================

class AlgebraScheme(ABC):
    """
    Abstract base class for algebra schemes (A-schemes).

    An A-scheme defines the number system and composition rules for
    quantum theory:
        - field: Number field (real, complex, quaternion, etc.)
        - composition_rule: How to combine multipartite states
        - representation_locality: Whether local operations remain local

    KEY INSIGHT (Hoffreumon-Woods):
        Different A-schemes can give IDENTICAL experimental predictions.
        Physical observables are "scheme-robust" - independent of number choice.

    This is analogous to scheme-robust observables in multi-calculus framework:
        calculus choice ~ number system choice
        invariant features ~ scheme-robust observables
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name for this scheme."""
        pass

    @property
    @abstractmethod
    def number_field(self) -> str:
        """Number field used: 'real', 'complex', 'quaternion', etc."""
        pass

    @abstractmethod
    def state_dim(self, base_dim: int) -> int:
        """
        Return state space dimension for base_dim-dimensional Hilbert space.

        Args:
            base_dim: Dimension of physical Hilbert space (e.g., 2 for qubit)

        Returns:
            Dimension of state representation in this scheme

        Example:
            Complex QT: qubit has dim=2 (2 complex amplitudes)
            Real NQT:   qubit has dim=4 (2x2 real symmetric matrix)
        """
        pass

    @abstractmethod
    def compose(self, rho1: np.ndarray, rho2: np.ndarray) -> np.ndarray:
        """
        Compose two states using this scheme's tensor product.

        Args:
            rho1, rho2: State matrices in this scheme's representation

        Returns:
            Composite state rho1 tensor rho2
        """
        pass

    @abstractmethod
    def observable_expectation(self, state: np.ndarray, observable: np.ndarray) -> float:
        """
        Compute expectation value of observable in given state.

        This MUST always return a real number (Born rule).

        Args:
            state: State matrix
            observable: Observable operator (self-adjoint)

        Returns:
            <observable> = Tr(state * observable)  [real number]
        """
        pass

    @abstractmethod
    def create_pure_state(self, amplitudes: np.ndarray) -> np.ndarray:
        """
        Create pure state from amplitude vector.

        Args:
            amplitudes: Amplitude vector (may be complex for CQT)

        Returns:
            State matrix in this scheme's representation
        """
        pass

    @abstractmethod
    def create_observable(self, matrix: np.ndarray) -> np.ndarray:
        """
        Create observable from Hermitian matrix.

        Args:
            matrix: Hermitian matrix (complex for CQT)

        Returns:
            Observable in this scheme's representation
        """
        pass


class ComplexQT(AlgebraScheme):
    """
    Standard complex quantum theory (CQT).

    States: Positive semidefinite Hermitian matrices on C^n
    Composition: Standard Kronecker tensor product
    Observables: Hermitian matrices
    Expectation: <O> = Tr(rho * O)
    """

    @property
    def name(self) -> str:
        return "Complex Quantum Theory (CQT)"

    @property
    def number_field(self) -> str:
        return "complex"

    def state_dim(self, base_dim: int) -> int:
        return base_dim

    def compose(self, rho1: np.ndarray, rho2: np.ndarray) -> np.ndarray:
        """Standard Kronecker product."""
        return np.kron(rho1, rho2)

    def observable_expectation(self, state: np.ndarray, observable: np.ndarray) -> float:
        """<O> = Tr(rho * O)."""
        result = np.trace(state @ observable)
        # Must be real for Hermitian observable
        assert np.abs(np.imag(result)) < 1e-10, "Expectation must be real"
        return np.real(result)

    def create_pure_state(self, amplitudes: np.ndarray) -> np.ndarray:
        """rho = |psi><psi| from amplitude vector."""
        psi = amplitudes / np.linalg.norm(amplitudes)  # normalize
        return np.outer(psi, psi.conj())

    def create_observable(self, matrix: np.ndarray) -> np.ndarray:
        """Observable is just the Hermitian matrix."""
        assert is_hermitian(matrix), "Observable must be Hermitian"
        return matrix


class RealNQT(AlgebraScheme):
    """
    Real Number Quantum Theory (RNQT) from Hoffreumon & Woods (2025).

    States: Special symmetric matrices SY_{2n}(R)
    Composition: Alternative tensor product tensor_r
    Observables: Special symmetric matrices (from Gamma map)
    Expectation: <O> = Tr(rho * O) / 2  [factor of 2 from doubling]

    KEY THEOREM (Hoffreumon-Woods):
        For any observable O and state rho in CQT,
        <O>_CQT = <Gamma(O)>_RNQT

        Meaning: RNQT reproduces all CQT predictions exactly!
    """

    @property
    def name(self) -> str:
        return "Real Number Quantum Theory (RNQT)"

    @property
    def number_field(self) -> str:
        return "real"

    def state_dim(self, base_dim: int) -> int:
        """RNQT doubles the dimension: 2n x 2n real for n x n complex."""
        return 2 * base_dim

    def compose(self, rho1: np.ndarray, rho2: np.ndarray) -> np.ndarray:
        """Use tensor_r instead of standard Kronecker."""
        return tensor_r(rho1, rho2)

    def observable_expectation(self, state: np.ndarray, observable: np.ndarray) -> float:
        """
        <O> = Tr(rho * O) / 2.

        Factor of 2 accounts for eigenvalue doubling in Gamma map.
        """
        result = np.trace(state @ observable) / 2
        return result

    def create_pure_state(self, amplitudes: np.ndarray) -> np.ndarray:
        """
        Create RNQT state from complex amplitudes.

        Steps:
            1. Form CQT density matrix: rho_C = |psi><psi|
            2. Apply Gamma map: rho_R = Gamma(rho_C)
        """
        # Normalize
        psi = amplitudes / np.linalg.norm(amplitudes)

        # CQT density matrix
        rho_complex = np.outer(psi, psi.conj())

        # Gamma map to RNQT
        rho_real = gamma_map(rho_complex)

        return rho_real

    def create_observable(self, matrix: np.ndarray) -> np.ndarray:
        """
        Create RNQT observable from complex Hermitian matrix.

        Simply apply Gamma map.
        """
        assert is_hermitian(matrix), "Observable must be Hermitian"
        return gamma_map(matrix)


# =============================================================================
# SCHEME EQUIVALENCE TESTING
# =============================================================================

class SchemeEquivalenceTest:
    """
    Test whether two A-schemes give identical predictions.

    KEY INSIGHT FROM HOFFREUMON-WOODS:
        CQT and RNQT are experimentally indistinguishable because:
        1. Observables are Hermitian --> eigenvalues are real
        2. Probabilities = |amplitude|^2 are real
        3. The Gamma map preserves all observable statistics

    This is a manifestation of "scheme robustness": physical predictions
    are invariant under number system choice (real vs complex).

    ANALOGY TO META-CALCULUS:
        Number system choice ~ Calculus choice
        Scheme-robust observable ~ Calculus-invariant feature
        Gamma map ~ Coordinate transformation
    """

    def __init__(self, scheme1: AlgebraScheme, scheme2: AlgebraScheme):
        """
        Initialize equivalence tester.

        Args:
            scheme1, scheme2: Algebra schemes to compare
        """
        self.scheme1 = scheme1
        self.scheme2 = scheme2

    def compare_expectations(
        self,
        amplitudes: np.ndarray,
        observable_complex: np.ndarray,
        tolerance: float = 1e-10
    ) -> Dict[str, Any]:
        """
        Compare expectation values across schemes for same physical state/observable.

        Args:
            amplitudes: Complex amplitude vector (physical state)
            observable_complex: Complex Hermitian matrix (physical observable)
            tolerance: Numerical tolerance for equality

        Returns:
            Dictionary with comparison results
        """
        # Create states in both schemes
        state1 = self.scheme1.create_pure_state(amplitudes)
        state2 = self.scheme2.create_pure_state(amplitudes)

        # Create observables in both schemes
        obs1 = self.scheme1.create_observable(observable_complex)
        obs2 = self.scheme2.create_observable(observable_complex)

        # Compute expectation values
        expect1 = self.scheme1.observable_expectation(state1, obs1)
        expect2 = self.scheme2.observable_expectation(state2, obs2)

        # Compare
        difference = abs(expect1 - expect2)
        equivalent = difference < tolerance

        return {
            'scheme1_name': self.scheme1.name,
            'scheme2_name': self.scheme2.name,
            'expectation_scheme1': expect1,
            'expectation_scheme2': expect2,
            'difference': difference,
            'equivalent': equivalent,
            'tolerance': tolerance
        }

    def is_scheme_robust(
        self,
        amplitudes_list: List[np.ndarray],
        observables_list: List[np.ndarray],
        tolerance: float = 1e-10
    ) -> Dict[str, Any]:
        """
        Check if observables give same results in both schemes across multiple tests.

        Args:
            amplitudes_list: List of state vectors to test
            observables_list: List of observables to test
            tolerance: Numerical tolerance

        Returns:
            Dictionary with robustness test results
        """
        all_comparisons = []

        for amplitudes in amplitudes_list:
            for observable in observables_list:
                result = self.compare_expectations(amplitudes, observable, tolerance)
                all_comparisons.append(result)

        # Check if all comparisons show equivalence
        all_equivalent = all(comp['equivalent'] for comp in all_comparisons)
        max_difference = max(comp['difference'] for comp in all_comparisons)

        return {
            'scheme_robust': all_equivalent,
            'num_tests': len(all_comparisons),
            'max_difference': max_difference,
            'tolerance': tolerance,
            'comparisons': all_comparisons
        }


# =============================================================================
# QUANTUM STATES AND OBSERVABLES (EXAMPLES)
# =============================================================================

def pauli_matrices() -> Dict[str, np.ndarray]:
    """
    Pauli matrices (observables for qubit).

    Returns:
        Dictionary with sigma_x, sigma_y, sigma_z, identity
    """
    return {
        'I': np.array([[1, 0], [0, 1]], dtype=complex),
        'X': np.array([[0, 1], [1, 0]], dtype=complex),
        'Y': np.array([[0, -1j], [1j, 0]], dtype=complex),
        'Z': np.array([[1, 0], [0, -1]], dtype=complex)
    }


def bell_state(which: str = 'phi_plus') -> np.ndarray:
    """
    Create Bell state (maximally entangled two-qubit state).

    Args:
        which: Which Bell state ('phi_plus', 'phi_minus', 'psi_plus', 'psi_minus')

    Returns:
        Amplitude vector for Bell state (4 components)
    """
    states = {
        'phi_plus':  np.array([1, 0, 0, 1]) / np.sqrt(2),   # (|00> + |11>)/sqrt(2)
        'phi_minus': np.array([1, 0, 0, -1]) / np.sqrt(2),  # (|00> - |11>)/sqrt(2)
        'psi_plus':  np.array([0, 1, 1, 0]) / np.sqrt(2),   # (|01> + |10>)/sqrt(2)
        'psi_minus': np.array([0, 1, -1, 0]) / np.sqrt(2),  # (|01> - |10>)/sqrt(2)
    }

    return states[which]


def random_hermitian(n: int, seed: Optional[int] = None) -> np.ndarray:
    """
    Generate random Hermitian matrix.

    Args:
        n: Matrix dimension
        seed: Random seed for reproducibility

    Returns:
        n x n Hermitian matrix
    """
    if seed is not None:
        np.random.seed(seed)

    # Random complex matrix
    A = np.random.randn(n, n) + 1j * np.random.randn(n, n)

    # Make Hermitian
    H = (A + A.conj().T) / 2

    return H


def random_pure_state(n: int, seed: Optional[int] = None) -> np.ndarray:
    """
    Generate random pure state (normalized amplitude vector).

    Args:
        n: Hilbert space dimension
        seed: Random seed for reproducibility

    Returns:
        n-dimensional complex amplitude vector (normalized)
    """
    if seed is not None:
        np.random.seed(seed)

    # Random complex vector
    psi = np.random.randn(n) + 1j * np.random.randn(n)

    # Normalize
    psi /= np.linalg.norm(psi)

    return psi


# =============================================================================
# DEMONSTRATION AND VALIDATION
# =============================================================================

def demo_gamma_map():
    """Demonstrate Gamma map preserves eigenvalues."""
    print("\n" + "="*70)
    print("DEMO: Gamma Map - Eigenvalue Preservation")
    print("="*70)

    # Create random Hermitian matrix
    H = random_hermitian(3, seed=42)

    print("\nComplex Hermitian matrix H (3x3):")
    print(H)

    # Apply Gamma map
    S = gamma_map(H)

    print("\nGamma(H) - Real symmetric matrix (6x6):")
    print(S)

    # Check special symmetric structure
    print(f"\nIs special symmetric: {is_special_symmetric(S)}")

    # Compare eigenvalues
    eig_H = np.linalg.eigvalsh(H)
    eig_S = np.linalg.eigvalsh(S)

    print("\nEigenvalues of H:")
    print(eig_H)

    print("\nEigenvalues of Gamma(H) (should be each eigenvalue of H doubled):")
    print(eig_S)

    # Check doubling
    eig_H_doubled = np.sort(np.concatenate([eig_H, eig_H]))
    eig_S_sorted = np.sort(eig_S)

    print(f"\nEigenvalue doubling error: {np.max(np.abs(eig_H_doubled - eig_S_sorted)):.2e}")


def demo_tensor_r():
    """Demonstrate tensor_r compatibility with Gamma map."""
    print("\n" + "="*70)
    print("DEMO: tensor_r Compatibility with Gamma Map")
    print("="*70)

    # Create two Pauli matrices
    pauli = pauli_matrices()
    sigma_z = pauli['Z']
    sigma_x = pauli['X']

    print("\nPauli Z:")
    print(sigma_z)
    print("\nPauli X:")
    print(sigma_x)

    # Method 1: Compose in CQT, then Gamma
    H_composite_CQT = np.kron(sigma_z, sigma_x)
    S_method1 = gamma_map(H_composite_CQT)

    print("\nMethod 1: Z tensor X in CQT, then Gamma:")
    print(H_composite_CQT)

    # Method 2: Gamma each, then tensor_r
    S_z = gamma_map(sigma_z)
    S_x = gamma_map(sigma_x)
    S_method2 = tensor_r(S_z, S_x)

    print("\nMethod 2: Gamma(Z) tensor_r Gamma(X):")
    print(S_method2)

    # Compare
    difference = np.max(np.abs(S_method1 - S_method2))
    print(f"\nDifference between methods: {difference:.2e}")
    print(f"Methods agree: {difference < 1e-10}")


def demo_scheme_equivalence():
    """Demonstrate CQT and RNQT give identical predictions."""
    print("\n" + "="*70)
    print("DEMO: Scheme Equivalence - CQT vs RNQT")
    print("="*70)

    # Initialize schemes
    cqt = ComplexQT()
    rnqt = RealNQT()

    print(f"\nScheme 1: {cqt.name}")
    print(f"Scheme 2: {rnqt.name}")

    # Test 1: Single qubit measurement
    print("\n" + "-"*70)
    print("Test 1: Single Qubit - Measure Pauli Z on |+> state")
    print("-"*70)

    # State: |+> = (|0> + |1>)/sqrt(2)
    psi_plus = np.array([1, 1]) / np.sqrt(2)

    # Observable: Pauli Z
    pauli = pauli_matrices()
    sigma_z = pauli['Z']

    # Compare schemes
    tester = SchemeEquivalenceTest(cqt, rnqt)
    result = tester.compare_expectations(psi_plus, sigma_z)

    print(f"\nState: |+> = (|0> + |1>)/sqrt(2)")
    print(f"Observable: sigma_z")
    print(f"\nExpectation in CQT:  {result['expectation_scheme1']:.6f}")
    print(f"Expectation in RNQT: {result['expectation_scheme2']:.6f}")
    print(f"Difference: {result['difference']:.2e}")
    print(f"Schemes equivalent: {result['equivalent']}")

    # Test 2: Entangled state
    print("\n" + "-"*70)
    print("Test 2: Two Qubits - Bell State Correlations")
    print("-"*70)

    # State: Bell state |phi+> = (|00> + |11>)/sqrt(2)
    bell = bell_state('phi_plus')

    # Observable: Z tensor Z (correlation measurement)
    Z_tensor_Z = np.kron(pauli['Z'], pauli['Z'])

    result = tester.compare_expectations(bell, Z_tensor_Z)

    print(f"\nState: Bell state |phi+> = (|00> + |11>)/sqrt(2)")
    print(f"Observable: Z tensor Z (correlation)")
    print(f"\nExpectation in CQT:  {result['expectation_scheme1']:.6f}")
    print(f"Expectation in RNQT: {result['expectation_scheme2']:.6f}")
    print(f"Difference: {result['difference']:.2e}")
    print(f"Schemes equivalent: {result['equivalent']}")

    # Test 3: Multiple random tests
    print("\n" + "-"*70)
    print("Test 3: Scheme Robustness - 100 Random States & Observables")
    print("-"*70)

    # Generate random test cases
    states_1qubit = [random_pure_state(2, seed=i) for i in range(10)]
    states_2qubit = [random_pure_state(4, seed=i+100) for i in range(10)]
    obs_1qubit = [random_hermitian(2, seed=i+200) for i in range(5)]
    obs_2qubit = [random_hermitian(4, seed=i+300) for i in range(5)]

    # Test 1-qubit systems
    result_1q = tester.is_scheme_robust(states_1qubit, obs_1qubit)

    print(f"\n1-Qubit Systems:")
    print(f"  Tests: {result_1q['num_tests']}")
    print(f"  Max difference: {result_1q['max_difference']:.2e}")
    print(f"  Scheme robust: {result_1q['scheme_robust']}")

    # Test 2-qubit systems
    result_2q = tester.is_scheme_robust(states_2qubit, obs_2qubit)

    print(f"\n2-Qubit Systems:")
    print(f"  Tests: {result_2q['num_tests']}")
    print(f"  Max difference: {result_2q['max_difference']:.2e}")
    print(f"  Scheme robust: {result_2q['scheme_robust']}")


def run_comprehensive_demo():
    """Run all demonstrations."""
    print("\n" + "="*70)
    print("REAL NUMBER QUANTUM THEORY (RNQT) - COMPREHENSIVE DEMO")
    print("="*70)
    print("\nReference: Hoffreumon & Woods (2025) arXiv:2504.02808")
    print("           'Real Number Quantum Theory'")

    demo_gamma_map()
    demo_tensor_r()
    demo_scheme_equivalence()

    print("\n" + "="*70)
    print("SUMMARY: Scheme Independence Verified")
    print("="*70)
    print("\nKEY RESULTS:")
    print("  1. Gamma map preserves eigenvalues (doubling)")
    print("  2. tensor_r is compatible with Gamma composition")
    print("  3. CQT and RNQT give IDENTICAL experimental predictions")
    print("  4. Observable expectations are scheme-robust (invariant)")
    print("\nCONCLUSION:")
    print("  Quantum theory can be formulated entirely with REAL numbers!")
    print("  Complex numbers are a CONVENIENCE, not a NECESSITY.")
    print("\nCONNECTION TO META-CALCULUS:")
    print("  Number system choice ~ Calculus choice")
    print("  Scheme-robust observables ~ Calculus-invariant features")
    print("  Both demonstrate: Physical = Invariant across representations")
    print("="*70 + "\n")


# =============================================================================
# COMMAND-LINE INTERFACE
# =============================================================================

def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Real Number Quantum Theory (RNQT) - Scheme Independence Demo'
    )

    parser.add_argument(
        'command',
        choices=['demo', 'gamma', 'tensor', 'compare'],
        help='Command to run'
    )

    parser.add_argument(
        '--state',
        choices=['plus', 'minus', 'bell', 'random'],
        default='plus',
        help='State to use for comparison'
    )

    parser.add_argument(
        '--observable',
        choices=['X', 'Y', 'Z', 'random'],
        default='Z',
        help='Observable to measure'
    )

    args = parser.parse_args()

    if args.command == 'demo':
        run_comprehensive_demo()

    elif args.command == 'gamma':
        demo_gamma_map()

    elif args.command == 'tensor':
        demo_tensor_r()

    elif args.command == 'compare':
        demo_scheme_equivalence()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # No arguments - run full demo
        run_comprehensive_demo()
    else:
        main()
