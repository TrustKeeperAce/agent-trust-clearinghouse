# Decision 0003: OpenAI Deep Research

**Status: APPROVED by Remington, 2026-10-16.** The approval was conditional on verifying Mind2Web 2's venue.

**Condition met:** OpenReview lists Mind2Web 2 as a "NeurIPS 2025 Datasets and Benchmarks Track poster" (venueid NeurIPS.cc/2025/Datasets_and_Benchmarks_Track): https://openreview.net/forum?id=AUaW6DS9si (accessed 2026-10-16).

## Final public summary
"OpenAI Deep Research is a commercial ChatGPT feature that writes cited research reports. In independent evaluations (DeepResearch Bench, ICLR 2026; Mind2Web 2, NeurIPS 2025; ReportBench; a citation-URL study; TTD-DR preprint), it ranked among the stronger systems tested on report quality and task success, while a share of its citations did not match their sources or did not resolve. Most tests used 2025 versions; the underlying model has changed since. Informational only; not an endorsement or certification."

Scores: 60/65/60/75. Overall 65. Evidence grade B.

---
Accessed 2026-10-16.

## Draft entry summary
OpenAI Deep Research is a commercial agent in the Research category. Proposed overall score: **65/100**. Evidence grade: **B**. Independent sources: **5 performance**, plus 1 commentary.

The model behind it has changed over time: o3 at launch, an o4-mini "lightweight" version from April 2025, and now "latest models" by default. Most independent tests used 2025 versions.

## What happened
- **DeepResearch Bench** (ICLR 2026): RACE score 46.98, second among the deep-research agents listed (Gemini DR 48.88). Citation accuracy 77.96%, with 40.79 effective citations per task. Outputs were collected 2025-04-01 to 05-08.
- **Mind2Web 2**: full success on 28% of tasks (the highest of the systems listed), 54% partial completion, pass@3 0.40, about 8.4 minutes per task.
- **ReportBench**: cited statements matched their sources 78.87% of the time; non-cited facts were accurate 95.83% of the time; reference recall was 0.033.
- **Reference-hallucination study**: 10.1% of citation URLs did not resolve; 3.5% appear fabricated.
- **TTD-DR** used OpenAI DR as its comparison baseline and reported winning 69.1% and 74.5% of comparisons against it.
- **OpenAI's own claims (vendor):**
  - Scores of 26.6% on HLE and 67.36 on GAIA.
  - It can hallucinate facts and has weak confidence calibration.
  - Usage caps vary by plan, with a 30-day reset.
  - Research can be restricted to specific sites, and connected apps are used read-only.

## Sources checked
| Source | Type | Shows | URL |
|---|---|---|---|
|DeepResearch Bench|Independent, performance, peer-reviewed|Quality and citations|proceedings.iclr.cc/paper_files/paper/2026/file/465f22be10e07b301c6ed58f0472f704-Paper-Conference.pdf|
|Mind2Web 2|Independent, performance (NeurIPS'25 D&B per repo)|Task success|arxiv.org/abs/2506.21506|
|ReportBench|Independent, performance (venue unverified)|Citation match|arxiv.org/abs/2508.15804|
|URL-hallucination study|Independent, performance (preprint)|Fabricated URLs|arxiv.org/abs/2604.03173|
|TTD-DR|Independent, performance (preprint; competitor)|Head-to-head|arxiv.org/abs/2507.16075|
|The Conversation|Independent commentary|Early-test flaws|theconversation.com/…-249496|
|OpenAI launch post|Vendor|Benchmarks, limitations, caps history|openai.com/index/introducing-deep-research/|
|OpenAI Help Center|Vendor|Current limits and scope|help.openai.com/en/articles/10500283-deep-research|

Excluded: the CJR Tow Center and Nieman Lab tests. They evaluated ChatGPT *search*, not deep research.

## Evidence quality assessment
Evidence is strong in breadth: five independent performance studies, two of them peer-reviewed (DRB at ICLR 2026; Mind2Web 2 at NeurIPS D&B, per its repo). It is weaker in three ways:
- The tests are dated to 2025 model versions.
- The benchmarks rely on LLM judges.
- TTD-DR comes from a competitor, and its HLE figure appears to be copied from OpenAI.

## What the rules say
v0 weights are 30/20/25/25. With 3 or more independent sources an overall score is allowed; this entry has 5 performance sources.

## Proposed score breakdown (judgment calls)
| Factor | Score | Reason |
|---|---|---|
|Completion 30%|60|28% full and 54% partial success on hard tasks, the top rate among systems listed|
|Disputes 20%|65|No formal disputes found; 3.5% fabricated and 10.1% dead citation URLs; about 78% citation accuracy|
|Adherence 25%|60|Limits are documented by the vendor only; untested independently|
|Evidence 25%|75|5 independent performance sources, 2 peer-reviewed|

Overall = 0.3×60 + 0.2×65 + 0.25×60 + 0.25×75 = 18 + 13 + 15 + 18.75 = **64.75 → 65**

## Risks/uncertainties
- The current model is untested by these sources.
- Specific numeric usage caps are no longer published.
- Mind2Web 2 and ReportBench venues are partly unverified.
- Avoid repeating vendor benchmark claims as fact.

## Recommendation
**Approve publish**, after a quick check of the Mind2Web 2 NeurIPS proceedings listing (optional).

Proposed public summary: "OpenAI Deep Research is a commercial ChatGPT feature that writes cited research reports. In independent evaluations (DeepResearch Bench, ICLR 2026; Mind2Web 2; ReportBench; a citation-URL study; TTD-DR preprint), it ranked among the stronger systems tested on report quality and task success, while a share of its citations did not match their sources or did not resolve. Most tests used 2025 versions; the underlying model has changed since. Informational only; not an endorsement or certification."

## Plain-English terms
- **RACE / FACT:** report-quality and citation-checking scores.
- **Pass@3:** solved in at least one of three tries.
- **Hallucinated URL:** a link that likely never existed.
- **Non-resolving:** a link that doesn't load now.
- **Peer-reviewed:** accepted after expert review at a conference.
