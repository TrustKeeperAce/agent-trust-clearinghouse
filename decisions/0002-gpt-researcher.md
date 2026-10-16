# Decision 0002: GPT Researcher

**Status: APPROVED by Remington, 2026-10-16.** Publish with score 53 and evidence grade B-, using the final public wording below.

## Final public wording
**Summary:** "GPT Researcher is an open-source research agent that writes cited reports. In independent evaluations (DeepResearchGym, ICTIR 2026; Deep Research Comparator, WWW 2026 Companion; TTD-DR preprint), results ranged from comparatively strong on citation quality to lower than a commercial deep-research system in head-to-head comparisons. Results vary with the AI model and search provider used. Informational only; not an endorsement or certification."

**Security:** "Public vulnerability databases (NVD and GitHub Advisory Database) list 7 security advisories (2 Critical, 3 High, 2 Medium). The maintainer has fixed one; several others concern the self-hosted server, which the project's security policy says ships without built-in authentication and is intended for trusted environments only. Status may change; see linked sources."

(This security wording supersedes the "versions up to 3.4.3" CVE line in 0002b. Four issues the maintainer classifies as by design remain in v3.7.0.)

---

## Part A: Initial packet (0002)


## Draft entry summary
GPT Researcher is an open-source (Apache-2.0) deep-research agent in the Research category. Proposed overall score: **55/100**. Evidence grade: C. It just meets the 3-independent-source minimum. Results depend on the LLM and search API it is configured with.

## What happened (facts + sources, accessed 2026-10-16)
- In DeepResearchGym, an independent academic evaluation run on default config, it scored key-point recall 60.61/64.67, citation precision 89.11/85.36 and recall 94.29/90.82, across two search back-ends. [1]
- In Deep Research Comparator, run in deep research mode with GPT-4.1/o4-mini, it ranked 1st of 3 agents in human pairwise judgments. However, its text-span upvote rate was 74.66%, compared with 90.72% for Perplexity. [2]
- NVD lists 6 CVEs: two Medium XSS, three High (code injection, missing authentication, SSRF; versions up to 3.4.3) and one Critical (unauthenticated RCE, v0.14.7 and earlier). Fix status in the current version was not verified. [3]
- The maintainers' own benchmark on 10 DeepResearch Bench tasks reports 35.2 verified citations per report, vs 18.6 for the baseline. [4]
- The latest release is v3.7.0 (2026-09-26). The repo shows 37 open issues+PRs, 1 issue labeled "bug" and 0 repo security advisories. [5]
- The docs describe iteration, token, word and breadth/depth limits. No dollar budget cap was found. [6]

## Sources checked
| # | Source | Type | Shows | URL |
|---|---|---|---|---|
|1|DeepResearchGym (arXiv 2505.19253)|Independent|Benchmark scores|https://arxiv.org/abs/2505.19253|
|2|Deep Research Comparator (arXiv 2507.05495)|Independent|Human-preference ranking|https://arxiv.org/html/2507.05495v2|
|3|NVD CVE search|Independent|6 CVEs|https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=gpt-researcher|
|4|BENCHMARK.md|Vendor|Self-reported DRB results|https://github.com/assafelovic/gpt-researcher/blob/main/deep_agents/BENCHMARK.md|
|5|GitHub API|Vendor platform metadata|Releases/issues/advisories|https://api.github.com/repos/assafelovic/gpt-researcher|
|6|Config docs|Vendor|Stated limits|https://docs.gptr.dev/docs/gpt-researcher/gptr/config|
|7|LinkedIn post|Vendor|Restates [1] as "#1"|https://www.linkedin.com/posts/gptrdev_carnegie-mellon-universitys-deepresearchgym-activity-7379043941104513026-kXha|
|-|DeepResearch Bench paper (2506.11763)|Independent|Does **not** evaluate GPT Researcher|https://arxiv.org/abs/2506.11763|

## Evidence quality assessment
The two independent studies are arXiv preprints whose peer-review status was not confirmed. They used different configurations, and both date from 2025. NVD is an authoritative record of vulnerabilities, but it says nothing about research performance. All of the DeepResearch Bench figures come from the maintainers. Overall the evidence is moderate and thin on reliability and failure rates.

## What the rules say
v0 weights are Completion 30%, Disputes 20%, Adherence 25% and Evidence 25%. An entry with fewer than 3 independent sources gets no overall score. This one has 3, so a score is allowed. That is borderline if NVD is not counted as a performance source.

## Proposed score breakdown
| Factor | Score | Reasoning (judgment calls) |
|---|---|---|
|Completion (30%)|60|There is no independent completion-rate figure. It completed cited reports in 2 independent studies, with key-point recall around 61-65%. Judgment.|
|Disputes (20%)|40|No user disputes were found. The 6 CVEs (1 Critical, 3 High) are the main negative signal, and fix status is unknown. Judgment.|
|Adherence (25%)|55|Configurable limits are vendor-documented only. The missing-auth and SSRF CVEs point to boundary weaknesses in older versions. Judgment.|
|Evidence (25%)|60|Two independent preprints plus NVD, with headline numbers self-reported. Judgment.|
|**Overall**|**55**|0.3×60 + 0.2×40 + 0.25×55 + 0.25×60 = 54.75|

## Risks/uncertainties
- The CVE patch status in v3.7.0 is unverified, so stating it either way carries defamation risk. CVEs should be worded as "reported in NVD for versions ≤ X".
- Results are LLM- and search-dependent and the evaluations are dated.
- The vendor's "#1" marketing should not be repeated.
- No independent data on cost or failure rates exists.

## Recommendation
**More info before publishing.** The factor notes can stand. Before anyone approves the overall score:
1. Check the repo's commits and changelog to confirm whether each CVE is fixed.
2. Confirm the peer-review status of the two preprints.
3. Look for one more independent evaluation that covers performance rather than security.

If those checks come back clean, publish with a neutral caveat.

## Plain-English terms
- **CVE:** a publicly catalogued security flaw.
- **SSRF:** tricking a server into fetching URLs for an attacker.
- **RCE:** running code on someone else's machine.
- **KPR:** the share of the key points a good answer should cover.
- **Citation precision:** the share of citations that actually support the claim they're attached to.
- **arXiv preprint:** a paper posted publicly, not necessarily peer-reviewed.

---

## Part B: Follow-up checks (0002b)

Accessed 2026-10-16. Code checked: tag v3.7.0 (commit 0957c30).

## 1. CVE status in v3.7.0
| CVE | Sev. | Affected | v3.7.0 status |
|---|---|---|---|
|2026-5625 XSS|Medium|≤3.4.3|**Fixed (verified)**: #1692 closed citing the fix; PR #1820 merged; `frontend/scripts.js` sanitizes WebSocket output with DOMPurify|
|2026-5630 XSS|Medium|≤3.4.3|**Unverified**: #1693 closed as out of scope; render path not traced|
|2026-5631 code injection|High|≤3.4.3|**Not fixed (by design)**: #1694 closed out of scope; `extract_command_data` still accepts `mcp_configs`|
|2026-5632 missing auth|High|≤3.4.3|**Not fixed (by design)**: #1695; SECURITY.md says no built-in auth|
|2026-5633 SSRF|High|≤3.4.3|**Not fixed (by design)**: #1696; `source_urls` still accepted|
|2026-37006 RCE|Critical|≤0.14.7|**Unverified**; same MCP vector class remains, by design|

NVD lists no fix versions for any of these. The repo has published 0 advisories of its own. I also found GHSA-8j86-h8gg-797p (CVE-2025-65720, Critical, ≥0.14.5 ≤0.14.7, no patched version listed).

The maintainer's position (SECURITY.md) is that the backend is meant to run in a trusted environment. Unauthenticated access, SSRF and MCP-command RCE on exposed servers are treated as operator responsibilities.

Sources: NVD API (`?cveId=…`); github.com/assafelovic/gpt-researcher/issues/1692–1696; /pull/1820; SECURITY.md; github.com/advisories/GHSA-8j86-h8gg-797p.

## 2. Peer review
- **DeepResearchGym:** published at ICTIR '26 (ACM SIGIR), DOI 10.1145/3805713.3820409, per the CMU camera-ready PDF (cs.cmu.edu/~callan/Papers/ictir26-Jo%C3%A3o_Coelho.pdf). The ACM DL page returned 403 to my fetch. Caveat: I took the GPT-Researcher figures from arXiv v3, because the ICTIR table text would not extract.
- **Deep Research Comparator:** Semantic Scholar and DBLP list it in the *Companion Proceedings of the ACM Web Conference 2026* (DOI 10.1145/3774905.3793116). That is a companion/demo-type track, and I did not verify how deep its review is. It shares an author (Jiahe Jin) with DeepResearchGym.
- arXiv carries no journal-ref for either paper. I found no OpenReview record.

## 3. Additional independent evaluation
I checked 8 other benchmark papers: Mind2Web 2, LiveResearchBench, ResearchQA, ReportBench, LifeSearch, WebSailor, BESPOKE and EDR. None evaluates GPT Researcher; EDR only cites it.

**TTD-DR** (arXiv 2507.16075, Google Cloud AI Research; preprint) does evaluate it, as a baseline against the authors' own system. Its results for GPT-Researcher:
- Win rate vs OpenAI Deep Research: 18.3% on LongForm Research, 9.4% on DeepConsult.
- Correctness: HLE-Search 2.0%, HLE-Full 4.1%, GAIA 37.7%.

## Independent source count
- **Performance: 3** (DeepResearchGym, Deep Research Comparator, TTD-DR).
- **Security: 2** (NVD, GitHub Advisory DB).

The threshold is now met on performance sources alone.

## Revised factor scores (all judgment calls)
| Factor | Old | New | Reason |
|---|---|---|---|
|Completion 30%|60|55|TTD-DR shows low win rates vs a commercial DR system|
|Disputes 20%|40|40|7 CVE IDs; 1 verified fixed; 4 declined as by-design|
|Adherence 25%|55|50|No built-in auth; client-supplied MCP commands and URLs accepted in v3.7.0|
|Evidence 25%|60|65|1 peer-reviewed main venue + companion track + preprint|

Overall = 0.3×55 + 0.2×40 + 0.25×50 + 0.25×65 = 16.5 + 8 + 12.5 + 16.25 = **53.25 → 53**. Evidence grade: **B- (moderate)**.

## Remaining risks
- Results depend on the LLM and search API, and the studies are 2025-era with mixed configurations.
- Fix status for CVE-2026-5630 and CVE-2026-37006 is unverified.
- TTD-DR's authors have a competing system.
- "By design" is the maintainer's characterization; NVD has not changed the records.

## Recommendation: publish, with neutral wording
**Entry summary:** "GPT Researcher is an open-source research agent that generates cited reports. In independent academic evaluations (DeepResearchGym, ICTIR 2026; Deep Research Comparator, WWW 2026 Companion; TTD-DR preprint), its results ranged from comparatively strong on report clarity and citation metrics to lower than a commercial deep-research system on head-to-head win rates. Results vary with the LLM and search provider used. Informational only; not an endorsement or certification."

**CVE line:** "NVD and GitHub's advisory database list 7 CVE IDs affecting versions up to 3.4.3 or 0.14.7 (2 rated Critical, 3 High). The maintainer has fixed one XSS issue and states in SECURITY.md that the backend ships without authentication by design and is intended for trusted environments. Sources linked; fix status of each item may change."

## Plain-English terms
- **By design:** the maintainer says the behavior is intended. The user must secure the server themselves.
- **Companion proceedings:** a shorter or demo track, usually reviewed more lightly than the main conference.
- **Win rate:** how often judges preferred its report over OpenAI's.
