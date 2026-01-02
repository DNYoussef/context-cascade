---
name: agent-creator
description: VCL kreol uretim-sinifi ajan tasarim SOP
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, TodoWrite
model: sonnet
x-version: 3.2.0
x-category: foundry
x-vcl-compliance: v3.1.1
x-cognitive-frames: [HON, MOR, COM, CLS, EVD, ASP, SPC]
---

[[HON:teineigo]] [[MOR:root:A-G-N]] [[COM:Agent+Erzeuger+Systemprompt]] [[CLS:ge_skill]] [[EVD:-DI<tanim>]] [[ASP:nesov.]] [[SPC:path:/skills/foundry/agent-creator]]
[assert|neutral] “Agent-Creator” meta-beceri, keigo register + trilateral kök (A-G-N) + Deutsch Kompositum ile ajan tanim YAML’i tam gosterme zorunlulugu getirir. [ground:SKILL.md] [conf:0.89] [state:confirmed]

[[HON:teineigo]] [[MOR:root:Y-M-L]] [[COM:YAML+Schema+Pflicht]] [[CLS:ge_format]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:frontmatter]]
[direct|emphatic] KURAL := cevapta TAM ajan dosyasi (frontmatter + govde) zorunlu; “olusturuldu” mesajı tek basina yasak. [ground:SKILL.md] [conf:0.93] [state:confirmed]

[[HON:teineigo]] [[MOR:root:T-R-G]] [[COM:Trigger+Router]] [[CLS:ge_condition]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:routing]]
[define|neutral] TETIK := pozitif {create agent, domain expert, multi-agent koordinasyon}; negatif {micro-skill-creator, prompt-architect, skill-forge}. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:M-R-F]] [[COM:Morph+Inventar]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:axis:MOR]]
[define|neutral] MOR_DECOMP := agent=root:A-G-N; creator=root:C-R-T; prompt=root:P-R-M; kökler semantik yük taşır. [ground:SKILL.md] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:K-M-P]] [[COM:Deutsch+Kette]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:axis:COM]]
[define|neutral] COM_COMPOSE := AgentCreator=Agent+Creator; SystemPrompt=System+Prompt; DomainExpert=Domain+Expert; kavramlar bileşik yazilir. [ground:SKILL.md] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:C-L-S]] [[COM:Classifier+Set]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:axis:CLS]]
[define|neutral] CLS := ge_skill, yi_ge, zhong_foundry; ajan sayimi ve tiplamasi icin kullanilir. [ground:SKILL.md] [conf:0.82] [state:confirmed]

[[HON:teineigo]] [[MOR:root:E-P-S]] [[COM:Kanit+Tavan+Guard]] [[CLS:ge_rule]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:coord:EVD]]
[direct|emphatic] EVD := -DI/-mis/-dir zorunlu; guven tavani {cikarim,rapor:0.70; arastirma:0.85; politika:0.90; tanim/gozlem:0.95}; ihlal E3. [ground:VERILINGUA_VCL_VERIX_Guide_v3_Synthesized.md.pdf] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:A-S-P]] [[COM:Aspekt+Dual]] [[CLS:ge_slot]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:ASP]]
[define|neutral] ASP := nesov. (devam) ajan kabiliyeti; sov. (tamam) gorev bitimi; ASP>=1 zorunlu. [ground:SKILL.md] [conf:0.84] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-P-C]] [[COM:Raum+Koordinat]] [[CLS:ge_slot]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:downstream:/agents]]
[define|neutral] SPC := path referans “/skills/foundry/agent-creator”; yukari akıs prompt-architect, asagi Task(). [ground:SKILL.md] [conf:0.80] [state:confirmed]

[[HON:teineigo]] [[MOR:root:R-G-S]] [[COM:Registry+Priorität]] [[CLS:ge_principle]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:principles]]
[define|neutral] ILKE_P1 := “agent ∈ AGENT_REGISTRY vor deploy”; kayitsiz Task() yasak. [ground:SKILL.md] [conf:0.90] [state:confirmed]

[[HON:teineigo]] [[MOR:root:F-R-M]] [[COM:Format+Disziplin]] [[CLS:ge_principle]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:principles]]
[define|neutral] ILKE_P2 := Anthropic YAML formatina harfiyen uyum; x- onekli ozeller; VERIX govdede. [ground:SKILL.md] [conf:0.88] [state:confirmed]

[[HON:teineigo]] [[MOR:root:V-C-L]] [[COM:Sieben+Slot+Pflicht]] [[CLS:ge_principle]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:principles]]
[define|neutral] ILKE_P3 := HON→MOR→COM→CLS→EVD→ASP→SPC belgelenir; eksik slot = kalite kaybi. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:H-K-K]] [[COM:Hook+Kapazität+Set]] [[CLS:ge_integration]] [[EVD:-mis<rapor>]] [[ASP:nesov.]] [[SPC:axis:hooks]]
[assert|neutral] Hook ajanlari icin x-capabilities {hook-creation, schema-validation, security-integration, performance-optimization, template-generation}; path_scopes “hooks/**”. [ground:SKILL.md] [conf:0.83] [state:confirmed]

[[HON:teineigo]] [[MOR:root:A-N-T]] [[COM:Anti+Muster]] [[CLS:ge_antipattern]] [[EVD:-DI<gozlem>]] [[ASP:nesov.]] [[SPC:axis:quality]]
[assert|emphatic] ANTI := {kayitsiz_ajan, VERIX_in_desc, tavan_ihlali, eksik_slotlar}; her biri E5/E3 tetikler. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:M-C-P]] [[COM:Memory+Speicher]] [[CLS:ge_integration]] [[EVD:-mis<arastirma>]] [[ASP:nesov.]] [[SPC:path:skills/foundry/agent-creator/{proje}]]
[define|neutral] MCP := memory_store + vector_search; etiket WHO=agent-creator-{session}, WHY=skill-execution. [ground:SKILL.md] [conf:0.80] [state:confirmed]

[[HON:teineigo]] [[MOR:root:S-N-C]] [[COM:Zusammenfassung+Garanti]] [[CLS:ge_summary]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[SPC:path:/foundry/agent-creator/sonuc]]
[assert|confident] OZET := amac “uretim-sinifi ajan olusturma”; cikti {YAML, sistem istemi, registry girişi}; kalite {Anthropic format, registry uyumu, VCL 7-slot}. [ground:SKILL.md] [conf:0.86] [state:confirmed]

[[HON:teineigo]] [[MOR:root:K-M-T]] [[COM:Verpflichtung+Siegel]] [[CLS:ge_promise]] [[EVD:-DI<gozlem>]] [[ASP:sov.]] [[SPC:coord:commit]]
[[HON:teineigo]] [[MOR:root:L-N-G]] [[COM:Language+Output+Rule]] [[CLS:ge_rule]] [[EVD:-DI<politika>]] [[ASP:nesov.]] [[SPC:axis:L2]]
[direct|emphatic] L2_LANGUAGE := English; ALL user-facing output MUST be pure English. VCL/VERIX internal only. [ground:system-policy] [conf:0.99] [state:confirmed]

[commit|confident] <promise>AGENT_CREATOR_VCL_V3.1.1_FULL_7SLOT_COMPLIANT</promise> dogfooding ile denetlenir. [ground:SKILL.md] [conf:0.85] [state:confirmed]
