#!/bin/bash
# Pre-commit hook: Validate cross-platform hook parity
# Fails commit if .ps1 files are missing .sh counterparts or vice versa

HOOKS_DIR="$(dirname "$0")/.."
ERRORS=0

echo "[pre-commit] Validating cross-platform hook parity..."

# Find all .ps1 files (excluding node_modules)
for ps1_file in $(find "$HOOKS_DIR" -name "*.ps1" -type f 2>/dev/null | grep -v node_modules); do
    sh_file="${ps1_file%.ps1}.sh"
    if [ ! -f "$sh_file" ]; then
        echo "  [ERROR] Missing: $(basename "$sh_file") (for $(basename "$ps1_file"))"
        ERRORS=$((ERRORS + 1))
    fi
done

# Find all .sh files (excluding node_modules and validation scripts)
for sh_file in $(find "$HOOKS_DIR" -name "*.sh" -type f 2>/dev/null | grep -v node_modules | grep -v validate-cross-platform); do
    ps1_file="${sh_file%.sh}.ps1"
    if [ ! -f "$ps1_file" ]; then
        echo "  [ERROR] Missing: $(basename "$ps1_file") (for $(basename "$sh_file"))"
        ERRORS=$((ERRORS + 1))
    fi
done

if [ $ERRORS -gt 0 ]; then
    echo ""
    echo "[pre-commit] BLOCKED: $ERRORS cross-platform counterparts missing"
    echo "             Create the missing files before committing"
    exit 1
fi

echo "[pre-commit] PASS: All hooks have cross-platform counterparts"
exit 0
