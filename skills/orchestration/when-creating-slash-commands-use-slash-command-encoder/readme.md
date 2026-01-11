# Slash Command Encoder - Quick Start

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Create ergonomic slash commands for fast access to micro-skills.

## Quick Start

```bash
# 1. Design command
cat > command-schema.json <<EOF
{
  "name": "analyze",
  "description": "Analyze codebase",
  "parameters": [{"name": "path", "type": "string", "required": true}]
}
EOF

# 2. Generate handler
npx claude-flow@alpha command generate --schema command-schema.json

# 3. Test command
npx claude-flow@alpha command test --command analyze --input '{"path": "./src"}'

# 4. Deploy
npx claude-flow@alpha command install --from dist/commands.bundle.js
```

## Agents
- **coder:** Command implementation
- **base-template-generator:** Template generation

## Success Metrics
- [assert|neutral] Registration: <100ms [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Validation: <50ms [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Execution: <2s [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Promise: `<promise>README_VERIX_COMPLIANT</promise>`* [ground:acceptance-criteria] [conf:0.90] [state:provisional]
