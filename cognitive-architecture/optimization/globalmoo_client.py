"""
GlobalMOO API client wrapper.

Provides interface to GlobalMOO multi-objective optimization API for:
- Creating optimization models and projects
- Loading initial seed cases
- Inverse suggestions (target outcomes -> config vectors)
- Reporting evaluation results
- Extracting Pareto frontier and impact factors

API:
- Base URI: https://app.globalmoo.com/api (CORRECT endpoint)
- Auth: Bearer token from GLOBALMOO_API_KEY

Discovered API Patterns (2025-12-28):
- POST /models - Create model (name, description)
- GET /models - List models
- GET /models/{id} - Get model with projects
- POST /models/{id}/projects - Create project (name, inputCount, minimums, maximums, inputTypes)

Note: Subscription limits may apply (e.g., max 5 input dimensions on free tier).
      Trial/objective/inverse endpoints require specific subscription levels.
"""

import os
import json
import time
import hashlib
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum
import sys
import logging
from functools import wraps

# Add parent for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logger = logging.getLogger(__name__)


def retry_with_backoff(max_attempts: int = 3, base_delay: float = 1.0, max_delay: float = 30.0):
    """
    Decorator for retrying API calls with exponential backoff.
    
    Args:
        max_attempts: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay between retries
    
    FIX: Added to prevent GlobalMOO API failures from breaking optimization.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        delay = min(base_delay * (2 ** attempt), max_delay)
                        logger.warning(
                            f"API call failed (attempt {attempt + 1}/{max_attempts}): {e}. "
                            f"Retrying in {delay:.1f}s..."
                        )
                        time.sleep(delay)
                    else:
                        logger.error(f"API call failed after {max_attempts} attempts: {e}")
            raise last_exception
        return wrapper
    return decorator

try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    HTTPX_AVAILABLE = False

from core.config import FullConfig, VectorCodec


class ObjectiveDirection(Enum):
    """Direction for optimization objectives."""
    MAXIMIZE = "maximize"
    MINIMIZE = "minimize"


# FR3.1: Two-tier optimization bounds (Hofstadter Nomic pattern)
# IMMUTABLE tier: Core safety constraints that CANNOT be violated
# MUTABLE tier: Parameters that optimization can freely adjust

@dataclass
class TwoTierBounds:
    """
    Two-tier optimization bounds following Hofstadter's Nomic pattern.

    TIER 1 (IMMUTABLE): Core constraints for system safety
    - evidential_min: Minimum evidential frame weight (epistemic hygiene)
    - require_ground_min: Minimum ground requirement (prevents hallucination)

    TIER 2 (MUTABLE): Freely optimizable within 0.0-1.0
    - All other frame weights and parameters
    """

    # IMMUTABLE bounds (cannot be crossed by optimization)
    evidential_min: float = 0.3  # Core evidence marking must be >= 30%
    require_ground_min: float = 0.5  # Ground requirement must be >= 50%

    # MUTABLE bounds (freely optimizable)
    mutable_min: float = 0.0
    mutable_max: float = 1.0

    # Index mapping for constraint application
    # These indices map to positions in the config vector
    IMMUTABLE_INDICES: Dict[str, int] = field(default_factory=lambda: {
        "evidential": 0,  # First frame in vector
        "require_ground": 9,  # Position of require_ground in FullConfig
    })

    def constrain_suggestion(self, suggestion: List[float]) -> List[float]:
        """
        Apply two-tier constraints to a suggestion vector.

        IMMUTABLE constraints are enforced with hard bounds.
        MUTABLE values are clamped to valid range.

        Args:
            suggestion: Raw suggestion vector from optimizer

        Returns:
            Constrained vector respecting two-tier architecture
        """
        constrained = list(suggestion)  # Don't mutate input

        # Apply IMMUTABLE tier constraints
        evidential_idx = self.IMMUTABLE_INDICES.get("evidential", 0)
        require_ground_idx = self.IMMUTABLE_INDICES.get("require_ground", 9)

        if len(constrained) > evidential_idx:
            constrained[evidential_idx] = max(
                self.evidential_min,
                constrained[evidential_idx]
            )

        if len(constrained) > require_ground_idx:
            constrained[require_ground_idx] = max(
                self.require_ground_min,
                constrained[require_ground_idx]
            )

        # Apply MUTABLE tier bounds (clamp to valid range)
        for i in range(len(constrained)):
            if i not in self.IMMUTABLE_INDICES.values():
                constrained[i] = max(
                    self.mutable_min,
                    min(self.mutable_max, constrained[i])
                )

        return constrained

    def validate_config(self, config_vector: List[float]) -> Tuple[bool, List[str]]:
        """
        Validate a config vector against two-tier bounds.

        Args:
            config_vector: Configuration to validate

        Returns:
            Tuple of (is_valid, list_of_violations)
        """
        violations = []

        evidential_idx = self.IMMUTABLE_INDICES.get("evidential", 0)
        require_ground_idx = self.IMMUTABLE_INDICES.get("require_ground", 9)

        if len(config_vector) > evidential_idx:
            if config_vector[evidential_idx] < self.evidential_min:
                violations.append(
                    f"evidential ({config_vector[evidential_idx]:.2f}) "
                    f"< minimum ({self.evidential_min})"
                )

        if len(config_vector) > require_ground_idx:
            if config_vector[require_ground_idx] < self.require_ground_min:
                violations.append(
                    f"require_ground ({config_vector[require_ground_idx]:.2f}) "
                    f"< minimum ({self.require_ground_min})"
                )

        return len(violations) == 0, violations


# Global default bounds instance
DEFAULT_TIER_BOUNDS = TwoTierBounds()


# FR3.3: Thrashing detection and recovery
@dataclass
class ThrashingDetector:
    """
    Detect and recover from optimization thrashing (FR3.3).

    Thrashing occurs when the optimizer oscillates between configurations
    without making progress. This can happen due to:
    - Conflicting objectives
    - Noisy fitness evaluations
    - Local optima traps

    Detection uses:
    - Configuration similarity (Euclidean distance)
    - Objective stagnation (no improvement over window)
    - Oscillation patterns (A->B->A->B)
    """

    # Thresholds for thrashing detection
    similarity_threshold: float = 0.1  # Configs closer than this are "similar"
    stagnation_window: int = 10  # Number of evaluations to check for progress
    improvement_threshold: float = 0.01  # Minimum improvement to count as progress
    oscillation_count_threshold: int = 3  # Number of oscillations to trigger

    # History tracking
    config_history: List[List[float]] = field(default_factory=list)
    outcome_history: List[Dict[str, float]] = field(default_factory=list)

    def record(self, config: List[float], outcomes: Dict[str, float]) -> None:
        """Record a configuration and its outcomes."""
        self.config_history.append(list(config))
        self.outcome_history.append(dict(outcomes))

    def detect_thrashing(self) -> Tuple[bool, Optional[str]]:
        """
        Check if optimization is thrashing.

        Returns:
            Tuple of (is_thrashing, reason_if_thrashing)
        """
        if len(self.config_history) < self.stagnation_window:
            return False, None

        # Check for stagnation
        if self._check_stagnation():
            return True, "stagnation"

        # Check for oscillation
        if self._check_oscillation():
            return True, "oscillation"

        # Check for similarity clustering
        if self._check_similarity_clustering():
            return True, "similarity_clustering"

        return False, None

    def _check_stagnation(self) -> bool:
        """Check if objectives are stagnating."""
        if len(self.outcome_history) < self.stagnation_window:
            return False

        recent = self.outcome_history[-self.stagnation_window:]
        if not recent:
            return False

        # Check if any objective has improved
        first_outcomes = recent[0]
        last_outcomes = recent[-1]

        for key in first_outcomes:
            if key in last_outcomes:
                improvement = last_outcomes[key] - first_outcomes[key]
                if abs(improvement) > self.improvement_threshold:
                    return False

        return True  # No objective improved

    def _check_oscillation(self) -> bool:
        """Check for A->B->A->B oscillation patterns."""
        if len(self.config_history) < 4:
            return False

        recent = self.config_history[-6:]  # Last 6 configs
        oscillations = 0

        for i in range(len(recent) - 2):
            dist_to_next = self._config_distance(recent[i], recent[i + 1])
            dist_to_skip = self._config_distance(recent[i], recent[i + 2])

            # If config[i] is far from config[i+1] but close to config[i+2]
            if dist_to_next > self.similarity_threshold * 2 and dist_to_skip < self.similarity_threshold:
                oscillations += 1

        return oscillations >= self.oscillation_count_threshold

    def _check_similarity_clustering(self) -> bool:
        """Check if recent configs are too similar (stuck in local area)."""
        if len(self.config_history) < self.stagnation_window:
            return False

        recent = self.config_history[-self.stagnation_window:]
        centroid = [sum(c[i] for c in recent) / len(recent) for i in range(len(recent[0]))]

        # Check if all configs are close to centroid
        for config in recent:
            if self._config_distance(config, centroid) > self.similarity_threshold * 2:
                return False

        return True  # All clustered together

    def _config_distance(self, a: List[float], b: List[float]) -> float:
        """Euclidean distance between configs."""
        return sum((ai - bi) ** 2 for ai, bi in zip(a, b)) ** 0.5

    def handle_thrashing(
        self,
        current_population: List[List[float]],
        reason: str,
    ) -> List[List[float]]:
        """
        Apply recovery strategy based on thrashing type.

        Args:
            current_population: Current config population
            reason: Type of thrashing detected

        Returns:
            Diversified population
        """
        if reason == "stagnation":
            return self._diversify_mutation(current_population)
        elif reason == "oscillation":
            return self._break_oscillation(current_population)
        elif reason == "similarity_clustering":
            return self._expand_search(current_population)
        return current_population

    def _diversify_mutation(self, population: List[List[float]]) -> List[List[float]]:
        """Add random mutations to break stagnation."""
        import random
        diversified = []
        for config in population:
            mutated = [
                max(0.0, min(1.0, v + random.uniform(-0.2, 0.2)))
                for v in config
            ]
            diversified.append(mutated)
        return diversified

    def _break_oscillation(self, population: List[List[float]]) -> List[List[float]]:
        """Average oscillating configs to break A-B-A pattern."""
        if len(population) < 2:
            return population

        # Average pairs of configs
        averaged = []
        for i in range(0, len(population) - 1, 2):
            avg = [(a + b) / 2 for a, b in zip(population[i], population[i + 1])]
            averaged.append(avg)
        return averaged or population

    def _expand_search(self, population: List[List[float]]) -> List[List[float]]:
        """Expand search radius when clustered."""
        import random
        expanded = []
        for config in population:
            # Push away from cluster center with larger step
            expanded_config = [
                max(0.0, min(1.0, v + random.uniform(-0.4, 0.4)))
                for v in config
            ]
            expanded.append(expanded_config)
        return expanded

    def clear_history(self) -> None:
        """Clear tracking history (e.g., after recovery)."""
        self.config_history.clear()
        self.outcome_history.clear()


@dataclass
class Objective:
    """An optimization objective."""
    name: str
    direction: ObjectiveDirection = ObjectiveDirection.MAXIMIZE
    threshold: Optional[float] = None  # For threshold-based optimization
    weight: float = 1.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "direction": self.direction.value,
            "threshold": self.threshold,
            "weight": self.weight,
        }


@dataclass
class OptimizationOutcome:
    """Result of evaluating a configuration."""
    config_vector: List[float]
    outcomes: Dict[str, float]
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "config_vector": self.config_vector,
            "outcomes": self.outcomes,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OptimizationOutcome":
        return cls(
            config_vector=data["config_vector"],
            outcomes=data["outcomes"],
            metadata=data.get("metadata", {}),
            timestamp=data.get("timestamp", time.time()),
        )


@dataclass
class ParetoPoint:
    """A point on the Pareto frontier."""
    config_vector: List[float]
    outcomes: Dict[str, float]
    dominance_rank: int = 0
    crowding_distance: float = 0.0

    def to_config(self) -> FullConfig:
        """Convert to FullConfig."""
        return VectorCodec.decode(self.config_vector)


@dataclass
class OptimizationProject:
    """An optimization project within a model."""
    project_id: str
    model_id: str
    name: str
    objectives: List[Objective]
    created_at: float = field(default_factory=time.time)
    case_count: int = 0


class GlobalMOOClient:
    """
    Client for GlobalMOO multi-objective optimization API.

    Supports both real API calls and mock mode for testing.
    """

    DEFAULT_BASE_URI = "https://app.globalmoo.com/api"

    # Standard objectives for cognitive architecture
    COGNITIVE_OBJECTIVES = [
        Objective("task_accuracy", ObjectiveDirection.MAXIMIZE, threshold=0.9),
        Objective("token_efficiency", ObjectiveDirection.MAXIMIZE),
        Objective("edge_robustness", ObjectiveDirection.MAXIMIZE),
        Objective("epistemic_consistency", ObjectiveDirection.MAXIMIZE),
    ]

    # FR3.2: Self-modification objective (20% weight)
    # This objective measures how well the system can improve itself
    SELF_MODIFICATION_OBJECTIVE = Objective(
        name="self_modification_potential",
        direction=ObjectiveDirection.MAXIMIZE,
        threshold=0.5,
        weight=0.2,  # 20% of total objective weight
    )

    # Full objectives including self-modification (Hofstadter FR3.2)
    HOFSTADTER_OBJECTIVES = [
        Objective("task_accuracy", ObjectiveDirection.MAXIMIZE, threshold=0.9, weight=0.25),
        Objective("token_efficiency", ObjectiveDirection.MAXIMIZE, weight=0.20),
        Objective("edge_robustness", ObjectiveDirection.MAXIMIZE, weight=0.15),
        Objective("epistemic_consistency", ObjectiveDirection.MAXIMIZE, weight=0.20),
        Objective("self_modification_potential", ObjectiveDirection.MAXIMIZE, threshold=0.5, weight=0.20),
    ]

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_uri: Optional[str] = None,
        use_mock: bool = False,
    ):
        """
        Initialize GlobalMOO client.

        Args:
            api_key: API key (defaults to GLOBALMOO_API_KEY env var)
            base_uri: Base URI (defaults to GLOBALMOO_BASE_URI or standard)
            use_mock: Use mock mode for testing without API
        """
        self.api_key = api_key or os.environ.get("GLOBALMOO_API_KEY")
        self.base_uri = base_uri or os.environ.get(
            "GLOBALMOO_BASE_URI",
            self.DEFAULT_BASE_URI
        )
        self.use_mock = use_mock

        # HTTP client (lazy init)
        self._client: Optional[Any] = None

        # Current project/model
        self.model_id: Optional[str] = None
        self.project_id: Optional[str] = None

        # Mock storage
        self._mock_cases: List[OptimizationOutcome] = []
        self._mock_pareto: List[ParetoPoint] = []

        # FR3.3: Thrashing detection
        self.thrashing_detector = ThrashingDetector()

    def __enter__(self) -> "GlobalMOOClient":
        """Context manager entry - returns self."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit - closes client."""
        self.close()

    def close(self) -> None:
        """
        Close HTTP client and release resources.

        FIX: Added to prevent httpx.Client resource leak.
        """
        if self._client is not None:
            self._client.close()
            self._client = None

    @property
    def client(self) -> Any:
        """Lazy-init HTTP client."""
        if self._client is None:
            if not HTTPX_AVAILABLE:
                raise ImportError("httpx required for API calls. Install with: pip install httpx")
            self._client = httpx.Client(
                base_url=self.base_uri,
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=30.0,
            )
        return self._client

    @property
    def is_available(self) -> bool:
        """Check if client is properly configured."""
        if self.use_mock:
            return True
        return bool(self.api_key)

    def test_connection(self) -> bool:
        """
        Test API connectivity.

        Returns:
            True if connection successful
        """
        if self.use_mock:
            return True

        try:
            # Try to list models as a connectivity test
            response = self.client.get("/models")
            return response.status_code in [200, 401, 403]  # Even auth errors mean we connected
        except Exception as e:
            print(f"  Connection test exception: {e}")
            return False

    @retry_with_backoff(max_attempts=3, base_delay=1.0)
    def list_models(self) -> List[Dict[str, Any]]:
        """
        List all models in the account.

        Returns:
            List of model dictionaries with id, name, description, projects
        """
        if self.use_mock:
            return [{"id": self.model_id, "name": "mock-model", "projects": []}]

        response = self.client.get("/models")
        response.raise_for_status()
        return response.json()

    @retry_with_backoff(max_attempts=3, base_delay=1.0)
    def get_model(self, model_id: int) -> Dict[str, Any]:
        """
        Get model details including projects.

        Args:
            model_id: Model ID

        Returns:
            Model dictionary with projects
        """
        if self.use_mock:
            return {"id": model_id, "name": "mock-model", "projects": []}

        response = self.client.get(f"/models/{model_id}")
        response.raise_for_status()
        return response.json()

    def create_model(
        self,
        name: str,
        description: str = "",
        input_dimensions: int = 14,
    ) -> str:
        """
        Create optimization model.

        Args:
            name: Model name
            description: Model description
            input_dimensions: Number of input dimensions (config vector size)

        Returns:
            Model ID
        """
        if self.use_mock:
            self.model_id = f"mock-model-{hashlib.md5(name.encode()).hexdigest()[:8]}"
            return self.model_id

        response = self.client.post("/models", json={
            "name": name,
            "description": description,
            "input_dimensions": input_dimensions,
        })
        response.raise_for_status()
        data = response.json()
        self.model_id = data["id"]
        return self.model_id

    def create_project(
        self,
        model_id: str,
        name: str,
        objectives: Optional[List[Objective]] = None,
    ) -> str:
        """
        Create project with objectives (mock mode only - real API uses create_project_with_inputs).

        Args:
            model_id: Parent model ID
            name: Project name
            objectives: List of objectives (defaults to COGNITIVE_OBJECTIVES)

        Returns:
            Project ID
        """
        objectives = objectives or self.COGNITIVE_OBJECTIVES

        if self.use_mock:
            self.project_id = f"mock-project-{hashlib.md5(name.encode()).hexdigest()[:8]}"
            self.model_id = model_id
            return self.project_id

        # Real API requires input specification - use create_project_with_inputs instead
        raise NotImplementedError(
            "Real API requires input dimensions. Use create_project_with_inputs() instead."
        )

    def create_project_with_inputs(
        self,
        model_id: int,
        name: str,
        input_count: int,
        minimums: List[float],
        maximums: List[float],
        input_types: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Create project with input specifications (REAL API format).

        Args:
            model_id: Parent model ID
            name: Project name (min 4 chars)
            input_count: Number of input dimensions
            minimums: Minimum value for each input
            maximums: Maximum value for each input
            input_types: Type for each input ('float', 'boolean', 'integer', 'category')

        Returns:
            Project dictionary with id, inputCases, etc.
        """
        if input_types is None:
            input_types = ["float"] * input_count

        if self.use_mock:
            self.project_id = f"mock-project-{hashlib.md5(name.encode()).hexdigest()[:8]}"
            self.model_id = str(model_id)
            return {
                "id": self.project_id,
                "name": name,
                "inputCount": input_count,
                "inputCases": [],
            }

        response = self.client.post(f"/models/{model_id}/projects", json={
            "name": name,
            "inputCount": input_count,
            "minimums": minimums,
            "maximums": maximums,
            "inputTypes": input_types,
        })
        response.raise_for_status()
        data = response.json()
        self.project_id = data["id"]
        self.model_id = str(model_id)
        return data

    def create_cognitive_5dim_project(
        self,
        model_id: int,
        name: str = "cognitive_5dim",
    ) -> Dict[str, Any]:
        """
        Create a 5-dimensional cognitive architecture project.

        Reduced dimensions for API subscription limits:
        - dim 0: evidential_frame (0-1, core evidence frame)
        - dim 1: aspectual_frame (0-1, temporal reasoning)
        - dim 2: verix_strictness (0-2, verification level)
        - dim 3: compression_level (0-2, token efficiency)
        - dim 4: require_ground (0-1, edge robustness)

        Returns:
            Project dictionary
        """
        return self.create_project_with_inputs(
            model_id=model_id,
            name=name,
            input_count=5,
            minimums=[0, 0, 0, 0, 0],
            maximums=[1, 1, 2, 2, 1],
            input_types=["float", "float", "float", "float", "float"],
        )

    def load_cases(
        self,
        project_id: str,
        cases: List[OptimizationOutcome],
    ) -> int:
        """
        Load initial seed cases for optimization.

        Args:
            project_id: Project ID
            cases: List of evaluation outcomes

        Returns:
            Number of cases loaded
        """
        if self.use_mock:
            self._mock_cases.extend(cases)
            self._update_mock_pareto()
            return len(cases)

        response = self.client.post(f"/projects/{project_id}/cases", json={
            "cases": [case.to_dict() for case in cases],
        })
        response.raise_for_status()
        return len(cases)

    def suggest_inverse(
        self,
        project_id: str,
        target_outcomes: Dict[str, float],
        num_suggestions: int = 5,
        apply_tier_bounds: bool = True,
    ) -> List[List[float]]:
        """
        Inverse query: Given target outcomes, suggest config vectors.

        This is the KEY method for optimization - it asks GlobalMOO
        "what configuration would achieve these outcomes?"

        FR3.1: Two-tier bounds are automatically applied to protect
        IMMUTABLE constraints (evidential >= 0.3, require_ground >= 0.5).

        Args:
            project_id: Project ID
            target_outcomes: Target values for each objective
            num_suggestions: Number of suggestions to return
            apply_tier_bounds: Apply two-tier constraints (default True)

        Returns:
            List of suggested config vectors (constrained if apply_tier_bounds)
        """
        if self.use_mock:
            suggestions = self._mock_suggest_inverse(target_outcomes, num_suggestions)
        else:
            response = self.client.post(f"/projects/{project_id}/suggest", json={
                "target_outcomes": target_outcomes,
                "num_suggestions": num_suggestions,
            })
            response.raise_for_status()
            suggestions = response.json()["suggestions"]

        # FR3.1: Apply two-tier bounds to protect IMMUTABLE constraints
        if apply_tier_bounds:
            suggestions = [
                DEFAULT_TIER_BOUNDS.constrain_suggestion(s)
                for s in suggestions
            ]

        return suggestions

    def report_outcome(
        self,
        project_id: str,
        outcome: OptimizationOutcome,
    ) -> None:
        """
        Report evaluation result back to GlobalMOO.

        This closes the optimization loop - after evaluating a suggested
        config, we report the actual outcomes to improve future suggestions.

        FR3.3: Also tracks outcomes for thrashing detection.

        Args:
            project_id: Project ID
            outcome: Evaluation result
        """
        # FR3.3: Record for thrashing detection
        self.thrashing_detector.record(outcome.config_vector, outcome.outcomes)

        if self.use_mock:
            self._mock_cases.append(outcome)
            self._update_mock_pareto()
            return

        response = self.client.post(f"/projects/{project_id}/outcomes", json={
            "outcome": outcome.to_dict(),
        })
        response.raise_for_status()

    def check_and_handle_thrashing(
        self,
        population: List[List[float]],
    ) -> Tuple[List[List[float]], bool]:
        """
        Check for optimization thrashing and apply recovery if needed (FR3.3).

        Args:
            population: Current config population

        Returns:
            Tuple of (possibly_modified_population, was_thrashing_detected)
        """
        is_thrashing, reason = self.thrashing_detector.detect_thrashing()

        if is_thrashing:
            logger.warning(f"Thrashing detected: {reason}. Applying recovery.")
            recovered_population = self.thrashing_detector.handle_thrashing(population, reason)

            # Apply tier bounds to recovered population
            recovered_population = [
                DEFAULT_TIER_BOUNDS.constrain_suggestion(config)
                for config in recovered_population
            ]

            # Clear history after recovery
            self.thrashing_detector.clear_history()

            return recovered_population, True

        return population, False

    def calculate_self_modification_potential(
        self,
        config_vector: List[float],
    ) -> float:
        """
        Calculate self-modification potential score (FR3.2).

        This measures how well a configuration enables the system to
        improve itself. Factors include:
        - Flexibility (distance from immutable bounds)
        - Diversity (coverage of parameter space)
        - Adaptability (how much the config has changed over time)

        Args:
            config_vector: Configuration to evaluate

        Returns:
            Score from 0.0 to 1.0
        """
        score = 0.0

        # Flexibility: How much room for adjustment?
        # Higher when parameters are mid-range (can go either way)
        flexibility_scores = []
        for v in config_vector:
            # Peak at 0.5, lower at edges
            flexibility = 1.0 - 2.0 * abs(v - 0.5)
            flexibility_scores.append(max(0.0, flexibility))
        avg_flexibility = sum(flexibility_scores) / len(flexibility_scores) if flexibility_scores else 0.0
        score += avg_flexibility * 0.4  # 40% weight

        # Diversity: Does this explore new parameter combinations?
        if self.thrashing_detector.config_history:
            recent_configs = self.thrashing_detector.config_history[-10:]
            avg_distance = sum(
                self.thrashing_detector._config_distance(config_vector, c)
                for c in recent_configs
            ) / len(recent_configs)
            # Normalize to 0-1 (assuming max distance of sqrt(n) where n = dims)
            max_distance = len(config_vector) ** 0.5
            diversity = min(1.0, avg_distance / max_distance)
            score += diversity * 0.3  # 30% weight
        else:
            score += 0.3  # Default if no history

        # Adaptability: Does this config enable learning?
        # Higher evidential and verix settings enable better learning
        if len(config_vector) > 9:
            evidential = config_vector[0]
            require_ground = config_vector[9] if len(config_vector) > 9 else 0.5
            adaptability = (evidential + require_ground) / 2
            score += adaptability * 0.3  # 30% weight
        else:
            score += 0.15  # Default

        return min(1.0, max(0.0, score))

    def get_pareto_frontier(
        self,
        project_id: str,
    ) -> List[ParetoPoint]:
        """
        Get all Pareto-optimal configurations.

        Args:
            project_id: Project ID

        Returns:
            List of Pareto-optimal points
        """
        if self.use_mock:
            return self._mock_pareto

        response = self.client.get(f"/projects/{project_id}/pareto")
        response.raise_for_status()
        data = response.json()

        return [
            ParetoPoint(
                config_vector=p["config_vector"],
                outcomes=p["outcomes"],
                dominance_rank=p.get("dominance_rank", 0),
                crowding_distance=p.get("crowding_distance", 0.0),
            )
            for p in data["pareto_points"]
        ]

    def get_impact_factors(
        self,
        project_id: str,
    ) -> Dict[str, Dict[int, float]]:
        """
        Get impact factors: how much each input affects each output.

        Returns:
            Dict mapping outcome_name -> {input_index: impact_score}
        """
        if self.use_mock:
            return self._mock_impact_factors()

        response = self.client.get(f"/projects/{project_id}/impact")
        response.raise_for_status()
        return response.json()["impact_factors"]

    # Mock implementations for testing

    def _mock_suggest_inverse(
        self,
        target_outcomes: Dict[str, float],
        num_suggestions: int,
    ) -> List[List[float]]:
        """Mock inverse suggestion based on known cases."""
        suggestions = []

        # Find cases closest to target
        if self._mock_cases:
            ranked = sorted(
                self._mock_cases,
                key=lambda c: self._mock_distance(c.outcomes, target_outcomes),
            )

            for case in ranked[:num_suggestions]:
                # Perturb slightly for variation
                suggestion = [
                    v + (0.1 * (i % 2 - 0.5))
                    for i, v in enumerate(case.config_vector)
                ]
                # Clamp to valid range
                suggestion = [max(0.0, min(1.0, v)) for v in suggestion]
                suggestions.append(suggestion)

        # Fill remaining with random variations
        while len(suggestions) < num_suggestions:
            base = VectorCodec.encode(FullConfig())
            variation = [
                v + (0.2 * ((i * 7) % 3 - 1) / 3)
                for i, v in enumerate(base)
            ]
            variation = [max(0.0, min(1.0, v)) for v in variation]
            suggestions.append(variation)

        return suggestions

    def _mock_distance(
        self,
        outcomes: Dict[str, float],
        target: Dict[str, float],
    ) -> float:
        """Calculate distance between outcomes and target."""
        distance = 0.0
        for key, target_val in target.items():
            actual_val = outcomes.get(key, 0.0)
            distance += (target_val - actual_val) ** 2
        return distance ** 0.5

    def _update_mock_pareto(self) -> None:
        """Update mock Pareto frontier."""
        if not self._mock_cases:
            return

        # Simple non-dominated sorting
        pareto = []
        for case in self._mock_cases:
            is_dominated = False
            for other in self._mock_cases:
                if self._dominates(other.outcomes, case.outcomes):
                    is_dominated = True
                    break
            if not is_dominated:
                pareto.append(ParetoPoint(
                    config_vector=case.config_vector,
                    outcomes=case.outcomes,
                    dominance_rank=0,
                ))

        self._mock_pareto = pareto

    def _dominates(
        self,
        outcomes_a: Dict[str, float],
        outcomes_b: Dict[str, float],
    ) -> bool:
        """Check if A dominates B (all objectives >= and at least one >)."""
        dominated_in_any = False
        better_in_all = True

        for key in outcomes_a:
            val_a = outcomes_a.get(key, 0.0)
            val_b = outcomes_b.get(key, 0.0)

            if val_a < val_b:
                better_in_all = False
            if val_a > val_b:
                dominated_in_any = True

        return better_in_all and dominated_in_any

    def _mock_impact_factors(self) -> Dict[str, Dict[int, float]]:
        """Generate mock impact factors."""
        return {
            "task_accuracy": {
                0: 0.3,  # evidential frame
                1: 0.2,  # aspectual frame
                7: 0.25,  # verix_strictness
            },
            "token_efficiency": {
                8: 0.4,  # compression_level
                7: 0.2,  # verix_strictness
            },
            "edge_robustness": {
                0: 0.2,  # evidential
                9: 0.3,  # require_ground
            },
            "epistemic_consistency": {
                7: 0.4,  # verix_strictness
                9: 0.25,  # require_ground
                10: 0.2,  # require_confidence
            },
        }


# Factory functions

def create_client(use_mock: bool = False) -> GlobalMOOClient:
    """
    Create GlobalMOO client.

    Args:
        use_mock: Use mock mode for testing

    Returns:
        Configured client
    """
    return GlobalMOOClient(use_mock=use_mock)


def create_cognitive_project(
    client: GlobalMOOClient,
    name: str = "cognitive-architecture-optimization",
) -> OptimizationProject:
    """
    Create a project with standard cognitive architecture objectives.

    Args:
        client: GlobalMOO client
        name: Project name

    Returns:
        Created project
    """
    model_id = client.create_model(
        name=f"{name}-model",
        description="VERILINGUA x VERIX x DSPy x GlobalMOO optimization",
        input_dimensions=VectorCodec.VECTOR_SIZE,
    )

    project_id = client.create_project(
        model_id=model_id,
        name=name,
        objectives=GlobalMOOClient.COGNITIVE_OBJECTIVES,
    )

    return OptimizationProject(
        project_id=project_id,
        model_id=model_id,
        name=name,
        objectives=GlobalMOOClient.COGNITIVE_OBJECTIVES,
    )
