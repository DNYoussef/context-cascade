# Platform - Quick Reference v2.1.0

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



## Purpose
Flow Nexus platform services hub.

## Sub-Skills

| Skill | Trigger |
|-------|---------|
| flow-nexus-neural | ML training |
| flow-nexus-platform | Auth, payments |
| flow-nexus-swarm | Swarm deployment |

## Quick Commands

```bash
# Neural training
Use platform/neural for: [training task]

# Platform services
Use platform/services for: [auth/payment]

# Swarm deploy
Use platform/swarm for: [deployment]
```

## Routing

```
neural/training/ml -> flow-nexus-neural
swarm/deploy -> flow-nexus-swarm
auth/payment/sandbox -> flow-nexus-platform
```

## Related Skills

- **flow-nexus-neural**
- **flow-nexus-platform**
- **flow-nexus-swarm**


---
*Promise: `<promise>QUICK_REFERENCE_VERIX_COMPLIANT</promise>`*
