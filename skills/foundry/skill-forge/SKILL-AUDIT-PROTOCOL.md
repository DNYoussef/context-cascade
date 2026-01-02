---
name: skill-forge-skill-audit-protocol
description: Protocol for auditing Skill Forge documentation completeness and quality
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: foundry/skill-forge
x-vcl-compliance: v3.1.1
---

### L1 Improvement
- Reformatted the audit protocol into English-first SOP with actionable phases.
- Preserved the full audit questionnaire and meta frames in the appendix.
- Added explicit confidence ceiling guidance for audit results.

## STANDARD OPERATING PROCEDURE

### Purpose
Automate and guide audits of Skill Forge documentation for completeness, quality, and compliance.

### Trigger Conditions
- During Skill Forge Phase 7a (Quality Review) or any recursive-improvement cycle.
- Before release to ensure all required sections, evidence, and hooks are present.

### Execution Phases
1. **Gather Meta Information**
   - Record purpose, integrations (Skill Forge Phase 7a, recursive loops), version (1.0.0), and last update.
2. **Run Section Checks**
   - Verify SKILL.md required sections, integration notes, MCP usage, hooks, quality gates, and evidence markers.
3. **Validate Artifacts**
   - Confirm examples, tests, references, resources, diagrams, and scripts exist and are referenced.
4. **Score and Report**
   - Apply audit scoring rubric; note findings, gaps, and remediation steps.
   - Produce an audit report aligned to the checklist in the appendix.

### Output Format
- Audit scope (skill, version) and checklist results.
- Missing items with remediation owners and timelines.
- Confidence statement using ceiling syntax: `Confidence: X.XX (ceiling: TYPE Y.YY)` (ceilings: inference/report 0.70; research 0.85; observation/definition 0.95).

### Validation Checklist
- [ ] Meta info captured (purpose, integrations, versions).
- [ ] Section completeness verified against template.
- [ ] Artifacts (examples/tests/resources/references/diagrams/scripts) present.
- [ ] Audit findings and remediation recorded.
- [ ] Confidence statement included with explicit ceiling.

Confidence: 0.70 (ceiling: inference 0.70) - Audit protocol rewritten to English-first SOP with full checklist preserved in the appendix.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

<details>
<summary>Legacy content (verbatim)</summary>

# Beceri Dokumantasyon Denetim Protokolu (Skill Documentation Audit Protocol) v1.0

<!-- VCL v3.1.1 COMPLIANT - L1 Internal Documentation -->
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_document]] -->

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

---

## S1 META BILGI CERCEVESI (Meta Information Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_metadata]] -->
<!-- [[MOR:root:D-N-T]] Denetim = root morpheme for audit-inspect-review -->
<!-- [[COM:Denetim+Protokol+Tanimlama]] German: Audit-Protokoll-Definition -->

[define|neutral] PROTOCOL_META := {
  amac: "Beceri dokumantasyon tamamlamasinin otomatik denetimi ve iyilestirilmesi", // purpose
  entegrasyonlar: ["skill-forge Faz 7a", "recursive-improvement meta-dongu"],
  surum: "1.0.0",
  son_guncelleme: "2025-12-17"
} [ground:witnessed:meta-definition] [conf:0.95] [state:confirmed]

---

## S2 GENEL BAKIS CERCEVESI (Overview Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_overview]] -->
<!-- [[MOR:root:O-T-M]] Otomatik = root for automatic-self-auto -->
<!-- [[COM:Otomatik+Denetim+Iyilestirme]] German: Automatische-Audit-Verbesserung -->
<!-- [[SPC:kuzey]] Primary execution direction -->

[define|neutral] PROTOCOL_OVERVIEW := {
  kural_adi: "Protokol Genel Bakisi", // Protocol Overview
  aciklama: "Meta-dongununun beceri dokumantasyonunu nasil otomatik denetleyip iyilestirdigini tanimlar",
  calistirma_zamanlari: [
    {
      ad: "Beceri olusturma sirasinda",
      faz: "skill-forge Faz 7a"
    },
    {
      ad: "Periyodik recursive-improvement ile",
      detay: "toplu denetim"
    },
    {
      ad: "Talep uzerine /skill-audit komutu ile",
      detay: null
    }
  ]
} [ground:witnessed:overview-design] [conf:0.90] [state:confirmed]

---

## S3 KATMAN GEREKSINIMLERI CERCEVESI (Tier Requirements Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_tier]] -->
<!-- [[MOR:root:G-R-K]] Gereksinim = root for requirement-need-demand -->
<!-- [[COM:Katman+Gereksinim+Tespit]] German: Stufen-Anforderungs-Erkennung -->

### S3.1 Katman 1: Kritik (SAHIP OLMALI - %100 zorunlu)

[define|neutral] TIER_1_REQUIREMENTS := {
  kural_adi: "Katman 1 Gereksinimleri", // Tier 1 Requirements
  zorunluluk: "SAHIP OLMALI - %100 zorunlu",
  bolumler: [
    {
      ad: "YAML Frontmatter",
      tespit_kaliplari: ["^---\\s*\\n.*?name:"],
      otomatik_uretim: true
    },
    {
      ad: "Overview",
      tespit_kaliplari: ["## Overview"],
      otomatik_uretim: true
    },
    {
      ad: "Core Principles",
      tespit_kaliplari: ["## Core Principles", "### Principle \\d"],
      otomatik_uretim: true
    },
    {
      ad: "When to Use",
      tespit_kaliplari: ["## When to Use", "\\*\\*Use When"],
      otomatik_uretim: true
    },
    {
      ad: "Main Workflow",
      tespit_kaliplari: ["## Workflow", "### Phase \\d", "### Step \\d"],
      otomatik_uretim: true
    }
  ]
} [ground:witnessed:tier-spec] [conf:0.95] [state:confirmed]

### S3.2 Katman 2: Gerekli (ZORUNLU - %100 hedef)

[define|neutral] TIER_2_REQUIREMENTS := {
  kural_adi: "Katman 2 Gereksinimleri", // Tier 2 Requirements
  zorunluluk: "ZORUNLU - %100 hedef",
  bolumler: [
    {
      ad: "Pattern Recognition",
      tespit_kaliplari: ["## .*Type Recognition", "## Pattern"],
      otomatik_uretim: true
    },
    {
      ad: "Advanced Techniques",
      tespit_kaliplari: ["## Advanced"],
      otomatik_uretim: true
    },
    {
      ad: "Anti-Patterns",
      tespit_kaliplari: ["## .*Anti-Pattern", "\\| Anti-Pattern"],
      otomatik_uretim: true
    },
    {
      ad: "Practical Guidelines",
      tespit_kaliplari: ["## Guidelines", "## Best Practices"],
      otomatik_uretim: true
    }
  ]
} [ground:witnessed:tier-spec] [conf:0.92] [state:confirmed]

### S3.3 Katman 3: Entegrasyon (ZORUNLU - %100 hedef)

[define|neutral] TIER_3_REQUIREMENTS := {
  kural_adi: "Katman 3 Gereksinimleri", // Tier 3 Requirements
  zorunluluk: "ZORUNLU - %100 hedef",
  bolumler: [
    {
      ad: "Cross-Skill Coordination",
      tespit_kaliplari: ["## Cross-Skill", "## Integration"],
      otomatik_uretim: true
    },
    {
      ad: "MCP Requirements",
      tespit_kaliplari: ["## MCP", "mcp_servers:"],
      otomatik_uretim: "kismi" // Partial
    },
    {
      ad: "Input/Output Contracts",
      tespit_kaliplari: ["input_contract:", "output_contract:"],
      otomatik_uretim: "sablon" // Template
    },
    {
      ad: "Recursive Improvement",
      tespit_kaliplari: ["## Recursive Improvement"],
      otomatik_uretim: true
    }
  ]
} [ground:witnessed:tier-spec] [conf:0.90] [state:confirmed]

### S3.4 Katman 4: Kapanis (ZORUNLU - %100 hedef)

[define|neutral] TIER_4_REQUIREMENTS := {
  kural_adi: "Katman 4 Gereksinimleri", // Tier 4 Requirements
  zorunluluk: "ZORUNLU - %100 hedef",
  bolumler: [
    {
      ad: "Examples",
      tespit_kaliplari: ["## Example"],
      otomatik_uretim: "sablon" // Template
    },
    {
      ad: "Troubleshooting",
      tespit_kaliplari: ["## Troubleshooting"],
      otomatik_uretim: true
    },
    {
      ad: "Conclusion",
      tespit_kaliplari: ["## Conclusion", "## Summary"],
      otomatik_uretim: true
    },
    {
      ad: "Completion Verification",
      tespit_kaliplari: ["## .*Completion", "- \\[ \\]"],
      otomatik_uretim: true
    }
  ]
} [ground:witnessed:tier-spec] [conf:0.90] [state:confirmed]

---

## S4 DENETIM ALGORITMASI CERCEVESI (Audit Algorithm Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_algorithm]] -->
<!-- [[MOR:root:A-L-G]] Algoritma = root for algorithm-procedure-method -->
<!-- [[COM:Denetim+Algoritma+Surec]] German: Audit-Algorithmus-Prozess -->

[define|neutral] AUDIT_ALGORITHM := {
  kural_adi: "Denetim Algoritmasi", // Audit Algorithm
  fonksiyon_adi: "auditSkill",
  giris: "skillPath",
  adimlar: [
    {
      sira: 1,
      ad: "Dosyayi oku",
      islem: "content = readFile(skillPath)"
    },
    {
      sira: 2,
      ad: "Sonuclari baslat",
      islem: "results = { tier1: {}, tier2: {}, tier3: {}, tier4: {}, missing: [] }"
    },
    {
      sira: 3,
      ad: "Her bolumu kontrol et",
      islem: "Her katman ve bolum icin: kalip eslestirmesi yap, sonuclara kaydet"
    },
    {
      sira: 4,
      ad: "Puanlari hesapla",
      islem: "tier1Score, tier2Score, overallScore hesapla"
    },
    {
      sira: 5,
      ad: "Durumu belirle",
      islem: "determineStatus(results)"
    }
  ],
  durum_belirleme: {
    COMPLETE: "tier1Score === 100 && tier2Score === 100",
    PARTIAL: "tier1Score >= 60 && tier2Score >= 50",
    INCOMPLETE: "diger tum durumlar"
  }
} [ground:witnessed:algorithm-design] [conf:0.88] [state:confirmed]

---

## S5 OTOMATIK URETIM SABLONLARI CERCEVESI (Auto-Generation Templates Frame)
<!-- [[HON:teineigo]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[CLS:ge_template]] -->
<!-- [[MOR:root:U-R-T]] Uretim = root for generate-produce-create -->
<!-- [[COM:Otomatik+Uretim+Sablon]] German: Automatische-Generierungs-Vorlage -->

### S5.1 Temel Ilkeler Sablonu (Core Principles Template)

[define|neutral] CORE_PRINCIPLES_AUTO_TEMPLATE := {
  kural_adi: "Temel Ilkeler Otomatik Sablonu", // Core Principles Auto Template
  yapi: {
    baslik: "## Core Principles",
    giris: "[Skill Name] operates on [N] fundamental principles:",
    ilke: {
      baslik: "### Principle [N]: [Domain-Specific Name]",
      aciklama: "[1-2 sentence explanation based on skill purpose]",
      pratik_baslik: "In practice:",
      pratik_maddeler: [
        "- [Practical application derived from skill workflow]",
        "- [Another practical application]"
      ]
    }
  }
} [ground:reported:template-design] [conf:0.85] [state:confirmed]

### S5.2 Anti-Kaliplar Sablonu (Anti-Patterns Template)

[define|neutral] ANTI_PATTERNS_AUTO_TEMPLATE := {
  kural_adi: "Anti-Kaliplar Otomatik Sablonu", // Anti-Patterns Auto Template
  yapi: {
    baslik: "## Common Anti-Patterns",
    tablo: {
      basliklar: ["Anti-Pattern", "Problem", "Solution"],
      satir_1: "**[Derived from skill domain]** | [Common mistake] | [How skill addresses it]",
      satir_2: "**[Another pattern]** | [What goes wrong] | [Correct approach]"
    }
  }
} [ground:reported:template-design] [conf:0.85] [state:confirmed]

### S5.3 Sonuc Sablonu (Conclusion Template)

[define|neutral] CONCLUSION_AUTO_TEMPLATE := {
  kural_adi: "Sonuc Otomatik Sablonu", // Conclusion Auto Template
  yapi: {
    baslik: "## Conclusion",
    paragraf_1: "[Skill Name] provides [core value proposition from Overview].",
    anahtar_cikarimlar_baslik: "Key takeaways:",
    anahtar_cikarimlar: [
      "- [Derived from Core Principles]",
      "- [Derived from Workflow]",
      "- [Derived from When to Use]"
    ],
    kapanish: "Use this skill when [When to Use summary]. Avoid [Anti-Pattern summary]."
  }
} [ground:reported:template-design] [conf:0.85] [state:confirmed]

---

## S6 ENTEGRASYON NOKTALARI CERCEVESI (Integration Points Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_integration]] -->
<!-- [[MOR:root:N-T-G]] Entegrasyon = root for integrate-combine-connect -->
<!-- [[COM:Entegrasyon+Nokta+Tanimlama]] German: Integrations-Punkt-Definition -->

### S6.1 skill-forge Faz 7a (Olusturma Sonrasi Denetim)

[define|neutral] PHASE_7A_INTEGRATION := {
  kural_adi: "Faz 7a Entegrasyonu", // Phase 7a Integration
  zamanlama: "Beceri olusturma sonrasi",
  adimlar: [
    "Katman uyum kontrolu calistir",
    "Sablonlari kullanarak eksik bolumleri uret",
    "Bolumleri uygun konumlara ekle",
    "TAMAMLANDI veya maksimum yinelemeye kadar yeniden dogrula"
  ]
} [ground:witnessed:integration-spec] [conf:0.90] [state:confirmed]

### S6.2 recursive-improvement (Toplu Denetim)

[define|neutral] RECURSIVE_IMPROVEMENT_INTEGRATION := {
  kural_adi: "Ozyineleme Iyilestirme Entegrasyonu", // Recursive Improvement Integration
  zamanlama: "Periyodik",
  adimlar: [
    "Plugin dizinindeki tum becerileri tara",
    "TAMAMLANMAMIS becerileri tespit et",
    "Onceliklendirme: kullanim sikligi > yas > kategori",
    "Iyilestirmeleri toplu olarak olustur",
    "Iyilestirme metriklerini Memory MCP'de izle"
  ]
} [ground:witnessed:integration-spec] [conf:0.88] [state:confirmed]

### S6.3 Komut ile Talep Uzerine

[define|neutral] ON_DEMAND_COMMANDS := {
  kural_adi: "Talep Uzerine Komutlar", // On-Demand Commands
  komutlar: [
    {
      ad: "/skill-audit [skill-name]",
      aciklama: "Tek beceri denetle"
    },
    {
      ad: "/skill-audit --all",
      aciklama: "Tum becerileri denetle"
    },
    {
      ad: "/skill-audit --fix",
      aciklama: "Denetle ve otomatik duzelt"
    },
    {
      ad: "/skill-audit --report",
      aciklama: "Tamamlanma raporu olustur"
    }
  ]
} [ground:witnessed:command-spec] [conf:0.90] [state:confirmed]

---

## S7 METRIK IZLEME CERCEVESI (Metrics Tracking Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:ge_metrics]] -->
<!-- [[MOR:root:M-T-R]] Metrik = root for metric-measure-indicator -->
<!-- [[COM:Metrik+Izleme+Depolama]] German: Metrik-Verfolgungs-Speicherung -->

[define|neutral] METRICS_TRACKING := {
  kural_adi: "Metrik Izleme", // Metrics Tracking
  bellek_namespace: "skill-audit/",
  mevcut_metrikler: {
    key: "skill-audit/metrics",
    alanlar: {
      total_skills: 180,
      complete: 1,
      partial: 22,
      incomplete: 157,
      avg_score: 36.5,
      last_audit: "2025-12-17T16:00:00Z",
      improvements_made: 0
    }
  },
  gecmis: {
    key: "skill-audit/history",
    kayit_formati: {
      date: "ISO tarih",
      before: {
        complete: "X",
        partial: "Y",
        incomplete: "Z"
      },
      after: {
        complete: "X'",
        partial: "Y'",
        incomplete: "Z'"
      },
      sections_added: "N"
    }
  }
} [ground:witnessed:metrics-design] [conf:0.88] [state:confirmed]

---

## S8 BASARI KRITERLERI CERCEVESI (Success Criteria Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_criteria]] -->
<!-- [[MOR:root:B-S-R]] Basari = root for success-achievement-victory -->
<!-- [[COM:Basari+Kriter+Hedef]] German: Erfolgs-Kriterien-Ziel -->

[define|neutral] SUCCESS_CRITERIA := {
  kural_adi: "Basari Kriterleri", // Success Criteria
  metrikler: [
    {
      ad: "Katman 1 uyumu",
      mevcut: "45%",
      hedef: "100%",
      zaman_dilimi: "Hemen"
    },
    {
      ad: "Katman 2 uyumu",
      mevcut: "20%",
      hedef: "100%",
      zaman_dilimi: "2 hafta"
    },
    {
      ad: "Katman 3 uyumu",
      mevcut: "35%",
      hedef: "80%",
      zaman_dilimi: "1 ay"
    },
    {
      ad: "Katman 4 uyumu",
      mevcut: "30%",
      hedef: "80%",
      zaman_dilimi: "1 ay"
    },
    {
      ad: "TAMAMLANDI becerileri",
      mevcut: 1,
      hedef: "50+",
      zaman_dilimi: "2 hafta"
    }
  ]
} [ground:witnessed:criteria-spec] [conf:0.85] [state:provisional]

---

## S9 UYGULAMA CERCEVESI (Enforcement Frame)
<!-- [[HON:sonkeigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:tiao_enforcement]] -->
<!-- [[MOR:root:U-Y-G]] Uygulama = root for enforce-apply-implement -->
<!-- [[COM:Uygulama+Zorlama+Mekanizma]] German: Durchsetzungs-Mechanismus -->

[define|neutral] ENFORCEMENT := {
  kural_adi: "Uygulama Mekanizmasi", // Enforcement Mechanism
  noktalar: [
    {
      konum: "skill-forge Faz 7a",
      kural: "Tum yeni beceriler denetimden gecmeli"
    },
    {
      konum: "recursive-improvement dongusu",
      kural: "Mevcut beceriler periyodik olarak denetlenir"
    },
    {
      konum: "CI/CD",
      kural: "PR dogrulamasi denetim kontrolu icerir"
    },
    {
      konum: "pre-commit hook",
      kural: "Istege bagli yerel uygulama"
    }
  ],
  kritik_kural: "Katman 1 uyumunda BASARISIZ olan beceriler uretim-hazir olarak ISARETLE NEMEZ"
} [ground:witnessed:enforcement-policy] [conf:0.92] [state:confirmed]

---

## S10 SONUC CERCEVESI (Conclusion Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_summary]] -->
<!-- [[MOR:root:S-N-C]] Sonuc = root for conclusion-result-end -->
<!-- [[COM:Sonuc+Ozet+Bildiri]] German: Schlussfolgerung-Zusammenfassung -->
Zaversheno. (Russian: Complete.)

[assert|confident] PROTOCOL_SUMMARY := {
  amac: "Otomatik beceri dokumantasyon denetimi ve iyilestirilmesi", // purpose
  metodoloji: "4-katmanli tespit kaliplari ile otomatik uretim", // methodology
  ciktilar: [
    "Katman uyum puanlari",
    "Otomatik bolum uretimi",
    "Metrik izleme",
    "Uygulama noktalari"
  ],
  tetikleyici: "Beceri konsolidasyonu denetimi %97 eksik bolum ortaya cikardi",
  kalite_kapilari: ["Faz 7a denetimi", "recursive-improvement dongusu", "CI/CD", "pre-commit hook"]
} [ground:witnessed:implementation] [conf:0.90] [state:confirmed]

---

*Promise: `<promise>SKILL_AUDIT_PROTOCOL_VCL_V3.1.1_COMPLIANT</promise>`*

</details>
