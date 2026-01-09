"""
Telemetry Bridge - Converts between loop formats and existing telemetry schema.

This module bridges:
- .loop/eval_report.json (new integration format)
- ExecutionTelemetry (cognitive architecture format)
- Memory-MCP storage format (v3.0 with x- prefixes)

INVARIANTS:
- Never use model-reported metrics
- Always use harness-graded metrics
- Maintain v3.0 schema compliance
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

# Add parent paths for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from optimization.telemetry_schema import ExecutionTelemetry, TelemetryStore
from optimization.mcp_client import get_mcp_client, MemoryMCPClient

logger = logging.getLogger(__name__)


@dataclass
class LoopTelemetryRecord:
    """
    A telemetry record that combines loop state with cognitive architecture metrics.

    This is the unified format that flows to Memory-MCP.
    """
    # Identity
    task_id: str
    timestamp: str
    session_id: Optional[str] = None

    # Loop state
    iteration: int = 0
    plane: str = "execution"
    timescale: str = "micro"

    # Configuration (from runtime_config.json)
    mode: str = "balanced"
    vector14: List[float] = field(default_factory=list)
    active_frames: List[str] = field(default_factory=list)
    verix_strictness: str = "MODERATE"
    compression_level: str = "L1"

    # Metrics (from eval_report.json - harness only)
    task_accuracy: float = 0.0
    token_efficiency: float = 0.0
    edge_robustness: float = 0.0
    epistemic_consistency: float = 0.0
    overall_score: float = 0.0

    # Decision
    decision: str = "continue"
    reason: str = ""

    # Git state
    git_head: Optional[str] = None

    def to_execution_telemetry(self) -> ExecutionTelemetry:
        """Convert to cognitive architecture ExecutionTelemetry format."""
        return ExecutionTelemetry(
            task_id=self.task_id,
            timestamp=self.timestamp,
            session_id=self.session_id,
            config_vector=self.vector14,
            active_frames=self.active_frames,
            verix_strictness={"RELAXED": 0, "MODERATE": 1, "STRICT": 2}.get(self.verix_strictness, 1),
            compression_level={"L0": 0, "L1": 1, "L2": 2}.get(self.compression_level, 1),
            task_type="general",
            aggregate_frame_score=self.epistemic_consistency,
            verix_compliance_score=self.epistemic_consistency,
            task_success=self.decision != "halt",
            error_occurred=self.decision == "halt" and "error" in self.reason.lower(),
            agent_type=f"ralph_loop_iteration_{self.iteration}",
        )

    def to_memory_mcp_format(self) -> Dict[str, Any]:
        """
        Convert to Memory-MCP v3.0 format with x- prefixes.

        Uses WHO/WHEN/PROJECT/WHY tagging protocol.
        """
        return {
            # Identity
            "task_id": self.task_id,
            "timestamp": self.timestamp,

            # WHO/WHEN/PROJECT/WHY tags
            "x-who": f"ralph_loop_iteration_{self.iteration}",
            "x-when": self.timestamp,
            "x-project": "cognitive-architecture-integration",
            "x-why": "loop-telemetry",

            # Loop state
            "x-iteration": self.iteration,
            "x-plane": self.plane,
            "x-timescale": self.timescale,

            # Configuration
            "x-mode": self.mode,
            "x-vector14": self.vector14,
            "x-active-frames": self.active_frames,
            "x-verix-strictness": self.verix_strictness,
            "x-compression-level": self.compression_level,

            # Metrics (harness-graded only)
            "task_accuracy": self.task_accuracy,
            "token_efficiency": self.token_efficiency,
            "edge_robustness": self.edge_robustness,
            "epistemic_consistency": self.epistemic_consistency,
            "overall_score": self.overall_score,

            # Decision
            "decision": self.decision,
            "reason": self.reason,

            # Git
            "git_head": self.git_head,

            # Schema version
            "_schema_version": "3.0",
        }

    @classmethod
    def from_loop_state(
        cls,
        eval_report: Dict[str, Any],
        runtime_config: Dict[str, Any],
        event: Dict[str, Any],
    ) -> "LoopTelemetryRecord":
        """
        Create record from loop state files.

        Args:
            eval_report: Contents of eval_report.json
            runtime_config: Contents of runtime_config.json
            event: A UnifiedEvent dict

        Returns:
            LoopTelemetryRecord
        """
        metrics = eval_report.get("metrics", {})
        frames = runtime_config.get("frames", {})

        return cls(
            task_id=event.get("task_id", f"ralph_{event.get('iteration', 0)}"),
            timestamp=event.get("timestamp", datetime.now().isoformat()),
            iteration=event.get("iteration", 0),
            plane=event.get("plane", "execution"),
            timescale=event.get("timescale", "micro"),
            mode=runtime_config.get("mode", "balanced"),
            vector14=runtime_config.get("vector14", []),
            active_frames=[k for k, v in frames.items() if v],
            verix_strictness=runtime_config.get("verix", {}).get("strictness", "MODERATE"),
            compression_level=runtime_config.get("verix", {}).get("compression", "L1"),
            task_accuracy=metrics.get("task_accuracy", 0.0),
            token_efficiency=metrics.get("token_efficiency", 0.0),
            edge_robustness=metrics.get("edge_robustness", 0.0),
            epistemic_consistency=metrics.get("epistemic_consistency", 0.0),
            overall_score=metrics.get("overall", 0.0),
            decision=event.get("decision", "continue"),
            reason=event.get("reason", ""),
            git_head=event.get("git_head"),
        )


class TelemetryBridge:
    """
    Bridge that syncs loop telemetry with cognitive architecture telemetry store.

    This maintains consistency between:
    - .loop/ contract files
    - Cognitive architecture telemetry
    - Memory-MCP storage
    """

    def __init__(self, loop_dir: Path, telemetry_store: Optional[TelemetryStore] = None):
        self.loop_dir = Path(loop_dir)
        self.telemetry_store = telemetry_store or TelemetryStore()

    def sync_iteration(self, iteration: int) -> Optional[LoopTelemetryRecord]:
        """
        Sync a specific iteration's telemetry.

        Reads from .loop/ files and stores in cognitive architecture format.
        """
        # Load loop state files
        eval_report = self._load_json(self.loop_dir / "eval_report.json")
        runtime_config = self._load_json(self.loop_dir / "runtime_config.json")
        events = self._load_events()

        # Find event for this iteration
        event = None
        for e in events:
            if e.get("iteration") == iteration:
                event = e
                break

        if event is None:
            return None

        # Create unified record
        record = LoopTelemetryRecord.from_loop_state(eval_report, runtime_config, event)

        # Store in cognitive architecture format
        exec_telemetry = record.to_execution_telemetry()
        self.telemetry_store.store(exec_telemetry)

        return record

    def sync_all(self) -> List[LoopTelemetryRecord]:
        """Sync all iterations from events.jsonl."""
        events = self._load_events()
        records = []

        eval_report = self._load_json(self.loop_dir / "eval_report.json")
        runtime_config = self._load_json(self.loop_dir / "runtime_config.json")

        for event in events:
            record = LoopTelemetryRecord.from_loop_state(eval_report, runtime_config, event)
            exec_telemetry = record.to_execution_telemetry()
            self.telemetry_store.store(exec_telemetry)
            records.append(record)

        return records

    def export_to_memory_mcp(self) -> List[Dict[str, Any]]:
        """Export all records in Memory-MCP v3.0 format."""
        events = self._load_events()
        eval_report = self._load_json(self.loop_dir / "eval_report.json")
        runtime_config = self._load_json(self.loop_dir / "runtime_config.json")

        records = []
        for event in events:
            record = LoopTelemetryRecord.from_loop_state(eval_report, runtime_config, event)
            records.append(record.to_memory_mcp_format())

        return records

    def store_to_memory_mcp(
        self,
        iteration: Optional[int] = None,
        mcp_client: Optional[MemoryMCPClient] = None,
    ) -> Dict[str, Any]:
        """
        Store telemetry record(s) to Memory MCP.

        This is the actual storage operation that completes the telemetry pipeline.

        Args:
            iteration: Specific iteration to store (None = all)
            mcp_client: Optional MCP client (uses default if not provided)

        Returns:
            Summary of storage operations
        """
        client = mcp_client or get_mcp_client(namespace="cognitive-architecture/telemetry")

        events = self._load_events()
        eval_report = self._load_json(self.loop_dir / "eval_report.json")
        runtime_config = self._load_json(self.loop_dir / "runtime_config.json")

        stored = []
        errors = []

        for event in events:
            # Filter by iteration if specified
            event_iteration = event.get("iteration", 0)
            if iteration is not None and event_iteration != iteration:
                continue

            record = LoopTelemetryRecord.from_loop_state(eval_report, runtime_config, event)
            mcp_format = record.to_memory_mcp_format()

            # Build storage key
            key = f"iteration_{event_iteration}_{record.timestamp}"

            # Build WHO/WHEN/PROJECT/WHY metadata
            metadata = {
                "WHO": f"telemetry-bridge:ralph_iteration_{event_iteration}",
                "WHEN": record.timestamp,
                "PROJECT": "cognitive-architecture",
                "WHY": "loop-telemetry",
                "x-iteration": str(event_iteration),
                "x-overall-score": str(record.overall_score),
                "x-decision": record.decision,
                "x-evaluation-mode": mcp_format.get("evaluation_mode", "unknown"),
            }

            # Store to Memory MCP
            result = client.memory_store(
                key=key,
                value=mcp_format,
                metadata=metadata,
            )

            if result.success:
                stored.append({
                    "iteration": event_iteration,
                    "key": key,
                    "location": result.data.get("location", "unknown"),
                })
                logger.info(f"Stored telemetry for iteration {event_iteration}")
            else:
                errors.append({
                    "iteration": event_iteration,
                    "error": result.error,
                })
                logger.error(f"Failed to store telemetry for iteration {event_iteration}: {result.error}")

        return {
            "stored_count": len(stored),
            "error_count": len(errors),
            "stored": stored,
            "errors": errors,
            "mcp_available": client.is_available(),
        }

    def _load_json(self, path: Path) -> Dict[str, Any]:
        """Load JSON file or return empty dict."""
        if path.exists():
            return json.loads(path.read_text())
        return {}

    def _load_events(self) -> List[Dict[str, Any]]:
        """Load events from events.jsonl."""
        events_path = self.loop_dir / "events.jsonl"
        events = []

        if events_path.exists():
            for line in events_path.read_text().strip().split("\n"):
                if line.strip():
                    try:
                        events.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue

        return events


def bridge_loop_to_telemetry(loop_dir: str) -> Dict[str, Any]:
    """
    Convenience function to bridge loop state to telemetry.

    Args:
        loop_dir: Path to .loop/ directory

    Returns:
        Summary of bridged records
    """
    bridge = TelemetryBridge(Path(loop_dir))
    records = bridge.sync_all()

    return {
        "records_synced": len(records),
        "iterations": [r.iteration for r in records],
        "latest_score": records[-1].overall_score if records else 0.0,
    }
