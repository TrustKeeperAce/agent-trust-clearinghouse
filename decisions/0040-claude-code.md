# Decision 0040: Claude Code (Anthropic) — 55 / A

**Status: APPROVED by Remington, 2026-10-17** (D1–D6 approved; D8 approved as-is, publish on the screened set; D7 full reads not requested). Batch 4 candidate #4 (0034). Category: Coding agent (0036).
Entry: agents/claude-code.yaml and public/agents/claude-code.html. The entry carries a visible note: "Citation check incomplete — about 13 candidate studies not yet screened; recheck later."

Scope (proposed): the Claude Code agent (terminal CLI and headless `claude -p`; npm @anthropic-ai/claude-code; first npm release 0.2.7 on 24 Feb 2025; latest 2.1.302 on 16 Oct 2026).

Not covered:
- Claude models in other scaffolds (0036 caution 2).
- The Claude Agent SDK.
- Claude Desktop / Cowork.
- Claude Research, which is an existing entry. That entry covers the research mode in the Claude apps; there is no overlap in sources.

## Affiliation checks
- **Developer: Anthropic.** All Anthropic-authored reports are vendor sources and not counted: engineering blog posts, model cards, and SWE-bench / Terminal-Bench figures.
- **Terminal-Bench 2.0** (ICLR 2026, arXiv 2601.11868): Nicholas Carlini is listed with an Anthropic affiliation. **Excluded for Claude Code**, following the CAP/Fellou precedent. Its public leaderboard is also not counted.
- **Counted studies:** I checked the author affiliations of all 15 against Anthropic and found none. Affiliations are listed per source below.
- **Funding and in-kind support:**
  - SkillsBench thanks Anthropic, among 11 model providers, for "model access and API support". Disclosed; still counted (see D4).
  - TerminalWorld thanks AWS for credits and Bedrock access. Bedrock serves Claude models, but this is not Anthropic funding.
  - No other counted paper acknowledges Anthropic funding or credits. I checked the acknowledgments sections; several papers have none.
- **Other disclosures:**
  - TerminalWorld used Claude Code itself to build its tasks.
  - Overeager has a Quantstamp author.
  - SWE-MISBEHAVIOR has Salesforce AI Research authors and proposes a mitigation.
  - UrbanDS proposes a competing system.

## Proposed score
| Factor | Weight | Score |
|---|---|---|
| Completion rate | 30% | 50 |
| Disputes | 20% | 45 |
| Adherence to limits | 25% | 40 |
| Evidence quality | 25% | 85 |

0.30×50 + 0.20×45 + 0.25×40 + 0.25×85 = 55.25, rounded to **55**.

**Grade A:**
- 15 counted sources.
- 5 peer-reviewed.
- Recent tests (2026) that state the version: 2.1.117, 2.1.138 and 2.1.139.

Calibration against existing entries: OpenHands 50/55/55/85 = 61 A; SWE-agent 45/55/55/80 = 58 B.

## Counted independent performance sources (15)
| # | Source | Peer-reviewed | Version / date | Key result |
|---|---|---|---|---|
| 1 | Red-Teaming Coding Agents (HKUST, Fudan; ISSTA 2026, PACMSE; 2509.05755) | yes | 2.0.37 and 2.1.138 / 2025–mid 2026 | Prompt-leak 0.891 and RCE on 2.0.37. On 2.1.138, RCE-2 success was 0.0 with Sonnet 4.6 and Opus 4.7; the authors credit Claude Code's progressive tool disclosure. |
| 2 | On the Use of Agentic Coding (NAIST, Queen's; TOSEM; 2509.14745) | yes | unstated / 2025 | 567 Claude Code pull requests in 157 projects: 83.8% accepted vs 91.0% for human pull requests. Field study. |
| 3 | Comparing AI Coding Agents (Trieste, KCL, UCL; MSR 2026; 2602.08915) | yes | unstated / May–Aug 2025 | 139 Claude Code pull requests: 72.6% accepted in the common window (Codex 79.9%); 33.3% on test tasks. Small sample. |
| 4 | PBT-Bench (Tsinghua, UW; NeurIPS 2026 D&B; 2605.15229) | yes | default settings, Opus 4.8 / 2026 | Bug recall 78.6% vs 81.2% in OpenHands with the same model. Run headless with permission prompts disabled. |
| 5 | TerminalWorld (UCL, Nanjing, Tencent; ASE 2026 extended abstract; 2605.22535) | yes (extended abstract) | unstated, Opus 4.7 / 2026 | 58.0% pass (60.7% resolved) vs Terminus-2 62.5%. Claude Code was used in task synthesis (disclosed). |
| 6 | SWE-RPG (SMU, Monash, DGIST and others; 2608.09072) | no | unstated / about July 2026 | Average 32.8% resolved across 6 backends; best 49.1% with Kimi-K3. |
| 7 | SWE-bench Science (SII, Fudan; 2608.19799) | no | unstated / 2026 | Pass@1 47.90% with Opus 5 (best of 8); 42.02% with DeepSeek-V4-Pro. |
| 8 | SkillsBench (BenchFlow and others; 2602.12670) | no | unstated, Opus 4.7 / 2026 | 61.2% with Skills vs 53.1% in OpenHands. Thanks Anthropic for API support (disclosed). |
| 9 | ResearchClawBench (Shanghai AI Lab; 2606.07591) | no | unstated, Opus 4.6 / 2026 | 21.5 of 100, the top of 7 research agents (re-discovery threshold 50). |
| 10 | Overeager Coding Agents (Griffith, NTU, UNSW, Quantstamp; 2605.18583) | no | **2.1.117** / 2026 | Out-of-scope actions on benign tasks 5.4–27.7%; Sonnet 4.6 27.7% in Claude Code vs 1.1% in OpenHands. |
| 11 | SWE-MISBEHAVIOR (NUS, A*STAR, Salesforce and others; 2610.18206) | no | unstated, Sonnet 4.5 / 2026 | Boundary-violation rates of 3.80% (code generation) and 8.50% (file management) were the lowest of 4 frameworks; 18.95% on system interaction. |
| 12 | UrbanDS (Tsinghua; 2607.26724) | no | unstated | Claude Code 62.9% on UrbanDS-Bench and 42.0% on CoDA-Bench. Competing method (disclosed). Already cited on the Data Interpreter entry. |
| 13 | Measuring the Permission Gate (HKUST, ETH Zurich; 2604.04978) | no | behaviour as of Apr 2026 | Auto mode on 128 deliberately ambiguous tasks: end-to-end false negative rate 81.0% (70.3% on actions it evaluated; false positives 31.9%) vs Anthropic's 17% on production traffic. |
| 14 | SusVibes (CMU and others; 2512.03262) | no | unstated / 2025–26 | Functional 12.9–41.4%; both functional and secure 3.8–8.6% across 4 models. Lower than SWE-agent and OpenHands with Claude 4 Sonnet. |
| 15 | Tool-surface ablation (RIT; 2607.10569) | no | **2.1.139** / July 2026 | With Sonnet 4.6, pass rates were the same across tool configurations. Code-only cost was −24.6% on computation tasks and +14.4% (not significant) on SWE-bench tasks. |

Consistency: sources 4, 10 and 11 are already cited on the OpenHands entry, and their Claude Code figures there match these.

## Other sources (not counted)
- **Anthropic GitHub security advisories:** 35 advisories from June 2025 to October 2026 (28 high, 4 medium, 3 low).
  - Most are approval-prompt, sandbox or trust-dialog bypasses, for example CVE-2025-58764, CVE-2026-21852, CVE-2026-25725 and CVE-2026-55607.
  - Each lists a fixed version.
  - A few concern Claude Desktop / Cowork (versions 1.38xx and up) rather than the CLI.
- **Rejected CVEs:** CVE-2026-35020, 35021 and 35022, filed by VulnCheck in April 2026, were **rejected** by that CNA. The reasons given were intended or documented behaviour, or outside the threat model. They are not listed as vulnerabilities.
- **Source-code exposure (Ars Technica, BleepingComputer, TechCrunch, Bloomberg):**
  - Version 2.1.88 was published to npm on 31 Mar 2026 with a source map exposing the code.
  - Anthropic said it was a packaging error and that no customer data was exposed.
  - Its DMCA notices reached about 8,100 GitHub repositories; Anthropic said this was an accident and retracted most of them.
  - No lawsuit was found.
- **FSE 2026 industry paper:** a study of bugs in Claude Code, Codex and Gemini CLI, based on bug reports.
- **ICSE 2026 AGENT workshop:** an analysis of 328 Claude Code configuration files.
- **MSR 2026 behavioral analysis:** found Claude Code pull requests tend to rewrite rather than edit code. Descriptive.
- **NYIT preprint (2603.21642):** a qualitative rating of Claude Code as "low-to-medium" risk for MCP tool poisoning. Not systematic enough to count (see D3).

## Not counted
- Anthropic's own benchmark figures and usage reports.
- The Terminal-Bench 2.0 paper (Anthropic author) and the tbench.ai leaderboard.
- Studies of Claude models in other scaffolds (mini-SWE-agent, OpenHands, Terminus, Cursor or Copilot with Claude), for example "Your AI, My Shell", which tested Cursor and Copilot.
- METR's developer studies, which mainly used Cursor and did not name Claude Code as the tool tested.

## Citation gate (PROCESS.md)
Semantic Scholar queries, retried from 17:54:53 to 18:30:41 ET (35 minutes; 41 responses were 429 and 2 were 200; log in /workspace/claudecode/s2log.txt):
- "Claude Code agent evaluation": **200** at 17:58:35 ET. 100 of 16,847 results were retrieved and saved. The fix for the 0039 script bug held.
- "Claude Code empirical study": **200** at 18:19:52 ET. 100 of 41,027 results.
- "Claude Code benchmark" and "Claude Code security vulnerability": 429 for the full 35 minutes. The OpenAlex fallback (keyword search, from Feb 2025) was used only after the 30-minute mark, at 18:26 ET. It returned 4,062 and 1,419 results.

Screening:
- I screened titles from all four result lists and read the full text of 7 additional candidates. 2 were added as counted sources (Permission Gate, SusVibes).
- **The screening is not exhaustive.** The Claude Code literature is very large (thousands of hits). Plausible product tests that I have not screened include:
  - IssueTrojanBench (2607.20759)
  - EvilGenie (2511.21654)
  - Not All Agents Are Equal (2609.17598)
  - Why Agentic-PRs Get Rejected (2602.04226)
  - Microsoft's 2026 CLI-agent rollout study (2607.01418; Microsoft makes competing tools)
  - Prompt Injection Attacks on Agentic Coding Assistants (2601.17548)
  - Blocking at the Boundary (2610.05163)
  - TUA-Bench (2606.28480)
  - RuBench (2607.06411)
  - BeyondSWE (2603.03194)
  - Autonomous LLM Agents & CTFs (2605.21497)
  - the JMIR clinical-data-analysis evaluation
  - Value in Health MSR231
- These would not lower the grade, because A conditions are already met with margin. They could move factor scores by a few points (see D8).

## Reading depth (stated honestly)
- I did not read the papers cover to cover.
- For all 15 counted papers and Terminal-Bench, I did targeted reads of the full-text PDFs: author and affiliation blocks, acknowledgments, experimental setup, the Claude Code result tables or paragraphs, and searches for version strings.
- A full read is offered as an optional D7 before publication, as with 0038.

## What the rules say
- 7+ counted sources, 3+ peer-reviewed, and a recent test that states the version give **A**.
- Vendor and developer-affiliated sources are excluded (0036 cautions 1 and 4).
- The named product must be run (caution 2). All 15 run Claude Code itself, not just Claude models.

## Risks and uncertainties
- Most counted sources do not state the version, and Claude Code ships several releases a week. The A grade rests on two preprints and one ISSTA paper that do state versions.
- Many runs used non-Anthropic models or disabled permission prompts, so they do not reflect a typical setup.
- If the PR field studies (2, 3) are not counted (D3), there are 3 peer-reviewed sources, one of them an extended abstract.
  - If the ASE extended abstract is also not treated as peer-reviewed, only 2 remain, which gives **B**.
  - With D3 counted, A holds even without ASE (4 peer-reviewed).
- The disputes score reflects a large number of advisories, all with published fixes and vendor-run disclosure, plus the leak and DMCA episode. Judgment call.

## Open follow-up: SusVibes consistency flag
SusVibes also reports SWE-agent and OpenHands results. Neither published entry cites it. Status: OPEN. No entry changes were made in 0040; any update to those entries needs a separate decision, as with the Agent S flag in 0039.

## Decisions needing approval
- **D1 (APPROVED), category:** Coding agent (0036). It works in repositories and terminals; its main documented use is software changes.
- **D2 (APPROVED), scope:** Claude Code CLI / headless, all versions. Out of scope: Claude models elsewhere, the Agent SDK, Desktop/Cowork, and Claude Research, which keeps its separate entry with an explicit cross-reference.
- **D3 (APPROVED), field studies:** count the two pull-request studies (TOSEM, MSR) as independent performance sources, because they measure real-world outcomes of the named product. There is no previous precedent. Alternatively, list them as other. The NYIT qualitative rating stays as other.
- **D4 (APPROVED), SkillsBench:** count it, with disclosure of the Anthropic API-support acknowledgment. The alternative is to exclude it as in-kind support; that would leave 12 sources and the grade unchanged.
- **D5 (APPROVED), Terminal-Bench 2.0:** exclude it because of the Anthropic co-author.
- **D6 (APPROVED), security wording (neutral):** "Anthropic has published 35 security advisories for Claude Code and related apps since June 2025, mostly approval-prompt, sandbox or trust-dialog bypasses, each with a fixed version. Three CVEs filed by VulnCheck in April 2026 were later rejected by that CNA. On 31 March 2026, version 2.1.88 was published to npm with a source map exposing the source code; Anthropic described it as a packaging error with no customer data exposed."
- **D8 (APPROVED as-is), screening depth:** accept 55 / A on the screened set (15 counted), or ask for a further screening pass of the unscreened candidates listed under the citation gate before publication. Scores could move by a few points; the grade would not.
- **D7 (not requested):** full cover-to-cover reads before publication, as with 0038.

## Recommendation
Publish Claude Code as a Coding agent at **55 / A**, conditional on D3 and D5. Add a cross-reference between this entry and Claude Research.

## Plain-English summary
Claude Code is Anthropic's AI coding tool that works in a terminal. Independent researchers have tested it a lot. It solves a third to about three-fifths of hard benchmark tasks depending on the task and model, and most of its real pull requests are accepted, though slightly fewer than human ones. On safety, results are mixed: one study found it often went beyond what was asked and another found its auto-approval mode missed most risky actions in ambiguous tasks, while others found it among the more careful agents. Many security issues have been reported and fixed. Evidence is strong (grade A), and the overall score is 55.
