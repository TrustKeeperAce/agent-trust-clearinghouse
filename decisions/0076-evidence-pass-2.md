# Decision packet 0076 — Evidence pass 2: Skyvern, Julius AI, Kimi Researcher

**Status: APPROVED by Remington, 2026-10-19: D1a, D2a, D3a, D4a, D5a, D6a, D7a, D8 as recommended (D8: Fellou, no pass now; recheck at the monthly review); implementation and changelog row approved. Deploy needs separate approval.**

Implementation notes (2026-10-19): Data: agents/skyvern.yaml, agents/julius-ai.yaml, agents/kimi-researcher.yaml (`last_reviewed` 2026-10-19). Skyvern: AgentBreaker added as a counted source (`peer_reviewed: true`; version and test date unstated, repository accessed 2025-10-07); 3 counted (1 peer-reviewed); scores 50 / 40 / 30 / 55, overall 44.25 → 44, grade B-. Julius AI: Quality & Quantity 2026 counted (`peer_reviewed: true`; the vendor's complimentary access is stated in the source note and an uncertainty) and IJRSI 2026 counted as limited (`peer_reviewed: false`); Vilakati (Teaching Statistics) recorded as independent other, not counted; Fastero recorded as competitor; 4 counted (2 peer-reviewed); scores 55 / 80 / 50 / 55, overall 58.75 → 59, grade B-; the 0058 recheck note and page banner removed. The `count_note` reads "Three of the four performance sources are limited" rather than the draft's "Two of the four", because the approved item labels the IJRSI study limited. Kimi Researcher: DualGraph (arXiv 2602.13830) added as an uncounted source; the completion note gives its FACT re-score with the parsing caution; recheck uncertainty replaced; stays Insufficient evidence (2 counted). Changelog row 2026-10-19-0076: score_change for skyvern and julius-ai, entry_update for kimi-researcher (as for the 0058 recheck).

*Per-entry drafts referenced below were kept as private working notes and are summarised in this record.*


**Outcome in one line (if recommended options are approved):** Skyvern 2 → 3 counted and Julius AI 2 → 4 counted, so both move from Insufficient evidence to **B-** with first scores (44 and 59). Kimi Researcher stays **Insufficient evidence** (2 counted).

## 0. Selection
Remaining Insufficient entries (excluding Manus, ChatGPT Work, Open Interpreter, done in 0071; and the `example-agent` template):

| Entry | Category | Counted | Last reviewed |
|---|---|---|---|
| autokaggle | Data science agent | 2 | 2026-10-17 |
| clay | Data enrichment | 0 | 2026-10-16 |
| fellou | Browser/web agent | 0 | 2026-10-17 |
| julius-ai | Simple analysis | 2 | 2026-10-16 |
| kimi-researcher | Research | 2 | 2026-10-17 |
| loki | Verification | 2 | 2026-10-17 |
| openfactcheck | Verification | 0 | 2026-10-17 |
| pactum | Negotiation | 1 | 2026-10-16 |
| skyvern | Browser/web agent | 2 | 2026-10-17 |
| ui-tars-desktop | Computer-use agent | 1 | 2026-10-17 |

Picked (3):
- **Skyvern:** widely used open-source browser agent; 1 source short; the security-research literature on web agents is active.
- **Julius AI:** widely used consumer data-analysis tool; 1 source short; 0058 left a recheck note and education journals keep publishing tests.
- **Kimi Researcher:** major deep-research product; 1 source short; several 2026 deep-research benchmarks to check.

Not picked:
- **Fellou** (the possible 4th): the only lead, CAP, was already excluded for Fellou in Decision 0031 (an author interned at FellouAI; FellouAI is listed as an affiliation; PROCESS.md caution 4). No new lead, so a pass would not change the outcome. (Manus's entry already lists CAP as reference-only, so there is nothing to carry over.)
- AutoKaggle and Loki (2 each): smaller research tools with less public interest. UI-TARS Desktop, Pactum, Clay, OpenFactCheck: 0–1 counted, so they would need 2–3 new sources.

## 1. What happened (facts and sources)
Web, arXiv, OpenAlex and publisher searches were run on 2026-10-18 and 2026-10-19 (last batch about 01:55–02:10 ET, 19 Oct). Every candidate counted below was read in full.

### Skyvern
- **AgentBreaker** (Son et al., KAIST / Seoul National University / Oregon State; Proc. ACM Softw. Eng. 3, ISSTA, Article ISSTA074, October 2026; https://doi.org/10.1145/3832165; full text from https://wsp-lab.github.io/papers/son-agentbreaker-issta26.pdf):
  - Five web agents (YuraScanner, Skyvern, Agent-E, BrowserOS, Nanobrowser), all with GPT-4.1, on static copies of 60 sites sampled from Online-Mind2Web. Skyvern repository "Accessed: 2025-10-07"; no release stated.
  - Indirect prompt-injection attack success on Skyvern: 96.7% averaged over four goals (the other four agents: 100%). Earlier baseline attacks reached 0–13.3% on Skyvern's "Terminate" goal.
  - Task success without attack: 33.3% (28.3% with the authors' defence). The proposed mitigations cut attack success to low single digits.
- WASP (arXiv 2504.18575): full text has no mention of Skyvern. ClawBench and CAP: Skyvern not run.

### Julius AI
- **Marmolejo-Ramos, Rojas-Galeano, Ciria, Tejada**, Quality & Quantity, 12 June 2026, https://doi.org/10.1007/s11135-026-02898-5 (open access, full text):
  - BLIS statistical literacy 32/37 (86.49%); all 5 errors on items needing a figure; text-only 26/26.
  - QRDATA: statistical 88/112 (78.6%), social science 20/35 (57.1%), causal 144/264 (54.5%).
  - MathBench probability and statistics subdomains 43.7%–100%.
  - Version, model and test date not stated. Disclosure: "julius.ai [provided] complimentary access".
- **Wolfe, Sawyer, Aga, Park, Sutherland, Smiley**, IJRSI 13(9), published 9 Oct 2026, https://doi.org/10.51244/ijrsi.2026.1309000109 (full text):
  - February 2025 test of 11 tools on a 9-question NAEP 2013 grade-12 math PDF. The paper lists Julius as "1.0.45".
  - Julius identified 4 of the 9 questions, had 5 omissions and got 0 of 5 multiple-choice answers correct.
  - Received 6 Sep, accepted 11 Sep 2026. Shares three authors with the already counted Ohio paper (Sept 2024 multiplication prompt).
- **Vilakati**, Teaching Statistics, 5 Nov 2025, https://doi.org/10.1111/test.70019. Only the preprint was read in full (doi 10.20944/preprints202506.2075.v1): an illustration on a hypothetical 10-row dataset, in which a plain prompt led Julius (GPT-4o) to run a t-test without checking assumptions.
- Not counted:
  - Fastero blog: a competitor.
  - Chang 2025: still closed access.
  - RIDE 2026: PDF blocked; Julius not named in the abstract.
  - Frontiers in AI 2025: Julius not named in the abstract.
  - Vilakati, Dlamini and Shongwe preprint: teaching scenarios.

### Kimi Researcher
- **DualGraph** (Shi et al., Microsoft and others; arXiv 2602.13830, Feb 2026):
  - Its Table 1 lists "Kimi (Res.)" at RACE 46.50, FACT citation accuracy 20.80, effective citations 2.30.
  - The authors "obtain the reports of proprietary systems from DeepResearch Bench and re-evaluate them" with a GPT-4.1 judge. These are the same Kimi outputs as counted source 1.
- The DeepResearch Bench leaderboard (Hugging Face `muset-ai/DeepResearch-Bench-Leaderboard`, data/leaderboard.csv, read 2026-10-19) still shows no FACT values for kimi-researcher.
- DeepResearchEval (arXiv 2601.09688; 9 systems) does not include Kimi. FINDER (arXiv 2512.01948) has a "Kimi K2" row that cites the model paper, not the Deep Research product. DeepResearch Bench II does not include Kimi.

## 2. What the rules say (Scoring rules v0.1, unchanged)
- An overall score needs at least 3 **independent performance sources**. These are tests that report their method and results: benchmarks, studies, documented hands-on tests, and security or safety evaluations.
- Reviews, commentary, competitor benchmarks and vulnerability listings are **other** sources.
- A source counts only if it tested the product, version and scope of the entry. Each study counts once.
- Independent means not the vendor, a customer's staff, or a competitor promoting itself. A source sharing authors with the developer is excluded (CAP/Fellou precedent). Competing-method authors count, with disclosure. Partial independence is labelled.
- Grades: Insufficient below 3 sources; B- for 3–4; B for 5–6 (or 7+ without the A conditions); A for 7+ with 3+ peer-reviewed and a current-version test within 12 months.
- Overall score = 0.30 completion + 0.20 disputes + 0.25 adherence + 0.25 evidence, rounded half up. Evidence guide: B- 55–69.
- Precedent 0058: a demonstration that is "not a measured accuracy test" was not counted (Chang).

## 3. Proposed changes (before → after, recommended options)
| | Skyvern | Julius AI | Kimi Researcher |
|---|---|---|---|
| Counted | 2 → **3** | 2 → **4** | 2 → 2 |
| Peer-reviewed counted | 0 → 1 | 1 → 2 | 1 → 1 |
| Other | 3 → 3 | 4 → 5 (+Vilakati); +1 competitor (Fastero) | 1 → 2 (+DualGraph re-score) |
| Grade | Insufficient → **B-** | Insufficient → **B-** | Insufficient (unchanged) |
| Scores (C / D / A / E) | null → 50 / 40 / 30 / 55 | null → 55 / 80 / 50 / 55 | null |
| Overall | null → **44** (44.25) | null → **59** (58.75) | null |
| Text | summary, 3 factor notes, 2 uncertainties | summary, all factor notes, uncertainties; 0058 recheck note removed | completion note (FACT re-score), recheck uncertainty replaced |

## 4. Risks and uncertainties
- **Both upgrades sit at or near the minimum.** Skyvern has exactly 3 sources; if any one is corrected or withdrawn, it returns to Insufficient. Julius has 4, or 3 without IJRSI.
- **No counted source states a product version** for Skyvern. AgentBreaker's repository access date (7 Oct 2025) places it inside the entry scope only by inference.
- **AgentBreaker** used static pages and attacks tuned to each agent. Its 33.3% task success is a side measurement.
- **Julius J3** states no version, model or test date, and the vendor gave free access (disclosed).
- **Julius J4** is in a low-assurance venue (5 days from receipt to acceptance), only partly fits the scope (a PDF math worksheet), and comes from the same group as the Ohio paper.
- **Julius scores** rest on mixed evidence: strong on text statistics, weak on figures and PDFs, and one source ran with code execution disabled. The 2026 product and billing changes are untested.
- **Rule boundary:** Vilakati (peer-reviewed) is a hands-on illustration with an observed error. Not counting it follows 0058, but the line between "documented hands-on test" and "illustration" is not defined. The earlier counted Ohio single-prompt paper is close to that line.
- **Kimi FACT re-score** may reflect the citation-parsing problem that DeepResearch Bench reported, not citation quality.
- **Sources that could not be fully read:**
  - ACM page (timed out; the authors' PDF was used instead).
  - Teaching Statistics journal version (Cloudflare block).
  - RIDE PDF (HTTP 406).
  - Chang (closed access).
- **Search coverage:** web index, arXiv and OpenAlex only; the Semantic Scholar gate was not rerun.

## 5. Decision items
- **D1 Skyvern: count AgentBreaker?**
  - a) Count it, giving 3 counted (1 peer-reviewed) (**recommended**: independent, peer-reviewed, ran the open-source agent).
  - b) Record it as other. Skyvern stays Insufficient at 2.
  - c) More info: ask the authors for the Skyvern commit or release before counting.
- **D2 Skyvern grade and scores (grade-changing; only if D1a).**
  - a) B-, with completion 50, disputes 40, adherence 30 and evidence 55, giving overall 44 (**recommended**).
  - b) B-, with completion 55, giving 46.
  - c) B-, with evidence 50 because two of the three share authors, giving 43.
  - d) Reject: keep Insufficient until a fourth source arrives.
- **D3 Julius: count Quality & Quantity (J3)?**
  - a) Count it, labelled "vendor provided complimentary access" (**recommended**).
  - b) Count it as partially independent.
  - c) Don't count it.
- **D4 Julius: count IJRSI (J4)?**
  - a) Count it, labelled limited, with `peer_reviewed: false` (**recommended**: a different study from Ohio, with stated method and results).
  - b) Don't count it (low-assurance venue).
  - Either way Julius reaches 3 or more if D3a is approved.
- **D5 Julius: Vilakati (Teaching Statistics).**
  - a) Record it as other, not counted, because it is an illustration on constructed data (0058 precedent) (**recommended**).
  - b) Count it (peer-reviewed hands-on demonstration), giving 5 counted and B (grade-changing to B rather than B-; not recommended).
  - c) More info: read the journal version first.
- **D6 Julius grade and scores (grade-changing; only if D3a).**
  - a) B-, with completion 55, disputes 80, adherence 50 and evidence 55, giving overall 59 (**recommended**).
  - b) B-, with completion 60, giving 60.
  - c) Reject: keep Insufficient pending a test of the 2026 product.
- **D7 Kimi Researcher.**
  - a) Stays Insufficient. Add DualGraph as an other source, add the FACT re-score to the completion note with a caution, and replace the recheck uncertainty (**recommended**).
  - b) Count DualGraph, giving 3 and B- (grade-changing; not recommended because it re-scores the same outputs).
  - c) No change.
- **D8 Fellou:** no pass. CAP stays excluded (0031). Recheck at the monthly review.
- **D9 Publishing:** implementing, adding checks if needed, adding a changelog row, committing, pushing and deploying each need separate approval. Not requested here.

## 6. MVP (smallest approvable set)
- Approve **D1a + D2a** (Skyvern B-, 44) and **D3a + D4a + D5a + D6a** (Julius B-, 59), plus **D7a** (Kimi note only).
- Data edits would be limited to `agents/skyvern.yaml`, `agents/julius-ai.yaml` and `agents/kimi-researcher.yaml`, plus `decisions/0076-evidence-pass-2.md`. The site would be regenerated and `check_scores.py` and `check_export.py` run.
- One changelog row would follow, after separate approval.
- If you prefer the narrowest change: D7a only (Kimi note), with Skyvern and Julius deferred under D1c / D5c.

## 7. Plain-English terms
- **Insufficient evidence:** fewer than 3 qualifying independent tests, so no score and no grade.
- **Independent performance source:** a test by someone other than the maker that explains how it tested and what it found.
- **Counted:** the source tested this product, in the scope the entry covers.
- **Other source:** useful background that does not count toward the 3 (commentary, re-scoring of someone else's data, vulnerability listings).
- **Grade-changing:** a decision that would move an entry from Insufficient to a letter grade, or between grades.
- **Prompt injection:** hidden instructions in content the agent reads that make it do something the user didn't ask for.
- **Attack success rate:** the share of attempts in which an attack made the agent do what the attacker wanted.
- **Re-scoring:** applying a new scoring method to outputs someone else already collected; no new run of the product.
- **Low-assurance venue:** a journal whose review process could not be confirmed (for example, very fast acceptance).

*Informational only; not a guarantee, endorsement, or certification.*
