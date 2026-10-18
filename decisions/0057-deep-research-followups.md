# Decision 0057: OpenAI Deep Research and Gemini Deep Research follow-ups (from 0052 sweep)

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1a count MisKnow-Agent for Gemini (8 counted, 2 peer-reviewed); D2a AMCIS 2026 paper not counted (abstract only; forecasting outside scope); D3a nothing counted for OpenAI (ANZ J Surg perspective; Eye brief communication paywalled, recheck after 2027-01-01); D4 scores unchanged (Gemini 63 / B with one completion-note sentence; OpenAI 65 / B); D5a recheck notes reworded.

Entries:
- **OpenAI Deep Research:** 65 / B. 5 counted performance sources (2 peer-reviewed), 2 other.
- **Gemini Deep Research:** 63 / B. 7 counted performance sources (2 peer-reviewed), 2 other. It already has one current-version test inside the 12-month window (Gemini 3.1 Pro API agent).

Neither entry has a separate scope line, so each covers the product as a whole: research reports with citations.

## Plain-English terms
- **Counted source:** an independent test that counts toward the evidence grade.
- **Grade A:** needs all three:
  1. 7 or more counted sources;
  2. 3 or more of them peer-reviewed;
  3. a test within the last 12 months that states the version (or a dated test of a named tier, for hosted products).
- **Preprint:** a paper posted online that has not been peer-reviewed.
- **Perspective / brief communication:** a short opinion or summary piece, not a full study.
- **FCAR (false-conclusion adoption rate):** the share of reports that end up endorsing a false claim that was planted in their sources.

## Research done
- Full reads:
  - C1 (open access via Europe PMC).
  - C4 (arXiv v2 PDF).
- Partial reads:
  - C2: publisher page and metadata. Full text is paywalled; the PMC copy is embargoed until 1 Jan 2027.
  - C3: abstract and proceedings page. Two attempts to fetch the PDF were blocked by a bot check.
- Semantic Scholar retry: 23:22–23:28 ET, 10 tries, every one HTTP 429. No new candidates found.

## Per-candidate findings
| # | Item | Independence | Peer review | Product / version / date | Scope fit | Results | Counted? |
|---|---|---|---|---|---|---|---|
| C1 | Jesudason, Gao, Seth, Chan, Bacchi, "OpenAI's 'Deep Research' for the Generation of Comprehensive Referenced Medical Text: Uses and Cautions", ANZ J Surg 2025;95(11):2250–2252, 10.1111/ans.70161 | Independent (Univ. of Adelaide, Peninsula Health, Harvard). No conflicts; Fulbright support for one author | Published in a peer-reviewed journal, but the article type is **Perspective** | OpenAI Deep Research (Feb 2025 release). Two example outputs in the supplement; no version or tier | OpenAI entry: topic fits, but there is no measured test | No measurements. Opinion on the benefits and risks: it can't see paywalled papers, may be biased, gives different outputs for the same prompt | **No.** Commentary, not a test |
| C2 | Loke, Srinivasan, Yang, Zou, Ong, Zhu, Antaki, Keane, Tham, "Can 'Deep Research' agents and general AI agentic systems autonomously perform systematic review and meta-analysis?", Eye 2026;40:147–149 (online 28 Nov 2025), 10.1038/s41433-025-04138-w | Independent (NUS, SNEC/SERI, Moorfields/UCL, Melbourne, Cleveland Clinic). Only competing interest: one author is on Eye's editorial board | Yes (Brief Communication; received 15 Sep 2025, accepted 17 Nov 2025) | Its references cite Gemini Deep Research, OpenAI Deep Research and Perplexity Deep Research product pages, accessed Apr 2025. Version, tier and results are behind a paywall | Possibly fits both entries: end-to-end systematic reviews | **Not readable:** full text paywalled, PMC embargoed until 1 Jan 2027 | **No.** Not reviewed (same rule as the paywalled Bloomberg source). Recheck after the embargo lifts |
| C3 | Pan, Cui, Yang, "Can Generative AI Truly Democratize Investment Analysis? An Evaluation of Gemini Deep Research", **AMCIS 2026 Proceedings** (AIS eLibrary; indexed as JAIS but it is a conference paper, "Complete" type), 15 Aug 2026 | Independent (Stevens Institute of Technology). Funding and conflicts not visible | Likely (the authors list it as "Peer-reviewed Conference Proceedings"). Not checked against the full paper | Gemini Deep Research. 2,845 forecasts, **May–Oct 2025**. Version and tier not visible in the abstract | Weak for the Gemini entry: tests stock-direction forecasting, not research or citation quality | Per the abstract: direction calls no better than chance at every horizon; portfolios built on its signals underperformed the index; its outlook "tracks source sentiment and visibility" | **No.** Abstract only (Hilkenmeier precedent) and weak scope fit |
| C4 | Zhu, Li, Yang, Su, Shao, "Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions", arXiv 2607.20891v2 (30 Jul 2026) | Independent (Beijing Univ. of Posts and Telecommunications, Shanghai AI Laboratory, Chongqing Univ. of Posts and Telecommunications). No Google authors or funding seen | **No** (preprint) | **Gemini Deep Research** (consumer product). Misleading documents were supplied through its local-source (file) interface with its own web search left on. Version not stated; product page accessed 2026-07-06, so the test was about July 2026 | Fits the Gemini entry: whether its reports adopt false claims from credible-looking sources. Not about OpenAI Deep Research | Gemini Deep Research false-conclusion rate:<br>- by source authority: 54% high, 46% medium, 8% low<br>- by source style: papers 54%, blogs 41%, news 34%, social posts 28%<br>- by number of misleading documents: 27% with one, 54% with three, 50–56% with four or five<br>(Open-source systems: mean 0% → 54.7% after one planted document) | **Yes** (recommended), for Gemini only |

S2 snapshot: still rate-limited; no other candidates screened.

## D-items

**D1. C4 (MisKnow-Agent) for Gemini Deep Research**
- **D1a (recommended):** count it as an independent performance source (robustness to misleading sources). Not peer-reviewed; version unstated; test date about July 2026. Gemini goes from 7 to **8 counted, still 2 peer-reviewed**.
- **D1b:** list it as uncounted context only.

**D2. C3 (AMCIS 2026, stock forecasts)**
- **D2a (recommended):** don't count it. It's abstract-only, and it measures forecasting, which is outside the entry's research-report scope. Mention it in decisions/0057 only.
- **D2b:** count it as peer-reviewed. That would give Gemini 9 counted / 3 peer-reviewed alongside the existing 3.1 Pro test, so **B → A (grade-changing).** Not recommended: it isn't fully read, and it would bring in a forecasting study through scoring.

> **Grade-change flag:** a third peer-reviewed counted source is the only thing between Gemini and grade A. C2 (if it turns out to test Gemini once readable) or C3 (if fully read and judged in scope) could each do that in a future packet. Nothing here changes the grade.

**D3. C1 and C2 for OpenAI Deep Research**
- **D3a (recommended):** count neither. C1 is a Perspective with no test; C2 isn't readable. OpenAI stays at 5 counted / 2 peer-reviewed. Record both in decisions/0057; C2 is flagged for recheck after 1 Jan 2027.
- **D3b:** count C2 from its metadata. Not recommended: we haven't read what it tested or found.

**D4. Factor scores (honest reasoning, nothing changed to fit a grade)**

*Gemini Deep Research*

| Factor | Score | Reasoning |
|---|---|---|
| Completion | 60, unchanged | C4 adds a reliability weakness (it adopts planted false claims from high-authority, paper-style sources about half the time). That is consistent with the existing note on hallucinated and non-resolving citations. It's one preprint with a single unstated version, so not enough on its own to move the score. Add a sentence to the note |
| Disputes | 65, unchanged | No new disputes |
| Adherence | 55, unchanged | C4 is about judging evidence, not limits or permissions |
| Evidence | 72, unchanged | One more counted source, but a preprint with an unstated version. Still inside the B guide band |

- Overall: 0.30×60 + 0.20×65 + 0.25×55 + 0.25×72 = 18 + 13 + 13.75 + 18 = **62.75 → 63**. **Grade B unchanged.**
- Grade A conditions:
  - 8 counted sources ✓
  - 2 peer-reviewed ✗ (needs 3)
  - recent test that states the version ✓ (3.1 Pro test)
- Alternative D4-alt: completion 60 → 55, giving 61.25 → 61, still B. Not recommended: a single preprint is thin for a score drop.

*OpenAI Deep Research*
- All scores unchanged (60 / 65 / 60 / 75): nothing new is counted.
- Overall: 0.30×60 + 0.20×65 + 0.25×60 + 0.25×75 = 18 + 13 + 15 + 18.75 = **64.75 → 65**. **Grade B unchanged.**
- Grade A conditions:
  - 5 counted sources ✗ (needs 7)
  - 2 peer-reviewed ✗ (needs 3)
  - no recent test that states the version ✗

**D5. Recheck notes (both entries)**
- **D5a (recommended):** reword both notes, keeping "Citation check incomplete — recheck later". Semantic Scholar is still unavailable, and C2/C3 aren't readable yet.
- **D5b:** leave the 0052 wording as is.

## Before / after
| | Gemini before | Gemini after (D1a) | OpenAI before | OpenAI after |
|---|---|---|---|---|
| Counted performance sources | 7 | **8** | 5 | 5 |
| Peer-reviewed | 2 | 2 | 2 | 2 |
| Other | 2 | 2 | 2 | 2 |
| Overall / grade | 63 / B | 63 / B | 65 / B | 65 / B |

## Exact wording (if D1a, D2a, D3a, D4 unchanged, D5a)

### Gemini Deep Research
- **New source row** (kind: independent performance; peer_reviewed: false; version_tested: unstated; test_date: about Jul 2026 (product page accessed 2026-07-06)):
  > Is Deep Research Reliable? (MisKnow-Agent; Beijing University of Posts and Telecommunications, Shanghai AI Laboratory; preprint, Jul 2026): misleading documents supporting false conclusions were supplied through Gemini Deep Research's file interface with web search on. Reports adopted the false conclusion in 54% of cases with high-authority sources, 46% medium and 8% low; 27% with one misleading document and 50–56% with three to five. Robustness test, not task completion
- **Count:** performance 7 → 8. Scoreline: "Independent sources: 8 performance, 2 other".
- **Completion note** (insert before "Judgment call."):
  > In a preprint robustness test (MisKnow-Agent, July 2026), its reports adopted planted false conclusions in up to 54% of cases when the misleading sources looked authoritative.
- **Evidence note:** replace "Seven independent performance sources, two peer-reviewed" with "Eight independent performance sources, two peer-reviewed".
- **Summary:** replace "Mind2Web 2, NeurIPS 2025; five preprints)" with "Mind2Web 2, NeurIPS 2025; six preprints)".
- **Recheck note** (last uncertainty; the banner stays generic):
  > Citation check incomplete — recheck later (0057: four 2025–2026 candidates screened, one counted; an Eye brief communication is paywalled until 2027 and an AMCIS 2026 forecasting paper was read as abstract only; Semantic Scholar still unavailable).
- **YAML:** decision_packet becomes a list that adds decisions/0057-deep-research-followups.md. The page gets a "Decision records" line (0015; 0057).

### OpenAI Deep Research
- No source, count or score changes.
- **Recheck note** (last uncertainty):
  > Citation check incomplete — recheck later (0057: an ANZ J Surg perspective was not a test; an Eye brief communication is paywalled until 2027; Semantic Scholar still unavailable).
- **YAML:** add decisions/0057 to the decision record list (0003, 0019 recheck, 0057), plus the matching page line.

### Changelog (one row, existing Date / Decision / Change columns)
> 2026-10-17 · 0057 · Gemini Deep Research: MisKnow-Agent (robustness preprint, July 2026) added as a counted source; 8 counted (2 peer-reviewed); reports adopted planted false conclusions in up to 54% of cases. Scores and grade unchanged (63, B). OpenAI Deep Research: two items reviewed, none counted (one perspective, one paywalled); 65, B unchanged. Recheck notes updated.

### Expected public file changes
- public/agents/gemini-deep-research.html
- public/agents/openai-deep-research.html
- public/changelog.html
- Plus the YAML files and decisions/0057.
- No index or llms.txt change, since no score or grade changes.

## Queue
- Recheck C2 (Eye) after 1 Jan 2027.
- Try C3 (AMCIS) full text again.
- Remaining 0052 follow-ups: Consensus, Google DeepMind SAFE, Julius AI, and the other Browser Use candidates.
