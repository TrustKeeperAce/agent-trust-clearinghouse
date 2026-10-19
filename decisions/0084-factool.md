# Decision 0084: FacTool — 55 / B

**Status: D1–D10 APPROVED by Remington, 2026-10-19, as recommended: D1a scope; D2 Verification, "FacTool (open-source)", slug factool; D3 the five MBZUAI-affiliated papers counted with disclosure; D4 Knowledge-Centric Hallucination Detection / RefChecker excluded (0031); D5 component and other-task tests counted with notes; D6 Re-Ex not peer-reviewed; D7a strict reading (grade B); D8 55 / B; D9 CVE wording as drafted; D10 recheck note. D11 (entry page with changelog row) APPROVED by Remington, 2026-10-19. D12 (deploy) is pending: nothing is deployed.**

Batch 5 candidate 2. Research completed 19 Oct 2026 (ET). Templates followed: 0030 (Loki / OpenFactCheck), 0017 (Elicit), 0083 (Cursor agent).

## What happened
1. **Scope set** (see D1). The entry covers the open-source FacTool framework:
   - GitHub GAIR-NLP/factool and PyPI `factool` 0.1.x. PyPI versions 0.0.1–0.1.3 were all released Jul–Aug 2023; the latest is 0.1.3 (14 Aug 2023).
   - Four modes: knowledge-based QA, code, math and scientific literature review.
   - It runs with any language model backend the user configures. GPT-3.5/GPT-4 are the defaults, and the package pins openai 0.27.8.
   - Out of scope: Halu-J (a separate judge model kept in the same repository), results for a language model alone (0039), and reuse of FacTool's datasets or prompts.
2. **Search.**
   - OpenAlex full-text search for "factool" returned 335 works. Pages 1–2 were fetched without an API key.
   - 304 of 333 PDFs were downloaded and their text extracted (/tmp/p84). Each was screened for FacTool result tables and for setup text saying FacTool was run.
   - Plus web searches, the ACL Anthology, publisher pages, GitHub, PyPI, NVD/CVE.org and the GitHub advisory database.
   - Semantic Scholar returned 429; the arXiv API was unreliable. Google Scholar was not reachable through the tools. OpenAlex was used as the PROCESS fallback.
3. **Results.**
   - **17 counted** independent performance sources, **13 peer-reviewed**.
   - **10 other** (9 other + 1 anecdotal).
   - **1 excluded** (shared author, 0031).
   - Vendor/maintainer material.
   - No counted study states a FacTool version or commit.
4. **Score:** 55, grade **B** (D7a approved: strict reading).

## Counted: independent performance sources (17; peer-reviewed 13)
| Ref | Source | Peer review | Backend / date | Key FacTool figures |
|---|---|---|---|---|
| S1 | Factcheck-Bench (MBZUAI and others; Findings EMNLP 2024; 2311.09000) | yes | LLaMA, GPT-3.5; Serper; 2023–24 | Verification step only. True-claim F1 0.84 and false-claim F1 0.47 (LLaMA); 0.81 / 0.46 (GPT-3.5). Component test. |
| S2 | OpenFactCheck (MBZUAI, Monash, Sofia; COLING 2025; 2405.05583) | yes | GPT-3.5 + Serper; 2024 | Checker on Factcheck-Bench (rows shared with S1), FacTool-QA and FELM-WK. $2.5 search + $12.2 model, 0.49 h for 765 claims. Component test. |
| S3 | Loki (LibrAI, MBZUAI and others; COLING 2025 demos; 2410.01794) | yes | GPT-4o + Serper; 2024 | Factcheck-Bench true/false F1 0.71 / 0.61; FacTool-QA 0.78 / 0.56. 12.38 s per sample against Loki's 8.32. Some rows reused from S2. |
| S4 | FIRE (MBZUAI, TU Darmstadt; Findings NAACL 2025) | yes | GPT-4o, GPT-4o-mini; 2024 | FacTool-QA 0.84 / 0.58; FELM-WK 0.60 / 0.64; BingCheck 0.68 / 0.56. Cost $24.76 model + $3.67 search against FIRE's $3.35 + $0.60. |
| S5 | UrduFactCheck (MBZUAI and others; Findings EMNLP 2025; 2505.15063) | yes | GPT-4o, GPT-4o-mini; 2025 | FacTool run on Urdu translations of FacTool-QA and BingCheck. Translated-data adaptation. |
| S6 | G2LDetect (Zhejiang; AAAI 2025) | yes | Llama3-8B, ChatGPT, GPT-4; 2024 | Run on HaluEval-Summary, QAGS, FEVER and SciFact; e.g. F1 about 70.9 on HaluEval-Summary with GPT-4. |
| S7 | FIZZ (EMNLP 2024) | yes | unstated; 2024 | Summary inconsistency on AggreFact: balanced accuracy 49.3–72.7. Outside FacTool's original tasks. |
| S8 | REVEAL / "CoT is as strong as its weakest link" (Google Research and others; ACL 2024) | yes | GPT-3-based; 2023–24 | Step attribution macro-F1 71.1. Evidence was inserted from the dataset rather than retrieved by FacTool. Component test. |
| S9 | FaStFact (Findings EMNLP 2025; 2510.12839) | yes | KB-QA setting; 2025 | F1@K' 0.987 against a ground truth of 0.792: the largest overestimate of five pipelines. Claim-count gap 9.09. |
| S10 | Rowen (CAS ICT; SIGIR-AP 2025; 2402.10612) | yes | unstated; 2024 | Mitigation baseline on TruthfulQA and StrategyQA, below Rowen. 12.5 and 11.6 retrieval calls per question, against Rowen's 1.5 and 0.5. |
| S11 | EMULATE (NUS; FEVER 2025 workshop, ACL Anthology) | yes | gpt-4.1-2025-04-14; 2025 | True-claim F1 0.87 (FacTool-KBQA), 0.88 (BingCheck), 0.82 (Factcheck-Bench). False-claim precision 0.52–0.59. |
| S12 | JointCQ (PKU, Huawei; Findings ACL 2026; 2510.19310) | yes | GPT-4.1; 2025 (arXiv 22 Oct 2025) | ANAH en/zh hallucination detection. JointCQ is about 5–8 points higher in accuracy. |
| S13 | LEAP, "Can a Small Model Learn to Look Before It Leaps?" (LNCS 2026; 2511.05854) | yes | Qwen2.5-7B, Llama3.1-8B and others; 2025 (arXiv Nov 2025) | Accuracy about 47–62%. Below FIRE in two of three result blocks and above it in the third. |
| S14 | Re-Ex (Yonsei; ICLR 2024 workshop, non-archival; 2402.17097) | no (D6) | GPT-3.5, GPT-4, official code; 2023–24 | FactPrompt F1 52.6 / 57.1. 20.0–26.2 s and 3.1–4.1K tokens per response. |
| S15 | PASS-FC (Trip.com Group; preprint 2504.09866, ACL submission on OpenReview) | no | GPT-3.5-turbo-0613, defaults; 2025 | FacTool-QA F1 62.5. |
| S16 | CoVer (preprint 2609.00508) | no | GPT-4o; 2026 | Seven claim sets with conflicting evidence. Accuracy 51.0–81.5%: on FEVER 51.0%, the lowest of six systems; on CONFACT HumC 80.0%, against 88.4% for CoVer. |
| S17 | Phantom Merge (preprint 2610.16141, Oct 2026) | no | unstated (agent backbone Qwen3-32B); 2026 | Agent-trajectory claim detection. AUROC 0.679 (FActScore 0.582, RARR 0.499). Outside FacTool's original tasks. |

All 17 run FacTool themselves. All except S1, S2 and S8 run it as a comparison baseline in a paper proposing a competing method; that is allowed with disclosure (SAFE precedent, 0009).

## Other sources (listed, not counted) — 10
- **Used as a tool or metric, not tested:**
  - UFO (Renmin; preprint): FacTool used as a reference metric.
  - Scientific Reports 2026 multi-agent credibility scoring: adapts FacTool prompts and does not run FacTool.
- **Repeats earlier figures; no new run shown:**
  - MERMAID (2601.22361): its FacTool-QA row equals FIRE's.
  - Markov-chain multi-agent debate (ICASSP 2025): its rows equal the FacTool paper's.
  - FactSearch (ACL 2026 demos): "reproduced from" the FacTool paper.
  - GAMED (2412.12164): Fakeddit 0.506, apparently from earlier work.
  - OpenFactCheck EMNLP 2024 demo: the same leaderboard figures as S2.
- **Adapted pipeline:** LEMMA (2402.11943). FacTool with GPT-4 plus an image-summary front end for multimodal misinformation, outside its text-only design.
- **CVE-2025-4261** (other). It is the same issue as GitHub issue #50 and is listed once.
- **GitHub issue #48** (anecdotal): a user reports the bundled example failing.

## Not counted
- **Vendor or maintainer:**
  - the FacTool paper (arXiv 2307.13528);
  - the GitHub repository;
  - the PyPI package;
  - Halu-J (same group; outside scope).
- **Excluded (0031, shared author):** Knowledge-Centric Hallucination Detection (EMNLP 2024), together with its RefChecker preprint (2405.14486). It runs FacTool with GPT-4 on KnowHalBench, but Pengfei Liu, a FacTool author, is a co-author. The Japanese thesis W7160743104 only quotes this paper's figures.
- **Not tests:**
  - dataset-only reuse (HaluAgent, Proof-of-Guardrail and many papers using FacTool-QA/KBQA);
  - systems papers using FacTool as a workload (Alto, Semantic Operators, Hermes);
  - surveys and descriptions (ClaimCLAIRE, Decomposition Dilemmas, and others);
  - SOTA2 leaderboard (an aggregator).
- **Not screened** (no text access):
  - 29 OpenAlex works whose PDFs did not download, including an ICIC 2025 hallucination-detection paper, LoCal (WWW 2025) and T2F (Discover AI 2025);
  - Google Scholar.

## Shared-author check (0031)
- **FacTool authors:** I-Chun Chern, Steffi Chern, Shiqi Chen, Weizhe Yuan, Kehua Feng, Chunting Zhou, Junxian He, Graham Neubig, Pengfei Liu.
- **Method:**
  - OpenAlex authorships for all 335 works were matched against these names.
  - The paper headers were then checked for all 17 counted sources.
- **Overlap found:**
  - FacTool paper: the developers.
  - Halu-J: Steffi Chern and Pengfei Liu.
  - Knowledge-Centric Hallucination Detection and RefChecker: Pengfei Liu, which is why they are excluded.
  - Five papers that only cite FacTool (FAVA: Neubig; Critique of Critique and System-Level NL Feedback: Yuan; Reformatted Alignment, O1 Replication, Alignment for Honesty: Liu, Yuan and Neubig). None tests FacTool.
- **Counted sources:** no overlap with any FacTool author. FELM, which includes Shiqi Chen, I-Chun Chern, Junxian He and Pengfei Liu, does not test FacTool and is not listed.
- **MBZUAI cluster (S1–S5; disclosure, not exclusion):**
  - Authors include Yuxia Wang, Preslav Nakov, Minghan Wang, Hasan Iqbal, Jiahui Geng, Rui Xing and Iryna Gurevych. They build competing checkers (Factcheck-GPT, OpenFactCheck, Loki, FIRE).
  - The five papers share authors with one another, but not with FacTool.
  - Some FacTool rows are reused along the chain: Factcheck-Bench → OpenFactCheck → Loki.
  - Disclosed in the notes and uncertainties (D3).

## Repository maintenance, disputes and security
- **GitHub GAIR-NLP/factool:**
  - created 25 Jul 2023;
  - FacTool code commits end about Sept/Oct 2023;
  - last push 19 Aug 2024 (Halu-J material);
  - no GitHub releases; not archived; Apache-2.0; 23 open issues.
- **PyPI:** 0.1.3 (14 Aug 2023) is the latest. `setup.cfg` pins openai==0.27.8, which predates the OpenAI v1 SDK.
- **CVE-2025-4261:**
  - CNA VulDB; published 5 May 2025; NVD status Deferred.
  - CVSS 4.0 score 4.8 (Medium), local attack.
  - Code injection through exec() in `factool/math/tool.py` (`run_single`), affecting code up to commit 3f3914b. No fix found.
  - It was reported as GitHub issue #50 (21 Apr 2025), with no maintainer reply.
  - No GitHub security advisory (GHSA) exists.
- **Issue #48** (Oct 2024): errors running example.py.
- **No legal, regulatory or public dispute found.**

## Precedents applied
- **0031:** shared-author exclusion. One paper (with its preprint) is excluded.
- **0039:** language-model-only results are out of scope. Running FacTool's own pipeline with another backend is a test of FacTool (D1). FacTool is designed to be backend-agnostic, as for SAFE, OpenHands and Aider.
- **0042:** re-implementations are not counted. Each counted paper either uses FacTool's code or states that FacTool was run. Where a paper only says "implemented" (FaStFact, CoVer), it describes configuration settings of FacTool, not a new system (flagged in Risks).
- **0009 (SAFE):** rival-method baselines and component tests count, with disclosure.
- **0033:** every counted source has peer_reviewed, version_tested and test_date.
- **0036:** the developers' results are not counted; CVE wording is neutral.
- **0065:** an entry page needs a feed item, so the page and the changelog row go together (D9).
- **0079:** derived_other counts 'other' and 'anecdotal' (10). 'excluded' and 'vendor or maintainer' are not other.
- **0051:** an A needs a test within 12 months that states the version.

## Score (Scoring rules v0.1; D8 approved)
| Factor | Weight | Score | Reasoning |
|---|---|---|---|
| Completion rate | 30% | **50** | True-claim F1 about 0.60–0.88; false-claim F1 about 0.46–0.64. It is usually below the newer method in each paper and sometimes ahead of FIRE (CoVer, LEAP). FaStFact found it overstated factual precision. Close to STORM and AIDE (50); below SAFE (65), whose independent agreement figures are higher. |
| Disputes | 20% | **55** | One unfixed medium-severity CVE, with no maintainer reply, and no legal or regulatory action. Comparable to STORM (55: an unanswered security report) and SWE-agent (55: one unfixed CVE, higher CVSS); above Agent S (45: three CVEs). |
| Adherence to limits | 25% | **40** | The math mode runs model-generated code with exec() and no sandbox. It pins a 2023 OpenAI SDK, and a user reports the example failing. Cost and latency are higher than newer checkers. Below STORM and AIDE (45), above Browser Use (30). |
| Evidence quality | 25% | **75** | 17 counted, 13 peer-reviewed. It is not higher because: nearly all are rival-method baselines; five are one connected group with shared rows; three are component tests; none states a version; and the backends vary. Same as STORM (75), below AIDE (80). |

- **Overall:** 0.30×50 + 0.20×55 + 0.25×40 + 0.25×75 = 15 + 11 + 10 + 18.75 = 54.75, which rounds to **55**.
- **Grade B:** 7+ counted and 3+ peer-reviewed, but no current-version test that states the version. check_scores gives a WARN ("A/B is a judgment call"), which the grade_note documents.

**Effect of an unmaintained research tool on the current-version condition:**
- FacTool's code has not changed since about October 2023, so the "current version" is the 2023 code. Any recent test very likely ran it.
- Tests within 12 months (since 19 Oct 2025):
  - CoVer (2026);
  - Phantom Merge (Oct 2026);
  - LEAP (arXiv Nov 2025);
  - JointCQ (arXiv 22 Oct 2025; runs probably earlier, so borderline).
- None of them states a version or commit.
- 0051 reads condition (3) as needing a stated version, or a dated tier for hosted services. FacTool fits neither, hence B.
- An "unchanged-code" reading would give A. See D7.

## Risks and uncertainties
- **Correlated evidence:** the MBZUAI cluster (5 papers) and its reused rows.
- **Rival-method bias:** almost every counted paper reports FacTool as a baseline below its own method.
- **Backend dependence:** figures run from GPT-3.5 to GPT-4.1, LLaMA and Qwen. FacTool's default SDK pin means newer runs had to modify the client code. That is likely, but not stated.
- **"Implemented" wording:** FaStFact and CoVer say they "implement" FacTool in a given setting. I read this as configuring FacTool, not re-implementing it (0042). If either is a re-implementation, the count is 15–16 and the grade stays B.
- **Figure-read values:** LEAP, CoVer, FIZZ, Rowen and Re-Ex values come from PDF text extraction of tables, and column alignment was inferred. LEAP's block-to-backbone mapping is not certain.
- **Peer review:** Re-Ex is a non-archival ICLR workshop paper (marked not peer-reviewed). EMULATE is in the archival FEVER workshop proceedings (marked peer-reviewed, as for the ICSE workshop papers in Aider and OpenHands).
- **Venues** are taken from DOIs and Anthology pages. LEAP is an LNCS chapter, conference not identified. UrduFactCheck, JointCQ and FaStFact have ACL Anthology DOIs.
- **Coverage gaps:** 29 OpenAlex works were not downloaded. Google Scholar and Semantic Scholar were unavailable.
- **SAFE's entry lists 4 counted sources;** FacTool would have 17. Several of these papers (FIRE, Loki, CoVer, LEAP) also test SAFE but are not in SAFE's entry. They are possible items for a later citation backfill (note only, not part of this approval).

## Decisions (D1–D11 approved 2026-10-19; D12 pending)
- **D1 Scope.**
  - (a) The FacTool framework as above. Running its pipeline with any backend counts. Halu-J, model-only results and dataset or prompt reuse are excluded (**recommended**).
  - (b) Only runs with GPT-3.5/GPT-4, the documented defaults: about 6–7 counted, so B or B-.
- **D2 Category, name and slug:** Verification; "FacTool (open-source)", following "Loki (open-source)"; slug `factool` (**recommended**). The Verification count goes from 4 to 5.
- **D3 MBZUAI cluster:** count all five with a visible disclosure (**recommended**). The alternative is to count the cluster as one source: 13 counted, 9 peer-reviewed, still B, evidence about 70, overall 54.
- **D4 Shared author:** exclude Knowledge-Centric Hallucination Detection and RefChecker under 0031 (**recommended**; this is required by the rule).
- **D5 Component and adapted tests:**
  - Count verification-only tests (S1, S2, S8) and tests on other tasks (S5, S7, S10, S17), with notes (**recommended**, SAFE precedent).
  - LEMMA stays other (multimodal adaptation).
- **D6 Re-Ex peer review:** mark it not peer-reviewed (non-archival workshop) (**recommended**). Marking it peer-reviewed would give 14 peer-reviewed; the grade is unchanged.
- **D7 Current-version reading for an unmaintained tool:**
  - (a) Keep 0051 strictly: a stated version is needed, so **B** (**recommended**; consistent with 0051).
  - (b) Treat a dated test after the last code change as a current-version test when the code is frozen: **A**. This would be a methodology change and would need its own packet, because it could affect other frozen research tools.
- **D8 Scores:** completion 50, disputes 55, adherence 40, evidence 75, giving **55 / B** (**recommended**).
- **D9 Disputes and CVE wording** as drafted. The CVE is stated with its CVSS, local-attack vector, unfixed status and NVD "Deferred" (**recommended**).
- **D10 Visible note** "Citation check incomplete — recheck later" (**recommended**; 29 works not screened, Scholar unavailable).
- **D11 Entry page together with the changelog row:**
  - Add `agents/factool.yaml`, the entry page, the index row, the JSON-LD and llms.txt line, the generated files, and the changelog row / feed item.
  - Under 0065 these go together: page only fails check_all ("no feed item").
  - **Approved** 2026-10-19 (implemented with this record).
- **D12 Deploy:** **pending** (separate approval), using the usual manifest procedure.

## Minimum viable version
Approve D1a, D2, D3–D6 and D7a–D10 as decisions only. Keep the YAML private and hold D11 and D12. If D7 needs more thought, approve everything else and decide D7 later; the score (55) does not depend on it.

## Plain-English terms
- **Counted source:** an outside test of FacTool that meets the independence rules. Three or more are needed for a score.
- **Baseline:** an existing system that a paper runs for comparison against its own new method.
- **Component test:** a test of one step of FacTool (here, judging a claim against evidence) rather than the whole pipeline.
- **Shared author:** a paper written partly by one of FacTool's authors. Not counted.
- **Backend:** the language model FacTool calls to do its work, such as GPT-4o.
- **F1:** a score from 0 to 1 combining how many claims were flagged correctly and how many were missed.
- **CVE:** a public identifier for a security flaw; CVSS rates its severity.
- **Current-version test:** a test within the last 12 months that states the version tested. It is needed for grade A.

*Informational only; not a guarantee, endorsement, or certification.*
