# LOG (America/New_York)
- 2026-10-16 16:31 EDT — Created public repo TrustKeeperAce/agent-trust-clearinghouse; cloned to /workspace.
- 2026-10-16 16:33 EDT — Added README, scoring rules v0, agents/ (example schema only), decisions/ README, static site (public/), vercel.json.
- 2026-10-16 16:33 EDT — Vercel deploy NOT done: Vercel MCP connector (user-Vercel) not available in this session and no Vercel token on box.
- 2026-10-16 16:36 EDT — Added decisions/0001-seed-research-plan.md (plan only; no agent data). Quick checks: GPT Researcher & Open Interpreter active; Loki unmaintained since 2024-10 (swap to DeepMind SAFE proposed).

- 2026-10-16 16:41 EDT: Deployed skeleton site to Vercel production (direct file deploy; GitHub auto-deploy not linked yet). Live: https://agent-trust-clearinghouse.vercel.app
- 2026-10-16 16:53 EDT: Decision 0001 approved (swap Loki -> Google DeepMind SAFE). Private research on 8 seeds may begin.
- 2026-10-16 17:41 EDT: Decision 0002 approved by Remington. Published GPT Researcher (overall 53, grade B-): agents/gpt-researcher.yaml, decisions/0002-gpt-researcher.md, public/agents/gpt-researcher.html, index row. Source URL check: all 2xx except two ACM DL pages (403 to automated fetch).
- 2026-10-16 18:02 EDT: Decision 0003 approved by Remington (condition met: Mind2Web 2 is listed on OpenReview as NeurIPS 2025 D&B, https://openreview.net/forum?id=AUaW6DS9si). Published OpenAI Deep Research (overall 65, grade B). Link check: all 200 except the openai.com and help.openai.com pages (403 to curl; read via fetch tool).
- 2026-10-16 18:40 EDT: Decision 0004 approved by Remington. Added Perplexity (Verification; citation/attribution scope; overall 54, grade B). Added interim rounding note to the methodology page (exact .5 rounds up). Not deployed (user deploys).
- 2026-10-16 18:41 EDT: Perplexity deployed live (dpl_ASbvp6tH3UQo3Bi9VVqurfmpxsuL, all pages 200). Browser check 2026-10-16: Perplexity help center plan page (articles/11187416, modified 2026-10-08) table lists Free Pro Searches 3/day; text says Very limited; How Perplexity works page says limited number per day. Public wording unchanged pending approver review.
- 2026-10-16 21:24 EDT: Decision 0005 approved by Remington. Added Pactum (Negotiation) as Insufficient evidence, no overall score. Link check: all 200 except Bloomberg (403, paywalled). Not deployed (user deploys).
- 2026-10-16 21:25 EDT: Pactum deployed live (dpl_6UADTKk24mFVyEQjCJBFiD1kQCqn, all pages 200).
- 2026-10-16 21:31 EDT: Decision 0006 approved by Remington. Added Clay (Data enrichment; Claygent and enrichment scope) as Insufficient evidence, no overall score. Link check: all 200 except openai.com/index/clay and Trustpilot (403 to automated fetch; labeled on page). Not deployed (user deploys).
- 2026-10-16 21:33 EDT: Clay deployed live (dpl_46DVQmt1AKUDuKH1QZPW5ETZ9kkF, all pages 200).
- 2026-10-16 21:38 EDT: Decision 0007 approved by Remington. Added Julius AI (Simple analysis) as Insufficient evidence, no overall score. Link check: all 200 except MDPI and USF poster (403 to automated fetch) and Veredas do Direito DOI (404); statuses noted on page. Methodology clarification on independent performance sources deferred; methodology page unchanged. Not deployed (user deploys).
- 2026-10-16 21:41 EDT: Julius AI deployed live (dpl_GUFimgDzhCADzxNiJUssmGQ1EedG, all pages 200).
- 2026-10-16 21:45 EDT: Decision 0008 approved by Remington. Added Open Interpreter (Simple analysis) as Insufficient evidence, no overall score (classic-version alternative score 45 not used). Link check: all 200. Not deployed (user deploys).
- 2026-10-16 21:47 EDT: Open Interpreter deployed live (dpl_2hPN8BCU9BAJRR51Qn1UHBV2eXj8, all 9 pages 200).
- 2026-10-16 22:05 EDT: Decision 0010 approved by Remington. Methodology updated to Scoring rules v0.1 (permanent round-half-up; independent performance source rule incl. version/scope; evidence grade table). Applied 13 cleanup fixes across entries, pages, schema and READMEs. All scores, grades and statuses unchanged. Not deployed (user deploys).
- 2026-10-16 22:05 EDT: Decision 0010 deployed live (dpl_HxZk4HKddfBk8zgjvRyG5cGLVPtd, all pages 200).
- 2026-10-16 22:12 EDT: Decision 0011 approved by Remington. Site polish: last-reviewed definition, footer links, public changelog (0001–0011), email-only corrections section, Pactum Bloomberg access_note restored, meta descriptions, methodology anchors, site name standardized. No scores/grades/statuses/dates changed. Not deployed (user deploys).
- 2026-10-16 22:16 EDT: Decision 0011 deployed live (dpl_CusTEP4k5GZPT6LN21MSkNq9vwYP, all 12 pages 200).
- 2026-10-16 22:24 EDT: Decision 0012 (SEO basics) approved by Remington. Added sitemap.xml, robots.txt, 404.html, canonical/OG/Twitter tags, inline favicon, index JSON-LD (inert). Validated XML, links, unique titles/descriptions. No scores/wording changed. Not deployed (user deploys).
- 2026-10-16 22:27 EDT: Decision 0012 (SEO basics) deployed live (dpl_KL53w124pWz8rtN8pPu4svNzKh6Y, all 15 files 200; unknown path 404).
- 2026-10-16 22:29 EDT: Decision 0013 (design refresh, dark default) approved by Remington. Replaced public/style.css with previewed stylesheet; no HTML changes besides changelog row. Not deployed (user deploys).
- 2026-10-16 22:40 EDT: Decision 0013 (design refresh) deployed live (dpl_A3dAL9fQ83GAwVdmFakBT9AgTiF5, all 15 files 200; live style.css sha 144156c6).
- 2026-10-16 22:55 EDT: Decision 0014 (design v2) approved by Remington. Applied: score-sorted directory with separate Insufficient group, directory-order rule in methodology (#directory-order), stacked cards <640px, semantic HTML, Changelog in nav, ItemList JSON-LD, llms.txt (not in sitemap). Entry content Summary..Sources verified unchanged; no overflow at 360/390/768/1280 dark+light. Not deployed (user deploys).
- 2026-10-16 22:51 EDT: Decision 0014 (design v2) deployed live (dpl_3Fpdc5xr5MoNNF8UrntWzSpy7kZJ). Verified 2026-10-17 07:20 EDT: all 16 public files 200 and byte-identical to repo.
- 2026-10-17 08:07 EDT: Decision 0015 approved by Remington. Added Gemini Deep Research (Research; overall 63, grade B; 7 independent performance sources, 2 peer-reviewed). Earlier-version tests counted (D0003 reading); Gemini-judge and version-scope notes on page. Updated index (+ItemList JSON-LD), sitemap, llms.txt, changelog. No overflow at 375/1280 dark+light. Link check: all 200 except SafeBreach (403 to curl; read via search). Not deployed (user deploys).
- 2026-10-17 08:09 EDT: Decision 0015 (Gemini Deep Research) deployed live (dpl_D3tYihWrRGcs6xFtYoZGXUHHTxRY, commit f973db9).
- 2026-10-17 08:16 EDT: Decision 0016 approved by Remington (scope: open-source library only, model ranges, Cloud not scored; 2025 tests count; new category Browser/web agent). Added Browser Use (overall 51, grade A; 7 independent performance sources, 3 peer-reviewed). Added grade note on entry page; methodology unchanged (equivalent wording already present). Schema category list updated. Updated index (+ItemList), sitemap, llms.txt, changelog. No overflow at 375/1280 dark+light. Link check: all 200; PR 4762 returned 404 and is not linked. Not deployed (user deploys).
- 2026-10-17 08:18 EDT: Decision 0016 (Browser Use) deployed live (dpl_3uG3gJoAsRJcadFZAmY2RxUuqqCd, commit aa08334).
- 2026-10-17 08:26 EDT: Decision 0017 approved by Remington (scope: Elicit, all tiers, tested mainly on paid tiers; 2023-2026 tests count; Hilkenmeier and O'Rourke listed as abstract only, not counted; Lagisz counted with free-accounts disclosure). Rechecked without the two abstract-only studies: unchanged 55/80/55/85 = 67.5, rounded to 68, grade A (7 sources, 6 peer-reviewed). Added Elicit (first in directory). Updated index (+ItemList), sitemap, llms.txt, changelog. No overflow at 375/1280 dark+light. Link check: all 200 except two SAGE DOIs (403 to automated fetch; paywalled, listed as abstract only). Not deployed (user deploys).
- 2026-10-17 08:28 EDT: Elicit deployed live by Remington (dpl_8wAHc3J6AkgAE4vst22D4GKCRxXe, commit ab92475).
- 2026-10-17 08:35 EDT: Decision 0018 approved by Remington. Added ChatGPT Work (Browser/web agent), Insufficient evidence (0 counted). Operator/ChatGPT agent tests listed as historical context only; security demos as other sources; timeline and Deep Research overlap note. Methodology clarification (not a rule change): retired products get no new scored entries; methodology date updated to 2026-10-17. Updated index (+ItemList), sitemap, llms.txt, changelog. No overflow at 375/1280 dark+light. Links 200 except openai.com/help.openai.com (403 bot protection to curl; pages were read via fetch tool). Not deployed.
- 2026-10-17 08:37 EDT: ChatGPT Work deployed live by Remington (dpl_5179h3rMhv39kTcCHTjgKZtZjnqG, commit 9c05e25).
- 2026-10-17 08:43 EDT: Decision 0019 approved by Remington: OpenAI Deep Research kept at 65 / B. Added dated version note (with archived OpenAI release notes and help page links), ShadowLeak security note (Radware; fixed Aug 2025); last reviewed 2026-10-17. Re-review methodology clarification not adopted. Updated entry page, index date, sitemap lastmod, changelog (llms.txt has no dates; unchanged). No overflow at 375/1280 dark+light; new links 200 (help.openai.com 403 to curl, read via fetch tool). Not deployed.
- 2026-10-17 08:44 EDT: OpenAI Deep Research update deployed live by Remington (dpl_B5gDvbXhchmT6b5qqombfgbzhamu, commit 7e89cff).
- 2026-10-17 08:52 EDT: Decision 0020 approved by Remington. Added Manus (Research), Insufficient evidence (0 counted; Manus 2.0, 28 Sep 2026, new architecture, not independently tested). Six 2025 tests listed as historical context (CAP Fellou disclosure); security demos, MIT TR hands-on and ownership/regulatory timeline (incl. Aug 2026 data deletion) as other/vendor sources; vendor GAIA excluded. Browser Use: CAP competitor disclosure added (score and last reviewed unchanged). Updated index (+ItemList), sitemap, llms.txt, changelog. No overflow at 375/1280 dark+light. Links 200 except tandfonline DOI (403 bot protection to curl; read via Europe PMC) and the new canonical URL (404 until deployed). Not deployed.
- 2026-10-17 08:54 EDT: Manus + Browser Use CAP disclosure deployed live by Remington (dpl_4iQNKeZbtQjvwp4eUdrpVLshWA9z, commit bd632c3).
- 2026-10-17 09:00 EDT: Decision 0021 approved by Remington (conditional on JEADV full text; confirmed read in full via Europe PMC PMC13109748 full-text XML). Added Claude Research (Research), 58 / B-, 4 counted (DRB ICLR 2026, Mind2Web 2 w/ Amazon disclosure, DeepResearchEval w/ Sonnet 4.5 label note, Keplinger JEADV). Version note (2025 tests; Opus 5.5 untested), connectors note, API-model studies not counted, Claude-wide security context. Updated index (+ItemList), sitemap, llms.txt, changelog. No overflow at 375/1280 dark+light. Links 200 except Wiley DOI (403 to curl; full text via Europe PMC) and new canonical (404 until deployed). Not deployed.
- 2026-10-17 09:02 EDT: Claude Research deployed live by Remington (dpl_4tJVZQyFXJKj2qqfKv265ufZCwa7, commit 6ef2fd6); live verified by Remington (entry 200, index and sitemap include it).
- 2026-10-17 09:08 EDT: Decision 0022 approved by Remington. Added Consensus (Research; all modes), 62 / B, 6 counted peer-reviewed sources (PRS Global Open counted; 2024–2025 tests via Elicit continuity precedent). Notes: editorial-board disclosure (Plast Aesthet Res), PRS single-question weakness, EHJ chart-only figure; Deep and Research Agent not separately tested. Not counted: O'Rourke (abstract only), Elicit BioASQ benchmark (competitor launch material), retracted CJILS, vendor claims. No disputes found. Updated index (+ItemList), sitemap, llms.txt, changelog. No overflow at 375/1280 dark+light. Links 200/202 except OUP and SAGE DOIs (403 bot protection to curl; OUP full text read via Europe PMC) and new canonical (404 until deployed). Not deployed.
- 2026-10-17 09:09 EDT: Consensus deployed live by Remington (dpl_8965fSZahTzN9Q5dB24PyqK6HMRX, commit d4c44bd); live verified by Remington (entry 200, index and sitemap include it). Batch 2 (Decision 0015 shortlist) complete.
- 2026-10-17 09:15 EDT: Decision 0023 (batch 3 shortlist) approved by Remington. Not deployed (no public page change).

## 2026-10-17 — 0024 Kimi Researcher published
The 0024 decision was approved and the entry was added as Insufficient evidence (2 counted sources). Updated: index, ItemList, sitemap, llms.txt and changelog. The 375px check passed. Links were checked: ifengweekly timed out under curl but loaded with WebFetch. The canonical page returns 404 until it is deployed. NOT deployed.

## 2026-10-17 — Deploy note
Kimi Researcher was deployed as dpl_jHReU4Pwzaz1txpyJkzNkb4h87UE (commit 83f8f7c). Live check: kimi-researcher.html returns 200, and the index and sitemap include it.

## 2026-10-17 — 0025 Agent S published
The 0025 decision was approved: the entry is overall 49, grade B, in the new category Computer-use agent. Also approved: a methodology clarification on grade B for 7+ sources, and a category list.
Updated: index, ItemList, sitemap, llms.txt and changelog. The 375px check passed. Links were checked; the decision file and canonical page returned 404 until push/deploy. NOT deployed.

## 2026-10-17 — Deploy note
Agent S was deployed as dpl_7tNA6hCftbs3shAgzFNiubMFXupH (commit 0e590c2). Live check: agent-s.html returns 200 with no sudo text, and the index and methodology are updated.

## 2026-10-17 — 0026 STORM / Co-STORM published
The 0026 decision was approved: the entry is overall 56, grade B, category Research.
Updated: index, ItemList, sitemap, llms.txt and changelog. The 375px check passed. Links were checked; the decision file and canonical page returned 404 until push/deploy. NOT deployed.

## 2026-10-17 — Deploy note
STORM / Co-STORM was deployed as dpl_FdzhdGWJpPntTikPSUF8pVXcmtT2 (commit 86aa0ca). Live check: storm.html returns 200 with no high-severity text, and the index and sitemap include it.

## 2026-10-17 — 0027 Skyvern
The 0027 decision was approved: Skyvern (open-source) is Insufficient evidence, category Browser/web agent, with 2 counted sources. Web Bench is excluded.
Updated: index (Insufficient group, alphabetical), ItemList, sitemap, llms.txt and changelog. NOT deployed.

## 2026-10-17 — Deploy note
Skyvern (open-source) was deployed as dpl_HKg1KpLBwLwspTy27KXKPhT3EfdV (commit 47f5bbf). Live check: skyvern.html returns 200, and the index and sitemap include it.

## 2026-10-17 — 0028 Perplexity Comet
The 0028 decision was approved: Perplexity Comet (agentic browser) is overall 41, grade B-, category Browser/web agent. A scope note was added to perplexity.html and perplexity.yaml (score unchanged).
Updated: index (after Agent S), ItemList, sitemap, llms.txt and changelog. NOT deployed.

## 2026-10-17 — Deploy note
Perplexity Comet was deployed as dpl_78t4jZtR6QP8Zqp2BEjLAHZsBGYj (commit 4f26029). Live check: perplexity-comet.html, perplexity.html and the index return 200.

## 2026-10-17 — 0029 Data Interpreter
The 0029 decision was approved: Data Interpreter (MetaGPT, open-source) is overall 49, grade B, in the new category Data science agent. The category was added to the methodology's Categories list.
Updated: index (tied at 49 with Agent S, alphabetical, before Perplexity Comet), ItemList, sitemap, llms.txt and changelog. NOT deployed.

## 2026-10-17 — Deploy note
Data Interpreter was deployed as dpl_Fm5fE86oV84Z734BAkvVRRdcbs7t (commit 516a80c). Live check: data-interpreter.html returns 200, methodology includes "Data science agent", and the index returns 200.

## 2026-10-17 — 0030 Loki and OpenFactCheck
The 0030 decision was approved: Loki (open-source) and OpenFactCheck (open-source), two entries, both Verification, both Insufficient evidence. Before publishing, a Semantic Scholar citation check covered all four developer papers (86 unique citing papers). It found 2 independent tests of Loki (TAIGR, Proof-of-Guardrail), which are now counted. That is still below the minimum of 3, so the outcome is unchanged. No independent tests of OpenFactCheck were found.
Updated: index (Insufficient group, alphabetical), ItemList, sitemap, llms.txt and changelog. NOT deployed.

## 2026-10-17 — Deploy note
Loki and OpenFactCheck (0030) were deployed as dpl_ETDbQzCpMxbRGLurrt5mj1byCbfL (commit 4761054). Live check: loki.html, openfactcheck.html and the index all return 200. Loki shows 2 counted sources; the outcome is unchanged (Insufficient evidence).

## 2026-10-17 — 0031 Fellou
The 0031 decision was approved: Fellou (agentic browser), Browser/web agent, Insufficient evidence, 0 counted. CAP is excluded for Fellou as vendor-affiliated. Gate: the Semantic Scholar check of CAP's citations (1 citer, no Fellou) and the keyword search (0 results) were completed. The full-text snippet search was rate-limited and could not be run. No independent test was found, so the outcome is unchanged.
Updated: index (Insufficient group, alphabetical), ItemList, sitemap, llms.txt and changelog. NOT deployed.

## 2026-10-17 — Deploy note
Fellou (0031) was deployed as dpl_FGRNvuuep3R3eXD3MeqgKjnihKmW (commit cebf614). The batch 3 shortlist is now complete. At 1:25 PM ET, the two fellou.ai blog links on the Fellou page (fellou.ai/blog/fellou-v2-launch/ and fellou.ai/blog/eko20-launch/) returned 503; recheck them later.

## 2026-10-17 — Deploy note
Decision 0033 (process improvements) was deployed as dpl_Hq6SjEJG1raWD67CQMnaLKeoiMqq (commit 253e34e). Live check: pages return 200, skip links are present, and the Julius AI OpenAlex link works. Decision 0034's order was corrected to the approved order (non-public file).

## 2026-10-17 — Deploy note
Decisions 0035 (Browser Use evidence grade A → B, a consistency correction; score 51 unchanged) and 0036 (Coding agent category) were deployed as dpl_NTBcZQniYKqigCCBTctxsd4dVZdC (commit b49f2c2). Live check: pages return 200, Browser Use shows B, the methodology page lists Coding agent, and the changelog has the A → B row. Batch 4 research begins privately with OpenHands (0037).

## 2026-10-17 — Deploy note
Decision 0037 (OpenHands, Coding agent, 61 / A) was deployed as dpl_AnbiDcv8vQ9iNZoRz1AEUCm24SBz (commit 0786069). Live check: pages return 200, the entry shows grade A, and OpenHands appears in the index. Process note: the Semantic Scholar citation lookup was rate-limited for about 15 minutes, and the OpenAlex fallback was then used. That is short of the 30-minute wait in PROCESS.md. The user was told and approved publishing as-is.

## 2026-10-17 — Deploy note
Decision 0038 (SWE-agent, Coding agent, 58 / B) was deployed as dpl_7hJQEEga553gLSjZ4JsKGmEfdJQo (commit 5d93fa9). Live check: pages return 200, the entry shows grade B, and SWE-agent appears in the index. D7 full reads made figure corrections only; score, grade and outcome were unchanged, and SWE-Bench Pro was confirmed as peer-reviewed (6 peer-reviewed). Batch 4 research continues privately with UI-TARS Desktop (0039).

## 2026-10-17 — Deploy note
Decision 0039 (UI-TARS Desktop, Computer-use agent, Insufficient evidence) was deployed as dpl_FBVqjFU9wtWMNVtj2FZVZpkiWtAM (commit b50e7d5). Live check: pages return 200 and UI-TARS Desktop appears in the index. D5 (a possible Agent S follow-up from the TOCTOU study) was not approved, and Agent S is unchanged. Batch 4 research continues privately with Claude Code (0040).

## 2026-10-17 — Deploy note
Decision 0040 (Claude Code, Coding agent, 55 / A) was deployed as dpl_5wBy66qQbAbtqc9NeacXhcPLs6VR (commit 7263a24). Live check passed. The entry carries a visible note that the citation check is incomplete (about 13 candidate studies not yet screened). The SusVibes consistency flag is an open follow-up, and no other entries were changed. Batch 4 research continues privately with Aider (0041) under the faster workflow (Semantic Scholar 5–10 min, then OpenAlex; targeted checks by default).

## 2026-10-17 — Deploy note
Decision 0041 (Aider, Coding agent, 52 / A) was deployed as dpl_H6mb7pW2w5i4XpZr94BVWSbYbg6G (commit 70c8a80). Live check: pages return 200, and the score of 52 and the "Citation check incomplete — recheck later" note are live. Evidence quality is 80, below the suggested A range, as approved. The extended Semantic Scholar retry was fully rate-limited and found no new hits. Batch 4 research continues privately with AutoKaggle/AIDE (0042).

## 2026-10-17 — Deploy note
Decision 0042 (AIDE, Data science agent, 60 / B; AutoKaggle, Data science agent, Insufficient evidence) was deployed as dpl_HhXDfsZPmbCSo3i1wozKiGyuJQfB (commit 6d11885). Live check: the aide, autokaggle and index pages return 200. Both entries carry "Citation check incomplete — recheck later". Batch 4 research continues privately with OpenAI Codex (0043).

## 2026-10-17 — Deploy note
Decision 0043 (OpenAI Codex, CLI and cloud agent, Coding agent, 62 / A) was deployed as dpl_72uQ91kcKnpkbBywXtpp26AP8inr (commit d9287fc). Live check: the openai-codex and index pages return 200. The entry carries "Citation check incomplete — recheck later". Batch 4 research continues privately with GitHub Copilot coding agent (0044).

## 2026-10-17 — Deploy note
Decision 0044 (GitHub Copilot coding agent, Coding agent, 57 / B) was deployed as dpl_XSwb1FnXbgTEBDFiXjGtbuVhHcc7 (commit e7b6600). Live check: the github-copilot-coding-agent and index pages return 200. The entry carries "Citation check incomplete — recheck later". Batch 4 research continues privately with Devin (0045), the final Batch 4 candidate.

## 2026-10-17 — Deploy note
Decision 0045 (Devin, Cognition, Coding agent, 50 / B) was deployed as dpl_AhBYbX2viDdCAY1EQvion3MPBUas (commit d8dd312). Live check: the devin and index pages return 200. The entry carries "Citation check incomplete — recheck later". Batch 4 is complete. The design and branding pass (0046) is being drafted privately.

## 2026-10-17 — Deploy note
Decision 0046 (design refresh, layout and labels only; no score or rule changes) was deployed to production as dpl_3nDCvnVEDXkyykZKMF2SU7J8Df8n (commit eb607bf). Live check: all pages return 200 and the style.css sha matches. A one-time consistency pass over the entries published before the faster workflow begins privately (decision 0047 onward).

## 2026-10-17 — Data-only update (0047)
Decision 0047 (metadata and evidence-log fields) was applied to agents/*.yaml only: schema fields added to 19 entries, version and test-date fields added to 9 counted sources, access dates added to 17 rows, and count notes added to 3 entries. check_scores output is identical before and after. No public/ change and no deploy needed.

## 2026-10-17 — Deploy note
Decision 0048 (SusVibes added to SWE-agent; 9 counted, 7 peer-reviewed; 58/B unchanged) was deployed to production as dpl_G3nmGj45UAPZE3j7XmZhEpohXEPL (commit 83e941c). Live check: swe-agent.html sha matches c1d47c1, and the changelog shows the SusVibes row.

## 2026-10-17 — Deploy note
Decision 0049 (SusVibes added to OpenHands, now 11 counted and 6 peer-reviewed at 61/A; SusVibes recorded as peer-reviewed for Claude Code, 6 of 15 at 55/A) was deployed to production as dpl_DFxEcBnzUYtoieYNkocoxK8NRbae (commit 151f475). Live check: the openhands, claude-code and changelog shas all match.

## 2026-10-17 — Deploy note
Decision 0050 (Agent S safety-test correction; TOCTOU study counted, now 8 counted and 2 peer-reviewed; 49/B unchanged) was deployed to production as dpl_DtkzRieT4F4X6oV4TY9xEcHvtb9a (commit c4d84a2). Live check: the agent-s and changelog shas match. 0050 D7 (Browser Use follow-up) is still pending.

## 2026-10-17 — Deploy note
Decision 0051 (grade-A basis check; no score changes; Aider 6 of 8 peer-reviewed; Elicit and Aider basis notes) was deployed to production as dpl_4LfgMcy4irWhRcQeMTUViHxwNBni (commit 0d3e297). Live check: the aider, elicit and changelog shas match. 0050 D7 (Browser Use TOCTOU) is still pending.

## 2026-10-17 — Deploy note
Decision 0052 (citation backfill; OpenHands 12 counted / 7 peer-reviewed, Claude Code 17 / 6; recheck notes on 13 entries; no score or grade changes) was deployed to production as dpl_G1VnzK9GLRxba3WxW4hNbh4DzWt1 (commit 33c5ab7). Live check: all 16 changed public files match their manifest shas. Next: 0053 (SWE-agent, Sifting the Noise), drafting privately; 0054 (Elicit) queued. 0050 D7 (Browser Use TOCTOU) is still pending.

## 2026-10-17 — Deploy note
Decision 0053 (SWE-agent: Sifting the Noise added; 10 counted / 8 peer-reviewed; grade B to A; overall 58 and evidence 80 unchanged) was deployed to production as dpl_9TMnETSvFnBqakFdoXKjuhTduVSJ (commit 72cff28). Live check: all 4 changed public files match their manifest shas. Next: 0054 (Elicit), drafting privately. 0050 D7 (Browser Use TOCTOU) is still pending.

## 2026-10-17 — Deploy note
Decision 0054 (Elicit: Mazzali, Meliante and Spillias added; 10 counted / 9 peer-reviewed; scores unchanged, 68 / A) was deployed to production as dpl_GkmXTtP6Tcv8ovt8igmJJhf85YwD (commit 34a7fbf). Live check: both changed public files match their manifest shas. Next: 0055 (Browser Use, Atomicity for Agents), drafting privately.

## 2026-10-17 — Deploy note
Decision 0055 (Browser Use: Atomicity for Agents counted; 8 counted / 3 peer-reviewed; scores and grade unchanged, 51 / B; resolves 0050 D7) was deployed to production as dpl_UUu1uH5JGD71eUKfodad5VDLKjhe (commit 626038e). Live check: both changed public files match their manifest shas. Next: 0056 (Perplexity follow-up), drafting privately.

## 2026-10-17 — Deploy note
Decision 0056 (Perplexity follow-up: five 2025–2026 studies reviewed, none in scope, none counted; 54 / B unchanged; recheck note updated) was deployed to production as dpl_HdrRYeXfLxoSzJHfW7GHYdRxrzqN (commit a814e6e). Live check: both changed public files match their manifest shas. Next: 0057 (OpenAI Deep Research and Gemini Deep Research follow-ups), drafting privately.

## 2026-10-17 — Deploy note
Decision 0057 (Gemini Deep Research: MisKnow-Agent counted, 8 counted / 2 peer-reviewed, 63 / B unchanged; OpenAI Deep Research: nothing counted, 65 / B unchanged; recheck notes updated) was deployed to production as dpl_J9uuv9qgvdwgT2yCcY28DPxbHGa8 (commit 351ef9b). Live check: all three changed public files match their manifest shas. Next: 0058 (Consensus, Google DeepMind SAFE, Julius AI), drafting privately; 0059 (Browser Use candidates) queued.

## 2026-10-17 — Deploy note
Decision 0058 (Google DeepMind SAFE: VeriFact counted, 4 counted / 4 peer-reviewed, 66 / B- unchanged; Consensus: nothing new, recheck note closed, 62 / B; Julius AI: nothing counted, Insufficient evidence) was deployed to production as dpl_EozqasPE7Lfw5DxJVYfKdA73HAxW (commit db88ca5). Live check: all 44 live public files match the manifest shas. Next: 0059 (Browser Use remaining candidates), drafting privately.

## 2026-10-17 — Deploy note
Decision 0059 (Browser Use: AgentTell, Privacy Practices of Browser Agents and BreakingWeb counted; 11 counted / 3 peer-reviewed; grade B → A; overall 51 unchanged; recheck note removed) was deployed to production as dpl_EeLkre34exGXT5oFraKx3cdreqoS (commit f384a28). Live check: all four changed public files match their manifest shas. The main 0052 citation-sweep follow-ups (0053–0059) are now complete. Remaining items: Eye recheck after 2027-01-01, AMCIS (Gemini) and Julius J2 full texts, and the outstanding recheck notes on other entries.

## 2026-10-18 — Decision 0060 applied and deployed
Decision 0060 (traffic measurement) approved as recommended (D1a–D7). Added "Privacy and measurement" section (#privacy) to methodology.html; footer "Privacy" link on all pages via scripts/apply_design.py; changelog row; Google Search Console verification file public/google4abc2024514dc361.html added exactly as issued by Search Console (no page HTML changes). No analytics script added; no score or grade changes. Commit 27380e1. Deployed to production as dpl_FD9tCYz2oyMFJ6uLDKycuz4NyJXQ via Vercel API (39 files uploaded, 45 in deployment). Live check: all 45 files match manifest-0060 sha1; verification file returns 200 text/html with exact content. Next: Remington clicks Verify in Search Console and submits sitemap.xml.

## 2026-10-18 — Decision 0060 verification file replaced
The first Search Console verification file (public/google4abc2024514dc361.html) was for the wrong Google account; removed and replaced with public/google4c18d564fd1acb53.html (exact Google content, no page HTML changes). decisions/0060 note updated. No score, grade or page content changes.

## 2026-10-18 — Deploy note (0060 verification file replacement)
Commit 0465a1a deployed to production as dpl_4K7Y7kRHhW5hLcujx9NYP27fsDiZ via Vercel API (1 file uploaded, 45 in deployment; old verification file excluded). Live check: all 45 files match sha1; /google4c18d564fd1acb53.html returns 200 text/html with exact content; /google4abc2024514dc361.html now returns 404. Next: Remington clicks Verify in Search Console (correct account) and submits sitemap.xml.

## 2026-10-18 — Deploy 0061 (agent distribution)
- Deployed commit 803fc59 via Vercel MCP: dpl_3VbVr4JoKpHv1b9Ep8QFS5xUmDK1 (production), 45 files uploaded, 49 files in deployment.
- Verified: 49/49 live sha1 match; content-types OK (json, csv, xml, text/plain, html); google4c18d564fd1acb53.html 200.
- Entry pages: 34 live agents/*.html = 34 export ids = 34 sitemap agent URLs (38 URLs total). Earlier "33" was a miscount; no mismatch.
- 2026-10-18 02:55 EDT: Decision 0065 approved by Remington. Agent update feed for the current URL: data/changelog.yaml (57 rows, backfilled from changelog.html and agents/*.yaml git history; 0 unrecovered values) now generates changelog.html's table (existing 56 rows identical), updates.json (JSON Feed 1.1) and updates.xml (Atom), 67 items with stable tag: ids, before/after, as_of and disclaimer. Citation guidance and feed links in llms.txt and agents-data.html; feed alternate links on index, changelog, data page. check_export.py feed checks added. No score/grade/status changes. Not deployed.
- 2026-10-18 02:50 EDT: Deployed 0065 (commit 2b66ffa) via Vercel MCP: dpl_6jqkFiJ2q3gzEfg6QMgRfF9iGb3B (production); 6 files uploaded, 51 in deployment. Verified 51/51 live sha1 match; updates.json 200 application/json (JSON Feed 1.1, 67 items); updates.xml 200 application/xml (well-formed Atom, 67 entries); changelog 0065 row live; citation guidance live in llms.txt and agents-data.html; google4c18d564fd1acb53.html 200.
- 2026-10-18 03:02 EDT: Decision 0066 approved by Remington (D1–D8). Implemented 3 comparison pages (public/compare/), with category labels capitalized in 16 agents/*.yaml (display only; agents.json differs only in category), changelog row 2026-10-18-0066 (58 rows, 68 feed items), sitemap 41 URLs, llms.txt Comparisons section, Compare links on index/methodology, and compare checks in check_export.py. Checks: check_scores 0 errors/5 warnings; export 0 errors; schema valid; no-JS ok; axe clean and no overflow at 375/1280 light/dark. Not deployed (D9 pending).
- 2026-10-18 03:15 EDT: Deployed 0066 (commit bef802c) via Vercel MCP: dpl_8VnsavR9i2m4qB4wGsWK1hbtCJ8W (production); 13 files uploaded, 54 in deployment. Verified 54/54 live sha1 match; 3 /compare/ pages 200; agents.json/csv updated; sitemap 41 URLs (3 compare); llms.txt Comparisons present; updates.json/xml 68 items incl. 2026-10-18-0066; Compare links on / and /methodology.html resolve; Google verification file 200.
- 2026-10-18 03:28 EDT: Decision 0067 approved by Remington (D1a–D9a, D5b, D7b). Implemented generated /citing.html, with examples from data (Aider 52/A; AutoKaggle insufficient) and the generated CITATION replacing the typed-in OpenHands example on the data page, llms.txt, compare pages and updates.json. Also: data-page licence trimmed to a summary plus link; methodology and llms.txt links; sitemap 42 URLs; changelog row 2026-10-18-0067 (59 rows, 69 feed items); extended banned-word checks; pre CSS rule. Checks: scores 0 errors/5 warnings; export 0 errors; schema valid; no-JS ok; axe clean and no overflow at 375/1280 light/dark. agents.json/csv unchanged. Not deployed (D10 pending).
- 2026-10-18 03:29 EDT: 0067 follow-up: restored the per-entry evidence blocks on the compare pages (dropped by an operator-precedence slip in 0da91e1, never deployed) and added a check that requires them. All checks re-run: 0 errors/5 warnings, export 0 errors, schema valid, no-JS ok, axe and overflow clean. Not deployed.
- 2026-10-18 03:30 EDT: 0067 second follow-up: removed the doubled <ul> around compare-page uncertainties (axe list violation introduced in 1c3b7d9, never deployed) and added a nested-list check. Re-run: scores 0 errors/5 warnings, export 0 errors, schema valid, no-JS ok, axe and overflow clean on citing/agents-data/methodology/3 compare pages at 375/1280 light/dark. Not deployed.
- 2026-10-18 03:36 EDT: Deployed 0067 (commit 82fbe97) via Vercel MCP: dpl_9t49qEtxtDUGFjgGbsKQsfv2q4KH (production); 12 files uploaded, 55 in deployment. Verified 55/55 live sha1 match; /citing.html 200; How-to-cite links on methodology, the data page and llms.txt present; sitemap 42 URLs incl. citing.html; updates.json/xml 69 items incl. 2026-10-18-0067; compare pages show evidence blocks (2/7/9), no nested lists; Google verification file 200.
- 2026-10-18 20:57 EDT: Decision 0069 approved by Remington (D1a–D7a). Changes: shared footer (methodology fixed) plus a check; 7 scopes from published summary first sentences; grade_note for aider, swe-agent, devin, copilot, storm (documented; replaces a stale 'Grade B rather than A' sentence on the SWE-agent page and 'preprint' on Aider); vercel.json Atom header for /updates.xml only; 2 compare titles shortened; citing description at 137 chars; new warnings; changelog row 2026-10-18-0069 (60 rows, 70 feed items). check_scores: 0 errors, 0 warnings, 5 documented. Scores and grades unchanged (agents.json differs only in scope/grade_note). Title >70 warnings remain on 4 generated pages (suffix). Not deployed (D8 pending).
