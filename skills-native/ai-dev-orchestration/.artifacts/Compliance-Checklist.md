# Compliance Checklist

Use this checklist before calling a feature "done". Ensures AI-assisted development follows best practices.

---

## Per-Feature Compliance

Before marking feature as **COMPLETE**, verify:

### 1. Specification & Planning

- [ ] **Feature has brief written spec**
  - Location: `docs/features/[feature-name].md`
  - Contains: Name, Purpose (1 sentence), User Journey, Data Changes, Design Direction
  - User journey is specific and testable (not vague)

- [ ] **Feature Prompt Framework used**
  - All 6 sections present: Context, User Journey, Tech & Data, Design, Constraints, Instructions
  - "Do not touch" list included and specific
  - Fresh AI chat used (not reused from previous feature)

### 2. Implementation

- [ ] **Work in fresh AI chat**
  - New conversation started for this feature
  - No context pollution from previous features
  - Chat closed after feature complete

- [ ] **"Do not touch" list respected**
  - Auth flow unchanged (unless explicitly scoped)
  - DB schema unchanged (unless explicitly scoped)
  - Payment logic unchanged (unless explicitly scoped)
  - Core navigation unchanged (unless explicitly scoped)
  - No scope creep into protected areas

- [ ] **Implementation matches spec**
  - All user journey steps work as described
  - Data changes match specification
  - Design follows direction
  - No unintended changes to other features

### 3. Testing

- [ ] **Manual tests executed against user journey**
  - Each step in user journey tested end-to-end
  - Happy path works
  - Edge cases tested (empty inputs, invalid data, error states)
  - Mobile responsive (if applicable)
  - No console errors or warnings

- [ ] **Bugs fixed or logged**
  - Critical bugs: FIXED before acceptance
  - Non-critical bugs: Logged with owner, priority, and timeline
  - Bug count: ≤5 per feature (never accumulate large backlog)

### 4. Documentation

- [ ] **Changes documented (3-5 bullets)**
  - What the feature does
  - What tables/routes/components it touches
  - Any TODOs or known limitations
  - Example:
    ```
    ## Feature: Shared Family Lists

    - Allows co-parents to collaborate on task lists
    - New tables: shared_lists, shared_list_members
    - Routes: POST /api/lists/share, GET /api/lists/shared
    - Components: ShareListModal.tsx, SharedListView.tsx
    - TODO: Add real-time sync when partner adds task
    ```

- [ ] **Committed with clear message**
  - Format: `feat: [feature-name]`
  - Body includes: What it does, key details, files/tables touched
  - Includes: "Tested: [user-journey-summary]"
  - Includes: Co-authorship attribution
  - Example:
    ```
    git commit -m "feat: Shared family lists

    - Allow co-parents to collaborate on task lists
    - New tables: shared_lists, shared_list_members
    - Email invitations via Resend
    - Real-time sync via Supabase Realtime

    Tested: Create shared list → invite partner → partner receives email → clicks link → list appears

    🤖 Generated with [Claude Code](https://claude.com/claude-code)

    Co-Authored-By: Claude <noreply@anthropic.com>"
    ```

### 5. Quality Gates

- [ ] **Feature accepted or rolled back (never left broken)**
  - Decision: ACCEPT or ROLLBACK (not "we'll fix later")
  - If ACCEPT: All tests pass, documented, committed
  - If ROLLBACK: Changes discarded, spec revised, restart loop

- [ ] **No accumulation of technical debt**
  - Code is production-quality (not "quick and dirty")
  - No commented-out code
  - No TODOs for critical functionality
  - Follows existing code patterns and style

---

## Per-Foundation Compliance

Before marking foundation as **COMPLETE**, verify:

### 1. Foundation Specification

- [ ] **Foundation Prompt Template used**
  - Context section complete (app, stack, current state)
  - Requirements section specific (MVP only)
  - Constraints section includes "do not touch" list

- [ ] **Fresh AI chat used**
  - New conversation per foundation (DB, Auth, Payments, etc.)
  - No mixing foundations in same chat

### 2. Implementation

- [ ] **Plan reviewed and approved**
  - AI proposed plan before implementing
  - Plan reviewed for scope creep
  - Plan approved explicitly

- [ ] **Implementation complete**
  - All requirements from spec implemented
  - No missing pieces
  - No extra features added without approval

### 3. Testing

- [ ] **Manual tests passing**
  - Database: Migrations run, tables created, CRUD operations work, RLS policies enforced
  - Auth: Signup works, login works, logout works, session persists
  - Payments: Sandbox payment succeeds, webhooks processed
  - APIs: External API calls succeed, errors handled gracefully

### 4. Documentation

- [ ] **Committed with clear message**
  - Format: `feat: [foundation-name] foundation`
  - Body includes: What was implemented, key decisions, testing summary

---

## Overall Project Compliance

### Behavioral Rules (Verified Throughout)

- [ ] **Never asked AI to "build my whole app"**
  - Always scoped to: one foundation OR one feature
  - No large batches of multiple features in one chat

- [ ] **Every feature had user journey**
  - Specific, testable steps (not vague descriptions)
  - Edge cases considered

- [ ] **Every prompt included "do not touch" list**
  - Protected DB schema, auth, payments by default
  - Added app-specific protected areas

- [ ] **One chat = one feature/foundation**
  - Context reset after each task
  - No chat reuse across features

- [ ] **Architecture choices documented with rationale**
  - Tech stack decisions recorded in `docs/tech-stack-decision.md`
  - Database schema decisions in migration comments
  - Major design decisions in feature specs or ADRs

- [ ] **Manual testing done before automated tests**
  - Understand failure modes first
  - Automated tests added incrementally

- [ ] **AI treated as factory, human as orchestrator**
  - Human wrote specs
  - Human ran pipeline
  - Human made pass/fail decisions
  - AI executed within constraints

---

## Metrics to Track

Track these metrics in Memory-MCP or project dashboard:

### Velocity
- Features completed per week
- Average time per feature (target: 1-3 hrs)
- Rollback rate (target: ≤20%)

### Quality
- Bugs per feature (target: ≤5)
- Test coverage (target: ≥80%)
- Deployment success rate (target: 100%)

### Compliance
- % features using Feature Prompt Framework (target: 100%)
- % features with "do not touch" list (target: 100%)
- % features with user journey (target: 100%)
- % features tested manually (target: 100%)
- % features documented (target: 100%)

---

## Red Flags (Immediate Stop & Review)

**STOP** and review if any of these occur:

🚩 **Feature implemented without written spec**
  - Action: Stop, write spec, restart

🚩 **"Do not touch" list violated**
  - Action: Rollback, add explicit constraint, restart

🚩 **Multiple features mixed in same chat**
  - Action: Rollback, separate into individual chats

🚩 **>10 bugs accumulated**
  - Action: Stop feature development, fix bugs first

🚩 **Test coverage <50%**
  - Action: Pause, add tests, then continue

🚩 **Deployment failing repeatedly**
  - Action: Fix deployment pipeline before next feature

🚩 **AI "hallucinating" implementations (theater coding)**
  - Action: Manual sandbox testing, theater-detection-audit skill

🚩 **Scope creep into unrelated areas**
  - Action: Rollback, tighten constraints, restart

---

## Review Frequency

- **Per-Feature**: This checklist (before marking complete)
- **Weekly**: Overall project metrics review
- **Monthly**: Compliance rate audit (should be 100%)

---

**Remember**: Compliance is not bureaucracy—it prevents chaos, rework, and broken deploys.
