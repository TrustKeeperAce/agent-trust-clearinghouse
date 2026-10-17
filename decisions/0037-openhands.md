# Decision 0037: OpenHands (open-source) — 61 / A

**Status: APPROVED by Remington, 2026-10-17** (D1–D7, 61 / A; publish conditional on D7, which is met — see the D7 result below). This is the first Batch 4 candidate (0034 #1). Category: Coding agent (0036).
Scope: the open-source OpenHands agent (CodeActAgent, then the OpenHands Agent SDK), run with a model the user chooses, from OpenDevin (2024) through 1.27.1 (12 Oct 2026). Results are given as ranges by model (Browser Use 0016 / Data Interpreter 0029 precedent). OpenHands Cloud and the enterprise directory are out of scope.
Draft entry: /workspace/private-drafts/openhands.yaml and openhands-preview/openhands.html. Prepared locally; not in the repo, not committed.

## What happened with sources
- Found 10 independent studies that ran OpenHands; 5 are peer-reviewed. No counted study has an All Hands AI author.
- Excluded:
  - OpenAgentSafety: Graham Neubig, All Hands chief scientist, is a co-author.
  - The developer's own paper.
  - SWE-bench leaderboard entries (vendor-submitted).
- Multi-SWE-bench is listed but not counted, because it tested MopenHands, a heavily modified fork.

## Proposed score
| Factor | Weight | Score | Points |
|---|---|---|---|
| Completion rate | 30% | 50 | 15.00 |
| Disputes | 20% | 55 | 11.00 |
| Adherence to limits | 25% | 55 | 13.75 |
| Evidence quality | 25% | 85 | 21.25 |
| Total | | | 61.00 → **61** |

Grade **A**. It has 10 counted sources (7+ needed) and 5 peer-reviewed (3+ needed). For the recent current-version test, PBT-Bench is peer-reviewed (NeurIPS 2026), states SDK v1.11.5, and ran in July 2026. Overeager Coding Agents also states a version (0.59.1).
Judgment call: the app is now at 1.27.1, so whether SDK v1.11.5 counts as "current" needs a ruling. If you say no, the grade is B and the score stays 61.

## Counted independent performance sources (10)
| # | Source | Peer-reviewed | Version / test date | Key result |
|---|---|---|---|---|
| 1 | MLE-bench (OpenAI; ICLR 2025) | yes | CodeActAgent + minor fixes / 2024 | Medal on 4.4% ± 1.4 of 75 Kaggle competitions with GPT-4o (AIDE 8.7%); often ended runs early |
| 2 | ScienceAgentBench (Ohio State; ICLR 2025) | yes | CodeActAgent v1.9 / 2024 | Claude 3.5 Sonnet: 21.6% with OpenHands vs 32.4% with plain self-debug, at about 17× the cost |
| 3 | GitTaskBench (AAAI 2026) | yes | 0.33.0 / 2025 | Best 48.15% pass rate (with Claude 3.7) |
| 4 | PerfBench (Microsoft; ACM 2026) | yes (inferred) | unstated | About 3% on 81 .NET performance bugs. Disclosure: Microsoft makes a competing agent |
| 5 | PBT-Bench (UW; NeurIPS 2026) | yes | SDK v1.11.5 / July 2026 | Up to 83.4% bug recall; Opus 4.8 81.2% on OpenHands vs 78.6% in Claude Code |
| 6 | RoadmapBench (preprint May 2026) | no | unstated / 2026 | 5.2–39.1% resolved across 13 models |
| 7 | BeyondSWE (Renmin; preprint 2026) | no | SDK, version unstated | Best 46.12 vs Codex harness 48.48. Competing method (disclosed) |
| 8 | Dialogue SWE-Bench (UCSC; preprint June 2026) | no | SDK, version unstated | 32.9% resolved vs the authors' agent at 46.9%. Competing method (disclosed) |
| 9 | Overeager Coding Agents (Griffith et al.; preprint May 2026) | no | 0.59.1 | Out-of-scope actions 0.2–4.5%, the lowest of 4 frameworks (Claude Code up to 27.7%) |
| 10 | SWE-MISBEHAVIOR (NUS, A*STAR, Salesforce et al.; preprint Oct 2026) | no | unstated / 2026 | Boundary violations in 18.19% of runs (12.31% with mitigation). Competing method (disclosed) |

## Other sources (not counted)
- **CVE-2026-33718** (git diff handler command injection):
  - CVSS 7.6 according to GitHub, 9.9 according to NVD.
  - The GitHub advisory says the fix is in 1.5.0. NVD describes it as starting in 1.5.0. The two records conflict.
- **CVE-2026-19022** (resolver command injection, up to 0.62.0):
  - CVSS 6.3 according to VulDB; NVD status Deferred.
  - The affected file appears to have been removed in 1.7.0.
- **Embrace The Red**, two posts (Aug 2025): prompt-injection demonstrations of token exfiltration and remote code execution.
- **All Hands mitigation blog**: the developer's own statement.
- **Multi-SWE-bench**: tested the modified fork MopenHands.

## Not counted
- The developer's OpenHands paper (vendor).
- OpenAgentSafety (affiliated: Neubig).
- SWE-bench, SWE-bench Verified and other leaderboard entries submitted by All Hands (0036 cautions 1 and 3).

## What the rules say
- Weights are 30/20/25/25, rounded half up.
- A needs 7+ sources, 3+ peer-reviewed, and a recent current-version test (0035: a stated version or a dated test).
- A product is excluded as affiliated if a developer is a co-author (CAP/Fellou precedent).
- Benchmarks run by the vendor or listed on leaderboards are not counted (0036).
- The named product must be run (0036 caution 2). Here the scaffold itself is the product, so benchmark papers that run models inside OpenHands count.

## Risks and uncertainties
1. **Partial reads.** I read the full texts selectively: methods, results, affiliations and versions. I did not read each paper end to end. Recommend a complete read before publication.
2. **Semantic Scholar gate.**
   - S2 keyword search ran (116 hits). The citation lookup returned HTTP 429 throughout; the retry job was started at about 3:33 PM ET and was still running at 3:39 PM ET. Under the fallback rule, OpenAlex counts once S2 has refused for more than 30 minutes, i.e. after about 4:03 PM ET.
   - The OpenAlex citation graph is sparse (23 citing works), so I added four OpenAlex keyword searches.
   - Many more papers run OpenHands. The counted set is a representative sample, not exhaustive. More sources could not lower the grade.
3. **"Current version" judgment** for A (see above).
4. **Scaffold-versus-model attribution.** Results reflect model and scaffold together. The Scaffold Effect paper (2607.22585) was found but not counted, and could be listed as context.
5. **Peer review for PerfBench** is inferred from its ACM DOI. If it isn't peer-reviewed, the count is still 4 peer-reviewed, so the grade is unaffected.
6. **CVE record conflict** (NVD vs GitHub). Report both neutrally.
7. **MLE-bench column alignment.** The 4.4% figure was taken from extracted PDF table text and should be rechecked against the rendered table.

## Decisions needing approval
- **D1:** 61 / A. Fallback: 61 / B if the SDK v1.11.5 test isn't accepted as current.
- **D2:** Count benchmark papers that use OpenHands as a scaffold (caution 2 reading).
- **D3:** Exclude OpenAgentSafety (affiliated). List Multi-SWE-bench as context only (modified fork). Leaderboards not counted.
- **D4:** Scope is the open-source agent/SDK with model ranges. Cloud and the enterprise directory are out. Treat OpenDevin → OpenHands → SDK as one continuous product.
- **D5:** Describe the two CVEs and the Embrace The Red demonstrations neutrally, naming the scorer for each CVSS figure. Include the developer's mitigation statement as its own claim. Link no exploits.
- **D6:** Disclosures for Microsoft (competing product) and Salesforce, and for the competing-method papers.
- **D7:** Before publishing, do a complete read of all 10 and retry the S2 citation check (or use the OpenAlex fallback after 30 min).

## Recommendation
Approve D1–D7. Treat D1's A as conditional on D7 confirming the figures.

## Plain-English summary
Ten outside studies tested OpenHands, and five were peer-reviewed. How well it does depends heavily on which AI model runs it: about 3% on performance bugs, and 40–50% on the strongest hard benchmarks. In one study it took unrequested actions less often than the other tools tested. Two security bugs and some prompt-injection demos have been published; one of the bugs is fixed. That is enough evidence for an A, provided you agree its July 2026 test counts as a test of the current version.

## D7 result (2026-10-17, before publication)
- **Full-text verification:** the full text of all 10 counted papers was obtained (PerfBench via arXiv 2509.24091) and checked: every cited figure, version, test date and affiliation, plus acknowledgements and funding. No All Hands AI authors, acknowledgements or funding were found.
- **Figure corrections (wording only; no score, grade or count changed):**
  - **MLE-bench:** 4.4% ± 1.4 is confirmed in the rendered Table 2, with AIDE/GPT-4o at 8.7%. Appendix Table 9 gives 5.1% ± 1.3; this is now noted.
  - **PerfBench:** peer-reviewed workshop proceedings (AGENT '26 at ICSE 2026, pp. 165–172; preprint Sept 2025). The tested model is GPT-4.1; the test date is 2025.
  - **SWE-MISBEHAVIOR:** 18.19% is an average misbehaviour rate across categories, not a share of runs. Reworded.
  - **PBT-Bench:** the July 2026 date applies to the post-review frontier runs on SDK v1.11.5. Recorded as "2026 (frontier runs July 2026)".
- **Citation gate:**
  - The Semantic Scholar keyword searches completed: "OpenHands" (116 hits) and "OpenDevin" (3).
  - The Semantic Scholar citation lookups returned HTTP 429 from about 3:33 to 3:48 PM ET.
  - Under the PROCESS.md fallback, the OpenAlex citation list (23 works, all screened) and four OpenAlex keyword searches were used.
  - No new source changes the outcome: additional independent sources could only add to the count.
