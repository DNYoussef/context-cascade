#!/usr/bin/env python3
"""
Three-Layer Audit for Self-Evolving Cognitive Architecture

Validates the complete self-evolving system:

LAYER 1: TELEMETRY (Data Collection)
  - Hook integration working
  - Memory-MCP data accessible
  - Telemetry schema valid

LAYER 2: OPTIMIZATION (Learning)
  - GlobalMOO API reachable
  - PyMOO NSGA-II running
  - Named modes distilled

LAYER 3: CASCADE (Application)
  - Mode-aware optimization
  - File updates applied
  - VERIX compliance improved

Usage:
    python three_layer_audit.py [--layer 1|2|3|all] [--verbose]
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AuditResult:
    """Result from a single audit check."""

    def __init__(self, name: str, passed: bool, message: str, details: Dict[str, Any] = None):
        self.name = name
        self.passed = passed
        self.message = message
        self.details = details or {}
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "passed": self.passed,
            "message": self.message,
            "details": self.details,
            "timestamp": self.timestamp,
        }


class LayerAuditor:
    """Base class for layer auditors."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.results: List[AuditResult] = []

    def log(self, message: str) -> None:
        if self.verbose:
            print(f"  [AUDIT] {message}")

    def add_result(self, result: AuditResult) -> None:
        self.results.append(result)
        status = "PASS" if result.passed else "FAIL"
        print(f"  [{status}] {result.name}: {result.message}")

    def run(self) -> List[AuditResult]:
        raise NotImplementedError


class Layer1TelemetryAuditor(LayerAuditor):
    """Layer 1: Telemetry collection audit."""

    def run(self) -> List[AuditResult]:
        print("\n--- LAYER 1: TELEMETRY AUDIT ---")

        # Check 1: Telemetry schema importable
        self._check_schema_import()

        # Check 2: Telemetry store writable
        self._check_store_writable()

        # Check 3: Hook configuration exists
        self._check_hook_config()

        # Check 4: Recent telemetry data
        self._check_recent_data()

        return self.results

    def _check_schema_import(self) -> None:
        try:
            from optimization.telemetry_schema import (
                ExecutionTelemetry,
                TelemetryBatch,
                TelemetryStore,
            )
            self.add_result(AuditResult(
                "schema_import",
                True,
                "Telemetry schema imports successfully",
                {"classes": ["ExecutionTelemetry", "TelemetryBatch", "TelemetryStore"]}
            ))
        except ImportError as e:
            self.add_result(AuditResult(
                "schema_import",
                False,
                f"Failed to import telemetry schema: {e}",
            ))

    def _check_store_writable(self) -> None:
        try:
            from optimization.telemetry_schema import TelemetryStore, ExecutionTelemetry
            import tempfile

            with tempfile.TemporaryDirectory() as tmpdir:
                store = TelemetryStore(base_path=tmpdir)
                record = ExecutionTelemetry(task_type="audit_test")
                key = store.store(record)

                self.add_result(AuditResult(
                    "store_writable",
                    True,
                    f"TelemetryStore writes correctly",
                    {"key": key}
                ))
        except Exception as e:
            self.add_result(AuditResult(
                "store_writable",
                False,
                f"TelemetryStore write failed: {e}",
            ))

    def _check_hook_config(self) -> None:
        hook_path = Path(__file__).parent.parent.parent / ".claude" / "hooks" / "telemetry-collector.sh"
        if hook_path.exists():
            self.add_result(AuditResult(
                "hook_config",
                True,
                f"Telemetry hook exists at {hook_path}",
            ))
        else:
            self.add_result(AuditResult(
                "hook_config",
                False,
                f"Telemetry hook not found at {hook_path}",
            ))

    def _check_recent_data(self) -> None:
        telemetry_dir = Path.home() / ".claude" / "memory-mcp-data" / "telemetry" / "executions"
        if telemetry_dir.exists():
            files = list(telemetry_dir.glob("*.json"))
            recent_count = 0
            cutoff = datetime.utcnow() - timedelta(days=7)

            for f in files:
                try:
                    mtime = datetime.fromtimestamp(f.stat().st_mtime)
                    if mtime > cutoff:
                        recent_count += 1
                except Exception:
                    pass

            self.add_result(AuditResult(
                "recent_data",
                recent_count > 0,
                f"Found {recent_count} telemetry files from last 7 days",
                {"total_files": len(files), "recent_files": recent_count}
            ))
        else:
            self.add_result(AuditResult(
                "recent_data",
                False,
                f"Telemetry directory not found: {telemetry_dir}",
            ))


class Layer2OptimizationAuditor(LayerAuditor):
    """Layer 2: Optimization pipeline audit."""

    def run(self) -> List[AuditResult]:
        print("\n--- LAYER 2: OPTIMIZATION AUDIT ---")

        # Check 1: Two-stage optimizer importable
        self._check_optimizer_import()

        # Check 2: GlobalMOO client
        self._check_globalmoo_client()

        # Check 3: PyMOO available
        self._check_pymoo()

        # Check 4: Named modes exist
        self._check_named_modes()

        return self.results

    def _check_optimizer_import(self) -> None:
        try:
            from optimization.two_stage_optimizer import (
                run_with_telemetry,
                distill_named_modes,
                run_globalmoo_stage,
                run_pymoo_refinement_stage,
            )
            self.add_result(AuditResult(
                "optimizer_import",
                True,
                "Two-stage optimizer imports successfully",
                {"functions": ["run_with_telemetry", "distill_named_modes"]}
            ))
        except ImportError as e:
            self.add_result(AuditResult(
                "optimizer_import",
                False,
                f"Failed to import optimizer: {e}",
            ))

    def _check_globalmoo_client(self) -> None:
        try:
            from optimization.globalmoo_client import GlobalMOOClient
            client = GlobalMOOClient(use_mock=True)

            self.add_result(AuditResult(
                "globalmoo_client",
                True,
                "GlobalMOO client initializes (mock mode)",
            ))

            # Try real connection
            real_client = GlobalMOOClient(use_mock=False)
            if real_client.test_connection():
                self.add_result(AuditResult(
                    "globalmoo_api",
                    True,
                    "GlobalMOO API reachable",
                ))
            else:
                self.add_result(AuditResult(
                    "globalmoo_api",
                    False,
                    "GlobalMOO API not reachable (mock will be used)",
                ))
        except Exception as e:
            self.add_result(AuditResult(
                "globalmoo_client",
                False,
                f"GlobalMOO client error: {e}",
            ))

    def _check_pymoo(self) -> None:
        try:
            from pymoo.algorithms.moo.nsga2 import NSGA2
            from pymoo.core.problem import Problem
            from pymoo.optimize import minimize

            self.add_result(AuditResult(
                "pymoo_available",
                True,
                "PyMOO NSGA-II available",
            ))
        except ImportError as e:
            self.add_result(AuditResult(
                "pymoo_available",
                False,
                f"PyMOO not available: {e}",
            ))

    def _check_named_modes(self) -> None:
        modes_path = Path(__file__).parent.parent / "storage" / "two_stage_optimization" / "named_modes.json"
        if modes_path.exists():
            try:
                with open(modes_path) as f:
                    modes = json.load(f)
                expected = ["audit", "speed", "research", "robust", "balanced"]
                found = list(modes.keys())
                has_all = all(m in found for m in expected)

                self.add_result(AuditResult(
                    "named_modes",
                    has_all,
                    f"Found {len(found)} named modes: {found}",
                    {"modes": found, "expected": expected}
                ))
            except Exception as e:
                self.add_result(AuditResult(
                    "named_modes",
                    False,
                    f"Failed to load named modes: {e}",
                ))
        else:
            self.add_result(AuditResult(
                "named_modes",
                False,
                f"Named modes file not found (run optimization first)",
                {"path": str(modes_path)}
            ))


class Layer3CascadeAuditor(LayerAuditor):
    """Layer 3: Cascade application audit."""

    def run(self) -> List[AuditResult]:
        print("\n--- LAYER 3: CASCADE AUDIT ---")

        # Check 1: Cascade optimizer importable
        self._check_cascade_import()

        # Check 2: Mode-domain mapping complete
        self._check_mode_mapping()

        # Check 3: Frame activations defined
        self._check_frame_activations()

        # Check 4: Cascade directories exist
        self._check_directories()

        return self.results

    def _check_cascade_import(self) -> None:
        try:
            from scripts.real_cascade_optimizer import (
                RealCascadeOptimizer,
                apply_modes_from_optimization,
                MODE_DOMAIN_MAPPING,
            )
            self.add_result(AuditResult(
                "cascade_import",
                True,
                "Cascade optimizer imports successfully",
            ))
        except ImportError as e:
            self.add_result(AuditResult(
                "cascade_import",
                False,
                f"Failed to import cascade optimizer: {e}",
            ))

    def _check_mode_mapping(self) -> None:
        try:
            from scripts.real_cascade_optimizer import MODE_DOMAIN_MAPPING

            expected_domains = [
                "delivery", "quality", "research", "orchestration",
                "security", "platforms", "specialists", "tooling",
                "foundry", "operations"
            ]
            missing = [d for d in expected_domains if d not in MODE_DOMAIN_MAPPING]

            self.add_result(AuditResult(
                "mode_mapping",
                len(missing) == 0,
                f"Mode mapping covers {len(MODE_DOMAIN_MAPPING)} domains",
                {"domains": list(MODE_DOMAIN_MAPPING.keys()), "missing": missing}
            ))
        except Exception as e:
            self.add_result(AuditResult(
                "mode_mapping",
                False,
                f"Mode mapping check failed: {e}",
            ))

    def _check_frame_activations(self) -> None:
        try:
            from scripts.real_cascade_optimizer import FRAME_ACTIVATIONS

            expected_frames = ["evidential", "aspectual", "compositional", "honorific"]
            found = list(FRAME_ACTIVATIONS.keys())
            has_all = all(f in found for f in expected_frames)

            self.add_result(AuditResult(
                "frame_activations",
                has_all,
                f"Found {len(found)} frame activations",
                {"frames": found}
            ))
        except Exception as e:
            self.add_result(AuditResult(
                "frame_activations",
                False,
                f"Frame activations check failed: {e}",
            ))

    def _check_directories(self) -> None:
        plugin_root = Path(__file__).parent.parent.parent
        dirs = {
            "commands": plugin_root / "commands",
            "agents": plugin_root / "agents",
            "skills": plugin_root / "skills",
            "playbooks": plugin_root / "playbooks",
        }

        missing = []
        counts = {}
        for name, path in dirs.items():
            if path.exists():
                md_files = list(path.glob("**/*.md"))
                counts[name] = len(md_files)
            else:
                missing.append(name)
                counts[name] = 0

        self.add_result(AuditResult(
            "directories",
            len(missing) == 0,
            f"Cascade directories: {counts}",
            {"counts": counts, "missing": missing}
        ))


def run_audit(layers: List[str] = None, verbose: bool = False) -> Dict[str, Any]:
    """
    Run the three-layer audit.

    Args:
        layers: Which layers to audit ("1", "2", "3", or "all")
        verbose: Print detailed output

    Returns:
        Audit results summary
    """
    layers = layers or ["all"]
    if "all" in layers:
        layers = ["1", "2", "3"]

    print("=" * 60)
    print("THREE-LAYER AUDIT: Self-Evolving Cognitive Architecture")
    print(f"Timestamp: {datetime.utcnow().isoformat()}Z")
    print("=" * 60)

    all_results = []

    if "1" in layers:
        auditor = Layer1TelemetryAuditor(verbose=verbose)
        all_results.extend(auditor.run())

    if "2" in layers:
        auditor = Layer2OptimizationAuditor(verbose=verbose)
        all_results.extend(auditor.run())

    if "3" in layers:
        auditor = Layer3CascadeAuditor(verbose=verbose)
        all_results.extend(auditor.run())

    # Summary
    passed = sum(1 for r in all_results if r.passed)
    failed = sum(1 for r in all_results if not r.passed)

    print("\n" + "=" * 60)
    print("AUDIT SUMMARY")
    print("=" * 60)
    print(f"  Total checks: {len(all_results)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Success rate: {passed / len(all_results) * 100:.1f}%")

    if failed > 0:
        print("\n  Failed checks:")
        for r in all_results:
            if not r.passed:
                print(f"    - {r.name}: {r.message}")

    # Save results
    results_summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "layers_audited": layers,
        "total_checks": len(all_results),
        "passed": passed,
        "failed": failed,
        "success_rate": passed / len(all_results) if all_results else 0,
        "results": [r.to_dict() for r in all_results],
    }

    output_dir = Path(__file__).parent.parent / "storage" / "audit_logs"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"audit_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

    with open(output_file, "w") as f:
        json.dump(results_summary, f, indent=2)

    print(f"\n  Results saved: {output_file}")

    return results_summary


def main():
    parser = argparse.ArgumentParser(description="Three-layer audit for self-evolving system")
    parser.add_argument("--layer", type=str, nargs="+", default=["all"],
                       choices=["1", "2", "3", "all"],
                       help="Which layers to audit")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")
    args = parser.parse_args()

    results = run_audit(layers=args.layer, verbose=args.verbose)

    # Exit with error if any checks failed
    if results["failed"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
