---
name: skill-forge-required-sections
description: Checklist of mandatory SKILL.md sections for Skill Forge
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: foundry/skill-forge
x-vcl-compliance: v3.1.1
---

### L1 Improvement
- Reorganized the required-sections guide into English-first SOP with actionable phases.
- Preserved the full v2.3 content in the appendix for section-by-section detail.
- Added explicit confidence ceiling guidance for compliance reports.

## STANDARD OPERATING PROCEDURE

### Purpose
Ensure every SKILL.md includes the mandatory sections defined in Skill Forge v2.3 and later.

### Trigger Conditions
- Before releasing or auditing any SKILL.md artifact.
- When updating templates or validating section completeness.

### Execution Phases
1. **Activate Evidential Frame**
   - Confirm version (2.3.0 reference) and enable evidence tracking.
2. **Review Mandatory Sections**
   - Purpose, triggers, inputs, execution phases, outputs, validation/quality gates, anti-patterns, integrations, MCP, hooks, and appendices.
   - Use the legacy appendix for exact wording and examples.
3. **Validate Completion**
   - Check each required section exists and is populated with actionable content.
   - Verify confidence ceilings and language requirements are followed.
4. **Record Findings**
   - Log any gaps, remediation steps, and alignments to the template.

### Output Format
- List of sections verified with pass/fail notes.
- Missing items and remediation plan.
- Confidence statement using ceiling syntax: `Confidence: X.XX (ceiling: TYPE Y.YY)` (ceilings: inference/report 0.70; research 0.85; observation/definition 0.95).

### Validation Checklist
- [ ] Evidential frame active; version noted.
- [ ] All mandatory sections present and populated.
- [ ] Confidence ceiling rules applied.
- [ ] Gaps logged with owners.
- [ ] Confidence statement included with explicit ceiling.

Confidence: 0.70 (ceiling: inference 0.70) - Required sections guide rewritten to English-first SOP while keeping full detail in the appendix.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

<details>
<summary>Legacy content (verbatim)</summary>

# Zorunlu SKILL.md Bolumleri (Required SKILL.md Sections) v2.3

<!-- VCL v3.1.1 COMPLIANT - L1 Internal Documentation -->
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_document]] -->

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

---

## S1 AMAC CERCEVESI (Purpose Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_purpose]] -->
<!-- [[MOR:root:Z-R-N]] Zorunlu = root morpheme for required-necessary-mandatory -->
<!-- [[COM:Zorunlu+Bolum+Tanim]] German: Pflicht-Abschnitt-Definition -->

[define|neutral] DOCUMENT_PURPOSE := {
  amac: "Her becerinin tamamlanmis sayilmasi icin ZORUNLU bolumleri tanimla", // purpose
  tetikleyici: "landing-page-generator v2.0 gelistirmesinde kesfedilen eksik bolumler",
  fayda: "Bu kontrol listesini takip etmek becerilerin bastan itibaren tam dokumante edilmesini saglar",
  surum: "2.3.0",
  son_guncelleme: "2025-12-17"
} [ground:witnessed:document-purpose] [conf:0.95] [state:confirmed]

---

## S2 BOLUM KATMANLARI CERCEVESI (Section Tiers Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_tier]] -->
<!-- [[MOR:root:K-T-M]] Katman = root for tier-layer-level -->
<!-- [[COM:Bolum+Katman+Siniflandirma]] German: Abschnitt-Stufen-Klassifizierung -->

### S2.1 Katman 1: Kritik (ZORUNLU)

[define|neutral] TIER_1_CRITICAL := {
  kural_adi: "Katman 1 - Kritik Bolumler", // Tier 1 - Critical Sections
  zorunluluk: "SAHIP OLMALI", // MUST HAVE
  bolumler: [
    {
      ad: "YAML Frontmatter",
      amac: "Kesfedilebilirlik, surum, tetikleyiciler",
      format: "---\\nname:\\nversion:\\ndescription:\\ntriggers:\\n---"
    },
    {
      ad: "Genel Bakis (Overview)",
      amac: "Felsefe, metodoloji, deger onerisi",
      format: "Becerinin NEDEN var oldugunu aciklayan 2-4 paragraf"
    },
    {
      ad: "Temel Ilkeler (Core Principles)",
      amac: "Temel calisma ilkeleri",
      format: "3-5 ilke, 'Pratikte:' maddeler ile"
    },
    {
      ad: "Ne Zaman Kullanilir (When to Use)",
      amac: "Net aktivasyon kriterleri",
      format: "'Kullan:' + 'Kullanma:' maddeleri"
    },
    {
      ad: "Ana Is Akisi (Main Workflow)",
      amac: "Temel prosedur",
      format: "Amac, Ajan, Giris/Cikis sozlesmeleri ile Fazlar"
    }
  ]
} [ground:witnessed:tier-spec] [conf:0.95] [state:confirmed]

### S2.2 Katman 2: Gerekli (ZORUNLU)

[define|neutral] TIER_2_ESSENTIAL := {
  kural_adi: "Katman 2 - Gerekli Bolumler", // Tier 2 - Essential Sections
  zorunluluk: "ZORUNLU", // REQUIRED
  bolumler: [
    {
      ad: "Kalip Tanima (Pattern Recognition)",
      amac: "Farkli giris tipleri/varyasyonlari",
      format: "Adlandirilmis kaliplar, ozellikler + anahtar odak"
    },
    {
      ad: "Ileri Teknikler (Advanced Techniques)",
      amac: "Sofistike yaklasimlar",
      format: "Hedef kitle optimizasyonu, coklu model, kenar durumlar"
    },
    {
      ad: "Yaygin Anti-Kaliplar (Common Anti-Patterns)",
      amac: "Kacinilmasi gerekenler",
      format: "Tablo: Anti-Kalip - Sorun - Cozum"
    },
    {
      ad: "Pratik Kilavuzlar (Practical Guidelines)",
      amac: "Karar rehberligi",
      format: "Tam vs hizli mod, kontrol noktalari, odunlesimler"
    }
  ]
} [ground:witnessed:tier-spec] [conf:0.92] [state:confirmed]

### S2.3 Katman 3: Entegrasyon (ZORUNLU)

[define|neutral] TIER_3_INTEGRATION := {
  kural_adi: "Katman 3 - Entegrasyon Bolumleri", // Tier 3 - Integration Sections
  zorunluluk: "ZORUNLU", // REQUIRED
  bolumler: [
    {
      ad: "Capraz-Beceri Koordinasyonu (Cross-Skill Coordination)",
      amac: "Ekosistem entegrasyonu",
      format: "Yukari/Asagi/Paralel beceriler"
    },
    {
      ad: "MCP Gereksinimleri (MCP Requirements)",
      amac: "Gerekce ile bagimliliklar",
      format: "Zorunlu/Istege bagli NEDEN aciklamalari ile"
    },
    {
      ad: "Giris/Cikis Sozlesmeleri (Input/Output Contracts)",
      amac: "Net arayuzler",
      format: "Zorunlu/istege bagli parametreler ile YAML"
    },
    {
      ad: "Ozyineleme Iyilestirme (Recursive Improvement)",
      amac: "Meta-dongu entegrasyonu",
      format: "Rol, eval harness, bellek isim alani"
    }
  ]
} [ground:witnessed:tier-spec] [conf:0.90] [state:confirmed]

### S2.4 Katman 4: Kapanış (ZORUNLU)

[define|neutral] TIER_4_CLOSURE := {
  kural_adi: "Katman 4 - Kapanis Bolumleri", // Tier 4 - Closure Sections
  zorunluluk: "ZORUNLU", // REQUIRED
  bolumler: [
    {
      ad: "Ornekler (Examples)",
      amac: "Somut kullanim",
      format: "Task() cagrilari ile 2-3 tam senaryo"
    },
    {
      ad: "Sorun Giderme (Troubleshooting)",
      amac: "Sorun cozumu",
      format: "Tablo: Sorun - Cozum"
    },
    {
      ad: "Sonuc (Conclusion)",
      amac: "Ozet ve cikarimlar",
      format: "Anahtar ilkeleri pekistiren 2-3 paragraf"
    },
    {
      ad: "Tamamlanma Dogrulamasi (Completion Verification)",
      amac: "Son kontrol listesi",
      format: "Tamamlanma kriterlerinin onay kutusu listesi"
    }
  ]
} [ground:witnessed:tier-spec] [conf:0.90] [state:confirmed]

---

## S3 FAZ 7 DOGRULAMA KONTROL LISTESI CERCEVESI (Phase 7 Validation Checklist Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:tiao_checklist]] -->
<!-- [[MOR:root:D-G-R]] Dogrulama = root for validate-verify-confirm -->
<!-- [[COM:Dogrulama+Kontrol+Liste]] German: Validierungs-Kontroll-Liste -->

[define|neutral] VALIDATION_CHECKLIST := {
  kural_adi: "Faz 7 Dogrulama Kontrol Listesi", // Phase 7 Validation Checklist
  aciklama: "Herhangi bir beceriyi TAMAMLANMIS saymadan once dogrula",
  kontroller: {
    katman_1: [
      "YAML frontmatter tam aciklama icerir (sadece ad degil)",
      "Genel Bakis felsefeyi ve metodolojiyi aciklar",
      "Temel Ilkeler bolumu pratik rehberlik ile 3-5 ilke icerir",
      "Ne Zaman Kullanilir net kullan/kullanma kriterleri icerir",
      "Ana Is Akisi sozlesmeler ile detayli fazlar icerir"
    ],
    katman_2: [
      "Kalip Tanima farkli giris tiplerini kapsar",
      "Ileri Teknikler sofistike yaklasimlar icerir",
      "Yaygin Anti-Kaliplar sorun-cozum tablolari icerir",
      "Pratik Kilavuzlar karar rehberleri icerir"
    ],
    katman_3: [
      "Capraz-Beceri Koordinasyonu ekosistem entegrasyonunu dokumante eder",
      "MCP Gereksinimleri her birinin NEDEN gerekli oldugunu aciklar",
      "Giris/Cikis Sozlesmeleri YAML'da net sekilde belirtilir",
      "Ozyineleme Iyilestirme Entegrasyonu dokumante edilir"
    ],
    katman_4: [
      "Ornekler 2-3 somut senaryo icerir",
      "Sorun Giderme yaygin sorunlari ele alir",
      "Sonuc beceri degerini ozetler",
      "Tamamlanma Dogrulamasi kontrol listesi mevcut"
    ]
  }
} [ground:witnessed:checklist-spec] [conf:0.92] [state:confirmed]

---

## S4 ORNEK BOLUM SABLONLARI CERCEVESI (Example Section Templates Frame)
<!-- [[HON:teineigo]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[CLS:ge_template]] -->
<!-- [[MOR:root:S-B-L]] Sablon = root for template-pattern-model -->
<!-- [[COM:Ornek+Bolum+Sablon]] German: Beispiel-Abschnitt-Vorlage -->

### S4.1 Temel Ilkeler Sablonu (Core Principles Template)

[define|neutral] CORE_PRINCIPLES_TEMPLATE := {
  kural_adi: "Temel Ilkeler Sablonu", // Core Principles Template
  yapi: {
    baslik: "## Temel Ilkeler",
    giris: "[Beceri Adi] [N] temel ilke uzerinde calisir:",
    ilke_formati: {
      baslik: "### Ilke [N]: [Ilke Adi]",
      aciklama: "[Ilkenin 1-2 cumleli aciklamasi]",
      pratik_baslik: "Pratikte:",
      pratik_maddeler: [
        "- [Pratik uygulama 1]",
        "- [Pratik uygulama 2]",
        "- [Pratik uygulama 3]"
      ]
    }
  }
} [ground:reported:template-design] [conf:0.85] [state:confirmed]

### S4.2 Kalip Tanima Sablonu (Pattern Recognition Template)

[define|neutral] PATTERN_RECOGNITION_TEMPLATE := {
  kural_adi: "Kalip Tanima Sablonu", // Pattern Recognition Template
  yapi: {
    baslik: "## [Alan] Tip Tanima",
    giris: "Farkli [giris tipleri] farkli yaklasimlar gerektirir:",
    kalip_formati: {
      baslik: "### [Kalip Adi]",
      kaliplar: "**Kaliplar**: '[tetikleyici kelime 1]', '[tetikleyici kelime 2]'",
      ozellikler_baslik: "**Yaygin ozellikler**:",
      ozellikler: ["- [Ozellik 1]", "- [Ozellik 2]"],
      odak_baslik: "**Anahtar odak**:",
      odak: "- [Bu kalip icin nelere odaklanilmali]",
      yaklasim: "**Yaklasim**: [Kullanilacak cerceve veya metodoloji]"
    }
  }
} [ground:reported:template-design] [conf:0.85] [state:confirmed]

### S4.3 Anti-Kaliplar Sablonu (Anti-Patterns Template)

[define|neutral] ANTI_PATTERNS_TEMPLATE := {
  kural_adi: "Anti-Kaliplar Sablonu", // Anti-Patterns Template
  yapi: {
    baslik: "## Yaygin Anti-Kaliplar",
    giris: "Bu yaygin hatalardan kacinin:",
    kategori_baslik: "### [Kategori] Anti-Kaliplari",
    tablo: {
      basliklar: ["Anti-Kalip", "Sorun", "Cozum"],
      satir_formati: "| **[Ad]** | [Ne yanlis gidiyor] | [Nasil duzeltilir] |"
    }
  }
} [ground:reported:template-design] [conf:0.85] [state:confirmed]

### S4.4 Capraz-Beceri Koordinasyonu Sablonu (Cross-Skill Coordination Template)

[define|neutral] CROSS_SKILL_TEMPLATE := {
  kural_adi: "Capraz-Beceri Koordinasyonu Sablonu", // Cross-Skill Coordination Template
  yapi: {
    baslik: "## Capraz-Beceri Koordinasyonu",
    giris: "[Beceri Adi] ekosistemdeki diger becerilerle calisir:",
    alt_bolumler: [
      {
        baslik: "### Yukari Akis Becerileri (giris saglar)",
        tablo_basliklar: ["Beceri", "Ne Zaman Once Kullanilir", "Ne Saglar"]
      },
      {
        baslik: "### Asagi Akis Becerileri (ciktiyi kullanir)",
        tablo_basliklar: ["Beceri", "Ne Zaman Sonra Kullanilir", "Ne Yapar"]
      },
      {
        baslik: "### Paralel Beceriler (birlikte calisir)",
        tablo_basliklar: ["Beceri", "Ne Zaman Birlikte Calistirilir", "Nasil Koordine Olurlar"]
      }
    ]
  }
} [ground:reported:template-design] [conf:0.85] [state:confirmed]

---

## S5 KALITE STANDARTLARI CERCEVESI (Quality Standards Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:tiao_standard]] -->
<!-- [[MOR:root:K-L-T]] Kalite = root for quality-value-standard -->
<!-- [[COM:Kalite+Standart+Tablo]] German: Qualitats-Standard-Tabelle -->

[define|neutral] QUALITY_STANDARDS := {
  kural_adi: "Kalite Standartlari", // Quality Standards
  metrikler: [
    {
      ad: "Katman 1 bolumleri",
      minimum: "100%",
      hedef: "100%"
    },
    {
      ad: "Katman 2 bolumleri",
      minimum: "100%",
      hedef: "100%"
    },
    {
      ad: "Katman 3 bolumleri",
      minimum: "100%",
      hedef: "100%"
    },
    {
      ad: "Katman 4 bolumleri",
      minimum: "100%",
      hedef: "100%"
    },
    {
      ad: "Temel Ilkeler",
      minimum: 3,
      hedef: 5
    },
    {
      ad: "Kalip Tipleri",
      minimum: 2,
      hedef: "4-6"
    },
    {
      ad: "Anti-Kalip Tablolari",
      minimum: 1,
      hedef: "3-4"
    },
    {
      ad: "Ornekler",
      minimum: 2,
      hedef: 3
    }
  ],
  uyari: "Herhangi bir Katman 1 veya Katman 2 bolumu EKSIK olan beceriler TAMAMLANMAMISTIR ve gelistirilmelidir"
} [ground:witnessed:quality-spec] [conf:0.92] [state:confirmed]

---

## S6 UYGULAMA CERCEVESI (Enforcement Frame)
<!-- [[HON:sonkeigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:tiao_enforcement]] -->
<!-- [[MOR:root:U-Y-G]] Uygulama = root for enforce-apply-implement -->
<!-- [[COM:Uygulama+Zorlama+Mekanizma]] German: Durchsetzungs-Mechanismus -->

[define|neutral] ENFORCEMENT_POINTS := {
  kural_adi: "Uygulama Noktalari", // Enforcement Points
  noktalar: [
    {
      konum: "Faz 7 Dogrulama",
      aciklama: "Skill-forge tum bolumleri kontrol eder"
    },
    {
      konum: "Beceri Denetcisi",
      aciklama: "Mevcut becerileri tamamlanma icin denetler"
    },
    {
      konum: "CI/CD",
      aciklama: "Birlestirmeden once otomatik dogrulama"
    }
  ],
  kural: "Skill-forge bir beceri olusturduğunda, TUM bolumleri URETMELI. Zaman kisitliysa, yinelemeli olarak doldurulabilecek TODO isaretleyicileri ile iskelet bolumler olustur"
} [ground:witnessed:enforcement-policy] [conf:0.90] [state:confirmed]

---

## S7 SONUC CERCEVESI (Conclusion Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_summary]] -->
<!-- [[MOR:root:S-N-C]] Sonuc = root for conclusion-result-end -->
<!-- [[COM:Sonuc+Ozet+Bildiri]] German: Schlussfolgerung-Zusammenfassung -->
Zaversheno. (Russian: Complete.)

[assert|confident] DOCUMENT_SUMMARY := {
  amac: "Beceri tamamlamasi icin zorunlu bolum gereksinimleri", // purpose
  metodoloji: "4-katmanli hiyerarsik bolum yapisi", // methodology
  ciktilar: [
    "Katman 1: Kritik bolumler (YAML, Genel Bakis, Ilkeler, Kullanim, Is Akisi)",
    "Katman 2: Gerekli bolumler (Kaliplar, Teknikler, Anti-Kaliplar, Kilavuzlar)",
    "Katman 3: Entegrasyon bolumleri (Koordinasyon, MCP, Sozlesmeler, Iyilestirme)",
    "Katman 4: Kapanis bolumleri (Ornekler, Sorun Giderme, Sonuc, Dogrulama)"
  ],
  kalite_kapilari: ["Faz 7 Dogrulama", "Beceri Denetcisi", "CI/CD"]
} [ground:witnessed:implementation] [conf:0.92] [state:confirmed]

---

*Promise: `<promise>REQUIRED_SECTIONS_VCL_V3.1.1_COMPLIANT</promise>`*

</details>
