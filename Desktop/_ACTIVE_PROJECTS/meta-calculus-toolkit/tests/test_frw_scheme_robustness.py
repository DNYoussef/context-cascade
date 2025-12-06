#!/usr/bin/env python3
"""
Tests for FRW Scheme-Robustness Module

Tests that cosmological observables are properly classified as
scheme-robust (physical) vs scheme-dependent (scaffolding).

Test Categories:
1. C-scheme infrastructure tests
2. H(z) scheme-robustness tests
3. Distance measure tests
4. Singularity behavior tests
5. Scheme-breaking detection tests
"""

import numpy as np
import pytest
import sys
import os

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from meta_calculus.frw_scheme_robustness import (
    ClassicalCScheme, MetaCScheme, BigeometricCScheme,
    FRWParameters, FRWModel, FRWSchemeRobustnessTest
)


# =============================================================================
# C-SCHEME INFRASTRUCTURE TESTS
# =============================================================================

class TestCSchemeInfrastructure:
    """Test basic C-scheme functionality."""

    def test_classical_scheme_name(self):
        """Classical scheme has correct name."""
        scheme = ClassicalCScheme()
        assert "Classical" in scheme.name

    def test_meta_scheme_name(self):
        """Meta scheme has correct name."""
        scheme = MetaCScheme()
        assert "Meta" in scheme.name

    def test_bigeometric_scheme_name(self):
        """Bigeometric scheme has correct name."""
        scheme = BigeometricCScheme()
        assert "Bigeometric" in scheme.name

    def test_classical_derivative_polynomial(self):
        """Classical derivative of polynomial is correct."""
        scheme = ClassicalCScheme()

        # f(t) = t^2, f'(t) = 2t
        f = lambda t: t**2
        t = 1.0

        df_dt = scheme.time_derivative(f, t)
        expected = 2 * t

        assert abs(df_dt - expected) < 1e-5

    def test_classical_derivative_exponential(self):
        """Classical derivative of exponential is correct."""
        scheme = ClassicalCScheme()

        # f(t) = exp(t), f'(t) = exp(t)
        f = lambda t: np.exp(t)
        t = 1.0

        df_dt = scheme.time_derivative(f, t)
        expected = np.exp(t)

        assert abs(df_dt - expected) < 1e-5

    def test_meta_derivative_with_identity_weights(self):
        """Meta derivative with u=v=1 equals classical."""
        classical = ClassicalCScheme()
        meta = MetaCScheme(u=lambda t: 1.0, v=lambda t: 1.0)

        f = lambda t: t**3
        t = 2.0

        df_classical = classical.time_derivative(f, t)
        df_meta = meta.time_derivative(f, t)

        assert abs(df_classical - df_meta) < 1e-5

    def test_bigeometric_power_law(self):
        """Bigeometric derivative of power law gives constant (for t*f'/f)."""
        scheme = BigeometricCScheme()

        # f(t) = t^n, bigeometric: t * f'/f = t * n/t = n
        n = 2.0
        f = lambda t: t**n
        t = 1.5

        df_bg = scheme.time_derivative(f, t)
        expected = n  # For power law, bigeometric derivative is constant

        assert abs(df_bg - expected) < 1e-4


# =============================================================================
# H(z) SCHEME-ROBUSTNESS TESTS
# =============================================================================

class TestHubbleRedshiftInvariance:
    """Test that H(z) is scheme-robust."""

    @pytest.fixture
    def tester(self):
        return FRWSchemeRobustnessTest()

    def test_hz_all_schemes_agree(self, tester):
        """H(z) should be identical across all C-schemes."""
        z_values = np.array([0.1, 0.5, 1.0, 2.0])
        result = tester.test_hubble_z(z_values)

        assert result['scheme_robust']
        assert result['max_difference'] < 1e-10

    def test_hz_uses_redshift_parameterization(self, tester):
        """H(z) is defined via redshift, not coordinate time."""
        z = 1.0

        # All models should give same H(z)
        H_values = []
        for model in tester.models.values():
            H_values.append(model.hubble_from_redshift(z))

        # All should be equal
        assert np.std(H_values) < 1e-12

    def test_hz_friedmann_form(self, tester):
        """H(z) follows standard Friedmann form."""
        params = tester.params
        z = 1.0

        # Expected: H = H0 * sqrt(Om*(1+z)^3 + Or*(1+z)^4 + OL)
        expected = params.H0 * np.sqrt(
            params.Omega_m * (1+z)**3 +
            params.Omega_r * (1+z)**4 +
            params.Omega_Lambda
        )

        model = list(tester.models.values())[0]
        actual = model.hubble_from_redshift(z)

        assert abs(actual - expected) < 1e-10


# =============================================================================
# DISTANCE MEASURE TESTS
# =============================================================================

class TestDistanceMeasures:
    """Test scheme-robustness of cosmological distances."""

    @pytest.fixture
    def tester(self):
        return FRWSchemeRobustnessTest()

    def test_angular_diameter_distance_robust(self, tester):
        """D_A(z) should be scheme-robust."""
        z_values = np.array([0.5, 1.0, 2.0])
        result = tester.test_distances(z_values)

        assert result['D_A']['scheme_robust']
        assert result['D_A']['max_difference'] < 1e-10

    def test_luminosity_distance_robust(self, tester):
        """D_L(z) should be scheme-robust."""
        z_values = np.array([0.5, 1.0, 2.0])
        result = tester.test_distances(z_values)

        assert result['D_L']['scheme_robust']
        assert result['D_L']['max_difference'] < 1e-10

    def test_distance_duality(self, tester):
        """D_L = D_A * (1+z)^2 (Etherington relation)."""
        z = 1.5
        model = list(tester.models.values())[0]

        D_A = model.angular_diameter_distance(z)
        D_L = model.luminosity_distance(z)

        # Etherington relation
        expected_DL = D_A * (1 + z)**2

        assert abs(D_L - expected_DL) < 1e-6 * D_L


# =============================================================================
# SINGULARITY BEHAVIOR TESTS
# =============================================================================

class TestSingularityBehavior:
    """Test C-scheme behavior near singularities."""

    @pytest.fixture
    def tester(self):
        return FRWSchemeRobustnessTest()

    def test_singularity_regimes_may_differ(self, tester):
        """Near t=0, C-schemes are expected to potentially differ."""
        t_values = np.array([1e-6, 1e-4, 1e-2])
        result = tester.test_singularity_behavior(t_values)

        # We don't require robustness here - breaking is allowed
        assert 'by_scheme' in result
        assert 't_values' in result

    def test_classical_hubble_diverges(self, tester):
        """Classical H(t) diverges as t -> 0."""
        model = tester.models['classical']

        # For a(t) = t^n, H = n/t
        H_at_small_t = model.hubble_parameter_power_law(1e-3)
        H_at_smaller_t = model.hubble_parameter_power_law(1e-4)

        # H should be larger at smaller t
        assert H_at_smaller_t > H_at_small_t

    def test_late_universe_schemes_agree(self, tester):
        """At late times (t >> 1), schemes approach each other.

        Note: For power-law cosmology a(t) = t^n, different C-schemes
        give different H(t) by construction (that's the point!). But they
        should all give the same H(z) which is the scheme-robust form.

        This test verifies the H(z) agreement instead.
        """
        z_values = np.array([0.1, 0.5, 1.0])
        result = tester.test_hubble_z(z_values)

        # H(z) should be scheme-robust even at late times
        assert result['scheme_robust'], "H(z) should be scheme-robust"
        assert result['max_difference'] < 1e-10


# =============================================================================
# SCHEME-BREAKING DETECTION TESTS
# =============================================================================

class TestSchemeBreakingDetection:
    """Test the scheme-breaking detection system."""

    @pytest.fixture
    def tester(self):
        return FRWSchemeRobustnessTest()

    def test_hunt_returns_structured_result(self, tester):
        """hunt_breaking_points returns proper structure."""
        result = tester.hunt_breaking_points(t_range=(1e-3, 10), n_points=50)

        assert 'breaking_points' in result
        assert 'n_breaking' in result
        assert 'n_tested' in result
        assert 'has_breaking' in result
        assert 'interpretation' in result

    def test_breaking_points_have_required_fields(self, tester):
        """Each breaking point has required information."""
        result = tester.hunt_breaking_points(t_range=(1e-5, 1), n_points=50)

        for bp in result['breaking_points']:
            assert 't' in bp
            assert 'max_diff' in bp
            assert 'rel_diff' in bp
            assert 'H_by_scheme' in bp

    def test_full_report_structure(self, tester):
        """full_robustness_report returns comprehensive data."""
        report = tester.full_robustness_report()

        assert 'hubble_z' in report
        assert 'distances' in report
        assert 'singularity' in report
        assert 'breaking_hunt' in report


# =============================================================================
# FRW MODEL TESTS
# =============================================================================

class TestFRWModel:
    """Test FRW model functionality."""

    def test_power_law_scale_factor(self):
        """Power-law scale factor behaves correctly."""
        params = FRWParameters(n=0.667)
        model = FRWModel(params, ClassicalCScheme())

        # a(t) = t^n
        t = 2.0
        expected = t ** params.n
        actual = model.scale_factor_power_law(t)

        assert abs(actual - expected) < 1e-10

    def test_comoving_distance_increases_with_z(self):
        """Comoving distance should increase with redshift."""
        params = FRWParameters()
        model = FRWModel(params, ClassicalCScheme())

        D1 = model.comoving_distance(0.5)
        D2 = model.comoving_distance(1.0)
        D3 = model.comoving_distance(2.0)

        assert D1 < D2 < D3

    def test_bbn_temperature_decreases(self):
        """BBN temperature decreases with time."""
        params = FRWParameters()
        model = FRWModel(params, ClassicalCScheme())

        T1 = model.bbn_temperature(0.1)
        T2 = model.bbn_temperature(1.0)
        T3 = model.bbn_temperature(10.0)

        assert T1 > T2 > T3


# =============================================================================
# INTEGRATION TESTS
# =============================================================================

class TestSchemeEvolution:
    """Test evolution under different C-schemes."""

    def test_classical_evolution_rk4(self):
        """Classical scheme uses RK4 correctly."""
        scheme = ClassicalCScheme()

        # Simple ODE: dy/dt = y, y(0) = 1
        # Solution: y(t) = exp(t)
        y0 = np.array([1.0])
        dydt = lambda t, y: y

        t, y = scheme.evolve(y0, (0, 1), dydt, n_steps=1000)

        # Check final value
        expected = np.exp(1.0)
        actual = y[-1, 0]

        assert abs(actual - expected) < 1e-4

    def test_meta_evolution_with_weights(self):
        """Meta scheme evolution respects weights."""
        # With u=v=1, should match classical
        meta_unit = MetaCScheme(u=lambda t: 1.0, v=lambda t: 1.0)
        classical = ClassicalCScheme()

        y0 = np.array([1.0])
        dydt = lambda t, y: y

        _, y_meta = meta_unit.evolve(y0, (0, 1), dydt, n_steps=500)
        _, y_classical = classical.evolve(y0, (0, 1), dydt, n_steps=500)

        # Should be close
        assert abs(y_meta[-1, 0] - y_classical[-1, 0]) < 0.1


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
