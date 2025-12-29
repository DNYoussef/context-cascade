"""
DSPy Compatibility Layer for Hofstadter Improvements.

Defense Layer 1 for R-DSP-01 (DSPy incompatibility risk).

This module provides:
1. Version detection and compatibility checks
2. Polyfills for missing homoiconic APIs
3. Graceful degradation for older DSPy versions
4. Abstract interface hiding DSPy internals

Requires: dspy-ai >= 2.0 for full homoiconic support
Fallback: Read-only mode for DSPy < 2.0
"""

import sys
import logging
from typing import Any, Dict, List, Optional, Type, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)

# Try to import DSPy
DSPY_AVAILABLE = False
DSPY_VERSION = "0.0.0"
DSPY_HOMOICONIC_SUPPORT = False

try:
    import dspy
    DSPY_AVAILABLE = True
    DSPY_VERSION = getattr(dspy, "__version__", "unknown")

    # Check for homoiconic support (requires 2.0+)
    # Test if key APIs exist
    try:
        # Check if Signature has the methods we need
        if hasattr(dspy, "Signature"):
            sig_class = dspy.Signature
            has_input_fields = hasattr(sig_class, "input_fields") or callable(getattr(sig_class, "input_fields", None))
            has_with_instructions = hasattr(sig_class, "with_instructions")
            DSPY_HOMOICONIC_SUPPORT = has_input_fields
    except Exception:
        DSPY_HOMOICONIC_SUPPORT = False

except ImportError:
    logger.warning("DSPy not installed. DSPy features will be disabled.")


class CompatMode(Enum):
    """DSPy compatibility modes."""
    FULL = "full"           # DSPy >= 2.0 with homoiconic support
    LIMITED = "limited"     # DSPy installed but missing features
    MOCK = "mock"           # DSPy not installed, use mocks
    DISABLED = "disabled"   # Explicitly disabled


@dataclass
class DSPyCompatConfig:
    """Configuration for DSPy compatibility layer."""
    mode: CompatMode = CompatMode.MOCK
    fallback_on_error: bool = True
    log_warnings: bool = True
    strict_type_checking: bool = True

    @classmethod
    def auto_detect(cls) -> "DSPyCompatConfig":
        """Auto-detect best compatibility mode."""
        if not DSPY_AVAILABLE:
            return cls(mode=CompatMode.MOCK)
        elif DSPY_HOMOICONIC_SUPPORT:
            return cls(mode=CompatMode.FULL)
        else:
            return cls(mode=CompatMode.LIMITED)


# Global config instance
COMPAT_CONFIG = DSPyCompatConfig.auto_detect()


def get_compat_status() -> Dict[str, Any]:
    """Get current compatibility status."""
    return {
        "dspy_available": DSPY_AVAILABLE,
        "dspy_version": DSPY_VERSION,
        "homoiconic_support": DSPY_HOMOICONIC_SUPPORT,
        "mode": COMPAT_CONFIG.mode.value,
    }


# =============================================================================
# MOCK IMPLEMENTATIONS (for when DSPy is not available)
# =============================================================================

@dataclass
class MockField:
    """Mock DSPy field for testing without DSPy."""
    name: str
    field_type: str  # "input" or "output"
    annotation: type = str
    desc: Optional[str] = None
    prefix: Optional[str] = None

    @property
    def json_schema_extra(self) -> Dict[str, Any]:
        return {
            "__dspy_field_type": self.field_type,
            "desc": self.desc,
            "prefix": self.prefix,
        }


class MockSignature:
    """
    Mock DSPy Signature for testing without DSPy.

    Implements the essential Signature API for homoiconic operations.
    """

    def __init__(
        self,
        name: str = "MockSignature",
        instructions: str = "",
        inputs: Optional[Dict[str, MockField]] = None,
        outputs: Optional[Dict[str, MockField]] = None,
    ):
        self._name = name
        self._instructions = instructions
        self._inputs = inputs or {}
        self._outputs = outputs or {}

        # Build model_fields compatible structure
        self.model_fields = {}
        for name, field in self._inputs.items():
            self.model_fields[name] = field
        for name, field in self._outputs.items():
            self.model_fields[name] = field

    @property
    def __name__(self) -> str:
        return self._name

    @property
    def __doc__(self) -> str:
        return self._instructions

    @property
    def instructions(self) -> str:
        return self._instructions

    @property
    def input_fields(self) -> Dict[str, MockField]:
        return self._inputs

    @property
    def output_fields(self) -> Dict[str, MockField]:
        return self._outputs

    @property
    def signature(self) -> str:
        """Generate string representation."""
        inputs = ", ".join(self._inputs.keys())
        outputs = ", ".join(self._outputs.keys())
        return f"{inputs} -> {outputs}"

    def with_instructions(self, text: str) -> "MockSignature":
        """Create new signature with updated instructions."""
        return MockSignature(
            name=self._name,
            instructions=text,
            inputs=dict(self._inputs),
            outputs=dict(self._outputs),
        )

    def __repr__(self) -> str:
        return f"MockSignature({self._name}: {self.signature})"


def create_mock_input_field(desc: Optional[str] = None) -> MockField:
    """Create a mock input field."""
    return MockField(name="", field_type="input", desc=desc)


def create_mock_output_field(desc: Optional[str] = None) -> MockField:
    """Create a mock output field."""
    return MockField(name="", field_type="output", desc=desc)


# =============================================================================
# SIGNATURE INTROSPECTION (FR4.1 support)
# =============================================================================

def get_signature_fields(sig: Any) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Extract input and output fields from a signature.

    Works with both real DSPy signatures and mocks.

    Args:
        sig: DSPy Signature or MockSignature

    Returns:
        Tuple of (input_fields_dict, output_fields_dict)
    """
    if COMPAT_CONFIG.mode == CompatMode.MOCK or isinstance(sig, MockSignature):
        return sig.input_fields, sig.output_fields

    # Real DSPy signature
    try:
        if hasattr(sig, "input_fields") and hasattr(sig, "output_fields"):
            # DSPy 2.0+ style
            inputs = dict(sig.input_fields) if callable(getattr(sig, "input_fields", None)) else sig.input_fields
            outputs = dict(sig.output_fields) if callable(getattr(sig, "output_fields", None)) else sig.output_fields
            return inputs, outputs
        elif hasattr(sig, "model_fields"):
            # Pydantic-based introspection
            inputs = {}
            outputs = {}
            for name, field in sig.model_fields.items():
                extra = getattr(field, "json_schema_extra", {}) or {}
                field_type = extra.get("__dspy_field_type", "input")
                if field_type == "input":
                    inputs[name] = field
                else:
                    outputs[name] = field
            return inputs, outputs
    except Exception as e:
        logger.warning(f"Failed to extract fields from signature: {e}")

    return {}, {}


def get_signature_instructions(sig: Any) -> str:
    """Get instructions/docstring from a signature."""
    if hasattr(sig, "instructions"):
        return sig.instructions or ""
    if hasattr(sig, "__doc__"):
        return sig.__doc__ or ""
    return ""


def get_signature_name(sig: Any) -> str:
    """Get name of a signature class."""
    if hasattr(sig, "__name__"):
        return sig.__name__
    return type(sig).__name__


# =============================================================================
# HOMOICONIC OPERATIONS (FR4.3 support)
# =============================================================================

def signature_to_dict(sig: Any) -> Dict[str, Any]:
    """
    Convert a DSPy Signature to a JSON-serializable dictionary.

    FR4.3: Enables homoiconic manipulation of signatures.

    Args:
        sig: DSPy Signature or MockSignature

    Returns:
        Dictionary representation suitable for JSON serialization
    """
    inputs, outputs = get_signature_fields(sig)

    def field_to_dict(name: str, field: Any) -> Dict[str, Any]:
        """Convert a single field to dict."""
        if isinstance(field, MockField):
            return {
                "name": name,
                "type": field.annotation.__name__ if hasattr(field.annotation, "__name__") else str(field.annotation),
                "desc": field.desc,
                "prefix": field.prefix,
            }

        # Real DSPy field
        extra = getattr(field, "json_schema_extra", {}) or {}
        annotation = getattr(field, "annotation", str)
        return {
            "name": name,
            "type": annotation.__name__ if hasattr(annotation, "__name__") else str(annotation),
            "desc": extra.get("desc"),
            "prefix": extra.get("prefix"),
        }

    return {
        "class_name": get_signature_name(sig),
        "docstring": get_signature_instructions(sig),
        "inputs": {name: field_to_dict(name, f) for name, f in inputs.items()},
        "outputs": {name: field_to_dict(name, f) for name, f in outputs.items()},
    }


def dict_to_signature(data: Dict[str, Any]) -> Any:
    """
    Create a signature from a dictionary specification.

    FR4.3: Enables dynamic signature creation from data.

    Args:
        data: Dictionary with class_name, docstring, inputs, outputs

    Returns:
        New signature instance (MockSignature or real dspy.Signature)
    """
    class_name = data.get("class_name", "DynamicSignature")
    docstring = data.get("docstring", "")
    inputs_data = data.get("inputs", {})
    outputs_data = data.get("outputs", {})

    if COMPAT_CONFIG.mode == CompatMode.MOCK or not DSPY_AVAILABLE:
        # Create MockSignature
        inputs = {}
        for name, field_data in inputs_data.items():
            inputs[name] = MockField(
                name=name,
                field_type="input",
                desc=field_data.get("desc"),
                prefix=field_data.get("prefix"),
            )

        outputs = {}
        for name, field_data in outputs_data.items():
            outputs[name] = MockField(
                name=name,
                field_type="output",
                desc=field_data.get("desc"),
                prefix=field_data.get("prefix"),
            )

        return MockSignature(
            name=class_name,
            instructions=docstring,
            inputs=inputs,
            outputs=outputs,
        )

    # Create real DSPy Signature dynamically
    try:
        # Build field annotations
        annotations = {}
        namespace = {"__doc__": docstring, "__module__": __name__}

        for name, field_data in inputs_data.items():
            annotations[name] = str  # Default to str
            namespace[name] = dspy.InputField(desc=field_data.get("desc"))

        for name, field_data in outputs_data.items():
            annotations[name] = str  # Default to str
            namespace[name] = dspy.OutputField(desc=field_data.get("desc"))

        namespace["__annotations__"] = annotations

        # Create new type dynamically
        new_sig = type(class_name, (dspy.Signature,), namespace)
        return new_sig

    except Exception as e:
        logger.error(f"Failed to create dynamic signature: {e}")
        if COMPAT_CONFIG.fallback_on_error:
            # Fallback to mock
            return dict_to_signature.__wrapped__(data) if hasattr(dict_to_signature, "__wrapped__") else MockSignature(name=class_name)
        raise


def mutate_signature(
    sig: Any,
    mutation: str,
    mutation_params: Optional[Dict[str, Any]] = None,
) -> Any:
    """
    Apply a mutation to a signature at runtime.

    FR4.3: Enables self-modifying signatures.

    Supported mutations:
    - "add_confidence_output": Add float confidence output field
    - "add_evidence_input": Add string evidence_type input field
    - "add_field": Add arbitrary field (requires field_name, field_type, is_output in params)
    - "remove_field": Remove a field (requires field_name in params)
    - "update_instructions": Update docstring (requires instructions in params)

    Args:
        sig: Signature to mutate
        mutation: Mutation type string
        mutation_params: Parameters for the mutation

    Returns:
        New mutated signature (original is not modified)
    """
    params = mutation_params or {}

    # Convert to dict for manipulation
    sig_dict = signature_to_dict(sig)

    if mutation == "add_confidence_output":
        sig_dict["outputs"]["confidence"] = {
            "name": "confidence",
            "type": "float",
            "desc": "Confidence score from 0.0 to 1.0",
        }

    elif mutation == "add_evidence_input":
        sig_dict["inputs"]["evidence_type"] = {
            "name": "evidence_type",
            "type": "str",
            "desc": "Type of evidence: witnessed, reported, inferred, assumed",
        }

    elif mutation == "add_field":
        field_name = params.get("field_name", "new_field")
        field_type = params.get("field_type", "str")
        is_output = params.get("is_output", False)
        desc = params.get("desc", None)

        target = sig_dict["outputs"] if is_output else sig_dict["inputs"]
        target[field_name] = {
            "name": field_name,
            "type": field_type,
            "desc": desc,
        }

    elif mutation == "remove_field":
        field_name = params.get("field_name")
        if field_name:
            sig_dict["inputs"].pop(field_name, None)
            sig_dict["outputs"].pop(field_name, None)

    elif mutation == "update_instructions":
        sig_dict["docstring"] = params.get("instructions", sig_dict["docstring"])

    else:
        logger.warning(f"Unknown mutation type: {mutation}")
        return sig

    # Convert back to signature
    return dict_to_signature(sig_dict)


def validate_signature_roundtrip(sig: Any) -> Tuple[bool, List[str]]:
    """
    Validate that a signature survives dict roundtrip.

    Defense Layer 2 for R-HOM-01 (type safety).

    Args:
        sig: Signature to validate

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    try:
        # Get original structure
        orig_inputs, orig_outputs = get_signature_fields(sig)
        orig_name = get_signature_name(sig)

        # Roundtrip
        sig_dict = signature_to_dict(sig)
        reconstructed = dict_to_signature(sig_dict)

        # Get reconstructed structure
        new_inputs, new_outputs = get_signature_fields(reconstructed)
        new_name = get_signature_name(reconstructed)

        # Validate
        if set(orig_inputs.keys()) != set(new_inputs.keys()):
            errors.append(f"Input fields mismatch: {set(orig_inputs.keys())} vs {set(new_inputs.keys())}")

        if set(orig_outputs.keys()) != set(new_outputs.keys()):
            errors.append(f"Output fields mismatch: {set(orig_outputs.keys())} vs {set(new_outputs.keys())}")

        if orig_name != new_name:
            errors.append(f"Name mismatch: {orig_name} vs {new_name}")

    except Exception as e:
        errors.append(f"Roundtrip failed with exception: {e}")

    return len(errors) == 0, errors


# =============================================================================
# OPTIMIZER SUPPORT (FR4.2 support)
# =============================================================================

@dataclass
class MockOptimizer:
    """Mock optimizer for testing without DSPy."""
    metric: Optional[Callable] = None
    max_bootstrapped_demos: int = 4
    max_labeled_demos: int = 4
    max_rounds: int = 1
    max_recursion_depth: int = 5
    base_case_threshold: float = 0.95

    def compile(self, student: Any, trainset: List[Any]) -> Any:
        """Mock compile that just returns the student."""
        logger.info("MockOptimizer.compile called - returning student unchanged")
        return student

    def is_base_case(self, score: float, depth: int) -> bool:
        """Check if we've reached base case (Hofstadter FR4.2)."""
        if score >= self.base_case_threshold:
            return True
        if depth >= self.max_recursion_depth:
            return True
        return False


def create_optimizer(
    metric: Optional[Callable] = None,
    optimizer_type: str = "bootstrap",
    **kwargs
) -> Any:
    """
    Create an optimizer with compatibility handling.

    Args:
        metric: Metric function for optimization
        optimizer_type: Type of optimizer (bootstrap, mipro, hofstadter)
        **kwargs: Additional optimizer parameters

    Returns:
        Optimizer instance (real or mock)
    """
    if COMPAT_CONFIG.mode == CompatMode.MOCK or not DSPY_AVAILABLE:
        return MockOptimizer(metric=metric, **kwargs)

    try:
        if optimizer_type == "bootstrap":
            return dspy.BootstrapFewShot(metric=metric, **kwargs)
        elif optimizer_type == "mipro":
            return dspy.MIPROv2(metric=metric, **kwargs)
        else:
            # Default to bootstrap
            return dspy.BootstrapFewShot(metric=metric, **kwargs)
    except Exception as e:
        logger.error(f"Failed to create optimizer: {e}")
        if COMPAT_CONFIG.fallback_on_error:
            return MockOptimizer(metric=metric, **kwargs)
        raise
