# Decision 0044: GitHub Copilot coding agent — 57 / B

**Status: APPROVED by Remington, 2026-10-17** (D1–D8 approved as recommended; D1 scope: cloud coding agent only).
Entry: agents/github-copilot-coding-agent.yaml and public/agents/github-copilot-coding-agent.html.

Category: Coding agent. Proposed slug: github-copilot-coding-agent. Visible note: "Citation check incomplete — recheck later."

## Proposed score
| Factor | Weight | Score |
|---|---|---|
| Completion rate | 30% | 45 |
| Disputes | 20% | 60 |
| Adherence to limits | 25% | 50 |
| Evidence quality | 25% | 75 |
0.30×45 + 0.20×60 + 0.25×50 + 0.25×75 = 56.75 → **57**. Grade **B**: 12 counted sources and 5 peer-reviewed, but no counted test states a version or falls within 12 months (all data is from Dec 2024 to Jul 2025). This fails the A condition, so B under the "7+ sources that fail an A condition" rule.
Comparison: Codex is 62/A. It was tested in versioned CLI benchmarks and led acceptance in the same field studies. Claude Code is 55/A. Copilot sits between them on score but has a lower grade because it has no benchmark and no versioned or recent test.

## Scope
This entry covers the cloud coding agent that opens pull requests (public preview May 2025, bot account copilot-swe-agent). It excludes completions, the 2021–23 Codex-era Copilot studies, Chat and agent mode in the IDE, Copilot CLI, and Copilot code review.

## Counted (independent performance, 12; peer-reviewed 5)
1. Comparing AI Coding Agents (MSR 2026, Trieste/KCL/UCL): 68.0% in the common May–Jul 2025 window (Codex 79.9%). 4.94 reviews per pull request. PR
2. Where Do AI Coding Agents Fail? (MSR 2026, Drexel/Missouri S&T): 43.04%, lowest of 5. PR
3. Fix-related PRs unmerged (MSR 2026, Saskatchewan): 42.4% (Codex 81.6%, Devin 42.9%). PR
4. CI/CD configurations (MSR 2026, Trent): Copilot CI/CD changes merged +15.63 points more often than its other changes. PR
5. Security in the Age of AI Teammates (Information and Software Technology 2026, Notre Dame): security PRs merged 49.60%, lowest. PR
6. Rise of AI Teammates (Queen's, preprint): 35% (Codex 64%, Devin 49%)
7. Why Agentic-PRs Get Rejected (Kyushu/Waterloo, preprint): 55.0%
8. How Do AI Coding Agents Contribute (Polytechnique Montréal, preprint): estimated 59.6%
9. Merged, Not Measured (preprint): performance fixes accepted 50%, falling from 61% to 42% as repository size grows
10. Who Finishes the Job? (EMSE submission, preprint): Copilot self-fixes about 95% of the follow-ups on its merged PRs
11. Not All Agents Are Equal (Texas Tech, preprint): most human reviews and change requests
12. Trust but Verify? (UTSA, preprint): security smell in 45.5% of PRs, the highest (average 38.9%)

## Other (not counted, 6)
- All Smoke, No Alarm: 26% of test patches had strong oracles.
- Habituation at the Gate: reviewer approval rose 9.1 points with exposure.
- What Makes a GitHub Issue Ready for Copilot? (prediction model).
- Why Are Agentic PRs Merged or Rejected? (descriptive).
- AgentLogs (dataset only).
- NVD: about 25 CVEs (2025–26) naming Copilot in VS Code or Visual Studio, Copilot Chat, or Copilot CLI (for example CVE-2025-53773, CVE-2026-29783, CVE-2026-45033). None names the cloud agent.

## Not counted (affiliation or vendor)
- GitHub and Microsoft documentation and reports.
- 2604.00917 (GitHub co-author Rahul Pandita). Excluded for Copilot only.
- 2608.00101 Copilot production traces (Microsoft Azure Research).
- Out of scope and also Microsoft-authored: BC-Bench 2608.20851 (Copilot CLI versions), Building to the Test 2606.28430, Lights-off code review 2610.13668 (Microsoft Research), Subagents vs Skills 2609.09233 (Microsoft Research).
- Out of scope (other Copilot products): library migration with agent mode (peer-reviewed, 10.1145/3786167.3788411), Refused in Chat (Copilot Chat 0.30.3), HarnessSecurity-Bench, MOSAIC and Setup Complete (Copilot CLI 1.0.60), "Go Home Copilot" (code review).

## Citation gate / reading depth
- **Semantic Scholar:** the 8-minute retry for the Copilot, agent mode, CLI and Devin queries (from 20:30 EDT) returned only 429. The saved s2_cx2.json (100 hits) and OpenAlex (oa_copilot_agent, oa_cp_agentmode, oa_cp_cli, oa_cp_agentpr) were used, so the recheck note applies.
- **Reading:** targeted reads only (figures, affiliations, venue, versions) for 34 PDFs. Venues were confirmed through MSR 2026 headers and DOIs and the IST DOI.
- **Borderline?** No. The grade depends on missing versions and dates, not on the source count.

## Rules applied
- Developer-affiliated authors are excluded for that product (GitHub and Microsoft, including Microsoft Research).
- PR field studies count.
- Neutral wording for CVEs. The evidence score was not fitted to the grade range: 75 sits in the B guide (70–84) on its merits, because there are many sources but they are correlated, old and unversioned.

## Risks
- Most counted studies share the AIDev dataset, so they are not independent samples. Results could move once post-2025 data appears.
- The excluded CVEs could be read as relevant if the products share infrastructure. D3 addresses this.

## Decisions requested
- **D1 Scope:** cloud coding agent only (recommended). Alternatives:
  - (b) Add Copilot CLI. This adds versioned tests (mostly security) and about 3 CLI CVEs, and could reach A if enough performance tests qualify.
  - (c) The whole Copilot family including IDE agent mode. That is a different product mix, with about 25 CVEs and disputes well below 60.
- **D2 Category:** Coding agent; name "GitHub Copilot coding agent"; slug github-copilot-coding-agent.
- **D3 Disputes 60:** no in-scope CVE or legal action. IDE and CLI CVEs and the 2022 completions litigation are listed as out of scope and not scored.
- **D4 Affiliation:** exclude GitHub and Microsoft (including Microsoft Research) co-authored studies, including 2604.00917, for this entry.
- **D5 Completion 45:** acceptance of 35–68.0%, lowest or near lowest in most comparisons, and no benchmark.
- **D6 Adherence 50:** human-gated PRs, but the highest security-smell rate and the most review effort. There is no direct measure of out-of-scope actions.
- **D7 Evidence 75 / grade B:** 12 sources, 5 peer-reviewed, no version and no test within 12 months.
- **D8 Recheck note:** show "Citation check incomplete — recheck later."

## Devin batch refresh (for next candidate)
- OpenAlex: oa_devin2.json (2,047 hits from 2025, none of the top 100 titles names Devin; the useful Devin evidence is in the multi-agent PR studies). S2 Devin query was 429.
- Devin figures seen in the Copilot sources: 49%, 42.9%, 53.76%, 55.5%, 43.0%, 68.0% common window, 30% performance fixes.

## Draft files (private, superseded)
/workspace/private-drafts/copilot-agent.yaml, copilot-preview/github-copilot-coding-agent.html, build_preview_0044.py
