# Decision 0021: Claude Research (candidate 6)

**Status: APPROVED by Remington, 2026-10-17**, with 58 / B-. The approval was conditional on the JEADV letter having been read in full. **Full-text confirmation:** I read Keplinger et al. (doi 10.1111/jdv.70035) in full from the Europe PMC full-text XML (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13109748/fullTextXML; open access, CC BY-NC). That covered the whole letter, Table 1, the Figure 1 legend, limitations, conclusion, funding and the conflict-of-interest statement, not only the abstract.

Decisions:
1. Continuity is read as in 0019: the same feature across model swaps. A version note says the 2025 tests are counted and the current Opus 5.5 is untested.
2. Mind2Web 2 is counted, with a disclosure of Amazon AGI co-authors and Amazon's investment in Anthropic.
3. DeepResearchEval is counted, with a note on the "Sonnet 4.5" label.
4. The JEADV letter is counted.
5. Category: Research.

## What happened (Anthropic primary sources)
- 15 Apr 2025: Research launched in early beta for Max, Team and Enterprise plans in the US, Japan and Brazil (https://claude.com/resources/articles/research). It used multiple connected web searches and Google Workspace, and did not use a custom model.
- 1 May 2025: an "advanced" Research mode added Integrations and runs of up to 45 minutes (Anthropic LinkedIn post; TechCrunch https://techcrunch.com/2025/05/01/anthropic-lets-you-connect-apps-to-claude/).
- Now: still called "Research", available on the Pro, Max, Team and Enterprise plans (https://support.claude.com/en/articles/11088861-use-research-on-claude).
  - It "runs on Claude Opus 5.5 and falls back to Claude Opus 4.8", regardless of the model selected for the chat.
  - It uses connector tools "automatically, without asking for approval each time".
  - On mobile it silently skips connectors.
- Claude Opus 5.5 was released on 22 Sep 2026 (https://www.anthropic.com/claude-opus-5-5).
- Continuity: the same named feature has been offered continuously, with model swaps over time (3.7 / Opus 4 / Sonnet 4.5 era to Opus 5.5). This is the 0019 OpenAI Deep Research pattern, not the 0008 rewrite or 0018 retirement. I read it as continuous, with a version note. Not retired.

## Counted independent performance sources (4; 3 peer-reviewed; all 2025)
1. DeepResearch Bench, ICLR 2026 camera-ready (USTC / MetaStone) https://proceedings.iclr.cc/paper_files/paper/2026/file/465f22be10e07b301c6ed58f0472f704-Paper-Conference.pdf
   - Claude Research is absent from arXiv v1 (https://arxiv.org/abs/2506.11763), which has only Claude-3.7/3.5 with search via API. The repo says it was added on 15 Jul 2025, and the ICLR paper includes it.
   - Method reported: outputs collected 23–25 Jun 2025 from the official UI. The FACT citation metrics are missing because citation links could not be parsed from the UI.
   - Results: RACE 45.00 (comprehensiveness 45.34 / depth 42.79 / instruction-following 47.58 / readability 44.66), 15th of 31 on the leaderboard; OpenAI DR 46.45, Gemini DR 49.71. The paper calls Claude Research "statistically indistinguishable" from the mid-tier agents. Judged by Gemini-2.5-Pro.
2. Mind2Web 2, NeurIPS 2025 D&B (Ohio State; Amazon AGI co-authors) https://arxiv.org/abs/2506.21506
   - Claude Research: partial completion 0.32, success 0.10, pass@3 0.19; 742 s average time.
   - Disclosure: Amazon is a major investor in Anthropic.
3. DeepResearchEval, preprint (Shanda / Infinity) https://arxiv.org/abs/2601.09688
   - "Claude-Sonnet-4.5 Deep Research", downloaded from the official website on 19–28 Aug 2025.
   - Results: quality 7.53/10, 2nd of 9; factual ratio 60.72%, 8th of 9.
   - Label inconsistency: Sonnet 4.5 was released on 29 Sep 2025, after the collection dates.
4. Keplinger et al., JEADV 2026 letter (West Virginia University; received 4 Jun 2025) https://doi.org/10.1111/jdv.70035
   - "Claude Opus 4 Research", three runs of a dermatology review.
   - Fake authors or titles in 95.8 ± 7.2% of references (ChatGPT DR 4.3%).

## Listed, not counted
- LiveResearchBench, ReportBench and DeepResearch Bench II tested Claude API models (Claude 4 Sonnet / 4.1 Opus), not the Research feature. DeepResearch Bench II does not include Claude Research.
- Rao, Wong, Callison-Burch (https://arxiv.org/abs/2604.03173) analysed only claude-3.5/3.7-sonnet-with-search and claude-sonnet-4-5 via API (hallucinated URLs 3.0–3.2%). There is no Claude Research row, so it is out of scope.
- Security: I found no incident specific to Research. Claude-wide findings are context only, not counted:
  - Oasis "Claudy Day": prompt injection exfiltrating data via the Files API (https://www.oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability).
  - Embrace The Red "Claude Pirate": Code Interpreter exfiltration via the Files API (https://www.mbgsec.com/archive/2025-10-30-claude-pirate-abusing-anthropic-s-file-api-for-data-exfiltration-embrace-the-red/).
- Excluded: Anthropic's own evaluations and marketing claims.

## Score breakdown (proposed)
- Completion 50: mid-tier report quality (DRB 15th of 31; DRE 2nd of 9); 10% full success on Mind2Web 2; 95.8% fake references in the dermatology test. Judgment call.
- Disputes 75: no lawsuit, regulatory action or incident specific to Research; Claude-wide prompt-injection exfiltration findings noted. Judgment call.
- Adherence 50: weak factual accuracy (60.7%); fabricated references; connector tools are used without per-call approval (vendor documentation). Judgment call.
- Evidence 60: 4 sources, 3 peer-reviewed; all from 2025 on earlier models; no test of Opus 5.5; Amazon tie (Mind2Web 2); no FACT scores on DRB. Judgment call.
- Overall = 0.30*50 + 0.20*75 + 0.25*50 + 0.25*60 = 57.5, which rounds half up to **58**. Grade **B-** (3–4 sources).

## Decision points
1. Continuity: accept the 0019-style reading across the model swaps to Opus 5.5 (recommended)? The alternative is the 0008 reading, which gives Insufficient evidence.
2. Mind2Web 2 and Amazon AGI co-authors: count it with a disclosure (recommended)? Note that ChatGPT Work already notes these co-authors. Treating it as partly independent leaves 3 sources and still B-.
3. DeepResearchEval label inconsistency (Sonnet 4.5 named before its release): count it as the product, since it was downloaded from the official site?
4. The JEADV letter is a three-run, small sample. Count it (drafted: yes)?
5. Category: Research.
