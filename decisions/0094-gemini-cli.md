# Decision 0094: Gemini CLI (open-source) — 53 / A

**Status: APPROVED by Remington, 2026-10-21 (3:31 PM ET, t244u), as recommended:** 53 / A (completion 45, disputes 45, adherence 35, evidence 85; 28 counted, 8 peer-reviewed); D1a scope, D2a 'What this entry does not cover' section (Jules, Gemini models), D3a (A kept, with the fragility stated plainly on the page and in the summary: A rests on the single lower-assurance IJLTER v0.27.3 study; otherwise B / 51), D4a, D5a, D6a, D7a, D8a, D9a, D10a, D11a (advisory wording as drafted), D12a ('Gemini CLI' added to the managed-products list in the coding-agents caveat), D13 ('Model dependence' section), D15a name; D14 cross-references NOT applied (listed only). Banner kept. Batch 6. The entry YAML carries `decision: APPROVED`. **Commit and push approved 2026-10-21 (3:40 PM ET, t245u) with W1–W4 as recommended; deploy (D18) NOT approved.** W1: the four ACM/MDPI DOI links that return 403 to automated requests are kept (all confirmed in Crossref). W2: "lower assurance for software claims" kept. W3: Cyera issue/PR detail not added. W4: Redguard credit kept as is. Entry commit 99f689a; the approved patch was applied unchanged.

**Citation check incomplete — recheck later.**
- **OpenAlex full text** was the main search ("Gemini CLI" and its variants). 457 works were screened. All 341 arXiv full texts were downloaded and grepped for mentions, versions, affiliations and venues; 126 mention Gemini CLI five or more times.
- **Not used:** the arXiv API and Semantic Scholar. **Not retrieved:** one MSR 2026 paper (10.1145/3793302.3793585) and the Redguard advisory (HTTP 504).
- **More studies ran Gemini CLI than were reviewed.** The counted set is a sample of 28; further candidates are listed below and were not counted.
- **Security records:** OSV, NVD, the GitHub advisory, and the Tracebit, Pillar, pwned.info, Cyera, Snyk and Ars Technica write-ups, plus issue #4586. All were fetched 21 Oct 2026. The unauthenticated GitHub API was rate-limited, so the repository advisory list came back empty. The two CVEs were found through NVD and OSV.
- Search notes: research/source-table.md.

## What happened
1. **Product and scope** (D1, D2). Gemini CLI (https://github.com/google-gemini/gemini-cli; npm @google/gemini-cli) is Google's Apache-2.0 terminal coding agent, written in TypeScript. It is built for Gemini models; studies used other models only through adapters or proxies. It is a different product from Google Jules (cloud agent, live entry 0092, which already excludes Gemini CLI) and from Gemini Code Assist agent mode. Results for Gemini models alone are model results (0039).

   | Date | Milestone (npm, repository) |
   |---|---|
   | 17 Apr 2025 | Repository created |
   | 25 Jun 2025 | v0.1.0 (public launch) |
   | 25 Jul 2025 | v0.1.14 (Tracebit fix) |
   | 22 Oct 2025 | 0.10.0 |
   | 6 Feb 2026 | 0.27.3 (tested in IJLTER, C7) |
   | Apr 2026 | 0.39.1 (fix for CVE-2026-12537 and CVE-2026-13745) |
   | 28 Apr 2026 | 0.40.0 |
   | 8 Jul 2026 | 0.50.0 |
   | 15 Sep 2026 | 0.60.0 |
   | 20 Oct 2026 | 0.65.0 (latest stable; 0.66.0-preview.0 also out) |

   On 21 Oct 2026 the repository had about 107,500 stars and 14,800 forks, with 202 stable releases on npm (roughly weekly).
2. **Search:** OpenAlex full text, arXiv texts, Crossref, and the security records. Each source was sorted into one of these groups:
   - tests of Gemini CLI itself (same-model harness comparisons, fixed-harness, baseline and security studies);
   - Google-authored work;
   - competitor head-to-heads;
   - systems built on Gemini CLI;
   - source-code and repository-mining studies;
   - mentions.
3. **Results:**
   - **28 counted** independent performance sources: **8 peer-reviewed**, **18 state a version**, **15 versioned tests within 12 months**.
   - **13 other.**
   - **Not counted:** 3 competitor, 6 vendor (5 Google-authored papers plus the repository and docs).
4. **Google-authored material** is not counted (0031): the repository and docs, plus TestEvo-Bench, Honeyval, 3DCodeBench, VeriHarness and "Agentic Coding Needs Proactivity" (D10). No counted paper has a Google or DeepMind author; affiliation blocks were grepped.

## Counted: independent performance sources (28; peer-reviewed 8)
All accessed 2026-10-21. Type codes:
- **H:** same-model harness comparison.
- **X:** cross-vendor comparison (each agent with its own model).
- **F:** fixed Gemini CLI harness comparing models.
- **B:** Gemini CLI as baseline for the authors' research method.
- **S:** security study.

| # | Source | Peer review / independence | Version / model | Type | Result (Gemini CLI) |
|---|---|---|---|---|---|
| C1 | Terminal-Bench 2.0 (Stanford, Laude, Anthropic, Amazon…), arXiv 2601.11868 | **ICLR 2026**. No Google author. (Excluded for Claude Code because of an Anthropic author; counted for Codex) | unstated; Gemini 2.5 Pro/Flash | H | 2.5 Pro: 19.6% ±2.9 vs Terminus 2 32.6%, mini-SWE-agent 26.1%, OpenHands 15.7%. 2.5 Flash: 15.4% vs 15.5–17.1% |
| C2 | FeatureBench (CASIA, Huawei), arXiv 2602.10975 | **ICLR 2026** (stated in paper). Huawei authors; no Huawei agent | unstated; Gemini-3-Pro-Preview | H | Lite 10.0% / Full 5.0% resolved vs OpenHands, same model, 10.0 / 4.5; about 2.4× fewer input tokens |
| C3 | Sakura (Georgia Tech, IBM, UGA), doi 10.1145/3832112 | **ISSTA 2026** (PACMSE; Crossref confirmed). IBM authors; no IBM agent | unstated; 2.5 Flash/Pro | B (D7) | Compilable tests 60.9% (Flash) / 54.6% (Pro) vs 85–97% for the authors' method; focal recall 18–23% at high abstraction |
| C4 | QiMeng-Kernel (CAS), doi 10.1609/aaai.v40i34.40155 | **AAAI-26** (Crossref) | unstated (accessed 30 Jul 2025) | B (D7) | KernelBench H100 correctness: L1 51%, L2 32%, L3 22%; L1 mean speedup ~1.29; authors' method higher |
| C5 | MCP Threat Modeling (NYIT), doi 10.3390/jcp6030084; arXiv 2603.22489 | **J. Cybersecurity & Privacy 2026** (Crossref) | **0.9.0** (15 Oct 2025; test date not given); Gemini model | S | "Partially protected": refused remote scripts; logging and phishing attacks blocked; file read possible with FS permissions |
| C6 | Beyond Tool Poisoning (Kyung Hee), doi 10.3390/electronics15102214 | **Electronics 15(10), May 2026** (Crossref) | unstated; gemini-3.1-flash-lite-preview | S | File exfiltration 100% (90% sensitive); email 100%; refusal 0%; noticed typosquatting in 3/20 |
| C7 | Thai thematic analysis (U. Phayao), doi 10.26803/ijlter.25.8.5 | **IJLTER 25(8), Aug 2026** (received May, accepted Jul 2026); lower-assurance journal (D6) | **v0.27.3** (run 7 Feb 2026); Gemini 3 Pro Preview | X | Thematic reading 8/9; widest theme-count variation; reproducibility across all three runs 37% (lowest of the three tools) |
| C8 | TerminalWorld (UCL, Nanjing, Tencent), arXiv 2605.22535 | **ASE 2026 extended abstract** (3-page doctoral-symposium paper, doi 10.1145/3832783.3844572); full paper is a preprint (D4). Same classification as the live Codex and Claude Code entries | unstated; Gemini 3.1 Pro | H | 56.0% pass (59.6% resolved) vs Terminus-2 55.0% (57.0%) with the same model |
| C9 | AdvCLI "Your Harness is Not Secure" (UGA, JHU…), arXiv 2510.06607 | Preprint | **v0.6.1**; 2.5 Pro | S | ASR 39.19%; attempted 56.76% |
| C10 | Beyond Accuracy (UBC, Queen's), arXiv 2511.11012 | Preprint (TOSEM format; acceptance not confirmed → false, 0076) | **0.10.0** | X | Repair 43.07% (Claude Code 92.82%, Codex 87.38%, Qwen Code 26.98%); localization 49.26% |
| C11 | Overeager (Griffith, Quantstamp…), arXiv 2605.18583 | Preprint; shares authors with C12 (D9) | **0.14.0** | H | Overreach 10.4 / 10.0 / 13.1% (Sonnet-4.6 / MiniMax / GLM) vs Claude Code 27.7 / 11.8 / 12.8 |
| C12 | SNARE (same group), arXiv 2605.28122 | Preprint | unstated; 5 models | H/F | Mean 11.20%; 4.80% (GPT-5.3-Codex) to 18.40% (Gemini 2.5 Pro) |
| C13 | AST rules / BigBag (KTH, Montréal), arXiv 2606.24446 | Preprint | **v0.22.5**; Gemini 3.1 Pro | H | Highest fix rate in the study, 78.6% (Gemini CLI + JavaParser) |
| C14 | Agentic Botnets (TAU, Technion, Intuit), arXiv 2607.07433 | Preprint. Intuit author; no Intuit agent | **v0.24.5–v0.26.0**; 2.5 Flash | S | Searched in only 16% of runs; 82% of valid repository names hallucinated (registrable); RCE 20–35% |
| C15 | SkillsBench, arXiv 2602.12670 | Preprint (counted for Codex and Claude Code) | unstated; Gemini 3.1 Pro | H | 36.0 → 60.8% with skills vs OpenHands, same model, 33.8 → 52.8% |
| C16 | OpenSkillRisk (CityU HK, BUPT, Li Auto), arXiv 2607.20121 | Preprint. Li Auto has no agent in the comparison | **0.36.0-preview.5** | S | ASR 52.85 / 43.73 / 26.62% (2.5 Pro / 3 Flash / 3.1 Pro) vs 17.11–39.16% for Claude Code/Codex; authors: "Gemini CLI performs worse overall" |
| C17 | CORA "What's in Your Agent's Context?" (UIUC), arXiv 2609.01222 | Preprint (counted for Cline, OpenCode) | **0.39.0-nightly** | S | 102 escalation paths, 80–100% confirmed depending on model; loads nested GEMINI.md from subdirectories |
| C18 | SkillSafetyBench (Shanghai AI Lab…), arXiv 2605.12015 | Preprint | **0.39.13**; Gemini-3-Flash | S | Overall ASR 48.4%; "broader high-ASR pattern" than Claude Code + Opus-4.6 |
| C19 | SWE-Marathon (Abundant, Zenity, Harvard…), arXiv 2606.07682 | Preprint | **v0.40.0**; 3.1 Pro / 3.5 Flash | H | Pass rate 10.7% → 0% as runs of repeated tool calls lengthen (Claude Code 41.9 → 3.2%) |
| C20 | Overtrust (Sydney, Nanjing), arXiv 2605.08828 | Preprint | **0.40.1** | H | Misgrounding 85.8% (Gemini 3.1 Pro) / 75.3% (Qwen) vs Codex 67.3%, Claude Code 72.0% on Qwen |
| C21 | AgenticVBench (Philo Labs), arXiv 2605.27705 | Preprint | **0.41.1** | H | Leanest harness; 3.1 Pro 0.12–0.25 across families; same model did better in a third-party harness in one case |
| C22 | LLVM peephole (Waterloo), arXiv 2607.02684 | Preprint | **0.41.2**; Gemini 3 Flash | X | Highest profitability (42% Pass@3); lowest behavioral validity (63% vs up to 79% for Codex) |
| C23 | When Context Gets Root (Nanjing, Honor), arXiv 2608.27299 | Preprint (counted for OpenCode) | **0.50.0**; 3.1 Pro | S | Role confusion (MCPTox) 7/13 vs 0/13 for Claude Code and Codex; tool-to-system escalation 61.7% |
| C24 | HarnessSafe (BUPT, China Telecom, BAAI), arXiv 2608.06984 | Preprint (counted for OpenCode) | **0.51.0**; 3.5 Flash | S | Composite safety 48.7; ASR 13.41% (44/328) |
| C25 | Residual authority (WPI, Tsinghua), arXiv 2609.33910 | Preprint | **v0.58.0** (1 Sep 2026) | S | Silent exposure 0.12 (h=1) → 0.84 (h=64) under command-root matching vs Codex 0.12, OpenCode 0.11 |
| C26 | Cross-session skills (ANU, CityU, Data61), arXiv 2610.13227 | Preprint | **v0.61.0** | S | ASR 75.9% (3.6-Flash) / 59.3% (3.7-Flash); range across all configurations 46.7–77.4% |
| C27 | HarnessSecurity-Bench (SYSU…), arXiv 2610.07639 | Preprint (counted for Codex) | unstated | S | Folder trust ON: refused startup in all 40 trials (attacks and task both blocked); auto-approve raised ASR in every harness |
| C28 | ABTest (York, Polytechnique, Concordia), arXiv 2604.03362 | Preprint (placeholder ACM reference → false) | unstated; 2.5 Flash-Lite | F | Anomalies in 53.5% of runs |

- **Peer-reviewed:** C1–C8.
- **Versions stated (18):** C5, C7, C9, C10, C11, C13, C14, C16–C26.
- **Within 12 months (tested on or after 21 Oct 2025; 15):** C7, C11, C13, C14, C16–C26. C10 (0.10.0, released 22 Oct 2025) is borderline and not relied on.
- **Peer-reviewed and versioned within 12 months:** **only C7** (D3).

## Other sources (listed, not counted) — 13

| # | Source | Why other |
|---|---|---|
| O1 | Tracebit blog (28 Jul 2025) | Reporter's disclosure (D11) |
| O2 | Snyk SNYK-JS-GOOGLEGEMINICLI-11342370 | Record (Tracebit issue; no CVE) |
| O3 | GHSA-wpqr-6v78-jr5g / CVE-2026-12537 | Security record |
| O4 | NVD CVE-2026-12537 | Record |
| O5 | Pillar Security, "My Agentic Trust Issues" (5 May 2026) | Reporter's write-up |
| O6 | NVD CVE-2026-13745 | Record |
| O7 | pwned.info write-up | Reporter's disclosure and CVE-refusal timeline |
| O8 | Cyera Research Labs (Nov 2025) | Reporter's write-up (two VRP-fixed flaws) |
| O9 | Ars Technica (Jul 2025) | News on the Tracebit finding |
| O10 | Issue #4586 | "Deleted files" report, later withdrawn by the user |
| O11 | Don't Blame the LLM, arXiv 2607.03691 | Repository mining (close rate 81.8%) |
| O12 | Inside the Scaffold, arXiv 2604.03515 | Source-code taxonomy |
| O13 | Harness Engineering, arXiv 2609.00006 | Source-code study |

0079: other = 13 + 0 anecdotal = 13.

## Not counted
**Competitor (3; 0080/0083, D5):**
- **YoloFS**, SOSP 2026 (doi 10.1145/3830418.3843858). It has a Microsoft Research co-author and compares Gemini CLI 0.29.0 with GitHub Copilot CLI, a Microsoft product.
- **SWE-Milestone**, arXiv 2603.13428. It has an OpenHands author, OpenHands is compared, and it tests Gemini CLI v0.29.5.
- **Android build repair**, arXiv 2510.08640. Authors are from UC Davis and CodeDroid LLC; Gemini CLI is a baseline for the company-linked tool.

**Vendor (6; 0031):**
- TestEvo-Bench 2607.02469
- Honeyval 2605.29963
- 3DCodeBench 2606.01057 (Google DeepMind)
- VeriHarness 2610.00972 (Google Cloud AI Research)
- Agentic Coding Needs Proactivity 2605.06717
- The google-gemini/gemini-cli repository and docs

**Further candidates found but not reviewed for counting (not on the page):**
- **Security and agent skills:** Comment and Control 2605.11229 (GitHub Action hijack), VeriGrey 2603.17639, malicious skill files 2608.05223, PoisonedSkills 2604.03081, AuthorityLens 2609.32378, SkillHarm 2606.02540 (Amazon AGI), Demystifying Agent Skills 2608.14036.
- **Benchmarks:** CliniCARE-Bench 2608.07796 (Scale AI), LH-Bench 2603.22744, Is Grep All You Need 2605.15184, ScarfBench 2605.06754, SWE Atlas 2605.08366, NatureBench 2606.24530, ProjDevBench 2602.01655, AgentHorizon 2610.11050, CyberArena 2610.19005, SkillEvolBench 2605.24117, Change2Task 2607.28591.
- **Possible competitor or affiliation issues to check:** agentic code review 2607.16740 (possible Atlassian authors; Rovo Dev compared), InfraBench 2608.11234 (Qoder compared), 2605.07769 (Google affiliation not checked).
- **Other:** ANCHOR 2607.10455, ADI 2607.05120, CollabSkill 2606.09833, theorem proving 2610.09681, READY 2609.02095.
- **Not retrieved:** the MSR 2026 CI-pipeline paper.

Adding them would raise the count; it could change the grade only if a peer-reviewed one states a recent version, which would firm up A.

**Not listed:**
- Related-work mentions: LongCLI-Bench (Findings ACL), SBSeg, the ASE doctoral abstract.
- Systems using Gemini CLI as a component (ICS Workshops '26, 0042).
- Model-only Gemini results, Jules, Code Assist.

## Shared-author and affiliation check (0031, 0059)
- **Developer set:** Google / Google DeepMind / Google Cloud staff. No counted or other-listed paper has a Google author.
- **Companies among counted authors** (disclosed in notes; their own coding product is not compared): Anthropic and Amazon (C1; their agents are not in C1's Gemini CLI comparison but Claude Code is on the leaderboard — same treatment as the live Codex entry), Huawei (C2), IBM (C3), Tencent (C8), Quantstamp (C11/C12), Intuit (C14), Li Auto (C16), Abundant/Zenity (C19), Philo Labs (C21), Honor (C23), China Telecom (C24).
- **Shared authors between counted studies:** C11/C12 (Qu, Liu, Deng, Zhang, Li, Zhang). They are counted separately, as on the Codex entry (D9).

## Disputes, incidents and security (status 21 Oct 2026)
**Tracebit prompt injection (2025): no CVE.** Snyk SNYK-JS-GOOGLEGEMINICLI-11342370.
- **What:** a README / GEMINI.md prompt injection, combined with weak command-allowlist matching (command root only) and whitespace that hid the rest of the command in the TUI, made Gemini CLI silently run an attacker's chained command once a harmless command (e.g. grep) was allowed. Default mode, no sandbox.
- **Timeline (Tracebit, Sam Cox):**
  - 27 Jun 2025: reported to Google VDP.
  - Triaged P2/S4.
  - 23 Jul 2025: raised to P1/S1.
  - 25 Jul 2025: fixed in **v0.1.14**.
  - 28 Jul 2025: disclosure.
- **Google's reply, as quoted by Tracebit:** its CLI security model is "centered on providing robust, multi-layered sandboxing". Covered by Ars Technica and others.

**CVE-2026-12537 / GHSA-wpqr-6v78-jr5g:** critical by the CNA (Google) CVSS 4.0 score of 10.0; NVD 3.1 score 7.8 (AV:L/AC:L/PR:N/UI:R); CWE-20 / CWE-78. GHSA published 24 Apr 2026; NVD 24 Jun 2026 (Analyzed).
- **What:** headless mode treated the workspace as trusted, so a planted .gemini/.env could run host code before the sandbox started; --yolo also ignored tool allowlists.
- **Affected / fix:**
  - Gemini CLI < 0.39.1 and 0.40.0-preview.2 → fixed in **0.39.1** and 0.40.0-preview.3.
  - run-gemini-cli Action < 0.1.22 → fixed in **0.1.22**.
- **Reporters:** Elad Meged (Novee Security) and Devansh Batham; Pillar Security (Dan Lisichkin) is covered by the same fix. A duplicate GHSA-jj69-4grx-fqj5 was withdrawn on 24 Sep 2026.
- **Pillar:** reported 16 Apr 2026. A prompt-injected issue-triage workflow could compromise the gemini-cli repository's supply chain (the same pattern was found in at least 8 other Google repositories). Google patched within two days; Pillar thanks Google for "amazing cooperation".

**CVE-2026-13745:** Google CNA; CVSS 4.0 score 7.7 (high); CWE-15. Published 10 Sep 2026; NVD Awaiting Analysis.
- **What:** a .env file in an untrusted folder sets GEMINI_CLI_HOME, bypasses folder trust and loads a malicious config / MCP server, leading to code execution. Affects < **0.39.1**.
- **Reporter's timeline (pwned.info):**
  - 5 Mar 2026: reported.
  - 26 Mar 2026: US$500 bounty paid.
  - Apr–May 2026: Google twice declined to issue a CVE ("does not satisfy the required threshold").
  - 11 May 2026: MITRE dispute opened.
  - 12 Jun 2026: Google agreed to issue a CVE.
  - 29 Jun 2026: CVE reserved.
  - 10 Sep 2026: published with errors.
  - 23 Sep 2026: corrected.
- Redguard is also credited (advisory of 3 Jun 2026; not retrieved).

**Cyera (Nov 2025):** two command-injection flaws, reported through Google's vulnerability reward program and fixed. Fix versions not stated:
- the /ide install command for the VS Code extension;
- backtick command substitution that bypassed shell validation (the latter also reported publicly as #14926 and fixed by PR #15034).

**Issue #4586 (Jul 2025, v0.1.13, Windows):** reported as Gemini CLI destroying files and widely covered (Ars Technica). On 28 Jul 2025 the user wrote: "Okay, my bad. I did find these files in the C:\ root upon a deeper search…". The page states the files were misplaced, not deleted (D11).

**Legal / regulatory:** none found.

## Precedents applied
- **0031:** vendor material not counted; 5 Google-authored papers excluded.
- **0039:** model-only results are context.
- **0040 D3:** each study counts once.
- **0042:** systems built on Gemini CLI are other or not listed.
- **0051 / 0084 D7a:** stated version within 12 months (D3).
- **0059:** affiliations disclosed.
- **0071:** documented tests count.
- **0076:** unconfirmed venues → false (Beyond Accuracy, ABTest, HarnessSafe).
- **0079:** other = other + anecdotal.
- **0080 / 0083:** competitor sources listed, not counted (D5).
- **0085 / 0087 D3a:** fixed-harness benchmarks and attack studies count (D8).
- **0092:** Jules boundary (D2).
- **0010:** half-up rounding (52.5 → 53).
- **0065:** feed item.
- **0075:** title ≤68.
- **0090 D1:** caveat names every coding entry (D12).

## Score (Scoring rules v0.1)
| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion rate | 30 | 45 | **Mixed, somewhat below the coding peers.** Level or above with the same model: C8 (56.0 vs 55.0), C2 (≈ OpenHands), C15 (60.8 vs 52.8), C13 (highest fix rate). Clearly below: C1 (19.6 vs 32.6 Terminus 2, ICLR), C10 (43% vs 87–93%), C19 (10.7 → 0%). Weak as a baseline: C3 (54.6–60.9% compilable), C4 (22–51%). C7 least reproducible. Below Claude Code / OpenCode / Cline (50) because the largest peer-reviewed same-model test (C1) is clearly unfavourable |
| Disputes | 20 | 45 | Fixes delivered (v0.1.14; 0.39.1 for two CVEs; Cyera via VRP); Pillar reports a 2-day patch and thanks Google. Against: Tracebit initially triaged as low priority; CVE-2026-12537 critical by Google's own score; CVE-2026-13745 issued only after a MITRE dispute and published with errors; Tracebit flaw has no CVE. The #4586 "deletion" was withdrawn (not weighed against). Same as Cline (45), above OpenCode (40) |
| Adherence to limits | 25 | 35 | Many attack studies, several comparative, show **more** exposure than peers: C16 ("performs worse overall"), C23 (7/13 vs 0/13), C25 (0.84 vs ~0.1), C20 (85.8%), C6 (90–100% exfiltration, 0% refusal), C14 (82% hallucinated repositories), C26 (59–76%). Offsetting: folder trust blocked all attacks (C27, by refusing to start), C5 refused remote scripts, C11 less overeager than Claude Code. Below OpenCode / Cline / Claude Code (40) because of the direct comparisons |
| Evidence quality | 25 | 85 | 28 counted, 8 peer-reviewed, 18 versioned, many same-model and comparative security studies. Limits: preprint-heavy; mostly Gemini models; only one peer-reviewed versioned recent test (C7, lower-assurance journal); shared authors C11/C12. Same as OpenCode / Cline (85) |

0.30×45 + 0.20×45 + 0.25×35 + 0.25×85 = 13.5 + 9 + 8.75 + 21.25 = **52.50 → 53** (half-up, 0010; exactly on the boundary, so any 1-point factor change moves it).

**Grade A (borderline):**
- 28 counted (≥7) and 8 peer-reviewed (≥3).
- Versioned tests within 12 months: C7 (peer-reviewed, v0.27.3, February 2026) and 14 versioned preprints (v0.14.0 to v0.61.0).
- On the 0093 reading (a versioned **peer-reviewed** recent test is needed), A rests on C7 alone (D3).

**Fragility (counting decisions):**
| Variant | Counted | Peer-reviewed | Grade / overall |
|---|---|---|---|
| Recommended | 28 | 8 | **A / 53** |
| D3b: require a peer-reviewed versioned test, and C7 not accepted (or D6b: C7 not peer-reviewed) | 28 | 7–8 | **B**, evidence 80 → **51** (51.25) |
| D4b: C8 TerminalWorld not peer-reviewed | 28 | 7 | A |
| D5b: count YoloFS (SOSP 2026, 0.29.0) | 29 | 9 | A (no longer borderline: a second peer-reviewed versioned recent test) |
| D7b: C3, C4 treated as authors' own method → not counted | 26 | 6 | A |
| D8b: attack studies as other | 16 | 6 | A |
| D9b: merge C11/C12 | 27 | 8 | A |

**Score range (recommended counting):**
| Change | Overall |
|---|---|
| As proposed | 53 (52.50) |
| Completion 40 / 50 | 51 (51.0) / 54 (54.0) |
| Disputes 40 / 50 | 52 (51.5) / 54 (53.5) |
| Adherence 30 / 40 | 51 (51.25) / 54 (53.75) |
| Evidence 80 / 90 | 51 (51.25) / 54 (53.75) |

Plausible range 51–54.

**Index position:** after Perplexity (54) and before GPT Researcher (53). Ties sort by lower-case name, and "gemini cli" comes before "gpt researcher". Confirmed in the dry run.

## Risks and uncertainties
1. **Grade A hangs on one source** (D3/D6). The only peer-reviewed versioned recent test is in IJLTER, an education journal with low assurance for software claims.
2. **Exact rounding boundary.** 52.50 rounds to 53; any 1-point change in a factor changes the overall.
3. **Model dependence** (D13). Most results pair Gemini CLI with Gemini models. Some studies used GPT, Claude, Qwen or GLM models via adapters, which ordinary users rarely do.
4. **Version churn.** Weekly releases; no counted test after 0.61.0. Folder trust and headless trust behaviour changed in 0.39.1.
5. **Attack studies** (12 of 28) are often run with --yolo, auto-approve or headless. They describe exposure under attack, not default use.
6. **CVE wording.** Google and NVD scores differ for CVE-2026-12537 (10.0 vs 7.8). The CVE-refusal history for CVE-2026-13745 comes from the reporter only. Tracebit's flaw has no CVE.
7. **Scope edges** (D1). CVE-2026-12537 is filed under the run-gemini-cli Action but names Gemini CLI versions. Jules and Code Assist are excluded.
8. **TerminalWorld classification** (D4) copies the live Codex and Claude Code entries. The ASE item is a 3-page doctoral-symposium abstract.
9. **Search gaps** (banner): many more studies ran Gemini CLI; one MSR paper not retrieved; some competitor/affiliation checks not done for unreviewed candidates.

## Decisions (approved as recommended, t244u 3:31 PM ET)
- **D1 Scope.**
  - (a) **Recommended.** One entry for google-gemini/gemini-cli:
    - versions v0.1.0 to 0.65.0;
    - interactive and headless use, with any model;
    - advisories for the run-gemini-cli Action described where they affect Gemini CLI versions.
    - Exclude: Jules, Gemini Code Assist agent mode, Antigravity and other Google agents, systems built on Gemini CLI, model-only results.
  - (b) Also exclude everything about the GitHub Action (CVE-2026-12537 would then be described only as a Gemini CLI headless-mode flaw). Counts unchanged.
- **D2 Boundary wording vs Jules and Gemini models.**
  - (a) **Recommended.** A "What this entry does not cover" section (drafted) and a scope sentence. No Jules source is counted here, and no Gemini CLI source is in the Jules entry.
  - (b) Scope sentence only.
- **D3 Grade A.**
  - (a) **Recommended. A.** The rule as written is met: 28 counted, 8 peer-reviewed, and versioned tests within 12 months, including peer-reviewed C7 (v0.27.3, Feb 2026). The grade note says plainly that the grade rests on one peer-reviewed versioned test.
  - (b) **B / 51** if a peer-reviewed versioned recent test is required and C7 is not accepted (evidence 80).
- **D4 TerminalWorld peer-review status.**
  - (a) **Recommended.** peer_reviewed true, as on the live Codex and Claude Code entries ("ASE 2026 extended abstract").
  - (b) False here, and queue a consistency review of Codex and Claude Code. Still A.
- **D5 Competitor sources.**
  - (a) **Recommended.** YoloFS (Microsoft / Copilot CLI), SWE-Milestone (OpenHands author) and Android build repair (CodeDroid LLC) are listed, not counted.
  - (b) Count YoloFS with disclosure. It would firm up A (SOSP, 0.29.0).
- **D6 IJLTER (C7).**
  - (a) **Recommended.** Count as peer-reviewed (journal with received, revised and accepted dates; DOI resolves), with "lower-assurance journal" in the note.
  - (b) peer_reviewed false → see D3b.
- **D7 Baseline papers (C3 Sakura, C4 QiMeng).**
  - (a) **Recommended.** Count. The authors' own research prototype is not a commercial competing product, so the competitor rule does not apply; it is noted as the subject.
  - (b) Treat as competitor (26 counted; still A).
- **D8 Attack studies (0087 D3a).**
  - (a) **Recommended.** Count, as for Cline and OpenCode.
  - (b) Other → 16 counted / 6 peer-reviewed; still A.
- **D9 Shared authors C11/C12.**
  - (a) **Recommended.** Count separately (different methods and data; both counted on Codex).
  - (b) Merge → 27.
- **D10 Google-affiliated exclusions.**
  - (a) **Recommended.** Not counted (0031): TestEvo-Bench, Honeyval, 3DCodeBench, VeriHarness, Proactivity, plus Google's repo and docs. They are listed under Not counted.
  - (b) Omit from the page.
- **D11 Advisories and incident wording.**
  - (a) **Recommended.** As drafted:
    - Tracebit with dates and v0.1.14 ("no CVE");
    - CVE-2026-12537 with both scores, the fix versions and Pillar's thanks;
    - CVE-2026-13745 with the CVE-refusal history attributed to the reporter;
    - Cyera without versions;
    - #4586 stated as "misplaced rather than deleted".
    - Weighed in disputes (45).
  - (b) Shorter: IDs and fix versions only, omitting the refusal history.
- **D12 Required caveat edit** (scripts/build_data.py, coding-agents caveat 1). Required for check_all (0090 D1); applied only in the scratch dry run.
  - (a) **Recommended.** Add "Gemini CLI" to the managed-products list, alongside Claude Code and OpenAI Codex (vendor-built CLIs normally run with the vendor's models): "…Cursor agent, Replit Agent, Google Jules, Gemini CLI) are tested as shipped."
  - (b) Add it to the open-source frameworks list ("…Cline, OpenCode, Gemini CLI) are run with a language model chosen by the user…").
- **D13 Model dependence wording.**
  - (a) **Recommended.** A "Model dependence" section (drafted) plus the first uncertainty line.
  - (b) Uncertainty line only.
- **D14 Cross-references (NOT applied; candidates only).**
  - (a) Comparative studies that also test entries where they are not yet counted:
    - C1 / C2 / C15 / C19: OpenHands, mini-SWE-agent.
    - C20: Codex, Claude Code, OpenCode.
    - C25: Codex, OpenCode.
    - C16 / C18 / C26 / C22 / C10: Codex, Claude Code.
    - C21: OpenCode.
    - C11: OpenHands.
  - (b) **TerminalWorld peer-review consistency** (D4b), if chosen.
  - No score changes are proposed for other entries.
- **D15 Name and title.**
  - (a) **Recommended.** "Gemini CLI (open-source)", slug gemini-cli, Coding agent. Title "Gemini CLI (open-source) — Agent Reputation & Trust Clearinghouse" (65 characters; checked in the dry run). Homepage link to the repository.
  - (b) "Gemini CLI (Google)".
- **D16 Score.** 53 / A (45 / 45 / 35 / 85). Range 51–54. Approved.
- **D17 (later, not requested)** commit/push. **D18 (later, not requested)** deploy.

**Recommendation:** D1a, D2a, D3a, D4a, D5a, D6a, D7a, D8a, D9a, D10a, D11a, D12a, D13a, D15a, D16 (53 / A), with the banner. D14 is left for those entries' next reviews.

## Link check (21 Oct 2026, ~3:27 PM ET; dryrun/link-check.txt)
52 external links on the draft page: **46 return 200**.
- **4 × 403, publisher bot challenges:** ACM DOIs 10.1145/3832112 and 10.1145/3830418.3843858; MDPI DOIs 10.3390/jcp6030084 and 10.3390/electronics15102214. All four were checked in Crossref (titles and venues match). Kept.
- **2 × 404 expected:** the entry page (until deployed) and the decision record on GitHub (until pushed).

## Private dry run (scratch clones of 9dd76c6; real tree untouched)
Script: run_dryrun.sh → dryrun/. The real repo was checked before and after: HEAD 9dd76c6, 0 changed files.
- **Base rebuild drift:** none.
- **Page-only build** (dryrun/page): check_all fails by design with 1 error ("gemini-cli: no feed item", 0065), as for 0092 and 0093.
- **Full build** (dryrun/scratch):
  - check_all: **0 errors**.
  - check_scores: "OK gemini-cli: overall 53 (computed 53), grade A, counted 28, peer-reviewed 8"; 0 errors, 0 warnings, 6 documented (unchanged).
- **final_checks.py: 0 failures.**
  - Totals: base 42 / 31 scored + 11 insufficient / 78 changelog rows / 92 feed items / sitemap 50 / 24 banner pages → scratch **43 / 32 + 11 / 79 / 93 / 51 / 25**.
  - The other 42 entries' agents.json records are byte-identical, with zero score, grade or source-count diffs, and their entry pages are unchanged.
  - Feed ids are unchanged apart from the new item.
  - Placement: index order Perplexity → Gemini CLI → GPT Researcher; llms.txt line in place; sitemap entry present; D12 caveat text on the coding-agents comparison.
  - Page: title 65 characters; required phrases present; no banned words outside the standard disclaimer (page, YAML, changelog row).
- **Patch:** dryrun/draft-0094.patch, 15 files:
  - agents/gemini-cli.yaml, decisions/0094-gemini-cli.md, public/agents/gemini-cli.html;
  - data/changelog.yaml, changelog.html, updates.json, updates.xml;
  - index.html, llms.txt, llms-full.txt, sitemap.xml, agents.json, agents.csv;
  - compare/coding-agents.html, scripts/build_data.py (D12 caveat).
- **Other outputs:** preview at dryrun/gemini-cli.preview.html, changelog row draft-changelog-row.yaml, feed item feed-item.txt, LOG line draft-LOG-line.md.

## Final private step (t244u, 2026-10-21 ~3:35 PM ET)
- **Approved changes applied:**
  - YAML set to `decision: APPROVED`.
  - The grade note and the summary now state plainly that A rests on the single lower-assurance IJLTER v0.27.3 study, and that the entry would otherwise be B / 51.
  - The changelog row carries the same sentence.
- **Final patch:** final/final-0094.patch against base 9dd76c6, 15 files.
  - It applies cleanly to a fresh clone, and the applied tree equals the build.
  - Rebuild drift after apply: 0 files.
- **Checks:**
  - check_all: 0 errors. check_scores: OK, 53 / A, 28 counted, 8 peer-reviewed.
  - final_checks_final.py: 0 failures, including the fragility wording on the page and in the summary.
- **Link recheck:** 52 external links. 46 return 200; 4 return 403 (ACM and MDPI DOI bot challenges, all confirmed in Crossref); 2 return 404 as expected (they appear after push and deploy). No source link was down, so no archive swaps were needed.
- **Deploy prep:** manifest /workspace/manifest-0094; verify script /workspace/verify-0094/v94.py. Rollback target: dpl_5WMewXES6cz7whh2m2eBDC5qQT4u.

## Minimum viable version
Approve D1a, D2a, D3a, D11a, D12a and D16 (53 / A) with the banner and the "What this entry does not cover" and "Model dependence" sections as drafted. Leave everything else as recommended.

**Conservative alternative:** if the single IJLTER test should not carry grade A, publish as **B / 51** (D3b) with the same text and a grade note naming the missing peer-reviewed versioned test.

## Plain-English terms
- **Gemini CLI:** Google's free, open-source program that lets a Gemini AI model work on code from your terminal.
- **Google Jules:** a different Google coding agent that works in the cloud; it has its own entry.
- **Harness:** the program around an AI model that gives it tools (read files, run commands) and decides what it sees.
- **Same-model comparison:** testing different harnesses with the same AI model, so differences come from the harness.
- **Headless mode:** running the agent from a script or automation without a person watching.
- **Folder trust:** a Gemini CLI setting that asks whether to trust a project folder before loading its settings.
- **--yolo / auto-approve:** the agent runs commands without asking the user first.
- **Prompt injection:** planted text that makes an AI follow someone else's instructions.
- **CVE / GitHub security advisory (GHSA):** public identifiers for a security flaw. **CVSS:** a 0–10 severity score; different bodies can give different scores.
- **Vulnerability reward program (VRP):** Google's program that pays researchers for reporting flaws.
- **Peer-reviewed:** checked by independent experts before publication at a conference or journal.

---
*Informational only. This is a private draft summarizing cited public evidence under published rules; it is not a guarantee, endorsement, certification or ranking of quality, and nothing here has been published.*
