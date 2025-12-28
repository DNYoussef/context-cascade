---
name: when-tracking-financial-runway-use-dashboard
description: Real-time financial tracking with burn rate analysis, runway projection, and critical alert thresholds. Know exactly how many weeks you can operate.
---

# Runway Dashboard

Real-time financial tracking with burn rate analysis, runway projection, and critical alert thresholds. Know exactly how many weeks you can operate.

## Overview

Single-agent dashboard that calculates:
- **Current liquid assets** (checking, savings, available credit)
- **Monthly burn rate** (fixed + variable expenses)
- **Revenue streams** (Guild workshops, consulting, hackathons, grants)
- **Runway remaining** (weeks until zero)
- **Alert thresholds** (30-day warning, 60-day caution, 90-day safe)

**Critical for**: Survival planning, decision-making under financial pressure

## Assigned Agent

**analyst (FinTracker role)** - Daily financial snapshot and projection
- Expertise: Financial modeling, trend analysis, forecasting
- Tools: CSV processing, arithmetic, projection algorithms
- Output: Daily dashboard with runway visualization

## Data Flow

```
SKILL: runway-dashboard
  ↓
analyst (FinTracker) executes daily
  ↓
COMMANDS:
  - Read accounts.yml (current balances)
  - Read expenses.yml (monthly burn)
  - Read revenue_streams.yml (income)
  - Calculate runway = assets / (burn - revenue)
  - Generate markdown dashboard
  - Store snapshot in Memory MCP
  ↓
OUTPUT: Daily dashboard + 30/60/90-day projections
```

## Current Status

| Metric | Value |
|--------|-------|
| **Liquid Assets** | \$$(printf "%.2f" $TOTAL_ASSETS) |
| **Monthly Burn** | \$$(printf "%.2f" $MONTHLY_BURN) |
| **Monthly Revenue** | \$$(printf "%.2f" $MONTHLY_REVENUE) |
| **Net Burn** | \$$(printf "%.2f" $NET_BURN) |
| **Runway Remaining** | **$RUNWAY_WEEKS weeks** |
| **Alert Status** | $ALERT_STATUS |

------|---------|
| Checking | \$$(printf "%.2f" $CHECKING) |
| Savings | \$$(printf "%.2f" $SAVINGS) |
| Credit Available | \$$(printf "%.2f" $CREDIT_AVAIL) (emergency only) |
| **Total Liquid** | **\$$(printf "%.2f" $TOTAL_ASSETS)** |

## Revenue Streams

| Source | Monthly Avg |
|--------|-------------|
| Guild Workshops | \$$(printf "%.2f" $GUILD_REVENUE) |
| Consulting | \$$(printf "%.2f" $CONSULTING_REVENUE) |
| Other (hackathons, grants) | \$$(printf "%.2f" $OTHER_REVENUE) |
| **Total Revenue** | **\$$(printf "%.2f" $MONTHLY_REVENUE)/month** |

-------|-----------------|
| Current trajectory | **$RUNWAY_WEEKS** |
| If revenue stops | $(echo "scale=1; ($TOTAL_ASSETS / $MONTHLY_BURN) * 4.33" | bc) weeks |
| If double Guild revenue | $(echo "scale=1; ($TOTAL_ASSETS / ($MONTHLY_BURN - $GUILD_REVENUE * 2)) * 4.33" | bc) weeks |
| If land 1 consulting gig (+\$5k/mo) | $(echo "scale=1; ($TOTAL_ASSETS / ($MONTHLY_BURN - 5000)) * 4.33" | bc) weeks |

## 30/60/90-Day Forecast

**Assumptions**:
- Fixed expenses remain constant
- Revenue continues at current average
- No major windfalls or emergencies

| Date | Projected Balance | Status |
|------|-------------------|--------|
| $(date -d '+30 days' +%Y-%m-%d) | \$$(echo "$TOTAL_ASSETS - $NET_BURN" | bc) | $(if (( $(echo "($TOTAL_ASSETS - $NET_BURN) < ($NET_BURN * 2)" | bc -l) )); then echo "🟠 Warning zone"; else echo "🟢 Safe"; fi) |
| $(date -d '+60 days' +%Y-%m-%d) | \$$(echo "$TOTAL_ASSETS - ($NET_BURN * 2)" | bc) | $(if (( $(echo "($TOTAL_ASSETS - $NET_BURN * 2) < ($NET_BURN * 2)" | bc -l) )); then echo "🔴 Critical"; else echo "🟡 Caution"; fi) |
| $(date -d '+90 days' +%Y-%m-%d) | \$$(echo "$TOTAL_ASSETS - ($NET_BURN * 3)" | bc) | $(if (( $(echo "($TOTAL_ASSETS - $NET_BURN * 3) < 0" | bc -l) )); then echo "🔴 Zero"; else echo "🟠 Low"; fi) |

**Last updated**: $(date)
**Next update**: $(date -d '+1 day' +%Y-%m-%d) 08:00 AM (automated)

**Data sources**:
- data/finances/accounts.yml (manual update required)
- data/finances/expenses.yml (reviewed monthly)
- data/finances/revenue_streams.yml (updated as income received)
DASHBOARD

# SAVE HISTORICAL SNAPSHOT
echo "$TODAY,$TOTAL_ASSETS,$NET_BURN,$RUNWAY_WEEKS" >> raw_data/runway/history.csv

# MEMORY STORE
npx claude-flow@alpha memory store \
  --key "life-os/runway/${MONTH}/daily-snapshots/${TODAY}" \
  --value "$(cat outputs/dashboards/runway_${TODAY}.md)" \
  --metadata "{
    \"WHO\": {\"agent\": \"analyst\", \"role\": \"FinTracker\", \"capabilities\": [\"financial-modeling\", \"forecasting\"]},
    \"WHEN\": {\"iso\": \"$(date -Iseconds)\", \"unix\": $(date +%s)},
    \"PROJECT\": \"life-os-financial-tracking\",
    \"WHY\": {\"intent\": \"analysis\", \"task_type\": \"runway-calculation\", \"outcome\": \"survival-metrics\", \"phase\": \"daily-snapshot\"}
  }"

# POST-TASK HOOK
npx claude-flow@alpha hooks post-task \
  --task-id "runway-dashboard-${TODAY}" \
  --metrics "runway_weeks=${RUNWAY_WEEKS},alert_status=${ALERT_STATUS}"

echo "✓ Runway Dashboard Updated: outputs/dashboards/runway_${TODAY}.md"
echo "  Status: $ALERT_STATUS"
echo "  Runway: $RUNWAY_WEEKS weeks"
```

## Scheduled Automation

**Frequency**: Daily at 8:00 AM (Monday-Friday)

**Windows Task Scheduler**:
```powershell
# scheduled_tasks/runway_update_scheduled.ps1
$PROJECT_PATH = "C:\Users\17175"
cd $PROJECT_PATH
Get-Content prompts\runway_update.txt | claude --project $PROJECT_PATH
```

**Manual execution**:
```bash
bash runway_dashboard.sh
```

## Success Metrics

- **Zero surprises**: Always know runway status
- **Alert response**: <24 hours to act on critical alerts
- **Forecast accuracy**: ±10% on 30-day projections
- **Peace of mind**: Quantified vs. emotional stress

**Last updated**: 2025-01-06
**Version**: 1.0.0
**Scheduled**: Daily, 8:00 AM (Mon-Fri)
**Maintainer**: David Youssef