/*============================================================================*/
/* SQL-DATABASE-SPECIALIST SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: sql-database-specialist
version: 1.0.0
description: |
  [assert|neutral] SQL database specialist for PostgreSQL/MySQL optimization, EXPLAIN plan analysis, index optimization, query rewriting, partitioning strategies, connection pooling, and database performance tuning. Use [ground:given] [conf:0.95] [state:confirmed]
category: Database Specialists
tags:
- general
author: system
cognitive_frame:
  primary: evidential
  goal_analysis:
    first_order: "Execute sql-database-specialist workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic Database Specialists processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "sql-database-specialist",
  category: "Database Specialists",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Evidential",
  source: "Turkish",
  force: "How do you know?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["sql-database-specialist", "Database Specialists", "workflow"],
  context: "user needs sql-database-specialist capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# SQL Database Specialist

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Expert SQL database optimization, schema design, and performance tuning for PostgreSQL and MySQL.

## Purpose

Comprehensive SQL expertise including EXPLAIN plan analysis, index optimization, query rewriting, partitioning, replication, and performance tuning. Ensures databases are fast, scalable, and maintainable.

## When to Use

- Optimizing slow database queries
- Designing efficient database schemas
- Analyzing EXPLAIN plans
- Creating optimal indexes
- Implementing database partitioning
- Setting up replication and high availability
- Migrating data with zero downtime
- Troubleshooting performance issues

## Prerequisites

**Required**: SQL basics, understanding of relational databases, familiarity with PostgreSQL or MySQL

**Agents**: `backend-dev`, `perf-analyzer`, `system-architect`, `code-analyzer`

## Core Workflows

### Workflow 1: Query Optimization with EXPLAIN

**Step 1: Analyze EXPLAIN Plan (PostgreSQL)**

```sql
-- EXPLAIN shows query plan
EXPLAIN
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2024-01-01';

-- EXPLAIN ANALYZE executes and shows actual timings
EXPLAIN (ANALYZE, BUFFERS)
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2024-01-01';
```

**Key Metrics to Check**:
- **Seq Scan** (bad): Full table scan, add index
- **Index Scan** (good): Using index
- **Bitmap Index Scan** (good): Efficient for multiple conditions
- **Nested Loop** (watch out): Can be slow for large datasets
- **Hash Join** (usually good): Efficient join method
- **Cost**: Estimated cost (lower is better)
- **Actual time**: Real execution time

**Step 2: Create Optimal Index**

```sql
-- ❌ SLOW: No index on created_at
SELECT * FROM orders WHERE created_at > '2024-01-01';

-- ✅ FAST: Create index
CREATE INDEX idx_orders_created_at ON orders (created_at);

-- ✅ COMPOUND INDEX: For multiple columns
CREATE INDEX idx_orders_user_created
ON orders (user_id, created_at);

-- ✅ PARTIAL INDEX: For filtered queries
CREATE INDEX idx_orders_pending
ON orders (created_at)
WHERE status = 'pending';

-- ✅ COVERING INDEX: Include frequently queried columns
CREATE INDEX idx_orders_covering
ON orders (user_id, created_at)
INCLUDE (total, status);
```

**Step 3: Rewrite Query for Performance**

```sql
-- ❌ SLOW: N+1 query pattern
SELECT id, name FROM users;
-- Then for each user:
SELECT * FROM orders WHERE user_id = ?;

-- ✅ FAST: Single query with JOIN
SELECT u.id, u.name, o.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- ❌ SLOW: NOT IN with subquery
SELECT * FROM users
WHERE id NOT IN (SELECT user_id FROM orders);

-- ✅ FAST: LEFT JOIN with NULL check
SELECT u.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.user_id IS NULL;

-- ❌ SLOW: OR conditions prevent index use
SELECT * FROM orders
WHERE user_id = 123 OR status = 'pending';

-- ✅ FAST: UNION ALL with indexes
SELECT * FROM orders WHERE user_id = 123
UNION ALL
SELECT * FROM orders WHERE status = 'pending' AND user_id != 123;
```

### Workflow 2: Table Partitioning (PostgreSQL)

**Step 1: Create Partitioned Table**

```sql
-- Range partitioning by date
CREATE TABLE orders (
  id BIGSERIAL,
  user_id INT NOT NULL,
  created_at DATE NOT NULL,
  total DECIMAL(10, 2),
  status VARCHAR(20)
) PARTITION BY RANGE (created_at);

-- Create partitions
CREATE TABLE orders_2024_q1 PARTITION OF orders
FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE orders_2024_q2 PARTITION OF orders
FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

-- Create index on each partition
CREATE INDEX idx_orders_2024_q1_user_id
ON orders_2024_q1 (user_id);

-- Queries automatically use correct partition
SELECT * FROM orders
WHERE created_at >= '2024-02-01'
  AND created_at < '2024-03-01';
-- Only scans orders_2024_q1 partition
```

**Step 2: List Partitioning by Status**

```sql
CREATE TABLE orders_

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
  pattern: "skills/Database Specialists/sql-database-specialist/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "sql-database-specialist-{session_id}",
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

[commit|confident] <promise>SQL_DATABASE_SPECIALIST_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
