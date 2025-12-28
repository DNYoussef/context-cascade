---
name: flow-nexus-platform
description: Comprehensive Flow Nexus platform management - authentication, sandboxes, app deployment, payments, and challenges (Gold Tier)
---

## When NOT to Use This Skill

- Local development without cloud infrastructure needs
- Simple scripts that do not require sandboxed execution
- Operations without distributed computing requirements
- Tasks that can run on single-machine environments

## Success Criteria

- API response time: <200ms for sandbox creation
- Deployment success rate: >99%
- Sandbox startup time: <5s
- Network latency: <50ms between sandboxes
- Resource utilization: <80% CPU/memory per sandbox
- Uptime: >99.9% for production deployments

## Edge Cases & Error Handling

- **Rate Limits**: Flow Nexus API has request limits; implement queuing and backoff
- **Authentication Failures**: Validate API tokens before operations; refresh expired tokens
- **Network Issues**: Retry failed requests with exponential backoff (max 5 retries)
- **Quota Exhaustion**: Monitor sandbox/compute quotas; alert before limits
- **Sandbox Timeouts**: Set appropriate timeout values; clean up orphaned sandboxes
- **Deployment Failures**: Implement rollback strategies; maintain previous working state

## Guardrails & Safety

- NEVER expose API keys or authentication tokens in code or logs
- ALWAYS validate responses from Flow Nexus API before processing
- ALWAYS implement timeout limits for long-running operations
- NEVER trust user input for sandbox commands without validation
- ALWAYS monitor resource usage to prevent runaway processes
- ALWAYS clean up sandboxes and resources after task completion

## Evidence-Based Validation

- Verify platform health: Check Flow Nexus status endpoint before operations
- Validate deployments: Test sandbox connectivity and functionality
- Monitor costs: Track compute usage and spending against budgets
- Test failure scenarios: Simulate network failures, timeouts, auth errors
- Benchmark performance: Compare actual vs expected latency/throughput


# Flow Nexus Platform Management

**Gold Tier Skill**: Comprehensive platform management for Flow Nexus with 4 automation scripts, 3 configuration templates, and comprehensive test suites - covering authentication, sandbox execution, app deployment, credit management, and coding challenges.

## Quick Access

- **Scripts**: `resources/scripts/` - 4 platform automation tools
- **Templates**: `resources/templates/` - 3 configuration templates
- **Tests**: `tests/` - 3 comprehensive test suites
- **Process Diagram**: `flow-nexus-platform-process.dot` - Visual workflow

## Automation Scripts

This skill includes functional automation scripts for streamlined platform operations:

### 1. Authentication Manager (`auth-manager.js`)

Automate user authentication workflows:

```bash
# Register new user
node resources/scripts/auth-manager.js register user@example.com SecurePass123 "John Doe"

# Login
node resources/scripts/auth-manager.js login user@example.com SecurePass123

# Check authentication status
node resources/scripts/auth-manager.js status --detailed

# Update profile
node resources/scripts/auth-manager.js update-profile user123 bio="AI Developer" github_username=johndoe

# Upgrade tier
node resources/scripts/auth-manager.js upgrade user123 pro
```

### 2. Sandbox Manager (`sandbox-manager.js`)

Manage sandbox lifecycle with a single script:

```bash
# Create sandbox with packages
node resources/scripts/sandbox-manager.js create node my-api --env PORT=3000 NODE_ENV=dev --packages express,cors

# List all sandboxes
node resources/scripts/sandbox-manager.js list --status running

# Execute code
node resources/scripts/sandbox-manager.js execute sbx_123 "console.log('Hello')"
node resources/scripts/sandbox-manager.js execute sbx_123 @script.js

# Upload file
node resources/scripts/sandbox-manager.js upload sbx_123 ./config.json /app/config.json

# View logs
node resources/scripts/sandbox-manager.js logs sbx_123 --lines 100

# Cleanup old sandboxes
node resources/scripts/sandbox-manager.js cleanup-all --older-than-hours 24
```

### 3. Deployment Manager (`deployment-manager.js`)

Automate application deployment:

```bash
# Browse templates
node resources/scripts/deployment-manager.js list-templates --category web-api --featured

# Get template details
node resources/scripts/deployment-manager.js template-info express-api-starter

# Deploy application
node resources/scripts/deployment-manager.js deploy express-api-starter my-production-api --var database_url=postgres://...

# Publish your app
node resources/scripts/deployment-manager.js publish "JWT Auth Service" "Production JWT auth" backend ./auth-service.js --tags auth,jwt,security

# Search apps
node resources/scripts/deployment-manager.js search "authentication" --category backend

# View analytics
node resources/scripts/deployment-manager.js analytics app_123 --timeframe 30d
```

### 4. Platform Health Monitor (`platform-health.js`)

Monitor system health and manage credits:

```bash
# Check platform health
node resources/scripts/platform-health.js check --detailed

# Check credit balance
node resources/scripts/platform-health.js credits --history

# Create payment link
node resources/scripts/platform-health.js payment-link 50

# Configure auto-refill
node resources/scripts/platform-health.js auto-refill enable --threshold 100 --amount 50

# View audit logs
node resources/scripts/platform-health.js audit-log --limit 100

# Get user statistics
node resources/scripts/platform-health.js user-stats user123

# Market data
node resources/scripts/platform-health.js market-data
```

## Configuration Templates

Three production-ready configuration templates in `resources/templates/`:

### 1. Platform Configuration (`platform-config.json`)

Complete platform settings including authentication, sandboxes, deployment, credits, monitoring, and integrations.

### 2. Sandbox Configuration (`sandbox-config.yaml`)

Comprehensive sandbox setup with environment variables, packages, lifecycle hooks, network configuration, and security settings.

### 3. Deployment Manifest (`deployment-manifest.yaml`)

Enterprise-grade deployment configuration with autoscaling, health checks, monitoring, CI/CD integration, and rollback strategies.

## Table of Contents
1. [Authentication & User Management](#authentication--user-management)
2. [Sandbox Management](#sandbox-management)
3. [App Store & Deployment](#app-store--deployment)
4. [Payments & Credits](#payments--credits)
5. [Challenges & Achievements](#challenges--achievements)
6. [Storage & Real-time](#storage--real-time)
7. [System Utilities](#system-utilities)



## Sandbox Management

### Create & Configure Sandboxes

**Create Sandbox**
```javascript
mcp__flow-nexus__sandbox_create({
  template: "node", // node, python, react, nextjs, vanilla, base, claude-code
  name: "my-sandbox",
  env_vars: {
    API_KEY: "your_api_key",
    NODE_ENV: "development",
    DATABASE_URL: "postgres://..."
  },
  install_packages: ["express", "cors", "dotenv"],
  startup_script: "npm run dev",
  timeout: 3600, // seconds
  metadata: {
    project: "my-project",
    environment: "staging"
  }
})
```

**Configure Existing Sandbox**
```javascript
mcp__flow-nexus__sandbox_configure({
  sandbox_id: "sandbox_id",
  env_vars: {
    NEW_VAR: "value"
  },
  install_packages: ["axios", "lodash"],
  run_commands: ["npm run migrate", "npm run seed"],
  anthropic_key: "sk-ant-..." // For Claude Code integration
})
```

### Execute Code

**Run Code in Sandbox**
```javascript
mcp__flow-nexus__sandbox_execute({
  sandbox_id: "sandbox_id",
  code: `
    console.log('Hello from sandbox!');
    const result = await fetch('https://api.example.com/data');
    const data = await result.json();
    return data;
  `,
  language: "javascript",
  capture_output: true,
  timeout: 60, // seconds
  working_dir: "/app",
  env_vars: {
    TEMP_VAR: "override"
  }
})
```

### Manage Sandboxes

**List Sandboxes**
```javascript
mcp__flow-nexus__sandbox_list({
  status: "running" // running, stopped, all
})
```

**Get Sandbox Status**
```javascript
mcp__flow-nexus__sandbox_status({
  sandbox_id: "sandbox_id"
})
```

**Upload File to Sandbox**
```javascript
mcp__flow-nexus__sandbox_upload({
  sandbox_id: "sandbox_id",
  file_path: "/app/config/database.json",
  content: JSON.stringify(databaseConfig, null, 2)
})
```

**Get Sandbox Logs**
```javascript
mcp__flow-nexus__sandbox_logs({
  sandbox_id: "sandbox_id",
  lines: 100 // max 1000
})
```

**Stop Sandbox**
```javascript
mcp__flow-nexus__sandbox_stop({
  sandbox_id: "sandbox_id"
})
```

**Delete Sandbox**
```javascript
mcp__flow-nexus__sandbox_delete({
  sandbox_id: "sandbox_id"
})
```

### Sandbox Templates

- **node**: Node.js environment with npm
- **python**: Python 3.x with pip
- **react**: React development setup
- **nextjs**: Next.js full-stack framework
- **vanilla**: Basic HTML/CSS/JS
- **base**: Minimal Linux environment
- **claude-code**: Claude Code integrated environment

### Common Sandbox Patterns

**API Development Sandbox**
```javascript
mcp__flow-nexus__sandbox_create({
  template: "node",
  name: "api-development",
  install_packages: [
    "express",
    "cors",
    "helmet",
    "dotenv",
    "jsonwebtoken",
    "bcrypt"
  ],
  env_vars: {
    PORT: "3000",
    NODE_ENV: "development"
  },
  startup_script: "npm run dev"
})
```

**Machine Learning Sandbox**
```javascript
mcp__flow-nexus__sandbox_create({
  template: "python",
  name: "ml-training",
  install_packages: [
    "numpy",
    "pandas",
    "scikit-learn",
    "matplotlib",
    "tensorflow"
  ],
  env_vars: {
    CUDA_VISIBLE_DEVICES: "0"
  }
})
```

**Full-Stack Development**
```javascript
mcp__flow-nexus__sandbox_create({
  template: "nextjs",
  name: "fullstack-app",
  install_packages: [
    "prisma",
    "@prisma/client",
    "next-auth",
    "zod"
  ],
  env_vars: {
    DATABASE_URL: "postgresql://...",
    NEXTAUTH_SECRET: "secret"
  }
})
```



## Payments & Credits

### Balance & Credits

**Check Credit Balance**
```javascript
mcp__flow-nexus__check_balance()
```

**Check rUv Balance**
```javascript
mcp__flow-nexus__ruv_balance({
  user_id: "your_user_id"
})
```

**View Transaction History**
```javascript
mcp__flow-nexus__ruv_history({
  user_id: "your_user_id",
  limit: 100
})
```

**Get Payment History**
```javascript
mcp__flow-nexus__get_payment_history({
  limit: 50
})
```

### Purchase Credits

**Create Payment Link**
```javascript
mcp__flow-nexus__create_payment_link({
  amount: 50 // USD, minimum $10
})
// Returns secure Stripe payment URL
```

### Auto-Refill Configuration

**Enable Auto-Refill**
```javascript
mcp__flow-nexus__configure_auto_refill({
  enabled: true,
  threshold: 100,  // Refill when credits drop below 100
  amount: 50       // Purchase $50 worth of credits
})
```

**Disable Auto-Refill**
```javascript
mcp__flow-nexus__configure_auto_refill({
  enabled: false
})
```

### Credit Pricing

**Service Costs:**
- **Swarm Operations**: 1-10 credits/hour
- **Sandbox Execution**: 0.5-5 credits/hour
- **Neural Training**: 5-50 credits/job
- **Workflow Runs**: 0.1-1 credit/execution
- **Storage**: 0.01 credits/GB/day
- **API Calls**: 0.001-0.01 credits/request

### Earning Credits

**Ways to Earn:**
1. **Complete Challenges**: 10-500 credits per challenge
2. **Publish Templates**: Earn when others deploy (you set pricing)
3. **Referral Program**: Bonus credits for user invites
4. **Daily Login**: Small daily bonus (5-10 credits)
5. **Achievements**: Unlock milestone rewards (50-1000 credits)
6. **App Store Sales**: Revenue share from paid templates

**Earn Credits Programmatically**
```javascript
mcp__flow-nexus__app_store_earn_ruv({
  user_id: "your_user_id",
  amount: 100,
  reason: "Completed expert algorithm challenge",
  source: "challenge" // challenge, app_usage, referral, etc.
})
```

### Subscription Tiers

**Free Tier**
- 100 free credits monthly
- Basic sandbox access (2 concurrent)
- Limited swarm agents (3 max)
- Community support
- 1GB storage

**Pro Tier ($29/month)**
- 1000 credits monthly
- Priority sandbox access (10 concurrent)
- Unlimited swarm agents
- Advanced workflows
- Email support
- 10GB storage
- Early access to features

**Enterprise Tier (Custom Pricing)**
- Unlimited credits
- Dedicated compute resources
- Custom neural models
- 99.9% SLA guarantee
- Priority 24/7 support
- Unlimited storage
- White-label options
- On-premise deployment

### Cost Optimization Tips

1. **Use Smaller Sandboxes**: Choose appropriate templates (base vs full-stack)
2. **Optimize Neural Training**: Tune hyperparameters, reduce epochs
3. **Batch Operations**: Group workflow executions together
4. **Clean Up Resources**: Delete unused sandboxes and storage
5. **Monitor Usage**: Check `user_stats` regularly
6. **Use Free Templates**: Leverage community templates
7. **Schedule Off-Peak**: Run heavy jobs during low-cost periods



## Storage & Real-time

### File Storage

**Upload File**
```javascript
mcp__flow-nexus__storage_upload({
  bucket: "my-bucket", // public, private, shared, temp
  path: "data/users.json",
  content: JSON.stringify(userData, null, 2),
  content_type: "application/json"
})
```

**List Files**
```javascript
mcp__flow-nexus__storage_list({
  bucket: "my-bucket",
  path: "data/", // prefix filter
  limit: 100
})
```

**Get Public URL**
```javascript
mcp__flow-nexus__storage_get_url({
  bucket: "my-bucket",
  path: "data/report.pdf",
  expires_in: 3600 // seconds (default: 1 hour)
})
```

**Delete File**
```javascript
mcp__flow-nexus__storage_delete({
  bucket: "my-bucket",
  path: "data/old-file.json"
})
```

### Storage Buckets

- **public**: Publicly accessible files (CDN-backed)
- **private**: User-only access with authentication
- **shared**: Team collaboration with ACL
- **temp**: Auto-deleted after 24 hours

### Real-time Subscriptions

**Subscribe to Database Changes**
```javascript
mcp__flow-nexus__realtime_subscribe({
  table: "tasks",
  event: "INSERT", // INSERT, UPDATE, DELETE, *
  filter: "status=eq.pending AND priority=eq.high"
})
```

**List Active Subscriptions**
```javascript
mcp__flow-nexus__realtime_list()
```

**Unsubscribe**
```javascript
mcp__flow-nexus__realtime_unsubscribe({
  subscription_id: "subscription_id"
})
```

### Execution Monitoring

**Subscribe to Execution Stream**
```javascript
mcp__flow-nexus__execution_stream_subscribe({
  stream_type: "claude-flow-swarm", // claude-code, claude-flow-swarm, claude-flow-hive-mind, github-integration
  deployment_id: "deployment_id",
  sandbox_id: "sandbox_id" // alternative
})
```

**Get Stream Status**
```javascript
mcp__flow-nexus__execution_stream_status({
  stream_id: "stream_id"
})
```

**List Generated Files**
```javascript
mcp__flow-nexus__execution_files_list({
  stream_id: "stream_id",
  created_by: "claude-flow", // claude-code, claude-flow, git-clone, user
  file_type: "javascript" // filter by extension
})
```

**Get File Content from Execution**
```javascript
mcp__flow-nexus__execution_file_get({
  file_id: "file_id",
  file_path: "/path/to/file.js" // alternative
})
```



## Quick Start Guide

### Step 1: Register & Login

```javascript
// Register
mcp__flow-nexus__user_register({
  email: "dev@example.com",
  password: "SecurePass123!",
  full_name: "Developer Name"
})

// Login
mcp__flow-nexus__user_login({
  email: "dev@example.com",
  password: "SecurePass123!"
})

// Check auth status
mcp__flow-nexus__auth_status({ detailed: true })
```

### Step 2: Configure Billing

```javascript
// Check current balance
mcp__flow-nexus__check_balance()

// Add credits
const paymentLink = mcp__flow-nexus__create_payment_link({
  amount: 50 // $50
})

// Setup auto-refill
mcp__flow-nexus__configure_auto_refill({
  enabled: true,
  threshold: 100,
  amount: 50
})
```

### Step 3: Create Your First Sandbox

```javascript
// Create development sandbox
const sandbox = mcp__flow-nexus__sandbox_create({
  template: "node",
  name: "dev-environment",
  install_packages: ["express", "dotenv"],
  env_vars: {
    NODE_ENV: "development"
  }
})

// Execute code
mcp__flow-nexus__sandbox_execute({
  sandbox_id: sandbox.id,
  code: 'console.log("Hello Flow Nexus!")',
  language: "javascript"
})
```

### Step 4: Deploy an App

```javascript
// Browse templates
mcp__flow-nexus__template_list({
  category: "backend",
  featured: true
})

// Deploy template
mcp__flow-nexus__template_deploy({
  template_name: "express-api-starter",
  deployment_name: "my-api",
  variables: {
    database_url: "postgres://..."
  }
})
```

### Step 5: Complete a Challenge

```javascript
// Find challenges
mcp__flow-nexus__challenges_list({
  difficulty: "beginner",
  category: "algorithms"
})

// Submit solution
mcp__flow-nexus__challenge_submit({
  challenge_id: "fizzbuzz",
  user_id: "your_id",
  solution_code: "...",
  language: "javascript"
})
```



## Troubleshooting

### Authentication Issues
- **Login Failed**: Check email/password, verify email first
- **Token Expired**: Re-login to get fresh tokens
- **Permission Denied**: Check tier limits, upgrade if needed

### Sandbox Issues
- **Sandbox Won't Start**: Check template compatibility, verify credits
- **Execution Timeout**: Increase timeout parameter or optimize code
- **Out of Memory**: Use larger template or optimize memory usage
- **Package Install Failed**: Check package name, verify npm/pip availability

### Payment Issues
- **Payment Failed**: Check payment method, sufficient funds
- **Credits Not Applied**: Allow 5-10 minutes for processing
- **Auto-refill Not Working**: Verify payment method on file

### Challenge Issues
- **Submission Rejected**: Check code syntax, ensure all tests pass
- **Wrong Answer**: Review test cases, check edge cases
- **Performance Too Slow**: Optimize algorithm complexity



## Progressive Disclosure

<details>
<summary><strong>Advanced Sandbox Configuration</strong></summary>

### Custom Docker Images
```javascript
mcp__flow-nexus__sandbox_create({
  template: "base",
  name: "custom-environment",
  startup_script: `
    apt-get update
    apt-get install -y custom-package
    git clone https://github.com/user/repo
    cd repo && npm install
  `
})
```

### Multi-Stage Execution
```javascript
// Stage 1: Setup
mcp__flow-nexus__sandbox_execute({
  sandbox_id: "id",
  code: "npm install && npm run build"
})

// Stage 2: Run
mcp__flow-nexus__sandbox_execute({
  sandbox_id: "id",
  code: "npm start",
  working_dir: "/app/dist"
})
```

</details>

<details>
<summary><strong>Advanced Storage Patterns</strong></summary>

### Large File Upload (Chunked)
```javascript
const chunkSize = 5 * 1024 * 1024 // 5MB chunks
for (let i = 0; i < chunks.length; i++) {
  await mcp__flow-nexus__storage_upload({
    bucket: "private",
    path: `large-file.bin.part${i}`,
    content: chunks[i]
  })
}
```

### Storage Lifecycle
```javascript
// Upload to temp for processing
mcp__flow-nexus__storage_upload({
  bucket: "temp",
  path: "processing/data.json",
  content: data
})

// Move to permanent storage after processing
mcp__flow-nexus__storage_upload({
  bucket: "private",
  path: "archive/processed-data.json",
  content: processedData
})
```

</details>

<details>
<summary><strong>Advanced Real-time Patterns</strong></summary>

### Multi-Table Sync
```javascript
const tables = ["users", "tasks", "notifications"]
tables.forEach(table => {
  mcp__flow-nexus__realtime_subscribe({
    table,
    event: "*",
    filter: `user_id=eq.${userId}`
  })
})
```

### Event-Driven Workflows
```javascript
// Subscribe to task completion
mcp__flow-nexus__realtime_subscribe({
  table: "tasks",
  event: "UPDATE",
  filter: "status=eq.completed"
})

// Trigger notification workflow on event
// (handled by your application logic)
```

</details>



**Skill Tier**: Gold (13 files: 1 SKILL.md + 4 scripts + 3 templates + 3 tests + 1 process diagram + 1 resources README)

*This skill consolidates 6 Flow Nexus command modules into a single comprehensive platform management interface with full automation capabilities.*

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Hardcoded API Keys** | Exposing authentication tokens in code or logs creates security vulnerabilities | Use environment variables via `env_vars` parameter in sandbox creation; never log credentials |
| **Orphaned Sandboxes** | Leaving sandboxes running after task completion wastes credits and resources | Always destroy sandboxes explicitly or set `timeout` parameter; use cleanup scripts for batch operations |
| **Ignoring Credit Limits** | Operations fail mid-execution when credits run out, losing progress | Check `check_balance()` before expensive operations; configure `auto_refill` with appropriate thresholds |
| **Manual Template Replication** | Repeatedly creating identical sandbox configurations is error-prone and slow | Use `template_deploy()` for standardized environments; publish reusable templates to app store |
| **Sync-Only Workflow Execution** | Blocking on long-running workflows prevents parallel operations | Use `async: true` for workflows >60s; monitor with `workflow_queue_status()` |

---

## Conclusion

The Flow Nexus Platform skill provides comprehensive cloud infrastructure management for AI-assisted development workflows. By combining ephemeral sandbox execution, credit-based metering, and gamified skill-building, it enables scalable development without local infrastructure overhead.

Use this skill when you need isolated execution environments, distributed compute resources, or cloud-based app deployment. The platform shines for teams requiring multi-user collaboration, auto-scaling workloads, or pay-per-use resource models. With 4 automation scripts, 3 production-ready templates, and comprehensive test coverage, this Gold-tier skill delivers enterprise-grade platform orchestration.

Key takeaways: Leverage sandbox templates for consistency, monitor credit usage to optimize costs, and publish successful configurations as templates to build passive credit income. The platform's event-driven architecture, real-time subscriptions, and Queen Seraphina AI assistant provide advanced capabilities for sophisticated workflows.