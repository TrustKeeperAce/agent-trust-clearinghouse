# Decision 0056: Perplexity follow-up (from 0052 sweep)

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1a count none of C1–C5; D2a add one uncounted-context uncertainty line for C1–C3; D3 C4 (abstract only) and C5 (no citation measure; underlying model not recorded) recorded here only, not counted; D4 scores unchanged (55/35/45/75; overall 53.5 → 54, grade B); D5a recheck note updated (banner kept; last uncertainty reworded).

Entry: Perplexity (search assistant; scope "Citation-backed answering and source attribution only"). Comet is out of scope.
Current: 54 / B. 6 counted performance sources (5 peer-reviewed + CJR), plus 3 court records (other).

## Research done
- Full reads of 4 candidates (3 via Europe PMC full text, 1 open-access PDF). 1 is abstract-only (closed access).
- Semantic Scholar retry: 8 tries 23:06–23:11 ET, all HTTP 429. Stopped there. No new candidates.

## Per-candidate findings
| # | Study | Independence | Peer review | What was tested | Scope fit | Results |
|---|---|---|---|---|---|---|
| C1 | Kara, Ozduran, Hancı et al., PLoS ONE 2025, 10.1371/journal.pone.0326351 | Independent (Turkish hospitals/universities, UTHealth Houston). No funding, no competing interests | Yes | Free Perplexity, version not stated. Data from Oct 2024. 25 ankylosing-spondylitis queries | Weak. Measures readability and health-information quality (EQIP, GQS, mDISCERN, JAMA). The JAMA "attribution" item only checks that sources are listed, not that they support the claims | Perplexity scored highest on all quality measures (p<0.001). Median JAMA 2/4 |
| C2 | Ozduran, Hancı et al., PeerJ 2025, 10.7717/peerj.18847 | Independent, but **shares authors with C1** (disclose) | Yes | Free versions, May 2024, version not stated. Low back pain | Weak (same instruments) | Perplexity scored highest on EQIP, JAMA, mDISCERN and GQS (p<0.001). All tools were above a 6th-grade reading level |
| C3 | Kıztanır & Çetin Özbek, PLoS ONE 2026, 10.1371/journal.pone.0359170 | Independent. No funding, no competing interests | Yes (received 20 Jun 2026, accepted 10 Sep 2026) | **Free web-grounded Sonar model, June 2026.** Named and dated, inside the 12-month window. 17 pediatric chest-pain queries | Weak (same instruments). The authors mention "observed citation biases and omissions" but do not measure them | Harder to read, but scored best on GQS, JAMA, mDISCERN and EQIP. JAMA ICC 0.891 |
| C4 | Kothandan, Watson, Basu, Singh, Semin Ophthalmol 2025, 10.1080/08820538.2025.2547077 | Independent (LV Prasad Eye Institute, Univ. of Sydney) | Yes | Version not given in the abstract. 10 dry-eye prompts | Partly relevant (comments on the sources cited) | 2.7 vs ChatGPT-4's 2.6. Perplexity's citations "were from web pages and were not evidence-based". Poor agreement between raters. **Abstract only, so not counted** (Hilkenmeier precedent) |
| C5 | Mihăluţe & Mititelu, Bul. Inst. Politeh. Iași 2026, 10.2478/bipcm-2026-0028 | Independent (Gheorghe Asachi TU Iași). No funding or interest statement found | Yes (university journal) | Accessed 20 Aug 2025. **Underlying model not recorded** (stated as a limitation). 20 prompts, 10 raters | Out of scope. The factual rubric "measures form, not verified accuracy"; there is no citation measure | Only the factual set showed agreement above chance. Perplexity ≈ ChatGPT > Claude and Gemini, "carried almost entirely by response structure" |

Plain terms: none of the five checks whether Perplexity's citations actually support its answers, which is what this entry rates. The three health studies (C1–C3) rate how readable and complete the health information is. Their "attribution" item gives credit just for listing sources.

## D-items
**D1. Count C1–C3?**
- D1a (recommended): don't count them; they fall outside the scope. Counts stay at 6 performance (5 peer-reviewed) + 3 other. Grade B.
- D1b: count C1–C3. That gives 9 counted / 8 peer-reviewed, and C3 (Sonar, June 2026) meets the dated, named-test condition, so **B → A (grade-changing)**. Not recommended: it would widen the scope through scoring instead of an explicit scope decision.
- D1c: count C3 only. 7 counted / 6 peer-reviewed plus a recent named test, so **also B → A**. Same objection, and it would be choosing a study because of what it does to the grade.

**D2. List them on the page as uncounted context?**
- D2a (recommended): one uncertainty line naming C1–C3 as uncounted (wording below). No source rows added.
- D2b: add nothing to the page; record only in decisions/0056.

**D3. C4 and C5:** not counted (C4 abstract only; C5 has no citation measure and the model wasn't recorded). Record in decisions/0056 only.

**D4. Factor scores (honest reasoning, nothing changed to fit a grade)**
- Completion 55: unchanged. C1–C3 don't measure task success on citation-backed answering.
- Disputes 35: unchanged. No new disputes found.
- Adherence 45: unchanged. Nothing new on robots.txt or limits.
- Evidence 75: unchanged. The counted base is the same. Out-of-scope positive health-quality results shouldn't raise it, and C4's "not evidence-based" remark is abstract-only, so it shouldn't lower it.
- Overall: 0.30×55 + 0.20×35 + 0.25×45 + 0.25×75 = 16.5 + 7 + 11.25 + 18.75 = 53.5 → **54** (rounded half up). **Grade B unchanged.** Under D1b/c, scores would still be 54 and the grade would become A. The evidence score would also need its own review, which isn't proposed here.
- Grade A conditions now: 6 of 7+ sources ✗; 5 of 3+ peer-reviewed ✓; dated, named test within 12 months (window opens 2025-10-17) ✗. The newest counted tests are from 2025 and older.

**D5. The 0052 recheck note**
- D5a (recommended): replace it with "Citation check incomplete — recheck later (0056: five 2025–2026 candidates read in full or by abstract, none in scope; Semantic Scholar still unavailable)." S2 still returned 429, so the check is still incomplete.
- D5b: remove the note. Not recommended while S2 remains unchecked.

## Exact wording (if D1a, D2a, D5a)
- Uncertainty added before the recheck note:
  "Three peer-reviewed health-information studies (PLoS ONE 2025, PeerJ 2025, PLoS ONE 2026; the first two share authors) rated Perplexity highly on readability and quality scales, including a June 2026 test of the free Sonar model; not counted because they check that sources are listed, not that sources support the answer."
- The recheck note (banner and last uncertainty) becomes:
  "Citation check incomplete — recheck later (0056: five 2025–2026 candidates read, none in scope; Semantic Scholar still unavailable)."
- Evidence note: unchanged.
- last_reviewed: 2026-10-17.
- decisions/0056 marked APPROVED and records C1–C5 with reasons, including C4 abstract-only and C5 model not recorded.

## Changelog row
`<tr><td>2026-10-17</td><td>Perplexity</td><td>Follow-up review of five 2025–2026 studies; none in scope (health-information quality, or no citation check), so none counted. Score 54 and grade B unchanged. Recheck note updated (0056).</td></tr>`
(Use the same column structure as the existing rows.)

## Expected public file changes
agents/perplexity.yaml, public/agents/perplexity.html, public/changelog.html, decisions/0056 (+ its public copy if there is one). No change to the index or llms.txt, since the grade doesn't change.
