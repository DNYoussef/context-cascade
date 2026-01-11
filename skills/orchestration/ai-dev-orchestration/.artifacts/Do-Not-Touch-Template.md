# Do Not Touch Template

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Template for creating "do not touch" constraint lists for AI coding prompts.

**Purpose**: Prevent AI from making unintended changes to critical/sensitive code areas.

**Usage**: Include in every Feature Prompt and Foundation Prompt under "Negative Constraints" section.

---

## Standard "Do Not Touch" List

These constraints apply to **most** projects. Customize for your specific app.

### Negative Constraints (DO NOT TOUCH)

**CRITICAL - DO NOT MODIFY**:

1. **Auth System**
   - Files: `auth/*`, `middleware/auth.ts`, `utils/auth.ts`, `lib/auth/*`
   - Reason: Breaking auth affects all users, requires careful migration
   - Exception: If this feature explicitly involves auth changes, specify exact scope

2. **Database Schema (existing columns)**
   - Do NOT rename existing columns
   - Do NOT change column types
   - Do NOT drop tables without explicit approval
   - Reason: Breaks existing code, requires data migration
   - Exception: Adding new columns/tables is OK if specified in feature spec

3. **Payment Logic**
   - Files: `payments/*`, `api/stripe/*`, `lib/payments/*`, `webhooks/stripe.ts`
   - Reason: Financial operations require extra scrutiny, audit trail
   - Exception: If this feature explicitly involves payment changes, specify exact scope

4. **Core Navigation**
   - Files: `components/Nav.tsx`, `layouts/*`, `navigation/*`, `app/layout.tsx`
   - Reason: Navigation changes affect entire app, require UX review
   - Exception: Adding new nav items is OK if specified in design direction

5. **Environment Variables (names)**
   - Do NOT rename env var names (DATABASE_URL, AUTH_SECRET, etc.)
   - Reason: Breaks deployment, requires config updates across environments
   - Exception: Adding new env vars is OK, document in .env.example

6. **API Contracts (existing endpoints)**
   - Do NOT change existing API endpoint paths, request/response formats
   - Reason: Breaks frontend, mobile apps, external integrations
   - Exception: Versioned APIs OK (e.g., /api/v2/...), deprecation with migration path

7. **Third-Party Integrations**
   - Files: `integrations/*`, `lib/[service-name]/*`
   - Reason: Breaking integrations can cause data loss, failed webhooks
   - Exception: If this feature explicitly changes integration, specify exact scope

---

## App-Specific Customizations

Add constraints specific to your app:

### Example: Multi-Tenant SaaS

```
8. **Tenant Isolation**
   - Do NOT modify RLS (Row Level Security) policies without security review
   - Do NOT change tenant_id columns or relationships
   - Files: `db/policies/*`, `middleware/tenant.ts`
   - Reason: Breaking tenant isolation is a CRITICAL security issue

9. **Billing Tiers**
   - Do NOT modify feature flags or tier checks without product approval
   - Files: `lib/tiers.ts`, `middleware/feature-gates.ts`
   - Reason: Changes affect revenue, require pricing strategy review
```

### Example: Real-Time Collaboration App

```
8. **WebSocket/Realtime Logic**
   - Do NOT modify socket event handlers without testing with multiple clients
   - Files: `lib/websocket.ts`, `hooks/useRealtime.ts`
   - Reason: Breaking realtime sync affects collaboration, hard to debug

9. **Conflict Resolution**
   - Do NOT change CRDT or OT (Operational Transform) logic
   - Files: `lib/sync/*`, `utils/conflict-resolution.ts`
   - Reason: Conflict resolution bugs cause data loss
```

### Example: E-Commerce Platform

```
8. **Cart & Checkout**
   - Do NOT modify cart calculation logic or tax calculations
   - Files: `lib/cart.ts`, `utils/pricing.ts`, `api/checkout/*`
   - Reason: Pricing bugs affect revenue, regulatory compliance

9. **Inventory Management**
   - Do NOT change inventory decrement logic or concurrency controls
   - Files: `lib/inventory.ts`, `db/transactions/inventory.ts`
   - Reason: Race conditions cause overselling
```

---

## How to Use This Template

### Step 1: Copy Standard List

Start with the standard "Do Not Touch" list above.

### Step 2: Add App-Specific Constraints

Identify critical areas in YOUR app:
- What code, if broken, would cause the most damage?
- What systems have complex logic that's hard to test?
- What areas require special expertise (security, compliance, etc.)?
- What integrations are fragile or hard to debug?

### Step 3: Document File Paths

For each constraint, specify:
- **Files**: Exact paths or glob patterns (e.g., `auth/*`)
- **Reason**: Why this area is protected
- **Exception**: When it's OK to modify (with explicit scope)

### Step 4: Update as Project Evolves

Add constraints when:
- New critical systems added (e.g., new payment provider)
- Bug caused by unintended change (prevent recurrence)
- Complex refactor completed (protect the result)

---

## Prompt Integration Example

Here's how to integrate into a Feature Prompt:

```markdown
# Feature Prompt Framework

## 1. Context
[...]

## 2. User Journey
[...]

## 3. Technology & Data
[...]

## 4. Design Direction
[...]

## 5. Negative Constraints (DO NOT TOUCH)

**CRITICAL - DO NOT MODIFY**:
- Do NOT change auth flow (files: `auth/*`, `middleware/auth.ts`)
- Do NOT rename existing DB columns (breaks existing code)
- Do NOT modify payment logic (files: `payments/*`, `api/stripe/*`)
- Do NOT alter core navigation (files: `components/Nav.tsx`, `layouts/*`)
- Do NOT change environment variable names (breaks deployment)

**App-Specific**:
- Do NOT modify RLS policies (files: `db/policies/*`) - Security critical
- Do NOT change tenant_id relationships - Breaks tenant isolation

**For This Feature**:
- You MAY add new columns to `tasks` table (as specified)
- You MAY create new components in `components/features/shared-lists/`
- You MAY add new API routes under `/api/lists/share/`

**ASK FIRST** if you need to:
- Modify existing API endpoint formats
- Change database indexes
- Add new third-party dependencies
```

---

## Red Flags: "Do Not Touch" Violations

Watch for these signs that AI violated constraints:

🚩 **Files in protected directories modified**
  - Check git diff for unexpected changes to `auth/*`, `payments/*`, etc.

🚩 **Database migration renames columns**
  - Review migrations carefully, should only ADD, not ALTER

🚩 **Environment variable names changed**
  - Check `.env.example` for renamed vars

🚩 **API endpoint paths changed**
  - Review route files for modified paths

🚩 **Navigation structure altered**
  - Check layout/nav components for unexpected changes

**If violation detected**:
1. **ROLLBACK** immediately: `git reset --hard HEAD`
2. **Add explicit constraint** to prompt
3. **Restart** feature implementation with stronger constraints

---

## Constraint Enforcement Checklist

Before submitting AI prompt:

- [ ] "Do not touch" list included in prompt
- [ ] Standard constraints present (auth, DB, payments, nav, env vars, APIs)
- [ ] App-specific constraints added (if applicable)
- [ ] File paths specified (not vague "don't change auth")
- [ ] Exceptions clarified (what IS allowed to change)

After AI implementation:

- [ ] Review git diff for changes to protected files
- [ ] Verify no column renames in migrations
- [ ] Check no env var name changes
- [ ] Confirm no API path changes
- [ ] Test that auth/payments/core features still work

---

## Template: Per-Feature "Do Not Touch" Customization

For each feature, customize the list:

```markdown
## 5. Negative Constraints (DO NOT TOUCH)

**STANDARD PROTECTIONS**:
[Copy standard list from above]

**FOR THIS FEATURE SPECIFICALLY**:
- You MAY [specific allowed changes]:
  - Add new component: `components/features/[feature-name]/[Component].tsx`
  - Add new route: `/api/[feature-name]/[endpoint]`
  - Add new table: `[table_name]` with specified columns

- You MAY NOT [specific forbidden changes]:
  - Modify existing `[component]` component (reuse, don't change)
  - Change `[table].[column]` (add new column instead)
  - Alter `[function]` logic (call it, don't modify)

**IF YOU NEED TO** [require explicit approval]:
- Add new npm package → ASK FIRST (check bundle size, license)
- Change API response format → ASK FIRST (affects frontend contract)
- Modify [complex-system] → ASK FIRST (requires deep understanding)
```

---

## Common Mistakes to Avoid

### Mistake 1: Vague Constraints

❌ **Bad**: "Don't change auth"
✅ **Good**: "Do NOT change auth flow (files: `auth/*`, `middleware/auth.ts`). You MAY add new auth providers if specified."

### Mistake 2: No File Paths

❌ **Bad**: "Don't modify database"
✅ **Good**: "Do NOT rename existing columns. Do NOT change column types. You MAY add new columns/tables as specified."

### Mistake 3: No Exceptions

❌ **Bad**: "Do NOT touch API"
✅ **Good**: "Do NOT change existing API endpoints. You MAY add new endpoints under `/api/[feature-name]/`"

### Mistake 4: Missing App-Specific Constraints

❌ **Bad**: Only using standard list
✅ **Good**: Standard list + your app's critical areas (RLS, billing, realtime, etc.)

---

## Summary

**Purpose**: Prevent AI chaos by constraining what can be modified

**Usage**: Include in EVERY Feature Prompt and Foundation Prompt

**Format**:
1. Standard protections (auth, DB, payments, nav, env, APIs)
2. App-specific protections (your critical areas)
3. Per-feature permissions (what IS allowed to change)
4. Explicit "ask first" items (require human approval)

**Enforcement**: Review git diffs, rollback violations immediately, strengthen constraints

**Remember**: Constraints are not restrictive—they enable safe AI assistance by preventing expensive mistakes.


---
*Promise: `<promise>DO_NOT_TOUCH_TEMPLATE_VERIX_COMPLIANT</promise>`*
