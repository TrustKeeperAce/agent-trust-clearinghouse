# Decision 0025: Agent S / S2 / S3 (Simular) — batch 3, candidate 2

**Status: APPROVED by Remington, 2026-10-17. Overall 49, grade B.** All 8 recommendations were approved:
- D1: continuous across S2/S2.5/S3; S1 is historical context only.
- D2: open-source library only; Sai, the app, Cloud and API are excluded; results are shown as model ranges.
- D3: OSWorld-Verified is not counted and is listed as other, with reasons.
- D4: rival-author studies are counted, with disclosures.
- D5: grade B.
- D6: the code finding is cited via the independent greenlitbooks write-up plus a link to commit 15776a8. It is described neutrally; credentials in prompts are not quoted.
- D7: new category "Computer-use agent".
- D8: all three CVEs are listed (no vendor response; NVD status Deferred), plus the issue #146 reproduction gap (fixed Oct 2025).

**Methodology clarification, also approved:** an entry with 7+ counted sources but fewer than 3 peer-reviewed (or lacking a recent current-version test) receives grade B. "Computer-use agent" is added to the category list.
Researched 2026-10-17. YAML draft: `agent-s.yaml`.

## What happened (with sources)

**The product**
- Agent S is Simular's open-source computer-use framework: <https://github.com/simular-ai/Agent-S>.
  - Apache-2.0 licence, PyPI package `gui-agents`, about 12.6k stars.
  - Last push 8 Oct 2026 (commit 15776a8); latest release 0.3.2 (16 Dec 2025).
- Generations:
  - S1: Oct 2024 (ICLR 2025).
  - S2: Mar 2025, 0.2.0 (COLM 2025).
  - S2.5: Aug 2025, 0.2.5.
  - S3: Oct 2025, 0.3.0 (TMLR 2026). S3 drops S2's hierarchical planning, adds a coding agent, and adds Behavior Best-of-N (bBoN), which runs several attempts and picks the best.
- All four generations ship side by side in the same package (`gui_agents/s1`, `s2`, `s2_5`, `s3`).
- Simular's commercial products are separate: Simular 1.0 desktop app (Dec 2025), Sai (hosted agent, Aug 2026), Simular Cloud, and the Simular API (Oct 2026).

**Counted independent performance sources (7, all read in full)**

| # | Source | Version tested | Key figures | Peer review | Disclosure |
|---|---|---|---|---|---|
| 1 | OS-Symphony, <https://aclanthology.org/2026.acl-long.1021/> (arXiv 2601.07779) | S3 | Reproduced OSWorld (361 tasks, 50 steps): GPT-5-Mini **47.58%**, Qwen3-VL-32B **40.11%** | **ACL 2026** | Competing framework (OS-Symphony 58.05/46.86 on the same models) |
| 2 | OSWorld-Human, <https://arxiv.org/abs/2506.16042> | S2 | Ran S2 on 39 tasks: planning and reflection are 76–96% of latency. Efficiency-weighted score: S2 + Gemini 2.5 **15.6%/9.6%** (original 41.4%), S2 + Claude 3.7 **6.6%/4.4%** (original 34.5%) | **MLSys 2026** | Weighted scores use published trajectories |
| 3 | MacAgentBench, <https://arxiv.org/abs/2606.22557> | S3 | 676 macOS tasks, 8 models: Pass@1 **9.6–66.9%** (Opus 4.6 66.9, GPT-5.4 58.9); all-4-attempts **1.8–50.3%** | preprint (Jun 2026) | Shares several authors with OS-Symphony (Shanghai AI Lab) |
| 4 | Agent Alpha, <https://arxiv.org/abs/2602.02995> | S3 | Own run, GPT-5-mini, Best-of-3, 30 steps: **54.29%**, 313 s per task | preprint (Feb 2026) | Competing method (Agent Alpha 64.27%); its 72.58% S3 figure is copied from the leaderboard |
| 5 | OS-Marathon, <https://arxiv.org/abs/2601.20650> | S2.5 | GPT-5: **33.50% field / 23.44% subtask** (humans 88.38/80.52) | preprint v3 (Aug 2026) | Microsoft co-authors; Simular is a Windows 365 for Agents pilot partner |
| 6 | SCUBA, <https://arxiv.org/abs/2509.26506> | S2.5 | GPT-5, 300 Salesforce CRM tasks: **39.00%** zero-shot, **40.38%** with demonstrations; about 25 min and $1.17 per task | preprint (Sep 2025) | Salesforce sells its own agent products |
| 7 | WorldGUI, <https://arxiv.org/abs/2502.08047> | S2 | **34.2%** overall (humans 85.3%) | preprint v5, ICML 2026 submission template (not accepted) | Competing method (WorldGUI-Agent 45.8%) |

**Listed but not counted**
- **OSWorld-Verified leaderboard** (<https://os-world.github.io/>, <https://xlang.ai/blog/osworld-verified>):
  - Agent S3 rows: 72.58% (Opus 4.5 + GPT-5, Best-of-10), 69.90%, 67.46%, 65.58%. Agent S2.5 with o3: 56.0%.
  - Maintainers rerun submitted code, *or* accept monitoring data and trajectories from a "trusted institution". Which route applied to Simular is not stated.
  - Simular helped fix OSWorld-Verified tasks, and a Simular author is on the OSWorld 2.0 paper.
  - Recommendation: list as *other (maintainer-verified)*, not counted. See decision D3.
- **Vendor and author-run results:**
  - S3 paper (<https://arxiv.org/abs/2510.02250>): OSWorld 62.6 / 69.9 / 72.6%, WindowsAgentArena 56.6%, AndroidWorld 71.6%.
  - S2 paper (<https://arxiv.org/abs/2504.00906>).
  - S1 paper (<https://arxiv.org/abs/2410.08164>, 20.6%): historical context only.
  - Sai's 73% on OSWorld 2.0 (<https://www.simular.ai/articles/sai-tops-osworld-2-0>): vendor claim, and Sai is outside scope.
- **Reused vendor figures:**
  - WorldGUI's WindowsAgentArena table.
  - OS-Symphony's S3 + GPT-5 62.63% row.
  - Agent Alpha's leaderboard table.
- **Checked, with no Agent S tested:**
  - Princeton HAL (no OSWorld board and no Agent S).
  - OSUniverse, OS-Harm, VPI-Bench, OSGuard.
  - OSWorld 2.0 (models only; Simular co-author).
  - CaMeL-CUA, SCOUT, DeskCraft, Measuring Harmfulness of CUAs, MLA-Trust, ScienceBoard, DashboardQA, DevicesWorld (these only cite Agent S or discuss it).
  - FlashAdventure: the text file was binary-garbled. I did not confirm whether Agent S is tested; not counted.

**Disputes and security (other sources)**
- **Three DoS CVEs** against 0.3.1/0.3.2, published 3 Sep 2026 by the VulDB CNA:
  - [CVE-2026-84885](https://nvd.nist.gov/vuln/detail/CVE-2026-84885): code_agent.py, CVSS 3.1 4.3.
  - [CVE-2026-84886](https://www.cve.org/CVERecord?id=CVE-2026-84886): s1 OCR server, CVSS 3.1 5.3.
  - [CVE-2026-84887](https://www.cve.org/CVERecord?id=CVE-2026-84887): grounding.py, CVSS 3.1 4.3.
  - VulDB says the vendor "did not respond in any way". NVD status is Deferred, and no fix has been released (0.3.2 is still the latest).
- **Reproduction gap**, [issue #146](https://github.com/simular-ai/Agent-S/issues/146), Oct 2025:
  - A user's S3 runs came in lower than the paper (for example about 208/361 with Azure GPT-5).
  - On 30 Oct 2025 Simular admitted a prompt commit (aaed16e) had been missing from the open-source code and fixed it. The user confirmed the fix worked.
- **Code observation**, my own reading of commit 15776a8, matching an independent [greenlitbooks field note](https://greenlitbooks.com/field-notes/is-agent-s-safe):
  - In all `cli_app.py` files (s1 to s3), model-generated code runs via `exec(code[0])` under the comment "# Ask for permission before executing". `show_permission_dialog` is defined but never called.
    - Optional local code execution is off by default, with a warning.
- No lawsuits, regulator actions or data incidents were found for Agent S or Simular. No independent prompt-injection measurement of Agent S was found.

## What the rules say
- **Weights v0:** completion 30, disputes 20, adherence 25, evidence 25, rounded half up. You need at least 3 counted independent sources on the covered version and scope.
- **Grades:**
  - A: at least 7 sources, at least 3 peer-reviewed, and at least 1 testing the current version within 12 months.
  - B: 5–6 sources. B-: 3–4. Insufficient: fewer than 3.
- **Other rules:** competing-author sources count with disclosure; vendor and author-run results are excluded; abstract-only sources are not counted.
- **Continuity precedents:**
  - 0015/0016/0019: continuous through model and version changes. 0016 (Browser Use) is the open-source library precedent: library-only scope, results given as model ranges.
  - 0008/0020: discontinuous because the product was rewritten into a different product.
- **Proposed continuity ruling: continuous across S2 → S2.5 → S3**, like 0016. Reasons:
  - Same repository, package, team and purpose.
  - Each generation is an incremental redesign; the S3 paper says it "builds directly on S2".
  - Older generations stay in the same package.
  - Unlike 0008, it was not replaced by a different product.
  - S1 is historical context only (no independent full-text tests found).
  - The page will label every figure with its generation and note that S3 (0.3.2) is current.

## Proposed score (continuous scope, recommended)

| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion | 30 | 45 | S3 reproduced OSWorld 40–54%; macOS 10–67% Pass@1; S2.5 39% CRM, 23–34% long tasks; S2 34% WorldGUI. Clearly below vendor 62.6–72.6% and human baselines. Comparable to or a bit above Browser Use (40) |
| Disputes | 20 | 45 | 3 low/medium DoS CVEs, unpatched and unanswered; reproduction gap admitted and fixed; no legal issues |
| Adherence | 25 | 35 | No confirmation step before executing model-generated actions (dialog never called); no independent injection test (absence of evidence, not evidence of safety) |
| Evidence | 25 | 70 | 7 sources, 2 peer-reviewed, 5 from 2026; heavy competing-method authorship; spread over 3 generations and many models |

**0.30×45 + 0.20×45 + 0.25×35 + 0.25×70 = 48.75 → 49.**

**Grade: B.** There are 7 sources but only 2 are peer-reviewed, so A is not met; I propose B per the 0010 fallback. Index position: after Browser Use (51), before the Insufficient group.

**Alternative (S3-only scope):** counted would be OS-Symphony, MacAgentBench and Agent Alpha (3 sources; 1 peer-reviewed) → B-. Completion about 50, evidence about 55. Roughly 0.3×50 + 0.2×45 + 0.25×35 + 0.25×55 = 46.25 → 46, B-.

## Decisions needing your approval
1. **D1 Continuity:** continuous across S2/S2.5/S3 (like 0016), with S1 as historical context. *Recommended.* The alternative is S3-only (46 / B-).
2. **D2 Scope:** the open-source library only, with Simular app, Sai, Cloud and API excluded and stated on the page. Results shown as model ranges, as in the Browser Use entry. *Recommended.*
3. **D3 OSWorld-Verified:** not counted, listed as maintainer-verified "other", because it may be based on Simular's own trajectories and Simular is close to the maintainers. *Recommended.* If you count it: 8 sources, still 2 peer-reviewed, grade B; completion might go to about 50 → overall about 50.
4. **D4 Count the competing-method sources** (OS-Symphony, Agent Alpha, WorldGUI) with disclosure. Count MacAgentBench separately from OS-Symphony despite the shared authors (different benchmark and study), with an overlap disclosure. Count OSWorld-Human although its weighted scores reuse published trajectories (it also ran S2 itself).
5. **D5 Grade:** B for 7 sources with fewer than 3 peer-reviewed (A not met). Please confirm this matches 0010.
6. **D6 Code observation:** state the never-called permission dialog as observed in source code at commit 15776a8 (with a link), plus the independent field note. Alternatively, cite only the field note.
7. **D7 Category:** new category "computer-use agent", or reuse "browser/web agent"? I recommend the new category because it covers desktop apps, not just the browser.
8. **D8 CVEs:** list all three under disputes with "vendor did not respond per VulDB; NVD Deferred".

## Risks and uncertainties
- Strong model dependence: one number misleads, so the page will show ranges.
- Most counted sources are preprints. Two peer-reviewed sources both have weaknesses: OS-Symphony is a competitor, and OSWorld-Human is about efficiency rather than success.
- No independent security testing of Agent S; the adherence score rests on a code reading.
- WorldGUI is under submission and may change.

## Plain-English terms
- **OSWorld:** a standard test of 369 real desktop tasks in a virtual computer. "Verified" is the maintainers' cleaned-up version and leaderboard.
- **Best-of-N / bBoN:** run the agent several times and let a judge pick the best attempt. This raises scores but costs more.
- **Pass@1 / Pass^4:** success on one try / success on all four tries.
- **Grounding model:** a small model that turns "click the Save button" into screen coordinates.
- **CVE / CVSS:** public vulnerability ID / severity score from 0 to 10.
- **Competing-method source:** a paper whose authors propose a rival system. It counts, with disclosure.
