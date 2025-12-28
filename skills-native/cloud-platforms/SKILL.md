---
name: cloud-platforms
description: Multi-cloud deployment and infrastructure management across AWS, GCP, and Azure. Use when deploying applications to cloud platforms, implementing serverless architectures, or managing cloud infrastructure as code. Supports containers, serverless, and traditional compute.
---

# Cloud Platforms - Multi-Cloud Infrastructure ⭐ GOLD TIER

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
   - 10 K8s resources with health checks and monitoring

3. **`gcp-config.json`** (8.9 KB)
   - Comprehensive GCP configuration for Cloud Run, GKE, Cloud SQL
   - 9 major configuration sections

4. **`docker-compose.yaml`** (7.5 KB)
   - Full local development stack (11 services)
   - Web, DB, cache, monitoring, worker, scheduler

### Test Suites
Located in `tests/`:

1. **`test-1-aws-deployment.md`** (9 KB)
   - 4 scenarios: Lambda, ECS, Terraform, CloudFormation
   - Complete testing procedures with validation

2. **`test-2-k8s-cluster.md`** (12 KB)
   - 5 scenarios: Local cluster, Helm, ConfigMaps, rolling updates, GKE
   - Performance and load testing included

3. **`test-3-multi-cloud.md`** (19 KB)
   - 5 scenarios: Parallel deploy, DB replication, GeoDNS, cost analysis, DR
   - Multi-cloud best practices and failover testing

## Quick Start Examples

### Deploy to AWS with Terraform
```bash
cd resources/templates
cp aws-infra.tf main.tf
echo 'project_name = "myapp"
environment = "prod"
container_image = "nginx:latest"' > terraform.tfvars

python ../scripts/terraform_apply.py init
python ../scripts/terraform_apply.py apply --var-file terraform.tfvars
```

### Deploy to Kubernetes
```bash
# Using kubectl
./resources/scripts/deploy_k8s.sh kubectl resources/templates/k8s-deployment.yaml production

# Using Helm
./resources/scripts/deploy_k8s.sh helm myapp ./charts/myapp production values.yaml
```

### Deploy to GCP
```bash
# Cloud Run
./resources/scripts/gcp_deploy.sh cloud-run myservice gcr.io/project/image us-central1

# GKE cluster
./resources/scripts/gcp_deploy.sh create-gke mycluster us-central1-a e2-medium 3 true
```

## Multi-Cloud Support

- **AWS:** Lambda, ECS Fargate, EC2, RDS, S3, CloudFormation
- **GCP:** Cloud Run, Cloud Functions, GKE, Cloud SQL, GCR
- **Kubernetes:** GKE, EKS, AKS, Kind, Minikube
- **Infrastructure:** Terraform, Docker Compose

## Testing

Run comprehensive test suites:
```bash
# AWS deployment tests
cd tests
bash test-1-aws-deployment.md

# Kubernetes cluster tests
bash test-2-k8s-cluster.md

# Multi-cloud tests
bash test-3-multi-cloud.md
```

## Documentation

See `ENHANCEMENT-SUMMARY.md` for complete Gold tier enhancement details including:
- All 11 new files created
- Usage examples for each script
- Performance metrics
- Cost estimates
- Troubleshooting guide


## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|--------------|------------------|
| **Manual Console Provisioning** | Creates undocumented infrastructure that cannot be reproduced. Violates compliance requirements and breaks disaster recovery. No code review or version control. | **Always use Infrastructure as Code** (Terraform/CloudFormation). All infrastructure changes must be code-reviewed and version-controlled. Enable CloudTrail auditing for compliance. |
| **Vendor Lock-In Without Justification** | Using cloud-specific services (AWS Lambda, GCP Cloud Functions) without architectural justification makes multi-cloud migration impossible and creates vendor dependency. | **Use portable abstractions** when multi-cloud is required (Kubernetes instead of ECS, PostgreSQL instead of DynamoDB). Accept vendor-specific services ONLY when performance/cost benefits outweigh portability. Document trade-offs explicitly. |
| **Ignoring Multi-Region Deployment** | Single-region deployments create catastrophic failure risk. AWS region outages have lasted hours to days (us-east-1 Dec 2021: 7+ hours). | **Deploy critical services across multiple regions** with active-active or active-passive failover. Use global load balancers (Route 53, Traffic Manager) for automatic failover. Test disaster recovery procedures quarterly. |

-----------|---------|----------|
| **Manual Console Provisioning** | Creating cloud resources through web console GUI instead of Infrastructure as Code. Results in undocumented infrastructure that cannot be reproduced. Violates compliance requirements. No version control or code review. Breaks disaster recovery. | Always use Infrastructure as Code (Terraform/CloudFormation). All infrastructure changes must be code-reviewed, version-controlled, and reproducible. Enable CloudTrail auditing for compliance. Never manual changes - codify everything. |
| **Single-Region Deployment** | Deploying critical services in single AWS/GCP/Azure region. Creates catastrophic failure risk. AWS region outages have lasted 7+ hours (us-east-1 Dec 2021). Single point of failure for entire application. | Deploy critical services across multiple regions with active-active or active-passive failover. Use global load balancers (Route 53, Traffic Manager) for automatic failover. Test disaster recovery procedures quarterly. Multi-region is non-negotiable for production systems. |
| **Vendor Lock-In Without Justification** | Using cloud-specific services (AWS Lambda, GCP Cloud Functions) without architectural justification. Makes multi-cloud migration impossible. Creates vendor dependency with no escape path. | Use portable abstractions when multi-cloud required (Kubernetes vs ECS, PostgreSQL vs DynamoDB). Accept vendor-specific services ONLY when performance/cost benefits outweigh portability loss. Document trade-offs explicitly in architecture decision records. |

---

## Conclusion

Cloud platform mastery requires balancing three competing forces: **speed of delivery**, **cost efficiency**, and **operational reliability**. The skills in this module provide production-ready automation for AWS, GCP, and Azure deployments, but success depends on applying three core principles consistently.

First, treat infrastructure as software. Every resource must be defined in code, version-controlled, and code-reviewed. Manual provisioning creates technical debt that compounds over time - a "snowflake server" that breaks during disaster recovery or fails compliance audits. The upfront investment in Infrastructure as Code pays dividends through reproducible environments, faster disaster recovery, and compliance automation.

Second, design for failure. Cloud services achieve high availability through redundancy, not perfection. Multi-region deployments, circuit breakers, and chaos engineering are not optional luxuries - they are fundamental requirements for production systems. The anti-pattern of single-region deployment has caused countless outages that could have been avoided with proper architectural planning. Test your disaster recovery procedures before you need them, not during an incident.

Third, optimize costs through architectural design, not reactive cost-cutting. Cloud bills grow exponentially when resources are provisioned without consideration for auto-scaling, right-sizing, and lifecycle policies. The difference between a well-architected cloud deployment and an unoptimized one can be 5-10x in monthly costs. Use reserved instances for predictable workloads, spot instances for fault-tolerant batch jobs, and auto-scaling for variable traffic patterns. Monitor spending continuously and set budget alerts to prevent surprises.

The Gold tier resources in this skill (20 files, 4 automation scripts, 4 infrastructure templates, 3 test suites) provide battle-tested patterns for production deployments. Use them as starting points, adapt them to your specific requirements, and always validate through automated testing before production rollout. Cloud mastery is not about memorizing service catalogs - it is about applying consistent principles to deliver reliable, cost-efficient, and secure systems.