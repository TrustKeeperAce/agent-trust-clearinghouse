# Decision 0026: STORM / Co-STORM (Stanford OVAL) — batch 3, candidate 3

**Status: APPROVED by Remington, 2026-10-17. Overall 56, grade B.** All 8 recommendations were approved:
- D1: knowledge-storm library only; results shown as model ranges; hosted demo excluded.
- D2: one combined entry, with Co-STORM results labelled.
- D3: v1.0.0 to 1.1.1 continuous; the 2024 NAACL branch is historical.
- D4: active but dormant ("no code changes since 30 Sep 2025").
- D5: grade B.
- D6: DeepScholar-Bench counted, with a Stanford-affiliation disclosure.
- D7: neutral security wording; the reporter's severity claims are not repeated as fact.
- D8: category Research. Researched 2026-10-17. YAML: `storm.yaml`.

## What happened (with sources)

**Product and status**
- <https://github.com/stanford-oval/storm>: MIT licence, PyPI `knowledge-storm`, about 31.7k stars, not archived.
- Timeline:
  - STORM paper: NAACL 2024.
  - Co-STORM: EMNLP 2024; merged into knowledge-storm v1.0.0 (Sept 2024).
  - v1.1.0 (Jan 2025): litellm support.
  - v1.1.1 (29 Sept 2025): only loosened requirements.
- **Last code commit: fb951af, 30 Sept 2025.** Outside PRs in 2026 (#416, #483) were closed unmerged. 111 open issues.
- Hosted research preview <https://storm.genie.stanford.edu/> answers HTTP 200.
- **Status: not retired (0018 not triggered), but dormant for about 12.5 months.**

**Counted independent performance sources (7; full texts read). All were run by authors of competing systems or benchmarks.**

| # | Source | Peer review | Mode tested | Key figures |
|---|---|---|---|---|
| 1 | WriteHERE, <https://aclanthology.org/2025.emnlp-main.1254/> | EMNLP 2025 | STORM v1.1.0 + Co-STORM, rerun | GPT-4o: 4.76/4.58/4.30/4.32 of 5; Claude 3.5: 4.66/4.63/4.40/4.41. Co-STORM 4.36–3.46. v1.1.0 slightly better than the NAACL branch |
| 2 | OmniThink, <https://aclanthology.org/2025.emnlp-main.50/> | EMNLP 2025 | STORM + Co-STORM, reproduced | WildSeek GPT-4o 4.34/4.21/4.21/3.80; as low as 2.42 with other backbones |
| 3 | MOG, <https://aclanthology.org/2025.acl-long.1423/> | ACL 2025 | STORM | Citation recall/precision 77.49/75.71% (FreshWiki), 67.72/66.50% (WikiStart) |
| 4 | CogGen, <https://aclanthology.org/2026.findings-acl.296/> | Findings ACL 2026 | STORM + Co-STORM | Relative score 0.3205/0.3351 (0.50 = parity with reference); Co-STORM 0.3227/0.3147 |
| 5 | MySQA, <https://aclanthology.org/2026.acl-long.723/> | ACL 2026 | STORM | Answer coverage 72.0% (lowest of 6), citation precision 73.3%, recall 64.7%. Ai2 makes the competing ScholarQA |
| 6 | ScaffoldAgent, <https://arxiv.org/abs/2606.20122> | preprint 2026 | STORM | DeepResearch Bench RACE 32.81 (Qwen3-32B) / 35.26 (DeepSeek-V3.2), lowest of the multi-agent baselines; citation accuracy 36.90/38.59% |
| 7 | DeepScholar-Bench, <https://arxiv.org/abs/2508.20033> | preprint | STORM (Llama-4) | Geometric mean .073 (OpenAI DR .309, human .782); citation precision .238; claim coverage .586. Stanford (Guestrin group, not OVAL) + Berkeley |

**Not counted**
- **Developers' own papers** (vendor claims): STORM, <https://arxiv.org/abs/2402.14207> (FreshWiki; editor study, where 7 of 10 editors called the tone "emotional" or "unneutral"), and Co-STORM, <https://arxiv.org/abs/2408.15232>.
- **Reused developer numbers:** DeFine, <https://arxiv.org/abs/2503.07170>.
- **STORM mentioned but not tested:**
  - DeepResearch Bench itself (<https://arxiv.org/abs/2506.11763>): STORM is not in the paper.
  - Rao et al. reference-hallucination study (2604.03173), Search Shapes Conclusions, DREAM, AutoSurvey, SurveyX, WebWeaver, LLM×MapReduce-V2, Benchmarking Hybrid DR, Ai2 meta-evaluation (lists STORM in a table only).
  - FrankenReport modifies the STORM pipeline rather than evaluating it.
- **No STORM in:** DeepResearchGym, ReportBench, DRBench, Wiki Live Challenge, SurveyBench, DeepSurvey-Bench, HiEviDR-Bench, DeepSynth-Eval, MMDeepResearch-Bench.

**Disputes and security (other sources)**
- [Issue #375](https://github.com/stanford-oval/storm/issues/375), 1 Jul 2025, Obscure Labs: reports an improper certificate validation problem (CWE-295) and asks for a private channel. **No maintainer reply in more than 15 months.**
- The code at fb951af confirms it: `WebPageHelper` downloads web pages with `httpx.Client(verify=False)` ([utils.py](https://github.com/stanford-oval/storm/blob/fb951af/knowledge_storm/utils.py)).
- No CVE, no GitHub advisory, no legal or regulatory action, and no Wikipedia-community enforcement found.

## What the rules say
- v0 weights 30/20/25/25, rounded half up; at least 3 counted sources needed.
- **Grades:** A = 7+ sources, 3+ peer-reviewed, and 1+ testing the current version within 12 months. The 0025 clarification says 7+ sources failing an A condition = B.
- Developers' (OVAL) papers count as vendor claims. Competing authors count with disclosure.
- **Continuity:** like 0016/0025 (library). One package from v1.0.0 to v1.1.1 with no rewrite, so it is continuous. The 2024 NAACL branch is historical context. WriteHERE found v1.1.0 slightly stronger than that branch, not a break.
- **0018 retired-product rule:** not applicable. The repo is live and not archived, and the demo is up.

## Proposed score (recommended)

| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion | 30 | 50 | Always produces full cited articles; ranks at or near the bottom against newer systems (RACE 33–35, relative score 0.32–0.34, lowest coverage in MySQA) |
| Disputes | 20 | 55 | Unanswered security report since Jul 2025, confirmed in code; dormant maintenance; no legal issues |
| Adherence | 25 | 45 | Citations support claims about 65–77% of the time (DeepScholar precision .24, DRB citation accuracy 37–39%) |
| Evidence | 25 | 75 | 7 sources, 5 peer-reviewed, 3 from 2026; all by competing authors; mostly LLM-judge relative scores; library version unstated except one 2025 study |

**0.30×50 + 0.20×55 + 0.25×45 + 0.25×75 = 56.00 → 56. Grade B.**
- Why not A: no source within 12 months states that it tested the current version (1.1.x).
- Index position: between Claude Research (58) and Perplexity (54).

**Alternative:** if you accept that the 2026 studies (CogGen, MySQA, ScaffoldAgent) tested the current code because nothing has changed since Sept 2025, A conditions are met. Evidence would be about 85 → 0.3×50 + 0.2×55 + 0.25×45 + 0.25×85 = 58.50 → **59, grade A**.

## Decisions needing your approval
1. **D1 Scope:** the knowledge-storm library only, with results given as model ranges (like Browser Use / Agent S). The hosted research preview is excluded because no independent test of it was found.
2. **D2 One entry for STORM + Co-STORM** as modes of one package, with Co-STORM results labelled. A separate Co-STORM entry would have 3 sources (OmniThink, WriteHERE, CogGen): B-, with no test of its human-collaboration mode.
3. **D3 Continuity:** v1.0.0 to v1.1.1 continuous; NAACL 2024 branch historical.
4. **D4 Status:** not retired; state "no code changes since 30 Sept 2025" on the page.
5. **D5 Grade:** B (current-version condition not met), not A. The alternative is 59/A.
6. **D6 Count DeepScholar-Bench** despite the Stanford affiliation (different group, not OVAL), with disclosure.
7. **D7 Security:** describe issue #375 neutrally ("reported; no maintainer reply"), together with what the code shows (certificate verification disabled for web-page downloads). Don't repeat the reporter's "high-severity" or credential-exfiltration claims as fact.
8. **D8 Category:** Research.

## Risks and uncertainties
- Relative LLM-judge scores are not success rates. "Completion" is a judgment call based on rankings.
- All counted sources are by competing authors. Older backbones (GPT-4o-era) are common.
- The developers' editor study raises neutrality and tone concerns, but it is a vendor source.

## Plain-English terms
- **RACE / FACT (DeepResearch Bench):** report quality compared with a reference report (50 = equal) / how often citations actually support the text.
- **Relative score 0.50:** as good as the reference report.
- **Citation recall / precision:** share of sentences backed by their citations / share of citations that are relevant.
- **Dormant:** still published but not being changed.
- **CWE-295:** software that doesn't properly check website security certificates.
