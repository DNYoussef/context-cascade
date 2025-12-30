/*============================================================================*/
/* I18N-AUTOMATION SKILL :: VERILINGUA x VERIX EDITION                      */
/*============================================================================*/

---
name: i18n-automation
version: 1.0.0
description: |
  [assert|neutral] Automate internationalization and localization workflows for web applications with translation, key generation, and library setup [ground:given] [conf:0.95] [state:confirmed]
category: delivery
tags:
- i18n
- translation
- localization
- automation
- react
author: ruv
cognitive_frame:
  primary: aspectual
  goal_analysis:
    first_order: "Execute i18n-automation workflow"
    second_order: "Ensure quality and consistency"
    third_order: "Enable systematic delivery processes"
---

/*----------------------------------------------------------------------------*/
/* S0 META-IDENTITY                                                            */
/*----------------------------------------------------------------------------*/

[define|neutral] SKILL := {
  name: "i18n-automation",
  category: "delivery",
  version: "1.0.0",
  layer: L1
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S1 COGNITIVE FRAME                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] COGNITIVE_FRAME := {
  frame: "Aspectual",
  source: "Russian",
  force: "Complete or ongoing?"
} [ground:cognitive-science] [conf:0.92] [state:confirmed]

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

/*----------------------------------------------------------------------------*/
/* S2 TRIGGER CONDITIONS                                                       */
/*----------------------------------------------------------------------------*/

[define|neutral] TRIGGER_POSITIVE := {
  keywords: ["i18n-automation", "delivery", "workflow"],
  context: "user needs i18n-automation capability"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S3 CORE CONTENT                                                             */
/*----------------------------------------------------------------------------*/

# i18n Automation

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.




## When to Use This Skill

- **Multi-Language Support**: Building apps for international markets
- **Translation Workflows**: Automating translation key extraction and management
- **Localization**: Adapting content for regional formats (dates, currencies, numbers)
- **RTL Support**: Implementing right-to-left languages (Arabic, Hebrew)
- **Pluralization**: Handling complex plural rules across languages
- **Dynamic Content**: Translating user-generated or CMS content

## When NOT to Use This Skill

- **Single-Language Apps**: English-only applications with no internationalization plans
- **Static Content**: Hardcoded strings that will not change
- **Non-Web Projects**: Embedded systems or native apps with platform-specific i18n
- **Third-Party Managed**: Apps using fully-managed translation services (Lokalise, Phrase)

## Success Criteria

- [ ] All user-facing strings externalized to translation files
- [ ] Translation keys organized by feature/namespace
- [ ] Pluralization rules implemented correctly
- [ ] Date/time/currency formatting respects locale
- [ ] RTL layouts functional (if applicable)
- [ ] Language switching works without reload
- [ ] Missing translation handling implemented
- [ ] Translation files validated for syntax errors

## Edge Cases to Handle

- **Interpolated Variables**: Preserve placeholders in translations
- **HTML in Translations**: Sanitize translated content safely
- **Nested Keys**: Manage deeply nested translation structures
- **Missing Translations**: Fallback to default language gracefully
- **Dynamic Keys**: Handle runtime-computed translation keys
- **Context-Sensitive**: Same word different meanings (e.g., Post noun vs verb)

## Guardrails

- **NEVER** hardcode user-facing strings in components
- **ALWAYS** use i18n library functions (t(), useTranslation(), etc.)
- **NEVER** assume left-to-right text direction
- **ALWAYS** validate translation file JSON/YAML syntax
- **NEVER** concatenate translated strings (breaks grammar)
- **ALWAYS** provide context for translators (comments in translation files)
- **NEVER** ship with empty or placeholder translations

## Evidence-Based Validation

- [ ] Run i18n linter to detect untranslated strings
- [ ] Test app in all supported locales
- [ ] Validate translation files with JSON Schema
- [ ] Check RTL layout in browser DevTools
- [ ] Test pluralization with boundary values (0, 1, 2, 5, 100)
- [ ] Verify date/number formatting with Intl API
- [ ] Review translations with native speakers

## Purpose
Automate complete internationalization workflows including translation, key-value generation, library installation, and locale configuration for web applications.

## Specialist Agent

I am an internationalization specialist with expertise in:
- i18n library selection and configuration (react-i18n, next-intl, i18next)
- Translation key architecture and organization
- Locale file formats (JSON, YAML, PO, XLIFF)
- RTL (Right-to-Left) language support
- SEO and metadata localization
- Dynamic content translation strategies

### Methodology (Plan-and-Solve Pattern)

1. **Analyze Project**: Detect framework, existing i18n setup, content to translate
2. **Design i18n Architecture**: Choose library, key structure, file organization
3. **Extract Content**: Identify all translatable strings and create keys
4. **Generate Translations**: Create locale files with translations
5. **Configure Integration**: Set up routing, language detection, switcher component
6. **Validate**: Test all locales, check RTL, verify SEO metadata

### Framework Support

**Next.js (Recommended: next-intl)**:
```javascript
// Installation
npm install next-intl

// Configuration: next.config.js
const createNextIntlPlugin = require('next-intl/plugin');
const withNextIntl = createNextIntlPlugin();

module.exports = withNextIntl({
  i18n: {
    locales: ['en', 'ja', 'es', 'fr'],
    defaultLocale: '

/*----------------------------------------------------------------------------*/
/* S4 SUCCESS CRITERIA                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] SUCCESS_CRITERIA := {
  primary: "Skill execution completes successfully",
  quality: "Output meets quality thresholds",
  verification: "Results validated against requirements"
} [ground:given] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S5 MCP INTEGRATION                                                          */
/*----------------------------------------------------------------------------*/

[define|neutral] MCP_INTEGRATION := {
  memory_mcp: "Store execution results and patterns",
  tools: ["mcp__memory-mcp__memory_store", "mcp__memory-mcp__vector_search"]
} [ground:witnessed:mcp-config] [conf:0.95] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S6 MEMORY NAMESPACE                                                         */
/*----------------------------------------------------------------------------*/

[define|neutral] MEMORY_NAMESPACE := {
  pattern: "skills/delivery/i18n-automation/{project}/{timestamp}",
  store: ["executions", "decisions", "patterns"],
  retrieve: ["similar_tasks", "proven_patterns"]
} [ground:system-policy] [conf:1.0] [state:confirmed]

[define|neutral] MEMORY_TAGGING := {
  WHO: "i18n-automation-{session_id}",
  WHEN: "ISO8601_timestamp",
  PROJECT: "{project_name}",
  WHY: "skill-execution"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S7 SKILL COMPLETION VERIFICATION                                            */
/*----------------------------------------------------------------------------*/

[direct|emphatic] COMPLETION_CHECKLIST := {
  agent_spawning: "Spawn agents via Task()",
  registry_validation: "Use registry agents only",
  todowrite_called: "Track progress with TodoWrite",
  work_delegation: "Delegate to specialized agents"
} [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* S8 ABSOLUTE RULES                                                           */
/*----------------------------------------------------------------------------*/

[direct|emphatic] RULE_NO_UNICODE := forall(output): NOT(unicode_outside_ascii) [ground:windows-compatibility] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_EVIDENCE := forall(claim): has(ground) AND has(confidence) [ground:verix-spec] [conf:1.0] [state:confirmed]

[direct|emphatic] RULE_REGISTRY := forall(agent): agent IN AGENT_REGISTRY [ground:system-policy] [conf:1.0] [state:confirmed]

/*----------------------------------------------------------------------------*/
/* PROMISE                                                                     */
/*----------------------------------------------------------------------------*/

[commit|confident] <promise>I18N_AUTOMATION_VERILINGUA_VERIX_COMPLIANT</promise> [ground:self-validation] [conf:0.99] [state:confirmed]
