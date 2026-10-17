# Decision 0020: Manus (candidate 5)

**Status: APPROVED by Remington, 2026-10-17.** Confirmations:
1. Manus entry: **Insufficient evidence**, 0 counted sources. Six tests of 2025 versions are listed as historical context only, including the CAP Fellou disclosure. Note: "Manus 2.0 (28 Sep 2026, new architecture) has not been independently tested". Security demos, the MIT Technology Review hands-on review and the ownership/regulatory timeline (including the data deletion) are other sources. Vendor GAIA figures are excluded. Category: Research (general-purpose agent).
2. Browser Use entry: CAP competitor disclosure added (one author interned at FellouAI, a system evaluated in CAP). Score unchanged; recorded in the changelog; last reviewed unchanged.
3. Option B (51/B, scored on 2025 versions only) is not adopted.

## What happened
- Status: still offered, not retired. Meta agreed to acquire it on 29 Dec 2025. China ordered the deal unwound in Apr 2026, and the two companies split operations in May 2026. Some user data created between 29 Dec 2025 and 23 Aug 2026 was deleted on 23–24 Aug 2026 "to comply with regulatory requirements" (https://help.manus.im/en/articles/16147831-service-change-overview-what-s-happening-and-am-i-affected). Manus resumed independent operations on 1 Sep 2026 (https://manus.im/blog/manus-resumes-independent-operations). Butterfly Effect raised more than $500M (TechCrunch, 8 Oct 2026).
- Versions: 1.5; then 1.6 (15 Dec 2025, https://manus.im/blog/manus-max-release); then **Manus 2.0** (28 Sep 2026, https://manus.im/blog/introducing-manus-2-0). The vendor says 2.0 "is not a version update. It's a new architecture" and introduces a new agent harness called "Cascade", plus Studio, Cloud Computer, Automations and Computer Use. 0018 does not apply.
- Every independent test I found used versions from Mar–Dec 2025 (pre-2.0).

## Independent performance sources (read in full)
1. LiveResearchBench (ICLR 2026; Salesforce, UW-Madison, Stanford) https://arxiv.org/abs/2510.14240. Scores: presentation 75.0, fact & logic 63.1, coverage 73.3, citation 45.6. LLM-judge ensemble; 2025 runs.
2. DeepResearchEval (preprint Jan 2026; Shanda/Infinity) https://arxiv.org/abs/2601.09688. 100 tasks; quality 5.95/10 (8th of 9); factual ratio 82.30% (1st of 9). Judged by Gemini-2.5-Pro, with a GPT-5 cross-check; 2025 runs.
3. CAP (COLM 2026) https://arxiv.org/abs/2608.08392. Nov–Dec 2025; partial completion 23.0%, full success 8.0%, best of the agents tested (humans 10%). **Competitor disclosure:** one author worked during an internship at FellouAI, and Fellou is one of the systems evaluated.
4. Loke et al., Eye 2026; 40(1):147–149 (online 28 Nov 2025) https://doi.org/10.1038/s41433-025-04138-w. Full text from the UCL accepted manuscript. Tested Apr 2025 on an end-to-end systematic review and meta-analysis. Manus was the only agent to attempt the full workflow; its search terms and cited sources were rated "Good". It fabricated all 10 selected studies and 5 references.
5. Madfa et al., Frontiers in Oral Health 2025 https://doi.org/10.3389/froh.2025.1686090 (PMC12823890). "Latest version as of March 2025"; 117 dental case-vignette multiple-choice questions. Round 2: Manus 92.3%, Claude 3 Opus 92.3%, GPT-4-turbo 76.9%; kappa 0.782. Differences not significant.
6. Annals of Medicine 2026 https://doi.org/10.1080/07853890.2026.2664903 (PMC13159575). "Clinical release, April 2025"; 120 dental radiographs. Manus 92.5% then 95.0%; radiologists 96.7%. Likely the same Ha'il research group as #5, but a separate study.

## Other sources (listed, not counted)
- MIT Technology Review hands-on (Mar 2025) https://www.technologyreview.com/2025/03/11/1113133/manus-ai-review/ : journalism, qualitative.
- Embrace The Red (Aug 2025) https://embracethered.com/blog/posts/2025/manus-ai-kill-chain-expose-port-vs-code-server-on-internet/ : prompt injection led to deploy_expose_port exposing VS Code server; disclosed 1 Jun 2025; fix status unclear.
- Salt Labs (1 Oct 2026) https://salt.security/blog/how-we-hijacked-an-ai-agent-with-a-single-email : a single email led to remote code execution and exposure of connected-account tokens; fixed via Meta bug bounty. Also covered by Dark Reading.
- Excluded: vendor GAIA scores (86.5/70.1/57.7) and the vendor's Cascade efficiency claims. I found no independent Manus results on GAIA, BrowseComp, Mind2Web 2, HAL, WideSearch, xbench, ResearchRubrics or FutureSearch DRB.
- Not read, not listed: the Ultrasound Journal lung-ultrasound study.

## Options
A. **0008 reading (recommended)**: Insufficient evidence for the current product. The vendor itself calls 2.0 a new architecture rather than a version update, which is stronger than the OpenAI DR model-swap case (0019). All tests of 1.x are listed with dates.
B. **Continuity reading (0015/0016/0019)**: score Manus scoped to 1.x tests (2025), with a banner that 2.0 is untested. Result: 6 counted sources, 5 peer-reviewed, grade **B** (7 needed for A; no test of 2.0 exists anyway).

## Score breakdown (option B)
- Completion 50: mid-range quality on research benchmarks; citation accuracy weak (45.6); 8% full success on CAP, though best of the agents tested; fabricated every study in the systematic-review test; high accuracy on dental multiple-choice and radiograph tasks. Judgment call.
- Disputes 40: two serious vulnerabilities (RCE and token exposure, fixed; port exposure); acquisition unwound by regulator; forced deletion of user data. Judgment call.
- Adherence 40: followed injected instructions in both security demos; fabrications. Judgment call.
- Evidence 70: 6 sources, 5 peer-reviewed, all pre-2.0; LLM judges; one competitor tie (CAP). Judgment call.
- Overall = 0.30*50 + 0.20*40 + 0.25*40 + 0.25*70 = 50.5, rounded half up to **51**.

## Decision points
1. Option A (Insufficient, per 0008) or option B (51/B, scoped to 1.x)?
2. MIT Technology Review: list it as other (as drafted), or count it? Counting it under B would make 7 sources, but the grade stays below A because no source tested the current version.
3. CAP Fellou tie: disclose it here. The Browser Use entry cites CAP without this disclosure; add it there too (small follow-up edit)?
4. Do the two dental studies count, given they are diagnostic Q&A tests rather than agentic tasks? Without them, the count is 4 and the grade would be B-.
5. Should the regulatory data deletion count as a dispute (drafted: yes)?
