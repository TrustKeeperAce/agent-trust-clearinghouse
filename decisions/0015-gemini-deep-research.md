# Decision 0015: Gemini Deep Research

**Status: APPROVED by Remington, 2026-10-17.** Publish with overall score 63, evidence grade B, using the proposed public wording exactly. Version-scope reading confirmed: tests of earlier Gemini Deep Research versions (2.5 Pro, 3 Pro) count, as in Decision 0003, with the current version (3.1 Pro) disclosed.

Numbering: drafted privately as 0016 (the private batch-2 shortlist used 0015 and was not added to the repo); published as the next repo number, 0015. The batch-2 shortlist (approved 2026-10-17) chose this candidate.

Accessed 2026-10-17 (America/New_York). Category: Research. Commercial (Gemini app feature and Gemini API agent). Batch 2, candidate 1 (private shortlist, approved 2026-10-17).

## Draft entry summary
Proposed: **overall 63, evidence grade B**, 7 independent performance sources (2 peer-reviewed).
Draft public wording: "Gemini Deep Research is a Google feature, in the Gemini app and as a Gemini API agent, that plans multi-step web research and writes cited reports. In independent evaluations (DeepResearch Bench, ICLR 2026; Mind2Web 2, NeurIPS 2025; five preprints), it ranked at or near the top on report quality and coverage, but completed fewer hard search tasks than the leader, and a larger share of its citation links did not resolve or did not exist. Most tests used 2025 versions (Gemini 2.5 Pro and 3 Pro); one tested the Gemini 3.1 Pro API agent. Several benchmarks used a Gemini model as the AI judge. Overall score 63. Informational only; not a guarantee, endorsement, or certification."

## 1. What happened with sources
All PDFs below were downloaded and the relevant sections were read (none paywalled).

**Counted: independent performance sources (7)**
| # | Source | Venue | Version / date tested | Key Gemini results | Flags |
|---|---|---|---|---|---|
|1|DeepResearch Bench, Du et al. (USTC) https://proceedings.iclr.cc/paper_files/paper/2026/file/465f22be10e07b301c6ed58f0472f704-Paper-Conference.pdf (arXiv 2506.11763)|ICLR 2026 (peer-reviewed)|Gemini-2.5-Pro DR, 27–29 Apr 2025|RACE 48.88, 1st of 4 deep research agents (ODR 46.98); 111.21 effective citations; citation accuracy 81.44% (Perplexity 90.24%)|**Gemini-2.5-pro was the RACE judge, Gemini-2.5-flash the FACT judge, and RACE reference reports were Gemini DR outputs**: a possible self-preference bias favoring Gemini|
|2|Mind2Web 2, Gou et al. (OSU; some Amazon co-authors) https://arxiv.org/abs/2506.21506|NeurIPS 2025 D&B (peer-reviewed; venue already confirmed in D0003)|Apr–Jun 2025 (web UI)|Partial completion 0.45, full success 0.18, Pass@3 0.30, 7.4 min (ODR 0.54/0.28/0.40; human 0.79/0.54)|Authors modified the prompt because Gemini DR "occasionally neglect[s]" source requirements|
|3|ReportBench, Li et al. (ByteDance) https://arxiv.org/abs/2508.15804|Preprint|2025 (web UI)|Cited-statement match 72.94% (ODR 78.87%); non-cited factual accuracy 92.21%; reference precision 0.145, recall 0.036|Authors' company sells Doubao DR (not evaluated in this paper); counted with disclosure|
|4|Rao, Wong, Callison-Burch (UPenn) https://arxiv.org/abs/2604.03173|Preprint, under review|DRB outputs, Apr 2025|11,309 URLs: 18.5% non-resolving, **13.3% hallucinated**, the highest of 10 systems (ODR 10.1%/3.5%)|Reuses DRB-generated outputs; a separate study and analysis, counted once|
|5|DeepResearch Bench II, Li et al. (USTC) https://arxiv.org/abs/2601.08536|Preprint|Systems as of Nov 2025|Gemini-3-Pro DR 44.60 (2nd of 8, behind o3 DR 45.40); 2.5-Pro 41.98 (3rd)|Same team as #1; Gemini-2.5-Pro judge (chosen for its human alignment)|
|6|DeepResearchEval, Wang et al. (Infinity Lab, Shanda Group; NTU) https://arxiv.org/abs/2601.09688|Preprint|Gemini-2.5-Pro DR, Aug–Sep 2025|Quality 8.51/10, 1st of 9; factual ratio 76.62% (2nd; Manus 82.30%); 4.16 wrong statements per report|Gemini-2.5-pro primary judge; GPT-5 cross-judge kept Gemini 1st (rank change 0). Agent built on MiroFlow|
|7|Asthana et al. (Deccan AI Research) https://arxiv.org/abs/2605.17554|Preprint (v3, 25 Jun 2026)|**Gemini 3.1 Pro deep-research via Gemini Interactions API (current generation)**|70 expert consulting tasks graded by human experts: VRS 52.6 (2nd of 3; o3 61.4, Claude 38.5); strict accept 12.9%; most criterion-zeros (74/350); highest perfect-verifier rate (14.3%); "system collapse" failures|Only 3 agents; API, not the app; Deccan is a data/eval vendor, not a competing DR product (affiliations not checked further)|

**Other sources (not counted)**
- SafeBreach "Invitation Is All You Need" https://www.safebreach.com/blog/invitation-is-all-you-need-hacking-gemini/ and the notification-injection follow-up https://www.safebreach.com/blog/gemini-voice-assistant-prompt-injection-exploit/ : prompt injection against the Gemini assistant, disclosed to Google, which reports mitigations (Nov 2025). Not Deep Research specifically.
- Tenable TRA-2025-23 https://www.tenable.com/security/research/tra-2025-23 : Gemini Search Personalization prompt injection (Medium); Google rolled the model back.

**Excluded**
- TTD-DR https://arxiv.org/abs/2507.16075 : Google Cloud AI Research authors, so it is vendor work.
- DRACO https://arxiv.org/abs/2602.11685 : by Perplexity, which ranks its own product first (competitor promoting itself). For reference it reported Gemini DR (deep-research-pro-preview-12-2025) at 59.0%.
- Vendor claims (Google blog 21 Apr 2026 https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/ ; API docs https://ai.google.dev/gemini-api/docs/deep-research): used for version history and scope only.

**Disputes/legal search:** no lawsuit, regulator action or CVE specific to Gemini Deep Research found. The AI Hallucination Cases database (https://www.damiencharlotin.com/hallucinations/) lists court filings naming "Gemini" or "Gemini Pro" generally, none naming Deep Research. These are not attributed to this entry.

**Version history (vendor):** 2.5 Pro (Apr 2025) → 3 Pro (late 2025; API agent deep-research-pro-preview-12-2025, deprecated, shuts down 23 Oct 2026) → Gemini 3.1 Pro "Deep Research" and "Deep Research Max" (21 Apr 2026).

## 2. What the rules say (methodology v0.1, D0010)
- ≥3 independent performance sources; competing-method or competing-company authors count, with disclosure. Self-promoting competitor studies (DRACO) do not count. Vendor studies (TTD-DR) do not count.
- **Scope/version:** a source counts only if it tested the product, version and scope in the entry. Precedent: D0003 counted 2025 tests of OpenAI Deep Research despite later model changes, disclosed as an uncertainty. D0008 excluded Open Interpreter tests because the product itself was rewritten. Here the product is continuous and only the underlying model changed, so the D0003 reading applies. The entry scope is defined as "Gemini Deep Research (app and API agent), versions tested 2025–2026", with 3.1 Pro disclosed as current.
- **Grade:** 7 sources but only 2 peer-reviewed (A needs ≥3), so **B** (7+ without meeting the A conditions). It does meet the A recency condition (#7, June 2026, current version).
- **Evidence factor guide:** B = 70–84. The proposed 72 sits low in the band because of the judge-bias and older-version issues.

## 3. Proposed scores (judgment calls)
- **Completion 60:** leading report quality (#1, #6) and coverage, but weaker task success than ODR on Mind2Web 2 (0.18 vs 0.28), the highest hallucinated-URL rate (#4), and low strict acceptance on expert tasks (#7). Comparable overall to ODR (60).
- **Disputes 65:** no Deep-Research-specific legal, regulatory or security finding; Gemini-family prompt-injection disclosures were mitigated. Deep Research can read Gmail/Drive/uploads in the app (vendor docs), so the family-level injection risk is relevant. Same as ODR (65).
- **Adherence 55:** documented lapses in citing sources (#2) and a cited-statement match of 72.94% (#3); vendor-documented tool and usage limits; no independent limit test. 5 below ODR because of the source-instruction lapse.
- **Evidence quality 72:** 7 sources, 2 peer-reviewed, 1 on the current version; 3 use a Gemini judge.
- **Math:** 0.30×60 + 0.20×65 + 0.25×55 + 0.25×72 = 18 + 13 + 13.75 + 18 = **62.75, rounded to 63**. No .5 tie.
- **Directory placement:** between ODR (65) and Perplexity (54).

## 4. Risks/uncertainties
1. **Gemini-as-judge:** in #1, #5 and #6 a Gemini model graded Gemini outputs, and #1 used Gemini DR reports as references, which may inflate Gemini's quality scores. Mitigations: #6's GPT-5 cross-judge kept the ranking; #7 used human experts and still ranked Gemini 2nd of 3. Report-quality factor notes rely partly on these.
2. **Version scope:** 5 of 7 sources tested 2.5 Pro (2025), #5 tested 3 Pro, and only #7 tested 3.1 Pro (via the API). Under a strict "current version only" reading the count would be 1, giving **Insufficient evidence**. This packet uses the D0003 reading instead. **Remington should confirm this reading explicitly.**
3. **Correlated sources:** #1 and #5 share authors, and #4 reuses #1's outputs, so three of the seven come from one data family. Each is counted once (D0010: "each study counts once"), but they are not fully independent of each other.
4. **Competitor affiliations:** ByteDance (#3) and Shanda/MiroMind-linked tools (#6) are disclosed. Deccan AI's commercial ties were not investigated.
5. **Preprints:** 5 of 7 are unreviewed. Venue status for #3–#7 was checked only via the arXiv page (no venue listed).
6. Deep Research Max was not independently tested.

## 5. Recommendation
**APPROVE** with overall score **63**, evidence grade **B**, and the draft wording above, *provided* Remington confirms the version-scope reading (Risk 2).
- If the strict current-version reading is preferred instead: **MORE INFO / Insufficient evidence** until 2 more independent tests of the 3.1 Pro agent appear.
- Once approved, a separate implementation step adds the YAML/page and changelog (not done here).

## 6. Plain-English terms
- **RACE / FACT:** DeepResearch Bench's report-quality score and citation-checking method.
- **Hallucinated URL:** a cited link that never existed. **Non-resolving:** a link that doesn't work, whether dead or invented.
- **Pass@3:** solved in at least one of three tries.
- **LLM judge / self-preference:** an AI grading answers may favor outputs from its own model family.
- **Peer-reviewed vs preprint:** checked by outside experts before publication, vs posted without review.
- **API agent vs app:** the developer version vs the consumer Gemini app; they can behave differently.
