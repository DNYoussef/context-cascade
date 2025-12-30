/*============================================================================*/
/* PLAYBOOK META-LOOP GUARDRAILS V1.0 :: VERILINGUA x VERIX EDITION                               */
/*============================================================================*/

[define|neutral] PLAYBOOK := {
  name: "PLAYBOOK-META-LOOP-GUARDRAILS",
  type: "workflow-orchestration",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

---

# Playbook Meta-Loop Guardrails v1.0

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



**Generated**: 2025-12-15
**Total Playbooks**: 38
**Framework**: 7-Dimensional Playbook Analysis + Evidence-Based Execution

This document provides comprehensive meta-loop improvements for ALL 38 playbooks, including trigger conditions, success criteria, edge cases, guardrails, and MCP requirements.

---

## Table of Contents

1. [Delivery Playbooks](#delivery-playbooks) (9)
2. [Operations Playbooks](#operations-playbooks) (4)
3. [Research Playbooks](#research-playbooks) (4)
4. [Security Playbooks](#security-playbooks) (3)
5. [Quality Playbooks](#quality-playbooks) (3)
6. [Platform/ML Playbooks](#platformml-playbooks) (3)
7. [GitHub Playbooks](#github-playbooks) (3)
8. [NEW v3.0 Playbooks](#new-v30-playbooks) (9)

---

## Delivery Playbooks

### 1. simple-feature-implementation

**Trigger Conditions**:
- WHEN: "add feature", "implement X", "build endpoint", "create component", single-scope work
- WHEN NOT: Multi-component features, payment/auth systems, requires research phase

**Success Criteria**:
- Primary: Feature passes all tests and code review
- Acceptance Gates:
  - Unit tests pass (>80% coverage on new code)
  - Integration tests pass
  - Code review approved
  - No security vulnerabilities introduced

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Scope creep mid-implementation | New requirements emerge during coding | Pause, re-route to three-loop-system if >4h additional work |
| Missing dependencies | Import/package errors | Add dependency, document in PR |
| Conflicting requirements | Tests fail on edge cases | Clarify with stakeholder before proceeding |

**Guardrails**:
- NEVER: Skip TDD cycle (write tests BEFORE implementation)
- NEVER: Merge without code review
- ALWAYS: Run functionality-audit before marking complete
- ALWAYS: Update relevant documentation

**MCP Requirements**:
- Required: memory-mcp (state tracking)
- Optional: sequential-thinking (complex logic)

---

### 2. three-loop-system (FLAGSHIP)

**Trigger Conditions**:
- WHEN: "payment processing", "authentication system", "data pipeline", complex multi-component features, high-risk implementations
- WHEN NOT: Simple CRUD, single-file changes, quick fixes

**Success Criteria**:
- Primary: >97% planning accuracy, 100% test recovery rate
- Acceptance Gates:
  - Loop 1: <3% failure confidence in pre-mortem
  - Loop 2: Theater detection passes (Byzantine consensus)
  - Loop 3: 100% test success after recovery

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Pre-mortem identifies >20% failure risk | Risk score exceeds threshold | Iterate planning, do NOT proceed to Loop 2 |
| Theater detected in implementation | Byzantine consensus fails | Reject implementation, re-spawn agents |
| CI/CD recovery exceeds 3 attempts | Recovery loop count | Escalate to human, document failure pattern |

**Guardrails**:
- NEVER: Skip pre-mortem cycles (5x minimum)
- NEVER: Proceed to Loop 2 with >5% failure confidence
- NEVER: Accept implementation without theater detection
- ALWAYS: Use multi-agent consensus (minimum 3 agents)
- ALWAYS: Document failure patterns for Loop 3->Loop 1 feedback
- ALWAYS: Validate in sandbox before production

**MCP Requirements**:
- Required: memory-mcp, ruv-swarm, sequential-thinking
- Optional: flow-nexus (cloud features)

---

### 3. feature-dev-complete

**Trigger Conditions**:
- WHEN: "ship feature end-to-end", "complete feature lifecycle", "from research to deployment"
- WHEN NOT: Partial implementations, quick prototypes, research-only tasks

**Success Criteria**:
- Primary: Feature deployed to production with monitoring
- Acceptance Gates:
  - All 12 stages complete
  - Production metrics healthy for 24h
  - Documentation complete

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Stage failure mid-pipeline | Stage exit code non-zero | Retry stage 2x, then escalate |
| Deployment rollback required | Health check failures | Automatic rollback, trigger smart-bug-fix |
| Stage 11 (CI/CD) loops infinitely | >5 recovery attempts | Break loop, human intervention |

**Guardrails**:
- NEVER: Skip stages (all 12 required)
- NEVER: Deploy without production-readiness check
- ALWAYS: Run all quality gates between stages
- ALWAYS: Maintain deployment rollback capability

**MCP Requirements**:
- Required: memory-mcp, ruv-swarm
- Optional: playwright (E2E), flow-nexus

---

### 4. smart-bug-fix

**Trigger Conditions**:
- WHEN: "production bug", "fix error", "debug issue", "mysterious failure"
- WHEN NOT: Feature requests disguised as bugs, refactoring needs

**Success Criteria**:
- Primary: Bug resolved, regression test added
- Acceptance Gates:
  - Root cause identified
  - Fix verified in sandbox
  - Regression test passes
  - No new bugs introduced

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Bug is symptom of deeper issue | Fix doesn't fully resolve | Escalate to three-loop-system for architectural fix |
| Cannot reproduce | Intermittent failure | Add logging, monitor for recurrence |
| Fix breaks other functionality | Regression tests fail | Revert, analyze dependencies |

**Guardrails**:
- NEVER: Deploy fix without regression test
- NEVER: Skip root cause analysis (symptom fixes recur)
- ALWAYS: Check Memory MCP for similar past bugs
- ALWAYS: Document fix pattern for future reference

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking (complex debugging)

---

### 5. rapid-prototyping

**Trigger Conditions**:
- WHEN: "quick POC", "validate idea", "spike", "prototype"
- WHEN NOT: Production code, customer-facing features

**Success Criteria**:
- Primary: Concept validated or invalidated within time budget
- Acceptance Gates:
  - Core hypothesis tested
  - Decision documented (proceed/pivot/abandon)
  - Technical learnings captured

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Prototype scope creeps | Time exceeds 2x estimate | Stop, document learnings, decide if worth full implementation |
| Prototype "good enough" to ship | Stakeholder wants to deploy | STOP - route to proper playbook for production code |

**Guardrails**:
- NEVER: Ship prototype code to production
- NEVER: Exceed time budget by >50%
- ALWAYS: Document learnings regardless of outcome
- ALWAYS: Explicitly mark code as prototype (comments, branch name)

**MCP Requirements**:
- Required: None (minimal overhead)
- Optional: memory-mcp (capture learnings)

---

### 6. frontend-development

**Trigger Conditions**:
- WHEN: "React app", "UI component", "frontend feature", "web interface"
- WHEN NOT: API-only work, backend services

**Success Criteria**:
- Primary: UI renders correctly, passes accessibility checks
- Acceptance Gates:
  - Component tests pass
  - Visual regression passes
  - Accessibility audit passes (WCAG 2.1 AA)
  - Performance budget met (<3s LCP)

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Design not specified | No mockups/specs | Use interactive-planner to gather requirements |
| Browser compatibility issues | Tests fail in specific browsers | Document support matrix, fix or document limitation |

**Guardrails**:
- NEVER: Skip accessibility testing
- NEVER: Ignore performance budgets
- ALWAYS: Test in multiple browsers
- ALWAYS: Use semantic HTML

**MCP Requirements**:
- Required: memory-mcp
- Optional: playwright (visual testing)

---

### 7. backend-api-development

**Trigger Conditions**:
- WHEN: "REST API", "GraphQL", "backend endpoint", "microservice"
- WHEN NOT: Frontend-only work, static sites

**Success Criteria**:
- Primary: API meets contract, passes security scan
- Acceptance Gates:
  - OpenAPI spec validates
  - All endpoints tested
  - Security scan passes (no OWASP top 10)
  - Performance meets SLO

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Breaking API change | Contract validation fails | Version API, maintain backward compatibility |
| Database bottleneck | Load test shows slow queries | Optimize queries, add indexes, consider caching |

**Guardrails**:
- NEVER: Expose internal errors to clients
- NEVER: Skip input validation
- ALWAYS: Rate limit public endpoints
- ALWAYS: Log requests for debugging

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

### 8. full-stack-application

**Trigger Conditions**:
- WHEN: "full app", "complete application", "frontend and backend", "end-to-end app"
- WHEN NOT: Single-layer work, quick features

**Success Criteria**:
- Primary: Application deployed and functional end-to-end
- Acceptance Gates:
  - Frontend + Backend integrated
  - E2E tests pass
  - Production deployment successful
  - Monitoring in place

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Frontend-backend contract mismatch | Integration tests fail | Align contracts, regenerate types |
| Deployment environment differences | Works locally, fails in prod | Use infrastructure-as-code, containerize |

**Guardrails**:
- NEVER: Deploy frontend and backend separately without integration test
- NEVER: Skip environment parity checks
- ALWAYS: Use typed API contracts
- ALWAYS: Implement health checks

**MCP Requirements**:
- Required: memory-mcp, ruv-swarm
- Optional: playwright, flow-nexus

---

### 9. infrastructure-as-code

**Trigger Conditions**:
- WHEN: "Terraform", "CloudFormation", "Pulumi", "infrastructure setup", "IaC"
- WHEN NOT: Application code, manual infrastructure

**Success Criteria**:
- Primary: Infrastructure provisioned successfully, reproducible
- Acceptance Gates:
  - Plan shows expected changes
  - Apply succeeds
  - Smoke tests pass
  - Rollback tested

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| State drift | Plan shows unexpected changes | Investigate, import or fix drift |
| Circular dependencies | Apply fails with dependency error | Refactor modules, use depends_on |

**Guardrails**:
- NEVER: Apply without reviewing plan
- NEVER: Store secrets in code
- ALWAYS: Use remote state with locking
- ALWAYS: Tag all resources

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

## Operations Playbooks

### 10. production-deployment

**Trigger Conditions**:
- WHEN: "deploy to production", "release to prod", "go live"
- WHEN NOT: Staging deployments, local testing

**Success Criteria**:
- Primary: Deployment successful, no customer impact
- Acceptance Gates:
  - All pre-deployment checks pass
  - Deployment completes without errors
  - Health checks pass
  - Rollback capability verified

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Deployment fails mid-way | Partial rollout state | Automatic rollback, investigate |
| Performance degradation post-deploy | Metrics exceed thresholds | Rollback, analyze with performance-optimization |

**Guardrails**:
- NEVER: Deploy without rollback plan
- NEVER: Deploy during high-traffic periods without approval
- ALWAYS: Use blue-green or canary deployment
- ALWAYS: Monitor for 15min post-deployment

**MCP Requirements**:
- Required: memory-mcp
- Optional: ruv-swarm (parallel health checks)

---

### 11. cicd-pipeline-setup

**Trigger Conditions**:
- WHEN: "setup CI/CD", "configure pipeline", "automate deployment"
- WHEN NOT: One-time manual deployments

**Success Criteria**:
- Primary: Pipeline runs automatically on trigger
- Acceptance Gates:
  - Build stage succeeds
  - Test stage succeeds
  - Deploy stage succeeds
  - Notifications configured

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Flaky tests | Intermittent failures | Quarantine flaky tests, fix separately |
| Secret exposure | Secrets in logs | Mask secrets, rotate immediately |

**Guardrails**:
- NEVER: Store secrets in pipeline code
- NEVER: Skip test stage
- ALWAYS: Use separate staging/production pipelines
- ALWAYS: Require approval for production deploys

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

### 12. infrastructure-scaling

**Trigger Conditions**:
- WHEN: "scale infrastructure", "handle more traffic", "autoscaling"
- WHEN NOT: Application optimization, code-level fixes

**Success Criteria**:
- Primary: System handles target load without degradation
- Acceptance Gates:
  - Load test passes at target capacity
  - Costs within budget
  - Failover tested

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Scaling hits cloud limits | Quota exceeded errors | Request limit increase, optimize resource usage |
| Cost explosion | Bill exceeds budget | Implement cost alerts, review autoscaling policies |

**Guardrails**:
- NEVER: Scale without load testing
- NEVER: Remove resource limits
- ALWAYS: Set maximum scale bounds
- ALWAYS: Configure cost alerts

**MCP Requirements**:
- Required: memory-mcp
- Optional: flow-nexus (cloud optimization)

---

### 13. performance-optimization

**Trigger Conditions**:
- WHEN: "optimize performance", "speed up", "reduce latency"
- WHEN NOT: Feature development, bug fixes

**Success Criteria**:
- Primary: Performance metrics improved by target %
- Acceptance Gates:
  - Baseline metrics captured
  - Optimizations applied
  - Improvement measured
  - No functionality regression

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Optimization breaks functionality | Tests fail post-optimization | Revert, find alternative approach |
| Diminishing returns | Further optimization yields <5% improvement | Stop, document current state |

**Guardrails**:
- NEVER: Optimize without measuring first
- NEVER: Sacrifice correctness for speed
- ALWAYS: Benchmark before AND after
- ALWAYS: Document optimization rationale

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

## Research Playbooks

### 14. deep-research-sop (FLAGSHIP)

**Trigger Conditions**:
- WHEN: "academic research", "NeurIPS submission", "systematic review", "replicate baseline"
- WHEN NOT: Quick lookups, implementation tasks

**Success Criteria**:
- Primary: Research passes all 3 quality gates
- Acceptance Gates:
  - Gate 1: Data quality + baseline replication (+/-1% tolerance)
  - Gate 2: Novel method validated + ablation complete
  - Gate 3: Production-ready + reproducible

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Baseline replication fails | Results outside +/-1% | Investigate methodology, contact original authors |
| Quality gate fails | GO/NO-GO = NO-GO | Do NOT proceed, iterate on current phase |
| Ethical concerns arise | Ethics agent flags issues | STOP, escalate to human review |

**Guardrails**:
- NEVER: Skip quality gates
- NEVER: Proceed without ethics review
- NEVER: Publish without reproducibility audit
- ALWAYS: Use PRISMA methodology for literature review
- ALWAYS: Document all hyperparameters and random seeds
- ALWAYS: Archive datasets with datasheets

**MCP Requirements**:
- Required: memory-mcp, sequential-thinking
- Optional: flow-nexus (distributed training)

---

### 15. research-quick-investigation

**Trigger Conditions**:
- WHEN: "research X", "find best practices", "what's the state of art"
- WHEN NOT: Deep research, implementation needed

**Success Criteria**:
- Primary: Question answered with sources
- Acceptance Gates:
  - Sources cited
  - Answer is actionable
  - Confidence level stated

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Conflicting sources | Sources disagree | Present both perspectives, note conflict |
| No reliable sources | Only blog posts, no papers | State limitation, recommend deeper research |

**Guardrails**:
- NEVER: Present opinions as facts
- NEVER: Skip source citation
- ALWAYS: State confidence level
- ALWAYS: Prefer primary sources over secondary

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 16. planning-architecture

**Trigger Conditions**:
- WHEN: "design architecture", "plan system", "technical design"
- WHEN NOT: Implementation, quick fixes

**Success Criteria**:
- Primary: Architecture documented and validated
- Acceptance Gates:
  - Requirements captured
  - Trade-offs documented
  - Stakeholder approval obtained

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Requirements unclear | Ambiguous constraints | Use interactive-planner to clarify |
| Conflicting requirements | Constraints conflict | Surface conflict, request prioritization |

**Guardrails**:
- NEVER: Skip requirements gathering
- NEVER: Ignore non-functional requirements
- ALWAYS: Document assumptions
- ALWAYS: Consider scalability and security

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

### 17. literature-review

**Trigger Conditions**:
- WHEN: "literature review", "survey papers", "academic sources"
- WHEN NOT: Quick lookups, implementation

**Success Criteria**:
- Primary: Comprehensive review with synthesis
- Acceptance Gates:
  - Search strategy documented
  - Inclusion/exclusion criteria defined
  - Synthesis complete
  - Gaps identified

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Too many results | >500 papers | Narrow scope, stricter criteria |
| Too few results | <10 papers | Broaden search, check synonyms |

**Guardrails**:
- NEVER: Cherry-pick supporting papers only
- NEVER: Skip quality assessment of sources
- ALWAYS: Use systematic search strategy
- ALWAYS: Document search terms and databases

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

## Security Playbooks

### 18. security-audit

**Trigger Conditions**:
- WHEN: "security audit", "vulnerability scan", "pentest"
- WHEN NOT: Feature development, performance work

**Success Criteria**:
- Primary: All vulnerabilities identified and prioritized
- Acceptance Gates:
  - OWASP Top 10 checked
  - Dependencies scanned
  - Report generated with severity ratings

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Critical vulnerability found | Severity = Critical | STOP other work, immediate remediation |
| False positives | Tool reports issue that isn't real | Document as false positive, tune scanner |

**Guardrails**:
- NEVER: Ignore critical/high severity findings
- NEVER: Skip dependency scanning
- ALWAYS: Check OWASP Top 10
- ALWAYS: Document all findings with remediation steps

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

### 19. compliance-validation

**Trigger Conditions**:
- WHEN: "compliance check", "GDPR", "SOC2", "HIPAA", "PCI"
- WHEN NOT: Feature development, non-regulated systems

**Success Criteria**:
- Primary: Compliance status documented with evidence
- Acceptance Gates:
  - All requirements checked
  - Evidence collected
  - Gaps identified with remediation plan

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Unclear requirement interpretation | Regulation is ambiguous | Document interpretation, seek legal review |
| Non-compliant finding | Gap identified | Do NOT proceed to production, remediate first |

**Guardrails**:
- NEVER: Assume compliance without evidence
- NEVER: Ship non-compliant code
- ALWAYS: Document evidence for each requirement
- ALWAYS: Involve legal/compliance team for interpretations

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 20. reverse-engineering

**Trigger Conditions**:
- WHEN: "reverse engineer", "analyze binary", "understand protocol"
- WHEN NOT: Standard development, documented systems

**Success Criteria**:
- Primary: System behavior documented
- Acceptance Gates:
  - Behavior documented
  - Findings verified
  - Legal review (if applicable)

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Obfuscated code | Cannot decompile | Use dynamic analysis, black-box testing |
| Legal concerns | Copyright/license issues | STOP, seek legal approval |

**Guardrails**:
- NEVER: Proceed without legal clearance
- NEVER: Distribute proprietary findings
- ALWAYS: Document methodology
- ALWAYS: Verify findings with testing

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

## Quality Playbooks

### 21. quick-quality-check

**Trigger Conditions**:
- WHEN: "quick check", "fast review", "sanity check"
- WHEN NOT: Deep audits, comprehensive reviews

**Success Criteria**:
- Primary: Major issues identified within 15 minutes
- Acceptance Gates:
  - Critical issues flagged
  - Pass/fail decision made

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Found critical issue | Severity = Critical | Flag immediately, recommend comprehensive-review |
| Unclear scope | What to check? | Default to security + functionality basics |

**Guardrails**:
- NEVER: Certify quality based only on quick check
- NEVER: Skip security basics
- ALWAYS: Recommend deeper review for concerns
- ALWAYS: Time-box to 15 minutes

**MCP Requirements**:
- Required: None
- Optional: memory-mcp

---

### 22. comprehensive-review

**Trigger Conditions**:
- WHEN: "full review", "comprehensive audit", "deep code review"
- WHEN NOT: Quick checks, time-critical work

**Success Criteria**:
- Primary: All quality dimensions evaluated
- Acceptance Gates:
  - Security reviewed
  - Performance reviewed
  - Maintainability reviewed
  - Documentation reviewed

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Codebase too large | >100k lines | Prioritize critical paths, sample non-critical |
| No test coverage | Tests missing | Flag as critical finding |

**Guardrails**:
- NEVER: Skip security dimension
- NEVER: Rush comprehensive review
- ALWAYS: Use structured checklist
- ALWAYS: Document all findings

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

### 23. dogfooding-cycle

**Trigger Conditions**:
- WHEN: "dogfood", "self-improvement", "run on ourselves"
- WHEN NOT: External code, customer work

**Success Criteria**:
- Primary: Improvements applied and validated
- Acceptance Gates:
  - Issues detected
  - Fixes applied
  - Tests pass post-fix

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Fix breaks something else | Tests fail | Revert, analyze dependencies |
| No issues found | Clean scan | Celebrate, document clean state |

**Guardrails**:
- NEVER: Skip sandbox testing of fixes
- NEVER: Apply fixes without review
- ALWAYS: Store findings in Memory MCP
- ALWAYS: Track improvement metrics

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

## Platform/ML Playbooks

### 24. ml-pipeline-development

**Trigger Conditions**:
- WHEN: "train model", "ML pipeline", "machine learning", "neural network"
- WHEN NOT: Traditional software, rule-based systems

**Success Criteria**:
- Primary: Model meets performance targets
- Acceptance Gates:
  - Data quality validated
  - Model trained successfully
  - Metrics meet thresholds
  - Model versioned and reproducible

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Data leakage | Test metrics suspiciously high | Audit data splits, re-train |
| Model overfitting | Train/val gap too large | Add regularization, more data |

**Guardrails**:
- NEVER: Train without validation split
- NEVER: Skip data quality checks
- ALWAYS: Version datasets and models
- ALWAYS: Log all hyperparameters and seeds

**MCP Requirements**:
- Required: memory-mcp, flow-nexus
- Optional: ruv-swarm (distributed training)

---

### 25. vector-search-rag

**Trigger Conditions**:
- WHEN: "RAG", "vector search", "semantic search", "embeddings"
- WHEN NOT: Keyword search, simple lookups

**Success Criteria**:
- Primary: Search returns relevant results
- Acceptance Gates:
  - Embeddings generated
  - Index built
  - Retrieval quality validated

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Poor retrieval quality | Irrelevant results | Tune chunking, try different embeddings |
| Index too large | Memory/cost issues | Use approximate search, shard index |

**Guardrails**:
- NEVER: Skip retrieval quality evaluation
- NEVER: Use embeddings without testing
- ALWAYS: Test with diverse queries
- ALWAYS: Monitor latency and costs

**MCP Requirements**:
- Required: memory-mcp
- Optional: flow-nexus

---

### 26. distributed-neural-training

**Trigger Conditions**:
- WHEN: "distributed training", "multi-GPU", "large model"
- WHEN NOT: Small models, single-GPU training

**Success Criteria**:
- Primary: Training completes with near-linear scaling
- Acceptance Gates:
  - Distributed setup working
  - Gradient sync verified
  - Training converges

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Gradient explosion | Loss = NaN | Reduce learning rate, gradient clipping |
| Node failure | Worker disconnects | Checkpoint recovery, retry |

**Guardrails**:
- NEVER: Train without checkpoints
- NEVER: Skip gradient verification
- ALWAYS: Monitor all workers
- ALWAYS: Test at small scale first

**MCP Requirements**:
- Required: memory-mcp, flow-nexus, ruv-swarm
- Optional: None

---

## GitHub Playbooks

### 27. pr-management-review

**Trigger Conditions**:
- WHEN: "review PR", "code review", "merge request"
- WHEN NOT: Creating PRs, feature development

**Success Criteria**:
- Primary: PR approved or changes requested with clear feedback
- Acceptance Gates:
  - Code reviewed
  - Tests pass
  - No security issues
  - Documentation adequate

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| PR too large | >500 lines changed | Request split into smaller PRs |
| Conflicting approvals | Reviewers disagree | Escalate to tech lead |

**Guardrails**:
- NEVER: Approve without running tests
- NEVER: Merge with failing CI
- ALWAYS: Check for security implications
- ALWAYS: Verify documentation updated

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 28. release-management

**Trigger Conditions**:
- WHEN: "release", "version bump", "tag release"
- WHEN NOT: Development work, feature branches

**Success Criteria**:
- Primary: Release created and deployed
- Acceptance Gates:
  - Version bumped correctly
  - Changelog updated
  - Tag created
  - Release notes published

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Breaking changes | Semver major required | Verify intentional, update all dependents |
| Release fails | Tag/publish error | Retry, verify credentials |

**Guardrails**:
- NEVER: Release without changelog
- NEVER: Skip version tag
- ALWAYS: Follow semver
- ALWAYS: Announce deprecations in advance

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 29. multi-repo-coordination

**Trigger Conditions**:
- WHEN: "multi-repo", "cross-repo", "monorepo sync"
- WHEN NOT: Single repo work

**Success Criteria**:
- Primary: All repos updated consistently
- Acceptance Gates:
  - All PRs created
  - Versions aligned
  - Integration tested

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Circular dependency | Repo A needs B needs A | Break cycle, release in correct order |
| Partial update | Some repos updated, others not | Rollback all, retry atomically |

**Guardrails**:
- NEVER: Partially update dependent repos
- NEVER: Skip integration testing
- ALWAYS: Coordinate release order
- ALWAYS: Document dependency graph

**MCP Requirements**:
- Required: memory-mcp
- Optional: ruv-swarm (parallel PRs)

---

## NEW v3.0 Playbooks

### 30. codebase-onboarding

**Trigger Conditions**:
- WHEN: "understand this code", "new to codebase", "onboard me"
- WHEN NOT: Implementation tasks, bug fixes

**Success Criteria**:
- Primary: Developer can navigate and contribute to codebase
- Acceptance Gates:
  - Architecture understood
  - Key files identified
  - Development workflow documented

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| No documentation exists | README missing | Generate documentation as part of onboarding |
| Codebase too large | >1M lines | Focus on specific area first |

**Guardrails**:
- NEVER: Assume implicit knowledge
- NEVER: Skip architecture overview
- ALWAYS: Identify entry points
- ALWAYS: Document gotchas and tribal knowledge

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 31. emergency-incident-response

**Trigger Conditions**:
- WHEN: "PRODUCTION DOWN", "P0", "critical outage", "emergency"
- WHEN NOT: Non-urgent issues, feature work

**Success Criteria**:
- Primary: Service restored within SLA
- Acceptance Gates:
  - Incident identified
  - Mitigation applied
  - Service restored
  - Post-mortem scheduled

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Root cause unknown | Cannot identify issue | Apply general mitigations, escalate |
| Rollback fails | Previous version also broken | Identify last known good, emergency patch |

**Guardrails**:
- NEVER: Skip rollback verification
- NEVER: Deploy fixes without testing (even in emergency)
- ALWAYS: Communicate status updates
- ALWAYS: Document timeline for post-mortem

**MCP Requirements**:
- Required: memory-mcp
- Optional: ruv-swarm (parallel investigation)

---

### 32. refactoring-technical-debt

**Trigger Conditions**:
- WHEN: "refactor", "tech debt", "god object", "clean up code"
- WHEN NOT: Feature development, bug fixes

**Success Criteria**:
- Primary: Code quality improved without functionality change
- Acceptance Gates:
  - All tests still pass
  - No behavior change
  - Metrics improved (complexity, coupling)

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Tests insufficient | Low coverage | Add tests BEFORE refactoring |
| Scope creep | Refactor grows | Time-box, split into phases |

**Guardrails**:
- NEVER: Refactor without tests
- NEVER: Change behavior during refactor
- ALWAYS: Measure before and after
- ALWAYS: Make atomic commits

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

### 33. database-migration

**Trigger Conditions**:
- WHEN: "migrate database", "schema change", "database upgrade"
- WHEN NOT: Application code changes, queries only

**Success Criteria**:
- Primary: Migration completed without data loss
- Acceptance Gates:
  - Backup verified
  - Migration tested on staging
  - Rollback tested
  - Data integrity verified

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Migration timeout | Large table locks | Use online migration tools, batch operations |
| Data corruption | Integrity check fails | ROLLBACK immediately, investigate |

**Guardrails**:
- NEVER: Migrate without backup
- NEVER: Skip staging test
- ALWAYS: Test rollback procedure
- ALWAYS: Run during low-traffic period

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 34. dependency-upgrade-audit

**Trigger Conditions**:
- WHEN: "update dependencies", "security patch", "upgrade packages"
- WHEN NOT: Feature development, new dependencies

**Success Criteria**:
- Primary: Dependencies updated without breaking changes
- Acceptance Gates:
  - Security vulnerabilities patched
  - All tests pass
  - No breaking changes introduced

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Breaking change in minor version | Tests fail | Pin version, schedule proper migration |
| Conflicting dependencies | Resolution fails | Find compatible versions, consider alternatives |

**Guardrails**:
- NEVER: Update all dependencies at once
- NEVER: Skip testing after upgrade
- ALWAYS: Update one major dependency at a time
- ALWAYS: Read changelogs for breaking changes

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 35. comprehensive-documentation

**Trigger Conditions**:
- WHEN: "generate docs", "document everything", "API docs"
- WHEN NOT: Code implementation, quick notes

**Success Criteria**:
- Primary: Documentation complete and accurate
- Acceptance Gates:
  - API documented
  - Architecture documented
  - README updated
  - Examples provided

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Code changes frequently | Docs outdated quickly | Automate doc generation, link to code |
| Complex system | Hard to document | Use diagrams, break into sections |

**Guardrails**:
- NEVER: Document implementation details that change
- NEVER: Skip examples
- ALWAYS: Keep docs close to code
- ALWAYS: Verify docs match reality

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 36. performance-optimization-deep-dive

**Trigger Conditions**:
- WHEN: "app is slow", "performance issues", "optimize deeply"
- WHEN NOT: Quick fixes, feature development

**Success Criteria**:
- Primary: Performance improved by measurable amount
- Acceptance Gates:
  - Baseline captured
  - Bottlenecks identified
  - Optimizations applied
  - Improvements measured

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Bottleneck is external | Database, network, etc. | Identify owner, coordinate fix |
| Optimization ineffective | <5% improvement | Document, try different approach |

**Guardrails**:
- NEVER: Optimize without profiling
- NEVER: Guess at bottlenecks
- ALWAYS: Measure before and after
- ALWAYS: Test for regressions

**MCP Requirements**:
- Required: memory-mcp
- Optional: sequential-thinking

---

### 37. i18n-implementation

**Trigger Conditions**:
- WHEN: "internationalization", "add languages", "translate app"
- WHEN NOT: Single-language apps, locale-specific work

**Success Criteria**:
- Primary: App supports target languages
- Acceptance Gates:
  - Strings extracted
  - Translations complete
  - RTL support (if needed)
  - Date/number formatting correct

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Missing translations | Fallback to default | Flag in UI, prioritize translation |
| Text expansion | Translated text longer | Adjust UI, use responsive design |

**Guardrails**:
- NEVER: Hardcode strings
- NEVER: Assume LTR only
- ALWAYS: Use ICU message format
- ALWAYS: Test with longest translations

**MCP Requirements**:
- Required: memory-mcp
- Optional: None

---

### 38. a11y-compliance

**Trigger Conditions**:
- WHEN: "accessibility", "WCAG", "screen reader", "a11y"
- WHEN NOT: Non-visual systems, APIs only

**Success Criteria**:
- Primary: Application meets WCAG 2.1 AA
- Acceptance Gates:
  - Automated scan passes
  - Manual testing complete
  - Screen reader tested
  - Keyboard navigation works

**Edge Cases**:
| Case | Detection | Handling |
|------|-----------|----------|
| Complex widget | Standard patterns don't apply | Use ARIA, test extensively |
| Third-party component | Cannot modify | Wrap or replace with accessible alternative |

**Guardrails**:
- NEVER: Rely only on automated testing
- NEVER: Skip screen reader testing
- ALWAYS: Test with keyboard only
- ALWAYS: Use semantic HTML

**MCP Requirements**:
- Required: memory-mcp
- Optional: playwright (automated testing)

---

## Summary

| Category | Playbooks | Key Guardrails |
|----------|-----------|----------------|
| Delivery | 9 | TDD, code review, functionality audit |
| Operations | 4 | Rollback plans, monitoring, approvals |
| Research | 4 | Quality gates, citations, methodology |
| Security | 3 | OWASP, evidence, legal review |
| Quality | 3 | Checklists, time-boxing, documentation |
| Platform/ML | 3 | Validation splits, checkpoints, versioning |
| GitHub | 3 | CI/CD, semver, coordination |
| NEW v3.0 | 9 | Domain-specific guardrails |

**Total**: 38 playbooks with comprehensive meta-loop integration

---

## Usage

When routing to a playbook, ALWAYS:
1. Verify trigger conditions match
2. Check MCP requirements are available
3. Apply guardrails during execution
4. Validate success criteria at completion
5. Handle edge cases as documented

This ensures consistent, high-quality execution across all playbook types.


---
*Promise: `<promise>PLAYBOOK_META_LOOP_GUARDRAILS_VERIX_COMPLIANT</promise>`*
