# Decision 0058: Consensus, Google DeepMind SAFE and Julius AI follow-ups (from 0052 sweep)

**Status: APPROVED by Remington, 2026-10-17**, exactly as recommended: D1a Consensus nothing counted (62 / B); D2a VeriFact counted for SAFE (4 counted, 4 peer-reviewed; 66 / B-); D3 DnDScore and arXiv 2610.18415 not counted; D4a Julius AI nothing counted (Insufficient evidence); D5 scores unchanged (SAFE completion-note sentence added); D6a Consensus recheck note closed, SAFE and Julius notes reworded.

The work was split as allowed:
- 0058 covers Consensus, Google DeepMind SAFE and Julius AI.
- **0059 (Browser Use: AgentTell 2609.32915, Privacy Practices 2512.07725, ceLLMate 2512.12594, controlled interventions 2609.35814) is queued** and will be sent separately.

## Plain-English terms
- **Counted source:** an independent test that counts toward the evidence grade.
- **Grades:**
  - A: 7 or more counted sources, 3 or more peer-reviewed, and a recent test that states the version.
  - B: 5–6 counted sources, or 7 or more that miss an A condition.
  - B-: 3–4 counted sources.
  - Insufficient evidence: fewer than 3.
- **Retracted:** the journal has withdrawn the paper, so it isn't used as evidence.
- **Rapid review / perspective / case study from public reports:** these summarise other people's material. None of them is the authors' own measured test of the tool.
- **Fact extraction:** SAFE's first step, which splits a long answer into separate facts to check. "Incomplete facts" are pieces missing context they need.

## Research done
- **Semantic Scholar:**
  - Retry started at 23:35 ET. The Consensus query returned HTTP 200 on the first try; I screened all 50 hits.
  - Follow-up queries for SAFE and Julius AI returned 429.
  - I stopped there, inside the time limit.
- **Full reads:**
  - VeriFact (EMNLP 2025, ACL Anthology PDF).
  - DnDScore (EMNLP 2025, ACL Anthology PDF).
  - arXiv 2610.18415.
  - The Julius AI / Power BI Copilot paper (publisher PDF).
- **Metadata and abstract only:**
  - The CJILS paper (retraction confirmed).
  - The Cureus review (abstract).
  - The Taiwan Educational Research Monthly article (closed access).

## Per-candidate findings

### Consensus (62 / B; 6 counted, all peer-reviewed)
| # | Item | Independence | Peer review | Version / date | Scope fit | Results | Counted? |
|---|---|---|---|---|---|---|---|
| K1 | Cruz, Factor, Rama, "Assessing the Effectiveness of AI Tools (Elicit, SciSpace, and Consensus) in Literature Review and Research", CJILS 2025, 10.5206/cjils-rcsib.v49i1.23075 | Independent (De La Salle University) | Was peer-reviewed; **now retracted** | n/a | n/a | n/a | **No.** Already excluded as retracted in 0022 (the page says "A retracted CJILS comparison was excluded"). This is the same paper, so nothing changes |
| K2 | Apata, Kwok, Lee, "The Use of Generative AI in Academic Research: A Review of the Consensus App", Cureus 2025, 10.7759/cureus.87297 (found through S2) | Independent | Yes (Cureus) | Literature search 23 Dec 2024 | Weak: a rapid review of 10 papers, not a test | Describes uses, benefits and ethical concerns, synthesised with ChatGPT-4.5's help | **No.** Not an evaluation |

The other 48 S2 hits were about Delphi "consensus" studies and contained nothing about Consensus the product.

### Google DeepMind SAFE (66 / B-; 3 counted, all peer-reviewed)
| # | Item | Independence | Peer review | Version / date | Scope fit | Results | Counted? |
|---|---|---|---|---|---|---|---|
| S1 | Liu, Zhang, Munir, Gu, Wang, "VeriFact: Enhancing Long-Form Factuality Evaluation with Refined Fact Extraction and Reference Facts", EMNLP 2025 (main), 10.18653/v1/2025.emnlp-main.905 | Independent (University of Michigan; NSF grant 2046016). No Google authors. **Authors propose a competing method**, as in all 3 existing sources | Yes (EMNLP 2025) | SAFE's fact extractor (Wei et al. 2024). Model and version not stated. About early 2025 (arXiv May 2025) | Fits: measures how well SAFE extracts facts, a core step of the tool | Preliminary check: 12.68% of 451 SAFE-extracted facts were incomplete. On the 1,168-fact human-annotated set, SAFE had 56.7% incomplete facts, 1.22 missing facts per response and 77.5% coverage of human facts. For comparison: VeriFact 22.5%, 0.76 and 87.1%; FactScore 70.4%; FactCheck-GPT 41.7%; VERIFY 43.4%. **Caveat:** the annotated set was deliberately chosen for responses with many problems, based on SAFE's own extractions | **Yes** (recommended) |
| S2 | Wanner, Van Durme, Dredze, "DnDScore", EMNLP 2025, 10.18653/v1/2025.emnlp-main.1205 | Independent (Johns Hopkins) | Yes | n/a | Doesn't fit: SAFE is cited only in related work and isn't evaluated | n/a | **No** |
| S3 | Amatya, Setty, V, Anand, "Do Factuality Methods Make LLMs More Factual? Reproducibility and Fair Comparison", arXiv 2610.18415 (13 Oct 2026) | Factiverse AS (a fact-checking company), University of Stavanger, Stockholm University, TU Delft. No Google authors | No (preprint) | 2026 | Doesn't fit: uses SAFE F1@100 as a scoring metric to rate other methods; doesn't test SAFE's accuracy | Notes that SAFE-style metrics credit supported claims "irrespective of the claim's relevance to the prompt" (shared with FActScore and VeriScore) | **No.** Uses SAFE, doesn't evaluate it |

### Julius AI (Insufficient evidence; 2 limited counted)
| # | Item | Independence | Peer review | Version / date | Scope fit | Results | Counted? |
|---|---|---|---|---|---|---|---|
| J1 | Mohamed, "Reimagining the Future of Data Analytics through Generative AI: A Mixed-Methods Comparative Study of Julius AI and Power BI Copilot", International Science and Technology Journal (Libya), No. 37, July 2025, 10.62341/absm3091 | Independent (University of Aljufra) | Journal says it is peer-reviewed. Venue assurance is low and unverified | No version. Sources date to 2024 | Weak: literature review plus three case studies taken from public reports and industry publications, with user testimonials | No measurement of correctness: no dataset was run through Julius and no answers were checked | **No.** No hands-on test |
| J2 | 張宥沁 (Chang Yu-Chin), "Applications of AI in Educational Research (4): Hands-on test of Julius AI for data analysis and visualization", Educational Research Monthly (教育研究月刊) No. 370, Feb 2025, 10.53106/168063602025020370009 | Appears independent (no vendor tie seen) | Not checked (practitioner monthly) | Version not given in the abstract. About late 2024 | Partial fit: hands-on demo of descriptive statistics, charts, normality tests and ANOVA | Per the abstract: "exceptional analytical capabilities". No error rate reported | **No.** Abstract only, and a demonstration rather than a measured accuracy test |
| — | Also screened: ESPACIOS 2025 (a survey instrument for student use of Julius), EDUNINE 2026 workshop, and Figshare/Zenodo/ResearchHub promo-code spam | — | — | — | Not evaluations | — | No |

## D-items

**D1. Consensus: count nothing.**
- **D1a (recommended):** K1 stays excluded (retracted) and K2 isn't a test. Stays at 6 counted / 6 peer-reviewed, **62 / B unchanged**.
- No alternative recommended. Counting a retracted paper isn't allowed.

**D2. SAFE: count VeriFact (S1)?**
- **D2a (recommended):** count it. That gives 4 counted / 4 peer-reviewed; **grade stays B-** (3–4 sources).
- **D2b:** list it as uncounted context. Not recommended: it is the same kind of study as VeriScore and FactBench, which are already counted.
- Not grade-changing. SAFE would need 5 counted sources to reach B, and S2 and S3 don't qualify.

**D3. SAFE: S2 and S3 not counted** (S2 only cites SAFE; S3 uses SAFE as a metric). Record them in decisions/0058 only.

**D4. Julius AI: count nothing.**
- **D4a (recommended):** J1 has no hands-on test; J2 is abstract-only and a demonstration. Stays at 2 counted, **Insufficient evidence, no scores**.
- **D4b:** count J2. That gives 3 counted, enough for B- and **first scores for Julius (grade-changing).** Not recommended: unread, a single demo, and no measured accuracy.

**D5. Factor scores (honest reasoning, nothing changed to fit a grade)**

*SAFE*

| Factor | Score | Reasoning |
|---|---|---|
| Completion | 65, unchanged | VeriFact backs up the existing "weaker for claim extraction" point (VeriScore) with numbers. The current score already reflects that weakness, and the test set was chosen to be hard. Add a sentence to the note |
| Disputes | 80, unchanged | Nothing new |
| Adherence | 60, unchanged | Nothing new |
| Evidence | 60, unchanged | Four peer-reviewed sources instead of three, but all still from authors of competing methods, with small and selected samples. Inside the B- guide band; not raised |

- Overall: 0.30×65 + 0.20×80 + 0.25×60 + 0.25×60 = 19.5 + 16 + 15 + 15 = **65.5 → 66** (exact .5 rounds up, Decision 0010). **B- unchanged.**
- Alternative: evidence 60 → 65 for the fourth peer-reviewed source, giving 66.75 → 67, still B-. Not recommended: independence and sample concerns are unchanged.

*Consensus*
- Scores unchanged at 50 / 80 / 50 / 75: nothing new is counted.
- Overall: 0.30×50 + 0.20×80 + 0.25×50 + 0.25×75 = 15 + 16 + 12.5 + 18.75 = **62.25 → 62**. **B unchanged.**
- Grade A conditions:
  - 6 counted sources ✗ (needs 7)
  - 6 peer-reviewed ✓
  - recent test that states the version ✓ (the July 2025 version test is inside the window, and so is the Nov 2025 Pro test)
- Only the source count is short.

*Julius AI*
- No scores: Insufficient evidence (2 counted, needs 3).

**D6. Recheck notes**
- **D6a (recommended):**
  - **Consensus:** close the note. S2 worked for Consensus and the only lead turned out to be the retracted paper. Remove the 0052 note from the banner and from the uncertainties.
  - **SAFE and Julius:** reword the notes. S2 still returns 429 for both, and J2 is unread.
- **D6b:** reword all three notes, keeping Consensus's as well.

## Before / after
| | Consensus | SAFE | Julius AI |
|---|---|---|---|
| Counted (peer-reviewed) before | 6 (6) | 3 (3) | 2 (1) |
| After (recommended) | 6 (6) | **4 (4)** | 2 (1) |
| Overall / grade | 62 / B, unchanged | 66 / B-, unchanged | Insufficient, unchanged |

## Exact wording (if D1a, D2a, D3, D4a, D5 unchanged, D6a)

### Consensus
- Remove the uncertainty "Citation check incomplete — recheck later (0052: Semantic Scholar unavailable; OpenAlex title screen only)."
- Remove the matching banner "Citation check incomplete — recheck later." from the page.
- Add this uncertainty in its place:
  > 0058 follow-up: a Semantic Scholar search (Oct 2026) found no new independent test; a Cureus 2025 review of the app is a literature review, not a test.
- Add 0058 to the decision records (YAML list and page line).

### Google DeepMind SAFE
- **New source row** (kind: independent performance; peer_reviewed: true; version_tested: unstated; test_date: about early 2025 (arXiv May 2025)):
  > VeriFact (EMNLP 2025; University of Michigan): on 1,168 human-annotated facts, 56.7% of SAFE-extracted facts were incomplete (VeriFact 22.5%) and SAFE covered 77.5% of human-identified facts; the annotated set was chosen for responses with many extraction problems; authors propose an alternative method
- **Count:** performance 3 → 4.
- **Completion note** (insert before "Judgment call."):
  > VeriFact (EMNLP 2025) found 56.7% of SAFE-extracted facts incomplete on a deliberately difficult annotated set.
- **Evidence note:** replace "Three peer-reviewed independent sources" with "Four peer-reviewed independent sources".
- **Uncertainty:** replace "All three independent studies come from researchers proposing competing evaluators." with "All four independent studies come from researchers proposing competing evaluators."
- **Summary:** replace "Independent peer-reviewed studies report agreement" with "Four independent peer-reviewed studies report agreement", and replace "weaker results for its claim extraction" with "weaker results for its claim extraction (including many incomplete extracted facts)".
- **Recheck note** (last uncertainty; the banner stays generic):
  > Citation check incomplete — recheck later (0058: three candidates read in full, one counted; Semantic Scholar still unavailable for SAFE).
- Add 0058 to the decision records.

### Julius AI
- No source, count or status changes.
- **Recheck note:**
  > Citation check incomplete — recheck later (0058: a 2025 comparison study had no hands-on test; a 2025 hands-on demonstration was read as abstract only; Semantic Scholar still unavailable).
- Add 0058 to the decision records.

### Changelog (one row, existing Date / Decision / Change columns)
> 2026-10-17 · 0058 · Google DeepMind SAFE: VeriFact (EMNLP 2025) added as a counted source; 4 counted (4 peer-reviewed); 56.7% of SAFE-extracted facts were incomplete on a difficult test set. Score 66 and grade B- unchanged. Consensus: no new tests found (the only lead was the already-excluded retracted paper); recheck note removed; 62, B unchanged. Julius AI: two 2025 items reviewed, none counted; Insufficient evidence unchanged.

### Expected public file changes
- public/agents/consensus.html
- public/agents/google-deepmind-safe.html
- public/agents/julius-ai.html
- public/changelog.html
- Plus the YAML files and decisions/0058.
- No index or llms.txt change, since no score or grade changes.

## Queue
- **0059 Browser Use** (AgentTell, Privacy Practices, ceLLMate, controlled interventions): queued, to be drafted after 0058 is approved and deployed, or when you say.
- Julius: try to get the J2 full text in a later pass.
- Eye recheck after 2027-01-01 (from 0057).
