# Example 2: TypeScript Build Errors

## Scenario

TypeScript strict mode enabled, 47 type errors blocking build.

## Process

### Step 1: Capture Error Baseline

```bash
npx tsc --noEmit 2>&1 | tee tsc-errors.log

# Output:
# error TS2322: Type 'string | undefined' is not assignable to type 'string'
# error TS2345: Argument of type 'null' is not assignable to parameter
# error TS7006: Parameter 'x' implicitly has an 'any' type
# ... (47 errors total)
```

### Step 2: Categorize Errors

```yaml
error_categories:
  strict_null_checks:
    count: 22
    pattern: "Type 'X | undefined' is not assignable"

  implicit_any:
    count: 15
    pattern: "Parameter 'x' implicitly has an 'any' type"

  type_mismatch:
    count: 7
    pattern: "Type 'X' is not assignable to type 'Y'"

  missing_properties:
    count: 3
    pattern: "Property 'x' does not exist on type"
```

### Step 3: Execute Codex Fix

```bash
./scripts/multi-model/codex-yolo.sh \
  "Fix all 47 TypeScript errors. Categories:
   1. Strict null checks (22): Add proper null handling
   2. Implicit any (15): Add explicit type annotations
   3. Type mismatches (7): Fix type declarations
   4. Missing properties (3): Add to interfaces
   Preserve existing functionality." \
  fix-types-001 \
  "." \
  20 \
  full-auto
```

### Step 4: Iteration Progress

```text
[Iteration 1-5] Fixing strict null checks...
  - Added optional chaining (?.)
  - Added nullish coalescing (??)
  - Added type guards where needed

[Iteration 6-10] Adding type annotations...
  - Annotated function parameters
  - Added return types
  - Created utility types

[Iteration 11-15] Fixing type mismatches...
  - Updated interface definitions
  - Added type assertions where safe
  - Fixed generic constraints

[Iteration 16] Running final tsc check...
  SUCCESS - 0 errors
```

### Step 5: Review Quality of Fixes

```typescript
// BEFORE (bad)
function processUser(user) {
  return user.name.toUpperCase();
}

// AFTER (good - Codex fix)
function processUser(user: User): string {
  return user.name?.toUpperCase() ?? '';
}

// NOT this (over-engineered)
function processUser(user: User | null | undefined): string | null | undefined {
  if (user === null || user === undefined) return undefined;
  if (user.name === null || user.name === undefined) return null;
  return user.name.toUpperCase();
}
```

### Step 6: New Types Created

```typescript
// src/types/utils.ts (new file by Codex)
export type Nullable<T> = T | null | undefined;

export interface ApiResponse<T> {
  data: T;
  error?: string;
  metadata?: Record<string, unknown>;
}

export type UserRole = 'admin' | 'user' | 'guest';
```

### Step 7: Final Verification

```bash
# Type check
npx tsc --noEmit  # Success!

# Run tests (ensure no regressions)
npm test  # All passing

# Build
npm run build  # Success!
```

### Step 8: Document

```json
{
  "key": "fixes/typescript/strict-mode-2024",
  "value": {
    "errors_fixed": 47,
    "categories": {
      "strict_null": 22,
      "implicit_any": 15,
      "type_mismatch": 7,
      "missing_props": 3
    },
    "new_files": ["src/types/utils.ts"],
    "patterns_used": [
      "optional_chaining",
      "nullish_coalescing",
      "type_guards",
      "utility_types"
    ],
    "iterations": 16
  },
  "tags": "WHO=codex-iterative-fix,WHY=strict-mode,PROJECT=my-app"
}
```

## Outcome

- **Errors fixed**: 47/47
- **Build status**: Passing
- **Tests**: All green
- **New technical debt**: None (clean solutions)
- **Time**: ~20 minutes
