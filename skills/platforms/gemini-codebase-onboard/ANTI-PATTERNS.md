# Gemini Codebase Onboard Anti-Patterns

## Anti-Pattern 1: Using for Small Codebases

**Problem**: Using 1M token megacontext for projects that fit in standard context.

```text
BAD:
[Small 500 line project]
gemini --all-files "Analyze this small project"

GOOD:
[Small 500 line project]
[Read files directly with Claude]
[Save megacontext for large codebases]
```

**Why it matters**: Gemini switches to Flash model after 5 min. Overkill for small projects.

## Anti-Pattern 2: Expecting Implementation

**Problem**: Asking Gemini to implement features during onboarding.

```text
BAD:
gemini --all-files "Understand codebase AND implement new auth feature"

GOOD:
gemini --all-files "Understand codebase architecture"
THEN
codex "Implement new auth feature based on patterns discovered"
```

**Why it matters**: Gemini gets stuck in loops on implementation. Use it for analysis only.

## Anti-Pattern 3: Ignoring Analysis Errors

**Problem**: Trusting Gemini output when it clearly has errors.

```text
BAD:
Gemini: "The codebase uses React..." [missing closing tag in output]
Agent: [Proceeds with incomplete analysis]

GOOD:
Gemini: "The codebase uses React..." [missing closing tag]
Agent: [Notes error, re-queries specific section]
Agent: [Validates findings against actual code]
```

**Why it matters**: Gemini can generate errors in analysis. Verify before trusting.

## Anti-Pattern 4: Not Storing Results

**Problem**: Running megacontext analysis without capturing findings.

```text
BAD:
[Run megacontext analysis]
[Start implementing]
[Forgot what Gemini said]

GOOD:
[Run megacontext analysis]
[Save architecture map to docs/]
[Store in Memory-MCP]
[Reference during implementation]
```

**Why it matters**: Megacontext is expensive. Capture value permanently.

## Anti-Pattern 5: Using for Complex Reasoning

**Problem**: Expecting Gemini to do deep reasoning during onboarding.

```text
BAD:
gemini --all-files "Analyze codebase and determine the best way to fix the performance issue considering all tradeoffs"

GOOD:
gemini --all-files "Map the architecture and identify where performance-critical code paths are"
THEN
Claude: [Reason about optimization tradeoffs]
```

**Why it matters**: Claude is better at complex reasoning. Use Gemini for breadth, Claude for depth.

## Anti-Pattern 6: Running Without Clear Questions

**Problem**: Vague analysis requests that waste megacontext.

```text
BAD:
gemini --all-files "Tell me about this codebase"

GOOD:
gemini --all-files "Analyze this codebase and document:
1. High-level architecture (components, layers)
2. Key design patterns used
3. External dependencies and integrations
4. Data flow between major components
5. Configuration and environment setup"
```

**Why it matters**: Specific questions get specific answers.

## Anti-Pattern 7: Single Pass Expectation

**Problem**: Expecting complete understanding from one query.

```text
BAD:
[One megacontext pass]
"I now fully understand everything"

GOOD:
[First pass: Architecture overview]
[Second pass: Specific subsystem deep-dive]
[Third pass: Integration patterns]
[Synthesize with Claude]
```

**Why it matters**: Complex codebases need layered analysis.

## Anti-Pattern 8: Using During Active Development

**Problem**: Running megacontext when files are rapidly changing.

```text
BAD:
[Mid-feature development]
gemini --all-files "What's the current state?"
[Files change while Gemini runs]
[Stale results]

GOOD:
[Stable codebase state]
gemini --all-files "Analyze architecture"
[Results reflect actual state]
```

**Why it matters**: Megacontext takes time. Use on stable code.

## Recovery Protocol

If you find yourself in an anti-pattern:

1. STOP current analysis
2. Identify what specific questions you actually need answered
3. Formulate targeted queries
4. Run appropriate tool (megacontext vs direct read)
5. Capture and store valuable findings
