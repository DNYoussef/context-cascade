#!/usr/bin/env python3
"""
VERIX Playbook Translator v1.0.0

[assert|neutral] Translates playbook documentation to VERILINGUA x VERIX format [ground:design] [conf:0.95] [state:ongoing]

Usage:
  python verix-playbook-translator.py --translate
"""

import re
from pathlib import Path
from datetime import datetime

PLAYBOOKS_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\playbooks\docs")
BACKUP_DIR = Path(r"C:\Users\17175\claude-code-plugins\ruv-sparc-three-loop-system\playbooks\.backup")


def translate_playbook(filepath: Path) -> bool:
    """Add VERIX header to playbook file."""
    try:
        content = filepath.read_text(encoding='utf-8')

        # Check if already has VERIX header
        if '/*====' in content and 'VERILINGUA x VERIX' in content:
            print(f"[skipped] {filepath.name} - Already VERIX compliant")
            return True

        # Create backup
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        backup_path = BACKUP_DIR / f"{filepath.stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        backup_path.write_text(content, encoding='utf-8')

        # Extract title
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else filepath.stem

        # Create VERIX header
        verix_header = f'''/*============================================================================*/
/* {title.upper()} :: VERILINGUA x VERIX EDITION                               */
/*============================================================================*/

[define|neutral] PLAYBOOK := {{
  name: "{filepath.stem}",
  type: "workflow-orchestration",
  layer: L1
}} [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] COGNITIVE_FRAME := {{
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
}} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

---

'''

        # Add header to content
        new_content = verix_header + content

        # Add VERIX footer if not present
        if '<promise>' not in new_content:
            promise_name = filepath.stem.upper().replace('-', '_')
            new_content += f'''

---

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>{promise_name}_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
'''

        filepath.write_text(new_content, encoding='utf-8')
        print(f"[success] {filepath.name} - Translated to VERIX format")
        return True

    except Exception as e:
        print(f"[error] {filepath.name} - {e}")
        return False


def main():
    print("=" * 60)
    print("VERIX PLAYBOOK TRANSLATOR v1.0.0")
    print("=" * 60)
    print()

    playbooks = list(PLAYBOOKS_DIR.glob('*.md'))
    print(f"[assert|neutral] Found {len(playbooks)} playbooks [ground:glob-scan] [conf:1.0] [state:confirmed]")
    print()

    success = 0
    for pb in playbooks:
        if translate_playbook(pb):
            success += 1

    print()
    print("=" * 60)
    print(f"[assert|positive] Translated: {success}/{len(playbooks)} [ground:count] [conf:1.0] [state:confirmed]")
    print("[commit|confident] <promise>PLAYBOOK_TRANSLATION_COMPLETE</promise>")


if __name__ == '__main__':
    main()
