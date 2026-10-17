# Decision 0027: Skyvern (open-source)

**Status: APPROVED by Remington, 2026-10-17**, as Insufficient evidence, as recommended. Category: Browser/web agent. Decisions:
1. D1: Insufficient evidence (2 counted independent performance sources; minimum 3).
2. D2: Web Bench is excluded as vendor co-built (Skyvern and Halluminate) and run on Skyvern infrastructure. It is listed, not counted.
3. D3: The two Fudan papers are counted separately, with the shared authors disclosed.
4. D4: Library only. Skyvern Cloud is out of scope; its privacy policy was not reviewed.
5. D5: 0.1.x to 1.0.x is treated as continuous.
6. D6: CVEs are described neutrally: CVSS attributed to MITRE / VulnCheck, NVD status Deferred, fixes noted, no extra severity wording. The Exploit-DB exploit is not linked; the page notes only that one is public.
7. D7: Emergence's task-rewording criticism is reported as their finding, with competing-author disclosure.

## Counted independent performance sources (2; minimum 3)
1. When Bots Take the Bait, arXiv 2601.07263 (Jan 2026, preprint, full read). GPT-4o. Benign completion 84.4% on 500 WebVoyager tasks (80.2-83.2% with defences). Social-engineering attack success averaged 62.6%.
2. WebTrap Park, arXiv 2601.08406 (Jan 2026, preprint, full read). Code accessed 11 Jan 2026. Score = 1 - attack success rate: 72.29 (Claude 4 Sonnet), 70.44 (o3), 61.67 (GPT-4o), the lowest of 4 frameworks at that model.
   Both papers are from overlapping Fudan authors. They are counted as separate studies with the overlap disclosed.

## Listed, not counted
- Skyvern WebVoyager 85.85%: vendor-run, in Skyvern Cloud, on a modified task set.
- Web Bench 64.4%: co-built and run by Skyvern. Excluded (D2).
- eval.skyvern.com Odysseys: vendor.
- Emergence WebVoyager, arXiv 2603.29020: critique only, competing author. Other source.
- Whose Agent Are You?, arXiv 2606.20910: fingerprinting. Other source.
- CVE-2025-49619 and CVE-2026-82447: other sources.
- Checked, no Skyvern test found: Online-Mind2Web, BrowseComp, WebArena, HAL, Mind2Web 2, VPI-Bench, AdInject, WebGuard, CAP (2608.08392), Hidden Dangers (2505.13076).

