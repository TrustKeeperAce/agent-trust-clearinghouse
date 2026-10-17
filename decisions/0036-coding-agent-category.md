# Decision 0036: New category "Coding agent"

**Status: APPROVED by Remington, 2026-10-17** (D1–D4). The 0034 shortlist is confirmed; private research may begin with #1 OpenHands.

## Proposed change
Add **Coding agent** to the methodology's Categories list:
Research; Verification; Browser/web agent; Computer-use agent; Data science agent; **Coding agent**; Data enrichment; Negotiation; Simple analysis.

## Definition (proposed public wording)
> **Coding agent:** an agent that works in a software repository or development environment to write, edit, run and test code over multiple steps, with limited step-by-step supervision. Examples: resolving an issue, making a multi-file change, or fixing failing tests.

## Boundaries
| Situation | Category |
|---|---|
| Agent edits and runs code in a repo or terminal toward a software change | **Coding agent** |
| Agent operates a desktop or apps through the GUI (clicks, typing), even if it sometimes opens an IDE | Computer-use agent |
| Agent writes code mainly to analyse data or build models and reports results (notebook or data workflow) | Data science agent (e.g. Data Interpreter) |
| Agent runs code locally for general tasks through natural language, without a repository workflow focus | Simple analysis (e.g. Open Interpreter, as now) |
| Inline code completion or chat-only code suggestions with no autonomous multi-step execution | Out of scope (not an agent under this directory) |

If a product spans several categories, the decision packet picks the category that matches its main documented use. Mixed products, such as a coding agent with browser tools, stay in one category.

## Evidence cautions (applying the existing rules; no rule changes)
1. **Vendor-reported benchmark results are not counted.** This includes SWE-bench (Verified, Lite, Multimodal, Pro), Terminal-Bench, Aider-style leaderboards and similar results that the developer reports, runs or self-submits. They are listed as vendor sources.
2. **The named product must be tested.** A study that tests a **model** inside a generic or third-party scaffold does not count for a product built on that model. Example: a study of Claude in mini-SWE-agent is not a test of Claude Code. A study counts only if it runs the named agent (framework, CLI or product) itself.
3. **Maintainer-verified leaderboards are other sources.** Leaderboards where benchmark maintainers check submissions (for example SWE-bench "verified" submissions or HAL entries) are listed as other sources, not counted, following the OSWorld-Verified precedent (0025). A peer-reviewed or preprint study by the maintainers that runs the agent themselves can count, subject to the affiliation checks.
4. **Affiliation checks.** Benchmark and agent authors often overlap (for example the SWE-bench, SWE-agent and HAL groups at Princeton). Shared authors with the developer mean the source is excluded for that product, as with CAP for Fellou. Competing-method authors count with disclosure.
5. **Version and test date matter.** Coding agents change monthly. Each counted source records `version_tested` and `test_date` (Decision 0033). The A-grade current-version condition needs a stated version or tier, or a dated test of the hosted current product (Decision 0035 approach).
6. **Contamination and benchmark quality.** Known contamination or flawed-task critiques (for example audits of SWE-bench task validity) are reported neutrally as context and do not count as performance tests.
7. **Security and dependency notes.** Neutral wording for CVEs, prompt-injection or sandbox findings (CVSS attributed, fix status, no exploit links), as on existing entries.
8. **Productivity studies.** Randomised or controlled developer studies (for example time-to-complete with or without the agent) can count as independent performance sources when they name and use the agent, with version and date recorded.

## What would change if approved
- methodology.html: the Categories list gains "Coding agent", with the one-sentence definition and a pointer to the boundaries.
- docs/PROCESS.md: evidence cautions 1–8 added as internal guidance.
- No existing entry changes category. Checked: Open Interpreter stays Simple analysis, Data Interpreter stays Data science agent, Agent S stays Computer-use agent.
- Changelog row and LOG entry when published. Nothing is published until you approve.

## Risks and uncertainties
- Many candidates may end up Insufficient because vendor-run benchmarks dominate. That is expected under the rules.
- The line between coding and computer-use agents can blur, for example for terminal agents that also drive a browser.
- Studies at the model level are common and easy to misread as product tests; caution 2 needs careful application.

## Decisions requested
- D1: Add the "Coding agent" category with the definition above.
- D2: Adopt the boundary table.
- D3: Adopt evidence cautions 1–8 as internal guidance under the existing rules.
- D4: After approval, confirm the Batch 4 shortlist (0034) to start private research on #1 OpenHands.
