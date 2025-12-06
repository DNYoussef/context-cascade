#!/usr/bin/env python3
"""
Solution Space Polytope and Canonical Form (Gaps 1-2)

This module formalizes the meta-cosmology parameter space as a polytope
with facet constraints from BBN/CMB observations and physical requirements.

KEY STRUCTURES:
  - Polytope P = { (n,s,k,w) : constraints satisfied }
  - Facet inequalities from BBN, CMB, energy conditions
  - Canonical form Omega with pole structure at facets
  - Vertex enumeration for extreme physical cases

CONNECTION TO POSITIVE GEOMETRY:
  - Cosmological polytope analogy
  - Facet functions L_i vanishing at boundaries
  - Canonical form = volume form / product of facets

Usage:
    python -m meta_calculus.polytope vertices
    python -m meta_calculus.polytope facets
    python -m meta_calculus.polytope canonical --n 0.5 --s 0.02 --k 0.01 --w 0.333
    python -m meta_calculus.polytope sample --n-points 100
"""

import numpy as np
from typing import Tuple, Dict, List, Optional
import argparse
import sys

# Import from existing modules
from .model_comparison import (
    n_action_based, n_derivative_weight, discriminant, allowed_s_range
)


# =============================================================================
# PHYSICAL CONSTRAINTS (Facet Bounds)
# =============================================================================

# BBN constraint on action-based parameter s
S_MAX = 0.05  # |s| < 0.05 from BBN (3% Hubble deviation)

# CMB constraint on derivative-weight parameter k
K_MAX = 0.03  # |k| < 0.03 from CMB acoustic peaks

# Energy condition bounds on equation of state w
W_MIN = -1.0  # Cosmological constant limit
W_MAX = 1.0   # Stiff matter limit

# Expansion requirement
N_MIN = 0.0   # Expanding universe


# =============================================================================
# POLYTOPE STRUCTURE (Gap 1)
# =============================================================================

class SolutionPolytope:
    """
    The parameter space polytope P = { (n,s,k,w) : constraints }.

    Facets:
      F1: |s| <= s_max (BBN)
      F2: |k| <= k_max (CMB)
      F3: -1 <= w <= 1 (energy conditions)
      F4: n >= 0 (expansion)
      F5: Delta(s,w) >= 0 (real solutions, curved)
    """

    def __init__(self,
                 s_max: float = S_MAX,
                 k_max: float = K_MAX,
                 w_min: float = W_MIN,
                 w_max: float = W_MAX,
                 n_min: float = N_MIN):
        """
        Initialize polytope with constraint bounds.

        Args:
            s_max: Maximum |s| from BBN
            k_max: Maximum |k| from CMB
            w_min: Minimum w from energy conditions
            w_max: Maximum w from energy conditions
            n_min: Minimum n (expansion requirement)
        """
        self.s_max = s_max
        self.k_max = k_max
        self.w_min = w_min
        self.w_max = w_max
        self.n_min = n_min

    def constraint_matrix(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Return constraint matrix A and bounds b such that A @ x <= b.

        Returns:
            (A, b) where A is constraint matrix, b is bound vector
        """
        # x = (n, s, k, w)
        # Constraints: A @ x <= b

        A = np.array([
            [0, 1, 0, 0],    # s <= s_max
            [0, -1, 0, 0],   # -s <= s_max (i.e., s >= -s_max)
            [0, 0, 1, 0],    # k <= k_max
            [0, 0, -1, 0],   # -k <= k_max
            [0, 0, 0, 1],    # w <= w_max
            [0, 0, 0, -1],   # -w <= -w_min (i.e., w >= w_min)
            [-1, 0, 0, 0],   # -n <= -n_min (i.e., n >= n_min)
        ], dtype=np.float64)

        b = np.array([
            self.s_max,
            self.s_max,
            self.k_max,
            self.k_max,
            self.w_max,
            -self.w_min,
            -self.n_min,
        ], dtype=np.float64)

        return A, b

    def is_inside(self, n: float, s: float, k: float, w: float) -> bool:
        """
        Check if point (n, s, k, w) is inside the polytope.

        Args:
            n, s, k, w: Parameter values

        Returns:
            True if all constraints satisfied
        """
        # Linear constraints
        if abs(s) > self.s_max:
            return False
        if abs(k) > self.k_max:
            return False
        if w < self.w_min or w > self.w_max:
            return False
        if n < self.n_min:
            return False

        # Nonlinear constraint: discriminant
        if discriminant(s, w) < 0:
            return False

        return True

    def vertices(self) -> List[Dict]:
        """
        Enumerate vertices (extreme points) of the polytope.

        Returns:
            List of vertex dictionaries with (n, s, k, w) and labels
        """
        vertices = []

        # Classical vertices (s=0, k=0) at different w
        for w, w_name in [(1.0/3.0, 'radiation'), (0.0, 'dust'), (1.0, 'stiff')]:
            n = n_action_based(0, w)
            vertices.append({
                'n': n, 's': 0.0, 'k': 0.0, 'w': w,
                'label': f'Classical {w_name}',
                'type': 'classical',
            })

        # Action-based extremes (s = +/- s_max, k=0)
        for w, w_name in [(1.0/3.0, 'radiation'), (0.0, 'dust')]:
            for s_sign, s_label in [(1, '+s_max'), (-1, '-s_max')]:
                s = s_sign * self.s_max
                if discriminant(s, w) >= 0:
                    n = n_action_based(s, w)
                    vertices.append({
                        'n': n, 's': s, 'k': 0.0, 'w': w,
                        'label': f'{w_name}, {s_label}',
                        'type': 'action-extreme',
                    })

        # Derivative-weight extremes (s=0, k = +/- k_max)
        for w, w_name in [(1.0/3.0, 'radiation'), (0.0, 'dust')]:
            for k_sign, k_label in [(1, '+k_max'), (-1, '-k_max')]:
                k = k_sign * self.k_max
                n = n_derivative_weight(k, w)
                vertices.append({
                    'n': n, 's': 0.0, 'k': k, 'w': w,
                    'label': f'{w_name}, {k_label}',
                    'type': 'deriv-extreme',
                })

        # Energy condition extremes (w = +/- 1)
        for w, w_name in [(-1.0, 'cosmological'), (1.0, 'stiff')]:
            if w != -1.0:  # w = -1 gives n = inf
                n = n_action_based(0, w)
                vertices.append({
                    'n': n, 's': 0.0, 'k': 0.0, 'w': w,
                    'label': f'{w_name} matter',
                    'type': 'w-extreme',
                })

        return vertices

    def facets(self) -> List[Dict]:
        """
        Return facet definitions.

        Returns:
            List of facet dictionaries with equation and physical meaning
        """
        return [
            {
                'id': 'F1+',
                'equation': f's = {self.s_max}',
                'constraint': f's <= {self.s_max}',
                'physics': 'BBN upper bound on action-based deformation',
            },
            {
                'id': 'F1-',
                'equation': f's = -{self.s_max}',
                'constraint': f's >= -{self.s_max}',
                'physics': 'BBN lower bound on action-based deformation',
            },
            {
                'id': 'F2+',
                'equation': f'k = {self.k_max}',
                'constraint': f'k <= {self.k_max}',
                'physics': 'CMB upper bound on derivative weight',
            },
            {
                'id': 'F2-',
                'equation': f'k = -{self.k_max}',
                'constraint': f'k >= -{self.k_max}',
                'physics': 'CMB lower bound on derivative weight',
            },
            {
                'id': 'F3+',
                'equation': 'w = 1',
                'constraint': 'w <= 1',
                'physics': 'Dominant energy condition (stiff matter limit)',
            },
            {
                'id': 'F3-',
                'equation': 'w = -1',
                'constraint': 'w >= -1',
                'physics': 'Dominant energy condition (cosmological constant)',
            },
            {
                'id': 'F4',
                'equation': 'n = 0',
                'constraint': 'n >= 0',
                'physics': 'Expanding universe requirement',
            },
            {
                'id': 'F5',
                'equation': 'Delta(s,w) = 0',
                'constraint': 'Delta(s,w) >= 0',
                'physics': 'Real solution existence (curved facet)',
            },
        ]

    def sample_interior(self, n_points: int = 100, seed: int = None) -> np.ndarray:
        """
        Sample random points from the polytope interior.

        Args:
            n_points: Number of points to sample
            seed: Random seed

        Returns:
            Array of shape (n_points, 4) with (n, s, k, w) columns
        """
        if seed is not None:
            np.random.seed(seed)

        samples = []
        attempts = 0
        max_attempts = n_points * 100

        while len(samples) < n_points and attempts < max_attempts:
            attempts += 1

            # Sample uniformly in bounding box
            s = np.random.uniform(-self.s_max, self.s_max)
            k = np.random.uniform(-self.k_max, self.k_max)
            w = np.random.uniform(self.w_min, self.w_max)

            # Skip w = -1 (singular)
            if abs(w + 1) < 0.01:
                continue

            # Check discriminant
            if discriminant(s, w) < 0:
                continue

            # Compute n (use action-based for consistency)
            n = n_action_based(s, w)

            if n >= self.n_min and np.isfinite(n):
                samples.append([n, s, k, w])

        return np.array(samples)


# =============================================================================
# CANONICAL FORM (Gap 2)
# =============================================================================

class CanonicalForm:
    """
    Canonical form Omega on the solution polytope.

    Omega = dn ^ ds ^ dk ^ dw / [F1(s) * F2(k) * F3(w) * F4(n)]

    where F_i are facet functions vanishing at boundaries.
    """

    def __init__(self, polytope: SolutionPolytope = None):
        """
        Initialize canonical form with polytope.

        Args:
            polytope: SolutionPolytope instance (uses defaults if None)
        """
        self.polytope = polytope or SolutionPolytope()

    def facet_function_F1(self, s: float) -> float:
        """
        BBN facet function: F1(s) = s_max^2 - s^2.

        Vanishes at s = +/- s_max.
        """
        return self.polytope.s_max**2 - s**2

    def facet_function_F2(self, k: float) -> float:
        """
        CMB facet function: F2(k) = k_max^2 - k^2.

        Vanishes at k = +/- k_max.
        """
        return self.polytope.k_max**2 - k**2

    def facet_function_F3(self, w: float) -> float:
        """
        Energy condition facet function: F3(w) = 1 - w^2.

        Vanishes at w = +/- 1.
        """
        return 1.0 - w**2

    def facet_function_F4(self, n: float) -> float:
        """
        Expansion facet function: F4(n) = n.

        Vanishes at n = 0.
        """
        return n

    def evaluate(self, n: float, s: float, k: float, w: float) -> float:
        """
        Evaluate canonical form at point.

        Returns:
            1 / [F1 * F2 * F3 * F4] (the coefficient of dn^ds^dk^dw)
        """
        F1 = self.facet_function_F1(s)
        F2 = self.facet_function_F2(k)
        F3 = self.facet_function_F3(w)
        F4 = self.facet_function_F4(n)

        denominator = F1 * F2 * F3 * F4

        if abs(denominator) < 1e-15:
            return float('inf')  # Pole at facet

        return 1.0 / denominator

    def pole_distance(self, n: float, s: float, k: float, w: float) -> Dict:
        """
        Compute distance to each facet (pole).

        Returns:
            Dictionary with distances to each facet
        """
        return {
            'F1': min(self.polytope.s_max - abs(s), abs(s) + self.polytope.s_max),
            'F2': min(self.polytope.k_max - abs(k), abs(k) + self.polytope.k_max),
            'F3': min(1 - abs(w), abs(w) + 1),
            'F4': n - self.polytope.n_min,
            'nearest': None,  # Will be filled
        }

    def residue_at_facet(self, facet_id: str) -> str:
        """
        Describe the residue structure at a given facet.

        Args:
            facet_id: One of 'F1', 'F2', 'F3', 'F4'

        Returns:
            Description of residue structure
        """
        residue_info = {
            'F1': 'Residue at s = +/- s_max encodes BBN boundary physics',
            'F2': 'Residue at k = +/- k_max encodes CMB boundary physics',
            'F3': 'Residue at w = +/- 1 encodes energy condition limits',
            'F4': 'Residue at n = 0 encodes static universe limit',
        }
        return residue_info.get(facet_id, 'Unknown facet')

    def integral_over_region(self,
                             s_range: Tuple[float, float],
                             k_range: Tuple[float, float],
                             w_range: Tuple[float, float],
                             n_samples: int = 1000) -> float:
        """
        Numerically integrate canonical form over a region.

        Uses Monte Carlo integration.

        Args:
            s_range, k_range, w_range: Integration bounds
            n_samples: Number of Monte Carlo samples

        Returns:
            Approximate integral value
        """
        s_vals = np.random.uniform(s_range[0], s_range[1], n_samples)
        k_vals = np.random.uniform(k_range[0], k_range[1], n_samples)
        w_vals = np.random.uniform(w_range[0], w_range[1], n_samples)

        total = 0.0
        count = 0

        for s, k, w in zip(s_vals, k_vals, w_vals):
            if abs(w + 1) < 0.01:  # Skip near w = -1
                continue
            if discriminant(s, w) < 0:
                continue

            n = n_action_based(s, w)
            if n <= 0 or not np.isfinite(n):
                continue

            omega = self.evaluate(n, s, k, w)
            if np.isfinite(omega):
                total += omega
                count += 1

        if count == 0:
            return 0.0

        # Volume of integration region
        volume = (s_range[1] - s_range[0]) * \
                 (k_range[1] - k_range[0]) * \
                 (w_range[1] - w_range[0])

        return total / count * volume


# =============================================================================
# CLI COMMANDS
# =============================================================================

def cmd_vertices(args):
    """Show polytope vertices."""
    print("=" * 70)
    print("SOLUTION POLYTOPE VERTICES")
    print("=" * 70)

    polytope = SolutionPolytope()
    vertices = polytope.vertices()

    print(f"\n  {'Label':<25} {'n':<10} {'s':<10} {'k':<10} {'w':<10}")
    print("  " + "-" * 65)

    for v in vertices:
        print(f"  {v['label']:<25} {v['n']:<10.4f} {v['s']:<10.4f} "
              f"{v['k']:<10.4f} {v['w']:<10.4f}")

    print(f"\n  Total vertices: {len(vertices)}")


def cmd_facets(args):
    """Show polytope facets."""
    print("=" * 70)
    print("SOLUTION POLYTOPE FACETS")
    print("=" * 70)

    polytope = SolutionPolytope()
    facets = polytope.facets()

    for f in facets:
        print(f"\n  [{f['id']}] {f['equation']}")
        print(f"      Constraint: {f['constraint']}")
        print(f"      Physics: {f['physics']}")


def cmd_canonical(args):
    """Evaluate canonical form at a point."""
    print("=" * 70)
    print("CANONICAL FORM EVALUATION")
    print("=" * 70)

    polytope = SolutionPolytope()
    canonical = CanonicalForm(polytope)

    n, s, k, w = args.n, args.s, args.k, args.w

    print(f"\n  Point: (n={n:.4f}, s={s:.4f}, k={k:.4f}, w={w:.4f})")

    # Check if inside polytope
    inside = polytope.is_inside(n, s, k, w)
    print(f"  Inside polytope: {inside}")

    # Evaluate facet functions
    print(f"\n  Facet functions:")
    print(f"    F1(s) = s_max^2 - s^2 = {canonical.facet_function_F1(s):.6f}")
    print(f"    F2(k) = k_max^2 - k^2 = {canonical.facet_function_F2(k):.6f}")
    print(f"    F3(w) = 1 - w^2       = {canonical.facet_function_F3(w):.6f}")
    print(f"    F4(n) = n             = {canonical.facet_function_F4(n):.6f}")

    # Evaluate canonical form
    omega = canonical.evaluate(n, s, k, w)
    print(f"\n  Canonical form Omega = {omega:.6e}")

    if omega > 1e10:
        print("  (Near a pole - approaching facet boundary)")


def cmd_sample(args):
    """Sample points from polytope interior."""
    print("=" * 70)
    print(f"SAMPLING {args.n_points} POINTS FROM POLYTOPE INTERIOR")
    print("=" * 70)

    polytope = SolutionPolytope()
    samples = polytope.sample_interior(args.n_points, seed=args.seed)

    print(f"\n  Successfully sampled {len(samples)} points")

    if len(samples) > 0:
        print(f"\n  Statistics:")
        print(f"    n: [{samples[:,0].min():.4f}, {samples[:,0].max():.4f}]")
        print(f"    s: [{samples[:,1].min():.4f}, {samples[:,1].max():.4f}]")
        print(f"    k: [{samples[:,2].min():.4f}, {samples[:,2].max():.4f}]")
        print(f"    w: [{samples[:,3].min():.4f}, {samples[:,3].max():.4f}]")

        if args.show_samples:
            print(f"\n  First 10 samples:")
            print(f"  {'n':<10} {'s':<10} {'k':<10} {'w':<10}")
            print("  " + "-" * 40)
            for i in range(min(10, len(samples))):
                print(f"  {samples[i,0]:<10.4f} {samples[i,1]:<10.4f} "
                      f"{samples[i,2]:<10.4f} {samples[i,3]:<10.4f}")


def cmd_integrate(args):
    """Integrate canonical form over a region."""
    print("=" * 70)
    print("CANONICAL FORM INTEGRATION")
    print("=" * 70)

    canonical = CanonicalForm()

    s_range = (-args.s_max, args.s_max)
    k_range = (-args.k_max, args.k_max)
    w_range = (args.w_min, args.w_max)

    print(f"\n  Integration region:")
    print(f"    s in [{s_range[0]:.4f}, {s_range[1]:.4f}]")
    print(f"    k in [{k_range[0]:.4f}, {k_range[1]:.4f}]")
    print(f"    w in [{w_range[0]:.4f}, {w_range[1]:.4f}]")

    integral = canonical.integral_over_region(
        s_range, k_range, w_range, n_samples=args.n_samples
    )

    print(f"\n  Integral (Monte Carlo, {args.n_samples} samples): {integral:.6e}")


def main():
    parser = argparse.ArgumentParser(
        description="Solution Space Polytope and Canonical Form",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # vertices command
    vert_parser = subparsers.add_parser('vertices',
        help='Show polytope vertices')
    vert_parser.set_defaults(func=cmd_vertices)

    # facets command
    facet_parser = subparsers.add_parser('facets',
        help='Show polytope facets')
    facet_parser.set_defaults(func=cmd_facets)

    # canonical command
    canon_parser = subparsers.add_parser('canonical',
        help='Evaluate canonical form at a point')
    canon_parser.add_argument('--n', type=float, default=0.5)
    canon_parser.add_argument('--s', type=float, default=0.02)
    canon_parser.add_argument('--k', type=float, default=0.01)
    canon_parser.add_argument('--w', type=float, default=1.0/3.0)
    canon_parser.set_defaults(func=cmd_canonical)

    # sample command
    sample_parser = subparsers.add_parser('sample',
        help='Sample points from polytope interior')
    sample_parser.add_argument('--n-points', type=int, default=100)
    sample_parser.add_argument('--seed', type=int, default=None)
    sample_parser.add_argument('--show-samples', action='store_true')
    sample_parser.set_defaults(func=cmd_sample)

    # integrate command
    int_parser = subparsers.add_parser('integrate',
        help='Integrate canonical form over region')
    int_parser.add_argument('--s-max', type=float, default=0.04)
    int_parser.add_argument('--k-max', type=float, default=0.02)
    int_parser.add_argument('--w-min', type=float, default=-0.5)
    int_parser.add_argument('--w-max', type=float, default=0.9)
    int_parser.add_argument('--n-samples', type=int, default=10000)
    int_parser.set_defaults(func=cmd_integrate)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
