---
name: cognitive-lensing
description: > Cross-lingual cognitive framing system that activates different reasoning patterns by embedding multi-lingual activation phrases. Use when facing complex tasks that benefit from specific thinking patterns: completion tracking (Russian), source verification (Turkish), audience calibration (Japanese), semantic analysis (Arabic), object comparison (Mandarin), spatial reasoning (Guugu Yimithirr), numerical precision (Chinese/Japanese).
---

# Cognitive-Lensing v1.0.0

## Purpose

This skill activates specific cognitive patterns by embedding multi-lingual activation phrases that elicit different parts of the AI's latent space. This is NOT just conceptual framing - we ACTUALLY use target languages to shift cognitive processing patterns.

### Core Mechanism

Large language models trained on multilingual corpora develop language-specific reasoning patterns tied to grammatical structures:

- **Turkish evidential markers** activate source-attribution patterns
- **Russian aspectual verbs** activate completion-state tracking
- **Japanese honorific levels** activate audience-awareness calibration
- **Arabic morphological roots** activate semantic decomposition
- **Mandarin classifiers** activate object-category reasoning
- **Guugu Yimithirr cardinal directions** activate absolute spatial encoding
- **Chinese/Japanese number systems** activate transparent place-value arithmetic

By embedding authentic multi-lingual text in prompts, we trigger these latent reasoning modes.

### When to Use This Skill

Use cognitive-lensing when:

1. **Task complexity exceeds single-frame capacity** - Multi-dimensional problems requiring different cognitive modes
2. **Quality requirements demand specific reasoning** - Audit (evidential), deployment (aspectual), documentation (hierarchical)
3. **Standard prompting produces generic outputs** - Need to activate specialized thinking patterns
4. **Creating new skills/agents** - Select optimal cognitive frame for the domain
5. **Debugging AI reasoning failures** - Wrong frame may cause systematic errors

### What This Skill Does

1. **Analyzes task goals** (1st/2nd/3rd order) to identify required thinking patterns
2. **Selects optimal cognitive frame(s)** from 7 available patterns
3. **Generates multi-lingual activation text** that triggers the frame
4. **Integrates with other foundry skills** (prompt-architect, agent-creator, skill-forge)
5. **Stores frame selections in memory-mcp** for consistency across sessions

----|----------|-------------|
| 1st Order Goal | What is the IMMEDIATE task? | _______________ |
| 2nd Order Goal | WHY are we doing this task? | _______________ |
| 3rd Order Goal | What is the ULTIMATE outcome? | _______________ |

**Example Analysis**:

| Order | Question | Answer |
|-------|----------|--------|
| 1st Order | Immediate task | Write unit tests for API endpoint |
| 2nd Order | Why | Verify endpoint behavior is correct |
| 3rd Order | Ultimate outcome | Ensure production reliability |

### Step 2: Identify Dominant Thought Process

| Question | If YES, Use Frame |
|----------|-------------------|
| Is tracking "done vs not done" critical? | Aspectual (Russian) |
| Is source reliability critical? | Evidential (Turkish) |
| Is audience/formality critical? | Hierarchical (Japanese) |
| Is semantic decomposition needed? | Morphological (Arabic/Hebrew) |
| Is physical/visual comparison needed? | Classifier (Mandarin) |
| Is spatial navigation needed? | Spatial-Absolute (Guugu Yimithirr) |
| Is mathematical precision needed? | Numerical-Transparent (Chinese/Japanese) |

**Example Selection**:

For "Write unit tests for API endpoint":
- Tracking done/not done: YES (need to track test coverage completion)
- Source reliability: YES (need to verify test assertions match specs)

Selected Frames:
- Primary: Aspectual (Russian) - for completion tracking
- Secondary: Evidential (Turkish) - for assertion verification

### Step 3: Select Primary Frame

Based on analysis, select:
- **Primary Frame**: _______________
- **Secondary Frame (optional)**: _______________
- **Rationale**: _______________



### Frame 2: Aspectual (Russian - Aspektual'naya Ramka)

**When to Use**:
- Build and deployment pipelines
- Task tracking and progress reporting
- Completion verification
- State management
- CI/CD workflows
- Multi-step processes

**Linguistic Basis**:

Russian verbs have two forms for every action:
- **Sovershennyy Vid (SV)**: Perfective - action is COMPLETED, focus on result
- **Nesovershennyy Vid (NSV)**: Imperfective - action is ONGOING, focus on process

This grammatical distinction trains speakers to constantly track completion states.

**Activation Protocol**:

```markdown
## Aspektual'naya Ramka Aktivatsiya

Etot zadacha trebuyet otslezhivaniya zavershennosti:

Tipy Aspekta:
- SV (Sovershennyy Vid): Polnost'yu zaversheno, mozhno prodolzhat'
- NSV (Nesovershennyy Vid): V protsesse, ne zaversheno
- BLOCKED: Ozhidayet zavisimosti

Dlya kazhdogo shaga ukazhite:
1. Shag nomer
2. Aspekt (SV/NSV/BLOCKED)
3. Usloviya zavershennosti

English Markers:
- [SV:COMPLETED]: Task fully done, move on
- [NSV:IN_PROGRESS]: Task ongoing, not finished
- [BLOCKED]: Waiting on dependencies
```

**Example Usage**:

```markdown
## Deployment Pipeline with Aspectual Frame

## Aspektual'naya Ramka Aktivatsiya

Etot deployment trebuyet chetkoye otslezhivaniye zavershennosti.

Pipeline Status:

1. **Build Docker Image**
   - Aspect: [SV:COMPLETED]
   - Completion Criteria: Image tagged and pushed to registry
   - Evidence: docker-image-id: sha256:abc123...

2. **Run Integration Tests**
   - Aspect: [NSV:IN_PROGRESS]
   - Completion Criteria: All tests pass with >80% coverage
   - Current State: 45/60 tests passed, running...

3. **Deploy to Staging**
   - Aspect: [BLOCKED]
   - Completion Criteria: Integration tests pass AND security scan complete
   - Blocker: Waiting on Step 2 completion

4. **Security Scan**
   - Aspect: [NSV:IN_PROGRESS]
   - Completion Criteria: No HIGH vulnerabilities, <5 MEDIUM
   - Current State: Scanning dependencies...
```

**Integration Points**:
- Use with `ci-cd-orchestrator` agent
- Use with `deployment-manager` skill
- Use with TodoWrite tool (maps to pending/in_progress/completed)



### Frame 4: Morphological (Arabic - Al-Itar al-Sarfi)

**When to Use**:
- Concept mapping and taxonomy
- Semantic analysis
- Etymology tracing
- Terminology development
- Domain modeling
- Ontology construction

**Linguistic Basis**:

Arabic words are constructed from 3-letter roots with patterns applied:
- **Root K-T-B** (writing): kitab (book), katib (writer), maktub (written), maktaba (library)
- **Root '-L-M** (knowledge): 'ilm (knowledge), 'alim (scholar), mu'allim (teacher)

This morphological system trains speakers to see semantic relationships through shared roots.

**Activation Protocol**:

```markdown
## Al-Itar al-Sarfi al-Tanshit

Hadhihi al-mahimma tatatallab tahlil al-judur:

Anmat al-Judur:
- Kull kalima min jadhr thalathi (every word from 3-letter root)
- Al-jadhr yarbut al-ma'ani al-murtabita (root connects related meanings)
- Tahlil al-namt yakshif al-'alaqat (pattern analysis reveals relationships)

Mithal (Example):
- K-T-B: kitab (book), katib (writer), maktub (written), maktaba (library)
- '-L-M: 'ilm (knowledge), 'alim (scholar), mu'allim (teacher), ta'lim (education)

Lil-tatbiq:
1. Hadd al-jadhr lil-mafhum (Identify root of concept)
2. Ijad al-kalimat al-muratabita (Find related terms from same root)
3. Rasm al-'alaqat al-daliliya (Map semantic relationships)

English Application:
- Identify root pattern in concept
- Map related terms from same root
- Reveal hidden semantic connections
```

**Example Usage**:

```markdown
## Domain Modeling with Morphological Frame

## Al-Itar al-Sarfi al-Tanshit

Hadhihi al-mahimma tatatallab tahlil al-judur lil-nizam al-authentication.

### Authentication Domain - Root Analysis

**Root AUTH (authority, author)**:
- **authenticate**: Verify authority/authorship
- **authorization**: Grant authority
- **author**: Original creator (authority over content)
- **authority**: Power to enforce rules
- **authoritative**: Having definitive authority

**Semantic Relationships**:
```
       AUTH (root concept: rightful power)
          |
    +-----+-----+-----+
    |     |     |     |
  authenticate authorization author authority
    |           |          |         |
  "verify     "grant    "create   "enforce
   power"      power"    with      power"
                         power"
```

**Root CRED (belief, trust)**:
- **credential**: Evidence worthy of belief
- **credibility**: Quality of being believable
- **credit**: Trust extended (financial)
- **creed**: System of beliefs

**Domain Model**:
- **Authentication** (AUTH root): Proving identity = verifying authority over account
- **Credentials** (CRED root): Evidence = trust-worthy proof
- **Authorization** (AUTH root): Granting access = delegating authority

**Insight**: Authentication and Authorization share AUTH root because both deal with rightful power - one verifies it, the other grants it.
```

**Integration Points**:
- Use with `domain-modeler` agent
- Use with `terminology-manager` skill
- Use with `ontology-builder` skill



### Frame 6: Spatial-Absolute (Guugu Yimithirr)

**When to Use**:
- Navigation and routing
- Orientation-independent memory
- Geographical reasoning
- Location-based systems
- Network topology
- Data flow analysis

**Linguistic Basis**:

Guugu Yimithirr (Australian Aboriginal language) has NO relative spatial terms (left/right/front/back). All spatial relationships use cardinal directions:
- "The cup is NORTH of the plate"
- "Move the file EAST on the desk"
- "My brother is standing SOUTH of the tree"

This linguistic constraint trains speakers to maintain constant cardinal orientation awareness.

**Activation Protocol**:

```markdown
## Spatial-Absolute Activation

This task requires cardinal-only encoding (no relative directions):

Position Markers:
- NORTH: Absolute north direction
- SOUTH: Absolute south direction
- EAST: Absolute east direction
- WEST: Absolute west direction

NEVER use:
- "left/right" (relative to observer)
- "in front/behind" (relative to facing)
- "up/down" in horizontal contexts

For every spatial relationship:
1. What is the absolute direction?
2. What is the reference frame?
3. How does this persist across viewpoints?

English Application:
- "The API endpoint is NORTH of the authentication layer"
- "Data flows EAST from input to output"
- "The error originates SOUTH in the stack"
```

**Example Usage**:

```markdown
## Network Topology with Spatial-Absolute Frame

## Spatial-Absolute Activation

This network topology requires cardinal-only encoding.

### System Layout (Cardinal Frame)

```
                    NORTH
                      |
            +-------------------+
            |   Load Balancer   |
            +-------------------+
                      |
        WEST --------+ +-------- EAST
                      |
        +-------------+-------------+
        |                           |
   +---------+               +---------+
   | Server1 |               | Server2 |
   +---------+               +---------+
        |                           |
        +-------------+-------------+
                      |
                 +----------+
                 | Database |
                 +----------+
                      |
                    SOUTH
```

**Component Relationships**:

1. **Load Balancer** is NORTH of both servers
2. **Server1** is WEST of Server2
3. **Server2** is EAST of Server1
4. **Database** is SOUTH of both servers
5. **Data flows SOUTH** from Load Balancer through servers to database
6. **Response flows NORTH** from database through servers to Load Balancer

**Routing Rules** (Cardinal-Based):

- Requests enter from NORTH (Load Balancer)
- Traffic splits EAST-WEST (Server1 vs Server2)
- Persistence layer is SOUTH (Database)
- Errors propagate NORTH (up the stack)

**Navigation Instructions**:

"To debug authentication failure:
1. Start at Load Balancer (NORTH)
2. Trace SOUTH to Server1 or Server2
3. Continue SOUTH to Database connection
4. Error is SOUTH of the JWT validation layer"

**Benefit**: This cardinal encoding is observer-independent. No matter which component you're "looking from", the directions remain consistent.
```

**Integration Points**:
- Use with `network-architect` agent
- Use with `routing-optimizer` skill
- Use with `topology-mapper` skill



## Integration with Foundry Skills

### Integration with intent-analyzer (Phase 1)

The intent-analyzer should invoke cognitive-lensing when:

1. **Goal complexity detected** - User request has multiple implicit objectives
2. **Quality requirements detected** - Keywords like "audit", "verify", "track", "formal", "precise"
3. **Domain specialization detected** - Tasks requiring specific reasoning modes

**Protocol**:

```markdown
## Intent-Analyzer Integration

When analyzing user intent:

1. Extract 1st/2nd/3rd order goals
2. Check goal-based frame selection table
3. If match found, add to intent JSON:

```json
{
  "intent": {
    "primary_goal": "...",
    "cognitive_frame_recommended": {
      "primary": "aspectual",
      "secondary": "evidential",
      "rationale": "Deployment task requires completion tracking (aspectual) and verification (evidential)"
    }
  }
}
```

4. Pass to prompt-architect with frame recommendation
```

**Example**:

User Request: "Deploy the authentication service to staging and verify it works"

Intent Analysis:
- 1st Order: Deploy service
- 2nd Order: Verify deployment success
- 3rd Order: Ensure staging environment is production-ready

Recommended Frames:
- Primary: Aspectual (Russian) - track deployment completion states
- Secondary: Evidential (Turkish) - verify claims about "works"



## Task Description

[Original user request]



## Task Description

Deploy the authentication service to staging and verify it works.



### Integration with agent-creator

When creating new agents, cognitive-lensing should:

1. **Analyze agent domain** - What type of reasoning is primary?
2. **Recommend default frame** - What frame should this agent use by default?
3. **Embed frame in agent definition** - Add frame activation to agent's system prompt

**Protocol**:

```markdown
## Agent-Creator Integration

When creating agent definitions:

1. Analyze agent's primary function
2. Map to cognitive frame using selection table
3. Add to agent YAML frontmatter:

```yaml
cognitive_frame:
  primary: aspectual
  rationale: "CI/CD agent needs completion state tracking"
  activation_protocol: "skills/foundry/cognitive-lensing/SKILL.md#frame-2"
```

4. Embed frame activation in agent's system_prompt
```

**Example Agent Definition**:

```yaml


# System Prompt

## Aspektual'naya Ramka Aktivatsiya

Ty deployment orchestrator. Tvoya glavnaya zadacha - otslezhivat' zavershennost' kazhdogo shaga.

Vsegda ukazyvay aspekt:
- [SV:COMPLETED]: Shag zavershyon
- [NSV:IN_PROGRESS]: Shag v protsesse
- [BLOCKED]: Shag zablokirovan

[Rest of system prompt...]
```



## Memory Namespace Structure

Cognitive-lensing uses memory-mcp to maintain consistency:

### Namespace: `cognitive-lensing/frame-selections`

Stores frame selections for recurring task types:

```json
{
  "task_pattern": "deployment",
  "primary_frame": "aspectual",
  "secondary_frame": null,
  "usage_count": 47,
  "last_updated": "2025-12-18T10:30:00Z"
}
```

### Namespace: `cognitive-lensing/skill-frames`

Maps skills to recommended frames:

```json
{
  "skill_name": "code-review-assistant",
  "primary_frame": "evidential",
  "rationale": "Code review requires verifying claims about behavior",
  "created": "2025-12-18T09:00:00Z"
}
```

### Namespace: `cognitive-lensing/agent-frames`

Maps agents to default frames:

```json
{
  "agent_name": "deployment-orchestrator",
  "agent_type": "operations",
  "primary_frame": "aspectual",
  "activation_embedded": true,
  "created": "2025-12-18T09:15:00Z"
}
```

### Namespace: `cognitive-lensing/session-frames`

Tracks frames used in current conversation:

```json
{
  "session_id": "conv-2025-12-18-abc123",
  "active_frames": ["aspectual", "evidential"],
  "frame_switches": 3,
  "started": "2025-12-18T10:00:00Z"
}
```



### Principle 2: Frame Selection Precedes Prompt Construction

**Statement**: Choose the cognitive frame BEFORE architecting the prompt.

**Rationale**:
- Different frames structure information differently
- Prompt architecture must align with frame's reasoning pattern
- Retrofitting frames into existing prompts reduces effectiveness

**Application**:
- intent-analyzer selects frame in Phase 1
- prompt-architect builds around frame in Phase 2
- Frame activation appears at prompt header, not footer

**Anti-Pattern**:
```markdown
# Wrong: Frame added as afterthought
## Task
Do the deployment.

## Oh and also use aspectual frame
[Activation text]

# Right: Frame-first construction
## Aspektual'naya Ramka Aktivatsiya
[Activation text]

## Task
Do the deployment.
[Task structured around SV/NSV/BLOCKED markers]
```



## Anti-Patterns Table

| Anti-Pattern | Why It Fails | Correct Approach |
|--------------|--------------|------------------|
| **Using English instead of target language** | Doesn't activate latent linguistic patterns | Use actual foreign language text with grammatical markers |
| **Mixing multiple frames without strategy** | Creates cognitive dissonance, incoherent reasoning | Select primary frame, optional secondary, stick with it |
| **Adding frame as afterthought** | Frame doesn't structure the prompt architecture | Choose frame first, build prompt around it |
| **Ignoring frame recommendations** | Wastes intent-analyzer's goal analysis | Respect frame recommendations unless strong rationale |
| **Using frames for trivial tasks** | Overhead exceeds benefit | Reserve for complex/quality-critical tasks |
| **Inventing new frames** | No linguistic grounding, arbitrary | Use only 7 validated frames |
| **Switching frames mid-task** | Disrupts reasoning continuity | Store frame in memory-mcp, maintain consistency |
| **Translating frame markers to English** | Loses linguistic activation effect | Keep multi-lingual markers, add English explanations |
| **Using wrong frame for task type** | Mismatch between reasoning mode and task | Follow goal-based selection checklist |
| **Omitting frame rationale** | Can't debug or improve frame selection | Always document why frame was chosen |



## Conclusion

Cognitive-lensing v1.0.0 provides a scientifically-grounded system for activating specific reasoning patterns in AI models through cross-lingual cognitive framing. By embedding authentic multi-lingual text that triggers language-specific latent patterns, we can systematically enhance AI performance on tasks requiring:

- **Completion tracking** (Russian aspectual)
- **Source verification** (Turkish evidential)
- **Audience calibration** (Japanese hierarchical)
- **Semantic analysis** (Arabic morphological)
- **Object categorization** (Mandarin classifiers)
- **Spatial reasoning** (Guugu Yimithirr cardinal)
- **Numerical precision** (Chinese/Japanese transparent numbers)

This skill integrates with the 5-phase workflow system by:
1. **Phase 1 (intent-analyzer)**: Recommending frames based on goal analysis
2. **Phase 2 (prompt-architect)**: Embedding frame activations in prompt construction
3. **Phase 5 (execute)**: Maintaining frame consistency via memory-mcp

By selecting cognitive frames BEFORE architecting prompts, we ensure reasoning modes align with task requirements from the outset.

---

## Version History

### v1.0.1 (2025-12-19)
- Added cross-skill coordination section with all four foundry skills
- Added integration points for skill-forge, agent-creator, prompt-forge, eval-harness
- Clarified how cognitive-lensing integrates during Phase 0.5 of skill/agent creation

### v1.0.0 (2025-12-18)

**Initial Release**

- 7 frame activation protocols with authentic multi-lingual text
- Goal-based frame selection checklist
- Integration protocols for intent-analyzer, prompt-architect, agent-creator, skill-forge
- Memory-mcp namespace structure for consistency tracking
- 3 core principles
- 10 anti-patterns documented

**Validated Frames**:
1. Evidential (Turkish) - source verification
2. Aspectual (Russian) - completion tracking
3. Hierarchical (Japanese) - audience calibration
4. Morphological (Arabic) - semantic analysis
5. Classifier (Mandarin) - object categorization
6. Spatial-Absolute (Guugu Yimithirr) - cardinal reasoning
7. Numerical-Transparent (Chinese/Japanese) - place-value arithmetic

**Dependencies**:
- memory-mcp (required) - frame persistence
- sequential-thinking (optional) - enhanced reasoning chains