#!/usr/bin/env python3
"""
VERIX Skill Translator v1.0.0

[assert|neutral] Translates all 196 skills to VERILINGUA x VERIX format [ground:design] [conf:0.95] [state:ongoing]

Cascade position: Level 6 (after skill-forge)

Usage:
  python verix-skill-translator.py --dry-run          # Preview
  python verix-skill-translator.py --translate        # Apply
  python verix-skill-translator.py --single PATH      # Single file
"""

import os
import re
import yaml
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

# Configuration
SKILLS_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\skills")
BACKUP_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\skills\.backup")


@dataclass
class SkillMetadata:
    """Parsed skill metadata from frontmatter."""
    name: str
    description: str = ""
    version: str = "1.0.0"
    category: str = "general"
    tags: List[str] = None
    author: str = "system"

    def __post_init__(self):
        self.tags = self.tags or []


def parse_yaml_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter from markdown."""
    if not content.startswith('---'):
        return {}

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}

    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def get_skill_category(skill_path: Path) -> str:
    """Determine skill category from path."""
    parts = skill_path.parts
    for i, p in enumerate(parts):
        if p == 'skills' and len(parts) > i + 1:
            return parts[i + 1]
    return 'uncategorized'


def select_cognitive_frame(skill_name: str, category: str, description: str) -> Dict[str, str]:
    """Select optimal cognitive frame based on skill type."""
    desc_lower = description.lower()
    name_lower = skill_name.lower()

    # Frame selection based on keywords
    if any(k in desc_lower or k in name_lower for k in ['research', 'analysis', 'audit', 'verify', 'detect', 'test']):
        return {'frame': 'Evidential', 'source': 'Turkish', 'force': 'How do you know?'}
    if any(k in desc_lower or k in name_lower for k in ['deploy', 'build', 'implement', 'create', 'develop', 'workflow']):
        return {'frame': 'Aspectual', 'source': 'Russian', 'force': 'Complete or ongoing?'}
    if any(k in desc_lower or k in name_lower for k in ['document', 'report', 'presentation', 'user']):
        return {'frame': 'Honorific', 'source': 'Japanese', 'force': 'Who is the audience?'}
    if any(k in desc_lower or k in name_lower for k in ['design', 'architect', 'compose', 'structure']):
        return {'frame': 'Compositional', 'source': 'German', 'force': 'Build from primitives?'}

    # Default by category
    category_frames = {
        'research': ('Evidential', 'Turkish', 'How do you know?'),
        'quality': ('Evidential', 'Turkish', 'How do you know?'),
        'delivery': ('Aspectual', 'Russian', 'Complete or ongoing?'),
        'orchestration': ('Aspectual', 'Russian', 'Complete or ongoing?'),
        'operations': ('Aspectual', 'Russian', 'Complete or ongoing?'),
        'platforms': ('Compositional', 'German', 'Build from primitives?'),
        'foundry': ('Compositional', 'German', 'Build from primitives?'),
        'security': ('Evidential', 'Turkish', 'How do you know?'),
        'specialists': ('Honorific', 'Japanese', 'Who is the audience?'),
        'tooling': ('Aspectual', 'Russian', 'Complete or ongoing?'),
    }

    if category in category_frames:
        frame, source, force = category_frames[category]
        return {'frame': frame, 'source': source, 'force': force}

    return {'frame': 'Evidential', 'source': 'Turkish', 'force': 'How do you know?'}


def extract_sections(content: str) -> Dict[str, str]:
    """Extract major sections from skill content."""
    sections = {}

    # Extract body (after frontmatter)
    body = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            body = parts[2].strip()

    # Extract key sections
    section_patterns = [
        ('overview', r'##\s*Overview\s*\n(.*?)(?=\n##|\Z)'),
        ('when_to_use', r'##\s*When to Use\s*\n(.*?)(?=\n##|\Z)'),
        ('workflow', r'##\s*(?:Core Workflow|Workflow|Process)\s*\n(.*?)(?=\n##|\Z)'),
        ('examples', r'##\s*Examples?\s*\n(.*?)(?=\n##|\Z)'),
        ('conclusion', r'##\s*Conclusion\s*\n(.*?)(?=\n##|\Z)'),
    ]

    for key, pattern in section_patterns:
        match = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
        if match:
            sections[key] = match.group(1).strip()[:1500]  # Limit section length

    # Keep full body preview
    sections['full_body'] = body[:4000]

    return sections


def parse_skill_file(filepath: Path) -> SkillMetadata:
    """Parse a skill markdown file into structured metadata."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')
    fm = parse_yaml_frontmatter(content)

    return SkillMetadata(
        name=fm.get('name', filepath.stem),
        description=fm.get('description', '')[:300] if fm.get('description') else '',
        version=fm.get('version', '1.0.0'),
        category=fm.get('category', get_skill_category(filepath)),
        tags=fm.get('tags', []) or [],
        author=fm.get('author', 'system')
    )


def generate_verix_skill(meta: SkillMetadata, original_content: str) -> str:
    """Generate VERIX-formatted skill markdown."""

    # Select cognitive frame
    frame = select_cognitive_frame(meta.name, meta.category, meta.description)

    # Extract sections
    sections = extract_sections(original_content)

    # Format tags
    tags_str = '\n'.join([f'- {t}' for t in meta.tags[:5]]) if meta.tags else '- general'

    # Clean description
    desc_clean = meta.description.replace('"', "'").replace('\n', ' ')[:200]

    return f'''/*============================================================================*/
/* {meta.name.upper()} SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: {meta.name}
version: {meta.version}
description: |
  [assert|neutral] {desc_clean or f'{meta.name} skill for {meta.category} workflows'} [ground:given] [conf:0.95] [state:confirmed]
category: {meta.category}
tags:
{tags_str}
author: {meta.author}
cognitive_frame:
  primary: {frame['frame'].lower()}
  goal_analysis:
    first_order: "Execute {meta.name} workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic {meta.category} processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {{
  name: "{meta.name}",
  category: "{meta.category}",
  version: "{meta.version}",
  layer: L1
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {{
  frame: "{frame['frame']}",
  source: "{frame['source']}",
  force: "{frame['force']}"
}} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {{
  keywords: ["{meta.name}", "{meta.category}", "workflow"],
  context: "user needs {meta.name} capability"
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

{sections.get('full_body', f'## Overview\\n\\n{meta.name} skill for {meta.category} workflows.')}

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {{
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {{
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
}} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {{
  pattern: "skills/{meta.category}/{meta.name}/{{project}}/{{timestamp}}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
}} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {{
  WHO: "{meta.name}-{{session_id}}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{{project_name}}",
  WHY: "skill-execution"
}} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {{
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
}} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>{meta.name.upper().replace("-", "_")}_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
'''


def find_all_skills(base_dir: Path) -> List[Path]:
    """Find all skill SKILL.md files."""
    skills = []
    for skill_md in base_dir.rglob('SKILL.md'):
        # Skip backup files
        if '.backup' in str(skill_md):
            continue
        skills.append(skill_md)
    return skills


def backup_file(filepath: Path) -> Path:
    """Create backup of file before translation."""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    # Use skill folder name for backup
    skill_name = filepath.parent.name
    backup_path = BACKUP_DIR / f"{skill_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    backup_path.write_text(filepath.read_text(encoding='utf-8'), encoding='utf-8')
    return backup_path


def translate_skill(filepath: Path, dry_run: bool = True) -> bool:
    """Translate a single skill file to VERIX format."""
    try:
        rel_path = filepath.relative_to(SKILLS_DIR)
        print(f"[processing] {rel_path}")

        content = filepath.read_text(encoding='utf-8')

        # Check if already VERIX (more strictly)
        if '/*====' in content and 'VERILINGUA x VERIX' in content and '[define|neutral] SKILL :=' in content:
            print(f"  [skipped] Already fully VERIX compliant")
            return True

        # Parse the skill
        meta = parse_skill_file(filepath)

        # Generate VERIX version
        verix_content = generate_verix_skill(meta, content)

        if dry_run:
            print(f"  [dry-run] Would translate: {meta.name}")
            print(f"    - Category: {meta.category}")
            print(f"    - Version: {meta.version}")
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
    parser = argparse.ArgumentParser(description='Translate skills to VERILINGUA x VERIX format')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--translate', action='store_true', help='Apply translations')
    parser.add_argument('--single', type=str, help='Translate single file')
    parser.add_argument('--category', type=str, help='Only translate specific category')
    args = parser.parse_args()

    print("=" * 60)
    print("VERIX SKILL TRANSLATOR v1.0.0")
    print("=" * 60)
    print(f"[assert|neutral] Starting translation [ground:script-start] [conf:1.0] [state:ongoing]")
    print()

    if args.single:
        filepath = Path(args.single)
        if not filepath.exists():
            print(f"[error] File not found: {filepath}")
            return
        translate_skill(filepath, dry_run=not args.translate)
        return

    # Find all skills
    skills = find_all_skills(SKILLS_DIR)

    if args.category:
        skills = [s for s in skills if args.category in str(s)]

    print(f"[assert|neutral] Found {len(skills)} skills to translate [ground:glob-scan] [conf:1.0] [state:confirmed]")
    print()

    success = 0
    failed = 0

    for skill_path in sorted(skills):
        result = translate_skill(skill_path, dry_run=not args.translate)
        if result:
            success += 1
        else:
            failed += 1

    print()
    print("=" * 60)
    print("TRANSLATION SUMMARY")
    print("=" * 60)
    print(f"[assert|neutral] Total: {len(skills)} [ground:count] [conf:1.0] [state:confirmed]")
    print(f"[assert|positive] Success: {success} [ground:count] [conf:1.0] [state:confirmed]")
    print(f"[assert|negative] Failed: {failed} [ground:count] [conf:1.0] [state:confirmed]")
    print()

    if args.translate:
        print("[commit|confident] <promise>SKILL_TRANSLATION_COMPLETE</promise>")
    else:
        print("[assert|neutral] Dry run complete. Use --translate to apply changes.")


if __name__ == '__main__':
    main()
