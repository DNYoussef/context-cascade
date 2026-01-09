"""
Library to Memory MCP Migration Script.

Phase 2 of Cognitive Architecture Integration:
Migrates historical data from file-based storage to Memory MCP.

Tier 1 (High Value - Migrate First):
1. named_modes.json - Pareto-optimal configurations
2. metaloop_optimization_results.json - Iteration tracking
3. policy.json - Governance rules
4. pareto_frontier.json - Full frontier results
5. eval_results/ - Quality history

WHO/WHEN/PROJECT/WHY tagging applied to all entries.
"""

import os
import sys
import json
import glob
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional

# Add parent paths for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from optimization.mcp_client import get_mcp_client, MemoryMCPClient


class LibraryMigrator:
    """Migrates cognitive architecture library to Memory MCP."""

    def __init__(self, base_dir: Optional[Path] = None):
        self.base_dir = base_dir or Path(__file__).parent.parent
        self.storage_dir = self.base_dir / "storage"
        self.integration_dir = self.base_dir / "integration"
        self.tasks_dir = self.base_dir / "tasks"
        self.evals_dir = self.base_dir / "evals"

        self.client = get_mcp_client(namespace="cognitive-architecture/library")
        self.migration_log = []

    def migrate_all_tier1(self) -> Dict[str, Any]:
        """Migrate all Tier 1 (High Value) data."""
        results = {
            "timestamp": datetime.now().isoformat(),
            "tier": 1,
            "migrations": {}
        }

        # 1. Named Modes (Pareto-optimal configurations)
        results["migrations"]["named_modes"] = self._migrate_named_modes()

        # 2. MetaLoop Optimization Results
        results["migrations"]["metaloop_results"] = self._migrate_metaloop_results()

        # 3. Policy/Governance Rules
        results["migrations"]["policy"] = self._migrate_policy()

        # 4. Pareto Frontier
        results["migrations"]["pareto_frontier"] = self._migrate_pareto_frontier()

        # 5. Eval Results (sample - most recent 5)
        results["migrations"]["eval_results"] = self._migrate_eval_results(limit=5)

        # Summary
        total_stored = sum(
            m.get("stored_count", 0) for m in results["migrations"].values()
        )
        total_errors = sum(
            m.get("error_count", 0) for m in results["migrations"].values()
        )

        results["summary"] = {
            "total_stored": total_stored,
            "total_errors": total_errors,
            "mcp_available": self.client.is_available(),
        }

        return results

    def _migrate_named_modes(self) -> Dict[str, Any]:
        """Migrate named_modes.json - Pareto-optimal configurations."""
        paths = [
            self.storage_dir / "real_optimization" / "named_modes.json",
            self.storage_dir / "two_stage_optimization" / "named_modes.json",
        ]

        stored = 0
        errors = 0

        for path in paths:
            if not path.exists():
                continue

            try:
                data = json.loads(path.read_text())
                modes = data.get("modes", data) if isinstance(data, dict) else data

                # Store each mode separately for granular retrieval
                for mode_name, mode_config in modes.items():
                    key = f"named_modes/{mode_name}"
                    metadata = {
                        "WHO": "library-migrator:named_modes",
                        "WHEN": datetime.now().isoformat(),
                        "PROJECT": "cognitive-architecture",
                        "WHY": "optimization",
                        "x-mode-name": mode_name,
                        "x-source-file": str(path.name),
                    }

                    result = self.client.memory_store(key, mode_config, metadata)
                    if result.success:
                        stored += 1
                    else:
                        errors += 1
                        self.migration_log.append(f"Error storing {key}: {result.error}")

            except Exception as e:
                errors += 1
                self.migration_log.append(f"Error processing {path}: {e}")

        return {"stored_count": stored, "error_count": errors}

    def _migrate_metaloop_results(self) -> Dict[str, Any]:
        """Migrate metaloop optimization iteration results."""
        path = self.integration_dir / "metaloop_optimization_results.json"

        if not path.exists():
            return {"stored_count": 0, "error_count": 0, "message": "File not found"}

        try:
            data = json.loads(path.read_text())

            # Handle both list and dict formats
            iterations_count = len(data) if isinstance(data, list) else len(data.get("iterations", []))

            # Wrap list in dict for consistent storage
            store_data = {"iterations": data} if isinstance(data, list) else data

            key = "metaloop/optimization_results"
            metadata = {
                "WHO": "library-migrator:metaloop",
                "WHEN": datetime.now().isoformat(),
                "PROJECT": "cognitive-architecture",
                "WHY": "optimization",
                "x-iterations": str(iterations_count),
            }

            result = self.client.memory_store(key, store_data, metadata)
            return {
                "stored_count": 1 if result.success else 0,
                "error_count": 0 if result.success else 1,
            }

        except Exception as e:
            return {"stored_count": 0, "error_count": 1, "error": str(e)}

    def _migrate_policy(self) -> Dict[str, Any]:
        """Migrate governance policy."""
        paths = [
            self.integration_dir / ".loop" / "policy.json",
            self.storage_dir / "policy.json",
        ]

        for path in paths:
            if not path.exists():
                continue

            try:
                data = json.loads(path.read_text())

                key = "governance/policy"
                metadata = {
                    "WHO": "library-migrator:policy",
                    "WHEN": datetime.now().isoformat(),
                    "PROJECT": "cognitive-architecture",
                    "WHY": "governance",
                    "x-regression-threshold": str(data.get("regression_threshold", 0.03)),
                    "x-max-iterations": str(data.get("max_iterations", 50)),
                }

                result = self.client.memory_store(key, data, metadata)
                return {
                    "stored_count": 1 if result.success else 0,
                    "error_count": 0 if result.success else 1,
                }

            except Exception as e:
                return {"stored_count": 0, "error_count": 1, "error": str(e)}

        return {"stored_count": 0, "error_count": 0, "message": "No policy file found"}

    def _migrate_pareto_frontier(self) -> Dict[str, Any]:
        """Migrate Pareto frontier results."""
        paths = [
            self.storage_dir / "real_optimization" / "pareto_frontier.json",
            self.storage_dir / "two_stage_optimization" / "pareto_frontier.json",
        ]

        stored = 0
        errors = 0

        for path in paths:
            if not path.exists():
                continue

            try:
                data = json.loads(path.read_text())

                # Handle both list and dict formats
                solutions_count = len(data) if isinstance(data, list) else len(data.get("solutions", data.get("frontier", [])))

                source = path.parent.name
                key = f"optimization/pareto_frontier_{source}"
                metadata = {
                    "WHO": "library-migrator:pareto",
                    "WHEN": datetime.now().isoformat(),
                    "PROJECT": "cognitive-architecture",
                    "WHY": "optimization",
                    "x-source": source,
                    "x-solutions-count": str(solutions_count),
                }

                # Wrap list in dict for consistent storage
                store_data = {"frontier": data} if isinstance(data, list) else data

                result = self.client.memory_store(key, store_data, metadata)
                if result.success:
                    stored += 1
                else:
                    errors += 1

            except Exception as e:
                errors += 1
                self.migration_log.append(f"Error processing {path}: {e}")

        return {"stored_count": stored, "error_count": errors}

    def _migrate_eval_results(self, limit: int = 5) -> Dict[str, Any]:
        """Migrate evaluation results (most recent N)."""
        eval_dir = self.storage_dir / "eval_results"

        if not eval_dir.exists():
            return {"stored_count": 0, "error_count": 0, "message": "Eval results dir not found"}

        # Get most recent eval files
        eval_files = sorted(eval_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)[:limit]

        stored = 0
        errors = 0

        for path in eval_files:
            try:
                data = json.loads(path.read_text())

                # Extract skill name from filename (e.g., prompt-architect-eval-20260101-171411.json)
                filename = path.stem
                parts = filename.split("-")
                skill_name = "-".join(parts[:-4]) if len(parts) > 4 else parts[0]

                key = f"evaluations/{filename}"
                metadata = {
                    "WHO": "library-migrator:evaluations",
                    "WHEN": datetime.now().isoformat(),
                    "PROJECT": "cognitive-architecture",
                    "WHY": "evaluation",
                    "x-skill": skill_name,
                    "x-filename": filename,
                }

                result = self.client.memory_store(key, data, metadata)
                if result.success:
                    stored += 1
                else:
                    errors += 1

            except Exception as e:
                errors += 1
                self.migration_log.append(f"Error processing {path}: {e}")

        return {"stored_count": stored, "error_count": errors}


def main():
    """Run the migration."""
    print("=" * 60)
    print("Library to Memory MCP Migration")
    print("=" * 60)

    migrator = LibraryMigrator()

    print("\nStarting Tier 1 migration...")
    results = migrator.migrate_all_tier1()

    print("\n--- Migration Results ---")
    print(f"MCP Available: {results['summary']['mcp_available']}")
    print(f"Total Stored: {results['summary']['total_stored']}")
    print(f"Total Errors: {results['summary']['total_errors']}")

    print("\n--- Per-Category Results ---")
    for category, stats in results["migrations"].items():
        status = "OK" if stats.get("error_count", 0) == 0 else "ERRORS"
        print(f"  {category}: {stats.get('stored_count', 0)} stored [{status}]")

    if migrator.migration_log:
        print("\n--- Migration Log ---")
        for entry in migrator.migration_log:
            print(f"  {entry}")

    # Save migration report
    report_path = Path(__file__).parent.parent / "storage" / "migration_report.json"
    report_path.write_text(json.dumps(results, indent=2))
    print(f"\nReport saved to: {report_path}")

    return results


if __name__ == "__main__":
    main()
