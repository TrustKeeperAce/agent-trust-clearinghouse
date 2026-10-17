# Decision 0023: Batch 3 shortlist

**Status: APPROVED by Remington, 2026-10-17.** Order: Kimi Researcher, Agent S, STORM/Co-STORM, Skyvern, Perplexity Comet, Data Interpreter, Loki/OpenFactCheck, Fellou. Reserves: Luminance, Exa Websets.

## What happened
- Batch 2 (Decision 0015) is complete. Its two reserves, STORM and Kimi Researcher, were re-checked, and both are still available.
- Underrepresented categories in the directory:
  - negotiation: 1 entry (Pactum);
  - data enrichment: 1 (Clay);
  - verification: 2;
  - simple analysis: 2;
  - browser/web: 2.
- Excluded: every product already in the directory, and retired products (0018).

## Candidates (proposed order)
1. **Kimi Researcher (Moonshot AI)**. Research.
   - Deep-research agent in Kimi, launched June 2025 and still offered as "Deep Research" (https://www.kimi.com/en/help/agent/agent-overview).
   - Evidence: DeepResearch Bench (ICLR 2026) evaluated it through the official app, RACE score 44.64 (https://proceedings.iclr.cc/paper_files/paper/2026/file/465f22be10e07b301c6ed58f0472f704-Paper-Conference.pdf). Vendor post: https://moonshotai.github.io/Kimi-Researcher/
   - Flags:
     - vendor HLE scores are excluded;
     - underlying models changed (K2, K2.5, K2.6, K3), so continuity needs a ruling;
     - possibly few independent tests beyond DRB;
     - China-based service, so a privacy and regulatory check is needed.
2. **Agent S / S2 / S3 (Simular)**. Browser/web and computer-use agent.
   - Open-source framework that operates a computer through its interface.
   - Evidence: OSWorld leaderboard (https://os-world.github.io/); papers at https://arxiv.org/abs/2410.08164 (ICLR 2025) and https://arxiv.org/abs/2504.00906; possibly Princeton HAL (https://hal.cs.princeton.edu/).
   - Flags: many results are run by the authors themselves; results depend on the model, as with Browser Use; versions change quickly.
3. **STORM / Co-STORM (Stanford OVAL)**. Research.
   - Open-source research prototype that writes Wikipedia-style cited reports; hosted demo at https://storm.genie.stanford.edu/
   - Evidence: NAACL 2024 paper (https://arxiv.org/abs/2402.14207, author-run); EMNLP 2024 Co-STORM paper (https://arxiv.org/abs/2408.15232); used as a baseline in later deep-research benchmarks.
   - Flags:
     - maintenance is slowing (last commit 30 Sep 2025, last release v1.1.0 in Jan 2025; https://github.com/stanford-oval/storm), but it is not retired;
     - its own papers are vendor-like evidence;
     - results depend on the model.
4. **Skyvern**. Browser/web agent.
   - Open-source and cloud browser automation.
   - Evidence: Web Bench (https://webbench.ai/; https://www.skyvern.com/blog/web-bench-a-new-way-to-compare-ai-browser-agents/); WebVoyager results.
   - Flags: Web Bench was co-built by Halluminate and Skyvern, which is a conflict; independent peer-reviewed tests are uncertain.
5. **Perplexity Comet (browser agent)**. Browser/web agent.
   - Agentic browser.
   - Evidence: Brave's prompt-injection disclosure (https://brave.com/blog/comet-prompt-injection/); Trail of Bits audit (https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/; paid by Perplexity, so not independent); BrowseSafe (Perplexity's own work, https://arxiv.org/html/2511.20597v2).
   - Flags: overlap with the existing Perplexity entry (scope note needed); performance evidence is likely thin, and security evidence is stronger.
6. **Data Interpreter (MetaGPT / DeepWisdom)**. Simple analysis / data science.
   - Open-source data-science agent.
   - Evidence: https://arxiv.org/abs/2402.18679; DSBench, DA-Code and similar benchmarks may include it (to verify).
   - Flags: mostly author-run evaluations; framework results depend on the model.
7. **Loki / OpenFactCheck (Libr-AI, MBZUAI)**. Verification.
   - Open-source fact-checking tools.
   - Evidence: https://arxiv.org/abs/2410.01794 (Loki); https://arxiv.org/abs/2405.05583 (OpenFactCheck benchmark framework).
   - Flags: evaluations are mostly by the authors; independent use is uncertain; likely Insufficient.
8. **Fellou**. Browser/web agent.
   - Agentic browser for deep search and automation (https://fellou.ai/).
   - Evidence: evaluated in CAP (COLM 2026, https://arxiv.org/abs/2608.08392).
   - Flags: one CAP author interned at FellouAI, which is a conflict; other independent tests are unknown; likely Insufficient.

## Reserves (underrepresented categories, thin evidence)
- **Luminance (autonomous contract negotiation)**. Negotiation. https://www.luminance.com/ Mostly vendor and press evidence; likely Insufficient.
- **Exa Websets**. Data enrichment. https://exa.ai/websets Vendor benchmarks only; likely Insufficient.

## Risks
- Several candidates are open-source frameworks whose results depend on the model, so they need a Browser Use-style scope.
- Author-run and competitor-run evaluations are common. Disclosures will be needed, and some sources won't count.
- Negotiation and data enrichment still have little independent evidence, so they will probably produce Insufficient entries.
- Continuity rulings will be needed (Kimi models; Agent S versions).

## Recommendation
Approve candidates 1–8 in the order above, with Luminance and Exa Websets as reserves. Research one candidate at a time under the same rules as batch 2.

## Plain-English terms
- **Shortlist:** candidates to research, not entries.
- **Reserve:** researched only if a shortlisted candidate drops out.
- **Author-run evaluation:** a test published by the tool's own makers. It is treated as a vendor claim.
- **Model-dependent:** results change with the language model plugged in.
