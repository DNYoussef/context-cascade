---
name: visual-art-composition
description: Orthogonal framework for generating image prompts using 13 independently combinable aesthetic dimensions from 29+ cultural and theoretical art traditions. Decomposes art styles into cognitive frameworks (decision-making questions) enabling novel cross-cultural synthesis. Transforms vague style references into structured prompts with productive tensions and deliberate absences. Ideal for AI image generation, art direction, and creative exploration requiring precision beyond generic style copying.
category: specialists
version: 2.0.0
triggers:
  - "art prompt"
  - "image generation"
  - "visual composition"
  - "aesthetic framework"
  - "generate art"
  - "combine art styles"
mcp_servers:
  required: []
  optional: [memory-mcp]
---

# Visual Art Composition System

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.



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

## Phase 0: Expertise Loading

**Load domain knowledge before prompt generation.**

**Check for existing expertise:**
```javascript
// Check if art tradition expertise exists
const domains = detectArtTraditions(userRequest);
// Examples: "byzantine", "yoruba", "futurism", "wabi-sabi"

for (const domain of domains) {
  const expertisePath = `.claude/expertise/art-traditions/${domain}.yaml`;
  if (fileExists(expertisePath)) {
    expertise[domain] = loadExpertise(expertisePath);
    console.log(`Loaded expertise: ${domain}`);
  }
}
```

**What to extract from expertise:**
- **Cognitive Questions**: What does this tradition ask? (e.g., "How does sacred space reach toward viewer?")
- **Visual Markers**: How to recognize it? (reverse perspective, gold backgrounds, frontal gaze)
- **Deliberate Absences**: What does it exclude? (naturalistic shadow, optical perspective, emotion)
- **Productive Pairings**: What combinations work well? (Byzantine + modern content, Yoruba + minimalism)
- **Known Conflicts**: What to avoid? (reverse perspective + linear perspective = impossible)

**If expertise missing:**
- Proceed with general knowledge from dimensional taxonomy
- Flag for expertise creation after successful prompt generation



---
*Promise: `<promise>SKILL_V2_VERIX_COMPLIANT</promise>`*
