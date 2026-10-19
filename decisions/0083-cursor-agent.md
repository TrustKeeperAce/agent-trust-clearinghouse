# Decision 0083: Cursor agent — 57 / A

**Status: APPROVED by Remington, 2026-10-19: D1–D8 as recommended (D1a with the CLI; D3a; D4a current practice; D5b; D6 57 / A; D7 as drafted; D8 recheck note), D9 entry page and D10 changelog row. D11 (deploy) is pending: nothing is deployed.**

Implementation notes (2026-10-19): Entry: agents/cursor-agent.yaml and public/agents/cursor-agent.html (57 / A; 19 counted, 10 peer-reviewed; other 17). Other is 17, not the 18 first drafted: under the 0079 rule the historical-context record (RedCodeAgent) is not an other source, so it is listed under "Not counted"; scores and grade are unaffected. The AIDev note (D4) appears in the summary, grade note, "How sources were counted" and the first uncertainty; the recheck note (D8) is shown at the head of the page and in the last uncertainty. Changelog row 2026-10-19-0083 (new entry). Comparison page: the generated caveat on compare/coding-agents.html (COMPARE in scripts/build_data.py) now lists Cursor agent among the managed products; no other wording changed. Batch 5, first candidate (approved for full research in t155u).
- **Category:** Coding agent. **Proposed name:** "Cursor agent". **Slug:** `cursor-agent`.
- **Research window:** 19 Oct 2026, about 05:06–05:25 ET. Most of the source texts were already on the box from the batch 4 coding-agent research; about 25 papers were downloaded or read again for this pass.
- **Visible note proposed:** "Citation check incomplete — recheck later."

## What happened
1. **Scope (D1).**
   - **In:** Cursor's agent features from January 2025:
     - agent mode in the editor (agentic Composer from Nov 2024; the default from Feb 2025);
     - background and cloud agents, which open pull requests on `cursor/` branches;
     - the Cursor CLI agent (`cursor-agent`).
   - **Out:**
     - Tab completion, inline edits (Cmd-K) and chat-only use (autocomplete is out of scope under 0036);
     - Bugbot code review;
     - the 2024 Composer before agent mode;
     - Cursor's Composer models when tested on their own;
     - studies of adopting Cursor as a whole product.
   - **Version window:** about v0.45 (early 2025) to v3.x (2026).
2. **Sources screened.**
   - About 45 sources were read in full or in the relevant parts (method, affiliations, versions, per-agent results). That covers:
     - 22 AIDev / MSR 2026 field studies;
     - 9 security or benchmark studies;
     - adoption studies;
     - NVD and Cursor's GitHub advisories;
     - dispute records.
   - Search: OpenAlex (5 queries), web search, plus the existing batch 4 corpora (`/workspace/batch-next/{cp,cx}`, `/workspace/claudecode`).
   - Semantic Scholar returned 429; the arXiv API timed out.
3. **Results.**
   - **19 counted** independent performance sources, **10 peer-reviewed**.
   - Versioned tests within 12 months: Cursor v3.3.30 (ISSTA 2026) and Cursor v2.3 (KDD 2026). AgentKernelArena (Apr 2026) is dated but gives only the CLI interface, no version.
   - **17 other** sources (other and anecdotal; corrected from 18 on 19 Oct 2026 to follow the 0079 rule, which does not count historical context), 1 historical context source, 2 competitor sources, 1 model-only, and vendor material.
4. **Proposed score:** 57, grade **A** under the recommended rulings (see D4/D5 for the sensitivity).

## Counted: independent performance sources (19; peer-reviewed 10)
| # | Source | Peer review | Version / date | Key Cursor figures |
|---|---|---|---|---|
| 1 | Comparing AI Coding Agents (Trieste/KCL/UCL) https://doi.org/10.1145/3793302.3793576 | MSR 2026 | cloud agent; May–Aug 2025 | 569 PRs; 74.5% accepted overall; 74.4% in the common window (2nd of 5, Codex 79.9%); fix 80.4%, test 77.8% (few samples) |
| 2 | Where Do AI Coding Agents Fail? (Drexel/Missouri S&T) https://arxiv.org/abs/2601.15195 | MSR 2026 | cloud agent; 2025 | 65.22% merged (1,005/1,541), 2nd of 5; build 0.57, performance 0.46 |
| 3 | Fix-related PRs unmerged (Saskatchewan) https://doi.org/10.1145/3793302.3793611 | MSR 2026 | cloud agent; 2025 | Fix PRs merged 68.4% (281/411) |
| 4 | CI/CD configurations (Trent) https://doi.org/10.1145/3793302.3793581 | MSR 2026 | cloud agent; 2025 | CI/CD-changing PRs +4.03 points (p = 0.029); build success 79.10–83.13% |
| 5 | Task-Level Evaluation (Idaho State) https://arxiv.org/abs/2602.02345 | MSR 2026 | cloud agent; 2025 | Average acceptance 0.67 (Codex 0.83, Copilot 0.45) |
| 6 | Reliability of AI Bots Footprints in CI/CD https://doi.org/10.1145/3793302.3793569 | MSR 2026 | cloud agent; 2025 | Workflow success 73.29% (high-level languages) and 65.07% (low-level); Copilot and Codex about 93–94% |
| 7 | How do Agents Refactor (Alberta) https://doi.org/10.1145/3793302.3793577 | MSR 2026 | cloud agent; 2025 | Fewest refactorings (31); the only agent with a significant rise in code smells (small sample) |
| 8 | Security in the Age of AI Teammates (Notre Dame) https://doi.org/10.1016/j.infsof.2026.108333 | IST 2026 | cloud agent; 2025 | Security PRs merged 76.47%, 2nd of 5 |
| 9 | Red-Teaming Coding Agents (HKUST/Fudan) https://doi.org/10.1145/3832267 | ISSTA 2026 | v1.7.39 and v3.3.30; revision mid-2026 | Prompt-leak similarity 0.949. Tool hijack to code execution: 0.8–1.0 on the older release; at most 0.3 on v3.3.30 with newer models |
| 10 | SWE-Bench Mobile (Toronto/Xiaohongshu and others) https://doi.org/10.1145/3770855.3818488 | KDD 2026 | v2.3, agent mode; about Jan 2026 | 12% task success with Opus 4.5 / Sonnet 4.5, tied highest of 22 configurations; 2% with GPT 5.1 |
| 11 | Rise of AI Teammates (Queen's; AIDev paper) https://arxiv.org/abs/2507.15003 | preprint | cloud agent; Jan–Jun 2025 | 51.4% accepted (Codex 65.3%, human 76.8%) |
| 12 | Why Agentic-PRs Get Rejected (Kyushu/Waterloo) https://arxiv.org/abs/2602.04226 | preprint | cloud agent; 2025 | 74.6% of 1,347 PRs accepted |
| 13 | How Do AI Coding Agents Contribute? (Polytechnique Montréal) https://arxiv.org/abs/2607.21832 | preprint | cloud agent; Jan–Nov 2025 | Estimated merge probability 63.9%, 3rd of 5 |
| 14 | Merged, Not Measured https://arxiv.org/abs/2609.37985 | preprint | cloud agent; 2025 (AIDev v4) | Performance fixes accepted 42% (Codex/Claude Code/Jules 73%) |
| 15 | Not All Agents Are Equal (Texas Tech) https://arxiv.org/abs/2609.17598 | preprint | cloud agent; Dec 2024–Jul 2025 | Lowest security-smell presence, 1.6%; hard-coded credentials 0.5% |
| 16 | Trust but Verify? (UTSA) https://arxiv.org/abs/2607.12428 | preprint | cloud agent; 2025 | About 40.6% of PRs with a security smell (corpus average 38.9%); value read from a figure |
| 17 | IssueTrojanBench (Concordia) https://arxiv.org/abs/2607.20759 | preprint | auto-run mode, version unstated; 2026 | Malicious issues succeeded in 66.5% of runs (Sonnet 4.6 41.1%, GPT-5.4 73.6%, GPT-5.3 Codex 84.8%) |
| 18 | Your Harness is Not Secure / AdvCLI (Georgia/JHU and others; one Apple author) https://arxiv.org/abs/2510.06607 | preprint | Cursor IDE and CLI with Opus 4.1; 2025–26 | Attack-technique misuse tasks completed: IDE 39.19%, CLI 62.16% |
| 19 | AgentKernelArena (AMD) https://arxiv.org/abs/2605.16819 | preprint | Cursor Agent CLI; 16–24 Apr 2026 | First on Triton-to-Triton (2.13×) with Opus 4.7; compilation 69.4% with GPT-5.4 on PyTorch-to-HIP |

**About the counted set:**
- 1–8 and 11–16 (14 sources) are pull-request field studies built largely on the **AIDev** dataset. They identify Cursor PRs by the `cursor/` branch prefix, which mostly captures background or cloud agents. D4 asks whether they should count separately.
- 9, 10 and 17–19 are independent benchmark or security tests with their own data.
- Field studies count under 0040 D3. Security tests that run the named agent count, as Red-Teaming did for Claude Code and HarnessSecurity-Bench did for Codex.

## Other sources (listed, not counted)
- **Descriptive or too small** (other):
  - All Smoke, No Alarm (Cursor tests have weaker oracles than Claude Code and Devin);
  - Habituation at the Gate (Cursor sample of 10–18, underpowered);
  - Who Finishes the Job? (only 8 Cursor pairs; the authors do not compare cohorts);
  - Why Agentic PRs Merged or Rejected;
  - Collaborator or Assistant?;
  - Beyond Simpson's Paradox;
  - Insights into Security-Related AI PRs;
  - Rejection of fixes (pooled agents);
  - Merge-conflict rates;
  - AI IDEs or Autonomous Agents? (pooled agents);
  - Agentic Much? (TOSEM, adoption).
- **Speed at the Cost of Quality** (CMU; MSR 2026; https://doi.org/10.1145/3793302.3793349; other under D5).
  - Projects adopting Cursor saw a short-lived 3–5× rise in lines added, then lasting increases in static-analysis warnings (+30%) and complexity (+41%).
  - Adoption is detected from `.cursorrules` files (Aug 2024–Mar 2025), mostly before agent mode became the default, so it measures the whole product. The appendix says the results hold for agent-era cohorts.
  - Google research awards are disclosed.
- **Security studies classified as other:**
  - NYIT MCP prompt-injection study (Cursor 1.6.45; all 4 attacks succeeded). Kept as other for consistency with the Claude Code entry's classification of the same paper.
  - HarnessSecurity-Bench: Cursor appears only in a documentation review.
- **Historical context:** RedCodeAgent (2025), which tested the 2024 "Composer" with the cursor-small model. Agent mode is not confirmed. It has a Microsoft Research co-author, but no Microsoft product is in the comparison.
- **CVEs and advisories** (other; disputes and adherence context):
  - **NVD:** 30 Cursor CVEs. 28 were published in 2025–26 and concern agent features. CVSS ranges from 4.4 to 9.8; four are 9.6 or higher. Examples:

    | CVE | Issue | Fixed in |
    |---|---|---|
    | CVE-2025-54135 | CurXecute: MCP file write leading to code execution | 1.3.9 |
    | CVE-2025-54136 | MCPoison: approved MCP config changed without re-approval | 1.3 |
    | CVE-2025-59944 | Sensitive-file case check | — |
    | CVE-2025-61590 to 61593 | Workspace RCE, MCP OAuth, CLI config, CLI sensitive files | — |
    | CVE-2026-22708 | Auto-run allowlist bypass | 2.3 |
    | CVE-2026-26268 | Git hooks sandbox escape | 2.5 |
    | CVE-2026-50548 / 50549 | Sandbox escapes | 3.0 |
    | CVE-2026-61613 | Cloud agent browser | 31 Mar 2026 |
    | CVE-2026-73217 / 73218 | macOS auto-run sandbox | 3.1.2 / 3.0.0 |

  - All 28 were published by Cursor through GitHub advisories, with patched versions given.
  - The two 2024 CVEs (macOS permissions; Cmd-K terminal) are out of scope.
  - **GitHub:** https://github.com/cursor/cursor/security/advisories lists 33 advisories (Sep 2024–Jul 2026), two rated critical (June 2026 desktop sandbox escapes). A few concern billing or usage APIs, not the agent.
- **Anecdotal:** PocketOS (April 2026). The founder reported that a Cursor agent running Opus 4.6 deleted a production database volume, using an unrelated over-scoped token. The cloud provider later restored the data. One self-reported incident; sources include https://www.businessinsider.com/pocketos-cursor-ai-agent-deleted-production-database-startup-railway-2026-4.

## Not counted
- **Competitor** (independence rule: "not published by a competing product to promote itself"; the authors' company's product is in the comparison and comes out ahead in places):
  - Setup Complete, Now You Are Compromised (https://arxiv.org/abs/2607.15143). Corresponding author at microsoft.com; Copilot CLI is compared. Cursor CLI installed a look-alike package in 28 of 30 runs.
  - RepoGenesis (https://arxiv.org/abs/2601.13943). Microsoft authors; GitHub Copilot is compared and leads on Python. Cursor deployability 68.18% (Python), 75.00% (Java).
- **Model only (0036 caution 2 / 0039):** IDE-Bench, which tests models in a Cursor-like harness, not Cursor.
- **Mentions only:** Approval Laundering (no Cursor test; a substitute was planned), DeepSWE, VibeJam, MT-Sec, PostTrainBench.
- **Vendor:** Anysphere blog and docs, CursorBench, the Composer 2 Technical Report (arXiv 2603.24477), and "Scaling long-running autonomous coding".
- **Not scored as disputes:**
  - A law firm's announced "investigation" (Aug 2026) about AI training on user code. It concerns data policy, and no filed action was found.
  - The August 2026 Terms of Service change (arbitration removed).
- **Not screened (recheck note):**
  - MSR 2026 papers available only by DOI: Bug-Fixing in the Age of AI (3793570), When AI Code Doesn't Stick (3793587), Behind Agentic Pull Requests (3793586).
  - "Who Migrates the Schema?" and "Can Coding Agents Produce Merge-Ready Feature PRs?" (replication packages only found).
  - SSRN 7508618; a university thesis comparing IDE agents; "Your Cursor is Not Secure" (a repository record, possibly an earlier AdvCLI version).
  - The METR 2025 developer RCT. Cursor was the tool most used, but the tool was not fixed by design, so it would be other at most.

## Precedents applied
- **0031:** no shared authors with Anysphere were found in any counted source. Author blocks were checked for all 19.
- **0039:** model-only results are context only.
- **0042 / 0076:** no re-implementations or re-scoring among the counted sources.
- **0058:** the illustrative case studies inside Red-Teaming are not counted separately.
- **0036 cautions:** vendor results are not counted; the named product must be run; versions and dates are recorded; CVE wording is neutral.
- **0040 D3:** pull-request field studies count.
- **0040 D4:** funding is disclosed and the source still counts (AdvCLI: Apple co-author; Speed at the Cost of Quality: Google awards, though it is other for scope reasons).

## Proposed score (Scoring rules v0.1)
| Factor | Weight | Score | Reasoning |
|---|---|---|---|
| Completion rate | 30% | **55** | PR acceptance is usually 2nd or 3rd of 5 (64–77%), below Codex and above Copilot and Devin. It is lower on performance fixes (42%) and CI success (65–73%). Benchmarks: tied highest on SWE-Bench Mobile (12%, low in absolute terms); first on one AgentKernelArena category. Between Claude Code (50) and Codex (60). |
| Disputes | 20% | **45** | 28 in-scope CVEs, including 2026 sandbox escapes rated 9.6 or higher. All have fixes published by Cursor. A 2025 pricing dispute was resolved with an apology and refunds. No filed legal or regulatory action. Same as Claude Code (45, with 35 advisories); below Codex (55, with 7 CVEs). |
| Adherence to limits | 25% | **40** | 66.5% malicious-issue success in auto-run mode; 39.19% (IDE) and 62.16% (CLI) misuse completion; NYIT rated Cursor the most exposed MCP client; many CVEs are allowlist, sensitive-file or sandbox bypasses; one destructive-action incident. Mitigating: newer versions were much harder to hijack (≤0.3), and security-smell rates in PRs were low or average. Same as Claude Code (40). |
| Evidence quality | 25% | **85** | 19 counted, 10 peer-reviewed, versioned tests within 12 months. It is not higher because 14 sources are correlated AIDev field studies and the benchmarks are few and model-dependent. Same as Codex and Claude Code (85). Scored on the evidence, not to fit the grade. |

- **Overall:** 0.30×55 + 0.20×45 + 0.25×40 + 0.25×85 = 16.5 + 9 + 10 + 21.25 = 56.75, which rounds to **57**.
- **Grade A:**
  - 7+ counted (19);
  - 3+ peer-reviewed (10);
  - a current-version test within 12 months (v3.3.30 in the ISSTA 2026 revision; v2.3 in KDD 2026).
- **Check:** check_scores on a temporary copy of the repo in /tmp returned "OK cursor-agent: overall 57 (computed 57), grade A, counted 19, peer-reviewed 10", with 0 errors and 0 warnings.

**Sensitivity:**
| Change | Counted | Peer-reviewed | Grade |
|---|---|---|---|
| D1b (no CLI) | 18 | 10 | A |
| D3b (count both competitor papers) | 21 | — | A |
| D5a (count Speed at the Cost of Quality) | 20 | 11 | A |
| **D4b (AIDev studies collapsed to one source)** | 6 (5 without CLI) | 3 | **B** (A needs 7+); evidence would drop to about 75 and the overall to about 54 |

D4b would also change other entries (see D4).

## Risks and uncertainties
- **Shared dataset.** Most counted sources reuse AIDev (2025 data). The grade depends on the D4 ruling.
- **What the field studies measure.** They see only PRs on `cursor/` branches, which mostly come from background or cloud agents. Agent mode inside the editor is measured mainly by the security and benchmark studies.
- **Model dependence.** Benchmark and security figures describe Cursor plus a chosen model; results swing widely by model (for example 2% vs 12% on SWE-Bench Mobile).
- **Version drift.** About v0.45 to v3.x in under two years; most field studies state no version.
- **Competitor rulings.** Excluding Microsoft-authored comparisons is a judgment under the independence wording. RedCodeAgent also has a Microsoft co-author but is held out for scope reasons, not as a competitor source.
- **Figure-read values.** The Trust but Verify figure (40.6%) and the Rise of AI Teammates table value (51.4%) come from PDF text extraction of figures and tables.
- **CVE counts.** NVD keyword search plus the GitHub advisory pages; four NVD records were not opened individually.
- **Venue claims.** Taken from paper headers or DOIs: MSR '26 headers, ISSTA/PACMSE DOI, KDD DOI, IST DOI.
- **Cross-entry follow-ups (note only, not part of this approval):**
  - SWE-Bench Mobile (KDD 2026) also tests Codex CLI v0.77.0 and Claude Code v2.1.37.
  - The Task-Level Evaluation and CI-footprints MSR papers also cover Copilot, Devin and Codex.
  - These are possible items for the monthly review.

## Decisions requested
- **D1 Scope.**
  - (a) Agent mode, background/cloud agents and the Cursor CLI agent, from January 2025. Tab completion, inline edits, chat-only use, Bugbot and the 2024 Composer are excluded (**recommended**; it matches the Codex and Claude Code approach of combining CLI and cloud).
  - (b) Agent mode and background/cloud agents only: 18 counted, grade A unchanged.
- **D2 Category and name.** Coding agent; name "Cursor agent"; slug `cursor-agent`. The page title is 59 characters, within the 68 limit. (**recommended**)
- **D3 Competitor sources.**
  - (a) Setup Complete and RepoGenesis are not counted (competitor) (**recommended**).
  - (b) Count both with disclosure: 21 counted.
- **D4 AIDev reuse: a ruling of its own, not decided silently.**
  - (a) Keep current practice (0040 D3, as applied in 0044 Copilot and 0045 Devin): each study counts once, with the visible note "largely drawn from one dataset" (**recommended for consistency now**).
  - (b) Count all AIDev-based studies as one counted source and list the rest as duplicates. Cursor becomes 6 / B. This is a methodology change: it would also cut Copilot (12 counted, nearly all AIDev) and Devin to about 1–2, which is Insufficient, and would lower counts for Codex and Claude Code. If wanted, it should be its own methodology packet with a review of every affected entry. It should not be applied to Cursor alone.
  - (c) A middle option for a later packet: count separately but cap evidence quality when most sources share one dataset.
- **D5 Whole-product adoption study** (Speed at the Cost of Quality).
  - (a) Count it as a productivity study (20 counted).
  - (b) Other, because it measures whole-product adoption that is mostly before the agent era and includes Tab (**recommended**).
- **D6 Scores.** Completion 55, disputes 45, adherence 40, evidence 85, giving **57 / A** (**recommended**).
- **D7 Disputes and CVE wording** as drafted. The 28 in-scope CVEs are described neutrally with fix versions. The pricing refund is recorded. The law-firm investigation and the ToS change are not scored. PocketOS is anecdotal. (**recommended**)
- **D8 Visible note** "Citation check incomplete — recheck later" (**recommended**; several MSR 2026 papers were not screened and Semantic Scholar/arXiv were unavailable).
- **D9 Entry page.** Add `agents/cursor-agent.yaml` and build the entry page plus the generated files (agents.json/csv, index, llms-full, sitemap, feeds). Approved 2026-10-19.
- **D10 Changelog row** for the new entry: separate approval.
- **D11 Deploy:** separate approval, using the usual manifest procedure.

## Minimum viable version
Approve D1a, D2, D3a, D4a and D6–D8 as decisions only. Keep the YAML private until D9 is approved. Hold D10 and D11. If you prefer to wait on the shared-dataset question, approve D1–D3 and D5 now, and decide D4 (and so the grade) in a separate methodology packet.

## Plain-English terms
- **Counted source:** an outside test of the product that meets the independence rules. Three or more are needed for a score.
- **Field study:** researchers measure what happened to real pull requests on GitHub, for example how many were merged.
- **AIDev:** a public dataset of agent-written pull requests from 2025 that many studies reuse.
- **Auto-run mode:** a setting that lets the agent run commands without asking each time.
- **Competitor source:** a test written by people from a company whose own product is in the comparison. Listed, not counted.
- **Current-version test:** a test within the last 12 months that states the version tested. It is needed for grade A.
- **CVE:** a public identifier for a security flaw. Here, Cursor published each one with a fixed version.

*Informational only; not a guarantee, endorsement, or certification.*

## Files
- Committed: agents/cursor-agent.yaml, public/agents/cursor-agent.html, this decision, the changelog row in data/changelog.yaml, the one-line caveat change in scripts/build_data.py, and the regenerated public files (index, compare/coding-agents, agents.json/csv, llms.txt, llms-full.txt, sitemap, changelog page and feeds).
- Kept private (not committed): the research working files and downloaded papers (/workspace/private-drafts/0083-cursor-agent/, /workspace/cursor83/).
