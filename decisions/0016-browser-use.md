# Decision 0016: Browser Use (open-source library)

**Status: APPROVED by Remington, 2026-10-17.** Publish with overall score 51, evidence grade A. Confirmations:
- (A) Scope: the open-source library only, with results shown as model ranges; Browser Use Cloud is not scored.
- (B) 2025 tests count (continuity reading, as for Decisions 0003 and 0015).
- (C) New category "Browser/web agent" (closely related digital-task agents).
Grade and scoring rules are unchanged.

Accessed 2026-10-17 (America/New_York). Category: Browser/web agent (new category label; closest existing are Research/Verification). Batch 2, candidate 2.

## Draft entry summary
Proposed: **overall 51, evidence grade A**, 7 independent performance sources (3 peer-reviewed; 4 task-performance and 3 security).
Draft public wording: see `summary` in the YAML. It covers: open-source MIT library, model of the user's choice; independent success rates of about 2–5% (full success on hard cross-site tasks) to 18–45%, far below vendor figures; frequent prompt-injection susceptibility; CVE-2025-47241 fixed in 0.1.45; Cloud not covered; overall 51; standard disclaimer.

## Scope (decision point A)
- **Covered:** the open-source `browser-use` Python library (GitHub browser-use/browser-use, MIT, about 118k stars, active; current PyPI release 0.13.11), run with any language model.
- **Not covered:** Browser Use Cloud and the vendor's own bu-* models. The only figures for these are vendor-run (97% Online-Mind2Web, BU Bench), so the Cloud would be Insufficient evidence on its own.
- **Model dependence:** independent studies ran the library with 1–12 different models. The entry scores the library as a framework across the models tested, with the range shown, rather than one model pairing. Precedent: SAFE (D0009) also depended on the LLM and search API used, which was disclosed as an uncertainty.

## 1. What happened with sources
All PDFs were downloaded and the Browser Use sections were read. None was paywalled.

**Counted: independent performance sources (7)**
| # | Source | Venue | When / version | Browser Use result | Flags |
|---|---|---|---|---|---|
|1|Online-Mind2Web, Xue et al. (OSU) https://arxiv.org/abs/2504.01382|**COLM 2025** (stated on PDF)|Early 2025; GPT-4o; version not stated (≈0.1.x)|**30.0%** human-evaluated success on 300 live tasks (Operator 61.3%; SeeAct 30.7%); automatic judges vary (24.3–40.1%); 26% without / 31% with Google Search|Says Browser Use's earlier WebVoyager figure relied on lenient automatic evaluation|
|2|Holistic Agent Leaderboard, Kapoor et al. (Princeton) https://arxiv.org/abs/2510.11977 + https://hal.cs.princeton.edu/online_mind2web|Preprint (venue not shown on arXiv)|Runs with models from Jan–Aug 2025|Online-Mind2Web **18.3–40.0%** across 12 models (best Claude Sonnet 4; GPT-5 Medium 32.0%); AssistantBench subset 2.0–38.8%; Online-Mind2Web costs $9–$1,610 per run|Third-party reproduction; leaderboard and paper counted once|
|3|CAP, Xu et al. https://arxiv.org/abs/2608.08392|**COLM 2026** (stated on PDF)|Nov–Dec 2025; GPT-5, Claude 4.5 Sonnet, DeepSeek-V4-Flash|Partial completion 15.0 / 21.0 / 25.0%; **full success 2.0 / 5.0 / 2.9%** on 198 cross-site tasks (human 35.0 / 10.0%; Comet 48.0 / 6.0%)|Authors also used Browser Use to annotate websites|
|4|Skim, Wong et al. https://arxiv.org/abs/2605.16565|Preprint 2026|GPT-4o; cites the 2026 library|**45.0%** baseline accuracy on a 300+ task WebVoyager/WebShop subset|Authors propose a competing acceleration method; disclosed|
|5|VPI-Bench, Cao et al. (NUS) https://arxiv.org/abs/2506.02456|**ICLR 2026**|2025; GPT-5, GPT-4o, Sonnet-3.7, Gemini-2.5-Pro, Llama-4, DeepSeek-V3|Visual prompt-injection **attack success**: Amazon 73.7–100%, Booking 75.4–98.3%, Messenger 16.7–76.7%, Email 30–50%; defenses helped only partly|Security/safety evaluation|
|6|Patlan et al. (Princeton) https://arxiv.org/abs/2506.17318|Preprint|2025; GPT-4o|Plan injection up to **63%** attack success (context-chained), 19% with no context; privacy prompt-injection over 80%|Security evaluation|
|7|ARIMLABS, Mudryi et al. https://arxiv.org/abs/2505.13076|Preprint|**v0.1.44**|White-box audit: allowed_domains bypass (became CVE-2025-47241) and credential exfiltration via prompt injection (proof of concept, rated high, no CVE)|Security firm; it found the CVE itself|

**Other sources (not counted):**
- GHSA-x39x-9qw5-ghrf https://github.com/advisories/GHSA-x39x-9qw5-ghrf : GitHub-reviewed, critical; one duplicate advisory, GHSA-f54f-hr32-586f, was withdrawn as duplicate.
- CVE-2025-47241 https://www.cve.org/CVERecord?id=CVE-2025-47241 : CVSS 3.1 score 4.0 (Medium) from the CNA record, versus "critical" in GitHub's review and 9.3 in ARIMLABS's own rating. **Severity labels conflict.**
- Community pull requests on prompt injection: https://github.com/browser-use/browser-use/pull/5241 (merge status not verified). A second pull request found in search (pull/4762) returned 404 at publication and is not linked.
- The repo's security-advisories API lists only this one advisory.

**Excluded:**
- Vendor claims: 89.1% WebVoyager https://browser-use.com/posts/sota-technical-report (modified harness and manual corrections); 97% Cloud https://browser-use.com/posts/online-mind2web-benchmark ; BU Bench https://github.com/browser-use/benchmark .
- Cybernaut (Amazon) https://arxiv.org/abs/2508.16688 : its "Browser-Use 82.20%" WebVoyager figure is labeled SOTA and appears to restate the vendor result rather than a re-run (unclear). The authors also build a competing framework.
- Digital Applied blog https://www.digitalapplied.com/blog/open-source-browser-computer-use-agents-2026 : commentary only.

**Disputes/legal:** none found (no lawsuits or regulator actions).

## 2. What the rules say
- ≥3 independent performance sources. Security or safety evaluations count as performance sources (methodology: "security or safety evaluation"). CVE and advisory listings are "other".
- **Version/scope (decision point B):** the library changed a lot in 2025, including the 0.5 release (July 2025) and steady changes since; it is now at 0.13.11.
  - Sources #1, #5, #6 and #7 tested 2025 versions (#7 is explicitly 0.1.44).
  - #3 (late 2025) and #4 (2026) are the clearly recent ones. #2's library version is unstated.
  - This draft applies the **D0003/D0015 continuity reading**: same project and API, and the maintained product is continuous. Under a strict reading (that the 0.5+ rewrite is a new product, as in D0008 Open Interpreter), only #3 and #4 clearly count, giving **Insufficient evidence**.
- **Grade:** 7 sources, 3 peer-reviewed (COLM 2025, COLM 2026, ICLR 2026), and ≥1 testing a recent version within 12 months (#3, Nov–Dec 2025; #4, 2026). That meets **A**. The guide says the evidence factor should be ≥85, so 85 is proposed.
  - Caveat: whether #3 and #4 tested the "current version" depends on the continuity reading, since neither states a version number. If Remington prefers, grade **B** with evidence 80 (overall 50 = 49.5 rounded half up) is the alternative.

## 3. Proposed scores (judgment calls)
- **Completion 40:**
  - Best independent human-checked live-web success is around 30–40%. Full success on hard cross-site tasks is 2–5%.
  - It is well below Operator (61%) and comparable to the SeeAct research baseline.
  - Highly model-dependent.
- **Disputes 50:**
  - No legal or regulatory actions.
  - One security advisory (fixed), with conflicting severity labels, plus an un-CVE'd credential-exfiltration proof of concept.
  - Comparable to GPT Researcher (40, two advisories) but fewer issues.
- **Adherence to limits 30:** the main safety control (allowed_domains) was bypassable before 0.1.45, and injection attack success is very high across models and studies. Lowest adherence score in the directory (Perplexity 45).
- **Evidence quality 85:** 7 sources, 3 peer-reviewed, recent tests, multiple independent teams. Held at the bottom of the A band because versions are unstated and results vary by model.
- **Math:** 0.30×40 + 0.20×50 + 0.25×30 + 0.25×85 = 12 + 10 + 7.5 + 21.25 = **50.75, rounded to 51**.
- **Directory placement:** 51 sits below GPT Researcher (53). Scored order: SAFE 66, ODR 65, Gemini 63, Perplexity 54, GPT Researcher 53, Browser Use 51.

## 4. Risks/uncertainties
1. **Version scope (B):** a strict rewrite reading gives Insufficient evidence; the continuity reading gives A.
2. **Model dependence:** scores span from about 2% to 45% depending on model and benchmark. One number can mislead, so the factor notes show ranges.
3. **Grade A with a middling score:** first A in the directory. The grade describes evidence, not performance (methodology), but readers may misread it. Wording should stress this.
4. **Security severity conflict:** CVSS 4.0 (CNA) vs critical (GitHub review) vs 9.3 (ARIMLABS). The draft reports the advisory without choosing one.
5. **Old security tests:** whether #5–#7 findings still apply to 0.13.x is not tested. Prompt-injection pull requests suggest the issue class is still open (status not verified).
6. **Category:** "Browser/web agent" is a new category label and needs approval (decision point C), or map to an existing one.
7. HAL venue not verified (treated as a preprint). #3 is dated 2026 at COLM; its arXiv page says accepted.

## 5. Recommendation
**APPROVE** at overall **51**, grade **A**, covering the open-source library only, *provided* Remington confirms:
- **A.** Library-only scope with model-range reporting.
- **B.** Continuity version reading (as for Gemini).
- **C.** New category label "Browser/web agent".

If B is the strict reading instead: **Insufficient evidence** (no overall score), keeping the factor notes. If Remington wants the grade A/score tension avoided: grade B with evidence 80, overall 50.

## 6. Plain-English terms
- **Library / framework:** code that developers run themselves; it needs a separately chosen AI model.
- **Backbone / model:** the AI model the library calls (GPT-4o, Claude and so on).
- **Prompt injection:** hidden text on a web page that tricks the agent into following an attacker's instructions.
- **Attack success rate:** the share of attempts where the trick worked. Lower is safer.
- **CVE / GHSA / CVSS:** public vulnerability IDs and a 0–10 severity score.
- **Human-evaluated success:** people, not an AI judge, checked whether each task was really done.
