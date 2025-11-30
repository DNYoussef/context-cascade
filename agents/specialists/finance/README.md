# Finance Specialists

**Category**: specialists/finance
**Agent Count**: 3
**Added**: 2025-11-26

This directory contains specialized agents for quantitative finance, risk management, and market data integration.

## Available Agents

| Agent | File | Specialization |
|-------|------|----------------|
| Quant Analyst | `quant-analyst.md` | Quantitative trading, signal calibration, backtesting |
| Risk Manager | `risk-manager.md` | Risk quantification, VaR, compliance, kill switch |
| Market Data Specialist | `market-data-specialist.md` | Real-time data feeds, Alpaca API, WebSocket streaming |

## Use Cases

### ISS-017: AI/Compliance Engines Return Fake Values

Use **quant-analyst** and **risk-manager** together:

```
Task("Quant Analyst", "Audit AI signal generators for proper calibration. Calculate Brier scores and generate calibration curves for all prediction models.", "quant-analyst")

Task("Risk Manager", "Validate risk engine calculations are real. Audit VaR, drawdown, and P(ruin) calculations against expected values.", "risk-manager")
```

### ISS-020: Real-Time Data Feeds Are Mock/Placeholder

Use **market-data-specialist**:

```
Task("Market Data Specialist", "Replace mock data generators with real Alpaca API integration. Implement WebSocket streaming for live quotes and trades.", "market-data-specialist")
```

## Integration Points

These agents integrate with existing agents:
- **soc-compliance-auditor**: Regulatory compliance
- **compliance-validation-agent**: Data privacy
- **kafka-streaming-agent**: Data streaming architecture
- **model-monitoring-agent**: Production monitoring
- **model-evaluation-agent**: Model validation

## Source Attribution

Based on agents from:
- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)
- [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- [alpacahq/alpaca-mcp-server](https://github.com/alpacahq/alpaca-mcp-server)

Adapted and enhanced for the ruv-sparc-three-loop-system plugin format.
