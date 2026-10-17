# Decision 0017: Elicit

**Status: APPROVED by Remington, 2026-10-17.** Publish with overall score 68, evidence grade A, **7 counted independent performance sources**. Confirmations:
- (A) Scope: "Elicit, all tiers, tested mainly on paid tiers".
- (B) Tests from 2023–2026 count (continuity reading).
- (C) #6 Hilkenmeier et al. and #8 O'Rourke et al. are listed but **not counted**, labelled "abstract only, not fully reviewed". #5 Lagisz et al. counts, with the free-accounts disclosure.

**Recheck without #6/#8 (2026-10-17):**
- Completion basis now uses search 17.6–39.5%, 1 of 59 and 158 of 5,285; extraction 77–92%. Still 55, since weak search and good extraction are unchanged.
- Disputes 80 and adherence 55 are unchanged (neither relied on #6/#8).
- Evidence 85: 7 sources, 6 peer-reviewed, #9 recent. Still grade A, lowest end of the A band.
- Overall 0.30×55 + 0.20×80 + 0.25×55 + 0.25×85 = 67.5, rounded half up to **68**. Unchanged.

The table below is the original 9-source draft; counts in the entry follow the approved confirmations.

Accessed 2026-10-17 (America/New_York). Category: Research. Batch 2, candidate 3.

## Draft entry summary
Proposed: **overall 68 (67.5 rounded half up), evidence grade A**, 9 independent performance sources (8 peer-reviewed, 1 preprint).
Draft public wording: see `summary` in the YAML. It says searching is weak, extraction mostly agrees with humans with some errors, screening is moderate, and Elicit can assist but not replace reviewers; it notes paid tiers 2023–2026 and gives overall 68 with the standard disclaimer.

## Scope (decision point A)
- **Covered:** Elicit as a product (search/Find Papers, Review/Systematic Review workflow, data extraction), all tiers.
- Every independent test used a paid or subscription tier, or did not state the tier:
  - Pro: Lau, Wei.
  - Plus: Lagisz.
  - Subscription/credits: Andersen.
  - Tier not stated: the others.
- The free Basic tier is not tested separately, and the entry says so.
- Alternative: limit the scope to the paid systematic-review features only. The count is the same, since all sources fit that scope.

## 1. What happened with sources
Read in full: PMC12483133, BMC, PMC12257877, PMC12462964, the Research Synthesis Methods (RSM) paper, the Acta dermatology paper (PMC13010132) and the medRxiv preprint. **Abstract only:** Social Science Computer Review (SSCR) and Western Journal of Nursing Research (WJNR); both full texts are paywalled or would not load.

| # | Source | Venue | When / tier | Key result | Flags |
|---|---|---|---|---|---|
|1|Lau et al. (York) https://pmc.ncbi.nlm.nih.gov/articles/PMC12483133/|Cochrane Evid Synth Methods 2025 (peer-reviewed)|Pro, Review mode, 2024–25|Search sensitivity **39.5%** (25.5–69.2%) vs 94.5% traditional; precision 41.8% vs 7.55%; found some unique studies|No conflicts declared|
|2|Bernard et al. (Besançon/Montréal) https://link.springer.com/article/10.1186/s12874-025-02528-y|BMC Med Res Methodol 2025|Searches **19–20 April 2023** (early product)|Found **17.6%** of included studies (+3 new); identical searches gave 246/169/172 results; summary cited the review protocol|Oldest version|
|3|Andersen et al. (Copenhagen) https://pmc.ncbi.nlm.nih.gov/articles/PMC12257877/|Cochrane Evid Synth Methods 2025|Extraction 5 July 2024, high-accuracy mode|Precision/recall/F1 **92%**; review-specific variables 77%; 4 confabulations; similar to ChatGPT|No conflicts declared|
|4|Bianchi et al. (Eastern Switzerland) https://pmc.ncbi.nlm.nih.gov/articles/PMC12462964/|Cochrane Evid Synth Methods 2025|Aug–Sep 2024, 20 RCTs|Equal 20.7%, partially equal 45.7%, more 29.3%, deviating 4.3%; intervention effects 95% only partial|No conflicts declared|
|5|Lagisz et al. (UNSW) https://doi.org/10.1017/rsm.2026.10080|Research Synthesis Methods 2026|2025, Plus; high-accuracy re-test 26 June 2025|70/90 prompts above 87% in development, lower on new articles; 90% value agreement across accounts (quotes 46%, reasoning 30%); high-accuracy mode 77% value match|**Partly independent:** temporary free Plus access from Elicit; Elicit had no other role, per the authors|
|6|Hilkenmeier et al. (Hochschule Fresenius/Potsdam) https://journals.sagepub.com/doi/10.1177/08944393251404052|Social Science Computer Review, Dec 2025|Not stated (abstract)|602 data points: **81.4%** vs human 86.7% (not significantly different); where both agreed, 100% correct|Abstract only|
|7|Vyas et al. (Cardiff) https://pmc.ncbi.nlm.nih.gov/articles/PMC13010132/|Acta Derm Venereol 2026|2025 (accepted Jan 2026)|1 of 59 search results met criteria; 13 incorrect extracted results across 24 articles; JADAD inputs wrong in 5/24; location wrong in 5/24|Two authors receive royalties for the DLQI (the dermatology quality-of-life index the review studies); not Elicit-related|
|8|O'Rourke et al. https://doi.org/10.1177/01939459261451723|West J Nurs Res 2026|Not stated (abstract)|Reference-list match **3.7%** (Consensus 21.3%)|Abstract only|
|9|Wei et al. (CAMH/Toronto) https://www.medrxiv.org/content/10.64898/2026.10.02.26364621v1|medRxiv preprint, Oct 2026|**Pro tier, Dec 2025–May 2026 (current)**|Search 158/5,285; screening sensitivity 0.71/0.78, precision 0.38 (false-positive skew); extraction 85% helpful, 79% fully accurate; 3.16 h end to end|Not peer-reviewed|

**Excluded:**
- Elicit's own evaluation https://elicit.com/blog/how-we-evaluated-elicit-systematic-review (93.6% recall, 94–99% extraction): vendor.
- Already-reviewed tool comparisons not re-checked in full for this packet (REACT librarian review; IEEE ICARC 2025 multi-tool SLR): not counted.

**Security/privacy/disputes:** no lawsuits, regulator actions, CVEs, GitHub advisories or reported data incidents found. Vendor statements only:
- Uploaded PDFs are private: https://support.elicit.com/en/articles/14758043-privacy-for-uploaded-papers
- No training on enterprise data, and SOC 2 Type II (vendor claim): https://elicit.com/industries/policy
- Data Processing Addendum with 72-hour breach notice: https://elicit.com/operations/dpa

None of these has been independently audited in public.

## 2. What the rules say (0010)
- ≥3 independent performance sources testing the product/scope. All 9 test Elicit itself.
- **Partly independent (#5):** counted and labelled, as with Pactum's thesis (D0005).
- **Version (decision point B):** the product is continuous but changed a lot:
  - credits switched to subscription in July 2024;
  - high-accuracy became the default in May 2025;
  - the Systematic Review workflow was added.

  Under the D0003/D0015/D0016 continuity reading, all 9 count. #9 (2025–26) and #7 (2025) are recent.
- **Grade:** 9 sources (≥7), 8 peer-reviewed (≥3), and ≥1 testing the current version within 12 months (#9). That gives **A**. The evidence factor must be ≥85, so 85 is proposed.
- Strict alternatives:
  - Drop #2 (2023 version) and the abstract-only #6 and #8: 6 sources, so grade B.
  - Also exclude #5: 5 sources, still B.

## 3. Proposed scores (judgment calls)
- **Completion 55.** Results depend on the task:
  - Search is weak: 3.7–39.5% of studies found.
  - Screening is moderate: sensitivity 0.71–0.78.
  - Extraction is good: 79–92%, but complex variables are only partly right.
- **Disputes 80.** No disputes or security issues found; fabrications are counted under completion. Same as SAFE (80).
- **Adherence 55.** Repeat runs vary, and it ignored output constraints (multiple answers where one was required, default location). Privacy and no-training commitments are vendor-only.
- **Evidence 85.** Strongest base in the directory, but samples are small and mostly health sciences, and two sources are abstract-only.
- **Math:** 0.30×55 + 0.20×80 + 0.25×55 + 0.25×85 = 16.5 + 16 + 13.75 + 21.25 = **67.5, rounded half up to 68**. Directory order: Elicit 68 would rank **first**, above SAFE 66.

## 4. Risks/uncertainties
1. **Top rank:** Elicit would lead the directory mainly because of its strong evidence and clean disputes record, despite weak search. Scores don't measure fitness for any one task, and readers may misread a high overall score.
2. **Exact .5:** 67.5 → 68, as with Perplexity and SAFE. Under round-half-down it would be 67, still first.
3. **Abstract-only sources (#6, #8):** method and results are only partly verified. Remington may prefer to count only sources read in full; that gives 7 sources, still grade A.
4. **Tier and version:** the free tier is untested; results from 2023–2024 may not reflect the current product.
5. **Domain:** most studies are biomedical; generalization to other fields is uncertain.
6. Venue dates were checked via publisher pages, Europe PMC and Crossref. Vyas et al.'s exact test dates are not stated.

## 5. Recommendation
**APPROVE** at **68**, grade **A**, scope = Elicit (all tiers, tested mainly on paid tiers), with these confirmations:
- (A) Scope wording.
- (B) Continuity reading for 2023–2026 tests.
- (C) Count the two abstract-only sources and the partly independent #5 with labels.

If C is declined (#6 and #8 not counted): **7 sources, still grade A**, and scores unchanged. If B is strict (only tests after July 2024): #2 is dropped, leaving 8 sources, still A.

## 6. Plain-English terms
- **Sensitivity (recall):** share of the relevant studies that Elicit found.
- **Precision:** share of what Elicit returned that was actually relevant.
- **Screening:** deciding which studies meet a review's inclusion rules.
- **Data extraction:** pulling specific facts (sample size, results) from papers.
- **Confabulation:** a made-up detail presented as fact.
- **High-accuracy mode:** an Elicit setting meant to improve extraction; it became the default in May 2025.
