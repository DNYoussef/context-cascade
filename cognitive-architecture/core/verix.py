"""
VERIX epistemic notation parser and validator.

VERIX provides a structured way to express epistemic claims with:
- AGENT: Who makes the claim (model, user, system, doc, process)
- ILLOCUTION: What speech act is being performed (assert, query, etc.)
- AFFECT: Emotional valence (neutral, positive, negative, uncertain)
- CONTENT: The actual claim being made
- GROUND: Source/evidence supporting the claim
- CONFIDENCE: Numeric confidence level (0.0 - 1.0)
- STATE: Claim status (provisional, confirmed, retracted)

Grammar:
STATEMENT := [AGENT] + ILLOCUTION + AFFECT + CONTENT + GROUND + CONFIDENCE + STATE

Compression Levels:
- L0 (AI<->AI): Emoji shorthand for machine communication
- L1 (AI+Human Inspector): Annotated format with explicit markers
- L2 (Human Reader): Natural language (lossy)
"""

from dataclasses import dataclass
from typing import Optional, List, Tuple
from enum import Enum
import re

from .config import PromptConfig, VerixStrictness, CompressionLevel


class Illocution(Enum):
    """
    Speech act types from speech act theory.

    Determines what the speaker is trying to DO with the utterance.
    """
    ASSERT = "assert"      # Making a factual claim
    QUERY = "query"        # Asking a question
    DIRECT = "direct"      # Giving an instruction
    COMMIT = "commit"      # Making a promise/commitment
    EXPRESS = "express"    # Expressing emotion/attitude


class Affect(Enum):
    """
    Emotional valence markers.

    Indicates the speaker's emotional stance toward the content.
    """
    NEUTRAL = "neutral"      # No emotional loading
    POSITIVE = "positive"    # Favorable stance
    NEGATIVE = "negative"    # Unfavorable stance
    UNCERTAIN = "uncertain"  # Epistemic uncertainty


class State(Enum):
    """
    Claim lifecycle states.

    Tracks whether a claim is still being evaluated, confirmed, or retracted.
    """
    PROVISIONAL = "provisional"  # Initial claim, may be revised
    CONFIRMED = "confirmed"      # Claim verified, high confidence
    RETRACTED = "retracted"      # Claim withdrawn/invalidated


class Agent(Enum):
    """
    Agent identity markers (Hofstadter SYNTH-SEM-003).

    Disambiguates WHO makes each claim.
    """
    MODEL = "model"      # AI model making claim
    USER = "user"        # User's stated claim
    SYSTEM = "system"    # System-generated (hooks, config)
    DOC = "doc"          # From documentation
    PROCESS = "process"  # From running code/computation


class MetaLevel(Enum):
    """
    Meta-level markers (Hofstadter FR2.3).

    Enables claims about claims (meta-reasoning) following
    Hofstadter's hierarchy of self-reference levels.

    Level 1 (OBJECT): Claims about the world/domain
    Level 2 (META): Claims about other claims
    Level 3 (META_VERIX): Claims about VERIX notation itself
    """
    OBJECT = "object"           # Level 1: Claims about the world (default)
    META = "meta"               # Level 2: Claims about claims
    META_VERIX = "meta:verix"   # Level 3: Claims about VERIX itself

    @classmethod
    def from_string(cls, s: Optional[str]) -> "MetaLevel":
        """Parse meta-level from string marker."""
        if s is None:
            return cls.OBJECT
        s_lower = s.lower().strip()
        if s_lower == "meta:verix":
            return cls.META_VERIX
        elif s_lower == "meta":
            return cls.META
        return cls.OBJECT

    def to_marker(self) -> Optional[str]:
        """Return the VERIX marker string for this level."""
        if self == MetaLevel.OBJECT:
            return None  # No marker for object-level claims
        elif self == MetaLevel.META:
            return "[meta]"
        elif self == MetaLevel.META_VERIX:
            return "[meta:verix]"
        return None


@dataclass
class VerixClaim:
    """
    Parsed VERIX claim with all components.

    Represents a single epistemic statement that can be validated
    and tracked through the system.

    Claim IDs enable cycle detection in recursive claims. When a claim's
    ground field references another claim by ID (e.g., ground:"claim-a"),
    we can build a reference graph and detect circular dependencies like
    claim-a -> claim-b -> claim-a.

    Meta-levels (FR2.3) enable Hofstadter-style self-reference:
    - OBJECT (Level 1): Claims about the world/domain
    - META (Level 2): Claims about other claims
    - META_VERIX (Level 3): Claims about VERIX notation itself
    """
    illocution: Illocution
    affect: Affect
    content: str
    ground: Optional[str]      # Source/evidence (required if config says so)
    confidence: float          # 0.0 - 1.0
    state: State
    raw_text: str             # Original unparsed text
    claim_id: Optional[str] = None  # Unique identifier for claim references
    agent: Optional[Agent] = None   # Who makes this claim (FR2.1)
    meta_level: MetaLevel = MetaLevel.OBJECT  # Hofstadter meta-level (FR2.3)

    def is_high_confidence(self, threshold: float = 0.8) -> bool:
        """Check if claim meets confidence threshold."""
        return self.confidence >= threshold

    def is_grounded(self) -> bool:
        """Check if claim has evidence/source."""
        return self.ground is not None and len(self.ground.strip()) > 0

    def to_l0(self) -> str:
        """
        Compress claim to L0 format (emoji shorthand).

        Format: {agent_prefix}{illocution_emoji}{affect_emoji}{confidence%}:{content[:20]}
        """
        agent_map = {
            Agent.MODEL: "M",
            Agent.USER: "U",
            Agent.SYSTEM: "S",
            Agent.DOC: "D",
            Agent.PROCESS: "P",
        }
        illocution_map = {
            Illocution.ASSERT: "A",
            Illocution.QUERY: "?",
            Illocution.DIRECT: "!",
            Illocution.COMMIT: "C",
            Illocution.EXPRESS: "E",
        }
        affect_map = {
            Affect.NEUTRAL: ".",
            Affect.POSITIVE: "+",
            Affect.NEGATIVE: "-",
            Affect.UNCERTAIN: "~",
        }
        agent_prefix = agent_map.get(self.agent, "") if self.agent else ""
        conf_pct = int(self.confidence * 100)
        short_content = self.content[:20] + "..." if len(self.content) > 20 else self.content
        return f"{agent_prefix}{illocution_map[self.illocution]}{affect_map[self.affect]}{conf_pct}:{short_content}"

    def to_l1(self) -> str:
        """
        Format claim as L1 (annotated format for human inspector).

        Format: [meta:X] [agent:X] [id:X] [illocution|affect] content [ground:source] [conf:N.N] [state:state]

        The [meta:X] prefix is only included for meta-level claims (FR2.3).
        The [agent:X] prefix is only included if agent is set (FR2.1).
        The [id:X] prefix is only included if claim_id is set, enabling
        other claims to reference this claim in their ground field.
        """
        parts = []
        # FR2.3: Add meta-level marker if not object-level
        meta_marker = self.meta_level.to_marker()
        if meta_marker:
            parts.append(meta_marker)
        if self.agent:
            parts.append(f"[agent:{self.agent.value}]")
        if self.claim_id:
            parts.append(f"[id:{self.claim_id}]")
        parts.append(f"[{self.illocution.value}|{self.affect.value}]")
        parts.append(self.content)
        if self.ground:
            parts.append(f"[ground:{self.ground}]")
        parts.append(f"[conf:{self.confidence:.2f}]")
        parts.append(f"[state:{self.state.value}]")
        return " ".join(parts)

    def is_meta(self) -> bool:
        """Check if this is a meta-level claim (FR2.3)."""
        return self.meta_level != MetaLevel.OBJECT

    def is_meta_verix(self) -> bool:
        """Check if this claim is about VERIX itself (FR2.3)."""
        return self.meta_level == MetaLevel.META_VERIX

    def to_l2(self) -> str:
        """
        Format claim as L2 (natural language, lossy).

        Converts to readable prose, losing some precision.
        """
        confidence_words = {
            (0.0, 0.3): "I'm quite uncertain, but",
            (0.3, 0.5): "I think",
            (0.5, 0.7): "I believe",
            (0.7, 0.9): "I'm fairly confident that",
            (0.9, 1.0): "I'm highly confident that",
        }

        conf_phrase = "I think"  # default
        for (low, high), phrase in confidence_words.items():
            if low <= self.confidence < high:
                conf_phrase = phrase
                break
        # FIX: Handle edge case of confidence == 1.0 (not covered by < high check)
        if self.confidence >= 1.0:
            conf_phrase = "I'm highly confident that"

        # Add agent attribution if set
        agent_phrase = ""
        if self.agent:
            agent_phrases = {
                Agent.MODEL: "The model claims",
                Agent.USER: "The user states",
                Agent.SYSTEM: "The system reports",
                Agent.DOC: "Documentation indicates",
                Agent.PROCESS: "Process output shows",
            }
            agent_phrase = agent_phrases.get(self.agent, "") + " "
            conf_phrase = conf_phrase.lower()

        ground_phrase = ""
        if self.ground:
            ground_phrase = f" (based on {self.ground})"

        return f"{agent_phrase}{conf_phrase} {self.content}{ground_phrase}."


class VerixParser:
    """
    Parse VERIX-formatted text into VerixClaim objects.

    Supports both L0 and L1 formats. L2 cannot be reliably parsed
    back into structured claims.
    """

    # L1 format pattern: [meta:X] [agent:X] [id:X] [illocution|affect] content [ground:...] [conf:N.N] [state:...]
    # The [meta] or [meta:verix] prefix is optional (FR2.3)
    # The [agent:X] prefix is optional and captures who makes the claim (FR2.1)
    # The [id:X] prefix is optional and captures claim_id for cycle detection
    L1_PATTERN = re.compile(
        r'(?:\[(?P<meta>meta(?::verix)?)\]\s*)?'
        r'(?:\[agent:(?P<agent>\w+)\]\s*)?'
        r'(?:\[id:(?P<claim_id>[\w\-]+)\]\s*)?'
        r'\[(?P<illocution>\w+)\|(?P<affect>\w+)\]'
        r'\s*(?P<content>.+?)'
        r'(?:\s*\[ground:(?P<ground>[^\]]+)\])?'
        r'(?:\s*\[conf:(?P<confidence>[\d.]+)\])?'
        r'(?:\s*\[state:(?P<state>\w+)\])?'
        r'\s*$',
        re.MULTILINE
    )

    # L0 format pattern: {A}{I}{A}{NNN}:{content} where first A is optional agent
    L0_PATTERN = re.compile(
        r'^(?P<agent>[MUSDP])?(?P<illocution>[A?!CE])(?P<affect>[.+\-~])(?P<confidence>\d+):(?P<content>.+)$',
        re.MULTILINE
    )

    def __init__(self, config: Optional[PromptConfig] = None):
        """
        Initialize parser with optional config for defaults.

        Args:
            config: PromptConfig for default values when parsing incomplete claims
        """
        self.config = config or PromptConfig()

    def parse(self, text: str) -> List[VerixClaim]:
        """
        Extract all VERIX claims from text.

        Tries L1 format first, then L0 format.

        Args:
            text: Text containing VERIX-formatted claims

        Returns:
            List of parsed VerixClaim objects
        """
        claims = []

        # Try L1 format
        for match in self.L1_PATTERN.finditer(text):
            claim = self._parse_l1_match(match)
            if claim:
                claims.append(claim)

        # If no L1 claims, try L0 format
        if not claims:
            for match in self.L0_PATTERN.finditer(text):
                claim = self._parse_l0_match(match)
                if claim:
                    claims.append(claim)

        return claims

    def parse_single(self, text: str) -> Optional[VerixClaim]:
        """
        Parse a single VERIX statement.

        Args:
            text: Single VERIX-formatted claim

        Returns:
            VerixClaim if parsing succeeds, None otherwise
        """
        claims = self.parse(text)
        return claims[0] if claims else None

    def _parse_l1_match(self, match: re.Match) -> Optional[VerixClaim]:
        """Parse an L1 format regex match into VerixClaim."""
        try:
            # Extract meta-level if present (FR2.3)
            meta_str = match.group("meta")
            meta_level = MetaLevel.from_string(meta_str)

            # Extract agent if present (FR2.1)
            agent_str = match.group("agent")
            agent = Agent(agent_str.lower()) if agent_str else None

            claim_id = match.group("claim_id")  # May be None if not present
            illocution = Illocution(match.group("illocution").lower())
            affect = Affect(match.group("affect").lower())
            content = match.group("content").strip()
            ground = match.group("ground")
            confidence_str = match.group("confidence")
            confidence = float(confidence_str) if confidence_str else 0.5
            state_str = match.group("state")
            state = State(state_str.lower()) if state_str else State.PROVISIONAL

            return VerixClaim(
                illocution=illocution,
                affect=affect,
                content=content,
                ground=ground,
                confidence=confidence,
                state=state,
                raw_text=match.group(0),
                claim_id=claim_id,
                agent=agent,
                meta_level=meta_level,
            )
        except (ValueError, KeyError):
            return None

    def _parse_l0_match(self, match: re.Match) -> Optional[VerixClaim]:
        """Parse an L0 format regex match into VerixClaim."""
        try:
            agent_map = {
                "M": Agent.MODEL,
                "U": Agent.USER,
                "S": Agent.SYSTEM,
                "D": Agent.DOC,
                "P": Agent.PROCESS,
            }
            illocution_map = {
                "A": Illocution.ASSERT,
                "?": Illocution.QUERY,
                "!": Illocution.DIRECT,
                "C": Illocution.COMMIT,
                "E": Illocution.EXPRESS,
            }
            affect_map = {
                ".": Affect.NEUTRAL,
                "+": Affect.POSITIVE,
                "-": Affect.NEGATIVE,
                "~": Affect.UNCERTAIN,
            }

            # Extract agent if present (FR2.1)
            agent_char = match.group("agent")
            agent = agent_map.get(agent_char) if agent_char else None

            illocution = illocution_map[match.group("illocution")]
            affect = affect_map[match.group("affect")]
            confidence = int(match.group("confidence")) / 100.0
            content = match.group("content").strip()

            return VerixClaim(
                illocution=illocution,
                affect=affect,
                content=content,
                ground=None,  # L0 doesn't include ground
                confidence=confidence,
                state=State.PROVISIONAL,  # L0 doesn't include state
                raw_text=match.group(0),
                agent=agent,
            )
        except (ValueError, KeyError):
            return None


class VerixValidator:
    """
    Validate VERIX compliance in responses.

    Checks that claims meet the requirements specified in PromptConfig,
    including required fields, confidence calibration, and ground chains.
    """

    def __init__(self, config: PromptConfig):
        """
        Initialize validator with configuration.

        Args:
            config: PromptConfig specifying validation requirements
        """
        self.config = config

    def validate(self, claims: List[VerixClaim]) -> Tuple[bool, List[str]]:
        """
        Validate a list of claims against configuration requirements.

        Args:
            claims: List of VerixClaim objects to validate

        Returns:
            Tuple of (is_valid, list_of_violations)
        """
        violations = []

        for i, claim in enumerate(claims):
            claim_violations = self._validate_single(claim, i)
            violations.extend(claim_violations)

        # Check inter-claim consistency
        if len(claims) > 1:
            consistency_violations = self._check_consistency(claims)
            violations.extend(consistency_violations)

        return len(violations) == 0, violations

    def _validate_single(self, claim: VerixClaim, index: int) -> List[str]:
        """Validate a single claim."""
        violations = []
        prefix = f"Claim {index + 1}"

        # Check required ground
        if self.config.require_ground and not claim.is_grounded():
            violations.append(f"{prefix}: Missing ground/evidence (require_ground=True)")

        # Check confidence range
        if not (0.0 <= claim.confidence <= 1.0):
            violations.append(f"{prefix}: Confidence {claim.confidence} outside [0, 1] range")

        # Check strictness requirements
        if self.config.verix_strictness == VerixStrictness.STRICT:
            if not claim.ground:
                violations.append(f"{prefix}: STRICT mode requires ground field")
            if claim.state == State.PROVISIONAL and claim.confidence > 0.8:
                violations.append(
                    f"{prefix}: High confidence ({claim.confidence}) with provisional state"
                )

        return violations

    def _check_consistency(self, claims: List[VerixClaim]) -> List[str]:
        """Check consistency across multiple claims."""
        violations = []

        # Check for contradicting confidence levels on same content
        content_confidence = {}
        for i, claim in enumerate(claims):
            normalized = claim.content.lower().strip()
            if normalized in content_confidence:
                prev_conf, prev_idx = content_confidence[normalized]
                if abs(claim.confidence - prev_conf) > 0.3:
                    violations.append(
                        f"Inconsistent confidence for same content: "
                        f"Claim {prev_idx + 1} ({prev_conf:.2f}) vs "
                        f"Claim {i + 1} ({claim.confidence:.2f})"
                    )
            else:
                content_confidence[normalized] = (claim.confidence, i)

        # Check for retracted claims referenced by confirmed claims
        retracted_content = {
            claim.content.lower().strip()
            for claim in claims
            if claim.state == State.RETRACTED
        }

        for i, claim in enumerate(claims):
            if claim.state == State.CONFIRMED:
                if claim.ground and claim.ground.lower().strip() in retracted_content:
                    violations.append(
                        f"Claim {i + 1}: Confirmed claim references retracted content"
                    )

        return violations

    def detect_ground_cycles(self, claims: List[VerixClaim]) -> List[str]:
        """
        Detect circular dependencies in claim ground references.

        Builds a directed graph where edges represent ground references between
        claims (via claim_id). Uses DFS to find cycles, which indicate circular
        reasoning (e.g., claim-a grounds claim-b which grounds claim-a).

        Args:
            claims: List of VerixClaim objects to analyze

        Returns:
            List of cycle descriptions (e.g., "claim-a -> claim-b -> claim-a")
        """
        # Build claim_id -> claim mapping
        id_to_claim = {}
        for claim in claims:
            if claim.claim_id:
                id_to_claim[claim.claim_id] = claim

        # Build adjacency list: claim_id -> list of referenced claim_ids
        graph = {}
        for claim in claims:
            if claim.claim_id:
                graph[claim.claim_id] = []
                if claim.ground:
                    # Check if ground references another claim by ID
                    # Ground format could be just the ID or contain it
                    ground_lower = claim.ground.lower().strip()
                    for other_id in id_to_claim.keys():
                        if other_id.lower() in ground_lower:
                            graph[claim.claim_id].append(other_id)

        # DFS cycle detection
        cycles = []
        visited = set()
        rec_stack = set()
        path = []

        def dfs(node: str) -> None:
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in rec_stack:
                    # Found cycle - extract it from path
                    cycle_start = path.index(neighbor)
                    cycle_nodes = path[cycle_start:] + [neighbor]
                    cycle_str = " -> ".join(cycle_nodes)
                    if cycle_str not in cycles:
                        cycles.append(cycle_str)

            path.pop()
            rec_stack.remove(node)

        # Run DFS from each unvisited node
        for node in graph.keys():
            if node not in visited:
                dfs(node)

        return cycles

    def compliance_score(self, claims: List[VerixClaim]) -> float:
        """
        Calculate overall compliance score (0.0 - 1.0).

        Higher score means better compliance with VERIX requirements.

        Args:
            claims: List of VerixClaim objects

        Returns:
            Float score from 0.0 (no compliance) to 1.0 (full compliance)
        """
        if not claims:
            return 0.0

        total_points = 0.0
        max_points = 0.0

        for claim in claims:
            # Points for having ground
            max_points += 1.0
            if claim.is_grounded():
                total_points += 1.0

            # Points for confidence in valid range
            max_points += 1.0
            if 0.0 <= claim.confidence <= 1.0:
                total_points += 1.0

            # Points for non-provisional state
            max_points += 0.5
            if claim.state != State.PROVISIONAL:
                total_points += 0.5

            # Points for content not being empty
            max_points += 0.5
            if claim.content.strip():
                total_points += 0.5

            # Bonus points for having agent marker (FR2.1)
            max_points += 0.25
            if claim.agent:
                total_points += 0.25

        # Inter-claim consistency bonus
        _, violations = self.validate(claims)
        consistency_penalty = len(violations) * 0.1
        total_points = max(0, total_points - consistency_penalty)

        return total_points / max_points if max_points > 0 else 0.0


def format_claim(
    claim: VerixClaim,
    compression: CompressionLevel = CompressionLevel.L1_AI_HUMAN
) -> str:
    """
    Format a claim at the specified compression level.

    Convenience function for formatting claims without instantiating objects.

    Args:
        claim: The claim to format
        compression: Target compression level

    Returns:
        Formatted string representation
    """
    if compression == CompressionLevel.L0_AI_AI:
        return claim.to_l0()
    elif compression == CompressionLevel.L1_AI_HUMAN:
        return claim.to_l1()
    else:
        return claim.to_l2()


def create_claim(
    content: str,
    illocution: Illocution = Illocution.ASSERT,
    affect: Affect = Affect.NEUTRAL,
    ground: Optional[str] = None,
    confidence: float = 0.5,
    state: State = State.PROVISIONAL,
    agent: Optional[Agent] = None,
    meta_level: MetaLevel = MetaLevel.OBJECT,
) -> VerixClaim:
    """
    Create a new VERIX claim with sensible defaults.

    Convenience function for creating claims without full specification.

    Args:
        content: The claim content
        illocution: Speech act type (default: ASSERT)
        affect: Emotional valence (default: NEUTRAL)
        ground: Evidence/source (default: None)
        confidence: Confidence level 0-1 (default: 0.5)
        state: Claim state (default: PROVISIONAL)
        agent: Who makes this claim (default: None) (FR2.1)
        meta_level: Hofstadter meta-level (default: OBJECT) (FR2.3)

    Returns:
        New VerixClaim instance
    """
    return VerixClaim(
        illocution=illocution,
        affect=affect,
        content=content,
        ground=ground,
        confidence=confidence,
        state=state,
        raw_text="",
        agent=agent,
        meta_level=meta_level,
    )


def create_meta_claim(
    content: str,
    about_claim: Optional[VerixClaim] = None,
    ground: Optional[str] = None,
    confidence: float = 0.5,
) -> VerixClaim:
    """
    Create a meta-level claim about another claim (FR2.3).

    Convenience function for creating claims about claims.

    Args:
        content: The meta-claim content
        about_claim: The claim this is about (for auto-grounding)
        ground: Explicit ground (overrides about_claim)
        confidence: Confidence level

    Returns:
        New VerixClaim at META level
    """
    actual_ground = ground
    if about_claim and not ground:
        if about_claim.claim_id:
            actual_ground = f"claim:{about_claim.claim_id}"
        else:
            actual_ground = f"claim:{about_claim.content[:30]}..."

    return VerixClaim(
        illocution=Illocution.ASSERT,
        affect=Affect.NEUTRAL,
        content=content,
        ground=actual_ground,
        confidence=confidence,
        state=State.PROVISIONAL,
        raw_text="",
        agent=Agent.MODEL,
        meta_level=MetaLevel.META,
    )


def create_meta_verix_claim(
    content: str,
    ground: Optional[str] = None,
    confidence: float = 0.5,
) -> VerixClaim:
    """
    Create a claim about VERIX notation itself (FR2.3).

    This is the highest meta-level - claims about the notation system.

    Args:
        content: The meta-VERIX claim content
        ground: Evidence/source for the claim
        confidence: Confidence level

    Returns:
        New VerixClaim at META_VERIX level
    """
    return VerixClaim(
        illocution=Illocution.ASSERT,
        affect=Affect.NEUTRAL,
        content=content,
        ground=ground or "verix-spec",
        confidence=confidence,
        state=State.PROVISIONAL,
        raw_text="",
        agent=Agent.SYSTEM,
        meta_level=MetaLevel.META_VERIX,
    )
