# Intent Analyzer - Quick Start Guide

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Advanced intent interpretation system that disambiguates user requests using cognitive science principles and probabilistic reasoning.

## When to Use
- Ambiguous or vague requests
- Complex multi-part instructions
- High-stakes decisions requiring clarity
- User may not know exactly what they need

## Quick Start

```bash
# Run intent analyzer skill
npx claude-flow@alpha skill-run intent-analyzer \
  --input "user-request.txt" \
  --output "/tmp/intent-brief.json"
```

## 5-Phase Process

1. **Capture Input** (2 min) - Gather request and context
2. **Decompose Intent** (5 min) - Break into components
3. **Map Probabilities** (5 min) - Rank interpretations
4. **Clarify Ambiguities** (10 min) - Ask targeted questions
5. **Synthesize Understanding** (8 min) - Create action plan

## Expected Output

```json
{
  "userIntent": {
    "original": "Create an API with security",
    "interpreted": "Build REST API with JWT authentication",
    "confidence": 0.87
  },
  "actionPlan": {
    "phases": ["Design schema", "Implement endpoints", "Add auth", "Test"],
    "agents": ["backend-dev", "security-reviewer", "tester"],
    "estimatedDuration": "4-6 hours"
  }
}
```

## Success Criteria
- [assert|neutral] Confidence score > 0.8 [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] User confirmation obtained [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Clear action plan generated [ground:acceptance-criteria] [conf:0.90] [state:provisional]
- [assert|neutral] Ready for execution handoff [ground:acceptance-criteria] [conf:0.90] [state:provisional]

## Common Use Cases
- **Before SPARC**: Clarify requirements before specification phase
- **Before Development**: Ensure clear understanding before coding
- **User Onboarding**: Help users articulate what they need

## Integration
```bash
# With SPARC
intent-analyzer → SPARC spec-pseudocode → implementation

# With Feature Development
intent-analyzer → feature-dev-complete

# Standalone
intent-analyzer → manual execution
```

## Tips
- Provide as much context as possible
- Answer clarifying questions thoughtfully
- Review interpretation before confirming
- Update if understanding changes

For detailed documentation, see SKILL.md


---
*Promise: `<promise>README_VERIX_COMPLIANT</promise>`*
