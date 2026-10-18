# Decision 0049: SusVibes for OpenHands; SusVibes peer-review status for Claude Code

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1 count (OpenHands 11 counted, 6 peer-reviewed); D2 CMU tie as disclosure plus other disclosures; D3 keep adherence 55 (61 / A); D4 wording as drafted; D5 grade A; D6 Claude Code SusVibes peer-reviewed (5 → 6; uncertainty three → four; 55 / A unchanged); D7 rollout. Part of the consistency pass. Closes the 0040 SusVibes follow-up, together with 0048.

## What happened (facts and sources)
- **Source:** "Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks" (SusVibes).
  - arXiv 2512.03262 v4, 21 Sept 2026: https://arxiv.org/abs/2512.03262
  - ICML 2026, PMLR 306: https://icml.cc/virtual/2026/poster/61427 (same paper as 0048).
  - 186 security-sensitive feature tasks in real Python repositories, with human-written functional and security tests.
  - Each framework ran with its default recommended system prompt and a maximum of 200 steps; pass@1.
- **Per-model numbers for OpenHands** (Table 3, v4; one row per model, columns per framework):

  | Model | FuncPass | SecPass |
  |---|---|---|
  | Claude 4 Sonnet | 53.2% | 11.8% |
  | Kimi K2 | 36.0% | 9.1% |
  | Gemini 2.5 Pro | 19.9% | 8.1% |
  | Gemini 3 Pro | 50.5% | 10.8% |

  - 77.8% of OpenHands + Claude 4 Sonnet's functionally correct solutions were insecure.
  - Across models, 20.1% of OpenHands' correct solutions were also secure. This was second of the three frameworks: SWE-agent 23.3%, Claude Code 17.4%.
  - With Claude 4 Sonnet, OpenHands matched SWE-agent's SecPass (11.8%) with lower FuncPass (53.2% vs 57.0%).
  - Figure 10 is a case study in which OpenHands + Claude 4 Sonnet introduced a vulnerability.
  - The prompting-strategy and file-count experiments used SWE-agent only, so they say nothing about OpenHands.
- **Version and test date:** no OpenHands version, commit or SDK release is stated. The test date is not stated; it was 2025–2026, at or after the Gemini 3 Pro release in November 2025.
- **Author independence (checked carefully because of CMU):**
  - **SusVibes authors:** Songwen Zhao (CMU, Columbia), Danqing Wang (CMU), Kexun Zhang (CMU), Jiaxuan Luo (Johns Hopkins), Zhuo Li (HydroX AI), Lei Li (CMU Language Technologies Institute).
  - **OpenHands developers:**
    - All Hands AI, the company that maintains OpenHands, was founded by Xingyao Wang, Graham Neubig (CMU LTI; All Hands chief scientist) and Robert Brennan (per the OpenHands docs and blog).
    - The 24 authors of the OpenHands paper (ICLR 2025) are: Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, Graham Neubig.
  - **Overlap:** none. No SusVibes author is an OpenHands paper author or an All Hands AI founder. Graham Neubig is not a SusVibes author and is not thanked in its acknowledgment.
  - **Institutional tie:** Lei Li and Graham Neubig are both CMU LTI faculty. They co-authored two unrelated 2024 CMU speech-translation system papers (IWSLT 2024, found via OpenAlex). That is shared institution and unrelated co-authorship, not developer affiliation. The OpenAgentSafety exclusion (0037) was because Neubig was a co-author of that study, which does not apply here.
  - **Contributor list:** I also checked the top 400 GitHub contributors to OpenHands for obvious usernames of the six authors and found none. This is a weak check: usernames may not match real names.
  - **Conclusion:** independent of OpenHands, with the CMU tie disclosed.
- **Disclosures:**
  - **Funding and compute:** Modal compute, Google Gemini API credits (Gemini models are tested), and partial support from HydroX AI (an author affiliation).
  - **Pipeline:** the benchmark's own task-building pipeline uses SWE-agent, a competing framework in the comparison. That could favour SWE-agent relative to OpenHands.
  - **Same institution:** several authors are at CMU, where OpenHands' co-founder and chief scientist is faculty.

## What the rules say
- **Counting:**
  - An independent study that ran the named product counts. Studies with developer-affiliated authors are excluded for that product (OpenAgentSafety precedent).
  - Shared institution alone is not affiliation; it is disclosed.
  - Peer review comes from the venue, and the version and test date are recorded as stated.
  - SusVibes counts for OpenHands.
- **Count:** 10 → **11** counted; peer-reviewed 5 → **6**.
- **Grade:** OpenHands is A, resting on PBT-Bench (NeurIPS 2026; SDK v1.11.5; July 2026). It has 11 sources, 6 peer-reviewed and a recent versioned test, so it stays **A**. SusVibes (unversioned) neither adds to nor weakens the A basis.
- **Scores:** judgment from the evidence, not fitted to the grade. Overall = 0.30 C + 0.20 D + 0.25 A + 0.25 E, rounded half up.

## Effect on factor scores (recomputed)
- **Completion rate (50, keep):** FuncPass of 19.9–53.2% is within the range the note already records (about 3% to 48%, plus 83.4% bug recall). No change.
- **Disputes (55, keep):** not a dispute.
- **Adherence to limits (55):** judgment call.
  - **For keeping 55:**
    - SusVibes measures whether code is secure, not whether the agent stays within limits.
    - OpenHands was middle of three frameworks.
    - The adherence note already includes both a favourable study (Overeager: lowest out-of-scope rate) and an unfavourable one (SWE-MISBEHAVIOR 18.19%).
    - This matches 0048, where SWE-agent kept 55.
  - **For lowering it to 50:**
    - Absolute security is poor: SecPass at most 11.8%, and 77.8% of correct solutions insecure with Claude 4 Sonnet.
  - **Recommendation: keep 55.** It is consistent with 0048, and the new evidence supports the existing picture.
- **Evidence quality (85, keep):** one more peer-reviewed, unversioned source. The A basis is unchanged, and 85 stays on its merits.

| Option | Computation | Overall | Grade |
|---|---|---|---|
| Recommended (adherence 55) | 0.30×50 + 0.20×55 + 0.25×55 + 0.25×85 = 61.00 | 61, unchanged | A |
| Alternative (adherence 50) | 0.30×50 + 0.20×55 + 0.25×50 + 0.25×85 = 59.75 | 60 | A |

With 61, the index order is unchanged (OpenAI Codex 62, OpenHands 61, AIDE 60). With 60, OpenHands would tie AIDE and, ties being alphabetical, drop one place below it.

## Proposed text changes (OpenHands entry; neutral wording)
- **Source row** (counted, peer_reviewed: true, version_tested: "unstated (default prompt, max 200 steps)", test_date: "2025-2026", accessed: 2026-10-17):

  > SusVibes (Carnegie Mellon, Columbia, Johns Hopkins, HydroX AI; ICML 2026): 186 security-sensitive feature tasks; OpenHands passed functional tests on 19.9-53.2% of tasks and was both functional and secure on 8.1-11.8%, across four models (best Claude 4 Sonnet 53.2/11.8; Gemini 3 Pro 50.5/10.8). Disclosures: Modal compute; Google Gemini API credits; partly supported by HydroX AI; several authors are at CMU, where an OpenHands co-founder is faculty (no author overlap); the benchmark's task pipeline uses SWE-agent.
- **Completion note, append:**

  > SusVibes (ICML 2026): 19.9-53.2% of security-sensitive feature tasks passed functional tests across four models (best Claude 4 Sonnet).
- **Adherence note (security wording), append:**

  > SusVibes (ICML 2026): 8.1-11.8% of OpenHands' solutions were both functional and secure, and 77.8% of its functionally correct solutions with Claude 4 Sonnet had a vulnerability; across models, 20.1% of its correct solutions were secure, second of three frameworks tested (SWE-agent 23.3%, Claude Code 17.4%).
- **Evidence-quality note:**
  - "Ten independent sources, five peer-reviewed (ICLR 2025 ×2, AAAI 2026, an ICSE 2026 workshop, NeurIPS 2026)" becomes "Eleven independent sources, six peer-reviewed (ICLR 2025 ×2, AAAI 2026, an ICSE 2026 workshop, NeurIPS 2026, ICML 2026)".
  - The rest is unchanged.
- **Summary:**
  - "Ten independent studies that ran it were found (five peer-reviewed)" becomes "Eleven … (six peer-reviewed)".
  - After the boundary-violation sentence, add:

    > In a security benchmark, 8.1-11.8% of its solutions were both functional and secure.
- **Disclosures section on the page, add:**

  > SusVibes acknowledges compute from Modal and Gemini API credits from Google (whose models it tests), and was partly supported by HydroX AI, an author affiliation. Several authors are at Carnegie Mellon, where OpenHands co-founder Graham Neubig is faculty; no SusVibes author is an OpenHands paper author or All Hands AI founder. The benchmark's task pipeline uses SWE-agent, a competing framework.
- **Page:** a new build script for the OpenHands page, then scripts/apply_design.py, plus a changelog row. The index is unchanged if 61 is kept.

## Claude Code: SusVibes peer-review status (D7 from 0048)
- **Facts:**
  - The Claude Code entry (0040) lists SusVibes as counted with peer_reviewed: false ("preprint v4 Sept 2026").
  - ICML 2026 (PMLR 306) is now confirmed (poster page; the v4 proceedings header).
  - Claude Code's figures in the source row (FuncPass 12.9–41.4%, SecPass 3.8–8.6%) match Table 3 v4. No figure changes.
- **Effect:**
  - Peer-reviewed count 5 → **6**; counted sources stay 15.
  - Grade A is unchanged: its basis is recent versioned tests (2.1.117–2.1.139) and was already met with 5.
  - Scores unchanged (evidence quality 85, overall 55).
  - The uncertainty that says "without [the two PR field studies], three peer-reviewed sources remain" becomes "four".
- **Wording:**
  - **Source row:**
    - Set peer_reviewed: true.
    - Change "(CMU and others; preprint v4 Sept 2026)" to "(Carnegie Mellon, Columbia, Johns Hopkins, HydroX AI; ICML 2026)".
    - Append: "Disclosures: Modal compute; Google Gemini API credits; partly supported by HydroX AI."
  - **Evidence note:** "Fifteen independent sources, five peer-reviewed (ISSTA 2026, TOSEM, MSR 2026, NeurIPS 2026 Datasets & Benchmarks, ASE 2026 extended abstract)" becomes "… six peer-reviewed (…, ASE 2026 extended abstract, ICML 2026)".
  - **Page counts line:** "15 performance (5 peer-reviewed)" becomes "(6 peer-reviewed)".
  - **Changelog:** combined row with OpenHands.

## Risks and uncertainties
- **Independence:** based on author lists, the OpenHands paper, All Hands' published founders, and an OpenAlex co-authorship search. Unpublished advisory or employment ties could exist. The GitHub username check is weak.
- **Disclosure scope:** the shared-institution disclosure is a judgment. Omitting it would be defensible, but disclosing is more transparent.
- **Numbers:** Table 3 values come from v4 layout extraction, with rows labelled by model. Earlier arXiv versions report different figures.
- **Version and date:** OpenHands version unstated; test date inferred from the models used.
- **Possible bias:** the pipeline uses SWE-agent, which could favour the competitor.
- **Benchmark scope:** Python-only feature requests, with a strict joint functional-and-security pass.

## Recommendation
**Approve** counting SusVibes for OpenHands (11 counted, 6 peer-reviewed, 61 / A unchanged) and recording SusVibes as peer-reviewed for Claude Code (6 peer-reviewed, 55 / A unchanged). Reasons:
- It is independent (no author overlap with OpenHands developers), peer-reviewed, and ran the named product.
- Treatment is consistent with 0048.
- No grade or score change is warranted by the evidence.

## Decisions requested
- **D1 Count (OpenHands):** count SusVibes as independent, peer-reviewed (ICML 2026), version unstated, test 2025–2026. Count 10 → 11; peer-reviewed 5 → 6.
- **D2 Independence and disclosures:** treat the CMU shared-institution tie as a disclosure, not an affiliation exclusion. Record Modal, Google Gemini API credits, HydroX AI, the CMU tie (no author overlap), and the SWE-agent pipeline.
- **D3 Adherence score:** keep 55 (recommended; overall 61) or lower to 50 (overall 60; index position changes, below AIDE). Completion 50, disputes 55 and evidence 85 are unchanged.
- **D4 Wording (OpenHands):** source row, completion, adherence (security), evidence, summary and disclosure text as above.
- **D5 Grade (OpenHands):** remains A, on the PBT-Bench basis. No methodology change.
- **D6 Claude Code:**
  - Record SusVibes as peer-reviewed (ICML 2026): peer-reviewed 5 → 6, with the wording above, including the uncertainty "three" → "four".
  - No score or grade change (55 / A); counted stays 15.
- **D7 Rollout:**
  - After approval, apply to both YAMLs and both pages (build plus apply_design.py).
  - Add decision record 0049 and one changelog row.
  - Run check_scores, check_links, overflow and axe on both pages.
  - Commit and push, then the manifest plus files.json. You deploy.
  - No recheck note added. This closes the 0040 SusVibes follow-up.

## Plain-English terms
- **FuncPass:** the share of tasks where the code passed the normal functional tests.
- **SecPass:** the share where it passed both the functional and the security tests.
- **pass@1:** one attempt per task.
- **Developer-affiliated:** an author works for or co-created the product. Such studies are not counted for that product.
- **Shared institution:** authors work at the same university as a developer, but did not build the product. Disclosed, still counted.
- **Peer-reviewed:** accepted after independent review; here, the ICML 2026 conference.
- **Round half up:** .5 and above rounds up (59.75 rounds to 60; 61.00 stays 61).
