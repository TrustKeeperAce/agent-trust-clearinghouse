# Decision 0055: Browser Use, TOCTOU study

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1a count Atomicity for Agents (8 counted, 3 peer-reviewed; Ohio State shared institution disclosed); D2 no score or grade change (51 / B); D3 drafted wording, 0052 recheck note kept; D4 rollout. **Resolves 0050 D7** (Browser Use follow-up, previously pending).

## Plain-English terms
- **TOCTOU ("time of check to time of use"):** the web page changes between the moment the agent looks at it and the moment it acts, so the action lands on something it did not intend.
- **Counted source:** an independent test that counts toward the evidence grade.
- **Grade A:** needs all of these:
  1. 7 or more counted sources;
  2. 3 or more of them peer-reviewed;
  3. a test within the last 12 months that states the version tested.

## The study
**Atomicity for Agents: Exposing, Exploiting, and Mitigating TOCTOU Vulnerabilities in Browser-Use Agents** (arXiv 2603.00476v1, 28 Feb 2026).
- **Authors:** Linxi Jiang, Zhijie Liu, Haotian Luo and Zhiqiang Lin, all at The Ohio State University.
- **Funding:** NSF award CNS-2112471 and a Schmidt Sciences Safety Science Award.

**Independence**
- No Browser Use developer is an author (the cited developers are Magnus Müller and Gregor Žunič), and no funding comes from Browser Use.
- Shared institution only: Online-Mind2Web, which is already counted for Browser Use, is also from Ohio State. There is no author overlap. Disclose it; it is not grounds to exclude (same rule as 0049 and 0054).

**Peer review:** no. It is a preprint, so peer-reviewed stays at 3.

**Version and date**
- The Browser Use version is not stated. The repository is cited as "Browser use: Enable ai to control your browser, 2024. Accessed: 2025-12-27."
- Test date: about late December 2025 to February 2026, which is inside the 12-month window.
- With no stated version, it does not meet A condition 3.
- This matches how the paper was recorded in UI-TARS (0039) and Agent S (0050): version unstated, test date about January 2026.

**What was tested**
- 10 open-source browser and computer-use agents on 14 cases: 9 synthesized pages and 5 real websites.
- The page changes between the agent's check and its action in three ways:
  - Type I: layout or UI changes.
  - Type II: data updates.
  - Type III: expiring states.

**Result for Browser Use** (my reading of Table 3, which is printed column by column)
- The vulnerability was triggered in **9 of 14 cases**:
  - all 7 Type II cases (S4–S7, R3–R5);
  - both Type III cases (S8–S9).
- It was not triggered in the 5 Type I layout-change cases (S1–S3, R1–R2). That matches the paper's text: DOM-based agents resisted UI changes, but "no design prevents failures under Type II data changes and Type III expiring state interactions."
- By comparison:
  - UI-TARS Desktop and Agent S were triggered in all 14 cases.
  - The paper's own mitigation was built on a different framework (openai-cua-sample-app), not Browser Use.

## Effect

| | Before | After |
|---|---|---|
| Counted performance sources | 7 (4 task-performance, 3 security) | **8** (4 task-performance, 4 security) |
| Peer-reviewed | 3 | 3 |
| Recent test that states the version | none | none (TOCTOU states no version) |
| Grade | B | **B** (A condition 3 still not met) |
| Scores (completion / disputes / adherence / evidence) | 40 / 50 / 30 / 85 | unchanged |
| Overall | 0.30×40 + 0.20×50 + 0.25×30 + 0.25×85 = 12 + 10 + 7.5 + 21.25 = 50.75 → **51** | **51** |

**Does any rule force a change? No.**
- **Grade:** grade A needs a recent test that states the version, and this one does not, so B stands. The check_scores note will read "2 recent test(s), version unstated". It stays a warning, not an error.
- **Factor scores:** these are judgment calls; no formula ties them to the source count.
  - **Adherence:** the study adds more negative security evidence. Adherence is already low at 30, on the basis of the allowed_domains bypass and prompt-injection results, so this confirms the score rather than forcing a change. Agent S was handled the same way in 0050, where adherence stayed 35 and evidence stayed 70.
  - **Evidence:** 85 is above the B guide band (70–84). That is an existing, accepted check_scores warning. The guide is advisory, and no rule requires lowering it.
- **check_scores:** expected to show 0 errors and 7 warnings, the same as now.
- **Recheck note:** the 0052 "Citation check incomplete" note stays. AgentTell, Privacy Practices of Browser Agents, ceLLMate and the controlled-interventions paper are still unscreened.

## Decision items
- **D1. Count the TOCTOU study for Browser Use.**
  - **D1a (recommended):** count it: 8 counted, 3 peer-reviewed. Disclose the shared Ohio State institution.
  - **D1b:** list it as other, not counted. This would be inconsistent with UI-TARS and Agent S.
- **D2. No score or grade change.** Stays 51/B. Recommended.
- **D3. Wording below. Keep the 0052 recheck note.** Recommended.
- **D4. Rollout:**
  1. Edit the YAML and page in place.
  2. Write decision record 0055, add one changelog row, and mark 0050 D7 as resolved by 0055 in the 0055 record.
  3. Run check_scores, check_links, overflow and axe.
  4. Commit and push, then write manifest-0055.
  5. You deploy.
  6. Add the LOG note.
  - No index or llms.txt change, because the score and grade are unchanged.

## Exact wording

**Source row** (kind: independent performance; peer_reviewed: false; version_tested: unstated; test_date: about Jan 2026 (repository accessed 2025-12-27)):
> Atomicity for Agents (Ohio State University; preprint, Feb 2026): tested 10 open-source browser- and computer-use agents on 14 cases where a web page changes between the agent's check and its action (9 synthesized pages, 5 real sites). For Browser Use, the vulnerability was triggered in 9 of 14 cases (all data-update and expiring-state cases) and not in the 5 layout-change cases. Security test, not task completion

**Adherence note** (insert before "Judgment call."):
> In a study of page changes between an agent's check and its action (Atomicity for Agents, Ohio State, preprint 2026), the vulnerability was triggered in 9 of 14 cases for Browser Use.

**Evidence note:**
- Replace "Seven independent performance sources (four task-performance, three security)" with "Eight independent performance sources (four task-performance, four security)".
- Replace "two run in late 2025/2026" with "three run in late 2025/2026".

**Disclosure** (in the uncertainties list, since the entry has no disclosure section):
> Atomicity for Agents and Online-Mind2Web are both from Ohio State University; there is no author overlap.

**Summary:**
- Replace "Independent security studies (VPI-Bench, ICLR 2026; two preprints) found it often followed instructions hidden in web pages," with:
  > Independent security studies (VPI-Bench, ICLR 2026; three preprints) found it often followed instructions hidden in web pages and could be misdirected when a page changed between check and action,

**Scoreline:**
> Overall score: 51 · Evidence grade: B · Independent sources: 8 performance, 3 other

**Count note** (unchanged in substance):
> Nine source rows record eight counted studies: the Holistic Agent Leaderboard paper and its leaderboard page are counted once.

**Decision records line:** add "0055 (TOCTOU study)".

**Changelog row:**
> 2026-10-17 · 0055 · Browser Use: Atomicity for Agents (TOCTOU security study, Ohio State, preprint 2026) added as a counted source; 8 counted (3 peer-reviewed). Vulnerability triggered in 9 of 14 test cases. Scores and grade unchanged (51, B).

## Queue
- 0050 D7 is resolved by this packet once approved.
- Remaining 0052 follow-ups: Perplexity, Gemini/OpenAI Deep Research, Consensus, Google DeepMind SAFE, Julius AI, and the other Browser Use candidates.
