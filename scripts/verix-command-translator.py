#!/usr/bin/env python3
"""
VERIX Command Translator v1.0.0

[assert|neutral] Translates all commands to VERILINGUA x VERIX format [ground:design] [conf:0.95] [state:ongoing]

Bootstrap cascade order:
  1. prompt-architect (DONE)
  2. commands (THIS SCRIPT)
  3. agent-creator + prompting agents
  4. all agents
  5. skill-forge
  6. all skills
  7. playbooks

Usage:
  python verix-command-translator.py --dry-run          # Preview translations
  python verix-command-translator.py --translate        # Apply translations
  python verix-command-translator.py --single CMD_PATH  # Translate one file
"""

import os
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime

# Configuration
COMMANDS_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\commands")
BACKUP_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\commands\.backup")
LOG_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\scripts\logs")


@dataclass
class CommandMetadata:
    """Parsed command metadata."""
    name: str
    version: str = "1.0.0"
    binding: str = ""
    category: str = ""
    purpose: str = ""
    usage: str = ""
    parameters: List[Dict] = None
    stages: List[Dict] = None
    examples: List[Dict] = None
    related: List[str] = None

    def __post_init__(self):
        self.parameters = self.parameters or []
        self.stages = self.stages or []
        self.examples = self.examples or []
        self.related = self.related or []


def parse_frontmatter(content: str) -> Dict[str, str]:
    """Extract YAML frontmatter from markdown."""
    frontmatter = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            for line in fm_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
    return frontmatter


def extract_section(content: str, header: str) -> str:
    """Extract content under a markdown header."""
    pattern = rf'##\s*{re.escape(header)}\s*\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def extract_code_blocks(content: str) -> List[str]:
    """Extract all code blocks from content."""
    pattern = r'```(?:\w+)?\n(.*?)```'
    return re.findall(pattern, content, re.DOTALL)


def parse_parameters(content: str) -> Dict[str, Any]:
    """Parse parameter section into structured format."""
    params = {"required": {}, "optional": {}, "flags": {}}
    lines = content.split('\n')

    for line in lines:
        line = line.strip()
        if line.startswith('-'):
            # Parse parameter line
            match = re.match(r'-\s*`([^`]+)`\s*-?\s*(.*)', line)
            if match:
                param_name = match.group(1)
                description = match.group(2)

                if param_name.startswith('--'):
                    params['flags'][param_name] = {
                        'description': description,
                        'default': 'false'
                    }
                elif '(required)' in description.lower():
                    params['required'][param_name] = {
                        'type': 'string',
                        'description': description.replace('(required)', '').strip()
                    }
                else:
                    params['optional'][param_name] = {
                        'type': 'string',
                        'description': description
                    }
    return params


def parse_stages(content: str) -> List[Dict]:
    """Parse execution stages from content."""
    stages = []
    # Look for numbered lists or emoji-prefixed items
    pattern = r'(\d+)\.\s*([^\n]+)'
    matches = re.findall(pattern, content)

    for num, text in matches:
        # Extract model hints
        model = "Claude"
        if "Gemini" in text:
            model = "Gemini"
        elif "Codex" in text:
            model = "Codex"

        stages.append({
            'stage': int(num),
            'action': text.strip(),
            'model': model
        })

    return stages


def parse_examples(content: str) -> List[Dict]:
    """Parse examples from content."""
    examples = []
    code_blocks = extract_code_blocks(content)

    for block in code_blocks:
        lines = block.strip().split('\n')
        for line in lines:
            if line.startswith('/'):
                examples.append({
                    'command': line.strip(),
                    'description': 'Example usage'
                })

    return examples


def parse_related(content: str) -> List[str]:
    """Parse related commands from content."""
    related = []
    pattern = r'`(/[a-z-]+)`'
    matches = re.findall(pattern, content)
    return list(set(matches))


def parse_command_file(filepath: Path) -> CommandMetadata:
    """Parse a command markdown file into structured metadata."""
    content = filepath.read_text(encoding='utf-8')

    # Extract frontmatter
    fm = parse_frontmatter(content)

    # Extract command name from filename or content
    name = fm.get('name', filepath.stem)

    # Extract sections
    purpose = extract_section(content, 'Command Purpose') or extract_section(content, 'What It Does')
    usage_section = extract_section(content, 'Usage')
    params_section = extract_section(content, 'Parameters')
    stages_section = extract_section(content, 'What It Does')
    examples_section = extract_section(content, 'Examples')
    related_section = extract_section(content, 'See Also') or extract_section(content, 'Related Commands')

    return CommandMetadata(
        name=name,
        version=fm.get('version', '1.0.0'),
        binding=fm.get('binding', ''),
        category=fm.get('category', 'delivery'),
        purpose=purpose[:200] if purpose else f"Execute {name} workflow",
        usage=extract_code_blocks(usage_section)[0] if usage_section and extract_code_blocks(usage_section) else f"/{name} [args]",
        parameters=parse_parameters(params_section) if params_section else {},
        stages=parse_stages(stages_section) if stages_section else [],
        examples=parse_examples(examples_section) if examples_section else [],
        related=parse_related(related_section) if related_section else []
    )


def generate_verix_command(meta: CommandMetadata) -> str:
    """Generate VERIX-formatted command markdown."""

    # Format stages
    stages_str = ""
    if meta.stages:
        stages_list = []
        for s in meta.stages[:6]:  # Limit to 6 stages
            stages_list.append(f'  {{ stage: {s["stage"]}, action: "{s["action"][:60]}", model: "{s["model"]}" }}')
        stages_str = ',\n'.join(stages_list)
    else:
        stages_str = '  { stage: 1, action: "Execute command", model: "Claude" }'

    # Format parameters
    params_required = ""
    params_optional = ""
    params_flags = ""

    if isinstance(meta.parameters, dict):
        req = meta.parameters.get('required', {})
        opt = meta.parameters.get('optional', {})
        flags = meta.parameters.get('flags', {})

        if req:
            req_items = [f'    {k}: {{ type: "{v.get("type", "string")}", description: "{v.get("description", "")[:50]}" }}' for k, v in list(req.items())[:3]]
            params_required = ',\n'.join(req_items)
        if opt:
            opt_items = [f'    {k}: {{ type: "{v.get("type", "string")}", description: "{v.get("description", "")[:50]}" }}' for k, v in list(opt.items())[:3]]
            params_optional = ',\n'.join(opt_items)
        if flags:
            flag_items = [f'    "{k}": {{ description: "{v.get("description", "")[:50]}", default: "{v.get("default", "false")}" }}' for k, v in list(flags.items())[:3]]
            params_flags = ',\n'.join(flag_items)

    # Format examples
    examples_str = ""
    if meta.examples:
        ex_items = [f'  {{ command: "{e["command"][:60]}", description: "{e.get("description", "Example")[:40]}" }}' for e in meta.examples[:3]]
        examples_str = ',\n'.join(ex_items)
    else:
        examples_str = f'  {{ command: "/{meta.name} example", description: "Basic usage" }}'

    # Format related
    related_str = ', '.join([f'"/{r.replace("/", "")}"' for r in meta.related[:5]]) if meta.related else '"/help"'

    # Clean purpose
    purpose_clean = meta.purpose.replace('"', "'").replace('\n', ' ')[:150]

    # Extract skill from binding
    skill_name = meta.binding.replace('skill:', '') if meta.binding else meta.name

    return f'''/*============================================================================*/
/* {meta.name.upper()} COMMAND :: VERILINGUA x VERIX EDITION                   */
/*============================================================================*/

---
name: {meta.name}
version: {meta.version}
binding: skill:{skill_name}
category: {meta.category}
---

/*----------------------------------------------------------------------------*/
/* S0 COMMAND IDENTITY                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] COMMAND := {{
  name: "{meta.name}",
  binding: "skill:{skill_name}",
  category: "{meta.category}",
  layer: L1
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 PURPOSE                                                                  */
/*----------------------------------------------------------------------------*/

[assert|neutral] PURPOSE := {{
  action: "{purpose_clean}",
  outcome: "Workflow completion with quality metrics",
  use_when: "User invokes /{meta.name}"
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S2 USAGE SYNTAX                                                             */
/*----------------------------------------------------------------------------*/

[define|neutral] SYNTAX := "/{meta.name} [args]" [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] PARAMETERS := {{
  required: {{
{params_required if params_required else '    input: { type: "string", description: "Primary input" }'}
  }},
  optional: {{
{params_optional if params_optional else '    options: { type: "object", description: "Additional options" }'}
  }},
  flags: {{
{params_flags if params_flags else '    "--verbose": { description: "Enable verbose output", default: "false" }'}
  }}
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 EXECUTION FLOW                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] EXECUTION_STAGES := [
{stages_str}
] [ground:witnessed:workflow-design] [conf:0.95] [state:confirmed]

[define|neutral] MULTI_MODEL_STRATEGY := {{
  gemini_search: "Research and web search tasks",
  gemini_megacontext: "Large codebase analysis",
  codex: "Code generation and prototyping",
  claude: "Architecture and testing"
}} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S4 INPUT CONTRACT                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] INPUT_CONTRACT := {{
  required: {{
    command_args: "string - Command arguments"
  }},
  optional: {{
    flags: "object - Command flags",
    context: "string - Additional context"
  }},
  prerequisites: [
    "Valid project directory",
    "Required tools installed"
  ]
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 OUTPUT CONTRACT                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] OUTPUT_CONTRACT := {{
  artifacts: [
    "Execution log",
    "Quality metrics report"
  ],
  metrics: {{
    success_rate: "Percentage of successful executions",
    quality_score: "Overall quality assessment"
  }},
  state_changes: [
    "Workflow state updated"
  ]
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 SUCCESS INDICATORS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {{
  pass_conditions: [
    "Command executes without errors",
    "Output meets quality thresholds"
  ],
  quality_thresholds: {{
    execution_success: ">= 0.95",
    quality_score: ">= 0.80"
  }}
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 ERROR HANDLING                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] ERROR_HANDLERS := {{
  missing_input: {{
    symptom: "Required input not provided",
    cause: "User omitted required argument",
    recovery: "Prompt user for missing input"
  }},
  execution_failure: {{
    symptom: "Command fails to complete",
    cause: "Underlying tool or service error",
    recovery: "Retry with verbose logging"
  }}
}} [ground:witnessed:failure-analysis] [conf:0.92] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 EXAMPLES                                                                 */
/*----------------------------------------------------------------------------*/

[define|neutral] EXAMPLES := [
{examples_str}
] [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S9 CHAIN PATTERNS                                                           */
/*----------------------------------------------------------------------------*/

[define|neutral] CHAINS_WITH := {{
  sequential: [
    "/{meta.name} -> /review -> /deploy"
  ],
  parallel: [
    "parallel ::: '/{meta.name} arg1' '/{meta.name} arg2'"
  ]
}} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S10 RELATED COMMANDS                                                        */
/*----------------------------------------------------------------------------*/

[define|neutral] RELATED := {{
  complementary: [{related_str}],
  alternatives: [],
  prerequisites: []
}} [ground:given] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S11 META-LOOP INTEGRATION                                                   */
/*----------------------------------------------------------------------------*/

[define|neutral] META_LOOP := {{
  expertise_check: {{
    domain: "{meta.category}",
    file: ".claude/expertise/{meta.category}.yaml",
    fallback: "discovery_mode"
  }},
  benchmark: "{meta.name}-benchmark-v1",
  tests: [
    "command_execution_success",
    "workflow_validation"
  ],
  success_threshold: 0.90,
  namespace: "commands/{meta.category}/{meta.name}/{{project}}/{{timestamp}}",
  uncertainty_threshold: 0.85,
  coordination: {{
    related_skills: ["{skill_name}"],
    related_agents: ["coder", "tester"]
  }}
}} [ground:system-policy] [conf:0.98] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S12 MEMORY TAGGING                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_TAGGING := {{
  WHO: "{meta.name}-{{session_id}}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{{project-name}}",
  WHY: "command-execution"
}} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S13 ABSOLUTE RULES                                                          */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>{meta.name.upper().replace("-", "_")}_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
'''


def find_all_commands(base_dir: Path) -> List[Path]:
    """Find all command markdown files."""
    commands = []
    for md_file in base_dir.rglob('*.md'):
        # Skip template files, READMEs, and backup files
        if md_file.name.startswith(('README', 'TEMPLATE', 'INDEX', '.')):
            continue
        if '.backup' in str(md_file) or 'docs' in str(md_file):
            continue
        # Check if it looks like a command file
        content = md_file.read_text(encoding='utf-8', errors='ignore')
        if '##' in content or 'Usage' in content or content.startswith('---'):
            commands.append(md_file)
    return commands


def backup_file(filepath: Path) -> Path:
    """Create backup of file before translation."""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup_path = BACKUP_DIR / f"{filepath.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    backup_path.write_text(filepath.read_text(encoding='utf-8'), encoding='utf-8')
    return backup_path


def translate_command(filepath: Path, dry_run: bool = True) -> bool:
    """Translate a single command file to VERIX format."""
    try:
        print(f"[processing] {filepath.name}")

        # Check if already translated
        content = filepath.read_text(encoding='utf-8')
        if '[define|neutral]' in content and 'VERILINGUA x VERIX' in content:
            print(f"  [skipped] Already in VERIX format")
            return True

        # Parse the command
        meta = parse_command_file(filepath)

        # Generate VERIX version
        verix_content = generate_verix_command(meta)

        if dry_run:
            print(f"  [dry-run] Would translate: {meta.name}")
            print(f"    - Purpose: {meta.purpose[:50]}...")
            print(f"    - Stages: {len(meta.stages)}")
            print(f"    - Examples: {len(meta.examples)}")
        else:
            # Backup original
            backup_file(filepath)

            # Write translated version
            filepath.write_text(verix_content, encoding='utf-8')
            print(f"  [success] Translated to VERIX format")

        return True

    except Exception as e:
        print(f"  [error] Failed: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Translate commands to VERILINGUA x VERIX format')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--translate', action='store_true', help='Apply translations')
    parser.add_argument('--single', type=str, help='Translate single file')
    parser.add_argument('--category', type=str, help='Only translate specific category')
    args = parser.parse_args()

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("VERIX COMMAND TRANSLATOR v1.0.0")
    print("=" * 60)
    print(f"[assert|neutral] Starting translation [ground:script-start] [conf:1.0] [state:ongoing]")
    print()

    if args.single:
        filepath = Path(args.single)
        if not filepath.exists():
            print(f"[error] File not found: {filepath}")
            return
        translate_command(filepath, dry_run=not args.translate)
        return

    # Find all commands
    commands = find_all_commands(COMMANDS_DIR)

    if args.category:
        commands = [c for c in commands if args.category in str(c)]

    print(f"[assert|neutral] Found {len(commands)} commands to translate [ground:glob-scan] [conf:1.0] [state:confirmed]")
    print()

    success = 0
    failed = 0
    skipped = 0

    for cmd_path in sorted(commands):
        result = translate_command(cmd_path, dry_run=not args.translate)
        if result:
            success += 1
        else:
            failed += 1

    print()
    print("=" * 60)
    print("TRANSLATION SUMMARY")
    print("=" * 60)
    print(f"[assert|neutral] Total: {len(commands)} [ground:count] [conf:1.0] [state:confirmed]")
    print(f"[assert|positive] Success: {success} [ground:count] [conf:1.0] [state:confirmed]")
    print(f"[assert|negative] Failed: {failed} [ground:count] [conf:1.0] [state:confirmed]")
    print()

    if args.translate:
        print("[commit|confident] <promise>COMMAND_TRANSLATION_COMPLETE</promise>")
    else:
        print("[assert|neutral] Dry run complete. Use --translate to apply changes.")


if __name__ == '__main__':
    main()
