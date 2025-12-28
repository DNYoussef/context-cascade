---
name: when-finding-high-ev-hackathons-use-ev-optimizer
description: Expected Value (EV) calculator for hackathons and bounties. Optimizes for prize × p(win) − time_cost with judge fit analysis and past win pattern learning.
---

# Hackathon EV Optimizer

Expected Value (EV) calculator for hackathons and bounties. Optimizes for prize × p(win) − time_cost with judge fit analysis and past win pattern learning.

## Overview

This skill orchestrates 3 specialist agents to:
1. **Collector** (researcher) - Scrape hackathon/bounty listings, normalize metadata
2. **EVCalc** (analyst) - Calculate expected value: (prize × p_win) − time_cost
3. **TeamBuilder** (researcher) - Identify skill gaps, generate outreach drafts
4. **SubmissionKit** (coder) - Auto-generate README, demo script, form fills

**Critical differentiator**: Learns from your past project wins to estimate p(win) for new competitions.

## When to Use

- **Weekly**: Scan for new hackathons/bounties (Monday, Thursday)
- **Before commitment**: Calculate EV before dedicating 48 hours
- **Team formation**: Identify skill gaps and potential collaborators
- **Quick wins**: Find high-EV, low-time-cost opportunities

## Assigned Agents

### Primary Agents

**researcher (Collector role)** - Phase 1: Web scraping, metadata extraction, judge research
- Expertise: API integration, web crawling, YAML processing
- Tools: curl, puppeteer, jq, yq
- Output: Normalized hackathon CSV with prizes, themes, judges, deadlines

**analyst (EVCalc role)** - Phase 2: Probability estimation, EV calculation, risk analysis
- Expertise: Statistical modeling, decision analysis, pattern matching
- Tools: Python/Node scoring, similarity algorithms, historical analysis
- Output: Ranked opportunities with EV justifications

### Secondary Agents

**researcher (TeamBuilder role)** - Phase 3: Skill gap analysis, network mapping
- Expertise: Competency mapping, collaboration strategy
- Tools: LinkedIn API, GitHub analysis, outreach templates
- Output: Team composition recommendations + outreach emails

**coder (SubmissionKit role)** - Phase 4: Automation, template generation, form filling
- Expertise: Boilerplate generation, documentation, automation
- Tools: Template engines, README generators, form auto-fill scripts
- Output: MVS (Minimum Viable Submission) package

## Coordination Pattern

```
SKILL: hackathon-ev-optimizer
  ↓
hierarchical-coordinator spawns 4 sequential phases
  ↓
Phase 1: Collector (researcher) → raw hackathon data
Phase 2: EVCalc (analyst) → EV-ranked opportunities
Phase 3: TeamBuilder (researcher) → skill gaps + outreach
Phase 4: SubmissionKit (coder) → MVS packages for top 3
  ↓
All phases coordinate via Memory MCP with WHO/WHEN/PROJECT/WHY tagging
```

## Phase 2: EVCalc (Expected Value Calculation)

**Agent**: `analyst` (EVCalc role)

### Inputs
- Memory: `life-os/hackathons/{YYYY-WW}/opportunities`
- `data/profiles/case_studies.md` - Past project wins for similarity matching

### Commands Executed

```bash
#!/bin/bash
# Phase 2: Expected Value Calculation

# PRE-TASK HOOK
npx claude-flow@alpha hooks pre-task \
  --description "Hackathon EV: probability estimation" \
  --agent "analyst" \
  --role "EVCalc" \
  --skill "hackathon-ev-optimizer"

# SETUP
WEEK=$(date +%Y-%W)

# RETRIEVE HACKATHON DATA
npx claude-flow@alpha memory retrieve \
  --key "life-os/hackathons/${WEEK}/opportunities" \
  > raw_data/hackathons/events_${WEEK}.csv

# READ CASE STUDIES (past wins)
CASE_STUDIES=$(grep -A 500 '## Past Projects' data/profiles/case_studies.md)

# EV CALCULATION SCRIPT
cat > raw_data/hackathons/calculate_ev.js <<'EVCALC'
const fs = require('fs');
const csv = require('csv-parser');

// Read case studies (simplified - in production, parse markdown properly)
const caseStudies = process.argv[2].split('\n')
  .filter(line => line.includes('###'))
  .map(line => {
    const match = line.match(/###\s+(.+)/);
    return match ? match[1].toLowerCase() : '';
  })
  .filter(Boolean);

console.error('[EVCalc] Past projects:', caseStudies.join(', '));

const results = [];

fs.createReadStream('raw_data/hackathons/events_' + process.argv[3] + '.csv')
  .pipe(csv())
  .on('data', (row) => {
    const theme = row.theme.toLowerCase();
    const topPrize = parseFloat(row.top_prize) || 0;
    const deadline = new Date(row.deadline);
    const daysUntil = Math.floor((deadline - Date.now()) / (1000 * 60 * 60 * 24));

    // PROBABILITY ESTIMATION
    // p(win) = similarity to past wins × judge alignment × skill coverage

    // Similarity score (0-1): keyword overlap with case studies
    const themeWords = theme.split(/\s+/);
    const similarityMatches = themeWords.filter(word =>
      caseStudies.some(project => project.includes(word))
    ).length;
    const similarityScore = Math.min(1, similarityMatches / Math.max(1, themeWords.length));

    // Judge alignment (0-1): placeholder - in production, match judge expertise to your profile
    const judgeAlignment = 0.5; // Default 50%

    // Skill coverage (0-1): deliverables match your capabilities
    const deliverables = row.deliverables.toLowerCase();
    const hasRequiredSkills =
      (deliverables.includes('ai') || deliverables.includes('ml')) &&
      (deliverables.includes('demo') || deliverables.includes('prototype'));
    const skillCoverage = hasRequiredSkills ? 0.8 : 0.4;

    // Combined probability (conservative)
    const p_win = (similarityScore * 0.4) + (judgeAlignment * 0.3) + (skillCoverage * 0.3);

    // TIME COST ESTIMATION
    // Base: 48 hours for hackathon, 20 hours for bounty
    const isHackathon = row.location !== 'Remote' || row.name.toLowerCase().includes('hackathon');
    const timeHours = isHackathon ? 48 : 20;
    const hourlyValue = 75; // Your opportunity cost ($/hour)
    const timeCost = timeHours * hourlyValue;

    // EXPECTED VALUE
    const EV = (topPrize * p_win) - timeCost;

    // RISK FLAGS
    const riskFlags = [];
    if (daysUntil < 7) riskFlags.push('SHORT_NOTICE');
    if (topPrize < 5000) riskFlags.push('LOW_PRIZE');
    if (p_win < 0.2) riskFlags.push('LOW_WIN_PROB');
    if (timeHours > 40) riskFlags.push('HIGH_TIME_COST');

    results.push({
      ...row,
      p_win: p_win.toFixed(3),
      time_hours: timeHours,
      time_cost: timeCost,
      ev: EV.toFixed(2),
      ev_per_hour: (EV / timeHours).toFixed(2),
      days_until: daysUntil,
      risk_flags: riskFlags.join('|'),
      rationale: `Similarity=${(similarityScore*100).toFixed(0)}%, Judge=${(judgeAlignment*100).toFixed(0)}%, Skills=${(skillCoverage*100).toFixed(0)}%`
    });
  })
  .on('end', () => {
    // Sort by EV descending
    results.sort((a, b) => parseFloat(b.ev) - parseFloat(a.ev));

    // Output top 20
    console.log(JSON.stringify(results.slice(0, 20), null, 2));
  });
EVCALC

# RUN EV CALCULATOR
node raw_data/hackathons/calculate_ev.js "$CASE_STUDIES" "$WEEK" \
  > raw_data/hackathons/ev_ranked_${WEEK}.json

RANKED_COUNT=$(jq length raw_data/hackathons/ev_ranked_${WEEK}.json)
echo "[EVCalc] Ranked $RANKED_COUNT opportunities by EV"

# GENERATE MARKDOWN REPORT
cat > outputs/reports/hackathons_${WEEK}.md <<REPORT_HEADER
# Hackathon EV Report - Week $WEEK

**Generated**: $(date)
**Source**: Automated multi-platform scanning
**Total Scanned**: $(tail -n +2 raw_data/hackathons/events_${WEEK}.csv | wc -l)
**High-EV Opportunities**: $RANKED_COUNT

---|-------|-------|-------|--------|------|----|----|----------|-------|------|
REPORT_HEADER

jq -r '.[] | [
  .name,
  .theme,
  "$" + .top_prize,
  (.p_win | tonumber * 100 | tostring + "%"),
  .time_hours + "h",
  "$" + .ev,
  "$" + .ev_per_hour,
  .days_until + "d",
  .risk_flags,
  .url
] | @tsv' raw_data/hackathons/ev_ranked_${WEEK}.json \
  | awk 'BEGIN{OFS="|"; rank=1} {print rank++, $1, $2, $3, $4, $5, $6, $7, $8, $9, $10}' \
  >> outputs/reports/hackathons_${WEEK}.md

# APPEND EV METHODOLOGY
cat >> outputs/reports/hackathons_${WEEK}.md <<'METHODOLOGY'

## Recommended Action

### Immediate Priorities (EV > $1,000)
METHODOLOGY

jq -r '.[] | select(.ev | tonumber > 1000) | "- **\(.name)** (EV: $\(.ev), Deadline: \(.days_until)d)\n  - **Rationale**: \(.rationale)\n  - **Action**: Review deliverables, form team if needed\n"' \
  raw_data/hackathons/ev_ranked_${WEEK}.json \
  >> outputs/reports/hackathons_${WEEK}.md

cat >> outputs/reports/hackathons_${WEEK}.md <<'FOOTER'

### Watch List (EV $500-$1,000)
Consider if time allows or theme strongly aligns.

### Skip (EV < $500)
Opportunity cost too high - focus on higher-EV options or direct client work.

## Phase 3: TeamBuilder (Skill Gap Analysis)

**Agent**: `researcher` (TeamBuilder role)

### Inputs
- Memory: `life-os/hackathons/{YYYY-WW}/ev-ranked` (top 3)
- `data/profiles/cv_core.md` - Your skills inventory

### Commands Executed

```bash
#!/bin/bash
# Phase 3: Team Formation & Skill Gap Analysis

# PRE-TASK HOOK
npx claude-flow@alpha hooks pre-task \
  --description "Hackathon EV: team building" \
  --agent "researcher" \
  --role "TeamBuilder" \
  --skill "hackathon-ev-optimizer"

# SETUP
WEEK=$(date +%Y-%W)
mkdir -p outputs/briefs/teams

# RETRIEVE TOP 3 OPPORTUNITIES
npx claude-flow@alpha memory retrieve \
  --key "life-os/hackathons/${WEEK}/ev-ranked" \
  | jq '.[0:3]' > raw_data/hackathons/top3_${WEEK}.json

# READ YOUR SKILLS
MY_SKILLS=$(grep -A 100 '## Skills' data/profiles/cv_core.md | grep '- ' | sed 's/- //')

# ANALYZE EACH OPPORTUNITY
jq -c '.[]' raw_data/hackathons/top3_${WEEK}.json | while read -r event; do
  SLUG=$(echo "$event" | jq -r '.slug')
  NAME=$(echo "$event" | jq -r '.name')
  DELIVERABLES=$(echo "$event" | jq -r '.deliverables')

  echo "[TeamBuilder] Analyzing: $SLUG"

  # SKILL GAP DETECTION (simple keyword matching)
  cat > outputs/briefs/teams/${SLUG}_team_analysis.md <<TEAM_HEADER
# Team Analysis: $NAME

**Event**: $NAME
**Slug**: $SLUG
**EV**: \$$(echo "$event" | jq -r '.ev')
**Deadline**: $(echo "$event" | jq -r '.days_until') days

## Your Skills Coverage

GAPS

  # Check which skills you have
  echo "$MY_SKILLS" | while read -r skill; do
    if echo "$DELIVERABLES" | grep -qi "$skill"; then
      echo "- ✓ **$skill** (covered)" >> outputs/briefs/teams/${SLUG}_team_analysis.md
    else
      echo "- $skill" >> outputs/briefs/teams/${SLUG}_team_analysis.md
    fi
  done

  cat >> outputs/briefs/teams/${SLUG}_team_analysis.md <<'RECOMMENDATIONS'

## Outreach Email Template

**Subject**: Hackathon Team Formation - $NAME

OUTREACH_TEMPLATE

  echo "[TeamBuilder] Created: outputs/briefs/teams/${SLUG}_team_analysis.md"
done

TEAM_ANALYSIS_COUNT=$(ls outputs/briefs/teams/*_team_analysis.md 2>/dev/null | wc -l)

# POST-TASK HOOK
npx claude-flow@alpha hooks post-task \
  --task-id "hackathon-ev-phase3-teambuilder" \
  --metrics "team_analyses=${TEAM_ANALYSIS_COUNT}"

echo "[TeamBuilder] Phase 3 complete: $TEAM_ANALYSIS_COUNT team analyses created"
```

### Outputs
- `outputs/briefs/teams/{slug}_team_analysis.md` - Skill gaps + outreach templates

## 24-Hour Plan

### Hour 0-4: Research & Planning
- [ ] Deep-read hackathon requirements and judging criteria
- [ ] Review past winning submissions (DevPost/GitHub)
- [ ] Finalize tech stack (bias toward what you know)
- [ ] Create project skeleton (README, repo structure)
- [ ] Set up dev environment and dependencies

### Hour 4-12: Core Implementation
- [ ] Implement MVP feature set (focus on demo-ability)
- [ ] Build proof-of-concept for most impressive feature
- [ ] Integrate AI/ML component if theme-relevant
- [ ] Create basic UI/dashboard (even if CLI)
- [ ] Commit progress regularly (backup strategy)

### Hour 12-18: Polish & Demo Prep
- [ ] Add error handling and edge case coverage
- [ ] Create demo dataset/examples
- [ ] Record demo video (2-3 minutes, script it)
- [ ] Write compelling README with screenshots
- [ ] Prepare judging criteria mapping document

### Hour 18-24: Submission & Presentation
- [ ] Final testing and bug fixes
- [ ] Deploy to public URL (Vercel/Netlify/Replit)
- [ ] Complete submission form (auto-fill where possible)
- [ ] Submit 2 hours before deadline (buffer for issues)
- [ ] Tweet/post about submission (social proof)

## Judging Criteria Mapping

$(echo "$event" | jq -r '.deliverables' | tr ',' '\n' | while read -r criterion; do
  echo "### $criterion"
  echo ""
  echo "**Your approach**:"
  echo "- [How you'll address this criterion]"
  echo "- [Specific feature/demo that proves it]"
  echo "- [Evidence/metrics to show success]"
  echo ""
done)

## Submission Form Auto-Fill

**Project Name**: [Catchy name related to theme]

**Tagline** (1 sentence): "We [verb] [problem] for [audience] using [innovation]"

**Description** (3 paragraphs):
1. **Problem**: What pain point does this solve? Who faces it?
2. **Solution**: How does your project address it? What's unique?
3. **Impact**: What's the potential? Why does it matter?

**Tech Stack**:
- Frontend: [e.g., React, Next.js]
- Backend: [e.g., Node.js, Python/FastAPI]
- AI/ML: [e.g., OpenAI API, Hugging Face, custom models]
- Database: [e.g., PostgreSQL, MongoDB]
- Deployment: [e.g., Vercel, AWS, Replit]

**Challenges**:
- [Specific technical hurdle you overcame]
- [How you learned something new during the hackathon]
- [Trade-off decision you made and why]

**Accomplishments**:
- [Quantified achievement, e.g., "Processed 10k records in <2s"]
- [Novel integration or approach]
- [Working MVP in 24 hours]

**What we learned**:
- [Technical learning]
- [Domain learning]
- [Team collaboration learning if applicable]

**What's next**:
- [Feature roadmap]
- [Scaling plan]
- [Potential users or customers]

## Post-Submission Actions

- [ ] Tweet about submission with demo link
- [ ] Post in hackathon Discord/Slack
- [ ] Star and watch competitor projects (networking)
- [ ] Prepare 1-min pitch for potential sponsor calls
- [ ] Document lessons learned for next time
- [ ] Update case_studies.md with project (win or lose)

## Master Orchestration + Scheduling

```bash
#!/bin/bash
# Master: Hackathon EV Optimizer with Scheduled Execution

set -e

WEEK=$(date +%Y-%W)
DAY=$(date +%A)

echo "=========================================="
echo "Hackathon EV Optimizer - Week $WEEK ($DAY)"
echo "=========================================="
echo ""

# Check if scheduled run (Monday or Thursday)
if [[ "$DAY" != "Monday" && "$DAY" != "Thursday" && "$1" != "--force" ]]; then
  echo "⏭️  Skipping: Scheduled for Monday/Thursday only"
  echo "   Use --force to run manually"
  exit 0
fi

# SESSION START
npx claude-flow@alpha hooks session-start \
  --session-id "hackathon-ev-${WEEK}"

echo ""
echo "[Phase 1/4] Collector - Scanning hackathon platforms..."
bash phases/phase1_collector.sh

echo ""
echo "[Phase 2/4] EVCalc - Calculating expected values..."
bash phases/phase2_evcalc.sh

echo ""
echo "[Phase 3/4] TeamBuilder - Analyzing skill gaps..."
bash phases/phase3_teambuilder.sh

echo ""
echo "[Phase 4/4] SubmissionKit - Generating MVS packages..."
bash phases/phase4_submissionkit.sh

# SESSION END
npx claude-flow@alpha hooks session-end \
  --session-id "hackathon-ev-${WEEK}" \
  --export-metrics true

echo ""
echo "=========================================="
echo "✓ Hackathon EV Optimization Complete"
echo "=========================================="
echo ""
echo "📊 Report: outputs/reports/hackathons_${WEEK}.md"
echo ""
echo "🎯 High-EV Opportunities:"
jq -r '.[0:3] | .[] | "  - \(.name) (EV: $\(.ev), Deadline: \(.days_until)d)"' \
  raw_data/hackathons/ev_ranked_${WEEK}.json
echo ""
echo "📦 MVS Packages:"
ls outputs/briefs/mvs/h_*_MVS.md 2>/dev/null | sed 's/^/  - /' || echo "  (none generated)"
```

## Usage

### One-Time Setup

```bash
# Create directories
mkdir -p data/sources data/profiles outputs/reports outputs/briefs/mvs outputs/briefs/teams raw_data/hackathons phases prompts scheduled_tasks

# Create hackathon sources config
cat > data/sources/hackathons.yml <<SOURCES
platforms:
  - name: DevPost
    url: https://devpost.com/api/hackathons
    type: api
  - name: Gitcoin
    url: https://gitcoin.co/api/v0.1/bounties
    type: api
  - name: DoraHacks
    url: https://dorahacks.io/api/buidl/grants
    type: api
  - name: ETHGlobal
    url: https://ethglobal.com/events
    type: scrape

prize_threshold: 1000
time_max_hours: 60
SOURCES

# Create case studies profile
cat > data/profiles/case_studies.md <<CASES
# Past Projects & Wins

## Past Projects

### AI Cultural Bias Research
Published paper using GPT-4 collaboration. Novel methodology.
**Themes**: AI, NLP, cultural studies, research
**Outcome**: Publication, academic credibility

### Guild of the Rose Workshops
Educational business covering AI integration, systems thinking.
**Themes**: Education, AI, workshops, facilitation
**Outcome**: Revenue generation, audience building

### Microbiology Nanostructure Research
Published work on antibacterial properties.
**Themes**: Biology, materials science, biomimicry
**Outcome**: Scientific publication

## Skills Inventory
- AI/ML implementation
- Systems thinking and analysis
- Workshop design and delivery
- Research methodology
- Python, Node.js development
- Data visualization
CASES

echo "✓ Setup complete! Run: ./hackathon_ev_master.sh"
```

### Running

```bash
# Manual execution
./hackathon_ev_master.sh --force

# Scheduled execution (automated via Task Scheduler)
# Runs Monday & Thursday at 9:00 AM automatically
```

## Success Metrics

- **Opportunities scanned**: 10-20/week
- **High-EV identified**: 2-5 with EV >$1,000
- **MVS packages generated**: 3/week
- **Actual entries**: 1-2/month
- **Win rate**: Track and improve (goal: >15%)
- **ROI**: (Prizes won) / (Time invested)

---

**Last updated**: 2025-01-06
**Version**: 1.0.0
**Scheduled**: Monday & Thursday, 9:00 AM
**Maintainer**: David Youssef