# Decision 0042: AIDE (Weco AI, open-source) — 60 / B; AutoKaggle (open-source) — Insufficient evidence

**Status: APPROVED by Remington, 2026-10-17** (D1–D8 approved as recommended). Two separate entries, both in the Data science agent category, both carrying a visible "Citation check incomplete — recheck later" note. D7: AutoKaggle stays Insufficient evidence now, with no extra Semantic Scholar wait.
Entries: agents/aide.yaml, public/agents/aide.html, agents/autokaggle.yaml and public/agents/autokaggle.html.

## Candidate and the one-or-two-entries question
Batch 4 #6 was listed as "AutoKaggle/AIDE". These are two unrelated products:
- **AIDE**
  - Developer: Weco AI.
  - Release: PyPI aideml v0.2.2 (5 Nov 2025). GitHub WecoAI/aideml, MIT licence, about 1.6k stars.
  - Activity: last commit 16 Oct 2026; actively maintained.
- **AutoKaggle**
  - Developer: the M-A-P research community (Ziming Li, Ge Zhang et al.).
  - Release: none tagged. GitHub multimodal-art-projection/AutoKaggle, Apache-2.0, about 320 stars.
  - Activity: last commit 4 Dec 2024. Published at the DL4C workshop at ICLR 2025.

They differ in design (tree search over code vs a fixed six-phase multi-agent pipeline) and in developers, and they share no evidence base. **Recommendation: two entries (D1).** AIDE is scored. AutoKaggle is Insufficient evidence.

## Affiliation checks
- **AIDE developers:** Zhengyao Jiang, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Yuxiang Wu and Deniss Jacenko (Weco AI), plus Dominik Schmidt (Runway ML, listed as a co-first author).
  - I checked the author blocks of all screened papers.
  - **FML-bench (2605.17373) has Zhengyao Jiang (Weco) as a co-author, so it is excluded for AIDE.**
  - No other counted paper has Weco authors. MLE-bench's mentions of Weco are citations and a comparison with Weco's own report.
- **Funding:** no counted paper acknowledges Weco funding or support.
- **Disclosures (competing-method authors count with disclosure):**
  - MLE-bench: OpenAI (model vendor; runs the MLE-bench leaderboard).
  - MARS: Google (competing method; supplies the Gemini models used).
  - ArchPilot: Meta (competing method).
  - SPIO, InnoGym and CO-Bench propose or evaluate alternatives.
  - InnoGym and "Can We Predict" share a Zhejiang University / Ant Group group.
- **AutoKaggle developers:** M-A-P (Li, Zang, Ma, Guo, Zheng, Liu, Niu, Wang, Yang, Liu, Zhong, Zhou, Huang, Zhang). Neither counted paper (VDSAgents, SPIO) has overlapping authors. Both propose competing methods.

## Proposed score: AIDE
| Factor | Weight | Score |
|---|---|---|
| Completion | 30% | 50 |
| Disputes | 20% | 70 |
| Adherence | 25% | 45 |
| Evidence | 25% | 80 |

- 15 + 14 + 11.25 + 20 = 60.25, which rounds to **60, grade B**.
- The grade fails A only on the version condition: no independent test in the last 12 months states the AIDE version.
- **I set the evidence score from the evidence itself, not to fit the grade range.**
  - Strengths: 13 counted sources, 6 peer-reviewed.
  - Weaknesses: most counted studies are competing-method baselines, several used forks adapted for their benchmark, and versions are almost never stated.
  - Compared with SWE-agent (80: 8 counted, 6 peer-reviewed, also unversioned), AIDE has more sources, but they are weaker as product tests. So I kept it at 80.
  - 80 also falls inside the 70–84 guide for B. That is a coincidence, not the reason.
- **check_scores** on a temporary repo copy:
  - "OK aide: overall 60 (computed 60), grade B, counted 13, peer-reviewed 6"
  - "OK autokaggle: Insufficient evidence, counted 2"
- **Comparables:** Data Interpreter 49 B (Data science agent), SWE-agent 58 B, OpenHands 61 A.
- **Factor rationale:**
  - Completion 50: strong on MLE-bench when first published and ahead of general-purpose agents on Kaggle-style tasks, but newer methods, and even simple baselines, match or beat it.
  - Disputes 70: no CVEs or legal action; actively maintained. One validity point: MLE-bench notes Weco's own claim used easier tasks.
  - Adherence 45: data-science failure modes (85–88% of pipelines report a single metric), well below expert solutions on fairness, and sabotage was possible under instruction. No study of unprompted unrequested actions.

## Counted: AIDE (13 independent performance sources)
| # | Source | Peer review | Version / date | Key figures |
|---|---|---|---|---|
| 1 | MLE-bench 2410.07095 (OpenAI) | ICLR 2025 | MLE-bench-adapted AIDE, 2024 | Medal 16.9% (o1-preview); GPT-4o 8.7% vs MLAB 0.8%, OpenHands 4.4% |
| 2 | CTRL-ALT-DECEIT 2511.09904 (LawZero, Apollo, Imperial) | NeurIPS 2025 | unstated, 2025 | Claude 3.7 + AIDE just above human median, ahead of ReAct; instructed sabotage sometimes undetected; monitors overall highly effective |
| 3 | CO-Bench 2504.04310 (CMU) | AAAI 2026 | unstated, 2025 | Below BestOfN on most metrics; higher valid-solution rate |
| 4 | InnoGym 2512.01822 (ZJU / Ant) | ICLR 2026 | unstated, 2025 | Lowest of 3 frameworks on novelty (N 23.33 vs MLAB 39.58) |
| 5 | Can LLM Agents Discover? 2608.30047 | COLM 2026 | unstated, 2026 | Attempt success 45.0% (GPT-5), 26.2% (Qwen3-32B) |
| 6 | SPIO 2503.23314 | ACL 2026 | unstated, 2025 | Close to baselines (Titanic 0.7775, GPT-4o); below SPIO 0.7871 |
| 7 | TimeSeriesGym 2505.13291 | preprint | Fork made May 2025 with MLE-bench changes | Valid 57.3%, reasonable 12.5% (GPT-4.1); beats OpenHands as a scaffold |
| 8 | ML-Dev-Bench 2502.00964 | preprint | unstated, 2025 | 17% success with GPT-4o (OpenHands + Sonnet 50%) |
| 9 | MARS 2602.02660 (Google) | preprint | unstated, 2026 | MLE-bench Lite any medal 36.4% / 53.0% (Gemini 2.5 Pro / 3 Pro Preview); below AIRA-dojo and MARS |
| 10 | ArchPilot 2511.03985 (Meta / UIUC) | preprint | unstated, 2025 | Valid 78.7%; beat 55% of teams vs ArchPilot 66% (same budget) |
| 11 | Simple Baselines 2602.16805 | preprint v2 Oct 2026 | unstated, 2026 | Simple sequential search matched or beat AIDE on 6 of 10 |
| 12 | Be Fair! 2606.04971 | preprint | Default configuration, 2026 | Better than MLZero on AUC and fairness gap with far fewer tokens (about 6M vs 86M); all agent pipelines at least 10 AUC points below experts |
| 13 | Silent Failures 2610.14115 (CWI) | preprint Oct 2026 | unstated, 2026 | Single eval metric in 85–88% of AIDE pipelines; fixes missing validation splits; some leakage failure modes increased with a small model |

## Counted: AutoKaggle (2 sources, Insufficient evidence)
| # | Source | Peer review | Key figures |
|---|---|---|---|
| 1 | VDSAgents (Stat, Wiley 2026; 2510.24339) | yes | Valid-output rate 0.577 (DeepSeek-V3) / 0.534 (GPT-4o) across 9 datasets; VDSAgents 0.894 / 0.950, Data Interpreter 0.676 / 0.672 |
| 2 | SPIO (ACL 2026) | yes | Close to baselines (Titanic 0.7781, GPT-4o); below SPIO |

The remaining citing papers, including MLE-Dojo, Agent K, EvoDS, DatawiseAgent, "Can Agentic AI Match…" and LongDS-Bench, only describe AutoKaggle.

## Other (not counted)
**AIDE:**
- AIRA-dojo (Meta): a re-implementation of AIDE that beat the original MLE-bench results by 10.68 points. It also found agent-reported validation medal rates were higher than held-out test rates.
- MLE-Dojo (NeurIPS 2025): integrates AIDE, but I found no AIDE-specific results.
- Can We Predict Before Executing (ACL 2026): uses AIDE trajectories as data.
- FML-bench: excluded because of the Weco co-author. AIDE was mid-tier.
- AutoMLGen: reuses the MLE-bench figures.
- aideml issue #100: a dependency path-traversal fix in October 2026.
- TraceML: applies a tracing tool to AIDE runs. Context only.

**AutoKaggle:** none.

## Not counted
- The AIDE technical report and Weco's April 2024 blog (vendor).
- The MLE-bench leaderboard (leaderboard).
- AutoKaggle's own paper (0.85 valid submission rate, 0.82 comprehensive score; developers).

## Citation gate
- **Semantic Scholar:**
  - AutoKaggle: the 18:41 batch loop got a 200 for "AutoKaggle multi-agent" (s2_2.json), but the keyword search is dominated by unrelated multi-agent RL papers.
  - AIDE: a new loop over 3 AIDE queries ran 19:19–19:28 EDT (9 minutes). One query returned 200 (s2_aide1.json, 1,590 results) with no new AIDE-specific titles; the others were rate-limited.
  - Per the workflow, I switched to OpenAlex (oa_autokaggle.json, 53; oa_aide.json, 100) and title lookups, and noted the switch.
- **No full 30-minute wait:**
  - AIDE has 13 counted (well above 7) and 6 peer-reviewed (above 3).
  - The A/B outcome depends only on the version condition. Extra citations are unlikely to add a versioned recent test.
  - AutoKaggle has 2 counted against a threshold of 3, which is technically one away. But the OpenAlex citing set was screened fully by title, and every likely runner was checked. If you want certainty on AutoKaggle, a full wait is an option (see D7).
- **Unscreened (→ "Citation check incomplete — recheck later" on both entries):**
  - AIDE: BioML-bench (bioRxiv PDF did not download), OPT-BENCH (2 mentions), Demystify Memory in MLE Agents (Findings ACL 2026), MLAlgo-Bench, Tree-Notebook, METR RE-Bench.
  - AutoKaggle: Tree-Notebook.
- **OpenAlex notice:** the OpenAlex API response included a notice suggesting I register an API key with your email. I did not act on it.
- **Files:**
  - /workspace/batch-next/ak/ (PDFs and text)
  - s2log.txt
  - s2_2.json and s2_aide1.json
  - oa_*.json, including the saved Codex batch (oa_codexcli.json) for the next candidate

## Reading depth
- Targeted checks only: figures, version, date, authors and acknowledgements.
- No full reads. No single paper can move AIDE across a grade boundary, and the AutoKaggle runners are clear.

## Rules applied
- 0036 cautions:
  - Vendor results are not counted.
  - The named product must be tested, so re-implementations are listed as other.
  - Developer co-author studies are excluded, for that product only.
  - Competing-method authors count with disclosure.
  - Version and test date are recorded.
- Version condition per the 0025 clarification and the SWE-agent (0038) precedent.

## Risks
- AIDE: a reviewer could argue forks (MLE-bench, TimeSeriesGym) are modified products. Removing both still leaves 11 counted and 5 peer-reviewed, so the outcome is unchanged.
- AIDE: CTRL-ALT-DECEIT measures instructed sabotage capability. I used it in adherence with that caveat.
- AutoKaggle: one more runner would move it to B- (3 sources). Tree-Notebook is unscreened.
- The category "Data science agent" matches Data Interpreter. AIDE could arguably be "ML engineering", but no such category exists.

## Decisions requested
- **D1:** Two separate entries, AIDE and AutoKaggle, both recorded under decision 0042 (or renumber AutoKaggle as 0042b / 0043, at your preference).
- **D2:** Both in category Data science agent. Names: "AIDE (Weco AI, open-source)" and "AutoKaggle (open-source)".
- **D3:** AIDE scope is aideml v0.1.x–v0.2.2 plus main. AIRA-dojo and other re-implementations, and Weco's commercial platform, are excluded.
- **D4:** FML-bench excluded for AIDE because of the Weco co-author.
- **D5:** Count competing-method baselines and benchmark-adapted forks with disclosure (MLE-bench, TimeSeriesGym).
- **D6:** AIDE 50/70/45/80 = 60, grade B (version condition), with evidence scored on the evidence and not fitted to the grade range.
- **D7:** AutoKaggle as Insufficient evidence (2 counted, both peer-reviewed). Optionally do a full 30-minute Semantic Scholar wait or screen Tree-Notebook first.
- **D8:** Visible "Citation check incomplete — recheck later" note on both entries.

## Recommendation
Approve D1–D8 and publish AIDE at 60/B and AutoKaggle as Insufficient evidence, both with the recheck note.

## Plain-English summary
- **AIDE:** Thirteen outside studies ran it. It was a leading approach when OpenAI's MLE-bench came out and beats general-purpose agents on Kaggle-style tasks. Newer methods, and sometimes simple baselines, now match or beat it. Studies flagged thin evaluation reporting and fairness gaps. No security or legal problems were found, and it is maintained. Score 60, grade B, because no recent test states the version.
- **AutoKaggle:** Only two outside studies ran it, so it is not scored. In one it produced valid output only about half the time. It has not been updated since December 2024.

## Draft files (private)
- /workspace/private-drafts/aide.yaml
- /workspace/private-drafts/autokaggle.yaml
- /workspace/private-drafts/aide-preview/aide.html and autokaggle.html (overflow check passed at 375 and 1280, light and dark)
- /workspace/private-drafts/build_preview_0042.py
