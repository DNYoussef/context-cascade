#!/usr/bin/env python3
"""
build-skill-index.py - Build searchable skill index from packaged .skill files

v3.0.0: Updated to scan skills/packaged/ directory for .skill ZIP archives.
Extracts SKILL.md content from inside each ZIP archive.

Features:
- Scans skills/packaged/*.skill files (ZIP archives containing skill folders)
- Extracts SKILL.md content from ZIP archives using zipfile module
- Backward compatible with supplementary skills in ~/.claude/skills/
- Packaged skills take precedence over supplementary skills with same name
- Properly extracts TRIGGER_POSITIVE patterns for auto-routing

Usage:
    python build-skill-index.py [--output skill-index.json] [--verbose]
"""

import json
import os
import re
import sys
import zipfile
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Configuration

# ============================================================
# LIBRARY-FIRST PROTOCOL
# ============================================================
# Before generating code, check:
#   1. .claude/library/catalog.json
#   2. .claude/docs/inventories/LIBRARY-PATTERNS-GUIDE.md
#   3. D:\Projects\* for existing implementations
#
# Decision: REUSE (>90%) | ADAPT (70-90%) | FOLLOW pattern | BUILD new
# ============================================================

PLUGIN_DIR = Path("C:/Users/17175/claude-code-plugins/context-cascade")
SKILLS_DIR = PLUGIN_DIR / "skills"
PACKAGED_SKILLS_DIR = SKILLS_DIR / "packaged"
SUPPLEMENTARY_SKILLS_DIR = Path("C:/Users/17175/.claude/skills")
DEFAULT_OUTPUT = PLUGIN_DIR / "scripts" / "skill-index" / "skill-index.json"

# Stopwords to filter from extracted keywords
STOPWORDS = {
    'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
    'may', 'might', 'must', 'shall', 'can', 'need', 'dare', 'ought', 'used',
    'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'from', 'as', 'into',
    'through', 'during', 'before', 'after', 'above', 'below', 'between',
    'and', 'or', 'but', 'if', 'then', 'else', 'when', 'where', 'why', 'how',
    'all', 'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    'just', 'also', 'now', 'here', 'there', 'this', 'that', 'these', 'those',
    'it', 'its', 'you', 'your', 'we', 'our', 'they', 'their', 'i', 'my',
    'use', 'using', 'used', 'skill', 'skills', 'agent', 'agents', 'task', 'tasks'
}

# Category-specific keywords for routing
CATEGORY_KEYWORDS = {
    'delivery': ['feature', 'implement', 'build', 'develop', 'create', 'add', 'new', 'frontend', 'backend', 'api', 'sparc', 'bug', 'fix', 'debug'],
    'quality': ['test', 'audit', 'review', 'verify', 'validate', 'check', 'quality', 'coverage', 'lint', 'style', 'code-review'],
    'security': ['security', 'auth', 'authentication', 'permission', 'vulnerability', 'pentest', 'compliance', 'encrypt', 'threat'],
    'research': ['research', 'find', 'discover', 'analyze', 'investigate', 'study', 'literature', 'paper', 'synthesis', 'survey'],
    'orchestration': ['coordinate', 'orchestrate', 'swarm', 'parallel', 'workflow', 'pipeline', 'cascade', 'hive', 'chain'],
    'operations': ['deploy', 'devops', 'cicd', 'infrastructure', 'docker', 'kubernetes', 'terraform', 'monitor', 'release', 'github'],
    'platforms': ['platform', 'database', 'ml', 'neural', 'flow', 'nexus', 'codex', 'gemini', 'multi-model', 'agentdb'],
    'foundry': ['create', 'agent', 'skill', 'template', 'forge', 'generator', 'builder', 'prompt', 'meta'],
    'specialists': ['business', 'finance', 'domain', 'expert', 'specialist', 'industry', 'legal', 'medical'],
    'tooling': ['documentation', 'docs', 'github', 'pr', 'issue', 'release', 'tool', 'integration']
}


@dataclass
class SkillData:
    """Represents extracted data from a SKILL.md file."""
    name: str
    path: str
    category: str
    description: str = ""
    triggers: List[str] = field(default_factory=list)
    negative_triggers: List[str] = field(default_factory=list)
    files: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    trigger_positive_raw: Optional[str] = None  # Raw TRIGGER_POSITIVE block

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "path": self.path,
            "category": self.category,
            "description": self.description[:200] if self.description else "",
            "triggers": self.triggers[:30],  # Cap at 30 triggers
            "negativeTriggers": self.negative_triggers[:15],
            "files": self.files,
            "tags": self.tags,
            "hasTriggerPositive": self.trigger_positive_raw is not None
        }


def find_skill_files(root_dir: Path) -> List[Path]:
    """Find all SKILL.md files recursively (for backward compatibility)."""
    skill_files = []
    for skill_path in root_dir.rglob("SKILL.md"):
        # Skip backup files
        if ".backup" in str(skill_path) or ".pre-" in str(skill_path):
            continue
        skill_files.append(skill_path)
    return skill_files


def find_packaged_skills(packaged_dir: Path) -> List[Path]:
    """Find all .skill files in the packaged directory."""
    if not packaged_dir.exists():
        return []
    return list(packaged_dir.glob("*.skill"))


def read_skill_md_from_archive(skill_archive: Path) -> Optional[Tuple[str, str]]:
    """
    Read SKILL.md content from a .skill ZIP archive.

    Returns:
        Tuple of (content, skill_name) or None if SKILL.md not found
    """
    try:
        with zipfile.ZipFile(skill_archive, 'r') as zf:
            # List all files in the archive
            namelist = zf.namelist()

            # Look for SKILL.md - it may be at root or in a subdirectory
            skill_md_path = None
            for name in namelist:
                if name.endswith('SKILL.md'):
                    skill_md_path = name
                    break

            if not skill_md_path:
                return None

            # Read the content
            content = zf.read(skill_md_path).decode('utf-8', errors='replace')

            # Extract skill name from the archive filename (without .skill extension)
            skill_name = skill_archive.stem

            return (content, skill_name)
    except (zipfile.BadZipFile, KeyError, IOError) as e:
        print(f"  Error reading {skill_archive}: {e}")
        return None


def get_supporting_files_from_archive(skill_archive: Path) -> List[str]:
    """Get list of supporting files from a .skill ZIP archive."""
    files = []
    try:
        with zipfile.ZipFile(skill_archive, 'r') as zf:
            for name in zf.namelist():
                # Get just the filename without path prefixes
                basename = Path(name).name
                if basename and basename.endswith('.md') and basename != 'SKILL.md':
                    files.append(basename)
                elif 'examples/' in name:
                    if 'examples/' not in files:
                        files.append('examples/')
    except (zipfile.BadZipFile, IOError):
        pass
    return files


def parse_yaml_frontmatter(content: str) -> Dict:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    yaml_text = match.group(1)
    result = {}

    # Simple YAML parsing for key: value pairs
    current_key = None
    current_values = []

    for line in yaml_text.split('\n'):
        # Key-value pair
        kv_match = re.match(r'^(\w[\w-]*)\s*:\s*(.*)$', line)
        if kv_match:
            # Save previous key
            if current_key:
                result[current_key] = current_values if len(current_values) > 1 else (current_values[0] if current_values else "")

            current_key = kv_match.group(1)
            value = kv_match.group(2).strip()

            # Check for list or special values
            if value.startswith('['):
                # Inline list: [item1, item2]
                items = re.findall(r'"([^"]+)"|\'([^\']+)\'|([^,\[\]]+)', value)
                current_values = [next(filter(None, item)).strip() for item in items if any(item)]
            elif value in ['|', '>']:
                current_values = []
            else:
                # Remove quotes
                value = value.strip('"\'')
                current_values = [value] if value else []
        # List item
        elif line.strip().startswith('-'):
            item = line.strip()[1:].strip().strip('"\'')
            if item:
                current_values.append(item)
        # Continuation
        elif line.startswith('  ') and current_key:
            current_values.append(line.strip())

    # Save last key
    if current_key:
        result[current_key] = current_values if len(current_values) > 1 else (current_values[0] if current_values else "")

    return result


def extract_trigger_positive(content: str) -> Optional[Dict]:
    """
    Extract TRIGGER_POSITIVE block from SKILL.md content.

    TRIGGER_POSITIVE format:
    [define|neutral] TRIGGER_POSITIVE := {
      keywords: ["keyword1", "keyword2"],
      context: "description"
    }
    """
    # Pattern to match TRIGGER_POSITIVE block
    patterns = [
        # VCL format: [define|neutral] TRIGGER_POSITIVE := { ... }
        r'\[define\|.*?\]\s*TRIGGER_POSITIVE\s*:=\s*\{([^}]+)\}',
        # Simple format: TRIGGER_POSITIVE: { ... }
        r'TRIGGER_POSITIVE\s*:\s*\{([^}]+)\}',
        # Markdown header format
        r'##\s*TRIGGER_POSITIVE\s*\n(.*?)(?=##|\Z)'
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            block = match.group(1)
            result = {"raw": match.group(0)}

            # Extract keywords array
            kw_match = re.search(r'keywords\s*:\s*\[(.*?)\]', block, re.DOTALL)
            if kw_match:
                # Parse array items
                items = re.findall(r'"([^"]+)"|\'([^\']+)\'', kw_match.group(1))
                result["keywords"] = [next(filter(None, item)) for item in items]

            # Extract context
            ctx_match = re.search(r'context\s*:\s*"([^"]+)"', block)
            if ctx_match:
                result["context"] = ctx_match.group(1)

            return result

    return None


def extract_section(content: str, section_name: str) -> str:
    """Extract content from a markdown section."""
    patterns = [
        rf'##\s*{re.escape(section_name)}[^\n]*\n(.*?)(?=##|\Z)',
        rf'###\s*{re.escape(section_name)}[^\n]*\n(.*?)(?=###|##|\Z)'
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return ""


def extract_keywords(text: str) -> List[str]:
    """Extract meaningful keywords from text."""
    if not text:
        return []

    # Convert to lowercase and extract words
    words = re.sub(r'[^a-z0-9\s-]', ' ', text.lower()).split()

    # Filter stopwords and short words
    filtered = [w for w in words if len(w) > 2 and w not in STOPWORDS]

    # Count occurrences
    counts: Dict[str, int] = {}
    for word in filtered:
        counts[word] = counts.get(word, 0) + 1

    # Return unique keywords sorted by frequency
    return sorted(counts.keys(), key=lambda w: counts[w], reverse=True)


def get_category_from_path(skill_path: Path, skills_dir: Path) -> str:
    """Determine category from file path."""
    try:
        rel_path = skill_path.relative_to(skills_dir)
        parts = rel_path.parts
        return parts[0] if parts else "unknown"
    except ValueError:
        return "unknown"


def get_supporting_files(skill_dir: Path) -> List[str]:
    """Get list of supporting files in the skill directory."""
    files = []
    try:
        for entry in skill_dir.iterdir():
            if entry.is_file() and entry.suffix == '.md':
                files.append(entry.name)
            elif entry.is_dir() and entry.name == 'examples':
                files.append('examples/')
    except PermissionError:
        pass
    return files


def process_skill_file(skill_path: Path, skills_dir: Path) -> Optional[SkillData]:
    """Process a single SKILL.md file and extract data."""
    try:
        content = skill_path.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        print(f"  Error reading {skill_path}: {e}")
        return None

    skill_dir = skill_path.parent
    category = get_category_from_path(skill_path, skills_dir)

    # Parse frontmatter
    frontmatter = parse_yaml_frontmatter(content)

    # Get skill name
    name = frontmatter.get('name', skill_dir.name)
    if isinstance(name, list):
        name = name[0] if name else skill_dir.name

    # Get description
    description = frontmatter.get('description', '')
    if isinstance(description, list):
        description = ' '.join(description)

    # Extract TRIGGER_POSITIVE block
    trigger_positive = extract_trigger_positive(content)

    # Collect trigger sources
    trigger_sources = [
        description,
        extract_section(content, 'When to Use'),
        extract_section(content, 'Purpose'),
    ]

    # Add TRIGGER_POSITIVE keywords if found
    if trigger_positive:
        if 'keywords' in trigger_positive:
            trigger_sources.extend(trigger_positive['keywords'])
        if 'context' in trigger_positive:
            trigger_sources.append(trigger_positive['context'])

    # Add tags from frontmatter
    tags = frontmatter.get('x-tags', [])
    if isinstance(tags, str):
        tags = [tags]
    trigger_sources.extend(tags)

    # Extract all triggers
    triggers = extract_keywords(' '.join(str(s) for s in trigger_sources))

    # Add explicit TRIGGER_POSITIVE keywords at the front
    if trigger_positive and 'keywords' in trigger_positive:
        explicit_kw = [k.lower() for k in trigger_positive['keywords']]
        triggers = explicit_kw + [t for t in triggers if t not in explicit_kw]

    # Extract negative triggers
    negative_sources = [
        extract_section(content, 'When NOT to Use'),
        extract_section(content, 'TRIGGER_NEGATIVE'),
        extract_section(content, 'Anti-Patterns')
    ]
    negative_triggers = extract_keywords(' '.join(negative_sources))

    # Get supporting files
    files = get_supporting_files(skill_dir)

    # Calculate relative path - prefer packaged skill files for efficient loading
    # Check if a corresponding .skill file exists in packaged directory
    packaged_file = PACKAGED_SKILLS_DIR / f"{name}.skill"
    if packaged_file.exists():
        rel_path = f"skills/packaged/{name}.skill"
    else:
        # Fall back to raw skill directory path
        try:
            rel_path = str(skill_dir.relative_to(PLUGIN_DIR)).replace('\\', '/') + '/'
        except ValueError:
            # Supplementary skill - use path relative to home/.claude/skills
            try:
                rel_path = '.claude/skills/' + str(skill_dir.relative_to(SUPPLEMENTARY_SKILLS_DIR)).replace('\\', '/') + '/'
            except ValueError:
                # Standalone file (not in a subdirectory)
                rel_path = '.claude/skills/' + skill_path.stem + '/'

    return SkillData(
        name=name,
        path=rel_path,
        category=category,
        description=description,
        triggers=triggers,
        negative_triggers=negative_triggers,
        files=files,
        tags=tags if isinstance(tags, list) else [tags],
        trigger_positive_raw=trigger_positive.get('raw') if trigger_positive else None
    )


def process_packaged_skill(skill_archive: Path) -> Optional[SkillData]:
    """Process a .skill ZIP archive and extract data."""
    result = read_skill_md_from_archive(skill_archive)
    if not result:
        return None

    content, archive_name = result

    # Parse frontmatter
    frontmatter = parse_yaml_frontmatter(content)

    # Get skill name - prefer frontmatter name, fallback to archive name
    name = frontmatter.get('name', archive_name)
    if isinstance(name, list):
        name = name[0] if name else archive_name

    # Get description
    description = frontmatter.get('description', '')
    if isinstance(description, list):
        description = ' '.join(description)

    # Try to determine category from frontmatter or archive name
    category = frontmatter.get('category', 'packaged')
    if isinstance(category, list):
        category = category[0] if category else 'packaged'

    # Extract TRIGGER_POSITIVE block
    trigger_positive = extract_trigger_positive(content)

    # Collect trigger sources
    trigger_sources = [
        description,
        extract_section(content, 'When to Use'),
        extract_section(content, 'Purpose'),
    ]

    # Add TRIGGER_POSITIVE keywords if found
    if trigger_positive:
        if 'keywords' in trigger_positive:
            trigger_sources.extend(trigger_positive['keywords'])
        if 'context' in trigger_positive:
            trigger_sources.append(trigger_positive['context'])

    # Add tags from frontmatter
    tags = frontmatter.get('x-tags', [])
    if isinstance(tags, str):
        tags = [tags]
    trigger_sources.extend(tags)

    # Extract all triggers
    triggers = extract_keywords(' '.join(str(s) for s in trigger_sources))

    # Add explicit TRIGGER_POSITIVE keywords at the front
    if trigger_positive and 'keywords' in trigger_positive:
        explicit_kw = [k.lower() for k in trigger_positive['keywords']]
        triggers = explicit_kw + [t for t in triggers if t not in explicit_kw]

    # Extract negative triggers
    negative_sources = [
        extract_section(content, 'When NOT to Use'),
        extract_section(content, 'TRIGGER_NEGATIVE'),
        extract_section(content, 'Anti-Patterns')
    ]
    negative_triggers = extract_keywords(' '.join(negative_sources))

    # Get supporting files from archive
    files = get_supporting_files_from_archive(skill_archive)

    # Path format: skills/packaged/{name}.skill
    rel_path = f"skills/packaged/{skill_archive.name}"

    return SkillData(
        name=name,
        path=rel_path,
        category=category,
        description=description,
        triggers=triggers,
        negative_triggers=negative_triggers,
        files=files,
        tags=tags if isinstance(tags, list) else [tags],
        trigger_positive_raw=trigger_positive.get('raw') if trigger_positive else None
    )


def build_keyword_index(skills: Dict[str, dict]) -> Dict[str, List[str]]:
    """Build inverted index: keyword -> [skill names]."""
    index: Dict[str, List[str]] = {}

    for name, skill in skills.items():
        for keyword in skill.get('triggers', []):
            if keyword not in index:
                index[keyword] = []
            if name not in index[keyword]:
                index[keyword].append(name)

    # Sort by specificity (fewer skills = more specific keyword)
    return dict(sorted(index.items(), key=lambda x: len(x[1])))


def build_category_index(skills: Dict[str, dict]) -> Dict[str, dict]:
    """Build category index with skill lists."""
    categories: Dict[str, dict] = {}

    for name, skill in skills.items():
        cat = skill.get('category', 'unknown')
        if cat not in categories:
            categories[cat] = {
                'description': '',
                'skills': [],
                'keywords': CATEGORY_KEYWORDS.get(cat, [])
            }
        categories[cat]['skills'].append(name)

    return categories


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Build skill index from SKILL.md files')
    parser.add_argument('--output', '-o', type=str, default=str(DEFAULT_OUTPUT),
                        help='Output JSON file path')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Verbose output')
    args = parser.parse_args()

    output_path = Path(args.output)

    print(f"Building skill index...")
    print(f"Packaged skills directory: {PACKAGED_SKILLS_DIR}")
    print(f"Supplementary directory: {SUPPLEMENTARY_SKILLS_DIR}")
    print(f"Output: {output_path}")

    # Process each skill
    skills: Dict[str, dict] = {}
    trigger_positive_count = 0
    supplementary_count = 0
    packaged_count = 0

    # Find and process packaged .skill files (primary source)
    packaged_skill_files = find_packaged_skills(PACKAGED_SKILLS_DIR)
    print(f"\nFound {len(packaged_skill_files)} packaged .skill files")

    for skill_archive in packaged_skill_files:
        skill_data = process_packaged_skill(skill_archive)
        if skill_data:
            skill_data.tags.append("packaged")
            packaged_count += 1
            skills[skill_data.name] = skill_data.to_dict()
            if skill_data.trigger_positive_raw:
                trigger_positive_count += 1
                if args.verbose:
                    print(f"  [TRIGGER+] {skill_data.name}")

    print(f"Processed {packaged_count} packaged skills")

    # Find supplementary skills (backward compatibility for ~/.claude/skills/)
    supplementary_files = []
    if SUPPLEMENTARY_SKILLS_DIR.exists():
        # Find SKILL.md files in subdirectories
        supplementary_files.extend(find_skill_files(SUPPLEMENTARY_SKILLS_DIR))
        # Also find standalone skill .md files (like codex-auto.md, gemini-search.md)
        for md_file in SUPPLEMENTARY_SKILLS_DIR.glob("*.md"):
            if md_file.name not in ['README.md', 'CHANGELOG.md', 'MASTER-SKILLS-INDEX.md']:
                supplementary_files.append(md_file)
        print(f"Found {len(supplementary_files)} supplementary skill files")

    # Process supplementary skills
    for skill_path in supplementary_files:
        skill_data = process_skill_file(skill_path, SUPPLEMENTARY_SKILLS_DIR)
        if skill_data:
            # Mark supplementary skills
            skill_data.tags.append("supplementary")
            supplementary_count += 1
            # Only add if not already present from packaged skills (packaged takes precedence)
            if skill_data.name not in skills:
                skills[skill_data.name] = skill_data.to_dict()
                if skill_data.trigger_positive_raw:
                    trigger_positive_count += 1
                    if args.verbose:
                        print(f"  [TRIGGER+] {skill_data.name}")
            elif args.verbose:
                print(f"  [SKIP] {skill_data.name} (already in packaged)")

    print(f"Processed {len(skills)} total skills (packaged: {packaged_count}, supplementary: {supplementary_count})")
    print(f"Skills with TRIGGER_POSITIVE: {trigger_positive_count}")

    # Build indices
    keyword_index = build_keyword_index(skills)
    categories = build_category_index(skills)

    # Build final index
    index = {
        'version': '3.0.0',  # Bumped version for packaged skills support
        'generated': datetime.now(tz=None).astimezone().isoformat(),
        'generator': 'build-skill-index.py',
        'total_skills': len(skills),
        'packaged_skills': packaged_count,
        'supplementary_skills': supplementary_count,
        'skills_with_trigger_positive': trigger_positive_count,
        'categories': categories,
        'skills': skills,
        'keyword_index': keyword_index,
        'category_keywords': CATEGORY_KEYWORDS
    }

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)

    print(f"\nIndex written to {output_path}")

    # Print summary
    print("\n=== Summary ===")
    print(f"Total skills: {index['total_skills']} (packaged: {index['packaged_skills']}, supplementary: {index['supplementary_skills']})")
    print(f"With TRIGGER_POSITIVE: {trigger_positive_count}")
    print(f"Categories: {len(categories)}")
    print(f"Keywords indexed: {len(keyword_index)}")

    print("\nSkills per category:")
    for cat, data in sorted(categories.items(), key=lambda x: len(x[1]['skills']), reverse=True):
        print(f"  {cat}: {len(data['skills'])}")


if __name__ == "__main__":
    main()
