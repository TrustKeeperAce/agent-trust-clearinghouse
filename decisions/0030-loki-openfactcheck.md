# Decision 0030: Loki and OpenFactCheck

**Status: APPROVED by Remington, 2026-10-17**, as two entries, both Insufficient evidence, as recommended. Category: Verification. Decisions:
1. D1: Two separate entries (loki, openfactcheck), both Insufficient evidence.
2. D2: Each page links to the other and notes the shared MBZUAI-linked authors (Yuxia Wang, Minghan Wang, Preslav Nakov).
3. D3: Developer papers (Loki COLING 2025 demo; OpenFactCheck EMNLP 2024 demo and COLING 2025) are listed, not counted.
4. D4: Category Verification. OpenFactCheck's Type field says framework.
5. D5: Libraries only. Hosted demos (loki.librai.tech; the OpenFactCheck web app) are out of scope and did not respond on 17 October 2026.
6. D6: Loki dormancy is noted: no code changes since June 2024 (last commit Oct 2024, README).
7. D7: OpenFactCheck is treated as continuous up to 1.1.2. The 2.0 alpha series is not assessed.
8. D8: Neutral notes: licence metadata differs (repository AGPL-3.0, PyPI GPL-3.0); no CVEs or security advisories found. UFO (AAAI 2026) and the Mitchell write-ups are context only.

## Citation check (gate, run 2026-10-17 before publishing)
Semantic Scholar's citation lists were retrieved for all four developer papers: Loki arXiv 2410.01794 (27 citing papers); OpenFactCheck arXiv 2405.05583 (20), arXiv 2408.11832 (48) and DOI 10.18653/v1/2024.emnlp-demo.23 (48). That is 86 unique citing papers. Full text was read for 57 arXiv papers and the open-access versions of the others. The rest (paywalled IEEE, Elsevier and similar) were checked by abstract only.

Result:
- **Loki: 2 independent tests found** (ran Loki and reported measurements; no shared authors with Libr-AI/MBZUAI):
  1. TAIGR, arXiv 2601.20032 (Jan 2026, preprint; Purdue). Loki adapted as a baseline for health-claim validation in TikTok influencer videos (PubMed evidence, GPT-4.1-mini): macro-F1 0.43 (Incorrect 0.71, Partially correct 0.29, Correct 0.29), vs TAIGR 0.52.
  2. Proof-of-Guardrail, arXiv 2603.05786 (2026, preprint; Sahara AI and USC). Loki as a fact-checking guardrail on FacTool-KBQA: non-factual P 0.71 / R 0.81 / F1 0.76; factual P 0.74 / R 0.61 / F1 0.67. Latency 20.4 s vs 16.0 s mean in a TEE.
  These are counted, so Loki's count goes from 0 (approved packet) to 2. That is still below the three-source minimum, so the outcome is unchanged: Insufficient evidence.
- Used Loki as a tool without evaluating it (not counted): WildSEEK (2608.30683), When the Chain Breaks (2603.21286), ADMIT (2510.13842), Czech claim metrics (2511.14566). Described only: CAAFC (2605.12436), UrduFactCheck, UFO (AAAI 2026).
- **OpenFactCheck: 0.** All citing papers cite or describe it; none ran it as a tested system (ADMIT names it only as an example RAG application).

## Sources
See agents/loki.yaml and agents/openfactcheck.yaml.
