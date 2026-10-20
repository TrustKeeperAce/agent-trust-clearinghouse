# Decision 0085: mini-SWE-agent — 61 / A

**Status: D1–D10 APPROVED by Remington, 2026-10-20 (t165u), as recommended: D1a separate scope v1.0.0–v2.4.6 with cross-references; D2 developer set; D3a counting; D4 versioned tests (S9 2.4.6, S3 v2.2.8, with S10 and S14 supporting); D5 no run counted in both entries; D6 SWEnergy peer-reviewed; D7 disclosures; D8 61 / A; D9 CVE wording ('no fix found as of 20 October 2026'; Bubblewrap optional, default local environment unsandboxed); D10 'Citation check incomplete — recheck later' banner. D11 (entry page with changelog row, plus the SWE-agent cross-reference edit, the coding-agents caveat and the shortened page title) APPROVED by Remington, 2026-10-20 (t166u). D12 (deploy) is pending: nothing is deployed.**

Batch 5 candidate 3 (from packet 0082). Research completed 20 Oct 2026 (ET). Templates followed: 0037 (OpenHands), 0038 (SWE-agent), 0083 (Cursor agent), 0084 (FacTool).

**Citation check incomplete — recheck later.** OpenAlex full text was the main search. Semantic Scholar returned 429 (rate limit) on the first call and worked on a retry; the arXiv API timed out. The counted set is a representative sample, not an exhaustive list.

## What happened
1. **Scope set** (see D1). The entry covers mini-SWE-agent:
   - GitHub SWE-agent/mini-swe-agent and PyPI `mini-swe-agent`. MIT licence. Repository created 28 Jun 2025.
   - 65 GitHub releases:
     - v1.0.0 (22 Jul 2025) to v1.17.5 (30 Jan 2026);
     - v2.0.0 (11 Feb 2026), which changed the interface (the README links a migration guide and a separate v1 branch);
     - latest v2.4.6 (23 Jul 2026).
   - Last code commit on main: 3 Sep 2026.
   - About 1,200 forks and 103 open issues (GitHub API, 20 Oct 2026).
   - The agent class is about 100 lines. The model acts only through bash commands, and each step is run in a fresh subprocess.
   - It runs with any model through litellm and other providers.
   - Package authors: Kilian Lieret and Carlos E. Jimenez. The citation also lists John Yang and Ofir Press. All are SWE-agent / SWE-bench team members (Princeton, Stanford).
2. **Search.**
   - OpenAlex full-text search for "mini-swe-agent" matched 455 works, and "minisweagent" 8; together 458 unique works (438 from 2026).
   - 443 had a PDF link and 419 were downloaded and converted to text (/tmp/p85).
   - All 419 were screened for mentions, harness lists, version strings and developer co-authors. About 190 mention it at least five times.
   - The strongest candidates were then read in full, about 30 papers.
   - Also checked: web search, Crossref (venues), GitHub (releases, issues, commits, advisories), PyPI, NVD, OSV.
   - Semantic Scholar was intermittently rate-limited, and the arXiv API timed out.
3. **Results.**
   - **16 counted** independent performance sources, **9 peer-reviewed**.
   - **10 other** (8 other + 2 anecdotal).
   - **2 excluded** for shared authors (0031), plus 2 leaderboards not counted.
   - Vendor/maintainer material.
   - Four counted tests state the mini-SWE-agent version tested, all within the last 12 months, including the latest release (2.4.6).
4. **Score:** 61, grade **A** (D8 approved).

## Counted: independent performance sources (16; peer-reviewed 9)
Type: H = runs mini-SWE-agent alongside other harnesses with the same models; B = baseline for a method built on it; F = fixed harness used to compare models (0039-style context under D3b).

| Ref | Source | Peer review | Version / date | Type | Key mini-SWE-agent figures |
|---|---|---|---|---|---|
| S1 | When "Correct" Is Not Safe (CMU, Michigan, PKU, Colorado State, Google; ACL 2026 long) | yes | unstated / 2025 | H | 4.3–6.0% of test-passing SWE-bench patches had security weaknesses with no attack. Injected-issue attack success averaged 10.4% (SWE-agent 14.7%, OpenHands 9.7%), up to 67.6% for CWE-538 with Claude Sonnet 4. Disclosure: Google co-author. |
| S2 | EET (NTU, KCL, UCL, UIUC, Tsinghua; Findings ACL 2026) | yes | unstated / 2025 | H | SWE-bench Verified: 55.6% (GPT-5-mini, $16.07) and 66.4% (DeepSeek-V3.2, $52.20). The add-on cut cost about 19% with resolution unchanged. Add-on method disclosed. |
| S3 | DCAS (Huawei Canada, Queen's; ASE 2026) | yes | **v2.2.8** / 2026 | H | Qwen3-Coder-30B: 35.4% base and 42.4% for the trained variant. Models fine-tuned on OpenHands data collapsed in mini-SWE-agent (49.7% to 20.4%). Disclosure: Huawei. |
| S4 | SWEnergy (IIIT Hyderabad; AGENT '26 at ICSE, ACM) | yes | unstated / 2025 | H | 0 of 50 tasks with 1.7B/4B models. Some runs reported "success" with destructive or invalid patches; others ended early on context overflow. |
| S5 | Coordinating Agents on a Shared Git Workspace (Istanbul TU; ESEM 2026, LIPIcs) | yes | unstated / 2026 | B | Single-agent baseline: 138.3 and 152.0 of 266 SWE-Bench Pro instances. The authors' two-agent system, built on it, adds about 5 points. |
| S6 | ABC-Bench (Fudan and others; Findings ACL 2026) | yes | unstated / 2025–26 | H | Backend tasks: OpenHands about 50%; mini-SWE-agent below 20% with GPT-5 (read from a chart). |
| S7 | SWE-Mutation (USTC, Beihang, PKU and others; Findings ACL 2026) | yes | unstated / 2025 | H | Below Claude Code on test repair and generation. sed-based edits caused indentation and syntax errors. Claude Sonnet 4.5: 42.60% repair, 29.80% generation. |
| S8 | CodeScout (UMD, AWS and others; Findings ACL 2026) | yes | unstated / 2025 | H | SWE-bench Verified defaults: 51.8% (GPT-5-mini), 40.2% (Qwen3-Coder), 11.0% (DeepSeek R1). Add-on method disclosed. Disclosure: Amazon. |
| S9 | What Does a Harness Buy? Tokens, Mostly (Shandong; preprint 2610.04433) | no (a PREreview exists) | **2.4.6** (latest) / Sep 2026 | H | Within 5 points of Claude Code on 447 tasks. On 45 hard tasks, a harness swap flipped as many tasks (13%) as a rerun. Cost up to 3× apart; preamble 829 tokens against 16,581 for Claude Code. |
| S10 | SWE-Serve (UC Berkeley; preprint 2609.26777) | no | **v2.4.3** / Jul–Sep 2026 | H+F | Common harness for 11 models. Harness check: 75.5% against 73.6% (Codex) and 69.8% (Claude Code). |
| S11 | Beyond the Model (NJUST, NJU, TUM; preprint 2609.32459) | no | unstated / 2026 | H | SWE-bench Pro (300 tasks): OpenCode's lead fell from about 6 to 2.67 points across Qwen models; DeepSeek-V4-Pro 33.7 against 34.3. Its SWE-bench Verified table reuses leaderboard figures, which are not relied on. |
| S12 | A Jagged Frontier (CMU, UIUC, Colorado State, Microsoft; preprint 2608.18389) | no | unstated / 2026 | H | Lost less than OpenCode under code rewrites (1.34 vs 1.88 points on SWE-bench Verified, 1.88 vs 3.65 on SWE-bench Pro). Resolved 89.05% vs 81.20% on SWE-bench Verified and 76.35% vs 79.33% on SWE-bench Pro. Shares two authors with S1. Disclosure: Microsoft. |
| S13 | Hearsay (CWRU, NTU, NUS; preprint 2609.32495) | no | unstated / 2026 | H | 23 of 28 runs passed the entry test. Primary examiner corroborated share 75.3% (aider 40.6, SWE-agent 45.0, OpenCode 77.0). |
| S14 | DeepSWE (Datacurve; preprint 2607.07946) | no | **commit adfe2023** (21 May 2026, v2.3.0) / May 2026 | F (+ small H pilot) | Main table compares models. Pilot (10 tasks): equal to or above each vendor harness (within noise per the authors). Disclosure: Datacurve sells training data; the mini-SWE-agent README promotes this result. |
| S15 | LiveCANNBench (Beihang, UESTC and others; Findings ACL 2026) | yes | unstated / 2025 | F | Default mini-SWE-agent used for one task to compare models. |
| S16 | SWE-CC (SMU, SUTD; preprint 2610.06193) | no | unstated / Aug 2026 | H | Policy compliance 55.7% against OpenHands 58.2%; resolve rate 81.7% against 83.9%; 64.4% compliance when policies were supplied. |

## Other sources (listed, not counted) — 10
- **Re-analyses of runs made by others (0076):**
  - Frozen Judges (2609.34198): 35 leaderboard submissions.
  - Same Signal, Different Semantics (2605.18332): 64,380 public runs, 33 models on mini-SWE-agent.
  - Trajectory-Level Security Debt (2609.35199): the mini-SWE-agent part re-scans ProgramBench runs published by a team that includes mini-SWE-agent developers. Its SWE-agent part is already counted for SWE-agent.
- **Modified copies, forks and agents built on it (0042):**
  - Empowering Autonomous Debugging Agents (FSE 2026, PACMSE). Its baseline figures come from the SWE-bench leaderboard; its own runs use a modified mini-SWE-agent.
  - Live-SWE-agent (2511.13646): its baselines are reused, not rerun.
  - GA4GC (SSBSE 2025, LNCS): a fork, on 12 tasks.
- **Calibration use only:** Same Model, Different Harness (2608.26218). It uses v2.2.8 as a reference: 87.6% agreement, kappa 0.66.
- **CVE-2026-108592** (other).
- **Anecdotal:**
  - GitHub issue #941 (unpinned litellm causes intermittent crashes);
  - GitHub issue #990 (parallel Bubblewrap runs can share a workspace; fix PR #993 open).

## Not counted
- **Vendor/maintainer:**
  - the repository, README and docs (for example ">74% on SWE-bench Verified" and the adoption list);
  - PyPI;
  - PR #794 (litellm exclusion).
- **Affiliated leaderboard:** SWE-bench, SWE-bench Verified and bash-only leaderboards (same team).
- **Leaderboard:** HAL (Princeton CITP; no mini-SWE-agent developers), as in the SWE-agent entry.
- **Excluded (0031, shared authors):**
  - CodeClash (2511.00839; Lieret, Jimenez, Press);
  - ProgramBench (2605.03546; J. Yang, Lieret, Press).
- **Not used:**
  - SWE-fficiency (Press) and E2E-SWE (a "John Yang" co-author); either would be excluded if relevant.
  - Can Agents Design Libraries for Agents? (Ludwig Schmidt, a Stanford collaborator of the team but not a mini-SWE-agent author). Not needed; see D2.
- **Out of scope:**
  - papers that use mini-SWE-agent only to generate training data (many RL papers);
  - results for a model alone.

## Shared-author check (0031)
- **Developer set used:**
  - mini-SWE-agent package and citation authors: Lieret, Jimenez, J. Yang, Press;
  - SWE-agent paper authors: Wettig, Yao, Narasimhan.
- **Search:** OpenAlex authorships of all 458 works were checked for these names and for close variants (also Diyi Yang, Ludwig Schmidt, Kabir Khandpur).
- **Matches:**
  - CodeClash and ProgramBench (excluded);
  - SWE-fficiency, E2E-SWE and Context-Aware RL (Narasimhan) — not used;
  - Laguna (Khandpur), OpenThoughts-Agent and Can Agents Design Libraries (Schmidt) — not used.
- **Counted sources:** none of the 16 has a developer co-author. "Shunyu Liu" (Causal Improvement Graph) is not Shunyu Yao.

## Repository maintenance, disputes and security
- **CVE-2026-108592:**
  - published 10 Oct 2026 by VulnCheck; CVSS 4.0 6.0 Medium; CWE-526; NVD Deferred;
  - affects 1.10.0–2.4.6: the BubblewrapEnvironment omits --clearenv, so sandboxed commands inherit host environment variables, including API keys, which a prompt injection in task content could exfiltrate;
  - no fix was found in a release or on main (last code commit 3 Sep 2026), and no GitHub security advisory exists;
  - Bubblewrap is an optional environment; the default local environment has no sandbox by design.
- **Supply chain:** litellm 1.82.7 and 1.82.8 were compromised on 24 Mar 2026 (an environment-secret stealer). PR #794 excluded them and was merged about two hours after it was opened. Issue #941 (open) asks for pinning or a lock file.
- **Open proposal #953** (29 Aug 2026): task text is untrusted input to an agent with shell access; it proposes execution boundaries.
- **Confirmation:** the `mini` command-line tool starts in confirm mode by default. Batch and benchmark runs use "yolo" mode, with no confirmation.
- **Other disputes:** no legal or regulatory action found. No independent re-check of developer leaderboard claims specific to mini-SWE-agent was found (SWE-Bench+ and UTBoost concern SWE-agent).

## Precedents applied
- **0036 caution 2:** the named product must be run. Every counted source runs unmodified mini-SWE-agent. Claude Code / Codex results in the same papers belong to those entries.
- **0037 D2 / 0038 D2:** benchmark papers that run the scaffold count, because the scaffold is the product. Under this reading, S10, S14 and S15 count as well as the harness comparisons (D3).
- **0039:** results for a model alone are context. Under D3b, fixed-harness model comparisons would be treated the same way.
- **0031:** developer co-authors are excluded (CodeClash, ProgramBench), and same-team leaderboards are not counted.
- **0042:** modified copies, forks and derived agents are other (ADI, Live-SWE-agent, GA4GC).
- **0058:** illustrations are not counted. The README's adoption list and blog claims are vendor material.
- **0076:** re-scoring or re-analysing others' outputs is other (Frozen Judges, Same Signal, Security Debt).
- **0083 D4a:** no AIDev-based studies were found, so it does not apply.
- **0079:** derived_other counts other plus anecdotal, giving 10.
- **0051 / 0084 D7a strict:** an A needs a test within 12 months that states the version or commit. S3 (v2.2.8, peer-reviewed), S9 (2.4.6), S10 (v2.4.3) and S14 (commit adfe2023) all qualify.
- **Competing-method papers** count, with disclosure (0009, 0037). Corporate co-author disclosures follow 0038 D6.

## Score (Scoring rules v0.1; D8 approved)
| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion rate | 30 | 55 | With strong recent models it is close to heavier harnesses (S9, S10, S12, S11). It is lower for backend tasks (S6), test generation (S7), models trained on other harnesses (S3) and small models (S4). Higher than SWE-agent (45), whose counted results use older models. |
| Disputes | 20 | 55 | One medium CVE, recent and unfixed; a fast response to the litellm compromise; no legal action. The same value as SWE-agent and OpenHands. |
| Adherence to limits | 25 | 50 | Weaknesses in 4.3–6.0% of test-passing patches, and attack success between SWE-agent's and OpenHands' (S1). False success reports with destructive patches (S4). Slightly lower policy compliance than OpenHands (S16). No sandbox by default, and batch runs have no confirmation. Its records were relatively checkable (S13). |
| Evidence quality | 85 | 85 | 16 counted, 9 peer-reviewed, mostly 2026, with four versioned recent tests including the latest release, and 13 same-model harness comparisons. Lower within the A range because several studies propose competing methods, two share authors, and the sample is not exhaustive. |

0.30 × 55 + 0.20 × 55 + 0.25 × 50 + 0.25 × 85 = 61.25, which rounds to **61** (half-up rule, Decision 0010). check_scores on the scratch copy reports no WARN for this entry.

**Grade A:** 16 counted (≥7), 9 peer-reviewed (≥3), and a current-version test within 12 months that states the version (S9: 2.4.6, the latest release; S3 is also peer-reviewed and versioned).

**Sensitivity (D3 and others):**
| Variant | Counted | Peer-reviewed | Versioned ≤12 months | Grade |
|---|---|---|---|---|
| D3a (recommended; 0037/0038 reading) | 16 | 9 | S3, S9, S10, S14 | A |
| D3b (drop fixed-harness-only S15; keep S14 for its pilot and S10 for its harness check) | 15 | 8 | S3, S9, S10, S14 | A |
| D3c (strictest: drop S5, S10, S14, S15) | 12 | 7 | S3, S9 | A |
| Preprints excluded entirely (not a rule; illustration) | 9 | 9 | S3 | A |

The score moves only through judgment on the factors. Lowering evidence to 80 gives 60. Lowering completion to 50 gives 59.75, which rounds to 60. The plausible range is 59–62.

## Risks and uncertainties
1. **Model and harness attribution.**
   - Every figure describes mini-SWE-agent with a given model.
   - The strongest harness-only evidence (S9) finds harness choice moves pass rate little and cost a lot. The entry should not read as "the harness scores X%".
2. **Same team as SWE-agent.**
   - Readers may conflate the two entries. The scopes cross-reference each other, and no runs are counted in both.
   - S1, S8 and S13 run SWE-agent separately. Those runs could count for SWE-agent at its next review; that is a different product's runs, not double counting (D5).
3. **Developer-run leaderboards.**
   - Many papers quote mini-SWE-agent figures from the SWE-bench leaderboard. Only authors' own runs are used here (S11 and ADI were checked).
4. **v1 versus v2.**
   - Most counted studies do not state a version. Studies from 2025 (S1, S2, S4, S7, S8, S15) likely ran v1.x.
5. **Peer review.**
   - S4 is in workshop proceedings (AGENT '26, ACM), like PerfBench for OpenHands. S9 has a PREreview, which is not counted as peer review.
6. **The CVE is 10 days old.**
   - A fix may land soon; the wording says "as of 20 Oct 2026".
7. **Disclosures.**
   - Google (S1), Huawei (S3), Amazon (S8), Microsoft (S12) and Datacurve (S14). The README promotes S14's result.
8. **Sample.**
   - About 190 papers mention mini-SWE-agent substantively. The counted set favours peer-reviewed, recent and harness-comparison studies, and is not exhaustive.

## Decisions (D1–D10 approved 2026-10-20; D11 approved 2026-10-20; D12 pending)
- **D1 Scope.**
  - (a) mini-SWE-agent v1.0.0–v2.4.6 plus main, unmodified, as a separate entry from SWE-agent, with cross-reference sentences in both scopes. **Recommended.**
  - (b) Fold it into the SWE-agent entry. Not recommended: different code, releases and behaviour, and it would change what the existing 58/A rates.
  - (c) v2 only (Feb 2026+). This would leave about 9 counted (S3, S5, S9–S14, S16), only 2 of them peer-reviewed (S3, S5), so grade **B**. Not recommended: v1 is still published on a v1 branch and widely used.
- **D2 Developer set and same-team material.**
  - Treat Lieret, Jimenez, J. Yang and Press (package and citation authors) plus the SWE-agent paper authors as the developer set.
  - Exclude CodeClash and ProgramBench. Do not count the SWE-bench / bash-only leaderboards (affiliated) or HAL (leaderboard).
  - Stanford collaborators (Diyi Yang, Ludwig Schmidt) are excluded only when they co-author with the developers. Their other papers are not used here.
  - **Recommended as stated.** Alternative: also exclude any paper by Stanford/Princeton SWE-bench collaborators. No counted source changes either way.
- **D3 What counts as testing the agent.**
  - (a) Count independent studies that run unmodified mini-SWE-agent, including fixed-harness benchmarks, consistent with 0037 D2 (OpenHands) and 0038 D2 (SWE-agent). **Recommended.**
  - (b) Count only studies whose results are about the harness: same-model comparisons, its own outputs, behaviour or cost, and baselines. Pure fixed-harness model comparisons become 0039 context. This gives 15 counted, 8 peer-reviewed.
  - (c) Strictest: only same-model harness comparisons. This gives 12 counted, 7 peer-reviewed.
  - Grade A and the score hold under all three. (b) and (c) would make mini-SWE-agent stricter than OpenHands and SWE-agent; aligning them would need a methodology packet.
- **D4 Versioning for A.**
  - Accept S9 (2.4.6, the latest release, preprint) and S3 (v2.2.8, peer-reviewed, ASE 2026) as current-version tests. S10 (v2.4.3) and S14 (commit adfe2023, the v2.3.0 release) are supporting. **Recommended.**
  - Alternative: require a peer-reviewed test of the latest minor line (2.4.x). None exists, so the grade would be B. Not recommended: 0051/0084 D7a requires a stated version within 12 months, not peer review of the latest release.
- **D5 Overlap with SWE-agent.**
  - Count no run in both entries. Trajectory-Level Security Debt stays counted for SWE-agent and is listed as other here.
  - Note in the 0085 decision that S1, S8 and S13 also ran SWE-agent separately, for its next review. No SWE-agent change now. **Recommended.**
  - Alternative: add the cross-reference sentence to the SWE-agent scope now. That is a public text change to another entry and would need its own approval.
- **D6 Peer-review calls.**
  - S4 (AGENT '26 workshop, ACM proceedings) counts as peer-reviewed, as with PerfBench (0037). The S9 PREreview is not peer review. **Recommended.**
- **D7 Disclosures.**
  - Corporate co-authors: Google, Huawei, Amazon, Microsoft and Datacurve (with the README promotion).
  - Competing or add-on methods: S2, S3, S5, S8 and S11.
  - Shared authors S1/S12.
  - **Recommended as drafted.**
- **D8 Score.** 61 / A (55 / 55 / 50 / 85). Alternatives: 60 / A (evidence 80, or completion 50).
- **D9 CVE wording.** As drafted, with "no fix found as of 20 October 2026" and the note that Bubblewrap is optional and the default local environment is unsandboxed.
- **D10 Recheck note.** Show the "Citation check incomplete — recheck later" banner (OpenAlex only; Semantic Scholar intermittently rate-limited; arXiv API timed out; 39 of 458 works not downloaded).
- **D11 (APPROVED 2026-10-20, t166u).** Entry page plus changelog row, with the SWE-agent cross-reference edit, the coding-agents caveat and the shortened page title ("mini-SWE-agent — Agent Reputation & Trust Clearinghouse").
- **D12 (pending).** Deploy.

**Recommendation (approved 2026-10-20 for D1–D10):** approve D1a, D2, D3a, D4, D5, D6, D7, D8 (61 / A), D9 and D10 as decisions only. Hold D11 and D12.

## D11 notes (approved 2026-10-20, t166u)
- The draft page plus changelog row also changes two shared texts:
  - **Coding-agents comparison caveat** (scripts/build_data.py): mini-SWE-agent is added to the list of open-source frameworks run with a model chosen by the user. Precedent: 0083 added Cursor agent the same way.
  - **SWE-agent cross-reference (D1a):** in agents/swe-agent.yaml and public/agents/swe-agent.html, the scope sentence now says mini-SWE-agent has its own entry, and the page links to it.
    - There is no score, grade, source or last-reviewed change.
    - D5 recommended no SWE-agent change "now"; Remington approved this edit explicitly with D11 (t166u).

## Minimum viable version
Approve D1a, D3a and D8 at 61 / A with D10's recheck banner; leave the other wording as drafted. If D3 needs more thought, D3b gives the same grade and score.

## Plain-English terms
- **Harness / scaffold:** the code around a language model that turns it into an agent: prompts, tools, and how results are fed back. mini-SWE-agent is a very small harness.
- **SWE-bench Verified / Pro:** sets of real GitHub issues used to test coding agents. "Resolved" means the agent's change passed the project's tests.
- **Same-model comparison:** running the same language model in two harnesses, so differences come from the harness.
- **Fixed-harness benchmark:** a benchmark that runs every model in one harness to compare the models.
- **Peer-reviewed:** published at a venue that reviews papers before acceptance.
- **CVE / CVSS:** a public identifier for a security flaw, and its severity score.
- **Current-version test:** a test within the last 12 months that states the version tested. It is needed for grade A.

*Informational only; not a guarantee, endorsement, or certification.*
