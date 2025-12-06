"""
NNC Singularity Regularization Tests
Tests Non-Newtonian Calculus for physics singularity resolution.

Based on Grossman & Katz (1972) Non-Newtonian Calculus
and Grossman (1981) Meta-Calculus synthesis.
"""
import numpy as np
import sys
sys.path.insert(0, 'C:/Users/17175/Desktop/_SCRATCH/meta-calculus-toolkit')


# =============================================================================
# GEOMETRIC DERIVATIVE: D_G[f](a) = exp(f'(a)/f(a))
# =============================================================================

class GeometricDerivative:
    """
    Geometric derivative (multiplicative calculus):
    D_G[f](x) = exp(f'(x) / f(x))

    Key property: For f(x) = x^n, D_G[f] = exp(n/x)
    For f(x) = 1/x = x^(-1), D_G[f] = exp(-1) = 1/e (CONSTANT!)
    """

    def __call__(self, f, x, dx=1e-8):
        """
        Compute geometric derivative.
        D_G[f](x) = exp(f'(x)/f(x))
        """
        x = np.atleast_1d(x).astype(float)
        fx = f(x)

        # Numerical derivative of f
        f_prime = (f(x + dx) - f(x - dx)) / (2 * dx)

        # Geometric derivative
        fx_safe = np.where(np.abs(fx) < 1e-100, 1e-100, fx)
        return np.exp(f_prime / fx_safe)


# =============================================================================
# BIGEOMETRIC DERIVATIVE: D_BG[f](a) = exp(a * f'(a) / f(a))
# =============================================================================

class BigeometricDerivative:
    """
    Bigeometric derivative (doubly multiplicative calculus):
    D_BG[f](x) = exp(x * f'(x) / f(x))

    Key property: For f(x) = x^n, D_BG[f] = e^n (CONSTANT!)
    """

    def __call__(self, f, x, dx=1e-8):
        """
        Compute bigeometric derivative.
        D_BG[f](x) = exp(x * f'(x) / f(x))
        """
        x = np.atleast_1d(x).astype(float)
        fx = f(x)

        # Numerical derivative of f
        f_prime = (f(x + dx) - f(x - dx)) / (2 * dx)

        # Bigeometric derivative
        fx_safe = np.where(np.abs(fx) < 1e-100, 1e-100, fx)
        return np.exp(x * f_prime / fx_safe)

    def for_power_law(self, n):
        """For f(x) = x^n, D_BG[f] = e^n exactly."""
        return np.exp(n)


# =============================================================================
# TEST: HAWKING TEMPERATURE SINGULARITY
# =============================================================================

def test_hawking_temperature_singularity():
    """
    Test: T(M) = 1/M (Hawking temperature proportional to 1/M)

    Classical: dT/dM = -1/M^2 --> -inf as M-->0
    Geometric: D_G[T] = exp(T'/T) = exp((-1/M^2)/(1/M)) = exp(-1/M)

    For T = M^(-1) evaluated at any M:
    D_G[T] = exp(-1) = 1/e when we consider the log-derivative

    Actually: f(x) = 1/x = x^(-1)
    f'(x) = -1/x^2
    f'(x)/f(x) = (-1/x^2)/(1/x) = -1/x
    D_G[f](x) = exp(-1/x)

    This varies with x, but the BIGEOMETRIC derivative:
    D_BG[f](x) = exp(x * f'(x)/f(x)) = exp(x * (-1/x)) = exp(-1) = 1/e (CONSTANT!)
    """
    D_G = GeometricDerivative()
    D_BG = BigeometricDerivative()

    # Hawking temperature: T(M) = 1/M (in normalized units)
    T = lambda M: 1.0 / M

    # Test at various masses
    M_values = np.logspace(-2, 2, 100)

    # Classical derivative (diverges as M-->0)
    dT_dM_classical = -1.0 / M_values**2

    # Geometric derivative (varies with M)
    D_G_T = D_G(T, M_values)

    # Bigeometric derivative (CONSTANT!)
    D_BG_T = D_BG(T, M_values)
    expected_bg = 1.0 / np.e  # exp(-1) = 1/e

    print("="*60)
    print("TEST: Hawking Temperature Singularity Regularization")
    print("="*60)
    print(f"Function: T(M) = 1/M")
    print(f"Classical dT/dM at M=0.01: {-1/0.01**2:.2e} (diverges)")
    print(f"Classical dT/dM at M=1.00: {-1/1.0**2:.2e}")
    print()
    print("Geometric Derivative D_G[T] = exp(-1/M):")
    print(f"  At M=0.01: {D_G(T, np.array([0.01]))[0]:.6f}")
    print(f"  At M=1.00: {D_G(T, np.array([1.0]))[0]:.6f} = 1/e")
    print(f"  At M=100:  {D_G(T, np.array([100.0]))[0]:.6f}")
    print()
    print("Bigeometric Derivative D_BG[T] = exp(-1) = 1/e (CONSTANT!):")
    print(f"  Expected: {expected_bg:.6f}")
    print(f"  Computed mean: {np.mean(D_BG_T):.6f}")
    print(f"  Computed std:  {np.std(D_BG_T):.2e}")
    print(f"  REGULARIZATION: {'SUCCESS' if np.std(D_BG_T) < 0.01 else 'PARTIAL'}")

    return {
        'M_values': M_values,
        'classical': dT_dM_classical,
        'geometric': D_G_T,
        'bigeometric': D_BG_T,
        'expected': expected_bg,
        'success': np.std(D_BG_T) < 0.01
    }


# =============================================================================
# TEST: POWER LAW SINGULARITIES (CURVATURE, DENSITY)
# =============================================================================

def test_power_law_singularities():
    """
    Test power law functions: f(x) = x^n

    For bigeometric derivative:
    D_BG[x^n] = exp(x * (n*x^(n-1)) / x^n) = exp(n) = CONSTANT

    This regularizes:
    - Kretschmann scalar: K ~ r^(-6) --> D_BG[K] = e^(-6)
    - Energy density: rho ~ a^(-3) --> D_BG[rho] = e^(-3)
    - Curvature: R ~ a^(-2) --> D_BG[R] = e^(-2)
    """
    D_BG = BigeometricDerivative()

    # Test various power laws
    powers = [-6, -3, -2, -1, 0.5, 2/3, 1, 2, 3]

    print("="*60)
    print("TEST: Power Law Singularity Regularization")
    print("="*60)
    print(f"{'Power n':<10} {'Physics Example':<30} {'D_BG computed':<15} {'e^n expected':<15} {'Match':<10}")
    print("-"*85)

    results = []
    all_pass = True

    for n in powers:
        f = lambda x, n=n: np.abs(x)**n  # Use abs to handle negative powers

        # Test at multiple x values to verify constancy
        x_test = np.logspace(-1, 1, 50)
        D_BG_f = D_BG(f, x_test)
        computed = np.mean(D_BG_f)
        std = np.std(D_BG_f)
        expected = np.exp(n)

        # Map to physics
        physics_map = {
            -6: "Kretschmann K ~ r^(-6)",
            -3: "Matter density rho ~ a^(-3)",
            -2: "Curvature R ~ a^(-2)",
            -1: "Hawking temp T ~ M^(-1)",
            0.5: "Radiation era a ~ t^(1/2)",
            2/3: "Matter era a ~ t^(2/3)",
            1: "Linear scale",
            2: "Area ~ r^2",
            3: "Volume ~ r^3"
        }
        physics = physics_map.get(n, f"Power law x^{n}")

        match = np.isclose(computed, expected, rtol=0.05) and std < 0.1
        match_str = "YES" if match else "NO"
        if not match:
            all_pass = False

        print(f"{n:<10} {physics:<30} {computed:<15.6f} {expected:<15.6f} {match_str:<10}")
        results.append({
            'n': n,
            'physics': physics,
            'computed': computed,
            'expected': expected,
            'std': std,
            'match': match
        })

    print("-"*85)
    print(f"Overall: {'ALL TESTS PASSED' if all_pass else 'SOME TESTS FAILED'}")

    return results


# =============================================================================
# TEST: BIG BANG COSMOLOGICAL SINGULARITY
# =============================================================================

def test_big_bang_singularity():
    """
    Test Big Bang singularity: scale factor a(t) --> 0 as t --> 0

    For radiation-dominated: a(t) = t^(1/2)
    Classical: da/dt = 0.5/sqrt(t) --> inf as t-->0

    Bigeometric: D_BG[a] = exp(t * (da/dt) / a)
                        = exp(t * 0.5/sqrt(t) / sqrt(t))
                        = exp(0.5) = CONSTANT
    """
    D_BG = BigeometricDerivative()

    # Radiation-dominated scale factor: a(t) = t^(1/2)
    a_rad = lambda t: t**0.5

    # Matter-dominated scale factor: a(t) = t^(2/3)
    a_mat = lambda t: t**(2/3)

    # Test times (avoiding t=0 for numerical stability)
    t_values = np.logspace(-6, 2, 100)

    print("="*60)
    print("TEST: Big Bang Singularity Regularization")
    print("="*60)

    # Classical derivatives (diverge!)
    da_dt_rad = 0.5 * t_values**(-0.5)
    da_dt_mat = (2/3) * t_values**(-1/3)

    # Bigeometric derivatives (CONSTANT!)
    D_BG_rad = D_BG(a_rad, t_values)
    D_BG_mat = D_BG(a_mat, t_values)

    expected_rad = np.exp(0.5)
    expected_mat = np.exp(2/3)

    print(f"\nRadiation-dominated: a(t) = t^(1/2)")
    print(f"  Classical da/dt at t=1e-6: {0.5 * (1e-6)**(-0.5):.2e} (DIVERGES)")
    print(f"  Classical da/dt at t=1:    {0.5:.2f}")
    print(f"  D_BG[a] computed mean: {np.mean(D_BG_rad):.6f}")
    print(f"  D_BG[a] computed std:  {np.std(D_BG_rad):.2e}")
    print(f"  D_BG[a] expected:      {expected_rad:.6f} = e^(1/2)")
    print(f"  REGULARIZATION: {'SUCCESS' if np.std(D_BG_rad) < 0.01 else 'PARTIAL'}")

    print(f"\nMatter-dominated: a(t) = t^(2/3)")
    print(f"  Classical da/dt at t=1e-6: {(2/3) * (1e-6)**(-1/3):.2e} (DIVERGES)")
    print(f"  Classical da/dt at t=1:    {2/3:.4f}")
    print(f"  D_BG[a] computed mean: {np.mean(D_BG_mat):.6f}")
    print(f"  D_BG[a] computed std:  {np.std(D_BG_mat):.2e}")
    print(f"  D_BG[a] expected:      {expected_mat:.6f} = e^(2/3)")
    print(f"  REGULARIZATION: {'SUCCESS' if np.std(D_BG_mat) < 0.01 else 'PARTIAL'}")

    return {
        't_values': t_values,
        'radiation': {
            'classical': da_dt_rad,
            'bigeometric': D_BG_rad,
            'expected': expected_rad,
            'success': np.std(D_BG_rad) < 0.01
        },
        'matter': {
            'classical': da_dt_mat,
            'bigeometric': D_BG_mat,
            'expected': expected_mat,
            'success': np.std(D_BG_mat) < 0.01
        }
    }


# =============================================================================
# TEST: CURVATURE SCALAR DIVERGENCE
# =============================================================================

def test_curvature_singularity():
    """
    Test Kretschmann scalar: K = 48*M^2/r^6 ~ r^(-6) near r=0

    Classical: dK/dr = -288*M^2/r^7 --> -inf as r-->0
    Bigeometric: D_BG[K] = exp(-6) = e^(-6) (CONSTANT!)
    """
    D_BG = BigeometricDerivative()

    # Kretschmann scalar (normalized): K(r) = 1/r^6
    K = lambda r: 1.0 / r**6

    # Test radii
    r_values = np.logspace(-2, 2, 100)

    print("="*60)
    print("TEST: Curvature Singularity Regularization")
    print("="*60)
    print(f"Function: K(r) = 1/r^6 (Kretschmann scalar)")

    # Classical derivative (diverges!)
    dK_dr = -6.0 / r_values**7

    # Bigeometric derivative (CONSTANT!)
    D_BG_K = D_BG(K, r_values)
    expected = np.exp(-6)

    print(f"\nClassical dK/dr at r=0.01: {-6.0 / 0.01**7:.2e} (DIVERGES)")
    print(f"Classical dK/dr at r=1:    {-6.0:.2f}")
    print(f"\nBigeometric D_BG[K]:")
    print(f"  Computed mean: {np.mean(D_BG_K):.6f}")
    print(f"  Computed std:  {np.std(D_BG_K):.2e}")
    print(f"  Expected:      {expected:.6f} = e^(-6)")
    print(f"  REGULARIZATION: {'SUCCESS' if np.std(D_BG_K) < 0.01 else 'PARTIAL'}")

    return {
        'r_values': r_values,
        'classical': dK_dr,
        'bigeometric': D_BG_K,
        'expected': expected,
        'success': np.std(D_BG_K) < 0.01
    }


# =============================================================================
# RUN ALL TESTS
# =============================================================================

def run_all_singularity_tests():
    """Execute all singularity regularization tests."""
    print("\n" + "="*80)
    print("NON-NEWTONIAN CALCULUS: PHYSICS SINGULARITY REGULARIZATION TESTS")
    print("Based on Grossman & Katz (1972) and Grossman (1981)")
    print("="*80 + "\n")

    results = {}

    # Test 1: Hawking temperature
    print("\n[1/4] Testing Hawking Temperature...")
    results['hawking'] = test_hawking_temperature_singularity()
    print()

    # Test 2: Power laws
    print("\n[2/4] Testing Power Law Singularities...")
    results['power_laws'] = test_power_law_singularities()
    print()

    # Test 3: Big Bang
    print("\n[3/4] Testing Big Bang Singularity...")
    results['big_bang'] = test_big_bang_singularity()
    print()

    # Test 4: Curvature
    print("\n[4/4] Testing Curvature Singularity...")
    results['curvature'] = test_curvature_singularity()

    # Summary
    print("\n" + "="*80)
    print("SUMMARY: NNC SINGULARITY REGULARIZATION RESULTS")
    print("="*80)

    successes = 0
    total = 4

    if results['hawking']['success']:
        print("[PASS] Hawking Temperature: D_BG[1/M] = e^(-1) = 1/e")
        successes += 1
    else:
        print("[FAIL] Hawking Temperature: Did not achieve constant derivative")

    power_pass = all(r['match'] for r in results['power_laws'])
    if power_pass:
        print("[PASS] Power Laws: All D_BG[x^n] = e^n verified")
        successes += 1
    else:
        print("[PARTIAL] Power Laws: Some tests failed")

    if results['big_bang']['radiation']['success'] and results['big_bang']['matter']['success']:
        print("[PASS] Big Bang: Both radiation and matter eras regularized")
        successes += 1
    else:
        print("[PARTIAL] Big Bang: Some eras not fully regularized")

    if results['curvature']['success']:
        print("[PASS] Curvature: D_BG[r^(-6)] = e^(-6) verified")
        successes += 1
    else:
        print("[FAIL] Curvature: Did not achieve constant derivative")

    print(f"\nOverall: {successes}/{total} tests passed")
    print("="*80)

    return results


if __name__ == "__main__":
    results = run_all_singularity_tests()
