# Decision packet 0072 — Differentiator note ("How this directory works")

**Status: APPROVED by Remington, 2026-10-18: D1a, D2a, D3a, D4a, D5a, D7a, D8a as recommended. D6 (README) not included. D9 deploy needs separate approval.**

Implementation notes: texts are constants in scripts/build_data.py (HOW_*), inserted by build_how(); the methodology section sits before the factor table, as the first section. D7a is a separate commit (build_index_dates plus an export date check); it corrected Manus, ChatGPT Work and Open Interpreter to 2026-10-18 and Perplexity from 2026-10-16 to 2026-10-17 (pre-existing drift). The D5a 'only' ban applies to promotional use: the approved text's rule wording 'only when' / 'only if' is allowed.
Previews (scratch copies of the live pages): `/workspace/private-drafts/0072/preview-index.html`, `/workspace/private-drafts/0072/preview-methodology.html`. Source text: `0072/texts.py`.
Goal: make the core distinction (counted independent evidence, separate factor scores, open data, no ranking or endorsement) visible on the home page, with a path to detail. No research, rules or score changes.

## 1. What happened (current state, quoted from the repo, 2026-10-18)
- **index.html hero:** "An informational directory of digital-task AI agents with transparent, rule-based scores. Informational only; not a guarantee, endorsement, or certification."
- **index.html "How scores work" aside:** "Four factors, shown separately: completion 30%, disputes 20%, adherence 25%, evidence 25%." / "Fewer than 3 independent performance sources: no overall score." / "Evidence grade describes the evidence, not the agent." Above the table: "Sorted by overall score; not a ranking of quality."
- **index.html gaps:** nothing about what "independent" or "counted" means, and no mention of the open data on the home page body (only the footer link "For agents / data").
- **methodology.html:** defines performance source, independent and counting:
  - "A source counts only if it tested the product, version and scope covered by the entry."
  - "The evidence grade describes the amount and type of independent evidence behind a score, not how well the agent performs."
  - "Order is not a recommendation."
  - "Entries are … not removed, added or re-scored for payment."
  - It has no single summary section. The anchors are rounding, insufficient-evidence, evidence-grade, categories, directory-order, last-reviewed, corrections, privacy, data-license and disclaimer.
- **agents-data.html:**
  - "The files are generated from the same approved entries as the pages and contain the same scores and grades."
  - "They are not guarantees, endorsements, certifications, or rankings of overall quality."
- **citing.html:** "Scores summarize cited public evidence under published rules; they are not a guarantee, endorsement, certification or ranking of quality."
- **README:** "An informational-only public directory … transparent, rule-based scores." (It still describes "Phase 1" and says "No agent entries are published yet". That is stale, and out of scope here; see D6.)
- **Defect found while reading (not fixed; private draft only):** the live index.html still shows **last reviewed 2026-10-17** for Manus, ChatGPT Work and Open Interpreter. Their entry pages and agents.json say 2026-10-18 since 0071, because index rows are not regenerated from the YAML. check_export compares index scores and grades with the data but not dates. See D7.

## 2. What the rules say
- Informational only; no guarantee, endorsement or certification.
- No ranking language. Order is "not a recommendation" / "not a ranking of quality".
- No Review/AggregateRating/Rating markup, no JavaScript, no cookies.
- Banned words (check_export `BANNED_CITE`): best, top, winner(s), "which is better", star(s), ★, #1, certified, verified, endorsed. The data page also says never to call an entry "verified", "certified", "approved" or "trusted".
- No scoring-rule changes; deploy needs separate approval.

## 3. Draft wording
### 3a. Home-page callout (4 sentences, 82 words)
Heading: **How this directory works**

> An overall score is given only when at least three independent performance sources (tests by someone other than the vendor that report their method and results) have tested the product covered by the entry; otherwise the entry is labeled Insufficient evidence. Scored entries show the four factor scores separately next to the overall score, and every entry lists its cited sources. The full data is open under CC BY 4.0. Listing order is not a ranking, and nothing here is an endorsement or certification. [More about how this directory works](/methodology.html#how-it-works).

Placement: a small aside directly above the existing "How scores work" aside in the hero area (see preview-index.html). It keeps the existing aside unchanged and adds no numbers that go stale.

### 3b. Fuller explanation, anchor `#how-it-works`
Heading: **How this directory works**

**Counted independent evidence**

An overall score is given only when there are at least 3 independent performance sources: benchmarks, research studies, documented hands-on tests, security or safety evaluations or audits that report their method and results. Independent means not produced, funded or co-authored by the vendor or maintainer, and not published by a competing product to promote itself. A source counts only if it tested the product, version and scope covered by the entry, and each study counts once. Reviews, commentary, press coverage without original testing and product descriptions are listed as other sources; they can inform factor scores but do not count toward the 3.

**Separate factor scores**

Each scored entry shows four factors, each scored 0–100: completion rate (30%), disputes (20%), adherence to limits (25%) and evidence quality (25%), together with the weighted overall score. The evidence grade (A, B or B-) describes the amount and type of independent evidence behind a score, not how well the agent performs.

**Open data**

The same entries are published as agents.json, agents.csv and schema.json under CC BY 4.0, generated from the same source files as the pages. agents.json lists every cited source with its kind, access date and whether it was counted. Changes are recorded in the changelog and the update feeds, and the decision records are in the public repository.

**No ranking or endorsement**

Scored entries are listed by overall score, but order is not a recommendation or a ranking of quality. Scores are informational, rule-based summaries of public evidence as of each entry's last-reviewed date; they are not a guarantee, endorsement or certification. Entries are not removed, added or re-scored for payment.

Links in 3b: agents.json, agents.csv, schema.json, the changelog, and the GitHub repository.

## 4. Placement options for 3b
| Option | Pros | Cons |
|---|---|---|
| **(a) New first section on methodology.html, `#how-it-works`** | One place; sits next to the rules it summarizes; no new URL, sitemap or llms.txt entry; the existing footer and nav already reach it | Methodology gets a little longer; partly repeats later sections |
| (b) Small dedicated page `/how-it-works.html` | Shareable URL; clean for agents | New page to maintain (sitemap, llms.txt, footer, checks); a third copy of the rules, so drift risk; thin-content risk |
| (c) README/data-page note only | Least change | Not visible to human visitors on the site; does not meet the goal |

**Recommendation: (a).** It meets the goal with the least duplication. Every sentence restates existing methodology rules, so drift is easy to check.

## 5. Link placement
- **Home:** the callout ends with "More about how this directory works", linking to `/methodology.html#how-it-works`.
- **Methodology:** the section itself, placed after the intro and before "Rounding"; the existing Compare line stays.
- **Data page:** one sentence after the intro: "How the counting and scores work: see [How this directory works](/methodology.html#how-it-works)."
- **llms.txt:** optional one-line link under the Methodology bullet (D4).
- **Footer:** no change (it is identical on all pages, and the 0069 check enforces that).

## 6. Fact check of the draft wording (against data and rules, 2026-10-18)
| Claim | Check | Result |
|---|---|---|
| Overall score only with ≥3 independent performance sources; otherwise Insufficient evidence | methodology "Insufficient evidence"; agents.json: all 21 scored entries have ≥3 counted, all 13 others have a null overall score | true |
| Performance source definition and independence | methodology wording, near-verbatim | true (the callout's "by someone other than the vendor" is a simplification; the full text gives the complete definition, including competing products) |
| A source must test the product, version and scope; each study counts once | methodology "Counting" | true |
| Reviews, commentary, press without testing and product descriptions are other sources that inform factor scores but don't count | methodology | true |
| Four factors, 0–100, weights 30/20/25/25, shown separately with an overall score | methodology table; every entry in agents.json has the same 4 score keys | true |
| Grade A/B/B- describes the evidence, not performance | methodology "Evidence grade" | true |
| Every entry lists its cited sources | all 34 entry pages have a Sources section | true |
| agents.json lists every cited source with kind, access date and counted | all sources in agents.json have a `counted` key; the data page field table | true. **Not** claimed for the entry pages: 4 pages (clay, gpt-researcher, julius-ai, pactum) don't label sources as counted/not counted |
| agents.json/csv/schema.json under CC BY 4.0, generated from the same source files | agents-data.html; dataset.license; LICENSE-DATA.md | true |
| Changes in the changelog and feeds; decision records in the public repo | changelog.html, updates.json/xml, decisions/ on GitHub | true |
| Listed by overall score; order is not a recommendation | methodology "Directory order" | true |
| Not removed, added or re-scored for payment | methodology "Corrections" | true |

**Banned-word check** (BANNED_CITE regexes run on all draft text): 0 hits. "ranking" appears only in negations ("not a ranking", "No ranking or endorsement"), matching the approved wording on index, citing and agents-data. "approved" was removed from the draft. No counts, dates, competitor names or comparisons appear.

**Previews:** axe and overflow are clean at 375 and 1280, light and dark (scratch copies using the live stylesheet; the callout reuses existing classes plus a new `how-dir` class with no new CSS).

## 7. Risks and mitigations
- **Sounding promotional or implying others don't do this.** Framed as "How this directory works"; no "unlike", "only", "first" or "unique"; no named competitors. Mitigation: add those words to a callout-specific check (D5).
- **Overclaiming accuracy.** The text says what the rules require, not that scores are correct, and keeps "informational", "not a guarantee" and "rule-based summaries of public evidence".
- **"Independent" read as "verified".** The definition is spelled out, and verified/certified are banned.
- **Drift between the callout, the section and the methodology rules.** Mitigation (D5): generate both texts from constants in build_data.py and check that they appear verbatim on index and methodology. Check that the numbers they state (3, the four weights) equal the rule constants used by check_scores, and that the anchor exists.
- **Stale numbers.** None are used (no entry counts or dates); the hero stats already generate counts.
- **Length and clutter on mobile.** 82 words; previews show no overflow at 375px. Alternative: the 2-sentence short form (D2b).

## 8. Minimum viable version
The home callout (3a) plus the methodology section (3b) at `#how-it-works`, the one data-page link line and a changelog row. The D5 check covers verbatim presence, banned words and the anchor. No new page, no llms.txt change, no footer change.

## 9. Decision items
- **D1 Placement of the fuller text:** a) new methodology section `#how-it-works` (**recommended**); b) dedicated page; c) README/data-page note only.
- **D2 Callout:**
  - a) the 4-sentence text in 3a above the "How scores work" aside (**recommended**).
  - b) Short form: "Overall scores are given only when at least three independent tests of the product exist, and the four factor scores are shown separately. The data is open under CC BY 4.0; order is not a ranking or endorsement. More about how this directory works."
  - c) Merge into the existing aside as an extra bullet.
- **D3 Links:** a) home callout link, plus one data-page sentence, plus methodology section (**recommended**); b) also a footer link (changes every page); c) home link only.
- **D4 llms.txt:** a) add one line "How this directory works: <methodology URL>#how-it-works" (**recommended**; agents read llms.txt); b) no change.
- **D5 Checks:** a) generate both texts from build_data constants, plus check_export rules for verbatim presence, banned words plus "unlike/only/first/unique", numbers equal to the rule constants, and the anchor existing (**recommended**); b) a banned-word scan only.
- **D6 README:** a) separate small fix later to replace the stale "Phase 1 … No agent entries are published yet" text with the callout (**recommended**, separate packet); b) include it in 0072; c) leave it.
- **D7 Index last-reviewed drift (found in passing):** a) separate small fix: regenerate index row dates from the YAML and add a check_export date comparison, then deploy with or before 0072 (**recommended**); b) fold into 0072; c) leave.
- **D8 Changelog row:** a) add one site-change row (**recommended**); b) none.
- **D9 Deploy:** separate approval.

## 10. Plain-English terms
- **Callout:** a short boxed note on a page.
- **Anchor:** a link target inside a page (`#how-it-works`), so a link opens at that section.
- **Independent performance source:** a test of the agent, not by its maker, that says how it tested and what it found.
- **Counted:** a source that meets the rules and counts toward the 3 needed for an overall score.
- **Factor score:** one of the four separate 0–100 scores.
- **Drift:** two copies of the same explanation slowly saying different things.

*Informational only; not a guarantee, endorsement, or certification.*
