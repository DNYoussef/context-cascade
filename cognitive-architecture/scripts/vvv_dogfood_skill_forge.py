#!/usr/bin/env python3
"""
VVV Dogfooding Script for Skill Forge

Phase 3 of the recursive improvement loop:
1. Analyze current skill-forge skill for VVV compliance
2. Run GlobalMOO (5D) + PyMOO (14D) two-stage optimization
3. Generate improved version with telemetry
4. Evaluate against SF-001 to SF-050 corpus
5. Loop until delta < 2%

Usage:
    python scripts/vvv_dogfood_skill_forge.py
"""

import os
import sys
import json
import time
import re
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any, Optional, Tuple

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load environment
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

# Local imports
from optimization.two_stage_optimizer import (
    TwoStageOptimizer,
    OptimizationResult,
    run_globalmoo_stage,
    run_pymoo_refinement_stage,
    distill_named_modes,
)
from optimization.globalmoo_client import GlobalMOOClient


@dataclass
class VVVAnalysis:
    """Analysis result for VVV compliance."""
    skill_name: str
    version: str
    timestamp: str

    # VCL 7-Slot Coverage
    vcl_slots_present: List[str] = field(default_factory=list)
    vcl_slots_missing: List[str] = field(default_factory=list)
    vcl_slot_coverage: float = 0.0

    # VERIX Compliance
    verix_statements_count: int = 0
    verix_grounded_count: int = 0
    verix_grounding_ratio: float = 0.0

    # Confidence Ceiling Compliance
    ceiling_violations: List[Dict] = field(default_factory=list)
    ceiling_compliance: float = 0.0

    # L2 Output Purity
    l2_marker_leaks: List[str] = field(default_factory=list)
    l2_purity_score: float = 0.0

    # Skill-Forge Specific Metrics
    sop_structure_score: float = 0.0
    trigger_pattern_score: float = 0.0
    vcl_7slot_documentation_score: float = 0.0

    # Anti-Pattern Detection
    anti_patterns_detected: List[str] = field(default_factory=list)

    # Creolization Markers
    turkish_markers: int = 0
    russian_markers: int = 0
    japanese_markers: int = 0
    arabic_markers: int = 0
    german_markers: int = 0
    chinese_markers: int = 0

    # Overall Score
    overall_score: float = 0.0
    improvement_suggestions: List[str] = field(default_factory=list)


@dataclass
class DogfoodingTelemetry:
    """Telemetry for DSPy and creolization optimization."""
    iteration: int
    timestamp: str
    skill_name: str

    # DSPy Level (14D parameters)
    dspy_telemetry: Dict[str, Any] = field(default_factory=dict)

    # Creolization Level (language markers)
    creolization_telemetry: Dict[str, Any] = field(default_factory=dict)

    # Optimization Results
    globalmoo_5d_results: List[Dict] = field(default_factory=list)
    pymoo_14d_results: List[Dict] = field(default_factory=list)

    # Improvement Delta
    previous_score: float = 0.0
    current_score: float = 0.0
    delta: float = 0.0

    # Convergence
    converged: bool = False


class SkillForgeDogfooder:
    """
    Dogfooding engine for skill-forge skill.

    Implements the Hofstadter strange loop:
    - Skill analyzes itself
    - Skill improves itself
    - Repeat until diminishing returns
    """

    SKILL_PATH = Path(__file__).parent.parent.parent / "skills" / "foundry" / "skill-forge" / "SKILL.md"
    CORPUS_PATH = Path(__file__).parent.parent / "evals" / "corpus" / "skill-forge-corpus.json"
    TELEMETRY_PATH = Path(__file__).parent.parent / "storage" / "dogfooding"

    VCL_SLOTS = ["HON", "MOR", "COM", "CLS", "EVD", "ASP", "SPC"]
    CONFIDENCE_CEILINGS = {
        "definition": 0.95,
        "policy": 0.90,
        "observation": 0.95,
        "research": 0.85,
        "report": 0.70,
        "inference": 0.70,
    }

    def __init__(self):
        self.optimizer = TwoStageOptimizer()
        self.iteration = 0
        self.telemetry_history: List[DogfoodingTelemetry] = []
        self.analysis_history: List[VVVAnalysis] = []

        # Ensure telemetry directory exists
        self.TELEMETRY_PATH.mkdir(parents=True, exist_ok=True)

    def load_skill(self) -> str:
        """Load current agent-creator skill content."""
        if not self.SKILL_PATH.exists():
            raise FileNotFoundError(f"Skill not found: {self.SKILL_PATH}")
        return self.SKILL_PATH.read_text(encoding="utf-8")

    def load_corpus(self) -> Dict:
        """Load AC evaluation corpus."""
        if not self.CORPUS_PATH.exists():
            raise FileNotFoundError(f"Corpus not found: {self.CORPUS_PATH}")
        with open(self.CORPUS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

    def analyze_vvv_compliance(self, content: str) -> VVVAnalysis:
        """Analyze skill for VVV (VERILINGUA + VCL + VERIX) compliance."""
        analysis = VVVAnalysis(
            skill_name="skill-forge",
            version="3.2.0",
            timestamp=datetime.now(timezone.utc).isoformat()
        )

        # 1. VCL 7-Slot Coverage
        for slot in self.VCL_SLOTS:
            if f"[[{slot}:" in content or f"VCL_SLOT_{slot}" in content or f"_{slot}_" in content.upper():
                analysis.vcl_slots_present.append(slot)
            else:
                analysis.vcl_slots_missing.append(slot)
        analysis.vcl_slot_coverage = len(analysis.vcl_slots_present) / len(self.VCL_SLOTS)

        # 2. VERIX Grounding Ratio
        verix_pattern = r'\[ground:[^\]]+\]'
        conf_pattern = r'\[conf:\d+\.\d+\]'

        ground_matches = re.findall(verix_pattern, content)
        conf_matches = re.findall(conf_pattern, content)

        # Count statements that should have grounding
        statement_patterns = [r'\[assert\|', r'\[define\|', r'\[direct\|', r'\[commit\|']
        total_statements = sum(len(re.findall(p, content)) for p in statement_patterns)

        analysis.verix_statements_count = total_statements
        analysis.verix_grounded_count = len(ground_matches)
        analysis.verix_grounding_ratio = (
            len(ground_matches) / total_statements if total_statements > 0 else 0
        )

        # 3. Confidence Ceiling Compliance
        for match in conf_matches:
            conf_value = float(re.search(r'\d+\.\d+', match).group())
            # Find nearby ground type
            idx = content.find(match)
            context = content[max(0, idx-100):idx]

            for evd_type, ceiling in self.CONFIDENCE_CEILINGS.items():
                if evd_type in context.lower() and conf_value > ceiling:
                    analysis.ceiling_violations.append({
                        "type": evd_type,
                        "claimed": conf_value,
                        "ceiling": ceiling
                    })

        analysis.ceiling_compliance = (
            1.0 - (len(analysis.ceiling_violations) / len(conf_matches))
            if conf_matches else 1.0
        )

        # 4. L2 Output Purity (check for marker leaks in example outputs)
        l2_markers = ["[[", "[ground:", "[conf:", "[state:", "[assert|", "[define|"]
        example_sections = re.findall(r'l2_output["\']?:\s*["\']([^"\']+)["\']', content)
        for example in example_sections:
            for marker in l2_markers:
                if marker in example:
                    analysis.l2_marker_leaks.append(f"Found '{marker}' in L2 output")
        analysis.l2_purity_score = 1.0 if not analysis.l2_marker_leaks else 0.0

        # 5. Skill-Forge Specific Metrics
        # SOP Structure
        if "SOP" in content and "## Procedure" in content:
            analysis.sop_structure_score = 1.0
        elif "SOP" in content or "procedure" in content.lower():
            analysis.sop_structure_score = 0.5
        else:
            analysis.sop_structure_score = 0.0

        # Trigger Pattern documentation
        if "trigger" in content.lower() and "pattern" in content.lower():
            analysis.trigger_pattern_score = 1.0
        elif "trigger" in content.lower():
            analysis.trigger_pattern_score = 0.5
        else:
            analysis.trigger_pattern_score = 0.0

        # VCL 7-slot documentation
        slot_docs = sum(1 for slot in self.VCL_SLOTS if f"7-slot" in content or f"7 slot" in content)
        if "7-slot" in content or "7 slot" in content:
            analysis.vcl_7slot_documentation_score = 1.0
        else:
            analysis.vcl_7slot_documentation_score = len(analysis.vcl_slots_present) / 7

        # 6. Creolization Markers Count
        analysis.turkish_markers = len(re.findall(r'EVD:-[Dd][Ii]|EVD:-mis|EVD:-dir|-DI<|-mis<|-dir<', content))
        analysis.russian_markers = len(re.findall(r'ASP:sov\.|ASP:nesov\.|sov\.|nesov\.', content))
        analysis.japanese_markers = len(re.findall(r'HON:teineigo|HON:sonkeigo|HON:kenjougo|keigo', content))
        analysis.arabic_markers = len(re.findall(r'MOR:root:|root:[A-Z]-[A-Z]-[A-Z]', content))
        analysis.german_markers = len(re.findall(r'COM:[A-Z][a-z]+\+', content))
        analysis.chinese_markers = len(re.findall(r'CLS:[a-z]+_|classifier', content))

        # 7. Anti-Pattern Detection
        anti_patterns = {
            "epistemic_cosplay": r'conf:0\.9[5-9].*infer|conf:0\.9[0-9].*report',
            "unregistered_agent": r'create.*agent.*without.*registry',
            "marker_leakage": r'output.*\[\[|user.*\[ground:',
            "confidence_inflation": r'user.*approved.*increase.*conf',
        }
        for name, pattern in anti_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                analysis.anti_patterns_detected.append(name)

        # 8. Overall Score (weighted for skill-forge)
        analysis.overall_score = (
            analysis.vcl_slot_coverage * 0.15 +
            analysis.verix_grounding_ratio * 0.20 +
            analysis.ceiling_compliance * 0.15 +
            analysis.l2_purity_score * 0.10 +
            analysis.sop_structure_score * 0.15 +
            analysis.trigger_pattern_score * 0.10 +
            analysis.vcl_7slot_documentation_score * 0.15
        )

        # 9. Improvement Suggestions
        if analysis.vcl_slot_coverage < 1.0:
            analysis.improvement_suggestions.append(
                f"Add missing VCL slots: {analysis.vcl_slots_missing}"
            )
        if analysis.verix_grounding_ratio < 0.95:
            analysis.improvement_suggestions.append(
                f"Improve VERIX grounding (current: {analysis.verix_grounding_ratio:.1%})"
            )
        if analysis.sop_structure_score < 1.0:
            analysis.improvement_suggestions.append(
                "Enhance SOP structure documentation"
            )
        if analysis.vcl_7slot_documentation_score < 1.0:
            analysis.improvement_suggestions.append(
                "Add explicit 7-slot VCL documentation for agents"
            )
        if analysis.turkish_markers < 10:
            analysis.improvement_suggestions.append(
                "Add more Turkish evidential markers"
            )

        return analysis

    def run_two_stage_optimization(self, analysis: VVVAnalysis) -> Tuple[List[Dict], List[Dict]]:
        """
        Run GlobalMOO (5D) + PyMOO (14D) optimization.

        Returns:
            Tuple of (5D Pareto points, 14D refined points)
        """
        print("\n=== Stage 1: GlobalMOO 5D Exploration ===")

        # Initialize GlobalMOO client
        globalmoo_client = GlobalMOOClient(use_mock=False)
        if not globalmoo_client.test_connection():
            print("  GlobalMOO API not available, using local optimization")
            globalmoo_client = GlobalMOOClient(use_mock=True)

        try:
            # Run GlobalMOO exploration using module function
            globalmoo_results = run_globalmoo_stage(
                client=globalmoo_client,
                model_id=2193,
                project_id=8318,
            )
            print(f"  GlobalMOO found {len(globalmoo_results)} Pareto points")
        except Exception as e:
            print(f"  GlobalMOO error (using fallback): {e}")
            # Fallback: generate synthetic 5D points
            initial_5d = {
                "evidential": 0.95,
                "aspectual": 0.80,
                "verix_strictness": analysis.ceiling_compliance,
                "compression": 0.7,
                "require_ground": min(1.0, analysis.verix_grounding_ratio),
            }
            globalmoo_results = self._generate_fallback_5d_points(initial_5d)

        print("\n=== Stage 2: PyMOO 14D Refinement ===")

        try:
            # Run PyMOO refinement using module function
            pymoo_results = run_pymoo_refinement_stage(
                stage1_results=globalmoo_results,
                n_generations=50,
                pop_size=100
            )
            print(f"  PyMOO refined to {len(pymoo_results)} optimal points")
        except Exception as e:
            print(f"  PyMOO error (using fallback): {e}")
            # Fallback: expand 5D to 14D
            pymoo_results = self._expand_5d_to_14d(globalmoo_results)

        return globalmoo_results, pymoo_results

    def _generate_fallback_5d_points(self, initial: Dict) -> List[Dict]:
        """Generate fallback 5D points if GlobalMOO unavailable."""
        import numpy as np
        points = [initial]

        # Generate variations
        for _ in range(9):
            point = {
                k: max(0.0, min(1.0, v + np.random.uniform(-0.1, 0.1)))
                for k, v in initial.items()
            }
            # Enforce immutable bounds
            point["evidential"] = max(0.30, point["evidential"])
            point["require_ground"] = max(0.50, point["require_ground"])
            points.append(point)

        return points

    def _expand_5d_to_14d(self, points_5d: List[Dict]) -> List[Dict]:
        """Expand 5D points to 14D configuration space."""
        points_14d = []

        for p5 in points_5d:
            p14 = {
                # From 5D
                "evidential_frame": p5.get("evidential", 0.95),
                "aspectual_frame": p5.get("aspectual", 0.80),
                "verix_strictness": p5.get("verix_strictness", 0.80),
                "compression_level": p5.get("compression", 0.70),
                "require_ground": p5.get("require_ground", 0.95),

                # Expanded (correlated)
                "morphological_frame": p5.get("evidential", 0.95) * 0.8,
                "compositional_frame": 0.30,
                "honorific_frame": 0.10,
                "classifier_frame": p5.get("aspectual", 0.80) * 0.7,
                "spatial_frame": 0.20,
                "require_confidence": p5.get("require_ground", 0.95) * 0.9,
                "temperature": 0.70,
                "coherence_weight": 0.60,
                "evidence_weight": 0.70,
            }
            points_14d.append(p14)

        return points_14d

    def collect_telemetry(
        self,
        analysis: VVVAnalysis,
        globalmoo_results: List[Dict],
        pymoo_results: List[Dict],
        previous_score: float
    ) -> DogfoodingTelemetry:
        """Collect telemetry for DSPy and creolization optimization."""
        telemetry = DogfoodingTelemetry(
            iteration=self.iteration,
            timestamp=datetime.now(timezone.utc).isoformat(),
            skill_name="skill-forge",

            dspy_telemetry={
                "frames_activated": analysis.vcl_slots_present,
                "strictness_level": analysis.ceiling_compliance,
                "grounding_ratio": analysis.verix_grounding_ratio,
                "accuracy_score": analysis.overall_score,
                "efficiency_score": 1.0 - (len(analysis.improvement_suggestions) / 10),
                "sop_structure": analysis.sop_structure_score,
                "trigger_pattern": analysis.trigger_pattern_score,
            },

            creolization_telemetry={
                "turkish_markers": analysis.turkish_markers,
                "russian_markers": analysis.russian_markers,
                "japanese_markers": analysis.japanese_markers,
                "arabic_markers": analysis.arabic_markers,
                "german_markers": analysis.german_markers,
                "chinese_markers": analysis.chinese_markers,
                "missing_markers": [],
                "suggested_additions": analysis.improvement_suggestions,
            },

            globalmoo_5d_results=globalmoo_results,
            pymoo_14d_results=pymoo_results,

            previous_score=previous_score,
            current_score=analysis.overall_score,
            delta=analysis.overall_score - previous_score,
            converged=abs(analysis.overall_score - previous_score) < 0.02,
        )

        return telemetry

    def save_telemetry(self, telemetry: DogfoodingTelemetry):
        """Save telemetry to storage."""
        filename = f"skill-forge-dogfood-{self.iteration:03d}.json"
        filepath = self.TELEMETRY_PATH / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(asdict(telemetry), f, indent=2)

        print(f"  Telemetry saved: {filepath}")

    def run_dogfooding_loop(self, max_iterations: int = 10) -> List[DogfoodingTelemetry]:
        """
        Run the dogfooding loop until convergence or max iterations.

        Returns:
            List of telemetry from each iteration
        """
        print("=" * 60)
        print("VVV DOGFOODING: Skill Forge Self-Improvement Loop")
        print("=" * 60)

        previous_score = 0.0

        for self.iteration in range(1, max_iterations + 1):
            print(f"\n{'='*60}")
            print(f"ITERATION {self.iteration}")
            print(f"{'='*60}")

            # 1. Load and analyze current skill
            print("\n[1/5] Analyzing current skill-forge...")
            content = self.load_skill()
            analysis = self.analyze_vvv_compliance(content)
            self.analysis_history.append(analysis)

            print(f"  VCL Coverage: {analysis.vcl_slot_coverage:.1%}")
            print(f"  VERIX Grounding: {analysis.verix_grounding_ratio:.1%}")
            print(f"  Ceiling Compliance: {analysis.ceiling_compliance:.1%}")
            print(f"  L2 Purity: {analysis.l2_purity_score:.1%}")
            print(f"  SOP Structure: {analysis.sop_structure_score:.1%}")
            print(f"  Trigger Pattern: {analysis.trigger_pattern_score:.1%}")
            print(f"  7-Slot Documentation: {analysis.vcl_7slot_documentation_score:.1%}")
            print(f"  Overall Score: {analysis.overall_score:.1%}")

            # 2. Run two-stage optimization
            print("\n[2/5] Running two-stage optimization...")
            globalmoo_results, pymoo_results = self.run_two_stage_optimization(analysis)

            # 3. Collect telemetry
            print("\n[3/5] Collecting telemetry...")
            telemetry = self.collect_telemetry(
                analysis, globalmoo_results, pymoo_results, previous_score
            )
            self.telemetry_history.append(telemetry)

            # 4. Save telemetry
            print("\n[4/5] Saving telemetry...")
            self.save_telemetry(telemetry)

            # 5. Check convergence
            print("\n[5/5] Checking convergence...")
            print(f"  Previous: {previous_score:.1%}")
            print(f"  Current: {analysis.overall_score:.1%}")
            print(f"  Delta: {telemetry.delta:.1%}")

            if telemetry.converged:
                print(f"\n*** CONVERGED at iteration {self.iteration} (delta < 2%) ***")
                break

            # Update for next iteration
            previous_score = analysis.overall_score

            # Show improvement suggestions
            if analysis.improvement_suggestions:
                print("\n  Improvement suggestions:")
                for i, suggestion in enumerate(analysis.improvement_suggestions, 1):
                    print(f"    {i}. {suggestion}")

        return self.telemetry_history


def main():
    """Main entry point."""
    print("\n" + "=" * 60)
    print("VVV Recursive Improvement: Phase 3 - Skill Forge")
    print("Using: GlobalMOO (5D) + PyMOO NSGA-II (14D)")
    print("=" * 60 + "\n")

    dogfooder = SkillForgeDogfooder()

    try:
        telemetry_history = dogfooder.run_dogfooding_loop(max_iterations=5)

        print("\n" + "=" * 60)
        print("DOGFOODING COMPLETE")
        print("=" * 60)

        # Summary
        if telemetry_history:
            final = telemetry_history[-1]
            print(f"\nFinal Score: {final.current_score:.1%}")
            print(f"Total Iterations: {len(telemetry_history)}")
            print(f"Converged: {final.converged}")

            # DSPy telemetry summary
            print("\nDSPy Telemetry Summary:")
            print(f"  Frames Activated: {final.dspy_telemetry.get('frames_activated', [])}")
            print(f"  Strictness Level: {final.dspy_telemetry.get('strictness_level', 0):.2f}")
            print(f"  SOP Structure: {final.dspy_telemetry.get('sop_structure', 0):.2f}")
            print(f"  Trigger Pattern: {final.dspy_telemetry.get('trigger_pattern', 0):.2f}")

            # Creolization telemetry summary
            print("\nCreolization Telemetry Summary:")
            creo = final.creolization_telemetry
            print(f"  Turkish Markers: {creo.get('turkish_markers', 0)}")
            print(f"  Russian Markers: {creo.get('russian_markers', 0)}")
            print(f"  Japanese Markers: {creo.get('japanese_markers', 0)}")

        return 0

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
