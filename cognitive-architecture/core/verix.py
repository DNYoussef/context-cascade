"""
VERIX epistemic notation parser and validator.

VERIX provides a structured way to express epistemic claims with:
- ILLOCUTION: What speech act is being performed (assert, query, etc.)
- AFFECT: Emotional valence (neutral, positive, negative, uncertain)
- CONTENT: The actual claim being made
- GROUND: Source/evidence supporting the claim
- CONFIDENCE: Numeric confidence level (0.0 - 1.0)
- STATE: Claim status (provisional, confirmed, retracted)

Grammar:
STATEMENT := ILLOCUTION + AFFECT + CONTENT + GROUND + CONFIDENCE + STATE

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


@dataclass
class VerixClaim:
    """
    Parsed VERIX claim with all components.

    Represents a single epistemic statement that can be validated
    and tracked through the system.
    """
    illocution: Illocution
    affect: Affect
    content: str
    ground: Optional[str]      # Source/evidence (required if config says so)
    confidence: float          # 0.0 - 1.0
    state: State
    raw_text: str             # Original unparsed text

    def is_high_confidence(self, threshold: float = 0.8) -> bool:
        """Check if claim meets confidence threshold."""
        return self.confidence >= threshold

    def is_grounded(self) -> bool:
        """Check if claim has evidence/source."""
        return self.ground is not None and len(self.ground.strip()) > 0

    def to_l0(self) -> str:
        """
        Compress claim to L0 format (emoji shorthand).

        Format: {illocution_emoji}{affect_emoji}{confidence%}:{content[:20]}
        """
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
        conf_pct = int(self.confidence * 100)
        short_content = self.content[:20] + "..." if len(self.content) > 20 else self.content
        return f"{illocution_map[self.illocution]}{affect_map[self.affect]}{conf_pct}:{short_content}"

    def to_l1(self) -> str:
        """
        Format claim as L1 (annotated format for human inspector).

        Format: [illocution|affect] content [ground:source] [conf:N.N] [state:state]
        """
        parts = [f"[{self.illocution.value}|{self.affect.value}]", self.content]
        if self.ground:
            parts.append(f"[ground:{self.ground}]")
        parts.append(f"[conf:{self.confidence:.2f}]")
        parts.append(f"[state:{self.state.value}]")
        return " ".join(parts)

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

        ground_phrase = ""
        if self.ground:
            ground_phrase = f" (based on {self.ground})"

        return f"{conf_phrase} {self.content}{ground_phrase}."


class VerixParser:
    """
    Parse VERIX-formatted text into VerixClaim objects.

    Supports both L0 and L1 formats. L2 cannot be reliably parsed
    back into structured claims.
    """

    # L1 format pattern: [illocution|affect] content [ground:...] [conf:N.N] [state:...]
    L1_PATTERN = re.compile(
        r'\[(?P<illocution>\w+)\|(?P<affect>\w+)\]'
        r'\s*(?P<content>.+?)'
        r'(?:\s*\[ground:(?P<ground>[^\]]+)\])?'
        r'(?:\s*\[conf:(?P<confidence>[\d.]+)\])?'
        r'(?:\s*\[state:(?P<state>\w+)\])?'
        r'\s*$',
        re.MULTILINE
    )

    # L0 format pattern: {I}{A}{NNN}:{content}
    L0_PATTERN = re.compile(
        r'^(?P<illocution>[A?!CE])(?P<affect>[.+\-~])(?P<confidence>\d+):(?P<content>.+)$',
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
            )
        except (ValueError, KeyError):
            return None

    def _parse_l0_match(self, match: re.Match) -> Optional[VerixClaim]:
        """Parse an L0 format regex match into VerixClaim."""
        try:
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
    )
