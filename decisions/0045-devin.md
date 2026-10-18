# Decision 0045: Devin (Cognition) — 50 / B

**Status: APPROVED by Remington, 2026-10-17** (D1–D8 approved). Entry: agents/devin.yaml and public/agents/devin.html. This completes Batch 4.

**D7 as approved (supersedes the draft below):** the Anthar Study (Deccan AI industry report) is counted, with its disclosure. The Answer.AI month-long review is moved to Other (not counted), following the Fellou precedent that informal reviews are context only. Final counts: 12 independent performance sources, 5 peer-reviewed, 7 other. Evidence quality 75, grade B, overall 50, all unchanged. Draft references below to "13 counted" and to Answer.AI as counted source 12 are superseded by this paragraph.

Category: Coding agent. Proposed slug: devin. Visible note: "Citation check incomplete — recheck later."

## Proposed score
| Factor | Weight | Score |
|---|---|---|
| Completion rate | 30% | 40 |
| Disputes | 20% | 45 |
| Adherence to limits | 25% | 40 |
| Evidence quality | 25% | 75 |

0.30×40 + 0.20×45 + 0.25×40 + 0.25×75 = 49.75 → **50**.

Grade **B**: 13 counted sources and 5 peer-reviewed, but no counted test states a version or falls within 12 months (the newest data is from July 2025). This fails the A condition.

Comparison:
- Codex (62/A) has versioned benchmarks and the highest acceptance.
- Copilot (57/B) has the same field-study base. Devin's acceptance is similar, but Devin has more dispute and security findings in scope.
- Claude Code (55/A) has versioned benchmarks.

Devin ranks below all three.

## Scope (D1)
The Devin cloud agent from its March 2024 announcement through Devin 2.x (2.0 released April 2025). No study states a version, and the AIDev window (Dec 2024 to Jul 2025) spans late 1.x and 2.0. Excluded: Windsurf (acquired by Cognition in July 2025), DeepWiki and other Cognition products.

## Counted (independent performance, 13; peer-reviewed 5)
1. Comparing AI Coding Agents (MSR 2026): 68.0% in the common May–Jul 2025 window. The only agent with a rising trend (+0.77 points per week). PR
2. Where Do AI Coding Agents Fail? (MSR 2026): 53.76%. PR
3. Fix-related PRs unmerged (MSR 2026): 42.9%. PR
4. CI/CD configurations (MSR 2026): changed CI/CD files the most (4.83%). PR
5. Security in the Age of AI Teammates (Information and Software Technology 2026): security PRs merged 52.12%. PR
6. Rise of AI Teammates (preprint): 49%
7. Why Agentic-PRs Get Rejected (preprint): 55.5%. 32.1% of rejections were auto-closes for inactivity
8. How Do AI Coding Agents Contribute (preprint): 43.0%, lowest of 5
9. Merged, Not Measured (preprint): 30% for performance fixes, lowest. Near zero in Jan–Apr 2025
10. Not All Agents Are Equal (preprint): reverted 14.5% vs human 11.5% (odds ratio 1.31)
11. Trust but Verify? (preprint): security smell in 39.7% of PRs (average 38.9%)
12. Answer.AI "Thoughts On A Month With Devin" (blog, Jan 2025, Devin 1.x): 3 of 20 tasks succeeded, 14 failed, 3 inconclusive
13. Anthar Study (Deccan AI, industry report, 2025): highest correctness on Python, 95.3% correlation with reference patches. Possible cross-task context leakage. Disclosure: Deccan AI sells evaluation data.

Dropped: Who Finishes the Job? (no Devin figure extracted under targeted reads).

## Other (not counted, 6)
- CVE-2024-56083 (CVSS 8.1): a VS Code live-share URL could give write access to code. Fixed 2024-12-12.
- Embrace The Red (Aug 2025): prompt injection led Devin to run downloaded code, leak secrets and expose ports. Reported to Cognition on 6 April 2025; the researcher says follow-up questions went unanswered.
- 2024 launch-demo dispute (Pragmatic Engineer write-up of the Internet of Bugs analysis and the client's statement; Cognition's reply that Devin "is often inefficient and makes mistakes").
- The original Cognition Upwork video.
- All Smoke, No Alarm: 26% of test patches had strong oracles.
- Habituation at the Gate: +3.8 points, not significant.

## Not counted (vendor)
- Cognition's launch post and technical report (self-reported SWE-bench 13.86% on a 25% subset).
- Cognition's later performance reviews and customer figures.
- No counted study has Cognition authors. Targeted checks of the 34 PDFs found none.

## Citation gate / reading depth
- **Semantic Scholar:** the 8-minute retry (4 Devin queries, from 20:42 EDT) returned only 429. The saved s2_cx3.json contained no relevant Devin hits. OpenAlex oa_devin.json and oa_devin2.json (2,047 hits) found no Devin-specific evaluation. The recheck note applies.
- **Web:** web search found the Answer.AI, Anthar, Embrace The Red and demo-dispute sources.
- **Reading:** targeted reads only, reusing the 34 PDFs from 0044.
- **Borderline?** No. With 13 sources, removing Anthar and Answer.AI still leaves 11, so the grade stays B. Score sensitivity: completion ±5 moves the overall by ±1.5.

## Rules applied
- Vendor self-reports are not counted.
- Developer-affiliated studies are excluded for that product. None was found for Devin.
- PR field studies count.
- Industry evaluations count, with disclosure.
- Neutral wording for the dispute and security findings.
- The evidence score was not fitted to the grade: 75 matches Copilot's, on the same base plus two non-peer-reviewed, older tests.

## Risks
- The shared AIDev dataset is the same caveat as Copilot.
- The Answer.AI blog and the Anthar industry report are not peer-reviewed and pull in opposite directions.
- The security findings are a researcher's report; fix status is unconfirmed.
- The demo dispute is from 2024 and predates GA.

## Decisions requested
- **D1 Scope:** Devin cloud agent, 1.x through 2.x, as one entry. Windsurf, DeepWiki and other Cognition products are excluded.
- **D2 Category, name and slug:** Coding agent; "Devin (Cognition)"; slug devin.
- **D3 Disputes 45:** counts the 2024 demo dispute (described neutrally, with sources), the fixed CVE-2024-56083, and the unanswered April 2025 disclosure per the researcher. No legal action.
- **D4 Vendor:** the SWE-bench 13.86% self-report and Cognition reviews are not counted. Affiliation check: no Cognition authors.
- **D5 Completion 40:** acceptance of 30–68.0%, usually among the lowest, plus 3 of 20 in Answer.AI and a positive Anthar result.
- **D6 Adherence 40:** prompt-injection exfiltration and port exposure, unrestricted internet by default (2025), higher reverts, and the most CI/CD edits.
- **D7 Evidence 75 / grade B:** count Answer.AI (blog) and Anthar (industry, with disclosure) as independent performance sources. The alternative is to treat them as other, which gives 11 sources, still B, overall unchanged.
- **D8 Recheck note:** show "Citation check incomplete — recheck later."

## Draft files (private, superseded)
/workspace/private-drafts/devin.yaml, devin-preview/devin.html, build_preview_0045.py
