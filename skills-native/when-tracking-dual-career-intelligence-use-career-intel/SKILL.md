---
name: when-tracking-dual-career-intelligence-use-career-intel
description: Automated tracking of internal/external roles across US/EU markets with policy monitoring, visa leverage analysis, and tailored pitch generation.
---

# Dual-Track Career Intelligence

Automated tracking of internal/external roles across US/EU markets with policy monitoring, visa leverage analysis, and tailored pitch generation.

## Overview

This skill orchestrates 3 specialist agents to:
1. **Scout** (researcher) - Crawl job boards and normalize opportunities
2. **RegWatch** (researcher) - Diff EU policy/regulatory pages for visa changes
3. **Ranker** (analyst) - Score opportunities by Fit, Option Value, Speed, Cred Stack
4. **PitchPrep** (coder) - Generate tailored bullets, Q&A, and anecdotes

**Critical differentiator**: Tracks visa leverage and immigration policy changes alongside traditional job factors.

## When to Use

- **Weekly/bi-weekly**: Systematic career opportunity scanning
- **Before major applications**: Generate tailored pitch materials
- **EU policy changes**: Understand immigration implications
- **Strategic planning**: Maintain optionality across geographies

## Assigned Agents

### Primary Agents

**researcher (Scout role)** - Phase 1: Web scraping, data normalization, source aggregation
- Expertise: API integration, data extraction, YAML processing
- Tools: curl, jq, yq, bash scripting
- Output: Raw CSV of opportunities with metadata

**researcher (RegWatch role)** - Phase 2: Policy diff analysis, regulatory monitoring
- Expertise: Document comparison, policy interpretation, change detection
- Tools: diff, git, web scraping
- Output: Policy change summary with action items

### Secondary Agents

**analyst (Ranker role)** - Phase 3: Multi-factor scoring, EV calculation
- Expertise: Scoring algorithms, decision analysis, prioritization
- Tools: Python/Node scoring scripts, statistical analysis
- Output: Ranked opportunities with justifications

**coder (PitchPrep role)** - Phase 4: Content generation, tailoring, formatting
- Expertise: Natural language generation, resume optimization, storytelling
- Tools: Template engines, GPT-assisted writing, markdown formatting
- Output: Tailored cover letters, Q&A prep, cred stack mapping

## Coordination Pattern

```
SKILL: dual-track-career-intelligence
  ↓
hierarchical-coordinator spawns 4 sequential phases
  ↓
Phase 1: Scout (researcher) → raw data
Phase 2: RegWatch (researcher) → policy deltas
Phase 3: Ranker (analyst) → scored opportunities
Phase 4: PitchPrep (coder) → tailored materials
  ↓
All phases coordinate via Memory MCP with WHO/WHEN/PROJECT/WHY tagging
```

## Phase 2: RegWatch (Policy Monitoring)

**Agent**: `researcher` (RegWatch role)

### Inputs
- `data/sources/biotech_watch.yml` - EU policy/regulatory URLs
- Previous week's policy snapshot (from memory)

### Commands Executed

```bash
#!/bin/bash
# Phase 2: EU Policy Change Detection

# PRE-TASK HOOK
npx claude-flow@alpha hooks pre-task \
  --description "Career intel: EU policy monitoring" \
  --agent "researcher" \
  --role "RegWatch" \
  --skill "dual-track-career-intelligence"

# SETUP
WEEK=$(date +%Y-%W)
mkdir -p raw_data/policy_snapshots

# READ POLICY SOURCES
POLICY_URLS=$(yq eval '.policy_sources[].url' data/sources/biotech_watch.yml)

# FETCH CURRENT SNAPSHOTS
for URL in $POLICY_URLS; do
  SOURCE_NAME=$(echo $URL | sed 's/[^a-zA-Z0-9]/_/g')

  echo "[RegWatch] Fetching: $URL"
  curl -s "$URL" > "raw_data/policy_snapshots/${SOURCE_NAME}_${WEEK}.html"
done

# RETRIEVE LAST WEEK'S SNAPSHOTS
LAST_WEEK=$(date -d '7 days ago' +%Y-%W)
PREV_SNAPSHOTS=$(npx claude-flow@alpha memory retrieve \
  --key "life-os/career/policy-changes/${LAST_WEEK}/snapshots" \
  2>/dev/null || echo "")

# DIFF DETECTION
echo "# EU Policy Changes - Week $WEEK" > outputs/reports/policy_changes_${WEEK}.md
echo "" >> outputs/reports/policy_changes_${WEEK}.md
echo "## Summary" >> outputs/reports/policy_changes_${WEEK}.md
echo "" >> outputs/reports/policy_changes_${WEEK}.md

CHANGES_DETECTED=0

for SNAPSHOT in raw_data/policy_snapshots/*_${WEEK}.html; do
  BASENAME=$(basename "$SNAPSHOT" _${WEEK}.html)
  PREV_SNAPSHOT="raw_data/policy_snapshots/${BASENAME}_${LAST_WEEK}.html"

  if [[ -f "$PREV_SNAPSHOT" ]]; then
    DIFF_OUTPUT=$(diff -u "$PREV_SNAPSHOT" "$SNAPSHOT" | grep -E '^\+|^-' | grep -v '^+++\|^---')

    if [[ -n "$DIFF_OUTPUT" ]]; then
      CHANGES_DETECTED=$((CHANGES_DETECTED + 1))

      echo "### ${BASENAME}" >> outputs/reports/policy_changes_${WEEK}.md
      echo "" >> outputs/reports/policy_changes_${WEEK}.md
      echo "**Changes detected**: Yes" >> outputs/reports/policy_changes_${WEEK}.md
      echo "" >> outputs/reports/policy_changes_${WEEK}.md
      echo "\`\`\`diff" >> outputs/reports/policy_changes_${WEEK}.md
      echo "$DIFF_OUTPUT" | head -n 20 >> outputs/reports/policy_changes_${WEEK}.md
      echo "\`\`\`" >> outputs/reports/policy_changes_${WEEK}.md
      echo "" >> outputs/reports/policy_changes_${WEEK}.md
      echo "**Action**: Review for visa/immigration impact" >> outputs/reports/policy_changes_${WEEK}.md
      echo "" >> outputs/reports/policy_changes_${WEEK}.md
    fi
  else
    echo "[RegWatch] No baseline for $BASENAME, skipping diff"
  fi
done

echo "[RegWatch] Detected $CHANGES_DETECTED policy changes"

# MEMORY STORE
npx claude-flow@alpha memory store \
  --key "life-os/career/policy-changes/${WEEK}/snapshots" \
  --value "$(ls raw_data/policy_snapshots/*_${WEEK}.html)" \
  --metadata "{
    \"WHO\": {
      \"agent\": \"researcher\",
      \"role\": \"RegWatch\",
      \"capabilities\": [\"policy-monitoring\", \"diff-analysis\", \"regulatory-tracking\"]
    },
    \"WHEN\": {\"iso\": \"$(date -Iseconds)\", \"unix\": $(date +%s)},
    \"PROJECT\": \"life-os-career-tracking\",
    \"WHY\": {
      \"intent\": \"research\",
      \"task_type\": \"policy-change-detection\",
      \"outcome_expected\": \"policy-delta-report\",
      \"phase\": \"regulatory-monitoring\"
    }
  }"

npx claude-flow@alpha memory store \
  --key "life-os/career/policy-changes/${WEEK}/report" \
  --value "$(cat outputs/reports/policy_changes_${WEEK}.md)" \
  --metadata "{\"WHO\": {\"agent\": \"researcher\", \"role\": \"RegWatch\"}, \"WHEN\": {\"iso\": \"$(date -Iseconds)\"}, \"PROJECT\": \"life-os-career-tracking\", \"WHY\": {\"intent\": \"analysis\", \"phase\": \"policy-diffing\"}}"

# POST-TASK HOOK
npx claude-flow@alpha hooks post-task \
  --task-id "career-intel-phase2-regwatch" \
  --metrics "changes_detected=${CHANGES_DETECTED}"

echo "[RegWatch] Phase 2 complete: $CHANGES_DETECTED changes documented"
```

### Outputs
- `outputs/reports/policy_changes_{YYYY-WW}.md` - Policy diff report
- Memory: `life-os/career/policy-changes/{YYYY-WW}/snapshots` + `/report`

## Top 15 Opportunities

| Rank | Title | Company | Location | Fit | Option | Speed | Cred | Total | Action Deadline | Link |
|------|-------|---------|----------|-----|--------|-------|------|-------|-----------------|------|
REPORT_HEADER

jq -r '.[] | [
  (. | keys | map(select(. == "total_score")) | .[0]),
  .title,
  .company,
  .location,
  .fit_score,
  .option_value,
  .speed_score,
  .cred_score,
  .total_score,
  (. | if .speed_score < 50 then "URGENT" else "Normal" end),
  .url
] | @tsv' raw_data/scored_opportunities_${WEEK}.json \
  | awk 'BEGIN{OFS="|"; rank=1} {print rank++, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11}' \
  >> outputs/reports/career_intel_${WEEK}.md

# APPEND POLICY CHANGES SECTION
echo "" >> outputs/reports/career_intel_${WEEK}.md
echo "---" >> outputs/reports/career_intel_${WEEK}.md
echo "" >> outputs/reports/career_intel_${WEEK}.md
echo "## EU Policy & Regulatory Changes" >> outputs/reports/career_intel_${WEEK}.md
echo "" >> outputs/reports/career_intel_${WEEK}.md

if [[ -f outputs/reports/policy_changes_${WEEK}.md ]]; then
  tail -n +5 outputs/reports/policy_changes_${WEEK}.md >> outputs/reports/career_intel_${WEEK}.md
else
  echo "*No policy changes detected this week*" >> outputs/reports/career_intel_${WEEK}.md
fi

# APPEND FAST PLAYS SECTION
echo "" >> outputs/reports/career_intel_${WEEK}.md
echo "---" >> outputs/reports/career_intel_${WEEK}.md
echo "" >> outputs/reports/career_intel_${WEEK}.md
echo "## 3 Fast Plays (This Week)" >> outputs/reports/career_intel_${WEEK}.md
echo "" >> outputs/reports/career_intel_${WEEK}.md

jq -r '.[0:3] | .[] | "1. **\(.title)** at \(.company) - Score: \(.total_score)\n   - **Why**: Fit=\(.fit_score), Visa=\(.option_value), Urgency=\(.speed_score)\n   - **Action**: [Apply](\(.url)) by " + (if .speed_score < 50 then "**THIS WEEK**" else "end of week" end) + "\n"' \
  raw_data/scored_opportunities_${WEEK}.json \
  >> outputs/reports/career_intel_${WEEK}.md

# MEMORY STORE
npx claude-flow@alpha memory store \
  --key "life-os/career/opportunities/${WEEK}/ranked" \
  --value "$(cat raw_data/scored_opportunities_${WEEK}.json)" \
  --metadata "{
    \"WHO\": {\"agent\": \"analyst\", \"role\": \"Ranker\", \"capabilities\": [\"scoring\", \"prioritization\", \"decision-analysis\"]},
    \"WHEN\": {\"iso\": \"$(date -Iseconds)\", \"unix\": $(date +%s)},
    \"PROJECT\": \"life-os-career-tracking\",
    \"WHY\": {\"intent\": \"analysis\", \"task_type\": \"opportunity-ranking\", \"outcome\": \"prioritized-list\", \"phase\": \"scoring\"}
  }"

# POST-TASK HOOK
npx claude-flow@alpha hooks post-task \
  --task-id "career-intel-phase3-ranker" \
  --metrics "opportunities_ranked=${TOP_COUNT}"

echo "[Ranker] Phase 3 complete: Top $TOP_COUNT opportunities ranked"
```

### Outputs
- `outputs/reports/career_intel_{YYYY-WW}.md` - Comprehensive ranked report
- Memory: `life-os/career/opportunities/{YYYY-WW}/ranked`

## Positioning Statement

**Core Thesis**: [Your unique value proposition for this role]

*Example*: "As someone who bridges AI implementation, systems thinking, and education design, I bring a rare combination that aligns perfectly with $ORG's mission to [inferred mission from job description]."

## Likely Interview Questions (Top 5)

### Question 1: "Tell me about yourself"
**Recommended approach**:
- Start with polymath framing (AI + biology + education)
- Emphasize cross-domain pattern recognition
- Connect to company's specific challenges

**Practice response**: [Draft 2-minute answer]

### Question 3: "Describe a technical challenge you solved"
**Recommended approach**:
- Pick achievement from CV that matches role requirements
- Use STAR method (Situation, Task, Action, Result)
- Emphasize learning and iteration

**Practice response**: [Draft using specific example]

### Question 5: "Where do you see yourself in 3-5 years?"
**Recommended approach**:
- Align with company growth trajectory
- Show ambition but not overreach
- Mention continuous learning and impact focus

**Practice response**: [Draft forward-looking answer]

### Anecdote 2: [Cross-domain example]
**Full story**: [Extract from CV]

**When to deploy**:
- Questions about innovation or creativity
- Discussions of unique perspective
- Why you vs. traditional candidates

**Impact framing**: "My unusual background in [domains] gives me the ability to [unique capability]"

## Application Checklist

- [ ] Customize resume with top 5 bullets above
- [ ] Write cover letter using positioning statement
- [ ] Prepare 2-minute "tell me about yourself" answer
- [ ] Research company's recent news/publications
- [ ] Identify 2-3 employees to connect with on LinkedIn
- [ ] Prepare 3 questions to ask interviewer
- [ ] Set up Google Alert for company name
- [ ] Document application in tracking system
- [ ] Follow up in 1 week if no response

**Next Steps**:
1. Refine bullets based on actual job description deep-read
2. Practice interview questions out loud (record yourself)
3. Apply within [deadline from ranking phase]

**Last updated**: $(date)
**Source**: Dual-track career intelligence skill v1.0.0
PITCH_TEMPLATE

  echo "[PitchPrep] Created: outputs/briefs/career_pitch_${ORG}.md"
done

PITCH_COUNT=$(ls outputs/briefs/career_pitch_*.md 2>/dev/null | wc -l)

# MEMORY STORE
npx claude-flow@alpha memory store \
  --key "life-os/career/pitches/${WEEK}/generated" \
  --value "$(ls outputs/briefs/career_pitch_*.md | xargs -I {} basename {})" \
  --metadata "{
    \"WHO\": {\"agent\": \"coder\", \"role\": \"PitchPrep\", \"capabilities\": [\"content-generation\", \"tailoring\", \"storytelling\"]},
    \"WHEN\": {\"iso\": \"$(date -Iseconds)\", \"unix\": $(date +%s)},
    \"PROJECT\": \"life-os-career-tracking\",
    \"WHY\": {\"intent\": \"implementation\", \"task_type\": \"pitch-generation\", \"outcome\": \"tailored-materials\", \"phase\": \"content-creation\"}
  }"

# POST-TASK HOOK
npx claude-flow@alpha hooks post-task \
  --task-id "career-intel-phase4-pitchprep" \
  --metrics "pitches_generated=${PITCH_COUNT}"

# POST-EDIT HOOK (for each generated file)
for PITCH in outputs/briefs/career_pitch_*.md; do
  npx claude-flow@alpha hooks post-edit \
    --file "$PITCH" \
    --memory-key "life-os/career/pitches/${WEEK}/$(basename $PITCH)"
done

echo "[PitchPrep] Phase 4 complete: $PITCH_COUNT pitch briefs generated"
```

### Outputs
- `outputs/briefs/career_pitch_{org}.md` (one per top 5 opportunity)
- Memory: `life-os/career/pitches/{YYYY-WW}/generated`

## Usage

### One-Time Setup

```bash
# Create directory structure
mkdir -p data/sources data/profiles outputs/reports outputs/briefs raw_data phases

# Create data source configs
cat > data/sources/job_boards.yml <<SOURCES
boards:
  - name: Indeed
    url: https://api.indeed.com/v1
    type: api
  - name: LinkedIn
    url: https://www.linkedin.com/jobs/search
    type: scrape
  - name: BioSpace
    url: https://www.biospace.com/jobs
    type: scrape

search_keywords:
  - AI
  - biotech
  - systems biology
  - computational biology
  - machine learning
  - education technology

geo_filters:
  - United States
  - Netherlands
  - Switzerland
  - Germany
  - EU

visa_priority: true
remote_ok: true
SOURCES

cat > data/sources/biotech_watch.yml <<WATCH
policy_sources:
  - name: EMA Regulatory
    url: https://www.ema.europa.eu/en/news
    type: regulatory
  - name: FDA Updates
    url: https://www.fda.gov/news-events
    type: regulatory
  - name: Dutch Immigration
    url: https://ind.nl/en/news
    type: visa
  - name: Swiss Work Permits
    url: https://www.sem.admin.ch/sem/en/home.html
    type: visa

update_frequency: weekly
WATCH

# Create CV profile (populate with your actual content)
cat > data/profiles/cv_core.md <<CV
# Core CV Profile

## Skills
- Artificial Intelligence & Machine Learning
- Prompt Engineering & LLM Integration
- Systems Biology & Computational Biology
- Workshop Design & Facilitation
- Research & Technical Writing
- Python, Node.js, Bash scripting

## Achievements

### AI Cultural Bias Research
Published paper co-written with GPT-4 on cultural archetypes in AI language models.
**Impact**: Novel methodology combining AI assistance with academic rigor.
**Proof**: [Link to publication]

### Guild of the Rose
Founded educational workshop business covering AI integration, personal development, and systems thinking.
**Impact**: Successfully delivered 20+ workshops to diverse audiences.
**Proof**: dnyoussef.com/guild

### Microbiology Research
Published work on insect wing nanostructure antibacterial properties.
**Impact**: Contributed to biomimicry and materials science.
**Proof**: [Link to publication]

### Oasis of Rest Podcast
Co-host of podcast promoting deep thinking and systems awareness.
**Impact**: Growing audience seeking intellectual depth.
**Proof**: Spotify, podcast platforms

## Keywords for Matching
AI, machine learning, biotech, computational biology, education, workshops, research, systems thinking, prompt engineering, Python, data science
CV

echo "✓ Setup complete!"
echo "Next: Run ./career_intel_master.sh"
```

### Running the Skill

```bash
# Weekly execution (recommended: Monday AM, Thursday PM)
./career_intel_master.sh

# Or run phases individually
bash phases/phase1_scout.sh
bash phases/phase2_regwatch.sh
bash phases/phase3_ranker.sh
bash phases/phase4_pitchprep.sh
```

## Expected Outcomes

### Week 1 Baseline
- **15-20 opportunities** scanned and ranked
- **1-3 policy changes** detected and analyzed
- **5 tailored pitches** generated
- **Time saved**: 12-15 hours vs. manual search

### Ongoing Performance
- **2 applications/week** with tailored materials
- **90% reduction** in manual job board scanning
- **Early detection** of EU policy changes affecting visa options
- **Improved application quality** through systematic tailoring

### Success Metrics
- **Applications sent**: 2+ per week
- **Interview conversion**: Track ratio (aim for >10%)
- **Time per application**: <30 min with pre-generated pitch
- **EU option awareness**: Zero missed policy deadlines

## Future Enhancements

1. **ML-based scoring**: Train model on past application outcomes
2. **Automated applications**: One-click apply for pre-vetted roles
3. **Network analysis**: LinkedIn connection recommendations
4. **Salary negotiation**: Historical data + market analysis
5. **Interview scheduling**: Calendar integration
6. **Follow-up automation**: Reminder system for unanswered applications

---

**Last updated**: 2025-01-06
**Version**: 1.0.0
**Maintainer**: David Youssef
**License**: Personal use (Life-OS IP)