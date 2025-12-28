---
name: platform
description: Platform services hub routing to Flow Nexus platform skills. Use for cloud AI platform management, neural network training, swarm deployment, and platform authentication. Routes to flow-nexus-neural, flow-nexus-platform, and flow-nexus-swarm. --- # Platform Central hub for Flow Nexus platform services and cloud AI capabilities. ## Phase 0: Expertise Loading ```yaml
---

# Platform

Central hub for Flow Nexus platform services and cloud AI capabilities.

## Phase 0: Expertise Loading

```yaml
expertise_check:
  domain: platform
  file: .claude/expertise/platform.yaml

  if_exists:
    - Load platform configurations
    - Load API patterns
    - Apply service quotas

  if_not_exists:
    - Flag discovery mode
    - Document patterns learned
```

## When to Use This Skill

Use platform when:
- Training neural networks in cloud sandboxes
- Deploying AI swarms to cloud
- Managing Flow Nexus platform services
- Setting up platform authentication
- Integrating payment systems

## Sub-Skills

| Skill | Use Case |
|-------|----------|
| flow-nexus-neural | Neural network training |
| flow-nexus-platform | Platform management |
| flow-nexus-swarm | Cloud swarm deployment |

## Routing Logic

```yaml
routing:
  if "neural" or "training" or "ml":
    route_to: flow-nexus-neural
  if "swarm" or "deploy":
    route_to: flow-nexus-swarm
  if "auth" or "payment" or "sandbox":
    route_to: flow-nexus-platform
  default:
    route_to: flow-nexus-platform
```

## MCP Requirements

- **claude-flow**: Platform coordination
- **memory-mcp**: State management

## Recursive Improvement Integration (v2.1)

### Eval Harness Integration

```yaml
benchmark: platform-benchmark-v1
  tests:
    - plat-001: Platform routing
    - plat-002: Service availability
  minimum_scores:
    routing_accuracy: 0.90
    service_uptime: 0.99
```

### Memory Namespace

```yaml
namespaces:
  - platform/services/{id}: Service configs
  - platform/metrics: Performance tracking
  - improvement/audits/platform: Skill audits
```

### Uncertainty Handling

```yaml
confidence_check:
  if confidence >= 0.8:
    - Route to appropriate service
  if confidence 0.5-0.8:
    - Present service options
  if confidence < 0.5:
    - Ask clarifying questions
```

### Cross-Skill Coordination

Works with: **flow-nexus-neural**, **flow-nexus-platform**, **flow-nexus-swarm**

-----------|--------------|------------------|
| Hardcoding service endpoints | Breaks when Flow Nexus platform migrates infrastructure or updates API versions | Use platform routing logic to resolve services dynamically, load from expertise files |
| Skipping Phase 0 expertise loading | Every request re-discovers service quotas, rate limits, and authentication patterns | Always check .claude/expertise/platform.yaml first, cache service configs in memory-mcp namespace |
| Bypassing confidence checks (forcing routes <0.5) | Routes neural training to generic platform service, wasting GPU time on incorrect setup | Respect confidence thresholds, present options or ask clarifying questions when uncertain |

## Conclusion

The platform skill serves as the intelligent gateway to Flow Nexus cloud services, ensuring requests reach specialized handlers (neural, swarm, or generic platform) without unnecessary overhead. By combining Phase 0 expertise loading with confidence-scored routing, it balances speed (cached service patterns) with safety (uncertainty handling), preventing the common failure mode of blindly routing expensive GPU requests to wrong endpoints.

For production deployments, the key success metric is routing accuracy above 0.90 - below this threshold, the cost of misrouted neural training jobs (hours of GPU waste) exceeds the benefit of automated routing. When in doubt, defer to explicit service selection rather than guessing; a 5-second clarification question prevents a 4-hour GPU misallocation.