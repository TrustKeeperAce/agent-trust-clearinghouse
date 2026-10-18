# Decision 0053: SWE-agent, Sifting the Noise

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1a count Sifting the Noise as a separate source and disclose the shared Vul4Py authors (10 counted, 8 peer-reviewed); D2 grade B → A; D3 completion, disputes and adherence stay 45 / 55 / 55 with the two appended note sentences; D4a evidence quality stays 80 (7th check_scores warning accepted); D5 drafted wording; D6 rollout. Overall score unchanged at 58. Follows 0052 D1.

## Plain-English terms
- **Counted source:** an independent test that counts toward the evidence grade.
- **Peer-reviewed:** published in a reviewed journal or conference.
- **Grade A:** all three conditions must be met:
  1. 7 or more counted sources;
  2. 3 or more of them peer-reviewed;
  3. at least one test within the last 12 months (since 2025-10-17) that states the version tested.
- **Evidence score:** one of four factor scores (25% weight). The guide bands (A 85–100, B 70–84) are advisory. Out-of-band scores raise a check_scores warning, not an error.

## What was read
Full text of arXiv 2601.22952v3 (23 July 2026), which matches the published version: Proc. ACM Softw. Eng. 3, ISSTA, Article ISSTA009 (October 2026), doi 10.1145/3832100.

## Findings

**1. Independence**
- **Authors:** Yunpeng Xiong and Ting Zhang, both at Monash University, Australia.
- **No overlap with the SWE-agent developers:**
  - No author is at Princeton or Stanford. Neither institution appears in the paper.
  - No SWE-agent developer is an author.
  - There is no acknowledgements or funding section.
- **Shared authors with another counted source (new disclosure):** both authors are also co-authors of Vul4Py (Singapore Management University, Monash and UNSW; ProvSec 2026), which is already counted for SWE-agent. This is not a developer tie. It does mean two counted sources come from overlapping authors.

**2. Peer review**
- Yes: ISSTA 2026, published in PACMSE, Vol. 3, ISSTA, Article ISSTA009.
- This is the same status already recorded for Aider in 0051 D4.

**3. Version and date**
- **Version:** SWE-agent commit 1d3cfb798a2c257a0fc6094f1d35ef084d9919e1 (reference [52]).
  - It is on the main branch after v1.1.0. The commit is dated 2025-12-05 (GitHub API).
  - The entry scope already covers the main branch, so this is in scope.
- **When the runs happened:**
  - They cannot be earlier than the commit date of 2025-12-05.
  - The OWASP Benchmark repo was accessed 2025-12-14, and arXiv v1 is 2601.x (January 2026).
  - So the runs fell roughly between December 2025 and January 2026. That is inside the 12-month window, which starts 2025-10-17.
- **Models:** claude-sonnet-4-20250514, gpt-5-2025-08-07 and deepseek-chat, all at temperature 0.

**4. What was tested**
- **Task:** SAST false-positive filtering. Given a static-analysis alert and read-only codebase access, the agent decides whether the alert is a real vulnerability. No code is written.
- **Agents compared:** SWE-agent, OpenHands Agent SDK v1.5.2 and Aider v0.86.1, under a unified prompt. The browser was disabled; an ablation showed this made no measurable difference.
- **Datasets:**
  - OWASP Benchmark v1.2 (Java).
  - 50 sampled CodeQL alerts from Vul4J (real Java projects).
  - A post-cutoff OSS-Fuzz C/C++ set of 5 projects, run only for SWE-agent with Claude Sonnet 4, plus ablations.

**5. Results for SWE-agent**
- **OWASP false-positive rate (lower is better; the SAST tools on their own flagged over 92%), Table 3:**

  | Model | SWE-agent | OpenHands | Aider | Vanilla prompting |
  |---|---|---|---|---|
  | Claude Sonnet 4 | **6.3%** (best of all 12 settings) | 14.9% | 14.3% | 23.0% |
  | GPT-5 | 14.1% | 16.3% | 20.3% | 20.4% |
  | DeepSeek Chat | 13.1% | 15.8% | 13.2% | **11.2%** (vanilla best) |

- **Real vulnerabilities kept (OWASP positives, SWE-agent with Claude Sonnet 4), Section 5.2:**
  - 1,411 of 1,415 runs completed.
  - 314 real vulnerabilities were wrongly labelled false positives: 77.7% kept, a 22.25% miss rate.
  - Miss rates were low for injection classes (CWE-78 2.38%, CWE-89 1.10%, CWE-79 0.41%) and very high for weak cryptography (CWE-327 77.17%).
  - The authors conclude that agents are "unsuitable for unconditional, automatic suppression of SAST warnings."
- **Vul4J real-world Java (n=50), Table 4:** with Claude Sonnet 4, SWE-agent was the weakest of the three agents but still above vanilla prompting.

  | Agent (Claude Sonnet 4) | Accuracy | Precision | Recall | F1 |
  |---|---|---|---|---|
  | SWE-agent | 68.1 | 78.3 | 64.3 | 70.6 |
  | Aider | 77.6 | 85.2 | 76.7 | 80.7 |
  | Vanilla prompting | 66.0 | 79.2 | 61.3 | 69.1 |

  - With GPT-5, SWE-agent's F1 was 80.6, against Aider 83.3 and OpenHands 80.0.
- **OSS-Fuzz, post-cutoff C/C++ (Claude Sonnet 4), Table 5:**
  - SWE-agent identified 95.5% of false positives with 95.5% precision (F1 95.5). Vanilla prompting identified 36.4%.
  - The gains came mainly from cross-file navigation and multi-turn interaction.
- **Cost:** SWE-agent used about 130,846 tokens per Claude run. SWE-agent with GPT-5 cost $0.1052 per task, which the paper calls "costly due to token load."

**6. Scope fit**
- In scope: it runs the open-source SWE-agent framework at a main-branch commit. It is not mini-SWE-agent or EnIGMA.
- The task (alert triage, no code edits) differs from the entry's core coding benchmarks. It is still an independent test of how the agent performs on a software-engineering task.

## Effect on counts and grade

| | Before | After (D1a, recommended) | After (D1b) |
|---|---|---|---|
| Counted sources | 9 | 10 | 9 (Sifting the Noise and Vul4Py counted as one group) |
| Peer-reviewed | 7 | 8 | 7 |
| Recent test that states the version | none | yes (commit 1d3cfb, Dec 2025) | yes |
| A condition 1 (7+) | met | met | met |
| A condition 2 (3+ peer-reviewed) | met | met | met |
| A condition 3 (recent versioned test) | **not met** | **met** | **met** |
| Grade | B | **A** | **A** |

Either counting option gives A, because the only condition that was missing was condition 3.

## Factor scores (no fitting to grade)

| Factor | Now | Recommended | Why |
|---|---|---|---|
| Completion (30%) | 45 | 45 | Strong triage results (best OWASP setting; 95.5% on OSS-Fuzz) are offset by the weakest Vul4J result among the three agents with Claude. One read-only triage study does not move the code-change results that drive this score. Add a note sentence. |
| Disputes (20%) | 55 | 55 | No disputes in the paper. |
| Adherence to limits (25%) | 55 | 55 | The paper does not report out-of-scope actions. The 22.25% miss rate is an accuracy and safety trade-off for anyone using the agent for auto-suppression, not a limits violation. Add a note sentence for transparency. |
| Evidence (25%) | 80 | **80 (recommended)** or 83 | See D4. |
| Overall | 58 | **58** (13.5 + 11 + 13.75 + 20 = 58.25 → 58) | |

**Evidence score, stated honestly.** The rules describe evidence quality as the depth, independence and recency of the evidence, and the bands are a guide.
- **What improves:** this study fills the specific gap the current note names (no recent versioned test).
- **What remains:**
  - The other 9 sources mostly use older models and unstated or 2025 versions.
  - The new test is a single study of a read-only side task.
  - The new source shares authors with Vul4Py.
- **Precedent:** Aider was graded A in 0041 and 0051 at evidence 80, on the strength of this same study as its recent versioned test, and that warning was accepted.
- **Recommendation:** keep 80. Accept a new check_scores warning ("evidence 80 below A guide"), which would make 7 warnings.
- **Alternative (83):** this would reflect the recency gain on its own merits. It is still below the A band, so it would also warn, and it would raise the overall to 59 (see D4b).

## Decision items

**D1. Count Sifting the Noise for SWE-agent**
- **D1a (recommended):** count it as a separate source: 10 counted, 8 peer-reviewed. Disclose the shared authors with Vul4Py.
- **D1b:** treat Sifting the Noise and Vul4Py as one source group: 9 counted, 7 peer-reviewed. Same disclosure.

**D2. Grade B → A.** All three A conditions are met under D1a or D1b. Recommended: approve.

**D3. Completion, disputes and adherence stay at 45 / 55 / 55.** Add one sentence each to the completion and adherence notes (wording below). Recommended: approve.

**D4. Evidence score**
- **D4a (recommended):** stay at 80. Accept the warning, consistent with Aider.
- **D4b:** 83. The overall becomes 13.5 + 11 + 13.75 + 20.75 = 59.0 → **59**, so the score would change.

**D5. Disclosure, uncertainties and summary wording** (exact text below). Recommended: approve.

**D6. Rollout**
1. Update the YAML and page (build_entry_0048.py or an in-place edit).
2. Write decision record 0053 and add one changelog row.
3. Run check_scores (expect 0 errors and 7 warnings), check_links, overflow and axe.
4. Commit and push, then write manifest-0053.
5. You deploy.
6. Add the LOG note.

## Proposed exact wording (under D1a, D4a)

**New source row (counted, peer-reviewed; version_tested "commit 1d3cfb798a2c (main, 2025-12-05)"; test_date "2025-12 to 2026-01"):**
> Sifting the Noise (Monash University; ISSTA 2026, doi 10.1145/3832100): SWE-agent commit 1d3cfb798a2c (main branch, 5 December 2025) triaging static-analysis alerts. OWASP Benchmark false-positive rate 6.3% with Claude Sonnet 4, the best of 12 agent-model settings (14.1% GPT-5, 13.1% DeepSeek Chat); kept 77.7% of real vulnerabilities (22.25% wrongly dismissed, mostly weak-cryptography cases); on post-cutoff OSS-Fuzz C/C++ alerts, 95.5% of false positives identified at 95.5% precision; on 50 real-world Java alerts, the lowest F1 of three agents with Claude Sonnet 4 (70.6). Both authors are also Vul4Py co-authors.

**Completion note (append):**
> Sifting the Noise (ISSTA 2026; commit 1d3cfb, Dec 2025): best OWASP false-positive filtering of 12 agent-model settings (6.3% false-positive rate, Claude Sonnet 4) and 95.5% of false positives identified on post-cutoff C/C++ alerts, but the lowest F1 of three agents on 50 real-world Java alerts with Claude Sonnet 4 (70.6).

**Adherence note (append):**
> In the same study, SWE-agent with Claude Sonnet 4 wrongly dismissed 22.25% of real vulnerabilities (77.17% for weak cryptography); the authors advise against using agent verdicts for automatic suppression.

**Evidence note (replace):**
> Ten independent sources, eight peer-reviewed (NeurIPS 2024, NeurIPS 2025 ×2, AAAI 2026, ICML 2026 ×2, ProvSec 2026 in Springer LNCS, ISSTA 2026). Sifting the Noise (ISSTA 2026) states the version tested (main-branch commit 1d3cfb, 5 December 2025) and ran within the last 12 months, so grade A. Most other sources use older models and unstated or 2025 versions, and the newest test is a read-only alert-triage task; evidence quality stays 80, below the usual A range (as for Aider, 0051).

**Disclosures (append):**
> Sifting the Noise and Vul4Py share two authors (Monash University); they are counted as separate studies with different tasks and datasets.

**Uncertainties:**
- Replace "No test from the last 12 months states the SWE-agent version. The latest release is v1.1.0 (May 2025), and the main branch was last updated in July 2026." with:
  > Only one test from the last 12 months states the SWE-agent version (Sifting the Noise, main-branch commit of December 2025), and it is an alert-triage task, not code changes. The latest release is v1.1.0 (May 2025), and the main branch was last updated in July 2026.
- Add:
  > Grade A rests on a single recent versioned study whose authors also wrote another counted source (Vul4Py).

**Summary:**
- Replace "Nine independent studies that ran or analysed it were found (seven peer-reviewed)." with "Ten independent studies that ran or analysed it were found (eight peer-reviewed)."
- Insert after the Vul4Py sentence:
  > In a static-analysis triage study (Sifting the Noise, ISSTA 2026), it had the best false-positive filtering of 12 agent-model settings but wrongly dismissed 22.25% of real vulnerabilities.

**Scoreline:**
> Overall score: 58 · Evidence grade: A · Independent sources: 10 performance (8 peer-reviewed), 6 other

**Decision records line:** add "0053 (Sifting the Noise; grade A)".

**Changelog row:**
> 2026-10-17 · 0053 · SWE-agent: Sifting the Noise (ISSTA 2026) added, testing a December 2025 main-branch commit; 10 counted sources (8 peer-reviewed). Grade B → A because a recent test now states the version. Overall score unchanged at 58; evidence quality stays 80.

## Queue
- **0054 (Elicit):** queued, not started.
- **0050 D7 (Browser Use TOCTOU):** still pending and undecided.
