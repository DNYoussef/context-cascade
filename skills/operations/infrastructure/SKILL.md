---

## CRITICAL: CI/CD SAFETY GUARDRAILS

**BEFORE any CI/CD operation, validate**:
- [ ] Rollback plan documented and tested
- [ ] Deployment window approved (avoid peak hours)
- [ ] Health checks configured (readiness + liveness probes)
- [ ] Monitoring alerts active for deployment metrics
- [ ] Incident response team notified

**NEVER**:
- Deploy without rollback capability
- Skip environment-specific validation (dev -> staging -> prod)
- Ignore test failures in pipeline
- Deploy outside approved maintenance windows
- Bypass approval gates in production pipelines

**ALWAYS**:
- Use blue-green or canary deployments for zero-downtime
- Implement circuit breakers for cascading failure prevention
- Document deployment state changes in incident log
- Validate infrastructure drift before deployment
- Retain audit trail of all pipeline executions

**Evidence-Based Techniques for CI/CD**:
- **Plan-and-Solve**: Break deployment into phases (build -> test -> stage -> prod)
- **Self-Consistency**: Run identical tests across environments (consistency = reliability)
- **Least-to-Most**: Start with smallest scope (single pod -> shard -> region -> global)
- **Verification Loop**: After each phase, verify expected state before proceeding

name: infrastructure
description: '- **Skill ID**: infrastructure-orchestration'
version: 1.0.0
category: operations
tags:
- operations
- deployment
- infrastructure
author: ruv
---

# Infrastructure Orchestration Skill

## Metadata
- **Skill ID**: infrastructure-orchestration
- **Category**: Infrastructure & DevOps
- **Tier**: Gold
- **Version**: 2.0.0
- **Last Updated**: 2025-11-02

## Overview

Comprehensive infrastructure orchestration skill that manages cloud resources, containerization, infrastructure as code (IaC), deployment automation, and monitoring setup. This parent skill coordinates specialized sub-skills for Docker containerization and Terraform IaC management.

## Capabilities

### Core Infrastructure Management
- **Cloud Provisioning**: Multi-cloud resource provisioning (AWS, Azure, GCP)
- **Container Orchestration**: Docker, Kubernetes, Docker Swarm
- **Infrastructure as Code**: Terraform, CloudFormation, Pulumi
- **Configuration Management**: Ansible, Chef, Puppet
- **Deployment Automation**: CI/CD pipelines, blue-green deployments
- **Monitoring & Observability**: Prometheus, Grafana, ELK stack, OpenTelemetry

### Specialized Sub-Skills
1. **Docker Containerization** (`docker-containerization/`)
   - Multi-stage builds, optimization, security scanning
   - Docker Compose orchestration
   - Registry management and image distribution

2. **Terraform IaC** (`terraform-iac/`)
   - Multi-cloud infrastructure provisioning
   - State management and GitOps workflows
   - Module development and reusability

## Trigger Conditions

Auto-invoke this skill when user mentions:
- "infrastructure", "cloud setup", "provision resources"
- "deploy to AWS/Azure/GCP", "multi-cloud"
- "container orchestration", "Kubernetes", "K8s"
- "infrastructure as code", "IaC", "Terraform", "CloudFormation"
- "monitoring setup", "observability", "logging"
- "configuration management", "Ansible"
- "CI/CD pipeline", "deployment automation"

## Agent Assignments

**Primary Agents**:
- `cicd-engineer` - CI/CD pipeline setup and deployment automation
- `backend-dev` - Infrastructure architecture and design
- `system-architect` - High-level infrastructure planning

**Supporting Agents**:
- `code-analyzer` - Infrastructure code review and optimization
- `reviewer` - Security and compliance validation
- `tester` - Infrastructure testing and validation

## Workflow

### 1. Assessment Phase
```yaml
Input: Infrastructure requirements, scale, compliance needs
Actions:
  - Analyze current infrastructure state
  - Identify gaps and requirements
  - Select appropriate tools and platforms
  - Design architecture with redundancy and scalability
Output: Infrastructure design document, technology stack selection
```

### 2. Provisioning Phase
```yaml
Input: Architecture design, resource specifications
Actions:
  - Write IaC templates (Terraform/CloudFormation)
  - Configure networking, security groups, IAM roles
  - Set up container orchestration (if needed)
  - Implement multi-region/AZ deployment
Output: IaC codebase, provisioned cloud resources
```

### 3. Deployment Automation Phase
```yaml
Input: Application artifacts, deployment strategy
Actions:
  - Configure CI/CD pipelines (GitHub Actions, GitLab CI, Jenkins)
  - Set up container registries and artifact storage
  - Implement blue-green or canary deployment strategies
  - Configure auto-scaling and load balancing
Output: Automated deployment pipeline, deployment scripts
```

### 4. Monitoring & Observability Phase
```yaml
Input: SLOs, SLIs, alerting requirements
Actions:
  - Deploy monitoring stack (Prometheus, Grafana, ELK)
  - Configure metrics collection and log aggregation
  - Set up distributed tracing (Jaeger, Zipkin)
  - Create dashboards and alerting rules
Output: Monitoring infrastructure, dashboards, alert configurations
```

### 5. Configuration Management Phase
```yaml
Input: Server configurations, application configs
Actions:
  - Write Ansible playbooks or Chef recipes
  - Implement configuration drift detection
  - Set up secrets management (Vault, AWS Secrets Manager)
  - Configure environment-specific variables
Output: Configuration management codebase, secrets vault
```

### 6. Testing & Validation Phase
```yaml
Input: Infrastructure code, deployment artifacts
Actions:
  - Run infrastructure tests (Terratest, InSpec)
  - Validate security compliance (Checkov, tfsec)
  - Test disaster recovery procedures
  - Perform load testing and chaos engineering
Output: Test reports, compliance validation, DR runbooks
```

## Resource Requirements

### Scripts
- `infra-provisioner.sh` - Automated infrastructure provisioning
- `config-manager.py` - Configuration management and validation
- `deployment-automation.js` - CI/CD pipeline orchestration
- `monitoring-setup.py` - Monitoring stack deployment

### Templates
- `terraform-config.tf` - Terraform configuration for multi-cloud
- `docker-compose.yml` - Docker Compose orchestration
- `k8s-deployment.yaml` - Kubernetes deployment manifests

### Tests
- `infrastructure.test.js` - Infrastructure validation tests
- `deployment.test.py` - Deployment pipeline tests
- `monitoring.test.sh` - Monitoring stack verification

## Integration Points

### Cloud Providers
- **AWS**: EC2, ECS, EKS, Lambda, RDS, S3, CloudFormation
- **Azure**: VMs, AKS, Azure Functions, Cosmos DB, ARM templates
- **GCP**: Compute Engine, GKE, Cloud Functions, Cloud SQL, Deployment Manager

### Container Platforms
- **Docker**: Container runtime, Docker Compose
- **Kubernetes**: Pod orchestration, Helm charts, Operators
- **Nomad**: Alternative orchestration platform

### IaC Tools
- **Terraform**: Multi-cloud provisioning, state management
- **Pulumi**: Programming language-based IaC
- **CloudFormation**: AWS-native IaC
- **Ansible**: Configuration management and provisioning

### Monitoring Tools
- **Prometheus**: Metrics collection and alerting
- **Grafana**: Visualization and dashboards
- **ELK Stack**: Log aggregation (Elasticsearch, Logstash, Kibana)
- **OpenTelemetry**: Distributed tracing and observability

## Performance Targets

- **Provisioning Time**: < 10 minutes for standard environments
- **Deployment Frequency**: Support multiple deployments per day
- **Recovery Time Objective (RTO)**: < 1 hour for critical systems
- **Recovery Point Objective (RPO)**: < 15 minutes data loss
- **Infrastructure Uptime**: 99.9% SLA
- **Monitoring Coverage**: 100% of critical services

## Best Practices

### Security
- ✅ Implement principle of least privilege (IAM, RBAC)
- ✅ Encrypt data at rest and in transit
- ✅ Use secrets management (never commit secrets)
- ✅ Regular security scanning (Trivy, Checkov, tfsec)
- ✅ Network segmentation and firewall rules

### Reliability
- ✅ Multi-AZ/region deployments for HA
- ✅ Implement health checks and auto-recovery
- ✅ Regular disaster recovery drills
- ✅ Automated backups with tested restore procedures
- ✅ Chaos engineering to test resilience

### Cost Optimization
- ✅ Right-size instances based on actual usage
- ✅ Use spot instances for non-critical workloads
- ✅ Implement auto-scaling policies
- ✅ Regular cost analysis and optimization
- ✅ Tag resources for cost allocation

### Maintainability
- ✅ Infrastructure as Code for all resources
- ✅ Version control for IaC and configuration
- ✅ Comprehensive documentation and runbooks
- ✅ Modular and reusable code
- ✅ Automated testing and validation

## Examples

### Example 1: Docker Deployment
```yaml
Scenario: Deploy microservices application with Docker Compose
Input: Application code, service dependencies
Steps:
  1. Create multi-stage Dockerfiles for each service
  2. Write docker-compose.yml with service definitions
  3. Configure networking and volumes
  4. Set up environment variables and secrets
  5. Implement health checks and restart policies
Output: Production-ready Docker Compose deployment
File: examples/docker-deployment-example.md
```

### Example 2: Kubernetes Setup
```yaml
Scenario: Set up production Kubernetes cluster with monitoring
Input: Application containers, scaling requirements
Steps:
  1. Provision managed K8s cluster (EKS/GKE/AKS)
  2. Create namespaces, deployments, services
  3. Configure Ingress controllers and load balancers
  4. Set up Helm charts for application deployment
  5. Deploy Prometheus/Grafana monitoring stack
  6. Configure auto-scaling (HPA, VPA, cluster autoscaler)
Output: Production K8s cluster with full observability
File: examples/kubernetes-setup-example.md
```

### Example 3: Terraform Multi-Cloud Infrastructure
```yaml
Scenario: Deploy multi-cloud infrastructure with Terraform
Input: Infrastructure requirements, compliance constraints
Steps:
  1. Design multi-cloud architecture (AWS + Azure)
  2. Write Terraform modules for networking, compute, storage
  3. Configure remote state backend (S3 + DynamoDB)
  4. Implement CI/CD pipeline for infrastructure changes
  5. Set up monitoring and alerting across clouds
  6. Run compliance checks (Checkov, tfsec)
Output: Multi-cloud infrastructure with GitOps workflow
File: examples/terraform-infrastructure-example.md
```

## Error Handling

### Common Issues
1. **State Lock Conflicts** (Terraform)
   - Solution: Implement state locking with DynamoDB/Azure Blob
   - Use `-lock=false` only in emergency

2. **Resource Quota Exceeded**
   - Solution: Request quota increases, optimize resource usage
   - Implement cost alerts and limits

3. **Deployment Failures**
   - Solution: Implement rollback strategies, health checks
   - Use blue-green or canary deployments

4. **Configuration Drift**
   - Solution: Regular drift detection, automated remediation
   - Use tools like Terraform Cloud or Spacelift

5. **Secret Leaks**
   - Solution: Use secrets management, never commit secrets
   - Implement pre-commit hooks with tools like git-secrets

## Dependencies

### Required Tools
- Docker (>= 20.10)
- Kubernetes CLI (`kubectl`) (>= 1.24)
- Terraform (>= 1.5)
- Ansible (>= 2.12)
- Cloud CLIs (AWS CLI, Azure CLI, gcloud)

### Optional Tools
- Helm (>= 3.10)
- Terragrunt (>= 0.45)
- Pulumi (>= 3.60)
- Packer (>= 1.8)

## Success Metrics

- ✅ Infrastructure provisioning automated (100% IaC coverage)
- ✅ Zero-downtime deployments achieved
- ✅ Monitoring covers all critical services
- ✅ RTO/RPO targets met in DR tests
- ✅ Security compliance validated (CIS benchmarks)
- ✅ Cost optimization targets achieved

## Related Skills

- `docker-containerization` - Docker-specific orchestration
- `terraform-iac` - Terraform infrastructure management
- `kubernetes-specialist` - Advanced K8s operations
- `aws-specialist` - AWS-specific deployments
- `opentelemetry-observability` - Observability setup
- `cicd-intelligent-recovery` - CI/CD automation

## Notes

- Always use IaC for infrastructure changes (no manual changes)
- Implement tagging strategy for resource organization
- Regular security audits and compliance checks
- Document all runbooks and disaster recovery procedures
- Use multi-region deployments for critical systems
- Implement cost allocation and optimization strategies

---

**Status**: Gold Tier - Production Ready with Comprehensive Resources
**Maintainer**: Infrastructure & DevOps Team
**Support**: Refer to sub-skills for specialized guidance

---

## Core Principles

### 1. Immutable Infrastructure Pattern
Treat servers as disposable cattle, not irreplaceable pets. Never modify running infrastructure - replace it entirely:
- **No SSH Access**: Eliminate manual server modification and configuration drift
- **Bake AMIs/Images**: Pre-configure all software in machine images, not at runtime
- **Blue-Green Deployments**: Run new version alongside old, switch traffic atomically
- **Rollback via Version**: Roll back by redeploying previous image version, not by patching

Configuration drift (servers modified manually) is the primary cause of "works on my machine" failures and unreproducible production issues. Immutable infrastructure eliminates drift by treating every deployment as a clean slate.

### 2. Observable Systems Through Instrumentation
You cannot debug what you cannot see. Every infrastructure component must expose three pillars of observability:
- **Metrics**: Time-series data for performance monitoring (CPU, memory, request rate, latency percentiles)
- **Logs**: Structured event streams for debugging (JSON format, centralized aggregation, retention policies)
- **Traces**: Distributed request tracking across services (OpenTelemetry, Jaeger, correlation IDs)

Without observability, production debugging becomes guesswork. Instrument BEFORE deploying, not after incidents occur. Use standardized formats (OpenTelemetry) for vendor-agnostic instrumentation.

### 3. Progressive Deployment Strategies
Deploying directly to 100% of production traffic is a failure mode. Use incremental rollout patterns:
- **Canary Deployment**: Route 1-5% traffic to new version, monitor error rates before full rollout
- **Blue-Green Deployment**: Run new version alongside old, switch traffic atomically with instant rollback
- **Feature Flags**: Decouple deployment from feature activation, enable features per user cohort
- **Circuit Breakers**: Automatically stop deployment if error rates exceed thresholds

Progressive deployment limits blast radius. A bug affecting 5% of users (canary) is recoverable; the same bug affecting 100% of users (direct deployment) is a crisis.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Configuration Drift Through Manual Changes** | SSH into servers and manually modify configuration. This creates "snowflake servers" - unique, undocumented configurations that break when scaled or replaced. Disaster recovery fails because configuration is not reproducible. | **Immutable Infrastructure**: Never modify running servers. Use configuration management (Ansible/Chef) for pre-deployment setup, then replace entire instances on configuration changes. Configuration must be version-controlled and code-reviewed. |
| **Monitoring as an Afterthought** | Deploy infrastructure without instrumentation, add monitoring only after production incidents occur. Results in blind spots during outages and prolonged incident resolution times. | **Observability-First Design**: Instrument metrics, logs, and traces BEFORE deploying. Define SLIs (Service Level Indicators) and SLOs (Service Level Objectives) during architecture phase. Deploy monitoring stack (Prometheus/Grafana) before application services. |
| **Single-Environment Testing** | Test only in development environment, then deploy directly to production. Results in "works on dev" failures in production due to configuration differences, data volume differences, or network topology differences. | **Multi-Stage Pipeline with Production Parity**: Maintain staging environment with production-like data volume, network topology, and resource constraints. Run full test suite (integration + E2E + load) on staging before production deployment. Use infrastructure-as-code to guarantee environment consistency. |

---

## Conclusion

Infrastructure orchestration is the foundation of reliable software delivery. The patterns and tools in this skill enable automated provisioning, deployment, and monitoring across cloud platforms, container orchestrators, and on-premises data centers. However, tools alone do not guarantee success - systematic adherence to core principles separates resilient production systems from brittle ones.

The principle of immutable infrastructure eliminates configuration drift by treating servers as disposable units that are replaced, not modified. This requires upfront investment in automation (Terraform, Packer, Docker) but eliminates entire categories of production failures caused by "snowflake servers" - servers with unique, undocumented configurations that break disaster recovery and scaling. When every deployment is a clean slate, reproducibility becomes automatic.

Observable systems expose the three pillars of instrumentation: metrics for performance monitoring, logs for debugging, and traces for distributed request tracking. Without observability, production debugging is guesswork. Instrument BEFORE deploying, not after incidents occur. Define Service Level Objectives (SLOs) during architecture design, not after availability targets are missed. The incremental cost of instrumentation is trivial compared to the cost of prolonged outages caused by blind spots.

Progressive deployment strategies (canary, blue-green, feature flags) limit blast radius by incrementally rolling out changes to small user cohorts before full production traffic. Deploying directly to 100% of traffic converts minor bugs into major incidents. A canary deployment catching a bug affecting 5% of users is a Tuesday; the same bug affecting 100% of users is a crisis requiring executive escalation and customer notifications.

The specialized sub-skills (Docker containerization, Terraform IaC) provide deep expertise in specific domains, but this parent skill provides the orchestration framework that coordinates their execution. Use the workflows and agent assignments in this skill to systematically provision infrastructure, deploy applications, and maintain production systems with confidence. Infrastructure mastery is not about memorizing tool syntax - it is about applying consistent principles that guarantee reliability, observability, and repeatability across all environments.

## Core Principles

1. **Infrastructure as Code (IaC)** - All infrastructure changes must be codified, version-controlled, and reproducible. Never make manual changes that cannot be recreated through code execution.

2. **Defense in Depth** - Implement multiple layers of security, reliability, and observability. Single points of failure are unacceptable for production systems.

3. **Immutable Infrastructure** - Treat infrastructure as disposable and replaceable. Deploy new instances rather than modifying existing ones to ensure consistency and enable rapid rollback.

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|--------------|-----------------|
| **Manual Configuration** - Making infrastructure changes directly through cloud console or SSH | Creates undocumented drift, prevents reproducibility, breaks disaster recovery | Use IaC tools (Terraform, CloudFormation), codify all changes, apply through CI/CD pipelines |
| **Skipping Multi-Environment Testing** - Deploying directly to production without staging validation | Production incidents from untested changes, no safe rollback path, user impact | Implement dev -> staging -> production pipeline, validate infrastructure changes in staging first |
| **Ignoring State Management** - Not locking or backing up Terraform/IaC state files | State conflicts between team members, lost infrastructure state, inability to manage resources | Use remote state backends (S3 + DynamoDB, Terraform Cloud), enable state locking, automated backups |

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Manual Infrastructure Changes** | Making infrastructure changes through web consoles, SSH, or manual configuration. Creates undocumented state, prevents reproducibility, breaks disaster recovery, violates compliance. Configuration drift accumulates over time. | Enforce Infrastructure as Code (IaC) exclusively. All changes through Terraform/CloudFormation/Ansible with code review and version control. Block manual access to production infrastructure. Use automated compliance scanning (checkov, tfsec) in CI pipeline. |
| **Single Point of Failure Architectures** | Deploying critical components without redundancy (single database, single region, single load balancer). Creates catastrophic failure risk. Minor outages become major incidents. Violates availability SLAs. | Defense in Depth: Multi-AZ database deployments, cross-region replication, multiple load balancer instances, redundant networking. Design for N+1 redundancy minimum. Test failover procedures quarterly. Document RTO/RPO requirements and validate with chaos engineering. |
| **Mutable Infrastructure** | Modifying running servers through configuration management, patches, or manual changes. Creates configuration drift where prod servers diverge from defined state. Rollback becomes impossible. Debugging failures requires forensics. | Immutable Infrastructure: Deploy new instances for every change, never modify running servers. Use golden images (AMI, container images) built in CI. Blue-green deployments for zero-downtime updates. Terminate old instances after validation. Configuration becomes code artifact, not runtime state. |

---

## Conclusion

The infrastructure orchestration skill enables teams to build robust, scalable, and secure cloud infrastructure through systematic automation and best practices. By treating infrastructure as code, implementing proper monitoring and observability, and following defense-in-depth principles, organizations can achieve high availability, rapid deployment, and operational excellence. The skill coordinates specialized sub-skills for Docker containerization and Terraform IaC while providing comprehensive workflows for provisioning, deployment, monitoring, and configuration management.

Success in infrastructure orchestration requires commitment to automation, security-first thinking, and operational discipline. Avoiding anti-patterns like manual configuration changes or skipping multi-environment testing prevents costly production incidents and technical debt. The integration of CI/CD pipelines, comprehensive monitoring, and disaster recovery procedures ensures infrastructure can scale reliably while maintaining security compliance. By following the workflows and best practices outlined in this skill, teams can deliver production-ready infrastructure that meets modern cloud-native standards while remaining maintainable and cost-effective over time.

---

## System Design Integration (Dr. Synthara Methodology)

### Scaling Decision Tree

```
Need to handle more load?
|
+-- Mostly CPU/RAM bound + small scale + OK if brief downtime?
|   +-- Vertical scale (scale up) as short-term patch
|
+-- Need high availability OR growth beyond one machine?
    +-- Horizontal scale (scale out)
        +-- Add load balancer
        +-- Make app tier stateless
        +-- Move state to shared systems (DB/cache/object storage)
```

**System-Designer Thought**: Vertical scaling is a DELAY TACTIC; horizontal scaling is an ARCHITECTURE CHOICE.

### Load Balancer Algorithm Selector

```
Are servers identical + requests similar?
+-- Round robin

Are sessions variable length (long polls, uploads)?
+-- Least connections

Do servers have different capacity?
+-- Weighted RR / Weighted least-connections

Need stickiness without shared session store?
+-- IP hash (but beware NAT skew) / consistent hashing

Global users?
+-- Geo routing + regional LBs
```

**What I'm Thinking**:
- Health checks AREN'T optional
- The LB forces the real question: "Where do sessions live?"
- If you need stickiness, say why
- If you can avoid it, you should

### SPOF Identification & Mitigation Table

| Component | SPOF Risk | Mitigation Strategy |
|-----------|-----------|---------------------|
| **Load Balancer** | Single LB failure | Redundancy, failover, managed LB, multi-AZ |
| **Database** | Single DB failure | Replication + automated failover + backups |
| **Cache** | Cache failure melts DB | Degrade gracefully (cache miss shouldn't melt DB) |
| **Queue** | Message loss | Durable broker, replay strategy, idempotent consumers |
| **DNS** | DNS failure | Multiple DNS providers, low TTL |
| **Secrets** | Vault unavailability | HA Vault cluster, cached secrets with expiry |

**What I'm Thinking**: "How does this fail at 2am under traffic?"
If the answer is "everything stops," you haven't finished.

### Master Design Flow for Infrastructure

```
DESIGN FLOW
1) Define invariants + SLOs
   +-- Uptime target (99.9%? 99.99%?)
   +-- RTO/RPO requirements
2) Model traffic (QPS, burstiness, geo)
3) Scale plan
   +-- vertical (short-term)
   +-- horizontal (LB + stateless)
4) Reliability plan
   +-- remove SPOFs
   +-- replication/failover
   +-- graceful degradation
5) Security plan
   +-- network segmentation
   +-- secrets management
   +-- least privilege
6) Observability + ops
   +-- metrics/logs/traces
   +-- deploy strategy + rollback
```

### Phase 0 Infrastructure Constraint Extraction

| Constraint | Questions |
|------------|-----------|
| **Availability** | SLO (99.9%? 99.99%)? RTO/RPO? |
| **Latency Target** | p50/p95/p99? Global vs regional? |
| **Traffic Model** | QPS now? Growth rate? Burst patterns? |
| **Compliance** | SOC2? HIPAA? PCI-DSS? Data residency? |
| **Cost** | Budget constraints? Cost per request target? |

### The 90-Second Interview Narrative for Infrastructure

1. **Clarify** SLOs, traffic model, compliance
2. **Baseline** single-server and request flow
3. **Identify SPOFs** (compute, DB, network, cache)
4. **Evolve** split tiers -> LB -> stateless app -> DB replication
5. **Reliability** failover, multi-AZ, graceful degradation
6. **Security** network segmentation, secrets, IAM
7. **Observability** logs/metrics/traces, alerting
8. **Trade-offs** cost vs latency vs complexity
