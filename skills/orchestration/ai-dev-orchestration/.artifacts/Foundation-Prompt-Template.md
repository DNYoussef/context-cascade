# Foundation Prompt Template

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Use this template when implementing infrastructure foundations (DB, Auth, Payments, APIs) with AI coding tools.

**Critical**: Use in a FRESH AI chat for each foundation piece.

---

## Foundation Prompt Template

You are helping me implement the [DATABASE/AUTH/PAYMENT/API] foundation for my app.

### Context

**App Description**: [1-2 sentence description from app-one-pager]
- Example: "A mobile to-do app for busy parents of toddlers to reduce mental load"

**Tech Stack**:
- Frontend: [Next.js/React/React Native/etc.]
- Backend: [Next API routes/Supabase/Express/etc.]
- Database: [Supabase Postgres/MongoDB/etc.]
- Auth: [Supabase Auth/Clerk/Auth0/etc.]
- Payments: [Stripe/RevenueCat/etc.] (if applicable)
- Deployment: [Vercel/Netlify/Render/etc.]

**Current State**:
- [What already exists]
- Example: "Base Next.js app created, health check route works, simple landing page visible"

---

### Goal

Implement [DB/auth/payments/API] capabilities needed for **MVP only** (no extra features).

**MVP Requirements**:
- [Specific capabilities needed]
- Example for DB: "Users table, Tasks table with foreign key to users"
- Example for Auth: "Email/password signup, login, logout, session management"

---

### Requirements

#### For DATABASE:
**Tables needed (MVP only)**:
1. `[table_name_1]`:
   - Columns: [col1 (type), col2 (type), ...]
   - Indexes: [indexed_columns]
   - Relationships: [foreign keys]

2. `[table_name_2]`:
   - ...

**Constraints**:
- [Multi-tenant? Regional? Soft deletes?]
- Example: "Multi-tenant: All tables have user_id column, RLS policies enabled"

#### For AUTH:
**Flows needed (MVP only)**:
1. Signup: [Email/password, social OAuth, magic link]
2. Login: [Email/password, social OAuth]
3. Logout: [Clear session, redirect]
4. Password reset: [Yes/No, if yes: email flow]
5. Session management: [JWT, server sessions, etc.]

**User fields**:
- Required: [email, password_hash, created_at]
- Optional: [name, avatar_url, etc.]

**Constraints**:
- [Email verification required? 2FA? Role-based access?]

#### For PAYMENTS:
**Payment flows (MVP only)**:
1. One-time payment: [Yes/No]
2. Subscription: [Yes/No, if yes: tiers and pricing]
3. Trial period: [Yes/No, if yes: duration]

**Stripe Products/Prices** (if using Stripe):
- Product 1: [name, price, billing period]
- Product 2: [name, price, billing period]

**Webhooks**:
- Events to handle: [payment_intent.succeeded, customer.subscription.updated, etc.]

#### For EXTERNAL APIs:
**API integrations (MVP only)**:
1. [API Name]: [Purpose, endpoints needed, auth method]
   - Example: OpenAI: Generate task suggestions, POST /v1/chat/completions, Bearer token

**Rate limits / quotas**:
- [Known limits that affect implementation]

---

### Constraints (DO NOT TOUCH)

**DO NOT**:
- Change existing routes/components not mentioned here
- Add more tables/features than specified without asking
- Modify [other protected areas specific to your app]

**ASK FIRST** if you need to:
- Add new dependencies/packages
- Change environment variable names
- Modify existing API contracts

---

### Implementation Instructions

**Step 1: Propose a Plan**

Before implementing, outline:
1. Files you'll create/modify
2. Database migrations (if applicable)
3. Environment variables needed
4. Key implementation decisions

Wait for my approval.

**Step 2: Implement Step-by-Step**

After each change, summarize:
- What you implemented
- What files changed
- What to test next

**Step 3: Testing Checklist**

After implementation, verify:
- [ ] Database: Migrations run successfully, tables created, can insert/query
- [ ] Auth: Can signup, login, logout, session persists across refreshes
- [ ] Payments: Sandbox payment succeeds, webhook received and processed
- [ ] API: Can call external API, handle responses, manage errors

---

## Example Foundation Prompts

### Example 1: Database Foundation

```
You are helping me implement the DATABASE foundation for my app.

### Context
**App**: Mobile to-do app for busy parents to reduce mental load
**Tech Stack**: React Native (Expo) + Supabase Postgres
**Current State**: Base Expo app created, Supabase project initialized

### Goal
Implement database schema for MVP (users and tasks only)

### Requirements
**Tables needed**:
1. `users` (managed by Supabase Auth, extends auth.users):
   - Columns: id (uuid, pk), email (text), created_at (timestamp)

2. `tasks`:
   - Columns:
     - id (uuid, pk)
     - user_id (uuid, fk to auth.users.id)
     - title (text, required)
     - description (text, nullable)
     - completed (boolean, default false)
     - due_date (timestamp, nullable)
     - created_at (timestamp)
     - updated_at (timestamp)
   - Indexes: user_id, completed, due_date
   - RLS: Users can only see/edit their own tasks

**Constraints**:
- Multi-tenant: All queries filtered by user_id automatically via RLS
- Soft deletes: Not needed for MVP

### Constraints (DO NOT TOUCH)
- Don't change Supabase project settings
- Don't add tables beyond users/tasks without asking

### Implementation Instructions
Step 1: Propose migration SQL
Step 2: Implement RLS policies
Step 3: Test: Insert task for user A, verify user B can't see it
```

### Example 2: Auth Foundation

```
You are helping me implement the AUTH foundation for my app.

### Context
**App**: Mobile to-do app for busy parents
**Tech Stack**: React Native (Expo) + Supabase Auth
**Current State**: Database created (users, tasks tables), base app running

### Goal
Implement email/password authentication for MVP

### Requirements
**Flows needed**:
1. Signup: Email + password (6+ chars), auto-login after signup
2. Login: Email + password, redirect to /tasks on success
3. Logout: Clear session, redirect to /login
4. Password reset: Email flow with magic link
5. Session management: Supabase session tokens, auto-refresh

**User fields**: (managed by Supabase Auth)
- Email (required, unique)
- Password (required, hashed)
- Email verification: Not required for MVP

**Constraints**:
- No social OAuth for MVP (add later)
- No 2FA for MVP
- Session expires after 7 days

### Constraints (DO NOT TOUCH)
- Don't modify database schema
- Don't change navigation structure yet (will integrate after)

### Implementation Instructions
Step 1: Propose auth flow and screens (Signup, Login, ForgotPassword)
Step 2: Implement Supabase Auth integration
Step 3: Test all flows:
  - [ ] Can signup with email/password
  - [ ] Can login with credentials
  - [ ] Can't login with wrong password
  - [ ] Can logout
  - [ ] Can reset password via email
  - [ ] Session persists across app restarts
```

### Example 3: Payments Foundation

```
You are helping me implement the PAYMENTS foundation for my app.

### Context
**App**: Mobile to-do app with Pro features
**Tech Stack**: React Native + Supabase + Stripe + RevenueCat
**Current State**: Auth working, users can signup/login

### Goal
Implement subscription payments for Pro tier (MVP only)

### Requirements
**Payment flows**:
1. One-time: No (not needed)
2. Subscription: Yes
   - Free tier: Basic task management
   - Pro tier: $4.99/month - Voice capture, shared lists, AI suggestions
3. Trial: 7-day free trial for Pro

**Stripe Products** (create in Stripe Dashboard first):
- Product: "TaskMaster Pro"
- Price: $4.99/month (recurring)
- Trial: 7 days

**RevenueCat** (for mobile in-app purchases):
- iOS: App Store subscription
- Android: Google Play subscription
- Both map to same "Pro" entitlement

**Webhooks** (from Stripe):
- `customer.subscription.created`: Grant Pro access
- `customer.subscription.updated`: Update Pro status
- `customer.subscription.deleted`: Revoke Pro access

### Constraints (DO NOT TOUCH)
- Don't modify auth system
- Don't add payment UI yet (just backend logic)

### Implementation Instructions
Step 1: Propose:
  - Supabase tables for subscriptions
  - Stripe webhook handler structure
  - RevenueCat integration approach

Step 2: Implement backend
Step 3: Test in Stripe sandbox:
  - [ ] Subscription created → Pro access granted
  - [ ] Subscription canceled → Pro access revoked
  - [ ] Trial ends → Payment processed or access revoked
```

---

**Remember**:
1. ONE foundation per chat (don't mix DB + Auth in same conversation)
2. Propose plan BEFORE implementing
3. Test thoroughly before moving to next foundation
4. Store decisions in Memory-MCP for future reference


---
*Promise: `<promise>FOUNDATION_PROMPT_TEMPLATE_VERIX_COMPLIANT</promise>`*
