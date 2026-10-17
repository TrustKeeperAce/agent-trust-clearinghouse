# Decision 0024: Kimi Researcher (batch 3, candidate 1)

**Status: APPROVED by Remington, 2026-10-17**, as Insufficient evidence, as recommended. Decisions:
1. Continuous product.
2. ICBCBench is counted, with a disclosure of the Alibaba co-authors and of the missing access method and dates.
3. The résumé leak is listed as a dispute affecting Kimi generally, not Deep Research specifically, with sources.
4. WebResearcher and the Moonshot vendor claims are not counted.
5. Category: Research.

## 1. What happened (Moonshot AI primary sources)
- 20 Jun 2025: Kimi-Researcher was announced and rolled out gradually (https://moonshotai.github.io/Kimi-Researcher/). It was described as an agent RL-trained end to end on "an internal version of the Kimi k-series model".
- Now: offered as **Deep Research** at kimi.com/deep-research and in the app. The help page calls it "Kimi's first Agent product, powered by the Kimi-Researcher model"; it takes 10–25 minutes and produces a 10,000+ word cited report plus an HTML report (https://www.kimi.ai/help/deep-research/deep-research-overview).
- Kimi's general models changed: K2, then K2.5 (Jan 2026), then K2.6 (Apr 2026), then K3 (16 Jul 2026), plus Agent Swarm (https://www.kimi.com/en/help/agent/agent-overview).
  - The Deep Research help pages still name the Kimi-Researcher model, with no announced swap to K3.
  - ICBCBench describes Kimi-deep-research as "Kimi-Researcher (trained on Kimi k1.5)".
- **Continuity:** the same named feature and the same named model, continuously offered. Read it as continuous (0003/0015/0019), not as a rewrite (0008/0020). Not retired.

## 2. Counted independent performance sources (2; read in full)
1. **DeepResearch Bench, ICLR 2026** (USTC / MetaStone) https://proceedings.iclr.cc/paper_files/paper/2026/file/465f22be10e07b301c6ed58f0472f704-Paper-Conference.pdf
   - Collected 29 Jun–1 Jul 2025 from the official UI.
   - RACE 44.64 (comprehensiveness 44.96, insight/depth 41.97, instruction-following 47.14, readability 45.59).
   - Comparison: OpenAI DR 46.45, Claude Research 45.00, Doubao 44.34.
   - No FACT citation scores: links could not be parsed from the UI.
   - The paper calls it "statistically indistinguishable" from the mid-tier agents. It is not in arXiv v1; it was added in July 2025.
2. **ICBCBench (financial deep research), arXiv 2606.17458 preprint, 2026** https://arxiv.org/abs/2606.17458
   - Authors from ICBC, Shanghai Jiao Tong University, Fudan University, Shanghai AI Lab, Alibaba Group and others.
   - "Kimi-deep-research": English overall 47.59 (objective 35.00, subjective 60.19), 3rd of the closed systems after Gemini DR 57.38 and o3-deep-research 54.67. Chinese overall 44.72.
   - **Disclosures:** Alibaba co-authors (Alibaba's Qwen deep research is a competing system evaluated in the paper). The paper does not state the access method or test dates for Kimi; references were accessed Mar–Apr 2026.

## 3. Listed, not counted
- WebResearcher (Alibaba Tongyi, https://arxiv.org/abs/2509.13309): Kimi-Researcher rows (HLE 26.9; xbench 69.0) are marked † as taken from vendor reports, so they are not independent tests.
- Vendor claims, excluded:
  - HLE 26.9% pass@1 and 40.17% pass@4;
  - xbench-DeepSearch 69%;
  - FRAMES, Seal-0 and SimpleQA (graded with o3-mini).
- xbench public leaderboard: no Kimi-Researcher row was found.
- Not tested in the other benchmarks I checked: LiveResearchBench, DeepResearchEval, Mind2Web 2, DeepResearch Bench II, ReportBench, DEER, Dr. Bench, and the Rao et al. citation-URL study. These were checked for "Kimi Research" rows; none was found except Kimi-K2 as a plain model.

## 4. Privacy, regulatory and disputes
- **Apr 2026 data leak (Kimi app; not specific to Deep Research):**
  - On 20 Apr 2026 Kimi returned another user's real résumé (name, phone, email, work history) during an unrelated translation request.
  - Staff first called it "AI hallucination", then a cross-user mix-up ("发串"). No official public statement.
  - Legal commentary says it may violate China's Personal Information Protection Law (PIPL).
  - Sources: Phoenix Weekly (http://www.ifengweekly.com/detil.php?id=26914), Sina / Cover News (https://finance.sina.cn/stock/jdts/2026-04-26/detail-inhvvuxz3018355.d.html?vt=4), Seoul Economic Daily (https://en.sedaily.com/international/2026/04/30/chinas-kimi-ai-leaks-strangers-resume-in-translation-request), OECD AI incident monitor (https://oecd.ai/en/incidents/2026-04-21-8c79).
- Regulators: no ban or action against Kimi found. The 2025 actions by Italy, South Korea and Germany concerned DeepSeek, not Kimi.
- China-based service: data handling and storage have not been independently verified. A review of Moonshot's privacy policy is not done yet (follow-up if published).

## 5. What the rules say
Fewer than 3 counted sources means **Insufficient evidence**: no overall score and no grade.

## 6. Recommendation
Publish as **Insufficient evidence** (2 counted sources). Show factor notes without scores:
- the DRB and ICBCBench results;
- the Apr 2026 résumé leak under disputes;
- the continuity note.

Category: Research.

## 7. Decision points
1. Continuity: read as continuous (same Kimi-Researcher model per the help page) — recommended.
2. ICBCBench: count it despite the unstated access method and the Alibaba co-authors (recommended, with disclosure)? Either way the result is Insufficient.
3. Résumé leak: include it under disputes for the Deep Research entry, even though it is app-wide (recommended, labelled as Kimi-wide)?
4. Should the WebResearcher paper's reuse of vendor numbers be listed as not counted (drafted: yes)?

## 8. Plain-English terms
- **Insufficient evidence:** too few independent tests to give a score.
- **RACE:** an LLM-judged report-quality score relative to a reference report.
- **Vendor claim:** a result published by Moonshot itself.
