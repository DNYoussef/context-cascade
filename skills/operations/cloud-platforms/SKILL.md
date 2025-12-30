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

# Cloud Platforms - Multi-Cloud Infrastructure ⭐ GOLD TIER

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Comprehensive cloud deployment and management for AWS, Google Cloud, and Azure platforms with production-ready automation scripts, infrastructure templates, and multi-cloud testing.

**Tier:** Gold
**Version:** 2.0.0
**Files:** 20
**Scripts:** 4 automation tools
**Templates:** 4 IaC configurations
**Tests:** 3 comprehensive suites

## When to Use This Skill

Use when deploying applications to cloud platforms, implementing serverless architectures (Lambda, Cloud Functions), managing containerized workloads (ECS, GKE, AKS), or provisioning cloud infrastructure with Terraform/CloudFormation.

## Supported Platforms

### AWS (Amazon Web Services)
- **Compute**: EC2, Lambda, ECS, Fargate, Batch
- **Storage**: S3, EBS, EFS, Glacier
- **Database**: RDS, DynamoDB, Aurora, Redshift
- **Networking**: VPC, Route 53, CloudFront, API Gateway
- **IaC**: CloudFormation, AWS CDK

### Google Cloud Platform
- **Compute**: Compute Engine, Cloud Functions, GKE, Cloud Run
- **Storage**: Cloud Storage, Persistent Disk, Filestore
- **Database**: Cloud SQL, Firestore, BigQuery, Spanner
- **Networking**: VPC, Cloud CDN, Cloud Load Balancing
- **IaC**: Deployment Manager, Terraform

### Microsoft Azure
- **Compute**: VMs, Azure Functions, AKS, Container Instances
- **Storage**: Blob Storage, Disk Storage, Azure Files
- **Database**: SQL Database, Cosmos DB, Synapse Analytics
- **Networking**: Virtual Network, Traffic Manager, Front Door
- **IaC**: ARM Templates, Bicep, Terraform

## Process

1. **Define requirements**
   - Determine workload type (compute, storage, database)
   - Assess scaling needs
   - Identify compliance requirements
   - Estimate costs

2. **Select platform and services**
   - Choose cloud provider (AWS/GCP/Azure)
   - Pick appropriate services for workload
   - Design for high availability
   - Plan disaster recovery

3. **Provision infrastructure**
   - Use Infrastructure as Code (Terraform, CloudFormation)
   - Implement security best practices
   - Configure networking and access
   - Set up monitoring and logging

4. **Deploy applications**
   - Containerize with Docker
   - Use CI/CD pipelines
   - Implement blue-green or canary deployments
   - Configure auto-scaling

5. **Monitor and optimize**
   - Track resource utilization
   - Optimize costs (right-sizing, spot instances)
   - Review security posture
   - Implement performance improvements

## Best Practices

- **Multi-region**: Deploy across regions for high availability
- **Infrastructure as Code**: Never provision manually
- **Cost Optimization**: Use reserved instances, spot instances
- **Security**: Least privilege IAM, encryption at rest/transit
- **Monitoring**: CloudWatch, Stackdriver, Azure Monitor

## 🚀 Automation Tools (Gold Tier)

### Deployment Scripts
Located in `resources/scripts/`:

1. **`deploy_aws.py`** (14 KB)
   - AWS Lambda, ECS Fargate, CloudFormation, EC2 deployment
   - Usage: `python deploy_aws.py lambda --name func --zip code.zip --handler index.handler`

2. **`deploy_k8s.sh`** (8.3 KB)
   - Kubernetes kubectl, Helm chart deployment
   - Usage: `./deploy_k8s.sh helm myapp ./charts/app production values.yaml`

3. **`terraform_apply.py`** (13 KB)
   - Terraform automation with validation, planning, state management
   - Usage: `python terraform_apply.py apply --var-file prod.tfvars`

4. **`gcp_deploy.sh`** (10 KB)
   - GCP Cloud Run, Cloud Functions, GKE, Compute Engine deployment
   - Usage: `./gcp_deploy.sh cloud-run myservice gcr.io/project/image us-central1`

### Infrastructure Templates
Located in `resources/templates/`:

1. **`aws-infra.tf`** (14 KB)
   - Complete AWS VPC, ALB, ECS Fargate, RDS setup
   - 30+ Terraform resources for production deployment

2. **`k8s-deployment.yaml`** (7.2 KB)
   - Production Kubernetes manifest with HPA, Ingress, PDB
   - 10 K8s resources with health checks and monit

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
