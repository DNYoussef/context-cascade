---
name: skill-forge-readme
description: Overview and quick start for the universal Skill Forge template
allowed-tools: [Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite]
model: claude-3-5-sonnet
x-version: 3.2.0
x-category: foundry/skill-forge
x-vcl-compliance: v3.1.1
---

### L1 Improvement
- Reframed the README into an English-first SOP while preserving the evidential frame and MECE structure rules in the appendix.
- Clarified mandatory vs. optional directories and files to align with the structure-first guardrail.
- Added an explicit confidence requirement to comply with the confidence ceiling rule.

## STANDARD OPERATING PROCEDURE

### Purpose
Provide an actionable overview and quick start for creating or consuming Skill Forge packages using the universal MECE-aligned template.

### Trigger Conditions
- Use this guide when orienting new contributors to Skill Forge or when preparing to create/validate a new skill package.
- Defer to `SKILL.md` for detailed execution mechanics and to `SKILL-AUDIT-PROTOCOL.md` for audits.

### Execution Phases
1. **Activate Evidential Frame**
   - Confirm you are using Skill Forge v3.2.0 artifacts and that source verification is on.
   - Capture the intent of the skill and any constraints from the requester.
2. **Review Meta Definition**
   - Restate the template’s goal: produce production-quality Claude Code skills via MECE organization.
   - Note the universal requirement: every new skill must follow this structure.
3. **Apply Universal Structure**
   - Required files: `SKILL.md` (imperative guidance) and `README.md` (overview & quick start).
   - Required directories: `examples/` (at least one example).
   - Recommended directories: `references/`, `resources/scripts/`, `resources/templates/`, `resources/assets/`, `graphviz/`, `tests/`.
   - For each directory, list planned contents and fill gaps before delivery.
4. **Quick Start Actions**
   - For skill creators: read `SKILL.md`, study `examples/`, and instantiate the prescribed structure.
   - For skill users: read this README, then review `examples/`, then `references/` for depth.
5. **Validation & Handoff**
   - Verify structure completeness, note any deviations, and document follow-ups.
   - Summarize the structure, quick-start pointers, and open items.

### Output Format
- Summary of intent and version context.
- Enumerated mandatory files/directories and their planned contents.
- Quick-start steps for creators and users.
- Open risks or missing items with owners.
- Confidence statement using ceiling syntax: `Confidence: X.XX (ceiling: TYPE Y.YY)` (ceilings: inference/report 0.70; research 0.85; observation/definition 0.95).

### Validation Checklist
- [ ] Version and evidential frame confirmed.
- [ ] Required files and directories accounted for.
- [ ] Quick-start steps documented for creators and users.
- [ ] Deviations and risks captured with owners.
- [ ] Confidence statement included with explicit ceiling.

Confidence: 0.70 (ceiling: inference 0.70) - English-first rewrite retains the evidential frame, MECE structure, and quick-start guidance.

---

## VCL COMPLIANCE APPENDIX (Internal Reference)

- Legacy VCL markers and definitions are retained below for internal use. User-facing content must remain pure English.

<details>
<summary>Legacy content (verbatim)</summary>

# Skill Forge - Evrensel Beceri Olusturma Sablonu (Universal Skill Creation Template)

<!-- VCL v3.1.1 COMPLIANT - L1 Internal Documentation -->
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_document]] -->

## Kanitsal Cerceve (Evidential Frame Activation)
Kaynak dogrulama modu etkin.

---

## S1 META BILGI CERCEVESI (Meta Information Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_metadata]] -->
<!-- [[MOR:root:B-C-R]] Beceri = root morpheme for skill-ability-capability -->
<!-- [[COM:Evrensel+Beceri+Sablon]] German: Universelle-Skill-Vorlage -->

[define|neutral] README_META := {
  surum: "3.0.0", // version
  tanim: "MECE-Yapilandirilmis Evrensel Sablon", // MECE-Structured Universal Template
  amac: "Sistematik MECE organizasyonu ile uretim-kalitesinde Claude Code becerileri olustur"
} [ground:witnessed:meta-definition] [conf:0.95] [state:confirmed]

---

## S2 SKILL FORGE NEDIR CERCEVESI (What This Is Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_definition]] -->
<!-- [[MOR:root:N-D-R]] Nedir = root for what-is-definition-essence -->
<!-- [[COM:Skill+Forge+Tanim]] German: Skill-Forge-Definition -->

[define|neutral] SKILL_FORGE_DEFINITION := {
  kural_adi: "Skill Forge Nedir", // What is Skill Forge
  aciklama: "Hem bir beceri olusturma metodolojisi hem de TUM gelecek Claude Code becerilerini organize etmek icin evrensel bir sablon",
  anahtar_ozellik: "Olusturduggunuz her beceri bu MECE (Karsilikli Disarida, Topluca Kapsamli) yapisini takip etmelidir"
} [ground:witnessed:definition] [conf:0.92] [state:confirmed]

---

## S3 EVRENSEL BECERI YAPISI CERCEVESI (Universal Skill Structure Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_structure]] -->
<!-- [[MOR:root:Y-P-S]] Yapi = root for structure-build-form -->
<!-- [[COM:MECE+Yapi+Organizasyon]] German: MECE-Struktur-Organisation -->
<!-- [[SPC:kuzey]] Primary organization direction -->

[define|neutral] UNIVERSAL_STRUCTURE := {
  kural_adi: "Evrensel Beceri Yapisi (MECE)", // Universal Skill Structure
  dizin_agaci: {
    root: "{skill-name}/",
    zorunlu_dosyalar: [
      {
        ad: "skill.md",
        gereklilik: "ZORUNLU",
        aciklama: "Emir kipi talimatlari"
      },
      {
        ad: "README.md",
        gereklilik: "ZORUNLU",
        aciklama: "Genel bakis ve hizli baslangic"
      }
    ],
    zorunlu_dizinler: [
      {
        ad: "examples/",
        gereklilik: "ZORUNLU (en az 1)",
        icindekiler: ["example-1-basic.md", "example-2-advanced.md", "example-3-edge-case.md"]
      }
    ],
    istege_bagli_dizinler: [
      {
        ad: "references/",
        aciklama: "Destekleyici dokumanlar",
        icindekiler: ["best-practices.md", "api-reference.md", "troubleshooting.md"]
      },
      {
        ad: "resources/scripts/",
        aciklama: "Calistirilabilir yardimcilar",
        icindekiler: ["validate.py", "deploy.sh"]
      },
      {
        ad: "resources/templates/",
        aciklama: "Hazir sablonlar",
        icindekiler: ["template.yaml"]
      },
      {
        ad: "resources/assets/",
        aciklama: "Statik kaynaklar",
        icindekiler: ["diagram.png"]
      },
      {
        ad: "graphviz/",
        aciklama: "Surec diyagramlari",
        icindekiler: ["workflow.dot", "architecture.dot"]
      },
      {
        ad: "tests/",
        aciklama: "Dogrulama testleri",
        icindekiler: ["test-basic.md", "test-integration.md"]
      }
    ]
  }
} [ground:witnessed:structure-design] [conf:0.92] [state:confirmed]

---

## S4 HIZLI BASLANGIC CERCEVESI (Quick Start Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:ge_quickstart]] -->
<!-- [[MOR:root:H-Z-L]] Hizli = root for quick-fast-rapid -->
<!-- [[COM:Hizli+Baslangic+Rehber]] German: Schnell-Start-Anleitung -->

[define|neutral] QUICK_START := {
  kural_adi: "Hizli Baslangic", // Quick Start
  beceri_olusturucular_icin: [
    "skill.md'yi tam metodoloji icin oku",
    "Farkli beceri tipleri icin examples/ klasorunu incele",
    "Tum yeni beceriler icin bu yapiyi kullan"
  ],
  beceri_kullanicilar_icin: [
    "Genel bakis icin README.md'yi oku",
    "Kullanim kaliplari icin examples/ klasorunu kontrol et",
    "Detayli bilgi icin references/ klasoruna bak"
  ]
} [ground:witnessed:quickstart-design] [conf:0.90] [state:confirmed]

</details>

---

## S5 DOSYA AMACLARI CERCEVESI (File Purposes Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:tiao_purpose]] -->
<!-- [[MOR:root:A-M-C]] Amac = root for purpose-goal-objective -->
<!-- [[COM:Dosya+Amac+Tablo]] German: Datei-Zweck-Tabelle -->

### S5.1 Temel Dosyalar (Karsilikli Disarida)

[define|neutral] CORE_FILES := {
  kural_adi: "Temel Dosyalar", // Core Files
  ilke: "Karsilikli Disarida", // Mutually Exclusive
  dosyalar: [
    {
      dosya: "skill.md",
      amac: "Claude icin emir kipi talimatlari",
      gereklilik: "ZORUNLU"
    },
    {
      dosya: "README.md",
      amac: "Insan-okunabilir genel bakis ve navigasyon",
      gereklilik: "ZORUNLU"
    }
  ]
} [ground:witnessed:file-spec] [conf:0.95] [state:confirmed]

### S5.2 Destekleyici Dizinler (Topluca Kapsamli)

[define|neutral] SUPPORTING_DIRECTORIES := {
  kural_adi: "Destekleyici Dizinler", // Supporting Directories
  ilke: "Topluca Kapsamli", // Collectively Exhaustive
  dizinler: [
    {
      dizin: "examples/",
      icerik_tipi: "Somut kullanim senaryolari",
      ne_zaman_dahil_et: "HER ZAMAN (en az 1)"
    },
    {
      dizin: "references/",
      icerik_tipi: "Soyut dokumantasyon",
      ne_zaman_dahil_et: "Karmasik beceriler icin"
    },
    {
      dizin: "resources/scripts/",
      icerik_tipi: "Calistirilabilir kod",
      ne_zaman_dahil_et: "Otomasyon gerektiginde"
    },
    {
      dizin: "resources/templates/",
      icerik_tipi: "Hazir sablonlar",
      ne_zaman_dahil_et: "Yeniden kullanilabilir kaliplar oldugunda"
    },
    {
      dizin: "resources/assets/",
      icerik_tipi: "Statik dosyalar",
      ne_zaman_dahil_et: "Gorsel/yapilandirma varliklarinda"
    },
    {
      dizin: "graphviz/",
      icerik_tipi: "Surec diyagramlari",
      ne_zaman_dahil_et: "Karmasik is akislari icin"
    },
    {
      dizin: "tests/",
      icerik_tipi: "Dogrulama test vakalari",
      ne_zaman_dahil_et: "Uretim becerileri icin"
    }
  ]
} [ground:witnessed:directory-spec] [conf:0.92] [state:confirmed]

---

## S6 BECERI OLUSTURMA FAZLARI CERCEVESI (Skill Creation Phases Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:tiao_phase]] -->
<!-- [[MOR:root:F-Z]] Faz = root for phase-stage-step -->
<!-- [[COM:Beceri+Olusturma+Faz]] German: Skill-Erstellungs-Phase -->

[define|neutral] CREATION_PHASES := {
  kural_adi: "Beceri Olusturma Fazlari", // Skill Creation Phases
  fazlar: [
    {
      numara: 1,
      ad: "Niyet Analizi",
      sure: "10-15 dakika",
      aciklama: "GERCEK ihtiyaci ve baglami anla"
    },
    {
      numara: 2,
      ad: "Kullanim Senaryosu Tasarimi",
      sure: "10-15 dakika",
      aciklama: "3-5 somut ornek olustur"
    },
    {
      numara: 3,
      ad: "Yapi Karari",
      sure: "15-20 dakika",
      aciklama: "Beceri tipini sec: mikro/ajan/orkestrasyon"
    },
    {
      numara: 4,
      ad: "Icerik Olusturma",
      sure: "20-30 dakika",
      aciklama: "Emir kipi ile skill.md yaz"
    },
    {
      numara: 5,
      ad: "Kaynak Gelistirme",
      sure: "20-40 dakika",
      aciklama: "Scriptler, sablonlar, referanslar olustur"
    },
    {
      numara: 6,
      ad: "Dokumantasyon",
      sure: "15-25 dakika",
      aciklama: "README, ornekler, referanslar yaz"
    },
    {
      numara: 7,
      ad: "Dogrulama",
      sure: "10-15 dakika",
      aciklama: "Test et ve kaliteyi incele"
    }
  ],
  toplam_sure: "1.5-2.5 saat uretim-hazir beceri icin"
} [ground:witnessed:phase-design] [conf:0.90] [state:confirmed]

---

## S7 KALITE STANDARTLARI CERCEVESI (Quality Standards Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:tiao_standard]] -->
<!-- [[MOR:root:K-L-T]] Kalite = root for quality-value-standard -->
<!-- [[COM:Kalite+Standart+Seviye]] German: Qualitats-Standard-Stufe -->

[define|neutral] QUALITY_TIERS := {
  kural_adi: "Kalite Seviyeleri", // Quality Tiers
  seviyeler: [
    {
      ad: "Bronz (Minimum Uygulanabilir)",
      gereksinimler: [
        "skill.md + README.md",
        "1 ornek"
      ],
      toplam_dosya: 3
    },
    {
      ad: "Gumus (Uretim Hazir)",
      gereksinimler: [
        "Tum Bronz gereksinimleri",
        "3 ornek",
        "references/ klasoru",
        "1 GraphViz diyagrami"
      ],
      toplam_dosya: "7+"
    },
    {
      ad: "Altin (Kurumsal Seviye)",
      gereksinimler: [
        "Tum Gumus gereksinimleri",
        "resources/scripts/",
        "resources/templates/",
        "tests/ klasoru"
      ],
      toplam_dosya: "12+"
    },
    {
      ad: "Platin (En Iyi Sinif)",
      gereksinimler: [
        "Tum Altin gereksinimleri",
        "Kapsamli references/",
        "Tam test kapsami",
        "Birden fazla diyagram"
      ],
      toplam_dosya: "20+"
    }
  ]
} [ground:witnessed:quality-spec] [conf:0.90] [state:confirmed]

---

## S8 MEVCUT KAYNAKLAR CERCEVESI (Available Resources Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[CLS:ge_resource]] -->
<!-- [[MOR:root:K-Y-N]] Kaynak = root for resource-source-origin -->
<!-- [[COM:Mevcut+Kaynak+Script]] German: Verfugbare-Ressourcen-Skript -->

### S8.1 Dogrulama Scripti (Validation Script)

[define|neutral] VALIDATION_SCRIPT := {
  kural_adi: "Dogrulama Scripti", // Validation Script
  komut: "python resources/scripts/validate_skill.py ~/path/to/skill",
  kontroller: [
    "YAML frontmatter formati",
    "Zorunlu dosyalar mevcut",
    "Dizin yapisi",
    "Emir kipi kullanimi"
  ]
} [ground:witnessed:script-spec] [conf:0.88] [state:confirmed]

### S8.2 Paketleme Scripti (Packaging Script)

[define|neutral] PACKAGING_SCRIPT := {
  kural_adi: "Paketleme Scripti", // Packaging Script
  komut: "python resources/scripts/package_skill.py ~/path/to/skill",
  olusturur: [
    "Zaman damgali .zip dosyasi",
    "Uygun dizin yapisi",
    "Kurulum talimatlari"
  ]
} [ground:witnessed:script-spec] [conf:0.88] [state:confirmed]

---

## S9 TASARIM ILKELERI CERCEVESI (Design Principles Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:tiao_principle]] -->
<!-- [[MOR:root:I-L-K]] Ilke = root for principle-rule-foundation -->
<!-- [[COM:Tasarim+Ilke+Temel]] German: Design-Prinzip-Grundlage -->

[define|neutral] DESIGN_PRINCIPLES := {
  kural_adi: "Tasarim Ilkeleri", // Design Principles
  ilkeler: [
    {
      numara: 1,
      ad: "MECE Organizasyonu",
      karsilikli_disarida: "Dizinler arasinda cakisma yok",
      topluca_kapsamli: "Tum icerigin bir yeri var"
    },
    {
      numara: 2,
      ad: "Asama Asama Acilim",
      aciklama: [
        "Metadata: Hizli tetikleyici anlayisi",
        "README: Baglam ve navigasyon",
        "skill.md: Tam talimatlar",
        "Resources: Derinlemesine materyaller"
      ]
    },
    {
      numara: 3,
      ad: "Emir Kipi",
      dogru: "Veriyi analiz et",
      yanlis: "Veriyi analiz etmelisiniz"
    },
    {
      numara: 4,
      ad: "Somut Ornekler",
      kural: "Her beceri en az 1 gercek kullanim ornegi ICERMELI"
    },
    {
      numara: 5,
      ad: "Bilesebilirlik",
      aciklama: [
        "Standart bellek isim alanlari",
        "Ajan koordinasyon protokolleri",
        "Tutarli dosya yapilari"
      ]
    }
  ]
} [ground:witnessed:principle-design] [conf:0.92] [state:confirmed]

---

## S10 SURUM GECMISI CERCEVESI (Version History Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_history]] -->
<!-- [[MOR:root:S-R-M]] Surum = root for version-edition-release -->
<!-- [[COM:Surum+Gecmis+Kayit]] German: Versions-Verlauf-Eintrag -->

[define|neutral] VERSION_HISTORY := {
  kural_adi: "Surum Gecmisi", // Version History
  surumler: [
    {
      surum: "v3.0.0",
      tarih: "2025-11-02",
      aciklama: "MECE Evrensel Sablon",
      degisiklikler: [
        "MECE ilkeleri kullanarak tam yeniden yapi",
        "TUM beceriler icin evrensel sablon",
        "examples/ gereksinimleri eklendi",
        "resources/ alt dizinlere organize edildi",
        "graphviz/ ve tests/ dizinleri eklendi"
      ]
    },
    {
      surum: "v2.0.0",
      tarih: "2025-10-29",
      aciklama: "SOP Gelistirmesi",
      degisiklikler: [
        "Acik ajan orkestrasyonu",
        "Bellek-tabanli koordinasyon",
        "Kanit-temelli prompt"
      ]
    },
    {
      surum: "v1.0.0",
      tarih: "Orijinal",
      aciklama: "Orijinal",
      degisiklikler: [
        "7-faz metodolojisi",
        "Asama asama acilim tasarimi"
      ]
    }
  ]
} [ground:witnessed:version-history] [conf:0.95] [state:confirmed]

---

## S11 FELSEFE CERCEVESI (Philosophy Frame)
<!-- [[HON:sonkeigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_philosophy]] -->
<!-- [[MOR:root:F-L-S]] Felsefe = root for philosophy-wisdom-thought -->
<!-- [[COM:Beceri+Felsefe+Vizyon]] German: Skill-Philosophie-Vision -->

[assert|confident] PHILOSOPHY := {
  kural_adi: "Skill Forge Felsefesi", // Skill Forge Philosophy
  vizyon: "Beceriler sadece sablonlar degildir - uzmanligi kodlayan, yetenekleri etkinlestiren ve ekosisteme sorunsuzca entegre olan stratejik tasarimlardir",
  sagladiklari: [
    "MECE yapisi ile sistematik kalite",
    "Sablonlar ile tekrarlanabilir mukemmellik",
    "Dogrulama ile surekli iyilestirme",
    "Standartlar ile ekosistem entegrasyonu"
  ]
} [ground:witnessed:philosophy-design] [conf:0.90] [state:confirmed]

---

## S12 BASLANGIC CERCEVESI (Get Started Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_start]] -->
<!-- [[MOR:root:B-S-L]] Basla = root for start-begin-initiate -->
<!-- [[COM:Baslangic+Adim+Rehber]] German: Start-Schritt-Anleitung -->

[define|neutral] GET_STARTED := {
  kural_adi: "Baslayin", // Get Started
  adimlar: [
    {
      numara: 1,
      aciklama: "Metodolojiyi calis",
      komut: "cat skill.md"
    },
    {
      numara: 2,
      aciklama: "Ornekleri incele",
      komut: "ls examples/"
    },
    {
      numara: 3,
      aciklama: "Bu sablonu kullanarak becerinizi olusturun",
      komut: "cp -r skill-forge/ ../my-new-skill/"
    }
  ],
  sonraki: "skill.md dosyasini acin ve olusturmaya baslayin!"
} [ground:witnessed:start-guide] [conf:0.90] [state:confirmed]

---

## S13 SONUC CERCEVESI (Conclusion Frame)
<!-- [[HON:teineigo]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[CLS:ge_summary]] -->
<!-- [[MOR:root:S-N-C]] Sonuc = root for conclusion-result-end -->
<!-- [[COM:Sonuc+Ozet+Bildiri]] German: Schlussfolgerung-Zusammenfassung -->
Zaversheno. (Russian: Complete.)

[assert|confident] README_SUMMARY := {
  amac: "Claude Code becerileri icin evrensel olusturma sablonu", // purpose
  metodoloji: "MECE-yapilandirilmis 7-fazli beceri olusturma", // methodology
  ciktilar: [
    "skill.md + README.md temel dosyalar",
    "Zorunlu examples/ dizini",
    "Istege bagli references/, resources/, graphviz/, tests/",
    "4-seviyeli kalite standartlari (Bronz -> Platin)"
  ],
  anahtar_ilkeler: ["MECE Organizasyonu", "Asama Asama Acilim", "Emir Kipi", "Somut Ornekler", "Bilesebilirlik"]
} [ground:witnessed:implementation] [conf:0.92] [state:confirmed]

---

*Promise: `<promise>README_VCL_V3.1.1_COMPLIANT</promise>`*
