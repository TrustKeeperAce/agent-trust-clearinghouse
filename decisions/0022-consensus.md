# Decision 0022: Consensus (candidate 7)

**Status: APPROVED by Remington, 2026-10-17**, at 62 / B as recommended. Decisions:
1. PRS Global Open is counted, which makes 6 sources.
2. The 2024–2025 tests are counted under the Elicit continuity precedent (0017).
3. The Elicit BioASQ benchmark stays excluded: it is listed as not counted, as competitor launch material.
4. One entry covers all modes, with a note that Deep and Research Agent were not separately tested.
5. Category: Research.

## 1. What happened (vendor primary sources)
- Consensus (Consensus NLP, Inc.) is an AI academic search engine that answers questions from scholarly papers. It offers Quick, Pro and Deep modes.
- 8 Jul 2025: Deep Search launched, "a research agent" running up to 20 searches (https://consensus.app/home/blog/deep-search/).
- 11 May 2026: $30M round led by GreatPoint Ventures; DJ Patil joins the board (https://consensus.app/home/blog/30m-in-new-funding-to-reach-the-next-10m-researchers/).
- Summer 2026 (https://consensus.app/home/blog/what-has-changed-in-consensus-summer-26/):
  - a Research Agent;
  - the corpus grew from 250M to over 400M sources;
  - "Citation Grounding": every AI citation mapped to a quote;
  - the API and MCP opened to all users.
- Oct 2026: Skills, ready-to-run research workflows (https://help.consensus.app/en/articles/11954907-consensus-product-changelog).
- Status: still offered and not retired. It has been continuous since launch, with features added; no rewrite or retirement. Continuity reading as in Elicit (0017) and 0019.

## 2. Counted independent performance sources (6; all peer-reviewed; all read in full)
1. **Menet et al., Eur Heart J Digit Health 2026** https://doi.org/10.1093/ehjdh/ztag125 (PMC13520940)
   - Free tier, Aug 2025–Jan 2026; four cardiology topics; blinded expert gold standard.
   - Consensus returned 158 references; its relevance was "intermediate", between ChatGPT-5 (90%) and Scite (20%). The exact Consensus value appears in a figure only.
   - No conflicts declared.
2. **Labenbacher et al., JMIR 2026** https://doi.org/10.2196/88766 (PMC13134821)
   - "Consensus Version July 2025"; tested Jun–Sep 2025; 15 retracted trials, 5 questions each, asked twice.
   - Consensus gave 0/15 fully correct sets (ChatGPT 5: 8/15).
   - It included the retracted article in topic overviews without warning in 6/15 (40%).
   - Discrepancies between repeated answers: 19 (25.3%), the worst of the 9 tools.
3. **Kermansaravi et al., Obesity Surgery 2026** https://doi.org/10.1007/s11695-026-08511-w (PMC13038736)
   - Web interface, 1 May 2025; 25 statements on GERD after bariatric surgery.
   - Consensus agreed with evidence-based expert answers 72% of the time (ChatGPT-4o and Grok 3: 80%; Gemini 72%).
   - No competing interests declared.
4. **Karakoyunlu et al., BMC Oral Health 2026** https://doi.org/10.1186/s12903-026-09298-z (PMC13647515)
   - Consensus Pro, Nov 2025; endodontic questions in English and Turkish; two blinded endodontists.
   - Consensus had the highest mDISCERN quality and completeness scores (for example GQS 3.95–4.10 vs Perplexity lower), but the longest response times.
5. **Plast Aesthet Res 2025;12:1 (Rozen group)** https://doi.org/10.20517/2347-9264.2024.99 (full text on the OAE site)
   - Searches against a manual search to Apr 2024, for RCTs on thumb-base arthritis.
   - Consensus found 9 of 23 eligible studies (manual search 23; Elicit 10); 76% false positives; it found no studies the manual search missed.
   - Disclosure: one author is on the journal's editorial board and was not involved in handling the paper.
6. **Plast Reconstr Surg Glob Open 2025** https://doi.org/10.1097/GOX.0000000000007176 (PMC12490650)
   - Dec 2024; a single question on migraine surgery, put to 9 tools.
   - Consensus cited the most references (10) and was rated "+++" for detail.
   - **Weak:** a qualitative comparison with no accuracy grading. Decision point.

## 3. Listed, not counted
- O'Rourke et al., West J Nurs Res 2026 https://doi.org/10.1177/01939459261451723: Consensus matched 21.3% of human references. Abstract only (paywalled); not counted (Elicit precedent).
- Elicit's BioASQ search evaluation https://github.com/elicit/elicit-paper-search-eval: recall Consensus 0.369@10 and 0.434@20 vs Elicit 0.390 and 0.483. Run by a direct competitor as launch marketing. Not counted, following the interested-party precedent (ChatGPT Work / Composio).
- Excluded:
  - CJILS "Elicit, SciSpace, and Consensus" (doi 10.5206/cjils-rcsib.v49i1.23075): **retracted**.
  - Vendor claims: corpus size, citation grounding and the privacy statements (https://help.consensus.app/en/articles/10093291-security).
- Disputes: no lawsuit, regulatory action, breach or security advisory found.

## 4. What the rules say
- At least 3 counted sources are needed for a score. 6 counted, all peer-reviewed, gives grade **B** (5–6 sources).
- A requires at least 7 sources. Two sources tested within 12 months (Nov 2025; Aug 2025–Jan 2026).
- If source 6 (PRS GO) is not counted, 5 remain and the grade is still B.

## 5. Score (proposed)
- Completion 50: found 9 of 23 RCTs with 76% false positives; 0/15 fully correct on retracted literature; 72% agreement on bariatric questions; intermediate cardiology relevance; best expert-rated quality in endodontics. Judgment call.
- Disputes 80: none found (consistent with Elicit, 0017). Judgment call.
- Adherence 50: inconsistent repeated answers (25.3%, worst of 9); retracted papers cited without warning; privacy commitments are vendor statements only. Judgment call.
- Evidence 75: 6 peer-reviewed sources, 2 recent; small samples, mostly health sciences, mostly free tier; Deep Search and the Research Agent not separately tested. Judgment call.
- Overall = 0.30*50 + 0.20*80 + 0.25*50 + 0.25*75 = 62.25, rounded to **62**. Grade **B**.

## 6. Risks and uncertainties
- Mostly standard or Pro search was tested. The Deep Search agent (Jul 2025) and the Research Agent (2026) were not specifically tested.
- Citation Grounding (2026) postdates all tests.
- Samples are small and the topics are mostly medical.

## 7. Recommendation
Publish at 62 / B, in the Research category. Scope: Consensus search (Quick, Pro, Deep), with a note that the Deep and Research Agent modes are not separately tested.

## 8. Decision points
1. Count PRS GO (qualitative, single question)? The grade is B either way. Without it the evidence factor might be 72, giving 61.5, which rounds to 62, so the overall is unchanged.
2. Continuity: count the 2024–2025 tests for the current product with its 2026 features, as in the Elicit precedent?
3. Elicit BioASQ benchmark: keep it excluded as a competitor's marketing test, or count it with a disclosure under the competing-author rule?
4. Scope: one entry covering all modes, or exclude Deep/Research Agent?

## 9. Plain-English terms
- Counted source: an independent study I read in full that tested Consensus itself.
- False positive: a paper returned that did not meet the review's criteria.
- mDISCERN / GQS: expert rating scales for the quality of health information.
