# Dependency Mapper – Process

1. **Intent & Scope**
   - Confirm ecosystem, repo path, and desired outputs (graph/report/remediation).
2. **Detection**
   - Locate lockfiles and package managers; note monorepo boundaries.
3. **Mapping**
   - Run ecosystem-specific commands to produce tree/graph; capture outputs.
4. **Risk Analysis**
   - Identify circular, unused, outdated, and vulnerable packages; note evidence and confidence.
5. **Visualization**
   - Generate diagram (`process-diagram.gv` as reference); highlight hotspots.
6. **Recommendations**
   - Propose actions (pin/upgrade/remove/isolate) with commands and blast radius.
7. **Validation & Delivery**
   - Verify graph consistency, store artifacts, and output confidence ceiling + memory keys.

Confidence: 0.70 (ceiling: inference 0.70).
