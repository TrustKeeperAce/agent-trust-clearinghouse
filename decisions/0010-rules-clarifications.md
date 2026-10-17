# Decision 0010: Rules clarifications

**Status: APPROVED by Remington, 2026-10-16.** All three rules (Items 1–3) and all 13 cleanup fixes (Item 4) approved as proposed and applied: methodology.html updated to Scoring rules v0.1; entries cleaned up; no score, grade, status or approved summary changed (disclaimer sentence standardized only).

Files audited: `public/methodology.html`, `agents/*.yaml` (8 entries plus the schema), `public/agents/*.html` (8), `decisions/0001–0009`.

---

## 1. What happened (audit facts)

### 1a. Per-entry summary
| Entry | Completion / Disputes / Adherence / Evidence | Weighted overall | Shown | Grade | Independent sources as recorded | Do the independent sources test performance? |
|---|---|---|---|---|---|---|
| OpenAI Deep Research (`agents/openai-deep-research.yaml`, D0003) | 60 / 65 / 60 / 75 | 64.75 | 65 | **B** | 5 performance, 1 other | 5 tests (DeepResearch Bench, ICLR 2026; Mind2Web 2, NeurIPS 2025; ReportBench, preprint; citation-URL study, preprint; TTD-DR, preprint). The other source (The Conversation) is commentary. |
| Perplexity (`perplexity.yaml`, D0004) | 55 / 35 / 45 / 75 | **53.5** | 54 | **B** | 6 performance, 3 other | 6 tests (CJR Tow Center test plus 5 papers in peer-reviewed venues). The 3 others are court records, which do not test performance. |
| GPT Researcher (`gpt-researcher.yaml`, D0002) | 55 / 40 / 50 / 65 | 53.25 | 53 | **B-** | 3 performance, 2 security | 3 tests (DeepResearchGym, ICTIR 2026; Deep Research Comparator, WWW 2026 Companion; TTD-DR, preprint by authors of a competing system). The 2 security sources (NVD, GitHub Advisory DB) list vulnerabilities and do not test performance. |
| Google DeepMind SAFE (`google-deepmind-safe.yaml`, D0009) | 65 / 80 / 60 / 60 | **65.5** | 66 | **B-** | 3 performance, 2 other | 3 peer-reviewed tests (Zhao et al., ACL Findings 2025; FactBench, ACL 2025; VeriScore, EMNLP Findings 2024). All three are by authors of competing methods. The 2 others are journalism (VentureBeat, ForkLog) reporting a critique. |
| Pactum (`pactum.yaml`, D0005) | none | n/a | Insufficient evidence | n/a | 1 performance (partly independent), 4 other | 1 test (an unreviewed BTH master's thesis using customer data). The HBR case study was co-written by the customer, so it is not independent. The other 4 are journalism or commentary. |
| Clay (`clay.yaml`, D0006) | none | n/a | Insufficient evidence | n/a | 0 / 0 | No independent tests. The evidence is vendor material, partner marketing, practitioner posts and review aggregates. |
| Julius AI (`julius-ai.yaml`, D0007) | none | n/a | Insufficient evidence | n/a | 2 performance (both limited), 4 other | 2 limited tests: an MDPI paper that ran with code execution disabled, and a single-prompt study. The other 4 are a tutorial, a guide, a student study and a poster, and none tests correctness. Competitor benchmarks were excluded. |
| Open Interpreter (`open-interpreter.yaml`, D0008) | none | n/a | Insufficient evidence | n/a | 0 for the current product, 3 for the earlier Python version | 3 behaviour/security tests (CIBER preprint, RedCode extension, ARPIbench), none peer-reviewed, all on the **earlier** version. IDA-Bench used it only as a harness to compare models. |

The arithmetic for all 4 scored entries was re-checked with 0.30/0.20/0.25/0.25 weights and is correct.

### 1b. How sources were counted in practice
- The **strict reading** was used in every case: only independent sources that test or measure the product count toward the 3. Descriptions, journalism without original testing, court records, CVE listings and review aggregates were reported as "other". D0007 Julius states this explicitly ("follow the stricter reading, as we did for Pactum"). D0007 also records that a methodology clarification was deferred, which is this packet.
- D0008 Open Interpreter also applied a **scope/version reading**: 3 tests of the earlier version were not counted for the current product.
- D0002 GPT Researcher first proposed grade C with a borderline count. It was revised to 3 performance sources and grade B-.

### 1c. How evidence grades were assigned
- `methodology.html` **does not define evidence grades at all**. It defines only the four factors, rounding, the Insufficient-evidence rule and the disclaimer.
- Grades were assigned by comparison with similar entries: ODR (65) got B, Perplexity (54) got B, GPT Researcher (53) got B-, SAFE (66) got B-.
- D0009 says "The grade comes from the methodology table". **No such table exists.** D0008 says the same about a hypothetical grade.
- **Empirically, the grade tracks evidence, not the overall score.** SAFE has the highest overall score (66) but got B-. Perplexity has 54 but got B. The observed pattern:

| Grade | Entries | Independent performance sources | Peer-reviewed among them | Evidence-quality factor |
|---|---|---|---|---|
| B | ODR, Perplexity | 5, 6 | 2, 5 | 75, 75 |
| B- | GPT Researcher, SAFE | 3, 3 | 1 (+1 companion track), 3 | 65, 60 |

So the grade is effectively "how many independent performance tests there are", and it lines up with the evidence-quality factor score. It does not depend on peer review alone, because SAFE has 3 of 3 peer-reviewed and still got B-.

## 2. What the rules currently say (`public/methodology.html`)
- "The overall score is rounded to the nearest whole number. Interim: exact .5 rounds up."
- "If an agent has fewer than 3 independent sources, it is labeled 'Insufficient evidence' and no overall score is given." The page does not define "independent" or "source", or say what kind of source counts.
- Evidence quality factor: "Independent third-party sources rate high; vendor claims low; anonymous anecdotes lowest."
- There is no mention of evidence grades.
- D0001 (plan) defines an independent source as "Evidence from someone with no stake in the product (e.g., researchers, journalists, independent testers)." Journalists are included there, which is looser than what was applied in practice.

---

## 3. Items: risks, recommendation, proposed wording

### Item 1: Make round-half-up permanent
- **Facts:** Two entries land exactly on .5: Perplexity (53.5 → 54) and SAFE (65.5 → 66). SAFE's YAML has no `overall_note` or uncertainty line about it, while Perplexity's does.
- **Risk:** Low. Under round-half-even, both entries would also be unchanged (54 and 66 are even). Only round-half-down would change them, to 53 and 65. A permanent rule removes an open question.
- **Recommendation: APPROVE.** It matches current practice, changes no entry, and is simple to explain.
- **Proposed wording (replaces the Rounding paragraph):**
  > **Rounding.** The overall score is calculated from the unrounded factor weights and then rounded to the nearest whole number. A result of exactly .5 is rounded up (for example, 53.5 is shown as 54). Factor scores are whole numbers and are not rounded further.
- **Per-entry impact:** none. Perplexity stays 54 and SAFE stays 66. Follow-up: drop "interim" from Perplexity's `overall_note`, uncertainty line and page, and add an equivalent note to SAFE for consistency (see Item 4).

### Item 2: What counts as an independent source for the 3-source threshold
- **Facts:** See 1b. The strict reading was applied consistently but was never written down. D0001's definition includes journalists.
- **Risks/uncertainties:**
  - Without a version/scope clause, Open Interpreter's 3 tests of the earlier version would numerically meet the threshold, so the rule needs that clause to match the approved outcome.
  - "Partly independent" (Pactum thesis using customer data) needs a home. The proposal is to count it only if the data or funding relationship is disclosed and the author is not the vendor or customer staff. Either way Pactum stays below 3.
  - Competing-author studies (SAFE, GPT Researcher's TTD-DR, ODR's TTD-DR) are a real conflict, but excluding them would remove SAFE's and GPT Researcher's scores. The proposal is to disclose them, not disqualify them.
  - Several copies of one study (arXiv, venue and ACM records) must count once. GPT Researcher already does this: 6 URLs, 3 studies.
- **Recommendation: APPROVE.** It codifies what was already done and changes no outcome.
- **Proposed wording (replaces the Insufficient evidence section):**
  > **Insufficient evidence.** An overall score is given only when there are at least **3 independent performance sources**. Otherwise the entry is labeled **"Insufficient evidence"** and no overall score is given; factor notes may still be shown.
  >
  > **Performance source:** a source that tests or measures the agent's performance, behaviour or outcomes, such as a benchmark, research study, documented hands-on test, security or safety evaluation, or audit, and reports its method and results. Product descriptions, reviews, user-review aggregates, press coverage without original testing, commentary, court filings and vulnerability listings are recorded as **other sources**. They can inform factor scores but do not count toward the 3.
  >
  > **Independent:** not produced, funded or co-authored by the vendor/maintainer or by a customer's staff, and not published by a competing product to promote itself. Studies by researchers who propose a competing research method may count; this is disclosed on the entry.
  >
  > **Counting:** each study counts once, however many versions or links it has. A source counts only if it tested the product, version and scope covered by the entry. A source whose independence is only partial (for example, relying on data supplied by a customer) is labeled as such.
- **Per-entry check under this rule (outcomes stay the same for all 8):**
  - **OpenAI Deep Research: unchanged.** 5 qualifying studies (≥3), score 65. The Conversation is other. TTD-DR is competing-author and disclosed.
  - **Perplexity: unchanged.** 6 qualifying (CJR counts as a documented test), score 54. The 3 court records are other.
  - **GPT Researcher: unchanged.** 3 qualifying (TTD-DR competing-author, disclosed), score 53. NVD and GHSA are other.
  - **SAFE: unchanged.** 3 qualifying (all competing-author, disclosed), score 66. The 2 journalism sources are other. The NeurIPS paper and repo are by the authors, so they are not independent.
  - **Pactum: unchanged, Insufficient evidence.** At most 1 qualifying (thesis, partly independent). HBR is customer-co-authored and does not count.
  - **Clay: unchanged, Insufficient evidence.** 0 qualifying. The practitioner posts are self-published anecdotes; one grades against Clay's own output.
  - **Julius AI: unchanged, Insufficient evidence.** 2 qualifying, both limited. The competitor benchmarks are excluded and the 4 others do not test.
  - **Open Interpreter: unchanged, Insufficient evidence.** 0 qualifying for the current product. The 3 earlier-version tests are excluded by the version/scope clause.

### Item 3: Evidence grades
- **Facts:** See 1c. The grade is undefined, D0009's reference to a "methodology table" is wrong, and grades were set by comparison.
- **Risks:**
  - An undefined label invites misreading as a quality or trust rating of the agent. The data shows it tracks evidence, so the definition should say so.
  - Peer review alone does not explain the existing grades, because SAFE has 3 of 3 peer-reviewed and got B-. A criterion based mainly on count fits the data.
  - Only B and B- are in use. Higher and lower bands are untested.
- **Recommendation: APPROVE the definition and table below.** It is based on count and type, uses peer review only as a tie-in for A, and adds the evidence-quality factor as a cross-check. Alternatively, choose **MORE INFO** if you would rather drop letter grades and show only the count.
- **Proposed wording (new section after Insufficient evidence):**
  > **Evidence grade.** The evidence grade describes the amount and type of independent evidence behind a score, not how well the agent performs. It is set by this table, using independent performance sources as defined above:
  >
  > | Grade | Independent performance sources |
  > |---|---|
  > | A | 7 or more, at least 3 peer-reviewed, at least 1 testing the current version within the last 12 months |
  > | B | 5–6, or 7+ without meeting the A conditions |
  > | B- | 3–4 |
  > | Insufficient evidence | fewer than 3 (no grade and no overall score) |
  >
  > The evidence-quality factor score should be consistent with the grade (as a guide: A ≥ 85, B 70–84, B- 55–69). If they diverge, the decision packet explains why.
- **Check against the existing 4 grades:** ODR has 5, so B (factor 75 is consistent). Perplexity has 6, so B (75, consistent). GPT Researcher has 3, so B- (65, consistent). SAFE has 3, so B- (60, consistent). **No grade changes.** The 4 Insufficient entries are unaffected.

### Item 4: Other small inconsistencies (proposed fixes; none changes a score or status)
1. **D0009 and D0008 cite a "methodology table" for grades that does not exist.** Fixed by Item 3. Add an erratum note to D0009 rather than rewriting the approved packet.
2. **SAFE's 65.5 rounding is not noted** in its YAML (`overall_note`/uncertainties), unlike Perplexity. Add a matching note. Remove "interim" from both once Item 1 is approved.
3. **The source-count field shape varies:** `performance/other` (most), `performance/security` (GPT Researcher), string values ("2 (both limited)", "1 (partly independent)"), and custom keys (Open Interpreter). The schema has a single integer. Proposed fix: standardize on `performance: <int>`, `other: <int>`, plus an optional `count_note`, and update `_schema.example.yaml`.
4. **Status-line wording differs on the pages:** Clay and Pactum say "fewer than three independent sources", Julius says "independent evaluations", and Open Interpreter gives no reason. Standardize to "fewer than three independent performance sources".
5. **`kind` labels are not controlled.** The schema allows independent / vendor / anonymous, but entries use about 20 free-text kinds (e.g. "maintainer", "journalism", "anecdotal aggregate", "competitor benchmark"). Court records and NVD entries are labeled `kind: independent` even though they are not counted as performance sources. Fix: a short controlled list (independent performance / independent other / vendor or maintainer / customer or partner / competitor / anecdotal), with detail in `note`.
6. **Blocked or unread sources are labeled inconsistently.** 403s are put in `kind` (Clay, Julius) while SAFE's 429 is in `note`. Pactum uses "paywalled; not reviewed" and Julius has "DOI returned 404". Fix: an optional `access_note` field with fixed phrases: "could not be fetched automatically (HTTP 403/429); read via search index" or "not reviewed (paywalled)".
7. **Scoring of disputes is not defined.** In practice the Disputes factor has absorbed lawsuits (Perplexity: pending, allegations), security advisories (GPT Researcher), public critique (SAFE) and fabricated citations (ODR, which arguably belongs to completion or evidence). Proposed wording for the factor table: "Disputes: documented complaints, legal or regulatory actions and security advisories concerning the agent. Pending cases are recorded as allegations, not findings. Errors in the agent's output are scored under Completion rate."
8. **Factor naming varies.** It is "Disputes" / "Evidence quality" on the methodology page, "Evidence" or "Completion / rating accuracy" in some packets, and `score_rationales` vs `factor_notes` in the YAML. Use the four methodology names everywhere, and `factor_notes` for both scored and unscored entries.
9. **Three different disclaimers:** the methodology body ("…verification beyond what is explicitly stated. No payments are handled…"), the footer (shorter), and the YAML/summary ("not a guarantee, endorsement, or certification"). Summaries say "endorsement or certification" and omit "guarantee". Proposal: one standard sentence everywhere, "Informational only; not a guarantee, endorsement, or certification."
10. **`agents/README.md` says "No entries are published yet"**, which is out of date because 8 are published. Update it.
11. **The `decision: APPROVED` field appears only in SAFE.** Either add it to all entries or remove it.
12. **D0001 defines "independent source" to include journalists**, which conflicts with practice. Item 2 supersedes it; add a pointer note.
13. **Dates:** all entries show `last_reviewed` and `accessed` dates of 2026-10-16 and are consistent. The methodology page has no "last updated" date or version history. Proposed: add "Scoring rules v0.1, updated YYYY-MM-DD (Decision 0010)" when Items 1–3 are applied.

---

## 4. Plain-English terms
- **Round half up:** if a score ends in exactly .5, show the next whole number up.
- **Round half even:** the alternative, where an exact .5 goes to the nearest even number. It is mentioned only for comparison.
- **Independent performance source:** a test, study or audit by someone with no stake in the product that actually measures how it performs.
- **Other source:** useful background (news, reviews, court records, vulnerability listings) that does not count toward the 3.
- **Competing-author study:** a study whose authors propose their own alternative method. It counts, but this is disclosed.
- **Peer-reviewed:** checked by outside experts before publication at a journal or conference.
- **Preprint:** a paper posted publicly before, or without, peer review.
- **Evidence grade:** a label for how much independent testing exists, not a rating of the agent itself.
- **CVE / NVD / GHSA:** public catalogues of software security vulnerabilities.

Informational only; not a guarantee, endorsement, or certification.
