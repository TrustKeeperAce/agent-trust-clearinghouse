# Decision packet 0077 — Evidence pass 3: AutoKaggle, Loki, UI-TARS Desktop

**Status: APPROVED by Remington, 2026-10-19: D1a, D3a, D4a, D5a as recommended (D6: no pass for Pactum, Clay, OpenFactCheck and Fellou; recheck at the monthly review); implementation and changelog row approved. Deploy needs separate approval.**

Implementation notes (2026-10-19): Data: agents/autokaggle.yaml, agents/loki.yaml, agents/ui-tars-desktop.yaml (`last_reviewed` 2026-10-19; this decision added to each `decision_packet`). Scores stay null and all three stay Insufficient evidence. AutoKaggle: DS-Lighting added as `other (re-implementation)` and LightAutoDS-Tab as `other (copied figures)`; other 0 → 2; one sentence on the DS-Lighting re-implementation added to the completion note (marked not counted); the Tree-Notebook recheck uncertainty replaced with the 19 Oct screen result and the list of papers not read in full. Loki: WildSEEK and When the Chain Breaks added as `other (used as a tool)`, each noting that Loki's own accuracy was not measured; other 1 → 3; first uncertainty replaced; summary unchanged (the optional sentence was left out so the records do not read as support for the tool). UI-TARS Desktop: VPI-Bench added as `not counted (model only)` and to the adherence context; first uncertainty replaced; issue 1854 not recorded. Changelog row 2026-10-19-0077: entry_update for the three entries.

*Per-entry drafts referenced below were kept as private working notes and are summarised in this record.*

**Outcome in one line (if recommended options are approved):** no grade or score changes. AutoKaggle (2 counted), Loki (2) and UI-TARS Desktop (1) stay **Insufficient evidence**. Only source records, notes and uncertainties are updated.

## 0. Selection
Remaining Insufficient entries (counted): autokaggle 2, loki 2, ui-tars-desktop 1, pactum 1, clay 0, openfactcheck 0, fellou 0.

Picked (3):
- **AutoKaggle:** 1 source short. 0042 left a citation recheck (Tree-Notebook unscreened), and Semantic Scholar now lists 86 citing papers, compared with 53 in OpenAlex for 0042.
- **Loki:** 1 source short. It is an open-source tool that other researchers can run, so new outside tests are plausible.
- **UI-TARS Desktop:** the highest public interest of the remaining entries (a widely used open-source ByteDance project, about 25k GitHub bookmarks). It needs 2 more sources, and the computer-use security literature is active.

Not picked:
- **Pactum** (1, partly independent thesis): commercial negotiation service with no public benchmark, so it is unlikely to reach 3.
- **Clay** (0): commercial data-enrichment tool with no independent benchmark found in earlier passes. It would need 3 new sources.
- **OpenFactCheck** (0): its results depend on how users configure it, and it would need 3 new sources. The 2.0 alpha has not been assessed.
- **Fellou** (0): CAP stays excluded (0031, shared author). No new independent lead was seen.
- **No 4th pick:** none of the above has a realistic path to 3 counted sources in this pass.

## 1. What happened (facts and sources)
Searches ran early on 19 Oct 2026; the last batch was about 02:38–02:50 ET. Sources used: Semantic Scholar (citations endpoint, which worked for AutoKaggle and Loki; snippet search returned HTTP 429 every time), OpenAlex, arXiv full text (pdftotext), ACL Anthology, AAAI OJS, SBC OpenLib, GitHub and web search. Every source recorded below was read in full unless flagged.

### AutoKaggle
- **DS-Lighting** (Fan Liu, Hao Liu; HKUST-Guangzhou; arXiv 2608.28590, Aug 2026, preprint):
  - The paper says DS-Lighting "natively integrates and reproduces seven state-of-the-art data-science agents" and that "all agents are instantiated through the same data, workflow, execution, and evaluation layers". This is a **re-implementation inside their harness**.
  - AutoKaggle (manual workflow) DABench overall average: 0.78493 with DeepSeek-V3.1-Terminus and 0.81482 with the second model (probably qwen3.5-plus; the column-to-model mapping was not fully checked).
  - 123.1K tokens per task (24.21× ReAct); 22.62 minutes per task, the slowest of the agents timed.
  - No author overlap with AutoKaggle.
- **LightAutoDS-Tab** (Sber AI Lab / ITMO; arXiv 2507.13413; AAMAS 2026 demo): "We directly include the normalized results from the aforementioned work, including the performance of the AutoKaggle and AIDE frameworks with GPT-4o". The figures are copied from another paper, so this is not a new test.
- **Tree-Notebook** (Findings ACL 2026, doi 10.18653/v1/2026.findings-acl.783): the full PDF only describes AutoKaggle. This resolves the 0042 recheck note.
- **DATAEXPLAINER** (UFLA; SBBD 2026): the full PDF cites AutoKaggle in related work and compares only with Data Interpreter.
- **21 further open citers** only describe AutoKaggle or list its reported numbers (list in `autokaggle.md`).
- **Not fully read:**
  - PACE (KDD 2026; ACM 403). Its abstract and the GitHub README show ML-Master and AIDE, not AutoKaggle.
  - AutoDS-Tools, "Towards Automated Integration…" (AAMAS 2026; 403). The abstract does not mention running AutoKaggle.
  - Not read at all: AutoMind (IEEE Access), PiML, CodeViz, AutoCluster, a Nature paper (10.1038/s41586-026-10658-6) and a bioRxiv benchmark.

### Loki
- **Semantic Scholar rerun** (19 Oct): 27 citing papers, the same set as on 17 Oct. OpenAlex added nothing: the arXiv record shows 0 citations, and a full-text search for "OpenFactVerification" returns only the Loki paper.
- **WildSEEK** (Bocconi / Stanford / ITU Copenhagen; arXiv 2608.30683, 31 Aug 2026, preprint) uses Loki (Serper plus GPT-5.4-mini) as its tool for measuring the factuality of language-model answers.
  - It does not measure Loki's own accuracy. Its human validation covers a separate LLM-as-a-judge.
- **When the Chain Breaks** (NTU Singapore / Bosch; Computer Graphics Forum, EuroVis 2026; arXiv 2603.21286) builds Loki into a visual tool for diagnosing chain-of-thought errors. Loki itself is not tested.
- **Describe or cite only:**
  - Now read in full, after being abstract-only on 17 Oct: StructFact (Findings ACL 2025), Deloitte SemEval-2025 and UFO (AAAI-26).
  - Re-checked: CAAFC 2605.12436, VeriTaS, DeepResearch-9K and 2511.21401.
- **Still abstract-only:** five closed-access papers (Greenwashing, ICAIDE, ICWS, mice.70063, KnoSys DCHD).

### UI-TARS Desktop
- **VPI-Bench** (NUS; ICLR 2026; arXiv 2506.02456v2, Appendix G) tested the UI-TARS 7B **model**.
  - The model attempted the injected malicious task in 78.95% (Amazon) and 70% (Messenger) of cases. Attack success was 0% because it could not complete the steps.
  - The app is not named, so this result is model-only.
- **GitHub issue 1854** (LuciferForge, 27 Mar 2026) makes two general security claims with no method or results and links to a paid ($29) report. It is promotional and cannot be checked.
- LexBench-Browser still has no published Agent TARS result. Mobile GUI Agents under Real-world Threats (2507.04227) tests the UI-TARS-1.5 model only. Two MCP and AI-infrastructure measurement papers (2605.20051, 2509.25292) do not mention UI-TARS or @agent-infra.
- The vendor's Agent TARS figures (WebVoyager 84.8, BrowseComp 2.3) are not counted.
- Semantic Scholar snippet search was rate limited, so coverage is incomplete.

## 2. What the rules say (Scoring rules v0.1, unchanged)
- An overall score needs at least 3 **independent performance sources**. These are tests that report their method and results.
- Reviews, commentary, use of a product as a tool, competitor benchmarks and vulnerability listings are **other** sources.
- A source counts only if it tested the product, version and scope of the entry. Each study counts once.
- Re-implementations do not count: "The named product must be tested, so re-implementations are listed as other" (0042, AIRA-dojo).
- Copied numbers are not a new test. Re-scoring of the same outputs is other (0076, DualGraph).
- Model-only tests are context for app entries (0039 scope).
- Independent means not the vendor, a customer's staff, or a competitor promoting itself.
  - A source that shares authors with the developer is excluded (0031, CAP/Fellou).
  - Authors of a competing method count, with disclosure.
- 0058: an illustration that is not a measured test is not counted.
- Grades:
  - Insufficient: below 3 sources.
  - B-: 3–4.
  - B: 5–6.
  - A: 7+, with 3+ peer-reviewed and a current-version test within 12 months.
- Overall = 0.30 completion + 0.20 disputes + 0.25 adherence + 0.25 evidence, rounded half up. Evidence guide for B-: 55–69.

## 3. Proposed changes (before → after, recommended options)
| | AutoKaggle | Loki | UI-TARS Desktop |
|---|---|---|---|
| Counted | 2 → 2 | 2 → 2 | 1 → 1 |
| Peer-reviewed counted | 2 → 2 | 0 → 0 | 0 → 0 |
| Other | 0 → **2** (DS-Lighting re-implementation; LightAutoDS-Tab copied figures) | 1 → **3** (WildSEEK, When the Chain Breaks: used as a tool) | 4 → 4 |
| Not counted (model only) | — | — | 3 → **4** (+VPI-Bench) |
| Grade | Insufficient (unchanged) | Insufficient (unchanged) | Insufficient (unchanged) |
| Scores / overall | null | null | null |
| Text | Recheck uncertainty replaced; optional completion-note sentence | First uncertainty replaced; optional summary sentence | Adherence note (VPI-Bench as context); first uncertainty replaced |
| last_reviewed | 2026-10-17 → 2026-10-19 | 2026-10-17 → 2026-10-19 | 2026-10-17 → 2026-10-19 |

## 4. Risks and uncertainties
- **DS-Lighting is a judgement call.** Its figures look like a real run of the AutoKaggle workflow, but inside the authors' own harness. If DS-Lighting wraps the original AutoKaggle code rather than rewriting it, the case for counting it is stronger.
  - The paper says "reproduces" and "instantiated through the same … layers". It does not say whether the original code is used.
  - Counting it would give AutoKaggle 3 sources and B- (D1b/D2).
- **The DS-Lighting model mapping** for the 0.81482 column was not fully checked from the extracted PDF text.
- **Sources not fully read:**
  - AutoKaggle: PACE, AutoDS-Tools, AutoMind, PiML, CodeViz, AutoCluster, the Nature paper and the bioRxiv paper. Any of them could contain a run.
  - Loki: five closed-access citers.
  - UI-TARS: the Semantic Scholar snippet search did not run (429).
- **Loki "used as a tool" records** show outside adoption, not quality. Recording them as other must not read as support for the tool.
- **VPI-Bench's** "recommended deployment procedure" might have been the app, but the paper does not say so. It is treated as model-only.
- **Issue 1854** is left out of the record. If it is later backed by a public report with a method, it would be re-screened.
- **AutoKaggle** is unmaintained (last commit Dec 2024). Any new run tests old code, which is in scope but ageing.

## 5. Decision items
- **D1 AutoKaggle: DS-Lighting.**
  - a) Record it as other, not counted, as a re-implementation (0042 rule) (**recommended**).
  - b) Count it (preprint, independent, ran the AutoKaggle workflow). AutoKaggle would then have 3 counted (2 peer-reviewed). Grade-changing; see D2.
  - c) More info: ask the DS-Lighting authors whether the original AutoKaggle code is wrapped, then decide.
- **D2 AutoKaggle grade and scores (grade-changing; only if D1b).**
  - a) B-, with completion 50, disputes 80, adherence 50 and evidence 55: 15 + 16 + 12.5 + 13.75 = 57.25, overall **57**. Completion is 50 because AutoKaggle was below competing systems in VDSAgents, close to the baselines in SPIO, and averaged 0.78–0.81 in DS-Lighting (its rank among the seven agents was not checked). Disputes and adherence follow the Julius precedent (no disputes found; no adherence study).
  - b) B-, with completion 45: 13.5 + 16 + 12.5 + 13.75 = 55.75, overall **56**.
  - c) Reject: keep Insufficient.
  - Recommendation: not applicable if D1a is approved. If D1b is chosen, D2a.
- **D3 AutoKaggle record updates.**
  - a) Add LightAutoDS-Tab as other (copied figures). Replace the Tree-Notebook recheck uncertainty with the 19 Oct screen result and the list of unread papers. Set last_reviewed to 2026-10-19 (**recommended**).
  - b) No change.
- **D4 Loki.**
  - a) Stays Insufficient. Add WildSEEK and When the Chain Breaks as other ("used Loki as a tool; no measured test"), replace the first uncertainty and set last_reviewed (**recommended**).
  - b) No change; keep the 17 Oct note.
  - c) Count WildSEEK, giving 3 and B- (grade-changing; **not recommended**). WildSEEK measured language models with Loki and did not measure Loki. Scores are not drafted because the option is not recommended; they would need a follow-up item.
- **D5 UI-TARS Desktop.**
  - a) Stays Insufficient. Add VPI-Bench as model-only (not counted), add it to the adherence context, replace the first uncertainty and set last_reviewed. Do not record issue 1854 (**recommended**).
  - b) Same as a), but also record issue 1854 as other, labelled "not checkable, links to a paid report".
  - c) No change.
- **D6 Not picked** (Pactum, Clay, OpenFactCheck, Fellou): no pass. Recheck them at the monthly review. Fellou: CAP stays excluded (0031).
- **D7 Publishing:** implementing, adding a changelog row, committing, pushing and deploying each need separate approval. Not requested here.

## 6. MVP (smallest approvable set)
- Approve **D1a + D3a + D4a + D5a**: no grade or score change, only record and text updates. Data edits would be limited to `agents/autokaggle.yaml`, `agents/loki.yaml` and `agents/ui-tars-desktop.yaml`, plus `decisions/0077-evidence-pass-3.md`. The site would be regenerated and `check_scores.py` and `check_export.py` run.
- One changelog row (entry_update for the three entries) would follow, after separate approval.
- Narrowest option: D3a only (AutoKaggle recheck note resolved), with the rest deferred to the monthly review.

## 7. Plain-English terms
- **Insufficient evidence:** fewer than 3 qualifying independent tests, so no score and no grade.
- **Independent performance source:** a test by someone other than the maker that explains how it tested and what it found.
- **Counted:** the source tested this product, in the scope the entry covers.
- **Other source:** useful background that does not count toward the 3. Examples: commentary, copied numbers, re-implementations, or use of the product as a tool.
- **Re-implementation:** someone rebuilds the product's method in their own code. The result tests their version, not the released product.
- **Used as a tool:** a study relies on the product to measure something else and does not check how well the product itself works.
- **Model only:** a test of the AI model on its own, not the app that packages it.
- **Grade-changing:** a decision that would move an entry from Insufficient to a letter grade, or between grades.
- **Prompt injection:** hidden instructions in content the agent reads that make it do something the user didn't ask for.

*Informational only; not a guarantee, endorsement, or certification.*
