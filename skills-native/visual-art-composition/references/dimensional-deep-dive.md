# Dimensional Deep-Dive Reference

Extended details for each orthogonal dimension with implementation guidance.

---

## SPATIAL_REPRESENTATION: Extended Values

### linear_perspective
**Origin**: Brunelleschi (1415), codified by Alberti (1435)
**Implementation**:
- Establish horizon line at eye level
- Place vanishing point(s) on horizon
- Draw orthogonals converging to VP
- Objects diminish proportionally with distance
**Prompt Keywords**: "one-point perspective", "vanishing point visible", "receding architecture", "mathematically correct depth"
**What to Avoid**: Multiple inconsistent vanishing points, parallel lines that should converge

### reverse_perspective
**Origin**: Byzantine iconography (4th-15th century)
**Implementation**:
- Objects in "distance" are LARGER than foreground
- Buildings widen toward viewer
- Creates sense of sacred space opening out
- No foreshortening—distant figures fully visible
**Prompt Keywords**: "Byzantine perspective", "inverted depth", "space opens toward viewer", "icons reaching out"
**What to Avoid**: Conventional atmospheric perspective, natural diminution

### aspective_composite
**Origin**: Ancient Egypt (3000+ BCE)
**Implementation**:
- Head in profile, eye frontal
- Shoulders frontal, legs profile
- Each body part shown in most characteristic view
- No foreshortening whatsoever
**Prompt Keywords**: "Egyptian composite view", "aspective rendering", "most recognizable angle per part"
**What to Avoid**: Consistent viewpoint, natural anatomical coherence

### motion_fragmented
**Origin**: Italian Futurism (1909-1918)
**Implementation**:
- Subject appears at multiple temporal positions simultaneously
- Overlapping translucent forms
- Lines of force radiating from moving elements
- Blur and repetition suggest trajectory
**Prompt Keywords**: "chronophotographic", "multiple exposure effect", "Boccioni-style fragmentation", "lines of force"
**What to Avoid**: Static frozen moment, single clear outline

---

## COLOR_PHILOSOPHY: Implementation Details

### emotion_first_ti (Chinese)
**Core Principle**: Saturation and brightness determine mood MORE than hue.
**Decision Tree**:
1. What should viewer FEEL? (calm, tense, energetic, melancholic)
2. Map to saturation/brightness:
   - Calm: Low saturation + High brightness (pastels)
   - Tense: High saturation + Low brightness (deep, pressing)
   - Energetic: High saturation + High brightness (bold, clear)
   - Melancholic: Low saturation + Low brightness (muted, aged)
3. Choose hues LAST, based on temperature needs
4. Use saturation sparingly as visual hierarchy—eye seeks most saturated point

**Example**: "A river scene should feel peaceful. Don't make water blue because water is blue—make it pale gray-white with subtle green undertones because peaceful water feels dissolving and calm."

### relativistic_context (Albers)
**Core Principle**: The same color appears different based on what surrounds it.
**Decision Tree**:
1. What is the background/neighboring color?
2. Will the target color shift toward neighbor's complement?
3. How can surrounding colors make focal color appear richer/duller?
4. Test: place target color on multiple grounds before committing

**Example**: "A medium gray looks greenish next to red, pinkish next to green. To make a red 'pop', surround with muted blue-green, not with another warm color."

### symbolic_coded (Wu Xing / Byzantine)
**Core Principle**: Colors encode meanings beyond visual perception.

**Wu Xing (Chinese Five Elements)**:
| Color | Element | Direction | Meaning |
|-------|---------|-----------|---------|
| Blue-Green (Qing) | Wood | East | Spring, vigor, growth |
| Red (Chi) | Fire | South | Summer, passion, auspice |
| Yellow (Huang) | Earth | Center | Royalty, nourishment |
| White (Bai) | Metal | West | Autumn, purity, mourning |
| Black (Hei) | Water | North | Winter, depth, resilience |

**Byzantine Color Code**:
| Color | Meaning |
|-------|---------|
| Gold | Divine light, heaven |
| Blue | Human nature, mortality |
| Red | Divine nature, Christ's blood |
| Purple | Royalty, Christ as King |
| White | Purity, resurrection |

---

## EMOTIONAL_REGISTER: Practical Application

### itutu_cool (Yoruba)
**Visual Markers**:
- Face: Serene, impassive, gentle, no strain
- Eyes: Large, almond-shaped, calm gaze
- Mouth: Slight smile or neutral, never grimace
- Posture: Balanced, dignified, no tension
- Surface: Smooth, polished, cool sheen
**Paradox**: Can embody powerful spiritual force while remaining utterly composed
**Prompt Language**: "mystic composure", "noble tranquility", "calm containing power", "cool in the Yoruba sense"

### qi_yun_resonance (Chinese)
**Visual Markers**:
- Brushwork feels alive, not mechanical
- Forms breathe—not dead accuracy
- Energy moves through composition
- Spirit of subject captured, not just appearance
**Test Question**: Does this feel like it's vibrating with life, or is it a dead copy?
**Prompt Language**: "spirit resonance", "vital energy", "living brushwork", "qi animating form"

### sublime_awe (Romantic)
**Visual Markers**:
- Vast scale dwarfing human figures
- Dramatic natural forces (storm, mountain, void)
- Light suggesting transcendence or terror
- Human figure small, humbled, facing immensity
**Prompt Language**: "Caspar David Friedrich scale", "terrifying beauty", "nature's power dwarfing humanity", "transcendent vastness"

---

## TENSION PAIRS: Resolution Strategies

### Horror Vacui + Ma (Fill vs. Empty)
**Resolution Options**:
1. **Zone segregation**: Dense focal zone surrounded by empty margin
2. **Gradient transition**: Density increases toward center, dissolves toward edge
3. **Nested frames**: Complex ornament frames empty central subject
4. **Temporal reading**: Dense area is past/memory; empty area is present/potential

### Perfect Ideal + Noble Imperfection
**Resolution Options**:
1. **Ideal form, imperfect surface**: Classical proportion but weathered texture
2. **Imperfect completion**: Beautiful form with deliberate gap/chip
3. **Kintsugi principle**: Ideal restored with visible repair as feature
4. **Age of perfection**: Perfect when made, now showing noble wear

### Dynamic Motion + Serene Stillness
**Resolution Options**:
1. **Eye of storm**: Motion in periphery, stillness at center (face/heart)
2. **Frozen peak**: Maximum tension before release (drawn bow)
3. **Motion trail**: Subject still, ghost trails show past positions
4. **Contrast subjects**: One figure still, surrounding motion

---

## DELIBERATE ABSENCES: Extended Catalog

### What Renaissance Ignores
- Symbolic/non-optical color
- Hierarchical scale by importance
- Multiple simultaneous viewpoints
- Pattern without depth
- Spiritual presence over physical accuracy

### What Wabi-Sabi Ignores
- Symmetry and geometric perfection
- Bright, saturated color
- New, unblemished surfaces
- Monumental scale
- Completion and polish
- Horror vacui density

### What Futurism Ignores
- Static single moment
- Stable vertical/horizontal axes
- Naturalistic color
- Peaceful subjects
- Historical reference
- Completion/polish in traditional sense

### What Byzantine Ignores
- Optical perspective (specifically rejects)
- Natural light and shadow modeling
- Individual portraiture/likeness
- Momentary expression
- Atmospheric depth
- Profane/secular subject matter

### What Islamic Geometric Ignores
- Human and animal figuration
- Central focal hierarchy
- Beginning/end to pattern
- Three-dimensional illusion
- Narrative sequence
- Individual artistic expression

---

## COGNITIVE SEQUENCE: Full Workflows

### Chinese Six Principles Full Process

1. **Before painting**: Contemplate subject until you feel its qi
2. **First stroke**: Is there spirit resonance? If not, do not continue
3. **Bone structure**: Build structural integrity through confident brushwork
4. **Correspondence**: Match essential nature, not optical surface
5. **Color application**: According to type—what colors does this subject's nature call for?
6. **Composition**: Where does each element sit? What is foreground/background/void?
7. **Validation**: Does this honor masters? What did they understand that you must preserve?

### Byzantine Icon Full Process

1. **Prayer and preparation**: Fast, pray, purify intent
2. **Prototype selection**: Which approved model will guide this?
3. **Ground preparation**: Gesso, gold leaf for heavenly light
4. **Outline**: Follow prototype faithfully
5. **Color application**: Symbolic colors in correct positions
6. **Final touches**: Eyes last (they bring presence)
7. **Inscription**: Greek letters identify the saint/scene
8. **Blessing**: Icon must be blessed before use

### Futurist Dynamic Composition Process

1. **Subject selection**: What embodies modern speed, machine, urban energy?
2. **Motion analysis**: What is the trajectory? How does force move?
3. **Fragmentation planning**: At what intervals to show subject?
4. **Lines of force**: What radiating lines convey thrust and impact?
5. **Color vibration**: What complementary pairs create optical energy?
6. **Diagonal dominance**: How to eliminate stable horizontals/verticals?
7. **Viewer immersion**: Does this surround and carry the spectator away?

---

## VIDEO AI PROMPTING INTEGRATION

When generating prompts for video AI (Sora, Veo, Runway), the dimensional framework adds temporal precision:

### Temporal Mode to Video Translation

| Temporal Mode | Video Implementation |
|---------------|---------------------|
| `frozen_ideal` | Minimal motion; single held pose; slow subtle breathing |
| `eternal_present` | Slow motion; no beginning/end implied; loop-friendly |
| `dynamic_sequence` | High motion; blur; subject crosses frame; 2-3 second shots |
| `dreamtime_perpetual` | Dissolves; multiple subjects coexisting; non-linear cuts |
| `impermanence_trace` | Time-lapse elements; decay/growth; weather changes |

### Camera Movement by Tradition

| Tradition | Natural Camera Movement |
|-----------|------------------------|
| Byzantine | Static; no camera movement; icon does not move |
| Renaissance | Slow dolly in; viewer entering window onto world |
| Futurism | Rapid tracking; handheld shake; whip pans |
| Japanese Ma | Extremely slow; long static holds; minimal movement |
| Aboriginal | Aerial drone; slow reveal of country from above |

### Dimensional Prompts for Video

**Example: Wabi-sabi temporal mode in video**
> "A ceramic bowl sits on weathered wood. Minimal motion. Steam rises slowly from tea inside, the only movement. Light changes almost imperceptibly as if hours pass in seconds—time-lapse but nearly still. The bowl shows its age; a single crack catches changing light. Camera: static, locked off. Duration: 8 seconds that feel like an hour. No sound except ambient room tone."

---

## CROSS-CULTURAL SYNTHESIS PATTERNS

### Pattern 1: East-West Spatial Hybrid
Combine **atmospheric_dissolve** (Chinese) with **linear_perspective** (Renaissance):
- Use linear perspective for architectural elements
- Apply atmospheric dissolving to distant natural elements
- Result: Buildings have geometric clarity; mountains fade into mist

### Pattern 2: Sacred Structure with Modern Content
Combine **Byzantine structure** with **Contemporary subject**:
- Reverse perspective opening toward viewer
- Hieratic frontal positioning
- Gold background
- But subject is modern: tech worker, activist, scientist
- Creates: Contemporary icons, modern saints

### Pattern 3: Indigenous + Minimalist
Combine **Aboriginal aerial** with **Japanese Ma**:
- Aerial/diagrammatic country view
- Symbols floating in vast empty space
- No horror vacui density
- Creates: Sparse, breathing maps of eternal relationship to land

### Pattern 4: Motion + Stillness
Combine **Futurist fragmentation** with **Yoruba itutu**:
- Body in dynamic motion blur
- Face remains utterly composed
- Creates: Visual koan—absolute peace within absolute motion
