# Decision 0054: Elicit citation backfill

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1a count Mazzali, Meliante and Spillias (10 counted, 9 peer-reviewed); D2 grade stays A; D3a completion 55, D4a adherence 55, D5a evidence 85 (all unchanged); D6 disputes 80, Hilkenmeier not counted, Acta Derm Venereol and Cochrane ESM 70033 already counted; D7 rollout with the drafted wording, including the UNSW disclosure. Overall 68 unchanged. Follows 0052 D5.

## Plain-English terms
- **Counted source:** an independent test that counts toward the evidence grade.
- **Peer-reviewed:** published in a reviewed journal.
- **Grade A:** all three conditions must be met:
  1. 7 or more counted sources;
  2. 3 or more of them peer-reviewed;
  3. at least one test within the last 12 months (since 2025-10-17) that states the version or tier tested. For hosted products, a dated test of a named tier counts (0051 E1).
- **Factor scores:** completion 30%, disputes 20%, adherence to limits 25%, evidence 25%. Scores are judgment calls against the independent results. Evidence-score guide bands (A 85–100) are advisory.
- **"Recall"** = share of the relevant studies a tool found. **"Precision"** = share of what it returned that was relevant.

## What was read
- **Full text, via Europe PMC open-access XML:**
  - Mazzali 2026 (PMC13412304).
  - Meliante 2025 (PMC12413140).
  - Spillias 2025 (PMC12128520).
- **Screened:**
  - Acta Derm Venereol 2026. This is Vyas et al., already counted, so there is no change.
  - Cochrane ESM 2025, 10.1002/cesm.70033 (PMC12462964). This is Bianchi et al., already counted, so there is no change.
- **Hilkenmeier 2025 (SSCR):** OpenAlex lists it as CC-BY open access. However, the publisher returned 403 for both the full-text and PDF pages, and Unpaywall has no repository copy. It stays abstract-only and not counted.

## Findings per study

**S1. Mazzali et al. 2026, BMC Medical Research Methodology (doi 10.1186/s12874-026-02892-3)**
- **Independence:**
  - Authors are from ATS Milano (the Milan health protection agency) and regional Italian health bodies, for the Air and Health Atlas Study Group.
  - Funding is from the Italian Ministry of Health (PNC PREVA-2022-12376981).
  - The authors declare "no competing interests."
  - The paper mentions Ought only as Elicit's history. No tie to Elicit or Ought was found.
- **Peer review:** yes (BMC MRM; published 30 May 2026).
- **Version, date and scope:**
  - Elicit "Pro" subscription, Systematic Reviews workflow. All runs were between September 2025 and October 2025.
  - In scope.
  - The 12-month window opens 2025-10-17, so the runs fall mostly or entirely before it. This study does not by itself meet A condition 3. Wei et al. still does (0051).
- **What was tested:** an umbrella review on air pollution and acute lower respiratory infections. The authors compared search, screening and quality appraisal (AMSTAR-2 EH) with the traditional method.
- **Results:**
  - **Search:** only 8% of Elicit's 500 records overlapped the 324 found by Boolean search. The authors judged that too low for a recall comparison.
  - **Screening** (run on the 324 Boolean records):
    - Title/abstract: recall 90.9%, precision 42.9% (30 of 33; 70 selected).
    - Full text: recall 100%, precision 62.5% (all 15; 24 selected).
  - **Quality appraisal:** 44 of 180 general-item answers were incorrect (24.4%), as were 17 of 56 additional-item answers (30.4%). Errors clustered on multi-part questions, expert judgment and supplementary material.
  - **Limit:** a maximum of 500 papers per search (1,000 with uploads).
  - The authors support a human-in-the-loop approach.

**S2. Meliante et al. 2025, JMIR AI (doi 10.2196/68592)**
- **Independence:**
  - Authors are from the University of Rome Tor Vergata, University Hospital Maggiore della Carità (Novara) and IRCCS Fondazione Bietti.
  - "Conflicts of Interest: None declared."
  - No Elicit tie was found.
- **Peer review:** yes. Received 10 Nov 2024, accepted 27 May 2025, published 5 Sept 2025.
- **Version, date and scope:**
  - The tier is not stated. Elicit is cited as "Accessed 03-03-2024." The paper describes the older "top 8 papers" interface.
  - So the test was about March 2024. That is in scope but outside the 12-month window, and before the May 2025 high-accuracy default.
- **What was tested:** four published glaucoma systematic reviews were recreated. Elicit and Connected Papers did the search; Elicit and ChatPDF did data extraction.
- **Results:**
  - **Search:** Elicit found 26 of the 106 included studies (24.5%): 15/30, 2/32, 6/14 and 3/30.
  - **Extraction:** 655 of 1,274 responses were accurate (mean 51.4%, SD 31.4). A further 13.7% were imprecise, 22.4% were missing and 12.5% were incorrect. ChatPDF was accurate in 60.3%.
  - The authors conclude that the traditional method remains clearly superior in accuracy and reproducibility.

**S3. Spillias et al. 2025, Environmental Evidence (doi 10.1186/s13750-025-00362-9)**
- **Independence:**
  - Authors are from CSIRO, the University of Tasmania, ANU and UNSW.
  - Funding: a CSIRO postdoctoral fellowship and the Centre for Marine Socioecology.
  - "The authors declare no competing interest."
  - No Elicit tie was found.
  - One author is at UNSW, as are the authors of Lagisz et al. (already counted). That is a shared institution only, with no author overlap. Disclose it; it is not grounds to exclude.
- **Peer review:** yes. Received 11 Dec 2024, accepted 11 May 2025.
- **Version, date and scope:**
  - PDFs were uploaded to Elicit on 29 January 2024 with "High-accuracy Mode" enabled. The tier is not stated.
  - In scope, but outside the 12-month window.
- **What was tested:** qualitative data extraction from 33 community-based fisheries management papers. Elicit was compared with two GPT-4 Turbo setups and human extractors, and separate human evaluators rated quality.
- **Results:**
  - **Presence or absence of data:**
    - Elicit agreed very poorly with humans (Cohen's kappa below 0).
    - It returned an answer for all but one paper-question pair, giving 27% false positives and near-zero false negatives.
  - **Extraction quality:**
    - Elicit was rated highest of the three AI setups, by both human and LLM evaluators.
    - Its mean quality was significantly above the acceptable threshold (t = 6.91, p < 0.001).
  - **Response length:** responses were verbose, averaging 306 words against 85 for humans.
  - The authors say the tools "can facilitate, but not reliably automate" extraction.

**S4. Hilkenmeier et al. 2025, SSCR:** no change. It stays listed, abstract-only and not counted. Recheck if full text becomes fetchable.

## Effect on counts and grade (D1a, recommended)

| | Before | After |
|---|---|---|
| Counted performance sources | 7 | 10 (+ Mazzali, Meliante, Spillias) |
| Peer-reviewed | 6 | 9 |
| Recent test that states the tier | Wei et al. (Pro tier, Dec 2025–Apr/May 2026) | unchanged. Mazzali's Pro-tier runs (Sept–Oct 2025) fall mostly or entirely before the window and are not relied on. |
| Grade | A | A (all three conditions still met) |

## Factor scores (no fitting to grade)

**Completion (now 55).**
- **What the current basis says:** weak search (18–40%), moderate screening, extraction 77–92% agreement.
- **What the new evidence shows:**
  - **Search:** still weak (8% overlap; 24.5% found). This confirms the current basis.
  - **Screening:** stronger than before (recall 90.9% and 100% in a 2025 Pro-tier test).
  - **Extraction:**
    - Mixed. Meliante's 51.4% accurate (March 2024, older interface) is well below the current low end of 77%.
    - Spillias found Elicit the best of three AI setups but unable to tell when data were absent.
    - Mazzali's appraisal answers were 24–30% wrong.
- **Reading the rules honestly:** completion is a judgment on how often the tool does the task correctly across independent tests. The extraction range now widens to roughly 51–92%. That lower result comes from the oldest version (pre-high-accuracy default), while the newest tests show better screening.
- **Recommendation: keep 55.** The new evidence moves screening up and extraction down; the net is not clearly one direction. State the wider range plainly.
- **Alternative: 50.** This weights the extraction drop more heavily.

**Disputes (now 80):** keep. No legal, regulatory, security or data-incident findings in any new study.

**Adherence to limits (now 55).**
- **New evidence:**
  - Spillias: Elicit returned an answer even when the paper had no relevant data (27% false positives).
  - Mazzali: hard cap of 500 papers per search.
- **Recommendation: keep 55.** The first point is the same kind of behaviour already in the note ("gave multiple answers where one was required"). Append one sentence.
- **Alternative: 50.** This treats answer-when-absent as a stronger limits failure.

**Evidence (now 85).**
- **What improves:** 10 counted sources, 9 peer-reviewed, across health and environmental fields.
- **What remains:**
  - Samples are still small.
  - Two of the new tests are from early 2024.
  - Tier is unstated in two of them.
  - Only one test falls clearly in the 12-month window.
- **Recommendation: keep 85.** It is inside the A guide band.
- **Alternative: 88**, to reflect more and broader peer-reviewed sources.

**Overall math:**
- **Now and recommended:** 0.30×55 + 0.20×80 + 0.25×55 + 0.25×85 = 16.5 + 16 + 13.75 + 21.25 = 67.5 → **68** (exact .5 rounds up, Decision 0010).
- **Alternatives:**
  - Completion 50: 66.0 → **66**.
  - Adherence 50: 66.25 → **66**.
  - Both at 50: 64.75 → **65**.
  - Evidence 88: 68.25 → **68**.
  - Completion 50 and evidence 88: 66.75 → **67**.

## Decision items

**D1. Count the three studies**
- **D1a (recommended):** count Mazzali, Meliante and Spillias: 10 counted, 9 peer-reviewed.
- **D1b:** count Mazzali and Spillias only, and list Meliante as context because its tier is unstated. Result: 9 counted, 8 peer-reviewed.
  - Note: Bernard, Bianchi and Vyas are already counted with unstated tiers, so D1b would be inconsistent with current practice.

**D2. Grade stays A.** Recommended: approve. Wei et al. remains the recent tier-stated test; Mazzali is not relied on for condition 3.

**D3. Completion score**
- **D3a (recommended):** keep 55, with the wider extraction range and the screening results stated.
- **D3b:** 50.

**D4. Adherence score**
- **D4a (recommended):** keep 55 and append one sentence.
- **D4b:** 50.

**D5. Evidence score**
- **D5a (recommended):** keep 85.
- **D5b:** 88.

**D6. Disputes stay 80.** Hilkenmeier stays not counted. Acta Derm Venereol and Cochrane ESM 70033 are confirmed as already counted (Vyas, Bianchi). Recommended: approve.

**D7. Rollout**
1. Update the YAML and page in place.
2. Write decision record 0054 and add one changelog row.
3. Run check_scores (expect 0 errors and 7 warnings, unchanged), check_links, overflow and axe.
4. Commit and push, then write manifest-0054.
5. You deploy.
6. Add the LOG note.
- Index and llms.txt need no change under the recommended options, because the score and grade are unchanged.

## Proposed exact wording (under D1a, D3a, D4a, D5a)

**New source rows (all `independent performance`, `peer_reviewed: true`):**
1. Version: "Pro (Systematic Reviews workflow)". Date: "2025-09 to 2025-10".
   > Mazzali et al. (BMC Medical Research Methodology 2026; ATS Milano): Elicit Pro Systematic Reviews workflow, runs Sept–Oct 2025, umbrella review on air pollution; search overlapped only 8% with a Boolean search; screening recall 90.9% (title/abstract, precision 42.9%) and 100% (full text, precision 62.5%); quality-appraisal answers incorrect in 24.4% (general items) and 30.4% (additional items)
2. Version: "unstated". Date: "2024-03".
   > Meliante et al. (JMIR AI 2025; University of Rome Tor Vergata): four glaucoma systematic reviews, Elicit accessed March 2024; search found 26 of 106 included studies (24.5%); extraction accurate in 51.4% of 1,274 responses, imprecise 13.7%, missing 22.4%, incorrect 12.5%
3. Version: "high-accuracy mode". Date: "2024-01".
   > Spillias et al. (Environmental Evidence 2025; CSIRO, University of Tasmania, ANU, UNSW): qualitative extraction from 33 fisheries-management papers, January 2024, high-accuracy mode; highest-rated of three AI setups and above the acceptable-quality threshold, but answered nearly every question even when the paper had no relevant data (kappa below 0; 27% false positives); responses averaged 306 words vs 85 for humans

**Completion note (append):**
> Mazzali et al. (Pro, Sept–Oct 2025): search overlapped 8% with a Boolean search; screening recall 90.9% (abstract) and 100% (full text). Meliante et al. (March 2024): search found 24.5% of included studies; extraction accurate in 51.4% of responses. Spillias et al. (January 2024): extraction quality above the acceptable threshold and best of three AI setups.

**Adherence note (append):**
> It answered nearly every extraction question even when the paper contained no relevant data (27% false positives; Spillias et al.), and the Systematic Reviews workflow was capped at 500 papers per search (Mazzali et al.).

**Evidence note (replace):**
> Ten independent performance sources, nine peer-reviewed, one testing the current paid tier in 2025–2026. Samples are small and mostly from health and environmental sciences; two tests date from early 2024, and several do not state the tier. One had free accounts from Elicit (partly independent). Two further studies were read from abstracts only and are not counted. Judgment call.

**Summary:**
- Replace "Elicit searches found about 18–40% of the studies identified by traditional systematic searches." with:
  > Elicit searches found about 18–40% of the studies identified by traditional systematic searches, and in one 2025 test only 8% of its results overlapped a Boolean search.
- Replace "Its data extraction agreed with human reviewers about 77–92% of the time on the variables tested, with some errors and made-up details, and screening caught 71–78% of relevant studies in a 2026 preprint." with:
  > Its data extraction agreed with human reviewers about 77–92% of the time in most tests but was accurate in only 51% of responses in a 2024 test, with some errors and made-up details; screening caught 71–100% of relevant studies in two recent tests.

**Uncertainties (add):**
> Extraction results vary widely between studies (51–92%); the lowest result comes from a March 2024 test, before the high-accuracy default.

**Scoreline:**
> Overall score: 68 · Evidence grade: A · Independent sources: 10 performance, 2 other

Also update the page's evidence-note sentence to the new text.

**Disclosures:** the entry has no disclosure section. Add one sentence to the Lagisz uncertainty line:
> Spillias et al. include a UNSW author; there is no author overlap with Lagisz et al.

**Decision records line:** add "0054 (citation backfill)".

**Changelog row:**
> 2026-10-17 · 0054 · Elicit: three peer-reviewed tests added (Mazzali et al. 2026, Meliante et al. 2025, Spillias et al. 2025); 10 counted sources (9 peer-reviewed). Search remains weak; screening was strong in a 2025 Pro-tier test; extraction ranged from 51% to 92% accurate. Scores unchanged; overall 68, grade A.

## Queue
- **0050 D7 (Browser Use TOCTOU):** still pending and undecided.
- **Later follow-ups (from 0052 Part 4):** Perplexity, Gemini/OpenAI Deep Research, Consensus, Google DeepMind SAFE, Julius AI, Browser Use library.
