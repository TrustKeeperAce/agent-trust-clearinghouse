# Decision 0019: OpenAI Deep Research, version-scope recheck (entry D0003, currently 65 / B)

**Status: APPROVED by Remington, 2026-10-17.** Confirmations:
1. Keep 65 / B (continuity reading).
2. Add the dated version note with OpenAI source links (archived release notes and help page).
3. Add ShadowLeak (Radware; fixed August 2025) to the security notes.
4. Set last-reviewed to 2026-10-17.
5. **The re-review methodology clarification (decision point 3) is NOT adopted.**

## 1. What happened (facts and sources)
**OpenAI primary sources:**
- **2 Feb 2025:** deep research launched in ChatGPT, "powered by a version of the upcoming OpenAI o3 model". https://openai.com/index/introducing-deep-research/
- **24 Apr 2025:** OpenAI added a lightweight version on o4-mini, used once the full-version limit is reached (same page).
- **17 Jul 2025:** a deeper version became part of ChatGPT agent; "the original deep research functionality remains available" in the tools menu (same page).
- **10 Feb 2026, "Updates to deep research":** OpenAI added site restriction, connections to any MCP server or app, an editable research plan, real-time progress with mid-run interruption, and a redesigned sidebar and fullscreen report view. **The release note names no model.**
  - Sources: same page, plus the release notes as archived by the Wayback Machine on 21 Mar 2026: https://web.archive.org/web/20260321044001/https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- **19 Mar 2026 notice, verified in the same archived release notes:**
  > "The legacy deep research mode will be removed on Thursday, March 26, 2026. This change only affects the legacy mode; the current deep research experience will remain unchanged. Historical conversations and results will remain accessible."
- **Help Center, current page:** https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt
  - "Deep research is powered by the latest models … If you prefer, you can choose a legacy model for a deep research task."
  - Entry points: /Deepresearch, the tools menu or the sidebar.
  - Deep research uses read actions only from connected apps.
  - No model is named.
- **ChatGPT agent:** retired (see D0018). Deep research was never removed; it stays a separate feature.
- **ChatGPT Work:** I found no OpenAI primary source saying deep research moved into Work. A search-result summary claimed it is available "in Chat and, where supported, Work". **Not verified.**

**Secondary sources only (not verified with OpenAI):**
- Blogs say the current deep research "runs on GPT-5.2" and that the legacy mode was the original o3 version:
  - https://findskill.ai/blog/openai-deep-research-legacy-removal/
  - https://www.davidborish.com/post/google-s-new-deep-research-max-agent-scores-93-on-benchmarks
- Treat both claims as unconfirmed.

**What versions the 5 counted sources tested:**

| Source | What it tested | Version |
|---|---|---|
| DeepResearch Bench (ICLR 2026) | OpenAI DR outputs collected in 2025 | 2025, o3-era |
| Mind2Web 2 (NeurIPS 2025 D&B) | Runs in mid-2025 | 2025 |
| ReportBench (arXiv Aug 2025) | 2025 | 2025 |
| Citation-URL study (Rao, UPenn; arXiv 3 Apr 2026), https://arxiv.org/abs/2604.03173 | The **pre-collected DeepResearch Bench outputs** ("openai-deepresearch", 4,121 URLs) | 2025 data, despite the 2026 date |
| TTD-DR (Google; preprint 2025) | 2025 | 2025 |

So **all 5 counted sources tested the pre-February-2026 version**, which is essentially the mode removed on 26 Mar 2026. The Feb 2026 update itself is not tested.

**New independent tests of the current version:** none found.
- DRACO (Perplexity, 2602.11685) tested the API models o3-deep-research-2025-06-26 and o4-mini-deep-research. That is the API, not ChatGPT; the authors are a competitor; and it was already excluded in D0015. Not counted.
- S1-DeepResearch (arXiv 2606.15367) is by builders of a competing agent. It reports OpenAI-DeepResearch rows that appear to come from earlier results, and its GPT-5.2 rows are for the base model. Not a test of the current ChatGPT feature.
- The SOTA2 leaderboard aggregator lists "OpenAI DeepResearch, reproduced 2026.06" with nearly identical scores. Its provenance is unverified. Not counted.

**Disputes:** nothing new found. ShadowLeak (Radware, Sep 2025) was a zero-click Gmail exfiltration in deep research, fixed in Aug 2025: https://www.radware.com/blog/threat-intelligence/shadowleak/
- **The current entry does not mention ShadowLeak (checked: 0 mentions in the YAML and the page).**

## 2. What the rules say
- **D0010:** a source counts only if it tested the product, version and scope covered by the entry.
- **D0003 (this entry), D0015 (Gemini) and D0016 (Browser Use) use a continuity reading:** tests of earlier versions count when the product is continuous and mainly the model changed.
- **D0008 (Open Interpreter):** earlier-version tests were not counted where the product was substantially different.
- **D0018 clarification:** retired products are not given new scored entries; their tests may be listed as historical context.
  - Deep research is **not retired**: same name, same entry point, and OpenAI says "the current deep research experience will remain unchanged". Only the legacy *mode* was removed.
  - D0018 also governs *new* entries, so it does not by itself apply to this existing one.
- Grades: B = 5–6 sources. The "current version within 12 months" condition applies only to grade A.

## 3. Options

| Option | Counted sources | Score / grade | Notes |
|---|---|---|---|
| **1. Keep with a version note** (continuity reading, as for Gemini) | 5 | **65 / B, unchanged** | Add a dated version note: the legacy mode was removed 26 Mar 2026, the Feb 2026 update is untested, and the counted tests used 2025 versions. Refresh last-reviewed. |
| 2. Change scope to "current version (Feb 2026 onwards)" only | 0 | **Insufficient evidence** | Strict D0008-style reading. Inconsistent with D0015 (Gemini 2.5→3.1 counted) unless that entry is rechecked too. |
| 3. Update scope or score in other ways | 5 | 65 / B (no new data to change factors) | With no new tests, none of the factor inputs change. Lowering evidence quality only for age would be a new rule. |
| 4. Mark as retired | n/a | n/a | **Not applicable.** The product is live; only a legacy mode was removed. |

## 4. Risks and uncertainties
- The model behind current deep research is not named by OpenAI. The "GPT-5.2" claim is secondary only.
- OpenAI says users "can choose a legacy model" for deep research. It is unclear whether the o3 deep-research model is still selectable, which would mean the tested version is still partly available.
- The Feb 2026 update is substantial (new controls and app connections), not only a model change. That makes the continuity reading weaker here than for Gemini; it is a judgment call.
- All evidence is now 2025-dated. The entry may overstate how well it describes today's product.
- Consistency: whatever is decided here should also apply to Gemini Deep Research (D0015) and Perplexity.

## 5. Recommendation
**Option 1: keep 65 / B** under the continuity reading, consistent with D0003 and D0015. Add a dated version note, roughly:
> "OpenAI updated deep research in February 2026 and removed the legacy mode on 26 March 2026. The counted tests used 2025 versions; the current version has not been independently tested."

Also:
- Add ShadowLeak to the security/disputes notes; the entry does not mention it.
- Set last_reviewed to 2026-10-17.
- Keep watching for tests of the current version.

If Remington prefers a strict reading, choose Option 2 (Insufficient evidence). In that case, Gemini (D0015) should be rechecked under the same reading.

**Decision points:**
1. Continuity reading (Option 1) or strict reading (Option 2).
2. Whether to add ShadowLeak.
3. Whether to set a general re-review trigger when a vendor removes a version. That would be a methodology clarification, flagged separately.

## 6. Plain-English terms
- **Legacy mode:** the older version of a feature, which the vendor has switched off.
- **Continuity reading:** counting tests of older versions because the product is essentially the same one.
- **Strict reading:** counting only tests of the exact current version.
- **Version note:** a dated sentence telling readers which versions the evidence covers.
- **Retired:** switched off entirely (not the case here).
