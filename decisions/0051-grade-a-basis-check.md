# Decision 0051: Grade-A basis check

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1 confirm A (OpenAI Codex, OpenHands, Claude Code); D2 Elicit E1 (keep A; date window and uncertainty line); D3 Aider A1 (keep A; inferred-date note); D4 Sifting the Noise peer-reviewed for Aider (5 → 6), wording fix, evidence stays 80; D5 warnings accepted; D6 rollout. D7 backfill flags move to 0052. Part of the consistency pass. Reference date: 2026-10-17, so the 12-month window starts on 2025-10-17.

## What was checked
- **Rule (methodology, 0010/0025):** grade A needs all three of the following.
  - (1) 7 or more counted independent sources.
  - (2) 3 or more of them peer-reviewed.
  - (3) At least one test within the last 12 months that states the version tested (0025 clarification: a current-version test shown by the evidence).
  - If (1) is met but (2) or (3) fails, the grade is B.
- **Entries graded A today (all of them):** Elicit 68, OpenAI Codex 62, OpenHands 61, Claude Code 55, Aider 52.
- **Method:**
  - Counts come from the YAML (check_scores agrees).
  - Condition (3) was checked against the source text: a targeted re-read of the version and date passages in local copies or the publisher page, today.
  - No evidence scores were changed.

## Results by entry

### Elicit — 68 / A
- **(1) 7 counted. (2) 6 peer-reviewed.** Pass.
- **(3) Recent versioned test: Wei et al.**, "Evaluation of Elicit as an adjunct search, screening, and data extraction tool for systematic reviews".
  - medRxiv preprint, posted 5 Oct 2026, CAMH / University of Toronto: https://www.medrxiv.org/content/10.64898/2026.10.02.26364621v1
  - Methods: "we purchased a paid ("Pro-tier") Elicit subscription between December 2025 and May 2026".
  - Elicit screening functions: "At the time of the study (April 2026), Elicit could output 1000 studies…"
  - Limitations: "this project was completed between December 2025 and April 2026". The paper is internally inconsistent on the end month (May vs April). Both fall within the window.
  - The test is within 12 months: Pass on date.
- **Version:** Elicit is a hosted web service with no public version numbers. The study states the tier (Pro) and the dates of use, not a release number.
  - 0017 accepted "Pro tier, Dec 2025–May 2026 (current)" as the current-version test. check_scores also treats "Pro tier" as a stated version.
  - **Judgment point:** for hosted services, a dated test of a named tier counts as a "stated version". This matches how other hosted entries were read (dated product or tier, for example Gemini Deep Research by model generation).
- **Other sources:** none satisfy (3). Lau et al. states "Elicit Pro (Review mode)" but no test date. Andersen (July 2024) and Bianchi (Aug–Sep 2024) are older than 12 months.
- **Outcome:** passes on the 0017 reading. A rests on one preprint. Under a strict reading (a release number is required) Elicit would be B: there is no other path to A, and 68 is unchanged because the evidence score is not touched.
- **Side note (not acted on):** Wei et al. cite further independent Elicit evaluations not in the entry: Mazzali et al., BMC Med Res Methodol 2026; Meliante et al., JMIR AI 2025; Hilkenmeier et al., Soc Sci Comput Rev 2025; Spillias et al., Environ Evid 2025. A citation backfill could add sources, but not a new versioned test.

### OpenAI Codex — 62 / A
- **(1) 26 counted. (2) 5 peer-reviewed.** Pass.
- **(3) Recent versioned tests:**
  - **WideSWE** (Zhejiang, Tsinghua; preprint Sept 2026; arXiv 2609.33382), §3 Experimental Setup: "The scaffolds are Codex CLI (v0.147.0) and Claude Code (v2.1.139)."
  - **Timeline-Bench** (TensorTest; preprint Sept 2026; arXiv 2609.35143), setup: "GPT-6 Astra in Codex CLI 0.155.1 … We use unmodified releases of all three harnesses". Its reference list has Sept 2026 access dates.
  - Also in the entry: RuBench, Codex CLI 0.142.5/0.144.0, July 2026; SWE-Duel, Codex CLI 0.62, 2026.
- **Outcome:** passes with several independent recent versioned tests. All are preprints; the rule does not require the versioned test to be peer-reviewed.

### OpenHands — 61 / A
- **(1) 11 counted. (2) 6 peer-reviewed.** Pass.
- **(3) Recent versioned test: PBT-Bench** (Jing, Wang, Zhang, Du; University of Washington; arXiv 2605.15229 v4, revised 6 Oct 2026).
  - The arXiv comment says "Accepted at NeurIPS 2026, Evaluations & Datasets Track (poster)", so it is peer-reviewed.
  - Agent scaffold section: "All models run inside the OpenHands SDK v1.11.5 with the standard tool set … and a maximum of 200 tool-call iterations."
  - Exclusion analysis: "This flags 106 of the 1,500 July OpenHands trajectories".
  - That places the runs in July 2026 (v1 was May 2026), within 12 months. Pass.
- **Also:** Overeager Coding Agents (preprint May 2026), Table "Agent product (version)": "OpenHands 0.59.1".
- **Caveat (already in the entry's uncertainties):** the SDK version (1.11.5) differs from the app release line (1.27.1, 12 Oct 2026). The rule asks for a stated version, which is met. Whether an SDK test represents the app is noted, not disqualifying.
- **Outcome:** passes. The basis is peer-reviewed and versioned.

### Claude Code — 55 / A
- **(1) 15 counted. (2) 6 peer-reviewed** (after 0049). Pass.
- **(3) Recent versioned tests:**
  - **Tool-surface ablation** (RIT; preprint July 2026; arXiv 2607.10569): "(model claude-sonnet-4-6, Claude Code 2.1.139)".
  - **Red-Teaming Coding Agents** (HKUST, Fudan; ISSTA 2026, peer-reviewed; arXiv 2509.05755, mid-2026 revision), Table 2: "Claude Code [6] Old New v2.0.37 v2.1.138". The 2.1.138 runs are the 2026 revision.
  - **Overeager Coding Agents** (preprint May 2026): "Claude Code 2.1.117".
- **Outcome:** passes, including one peer-reviewed versioned recent test.
- **Side note (not acted on):** WideSWE (Claude Code v2.1.139, Sept 2026) and Timeline-Bench (Claude Code 2.1.278) also test Claude Code but are not in its entry. They would be candidates for a later citation backfill and would not change the grade.

### Aider — 52 / A
- **(1) 8 counted. (2) 5 peer-reviewed** in the YAML. Pass.
- **(3) Recent versioned test: Sifting the Noise** (Xiong and Zhang, Monash University; arXiv 2601.22952).
  - "Agentic Frameworks. We then provided these aggregated findings to three LLM-based agent frameworks: Aider v0.86.1, OpenHands Agent SDK v1.5.2, and SWE-agent commit 1d3cfb".
  - **Version:** stated. Pass.
  - **Test date: not stated in the paper.** The available bounds are:
    - Aider v0.86.1 was tagged on 13 Aug 2025 (GitHub, commit date of the tag).
    - Reference access dates are 2025-12-14 (aider.chat, CodeQL) and 2026-01-30 (NVD).
    - The paper was received 2026-01-30 and accepted 2026-06-25 (from the footer), and arXiv v1 was posted in January 2026.
    - So the runs happened between 13 Aug 2025 and 30 Jan 2026. The 0041 entry's "Dec 2025 to Jan 2026" is an inference from the access dates.
    - The window opens on 2025-10-17. If the runs were before that, condition (3) fails.
  - **New fact found in this check:** Sifting is now **peer-reviewed**. It appears in Proc. ACM Softw. Eng. Vol. 3, ISSTA, Article ISSTA009 (October 2026), doi:10.1145/3832100.
    - The Aider YAML still says "preprint v3 July 2026, venue unconfirmed".
    - Peer-reviewed count 5 → 6, so (2) is unaffected.
    - The 0041 evidence note says the A "rests on a single recent versioned test, which is a preprint". That wording is now inaccurate.
  - **Other Aider tests:**
    - **SecureVibeBench** (Aider 0.86.1, preprint v5 June 2026) has no test date; its earlier versions were 2025.
    - **MT-Sec** (v0.82.1), **GitTaskBench** (v0.84.1.dev, 2025-07) and **SEC-bench** (0.82.0) are older than 12 months or undated.
- **Outcome:** passes only on the inference that the runs were after 17 Oct 2025. The access dates support that (Dec 2025 – Jan 2026), but it is not stated. Under a strict reading (an explicit test date is required), Aider would be B, with the score unchanged at 52.
  - Note that Aider's evidence score of 80 already sits in the B guide range (70–84). That is the cause of its check_scores warning.
  - Under B, that warning would disappear. That is a side effect, not a reason to choose B.
- **Related flag (not acted on):** Sifting also tests the OpenHands Agent SDK v1.5.2 and SWE-agent commit 1d3cfb. Neither entry cites it. It is a candidate for a later backfill; for SWE-agent it would be a versioned test, but only if the date is shown to be recent.

## check_scores warnings (6) and what each means
1. **aider:** "evidence_quality 80 outside guide 85-100 for A". The evidence score sits below the methodology's suggested A band. This was deliberately approved in 0041 because the A rests on one recent versioned test. It is informational, not an error.
2. **browser-use:** "7+ sources, 3 peer-reviewed; current-version test within 12 months not shown by data (1 recent test(s), version unstated) - A/B is a judgment call". It has enough sources for A, but no recent test states a version. Graded B since 0035, consistent with the rule.
3. **browser-use:** "evidence_quality 85 outside guide 70-84 for B". The evidence score sits above the B band. It was kept at 85 when the grade moved to B in 0035, so the score was not fitted to the grade.
4. **devin:** the same A/B message as warning 2 (12 sources, 5 peer-reviewed, no recent versioned test). B is consistent with the rule.
5. **github-copilot-coding-agent:** the same as 4 (12 sources, 5 peer-reviewed). B is consistent.
6. **storm:** the same as 4 (7 sources, 5 peer-reviewed). B is consistent with the 0025 clarification.

**Summary of the warnings:**
- None is an error. Four say the data alone cannot settle A vs B; in each the published grade is B, which is the rule's default when (3) is not shown.
- Two say an evidence score sits outside the suggested band for its grade; both were approved explicitly and left as they are.
- Elicit and Aider pass the script because it reads "Pro tier" and "v0.86.1 / 2025-12 to 2026-01" as a recent version. The judgment points above are not visible to the script.

Not covered here: Browser Use TOCTOU (0050 D7) is still pending and not decided.

## What the rules imply, and options
- **Codex, OpenHands, Claude Code:** A is confirmed on stated versions and stated or clearly bounded recent dates. No change.
- **Elicit:**
  - Option E1 (recommended): keep A under the 0017 reading that, for a hosted service with no version numbers, a dated test of a named tier states the version.
  - Option E2: strict reading, change to B (68 unchanged; evidence 85 then sits above the B guide, as with Browser Use).
  - Either way, record the Dec 2025–April/May 2026 window in the source row.
- **Aider:**
  - Option A1 (recommended): keep A on the access-date evidence (Dec 2025 – Jan 2026), and add an explicit note that the test date is inferred and bounded 13 Aug 2025 – 30 Jan 2026.
  - Option A2: strict reading, change to B (52 unchanged).
  - In both options, correct the facts:
    - Sifting the Noise is peer-reviewed (ISSTA 2026, PACMSE), so the count goes 5 → 6.
    - The evidence-note wording "which is a preprint" goes.
    - The evidence score stays 80. The 0041 reason for 80 is still that the A rests on a single recent versioned test, which is unchanged. It is not raised now to fit the A band.

## Proposed text changes
- **Elicit, Wei et al. source row, test_date:** "2025-12 to 2026-04/05 (paper gives both)".
  - Add to the uncertainties: "Grade A rests on one recent test (Wei et al., preprint) that states the Pro tier and the dates of use; Elicit publishes no version numbers."
  - The score is unchanged.
- **Aider, Sifting row:**
  - Set peer_reviewed: true.
  - Change the note from "(Monash University et al.; preprint v3 July 2026, venue unconfirmed)" to "(Monash University; ISSTA 2026, Proc. ACM Softw. Eng. 3, ISSTA009)".
  - Set test_date to "unstated; between 2025-08-13 (v0.86.1 tag) and 2026-01-30 (submission); access dates Dec 2025–Jan 2026".
- **Aider, evidence note:**

  > Eight independent sources, six peer-reviewed (NeurIPS 2025, AAAI 2026, EMNLP 2026, ACL Findings 2026, ISSTA 2026, LLM4Code workshop at ICSE 2026). Stated versions are v0.82.0, v0.82.1, v0.84.1.dev and v0.86.1 (twice). Sifting the Noise tested v0.86.1; the test date is not stated, but its access dates (December 2025 to January 2026) place it within 12 months, so grade A. This score is below the methodology's suggested A range (85-100) because the A rests on a single recent versioned test whose date is inferred.

- **Aider, uncertainty:** add "Grade A depends on the inferred test date of Sifting the Noise; if it predates 17 October 2025, the grade would be B."
- **Pages:** the Aider counts line changes to 8 performance (6 peer-reviewed), with an Elicit uncertainty line, a changelog row, decision record 0051, and apply_design.py.

## Risks and uncertainties
- **Hosted products:** for hosted products (Elicit) "version" cannot mean a release number. The tier-plus-date reading is a precedent, not written methodology. A one-line methodology clarification could settle it, but that would be a rules change and is not proposed here.
- **Aider's grade** depends on an inferred date. A strict reader could call it B.
- **Single-preprint A:** Elicit's A rests on a single preprint. That is allowed by the rule (peer review is required only for the count of 3), but it is thin.
- **Source excerpts:** quotes come from local text extractions (arXiv/ACM PDFs) and the medRxiv full-text page as fetched today. Page and section locations are given where the extraction preserves them.
- **Backfill not done:** the candidate sources noted above (Elicit citations; WideSWE and Timeline-Bench for Claude Code; Sifting for OpenHands and SWE-agent) are not screened. They would not reduce any grade.

## Recommendation
Approve:
- Codex, OpenHands and Claude Code: A confirmed, no change.
- Elicit: keep A (E1), recording the dates and the basis.
- Aider: keep A (A1), correcting Sifting to peer-reviewed (5 → 6) and making the inferred date explicit, with the evidence score kept at 80.

No score changes. Reason: every A entry meets (1) and (2). Condition (3) is met on stated versions and dates for three entries, and on documented, previously approved readings for two. Those readings are now disclosed on the pages.

## Decisions requested
- **D1:** confirm A for OpenAI Codex (WideSWE v0.147.0, Sept 2026), OpenHands (PBT-Bench SDK v1.11.5, July 2026, NeurIPS 2026) and Claude Code (2.1.139 July 2026; 2.1.138 ISSTA 2026). No change.
- **D2 Elicit:** E1 keep A on the tier-plus-date reading (recommended), or E2 change to B (68 unchanged). Record the Wei et al. date window and add the uncertainty line.
- **D3 Aider grade:** A1 keep A with an explicit inferred-date note (recommended), or A2 change to B (52 unchanged).
- **D4 Aider facts:** record Sifting the Noise as peer-reviewed (ISSTA 2026, PACMSE; doi 10.1145/3832100), peer-reviewed 5 → 6, updating the evidence-note wording. Evidence score stays 80 (overall 52).
- **D5 Warnings:** accept the six check_scores warnings as explained. No change.
- **D6 Rollout:**
  - Elicit and Aider YAML and pages (apply_design.py), decision record 0051, one changelog row.
  - Run check_scores, check_links, overflow and axe; commit and push; manifest plus files.json. You deploy.
- **D7 Backfill flags (note only):** Elicit citations in Wei et al.; WideSWE and Timeline-Bench for Claude Code; Sifting for OpenHands and SWE-agent. Handle in a later packet, or not.
- **Pending, not part of 0051:** Browser Use TOCTOU (0050 D7).

## Plain-English terms
- **Grade A:** lots of independent evidence (7+ studies, at least 3 peer-reviewed), including at least one recent test that says exactly which version was tested.
- **Stated version:** the study names the release, for example "v0.86.1". For a web service without release numbers, the closest equivalent is the plan or tier used and when.
- **Within 12 months:** the testing happened after 17 Oct 2025.
- **Inferred date:** the paper doesn't say when the tests ran, but other clues do, such as when web pages it cites were accessed or when it was submitted.
- **check_scores warning:** the checking script flags something for a human to look at. It is not an error.
- **Evidence score vs grade:** the score (0–100) is a judgment on evidence quality and feeds the overall score. The grade is a separate label from fixed rules. They are kept independent, so a score can sit outside the "usual" band for its grade.
