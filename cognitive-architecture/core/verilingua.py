"""
VERILINGUA cognitive frames from natural language distinctions.

Each frame adds specific cognitive constraints derived from how
different natural languages force speakers to make distinctions:

1. EvidentialFrame (Turkish): Mark evidence type for claims
2. AspectualFrame (Russian): Mark completion status of actions
3. MorphologicalFrame (Arabic): Decompose concepts into roots
4. CompositionalFrame (German): Build compounds from primitives
5. HonorificFrame (Japanese): Calibrate formality to audience
6. ClassifierFrame (Chinese): Use measure words for objects
7. SpatialFrame (Guugu Yimithirr): Use absolute positioning

Protocol:
- Each frame defines activation_instruction() and compliance_markers()
- Frames are composable (multiple can be active simultaneously)
- Frame selection affects prompt structure and response validation
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Protocol, runtime_checkable
from dataclasses import dataclass
import re
import threading

from .config import FrameworkConfig


@runtime_checkable
class CognitiveFrame(Protocol):
    """
    Protocol for cognitive frames.

    All cognitive frames must implement these methods to be usable
    in the prompt building system.
    """

    name: str
    linguistic_source: str
    cognitive_force: str

    def activation_instruction(self) -> str:
        """Return prompt text to activate this frame."""
        ...

    def compliance_markers(self) -> List[str]:
        """Return patterns that indicate frame is active in response."""
        ...

    def score_response(self, response: str) -> float:
        """Score how well response adheres to frame (0.0 - 1.0)."""
        ...


@dataclass
class EvidentialFrame:
    """
    Turkish -mis/-di: Forces distinction between witnessed/reported/inferred.

    Turkish grammar requires speakers to mark whether they personally
    witnessed something (-di) or learned it secondhand (-mis). This frame
    forces AI responses to explicitly mark evidence type for all claims.
    """

    name: str = "evidential"
    linguistic_source: str = "Turkish"
    cognitive_force: str = "How do you know?"

    MARKERS = ["[witnessed]", "[reported]", "[inferred]", "[assumed]"]

    def activation_instruction(self) -> str:
        return """
## EVIDENTIAL FRAME (Turkish -mis/-di)

For every factual claim, explicitly mark the evidence type:
- [witnessed]: You directly observed/verified this (e.g., read the code, ran the test)
- [reported]: You learned this from a source (cite it: documentation, user input, etc.)
- [inferred]: You deduced this from other facts (show the reasoning chain)
- [assumed]: This is an assumption (state confidence level)

Example:
"[witnessed] The function returns None when input is empty - I traced the code path."
"[reported:user_message] The bug occurs on login - as described in the user's request."
"[inferred] The cache is stale [because] the timestamp is 3 hours old and TTL is 1 hour."
"[assumed:0.7] The API follows REST conventions - this is a common pattern."

DO NOT make claims without evidence markers. Every factual statement needs a source.
"""

    def compliance_markers(self) -> List[str]:
        return self.MARKERS

    def score_response(self, response: str) -> float:
        """Score based on marker usage density."""
        marker_count = sum(1 for m in self.MARKERS if m.lower() in response.lower())

        # Estimate number of claims (sentences that could be factual)
        sentences = len(re.findall(r'[.!?]+', response))
        claim_sentences = max(1, sentences * 0.6)  # Assume 60% are factual claims

        # Score is ratio of marked claims
        coverage = min(1.0, marker_count / claim_sentences)
        return coverage

    def meta_instruction(self) -> str:
        """
        Return instruction for discussing THIS frame (mention mode).

        Hofstadter FR1.1 (SYNTH-FOUND-002): Self-reference is not paradox.
        Enables frames to discuss themselves without logical issues.
        """
        return """
## META-EVIDENTIAL MODE (Self-Reference)

When discussing the evidential frame itself:
- [mentioning:evidential] The evidential frame forces evidence marking
- [using:evidential] [witnessed] The function returns null

The distinction:
- [using:evidential] = applying this frame to content
- [mentioning:evidential] = discussing this frame as an object

This frame derives from Turkish -mis/-di evidential markers.
"""


@dataclass
class AspectualFrame:
    """
    Russian perfective/imperfective: Forces completion status marking.

    Russian verbs require speakers to indicate whether an action is
    complete (perfective) or ongoing (imperfective). This frame forces
    AI responses to mark the completion status of all actions and processes.
    """

    name: str = "aspectual"
    linguistic_source: str = "Russian"
    cognitive_force: str = "Complete or ongoing?"

    MARKERS = ["[complete]", "[ongoing]", "[habitual]", "[attempted]"]

    def activation_instruction(self) -> str:
        return """
## ASPECTUAL FRAME (Russian Perfective/Imperfective)

For every action or process, mark its completion aspect:
- [complete]: Action is finished with definite endpoint (done, succeeded, failed)
- [ongoing]: Action is in progress, no endpoint yet (running, processing, waiting)
- [habitual]: Action repeats regularly (always does, typically, usually)
- [attempted]: Action was tried but outcome uncertain (tried to, attempted)

Example:
"[complete] The migration script executed successfully - all tables created."
"[ongoing] The test suite is running - 45/100 tests completed so far."
"[habitual] The cron job runs every hour to sync the data."
"[attempted] I tried to connect to the API but the response is still pending."

DO NOT describe actions without aspect markers. Every verb needs completion status.
"""

    def compliance_markers(self) -> List[str]:
        return self.MARKERS

    def score_response(self, response: str) -> float:
        """Score based on marker usage for action descriptions."""
        marker_count = sum(1 for m in self.MARKERS if m.lower() in response.lower())

        # Estimate action descriptions (verb phrases)
        action_patterns = r'\b(is|are|was|were|has|have|had|will|would|should|could|can|may|might)\b'
        action_count = len(re.findall(action_patterns, response, re.IGNORECASE))
        expected_markers = max(1, action_count * 0.3)  # 30% of verb phrases are trackable

        coverage = min(1.0, marker_count / expected_markers)
        return coverage

    def meta_instruction(self) -> str:
        """
        Return instruction for discussing THIS frame (mention mode).

        Hofstadter FR1.1 (SYNTH-FOUND-002): Self-reference is not paradox.
        """
        return """
## META-ASPECTUAL MODE (Self-Reference)

When discussing the aspectual frame itself:
- [mentioning:aspectual] The aspectual frame marks completion status
- [using:aspectual] [ongoing] The analysis is in progress

The distinction:
- [using:aspectual] = applying this frame to content
- [mentioning:aspectual] = discussing this frame as an object

This frame derives from Russian perfective/imperfective verb aspects.
"""


@dataclass
class MorphologicalFrame:
    """
    Arabic trilateral roots: Forces semantic decomposition of concepts.

    Arabic derives words from 3-consonant roots (k-t-b = write/book/author).
    This frame forces AI to break down complex concepts into their
    fundamental semantic components.
    """

    name: str = "morphological"
    linguistic_source: str = "Arabic"
    cognitive_force: str = "What are the root components?"

    MARKERS = ["[root:", "[derived:", "[composed:"]

    def activation_instruction(self) -> str:
        return """
## MORPHOLOGICAL FRAME (Arabic Trilateral Roots)

For complex concepts, decompose them into fundamental components:
- [root:X] identifies the core semantic kernel
- [derived:X->Y] shows how one concept derives from another
- [composed:A+B=C] shows how components combine

Example:
"[root:authenticate] The authentication system [derived:authenticate->authorization]
controls [derived:authorize->access] what resources users can access."

"[composed:micro+service=microservice] The microservice architecture uses
[root:service] small independent services that [derived:service->serve] requests."

When introducing technical terms, show their compositional structure.
"""

    def compliance_markers(self) -> List[str]:
        return self.MARKERS

    def score_response(self, response: str) -> float:
        """Score based on decomposition marker usage."""
        marker_count = sum(1 for m in self.MARKERS if m.lower() in response.lower())

        # Estimate complex terms (multi-syllable technical words)
        technical_pattern = r'\b[A-Z][a-z]+[A-Z][a-z]+\b|\b\w{8,}\b'
        technical_count = len(re.findall(technical_pattern, response))
        expected_markers = max(1, technical_count * 0.2)  # 20% should be decomposed

        coverage = min(1.0, marker_count / expected_markers)
        return coverage

    def meta_instruction(self) -> str:
        """
        Return instruction for discussing THIS frame (mention mode).

        Hofstadter FR1.1 (SYNTH-FOUND-002): Self-reference is not paradox.
        """
        return """
## META-MORPHOLOGICAL MODE (Self-Reference)

When discussing the morphological frame itself:
- [mentioning:morphological] The morphological frame decomposes concepts
- [using:morphological] [root:compute] -> [derived:compute->computation]

The distinction:
- [using:morphological] = applying this frame to content
- [mentioning:morphological] = discussing this frame as an object

This frame derives from Arabic trilateral root system.
"""


@dataclass
class CompositionalFrame:
    """
    German compounding: Forces building definitions from primitives.

    German creates compound words (Schadenfreude = damage+joy). This frame
    forces AI to build up complex concepts from well-defined primitives.
    """

    name: str = "compositional"
    linguistic_source: str = "German"
    cognitive_force: str = "How does this build from primitives?"

    MARKERS = ["[primitive:", "[compound:", "[builds:"]

    def activation_instruction(self) -> str:
        return """
## COMPOSITIONAL FRAME (German Compounding)

Build complex concepts from defined primitives:
- [primitive:X] identifies a basic building block concept
- [compound:A+B] shows how primitives combine
- [builds:X->Y] shows compositional hierarchy

Example:
"[primitive:request] A request is a message asking for something.
[primitive:handler] A handler is code that processes input.
[compound:request+handler] A request handler processes incoming requests."

"[builds:function->method->class] The User class contains methods,
which are functions bound to the class instance."

Start with primitives, then show how they compose into the complex concept.
"""

    def compliance_markers(self) -> List[str]:
        return self.MARKERS

    def score_response(self, response: str) -> float:
        """Score based on compositional marker usage."""
        marker_count = sum(1 for m in self.MARKERS if m.lower() in response.lower())

        # Estimate definable concepts
        definition_triggers = r'\b(is a|means|refers to|defined as)\b'
        definition_count = len(re.findall(definition_triggers, response, re.IGNORECASE))
        expected_markers = max(1, definition_count * 0.5)

        coverage = min(1.0, marker_count / expected_markers)
        return coverage

    def meta_instruction(self) -> str:
        """
        Return instruction for discussing THIS frame (mention mode).

        Hofstadter FR1.1 (SYNTH-FOUND-002): Self-reference is not paradox.
        """
        return """
## META-COMPOSITIONAL MODE (Self-Reference)

When discussing the compositional frame itself:
- [mentioning:compositional] The compositional frame builds from primitives
- [using:compositional] [primitive:frame] + [primitive:meta] = [compound:meta-frame]

The distinction:
- [using:compositional] = applying this frame to content
- [mentioning:compositional] = discussing this frame as an object

This frame derives from German compound word formation.
"""


@dataclass
class HonorificFrame:
    """
    Japanese keigo: Forces audience-appropriate formality calibration.

    Japanese has elaborate honorific systems (sonkeigo, kenjougo, teineigo).
    This frame forces AI to calibrate response formality to the audience.
    """

    name: str = "honorific"
    linguistic_source: str = "Japanese"
    cognitive_force: str = "Who is the audience?"

    MARKERS = ["[audience:", "[formality:", "[register:"]

    def activation_instruction(self) -> str:
        return """
## HONORIFIC FRAME (Japanese Keigo)

Calibrate formality and tone to the audience:
- [audience:X] explicitly identifies who you're addressing
- [formality:high/medium/low] sets the register
- [register:technical/casual/formal] adjusts terminology

Example:
"[audience:senior_developer] [formality:medium] [register:technical]
The race condition occurs because the mutex isn't acquired before the write."

"[audience:end_user] [formality:high] [register:casual]
Your account is now set up! You can start using the app right away."

"[audience:stakeholder] [formality:high] [register:formal]
The implementation is progressing according to schedule. We anticipate
completion by the end of the sprint."

Always consider: Who will read this? What do they need to know?
"""

    def compliance_markers(self) -> List[str]:
        return self.MARKERS

    def score_response(self, response: str) -> float:
        """Score based on audience awareness markers."""
        marker_count = sum(1 for m in self.MARKERS if m.lower() in response.lower())

        # Audience should be set at least once
        has_audience = "[audience:" in response.lower()
        base_score = 0.5 if has_audience else 0.0

        # Additional markers add to score
        additional = min(0.5, marker_count * 0.1)
        return base_score + additional

    def meta_instruction(self) -> str:
        """
        Return instruction for discussing THIS frame (mention mode).

        Hofstadter FR1.1 (SYNTH-FOUND-002): Self-reference is not paradox.
        """
        return """
## META-HONORIFIC MODE (Self-Reference)

When discussing the honorific frame itself:
- [mentioning:honorific] The honorific frame calibrates formality
- [using:honorific] [audience:linguist] [formality:medium] [register:technical]

The distinction:
- [using:honorific] = applying this frame to content
- [mentioning:honorific] = discussing this frame as an object

This frame derives from Japanese keigo honorific system.
"""


@dataclass
class ClassifierFrame:
    """
    Chinese measure words: Forces appropriate categorization of objects.

    Chinese requires measure words between numbers and nouns. This frame
    forces AI to use appropriate classifiers when comparing or counting.
    """

    name: str = "classifier"
    linguistic_source: str = "Chinese"
    cognitive_force: str = "What category/type is this?"

    MARKERS = ["[type:", "[category:", "[measure:"]

    def activation_instruction(self) -> str:
        return """
## CLASSIFIER FRAME (Chinese Measure Words)

Use explicit type classifiers when comparing or counting:
- [type:X] classifies objects into types
- [category:X] groups related items
- [measure:unit] specifies measurement units

Example:
"[type:function] We have 5 functions in this module.
[type:class] There are 2 classes: User and Admin.
[category:authentication] Both classes belong to the auth category."

"[measure:lines] The file is 200 lines long.
[measure:ms] Response time is 45ms.
[measure:requests/sec] Throughput is 1000 requests per second."

Never say "some things" or "a few items" - always classify and count precisely.
"""

    def compliance_markers(self) -> List[str]:
        return self.MARKERS

    def score_response(self, response: str) -> float:
        """Score based on classifier usage."""
        marker_count = sum(1 for m in self.MARKERS if m.lower() in response.lower())

        # Estimate countable references
        number_pattern = r'\b\d+\b|\b(some|few|many|several|multiple)\b'
        number_count = len(re.findall(number_pattern, response, re.IGNORECASE))
        expected_markers = max(1, number_count * 0.3)

        coverage = min(1.0, marker_count / expected_markers)
        return coverage

    def meta_instruction(self) -> str:
        """
        Return instruction for discussing THIS frame (mention mode).

        Hofstadter FR1.1 (SYNTH-FOUND-002): Self-reference is not paradox.
        """
        return """
## META-CLASSIFIER MODE (Self-Reference)

When discussing the classifier frame itself:
- [mentioning:classifier] The classifier frame categorizes objects
- [using:classifier] [type:frame] There are 7 frames [measure:count]

The distinction:
- [using:classifier] = applying this frame to content
- [mentioning:classifier] = discussing this frame as an object

This frame derives from Chinese measure word system.
"""


@dataclass
class SpatialFrame:
    """
    Guugu Yimithirr absolute positioning: Forces absolute reference frames.

    Guugu Yimithirr uses absolute directions (north/south) instead of
    relative (left/right). This frame forces AI to use absolute,
    unambiguous positioning in code and architecture descriptions.
    """

    name: str = "spatial"
    linguistic_source: str = "Guugu Yimithirr"
    cognitive_force: str = "What is the absolute position/path?"

    MARKERS = ["[path:", "[location:", "[direction:"]

    def activation_instruction(self) -> str:
        return """
## SPATIAL FRAME (Guugu Yimithirr Absolute Positioning)

Use absolute, unambiguous positioning:
- [path:X] gives full path from root
- [location:file:line] pinpoints exact location
- [direction:upstream/downstream] clarifies data flow

Example:
"[path:/src/auth/middleware.js] The auth middleware is located at this path.
[location:middleware.js:45] The validation happens on line 45."

"[direction:upstream] The API gateway is upstream from the service.
[direction:downstream] The database is downstream from the cache."

Never use relative references like "above" or "nearby" without absolute anchors.
Always provide full paths, exact line numbers, or clear directional flow.
"""

    def compliance_markers(self) -> List[str]:
        return self.MARKERS

    def score_response(self, response: str) -> float:
        """Score based on absolute positioning markers."""
        marker_count = sum(1 for m in self.MARKERS if m.lower() in response.lower())

        # Estimate location references
        location_pattern = r'\b(file|function|class|module|line|path)\b'
        location_count = len(re.findall(location_pattern, response, re.IGNORECASE))
        expected_markers = max(1, location_count * 0.3)

        coverage = min(1.0, marker_count / expected_markers)
        return coverage

    def meta_instruction(self) -> str:
        """
        Return instruction for discussing THIS frame (mention mode).

        Hofstadter FR1.1 (SYNTH-FOUND-002): Self-reference is not paradox.
        """
        return """
## META-SPATIAL MODE (Self-Reference)

When discussing the spatial frame itself:
- [mentioning:spatial] The spatial frame uses absolute positioning
- [using:spatial] [path:/core/verilingua.py] [location:verilingua.py:500]

The distinction:
- [using:spatial] = applying this frame to content
- [mentioning:spatial] = discussing this frame as an object

This frame derives from Guugu Yimithirr absolute directional system.
"""


class FrameRegistry:
    """
    Registry of all cognitive frames.

    Provides centralized access to frame instances and utilities
    for getting active frames based on configuration.
    """

    _frames: Dict[str, CognitiveFrame] = None
    _lock: threading.Lock = threading.Lock()
    _initialized: bool = False

    # FR1.3: Keyword triggers for fast frame detection (first 500 chars)
    # Each frame maps to keywords that strongly suggest its activation
    KEYWORD_TRIGGERS: Dict[str, List[str]] = {
        "evidential": [
            "evidence", "witnessed", "reported", "inferred", "assumed",
            "source", "citation", "verified", "confirmed", "prove",
            "how do you know", "what's your evidence", "based on",
        ],
        "aspectual": [
            "complete", "ongoing", "progress", "finished", "started",
            "still running", "done", "in progress", "completed", "pending",
            "status", "state", "phase", "stage",
        ],
        "morphological": [
            "root", "derived", "component", "decompose", "break down",
            "etymology", "structure", "composed of", "made up of",
        ],
        "compositional": [
            "primitive", "compound", "builds", "define", "definition",
            "what is", "means", "refers to", "consists of", "made from",
        ],
        "honorific": [
            "audience", "formality", "formal", "casual", "technical",
            "stakeholder", "manager", "developer", "user", "client",
            "tone", "register", "who is reading",
        ],
        "classifier": [
            "type", "category", "measure", "count", "how many",
            "number of", "classification", "kind of", "sort of",
            "units", "metrics",
        ],
        "spatial": [
            "path", "location", "directory", "file", "line",
            "upstream", "downstream", "where", "position", "navigate",
            "architecture", "flow", "route",
        ],
    }

    @classmethod
    def _ensure_initialized(cls) -> None:
        """Initialize registry with all frames if not already done (thread-safe)."""
        # Double-checked locking pattern for thread safety
        if cls._initialized:
            return

        with cls._lock:
            # Check again inside lock to prevent race conditions
            if cls._initialized:
                return

            cls._frames = {
                "evidential": EvidentialFrame(),
                "aspectual": AspectualFrame(),
                "morphological": MorphologicalFrame(),
                "compositional": CompositionalFrame(),
                "honorific": HonorificFrame(),
                "classifier": ClassifierFrame(),
                "spatial": SpatialFrame(),
            }
            cls._initialized = True

    @classmethod
    def register(cls, frame: CognitiveFrame) -> None:
        """
        Register a cognitive frame.

        Args:
            frame: Frame instance to register
        """
        cls._ensure_initialized()
        cls._frames[frame.name] = frame

    @classmethod
    def get(cls, name: str) -> CognitiveFrame:
        """
        Get a frame by name.

        Args:
            name: Frame name (e.g., "evidential")

        Returns:
            CognitiveFrame instance

        Raises:
            KeyError: If frame not found
        """
        cls._ensure_initialized()
        return cls._frames[name]

    @classmethod
    def get_all(cls) -> Dict[str, CognitiveFrame]:
        """Get all registered frames."""
        cls._ensure_initialized()
        return dict(cls._frames)

    @classmethod
    def get_active(cls, config: FrameworkConfig) -> List[CognitiveFrame]:
        """
        Get all frames that are enabled in config.

        Args:
            config: FrameworkConfig specifying which frames are active

        Returns:
            List of active CognitiveFrame instances
        """
        cls._ensure_initialized()
        active = []

        if config.evidential:
            active.append(cls._frames["evidential"])
        if config.aspectual:
            active.append(cls._frames["aspectual"])
        if config.morphological:
            active.append(cls._frames["morphological"])
        if config.compositional:
            active.append(cls._frames["compositional"])
        if config.honorific:
            active.append(cls._frames["honorific"])
        if config.classifier:
            active.append(cls._frames["classifier"])
        if config.spatial:
            active.append(cls._frames["spatial"])

        return active

    @classmethod
    def list_names(cls) -> List[str]:
        """Get list of all registered frame names."""
        cls._ensure_initialized()
        return list(cls._frames.keys())

    @classmethod
    def get_active_fast(
        cls,
        prompt: str,
        config: FrameworkConfig,
        max_chars: int = 500,
    ) -> List[CognitiveFrame]:
        """
        Fast frame selection using keyword triggers (FR1.3: Thrashing prevention).

        Instead of O(n) evaluation of all frames against the full prompt,
        this method uses keyword triggers on the first `max_chars` characters
        for O(1) amortized lookup.

        Fallback behavior:
        - If no triggers match, returns [evidential] (safest default)
        - Always respects config-disabled frames

        Args:
            prompt: The input prompt to analyze
            config: FrameworkConfig specifying which frames are enabled
            max_chars: Characters to scan for triggers (default 500)

        Returns:
            List of activated CognitiveFrame instances
        """
        cls._ensure_initialized()

        # Scan only first N chars for efficiency
        scan_text = prompt[:max_chars].lower()

        # Find matching frames by keyword triggers
        matched_frames: List[str] = []

        for frame_name, triggers in cls.KEYWORD_TRIGGERS.items():
            for trigger in triggers:
                if trigger in scan_text:
                    matched_frames.append(frame_name)
                    break  # One match is enough per frame

        # Fallback to evidential if no matches (Hofstadter base case)
        if not matched_frames:
            matched_frames = ["evidential"]

        # Filter by config-enabled frames
        active = []
        for frame_name in matched_frames:
            # Check if frame is enabled in config
            if hasattr(config, frame_name) and getattr(config, frame_name):
                if frame_name in cls._frames:
                    active.append(cls._frames[frame_name])

        # If config disabled all matched frames, still use evidential if enabled
        if not active and config.evidential:
            active.append(cls._frames["evidential"])

        return active

    @classmethod
    def score_triggers(cls, prompt: str, max_chars: int = 500) -> Dict[str, int]:
        """
        Score all frames by trigger match count (diagnostic utility).

        Args:
            prompt: Text to analyze
            max_chars: Characters to scan

        Returns:
            Dict mapping frame_name -> trigger_match_count
        """
        cls._ensure_initialized()
        scan_text = prompt[:max_chars].lower()

        scores = {}
        for frame_name, triggers in cls.KEYWORD_TRIGGERS.items():
            count = sum(1 for t in triggers if t in scan_text)
            scores[frame_name] = count

        return scores


def score_all_frames(response: str, config: FrameworkConfig) -> Dict[str, float]:
    """
    Score a response against all active frames.

    Args:
        response: The response text to score
        config: Configuration specifying active frames

    Returns:
        Dict mapping frame names to scores (0.0 - 1.0)
    """
    active_frames = FrameRegistry.get_active(config)
    return {frame.name: frame.score_response(response) for frame in active_frames}


def aggregate_frame_score(response: str, config: FrameworkConfig) -> float:
    """
    Calculate aggregate compliance score across all active frames.

    Args:
        response: The response text to score
        config: Configuration specifying active frames

    Returns:
        Average score across all active frames (0.0 - 1.0)
    """
    scores = score_all_frames(response, config)
    if not scores:
        return 1.0  # No frames active = full compliance
    return sum(scores.values()) / len(scores)


def get_combined_activation_instruction(config: FrameworkConfig) -> str:
    """
    Get combined activation instructions for all active frames.

    Args:
        config: Configuration specifying active frames

    Returns:
        Combined instruction string
    """
    active_frames = FrameRegistry.get_active(config)
    if not active_frames:
        return ""

    instructions = [
        "# COGNITIVE FRAMES ACTIVATION",
        "",
        "The following cognitive frames are ACTIVE. You MUST follow their requirements:",
        "",
    ]

    for frame in active_frames:
        instructions.append(frame.activation_instruction())
        instructions.append("")

    return "\n".join(instructions)
