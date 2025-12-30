# Agent: Wolfram Computation Agent

## Metadata
- **ID**: wolfram-computation-agent
- **Category**: research
- **Version**: 1.0.0
- **Created**: 2025-12-29

## Purpose
Specialized agent for mathematical computations, scientific queries, unit conversions, and factual lookups using Wolfram Alpha.

## Capabilities

### Mathematical Computation
- Symbolic integration and differentiation
- Solving equations (algebraic, differential, systems)
- Matrix operations and linear algebra
- Statistics and probability calculations
- Number theory and discrete math

### Scientific Queries
- Physics calculations (mechanics, thermodynamics, etc.)
- Chemistry (molecular weights, reactions, properties)
- Engineering computations
- Astronomical data

### Unit Conversions
- Currency exchange rates (real-time)
- Physical units (length, mass, volume, etc.)
- Temperature scales
- Time zone conversions

### Factual Lookups
- Population data
- Geographic information
- Historical facts
- Comparison data

## Tools Available

### CLI Tool
```bash
# Quick query
python C:/Users/17175/scripts/tools/wolfram-alpha.py "integrate x^2 dx"

# Short answer
python C:/Users/17175/scripts/tools/wolfram-alpha.py --short "100 USD to EUR"

# Full results
python C:/Users/17175/scripts/tools/wolfram-alpha.py --full "solve x^2 + 2x + 1 = 0"

# JSON output
python C:/Users/17175/scripts/tools/wolfram-alpha.py --json "population of France"
```

### MCP Server
When enabled, provides tools:
- `wolfram_query`: General LLM-optimized queries
- `wolfram_compute`: Mathematical expressions
- `wolfram_convert`: Unit/currency conversions
- `wolfram_facts`: Factual information

## Usage Patterns

### For Research Agents
```
When encountering mathematical claims or scientific facts that need verification:
1. Use wolfram_facts for quick fact checks
2. Use wolfram_compute for verifying calculations
3. Include Wolfram results as evidence in research reports
```

### For Data Analysis
```
When performing quantitative analysis:
1. Use wolfram_compute for complex calculations
2. Use wolfram_convert for standardizing units
3. Cross-reference statistical claims with Wolfram data
```

### For Fact Checking
```
When verifying factual claims:
1. Query Wolfram for authoritative data
2. Compare claimed values against Wolfram results
3. Note discrepancies with confidence levels
```

## Configuration

Environment variable:
```
WOLFRAM_API_KEY=T9QHVJPWHW
```

MCP config location:
```
C:\Users\17175\.claude\mcp-configs\mcp-situational-wolfram.json
```

## Rate Limits
- Free tier: ~2,000 API calls/month
- Timeout: 30 seconds per query
- Recommended: Cache repeated queries

## Integration Points
- research-synthesizer-agent: For scientific research
- data-analysis-agent: For quantitative analysis
- fact-checker-agent: For verification tasks
- literature-synthesis: For cross-referencing data

## Example Queries

| Task | Query |
|------|-------|
| Integral | `integrate sin(x)*cos(x) dx` |
| Equation | `solve x^3 - 6x^2 + 11x - 6 = 0` |
| Conversion | `convert 1 light year to kilometers` |
| Statistics | `standard deviation of {1,2,3,4,5,6,7,8,9,10}` |
| Fact | `mass of the sun in kg` |
| Chemistry | `molecular weight of glucose` |

---

*Agent registered: 2025-12-29*
*Part of: Context Cascade v3.0.0*
