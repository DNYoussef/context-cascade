#!/usr/bin/env python3
"""
SKILL PACKAGER v1.0.0

[assert|neutral] Packages skill folders into .skill.zip format [ground:design] [conf:0.95] [state:ongoing]

Purpose: Package each skill folder into a single zip file that FORCES Claude to read
all skill documentation as a cohesive unit when the skill is invoked.

Format:
  {skill-name}.skill.zip
    - SKILL.md (main definition in VERILINGUA x VERIX)
    - manifest.json (metadata for quick parsing)
    - examples/ (if present)
    - resources/ (if present)

Usage:
  python skill-packager.py --dry-run          # Preview packaging
  python skill-packager.py --package          # Create .skill.zip files
  python skill-packager.py --single SKILL_DIR # Package one skill
  python skill-packager.py --unpack SKILL_ZIP # Extract a skill
"""

import os
import re
import json
import zipfile
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any


# Configuration
SKILLS_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\skills")
OUTPUT_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\skills-packaged")
BACKUP_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\skills-backup")


@dataclass
class SkillManifest:
    """Manifest for packaged skill."""
    name: str
    version: str
    category: str
    description: str
    files: List[str]
    dependencies: List[str]
    triggers: List[str]
    layer: str = "L1"
    packaged_at: str = ""
    verix_compliant: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def parse_skill_md(filepath: Path) -> Dict[str, Any]:
    """Extract metadata from SKILL.md file."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')

    metadata = {
        'name': filepath.parent.name,
        'version': '1.0.0',
        'description': '',
        'dependencies': [],
        'triggers': []
    }

    # Extract from frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            for line in fm_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip().lower()
                    value = value.strip()
                    if key == 'name':
                        metadata['name'] = value
                    elif key == 'version':
                        metadata['version'] = value
                    elif key == 'description':
                        metadata['description'] = value[:200]

    # Check for VERIX compliance
    metadata['verix_compliant'] = '[define|neutral]' in content or '[assert|neutral]' in content

    # Extract trigger keywords
    if 'USE WHEN' in content or 'Trigger' in content:
        # Simple extraction of trigger keywords
        triggers = re.findall(r'"([^"]+)"', content[:2000])
        metadata['triggers'] = triggers[:10]

    # Extract dependencies (MCP, related skills)
    if 'MCP' in content:
        mcp_matches = re.findall(r'(\w+-mcp|\w+_mcp)', content, re.IGNORECASE)
        metadata['dependencies'] = list(set(mcp_matches))[:5]

    return metadata


def get_skill_category(skill_path: Path) -> str:
    """Determine skill category from path."""
    parts = skill_path.parts
    skills_idx = None
    for i, p in enumerate(parts):
        if p == 'skills':
            skills_idx = i
            break

    if skills_idx is not None and len(parts) > skills_idx + 1:
        return parts[skills_idx + 1]
    return 'uncategorized'


def find_all_skills(base_dir: Path) -> List[Path]:
    """Find all skill directories containing SKILL.md."""
    skills = []

    for skill_md in base_dir.rglob('SKILL.md'):
        skill_dir = skill_md.parent
        # Skip if in backup or packaged
        if '.backup' in str(skill_dir) or 'packaged' in str(skill_dir):
            continue
        skills.append(skill_dir)

    return sorted(skills)


def package_skill(skill_dir: Path, output_dir: Path, dry_run: bool = True) -> Optional[Path]:
    """Package a skill folder into .skill.zip format."""
    skill_name = skill_dir.name
    category = get_skill_category(skill_dir)

    print(f"[processing] {category}/{skill_name}")

    # Find SKILL.md
    skill_md = skill_dir / 'SKILL.md'
    if not skill_md.exists():
        print(f"  [error] No SKILL.md found")
        return None

    # Parse metadata
    metadata = parse_skill_md(skill_md)

    # Collect all files to package
    files_to_package = []
    for f in skill_dir.rglob('*'):
        if f.is_file() and '.backup' not in str(f):
            rel_path = f.relative_to(skill_dir)
            files_to_package.append((f, str(rel_path)))

    # Create manifest
    manifest = SkillManifest(
        name=metadata['name'],
        version=metadata['version'],
        category=category,
        description=metadata['description'],
        files=[fp[1] for fp in files_to_package],
        dependencies=metadata.get('dependencies', []),
        triggers=metadata.get('triggers', []),
        layer="L1",
        packaged_at=datetime.now().isoformat(),
        verix_compliant=metadata.get('verix_compliant', False)
    )

    # Output path
    category_dir = output_dir / category
    zip_path = category_dir / f"{skill_name}.skill.zip"

    if dry_run:
        print(f"  [dry-run] Would create: {zip_path.name}")
        print(f"    - Files: {len(files_to_package)}")
        print(f"    - Version: {manifest.version}")
        print(f"    - VERIX: {'Yes' if manifest.verix_compliant else 'No'}")
        return None

    # Create output directory
    category_dir.mkdir(parents=True, exist_ok=True)

    # Create zip file
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add manifest first
        manifest_json = json.dumps(manifest.to_dict(), indent=2)
        zf.writestr('manifest.json', manifest_json)

        # Add all files
        for file_path, rel_path in files_to_package:
            zf.write(file_path, rel_path)

    print(f"  [success] Created: {zip_path.name}")
    print(f"    - Size: {zip_path.stat().st_size / 1024:.1f} KB")

    return zip_path


def unpack_skill(zip_path: Path, output_dir: Path) -> Optional[Path]:
    """Unpack a .skill.zip file."""
    if not zip_path.exists():
        print(f"[error] File not found: {zip_path}")
        return None

    skill_name = zip_path.stem.replace('.skill', '')

    with zipfile.ZipFile(zip_path, 'r') as zf:
        # Read manifest
        if 'manifest.json' in zf.namelist():
            manifest_data = json.loads(zf.read('manifest.json'))
            category = manifest_data.get('category', 'uncategorized')
        else:
            category = 'uncategorized'

        # Extract to output directory
        extract_dir = output_dir / category / skill_name
        extract_dir.mkdir(parents=True, exist_ok=True)

        zf.extractall(extract_dir)
        print(f"[success] Unpacked to: {extract_dir}")

    return extract_dir


def create_skill_index(output_dir: Path) -> Path:
    """Create an index of all packaged skills."""
    index = {
        'generated_at': datetime.now().isoformat(),
        'format': 'skill.zip v1.0',
        'categories': {},
        'total': 0
    }

    for zip_file in output_dir.rglob('*.skill.zip'):
        category = zip_file.parent.name

        if category not in index['categories']:
            index['categories'][category] = []

        with zipfile.ZipFile(zip_file, 'r') as zf:
            if 'manifest.json' in zf.namelist():
                manifest = json.loads(zf.read('manifest.json'))
                index['categories'][category].append({
                    'name': manifest['name'],
                    'file': zip_file.name,
                    'version': manifest['version'],
                    'verix_compliant': manifest.get('verix_compliant', False),
                    'description': manifest.get('description', '')[:100]
                })
                index['total'] += 1

    # Write index
    index_path = output_dir / 'SKILLS-INDEX.json'
    index_path.write_text(json.dumps(index, indent=2), encoding='utf-8')

    # Also create markdown index
    md_index = f"""# Packaged Skills Index

[assert|neutral] Generated: {index['generated_at']} [ground:script-output] [conf:1.0] [state:confirmed]

## Summary

[define|neutral] SKILLS_INVENTORY := {{
  total: {index['total']},
  categories: {len(index['categories'])},
  format: "skill.zip v1.0"
}} [ground:counted] [conf:1.0] [state:confirmed]

## By Category

"""

    for category, skills in sorted(index['categories'].items()):
        md_index += f"### {category.title()} ({len(skills)} skills)\n\n"
        for skill in sorted(skills, key=lambda x: x['name']):
            verix = "[VERIX]" if skill['verix_compliant'] else ""
            md_index += f"- **{skill['name']}** {verix} - {skill['description'][:50]}\n"
        md_index += "\n"

    md_index += """
---

[commit|confident] <promise>SKILLS_INDEX_COMPLETE</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
"""

    md_index_path = output_dir / 'SKILLS-INDEX.md'
    md_index_path.write_text(md_index, encoding='utf-8')

    print(f"[success] Index created: {index_path.name}")
    return index_path


def main():
    parser = argparse.ArgumentParser(description='Package skills into .skill.zip format')
    parser.add_argument('--dry-run', action='store_true', help='Preview without creating zips')
    parser.add_argument('--package', action='store_true', help='Create .skill.zip files')
    parser.add_argument('--single', type=str, help='Package single skill directory')
    parser.add_argument('--unpack', type=str, help='Unpack a .skill.zip file')
    parser.add_argument('--category', type=str, help='Only package specific category')
    parser.add_argument('--index-only', action='store_true', help='Only regenerate index')
    args = parser.parse_args()

    print("=" * 60)
    print("SKILL PACKAGER v1.0.0")
    print("=" * 60)
    print(f"[assert|neutral] Starting packaging [ground:script-start] [conf:1.0] [state:ongoing]")
    print()

    if args.unpack:
        zip_path = Path(args.unpack)
        unpack_skill(zip_path, SKILLS_DIR)
        return

    if args.index_only:
        create_skill_index(OUTPUT_DIR)
        return

    if args.single:
        skill_dir = Path(args.single)
        if not skill_dir.exists():
            print(f"[error] Directory not found: {skill_dir}")
            return
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        package_skill(skill_dir, OUTPUT_DIR, dry_run=not args.package)
        return

    # Find all skills
    skills = find_all_skills(SKILLS_DIR)

    if args.category:
        skills = [s for s in skills if args.category in str(s)]

    print(f"[assert|neutral] Found {len(skills)} skills to package [ground:glob-scan] [conf:1.0] [state:confirmed]")
    print()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    success = 0
    failed = 0

    for skill_dir in skills:
        result = package_skill(skill_dir, OUTPUT_DIR, dry_run=not args.package)
        if result or (not args.package):  # Dry run counts as success
            success += 1
        else:
            failed += 1

    print()
    print("=" * 60)
    print("PACKAGING SUMMARY")
    print("=" * 60)
    print(f"[assert|neutral] Total: {len(skills)} [ground:count] [conf:1.0] [state:confirmed]")
    print(f"[assert|positive] Success: {success} [ground:count] [conf:1.0] [state:confirmed]")
    print(f"[assert|negative] Failed: {failed} [ground:count] [conf:1.0] [state:confirmed]")

    # Create index if actually packaging
    if args.package:
        print()
        create_skill_index(OUTPUT_DIR)
        print()
        print("[commit|confident] <promise>SKILL_PACKAGING_COMPLETE</promise>")
    else:
        print()
        print("[assert|neutral] Dry run complete. Use --package to create .skill.zip files.")


if __name__ == '__main__':
    main()
