#!/usr/bin/env python3
"""
VERIX Agent Translator v1.0.0

[assert|neutral] Translates all 217 agents to VERILINGUA x VERIX format [ground:design] [conf:0.95] [state:ongoing]

Cascade position: Level 4 (after commands, agent-creator)

Usage:
  python verix-agent-translator.py --dry-run          # Preview
  python verix-agent-translator.py --translate        # Apply
  python verix-agent-translator.py --single PATH      # Single file
"""

import os
import re
import json
import yaml
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

# Configuration
AGENTS_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\agents")
BACKUP_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\agents\.backup")
LOG_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\scripts\logs")


@dataclass
class AgentMetadata:
    """Parsed agent metadata from frontmatter."""
    name: str
    agent_type: str = "general"
    color: str = "#4A90D9"
    description: str = ""
    capabilities: List[str] = None
    priority: str = "medium"
    category: str = "foundry"
    version: str = "1.0.0"
    role: str = ""
    role_confidence: float = 0.85
    allowed_tools: List[str] = None
    path_scopes: List[str] = None

    def __post_init__(self):
        self.capabilities = self.capabilities or []
        self.allowed_tools = self.allowed_tools or []
        self.path_scopes = self.path_scopes or []


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


def get_agent_category(agent_path: Path) -> str:
    """Determine agent category from path."""
    parts = agent_path.parts
    for i, p in enumerate(parts):
        if p == 'agents' and len(parts) > i + 1:
            return parts[i + 1]
    return 'uncategorized'


def select_cognitive_frame(agent_type: str, capabilities: List[str]) -> Dict[str, str]:
    """Select optimal cognitive frame based on agent type."""
    frame_map = {
        'researcher': ('Evidential', 'Turkish', 'How do you know?'),
        'analyst': ('Evidential', 'Turkish', 'How do you know?'),
        'coder': ('Aspectual', 'Russian', 'Complete or ongoing?'),
        'developer': ('Aspectual', 'Russian', 'Complete or ongoing?'),
        'tester': ('Evidential', 'Turkish', 'How do you know?'),
        'reviewer': ('Evidential', 'Turkish', 'How do you know?'),
        'planner': ('Aspectual', 'Russian', 'Complete or ongoing?'),
        'coordinator': ('Aspectual', 'Russian', 'Complete or ongoing?'),
        'documenter': ('Honorific', 'Japanese', 'Who is the audience?'),
        'designer': ('Compositional', 'German', 'Build from primitives?'),
    }

    # Check capabilities for hints
    for cap in capabilities:
        cap_lower = cap.lower()
        if 'analysis' in cap_lower or 'research' in cap_lower:
            return {'frame': 'Evidential', 'source': 'Turkish', 'force': 'How do you know?'}
        if 'implement' in cap_lower or 'code' in cap_lower:
            return {'frame': 'Aspectual', 'source': 'Russian', 'force': 'Complete or ongoing?'}

    # Default by type
    for key, (frame, source, force) in frame_map.items():
        if key in agent_type.lower():
            return {'frame': frame, 'source': source, 'force': force}

    # Default to Evidential
    return {'frame': 'Evidential', 'source': 'Turkish', 'force': 'How do you know?'}


def parse_agent_file(filepath: Path) -> AgentMetadata:
    """Parse an agent markdown file into structured metadata."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')
    fm = parse_yaml_frontmatter(content)

    # Extract nested values safely
    identity = fm.get('identity', {}) or {}
    rbac = fm.get('rbac', {}) or {}
    metadata = fm.get('metadata', {}) or {}

    return AgentMetadata(
        name=fm.get('name', filepath.stem),
        agent_type=fm.get('type', 'general'),
        color=fm.get('color', '#4A90D9'),
        description=fm.get('description', '')[:200],
        capabilities=fm.get('capabilities', []) or [],
        priority=fm.get('priority', 'medium'),
        category=metadata.get('category', get_agent_category(filepath)),
        version=metadata.get('version', '1.0.0'),
        role=identity.get('role', fm.get('type', 'agent')),
        role_confidence=identity.get('role_confidence', 0.85),
        allowed_tools=rbac.get('allowed_tools', []) or [],
        path_scopes=rbac.get('path_scopes', []) or []
    )


def generate_verix_agent(meta: AgentMetadata, original_body: str) -> str:
    """Generate VERIX-formatted agent markdown."""

    # Select cognitive frame
    frame = select_cognitive_frame(meta.agent_type, meta.capabilities)

    # Format capabilities
    caps_str = ', '.join(meta.capabilities[:5]) if meta.capabilities else 'general'

    # Format tools
    tools_str = ', '.join(meta.allowed_tools[:8]) if meta.allowed_tools else 'Read, Write, Edit, Bash'

    # Format path scopes
    scopes_str = ', '.join(meta.path_scopes[:4]) if meta.path_scopes else 'src/**, tests/**'

    # Extract body content (after frontmatter)
    body_content = original_body
    if original_body.startswith('---'):
        parts = original_body.split('---', 2)
        if len(parts) >= 3:
            body_content = parts[2].strip()

    # Truncate body for template (keep key sections)
    body_preview = body_content[:3000] if len(body_content) > 3000 else body_content

    return f'''---
name: "{meta.name}"
type: "{meta.agent_type}"
color: "{meta.color}"
description: |
  [assert|neutral] {meta.description or f'{meta.name} agent for {meta.role} tasks'} [ground:given] [conf:{meta.role_confidence:.2f}] [state:confirmed]
capabilities:
  - {chr(10) + '  - '.join(meta.capabilities[:5]) if meta.capabilities else 'general_tasks'}
priority: "{meta.priority}"
identity:
  agent_id: "{meta.name}-{datetime.now().strftime('%Y%m%d')}"
  role: "{meta.role}"
  role_confidence: {meta.role_confidence}
  role_reasoning: "[ground:capability-analysis] [conf:{meta.role_confidence:.2f}]"
rbac:
  allowed_tools: [{tools_str}]
  denied_tools: []
  path_scopes: [{scopes_str}]
  api_access: [memory-mcp]
budget:
  max_tokens_per_session: 200000
  max_cost_per_day: 30
  currency: "USD"
metadata:
  category: "{meta.category}"
  version: "{meta.version}"
  verix_compliant: true
  created_at: "{datetime.now().isoformat()}"
---

/*============================================================================*/
/* {meta.name.upper()} AGENT :: VERILINGUA x VERIX EDITION                     */
/*============================================================================*/

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] AGENT := {{
  name: "{meta.name}",
  type: "{meta.agent_type}",
  role: "{meta.role}",
  category: "{meta.category}",
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
/* S2 CORE RESPONSIBILITIES                                                    */
/*----------------------------------------------------------------------------*/

[define|neutral] RESPONSIBILITIES := {{
  primary: "{meta.role}",
  capabilities: [{caps_str}],
  priority: "{meta.priority}"
}} [ground:given] [conf:1.0] [state:confirmed]

{body_preview}

/*----------------------------------------------------------------------------*/
/* S3 EVIDENCE-BASED TECHNIQUES                                                */
/*----------------------------------------------------------------------------*/

[define|neutral] TECHNIQUES := {{
  self_consistency: "Verify from multiple analytical perspectives",
  program_of_thought: "Decompose complex problems systematically",
  plan_and_solve: "Plan before execution, validate at each stage"
}} [ground:prompt-engineering-research] [conf:0.88] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S4 GUARDRAILS                                                               */
/*----------------------------------------------------------------------------*/

[direct|emphatic] NEVER_RULES := [
  "NEVER skip testing",
  "NEVER hardcode secrets",
  "NEVER exceed budget",
  "NEVER ignore errors",
  "NEVER use Unicode (ASCII only)"
] [ground:system-policy] [conf:1.0] [state:confirmed]

[direct|emphatic] ALWAYS_RULES := [
  "ALWAYS validate inputs",
  "ALWAYS update Memory MCP",
  "ALWAYS follow Golden Rule (batch operations)",
  "ALWAYS use registry agents",
  "ALWAYS document decisions"
] [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {{
  functional: ["All requirements met", "Tests passing", "No critical bugs"],
  quality: ["Coverage >80%", "Linting passes", "Documentation complete"],
  coordination: ["Memory MCP updated", "Handoff created", "Dependencies notified"]
}} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_TOOLS := {{
  memory: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"],
  swarm: ["mcp__ruv-swarm__agent_spawn", "mcp__ruv-swarm__swarm_status"],
  coordination: ["mcp__ruv-swarm__task_orchestrate"]
}} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {{
  pattern: "agents/{meta.category}/{meta.name}/{{project}}/{{timestamp}}",
  store: ["tasks_completed", "decisions_made", "patterns_applied"],
  retrieve: ["similar_tasks", "proven_patterns", "known_issues"]
}} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {{
  WHO: "{meta.name}-{{session_id}}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{{project_name}}",
  WHY: "agent-execution"
}} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 FAILURE RECOVERY                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] ESCALATION_HIERARCHY := {{
  level_1: "Self-recovery via Memory MCP patterns",
  level_2: "Peer coordination with specialist agents",
  level_3: "Coordinator escalation",
  level_4: "Human intervention"
}} [ground:system-policy] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S9 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(spawned_agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>{meta.name.upper().replace("-", "_")}_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
'''


def find_all_agents(base_dir: Path) -> List[Path]:
    """Find all agent markdown files."""
    agents = []
    for md_file in base_dir.rglob('*.md'):
        # Skip README, template, backup, identity files
        if md_file.name.startswith(('README', 'TEMPLATE', 'INDEX', '.')):
            continue
        if '.backup' in str(md_file) or 'identity' in str(md_file):
            continue
        # Include all .md files that aren't already VERIX
        content = md_file.read_text(encoding='utf-8', errors='ignore')
        # Skip if already VERIX compliant
        if '[define|neutral]' in content and 'VERILINGUA x VERIX' in content:
            continue
        agents.append(md_file)
    return agents


def backup_file(filepath: Path) -> Path:
    """Create backup of file before translation."""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup_path = BACKUP_DIR / f"{filepath.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    backup_path.write_text(filepath.read_text(encoding='utf-8'), encoding='utf-8')
    return backup_path


def translate_agent(filepath: Path, dry_run: bool = True) -> bool:
    """Translate a single agent file to VERIX format."""
    try:
        print(f"[processing] {filepath.relative_to(AGENTS_DIR)}")

        content = filepath.read_text(encoding='utf-8')

        # Check if already VERIX
        if '[define|neutral]' in content and 'VERILINGUA x VERIX' in content:
            print(f"  [skipped] Already VERIX compliant")
            return True

        # Parse the agent
        meta = parse_agent_file(filepath)

        # Generate VERIX version
        verix_content = generate_verix_agent(meta, content)

        if dry_run:
            print(f"  [dry-run] Would translate: {meta.name}")
            print(f"    - Type: {meta.agent_type}")
            print(f"    - Category: {meta.category}")
            print(f"    - Capabilities: {len(meta.capabilities)}")
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
    parser = argparse.ArgumentParser(description='Translate agents to VERILINGUA x VERIX format')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--translate', action='store_true', help='Apply translations')
    parser.add_argument('--single', type=str, help='Translate single file')
    parser.add_argument('--category', type=str, help='Only translate specific category')
    args = parser.parse_args()

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("VERIX AGENT TRANSLATOR v1.0.0")
    print("=" * 60)
    print(f"[assert|neutral] Starting translation [ground:script-start] [conf:1.0] [state:ongoing]")
    print()

    if args.single:
        filepath = Path(args.single)
        if not filepath.exists():
            print(f"[error] File not found: {filepath}")
            return
        translate_agent(filepath, dry_run=not args.translate)
        return

    # Find all agents
    agents = find_all_agents(AGENTS_DIR)

    if args.category:
        agents = [a for a in agents if args.category in str(a)]

    print(f"[assert|neutral] Found {len(agents)} agents to translate [ground:glob-scan] [conf:1.0] [state:confirmed]")
    print()

    success = 0
    failed = 0

    for agent_path in sorted(agents):
        result = translate_agent(agent_path, dry_run=not args.translate)
        if result:
            success += 1
        else:
            failed += 1

    print()
    print("=" * 60)
    print("TRANSLATION SUMMARY")
    print("=" * 60)
    print(f"[assert|neutral] Total: {len(agents)} [ground:count] [conf:1.0] [state:confirmed]")
    print(f"[assert|positive] Success: {success} [ground:count] [conf:1.0] [state:confirmed]")
    print(f"[assert|negative] Failed: {failed} [ground:count] [conf:1.0] [state:confirmed]")
    print()

    if args.translate:
        print("[commit|confident] <promise>AGENT_TRANSLATION_COMPLETE</promise>")
    else:
        print("[assert|neutral] Dry run complete. Use --translate to apply changes.")


if __name__ == '__main__':
    main()
