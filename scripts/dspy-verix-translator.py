#!/usr/bin/env python3
"""
DSPy-Enhanced VERIX Translator v1.0.0

[assert|neutral] Uses DSPy at inference level to translate content to VERILINGUA x VERIX [ground:design] [conf:0.95] [state:ongoing]

This script leverages DSPy's programmatic prompt optimization to:
1. Parse existing command/skill/agent content
2. Apply VERILINGUA cognitive frames during translation
3. Generate VERIX-compliant output
4. Validate epistemic markers and confidence scores

DSPy Integration:
  - Uses DSPy signatures for structured translation
  - Applies VERILINGUA frames as constraints
  - Generates ground chains and confidence scores
  - Validates output against VERIX grammar

Usage:
  python dspy-verix-translator.py --translate-command PATH
  python dspy-verix-translator.py --translate-skill PATH
  python dspy-verix-translator.py --translate-agent PATH
  python dspy-verix-translator.py --batch-translate TYPE DIR
"""

import os
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime

# Try to import DSPy
try:
    import dspy
    from dspy import Signature, InputField, OutputField, Module, ChainOfThought
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("[warn|neutral] DSPy not installed, using fallback translator [ground:import-check] [conf:1.0] [state:confirmed]")


# ============================================================================
# VERIX GRAMMAR DEFINITIONS
# ============================================================================

ILLOCUTION_TYPES = {
    'assert': 'factual claim',
    'query': 'question',
    'direct': 'instruction/command',
    'request': 'polite request',
    'commit': 'promise/commitment',
    'warn': 'warning/caution',
    'hypo': 'hypothesis/supposition',
    'define': 'definition'
}

AFFECT_TYPES = {
    'neutral': '',
    'positive': 'with satisfaction',
    'negative': 'with concern',
    'confident': 'with conviction',
    'uncertain': 'with doubt',
    'emphatic': 'strongly'
}

GROUND_TYPES = {
    'witnessed': 0.95,
    'reported': 0.70,
    'inferred': 0.85,
    'assumed': 0.30,
    'calculated': 0.99,
    'given': 1.0,
    'entailed': 1.0
}

# VERILINGUA cognitive frames
VERILINGUA_FRAMES = {
    'evidential': 'How do you know? (witnessed/reported/inferred/assumed)',
    'aspectual': 'Complete or ongoing? (complete/ongoing/habitual/attempted)',
    'morphological': 'What are the root components? (root/derived/composed)',
    'compositional': 'Build from primitives? (primitive/compound/builds)',
    'honorific': 'Who is the audience? (audience/formality/register)',
    'classifier': 'What type/count? (type/category/measure)',
    'spatial': 'Absolute position? (path/location/direction)'
}


# ============================================================================
# DSPy SIGNATURES FOR VERIX TRANSLATION
# ============================================================================

if DSPY_AVAILABLE:
    class VerixTranslationSignature(Signature):
        """Translate content to VERILINGUA x VERIX format.

        Apply all 7 VERILINGUA cognitive frames and output in VERIX L1 notation.
        Every statement must include: [illocution|affect] content [ground:source] [conf:X.XX] [state:status]
        """
        original_content = InputField(desc="The original command/skill/agent content to translate")
        content_type = InputField(desc="Type: 'command', 'skill', or 'agent'")
        verilingua_frames = InputField(desc="The 7 VERILINGUA cognitive frames to apply")

        verix_content = OutputField(desc="The translated content in VERIX L1 format")
        claims_extracted = OutputField(desc="List of claims with illocution, ground, confidence, state")
        validation_report = OutputField(desc="Validation of VERIX compliance")


    class ClaimExtractionSignature(Signature):
        """Extract individual claims from content and assign VERIX markers."""
        content = InputField(desc="Content to extract claims from")

        claims = OutputField(desc="List of claims with {text, illocution, affect, ground, confidence, state}")


    class VerixValidationSignature(Signature):
        """Validate VERIX-formatted content."""
        verix_content = InputField(desc="VERIX-formatted content to validate")

        is_valid = OutputField(desc="Whether content is valid VERIX")
        errors = OutputField(desc="List of validation errors if any")
        suggestions = OutputField(desc="Suggestions for fixing errors")


    class VerixTranslatorModule(Module):
        """DSPy module for VERIX translation."""

        def __init__(self):
            super().__init__()
            self.translate = ChainOfThought(VerixTranslationSignature)
            self.extract = ChainOfThought(ClaimExtractionSignature)
            self.validate = ChainOfThought(VerixValidationSignature)

        def forward(self, content: str, content_type: str) -> Dict[str, Any]:
            # Step 1: Translate to VERIX
            translation = self.translate(
                original_content=content,
                content_type=content_type,
                verilingua_frames=json.dumps(VERILINGUA_FRAMES)
            )

            # Step 2: Extract and validate claims
            claims = self.extract(content=translation.verix_content)

            # Step 3: Validate output
            validation = self.validate(verix_content=translation.verix_content)

            return {
                'verix_content': translation.verix_content,
                'claims': claims.claims,
                'validation': {
                    'is_valid': validation.is_valid,
                    'errors': validation.errors,
                    'suggestions': validation.suggestions
                }
            }


# ============================================================================
# FALLBACK TRANSLATOR (when DSPy not available)
# ============================================================================

@dataclass
class VerixClaim:
    """A single VERIX claim."""
    text: str
    illocution: str = 'assert'
    affect: str = 'neutral'
    ground: str = 'given'
    confidence: float = 0.95
    state: str = 'confirmed'

    def to_verix(self) -> str:
        return f"[{self.illocution}|{self.affect}] {self.text} [ground:{self.ground}] [conf:{self.confidence:.2f}] [state:{self.state}]"


class FallbackVerixTranslator:
    """Simple rule-based VERIX translator."""

    def __init__(self):
        self.claim_patterns = [
            (r'^##\s+(.+)$', 'define', 'neutral', 'given', 1.0),  # Headers -> definitions
            (r'^\*\*(.+)\*\*:', 'define', 'neutral', 'given', 0.95),  # Bold labels
            (r'^-\s+(.+)$', 'assert', 'neutral', 'witnessed', 0.90),  # List items
            (r'^```', 'define', 'neutral', 'given', 1.0),  # Code blocks
            (r'^(Note|Warning|Important):', 'warn', 'emphatic', 'given', 0.95),  # Warnings
            (r'^\?', 'query', 'uncertain', 'assumed', 0.60),  # Questions
        ]

    def extract_claims(self, content: str) -> List[VerixClaim]:
        """Extract claims from content."""
        claims = []
        lines = content.split('\n')

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Match against patterns
            for pattern, illocution, affect, ground, conf in self.claim_patterns:
                if re.match(pattern, line, re.MULTILINE):
                    claim = VerixClaim(
                        text=line[:100],
                        illocution=illocution,
                        affect=affect,
                        ground=ground,
                        confidence=conf
                    )
                    claims.append(claim)
                    break
            else:
                # Default claim
                claims.append(VerixClaim(
                    text=line[:100],
                    illocution='assert',
                    affect='neutral',
                    ground='given',
                    confidence=0.90
                ))

        return claims

    def translate(self, content: str, content_type: str) -> Dict[str, Any]:
        """Translate content to VERIX format."""
        claims = self.extract_claims(content)

        # Build VERIX output
        verix_lines = []
        for claim in claims[:50]:  # Limit to 50 claims
            verix_lines.append(claim.to_verix())

        return {
            'verix_content': '\n'.join(verix_lines),
            'claims': [c.__dict__ for c in claims],
            'validation': {
                'is_valid': True,
                'errors': [],
                'suggestions': []
            }
        }


# ============================================================================
# MAIN TRANSLATOR CLASS
# ============================================================================

class VerixTranslator:
    """Main translator class that uses DSPy if available, fallback otherwise."""

    def __init__(self, use_dspy: bool = True):
        self.use_dspy = use_dspy and DSPY_AVAILABLE

        if self.use_dspy:
            self._configure_dspy()
            self.module = VerixTranslatorModule()
            print("[assert|positive] Using DSPy-enhanced translation [ground:dspy-configured] [conf:0.95] [state:confirmed]")
        else:
            self.fallback = FallbackVerixTranslator()
            print("[assert|neutral] Using fallback translation [ground:dspy-unavailable] [conf:0.90] [state:confirmed]")

    def _configure_dspy(self):
        """Configure DSPy with Claude."""
        try:
            # Try to configure with Claude
            api_key = os.environ.get('ANTHROPIC_API_KEY')
            if api_key:
                lm = dspy.LM(
                    model="anthropic/claude-3-haiku-20240307",
                    api_key=api_key,
                    max_tokens=4096
                )
                dspy.configure(lm=lm)
            else:
                print("[warn|neutral] No API key found, DSPy will use defaults [ground:env-check] [conf:0.80] [state:confirmed]")
        except Exception as e:
            print(f"[warn|negative] DSPy configuration error: {e} [ground:error] [conf:0.70] [state:confirmed]")

    def translate(self, content: str, content_type: str) -> Dict[str, Any]:
        """Translate content to VERIX format."""
        if self.use_dspy:
            try:
                return self.module(content=content, content_type=content_type)
            except Exception as e:
                print(f"[warn|negative] DSPy translation failed, using fallback: {e}")
                return self.fallback.translate(content, content_type)
        else:
            return self.fallback.translate(content, content_type)

    def translate_file(self, filepath: Path, content_type: str) -> Optional[str]:
        """Translate a file to VERIX format."""
        if not filepath.exists():
            print(f"[error] File not found: {filepath}")
            return None

        content = filepath.read_text(encoding='utf-8', errors='ignore')

        # Check if already VERIX
        if '[define|neutral]' in content and 'VERILINGUA x VERIX' in content:
            print(f"[skipped] Already VERIX compliant: {filepath.name}")
            return content

        result = self.translate(content, content_type)
        return result.get('verix_content', '')


# ============================================================================
# BATCH PROCESSING
# ============================================================================

def process_batch(translator: VerixTranslator, content_type: str, directory: Path, dry_run: bool = True):
    """Process all files of a type in a directory."""
    if content_type == 'command':
        pattern = '**/*.md'
    elif content_type == 'skill':
        pattern = '**/SKILL.md'
    elif content_type == 'agent':
        pattern = '**/*.md'
    else:
        pattern = '**/*.md'

    files = list(directory.rglob(pattern))
    print(f"[assert|neutral] Found {len(files)} files to translate [ground:glob] [conf:1.0] [state:confirmed]")

    for f in files[:10]:  # Limit for testing
        print(f"\n[processing] {f.name}")
        result = translator.translate_file(f, content_type)
        if result:
            if dry_run:
                print(f"  [dry-run] Preview (first 200 chars):")
                print(f"  {result[:200]}...")
            else:
                # Backup and write
                backup_path = f.with_suffix('.md.backup')
                f.rename(backup_path)
                f.write_text(result, encoding='utf-8')
                print(f"  [success] Translated to VERIX")


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='DSPy-Enhanced VERIX Translator')
    parser.add_argument('--translate-command', type=str, help='Translate a command file')
    parser.add_argument('--translate-skill', type=str, help='Translate a skill file')
    parser.add_argument('--translate-agent', type=str, help='Translate an agent file')
    parser.add_argument('--batch-translate', nargs=2, metavar=('TYPE', 'DIR'), help='Batch translate files')
    parser.add_argument('--no-dspy', action='store_true', help='Force fallback translator')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    args = parser.parse_args()

    print("=" * 60)
    print("DSPy-Enhanced VERIX Translator v1.0.0")
    print("=" * 60)
    print()

    translator = VerixTranslator(use_dspy=not args.no_dspy)

    if args.translate_command:
        result = translator.translate_file(Path(args.translate_command), 'command')
        if result:
            print("\n[VERIX OUTPUT]:\n")
            print(result[:2000])

    elif args.translate_skill:
        result = translator.translate_file(Path(args.translate_skill), 'skill')
        if result:
            print("\n[VERIX OUTPUT]:\n")
            print(result[:2000])

    elif args.translate_agent:
        result = translator.translate_file(Path(args.translate_agent), 'agent')
        if result:
            print("\n[VERIX OUTPUT]:\n")
            print(result[:2000])

    elif args.batch_translate:
        content_type, directory = args.batch_translate
        process_batch(translator, content_type, Path(directory), dry_run=args.dry_run)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
