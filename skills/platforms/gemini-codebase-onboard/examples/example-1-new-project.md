# Example 1: New Project Onboarding

## Scenario

Developer joining a team needs to understand an existing Node.js/TypeScript microservices codebase.

## Process

### Step 1: Initial Megacontext Analysis

```bash
./scripts/multi-model/delegate.sh gemini \
  "Create comprehensive onboarding guide including:
   1. High-level architecture (services, layers)
   2. Key components and their responsibilities
   3. Data flow between services
   4. External integrations (DBs, APIs, queues)
   5. Configuration and environment setup
   6. Common patterns used" \
  --all-files
```

### Step 2: Gemini Analysis Output

```yaml
architecture:
  type: "Microservices with API Gateway"

  services:
    - name: api-gateway
      port: 3000
      responsibility: "Request routing, auth validation, rate limiting"

    - name: auth-service
      port: 3001
      responsibility: "User authentication, JWT management"
      database: "PostgreSQL (users, sessions)"

    - name: order-service
      port: 3002
      responsibility: "Order lifecycle, inventory coordination"
      database: "PostgreSQL (orders, order_items)"

    - name: notification-service
      port: 3003
      responsibility: "Email, SMS, push notifications"
      queue: "RabbitMQ subscriber"

  communication:
    sync: "REST between services"
    async: "RabbitMQ for events"
    events:
      - "order.created -> notification.send_confirmation"
      - "order.shipped -> notification.send_tracking"

patterns:
  - name: "Repository Pattern"
    locations: ["*/repositories/*.ts"]
    purpose: "Data access abstraction"

  - name: "Event-Driven"
    locations: ["*/events/*.ts", "*/handlers/*.ts"]
    purpose: "Async service communication"

  - name: "Middleware Chain"
    locations: ["api-gateway/middleware/*.ts"]
    purpose: "Request processing pipeline"

external_integrations:
  - name: Stripe
    purpose: "Payment processing"
    files: ["order-service/integrations/stripe.ts"]

  - name: SendGrid
    purpose: "Email delivery"
    files: ["notification-service/providers/sendgrid.ts"]

  - name: Twilio
    purpose: "SMS delivery"
    files: ["notification-service/providers/twilio.ts"]

configuration:
  docker: "docker-compose.yml for local dev"
  env_files: [".env.example", "services/*/.env.example"]
  required_secrets:
    - DATABASE_URL
    - RABBITMQ_URL
    - STRIPE_API_KEY
    - SENDGRID_API_KEY

setup_steps:
  1: "cp .env.example .env && fill in values"
  2: "docker-compose up -d (postgres, rabbitmq)"
  3: "npm install in each service"
  4: "npm run migrate in each service"
  5: "npm run dev (starts all services)"
```

### Step 3: Claude Synthesis

Based on Gemini's analysis, create onboarding document:

```markdown
# Developer Onboarding Guide

## Quick Start
1. Clone repo
2. Copy .env files from examples
3. Run `docker-compose up -d`
4. Run `npm install && npm run migrate` in each service
5. Run `npm run dev`

## Architecture Overview
This is a microservices system with 4 services communicating via REST and RabbitMQ...

[Continue with synthesized documentation]
```

### Step 4: Store in Memory-MCP

```bash
mcp__memory-mcp__memory_store \
  --key "onboarding/myproject/architecture-2024" \
  --value '{"services": 4, "patterns": ["repository", "event-driven"], "setup_time": "15min"}' \
  --tags "WHO=gemini-megacontext,WHY=onboarding,PROJECT=myproject"
```

### Step 5: Save Documentation

```bash
# Save to project docs
Write docs/ARCHITECTURE.md with synthesized content
Write docs/ONBOARDING.md with setup guide
```

## Outcome

- **Time to understand**: ~30 minutes (vs days manually)
- **Documentation created**: Architecture + Onboarding guides
- **Knowledge preserved**: Memory-MCP + docs folder
- **Ready for**: Contributing to codebase
