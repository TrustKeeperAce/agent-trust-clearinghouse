# Decision 0050: Agent S safety-test correction (TOCTOU study)

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1a count TOCTOU (7 → 8; peer-reviewed 2); D2 wording correction; D3 adherence 35; D4 evidence 70 (49 / B); D5 wording as drafted; D6 rollout. **D7 (Browser Use follow-up): pending, not decided.** Part of the consistency pass. Resolves the Agent S flag opened in 0039.

## Background: the 0039 D5 item
- **What D5 proposed:** in the UI-TARS Desktop packet (0039), D5 was only a procedural question.
  - It asked whether to open a separate correction for Agent S, based on the TOCTOU paper (14/14 triggered for Agent S).
  - The packet's consistency flag noted that the live Agent S page says "No independent prompt-injection or safety test of Agent S was found."
  - D5 proposed no wording, count or score change.
- **Outcome:** recorded as "D5 not approved; Agent S unchanged". No reason is recorded in the decision file or private drafts.
  - The likely reading is that the change was out of scope for a UI-TARS packet and should not ride along with an unrelated entry.
  - That is consistent with the rule that anything which might change a score gets its own packet.
- **How 0050 differs:**
  - It is the separate, self-contained Agent S packet, inside the one-time consistency pass you approved.
  - It verifies the paper specifically for Agent S.
  - It gives exact wording, count, grade and score options for you to decide on their own merits.
  - Nothing from 0039 is applied automatically. If you prefer to leave Agent S unchanged again, D1 = reject keeps the page as is, apart from the factual correction in D2, which can be approved on its own.

## What happened (facts and sources)
- **Paper:** Jiang, Liu, Luo and Lin, "Atomicity for Agents: Exposing, Exploiting, and Mitigating TOCTOU Vulnerabilities in Browser-Use Agents".
  - arXiv 2603.00476 v1, 28 Feb 2026, cs.CR: https://arxiv.org/abs/2603.00476
  - **Peer review:** none found. Only v1 exists, and no venue is stated in the paper. Recorded as not peer-reviewed, as in the UI-TARS entry.
- **Authors and independence:**
  - All four authors are at The Ohio State University.
  - The Agent S authors (Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, Xin Eric Wang; Simular and UC Santa Cruz) do not appear.
  - The paper has no Simular affiliation or acknowledgment. Funding: NSF award CNS-2112471 and a Schmidt Sciences Safety Science Award.
  - The authors propose a mitigation (pre-execution validation), so they have a method interest in showing that agents are vulnerable. They are not competing with Agent S on its own tasks.
  - **Conclusion:** independent of Simular.
- **Setup:**
  - Ten popular open-source browser- and computer-use agents, collected from GitHub.
  - The test bed (the authors' "DynWeb" benchmark) has 14 cases: 9 synthesized pages run locally, plus 5 real websites with human observers who stop harmful runs.
  - Three manipulation types:
    - Type I: the layout or UI changes after the agent looks (for example an ad overlay appears where it was about to click).
    - Type II: data changes, such as a price or label.
    - Type III: expiring state, such as an OTP or session.
  - The adversary only changes page content at the right moment. The threat model explicitly excludes prompt injection and model compromise.
  - Outcomes are judged by a per-case oracle and confirmed by manual inspection of the trajectory.
- **Agent S result (Table 3):**
  - The vulnerability was triggered in **all 14 cases** (S1–S9, R1–R5).
  - Agent S is classed as screenshot-observation with human-like (coordinate) actions. All agents of that type failed every case.
  - Six other agents also failed 14/14: computer-use-demo, openai-cua-sample-app, Cua, UI-TARS-desktop, Bytebot and Midscene.
  - Agent-E, WebVoyager and Browser-Use resisted the five Type I cases (9/14 triggered).
  - "All 10 agents fail on at least one manipulation type."
- **Version and model:** the paper cites the Agent S and Agent S2 papers for "Agent-S" but states no version, gui-agents release or backbone model.
  - **Test date:** not stated. Other repositories were accessed on 27 Dec 2025 and the paper is dated 28 Feb 2026, so the test was probably late 2025 to early 2026, when the public release was gui-agents 0.3.x (S3). This is inferred, not stated.
- **Mitigation results:** the 10-run repeat experiments (prompt-only baseline vs pre-execution validation) were run on openai-cua-sample-app only. They do not test Agent S.
- **The live Agent S page:**
  - The adherence note and Security list say "No independent prompt-injection or safety test of Agent S was found."
  - The uncertainties say "No independent security or prompt-injection evaluation of Agent S was found."
  - Given TOCTOU, the "safety test" and "security evaluation" parts are factually incorrect.
  - The "prompt-injection" part is still accurate: TOCTOU is not a prompt-injection test.

## What the rules say
- **Counting:** an independent study that ran the named product counts as an independent performance source, including safety and security tests (Browser Use precedent: 3 of its 7 are security tests).
  - Version and test date are recorded as stated (here: unstated), and the source is marked not peer-reviewed.
  - **Precedent 0039 D3:** the same paper was counted for UI-TARS Desktop as "a systematic, reproducible test of the named app".
  - Counting it here is consistent. It ran Agent S code from GitHub, which is the open-source framework this entry covers.
- **Scope caution:** the paper does not say which Agent S generation was run. The entry covers S2, S2.5 and S3 (gui-agents 0.2.x–0.3.2). S1 is context only.
  - The run dates point to S3, and the citation of S2 points to S2 or later. Both are in scope.
  - If you consider an unstated generation disqualifying, the alternative is "other (context)" (D1b).
- **Count:** 7 → **8** counted; peer-reviewed stays **2**.
- **Grade:** B applies to 5–6 sources, or 7+ that fail an A condition. With 8 sources and only 2 peer-reviewed (A needs 3+), the grade stays **B** either way. Not fitted.

## Effect on factor scores (recomputed)
- **Completion (45), disputes (45):** unaffected. TOCTOU measures susceptibility, not task success, and it is not a dispute.
- **Adherence to limits (35):** judgment call.
  - **For keeping 35:**
    - 35 was already set low because of evidence that the command-line app acts without confirmation, with an unused permission dialog and no sandbox.
    - The TOCTOU weakness is shared by every screenshot/coordinate agent tested (7 of 10, including reference implementations from Anthropic and OpenAI).
    - It is a single preprint with unstated version and model.
    - UI-TARS Desktop, with the same 14/14, was not scored, so there is no scored precedent for a downgrade.
  - **For lowering it to 30:**
    - It is the first independent safety test, and it found no resistance in any case, including real websites.
    - Agent S has no confirmation step that might catch a misdirected click (from the code review).
  - **Recommendation: keep 35.** The new test confirms the risk the score already reflects rather than revealing a new one, and its result is not specific to Agent S.
- **Evidence quality (70):** one more independent, non-peer-reviewed source, which addresses a stated gap (no safety testing).
  - That is a modest improvement, but the peer-reviewed share is unchanged and the version is unstated. Keep 70.
  - 75 is defensible but is not recommended.

| Option | Computation | Overall | Grade |
|---|---|---|---|
| A (recommended): adherence 35, evidence 70 | 0.30×45 + 0.20×45 + 0.25×35 + 0.25×70 = 48.75 | 49, unchanged | B |
| B: adherence 30, evidence 70 | 0.30×45 + 0.20×45 + 0.25×30 + 0.25×70 = 47.50 | 48 (half up) | B |
| C: adherence 35, evidence 75 | 0.30×45 + 0.20×45 + 0.25×35 + 0.25×75 = 50.00 | 50 | B |

- **Index position:** at 49, Agent S stays tied with Data Interpreter, listed first alphabetically. At 48 it moves one place below Data Interpreter. At 50 it ties Devin, listed first alphabetically.

## Proposed text changes (neutral wording)
- **Source row** (kind: independent performance; peer_reviewed: false; version_tested: "unstated (Agent S / S2 cited; model not stated)"; test_date: "unstated (likely late 2025 to early 2026)"; accessed: 2026-10-17):

  > TOCTOU study (Ohio State University; preprint, Feb 2026): tested 10 open-source browser- and computer-use agents on 14 cases where a web page changes between the agent's check and its action (layout changes, data updates, expiring states; 9 synthesized pages, 5 real sites). The vulnerability was triggered in all 14 cases for Agent S, as for the six other screenshot-based agents; agents with structured page access resisted layout changes. Version and model not stated. Funding: NSF and Schmidt Sciences; the authors propose a mitigation.
- **Adherence note**, replacing "No independent prompt-injection or safety test of Agent S was found." with:

  > An independent TOCTOU study (Ohio State, preprint Feb 2026; version and model not stated) found that page changes between the agent's check and its action redirected Agent S in all 14 test cases, as for every other screenshot-based agent tested. No independent prompt-injection test of Agent S was found.

  The rest is unchanged.
- **Security list item**, replacing "No independent prompt-injection or safety test of Agent S was found." with:

  > One independent safety test (TOCTOU study, preprint): page changes timed between the agent's check and its action caused unintended actions in all 14 cases tested. No independent prompt-injection test of Agent S was found.

  "No legal or regulatory action was found." is kept.
- **Uncertainty**, replacing "No independent security or prompt-injection evaluation of Agent S was found." with:

  > The only independent safety test (TOCTOU, preprint) does not state the Agent S version or model, and its result is shared by all screenshot-based agents tested; no independent prompt-injection evaluation was found.
- **Evidence note:** "Seven independent performance sources, two peer-reviewed (ACL 2026, MLSys 2026), five run in 2026." becomes:

  > Eight independent performance sources, two peer-reviewed (ACL 2026, MLSys 2026), five run in 2026, one a safety test (preprint).
- **Summary:** after the code-review sentence, add:

  > An independent preprint found that web pages changing at the moment of action could redirect it in all 14 cases tested, as for other screenshot-based agents.
- **Page:**
  - The counts line changes to 8 performance (2 peer-reviewed).
  - Add decision record 0050 alongside 0025.
  - Add a changelog row.
  - Build with scripts/apply_design.py. The index is unchanged under option A.

## Related consistency flag (not part of this decision)
- The same paper tested Browser-Use (9/14 triggered: it resisted layout changes and failed data-change and expiring-state cases).
- The Browser Use entry does not cite it. Grep shows only ui-tars-desktop.yaml references 2603.00476.
- Browser Use is 51/B with 7 counted sources, 3 peer-reviewed. Adding an 8th non-peer-reviewed source would not change the grade by itself, but its A/B basis has a check_scores warning.
- Suggest a separate packet (0051).

## Risks and uncertainties
- **Which generation:** the Agent S generation tested is not stated. If it was S1, it would be out of scope; the dates and the S2 citation make that unlikely.
- **Not peer-reviewed:** a single preprint.
- **Not specific to Agent S:** the result reflects an architecture-wide weakness of coordinate-based agents.
- **Small and favourable test:** 14 cases, likely single runs for the vulnerability table (repeat runs are described only for the mitigation study), and the authors propose a fix.
- **What it measures:** robustness to timing manipulation, not instruction-following or prompt injection. The wording keeps the "no prompt-injection test" statement for that reason.
- **Precedent:** counting this here mirrors UI-TARS (0039 D3). Not counting it would make the two entries inconsistent.

## Recommendation
**Approve** the factual correction and count the TOCTOU study for Agent S (8 counted, 2 peer-reviewed), keeping 49 / B (option A). Reasons:
- The live page is factually inaccurate on "safety test".
- The study is independent, ran the in-scope open-source framework, and was already counted for UI-TARS.
- The evidence confirms rather than changes the existing low adherence score.

## Decisions requested
- **D1 Count:** (a) count TOCTOU as an independent performance source for Agent S, not peer-reviewed, version, model and test date unstated: 7 → 8 (recommended). (b) List it as other (context), not counted: count stays 7. (c) Reject, leaving Agent S unchanged as after 0039, apart from D2.
- **D2 Factual correction:** replace "No independent prompt-injection or safety test" and "No independent security or prompt-injection evaluation" with the wording above, so it acknowledges TOCTOU and keeps "no prompt-injection test". Applies under D1a or D1b.
- **D3 Adherence score:** keep 35 (recommended) or 30.
- **D4 Evidence quality:** keep 70 (recommended) or 75.
  - Resulting overall: A 49 / B (recommended); B 48 / B; C 50 / B. Grade B in all cases.
- **D5 Wording:** approve the source row, adherence, security, uncertainty, evidence and summary text above.
- **D6 Rollout:**
  - YAML and page (apply_design.py), decision record 0050 approved, one changelog row.
  - Run check_scores, check_links, overflow and axe; commit and push; manifest plus files.json. You deploy.
  - No recheck note.
- **D7 Follow-up:** open packet 0051 for TOCTOU in the Browser Use entry (yes or no). **Status: pending, not decided.**

## Plain-English terms
- **TOCTOU (time of check to time of use):** the agent looks at a page, decides what to click, and by the time it clicks, the page has changed. So it clicks something it didn't intend.
- **Screenshot-based / coordinate actions:** the agent sees an image of the screen and clicks at x,y positions, rather than referring to named page elements.
- **Prompt injection:** hidden instructions in content that try to make the agent do something else. TOCTOU is a different attack, which only moves or changes page content.
- **Preprint:** a paper posted publicly without (yet) passing peer review.
- **Counted source:** independent evidence used for the evidence grade.
- **Round half up:** .5 and above rounds up (47.5 rounds to 48; 48.75 rounds to 49).
