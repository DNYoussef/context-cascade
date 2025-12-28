---
name: aws-specialist
description: AWS cloud specialist for infrastructure as code with CloudFormation/CDK, serverless with Lambda, container orchestration with ECS/Fargate, database management with RDS, storage with S3/CloudFront CDN, and deployment automation. Use when deploying to AWS, optimizing cloud costs, implementing auto-scaling, or requiring AWS-specific best practices. Handles IAM policies, VPC networking, monitoring with CloudWatch, and multi-region deployments.
category: Cloud Platforms
complexity: High
triggers: ["aws", "cloudformation", "lambda", "ecs", "fargate", "rds", "s3", "cloudfront", "aws deployment", "aws cdk", "cloudwatch", "auto-scaling"]
---

# AWS Specialist

Expert AWS cloud infrastructure design, deployment, and optimization for production-grade applications.

## Purpose

Comprehensive AWS expertise across IaC (CloudFormation, CDK), serverless (Lambda), containers (ECS/Fargate), databases (RDS, DynamoDB), storage (S3), CDN (CloudFront), and DevOps automation. Ensures AWS architectures are secure, cost-effective, and scalable.

## When to Use

- Deploying applications to AWS
- Creating infrastructure as code templates
- Setting up serverless architectures
- Configuring auto-scaling and load balancing
- Implementing multi-region deployments
- Optimizing AWS costs (FinOps)
- Securing AWS resources with IAM

## Prerequisites

**Required**: AWS account, AWS CLI installed, basic understanding of cloud concepts

**Agent Assignments**: `cicd-engineer`, `system-architect`, `security-manager`, `perf-analyzer`

## Core Workflows

### Workflow 1: AWS CDK Infrastructure as Code

**Step 1: Initialize CDK Project**

```bash
mkdir my-infra && cd my-infra
npx cdk init app --language typescript
npm install @aws-cdk/aws-lambda @aws-cdk/aws-apigateway @aws-cdk/aws-dynamodb
```

**Step 2: Define Lambda + API Gateway Stack**

```typescript
// lib/api-stack.ts
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';

export class ApiStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // DynamoDB table
    const table = new dynamodb.Table(this, 'ItemsTable', {
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // ONLY for dev
    });

    // Lambda function
    const handler = new lambda.Function(this, 'ItemsHandler', {
      runtime: lambda.Runtime.NODEJS_18_X,
      code: lambda.Code.fromAsset('lambda'),
      handler: 'index.handler',
      environment: {
        TABLE_NAME: table.tableName,
      },
    });

    table.grantReadWriteData(handler);

    // API Gateway
    const api = new apigateway.RestApi(this, 'ItemsApi', {
      restApiName: 'Items Service',
    });

    const items = api.root.addResource('items');
    items.addMethod('GET', new apigateway.LambdaIntegration(handler));
    items.addMethod('POST', new apigateway.LambdaIntegration(handler));
  }
}
```

**Step 3: Deploy Stack**

```bash
# Bootstrap CDK (first time only)
cdk bootstrap

# Deploy
cdk deploy
```

### Workflow 2: ECS Fargate Deployment

**Step 1: Create Fargate Service with CDK**

```typescript
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as elbv2 from 'aws-cdk-lib/aws-elasticloadbalancingv2';

export class FargateStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, 'MyVpc', { maxAzs: 2 });

    const cluster = new ecs.Cluster(this, 'MyCluster', { vpc });

    const taskDefinition = new ecs.FargateTaskDefinition(this, 'TaskDef', {
      memoryLimitMiB: 512,
      cpu: 256,
    });

    taskDefinition.addContainer('web', {
      image: ecs.ContainerImage.fromRegistry('nginx'),
      portMappings: [{ containerPort: 80 }],
      logging: ecs.LogDrivers.awsLogs({ streamPrefix: 'MyApp' }),
    });

    const service = new ecs.FargateService(this, 'Service', {
      cluster,
      taskDefinition,
      desiredCount: 2,
    });

    const lb = new elbv2.ApplicationLoadBalancer(this, 'LB', {
      vpc,
      internetFacing: true,
    });

    const listener = lb.addListener('Listener', { port: 80 });
    listener.addTargets('ECS', {
      port: 80,
      targets: [service],
      healthCheck: { path: '/' },
    });
  }
}
```

### Workflow 3: RDS Database with Backups

```typescript
import * as rds from 'aws-cdk-lib/aws-rds';
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';

const dbSecret = new secretsmanager.Secret(this, 'DBSecret', {
  generateSecretString: {
    secretStringTemplate: JSON.stringify({ username: 'admin' }),
    generateStringKey: 'password',
    excludePunctuation: true,
  },
});

const db = new rds.DatabaseInstance(this, 'MyDatabase', {
  engine: rds.DatabaseInstanceEngine.postgres({
    version: rds.PostgresEngineVersion.VER_15_3,
  }),
  instanceType: ec2.InstanceType.of(
    ec2.InstanceClass.T3,
    ec2.InstanceSize.MICRO
  ),
  vpc,
  credentials: rds.Credentials.fromSecret(dbSecret),
  backupRetention: cdk.Duration.days(7),
  deleteAutomatedBackups: false,
  removalPolicy: cdk.RemovalPolicy.SNAPSHOT,
});
```

### Workflow 4: S3 + CloudFront CDN

```typescript
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';

const bucket = new s3.Bucket(this, 'WebsiteBucket', {
  publicReadAccess: false,
  blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
  removalPolicy: cdk.RemovalPolicy.DESTROY,
  autoDeleteObjects: true,
});

const distribution = new cloudfront.Distribution(this, 'Distribution', {
  defaultBehavior: {
    origin: new origins.S3Origin(bucket),
    viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
  },
  defaultRootObject: 'index.html',
});
```

## Best Practices

**1. Use IAM Least Privilege**
```typescript
// ✅ GOOD: Specific permissions
lambda.addToRolePolicy(new iam.PolicyStatement({
  actions: ['dynamodb:GetItem', 'dynamodb:PutItem'],
  resources: [table.tableArn],
}));

// ❌ BAD: Overly permissive
lambda.addToRolePolicy(new iam.PolicyStatement({
  actions: ['*'],
  resources: ['*'],
}));
```

**2. Enable Encryption**
```typescript
const bucket = new s3.Bucket(this, 'Bucket', {
  encryption: s3.BucketEncryption.S3_MANAGED, // or KMS
});
```

**3. Use Secrets Manager for Credentials**
```typescript
// ✅ GOOD: Secrets Manager
const secret = secretsmanager.Secret.fromSecretNameV2(this, 'Secret', 'my-secret');

// ❌ BAD: Hardcoded in environment
environment: { API_KEY: 'hardcoded-key-123' }
```

**4. Enable Auto-Scaling**
```typescript
const scaling = service.autoScaleTaskCount({ maxCapacity: 10 });
scaling.scaleOnCpuUtilization('CpuScaling', {
  targetUtilizationPercent: 70,
});
```

**5. Cost Optimization**
- Use Spot Instances for non-critical workloads
- Enable S3 Intelligent-Tiering
- Use Lambda for short-lived tasks
- Set up CloudWatch billing alarms

## Quality Criteria

- ✅ Infrastructure defined in code (CDK/CloudFormation)
- ✅ All secrets in Secrets Manager
- ✅ Encryption at rest and in transit
- ✅ Auto-scaling configured
- ✅ CloudWatch monitoring enabled
- ✅ Cost allocation tags applied
- ✅ Multi-AZ for production databases

## Troubleshooting

**Issue**: CDK deployment fails with "not authorized"
**Solution**: Check AWS credentials (`aws sts get-caller-identity`), ensure IAM permissions

**Issue**: Lambda timeout errors
**Solution**: Increase timeout (max 15 minutes), check VPC NAT gateway if Lambda in VPC

**Issue**: High RDS costs
**Solution**: Use Aurora Serverless v2 for variable workloads, stop dev databases overnight

## Related Skills

- `terraform-iac`: Multi-cloud IaC
- `docker-containerization`: Container best practices
- `kubernetes-specialist`: K8s on EKS
- `opentelemetry-observability`: Distributed tracing

## Tools

- AWS CDK: Infrastructure as code in TypeScript/Python
- AWS CLI: Command-line interface
- CloudFormation: Declarative IaC
- Copilot CLI: ECS simplified deployment

## MCP Tools

- `mcp__flow-nexus__sandbox_execute` for AWS CLI commands
- `mcp__memory-mcp__memory_store` for AWS architecture patterns

## Success Metrics

- Deployment time: <15 minutes for full stack
- Infrastructure drift: 0%
- Cost optimization: 20-30% reduction with reserved instances
- Availability: 99.9%+ with multi-AZ

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-11-02

## Core Principles

AWS Specialist operates on 3 fundamental principles:

### Principle 1: Infrastructure as Code - Version Control for Cloud Resources

Manual AWS console configuration creates snowflake environments that cannot be reproduced, audited, or rolled back. Infrastructure as Code (IaC) with CDK/CloudFormation treats infrastructure as software - versioned in Git, peer-reviewed through PRs, and deployed through CI/CD pipelines with automated testing and rollback capabilities.

In practice:
- Define all AWS resources in CDK TypeScript code (Lambda, RDS, VPC, IAM policies) and store in version control
- Use CDK stacks to organize resources by lifecycle (network stack deployed once, application stack updated weekly)
- Implement drift detection to identify manual console changes that violate IaC - automatically revert or alert
- Deploy through CI/CD pipelines with staging environments for validation before production changes

### Principle 2: Least Privilege IAM - Grant Minimum Permissions Required for Task

Overly permissive IAM policies (Action: *, Resource: *) create massive security blast radius - compromised credentials can delete entire AWS accounts. Least privilege IAM grants only the specific actions and resources required for each service, limiting damage from breaches to isolated components.

In practice:
- Define IAM policies with explicit resource ARNs (arn:aws:dynamodb:us-east-1:123456789012:table/Users) instead of wildcards
- Use IAM policy conditions to restrict access by IP range, MFA requirement, or time windows
- Grant Lambda functions only the specific DynamoDB actions needed (GetItem, PutItem) on specific tables, never dynamodb:*
- Review IAM policies quarterly using Access Analyzer to identify unused permissions and remove them

### Principle 3: Cost Optimization Through Right-Sizing and Spot Instances

Default AWS configurations prioritize convenience over cost - on-demand instances, over-provisioned RDS, S3 standard storage. Production-grade architectures optimize costs through reserved instances (60% savings), spot instances for fault-tolerant workloads (70% savings), and intelligent storage tiering (S3 Intelligent-Tiering automatically moves cold data to cheaper tiers).

In practice:
- Use RDS reserved instances for production databases with predictable load (1-year commitment = 40% savings)
- Deploy non-critical batch jobs on Spot instances with interruption handling (spot price = 70% cheaper than on-demand)
- Enable S3 Intelligent-Tiering for data lakes and backups to automatically move cold data to Glacier (80% storage cost reduction)
- Set CloudWatch billing alarms at 50%, 75%, 90% of monthly budget to prevent surprise overages

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Console Cowboy - Manual AWS Console Configuration** | Clicking through AWS console to create resources is fast initially but creates undocumented, unreproducible infrastructure. When production breaks, no one knows how it was configured. Console changes bypass code review and introduce drift. | Define 100% of infrastructure in CDK/CloudFormation code. Enforce through AWS Config rules that alert on manually created resources. Use AWS Service Catalog to provide approved templates for common patterns. Implement drift detection that automatically reverts manual changes. |
| **Secrets in Environment Variables - Hardcode API Keys in Lambda Configuration** | Storing secrets in Lambda environment variables exposes them in CloudFormation templates, console UI, and CloudTrail logs. Anyone with Lambda read permissions can extract production API keys and database credentials. | Use AWS Secrets Manager for all credentials (RDS passwords, API keys, OAuth tokens). Grant Lambda IAM permission to retrieve specific secrets at runtime. Enable automatic rotation for RDS passwords (30-day rotation). Secrets Manager encrypts with KMS and provides audit trail. |
| **Single-AZ Database - RDS in One Availability Zone** | Single-AZ RDS means entire application goes down during AZ failures (happens quarterly in AWS), maintenance windows (weekly), and failover testing. RPO = hours of data loss if AZ fails before latest snapshot. | Enable Multi-AZ for production RDS (automatic failover in 1-2 minutes, synchronous replication = zero data loss). Use Aurora for mission-critical workloads (6 replicas across 3 AZs, <30 second failover). Test failover quarterly to validate runbooks. |

## Conclusion

AWS Specialist provides comprehensive expertise for deploying production-grade applications on AWS through Infrastructure as Code with CDK/CloudFormation, security-hardened IAM policies, and cost-optimized architectures. The skill covers the full AWS service portfolio - serverless with Lambda, containers with ECS/Fargate, databases with RDS/DynamoDB, storage with S3/CloudFront, networking with VPC, and deployment automation with CodePipeline. By implementing the 3 core principles (IaC, least privilege IAM, cost optimization), you build AWS architectures that are reproducible, secure, scalable, and cost-effective.

This skill is essential when migrating applications to AWS, implementing modern cloud-native architectures, or optimizing existing AWS deployments for security and cost. The CDK-first approach enables defining infrastructure in TypeScript with full IDE support (autocomplete, type checking) while automatically generating CloudFormation templates for deployment. This combines the expressiveness of programming languages with the safety of declarative infrastructure. The comprehensive examples for Lambda + API Gateway, ECS Fargate, RDS with automated backups, and S3 + CloudFront CDN provide production-ready templates for common architectural patterns.

The key differentiator is security-by-default through least privilege IAM and Secrets Manager integration. Rather than treating security as an afterthought, the skill embeds IAM best practices into every workflow - explicit resource ARNs, minimal permission sets, MFA requirements, and automatic credential rotation. Combined with cost optimization through reserved instances, spot instances, and intelligent storage tiering, you achieve AWS architectures that are simultaneously secure, scalable, and cost-efficient - the trifecta required for sustainable production operations.
