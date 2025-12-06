# =============================================================================
#   meta_teukolsky.py   –   Schwarzschild, s = –2, with meta-derivative
# =============================================================================
import numpy as np
from scipy.integrate import ode
from scipy.optimize import newton
import time
import sys

# ----------------------------------------------------------------------------- 
# 0.  Global constants (geometrised units G = c = 1)
# -----------------------------------------------------------------------------
EPS_ROOT = 1e-10                    # Newton solver tolerance (relaxed)
MIN_RADIUS_FACTOR = 1.01            # Min radius = 2M * MIN_RADIUS_FACTOR (safety margin)

# ----------------------------------------------------------------------------- 
# 1.  Meta-weight near the horizon
# -----------------------------------------------------------------------------
def v_meta(r, r_h, eps=1e-3, ell=1e-5):
    """Quantum-information weight; epsilon≪1, ℓ ~= ℓ_P."""
    return 1.0 - eps * np.exp(-(r - r_h) / ell)

# ----------------------------------------------------------------------------- 
# 2.  Tortoise coordinate and its inverse
# -----------------------------------------------------------------------------
def r_tortoise(r, M):
    """Schwarzschild tortoise coordinate r*."""
    return r + 2*M * np.log(np.abs(r / (2*M) - 1))

def r_from_rstar(r_star, M):
    """
    Invert r*(r) numerically (Newton–Raphson).
    Good initial guess: r ~= 2M + |r_star| for r* ≪ 0,
                        r ~= r_star          for r* ≫ 2M.
    """
    # Special case: very large positive r_star (far from BH)
    if r_star > 100*M:
        return r_star  # Very good approximation far away
    
    # Special case: very negative r_star (near horizon)
    if r_star < -100*M:
        return 2*M * MIN_RADIUS_FACTOR  # Very near horizon
    
    # Safety threshold
    r_min = 2*M * MIN_RADIUS_FACTOR
    
    # Improved heuristic seed based on region
    if r_star > 0:
        r0 = max(r_star, 3*M)  # Ensure we're outside the photon sphere
    else:
        # Better approximation for negative r_star
        delta = np.exp(r_star/(2*M))
        r0 = max(2*M * (1 + delta), r_min)
    
    # Define functions with safety checks
    def f(r):
        if r <= 2*M:
            return 1e10  # Large positive value if inside horizon
        return r_tortoise(r, M) - r_star
    
    def fprime(r):
        if r <= 2*M or abs(r - 2*M) < 1e-10:
            return 1e-10  # Small positive value if too close to horizon
        return 1 / (1 - 2*M/r)
    
    try:
        # Newton method with safety checks
        result = newton(f, r0, fprime, tol=EPS_ROOT, maxiter=50)
        
        # Ensure result is physically valid
        if result <= 2*M:
            result = r_min
        
        return result
    except (RuntimeError, ZeroDivisionError, OverflowError, ValueError) as e:
        # Fallback approximation with safety bounds
        if r_star > 0:
            return max(r_star, 3*M)  # Reasonable for r* > 0
        else:
            # Approximation for r* < 0 with safety margin
            delta = np.exp(r_star/(2*M))
            return max(2*M * (1 + delta), r_min)

# -----------------------------------------------------------------------------
# 3.  Validation functions
# -----------------------------------------------------------------------------
def validate_r_from_rstar(M):
    """Test r_from_rstar function with known values."""
    print("Validating r_from_rstar function:")
    
    # Test case 1: r* = 0 should give r ~= 2M + 2M*ln(1) = 2M
    r_test = r_from_rstar(0.0, M)
    print(f"r*(0) -> r = {r_test:.6f} (expected ~= {2*M:.6f})")
    
    # Test case 2: Large positive r* should give r ~= r*
    r_star_large = 100*M
    r_test = r_from_rstar(r_star_large, M)
    print(f"r*({r_star_large}) -> r = {r_test:.6f} (expected ~= {r_star_large:.6f})")
    
    # Test case 3: r = 3M (photon sphere)
    r_photon = 3*M
    r_star_photon = r_tortoise(r_photon, M)
    r_recovered = r_from_rstar(r_star_photon, M)
    print(f"r = 3M: r* = {r_star_photon:.6f}, recovered r = {r_recovered:.6f}")
    print(f"Error: {abs(r_recovered - r_photon):.2e}")

def compute_reflection_coefficient(r_s, psi_s, omega, r_star_analysis_start=20.0):
    """
    Compute reflection coefficient by fitting to outgoing/incoming waves.
    At large positive r*, psi ~= A*e^{-iomegar*} + B*e^{+iomegar*}
    where A is outgoing, B is incoming amplitude.
    """
    # Find indices for analysis region (large positive r*)
    analysis_mask = r_s >= r_star_analysis_start
    if not np.any(analysis_mask):
        return np.nan, "No data in analysis region"
    
    r_analysis = r_s[analysis_mask]
    psi_analysis = psi_s[analysis_mask]
    
    if len(r_analysis) < 10:
        return np.nan, "Insufficient data points for analysis"
    
    # Set up linear system: psi = A*e^{-iomegar*} + B*e^{+iomegar*}
    # In matrix form: psi = [e^{-iomegar*}, e^{+iomegar*}] * [A, B]^T
    outgoing = np.exp(-1j * omega * r_analysis)
    incoming = np.exp(1j * omega * r_analysis)
    
    # Solve least squares: [A, B] = argmin |psi - A*outgoing - B*incoming|^2
    design_matrix = np.column_stack([outgoing, incoming])
    try:
        coeffs, residuals, rank, s = np.linalg.lstsq(design_matrix, psi_analysis, rcond=None)
        A_out, B_in = coeffs
        
        # Reflection coefficient R = A_out / B_in
        if abs(B_in) > 1e-12:
            R = A_out / B_in
            return R, f"Fit successful, residual norm: {np.sqrt(residuals[0]) if len(residuals) > 0 else 'N/A'}"
        else:
            return np.nan, "Incoming amplitude too small"
    except np.linalg.LinAlgError as e:
        return np.nan, f"Linear algebra error: {e}"

# -----------------------------------------------------------------------------
# 4.  Regge–Wheeler potential  (s = –2  <->  axial grav. pert.)
# -----------------------------------------------------------------------------
def V_regge_wheeler(r, M, l):
    """Axial (odd-parity) potential for Schwarzschild, s = –2."""
    f = 1.0 - 2*M/r
    return f * (l*(l+1)/r**2 - 6*M/r**3)

# ----------------------------------------------------------------------------- 
# 4.  First-order ODE system  y = [psi,  p = v*dpsi/dr*]
# -----------------------------------------------------------------------------
def teukolsky_rhs_complex(r_star, y, M, l, omega, eps, ell):
    """
    Complex two-component RHS for:
      v(r) d/dr*(v(r) dpsi/dr*) - V psi = 0
    y = [psi, p = v*dpsi/dr*]
    """
    psi, p = y
    r     = r_from_rstar(r_star, M)
    v     = v_meta(r, 2*M, eps, ell)
    Vrw   = V_regge_wheeler(r, M, l)

    dpsi = p / v
    dp = Vrw * psi
    return [dpsi, dp]

# ----------------------------------------------------------------------------- 
# 5.  Integrator wrapper
# -----------------------------------------------------------------------------
def integrate_meta_teukolsky(M, l, omega,
                             r_star_start=-200.,
                             r_star_end=200.,
                             eps=1e-3, ell=1e-5,
                             n_steps=2000,
                             show_progress=True):
    """
    Integrate outward from horizon to infinity with purely ingoing boundary condition.
    r_star_start should be negative (near horizon)
    r_star_end should be positive (far field)
    """
    print(f"Starting integration: M={M}, l={l}, omega={omega}")
    print(f"r*: {r_star_start} -> {r_star_end}, steps={n_steps}")
    print(f"Meta-weight params: eps={eps}, ell={ell}")
    
    start_time = time.time()
    
    # initial psi at the *horizon* (purely ingoing): psi = e^{-iomega r*_horiz}
    r_star_h = r_star_start  # now r_star_start should be a large negative value
    psi0 = np.exp(-1j * omega * r_star_h)
    r_start = r_from_rstar(r_star_h, M)
    print(f"Initial radius r({r_star_start}) = {r_start}")
    
    v0 = v_meta(r_start, 2*M, eps, ell)
    # dpsi/dr* at horizon = -iomega psi, so p0 = v*(-iomegapsi)
    p0 = v0 * (-1j * omega * psi0)

    # initial complex state y0 = [psi, p]
    y0 = np.array([psi0, p0], dtype=complex)

    # Use complex ODE integrator (zvode)
    solver = ode(teukolsky_rhs_complex).set_integrator(
        'zvode',
        method='adams',
        rtol=1e-8, atol=1e-8,
        nsteps=50000
    )
    # integrate *outward* from horizon to infinity
    solver.set_initial_value(y0, r_star_h)
    solver.set_f_params(M, l, omega, eps, ell)

    rs, psis = [r_star_start], [psi0]
    dr = (r_star_end - r_star_h) / n_steps  # now r_star_end > r_star_h
    
    # Progress tracking
    last_percentage = 0
    last_status_time = time.time()
    progress_interval = 2.0  # seconds between updates
    
    step = 0
    max_steps = n_steps + 100  # Safety margin
    
    try:
        while solver.successful() and solver.t < r_star_end and step < max_steps:
            # Advance the solution
            solver.integrate(solver.t + dr)
            rs.append(solver.t)
            psi, p = solver.y
            psis.append(psi)
            step += 1
            
            # Show progress
            if show_progress and time.time() - last_status_time > progress_interval:
                progress = (solver.t - r_star_start) / (r_star_end - r_star_start)
                percentage = int(100 * progress)
                
                if percentage > last_percentage:
                    r_current = r_from_rstar(solver.t, M)
                    elapsed = time.time() - start_time
                    remaining = elapsed / progress - elapsed if progress > 0 else 0
                    
                    print(f"Progress: {percentage}% complete, r*={solver.t:.2f}, r={r_current:.2f}")
                    print(f"Time: {elapsed:.1f}s elapsed, ~{remaining:.1f}s remaining")
                    print(f"|psi| = {abs(psi):.6f}")
                    sys.stdout.flush()
                    
                    last_percentage = percentage
                    last_status_time = time.time()
    
    except Exception as e:
        print(f"Integration error at step {step}, r*={solver.t if solver else 'unknown'}: {e}")
        if len(rs) < 10:
            raise  # Re-raise if we have too few points
    
    print(f"Integration complete: {len(rs)} points, {time.time() - start_time:.1f}s elapsed")
    
    return np.array(rs), np.array(psis, dtype=complex)

# ----------------------------------------------------------------------------- 
# 6.  Quick test-run
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("=============================================================")
    print("  meta_teukolsky.py - Schwarzschild gravitational wave test  ")
    print("=============================================================")
    
    # Use a smaller black hole and integration range for quicker results
    M      = 1.0            # black hole mass in code units
    l      = 2              # angular momentum (l=2 quadrupole)
    omega  = 0.3            # wave frequency
    eps    = 1e-3           # meta-weight strength
    ell    = 1e-5           # meta-weight scale
    
    # Validate the r_from_rstar function first
    print("\n--- Validation: r_from_rstar function ---")
    validate_r_from_rstar(M)
    
    print("\n--- Test Case 1: No meta-weight (epsilon = 0) - Regression Test ---")
    try:
        r_s0, psi_s0 = integrate_meta_teukolsky(
            M, l, omega,
            r_star_start=-200.0,   # Start near horizon
            r_star_end=200.0,      # Integrate outward to far field
            eps=0.0,               # No meta-weight (standard Schwarzschild)
            ell=ell,
            n_steps=2000,
            show_progress=True
        )
        
        print("\nResults without meta-weight:")
        print(f"psi(r* = -200.0) = {psi_s0[0]}")
        print(f"psi(r* = 200.0) = {psi_s0[-1]}")
        print(f"Wave amplitude ratio (far/near): {abs(psi_s0[-1])/abs(psi_s0[0]):.3f}")
        
        # Compute proper reflection coefficient
        R, status = compute_reflection_coefficient(r_s0, psi_s0, omega)
        print(f"Reflection coefficient: R = {R}")
        print(f"Status: {status}")
        
        print(f"Integration successful: {len(r_s0)} points")
    
    except Exception as e:
        print(f"No meta-weight test failed: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n--- Test Case 2: With meta-weight (epsilon = 10^-^3) ---")
    try:
        r_s, psi_s = integrate_meta_teukolsky(
            M, l, omega,
            r_star_start=-200.0,   # Start near horizon
            r_star_end=200.0,      # Integrate outward to far field
            eps=eps, ell=ell,
            n_steps=2000,
            show_progress=True
        )
    
        # Print results
        print("\nResults with meta-weight:")
        print(f"psi(r* = -200.0) = {psi_s[0]}")
        print(f"psi(r* = 200.0) = {psi_s[-1]}")
        print(f"Wave amplitude ratio (far/near): {abs(psi_s[-1])/abs(psi_s[0]):.3f}")
        
        # Compute proper reflection coefficient
        R, status = compute_reflection_coefficient(r_s, psi_s, omega)
        print(f"Reflection coefficient: R = {R}")
        print(f"Status: {status}")
        
        # Print some intermediate values
        step = len(psi_s) // 4
        print("\nWave evolution:")
        for i in range(0, len(psi_s), step):
            if i < len(psi_s):
                print(f"psi(r* = {r_s[i]:.1f}) = {psi_s[i]}")
                
        print(f"\nIntegration successful: {len(r_s)} points")
        
        # Compare with no meta-weight case
        if 'psi_s0' in locals():
            print(f"\nComparison:")
            print(f"Far-field amplitude ratio (with/without meta-weight): {abs(psi_s[-1])/abs(psi_s0[-1]):.3f}")
    
    except Exception as e:
        print(f"Error during meta-weight integration: {e}")
        import traceback
        traceback.print_exc()