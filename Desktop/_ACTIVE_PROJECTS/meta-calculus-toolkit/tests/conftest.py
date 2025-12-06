#!/usr/bin/env python3
"""
Pytest configuration for meta-calculus test suite.

Provides fixtures used across test modules.
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class _TestResults:
    """
    Accumulator for test results.

    Renamed from TestResults to _TestResults to prevent pytest from
    trying to collect it as a test class.
    """
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.results = []

    def record(self, name: str, passed: bool, details: str = ""):
        self.results.append({
            'name': name,
            'passed': passed,
            'details': details
        })
        if passed:
            self.passed += 1
            print(f"  [PASS] {name}")
        else:
            self.failed += 1
            print(f"  [FAIL] {name}: {details}")

    def summary(self):
        total = self.passed + self.failed
        print(f"\n{'='*70}")
        print(f"SUMMARY: {self.passed}/{total} tests passed")
        if self.failed > 0:
            print(f"\nFailed tests:")
            for r in self.results:
                if not r['passed']:
                    print(f"  - {r['name']}: {r['details']}")
        print(f"{'='*70}")
        return self.failed == 0

    def assert_all_passed(self):
        """Assert that all recorded tests passed (for pytest integration)."""
        for r in self.results:
            assert r['passed'], f"{r['name']}: {r['details']}"


# Alias for backwards compatibility
TestResults = _TestResults


@pytest.fixture
def results():
    """Provide a TestResults instance for tests."""
    return _TestResults()
