# Sandbox Configurator Routing Process

1. **Scope**: Gather HARD/SOFT/INFERRED constraints (runtime, mounts, network, secrets, observability).
2. **Safety**: Enforce isolation, deny-by-default networking, secure secrets, and rollback path.
3. **Execute**: Trigger `sandbox-configurator` SOP; tag MCP (`WHO=sandbox-configurator-{session}`, `WHY=skill-execution`).
4. **Validate**: Test allowed vs. blocked behaviors; capture evidence with confidence ceilings.
5. **Deliver**: Policy pack + validation log stored at `skills/security/specialized-tools/when-configuring-sandbox-security-use-sandbox-configurator/{project}/{timestamp}`.

Confidence: 0.70 (ceiling: inference 0.70) - Process updated to mirror the sandbox-configurator SOP.
