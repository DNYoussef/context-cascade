---
name: sop-product-launch
description: Complete product launch workflow coordinating 15+ specialist agents across research, development, marketing, sales, and operations. Uses sequential and parallel orchestration for 10-week launch timeline.
---

# SOP: Product Launch Workflow

Complete end-to-end product launch process using multi-agent coordination.

## Timeline: 10 Weeks

**Phases**:
1. Research & Planning (Week 1-2)
2. Product Development (Week 3-6)
3. Marketing & Sales Prep (Week 5-8)
4. Launch Execution (Week 9)
5. Post-Launch Monitoring (Week 10+)

## Phase 2: Product Development (Week 3-6)

### Week 3-4: Technical Architecture & Development

**Parallel Workflow** (Backend + Frontend + Mobile):

```javascript
// Initialize development swarm
await mcp__ruv-swarm__swarm_init({
  topology: 'mesh',
  maxAgents: 6,
  strategy: 'adaptive'
});

// Parallel agent spawning
const [backend, frontend, mobile, database, security, tester] = await Promise.all([
  Task("Backend Developer", `
Using product requirements from: product-strategy/product-launch-2024/plan

Build:
- REST API with authentication
- Database schema and migrations
- Business logic layer
- Integration with payment gateway

Store API spec: backend-dev/product-launch-2024/api-spec
Store schema: backend-dev/product-launch-2024/db-schema
`, "backend-dev"),

  Task("Frontend Developer", `
Using API spec from: backend-dev/product-launch-2024/api-spec

Build:
- React web application
- Component library
- State management (Redux/Context)
- API integration layer

Store components: frontend-dev/product-launch-2024/components
`, "coder"),

  Task("Mobile Developer", `
Using API spec from: backend-dev/product-launch-2024/api-spec

Build:
- React Native mobile app (iOS + Android)
- Native modules for device features
- Offline sync capability
- Push notifications

Store builds: mobile-dev/product-launch-2024/builds
`, "mobile-dev"),

  Task("Database Architect", `
Design optimized database:
- Schema design for scalability
- Indexing strategy
- Query optimization
- Backup and recovery plan

Store: database/product-launch-2024/architecture
`, "code-analyzer"),

  Task("Security Specialist", `
Implement security:
- Authentication (OAuth 2.0 + JWT)
- Authorization (RBAC)
- Data encryption (at rest + in transit)
- Security audit and penetration testing

Store audit: security/product-launch-2024/audit
`, "reviewer"),

  Task("QA Engineer", `
Create test suite:
- Unit tests (90%+ coverage)
- Integration tests
- E2E tests
- Performance tests
- Security tests

Store test plan: testing/product-launch-2024/plan
`, "tester")
]);

// Wait for all parallel tasks to complete
await Promise.all([backend, frontend, mobile, database, security, tester]);
```

### Week 5-6: Integration & Testing

**Sequential Workflow**:

```javascript
// Step 1: System Integration
await Task("System Integrator", `
Integrate all components:
- Backend API + Frontend web
- Backend API + Mobile apps
- Payment gateway integration
- Third-party services

Run integration tests
Store integration report: integration/product-launch-2024/report
`, "reviewer");

// Step 2: Performance Optimization
await Task("Performance Optimizer", `
Optimize system performance:
- API response time < 200ms
- Frontend load time < 2s
- Mobile app startup < 1s
- Database query optimization

Run benchmarks
Store metrics: performance/product-launch-2024/metrics
`, "perf-analyzer");

// Step 3: Security Audit
await Task("Security Auditor", `
Final security audit:
- Vulnerability scanning
- Penetration testing
- Compliance check (GDPR, CCPA)
- Security best practices review

Generate compliance report
Store: security/product-launch-2024/final-audit
`, "security-manager");
```

**Deliverables**:
- Production-ready application (Web + Mobile)
- API documentation
- Security audit report
- Performance benchmarks

## Phase 4: Launch Execution (Week 9)

### Launch Week: Coordinated Execution

**Sequential + Parallel**:

```javascript
// Day 1: Final Pre-Launch Checks
await Task("Production Validator", `
Final validation checklist:
- All tests passing (unit, integration, E2E)
- Security audit complete and passed
- Performance benchmarks met
- Monitoring and alerting active
- Backup and recovery tested
- Rollback plan ready

Generate go/no-go report
Store: validation/product-launch-2024/final-check
`, "production-validator");

// Day 2: Deployment
await Task("DevOps Engineer", `
Production deployment:
- Deploy backend to production (blue-green)
- Deploy frontend to CDN
- Submit mobile apps to App Store + Play Store
- Configure production databases
- Enable monitoring and alerting

Store deployment report: devops/product-launch-2024/deployment
`, "cicd-engineer");

// Day 3-4: Launch Marketing (Parallel)
const [emailCampaign, socialCampaign, paidAds, prOutreach] = await Promise.all([
  Task("Email Marketing", `
Execute email campaign:
- Send launch announcement to existing list
- Trigger automated welcome sequences
- Monitor open rates, click rates

Store metrics: marketing/product-launch-2024/email-metrics
`, "researcher"),

  Task("Social Media", `
Execute social campaign:
- Post launch announcements (all channels)
- Engage with audience comments
- Share user testimonials and demos

Store metrics: marketing/product-launch-2024/social-metrics
`, "researcher"),

  Task("Paid Advertising", `
Launch paid campaigns:
- Google Ads (Search + Display)
- Facebook/Instagram Ads
- LinkedIn Ads (if B2B)
- Monitor ROI and adjust bids

Store metrics: marketing/product-launch-2024/ad-metrics
`, "researcher"),

  Task("PR Outreach", `
Media and influencer outreach:
- Send press releases
- Influencer partnerships
- Product Hunt launch
- Tech blog features

Store coverage: marketing/product-launch-2024/pr-coverage
`, "researcher")
]);

// Day 5: Monitor and Optimize
await Task("Analytics Monitor", `
Real-time monitoring:
- Application performance and uptime
- User signups and activation rates
- Marketing campaign performance
- Customer support ticket volume
- Revenue and conversion tracking

Generate daily reports
Store: analytics/product-launch-2024/daily-metrics
`, "performance-monitor");
```

**Deliverables**:
- Live production application
- Active marketing campaigns across all channels
- Sales team actively selling
- Support team handling inquiries

## Success Metrics

### Technical Metrics
- **Uptime**: 99.9%+
- **API Response Time**: < 200ms (p95)
- **Page Load Time**: < 2s
- **Error Rate**: < 0.1%
- **Test Coverage**: > 90%

### Business Metrics
- **User Signups**: Target (defined in strategy)
- **Activation Rate**: > 40%
- **Conversion Rate**: > 2.5%
- **Customer Acquisition Cost**: < $X (defined)
- **Monthly Recurring Revenue**: Target (defined)
- **Churn Rate**: < 5%

### Marketing Metrics
- **Campaign ROI**: > 3:1
- **Email Open Rate**: > 25%
- **Social Engagement**: > 5%
- **Paid Ad CTR**: > 2%
- **Organic Traffic Growth**: > 20% MoM

### Support Metrics
- **Response Time**: < 2 hours
- **Resolution Time**: < 24 hours
- **Customer Satisfaction**: > 4.5/5
- **Self-Service Rate**: > 60%

## Usage

```javascript
// Invoke this SOP skill
Skill("sop-product-launch")

// Or use with Claude Code Task tool for full orchestration
Task("Product Launch Orchestrator", "Execute complete product launch using SOP", "planner")
```

## Core Principles

SOP: Product Launch operates on 3 fundamental principles:

### Principle 1: Coordinated Multi-Channel Execution
Product launches require simultaneous coordination across technical development, marketing campaigns, sales enablement, and operational readiness. Sequential execution creates gaps where momentum is lost.

In practice:
- Development, marketing, and sales work streams run in parallel phases
- Coordination through shared memory namespaces ensures alignment
- Phase gates prevent downstream teams from blocking on incomplete upstream work

### Principle 2: Evidence-Based Milestone Validation
Each phase must produce measurable artifacts that validate readiness for the next phase. Subjective "done" assessments lead to launch failures.

In practice:
- Technical gates: All tests passing, security audit complete, performance benchmarks met
- Marketing gates: Campaign assets complete, A/B tests run, analytics configured
- Sales gates: Enablement materials ready, CRM configured, support trained

### Principle 3: Rollback-First Deployment Strategy
Launch failures are inevitable. The difference between recoverable incidents and catastrophic failures is having tested rollback procedures before deployment.

In practice:
- Blue-green deployments with instant traffic switching
- Database migration rollback scripts tested in staging
- Communication templates pre-written for rollback scenarios

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Waterfall Launch** | Development completes, THEN marketing starts, THEN sales prepares. Launch delayed by 2-3x. | Run development, marketing, and sales in parallel phases (Week 3-8). Use memory coordination for dependencies. |
| **Launch Without Metrics** | "We launched!" but no way to measure success. Teams argue about what worked. | Configure analytics, monitoring, and dashboards BEFORE launch (Week 7-8). Define success metrics in Week 1. |
| **No Rollback Plan** | Launch fails, team scrambles to fix in production. Downtime extends for hours/days. | Document and TEST rollback procedures in Week 8. Practice rollback in staging environment. |

## Conclusion

SOP: Product Launch provides a battle-tested 10-week framework for coordinating 15+ specialist agents across research, development, marketing, sales, and operations. The key insight is parallelization - development, marketing, and sales work streams run concurrently, coordinated through shared memory namespaces and phase gates. This reduces launch timeline from 18-24 weeks (sequential) to 10 weeks (parallel).

Use this skill when launching new products, major features, or market expansions requiring cross-functional coordination. The hybrid sequential-parallel pattern ensures critical dependencies are respected (research before development) while maximizing throughput (backend + frontend + mobile development in parallel).

The framework scales from MVP launches (6-8 weeks, 10 agents) to enterprise launches (12-16 weeks, 20+ agents) by adjusting phase durations and agent counts. Success requires rigorous milestone validation at each phase gate - subjective "done" assessments are the primary cause of launch delays and failures.