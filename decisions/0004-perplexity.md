# Decision 0004: Perplexity (citation and source-attribution scope)

**Status: APPROVED by Remington, 2026-10-16.** Publish with the drafted neutral summary exactly as written. Score 54, evidence grade B.

Approver guidance:
- Lawsuit wording is strictly "filed / alleges / pending".
- The robots.txt point is attributed to CJR as a suggestion.
- Rounding: interim practice is that an exact .5 rounds up (53.5 → 54). This is noted here and on the methodology page; it is not a core rule change.

## Final public summary
"Perplexity is a commercial AI answer engine; this entry covers only its citation and source-attribution behavior. In independent evaluations (CJR Tow Center, 2025; Findings of EMNLP 2023; DeepResearch Bench, ICLR 2026; DeepResearchGym, ICTIR 2026; Deep Research Comparator, WWW 2026 Companion; Mind2Web 2, NeurIPS 2025), results varied by product mode: its Deep Research mode scored comparatively high on citation accuracy, while news-attribution tests found a share of incorrect or syndicated citations. Several publishers have filed copyright lawsuits against Perplexity that are pending; these are allegations, not findings. Informational only; not an endorsement or certification."

---
Accessed 2026-10-16.

## Draft entry summary
Perplexity is a commercial product, entered in the Verification category. This entry covers **only** citation-backed answering and source attribution. Proposed overall score: **54/100**. Evidence grade: **B**. Independent sources: **6 performance** and **3 other** (court records).

## What happened
- **CJR Tow Center** (Feb 2025 tests; free Perplexity and Pro search):
  - Perplexity answered 37% of attribution queries incorrectly, the lowest error rate of the 8 tools tested.
  - Perplexity Pro cited syndicated copies for 3 of 10 Texas Tribune queries.
  - The free version identified all 10 paywalled National Geographic excerpts despite National Geographic blocking its crawler. CJR says this "suggests" Perplexity "may have disregarded" robots.txt.
- **Liu et al.** (Findings of EMNLP 2023; perplexity.ai, 2023): citation recall 68.7, the best of 4 systems; precision 72.7.
- **DeepResearch Bench** (ICLR 2026; Perplexity Deep Research): citation accuracy 90.24%, the highest among the deep-research agents listed.
- **DeepResearchGym** (ICTIR 2026; sonar-deepresearch API): citation precision 55.65, recall 99.22.
- **Deep Research Comparator** (WWW 2026 Companion): human annotators upvoted 90.72% of its text spans.
- **Mind2Web 2** (NeurIPS 2025 D&B): task success 0.08 for Pro Search and 0.15 for Deep Research.
- **Court records** (allegations only, all pending):
  - Dow Jones and NYP Holdings: copyright and trademark claims. The motion to dismiss was denied 2025-08-21.
  - Britannica and Merriam-Webster: copyright claims, filed 2025-09-10.
  - Chicago Tribune: filed 2025-12-04.
  - The New York Times: filed 2025-12-05.

## Sources checked
| Source | Type | Mode | URL |
|---|---|---|---|
|CJR Tow Center|Independent, performance (journalism)|Free + Pro|cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php|
|Liu et al. 2023|Independent, performance (peer-reviewed)|perplexity.ai|aclanthology.org/2023.findings-emnlp.467/|
|DeepResearch Bench|Independent, performance (ICLR 2026)|Deep Research|proceedings.iclr.cc/…465f22be…Paper-Conference.pdf|
|DeepResearchGym|Independent, performance (ICTIR 2026)|sonar-deepresearch|arxiv.org/abs/2505.19253|
|Deep Research Comparator|Independent, performance (WWW Companion)|Deep Research|arxiv.org/html/2507.05495v2|
|Mind2Web 2|Independent, performance (NeurIPS D&B)|Pro + DR|openreview.net/forum?id=AUaW6DS9si|
|Dow Jones opinion|Independent, court record|n/a|storage.courtlistener.com/…630270.65.0.pdf|
|Britannica docket|Independent, court record|n/a|pacermonitor.com/public/case/60086917/…|
|NYT related-case statement|Independent, court record|n/a|storage.courtlistener.com/…654190.3.0.pdf|
|Help center (Pro Search, plans)|Vendor|n/a|perplexity.ai/help-center/… (returned 403 or timed out; seen via search index only)|

## Evidence quality assessment
The evidence is broad: 6 independent tests, 5 of them in peer-reviewed venues. The weakness is mixing. The tests cover different modes (standard, Pro, Deep Research, API) and dates (2023–2025), and they use different metrics. I could not fetch the vendor's limit pages directly. The search-index snippets conflict (3/day vs 5/day free Pro Searches).

## What the rules say
v0 weights are 30/20/25/25. There are 3 or more independent sources, so an overall score is allowed. Lawsuits are recorded as neutral facts, not as findings.

## Proposed score breakdown (judgment calls)
| Factor | Score | Reason |
|---|---|---|
|Completion 30%|55|37% incorrect on CJR's attribution test (best of 8); Mind2Web 2 success 8–15%|
|Disputes 20%|35|4 pending publisher lawsuits (allegations only); CJR attribution and robots.txt concerns|
|Adherence 25%|45|CJR suggests a crawler block may have been bypassed in one case; vendor limit docs are inconsistent|
|Evidence 25%|75|6 independent performance sources, mostly peer-reviewed|

Overall = 0.3×55 + 0.2×35 + 0.25×45 + 0.25×75 = 16.5 + 7 + 11.25 + 18.75 = **53.5 → 54** (rounded half up)

## Risks/uncertainties
- **Defamation risk:** lawsuits must be stated only as "filed / alleges / pending". CJR's robots.txt point must be attributed to CJR as a suggestion, not stated as fact.
- Results differ by mode.
- Vendor limits are unverified.
- The tests are dated and the product changes.

## Recommendation
**Approve publish.** The lawsuit wording should get legal-sensitivity review first. Before publishing, fetch the vendor limits page directly (optional).

Proposed public summary: "Perplexity is a commercial AI answer engine; this entry covers only its citation and source-attribution behavior. In independent evaluations (CJR Tow Center, 2025; Findings of EMNLP 2023; DeepResearch Bench, ICLR 2026; DeepResearchGym, ICTIR 2026; Deep Research Comparator, WWW 2026 Companion; Mind2Web 2, NeurIPS 2025), results varied by product mode: its Deep Research mode scored comparatively high on citation accuracy, while news-attribution tests found a share of incorrect or syndicated citations. Several publishers have filed copyright lawsuits against Perplexity that are pending; these are allegations, not findings. Informational only; not an endorsement or certification."

## Plain-English terms
- **Citation precision:** the share of citations that actually support the claim.
- **Citation recall:** the share of claims that have a supporting citation.
- **robots.txt:** a website's "do not crawl" instructions.
- **Syndicated copy:** a republished version of an article on another site.
- **Pending lawsuit:** filed but not decided.

---

## Post-publication notes
- Deployed live: dpl_ASbvp6tH3UQo3Bi9VVqurfmpxsuL.
- Browser check 2026-10-16: Perplexity help center plan page (articles/11187416, modified 2026-10-08) table lists Free Pro Searches 3/day; text says Very limited; How Perplexity works page says limited number per day. Public wording unchanged pending approver review.
