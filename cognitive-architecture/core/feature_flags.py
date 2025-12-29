"""
Feature Flags for Hofstadter Improvements.

This module provides a feature flags system for safe rollout and rollback
of Hofstadter-related improvements to the cognitive architecture. Each
feature requirement (FR) can be independently toggled.

Config Version: 1.0.0
"""

from dataclasses import dataclass
from typing import ClassVar, Dict, List, Optional


CONFIG_VERSION = "1.0.0"


@dataclass
class HofstadterFeatureFlags:
    """
    Feature flags for Hofstadter improvements.

    All flags default to False for safe rollout. Each flag corresponds
    to a specific Feature Requirement (FR) from the Hofstadter premortem
    consensus document.

    Attributes:
        verix_agent_markers: FR2.1 - Agent markers for Verix validation
        frame_meta_instruction: FR1.1 - Meta-instruction framing
        frame_recursion_limits: FR1.2 - Recursion depth limits for frames
        frame_thrashing_prevention: FR1.3 - Prevention of frame thrashing
        verix_recursive_validation: FR2.2 - Recursive validation in Verix
        verix_meta_levels: FR2.3 - Meta-level handling in Verix
        globalmoo_tier_constraints: FR3.1 - Tier constraints for GlobalMOO
        globalmoo_self_mod_objective: FR3.2 - Self-modification objectives
        globalmoo_thrashing_detection: FR3.3 - Thrashing detection in GlobalMOO
        dspy_self_ref_signatures: FR4.1 - Self-referential DSPy signatures
        dspy_hofstadter_optimizer: FR4.2 - Hofstadter-aware optimizer
        dspy_homoiconic: FR4.3 - Homoiconic DSPy patterns
    """

    # FR1.x - Frame-related features
    frame_meta_instruction: bool = False
    frame_recursion_limits: bool = False
    frame_thrashing_prevention: bool = False

    # FR2.x - Verix-related features
    verix_agent_markers: bool = False
    verix_recursive_validation: bool = False
    verix_meta_levels: bool = False

    # FR3.x - GlobalMOO-related features
    globalmoo_tier_constraints: bool = False
    globalmoo_self_mod_objective: bool = False
    globalmoo_thrashing_detection: bool = False

    # FR4.x - DSPy-related features
    dspy_self_ref_signatures: bool = False
    dspy_hofstadter_optimizer: bool = False
    dspy_homoiconic: bool = False

    # Class-level singleton instance
    _instance: ClassVar[Optional["HofstadterFeatureFlags"]] = None


    @classmethod
    def _get_feature_map(cls) -> Dict[str, str]:
        """
        Get the mapping of feature names to attribute names.

        Returns:
            Dict mapping feature name strings to attribute names.
        """
        return {
            # FR1.x - Frame features
            "frame_meta_instruction": "frame_meta_instruction",
            "FR1.1": "frame_meta_instruction",
            "frame_recursion_limits": "frame_recursion_limits",
            "FR1.2": "frame_recursion_limits",
            "frame_thrashing_prevention": "frame_thrashing_prevention",
            "FR1.3": "frame_thrashing_prevention",

            # FR2.x - Verix features
            "verix_agent_markers": "verix_agent_markers",
            "FR2.1": "verix_agent_markers",
            "verix_recursive_validation": "verix_recursive_validation",
            "FR2.2": "verix_recursive_validation",
            "verix_meta_levels": "verix_meta_levels",
            "FR2.3": "verix_meta_levels",

            # FR3.x - GlobalMOO features
            "globalmoo_tier_constraints": "globalmoo_tier_constraints",
            "FR3.1": "globalmoo_tier_constraints",
            "globalmoo_self_mod_objective": "globalmoo_self_mod_objective",
            "FR3.2": "globalmoo_self_mod_objective",
            "globalmoo_thrashing_detection": "globalmoo_thrashing_detection",
            "FR3.3": "globalmoo_thrashing_detection",

            # FR4.x - DSPy features
            "dspy_self_ref_signatures": "dspy_self_ref_signatures",
            "FR4.1": "dspy_self_ref_signatures",
            "dspy_hofstadter_optimizer": "dspy_hofstadter_optimizer",
            "FR4.2": "dspy_hofstadter_optimizer",
            "dspy_homoiconic": "dspy_homoiconic",
            "FR4.3": "dspy_homoiconic",
        }

    @classmethod
    def get_instance(cls) -> "HofstadterFeatureFlags":
        """
        Get the singleton instance of feature flags.

        Returns:
            The singleton HofstadterFeatureFlags instance.
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Reset the singleton instance (useful for testing)."""
        cls._instance = None

    @classmethod
    def is_enabled(cls, feature_name: str) -> bool:
        """
        Check if a feature is enabled.

        Args:
            feature_name: The name of the feature to check. Can be either
                the attribute name (e.g., "verix_agent_markers") or the
                FR code (e.g., "FR2.1").

        Returns:
            True if the feature is enabled, False otherwise.

        Raises:
            ValueError: If the feature name is not recognized.
        """
        instance = cls.get_instance()
        feature_map = cls._get_feature_map()

        if feature_name not in feature_map:
            raise ValueError(
                f"Unknown feature: {feature_name}. "
                f"Valid features: {list(set(feature_map.values()))}"
            )

        attr_name = feature_map[feature_name]
        return getattr(instance, attr_name)

    @classmethod
    def enable_feature(cls, feature_name: str) -> None:
        """
        Enable a feature.

        Args:
            feature_name: The name of the feature to enable. Can be either
                the attribute name (e.g., "verix_agent_markers") or the
                FR code (e.g., "FR2.1").

        Raises:
            ValueError: If the feature name is not recognized.
        """
        instance = cls.get_instance()
        feature_map = cls._get_feature_map()

        if feature_name not in feature_map:
            raise ValueError(
                f"Unknown feature: {feature_name}. "
                f"Valid features: {list(set(feature_map.values()))}"
            )

        attr_name = feature_map[feature_name]
        setattr(instance, attr_name, True)

    @classmethod
    def disable_feature(cls, feature_name: str) -> None:
        """
        Disable a feature.

        Args:
            feature_name: The name of the feature to disable. Can be either
                the attribute name (e.g., "verix_agent_markers") or the
                FR code (e.g., "FR2.1").

        Raises:
            ValueError: If the feature name is not recognized.
        """
        instance = cls.get_instance()
        feature_map = cls._get_feature_map()

        if feature_name not in feature_map:
            raise ValueError(
                f"Unknown feature: {feature_name}. "
                f"Valid features: {list(set(feature_map.values()))}"
            )

        attr_name = feature_map[feature_name]
        setattr(instance, attr_name, False)

    @classmethod
    def enable_all(cls) -> None:
        """Enable all feature flags."""
        instance = cls.get_instance()
        for attr_name in set(cls._get_feature_map().values()):
            setattr(instance, attr_name, True)

    @classmethod
    def disable_all(cls) -> None:
        """Disable all feature flags."""
        instance = cls.get_instance()
        for attr_name in set(cls._get_feature_map().values()):
            setattr(instance, attr_name, False)

    @classmethod
    def get_enabled_features(cls) -> List[str]:
        """
        Get a list of all enabled feature names.

        Returns:
            List of enabled feature attribute names.
        """
        instance = cls.get_instance()
        enabled = []
        for attr_name in set(cls._get_feature_map().values()):
            if getattr(instance, attr_name):
                enabled.append(attr_name)
        return sorted(enabled)

    @classmethod
    def get_config_version(cls) -> str:
        """
        Get the configuration version.

        Returns:
            The config version string.
        """
        return CONFIG_VERSION

    def to_dict(self) -> Dict[str, bool]:
        """
        Convert feature flags to a dictionary.

        Returns:
            Dictionary mapping feature names to their boolean states.
        """
        return {
            "frame_meta_instruction": self.frame_meta_instruction,
            "frame_recursion_limits": self.frame_recursion_limits,
            "frame_thrashing_prevention": self.frame_thrashing_prevention,
            "verix_agent_markers": self.verix_agent_markers,
            "verix_recursive_validation": self.verix_recursive_validation,
            "verix_meta_levels": self.verix_meta_levels,
            "globalmoo_tier_constraints": self.globalmoo_tier_constraints,
            "globalmoo_self_mod_objective": self.globalmoo_self_mod_objective,
            "globalmoo_thrashing_detection": self.globalmoo_thrashing_detection,
            "dspy_self_ref_signatures": self.dspy_self_ref_signatures,
            "dspy_hofstadter_optimizer": self.dspy_hofstadter_optimizer,
            "dspy_homoiconic": self.dspy_homoiconic,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, bool]) -> "HofstadterFeatureFlags":
        """
        Create a HofstadterFeatureFlags instance from a dictionary.

        Args:
            data: Dictionary mapping feature names to boolean states.

        Returns:
            A new HofstadterFeatureFlags instance.
        """
        # Filter to only known fields
        known_fields = {
            "frame_meta_instruction",
            "frame_recursion_limits",
            "frame_thrashing_prevention",
            "verix_agent_markers",
            "verix_recursive_validation",
            "verix_meta_levels",
            "globalmoo_tier_constraints",
            "globalmoo_self_mod_objective",
            "globalmoo_thrashing_detection",
            "dspy_self_ref_signatures",
            "dspy_hofstadter_optimizer",
            "dspy_homoiconic",
        }
        filtered_data = {k: v for k, v in data.items() if k in known_fields}
        return cls(**filtered_data)
