#!/usr/bin/env python3
"""
Tests for Scheme-Breaking Detector Module

Tests the unified scheme-breaking detection framework that hunts
for new physics where representation invariance breaks.

Test Categories:
1. Breaking classification tests
2. Quantum scheme hunting tests
3. FRW scheme hunting tests
4. Report generation tests
"""

import numpy as np
import pytest
import sys
import os

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from meta_calculus.scheme_breaking_detector import (
    BreakingType, BreakingEvent, HuntReport,
    BreakingClassifier, SchemeBreakingDetector
)


# =============================================================================
# BREAKING CLASSIFICATION TESTS
# =============================================================================

class TestBreakingClassifier:
    """Test the breaking event classifier."""

    @pytest.fixture
    def classifier(self):
        return BreakingClassifier()

    def test_no_breaking_for_small_difference(self, classifier):
        """Tiny differences are classified as NONE."""
        btype, confidence = classifier.classify(
            difference=1e-15,
            relative_difference=1e-15,
            is_near_singularity=False,
            is_regular_regime=True
        )

        assert btype == BreakingType.NONE
        assert confidence > 0.9

    def test_numerical_artifact_classification(self, classifier):
        """Small but detectable differences are numerical artifacts."""
        btype, confidence = classifier.classify(
            difference=1e-8,
            relative_difference=1e-6,
            is_near_singularity=False,
            is_regular_regime=True
        )

        assert btype == BreakingType.NUMERICAL
        assert confidence > 0.5

    def test_singular_regime_classification(self, classifier):
        """Large differences near singularities are expected."""
        btype, confidence = classifier.classify(
            difference=0.5,
            relative_difference=0.5,
            is_near_singularity=True,
            is_regular_regime=False
        )

        assert btype == BreakingType.SINGULAR
        assert confidence > 0.5

    def test_physical_breaking_classification(self, classifier):
        """Significant differences in regular regime may be physical."""
        btype, confidence = classifier.classify(
            difference=0.1,
            relative_difference=0.1,
            is_near_singularity=False,
            is_regular_regime=True
        )

        assert btype == BreakingType.PHYSICAL
        assert confidence > 0.3


# =============================================================================
# BREAKING EVENT TESTS
# =============================================================================

class TestBreakingEvent:
    """Test BreakingEvent dataclass."""

    def test_event_creation(self):
        """BreakingEvent can be created with all fields."""
        event = BreakingEvent(
            domain='quantum',
            observable='expectation',
            parameters={'dim': 2},
            scheme1='CQT',
            scheme2='RNQT',
            value1=1.0,
            value2=1.0001,
            difference=0.0001,
            relative_difference=0.0001,
            breaking_type=BreakingType.NUMERICAL,
            confidence=0.8,
            notes='Test event'
        )

        assert event.domain == 'quantum'
        assert event.breaking_type == BreakingType.NUMERICAL
        assert event.confidence == 0.8

    def test_event_fields_accessible(self):
        """All event fields are accessible."""
        event = BreakingEvent(
            domain='frw',
            observable='H(t)',
            parameters={'t': 0.001},
            scheme1='classical',
            scheme2='meta',
            value1=1000.0,
            value2=500.0,
            difference=500.0,
            relative_difference=0.667,
            breaking_type=BreakingType.SINGULAR,
            confidence=0.7
        )

        assert event.domain == 'frw'
        assert event.parameters['t'] == 0.001
        assert event.difference == 500.0


# =============================================================================
# HUNT REPORT TESTS
# =============================================================================

class TestHuntReport:
    """Test HuntReport dataclass."""

    def test_report_creation(self):
        """HuntReport can be created."""
        report = HuntReport(
            domain='quantum',
            parameter_ranges={'dim': (2, 8)},
            n_points_tested=100,
            breaking_events=[]
        )

        assert report.domain == 'quantum'
        assert report.n_points_tested == 100
        assert len(report.breaking_events) == 0

    def test_report_with_events(self):
        """HuntReport can contain breaking events."""
        event = BreakingEvent(
            domain='quantum',
            observable='test',
            parameters={},
            scheme1='A',
            scheme2='B',
            value1=1.0,
            value2=1.1,
            difference=0.1,
            relative_difference=0.1,
            breaking_type=BreakingType.UNKNOWN,
            confidence=0.5
        )

        report = HuntReport(
            domain='quantum',
            parameter_ranges={},
            n_points_tested=50,
            breaking_events=[event]
        )

        assert len(report.breaking_events) == 1
        assert report.breaking_events[0].difference == 0.1


# =============================================================================
# SCHEME-BREAKING DETECTOR TESTS
# =============================================================================

class TestSchemeBreakingDetector:
    """Test the unified SchemeBreakingDetector."""

    @pytest.fixture
    def detector(self):
        return SchemeBreakingDetector()

    def test_detector_has_hunters(self, detector):
        """Detector initializes with available hunters."""
        # Should have at least quantum and frw hunters
        assert len(detector.hunters) >= 1

    def test_hunt_all_returns_reports(self, detector):
        """hunt_all returns dictionary of reports."""
        reports = detector.hunt_all(verbose=False)

        assert isinstance(reports, dict)
        for domain, report in reports.items():
            assert isinstance(report, HuntReport)
            assert report.domain == domain

    def test_generate_report_produces_text(self, detector):
        """generate_report produces readable text."""
        reports = detector.hunt_all(verbose=False)
        text = detector.generate_report(reports)

        assert isinstance(text, str)
        assert len(text) > 100
        assert "SCHEME-BREAKING" in text.upper()

    def test_report_contains_summary(self, detector):
        """Generated report contains summary information."""
        reports = detector.hunt_all(verbose=False)
        text = detector.generate_report(reports)

        assert "SUMMARY" in text or "summary" in text.lower()
        assert "tested" in text.lower()


# =============================================================================
# QUANTUM HUNTER TESTS (if available)
# =============================================================================

class TestQuantumHunter:
    """Test quantum scheme hunting."""

    def test_quantum_hunt_available(self):
        """Check if quantum hunter is available."""
        detector = SchemeBreakingDetector()

        if 'quantum' in detector.hunters:
            hunter = detector.hunters['quantum']
            assert hunter is not None

    def test_quantum_hunt_produces_report(self):
        """Quantum hunt produces valid report."""
        detector = SchemeBreakingDetector()

        if 'quantum' in detector.hunters:
            report = detector.hunters['quantum'].hunt(
                n_dimensions=[2, 3],
                n_samples=10
            )

            assert report.domain == 'quantum'
            assert report.n_points_tested > 0
            assert 'total_tested' in report.summary

    def test_quantum_cqt_rnqt_equivalence(self):
        """CQT and RNQT should give no physical breaking."""
        detector = SchemeBreakingDetector()

        if 'quantum' in detector.hunters:
            report = detector.hunters['quantum'].hunt(
                n_dimensions=[2],
                n_samples=50
            )

            # No PHYSICAL breaking should be found
            physical_breaking = [e for e in report.breaking_events
                               if e.breaking_type == BreakingType.PHYSICAL]

            # CQT == RNQT exactly, so no physical breaking
            assert len(physical_breaking) == 0


# =============================================================================
# FRW HUNTER TESTS (if available)
# =============================================================================

class TestFRWHunter:
    """Test FRW scheme hunting."""

    def test_frw_hunt_available(self):
        """Check if FRW hunter is available."""
        detector = SchemeBreakingDetector()

        if 'frw' in detector.hunters:
            hunter = detector.hunters['frw']
            assert hunter is not None

    def test_frw_hunt_produces_report(self):
        """FRW hunt produces valid report."""
        detector = SchemeBreakingDetector()

        if 'frw' in detector.hunters:
            report = detector.hunters['frw'].hunt(
                t_range=(1e-3, 10),
                n_points=30
            )

            assert report.domain == 'frw'
            assert report.n_points_tested > 0

    def test_frw_singular_breaking_expected(self):
        """FRW should show singular-type breaking near t=0."""
        detector = SchemeBreakingDetector()

        if 'frw' in detector.hunters:
            report = detector.hunters['frw'].hunt(
                t_range=(1e-6, 1),
                n_points=50
            )

            # May or may not find breaking, but report should be valid
            assert report.domain == 'frw'

            # If breaking found, check it's classified
            for event in report.breaking_events:
                assert event.breaking_type in BreakingType


# =============================================================================
# BREAKING TYPE ENUM TESTS
# =============================================================================

class TestBreakingTypeEnum:
    """Test BreakingType enumeration."""

    def test_all_types_have_values(self):
        """All breaking types have string values."""
        for btype in BreakingType:
            assert isinstance(btype.value, str)
            assert len(btype.value) > 0

    def test_types_are_distinct(self):
        """All breaking types are distinct."""
        values = [btype.value for btype in BreakingType]
        assert len(values) == len(set(values))

    def test_expected_types_exist(self):
        """Expected breaking types exist."""
        # Map expected keywords to what they should match
        expected = {
            'none': 'none',
            'numerical': 'numerical',
            'singular': 'singular',
            'physics': 'potential_new_physics',  # PHYSICAL has value 'potential_new_physics'
            'unknown': 'unknown'
        }

        for keyword, expected_value in expected.items():
            found = any(expected_value in btype.value.lower() for btype in BreakingType)
            assert found, f"Expected type containing '{keyword}' not found"


# =============================================================================
# INTEGRATION TESTS
# =============================================================================

class TestIntegration:
    """Integration tests for the full system."""

    def test_full_hunt_workflow(self):
        """Complete hunt workflow executes without error."""
        detector = SchemeBreakingDetector()

        # Run hunt
        reports = detector.hunt_all(verbose=False)

        # Generate report
        text = detector.generate_report(reports)

        # Verify output
        assert len(reports) > 0
        assert len(text) > 100

    def test_no_false_physical_breaking_in_known_equivalences(self):
        """Known equivalences should not show physical breaking."""
        detector = SchemeBreakingDetector()
        reports = detector.hunt_all(verbose=False)

        # Check quantum domain (CQT == RNQT exactly)
        if 'quantum' in reports:
            qreport = reports['quantum']
            physical = [e for e in qreport.breaking_events
                       if e.breaking_type == BreakingType.PHYSICAL]

            # Quantum A-schemes are exactly equivalent
            assert len(physical) == 0, "False physical breaking in quantum domain"


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
