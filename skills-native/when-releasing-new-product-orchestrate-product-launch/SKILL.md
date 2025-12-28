---
name: when-releasing-new-product-orchestrate-product-launch
description: | Use when launching a new product end-to-end from market research through post-launch monitoring. Orchestrates 15+ specialist agents across 5 phases in a 10-week coordinated workflow including research, development, marketing, sales preparation, launch execution, and ongoing optimization. Employs hierarchical coordination with parallel execution for efficiency and comprehensive coverage.
---

# Product Launch Orchestration Workflow

Complete end-to-end product launch workflow orchestrating 15+ specialist agents across research, development, marketing, launch execution, and post-launch monitoring. Designed for comprehensive product launches requiring coordination across technical, marketing, sales, and operations teams.

## Overview

This SOP orchestrates a complete 10-week product launch using multi-agent coordination with hierarchical topology. The workflow balances sequential dependencies with parallel execution to optimize both speed and quality. Each phase produces specific deliverables stored in memory for subsequent phases to consume, ensuring continuity and context preservation.

## Trigger Conditions

Use this workflow when:
- Launching a new product or major feature requiring comprehensive go-to-market
- Coordinating across multiple teams (engineering, marketing, sales, support)
- Need systematic approach covering all launch aspects from research to post-launch
- Timeline spans multiple weeks with clear phases and deliverables
- Require coordination between development, marketing campaigns, and sales enablement
- Post-launch monitoring and optimization are critical to success

## Orchestrated Agents (15 Total)

### Research & Planning Agents
- **`market-researcher`** - Market analysis, competitive research, customer insights, trend identification
- **`business-analyst`** - SWOT analysis, business model validation, revenue projections, risk assessment
- **`product-manager`** - Product strategy, feature prioritization, positioning, go-to-market planning

### Development & Engineering Agents
- **`backend-developer`** - REST/GraphQL API development, server-side logic, business layer implementation
- **`frontend-developer`** - Web UI development, React/Vue components, state management, client integration
- **`mobile-developer`** - iOS/Android applications, React Native, cross-platform, offline sync
- **`database-architect`** - Schema design, query optimization, indexing strategy, data modeling
- **`security-specialist`** - Security audits, vulnerability scanning, compliance validation, penetration testing
- **`qa-engineer`** - Test suite creation, integration testing, E2E testing, performance validation

### Marketing & Sales Agents
- **`marketing-specialist`** - Campaign creation, audience segmentation, multi-channel strategy, KPI tracking
- **`sales-specialist`** - Sales enablement, pipeline setup, lead qualification, revenue forecasting
- **`content-creator`** - Blog posts, social media content, email sequences, video scripts, landing pages
- **`seo-specialist`** - Keyword research, on-page SEO, link building, search optimization

### Launch & Operations Agents
- **`devops-engineer`** - CI/CD pipelines, Docker/K8s deployment, infrastructure setup, monitoring configuration
- **`production-validator`** - Production readiness assessment, go/no-go decision, deployment validation
- **`performance-monitor`** - Metrics collection, alert configuration, anomaly detection, dashboard setup
- **`customer-support-specialist`** - Support infrastructure, knowledge base, ticket workflows, team training

## Workflow Phases

### Phase 1: Research & Planning (Week 1-2, Sequential → Parallel)

**Duration**: 2 weeks
**Execution Mode**: Sequential analysis then parallel strategy
**Agents**: `market-researcher`, `business-analyst`, `product-manager`

**Process**:

1. **Conduct Comprehensive Market Analysis** (Day 1-3)
   ```bash
   npx claude-flow hooks pre-task --description "Product launch: ${PRODUCT_NAME}"
   npx claude-flow swarm init --topology hierarchical --max-agents 15
   npx claude-flow agent spawn --type researcher
   ```

   Spawn `market-researcher` agent to:
   - Analyze target market size, demographics, and segmentation
   - Research competitors (features, pricing, positioning, market share)
   - Identify market trends, opportunities, and threats
   - Document customer pain points and unmet needs
   - Validate product-market fit hypotheses

   **Memory Storage**:
   ```bash
   npx claude-flow memory store --key "product-launch/${LAUNCH_ID}/phase-1/market-researcher/analysis" \
     --value "${MARKET_ANALYSIS_JSON}"
   ```

2. **Perform Business Analysis** (Day 4-6)

   Retrieve market analysis and spawn `business-analyst` agent:
   ```bash
   npx claude-flow memory retrieve --key "product-launch/${LAUNCH_ID}/phase-1/market-researcher/analysis"
   npx claude-flow agent spawn --type analyst
   ```

   Conduct:
   - SWOT analysis (Strengths, Weaknesses, Opportunities, Threats)
   - Business model validation and monetization strategy
   - Revenue projections and financial modeling (3-year forecast)
   - Risk assessment and mitigation strategies
   - Competitive differentiation analysis

   **Memory Storage**:
   ```bash
   npx claude-flow memory store --key "product-launch/${LAUNCH_ID}/phase-1/business-analyst/strategy"
   ```

3. **Define Product Strategy** (Day 7-10)

   Retrieve market and business analysis, spawn `product-manager` agent:
   ```bash
   npx claude-flow memory retrieve --pattern "product-launch/${LAUNCH_ID}/phase-1/*/analysis"
   npx claude-flow agent spawn --type planner
   ```

   Define:
   - Product positioning statement and value proposition
   - Feature prioritization (MVP vs future roadmap)
   - Pricing strategy (tiers, packaging, discounts)
   - Go-to-market strategy and launch timeline
   - Success metrics and KPIs

   **Memory Storage**:
   ```bash
   npx claude-flow memory store --key "product-launch/${LAUNCH_ID}/phase-1/product-manager/plan"
   npx claude-flow hooks post-task --task-id "phase-1-planning"
   ```

**Outputs**:
- Market analysis report with competitive landscape
- SWOT analysis and business validation
- Product strategy document with positioning and pricing
- Launch timeline with milestones

**Success Criteria**:
- [ ] Market opportunity clearly quantified (TAM, SAM, SOM)
- [ ] Competitive differentiation documented
- [ ] Business model validated with financial projections
- [ ] Product strategy approved by stakeholders
- [ ] Phase 1 deliverables stored in memory



### Phase 3: Marketing & Sales Preparation (Week 5-9, Parallel Execution)

**Duration**: 4-5 weeks (overlaps with development)
**Execution Mode**: Parallel marketing campaigns
**Agents**: `marketing-specialist`, `sales-specialist`, `content-creator`, `seo-specialist`

**Process**:

1. **Initialize Marketing Swarm** (Week 5)
   ```bash
   npx claude-flow swarm init --topology star --max-agents 4 --strategy specialized
   npx claude-flow memory retrieve --key "product-launch/${LAUNCH_ID}/phase-1/product-manager/plan"
   ```

2. **Parallel Campaign Creation** (Week 5-7)

   Spawn all marketing agents concurrently:
   ```bash
   npx claude-flow task orchestrate --strategy parallel --priority high
   ```

   **Marketing Specialist** creates:
   - Multi-channel campaign strategy (email, social, paid ads, PR)
   - Audience segmentation and targeting
   - Campaign timeline aligned with launch date
   - Budget allocation across channels
   - KPI tracking and analytics setup

   **Memory Pattern**: `product-launch/${LAUNCH_ID}/phase-3/marketing-specialist/{campaign,metrics}`

   **Content Creator** produces:
   - Product landing page copy (hero, features, testimonials, CTA)
   - Blog posts (3-5 pre-launch, 10+ post-launch schedule)
   - Social media content calendar (50+ posts across platforms)
   - Email sequences (welcome, onboarding, nurture, re-engagement)
   - Video demos, tutorials, and explainer videos

   **Memory Pattern**: `product-launch/${LAUNCH_ID}/phase-3/content-creator/{landing-page,blog,social,email}`

   **SEO Specialist** optimizes:
   - Keyword research and mapping (primary, secondary, long-tail)
   - On-page SEO (meta tags, headers, schema markup)
   - Content optimization for search intent
   - Link building strategy and outreach plan
   - Technical SEO audit and fixes

   **Memory Pattern**: `product-launch/${LAUNCH_ID}/phase-3/seo-specialist/{keywords,seo-plan}`

3. **Sales Enablement** (Week 7-9)

   **Sales Specialist** prepares:
   - Product demo scripts and presentation decks
   - Sales playbook with objection handling
   - Pricing calculator and proposal templates
   - CRM configuration and automation workflows
   - Sales pipeline stages and conversion targets

   **Memory Pattern**: `product-launch/${LAUNCH_ID}/phase-3/sales-specialist/{enablement,pipeline}`

4. **Support Infrastructure** (Week 8-9)

   **Customer Support Specialist** sets up:
   - Help desk software and ticket workflows
   - Knowledge base articles (50+ FAQ entries)
   - Support team training materials
   - Escalation procedures and SLAs
   - Self-service resources (docs, videos, troubleshooting)

   **Memory Pattern**: `product-launch/${LAUNCH_ID}/phase-3/customer-support-specialist/{knowledge-base,workflows}`

   **Coordination**:
   ```bash
   npx claude-flow hooks post-task --task-id "phase-3-marketing-prep"
   npx claude-flow memory retrieve --pattern "product-launch/${LAUNCH_ID}/phase-3/*"
   ```

**Outputs**:
- Multi-channel marketing campaign (ready to execute)
- Complete content library (landing page, blog, social, email)
- SEO optimization plan with keyword targeting
- Sales enablement kit with playbooks and tools
- Support infrastructure and knowledge base

**Success Criteria**:
- [ ] Marketing campaigns ready for launch day
- [ ] Content calendar planned for 3 months post-launch
- [ ] SEO foundation established (technical + content)
- [ ] Sales team trained and equipped with materials
- [ ] Support infrastructure tested and operational



### Phase 5: Post-Launch Monitoring & Optimization (Week 11+, Continuous)

**Duration**: Ongoing
**Execution Mode**: Weekly reviews with adaptive optimization
**Agents**: `performance-monitor`, `business-analyst`, Various optimization agents

**Process**:

1. **Weekly Performance Review** (Every Monday)
   ```bash
   npx claude-flow hooks session-restore --session-id "launch-${LAUNCH_ID}"
   npx claude-flow agent spawn --type analyst
   ```

   **Business Analyst** aggregates:
   - User acquisition metrics (signups, activations, churn)
   - Marketing performance (campaigns, channels, ROI)
   - Sales pipeline progress (leads, opportunities, revenue)
   - Support metrics (tickets, resolution time, satisfaction)
   - Product usage analytics (features, engagement, retention)

   Retrieve all metrics:
   ```bash
   npx claude-flow memory retrieve --pattern "product-launch/${LAUNCH_ID}/phase-5/week-${WEEK_NUM}/*"
   ```

   Generate insights and recommendations:
   ```bash
   npx claude-flow memory store --key "product-launch/${LAUNCH_ID}/phase-5/weekly-report/week-${WEEK_NUM}"
   ```

2. **Adaptive Optimization** (Continuous)

   Based on weekly insights, spawn specialist agents for targeted improvements:

   **If conversion rate is low**:
   ```bash
   npx claude-flow agent spawn --type optimizer --focus "conversion-optimization"
   ```
   - A/B testing on landing page elements
   - Funnel analysis and friction point identification
   - Pricing experiment variations
   - Checkout flow optimization

   **If support volume is high**:
   ```bash
   npx claude-flow agent spawn --type planner --focus "support-optimization"
   ```
   - Identify common issues and root causes
   - Create self-service solutions and documentation
   - Proactive user education (tooltips, guides, videos)
   - Product improvements to prevent issues

   **If marketing ROI is below target**:
   ```bash
   npx claude-flow agent spawn --type researcher --focus "marketing-optimization"
   ```
   - Channel performance analysis
   - Audience segment refinement
   - Ad creative and copy testing
   - Budget reallocation to high-performing channels

3. **Continuous Improvement Cycle**
   ```bash
   npx claude-flow hooks post-task --task-id "weekly-optimization-${WEEK_NUM}"
   npx claude-flow hooks session-end --export-metrics true
   ```

   Store learnings for future launches:
   ```bash
   npx claude-flow memory store --key "product-launch/learnings/${LAUNCH_ID}" \
     --value "${LESSONS_LEARNED_JSON}"
   ```

**Outputs**:
- Weekly performance reports with trends
- Continuous product improvements and iterations
- Optimized marketing campaigns (improved ROI)
- Enhanced customer experience (reduced friction)
- Documented learnings for future launches

**Success Criteria**:
- [ ] Weekly reports delivered on schedule
- [ ] Key metrics trending positively week-over-week
- [ ] Customer satisfaction scores improving
- [ ] Product-market fit validated through usage data
- [ ] Launch learnings documented for knowledge sharing



## Scripts & Automation

### Pre-Workflow Initialization

```bash
#!/bin/bash
# Initialize product launch workflow

PRODUCT_NAME="$1"
LAUNCH_ID="${PRODUCT_NAME}-$(date +%Y%m%d)"

# Setup coordination
npx claude-flow hooks pre-task --description "Product launch: ${PRODUCT_NAME}"

# Initialize hierarchical swarm
npx claude-flow swarm init --topology hierarchical --max-agents 15 --strategy adaptive

# Store launch metadata
npx claude-flow memory store --key "product-launch/${LAUNCH_ID}/metadata" --value '{
  "product_name": "'"${PRODUCT_NAME}"'",
  "launch_id": "'"${LAUNCH_ID}"'",
  "start_date": "'"$(date -I)"'",
  "timeline_weeks": 10,
  "phases": 5
}'

echo "✅ Product launch initialized: ${LAUNCH_ID}"
```

### Per-Phase Coordination

```bash
#!/bin/bash
# Execute specific phase

LAUNCH_ID="$1"
PHASE="$2"

# Restore session context
npx claude-flow hooks session-restore --session-id "launch-${LAUNCH_ID}"

# Retrieve prior phase outputs
if [ "$PHASE" -gt 1 ]; then
  PREV_PHASE=$((PHASE - 1))
  npx claude-flow memory retrieve --pattern "product-launch/${LAUNCH_ID}/phase-${PREV_PHASE}/*"
fi

# Execute phase-specific workflow
case $PHASE in
  1)
    echo "🔬 Executing Phase 1: Research & Planning"
    npx claude-flow task orchestrate --strategy sequential --task "market-research"
    ;;
  2)
    echo "⚙️ Executing Phase 2: Product Development"
    npx claude-flow task orchestrate --strategy parallel --max-agents 6
    ;;
  3)
    echo "📢 Executing Phase 3: Marketing & Sales Prep"
    npx claude-flow task orchestrate --strategy parallel --max-agents 4
    ;;
  4)
    echo "🚀 Executing Phase 4: Launch Execution"
    npx claude-flow task orchestrate --strategy sequential --priority critical
    ;;
  5)
    echo "📊 Executing Phase 5: Post-Launch Monitoring"
    npx claude-flow task orchestrate --strategy adaptive
    ;;
esac

# Store phase completion
npx claude-flow hooks post-task --task-id "phase-${PHASE}-complete"
```

### Post-Workflow Summary

```bash
#!/bin/bash
# Generate launch summary report

LAUNCH_ID="$1"

# Retrieve all phase data
npx claude-flow memory retrieve --pattern "product-launch/${LAUNCH_ID}/*" > "/tmp/${LAUNCH_ID}-data.json"

# Generate summary
npx claude-flow hooks post-task --task-id "launch-${LAUNCH_ID}" --export-metrics true

# Export workflow for future reference
npx claude-flow hooks session-end --export-workflow "/tmp/${LAUNCH_ID}-workflow.json"

echo "✅ Product launch complete: ${LAUNCH_ID}"
echo "📊 Summary report: /tmp/${LAUNCH_ID}-data.json"
echo "📈 Workflow export: /tmp/${LAUNCH_ID}-workflow.json"
```



## Usage Examples

### Example 1: SaaS Product Launch

```bash
# Initialize launch
PRODUCT="TaskFlow AI"
LAUNCH_ID="taskflow-ai-20250101"

# Phase 1: Market Research (Week 1-2)
npx claude-flow agent spawn --type researcher
# Output: Market size $2B TAM, 50k potential customers identified

# Phase 2: Development (Week 3-8)
npx claude-flow swarm init --topology mesh --max-agents 6
# Output: Web app + mobile apps + API complete with 93% test coverage

# Phase 3: Marketing (Week 5-9)
npx claude-flow task orchestrate --strategy parallel
# Output: Campaign across 5 channels, 100+ content pieces created

# Phase 4: Launch (Week 10)
npx claude-flow workflow execute --workflow-id "prod-deploy-${LAUNCH_ID}"
# Output: Deployed successfully, 1,000 signups in first week

# Phase 5: Optimization (Week 11+)
npx claude-flow hooks session-restore --session-id "launch-${LAUNCH_ID}"
# Output: Weekly reports, 15% improvement in conversion rate
```

### Example 2: Mobile App Launch

```bash
# Focus on mobile-first approach
LAUNCH_ID="fitness-tracker-20250201"

# Phase 2: Prioritize mobile development
npx claude-flow agent spawn --type mobile-dev --priority high
npx claude-flow agent spawn --type backend-dev --priority high
# Output: React Native app (iOS + Android) with offline-first architecture

# Phase 3: App store optimization
npx claude-flow agent spawn --type seo-specialist --focus "app-store-optimization"
# Output: ASO strategy, 50+ keywords, compelling app store listings

# Phase 4: Soft launch to beta users
npx claude-flow workflow execute --workflow-id "beta-deploy-${LAUNCH_ID}"
# Output: 500 beta users, 4.8 star rating, feedback incorporated
```

### Example 3: Enterprise B2B Launch

```bash
# Enterprise focus with sales-led approach
LAUNCH_ID="enterprise-analytics-20250301"

# Phase 1: Enterprise market research
npx claude-flow agent spawn --type researcher --focus "enterprise-b2b"
# Output: Target 500 enterprise accounts, decision-maker personas

# Phase 3: Sales enablement priority
npx claude-flow agent spawn --type sales-specialist --priority critical
# Output: Enterprise sales playbook, ROI calculator, case studies

# Phase 4: Account-based marketing launch
npx claude-flow task orchestrate --strategy "account-based-marketing"
# Output: 50 target accounts engaged, 10 pilot customers secured
```



## Quality Checklist

Before considering launch complete, verify:

- [ ] **Phase 1**: Market validated, strategy approved, business case solid
- [ ] **Phase 2**: All applications deployed, tests passing, security audited
- [ ] **Phase 3**: Marketing campaigns ready, sales team trained, support operational
- [ ] **Phase 4**: Production stable, first customers acquired, monitoring active
- [ ] **Phase 5**: Metrics tracking positively, optimization loops running

**All phase deliverables stored in memory following namespace convention**:
- [ ] `product-launch/${LAUNCH_ID}/phase-1/*` - Research and strategy
- [ ] `product-launch/${LAUNCH_ID}/phase-2/*` - Development artifacts
- [ ] `product-launch/${LAUNCH_ID}/phase-3/*` - Marketing materials
- [ ] `product-launch/${LAUNCH_ID}/phase-4/*` - Launch metrics
- [ ] `product-launch/${LAUNCH_ID}/phase-5/*` - Weekly reports

## !! SKILL COMPLETION VERIFICATION (MANDATORY) !!

**After invoking this skill, you MUST complete ALL items below before proceeding:**

### Completion Checklist

- [ ] **Agent Spawning**: Did you spawn at least 1 agent via Task()?
  - Example: `Task("Agent Name", "Task description", "agent-type-from-registry")`

- [ ] **Agent Registry Validation**: Is your agent from the registry?
  - Registry location: `claude-code-plugins/ruv-sparc-three-loop-system/agents/`
  - Valid categories: delivery, foundry, operations, orchestration, platforms, quality, research, security, specialists, tooling
  - NOT valid: Made-up agent names

- [ ] **TodoWrite Called**: Did you call TodoWrite with 5+ todos?
  - Example: `TodoWrite({ todos: [8-10 items covering all work] })`

- [ ] **Work Delegation**: Did you delegate to agents (not do work yourself)?
  - CORRECT: Agents do the implementation via Task()
  - WRONG: You write the code directly after reading skill

### Correct Pattern After Skill Invocation

```javascript
// After Skill("<skill-name>") is invoked:
[Single Message - ALL in parallel]:
  Task("Agent 1", "Description of task 1...", "agent-type-1")
  Task("Agent 2", "Description of task 2...", "agent-type-2")
  Task("Agent 3", "Description of task 3...", "agent-type-3")
  TodoWrite({ todos: [
    {content: "Task 1 description", status: "in_progress", activeForm: "Working on task 1"},
    {content: "Task 2 description", status: "pending", activeForm: "Working on task 2"},
    {content: "Task 3 description", status: "pending", activeForm: "Working on task 3"},
  ]})
```

### Wrong Pattern (DO NOT DO THIS)

```javascript
// WRONG - Reading skill and then doing work yourself:
Skill("<skill-name>")
// Then you write all the code yourself without Task() calls
// This defeats the purpose of the skill system!
```

**The skill is NOT complete until all checklist items are checked.**

## Core Principles

### 1. Phased Execution with Clear Gates
**Principle**: Product launches must proceed through well-defined phases with explicit success criteria before advancing. Each phase builds foundation for next, preventing premature launch.

**In practice**:
- Phase 1 research validates market opportunity before committing development resources
- Phase 2 development cannot begin until strategy approved and requirements documented
- Phase 3 marketing prepares in parallel with development to align launch timing
- Phase 4 deployment requires automated checks passing plus production readiness validation
- Phase 5 monitoring tracks post-launch metrics with weekly optimization cycles

### 2. Cross-Functional Coordination from Day One
**Principle**: Engineering, marketing, sales, and operations teams work in parallel from earliest phases to ensure aligned launch execution.

**In practice**:
- Product manager owns overall strategy coordinating all functional areas
- Marketing receives product specs early (Phase 2) to prepare campaigns during development
- Sales enablement starts in Phase 3 ensuring team trained before launch day
- DevOps participates in Phase 2 to plan infrastructure preventing deployment surprises
- Support builds knowledge base during Phase 3 ready for customer inquiries at launch

### 3. Memory-Driven Context Preservation
**Principle**: All phase deliverables store in shared memory enabling subsequent phases to leverage prior work without information loss.

**In practice**:
- Market research findings inform product strategy which guides development priorities
- Technical architecture decisions documented for marketing to understand product capabilities
- Performance benchmarks from Phase 2 inform monitoring thresholds in Phase 5
- Launch learnings captured in memory namespace for future product launches
- Audit trail preserved showing decision rationale for compliance and retrospectives

----------|---------|----------|
| **Launch Without Market Validation** | Skipping Phase 1 research to accelerate timeline results in building product nobody wants, wasting months of effort on unvalidated assumptions. | Never skip market validation phase. Spend 2 weeks upfront researching target market, competitors, and customer pain points. Use findings to validate product-market fit before committing to development. |
| **Siloed Development Without Marketing** | Engineering builds product in isolation while marketing scrambles to prepare campaigns days before launch, resulting in rushed messaging and weak go-to-market. | Run Phase 3 marketing preparation in parallel with Phase 2 development. Share product specs and demos early. Marketing needs 4-6 weeks lead time for campaign creation and sales enablement. |
| **No Production Readiness Validation** | Deploying to production without comprehensive validation (Phase 4) risks critical failures on launch day when maximum traffic and visibility occurs. | Implement mandatory production validator review in Phase 4. Check all tests passing, security audit complete, performance benchmarks met, monitoring active, rollback plan tested. Go/no-go decision must be evidence-based. |

-----------|---------|----------|
| **Launch Without Market Validation** | Skipping Phase 1 research to accelerate timeline results in building product nobody wants, wasting months of effort on unvalidated assumptions. | Never skip market validation phase. Spend 2 weeks upfront researching target market, competitors, and customer pain points. Use findings to validate product-market fit before committing to development. |
| **Siloed Development Without Marketing** | Engineering builds product in isolation while marketing scrambles to prepare campaigns days before launch, resulting in rushed messaging and weak go-to-market. | Run Phase 3 marketing preparation in parallel with Phase 2 development. Share product specs and demos early. Marketing needs 4-6 weeks lead time for campaign creation and sales enablement. |
| **No Production Readiness Validation** | Deploying to production without comprehensive validation (Phase 4) risks critical failures on launch day when maximum traffic and visibility occurs. | Implement mandatory production validator review in Phase 4. Check all tests passing, security audit complete, performance benchmarks met, monitoring active, rollback plan tested. Go/no-go decision must be evidence-based. |

## Conclusion

Orchestrated product launches transform chaotic, ad-hoc release processes into systematic workflows coordinating 15+ specialists across 10 weeks and 5 distinct phases. The workflow's power comes from balancing sequential dependencies (research before development) with parallel execution (development and marketing concurrently) to optimize both speed and quality. Memory coordination ensures each phase builds upon prior work without information loss, creating continuity across the multi-week timeline even as team members join and leave.

The phased approach with explicit gates prevents the most common launch failures - building products without market validation, deploying without production readiness, or launching without marketing support. Each gate acts as quality checkpoint forcing teams to pause and validate assumptions before proceeding. The cross-functional coordination pattern recognizes that product launches require simultaneous progress across engineering, marketing, sales, and operations - sequential handoffs between teams add weeks of latency and information loss that compound into launch delays.

Success depends on disciplined memory coordination where every agent documents deliverables in the shared namespace following the established pattern. This enables downstream phases to retrieve exactly the context needed without searching or reconstructing knowledge. The weekly optimization cycle in Phase 5 closes the feedback loop, capturing launch learnings that improve future executions. Teams must resist the temptation to skip phases or compress timelines - the 10-week duration reflects realistic minimum time required for comprehensive market research, quality development, effective marketing, and production-ready deployment. Rushing these phases inevitably surfaces as launch day failures that damage product reputation far more than modest timeline extensions.