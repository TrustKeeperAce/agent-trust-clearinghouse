# Decision 0088: Magentic-One — 50 / B

**Status: D1–D10 APPROVED by Remington, 2026-10-20 (4:41 PM ET), exactly as drafted: D1a scope (AutoGen Magentic-One with its own agents, magentic-one-cli and the Nov 2024 package; Magentic-UI, the Microsoft Agent Framework Magentic orchestration and AutoGen Studio out of scope); D2a orchestrator-only setups as other; D3a Microsoft-affiliated papers excluded; D4a Who&When and Who&When Pro excluded; D5a 0.7.5 treated as the current version, with the archive notice stated; D6a Browser/web agent; D7a name 'Magentic-One (open-source)'; D8 50 / B (40 / 60 / 30 / 75, disputes 60); D9 disputes wording; D10 'Citation check incomplete — recheck later' banner. D13 cross-references are NOT approved and not applied (left for those entries' next reviews). D11 (Magentic-One page, changelog row with two wording fixes — the not-counted sentence reads 'Material from the Magentic-One and AutoGen teams and from Microsoft-affiliated authors, orchestrator-only setups, Magentic-UI and the Agent Framework re-implementation are not counted.' and the archive sentence reads 'No CVE was found; since October 2026 the developer's AutoGen page says the project is archived and no longer receives bug or security fixes.' — with the page's archive wording aligned to the README notice; commit and push) APPROVED by Remington, 2026-10-20 (4:56 PM ET). D12 (deploy) is NOT approved: nothing is deployed.**

Batch 5 candidate 2. Research done on 20 Oct 2026 (ET). The packet follows the 0087 (Cline) structure. All new URLs use https://www.agentclearinghouse.org. The entry YAML carries `decision: APPROVED` (D1–D10 approved 2026-10-20).

**Citation check incomplete — recheck later.**
- OpenAlex full text was the main search: 4 queries ("Magentic-One", "MagenticOne", "MagenticOneGroupChat", and "Magentic-One" with Orchestrator/WebSurfer) matched 284 works, and 244 PDFs were downloaded (/tmp/p88).
- Semantic Scholar returned an error (rate limit) and the arXiv API timed out. Three key papers not in the OpenAlex set (arXiv 2503.12188, 2503.13657, 2505.00212) were fetched directly from arXiv.
- The counted set is a sample of the studies found, not an exhaustive list.

## What happened
1. **Scope set** (see D1). The entry covers Magentic-One as Microsoft released it in AutoGen:
   - Technical report arXiv 2411.04468 (Fourney et al., Microsoft Research AI Frontiers, 4 Nov 2024). The first package, `autogen-magentic-one`, was followed by the AgentChat implementation.
   - `MagenticOneGroupChat` with the Orchestrator, MultimodalWebSurfer, FileSurfer, Coder (MagenticOneCoderAgent) and ComputerTerminal agents in `autogen-agentchat` / `autogen-ext` 0.4–0.7.5. The **latest release is 0.7.5 (30 Sep 2025, 2:16 AM ET)**, and it is still the latest on PyPI on 20 Oct 2026. Also covered: `magentic-one-cli` 0.2.4 (3 Apr 2025).
   - GitHub microsoft/autogen: CC-BY-4.0 (docs) / MIT (code), last push 16 Oct 2026 (GitHub API, 20 Oct 2026). 9 commits on main after the python-v0.7.5 tag.
   - **Separate products, not counted here:** Magentic-UI (a reserve candidate), the Magentic orchestration in Microsoft Agent Framework (a re-implementation), and AutoGen Studio (context under disputes only).
2. **Search.**
   - OpenAlex full text (284 works, 244 downloaded), then screening of every download for Magentic-One as a tested system. This separated runs of Magentic-One from citations, from re-analyses of others' traces, from orchestrator-only adaptations and from Magentic-UI. About 40 papers were read in the relevant sections. The figures quoted below were rechecked against the extracted text.
   - Also checked: PyPI JSON (autogen-agentchat, autogen-ext, autogen-core, magentic-one-cli), GitHub (README, releases, compare, pull requests, repository security advisories), the GitHub global advisory database (pip: autogen-agentchat, autogen-ext, autogen-core, magentic-one-cli), NVD keyword searches ("autogen", "magentic"), the Microsoft Agent Framework docs, the GAIA leaderboard dataset, and web reports.
3. **Results.**
   - **6 counted** independent performance sources, **4 peer-reviewed**. One counted test states the current version.
   - **13 other.** 5 vendor or maintainer sources and 6 excluded sources are not counted.
4. **Developer-authored material:** the technical report and Microsoft's GAIA, AssistantBench and WebArena numbers are excluded (0031). The GAIA leaderboard rows were submitted by MSR AI Frontiers and are listed as other.

## Counted: independent performance sources (6; peer-reviewed 4)
All accessed 2026-10-20.

| # | Source | Peer review | Version / test date | Result (exact quote where given) |
|---|---|---|---|---|
| C1 | Triedman, Jha, Shmatikov, "Multi-Agent Systems Execute Arbitrary Malicious Code", Cornell Tech. https://arxiv.org/abs/2503.12188 | Yes (COLM 2025) | Unstated; arXiv v1 Mar 2025. "AutoGen multi-agent systems were initialized using the default Magentic-One group chat, with an orchestrator agent, file surfer, web surfer, coder, and code executor" | "the Magentic-One orchestrator, running on GPT-4o, executes arbitrary malicious code 97% of the time if it interacts with a malicious local file. The same orchestrator, running on Gemini 1.5 Pro, executes arbitrary malicious code 88% of the time when it interacts with a malicious web page." Known indirect-injection attacks "have near-zero success rate". Shares 2 authors with C5 |
| C2 | Cemri, Pan, Yang et al., "Why Do Multi-Agent LLM Systems Fail?" (MAST), UC Berkeley and Intesa Sanpaolo. https://arxiv.org/abs/2503.13657 | Yes (NeurIPS 2025 Datasets and Benchmarks) | Unstated; 2025 | Table 1: "Magentic-One GAIA GPT-4o" with 30 human-annotated and 165 LLM-annotated traces. Figure 5: "Magentic-One 38.0% [success] 62.0% [failure] (GAIA)" |
| C3 | Chen, Wang, Mu et al., "Seeing the Whole Elephant" (TraceElephant), Institute of Software, CAS. https://doi.org/10.18653/v1/2026.acl-long.912 (preprint https://arxiv.org/abs/2604.22708) | Yes (ACL 2026 long) | Unstated; temperature 0.3; 2025–2026 | Table 1: Magentic-One GAIA 119 traces / 74 failed; AssistantBench 30 / 17 failed. "Agents responsible for interacting with external environments or performing concrete operations are most prone to errors (almost over 50% of the failures)". The tasks were chosen to build a failure-attribution benchmark, so the failure share is not a benchmark score |
| C4 | Xu, Tian, Jiang, "A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems", BUPT. https://proceedings.mlr.press/v306/xu26bb.html (preprint https://arxiv.org/abs/2608.05791, counted once) | Yes (ICML 2026, PMLR 306 pp. 141936–141949; ICML poster 66552) | Unstated; Qwen-Plus; 2026 | "We choose Magentic-One (Fourney et al., 2024) as the baseline"; "accuracy improves from approximately 43% to 52–57% on Level 1 tasks, and from around 26% to up to 39% on Level 2 tasks"; on Level 2 "Magentic-One requires approximately 320s, while parallel configurations reduce this to around 170–280s." Competing method built on the Magentic-One architecture (disclosed) |
| C5 | Jha, Triedman, Bhattacharya, Shmatikov, "Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents", Cornell. https://arxiv.org/abs/2605.19149 | No (preprint, 18 May 2026) | **"Version 0.7.5, accessed via AutoGen on PyPI on 2026-05-02"**: the current release, tested within 12 months | With GPT-5, for medium- and high-severity behaviours: "the planned-to-attempted conversion rates are … 90.9% for Magentic-One", attempted-to-successful "58.6% for Magentic-One", and reporting rate "54.3% for Magentic-One". "Magentic-One contributes the largest share of access-control-related meltdowns: 45.5% of agent privilege escalations (30/66), 76.9% of access-control mutations (10/13), and 37.5% of private content disclosures (39/104)." Shares authors with C1 |
| C6 | Rose, Mallick, Laws, Nita-Rotaru, Oprea, "APWA: A Distributed Architecture for Parallelizable Agentic Workflows", Northeastern. https://arxiv.org/abs/2605.15132 | No (preprint, 14 May 2026) | Unstated; GPT-5.4 / mini / nano; 2026 | "Magentic-One is unable to complete any of the tasks reliably, only managing to produce an output in a single trial for PII-300k with all 4096 documents." The FileSurfer "consumed over 6.5M input tokens, blocking progress until a timeout at 30 minutes." Competing architecture (disclosed) |

## Other sources (listed, not counted) — 13
| # | Source | Why other |
|---|---|---|
| O1 | Repair or Resample? (ECNU, NTU and others; preprint Aug 2026) https://arxiv.org/abs/2608.25920 | "The Magentic-One adapter uses AutoGen AgentChat 0.7.5. Its execution path imports AssistantAgent and MagenticOneGroupChat". This is the orchestrator with general assistant agents, not Magentic-One's own agents. 181 Magentic-One runs were kept as failures. Experiments ran 15–16 Jun 2026 (UTC). **D2** |
| O2 | AgentX (IISc, IBM India Research Lab; preprint Sep 2025) https://arxiv.org/abs/2509.07595 | "we adapt this architecture by replacing the default agents with a new set of agents" (one per MCP server). Adapted configuration (0042). **D2** |
| O3 | Ask Your Advisor (ETH Zurich; preprint 9 Oct 2026) https://arxiv.org/abs/2610.13870 | Magentic-One is the execution framework for the authors' consultation controller on SWE-bench, Terminal-Bench 2.1 and τ2-bench. Adapted per benchmark. **D2** |
| O4 | SentinelAgent (preprint May 2025) https://arxiv.org/abs/2505.24201 | A qualitative case study on Magentic-One; no measured rate |
| O5 | XPerf (UIUC; preprint Jun 2026) https://arxiv.org/abs/2608.20370 | Magentic-One traces used as a serving workload; no task results |
| O6 | GAIA leaderboard results https://huggingface.co/datasets/gaia-benchmark/results_public | "Magentic-1" 0.369697 (GPT-4o) and "Magentic-1 (o1)" 0.460606, organisation "MSR AI Frontiers", 14–15 Oct 2024. Submitted by the developer and scored by the maintainers (0036 caution 3) |
| O7 | The AI Agent Index (Casper et al. 2025) https://arxiv.org/abs/2502.01635 | Documentation card, not a test. "No authors have conflicts of interest related to Microsoft or Magentic One" |
| O8 | Coding Agents with Multimodal Browsing (CMU and others; Findings of EACL 2026) https://doi.org/10.18653/v1/2026.findings-eacl.318 | Lists "Magentic-One … GPT-4o, o1 37.87%" (GAIA), Microsoft's reported figure. Also lists Magentic-UI, which is out of scope |
| O9 | BLADE (UConn; preprint Oct 2026) https://arxiv.org/abs/2610.18780 | Uses Who&When / Who&When Pro Magentic-One traces. Re-analysis (0076) |
| O10 | ReCast (preprint Oct 2026) https://arxiv.org/abs/2610.11334 | Re-analysis of existing Magentic-One traces (0076) |
| O11 | Can Failed Trajectories Reveal Where Agents Go Wrong? (preprint Oct 2026) https://arxiv.org/abs/2610.13105 | Uses "the Magentic-One subset TE-MAG (91 trajectories)" of C3. Re-analysis (0076) |
| O12 | Correctover audit page https://www.correctover.com/audit | Lists "P1-PATH \| Path Traversal \| AutoGen magentic-one-cli \| 9.8 \| MSRC Submitted". Unconfirmed; no CVE or advisory found |
| O13 | BleepingComputer, 22 Jun 2026 https://www.bleepingcomputer.com/news/security/microsoft-fixes-autogen-studio-flaw-that-enabled-code-execution/ | AutoJack in AutoGen Studio: "This issue was identified and remediated before any PyPI release". Outside Magentic-One; context only |

0079: other = 13 (other) + 0 (anecdotal) = 13.

## Not counted
**Vendor or maintainer (5):**
- microsoft/autogen README (archived notice).
- PyPI release metadata.
- PR #7463.
- Microsoft Security Blog on AutoJack (18 Jun 2026).
- Microsoft Agent Framework Magentic orchestration docs: "designed based on the Magentic-One system"; "it is untested how well the Magentic orchestration will perform outside of the original Magentic-One design".

**Excluded (6):**
- **Technical report** (arXiv 2411.04468), including its GAIA, AssistantBench and WebArena numbers (0031).
- **Who&When** (ICML 2025; https://arxiv.org/abs/2505.00212). Co-authors include AutoGen co-creators Chi Wang (Google DeepMind) and Qingyun Wu (Penn State, AG2AI), and Beibin Li, an AutoGen paper co-author. The paper says it used "settings of CaptainAgent and Magentic-One from their official libraries (AG2 and Autogen)". **D4.**
- **Who&When Pro** (arXiv 2607.09996): Chi Wang and Qingyun Wu. **D4.**
- **Breaking and Fixing Defenses Against Control-Flow Hijacking** (ICLR 2026; https://arxiv.org/abs/2510.17276; Cornell and Microsoft, with Justin Wagle at Microsoft). Runs "the popular, open-source, general-purpose Magentic-One configuration". Its Slack attack reached "ASRs of up to 56%" against two defences, and undefended Magentic-One had 65% benign success. **D3.**
- **TAMAS** (ACL 2026; https://doi.org/10.18653/v1/2026.acl-long.1442; IIIT Hyderabad and Microsoft Research India, with Tanuja Ganu). "DPI 81% in Magentic-One"; IPI "average 27.4% in Magentic-One". **D3.**
- **Litmus (Re)Agent** (preprint Apr 2026; https://arxiv.org/abs/2604.08970; first author at Microsoft Corporation India). Magentic-One baseline "2.1% and 3.6%" in two scenarios. **D3.**

**Not listed (no Magentic-One result of its own), with reasons:**
- **Microsoft authors:** AgentRx (Microsoft Research; Magentic-One trajectories from existing sets), EAIR (Microsoft; MAST traces) and LEGOMem (Microsoft; its own system "based on Magentic-One system").
- **Cite Magentic-One only:** Benchmarking Robustness to Adversarially-Induced Harms, KramaBench (smolagents with a Magentic-One text inspector), MaMa, MESA, From Monoliths to Swarms, BRA-Audit, Misleading the Planner (its own AutoGen planner–worker system), Recognize Your Orchestrator, How Strongly Should Task State Influence an LLM Agent?, Right-Sizing (a "Magentic-One-style orchestrator").
- **Re-implementations (0042):**
  - Autonomous Repair via MCTS and Learning to Share build on the Magentic-One team or framework.
  - Can LLM Agents Sustain Long-Horizon Organizational Dynamics? compares a Magentic-One baseline on a data-generation task, with an unclear setup.
  - Beyond the Final Answer (TRACE) applies Magentic-One to GAIA only to show its trajectory evaluator.
  - Agent Context Protocols lists Magentic-One AssistantBench figures, apparently reported results.
- **Magentic-UI papers:** out of scope.
- **PyPI `autogen` CVE-2025-69872** (AIKIDO-2026-10545): concerns the PyPI `autogen` meta-package that pins AG2, a separate fork, not Microsoft's autogen-agentchat. Out of scope.

## Shared-author check (0031)
- **Developer set (technical report):** Adam Fourney, Gagan Bansal, Hussein Mozannar, Cheng Tan, Eduardo Salinas, Erkang (Eric) Zhu, Friederike Niedtner, Grace Proebsting, Griffin Bassman, Jack Gerrits, Jacob Alber, Peter Chang, Ricky Loynd, Robert West, Victor Dibia, Ahmed Awadallah, Ece Kamar, Rafah Hosn and Saleema Amershi. **AutoGen team:** also Chi Wang, Qingyun Wu and Beibin Li (AutoGen paper).
- **Counted sources:** no counted source has a developer, AutoGen-team or Microsoft author or affiliation. Checked:
  - C1, C5: Cornell.
  - C2: Berkeley, Intesa Sanpaolo.
  - C3: CAS.
  - C4: BUPT.
  - C6: Northeastern.
- **AgentRx:** its author Chetan Bansal (Microsoft) is not Gagan Bansal. It is not listed in any case (Microsoft affiliation, re-used traces).
- **C1 and C5** share Jha, Triedman and Shmatikov. They are different studies (adversarial hijacking versus benign-error behaviour), so both are counted, with disclosure. Their ICLR 2026 paper with a Microsoft co-author is excluded (D3).

## Repository maintenance, disputes and security
Status is as of 20 Oct 2026.

- **No CVE and no GitHub advisory** for Magentic-One, autogen-agentchat, autogen-ext, autogen-core or magentic-one-cli:
  - The repository advisories list was empty.
  - The global advisory queries returned 0.
  - NVD keyword searches "autogen" and "magentic" found only unrelated products.
- **Unreleased security hardening:**
  - PR #7463, "fix: restrict importlib provider loading to trusted namespaces", merged 25 Mar 2026, 11:15 PM ET. It also hardened "VideoSurfer `extract_audio()` to reject URL inputs (SSRF), enforce `.mp3` extension, and block path traversal".
  - PR #7362 hardened the AutoGen Studio MCP WebSocket (AutoJack), merged 11 Mar 2026, 3:42 PM ET.
  - Neither is in a PyPI release. Main is 9 commits ahead of python-v0.7.5.
  - VideoSurfer is an optional add-on, not one of the four default Magentic-One agents.
- **Maintenance status:**
  - The README banner was added on 2 Oct 2025 (7:54 PM ET, maintenance mode) and updated on 6 Apr 2026.
  - Commit 004749e (16 Oct 2026, 12:14 PM ET) changed it to: "**⚠️ Project archived and no longer maintained** … Microsoft is not providing bug fixes, security fixes, new features, or support for this project." It adds: "AutoGen was developed for research and experimentation and as it transitions to archived, we continue to advise against production use." New users are pointed to Microsoft Agent Framework.
  - The GitHub `archived` flag is still false on 20 Oct 2026.
- **Researcher claim (O12):** a magentic-one-cli `--config` path traversal (company-rated 9.8), "MSRC Submitted". Unconfirmed: no CVE, advisory or maintainer statement was found.
- **AutoJack (O13, vendor blog):** an AutoGen Studio chain. Microsoft: "The affected MCP WebSocket surface was never included in a Python Package Index (PyPI) release". Outside Magentic-One's scope.
- **Disputes with the developer:** none found, apart from the unconfirmed O12 report. **Legal / regulatory:** none found.

## Precedents applied
- **0031:** shared-author and developer-company exclusions:
  - The technical report and the AutoGen-team papers (Who&When, Who&When Pro).
  - Microsoft-affiliated papers (D3). This follows the CAP/Fellou logic, where a developer affiliation meant exclusion.
- **0036 caution 2 / 3:** the named system must be run. Leaderboard rows submitted by the developer are other (O6).
- **0039:** results for a model alone are context only. None were counted.
- **0042:** re-implementations and adapted configurations are other: O2, the MAF Magentic orchestration and the substituted-agent setups (D2).
- **0058:** illustrations and demos are not counted (README demos, the Microsoft blog).
- **0076:** re-analysis of traces produced by others is other (O9–O11).
- **0083 D4a:** a preprint and its proceedings version count once (C3: ACL 2026 and arXiv 2604.22708; C4: PMLR and arXiv 2608.05791).
- **0079:** derived_other = 13 + 0 = 13.
- **0051 strict:** an A grade needs ≥7 counted, ≥3 peer-reviewed and a versioned current-version test within 12 months. Here 6 are counted, so the grade is B by count. C5 would satisfy the version condition.
- **Competing-method papers** count, with disclosure: C4, C6.

## Score (Scoring rules v0.1)
| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion rate | 30 | 40 | **Low to moderate.** GAIA about 38% with GPT-4o (C2), about 43% Level 1 and 26% Level 2 with Qwen-Plus (C4). 74/119 GAIA and 17/30 AssistantBench runs failed (C3). It did not complete large document workflows (C6). Same as Browser Use (40); below Agent S (45). |
| Disputes | 20 | 60 | **No CVE or advisory**, and no legal action. But the hardening is unreleased, the AutoGen README says the project is archived with no further security fixes, and there is one unconfirmed path-traversal report. Below AIDE (70; maintained, no CVEs); above Browser Use (50) and the 55-type unfixed-high-CVE treatment, because no CVE exists. |
| Adherence to limits | 25 | 30 | **Weak:** 97% / 88% arbitrary code execution (C1). 90.9% of planned unsafe actions were attempted, with 54.3% reporting, and the largest share of access-control meltdowns (C5). Same as Browser Use and Skyvern (30). |
| Evidence quality | 25 | 75 | **6 counted, 4 peer-reviewed** (COLM, NeurIPS D&B, ACL, ICML). One is versioned and current. Limits: two Cornell studies share authors, one is an attribution benchmark, most tests are unversioned, and the sample is incomplete. Same as STORM, Devin and GitHub Copilot coding agent (75; B). |

0.30 × 40 + 0.20 × 60 + 0.25 × 30 + 0.25 × 75 = 12 + 12 + 7.5 + 18.75 = 50.25. This rounds to **50** under the half-up rule (0010).

**Grade B:** 6 counted (5–6), 4 peer-reviewed.

**Sensitivity:**
| Variant | Counted | Peer-reviewed | Versioned ≤12 months | Grade |
|---|---|---|---|---|
| Recommended (D2a, D3a, D4a) | 6 | 4 | C5 (0.7.5) | B |
| D2b: count O1 Repair or Resample (shipped MagenticOneGroupChat 0.7.5) | 7 | 4 | C5, O1 | A eligible (evidence about 80–85 → 51–52) |
| D2c: count O1–O3 | 9 | 4 | C5, O1 | A eligible |
| D3b: count the Microsoft-affiliated (non-developer) papers | 9 | 6 | C5 | A eligible |
| D4b: Who&When as counted | 7 | 5 | C5 | A eligible (not recommended) |
| D5b: treat 0.7.5 as not current (archived) | 6 | 4 | none | B (no change) |
| Preprints excluded (illustration only) | 4 | 4 | none | B- |

**Score range:**
| Change | Overall |
|---|---|
| As proposed | 50 |
| Disputes 55 | 49 (49.25) |
| Disputes 65 | 51 (51.25) |
| Completion 45 | 52 (51.75) |
| Adherence 35 | 51 (51.5) |
| Evidence 80 | 52 (51.5) |

The plausible range is 49–52.

**Index position:** the page sits after Devin (50) and before Agent S (49) (score descending, then name). The page title is "Magentic-One (open-source) — Agent Reputation & Trust Clearinghouse", 67 characters (≤68).

## Risks and uncertainties
1. **Model attribution.** Each figure is Magentic-One plus a model (GPT-4o, Gemini 1.5, Qwen-Plus, GPT-5, GPT-5.4).
2. **Version.** Only C5 states a version. C1–C3 likely used 0.4.x (2025). All 0.4–0.7 releases share the same AgentChat design, but this was not checked release by release.
3. **Archive status.** The 16 Oct 2026 README says AutoGen is archived and gets no security fixes, but the GitHub archived flag is still false. Wording quotes the README. The disputes score may need revisiting if a CVE appears with no fix.
4. **Grade edge.** The grade depends on D2 and D3. Counting one orchestrator-only study (O1) or the Microsoft-affiliated papers would make it A eligible.
5. **C3 failure counts** come from benchmark construction, so they are not a sampled success rate. The page says so.
6. **C4 peer review.** Confirmed in the PMLR volume 306 listing (proceedings.mlr.press/v306/xu26bb.html). OpenAlex lists only the arXiv version.
7. **Unconfirmed security claim (O12).** It comes from a company marketing page and is reported neutrally as unconfirmed.
8. **Sample.** 40 of 284 works were not downloaded, and Semantic Scholar and the arXiv API were unavailable (D10 banner).
9. **Disclosures.** C1/C5 share authors. C4 and C6 are competing methods. C2 has an industry co-author (Intesa Sanpaolo).

## Decisions (D1–D10 approved 2026-10-20; D11 approved 2026-10-20; D12 pending; D13 not approved)
- **D1 Scope.**
  - (a) One entry for AutoGen's Magentic-One: MagenticOneGroupChat with its own agents (0.4–0.7.5), magentic-one-cli and the Nov 2024 package. Magentic-UI, the MAF Magentic orchestration and AutoGen Studio are out of scope (Studio is disputes context only). **Recommended.**
  - (b) Also include the MAF Magentic orchestration as the "successor". Not recommended: it is a separate re-implementation, and Microsoft says it is untested outside the original design.
  - (c) Combine with Magentic-UI. Not recommended: it is a separate reserve candidate.
- **D2 Orchestrator with substituted agents** (O1 Repair or Resample, O2 AgentX, O3 Ask Your Advisor).
  - (a) Other: none runs Magentic-One's own agent team (0042). **Recommended.** Gives 6 counted, B.
  - (b) Count O1 only, because it runs the shipped `MagenticOneGroupChat` from 0.7.5 unmodified. Gives 7 counted, A eligible.
  - (c) Count all three: 9 counted.
- **D3 Microsoft-affiliated authors not on the Magentic-One or AutoGen team** (Breaking and Fixing, ICLR 2026; TAMAS, ACL 2026; Litmus (Re)Agent).
  - (a) Excluded under 0031 (developer-company affiliation, as with CAP/Fellou), consistent with the task rule that Microsoft Research papers do not count. **Recommended.**
  - (b) Other.
  - (c) Count, with disclosure: 9 counted, 6 peer-reviewed, A eligible.
- **D4 Who&When / Who&When Pro.** (a) Excluded as AutoGen-team papers (Chi Wang, Qingyun Wu). **Recommended.** (b) Other.
- **D5 "Current version" question.**
  - (a) Treat autogen-agentchat / autogen-ext 0.7.5 (30 Sep 2025), still the latest release, as the current version. C5 is a current-version test. State the archive notice on the page (summary, disputes, uncertainties). **Recommended.**
  - (b) Treat Magentic-One as discontinued, so no test can be current (no grade change now, but A is blocked later).
  - (c) Defer the entry until Magentic-One in Microsoft Agent Framework is tested. Not recommended (D1).
  - Also flagged: if the README archive notice becomes a GitHub archive, consider a visible status note at the next review.
- **D6 Category.**
  - (a) **Browser/web agent:** its main documented use is web and file tasks (GAIA, AssistantBench, WebArena). **Recommended.**
  - (b) Computer-use agent: its peers are Agent S and UI-TARS Desktop, but Magentic-One does not operate a desktop GUI.
  - (c) A new "Generalist multi-agent system" category. This needs a separate methodology decision.
- **D7 Name and title.** (a) "Magentic-One (open-source)" (title 67 characters). **Recommended.** (b) "Magentic-One (Microsoft)" (65). A name with "Microsoft Research, open-source" exceeds 68.
- **D8 Score.** 50 / B (40 / 60 / 30 / 75). Alternatives: 49 (disputes 55, if the archive with unreleased fixes is weighted like an unfixed issue) or 51 (disputes 65).
- **D9 Disputes wording.** "No CVE was found; since October 2026 the developer's AutoGen page says the project is archived and no longer receives bug or security fixes" (approved D11 wording), plus the unreleased PR #7463 and the unconfirmed O12 claim, as drafted. **Recommended.**
- **D10 Recheck banner.** "Citation check incomplete — recheck later". **Recommended.**
- **D11 (APPROVED 2026-10-20, 4:56 PM ET) Entry page + changelog row + feed item + decision record.** As in the final private draft, with the two approved changelog-row wording fixes; the page's archive wording follows the README notice and notes that GitHub does not mark the repository as archived.
- **D12 (pending) Deploy.**
- **D13 Cross-reference / caveat edits (NOT approved; not applied; left for those entries' next reviews):**
  - (a) **Data Interpreter page:** C1 also tests MetaGPT's Data Interpreter and C2 includes MetaGPT traces. Consider these at the next Data Interpreter review. No change now.
  - (b) **OpenAI Codex page:** C5 tests OpenAI Codex. Consider at the next Codex review. No change now.
  - (c) **Magentic-UI reserve note:** O8 and several others report Magentic-UI separately. Keep them for that candidate.
  - (d) No comparison page exists for Browser/web agents, so no caveat edit is needed.

**Recommendation (approved 2026-10-20, 4:41 PM ET, for D1–D10 exactly as drafted):** D1a, D2a, D3a, D4a, D5a, D6a, D7a, D8 (50 / B), D9, D10. D11 approved separately (2026-10-20, 4:56 PM ET); D12 held for separate approval. D13 not approved.

## Final private draft (scratch clone of master 1bff6f4; real tree untouched)
Combined build (entry page, changelog row, feed item, this decision record): see final/final-results.txt for the check output, projected totals and manifest preview.

## Minimum viable version
Approve D1a, D2a, D3a, D5a and D8 at 50 / B with the D10 banner, and keep the other wording as drafted. D13 needs no action.

## Plain-English terms
- **Orchestrator:** the agent in Magentic-One that makes the plan, picks which agent acts next and re-plans when stuck.
- **WebSurfer / FileSurfer / Coder / ComputerTerminal:** the agents Magentic-One directs. They browse web pages, read local files, write code and run it.
- **AutoGen / AgentChat:** Microsoft's open-source framework that Magentic-One is built on. AgentChat is its high-level layer.
- **Microsoft Agent Framework:** the framework Microsoft now recommends instead of AutoGen. Its "Magentic orchestration" is a separate re-implementation.
- **Archived / maintenance mode:** the developer has stopped adding features, and now also says it gives no bug or security fixes.
- **Control-flow hijacking:** hidden instructions in a file or page that make the orchestrator send work to the wrong agent, for example to run attacker code.
- **Meltdown (C5):** an unsafe action an agent takes on its own after a harmless error, such as a missing web page.
- **GAIA / AssistantBench / WebArena:** public benchmarks of multi-step web and file tasks.
- **Peer-reviewed:** published at a venue that reviews papers before acceptance.
- **CVE:** a public identifier for a security flaw.
- **Current-version test:** a test within the last 12 months that states the version tested. Grade A needs one.

*Informational only; not a guarantee, endorsement, or certification.*
