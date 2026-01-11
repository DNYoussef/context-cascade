# Feature Prompt Framework

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



Use this template when implementing features with AI coding tools (Cursor, Claude Code, Lovable, Bolt).

**Critical**: Use in a FRESH AI chat (don't reuse previous conversations).

---

## 1. Context

I'm building a [web/mobile] app for [target user] to [primary outcome].

**App**: [1-2 sentence description]

**This feature**: [Short name and purpose]

---

## 2. User Journey (step-by-step narrative)

What the user does and sees:

1. User opens [screen/page]
2. User clicks [button/link]
3. User sees [what appears]
4. User enters [data in form]
5. User clicks [submit/next]
6. System [processes/saves/validates]
7. User sees [success message/next screen]

**Edge Cases**:
- Empty inputs: [expected behavior]
- Invalid data: [validation rules]
- Error states: [error messages]

---

## 3. Technology & Data

### Stack
- **Frontend**: [Next.js/React/Vue/React Native]
- **Backend**: [Next API routes/Supabase/Express/FastAPI]
- **Database**: [Supabase Postgres/MongoDB/etc.]

### DB Changes
- **New tables**:
  - `[table_name]` with columns: [col1, col2, col3, ...]

- **New columns**:
  - `[existing_table].[new_column]` (type: [string/int/etc.])

- **New relationships**:
  - `[table1]` → `[table2]` (foreign key on [column])

### APIs/External Services (if applicable)
- **[Service Name]**: [Purpose]
  - Example: OpenAI for generating suggested tasks
  - Example: Stripe for payment processing

---

## 4. Design Direction

### Style Notes
- **Overall**: Clean, minimal, mobile-first
- **Reuse**: Use existing components from `components/[Button|Input|Card].tsx`
- **Layout**: [Same as X screen / Grid 2-column / Stack vertical / etc.]
- **Colors**: Follow existing color palette from `styles/colors.ts`

### Specific UI Elements
- **Buttons**: [Primary/Secondary/Danger style]
- **Forms**: [Inline validation / Submit behavior]
- **Loading states**: [Spinner / Skeleton / Progress bar]
- **Empty states**: [Message when no data]

---

## 5. Negative Constraints (DO NOT TOUCH)

**CRITICAL - DO NOT MODIFY**:
- Do NOT change auth flow (files: `auth/*`, `middleware/auth.ts`)
- Do NOT rename existing DB columns (breaks existing code)
- Do NOT modify payment logic (files: `payments/*`, `api/stripe/*`)
- Do NOT alter core navigation components (files: `components/Nav.tsx`, `layouts/*`)
- Do NOT change environment variable names (breaks deployment)

**Other Constraints**:
- [Add app-specific constraints]
- [Protected files/components]
- [API contracts that must remain stable]

---

## 6. Implementation Instructions

**Step 1: Propose a Plan**
- Outline the files you'll create/modify
- Describe the main changes
- Wait for my approval before proceeding

**Step 2: Implement Step-by-Step**
- Make changes incrementally
- After each significant change, summarize what you did
- Stick to the scope defined above

**Step 3: Testing Checklist**
- [ ] User journey works end-to-end
- [ ] Edge cases handled (empty, invalid, error)
- [ ] Mobile responsive (if applicable)
- [ ] No console errors
- [ ] "Do not touch" constraints respected

---

## Example Feature Prompt

```
# Feature Prompt Framework

## 1. Context
I'm building a mobile to-do app for busy parents of toddlers to reduce mental load.
This feature: **Shared Family Lists** - allow co-parents to collaborate on a single task list

## 2. User Journey
1. User opens "Lists" screen
2. User clicks "Create Shared List" button
3. User sees form: "List Name" and "Share with (email)"
4. User enters "Grocery Shopping" and partner's email "partner@example.com"
5. User clicks "Create & Share"
6. System creates list and sends email invitation
7. User sees confirmation: "List created! Invitation sent to partner@example.com"
8. Partner receives email, clicks link, list appears in their app

**Edge Cases**:
- Empty email: Show validation "Email required"
- Invalid email: Show "Please enter valid email"
- Partner not registered: Send invitation email to sign up

## 3. Technology & Data

### Stack
- Frontend: React Native (Expo)
- Backend: Supabase
- Database: Supabase Postgres

### DB Changes
- New table: `shared_lists`
  - Columns: id (uuid), name (text), owner_id (uuid), created_at (timestamp)
- New table: `shared_list_members`
  - Columns: id (uuid), list_id (uuid), user_id (uuid), invited_email (text), status (enum: pending/accepted)
- New column: `tasks.shared_list_id` (uuid, nullable, foreign key to shared_lists.id)

### APIs
- Supabase Realtime: For live sync when partner adds/edits tasks
- Resend (email service): Send invitation emails

## 4. Design Direction

### Style
- Clean, minimal, mobile-first
- Reuse: Button from `components/Button.tsx`, Input from `components/Input.tsx`
- Layout: Stack vertical (form fields), full-width buttons

### Specific UI
- Buttons: Primary style for "Create & Share", secondary for "Cancel"
- Forms: Inline validation on blur
- Loading: Show spinner on button during creation
- Empty state: "No shared lists yet. Create one to collaborate!"

## 5. Negative Constraints (DO NOT TOUCH)

**DO NOT**:
- Change auth flow (files: `auth/*`, `utils/supabase.ts`)
- Rename existing DB columns (breaks: tasks.id, tasks.user_id, etc.)
- Modify navigation (files: `navigation/*`)

## 6. Implementation Instructions

Step 1: Propose plan for:
- DB migrations for new tables
- React Native screens/components
- Supabase queries
- Email integration

Step 2: Implement incrementally
Step 3: Test checklist above
```

---

**Remember**:
1. Fresh AI chat per feature
2. Include all 6 sections
3. "Do not touch" list is MANDATORY
4. User journey must be specific and testable


---
*Promise: `<promise>FEATURE_PROMPT_FRAMEWORK_VERIX_COMPLIANT</promise>`*
