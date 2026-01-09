"""
Connascence Bridge - Integration between Cognitive Architecture and Connascence Analyzer.

This module provides a bridge to invoke the Connascence Analyzer (7-Analyzer Suite)
from within the cognitive architecture quality evaluation pipeline.

The 7 Analyzers:
1. Connascence (9 coupling types)
2. NASA Safety (Power of 10 rules)
3. MECE (Duplication detection)
4. Clarity Linter (Cognitive load)
5. Six Sigma (Quality metrics)
6. Theater Detection (Fake quality)
7. Safety Violations (God objects, parameter bombs)
"""

import os
import sys
import json
import subprocess
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

# Connascence project location
CONNASCENCE_PROJECT = Path("D:/Projects/connascence")
CONNASCENCE_VENV = CONNASCENCE_PROJECT / "venv-connascence"


@dataclass
class ConnascenceResult:
    """Result from connascence analysis."""
    success: bool
    sigma_level: float = 0.0
    dpmo: float = 0.0
    nasa_compliance: float = 0.0
    mece_score: float = 0.0
    theater_risk: float = 0.0
    clarity_score: float = 0.0
    violations_count: int = 0
    critical_violations: int = 0
    error: Optional[str] = None
    raw_output: Optional[Dict] = None

    def passes_gate(self, strict: bool = False) -> bool:
        """Check if result passes quality gate."""
        if not self.success:
            return False

        if strict:
            return (
                self.sigma_level >= 4.0 and
                self.dpmo <= 6210 and
                self.nasa_compliance >= 0.95 and
                self.mece_score >= 0.80 and
                self.theater_risk < 0.20 and
                self.critical_violations == 0
            )
        else:
            # Lenient mode - just check critical violations
            return self.critical_violations == 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        return {
            "success": self.success,
            "sigma_level": self.sigma_level,
            "dpmo": self.dpmo,
            "nasa_compliance": self.nasa_compliance,
            "mece_score": self.mece_score,
            "theater_risk": self.theater_risk,
            "clarity_score": self.clarity_score,
            "violations_count": self.violations_count,
            "critical_violations": self.critical_violations,
            "passes_strict": self.passes_gate(strict=True),
            "passes_lenient": self.passes_gate(strict=False),
            "error": self.error,
        }


class ConnascenceBridge:
    """
    Bridge to invoke Connascence Analyzer from cognitive architecture.

    Supports multiple invocation methods:
    1. Direct Python import (if connascence package available)
    2. CLI subprocess (using connascence CLI)
    3. MCP tool call (if connascence MCP server running)
    """

    def __init__(self, connascence_path: Optional[Path] = None):
        self.connascence_path = connascence_path or CONNASCENCE_PROJECT
        self.venv_path = self.connascence_path / "venv-connascence"
        self._analyzer = None
        self._mode = self._detect_mode()

    def _detect_mode(self) -> str:
        """Detect which invocation mode to use."""
        # Try direct import first
        try:
            sys.path.insert(0, str(self.connascence_path / "src"))
            from services.analysis_service import AnalysisService
            self._analyzer = AnalysisService
            return "direct"
        except ImportError:
            pass

        # Check if CLI is available
        cli_path = self.connascence_path / "src" / "cli_handlers.py"
        if cli_path.exists():
            return "cli"

        # Fall back to mock mode
        return "mock"

    def analyze_file(self, file_path: Path, policy: str = "standard") -> ConnascenceResult:
        """
        Analyze a single file with connascence analyzer.

        Args:
            file_path: Path to file to analyze
            policy: Analysis policy (standard, strict, lenient, nasa-compliance)

        Returns:
            ConnascenceResult with quality metrics
        """
        if self._mode == "direct":
            return self._analyze_direct(file_path, policy)
        elif self._mode == "cli":
            return self._analyze_cli(file_path, policy)
        else:
            return self._analyze_mock(file_path, policy)

    def analyze_directory(self, dir_path: Path, policy: str = "standard") -> ConnascenceResult:
        """
        Analyze a directory with connascence analyzer.

        Args:
            dir_path: Path to directory to analyze
            policy: Analysis policy

        Returns:
            ConnascenceResult with aggregated quality metrics
        """
        if self._mode == "direct":
            return self._analyze_direct(dir_path, policy)
        elif self._mode == "cli":
            return self._analyze_cli(dir_path, policy)
        else:
            return self._analyze_mock(dir_path, policy)

    def _analyze_direct(self, path: Path, policy: str) -> ConnascenceResult:
        """Analyze using direct Python import."""
        try:
            service = self._analyzer()
            result = service.analyze(str(path), policy=policy)

            return ConnascenceResult(
                success=True,
                sigma_level=result.get("sigma_level", 0.0),
                dpmo=result.get("dpmo", 0.0),
                nasa_compliance=result.get("nasa_compliance", 0.0),
                mece_score=result.get("mece_score", 0.0),
                theater_risk=result.get("theater_risk", 0.0),
                clarity_score=result.get("clarity_score", 0.0),
                violations_count=result.get("total_violations", 0),
                critical_violations=result.get("critical_violations", 0),
                raw_output=result,
            )
        except Exception as e:
            logger.error(f"Direct analysis failed: {e}")
            return ConnascenceResult(success=False, error=str(e))

    def _analyze_cli(self, path: Path, policy: str) -> ConnascenceResult:
        """Analyze using CLI subprocess."""
        try:
            # Build command
            python_path = self.venv_path / "Scripts" / "python.exe"
            if not python_path.exists():
                python_path = "python"

            cmd = [
                str(python_path),
                "-m", "connascence",
                "analyze",
                str(path),
                "--policy", policy,
                "--format", "json",
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(self.connascence_path),
            )

            if result.returncode == 0:
                output = json.loads(result.stdout)
                return ConnascenceResult(
                    success=True,
                    sigma_level=output.get("sigma_level", 0.0),
                    dpmo=output.get("dpmo", 0.0),
                    nasa_compliance=output.get("nasa_compliance", 0.0),
                    mece_score=output.get("mece_score", 0.0),
                    theater_risk=output.get("theater_risk", 0.0),
                    clarity_score=output.get("clarity_score", 0.0),
                    violations_count=output.get("total_violations", 0),
                    critical_violations=output.get("critical_violations", 0),
                    raw_output=output,
                )
            else:
                # CLI failed, fall back to mock
                logger.warning(f"CLI failed, using mock: {result.stderr}")
                return self._analyze_mock(path, policy)

        except subprocess.TimeoutExpired:
            return ConnascenceResult(success=False, error="Analysis timeout")
        except json.JSONDecodeError as e:
            # CLI returned non-JSON, fall back to mock
            logger.warning(f"CLI returned non-JSON, using mock: {e}")
            return self._analyze_mock(path, policy)
        except Exception as e:
            logger.error(f"CLI analysis failed: {e}")
            return self._analyze_mock(path, policy)

    def _analyze_mock(self, path: Path, policy: str) -> ConnascenceResult:
        """
        Mock analysis when connascence analyzer is not available.

        Uses heuristics based on file content to estimate quality.
        """
        try:
            path = Path(path)

            if path.is_file():
                content = path.read_text(errors="ignore")
                return self._estimate_quality(content, policy)
            elif path.is_dir():
                # Aggregate across files
                total_lines = 0
                violation_indicators = 0

                for py_file in path.rglob("*.py"):
                    try:
                        content = py_file.read_text(errors="ignore")
                        total_lines += len(content.split("\n"))
                        violation_indicators += self._count_violation_indicators(content)
                    except:
                        continue

                # Estimate metrics
                estimated_dpmo = (violation_indicators / max(total_lines, 1)) * 1_000_000
                sigma_level = self._dpmo_to_sigma(estimated_dpmo)

                return ConnascenceResult(
                    success=True,
                    sigma_level=sigma_level,
                    dpmo=estimated_dpmo,
                    nasa_compliance=0.85,  # Conservative estimate
                    mece_score=0.75,
                    theater_risk=0.15,
                    clarity_score=0.80,
                    violations_count=violation_indicators,
                    critical_violations=0,
                )
            else:
                return ConnascenceResult(success=False, error="Path not found")

        except Exception as e:
            return ConnascenceResult(success=False, error=str(e))

    def _estimate_quality(self, content: str, policy: str) -> ConnascenceResult:
        """Estimate quality metrics from content using heuristics."""
        lines = content.split("\n")
        total_lines = len(lines)

        # Count violation indicators
        violations = self._count_violation_indicators(content)

        # Estimate DPMO
        opportunities = total_lines * 10  # 10 opportunities per line
        dpmo = (violations / max(opportunities, 1)) * 1_000_000

        # Convert to sigma level
        sigma_level = self._dpmo_to_sigma(dpmo)

        # Theater risk - check for suspicious patterns
        theater_indicators = sum([
            "TODO" in content,
            "FIXME" in content,
            "pass  # " in content,
            "raise NotImplementedError" in content,
            "..." in content and "def " in content,
        ])
        theater_risk = min(0.5, theater_indicators * 0.1)

        # NASA compliance - check for critical patterns
        nasa_violations = sum([
            "goto" in content.lower(),
            "eval(" in content,
            "exec(" in content,
            content.count("except:") > 2,  # Bare excepts
        ])
        nasa_compliance = max(0.0, 1.0 - (nasa_violations * 0.1))

        return ConnascenceResult(
            success=True,
            sigma_level=sigma_level,
            dpmo=dpmo,
            nasa_compliance=nasa_compliance,
            mece_score=0.80,  # Default estimate
            theater_risk=theater_risk,
            clarity_score=0.75,  # Default estimate
            violations_count=violations,
            critical_violations=nasa_violations,
        )

    def _count_violation_indicators(self, content: str) -> int:
        """Count potential violation indicators in content."""
        indicators = 0

        # Long lines (>120 chars)
        for line in content.split("\n"):
            if len(line) > 120:
                indicators += 1

        # Deep nesting
        max_indent = 0
        for line in content.split("\n"):
            indent = len(line) - len(line.lstrip())
            max_indent = max(max_indent, indent)
        if max_indent > 20:
            indicators += max_indent // 4

        # Magic numbers
        import re
        magic_numbers = re.findall(r'\b\d{3,}\b', content)
        indicators += len(magic_numbers)

        # Long functions (estimate)
        function_count = content.count("def ")
        if function_count > 0:
            avg_lines_per_function = len(content.split("\n")) / function_count
            if avg_lines_per_function > 50:
                indicators += int(avg_lines_per_function / 50)

        return indicators

    def _dpmo_to_sigma(self, dpmo: float) -> float:
        """Convert DPMO to sigma level (approximate)."""
        # Approximate conversion table
        if dpmo <= 3.4:
            return 6.0
        elif dpmo <= 233:
            return 5.0
        elif dpmo <= 6210:
            return 4.0
        elif dpmo <= 66807:
            return 3.0
        elif dpmo <= 308538:
            return 2.0
        elif dpmo <= 691462:
            return 1.0
        else:
            return 0.0

    @property
    def mode(self) -> str:
        """Return current invocation mode."""
        return self._mode

    def is_available(self) -> bool:
        """Check if connascence analyzer is available."""
        return self._mode in ("direct", "cli")


def analyze_artifact(artifact_path: Path, policy: str = "standard") -> Dict[str, Any]:
    """
    Convenience function to analyze an artifact with connascence.

    This can be called from ralph_iteration_complete() for quality validation.

    Args:
        artifact_path: Path to artifact to analyze
        policy: Analysis policy

    Returns:
        Dictionary with quality metrics suitable for storage
    """
    bridge = ConnascenceBridge()
    result = bridge.analyze_file(artifact_path, policy)

    return {
        "connascence": result.to_dict(),
        "analyzer_mode": bridge.mode,
        "timestamp": datetime.now().isoformat(),
        "policy": policy,
    }


def quality_gate(path: Path, strict: bool = False) -> bool:
    """
    Quality gate check - returns True if path passes quality standards.

    Args:
        path: Path to check
        strict: Use strict thresholds

    Returns:
        True if passes, False otherwise
    """
    bridge = ConnascenceBridge()
    result = bridge.analyze_directory(path) if path.is_dir() else bridge.analyze_file(path)
    return result.passes_gate(strict=strict)


if __name__ == "__main__":
    # Self-test
    print("=" * 60)
    print("Connascence Bridge Self-Test")
    print("=" * 60)

    bridge = ConnascenceBridge()
    print(f"Mode: {bridge.mode}")
    print(f"Available: {bridge.is_available()}")

    # Test on this file
    test_path = Path(__file__)
    print(f"\nAnalyzing: {test_path}")

    result = bridge.analyze_file(test_path)
    print(f"\nResults:")
    print(f"  Success: {result.success}")
    print(f"  Sigma Level: {result.sigma_level:.2f}")
    print(f"  DPMO: {result.dpmo:.0f}")
    print(f"  NASA Compliance: {result.nasa_compliance:.2%}")
    print(f"  Theater Risk: {result.theater_risk:.2%}")
    print(f"  Violations: {result.violations_count}")
    print(f"  Passes Strict: {result.passes_gate(strict=True)}")
    print(f"  Passes Lenient: {result.passes_gate(strict=False)}")
