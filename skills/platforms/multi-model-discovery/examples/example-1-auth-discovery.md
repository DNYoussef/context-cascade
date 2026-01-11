# Example 1: Authentication Implementation Discovery

## Scenario

User wants to implement user authentication for a Node.js/Express application.

## Discovery Process

### Step 1: Initial Query

```bash
./scripts/multi-model/delegate.sh gemini "What are best practices for user authentication in Node.js Express 2024? Find existing libraries: passport, next-auth, lucia-auth, better-auth"
```

### Step 2: Gemini Response (Synthesized)

```yaml
discovered_libraries:
  - name: passport.js
    stars: 22k
    last_update: 2024
    pros: ["Battle-tested", "Many strategies", "Large ecosystem"]
    cons: ["Complex setup", "Callback-based"]

  - name: lucia-auth
    stars: 8k
    last_update: 2024
    pros: ["Type-safe", "Modern", "Lightweight"]
    cons: ["Smaller ecosystem", "Newer"]

  - name: better-auth
    stars: 5k
    last_update: 2024
    pros: ["Zero-config", "Built-in UI"]
    cons: ["Less flexible"]

best_practices:
  - Use refresh tokens with rotation
  - Store tokens securely (httpOnly cookies)
  - Implement rate limiting on auth endpoints
  - Use PKCE for OAuth flows
  - Hash passwords with bcrypt/argon2
```

### Step 3: Claude Synthesis

Based on the research:

| Factor | Passport | Lucia | Better-Auth |
|--------|----------|-------|-------------|
| Project Size | Large | Medium | Small |
| Type Safety | Partial | Full | Partial |
| Learning Curve | High | Medium | Low |
| Flexibility | High | High | Low |

**Recommendation**: For this project (medium-sized, TypeScript), **lucia-auth** is the best fit.

### Step 4: Memory Storage

```bash
# Store decision
mcp__memory-mcp__memory_store \
  --key "discovery/auth/express-2024" \
  --value '{"chosen": "lucia-auth", "reason": "type-safe, modern, fits project size"}' \
  --tags "WHO=multi-model-discovery,WHY=auth-implementation,PROJECT=my-app"
```

### Step 5: Proceed to Implementation

```bash
# Now use codex-iterative-fix for implementation
./scripts/multi-model/delegate.sh codex "Implement lucia-auth following best practices: refresh token rotation, httpOnly cookies, rate limiting" --full-auto
```

## Outcome

- **Time saved**: ~4 hours of trial-and-error
- **Quality**: Used proven library with modern patterns
- **Knowledge**: Captured for future reference
