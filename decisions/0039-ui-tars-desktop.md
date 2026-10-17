# Decision 0039: UI-TARS Desktop (ByteDance) — Insufficient evidence

**Status: APPROVED by Remington, 2026-10-17** (D1–D4 approved; D5 not approved, Agent S unchanged). Batch 4 candidate #3 (0034). Category: Computer-use agent (0036).
Entry: agents/ui-tars-desktop.yaml and public/agents/ui-tars-desktop.html.

## Affiliation checks
- Developer: ByteDance (repo bytedance/UI-TARS-desktop, Apache-2.0, about 39.3k stars). The MIT AI Agent Index names the legal entity as Beijing Douyin Information Service Co., Ltd. The model is from ByteDance Seed.
- All ByteDance / ByteDance Seed papers are vendor sources: UI-TARS (2501.12326), UI-TARS-1.5 repo figures, and the UI-TARS-2 report (2509.02544). Not counted.
- TOCTOU paper (2603.00476): all four authors are at Ohio State. No ByteDance affiliation. Independent.
- GhostEI-Bench (2510.20333): authors are at SJTU, Shanghai AI Lab and HKU. "ByteDance Seed" appears only as a model-provider label (line 1422), not as an author affiliation. Independent, but it tests the model only.
- CUAHarm (2508.00935) and AgentHijack (2605.25707): no ByteDance authors found. They test the model only.
- Agentic Botnets (2607.07433): Tel Aviv University, Technion and Intuit. No ByteDance authors.
- No counted or listed study has ByteDance co-authors. The vendor papers are the only ByteDance work.

## Proposed score
- Overall score: none. Evidence grade: **Insufficient evidence**.
- Reason: there is 1 counted independent test of the named product, below the 3-source minimum.
- All four factors are unscored, with notes only (as in the Fellou and Open Interpreter entries).

## Counted independent sources (1)
1. **Atomicity for Agents / TOCTOU** (arXiv 2603.00476v1, 28 Feb 2026, Ohio State; preprint, not peer reviewed).
   - The authors ran 10 GitHub agents, including **UI-TARS-desktop** (the named app), on 9 synthesized DynWeb cases and 5 real websites.
   - In all 14/14 cases, UI-TARS-desktop could be made to act on a page that changed between when it looked and when it clicked. All screenshot-based agents behaved the same way.
   - Not stated: the app version and the model used. Repos were accessed 2025-12-27, so the test was likely around Jan 2026.
   - This is a security / adherence test, not a task-completion test.

## Other sources (not counted)
- **MIT 2025 AI Agent Index** entry (FAccT 2026, DOI 10.1145/3805689.3806728).
  - It documents the product's features, not its performance.
  - It lists "None found" for a safety framework, third-party testing and risk evaluations.
  - It rates the app at L4 autonomy and notes that user input is needed for logins and payments.
- **CVE-2026-81735** (NVD published 27 Aug 2026; status Deferred; GHSA-p68p-fq8j-3639, Critical, Unreviewed).
  - The @agent-infra MCP command and filesystem servers bound to all network interfaces without authentication, which allowed remote command execution.
  - CVSS 3.1 / 4.0 score of 10.0 from VulnCheck.
  - Commit c2ad42e (PR #1918, 1 Jul 2026) changed the default bind to 127.0.0.1 but added no authentication. The change is in v0.3.1 (8 Oct 2026) and not in v0.3.0.
  - v0.3.1 also added loopback-by-default, an access token once off loopback, Host checks, CSRF protection, a CORS allowlist and an iframe sandbox fix to the Agent TARS server.
- **Agentic Botnets / HalluSquatting** (arXiv 2607.07433).
  - When asked how to install trending repos, language models invented GitHub names. For ui-tars-desktop, registering the top five invented names would catch 84% of the invented install links.
  - This is a supply-chain risk to users. It does not test the app.
- **LexBench-Browser** (Lexmount) supports Agent TARS but has published no result. Discussion #1889 (12 May 2026) invited ByteDance to submit one.

## Not counted
- Vendor results:
  - UI-TARS paper.
  - UI-TARS-1.5: OSWorld 42.5, WAA 42.1.
  - UI-TARS-2: OSWorld 47.5, WAA 50.6, AndroidWorld 73.3, Online-Mind2Web 88.2.
  - Leaderboard entries.
- Model-only tests (the model was tested, not the Desktop app; named-product caution):
  - CUAHarm: UI-TARS-1.5 completed 42.3% of harmful tasks.
  - GhostEI-Bench (ICLR 2026): UI-TARS-1.5-7B.
  - AgentHijack: UI-TARS model.
- Mentions only, no test:
  - nanoMuse (2610.08699): ported the computer operator from UI-TARS-desktop.
  - Code as Agent Harness (2605.18747): survey.
  - AgentSWE (2610.13361): lists UI-TARS-desktop as a target to rebuild.
  - Malva (Figshare 10.6084/m9.figshare.32838281): anonymous, unreviewed dataset of defects mined from 40 apps. The per-app files could not be retrieved because Figshare's API returned no data.
- GitHub issue #1854: an unverified "audit" offered as a $29 paid report. Not credible as evidence and excluded.
- Informal blogs (segmentfault/juejin, CSDN, note.com v0.2.4 test): not systematic.

## Citation gate (PROCESS.md)
- **Semantic Scholar** returned 429 (rate limited) continuously from 16:40:23 to 17:14:47 ET, more than 30 minutes, with one exception.
  - At 17:04:55 ET a single 200 came back for "UI-TARS Desktop agent evaluation". It was lost because of a bug in my retry script: an empty marker file made the script re-query and overwrite the result with a 429.
  - Disclosed here for transparency. No S2 result was used.
- **OpenAlex full-text fallback**, started after the full wait. Searches:
  - "UI-TARS-desktop" and "UI TARS Desktop": 5 hits each.
  - "TARS desktop": 7.
  - "bytedance/UI-TARS-desktop": 2.
  - "Agent TARS CLI": 0.
  - "agent-tars": noise apart from the AI Agent Index.
- I read the full text of all non-noise hits.
- arXiv's export API timed out, and its site search covers only titles and abstracts.

## What the rules say
- Fewer than 3 counted independent sources means Insufficient evidence, with no overall score.
- Vendor and leaderboard results are not counted, and the named product must be tested (0036).
- Category boundary (0036): "An agent that operates a desktop or apps through the screen ... is a Computer-use agent."

## Risks and uncertainties
- OpenAlex full-text coverage is incomplete. Studies that tested the app might exist but not be indexed. S2 was unavailable.
- The TOCTOU paper is a preprint and does not state the app version or the model.
- Counting TOCTOU as a counted source is a judgment call (see D3). It does not change the outcome.
- **Consistency flag:** TOCTOU also tested Agent S (14/14 triggered). The live Agent S entry says "No independent prompt-injection or safety test of Agent S was found."
  - That may need a correction, which would be a separate decision. Its adherence note and possibly its score of 35 would change.
  - Not touched here.
- The CVE affects @agent-infra MCP servers used by Agent TARS rather than the Electron GUI app, so how it is scoped depends on D2.

## Decisions (outcome)
- **D1 (APPROVED) Category:** Computer-use agent, not Coding agent. Its main documented use is operating the desktop and browser through screenshots, mouse and keyboard.
- **D2 (APPROVED) Scope:** Cover the UI-TARS Desktop app, v0.2.x–v0.3.1, with Agent TARS (CLI and Web UI) included, because both ship from the same repo and release. The UI-TARS models are not covered except as context.
  - Alternative: Desktop app only, which moves the CVE to "related component".
- **D3 (APPROVED) Treatment of TOCTOU:** count it as the 1 independent test of the named product (security/adherence), or list it as "other" (the Fellou precedent for demonstrations).
  - The outcome is unchanged either way. Recommended: count it, because it is a systematic, reproducible test of the named app.
- **D4 (APPROVED) CVE wording (neutral):** "CVE-2026-81735: MCP command and filesystem servers in the @agent-infra packages bound all network interfaces without authentication, allowing remote command execution. CVSS 10.0 (VulnCheck); NVD status Deferred. Default changed to localhost in v0.3.1; no authentication added to those servers."
- **D5 Agent S follow-up (NOT approved; Agent S entry unchanged):** whether to open a separate correction for Agent S based on TOCTOU.

## Recommendation
Publish as Insufficient evidence (Computer-use agent), with the TOCTOU result, the CVE and the Agent Index noted. Re-check when independent app-level benchmarks appear, for example a LexBench-Browser submission.

## Plain-English summary
UI-TARS Desktop is ByteDance's free app that lets an AI model operate your computer by looking at the screen. Almost all published results test ByteDance's model rather than this app, or come from ByteDance itself. The one independent test of the app found that a web page that changes at the right moment can trick it into clicking the wrong thing in every case tried. A critical security flaw in companion tool servers was partly fixed in October 2026. There is not yet enough independent evidence for a score.
