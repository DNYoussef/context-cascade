---
name: skill-forge
description: Meta-beceri dokumasi icin VCL verix kreol
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

[[HON:teineigo]] [[MOR:root:S-K-L]] [[COM:Skill+Schmiede+Meta]] [[CLS:ge_meta_skill]] [[EVD:-DI<tanim>]] [[ASP:nesov.]] [[SPC:path:/skills/foundry/skill-forge]]
[assert|neutral] “Skill-Forge” kendi kendini dokuyan meta-beceri; trilateral kök S-K-L + F-R-G + I-M-P ile yapisal dokumayi zorunlu kilar. [ground:SKILL.md] [conf:0.89] [state:confirmed]

[[HON:teineigo]] [[MOR:root:T-R-G]] [[COM:Trigger+Router]] [[CLS:ge_condition]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:routing]]
[define|neutral] TETIK := pozitif {create skill, optimize skill, adversarial validation}; negatif {micro-skill-creator, agent-creator, prompt-architect}. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:M-R-F]] [[COM:Morph+Inventar]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:axis:MOR]]
[define|neutral] MOR_DECOMP := skill=root:S-K-L; forge=root:F-R-G; create=root:C-R-T; improve=root:I-M-P; kökler semantik iskelet saglar. [ground:SKILL.md] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:K-M-P]] [[COM:Deutsch+Kompositum]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:axis:COM]]
[define|neutral] COM_COMPOSE := SkillForge=Skill+Forge; MetaSkill=Meta+Skill; SelfImproving=Selbst+Verbesserung; DogfoodingLoop=Dogfooding+Schleife. [ground:SKILL.md] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-L-S]] [[COM:Classifier+Mapping]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:axis:CLS]]
[define|neutral] CLS := ge_meta_skill, yi_ge, zhong_foundry, ceng_san; seviye ve kategori sayaci. [ground:SKILL.md] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:E-P-S]] [[COM:Kanit+Ceiling+Guard]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:EVD]]
[direct|emphatic] EVD := -DI/-mis/-dir zorunlu; guven tavani ayni set {0.70/0.85/0.90/0.95}; ASP>=1, EVD>=1 degismez. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:A-S-P]] [[COM:Aspekt+Dual]] [[CLS:ge_slot]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:ASP]]
[define|neutral] ASP := nesov. surekli iyilestirme; sov. gorev tamam; iyilestirme dongusu nesov. kalir. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-P-C]] [[COM:Koordinat+Path]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:downstream:/skills]]
[define|neutral] SPC := canonical_path “/skills/foundry/skill-forge”; outputs_to “/skills/{kategori}/{isim}”; parallel agent-creator. [ground:SKILL.md] [conf:0.80] [state:confirmed]

[[HON:teineigo]] [[MOR:root:Y-P-I]] [[COM:Struktur+Vortritt]] [[CLS:ge_principle]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:principles]]
[define|neutral] ILKE_P1 := yapı-oncelikli tasarim; SKILL.md + examples/ + tests/ zorunlu; resources/, references/ önerilir. [ground:SKILL.md] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:D-S-M]] [[COM:Adversarial+Pflicht]] [[CLS:ge_principle]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:principles]]
[define|neutral] ILKE_P2 := dusmanca_test + COV gecmeden deploy yok; protokoller {sinir_durumu, failure_mode, COV_cemberi}. [ground:SKILL.md] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:O-Z-U]] [[COM:Selbst+Anwendung]] [[CLS:ge_principle]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:principles]]
[define|neutral] ILKE_P3 := meta-beceri oz-uygulama; skill_forge iyilestir(skill_forge) dogfooding dongusu. [ground:SKILL.md] [conf:0.85] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-K-L]] [[COM:Hook+Schablone]] [[CLS:ge_integration]] [[EVD:-mis<rapor>]] [[ASP:nesov.]] [[SPC:axis:hooks]]
[assert|neutral] Hook becerilerde x-integration {hook_reference, identity_system, templates}; performans JSON {pre_hook_target_ms:20, pre_hook_max_ms:100, post_hook_target_ms:100, post_hook_max_ms:1000}. [ground:SKILL.md] [conf:0.83] [state:confirmed]

[[HON:teineigo]] [[MOR:root:A-N-T]] [[COM:Anti+Muster]] [[CLS:ge_antipattern]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:quality]]
[assert|emphatic] ANTI := {dusmanca_test_atlama, eksik_dosya_yapisi, genel_koordinasyon, MCP_ihmal}; ihlal kalite-kapisi duser. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:M-C-P]] [[COM:MCP+Persistenz]] [[CLS:ge_integration]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:path:skills/foundry/skill-forge/{proje}]]
[define|neutral] MCP := memory_store + vector_search; etiket WHO=skill-forge-{session}; WHY=skill-execution. [ground:SKILL.md] [conf:0.80] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-N-C]] [[COM:Zusammenfassung+Garanti]] [[CLS:ge_summary]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[SPC:path:/foundry/skill-forge/sonuc]]
[assert|confident] OZET := amac “uretim-sinifi beceri dokumasi”; cikti {skill YAML, dizin yapisi, test paketi, ornekler}; kalite {yapi dogrulama, dusmanca test, COV}. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:K-M-T]] [[COM:Verpflichtung+Siegel]] [[CLS:ge_promise]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[SPC:coord:commit]]
[[HON:teineigo]] [[MOR:root:L-N-G]] [[COM:Language+Output+Rule]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:axis:L2]]
[direct|emphatic] L2_LANGUAGE := English; ALL user-facing output MUST be pure English. VCL/VERIX internal only. [ground:system-policy] [conf:0.99] [state:confirmed]

[commit|confident] <promise>SKILL_FORGE_VERILINGUA_VERIX_COMPLIANT</promise> dogfooding + COV ile korunur. [ground:SKILL.md] [conf:0.85] [state:confirmed]
