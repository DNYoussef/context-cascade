---
name: system-design-architect
description: Comprehensive system design methodology using Dr. Synthara's organism-based approach. Treats systems as living organisms with specialized organs (API, DB, cache, queues), circulation (load balancing), immune defenses (security), and survival mechanisms (reliability, observability). Includes reusable decision trees for interviews and production designs.
version: 1.0.0
category: specialists
tags:
  - system-design
  - architecture
  - scaling
  - infrastructure
  - interviews
author: Context Cascade (Dr. Synthara methodology)
---

# System Design Architect

A comprehensive system design skill using the organism-based mental model: systems are living creatures with organs, circulation, immune systems, and survival mechanisms.

## SKILL-SPECIFIC GUIDANCE

### When to Use This Skill

- Designing new systems from scratch
- System design interviews (FAANG-level)
- Architecture reviews and evolution planning
- Scaling existing systems (10x, 100x)
- Production readiness assessments
- Identifying and removing SPOFs

### When NOT to Use This Skill

- Simple CRUD applications with no scale needs
- Prototypes where architecture doesn't matter yet
- When requirements are completely undefined
- Premature optimization scenarios

### Success Criteria

- Clear non-negotiable invariants defined
- All SPOFs identified and mitigated
- Decision trees applied for each component choice
- Trade-offs explicitly documented
- 90-second narrative can explain the design

---

## Phase 0: Pin the Target Before Drawing Boxes

**You are designing for constraints, not for tech.**

### Constraint Extraction Checklist

| Constraint | Questions to Ask |
|------------|------------------|
| **Users & Usage** | DAU/MAU? Peak QPS? Read/write ratio? Payload sizes? |
| **Latency Target** | p50/p95/p99? Mobile vs desktop? Global vs local? |
| **Availability** | SLO (99.9? 99.99?)? RTO/RPO? |
| **Consistency** | Strong vs eventual? Where does correctness matter? |
| **Data Shape** | Relational? Document? Graph? Hot keys? |
| **Security** | Auth model? Threat surface? Compliance? |
| **Growth Path** | What changes if traffic 10x? 100x? |

### What I'm Thinking as a Designer

"What are the non-negotiable invariants?"

Examples:
- "No double-charging" (payments)
- "Messages never delivered out of order per conversation" (chat)
- "Inventory can't go negative" (e-commerce)
- "Tokens must be revocable" (auth)

---

## Phase 1: Baseline Single-Server Organism

Start with a simple diagram you can explain in 30 seconds:

```
Domain -> DNS -> Server IP
Client -> HTTPS -> Server
Server -> Business Logic -> DB -> Response
```

This sets a clean foundation to EVOLVE from, instead of prematurely microservicing.

---

## Phase 2: First Evolution - Split Tiers

Split into:
- **Web/App Tier**: Stateless compute (horizontally scalable by default)
- **Data Tier**: Database + durable storage

**Design Rule**: The web/app tier should be horizontally scalable BY DEFAULT.

**What I'm Thinking**: "Where is state living? Where does it need to live?"

If state lives in app memory, scaling breaks it.

---

## Decision Tree 1: Scaling

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

---

## Decision Tree 2: Database Choice

```
What is the data + correctness need?
|
+-- Strong transactions / invariants (money, inventory, ledgers)?
|   +-- SQL (Postgres/MySQL) + ACID + constraints
|
+-- Clear relationships + joins matter?
|   +-- SQL (normalized + indexes)
|
+-- Semi-structured JSON + evolving schema + high scale writes?
|   +-- Document or wide-column (Mongo/Cassandra)
|
+-- Ultra-low latency key lookup / caching / rate limits / sessions?
|   +-- Key-value (Redis/Memcached)
|
+-- Relationship traversal is the product (social graph, recs)?
    +-- Graph DB (Neo4j/Neptune) or graph model over SQL/NoSQL
```

**What I'm Thinking**: "Where do I want correctness enforced - DB constraints or application code?"

If the DB doesn't enforce it, YOUR BUGS WILL.

---

## Decision Tree 3: API Style

```
Who consumes it and what do they need?
|
+-- Public API, broad compatibility, caching & simplicity matter?
|   +-- REST
|
+-- Complex UI needing shaped responses, reducing round trips?
|   +-- GraphQL (but control query cost + N+1)
|
+-- Internal service-to-service, performance + typed contracts?
    +-- gRPC (protobuf, streaming, strong typing)
```

**Designer Note**: GraphQL often trades "fewer requests" for "harder caching + expensive resolvers."

---

## Decision Tree 4: Protocol Selection

```
What interaction pattern do you need?
|
+-- Simple request/response?
|   +-- HTTPS (default)
|
+-- Real-time push, bidirectional updates (chat, live presence)?
|   +-- WebSockets (plan for sticky connections & backpressure)
|
+-- Async work, decoupling, smoothing spikes (orders, emails)?
|   +-- Queue (AMQP/Kafka/etc.)
|
+-- Microservices needing speed/streaming contracts?
    +-- gRPC over HTTP/2
```

**Transport Layer Reminder**:
- **TCP**: When correctness matters
- **UDP**: When freshness matters more than perfection (voice/video/games)

---

## Decision Tree 5: Load Balancer Algorithm

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

---

## Decision Tree 6: Cache Placement

```
What are you caching?
|
+-- Static assets (images/js/css)
|   +-- CDN + long TTL + versioned filenames
|
+-- Hot reads that tolerate slight staleness
|   +-- App cache (Redis) + TTL
|
+-- Expensive computed results
    +-- Cache with invalidation strategy + stampede protection
```

**What Impresses Devs**: You mention STAMPEDES (thundering herd) and INVALIDATION as the hardest part:
- TTL + soft TTL
- Request coalescing / single-flight
- Stale-while-revalidate patterns

---

## Decision Tree 7: Authentication

```
Need simple internal tool auth?
+-- Basic auth (only over HTTPS) or SSO

Public app / APIs?
+-- Bearer tokens (often JWT) + refresh token rotation

Need login via Google/GitHub?
+-- OAuth2 + OIDC (identity claims) + secure callback flows
```

---

## Decision Tree 8: Authorization Model

```
How complex are permissions?
|
+-- Few roles, straightforward (admin/editor/viewer)?
|   +-- RBAC
|
+-- Policies depend on attributes (dept, region, device, time)?
|   +-- ABAC
|
+-- Per-object sharing (docs, folders, repos)?
    +-- ACL (often combined with roles)
```

**What I'm Thinking**: Revocation + token rotation + compromise response.
If tokens are "stateless forever," you can't cleanly recover from theft.

---

## SPOF Identification & Mitigation

A clean system design always calls out SPOFs:

| Component | SPOF Risk | Mitigation |
|-----------|-----------|------------|
| Load Balancer | Single LB failure | Redundancy, failover, managed LB, multi-AZ |
| Database | Single DB failure | Replication + automated failover + backups |
| Cache | Cache failure melts DB | Degrade gracefully (cache miss shouldn't melt DB) |
| Queue | Message loss | Durable broker, replay strategy, idempotent consumers |

**What I'm Thinking**: "How does this fail at 2am under traffic?"
If the answer is "everything stops," you haven't finished.

---

## Security Hardening Checklist

Defense is mostly about AMPLIFICATION CONTROL:

| Defense | Purpose |
|---------|---------|
| Rate limiting | Per user/IP + global; protect from brute force and cost attacks |
| CORS | Browser constraint, not a full security boundary |
| Injection defense | Parameterized queries + validation + escaping |
| WAF/firewalls | Block known bad patterns, reduce blast radius |
| VPN/private endpoints | Keep internal APIs off the public internet |
| CSRF | Cookie-based auth needs CSRF defenses |
| XSS | Sanitize, escape, CSP, safe templating |

**What I'm Thinking**: "If attacked, what fails closed vs fails open?"

---

## REST API Checklist (Interview Gold)

- Resources are NOUNS: `/users`, `/orders/{id}`
- Proper verbs via HTTP methods (GET/POST/PATCH/DELETE)
- PAGINATION always for lists (limit/offset or cursor)
- IDEMPOTENCY where needed (especially POST for payments/orders)
- Correct status codes (201 Created, 204 No Content, 400/401/403/404/409/429, 5xx)
- Versioning strategy (URL or headers), deprecation plan

---

## GraphQL Checklist

- Schema mirrors domain, modular types
- Depth/complexity limits
- Avoid N+1 (batching, dataloaders)
- Caching strategy (often app-level)
- Explicit error shape (don't hide failures behind 200-only assumptions)

---

## The Interview-Grade 90-Second Narrative

Use this exact flow:

1. **Clarify** requirements + scale + SLOs + constraints
2. **Baseline** single-server and request flow
3. **Identify bottlenecks** (compute, DB, network, latency, SPOFs)
4. **Evolve architecture**: split tiers -> LB -> stateless app -> DB strategy -> cache/CDN -> queues
5. **Reliability**: failover, replication, graceful degradation
6. **Security**: authn/authz + API hardening
7. **Observability**: logs/metrics/traces, alerting, health checks
8. **Trade-offs**: cost vs latency vs consistency vs complexity

---

## Master Design Flow

```
DESIGN FLOW
1) Define invariants + SLOs
2) Model traffic (QPS, R/W, burstiness, geo)
3) Choose interaction pattern
   +-- sync (HTTPS)
   +-- realtime (WebSockets)
   +-- async (queues)
4) Choose data model
   +-- SQL (invariants/joins)
   +-- NoSQL (scale/shape)
   +-- KV (hot lookups)
   +-- Graph (relationship traversal)
5) Scale plan
   +-- vertical (short-term)
   +-- horizontal (LB + stateless)
6) Performance plan
   +-- CDN
   +-- caching + invalidation
   +-- pagination + payload shaping
7) Reliability plan
   +-- remove SPOFs
   +-- replication/failover
   +-- graceful degradation
8) Security plan
   +-- authn/authz
   +-- layered API defenses
9) Observability + ops
   +-- metrics/logs/traces
   +-- deploy strategy + rollback
```

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| Premature microservices | Adds complexity before understanding domain | Start monolith, extract when boundaries clear |
| "Make it good" requirements | Unverifiable, subjective | Define binary success criteria |
| Ignoring SPOFs | 2am failures | Every component needs failover plan |
| Stateful app tier | Can't scale horizontally | Move state to shared systems |
| No rate limiting | Cost attacks, brute force | Per-user and global limits |
| Cached forever | Stale data, no invalidation | TTL + explicit invalidation strategy |

---

## Conclusion

System design is about CONSTRAINTS, not TECH. Start with invariants, evolve from baseline, apply decision trees, and always ask: "How does this fail at 2am?"

The organism model helps: every system needs organs (components), circulation (load balancing), immune defenses (security), and survival mechanisms (reliability + observability).

**Philosophy**: Iteration > Perfection. Design for the 10x case, not the 1000x case you'll never reach.
