# Skill Discovery Index

**Purpose:** Top-level model uses this to discover and route to skills
**Updated:** 2026-01-09
**Total Skills:** 175 (all consolidated, duplicates removed, structures fixed)

---

## Quick Lookup by Intent

| User Intent | Skill | Agent Chain |
|-------------|-------|-------------|
| Build a feature | `feature-dev-complete` | planner -> coder -> tester -> reviewer |
| Fix a bug | `smart-bug-fix` | debugger -> coder -> tester |
| Review code | `code-review-assistant` | reviewer -> security-auditor |
| Research topic | `deep-research-orchestrator` | researcher -> synthesizer |
| Create skill | `skill-forge` | skill-creator -> validator |
| Create agent | `agent-creator` | agent-architect -> validator |
| Deploy app | `production-readiness` | devops -> tester -> deployer |
| Analyze code | `functionality-audit` | analyzer -> reporter |
| Use Codex CLI | `codex-auto` | codex-agent |
| Use Gemini CLI | `gemini-megacontext` | gemini-agent |
| Check system health | `health-system` | health-agents |
| Respond to recruiters | `recruiter-outreach-pipeline` | writer -> scheduler |

---

## Skills by Category

### delivery/ (10+ skills)
Core development workflows that ship features.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `feature-dev-complete` | 12-stage feature lifecycle | planner, coder, tester, reviewer |
| `smart-bug-fix` | Systematic debugging | debugger, coder, tester |
| `sop-api-development` | API development workflow | api-designer, coder, tester |
| `testing-framework` | Comprehensive testing | tester, e2e-tester |

### quality/ (22+ skills)
Testing, auditing, and verification.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `code-review-assistant` | Multi-agent code review | reviewer, security-auditor |
| `functionality-audit` | Verify code works | analyzer, tester |
| `theater-detection-audit` | Detect fake code | theater-detector |
| `quick-quality-check` | Fast parallel checks | linter, tester |

### research/ (21+ skills)
Research pipelines and analysis.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `deep-research-orchestrator` | Full research pipeline | researcher, synthesizer |
| `literature-synthesis` | PRISMA-compliant review | literature-reviewer |
| `baseline-replication` | Statistical validation | statistician |
| `method-development` | Novel algorithm design | innovator |

### orchestration/ (23+ skills)
Multi-agent coordination.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `cascade-orchestrator` | Multi-skill pipelines | coordinator |
| `swarm-orchestration` | Complex workflows | swarm-coordinator |
| `hive-mind-advanced` | Collective intelligence | queen, workers |
| `parallel-swarm-implementation` | 54-agent parallel | swarm-master |

### foundry/ (22+ skills)
Creating new agents, skills, prompts.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `skill-forge` | Create skills | skill-creator, validator |
| `agent-creator` | Create agents | agent-architect |
| `prompt-architect` | Optimize prompts | prompt-engineer |
| `hook-creator` | Create hooks | hook-developer |

### operations/ (23+ skills)
DevOps, infrastructure, releases.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `production-readiness` | Deployment validation | devops, tester |
| `cicd-intelligent-recovery` | CI/CD with recovery | cicd-engineer |
| `cloud-platforms` | Cloud deployment | aws/gcp/azure-specialist |

### security/ (13+ skills)
Security and compliance.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `network-security-setup` | Network security | security-engineer |
| `reverse-engineering-deep` | Deep RE analysis | reverse-engineer |
| `compliance` | Security compliance | compliance-auditor |

### platforms/ (18+ skills)
Core platform services.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `agentdb-advanced` | Agent database | db-architect |
| `flow-nexus-platform` | Flow orchestration | flow-manager |
| `machine-learning` | ML pipelines | ml-engineer |

### specialists/ (11+ skills)
Domain experts.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `python-specialist` | Python expertise | python-expert |
| `ml-expert` | ML expertise | ml-specialist |
| `language-specialists` | Multi-language | lang-experts |

### tooling/ (17+ skills)
Utilities and adapters.

| Skill | Purpose | Key Agents |
|-------|---------|------------|
| `web-cli-teleport` | Web-to-CLI bridge | teleporter |
| `pptx-generation` | Presentation creation | pptx-generator |
| `intent-analyzer` | Analyze user intent | intent-parser |

---

## Packaged Skills

All skills are now packaged in `skills/packaged/` as `.skill` files for efficient loading.

### foundry/recursive-improvement/ (5 skills)
Self-improvement and meta-optimization loops.

| Skill | Purpose | Key Agents | Location |
|-------|---------|------------|----------|
| `recursive-improvement` | Parent skill for recursive loops | coordinator | `skills/packaged/recursive-improvement.skill` |
| `bootstrap-loop` | Self-improvement bootstrap cycle | coordinator | `skills/packaged/bootstrap-loop.skill` |
| `eval-harness` | Evaluation framework for skill quality | evaluator | `skills/packaged/eval-harness.skill` |
| `improvement-pipeline` | Automated improvement workflow | optimizer | `skills/packaged/improvement-pipeline.skill` |
| `prompt-forge` | Iterative prompt refinement | prompt-engineer | `skills/packaged/prompt-forge.skill` |

### guards/ (1 skill)
Pre-execution safety checks.

| Skill | Purpose | Key Agents | Location |
|-------|---------|------------|----------|
| `library-check` | Pre-coding library reuse guard | scanner | `skills/packaged/library-check.skill` |

### specialists/health-system/ (1 skill)
System monitoring and self-repair.

| Skill | Purpose | Key Agents | Location |
|-------|---------|------------|----------|
| `health-system` | 7-agent health monitoring | health-agents | `skills/packaged/health-system.skill` |

### security/ (1 skill)
Security and reverse engineering.

| Skill | Purpose | Key Agents | Location |
|-------|---------|------------|----------|
| `reverse-engineer-debug` | Binary/protocol RE debugging | reverse-engineer | `skills/packaged/reverse-engineer-debug.skill` |

### tooling/ (1 skill)
Professional automation.

| Skill | Purpose | Key Agents | Location |
|-------|---------|------------|----------|
| `recruiter-outreach-pipeline` | Automated recruiter response | writer, scheduler | `skills/packaged/recruiter-outreach-pipeline.skill` |

---

## Skill Invocation Pattern

```
Skill("skill-name")           // Load the SOP
    |
    v
Task("description", "prompt", "agent-type")  // Invoke agent
    |
    v
TodoWrite({ todos })          // Track progress
```

**Golden Rule:** Skills define the SOP, Agents execute it.

---

## Playbooks (7)

High-level workflows that chain multiple skills:

| Playbook | Skills Chained | Purpose |
|----------|----------------|---------|
| `full-feature` | intent-analyzer -> feature-dev-complete -> code-review | Complete feature |
| `research-to-code` | deep-research -> method-development -> coder | Research implementation |
| `quality-gate` | functionality-audit -> theater-detection -> security | Full quality check |

---

## Discovery Paths

- **Skill Index:** `discovery/SKILL-INDEX.md` (this file)
- **Agent Registry:** `agents/foundry/registry/registry.json`
- **Command Index:** `commands/README.md`
- **Packaged Skills:** `skills/packaged/{skill-name}.skill`
- **Raw Skill Sources:** `skills/{category}/{skill-name}/SKILL.md` (used for building packaged skills)

---

## Auto-Routing

The `skill-router-hook.sh` automatically matches user requests to skills using:
1. Keyword matching against skill-index.json
2. Intent classification
3. Confidence scoring

Example:
- "build a login feature" -> `feature-dev-complete` (0.92)
- "fix the auth bug" -> `smart-bug-fix` (0.88)
- "review this PR" -> `code-review-assistant` (0.95)
