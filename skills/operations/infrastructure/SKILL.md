/*============================================================================*/
/* SKILL SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: SKILL
version: 1.0.0
description: |
  [assert|neutral] SKILL skill for operations workflows [ground:given] [conf:0.95] [state:confirmed]
category: operations
tags:
- general
author: system
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute SKILL workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic operations processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "SKILL",
  category: "operations",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["SKILL", "operations", "workflow"],
  context: "user needs SKILL capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# Infrastructure Orchestration Skill

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



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
  - Configure envir

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/operations/SKILL/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "SKILL-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>SKILL_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
