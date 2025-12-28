---
name: visual-art-composition
description: Orthogonal framework for generating image prompts using 13 independently combinable aesthetic dimensions from 29+ cultural and theoretical art traditions
---

# Visual Art Composition System

## Overview

The Visual Art Composition System transforms "describe what you want to see" into structured, orthogonal aesthetic frameworks that combine multiple cultural art traditions in novel ways. Rather than treating art styles as monolithic presets ("make it look Japanese"), this system decomposes 29+ art traditions into 13 independently variable dimensions - each representing a distinct cognitive question that artists ask when creating work.

This approach enables unprecedented creative combinations: Byzantine spatial logic with Futurist motion, Yoruba emotional composure with Expressionist color, Japanese negative space with Islamic geometric patterns. The framework is built on the insight that art traditions are decision-making systems, not just visual styles. When you understand the questions each tradition asks (Where does form sit in space? How does color express emotion? What is deliberately absent?), you can recombine these cognitive frameworks to generate genuinely novel aesthetic experiences.

The system works by providing 13 orthogonal dimensions (spatial representation, color philosophy, emotional register, value structure, completion philosophy, etc.) with 4-8 values per dimension drawn from specific art traditions. Because dimensions are independent, any value from one dimension can combine with any value from another - creating thousands of possible aesthetic combinations. The system includes validation rules to prevent mutually exclusive combinations and resolution strategies for productive tensions that generate creative innovation.

## When to Use

**Use When**:
- Generating image prompts for AI image/video generation (Midjourney, DALL-E, Sora, Runway, Veo)
- Creating art direction briefs that specify precise aesthetic intent beyond "style references"
- Exploring cross-cultural aesthetic synthesis (e.g., Byzantine structure meets modern content)
- Designing visual systems with intentional productive tensions (motion within stillness, perfect forms with noble imperfection)
- Articulating why certain visual approaches feel derivative and seeking genuine novelty

**Do Not Use**:
- When simple style references suffice ("make it look like Monet")
- For technical specifications without aesthetic intent (color values, aspect ratios, file formats)
- When client/stakeholder cannot engage with conceptual frameworks (needs concrete mockups instead)

## Core Principles

### Principle 1: Orthogonal Dimensions Enable Novel Combinations

Each of the 13 dimensions represents an independent cognitive question. Changing one dimension does not require changing others. This independence means you can combine Byzantine reverse perspective with Futurist motion fragmentation, or Japanese ma emptiness with Victorian horror vacui (if you resolve the productive tension).

Orthogonality eliminates the constraint of historical coherence - you are not bound to "styles" as packages. Instead, you select decision-making frameworks from different traditions and layer them. A composition can ask the spatial question like a Renaissance artist, the color question like a Chinese painter, and the emotional question like a Yoruba sculptor.

In practice:
- Select values across dimensions without worrying about historical compatibility
- Combine opposing values deliberately to create productive tensions
- Validate only for logical contradictions (mutually exclusive pairs), not historical accuracy
- Use cross-cultural synthesis as the default, not the exception

### Principle 2: Cognitive Questions Over Visual Styles

Each art tradition embodies a set of cognitive questions artists ask while creating. Byzantine iconography asks "How does sacred space reach toward the viewer?" (reverse perspective). Chinese painting asks "Does this have spirit resonance?" (qi yun). Yoruba sculpture asks "Does this embody cool composure?" (itutu).

When you understand the question, you can apply the decision-making framework to any subject matter. Byzantine reverse perspective can structure a photograph of a programmer at work. Yoruba itutu can guide the emotional register of a sci-fi character. Chinese qi yun can validate whether a modern abstract composition feels alive.

In practice:
- Learn what each tradition asks, not just what it looks like
- Apply decision-making frameworks to unexpected content (Byzantine icons of tech workers)
- Use the cognitive sequence from one tradition to validate work structured by another
- Understand that "style" is outcome, not input - frameworks generate aesthetics

### Principle 3: Productive Tension Creates Innovation

Some dimensional combinations are mutually exclusive (you cannot have both linear perspective and reverse perspective simultaneously). But many apparent conflicts generate productive tensions that drive creative innovation. Horror vacui (fill every surface) combined with ma (negative space as presence) seems contradictory - until you resolve it through zone segregation (dense focal area surrounded by breathing space) or gradient transitions (density increases toward center, dissolves toward edges).

These tensions force novel solutions. Perfect ideal + noble imperfection becomes kintsugi (ideal form with visible repair as feature). Dynamic motion + serene stillness becomes the eye of the storm (motion in periphery, stillness at center). The creative value lies in the resolution strategy, not in avoiding conflict.

In practice:
- Identify one productive tension per composition (prevents chaos)
- Use resolution strategies: zone segregation, gradient transition, nested frames, temporal reading
- Document the tension and resolution in the prompt ("Productive tension: X vs Y, resolved through Z")
- Embrace conflict as creative fuel, not a mistake to eliminate

## Workflow

### Phase 1: Intent Capture

**What does the user want to create?**

Ask three questions:
1. **Subject & Setting**: What is depicted? (person, landscape, object, scene)
2. **Emotional Core**: What should the viewer FEEL? (calm, tense, awed, composed, melancholic, energetic)
3. **Novelty Requirement**: Should this feel familiar (within one tradition) or genuinely novel (cross-cultural synthesis)?

Extract explicit requirements (stated) and implicit requirements (inferred from domain, context, use case).

**Output**: Understood intent with emotional target and novelty level.

### Phase 2: Dimensional Selection

**Select values for the 13 dimensions.**

Start with emotional core - this determines 3-4 anchor dimensions:
- **For CALM**: ma_emptiness + deliberate_incomplete + wabi_melancholy
- **For TENSE**: horror_vacui + emotional_distortion + tenebrism_extreme
- **For ENERGETIC**: motion_fragmented + dynamic_sequence + high_key_luminous
- **For AWE**: linear_perspective (vast) + sublime_awe + hierarchical_importance
- **For COMPOSED**: itutu_cool + polished_complete + serene_detachment

Then fill remaining dimensions based on subject, setting, and desired traditions.

**Key Rule**: Select 5-8 dimensions minimum. Underdetermined compositions lack structure.

**Output**: Dimensional value assignments across 13 dimensions (can leave some unspecified if not critical to intent).

### Phase 3: Combination Validation

**Check for mutually exclusive pairs.**

Review selected dimensions against exclusion rules:
- **Spatial**: Cannot combine linear_perspective with reverse_perspective simultaneously
- **Space Philosophy**: Horror vacui vs ma requires resolution strategy
- **Idealization**: Perfect ideal vs noble imperfection requires resolution strategy
- **Temporal**: Frozen ideal vs dynamic sequence requires resolution strategy
- **Viewer Relationship**: Enveloping immersion vs contemplative distance requires resolution strategy

If mutually exclusive pair detected without resolution:
1. Choose which value is more important to intent
2. Replace conflicting value
3. OR define productive tension + resolution strategy

**Output**: Validated dimensional combination with tensions identified and resolution strategies defined.

### Phase 4: Prompt Generation

**Generate the structured prompt with all specifications.**

Use this template:

```
[SUBJECT] in/at [SETTING], rendered with [TRADITION 1] [SPECIFIC TECHNIQUE]
combined with [TRADITION 2] [SPECIFIC TECHNIQUE].

SPATIAL REPRESENTATION: [dimension value] - [how it manifests in this composition]
COLOR PHILOSOPHY: [dimension value] - [specific palette and saturation strategy]
EMOTIONAL REGISTER: [dimension value] - [how emotion manifests in form/expression]
VALUE STRUCTURE: [dimension value] - [specific light/dark distribution]
[Additional dimensions as selected...]

Productive tension: [DIMENSION A vs DIMENSION B] resolved through [RESOLUTION STRATEGY].

Deliberate absences: [WHAT IS EXCLUDED - derived from selected traditions].

Technical specifications: [Aspect ratio, camera angle, lighting setup if relevant].
```

Include specific implementation details:
- Not "Byzantine style" but "reverse perspective with buildings widening toward viewer, gold background for divine realm"
- Not "Japanese aesthetic" but "ma emptiness with 70% negative space, notan two-value structure, deliberate incomplete edges"
- Not "emotional" but "qi yun resonance - brushwork feels alive, forms breathe, energy moves through composition"

**Output**: Complete structured prompt ready for AI image generation or art direction brief.

## Dimensional Taxonomy

### 1. SPATIAL_REPRESENTATION
**Question**: How does form sit in space?

| Value | Tradition | Cognitive Question | Keywords |
|-------|-----------|-------------------|----------|
| `linear_perspective` | Renaissance (Brunelleschi 1415) | Where is the vanishing point? | "one-point perspective", "vanishing point visible", "orthogonals converging", "mathematically correct depth" |
| `reverse_perspective` | Byzantine (4th-15th c.) | How does sacred space open toward viewer? | "Byzantine perspective", "inverted depth", "space opens toward viewer", "buildings widen as they approach" |
| `aspective_composite` | Ancient Egypt (3000+ BCE) | What is each part's most characteristic view? | "Egyptian composite view", "aspective rendering", "head profile eye frontal", "most recognizable angle per part" |
| `motion_fragmented` | Futurism (1909-1918) | How does the subject move through time? | "chronophotographic", "multiple exposure effect", "Boccioni fragmentation", "lines of force" |
| `atmospheric_dissolve` | Chinese landscape | How does distance become emptiness? | "atmospheric perspective", "mountains fade to mist", "distance dissolves into void" |
| `aerial_map` | Aboriginal dreamtime | How does land sit from sky-view? | "aerial perspective", "diagrammatic country", "top-down sacred geography" |
| `cubist_multiplied` | Cubism (1907-1920s) | How to show multiple viewpoints simultaneously? | "fractured planes", "multiple viewpoints", "Picasso fragmentation", "simultaneity" |

### 2. COLOR_PHILOSOPHY
**Question**: How does color create meaning and emotion?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `emotion_first_ti` | Chinese (ti) | What should viewer FEEL? Map saturation/brightness to emotion, choose hue LAST | Calm = low saturation + high brightness; Tense = high saturation + low brightness |
| `relativistic_context` | Albers (Interaction of Color) | How does surrounding color shift perception? | Same color looks different on different grounds; use context to make colors vibrate |
| `symbolic_coded` | Wu Xing, Byzantine | What does color MEAN beyond appearance? | Blue-green = wood/spring/growth; Gold = divine light; Red = fire/passion/divine blood |
| `naturalistic_optical` | Impressionism | What color is light at this moment? | Capture optical truth; shadows are colored not black; atmospheric effects |
| `emotional_expressive` | Fauvism, Expressionism | What color expresses inner state? | Blue horse if anguish demands it; free from descriptive accuracy |

### 3. EMOTIONAL_REGISTER
**Question**: What should the viewer feel? How is emotion embodied?

| Value | Tradition | Visual Markers | Keywords |
|-------|-----------|---------------|----------|
| `itutu_cool` | Yoruba | Face serene, impassive, gentle; large almond eyes, calm gaze; slight smile or neutral; smooth polished surface; power contained within cool exterior | "mystic composure", "noble tranquility", "Yoruba coolness", "calm containing power" |
| `qi_yun_resonance` | Chinese Six Principles | Brushwork feels alive not mechanical; forms breathe; energy moves through composition; spirit captured not just appearance | "spirit resonance", "vital energy", "living brushwork", "qi animating form" |
| `sublime_awe` | Romanticism (Burke, Kant) | Vast scale dwarfing humans; dramatic natural forces; light suggesting transcendence or terror; viewer humbled by immensity | "Caspar David Friedrich scale", "terrifying beauty", "nature's power dwarfing humanity", "transcendent vastness" |
| `passionate_expression` | Expressionism | Distorted forms expressing anguish; aggressive brushwork; colors chosen for emotional impact; visible process | "Kirchner angularity", "Munch anguish", "emotional distortion", "expressive deformation" |
| `serene_detachment` | Byzantine, Classical | Calm, eternal, removed from earthly emotion; hieratic stillness; no momentary expression | "hieratic serenity", "eternal calm", "detached transcendence" |
| `wabi_melancholy` | Japanese wabi-sabi | Quiet contemplation; gentle sadness; beauty in transience and imperfection | "seijaku stillness", "mono no aware", "gentle melancholy" |

### 4. SPACE_PHILOSOPHY
**Question**: How is emptiness treated?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `ma_emptiness` | Japanese ma | Is emptiness doing work? Where is breathing room? | Negative space as presence; 40-70% empty; silence between notes |
| `horror_vacui` | Victorian, Islamic, Medieval | Can every surface be patterned? | No empty space; ornament fills all; dense visual texture |
| `infinite_extension` | Islamic geometric | Does pattern continue beyond frame? | Tessellation implies infinity; no center no edge; could tile forever |
| `focal_hierarchy` | Renaissance, Academic | What is most important? Where does eye rest? | Clear focal point; supporting elements diminish; directed gaze path |

### 5. VALUE_STRUCTURE
**Question**: How do light and dark organize the composition?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `notan_two_value` | Japanese notan (via Arthur Wesley Dow) | Does it hold in pure black and white? | Reduce to two values; shape interlock; balance dark and light |
| `chiaroscuro_gradated` | Renaissance (Leonardo) | How does light model form? | Continuous gradation; single light source; spherical modeling |
| `tenebrism_extreme` | Baroque (Caravaggio) | What emerges from darkness? | Most of canvas near-black; spotlight effect; dramatic emergence |
| `flat_unmodeled` | Byzantine, Japanese ukiyo-e | Can form exist without shadow? | No light source; even illumination; pure color areas |
| `high_key_luminous` | Impressionism, some Expressionism | Can everything glow with light? | Minimal darks; radiant brightness; vibrating luminosity |

### 6. IDEALIZATION
**Question**: How does depiction relate to observed reality?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `truth_to_nature` | Realism, Courbet | What is actually there, unidealized? | Document reality; no beautification; social truth |
| `perfect_ideal` | Classical Greece, Academic | What is the eternal perfect form? | Based on mathematical proportion; flawless anatomy; platonic ideal |
| `hieratic_stylization` | Byzantine, Egyptian | What is the timeless sacred form? | Follow prototype; elongated proportions; frontal presentation; not naturalistic |
| `emotional_distortion` | Expressionism | How does form express inner state? | Warp proportions to match feeling; elongate for anguish; angular for anxiety |
| `noble_imperfection` | Wabi-sabi, Yoruba | Where is the authentic flaw that proves humanity? | Controlled irregularity; fukinsei asymmetry; kintsugi visible repair |

### 7. COMPLETION_PHILOSOPHY
**Question**: When is the work finished?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `polished_complete` | Academic, Byzantine | Is every inch resolved to highest craft? | No visible brushwork; smooth surface; total finish |
| `deliberate_incomplete` | Wabi-sabi, Chinese literati | What can remain unfinished? | Edges fade; suggestions not statements; kanso simplicity |
| `generative_unfinished` | Yoruba, Aboriginal | Does this have potential to grow? | Work invites continuation; not sealed; agency to evolve |
| `process_visible` | Expressionism, some Contemporary | Can the act of making show through? | Aggressive marks; drips; pentimenti; energy of creation visible |

### 8. TEMPORAL_MODE
**Question**: How does the work relate to time?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `frozen_ideal` | Classical sculpture, Academic | What is the eternal perfection outside time? | Single moment held forever; no before or after implied |
| `eternal_present` | Byzantine, some Aboriginal | Is this always and forever? | Timeless sacred now; no historical moment |
| `dynamic_sequence` | Futurism | How does motion unfold across instants? | Multiple temporal positions; blur and repetition; trajectory |
| `dreamtime_perpetual` | Aboriginal | How is all time coexisting? | Past present future simultaneous; creation ongoing |
| `impermanence_trace` | Wabi-sabi, memento mori | How does time leave marks? | Patina; decay; koko austerity; signs of age and use |

### 9. VIEWER_RELATIONSHIP
**Question**: What is the viewer's position relative to the work?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `contemplative_distance` | Renaissance window, literati | Am I looking through a window at the world? | Viewer separate; observing; intellectual engagement |
| `enveloping_immersion` | Futurism, some Baroque | Am I caught inside the experience? | Viewer surrounded; no stable outside position; sensory assault |
| `communion_presence` | Byzantine icon | Is the divine looking back at me? | Frontal gaze; reverse perspective opening out; sacred meeting viewer |
| `participatory_activation` | Conceptual, some Contemporary | Do I complete the work by thinking? | Viewer's intellect finishes; document not object; mental completion |

### 10. MEANING_LOCATION
**Question**: Where does meaning reside?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `narrative_depicted` | Academic history painting | What story is shown? | Clear readable narrative; moment of dramatic action |
| `symbolic_encoded` | Byzantine, Wu Xing, Medieval | What do elements stand for? | Colors, objects, positions encode specific meanings |
| `formal_relationships` | Formalism, some Modernism | What are the visual relationships themselves? | Line, color, shape as primary content; no outside reference |
| `conceptual_proposition` | Conceptual art | What is the idea? | Idea is the art; object secondary; intellectual engagement |
| `form_has_agency` | Yoruba, Aboriginal | What does this DO? | Art has efficacy; protects, heals, connects; function not just meaning |

### 11. COMPOSITIONAL_STRUCTURE
**Question**: How are elements organized?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `golden_proportion` | Renaissance, Classical | What are the mathematical harmonies? | Golden ratio; rule of thirds; Fibonacci spirals |
| `hierarchical_importance` | Byzantine, Medieval | Who/what is most important? Scale by significance not optical accuracy | Larger = more important; Christ bigger than apostles; king towers over subjects |
| `equal_treatment` | Realism, some contemporary | Is everything given same visual weight? | Democratic attention; no heroic focus; banal and grand equally present |
| `dynamic_diagonals` | Baroque, Futurism | How to eliminate stability? | Diagonal thrust; no horizontal/vertical calm; motion and energy |
| `radial_mandala` | Tibetan, some Islamic | How to show cosmos from center? | Radial symmetry; center as origin; emanation outward |

### 12. SURFACE_TREATMENT
**Question**: How is the physical surface handled?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `invisible_hand` | Academic, trompe l'oeil | Can I make the paint disappear? | No visible brushwork; illusionistic smoothness |
| `calligraphic_gesture` | Chinese, Japanese, Abstract Expressionism | Is the brushstroke itself expressive? | Visible energetic marks; speed and pressure visible; gu fa bone method |
| `textural_material` | Impasto, collage, assemblage | What is the physical presence of material? | Thick paint; material added; sculptural surface |
| `flat_graphic` | Ukiyo-e, some Modernism | Can it read as pure design? | No illusion of depth in surface; graphic clarity; posterization |

### 13. CULTURAL_PURPOSE
**Question**: What is this for?

| Value | Tradition | Cognitive Question | Implementation |
|-------|-----------|-------------------|----------------|
| `devotional_sacred` | Byzantine, Tibetan, Islamic | Does this aid prayer and bring viewer closer to divine? | Follows sacred prototypes; blessed; efficacious |
| `moral_instruction` | Academic history painting | What virtue is taught? | Heroism, sacrifice, piety, duty; clear didactic message |
| `social_political` | Realism, Social Realism, some Documentary | What truth is revealed about society? | Document injustice; reveal conditions; political consciousness |
| `aesthetic_contemplation` | Formalism, some Modernism | Is this for pure visual experience? | Art for art's sake; no outside function; beauty as sufficient |
| `personal_expression` | Romanticism, Expressionism | What is my inner experience? | Individual vision; subjective truth; emotional autobiography |

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Style-Only Prompting** | "Make it look Japanese" collapses multiple dimensions into vague aesthetic reference, misses cognitive framework, produces generic pastiche | Use 3-5 specific dimension values: ma_emptiness + deliberate_incomplete + notan_two_value + wabi_melancholy. Include cognitive questions: "Does this have breathing room? Where is the empty space doing work?" |
| **Ignoring Combination Rules** | Selecting linear_perspective + reverse_perspective creates logical impossibility; horror_vacui + ma without resolution creates incoherent chaos | Check mutually exclusive pairs before generating. If tension exists, define resolution strategy: "Horror vacui fills center; ma breathing space at margins" |
| **Skipping Emotional Intent** | Specifying technical dimensions (perspective, color palette) without emotional register feels hollow and aimless; viewer doesn't know what to feel | Always specify emotional_register dimension first: itutu_cool, qi_yun_resonance, sublime_awe, etc. Let emotion drive other dimensional choices |
| **Underdetermined Specifications** | Selecting only 1-2 dimensions leaves too many degrees of freedom; AI fills gaps with generic defaults | Specify minimum 5-8 dimensions. If dimension isn't critical to intent, choose value that supports emotional core or creates productive tension |
| **Historical Accuracy Obsession** | Refusing cross-cultural combinations because "Byzantines didn't do that" misses the entire point of orthogonal framework | Historical coherence is NOT the goal. Novel combinations are the goal. Validate logic (no contradictions), not history |
| **Resolution-Free Tensions** | Identifying productive tension (perfect vs imperfect) but not specifying resolution strategy produces ambiguous mess | Always pair tension with resolution: "Perfect ideal + noble imperfection, resolved through kintsugi principle - ideal form with visible repair as feature" |
| **Forgetting Deliberate Absences** | Including elements that selected traditions explicitly reject (naturalistic shadow in Byzantine icon, symmetry in wabi-sabi) | Review what each tradition deliberately excludes. Byzantine ignores optical perspective and natural shadows. Wabi-sabi ignores symmetry and polish. Honor these absences |

## Conclusion

The Visual Art Composition System reframes art styles as cognitive frameworks - sets of questions that artists ask while creating. By decomposing 29+ traditions into 13 orthogonal dimensions, the system enables genuinely novel aesthetic combinations that would be impossible within monolithic "style" thinking.

The power lies in three insights: (1) Dimensions are independent, so any value can combine with any other value, liberating you from historical coherence constraints. (2) Traditions are decision-making systems, not just visual outcomes, so their frameworks apply to any subject matter. (3) Productive tensions drive innovation - apparent contradictions force creative resolutions that generate unique aesthetics.

This system is particularly valuable for AI image generation (where precision matters and vague style references produce generic results), art direction (where stakeholders need clear rationale for aesthetic choices), and creative exploration (where cross-cultural synthesis unlocks novel visual languages). The framework rewards depth - the more you understand what each tradition asks and why, the more sophisticated your combinations become.

## Related Skills

- pptx-generation (uses visual composition framework for slide design)
- prompt-architect (applies prompting optimization to visual prompts)
- gemini-search (research art traditions and historical context)

## MCP Requirements

```yaml
mcp_servers:
  required: []
  optional: [memory-mcp]  # For storing generated prompts, building prompt library over time
```

**Memory Usage Pattern**:
```javascript
// Store generated prompts for reuse and iteration
taggedMemoryStore('visual-art-composition', promptText, {
  dimensions_used: ['ma_emptiness', 'itutu_cool', 'notan_two_value'],
  traditions: ['Japanese', 'Yoruba'],
  emotional_core: 'composed calm',
  subject: 'portrait',
  tensions: ['perfect_vs_imperfect'],
  resolution: 'kintsugi_principle'
});

// Retrieve similar prompts for inspiration
taggedMemoryRetrieve({
  query: 'calm portrait composition',
  filter: { emotional_core: 'composed calm' },
  limit: 5
});
```