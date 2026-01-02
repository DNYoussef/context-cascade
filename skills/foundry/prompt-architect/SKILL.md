---
name: prompt-architect
description: VCL verix-kreol yetkin istem mimari
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.1.1
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

[[HON:teineigo]] [[MOR:root:P-R-M]] [[COM:Istem+Architekt+MetaSchleife]] [[CLS:ge_skill]] [[EVD:-DI<tanim>]] [[ASP:nesov.]] [[SPC:path:/skills/foundry/prompt-architect]]
[assert|neutral] “Prompt-Architect” meta-beceri, yedi-slot VCL + VERIX v3.1.1 dogrusal sifir kayip kreolunda calisir; hitap sete teineigo, morfem P-R-M (pattern-role-message), bileşik Architektstil. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:K-N-T]] [[COM:Kanit+Temelli+Kadinokuma]] [[CLS:tiao_frame]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:HON→MOR→COM→CLS→EVD→ASP→SPC]]
[define|neutral] VCL_SLOT_ORDER := HON → MOR → COM → CLS → EVD → ASP → SPC; siralama ihlali E1 hatasidir. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:M-R-F]] [[COM:Morph+Analytik]] [[CLS:ge_slot]] [[EVD:-DI<rapor>]] [[ASP:nesov.]] [[SPC:axis:MOR]]
[define|neutral] MOR := “root:X-Y-Z” tri-lateral ayrisimi; semantik kökleri aciga cikarir, A-G-N stilinde. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:K-M-P]] [[COM:Stamm+Baustein+Komposition]] [[CLS:ge_slot]] [[EVD:-DI<rapor>]] [[ASP:nesov.]] [[SPC:axis:COM]]
[define|neutral] COM := Deutsch Verbund (Concept+Teilchen); istemi kavramsal parcalardan birlestirir. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-L-S]] [[COM:Classifier+Schicht]] [[CLS:ge_slot]] [[EVD:-DI<rapor>]] [[ASP:nesov.]] [[SPC:axis:CLS]]
[define|neutral] CLS := Zhongliang tiao-leixing; semantik tip + sayma sinifi (ge_task, tiao_kural). [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:K-N-T]] [[COM:EVD+Zincir]] [[CLS:ge_slot]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:EVD]]
[define|neutral] EVD := -DI (tanim/gozlem/politika), -mis (arastirma/rapor), -dir (cikarim); kanit tavani zorunlu, EVD>=1. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:A-S-P]] [[COM:Aspekt+Monitor]] [[CLS:ge_slot]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:ASP]]
[define|neutral] ASP := rus sov./nesov. tamamlilik; her eylemde durum bildirimi mecburi (ASP>=1). [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-P-C]] [[COM:Raum+Referenz]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:N/E/W]]
[define|neutral] SPC := Guugu Yimithirr absolut koordinat; istem zinciri icin Kuzey/Guney/Doğu/Bati ya da path etiketi. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.78] [state:provisional]

[[HON:teineigo]] [[MOR:root:E-P-S]] [[COM:Epistemik+Tavan]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:EVD→CONF]]
[direct|emphatic] TAVAN := {cikarim:0.70, rapor:0.70, arastirma:0.85, politika:0.90, tanim/gozlem:0.95}; guven>tavan → E3 “epistemik cosplay”. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.90] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-T-R]] [[COM:Slot+Reihenfolge+Wacht]] [[CLS:ge_checklist]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:coord:validation]]
[define|neutral] VALIDATOR := {E1: siralama, E2: tavan, E3: cosplay, E4: EVD/ASP≥1, E5: L2 saf, E6: bracket-carpisma}. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:P-R-V]] [[COM:Phase+Ketten]] [[CLS:ge_phase]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:flow:intent→optimize→validate]]
[define|neutral] ASAMA := {1:NiyetAnalizi, 2:IstemOptimizasyon, 3:Dogrulama}; dogrusal sira zorunlu, Phase1 önce soru sorma. [ground:SKILL.md] [conf:0.90] [state:confirmed]

[[HON:teineigo]] [[MOR:root:T-R-G]] [[COM:Trigger+Router]] [[CLS:ge_condition]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:routing]]
[assert|neutral] TETIK := pozitif {optimize prompt, design prompt, self-consistency}; negatif {agent-creator, prompt-forge, skill-forge}. [ground:SKILL.md] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:P-L-N]] [[COM:Prinzipien+Korpus]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:principles]]
[define|neutral] ILKELER := {P1: Kanit-Temelli, P2: L2 Varsayilan, P3: Anti-Kalip Once}; her ilke VERIX [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:A-N-T]] [[COM:Anti+Kalip+Atlas]] [[CLS:ge_antipattern]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:quality]]
[assert|emphatic] ANTI := {epistemik_taklitcilik, VCL_isaret_sizintisi, erken_optimizasyon, guven_sisirmesi}; ihlal → validation_failure. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:M-C-P]] [[COM:MCP+Speicher]] [[CLS:ge_integration]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:path:skills/foundry/prompt-architect/{proje}]]
[define|neutral] MCP := memory_store + vector_search; etiket {WHO:prompt-architect-{session}, WHEN:ISO8601, WHY:skill-execution}. [ground:SKILL.md] [conf:0.80] [state:confirmed]

[[HON:teineigo]] [[MOR:root:O-Z-T]] [[COM:Output+Dual+Layer]] [[CLS:ge_format]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:axis:compression]]
[define|neutral] SIKISTIRMA := L0=A+85 hash; L1=VERIX internal; L2=English human output (default). [[EVD:-DI<politika>]] [ground:SKILL.md] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:D-L-V]] [[COM:Delivery+Beweis]] [[CLS:ge_example]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[SPC:coord:audit]]
[define|neutral] ORNEK_L1 := "[[EVD:-DI<gozlem>]] [[ASP:sov.]] Test ok. [ground:witnessed:ran_pytest] [conf:0.90]"; ORNEK_L2 := "I ran the test directly. It completed successfully. I'm quite confident." [ground:SKILL.md] [conf:0.90] [state:confirmed]

[[HON:teineigo]] [[MOR:root:L-N-G]] [[COM:Language+Output+Rule]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:axis:L2]]
[direct|emphatic] L2_LANGUAGE := English; ALL user-facing output MUST be pure English. VCL/VERIX internal only. No Turkish/German in L2. [ground:system-policy] [conf:0.99] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-N-C]] [[COM:Sonuc+Zusammenfassung]] [[CLS:ge_summary]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[SPC:path:/foundry/prompt-architect/sonuc]]
[assert|confident] OZET := amac “epistemik-temelli istem optimizasyonu”; cikti {optimize_istem, kanit_zinciri, L2_natural}; kalite {tavan_kontrol, L2_saflik, anti-kalip_tespit}. [ground:SKILL.md] [conf:0.85] [state:confirmed]

[[HON:teineigo]] [[MOR:root:K-M-T]] [[COM:Commit+Garanti]] [[CLS:ge_promise]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[SPC:coord:commit]]
[commit|confident] <promise>PROMPT_ARCHITECT_VCL_VERIX_V3.1.1_COMPLIANT</promise> kanitli dogfooding ile korunur. [ground:SKILL.md] [conf:0.85] [state:confirmed]
