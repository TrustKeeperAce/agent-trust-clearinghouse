# Decision 0048: SusVibes for SWE-agent

**Status: APPROVED by Remington, 2026-10-17.** As recommended: D1 count (9 counted, 7 peer-reviewed); D2 disclosures; D3 keep adherence 55 (overall 58 / B); D4 wording as drafted; D5 grade B; D6 rollout (no recheck note added); D7 deferred to 0049. Part of the consistency pass (follow-up flag opened in 0040).

## What happened (facts and sources)
- **Source:** Zhao, Wang, Zhang, Luo, Li and Li, "Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks" (SusVibes). arXiv 2512.03262 v4, 21 Sept 2026: https://arxiv.org/abs/2512.03262
  - **Peer review:** ICML 2026 (PMLR 306). Confirmed by the ICML 2026 poster page (https://icml.cc/virtual/2026/poster/61427) and the v4 proceedings header.
  - **The benchmark:** 186 security-sensitive feature-request tasks from real Python repositories with human-written functional and security tests. Three frameworks (SWE-agent, OpenHands, Claude Code) × four models. Pass@1, maximum 200 steps.
- **Per-model numbers for SWE-agent:** Table 3 (layout extraction; the model is named on each row). FuncPass is the share of tasks solved correctly; SecPass is the share both correct and secure.

  | Model | FuncPass | SecPass |
  |---|---|---|
  | Claude 4 Sonnet | 57.0% | 11.8% |
  | Kimi K2 | 21.5% | 5.4% |
  | Gemini 2.5 Pro | 18.3% | 6.5% |
  | Gemini 3 Pro | 37.1% | 12.9% |

  - 79.3% of SWE-agent + Claude 4 Sonnet's functionally correct solutions were insecure.
  - Averaged over models, SWE-agent had the highest share of correct solutions that were also secure: 23.3%, against OpenHands 20.1% and Claude Code 17.4%. The authors call it the most secure of the three frameworks.
  - With Claude 4 Sonnet, FuncPass fell from 66.9% on single-file tasks to 30.3% on tasks touching more than two files.
  - Prompting with vulnerability hints (generic, self-selection or oracle CWE) improved security only slightly and cut functional correctness by about 7 points. Those experiments were SWE-agent + Claude 4 Sonnet.
  - Earlier arXiv versions gave different headline figures (61% functional, 10.5% secure). v4 is the camera-ready version and is used here.
- **Version and test date:** no SWE-agent version or commit is stated. Test date is not stated; it was 2025–2026, at or after the Gemini 3 Pro release in November 2025, so within roughly 12 months, but unversioned.
- **Author independence:**
  - Affiliations: Carnegie Mellon (Language Technologies Institute), Columbia, Johns Hopkins and HydroX AI.
  - None of the SWE-agent authors (Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press; Princeton/Stanford) is an author.
  - Independent for SWE-agent. OpenHands independence is checked separately in 0049, because OpenHands is also at CMU.
- **Disclosures:** the acknowledgment thanks Modal for compute (model serving and inference) and Google for Gemini API credits, and says the work was "partly supported by HydroX AI" (an author affiliation). Neither is the SWE-agent developer. Google's models are among those tested, so disclose.
- **A design point to disclose:** SusVibes uses SWE-agent instances in its own task-building pipeline (to mask features, write task descriptions and set up environments). That is not a conflict of interest, but SWE-agent-shaped tasks could favour SWE-agent.

## What the rules say
- **Counting:** an independent study that ran the named product counts as an independent performance source. Peer review is recorded from the venue. Version and test date are recorded as stated. Disclosures are noted, not disqualifying. SusVibes counts: it ran SWE-agent itself, its authors are not affiliated with SWE-agent, and it is peer-reviewed (ICML 2026).
- **Count:** 8 → **9** counted sources; peer-reviewed 6 → **7**.
- **Grade:** A needs 7+ sources, 3+ peer-reviewed, and a test within 12 months that states the version. SusVibes states no version, so the A condition still fails. Grade stays **B**.
- **Scores:** factor scores are judgment calls from the evidence. They must not be moved to fit a grade. Overall = 0.30 C + 0.20 D + 0.25 A + 0.25 E, rounded half up.

## Effect on factor scores (recomputed)
- **Completion rate (45, keep):** FuncPass of 18.3–57.0% is within the range the note already records for SWE-agent (about 10–44% elsewhere). The best result (57.0%, best of 12 settings) is notable but on one benchmark. No change.
- **Disputes (55, keep):** SusVibes is not a dispute. No change.
- **Adherence to limits (55):** this is the judgment call.
  - **For keeping 55:**
    - SusVibes measures whether the code is secure, not whether the agent stayed within its instructions or permissions.
    - SWE-agent was the most secure of three frameworks.
    - The Claude Code entry also placed SusVibes under adherence and completion. Its adherence there (40) rests mainly on other permission and boundary studies.
  - **For lowering it to 50:**
    - This is the first direct, peer-reviewed security measurement of SWE-agent's output.
    - Absolute results are poor (SecPass at most 12.9%; about 80% of correct solutions insecure).
    - The current note says only scanner findings exist.
  - **Recommendation: keep 55.** The current note says SWE-agent shows no measured out-of-scope behaviour. SusVibes adds secure-coding evidence where SWE-agent is the best of the agents compared. That supports the score, with a clearer note, rather than a change.
- **Evidence quality (80, keep):** one more peer-reviewed but unversioned source. 80 stays within the B guide on its merits (more sources, still none versioned and recent). Not raised or lowered to fit anything.

| Option | Computation | Overall | Grade |
|---|---|---|---|
| Recommended (adherence 55) | 0.30×45 + 0.20×55 + 0.25×55 + 0.25×80 = 58.25 | 58, unchanged | B |
| Alternative (adherence 50) | 0.30×45 + 0.20×55 + 0.25×50 + 0.25×80 = 57.00 | 57 | B |

## Proposed text changes (SWE-agent entry; neutral wording)
- **Source row** (counted, peer_reviewed: true, version_tested: "unstated (max 200 steps)", test_date: "2025-2026", accessed: 2026-10-17):

  > SusVibes (Carnegie Mellon, Columbia, Johns Hopkins, HydroX AI; ICML 2026): 186 security-sensitive feature tasks; SWE-agent passed functional tests on 18.3-57.0% of tasks and was both functional and secure on 5.4-12.9%, across four models (best Claude 4 Sonnet 57.0/11.8; Gemini 3 Pro 37.1/12.9). Disclosures: Modal compute; Google Gemini API credits; partly supported by HydroX AI; the benchmark's own task pipeline uses SWE-agent.
- **Completion note, append:**

  > SusVibes (ICML 2026): 18.3-57.0% of feature tasks passed functional tests across four models; 57.0% with Claude 4 Sonnet was the highest of 12 agent-model settings.
- **Adherence note (security wording), replacing the sentence "No independent study of out-of-scope or unrequested actions by SWE-agent was found." with:**

  > SusVibes (ICML 2026): only 5.4-12.9% of SWE-agent's solutions were both functional and secure, and 79.3% of its functionally correct solutions with Claude 4 Sonnet had a vulnerability; across models, SWE-agent had the highest share of secure correct solutions of the three frameworks tested (23.3%, vs OpenHands 20.1% and Claude Code 17.4%). Prompting with vulnerability hints raised security slightly but lowered functional correctness. No independent study of out-of-scope or unrequested actions by SWE-agent was found.
- **Evidence-quality note:** "Eight" becomes "Nine". "six peer-reviewed" becomes "seven peer-reviewed", adding ICML 2026 (SusVibes). The grade-B sentence is unchanged.
- **Summary:** "Eight independent studies … (six peer-reviewed)" becomes "Nine independent studies … (seven peer-reviewed)". Add the clause:

  > in a security benchmark, 5.4-12.9% of its solutions were both functional and secure, the best of three frameworks tested.
- **Page:** regenerate with the entry build plus scripts/apply_design.py. The factor table, score bar (58 unchanged), counts (9 performance, 7 peer-reviewed) and source list update; the index is unchanged if 58 is kept.

## Cross-entry consequence (flagged, not part of this decision)
- The Claude Code entry (0040) counts SusVibes as not peer-reviewed (it was a preprint then).
- With ICML 2026 confirmed, Claude Code's peer-reviewed count would go from 5 to 6. Grade A and the score are unaffected.
- Propose handling it with the OpenHands packet (0049) or as a one-line metadata fix.

## Risks and uncertainties
- Table 3 numbers come from layout text extraction of v4. Rows are labelled by model, so the pairing is reliable, but earlier versions differ.
- The test date is inferred from the models used, not stated.
- SusVibes is Python-only and feature-request-only.
- The pipeline uses SWE-agent, which could favour it (disclosed).
- The SecPass definitions are strict: both the functional and security tests must pass.
- An adherence score change is defensible either way (see D3).

## Recommendation
**Approve** counting SusVibes for SWE-agent (9 counted, 7 peer-reviewed) with the wording above, keeping 58 / B. Reasons:
- SusVibes is independent and peer-reviewed, and it ran the named product.
- It fills a stated gap (direct security evidence).
- Under the rules it does not change the grade, and the evidence supports the current scores.

## Decisions requested
- **D1 Count:** count SusVibes as an independent performance source for SWE-agent, recorded as peer_reviewed: true (ICML 2026), version unstated, test 2025–2026. Count 8 → 9; peer-reviewed 6 → 7.
- **D2 Disclosures:** record Modal compute, Google Gemini API credits, HydroX AI partial support, and the benchmark's own use of SWE-agent in task building.
- **D3 Adherence score:** keep 55 (recommended; overall 58) or lower to 50 (overall 57). Completion 45, disputes 55 and evidence 80 are unchanged in both options.
- **D4 Wording:** approve the source row, completion, adherence (security), evidence and summary text above.
- **D5 Grade:** remains B (no recent test that states the version). No methodology change.
- **D6 Rollout:**
  - After approval: update the YAML, page and decision record 0048.
  - Run check_scores, check_links, overflow and axe on the page; commit; manifest plus files.json.
  - You deploy.
  - Recheck note: SWE-agent's page currently has none. Recommend adding "Citation check incomplete — recheck later" only if the citation backfill packet says so, not here.
- **D7 Claude Code follow-up:** record SusVibes as peer-reviewed in the Claude Code entry (5 → 6), in 0049 or a separate metadata fix.

## Plain-English terms
- **FuncPass:** the share of tasks where the agent's code passed the normal functional tests.
- **SecPass:** the share of tasks where the code passed both the functional tests and the security tests.
- **pass@1:** one attempt per task, no retries.
- **CWE:** a standard list of software weakness types.
- **Peer-reviewed:** checked by independent reviewers before publication; here, accepted at the ICML 2026 conference.
- **Round half up:** .5 and above rounds up (58.25 rounds to 58).
