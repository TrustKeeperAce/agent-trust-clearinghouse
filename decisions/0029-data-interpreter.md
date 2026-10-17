# Decision 0029: Data Interpreter (MetaGPT, open-source)

**Status: APPROVED by Remington, 2026-10-17**, at 49 / B as recommended. Category: Data science agent (new). Decisions:
1. D1: 49 / B, with 9 counted sources (2 peer-reviewed). Grade B under the 0025 clarification.
2. D2: The 8 competing-agent papers are counted, with rival-author disclosures.
3. D3: The reproduction gap is described neutrally under disputes, as the papers' finding.
4. D4: Library only, with model ranges. MGX / MetaGPT X and MetaGPT's other roles are out of scope.
5. D5: Continuous product from 2024 through 0.8.2, with a dormancy note.
6. D6: Neutral CVE section: each CVSS figure names its scorer and gives the NVD status. Data Interpreter CVEs are listed separately from framework-wide ones. No severity wording, no exploit links.
7. D7: The security study's low attack success rate is reported with the authors' limited-functionality caveat and the 9.3% severe-outcome finding.
8. D8: New category "Data science agent", added to the methodology's Categories list.
9. D9: MetricsAI and Jupiter are excluded; I-MCTS is not counted.

## Proposed score
| Factor | Weight | Score | Points |
|---|---|---|---|
| Completion rate | 30% | 45 | 13.50 |
| Disputes | 20% | 35 | 7.00 |
| Adherence to limits | 25% | 45 | 11.25 |
| Evidence quality | 25% | 70 | 17.50 |
| Total | | | 49.25, rounded half up to **49** |

Grade **B**: 9 counted sources but only 2 peer-reviewed, which fails the A condition of 3+ peer-reviewed. This applies the 0025 clarification (7+ sources failing an A condition = B). The current-version condition is likely met by 2026 studies, but the peer-review condition is not.

## Counted independent performance sources (9, all full reads)
Every source except no. 9 proposes a competing agent; competing-author disclosure applies to each.
1. **DatawiseAgent** (EMNLP 2025, peer-reviewed), https://aclanthology.org/2025.emnlp-main.58/
   - InfiAgent-DABench re-run: 75.78% with GPT-4o and 67.70% with GPT-4o-mini.
   - The developers reported 94.93%; the authors say they could not match it.
2. **DataMind** (ICLR 2026, peer-reviewed; Zhejiang University / Alibaba), https://arxiv.org/abs/2509.25084
   - Could not reproduce 94.93%.
   - DABench pass@1 54.09–67.70% and TableBench 27.99–61.98% across 4 open models.
3. **EvoDS** (HKUST, preprint June 2026), https://arxiv.org/abs/2606.03841
   - Average over 4 benchmarks: 0.288 (GPT-4o), 0.299 (DeepSeek-V3.1), 0.316 (o4-mini).
   - Below a plain ReAct agent with every model.
4. **Fail Loudly** (preprint Sept 2026), https://arxiv.org/abs/2609.32528
   - KramaBench: 0.256–0.301 across 3 models, 0.382 when gold sources are supplied; human 0.768.
5. **Blackboard** (UMass Amherst / Google Cloud AI Research, preprint), https://arxiv.org/abs/2510.01285
   - KramaBench 30.34% with Gemini 2.5 Pro.
6. **SPIO** (preprint), https://arxiv.org/abs/2503.23314
   - 12 Kaggle/OpenML tabular tasks with 3 models; Data Interpreter competitive with AIDE.
7. **VDSAgents** (preprint Oct 2025), https://arxiv.org/abs/2510.24339
   - Execution stability 0.676 (DeepSeek-V3) and 0.672 (GPT-4o).
8. **UrbanDS** (preprint 2026), https://arxiv.org/abs/2607.26724
   - UrbanDS-Bench 3.3%, CoDA-Bench 5.0%.
9. **Data Agents Under Attack** (NTU, preprint June 2026; security study), https://arxiv.org/abs/2606.08661
   - Mean attack success about 12.9%, the lowest of 4 open-source data agents.
   - The authors attribute this to limited functionality, not stronger defence.
   - When attacks did connect, it had the largest share of the most severe outcome level (BR4, 9.3%).

## Other sources (not counted as performance)
- **CVE-2026-4516** (Data Interpreter write_analysis_code.py, up to 0.8.1): CVSS 3.1 6.3 per VulDB; NVD Analyzed; VulDB says the vendor did not respond.
- **CVE-2026-19058** (data_interpreter.py, up to 0.8.2): CVSS 3.1 5.3 per VulDB; NVD Deferred.
- **CVE-2026-0760 and CVE-2026-0761**: MetaGPT framework; CVSS 3.0 9.8 per ZDI; published as 0-day advisories on 9 Jan 2026 after no vendor update.
- **CVE-2024-23750**: QaEngineer role, through 0.6.4; CVSS 3.1 8.8 per NIST.
- **CVE-2026-19059 and CVE-2026-19060**: CVSS 3.1 3.3 and 5.3 per VulDB; NVD Deferred.
- **Repository status**: last commit 21 Jan 2026, last release 0.8.2 (9 Mar 2025), no GitHub security advisories published.
- No fixes have been identified for the Data Interpreter CVEs.

## Not counted
- **Developer paper** (Findings of ACL 2025): 94.93% DABench. Vendor claim.
- **MetricsAI** (2506.00856): includes a Data Interpreter co-author (Tuo Zhou), so it is developer-affiliated.
- **Jupiter** (2509.09245): its Data Interpreter figures are copied from DatawiseAgent, not re-run.
- **Mentions without a usable Data Interpreter run**:
  - LAMBDA (2407.17535): qualitative case study only.
  - DataSciBench (2502.13897): uses Data Interpreter as a tool for generating data.
  - I-MCTS (2502.14693): Data Interpreter is the experimenter inside SELA (MetaGPT team); not a standalone test.
  - Surveys.
- **MetaGPT-team follow-ups** (SELA, AFlow): vendor.

