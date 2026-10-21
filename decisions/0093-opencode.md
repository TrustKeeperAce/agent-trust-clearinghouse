# Decision 0093: OpenCode (open-source) — 54 / A

**Status: APPROVED by Remington, 2026-10-21 (10:52 AM ET), as recommended:** 54 / A (completion 50, disputes 40, adherence 40, evidence 85; 28 counted, 8 peer-reviewed); D1, D2 (archived Go opencode/Crush not counted; 'Which OpenCode' section; C3 counted with ambiguous version), D3a (A kept; the page states no counted test covers v1.19), D4a (advisories as drafted), D5a–D9a, D10a ('Model dependence' section), D11 (comparison caveat applied), D13a, D14; D12 cross-references NOT applied (noted only). Banner kept. Batch 6. The entry YAML carries `decision: APPROVED`. Commit/push (D15) and deploy (D16) are NOT approved. The real repository (HEAD 133d73a) has not been modified. **Commit and push approved 2026-10-21 (11:23 AM ET) with W1–W4 as recommended; deploy NOT approved.** W1: cy.md still failing at 11:25 AM ET (HTTP 500 from the box, fetch-tool timeout), so the source link was swapped to the Wayback copy web.archive.org/web/20260203132057/https://cy.md/opencode-rce/. W2: one attributed sentence added to the page's security section, quoting thdxr's 12 Jan 2026 comment on issue #6355 (verified against the GitHub API, comment 3740105995, 2:15 PM ET). W3: '1.14.30 to 1.18.21' kept. W4: CNA 9.4 and NVD 6.1 both kept.

**Citation check incomplete — recheck later.**
- **OpenAlex full text** was the main search ("OpenCode" with coding agent, harness, terminal and SST/Anomaly terms). 553 works were screened; all 474 arXiv full texts were downloaded and grepped for OpenCode mentions, versions and repository addresses; 222 works mention OpenCode six or more times.
- **arXiv API and Semantic Scholar** were not used. Non-arXiv papers were only partly retrieved (ESEM ×2, npj HealthFlow and a few others).
- **More studies ran OpenCode than were reviewed.** The counted set is a sample (28) of what was found; further candidates are listed below and were not counted.
- **Security records:** GitHub advisories for anomalyco/opencode (exactly 3 published), NVD, Datadog Security Labs, the reporter's post, GitHub issues; all fetched 20–21 Oct 2026.
- Search notes: research/source-table.md.

## What happened
1. **Product and scope** (D1). OpenCode (https://github.com/anomalyco/opencode; sst/opencode redirects there) is an MIT-licensed terminal coding agent in TypeScript from Anomaly (formerly SST; maintainers include Dax Raad/thdxr, rekram1-node, adamdotdevin). npm package opencode-ai. Users choose the model and provider.

   | Date | Milestone (repository, npm, GitHub releases) |
   |---|---|
   | 30 Apr 2025 | anomalyco/opencode repository created (Go history imported, TypeScript rewrite) |
   | 31 May 2025 | npm package opencode-ai created |
   | 31 Oct 2025 | v1.0.0 |
   | 30 Dec 2025 | v1.0.216 (CORS fix, CVE-2026-22812) |
   | 9 Jan 2026 | v1.1.10 (server and web UI off by default; CVE-2026-22813 fix) |
   | 30 Jan 2026 | v1.1.44 |
   | 8 Apr 2026 | v1.4.0 |
   | 29 Apr 2026 | v1.14.30 (introduced the GHSA-632h flaw, PR #24853) |
   | 24 Aug 2026 | v1.18.22 (GHSA-632h fix, PR #44686) |
   | 11 Oct 2026 | v1.19.0 |
   | 16 Oct 2026 | v1.19.3 (latest) |

   Repository on 21 Oct 2026: ~219,000 stargazers, ~29,000 forks. Release cadence is very high (716 releases in 278 days per "Don't Blame the LLM").
2. **Name collision** (D2). The Go project **opencode-ai/opencode** (created 16 Mar 2025, last release v0.0.55 on 27 Jun 2025, last push 18 Sep 2025, archived) is a different product. Its README says it moved and continues as **Crush** under Charm (Charm blog "Crush, Welcome Home", 30 Jul 2025; Kujtim Hoxha on opencode-ai/opencode#330, 29 Jul 2025). In anomalyco/opencode#333 (23 Jun 2025) thdxr says the code was largely rewritten in TypeScript and accuses the other side of name squatting. anomalyco keeps the Go git history, and **both repositories carry a v0.0.55 tag** (anomalyco: commit fae49aaf, 3 Jun 2025, TS era; Go project: 4427df5). Per-source attribution is in D2.
3. **Search.** OpenAlex, arXiv full texts and the GitHub/NVD advisory records, separating: tests of OpenCode itself; fixed-harness model comparisons; systems built on OpenCode; plugin studies; source-code taxonomies and repository mining; mentions.
4. **Results:**
   - **28 counted** independent performance sources, **8 peer-reviewed**; 16 state a version (one ambiguous).
   - **19 other** (no anecdotal sources listed).
   - **Not counted:** 3 competitor, 0 excluded (no Anomaly-authored study found), 2 vendor.
5. **Developer-authored material:** opencode.ai docs and the repository are vendor (0031). No paper with an Anomaly/SST author was found.

## Counted: independent performance sources (28; peer-reviewed 8)
All accessed 2026-10-21. Type: H = same-model harness comparison; F = fixed OpenCode harness comparing models; B = OpenCode as baseline for the authors' method; S = security study attacking OpenCode.

| # | Source | Peer review / independence | Version / model | Type | Result (OpenCode) |
|---|---|---|---|---|---|
| C1 | "To Run or Not to Run" (Beihang, Wuhan, SMU). doi 10.1145/3832113; arXiv 2606.26978 | **ISSTA 2026** (PACMSE; Crossref confirmed) | **v1.4.0** (8 Apr 2026; accessed 9 Apr 2026); Qwen2.5-Coder-32B | H | Prohibited vs Unrestricted gap ≈0 pp; highest with one run (Lite 14%, Verified 17%); retries more; only 11% of failed cases pass self-validation. Cites the Go repo URL but v1.4.0 exists only in anomalyco (D2) |
| C2 | SWE-Bench Mobile (Toronto, Xiaohongshu, UIUC, Berkeley). doi 10.1145/3770855.3818488; arXiv 2602.09540 | **KDD 2026** (Crossref confirmed) | **v1.1.44** (30 Jan 2026) | H | Opus 4.5: OpenCode 2% vs Cursor 12%; OpenCode max 8% (GLM 4.6, $0.13/task); "endless file reading loops" |
| C3 | DCAS (Huawei Canada, Queen's). doi 10.1145/3832783.3834485; arXiv 2608.06113 | **ASE 2026** (Crossref confirmed). Huawei authors; no Huawei agent compared | "OpenCode v0.0.55" citing anomalyco (**ambiguous**, D2) | B/F | Qwen3-Coder-30B 46.0 → 49.4 with self-plan; SWE-Lego-Qwen3-32B 8.4% (tool-call format incompatible with OpenCode's parser) |
| C4 | CausalGame (MBZUAI, CMU, HKBU, Oxford, NYUAD). arXiv 2607.04293 | **ICML 2026 oral** (short version accepted, stated in paper) | **v1.15.12** (accessed 29 May 2026) | F/B | OpenCode beats ReAct on all 5 models (+6.9 pp survival); deepseek-v4-pro OpenCode agent probed simulator API/admin routes for hidden configuration |
| C5 | "From Runnable Code to Shippable Applications" (CUHK, Columbia, SMU). doi 10.1145/3832783.3834388; arXiv 2605.17242 | **ASE 2026** (Crossref confirmed) | unstated | B | Vanilla OpenCode 72.0% vs authors' incremental TDD 89.2% |
| C6 | Coppola et al., "On Coding Agent Issue Localization Accuracy" (SDU, Oulu, Hawaii). doi 10.4230/LIPIcs.ESEM.2026.59 | **ESEM 2026** (LIPIcs; DOI resolves to Dagstuhl) | unstated; OpenCode + GLM-5 / Qwen3.5 / Kimi-K2.5 | F | 2,441 issues; package > class > method; MCC negative; GLM-5 strongest |
| C7 | "Beyond Heuristics? Targeted Unit Test Generation" (ISCAS). doi 10.4230/LIPIcs.ESEM.2026.47 | **ESEM 2026** (LIPIcs) | unstated | H | OpenCode 82.9 / 87.1 / 65.2% (Claude 4.5 Sonnet / GPT-5 / DeepSeek-V3.2) vs Claude Code 83.8 / 89.5 / 67.1, OpenHands 81.4 / 87.6 / 63.8; lowest cost per task for each model |
| C8 | Workspace Topology as an Attack Vector (Capital One). arXiv 2608.14876 | **CAMLIS 2026** (accepted, per the preprint) (D5) | **opencode 1.14.46**; gpt-oss-120b | S | Compliance with injected instruction 41% → 21% from low to high modularity; low/high ASR intervals separated |
| C9 | SWE-RPG (SMU, Monash Malaysia, DGIST, CUHK…). arXiv 2608.09072 | Preprint | unstated | H | Highest harness average 33.0%; OpenCode + Kimi-K3 49.7% (strongest pairing); overall average 31.5% |
| C10 | "What Does a Harness Buy?" (Shandong Univ.). arXiv 2610.04433 | Preprint | **1.18.25–1.18.31**; Qwen3.8-27B | H | Most differences within noise; OpenCode trails by up to 9 pts on 447 tasks, ~half from output cap |
| C11 | "Beyond the Model" (NJUST, TUM, NJU). arXiv 2609.32459 | Preprint | unstated | H | Gap vs mini-SWE-agent narrows to 2.67 pp with stronger Qwen; DeepSeek-V4-Pro 34.3 vs 33.7 |
| C12 | "A Jagged Frontier" (CSU, Microsoft, UIUC, CMU). arXiv 2608.18389 | Preprint. Microsoft co-author; Copilot not compared (disclosed) | **v1.18.4** | H | −1.88 (Verified) / −3.65 (Pro) under perturbation; 81.20% unperturbed Verified; Qwen most brittle under OpenCode (5.5) |
| C13 | Hearsay (NTU, NUS, CWRU). arXiv 2609.32495 | Preprint | unstated | H | Record corroborated 77.0%; 390/390 tool calls reconciled |
| C14 | SWE-Nexus (NUS, Shanghai AI Lab, Tsinghua, independents). arXiv 2610.20038 | Preprint. Shares authors with C15 (D7) | unstated | H | Max 29.7% (Opus 4.8) vs Claude Code 37.8% |
| C15 | ANCHOR (SUSTech, NJU, NUS, Beihang, Michigan, independents). arXiv 2610.16859 | Preprint. Shares authors with C14 (D7) | unstated | H | GPT-5.4-Mini IPR 58.5% in OpenCode vs 30.8% in Cline |
| C16 | "Identical Runs, Different Results" (CEU; Epoch). arXiv 2609.33812 | Preprint | **1.18.30** | H | Run-to-run variation exceeds between-agent differences; one OpenCode/GLM-5.3 run built a train/eval-row classifier (borderline rule-breaking) |
| C17 | StaminaBench (AWS Agentic AI). arXiv 2606.19613 | Preprint. AWS authors; no AWS agent compared (disclosed) | unstated | H | OpenCode strongest or tied for 6/7 models; Qwen Code significantly worse than OpenCode on Qwen models |
| C18 | PERFOPT-Bench (OPPO, Arizona, CityU). arXiv 2607.07744 | Preprint | **v1.14.31** | H | OC+GPT-5.5: 4 wins, 9.2× (Codex+GPT-5.5: 4, 8.2×); OC+Opus 4.7 2.5 wins vs Claude Code 1.5; shortcut exploitation found in audits |
| C19 | RepoMod-Bench (Modelcode AI). arXiv 2602.22518 | Preprint. Company in code modernization; own product not compared (disclosed) | **v1.1.4** | H | GPT-5.2 43.0%, Opus 4.5 42.0% vs Claude Code 48.2%, Codex CLI 30.4%; per-repo 0.5%–99.5% by model |
| C20 | MobileCybench (Stanford, Berkeley). arXiv 2609.23980 | Preprint | unstated | H/F | OC + GPT-5.6-Sol: 53.8% (malicious app) / 16.7% (remote) probe trigger, highest of 5 configurations |
| C21 | BioXArena (MBZUAI, UCAS, CMU). arXiv 2605.15766 | Preprint | unstated | H | GPT-5.6-Sol: 68.69 vs Codex 68.67, minimal 65.35; Opus 4.6: 60.38 vs Claude Code 64.55 |
| C22 | Timeline-Bench (TensorTest / Ritivel Labs). arXiv 2609.35143 | Preprint. Benchmark company; no own agent compared | **1.18.31** | H | GPT-6 Astra: 21.4% in OpenCode = Codex CLI; ±11 pt CIs |
| C23 | "Can Agents Trust Their Skills?" (CAS IIE, WPI). arXiv 2609.39065 | Preprint | **1.17.18** (8a03fc265b6d) | S | 17 confirmed vulnerabilities (2nd of 11 agents), 42.78 min to earliest exposure; 0/17 with permission-skipping removed and Bash/Edit = ask |
| C24 | Package Hallucination Attacks (Duke). arXiv 2610.09264 | Preprint | unstated | S | Qwen3-Coder-30B SASR 15.85–84.78% vs OpenHands 81.82–98.72%; DeepSeek-V4-Flash 75.32–93.94%; authors note "noticeably lower SASR" |
| C25 | When Context Gets Root (Nanjing Univ., Honor). arXiv 2608.27299 | Preprint | **1.18.1**; DeepSeek-V4-Pro | S | Full access: ~1.38 attempts to success; one installation objective 100%; persistent goals used a third-party plugin |
| C26 | Trust the Brand, Lose Control (CityU HK, Fudan…). arXiv 2609.32635 | Preprint | **1.18.13** | S | Lowest OpenCode configuration (GPT-5.6-Sol) still 48.6% CAR |
| C27 | HarnessSafe (BUPT, China Telecom, BAAI). arXiv 2608.06984 | Preprint (AAAI-style template; status unknown → false) | **1.18.4**; Qwen 3.7 Plus | S | CSS 48.4, 5th of 7 (43.3–62.3); ASR 10.08% |
| C28 | "What's in Your Agent's Context?" (UIUC). arXiv 2609.01222 | Preprint (also counted for Cline) | **1.4.3** | S | 25 context sources; 246 escalation paths; 204 (83%) / 197 (80%) confirmed with GPT-5.4 mini / GPT-5.5; AGENTS.md enters at system level |

Peer-reviewed: C1–C8. Versions stated: C1, C2, C3 (ambiguous), C4, C8, C10, C12, C16, C18, C19, C22, C23, C25, C26, C27, C28 = 16.

## Other sources (listed, not counted) — 19
| # | Source | Why other |
|---|---|---|
| O1 | GHSA-vxw4-wv6m-9hhh / CVE-2026-22812 advisory | Security record (D4) |
| O2 | cy.md/opencode-rce (CyberShadow) | Reporter's disclosure and timeline (D4) |
| O3 | GHSA-c83v-7274-4vgp / CVE-2026-22813 advisory | Security record |
| O4 | GHSA-632h-h47v-g4x4 advisory | Security record (no CVE) |
| O5 | Datadog Security Labs post, 24 Sep 2026 | Reporter's write-up |
| O6, O7 | NVD CVE-2026-22812, CVE-2026-22813 | Records |
| O8 | VentureBeat, 9 Jan 2026 | ToS dispute reporting (Anthropic is a competitor; attribution to VentureBeat) |
| O9 | anomalyco/opencode#6930 | Ban report; maintainer's "anthropic legal demanded…" comment |
| O10 | opencode-ai/opencode (archived Go repo) | Name-collision context |
| O11 | Charm "Crush, Welcome Home" | Name-collision context |
| O12 | anomalyco/opencode#333 | Naming dispute |
| O13 | "Don't Blame the LLM" (Queen's), arXiv 2607.03691 | Repository mining for OpenCode; controlled tests were on Qwen Code. ACM TOSEM template, acceptance not confirmed |
| O14 | Denylist fragility, arXiv 2606.15549 | Counts OpenCode denylists; no OpenCode result |
| O15 | CORAL, arXiv 2604.01658 (COLM 2026) | OpenCode as a component (0042) |
| O16 | HealthFlow, npj Digit. Med. | OpenCode as a component (0042) |
| O17 | Beware of Agentic Botnets, arXiv 2607.07433 | Tests oh-my-opencode plugin, not OpenCode |
| O18 | Inside the Scaffold, arXiv 2604.03515 | Source-code taxonomy |
| O19 | Harness Engineering, arXiv 2609.00006 | Source-code study |

0079: other = 19 + 0 anecdotal = 19.

## Not counted
**Competitor (3):**
- ProcCtrlBench (Amap, Alibaba Group), arXiv 2605.20251: compares Qoder (Alibaba) with OpenCode (0080/0083).
- DeepDiscovery, arXiv 2606.22906: authors' Qoder-based system vs OpenCode.
- MTAC-IFBench (Tsinghua, **Zhipu AI**), arXiv 2609.14992: Zhipu's GLM models are compared; GLM-5.2 CSR 80.4% under Claude Code vs 76.8% under OpenCode v1.1.21 (D6).

**Vendor (2):** opencode.ai docs; anomalyco/opencode repository.

**Further candidates found but not reviewed for counting (not listed on the page):** On the Clock (AWS, 2610.10833, OpenCode 1.17.4), Learn2Play Bench (NUS, 2610.08215, fixed OpenCode harness), AstroAgentBench (Fudan, 2601.11354, v1.14.19), The Scaffold Effect (2607.22585), AlphaDiana (2610.20675, v1.3.2), GameLogicBench (2609.21562, 1.17.18), LongHarness (2609.38137, 1.18.21), OmicsBench (2610.21074, 1.18.11), EvoCowork (2610.14828, 1.4.14), Power Systems Agent Benchmark (2606.20950, 1.15.13), Automating Computational Reproducibility (WWW 2026 Companion, doi 10.1145/3774905.3795485), Tracking Capabilities (2603.00991), ActBench (2608.09476), Breaking/Stale/Missing (2605.06125), Mingbird (2610.02001, OpenCode as baseline), AgenticVBench (2605.27705). Adding them would raise the count but not change the grade.

**Not listed:** related-work mentions; model-only results; studies of Crush or the Go project.

## Shared-author check (0031)
- **Developer set:** Anomaly/SST staff (thdxr, adamdotdevin, rekram1-node and others). No counted or listed paper has an Anomaly author.
- **Companies among counted authors** (disclosed in notes; their own coding product is not compared): Huawei (C3), Capital One (C8), Microsoft (C12; Copilot not compared), AWS (C17), OPPO (C18), Modelcode AI (C19), Xiaohongshu (C2), TensorTest (C22), Honor (C25), China Telecom (C27).
- **Shared authors between counted studies:** C14/C15 (Yu, Xu, Li, Fan, Wu, Zhu) — counted separately as distinct studies (D7).

## Disputes, incidents and security (status 21 Oct 2026)
**CVE-2026-22812 / GHSA-vxw4-wv6m-9hhh** — high, CVSS 3.1 8.8 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H); CWE-306/749/942. NVD: Analyzed.
- **What:** `opencode` started an unauthenticated HTTP server with permissive CORS, so any website could run shell commands.
- **Affected / fix:** opencode-ai < 1.0.216; fixed in **1.0.216** (commit 7d2d87fa, 30 Dec 2025). From **1.1.10** (9 Jan 2026, commit 982b71e) the server is opt-in.
- **Reporter:** GitHub user **CyberShadow** (cy.md). Advisory published by thdxr on 12 Jan 2026 (GitHub global advisory 13 Jan 2026 UTC).
- **Timeline (reporter's account):** 17 Nov 2025 email to support@sst.dev, no reply → 27 Dec 2025 GHSA filed → 29 Dec public issue #6355 (by another user) → 30 Dec v1.0.216 → 7 Jan 2026 Discord, no reply → 8 Jan comment → 9 Jan thdxr: "hey sorry this got dropped over the holidays", server no longer started by default → 11 Jan public post (HN 46581095, 432 points).
- **Still open per reporter at disclosure (12 Jan 2026):** an enabled server remained unauthenticated; *.opencode.ai allowed as CORS origin; --mdns binds 0.0.0.0. (Datadog later notes an OPENCODE_SERVER_PASSWORD option.) Reporter discloses help from an AI model.

**CVE-2026-22813 / GHSA-c83v-7274-4vgp** — critical (CNA CVSS 4.0 9.4); NVD's own score 6.1; CWE-79.
- **What:** XSS in the web UI via the `?url=` override → /pty command execution.
- **Affected / fix:** < 1.1.10; fixed in **1.1.10** (web UI/API off by default). Hosted `?url=` override disabled 9 Jan 2026 21:36 GMT.
- **Reporter:** GitHub user **AlbertSPedersen**. Published by thdxr 12 Jan 2026.

**GHSA-632h-h47v-g4x4** — high, CVSS 3.1 7.5 (AV:N/AC:H/PR:N/UI:R…). **No CVE.**
- **What:** with `opencode serve` running, /global/upgrade accepted a text/plain body parsed as JSON with an arbitrary npm spec → attacker package installed via npm/pnpm/Bun.
- **Affected / fix:** introduced in **1.14.30** (PR #24853, 29 Apr 2026); fixed in **1.18.22** (PR #44686, commit c6e76e9, 24 Aug 2026). Last affected version: advisory text "I believe v1.14.30 through v1.18.16"; Datadog 1.18.21; the advisory's patched field 1.18.22. The page uses "1.14.30 to 1.18.21" (fix-version based).
- **Reporter:** Christophe Tafani-Dereeper (**Datadog Security Labs**). Published by rekram1-node, 24 Sep 2026.
- **Timeline:** reported 11 Aug 2026 → fixed 24 Aug (13 days) → publication delayed one month at Anomaly's request → 24 Sep publication.
- **Vendor response (per Datadog):** thanked Anomaly for "continuous open communication and for quickly patching"; "Anomaly chose not to request a CVE", believing CVEs incentivize low-quality reports. Datadog counted >647,000 npm downloads of the 82 vulnerable versions in 17–23 Sep 2026 (38.9%).

**Anthropic terms-of-service dispute (Jan–Feb 2026).** Anthropic blocked Claude Pro/Max OAuth use in third-party harnesses including OpenCode (VentureBeat, 9 Jan 2026; VentureBeat describes the harnesses as spoofing the Claude Code client — attributed to VentureBeat, Anthropic being a competitor). #6930: a user's ban report; on 19 Feb 2026 thdxr wrote "anthropic legal demanded we respond to this issue and close it". PR #10595 (26 Jan 2026) added a docs note that Pro/Max is not officially supported. Weighed lightly (D8).

**Naming dispute (2025):** #333; ended with the Go project renamed Crush. Context only.

**Legal / regulatory:** none found.

## Precedents applied
- **0031:** vendor material not counted; no Anomaly-authored study found.
- **0039:** model-only results are context.
- **0040 D3:** each study counts once.
- **0042:** systems built on OpenCode (CORAL, HealthFlow) are other.
- **0051 / 0084 D7a:** A needs a stated version within 12 months (met; D3).
- **0059 / CAP:** company affiliations disclosed.
- **0071:** documented tests count.
- **0076:** unconfirmed venues → peer_reviewed false (HarnessSafe, Don't Blame).
- **0079:** other = other + anecdotal.
- **0080 / 0083:** competitor sources listed, not counted (D6).
- **0085 / 0087 D3a:** fixed-harness benchmarks and security studies of the unmodified agent count (as for OpenHands, SWE-agent, mini-SWE-agent, Cline).
- **0010:** half-up rounding. **0065:** feed item. **0075:** title ≤68. **0090 D1:** caveat names every coding entry (D11).

## Score (Scoring rules v0.1)
| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion rate | 30 | 50 | **Mixed, model-dependent.** Level with or above other harnesses with the same model in C7, C9, C17, C18, C21, C22, C4; below in C2 (2% vs 12%), C10 (−9), C14 (29.7 vs 37.8), C19 (43 vs 48.2). Small/incompatible models: 10–17% (C1), 8.4% (C3). Same as Cline (50), Claude Code (50), OpenHands (50) |
| Disputes | 20 | 40 | Three advisories in 2026 (one critical by CNA, two high); slow initial response to the first (≈7 weeks without reply); gaps left at disclosure; third fixed in 13 days with praise from the reporter but no CVE requested; Anthropic ToS conflict incl. a legal demand; naming dispute. Below Cline (45) because of the slow initial response and the no-CVE choice |
| Adherence to limits | 25 | 40 | Attack studies (C8, C23–C28) show high success with confirmations off; permission "ask" for Bash/Edit stopped all 17 skill exploits (C23); lower package-hallucination success than peers (C24); no runtime sandbox (O13); task workarounds (C4, C16). Same as Cline/Claude Code (40) |
| Evidence quality | 25 | 85 | 28 counted, 8 peer-reviewed, 16 versioned, many same-model comparisons; limits: preprint-heavy, one ambiguous version, model heterogeneity, high release cadence. Same as Cline (85) |

0.30×50 + 0.20×40 + 0.25×40 + 0.25×85 = 15 + 8 + 10 + 21.25 = 54.25 → **54**.

**Grade A:** 28 counted (≥7), 8 peer-reviewed (≥3), stated versions within 12 months in four peer-reviewed tests (C1 v1.4.0 Apr 2026, C2 v1.1.44 Jan–Feb 2026, C4 v1.15.12 May 2026, C8 1.14.46) and many preprints (to 1.18.31, Sep 2026). **Not borderline** (D3).

**Fragility (counting decisions):**
| Variant | Counted | Peer-reviewed | Grade |
|---|---|---|---|
| Recommended | 28 | 8 | **A / 54** |
| D3 strict: require v1.19.x ("current version") | 28 | 8 | **B** (no v1.19 test), evidence ~80 → 53 |
| D2b: drop C1 and C3 (Go-repo URL / v0.0.55) | 26 | 6 | A |
| D5b: C8 not peer-reviewed | 28 | 7 | A |
| Drop all 4 versioned peer-reviewed (C1, C2, C4, C8) | 24 | 4 | B (no versioned peer-reviewed test) — needs 4 independent reversals |
| D6b: count MTAC-IFBench | 29 | 8 | A |
| D7b: merge C14/C15 | 27 | 8 | A |
| D9b: security studies as other | 21 | 7 | A |

Grade A survives every single reversal except the strict "v1.19.x" reading of "current version" (which the 0084 D7a precedent does not require; Cline is A without a v4.x test).

**Score range (recommended counting):**
| Change | Overall |
|---|---|
| As proposed | 54 (54.25) |
| Completion 45 / 55 | 53 (52.75) / 56 (55.75) |
| Disputes 35 / 45 | 53 (53.25) / 55 (55.25) |
| Adherence 35 / 45 | 53 (53.0) / 56 (55.5) |
| Evidence 80 / 90 | 53 (53.0) / 56 (55.5) |

Plausible range 53–56.

**Index position:** after FacTool (open-source) (55) and before Perplexity (54) — "OpenCode" sorts before "Perplexity" by name. Confirmed in the dry run.

## Risks and uncertainties
1. **Model dependence** (D10). Every result is OpenCode + a model + settings; no two studies share a configuration. Same-model comparisons point both ways.
2. **Name collision** (D2). Mis-cited repository URLs; one peer-reviewed study with an ambiguous v0.0.55.
3. **Version churn.** ~2.6 releases/day; no counted v1.19 test; security-relevant behaviour (server defaults, permissions) changed across versions.
4. **Attack studies with confirmations off.** They show exposure in permissive modes, not default-mode rates. C23 shows "ask" permissions closing the tested exploits.
5. **Preprint weight.** 20 of 28 counted are preprints (2026).
6. **CVE wording.** NVD and CNA scores differ for CVE-2026-22813 (6.1 vs 9.4); the page gives both. GHSA-632h has no CVE; affected range sources differ slightly (1.18.16 vs 1.18.21).
7. **ToS dispute.** Reported via VentureBeat and GitHub issues; Anthropic is a competitor; weighed lightly.
8. **Search gaps** (banner). More OpenCode studies exist than were reviewed.

## Decisions (D1–D11, D13, D14 approved 2026-10-21, 10:52 AM ET, as recommended; D12 not applied; D15–D16 not approved)
- **D1 Scope.**
  - (a) **Recommended.** One entry for anomalyco/opencode (formerly sst/opencode), all clients and `opencode serve`, 2025 releases to v1.19.3, any user-chosen model. Exclude the Go project/Crush, systems built on OpenCode, third-party plugins (oh-my-opencode), model-only results.
  - (b) Only v1.x (Oct 2025 on) — same counts (all counted tests are 2026), except C3's ambiguous v0.0.55.
- **D2 Name collision — per-source attribution.**
  - C1 (To Run): cites github.com/opencode-ai/opencode but states v1.4.0, accessed 9 Apr 2026; only anomalyco has 1.4.0 (8 Apr 2026) → **anomalyco tested; count.**
  - C3 (DCAS): cites anomalyco (accessed Apr 2026) and describes OpenCode's Plan agent (a TS-era feature) but states "v0.0.55", a tag in both repos → (a) **Recommended:** count as anomalyco with version_tested "stated as v0.0.55 (ambiguous)"; (b) drop C3 (26/7 if combined with dropping C1: still A).
  - Other counted sources cite anomalyco/sst or opencode.ai, or state 1.x versions — unambiguous.
  - Papers citing opencode-ai/opencode that are not counted (2605.06125, 2606.24446, 2604.03088, 2606.18425, 2608.25593, 2610.05281, 2606.28480, 2606.04484, 2609.19203): not reviewed; recheck later. 2605.06717 (Google) mentions Crush.
  - **Page wording:** a "Which OpenCode" section (drafted).
- **D3 Grade A.**
  - (a) **Recommended. A**: ≥3 peer-reviewed (8) and versioned tests within 12 months (C1, C2, C4, C8 all 2026). Follows 0084 D7a (stated version within 12 months; Cline A without v4.x test). Grade note states "No counted test states a v1.19 version."
  - (b) Strict reading (current v1.19.x only) → B, evidence 80, overall 53.
- **D4 Security advisories — wording and weighting.**
  - (a) **Recommended.** Name each with reporter, severity (both scores for CVE-2026-22813), affected range, fix version and dates; quote the vendor reply ("dropped over the holidays") and Datadog's thanks; state "Anomaly chose not to request a CVE" attributed to Datadog; use 1.14.30–1.18.21 for GHSA-632h with the variation noted in the YAML note. Weighed in disputes (40).
  - (b) Shorter: list IDs and fix versions only.
- **D5 Workspace Topology (CAMLIS).**
  - (a) **Recommended.** peer_reviewed true (accepted at CAMLIS 2026, per the authors).
  - (b) false → 7 peer-reviewed; still A.
- **D6 MTAC-IFBench (Zhipu AI).**
  - (a) **Recommended.** Competitor: the authors' own product (Zhipu's GLM models) is in the comparison, and the OpenCode result is a GLM-in-OpenCode vs GLM-in-Claude-Code comparison — listed, not counted (0080/0083 applied to the authors' own model).
  - (b) Count with disclosure (29 counted). No grade change.
- **D7 Shared authors C14/C15.** (a) **Recommended.** Count separately (different benchmarks, data and questions). (b) Merge → 27.
- **D8 Anthropic ToS dispute.** (a) **Recommended.** Mention under disputes, attributed; weigh lightly (it concerns a third party's terms, not OpenCode's conduct toward its users). (b) Omit.
- **D9 Counting rule for attack studies (0087 D3a).** (a) **Recommended.** Count (as for Cline). (b) Other → 21 counted / 7 peer-reviewed; still A; adherence evidence thinner.
- **D10 Model dependence — page wording.**
  - (a) **Recommended.** A "Model dependence" section: every result is OpenCode with a particular model; with the same model, studies found it level with or above some harnesses and below others; results fell sharply with small or poorly matched models (8.4% example); results for one model do not carry over. Plus the first uncertainty line "Results reflect the model and the harness together".
  - (b) Uncertainty line only (as Cline).
- **D11 Required caveat edit.** Add "OpenCode" to the open-source list in coding-agents caveat 1 (scripts/build_data.py): "Open-source frameworks (OpenHands, SWE-agent, mini-SWE-agent, Aider, Cline, OpenCode) are run with a language model chosen by the user…". **Required** for check_all (0090 D1). Applied only in the scratch dry run.
- **D12 Cross-references (NOT applied; candidates only).**
  - (a) C7 (ESEM, Claude Code / OpenHands / OpenCode) is not on the Claude Code or OpenHands pages.
  - (b) C10, C11, C12, C17 compare mini-SWE-agent/OpenHands/Claude Code/Codex with OpenCode; check those pages at next review.
  - (c) C15 ANCHOR and C28 compare Cline; C28 is already counted for Cline.
  - (d) C2 SWE-Bench Mobile (Cursor), C18 PERFOPT and C19 RepoMod (Codex, Claude Code), C21 BioXArena (Codex, Claude Code), C22 Timeline-Bench (Codex, Claude Code).
  - (e) MTAC-IFBench and ProcCtrlBench for Claude Code / Codex (for those entries the competitor question differs).
  - No score changes are proposed for other entries.
- **D13 Name and title.** (a) **Recommended.** "OpenCode (open-source)", slug opencode, Coding agent; title "OpenCode (open-source) — Agent Reputation & Trust Clearinghouse" (≤68; checked in dry run). Homepage link to the repository. (b) "OpenCode (Anomaly)".
- **D14 Score.** 54 / A (50 / 40 / 40 / 85). Range 53–56.
- **D15 (later, not requested)** commit/push. **D16 (later, not requested)** deploy.

**Recommendation (APPROVED 2026-10-21, 10:52 AM ET):** D1a, D2 as attributed (C3 a), D3a, D4a, D5a, D6a, D7a, D8a, D9a, D10a, D11, D13a, D14 (54 / A), banner. D12 left for those entries' next reviews.

## Link check (21 Oct 2026, ~12:50 AM ET; dryrun/link-check.txt)
54 external links on the draft page: 47 return 200.
- **4 × 403, ACM DOIs** (10.1145/3832113, 3770855.3818488, 3832783.3834485, 3832783.3834388): ACM's Cloudflare bot challenge. All four DOIs checked in Crossref (titles and venues match: PACMSE/ISSTA, KDD 2026, ASE 2026 ×2). Kept.
- **1 × 429, VentureBeat article:** Vercel bot challenge from the box; the article loaded via the fetch service (Carl Franzen, 9 Jan 2026, 3:14 PM PT). Kept.
- **2 × 404 expected:** the entry page (until deployed) and the decision record on GitHub (until pushed).
- The two ESEM DOIs resolve to Dagstuhl DROPS (302 → 200).

## Link recheck after approval (21 Oct 2026, ~11 AM ET)
- **ACM DOIs — all valid, kept.** doi.org answers 302 to dl.acm.org for each; ACM answers automated requests with a Cloudflare challenge (403), which is a bot block, not a dead link. Crossref metadata matches each source:
  - 10.1145/3832113 — "To Run or Not to Run…", Proceedings of the ACM on Software Engineering (ISSTA 2026); Lin, Zhu, Zhou, Wang… Open copy arXiv 2606.26978 (200).
  - 10.1145/3770855.3818488 — "SWE-Bench Mobile…", KDD 2026 Proceedings V.2; Tian, Wang, Tang, Yang… Open copy arXiv 2602.09540 (200).
  - 10.1145/3832783.3834485 — "DCAS…", ASE 2026; Thangarajah, Chen, Hassan. Open copy arXiv 2608.06113 (200).
  - 10.1145/3832783.3834388 — "From Runnable Code to Shippable Applications…", ASE 2026; Wan, Liang, Xu, Xiao… (CUHK, Columbia, SMU). Open copy arXiv 2605.17242 (200).
- **VentureBeat — valid, kept.** The box gets 429 (Vercel bot challenge); the fetch tool loaded the article in full (Carl Franzen, 3:14 PM PT, 9 Jan 2026; text matches the note).
- **cy.md/opencode-rce (reporter's CVE-2026-22812 disclosure) — failing; swapped to the archived copy at commit (W1, 11:25 AM ET).** It returned 200 at ~12:50 AM ET, then 500 (nginx) and timeouts from ~10:55 AM ET, from both the box and the fetch tool; the home page also timed out. That looks like a site outage rather than a removed page. The Wayback Machine has snapshots from 11 Jan to 3 Feb 2026; https://web.archive.org/web/20260203132057/https://cy.md/opencode-rce/ loads via the fetch tool and matches the note (timeline, remaining gaps, AI-assistance statement). The original link is kept; if it still fails at commit time, swap in this archived copy.
- The maintainer's reply quoted on the page was rechecked on issue #6355: thdxr, 9 Jan 2026, 5:58 PM ET: "hey sorry this got dropped over the holidays … we've made a change recently not to start the server by default, it's opted into". A later maintainer comment (12 Jan 2026) is not on the page (W2).
- **No other dead links.** Full results: final/link-check.txt.

## Private dry run before approval (scratch clones of 133d73a; real tree untouched)
Script: run_dryrun.sh → dryrun/. Real repo before and after: HEAD 133d73a, 0 changed files.
- **Base rebuild drift:** none (rebuilding the unmodified clone changes nothing).
- **Page-only build** (dryrun/page): check_all fails by design (no feed item, 0065; llms-full as-of date), as for 0092.
- **Full build** (dryrun/scratch): check_all **0 errors**; check_scores "OK opencode: overall 54 (computed 54), grade A, counted 28, peer-reviewed 8"; 0 errors, 0 warnings, 6 documented.
- **final_checks.py: 0 failures**. Totals base 41 / 30 scored + 11 insufficient / 77 changelog rows / 91 feed items / sitemap 49 → scratch **42 / 31 + 11 / 78 / 92 / 50**. Other 41 entries' agents.json records byte-identical; zero score/grade/source-count diffs; other entry pages unchanged; feed ids unchanged apart from the new item; index order FacTool → OpenCode → Perplexity; llms.txt line in place; sitemap; D11 caveat text on the coding-agents comparison; title 63 characters; required phrases present; no banned words outside the standard disclaimer (page, YAML, changelog row).
- **Patch:** dryrun/draft-0093.patch, 19 files (entry YAML, decision record, entry page, changelog row, feeds, index, llms files, sitemap, data exports, coding-agents comparison, D11 caveat in scripts/build_data.py; plus as-of date lines on agents-data, changelog, citing and two comparison pages).
- Preview: dryrun/opencode.preview.html. Changelog row: draft-changelog-row.yaml. Feed item: feed-item.txt.

## Final private patch (scratch clone of 133d73a; real tree untouched)
final/final-0093.patch, built by finalize.sh with the approved YAML (decision: APPROVED) and this record. Checks: final/check_all-scratch.txt, final/check_scores-scratch.txt, final/final-checks.txt, final/apply-check.txt (a fresh clone with the patch applied matches the build, and rebuilding it changes nothing). Deploy manifest /workspace/manifest-0093 and verify script /workspace/verify-0093/v93.py prepared; not deployed (rollback target dpl_7VVVFhGqgcajXeQ9GUHTg3ggLcVe, current live 0092). If the commit happens on a later date, rebuild the patch and manifest (as-of dates change).

## Minimum viable version
Approve D1a, D2 (count C1; C3 as ambiguous), D3a, D4a, D11 and D14 (54 / A) with the banner, the "Which OpenCode" and "Model dependence" sections as drafted. Everything else can stay as recommended. Alternative minimum: if the ambiguous-version or strict-current-version concerns weigh more, publish as **B / 53** (D3b) with the same text.

## Plain-English terms
- **OpenCode:** a free, open-source program that lets an AI model work on code from your terminal; you pick which AI model it uses.
- **Harness:** the program around an AI model that gives it tools (read files, run commands) and decides what it sees.
- **Same-model comparison:** testing different harnesses with the same AI model, so differences come from the harness.
- **Name collision:** two different projects were both called OpenCode; the older one is now called Crush.
- **CVE / GitHub security advisory (GHSA):** public identifiers for a security flaw.
- **CVSS:** a 0–10 severity score for security flaws; different bodies can give different scores.
- **CORS / local server:** settings that decide whether websites in your browser can talk to a program running on your computer.
- **Cross-site scripting (XSS):** a flaw that lets a malicious link run code inside a web page.
- **Prompt injection:** planted text that makes an AI follow someone else's instructions.
- **Confirmations off / full access:** the agent runs commands without asking the user first.
- **Peer-reviewed:** checked by independent experts before publication at a conference or journal.

---
*Informational only. This is a private draft summarizing cited public evidence under published rules; it is not a guarantee, endorsement, certification or ranking of quality, and nothing here has been published.*
