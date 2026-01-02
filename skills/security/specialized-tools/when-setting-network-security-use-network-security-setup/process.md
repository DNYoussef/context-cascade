# Network Security Setup Routing Process

1. **Scope**: Gather HARD/SOFT/INFERRED constraints (environment, allowlists, proxy needs, TLS requirements).
2. **Safety**: Confirm authorization, isolation, deny-by-default stance, and change logging.
3. **Execute**: Trigger `network-security-setup` SOP; tag MCP (`WHO=network-security-setup-{session}`, `WHY=skill-execution`).
4. **Validate**: Test allowed vs. blocked connectivity and TLS posture; capture evidence with confidence ceilings.
5. **Deliver**: Policy pack + validation log saved at `skills/security/specialized-tools/when-setting-network-security-use-network-security-setup/{project}/{timestamp}`.

Confidence: 0.70 (ceiling: inference 0.70) - Process updated to mirror the network-security-setup SOP.
