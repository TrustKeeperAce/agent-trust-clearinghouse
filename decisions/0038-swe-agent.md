# Decision 0038: SWE-agent (open-source) — 58 / B

**Status: APPROVED by Remington, 2026-10-17** (D1–D7, 58 / B; D7 met — see the D7 result below; figures in the tables below are corrected per D7). This is Batch 4 candidate #2 (0034). Category: Coding agent (0036).
Scope (proposed): the open-source SWE-agent framework run with a model the user chooses, from the 2024 release through v1.1.0 (22 May 2025) plus the main branch (last commit 16 July 2026). Results are given as ranges by model. **mini-SWE-agent** (separate minimal agent, v2.4.6, July 2026) and **EnIGMA** (security variant) are out of scope.
Entry: agents/swe-agent.yaml and public/agents/swe-agent.html.

## Affiliation checks
- **Developer team**, from the SWE-agent paper: John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press (Princeton / Stanford). Related team papers (SWE-smith, SWE-bench Multimodal, EnIGMA) also include Diyi Yang, Ludwig Schmidt and others.
- **Checked:** the author lists and acknowledgements of all counted papers. No developer is an author of any counted paper.
- **SWE-PolyBench (Amazon)** acknowledges Jimenez and Yang. It also tested a modified "SWE-Agent-PB", so it is listed but not counted (MopenHands precedent).
- **SWE-bench / SWE-bench Verified leaderboard:** maintained by the SWE-agent team, so it is affiliated and not counted (cautions 1, 3, 4).
- **HAL (Princeton CITP):** different authors; no SWE-agent developers among the 31 authors. It is a leaderboard, so it is listed but not counted (caution 3).
- **SWE-bench-derived benchmarks** built by others (Live, Pro, SWT, SEC, EVO) count. Using the team's dataset does not make a study affiliated.

## Proposed score
| Factor | Weight | Score | Points |
|---|---|---|---|
| Completion rate | 30% | 45 | 13.50 |
| Disputes | 20% | 55 | 11.00 |
| Adherence to limits | 25% | 55 | 13.75 |
| Evidence quality | 25% | 80 | 20.00 |
| Total | | | 58.25 → **58** |

Grade **B**. There are 8 counted sources and 6 peer-reviewed (SWE-Bench Pro confirmed in D7), but no independent test from the last 12 months states the SWE-agent version.
- Versions are stated only in 2025 tests: v1.0.1 (SEC-bench) and v1.0.1-61-gaa4e8ea1 (GitTaskBench).
- Tests from 2026 (SWE-EVO, Vul4Py) don't state a version.

So it fails A's current-version condition. Under 0025 and 0035 that gives B, consistent with Browser Use and STORM.

## Counted independent performance sources (8)
| # | Source | Peer-reviewed | Version / date | Key result |
|---|---|---|---|---|
| 1 | SWT-Bench (ETH Zurich; NeurIPS 2024) | yes | adapted for test generation / 2024 | Beat non-agent methods at issue reproduction (15.9% with GPT-4; 18.5% improved variant); filtering its own fixes with its tests raised fix precision to 47.8% at 20% recall. Disclosure: one author is affiliated with LogicStar.ai |
| 2 | SWE-bench-Live (Microsoft; NeurIPS 2025) | yes | unstated / 2025 | Lite subset: 10.00–17.67% resolved across 4 models. Disclosure: Microsoft makes a competing agent |
| 3 | GitTaskBench (AAAI 2026) | yes | v1.0.1-61 / 2025 | Task pass rate 3.70–42.59% (best Claude 3.7); below OpenHands |
| 4 | SEC-bench (UIUC; NeurIPS 2025) | yes | 1.0.1 / 2025 | Vulnerability patches 26.2–33.8%, proof-of-concept 3.8–12.5%; best of 3 agents |
| 5 | Vul4Py (SMU, Monash, UNSW; Springer proceedings, Sept 2026) | yes | unstated / 2026 | 22 of 100 vulnerabilities fixed correctly (OpenHands 41, Trae 29) |
| 6 | SWE-Bench Pro (Scale AI) | yes (ICML 2026, PMLR v306; confirmed in D7) | unstated / Sept 2025 | Unified scaffold; public set 16.2–43.6%; 50-turn/$2 cap GPT-5 25.9%, Opus 4.1 22.7%; commercial set ≤17.8%. Disclosure: Scale runs a commercial leaderboard for this benchmark |
| 7 | SWE-EVO (FPT AI; preprint Dec 2025 / 2026) | no | unstated / 2025–26 | 4.17–39.58% resolved across 18 models |
| 8 | Trajectory-Level Security Debt (Univ. of Luxembourg et al.; preprint Sept 2026) | no | Nebius public runs | 3.9% (two scanners agree) to 14.9% (any scanner) of 830 test-passing runs had scanner findings in final code (not validated; authors cannot attribute them to the agent) |

## Other sources (not counted)
- **CVE-2026-75482:** path traversal in the optional trajectory inspector, confirmed in v1.1.0.
  - The inspector binds all network interfaces, allows any site to call it (wildcard CORS), and needs no login.
  - CVSS 3.1 7.5 (VulnCheck); NVD status Deferred.
  - GitHub issue #1472 has been open since 19 July 2026; no fix identified.
- **SWE-Bench+ (York University):** re-checked the patches the developers submitted. SWE-agent + GPT-4 fell from 12.47% to 3.97% after removing cases with leaked solutions or weak tests. Reported under disputes, because it re-analyses vendor runs rather than running SWE-agent.
- **UTBoost (ACL 2025):** added tests and re-ranked leaderboard entries, including SWE-agent's. Same treatment as SWE-Bench+.
- **SWE-PolyBench:** tested a modified version (see above).
- **HarnessSecurity-Bench:** a design review of security features across 40 coding tools, not a performance run.
- **USTC empirical study (2511.00872):** SWE-agent had the lowest correction rate (6.93%). It's unclear whether its repair patches were re-run, so it isn't counted.

## Not counted
- The developer's paper and the team's own follow-ups.
- SWE-bench leaderboards (affiliated) and HAL (leaderboard).
- Studies that ran only mini-SWE-agent (out of scope), e.g. "Beyond the Model" (2609.32459) and SWE-Bench ProMax.
- AgentLens: on checking, it ran OpenHands, not SWE-agent.

## Citation gate (PROCESS.md)
- **S2 keyword search:** "SWE-agent" completed (100 results screened). The remaining keyword queries and the citation lookup returned HTTP 429 continuously from 3:57 to 4:26 PM ET (more than 30 minutes).
- **OpenAlex fallback, run after the 30-minute wait:** citations of the SWE-agent paper (W7103754783, 248 citing works). The first pages were screened before OpenAlex returned 401 on later pages. That screening found Vul4Py, which is now counted. Plus five OpenAlex keyword searches.
- **Result:** best effort. This is a sample of a large literature. More sources could raise the count but can't by themselves change the grade, because the A condition needs a stated current version.

## What the rules say
- Weights are 30/20/25/25, rounded half up.
- A needs 7+ sources, 3+ peer-reviewed, and a recent test with a stated version or date (0035).
- Developer co-authors mean a study is excluded (0036 caution 4).
- The named product must be the thing run: mini-SWE-agent ≠ SWE-agent (caution 2).
- Re-analyses of developer-submitted runs are not independent runs.

## Risks and uncertainties
1. **mini-SWE-agent scope (D4).** Many 2026 benchmarks use mini-SWE-agent. Excluding it keeps the entry about one product, but it leaves out the most recent evidence from the team's ecosystem. Merging the two would likely give enough version-stated recent tests for an A, but it would rate a different, simpler agent.
2. **SWE-Bench Pro venue:** confirmed in D7 as ICML 2026 (PMLR v306); the count is 6 peer-reviewed; the grade is unchanged.
3. **Vul4Py peer review** is inferred from its Springer proceedings DOI. Without it, 4 remain; the grade is unchanged.
4. **Whether the project is dormant:** no release since May 2025, last commit July 2026, and the inspector CVE is unfixed.
5. **Selective reads.** Figures, versions, dates and affiliations were checked against full texts, but the papers weren't read cover to cover. Recommend a full read before publishing, as in 0037's D7.
6. **SWE-bench conflicts of interest.** The team maintains the benchmark that most studies build on. Studies by others are counted, which is consistent with the Agent S / OSWorld approach.

## Decisions needing approval
- **D1:** 58 / B, with 8 counted sources (5 peer-reviewed). Grade B because there's no recent test with a stated version.
- **D2:** Count independent benchmark papers that run SWE-agent, including those built on SWE-bench data.
- **D3:** Exclusions: the SWE-bench leaderboards (affiliated); HAL (leaderboard); SWE-PolyBench (modified version); and SWE-Bench+ and UTBoost as disputes rather than performance runs.
- **D4:** Scope is SWE-agent only; mini-SWE-agent and EnIGMA are out. Alternative: a separate mini-SWE-agent entry later.
- **D5:** Report CVE-2026-75482 neutrally (VulnCheck score, NVD Deferred, issue open, no fix identified, no exploit links). Note that the project appears dormant.
- **D6:** Disclosures for Microsoft (competing product) and Scale AI (commercial leaderboard).
- **D7:** Before publishing, a full read of all 8 and venue confirmation for SWE-Bench Pro and Vul4Py.

## Recommendation
Approve D1–D7. B is robust: no plausible correction changes it without a version-stated 2026 test.

## Plain-English summary
Eight outside studies tested SWE-agent, and five were peer-reviewed. How well it does depends heavily on the model and task: about 10–18% on fresh GitHub issues, and up to about 40% on some harder benchmarks with strong models. Some early results the developers reported were found to overstate it. One security bug in an optional viewer is unfixed, and the project hasn't had a release since May 2025. There's good evidence, but none of it confirms the current version, so the grade is B.

## D7 result (2026-10-17, before publication)
**Outcome unchanged: 58 / B, 8 counted sources, now 6 peer-reviewed.** No score, grade or outcome change.

**Venues.** Vul4Py: ProvSec 2026 (Provable and Practical Security), Springer LNCS — peer-reviewed. SWE-Bench Pro: ICML 2026, PMLR v306 — peer-reviewed (the LIPIcs DOI OpenAlex attached belongs to a different paper). Peer-reviewed count 5 → 6; grade stays B (A still needs a test from the last 12 months with a stated version: GitTaskBench and SEC-bench state v1.0.1 but are from 2025; SWE-EVO's 2026 runs and Vul4Py do not state a version).

**Reads.** Read cover to cover, references excluded: Vul4Py; SWE-Bench Pro (v2, incl. appendix); SWT-Bench (incl. appendix); SWE-bench-Live (incl. appendices and checklist); Trajectory-Level Security Debt; GitTaskBench (v2, incl. appendices A–G); SWE-EVO (v6, incl. appendices A–N). SEC-bench (v2): main text and appendices A and B.1–B.3 read in full; the prompt listings (B.4–B.5), licence table and verifier-agent prompt appendices were checked by keyword only, not read line by line.

**Corrections applied to the entry.**
- SWE-Bench Pro: "up to 23.3%" replaced by the v2 Table 1 public-set range 16.2–43.6% (models as of 18 Sept 2025), the 50-turn/$2-capped figures (GPT-5 25.9%, Opus 4.1 22.7%) and commercial set ≤17.8%; test date Sept 2025.
- SWT-Bench: the 47.8% figure is SWE-agent's own fix precision after filtering with its generated tests (20% recall), not precision "over non-agent baselines"; added 15.9% (GPT-4) / 18.5% (improved variant); disclosed one author's LogicStar.ai affiliation.
- Vul4Py: agents were given the CVE ID and fix-location hints (100 steps, $3 cap); noted.
- SWE-bench-Live: added full-set results (GPT-4.1 18.57%, Claude 3.7 Sonnet 17.13%).
- SEC-bench: "highest of three agents" limited to the 80-instance subset (comparable to OpenHands on the full 200); added the five-run repeat (30.0%, SD 7.9); "patches mostly under 10 lines" corrected to one cited case.
- GitTaskBench: testers raised timeouts and removed a default "do not install packages" instruction; noted.
- Trajectory-Level Security Debt: "introduced security findings" corrected to "had scanner findings in final code"; the authors state findings are not validated and may predate the agent (Llama 3.1 runs by Nebius).

**Judgment calls kept (flagged to the user).** Completion stays 45 although SWE-Bench Pro's v2 public-set top figure is 43.6%: most counted results are 10–40% and the capped and commercial figures are lower. Trajectory-Level Security Debt stays counted as approved; it analyses third-party runs and does not attribute findings to the agent, so it could instead be listed as context — doing so would give 7 counted / 6 peer-reviewed and still B.

**Citation gate:** as recorded above (S2 after 30-minute 429 wait; OpenAlex fallback, first pages only). No new sources added in D7.
