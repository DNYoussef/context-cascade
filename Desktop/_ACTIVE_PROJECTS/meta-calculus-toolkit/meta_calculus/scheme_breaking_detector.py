#!/usr/bin/env python3
"""
Scheme-Breaking Detector: Systematic Hunt for New Physics

This module implements the key insight from the scheme-invariance framework:

    NEW PHYSICS LIVES WHERE SCHEME-ROBUSTNESS BREAKS.

If two representation schemes (A-scheme or C-scheme) give DIFFERENT predictions,
this is not a bug - it's potentially new physics waiting to be discovered.

STRATEGY:
    1. Define observables that SHOULD be scheme-robust
    2. Systematically scan parameter space
    3. Find regimes where schemes diverge
    4. Classify the breaking: artifact vs genuine physics

BREAKING TYPES:
    - Numerical artifact: Schemes agree with higher precision
    - Singular regime: Near singularities, schemes may legitimately differ
    - New physics: Genuinely different predictions in physical regime

DOMAINS TO SCAN:
    - Quantum mechanics near Planck scale (A-scheme + C-scheme)
    - FRW cosmology near Big Bang (C-scheme)
    - Amplitudes at strong coupling (scheme-dependent)

References:
    - Hoffreumon & Woods (2025) "Real Number Quantum Theory"
    - Meta-calculus framework documentation

Usage:
    python -m meta_calculus.scheme_breaking_detector hunt
    python -m meta_calculus.scheme_breaking_detector report
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Callable, Any, Union
from dataclasses import dataclass, field
from enum import Enum
import argparse
import sys
import json

# Import domain modules
try:
    from .quantum_number_schemes import (
        ComplexQT, RealNQT, SchemeEquivalenceTest,
        random_pure_state, random_hermitian
    )
    HAVE_QUANTUM = True
except ImportError:
    HAVE_QUANTUM = False

try:
    from .frw_scheme_robustness import (
        FRWSchemeRobustnessTest, FRWParameters
    )
    HAVE_FRW = True
except ImportError:
    HAVE_FRW = False


# =============================================================================
# BREAKING CLASSIFICATION
# =============================================================================

class BreakingType(Enum):
    """Classification of scheme-breaking events."""
    NONE = "none"                          # Schemes agree
    NUMERICAL = "numerical_artifact"        # Due to finite precision
    SINGULAR = "singular_regime"            # Near mathematical singularity
    PHYSICAL = "potential_new_physics"      # Genuinely different predictions
    UNKNOWN = "unknown"                     # Needs further investigation


@dataclass
class BreakingEvent:
    """A detected scheme-breaking event."""
    domain: str                             # 'quantum', 'frw', 'amplitudes'
    observable: str                         # What observable diverged
    parameters: Dict[str, Any]              # Parameter values at breaking
    scheme1: str                            # First scheme
    scheme2: str                            # Second scheme
    value1: Any                             # Value in scheme1
    value2: Any                             # Value in scheme2
    difference: float                       # Numerical difference
    relative_difference: float              # Relative difference
    breaking_type: BreakingType             # Classification
    confidence: float                       # Confidence in classification
    notes: str = ""                         # Additional notes


@dataclass
class HuntReport:
    """Report from a scheme-breaking hunt."""
    domain: str
    parameter_ranges: Dict[str, Tuple[float, float]]
    n_points_tested: int
    breaking_events: List[BreakingEvent]
    summary: Dict[str, Any] = field(default_factory=dict)


# =============================================================================
# BREAKING CLASSIFIER
# =============================================================================

class BreakingClassifier:
    """
    Classify scheme-breaking events.

    Uses heuristics to distinguish:
    - Numerical artifacts (precision-dependent)
    - Singular regime behavior (expected divergence)
    - Genuine new physics (robust divergence in regular regime)
    """

    def __init__(self,
                 numerical_threshold: float = 1e-10,
                 singular_threshold: float = 0.1,
                 physical_threshold: float = 0.01):
        """
        Initialize classifier.

        Args:
            numerical_threshold: Below this, treat as numerical artifact
            singular_threshold: Above this near singularity, expected behavior
            physical_threshold: Divergence in regular regime above this = physics
        """
        self.numerical_threshold = numerical_threshold
        self.singular_threshold = singular_threshold
        self.physical_threshold = physical_threshold

    def classify(self,
                 difference: float,
                 relative_difference: float,
                 is_near_singularity: bool,
                 is_regular_regime: bool) -> Tuple[BreakingType, float]:
        """
        Classify a scheme-breaking event.

        Returns:
            (BreakingType, confidence) where confidence in [0, 1]
        """
        # No breaking
        if difference < self.numerical_threshold:
            return BreakingType.NONE, 1.0

        # Numerical artifact: small but above threshold
        if difference < 1e-6 and relative_difference < 1e-4:
            return BreakingType.NUMERICAL, 0.8

        # Near singularity
        if is_near_singularity:
            if relative_difference > self.singular_threshold:
                return BreakingType.SINGULAR, 0.7
            else:
                return BreakingType.NUMERICAL, 0.5

        # Regular regime with significant difference
        if is_regular_regime and relative_difference > self.physical_threshold:
            return BreakingType.PHYSICAL, 0.6

        return BreakingType.UNKNOWN, 0.3


# =============================================================================
# DOMAIN-SPECIFIC HUNTERS
# =============================================================================

class QuantumSchemeHunter:
    """
    Hunt for A-scheme breaking in quantum mechanics.

    Tests CQT vs RNQT across parameter regimes:
    - Standard quantum mechanics (should agree)
    - Near Planck scale (may differ with additional constraints)
    - Extreme entanglement (test tensor_r vs tensor_K)
    """

    def __init__(self):
        if not HAVE_QUANTUM:
            raise ImportError("quantum_number_schemes module not available")
        self.cqt = ComplexQT()
        self.rnqt = RealNQT()
        self.tester = SchemeEquivalenceTest(self.cqt, self.rnqt)
        self.classifier = BreakingClassifier()

    def hunt(self,
             n_dimensions: List[int] = [2, 3, 4, 8],
             n_samples: int = 100) -> HuntReport:
        """
        Hunt for A-scheme breaking across Hilbert space dimensions.

        Args:
            n_dimensions: List of Hilbert space dimensions to test
            n_samples: Samples per dimension
        """
        events = []
        total_tested = 0

        for dim in n_dimensions:
            for sample_idx in range(n_samples):
                # Random state and observable
                psi = random_pure_state(dim, seed=sample_idx + dim*1000)
                obs = random_hermitian(dim, seed=sample_idx + dim*2000)

                # Compare schemes
                result = self.tester.compare_expectations(psi, obs)
                total_tested += 1

                difference = result['difference']

                # Check for breaking
                if difference > 1e-12:
                    val1 = result['expectation_scheme1']
                    val2 = result['expectation_scheme2']
                    mean_val = (abs(val1) + abs(val2)) / 2 + 1e-15
                    rel_diff = difference / mean_val

                    breaking_type, confidence = self.classifier.classify(
                        difference=difference,
                        relative_difference=rel_diff,
                        is_near_singularity=False,
                        is_regular_regime=True
                    )

                    if breaking_type != BreakingType.NONE:
                        events.append(BreakingEvent(
                            domain='quantum',
                            observable='random_hermitian_expectation',
                            parameters={'dimension': dim, 'sample': sample_idx},
                            scheme1='CQT',
                            scheme2='RNQT',
                            value1=val1,
                            value2=val2,
                            difference=difference,
                            relative_difference=rel_diff,
                            breaking_type=breaking_type,
                            confidence=confidence,
                            notes=f'Dimension {dim}, sample {sample_idx}'
                        ))

        return HuntReport(
            domain='quantum',
            parameter_ranges={'dimension': (min(n_dimensions), max(n_dimensions))},
            n_points_tested=total_tested,
            breaking_events=events,
            summary={
                'total_tested': total_tested,
                'breaking_found': len(events),
                'by_type': self._count_by_type(events)
            }
        )

    def _count_by_type(self, events: List[BreakingEvent]) -> Dict[str, int]:
        counts = {}
        for event in events:
            t = event.breaking_type.value
            counts[t] = counts.get(t, 0) + 1
        return counts


class FRWSchemeHunter:
    """
    Hunt for C-scheme breaking in FRW cosmology.

    Tests different calculus choices (classical, meta, bigeometric):
    - Late universe (should agree)
    - Near Big Bang (may differ)
    - Inflation regime (test different dynamics)
    """

    def __init__(self):
        if not HAVE_FRW:
            raise ImportError("frw_scheme_robustness module not available")
        self.tester = FRWSchemeRobustnessTest()
        self.classifier = BreakingClassifier()

    def hunt(self,
             t_range: Tuple[float, float] = (1e-10, 100.0),
             n_points: int = 200) -> HuntReport:
        """
        Hunt for C-scheme breaking across cosmic time.

        Args:
            t_range: (t_min, t_max) in cosmic time
            n_points: Number of time points to test
        """
        events = []

        # Use the existing hunt_breaking_points method
        result = self.tester.hunt_breaking_points(t_range, n_points)

        # Convert to BreakingEvents
        for bp in result['breaking_points']:
            # Classify the breaking
            t = bp['t']
            is_near_singularity = t < 1e-3

            breaking_type, confidence = self.classifier.classify(
                difference=bp['max_diff'],
                relative_difference=bp['rel_diff'],
                is_near_singularity=is_near_singularity,
                is_regular_regime=not is_near_singularity
            )

            events.append(BreakingEvent(
                domain='frw',
                observable='H(t)',
                parameters={'t': t},
                scheme1='classical',
                scheme2='meta/bigeometric',
                value1=list(bp['H_by_scheme'].values())[0] if bp['H_by_scheme'] else None,
                value2=list(bp['H_by_scheme'].values())[-1] if bp['H_by_scheme'] else None,
                difference=bp['max_diff'],
                relative_difference=bp['rel_diff'],
                breaking_type=breaking_type,
                confidence=confidence,
                notes=f"Near singularity" if is_near_singularity else "Regular regime"
            ))

        return HuntReport(
            domain='frw',
            parameter_ranges={'t': t_range},
            n_points_tested=n_points,
            breaking_events=events,
            summary={
                'total_tested': n_points,
                'breaking_found': len(events),
                'by_type': self._count_by_type(events),
                'interpretation': result['interpretation']
            }
        )

    def _count_by_type(self, events: List[BreakingEvent]) -> Dict[str, int]:
        counts = {}
        for event in events:
            t = event.breaking_type.value
            counts[t] = counts.get(t, 0) + 1
        return counts


# =============================================================================
# UNIFIED SCHEME-BREAKING DETECTOR
# =============================================================================

class SchemeBreakingDetector:
    """
    Unified detector for scheme-breaking across all domains.

    Coordinates hunts across:
    - Quantum mechanics (A-scheme: CQT vs RNQT)
    - FRW cosmology (C-scheme: classical vs meta vs bigeometric)
    - Scattering amplitudes (representation scheme)

    And generates comprehensive reports.
    """

    def __init__(self):
        self.hunters = {}

        if HAVE_QUANTUM:
            self.hunters['quantum'] = QuantumSchemeHunter()
        if HAVE_FRW:
            self.hunters['frw'] = FRWSchemeHunter()

    def hunt_all(self, verbose: bool = True) -> Dict[str, HuntReport]:
        """
        Run comprehensive scheme-breaking hunt across all domains.

        Returns:
            Dictionary mapping domain name to HuntReport
        """
        reports = {}

        for domain, hunter in self.hunters.items():
            if verbose:
                print(f"\n{'='*60}")
                print(f"HUNTING IN DOMAIN: {domain.upper()}")
                print('='*60)

            try:
                report = hunter.hunt()
                reports[domain] = report

                if verbose:
                    self._print_report_summary(report)

            except Exception as e:
                if verbose:
                    print(f"  ERROR: {e}")

        return reports

    def _print_report_summary(self, report: HuntReport):
        """Print summary of a hunt report."""
        print(f"\n  Domain: {report.domain}")
        print(f"  Points tested: {report.n_points_tested}")
        print(f"  Breaking events found: {len(report.breaking_events)}")

        if report.summary.get('by_type'):
            print(f"\n  By type:")
            for btype, count in report.summary['by_type'].items():
                print(f"    {btype}: {count}")

        if report.summary.get('interpretation'):
            print(f"\n  Interpretation: {report.summary['interpretation']}")

    def generate_report(self, reports: Dict[str, HuntReport]) -> str:
        """Generate comprehensive text report."""
        lines = []
        lines.append("=" * 70)
        lines.append("SCHEME-BREAKING DETECTION REPORT")
        lines.append("=" * 70)
        lines.append("")
        lines.append("The meta-principle: Physical = Scheme-Invariant")
        lines.append("New physics lives where this invariance BREAKS.")
        lines.append("")

        total_tested = sum(r.n_points_tested for r in reports.values())
        total_breaking = sum(len(r.breaking_events) for r in reports.values())

        lines.append(f"SUMMARY: {total_tested} points tested, {total_breaking} breaking events")
        lines.append("")

        for domain, report in reports.items():
            lines.append("-" * 60)
            lines.append(f"DOMAIN: {domain.upper()}")
            lines.append("-" * 60)
            lines.append(f"  Tested: {report.n_points_tested} points")
            lines.append(f"  Breaking: {len(report.breaking_events)} events")

            if report.summary.get('by_type'):
                lines.append("  By type:")
                for btype, count in report.summary['by_type'].items():
                    lines.append(f"    - {btype}: {count}")

            # Show most significant breaking events
            significant = [e for e in report.breaking_events
                          if e.breaking_type == BreakingType.PHYSICAL]
            if significant:
                lines.append("  Potentially physical breaking:")
                for event in significant[:5]:
                    lines.append(f"    - {event.observable} at {event.parameters}")
                    lines.append(f"      Difference: {event.difference:.2e} "
                               f"(rel: {event.relative_difference:.2%})")

            lines.append("")

        # Conclusions
        lines.append("=" * 70)
        lines.append("CONCLUSIONS")
        lines.append("=" * 70)

        physical_breaking = any(
            any(e.breaking_type == BreakingType.PHYSICAL for e in r.breaking_events)
            for r in reports.values()
        )

        if physical_breaking:
            lines.append("")
            lines.append("*** POTENTIAL NEW PHYSICS DETECTED ***")
            lines.append("")
            lines.append("Some observables show scheme-dependence in regular regimes.")
            lines.append("This requires further investigation:")
            lines.append("  1. Increase numerical precision")
            lines.append("  2. Check for hidden singularities")
            lines.append("  3. If robust, this indicates new physics!")
        else:
            lines.append("")
            lines.append("No scheme-breaking found in tested regimes.")
            lines.append("")
            lines.append("This confirms:")
            lines.append("  - A-schemes (CQT vs RNQT) are equivalent for QM")
            lines.append("  - C-schemes agree in regular cosmological regime")
            lines.append("  - Breaking only occurs near singularities (expected)")
            lines.append("")
            lines.append("To find new physics, probe:")
            lines.append("  - Planck-scale quantum mechanics")
            lines.append("  - Trans-Planckian cosmology")
            lines.append("  - Strong-coupling amplitudes")

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)


# =============================================================================
# DEMO AND CLI
# =============================================================================

def demo_scheme_breaking():
    """Demonstrate scheme-breaking detection."""
    print("=" * 70)
    print("SCHEME-BREAKING DETECTOR")
    print("Hunting for new physics where representations diverge")
    print("=" * 70)

    detector = SchemeBreakingDetector()

    print(f"\nAvailable domains: {list(detector.hunters.keys())}")

    # Run hunts
    reports = detector.hunt_all(verbose=True)

    # Generate report
    print("\n" + "=" * 70)
    print("GENERATING COMPREHENSIVE REPORT")
    print("=" * 70)

    report_text = detector.generate_report(reports)
    print(report_text)


def main():
    parser = argparse.ArgumentParser(
        description="Scheme-Breaking Detector: Hunt for new physics"
    )
    parser.add_argument('command', choices=['hunt', 'report', 'demo'],
                        nargs='?', default='demo')
    parser.add_argument('--domain', choices=['quantum', 'frw', 'all'],
                        default='all')
    parser.add_argument('--output', type=str, default=None,
                        help='Output file for report')

    args = parser.parse_args()

    if args.command == 'demo':
        demo_scheme_breaking()
    elif args.command == 'hunt':
        detector = SchemeBreakingDetector()
        reports = detector.hunt_all()
        if args.output:
            report = detector.generate_report(reports)
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to {args.output}")
    elif args.command == 'report':
        demo_scheme_breaking()


if __name__ == '__main__':
    demo_scheme_breaking()
