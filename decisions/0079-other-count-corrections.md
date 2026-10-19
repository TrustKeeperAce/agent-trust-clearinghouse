# Decision packet 0079 — Correct the typed "other sources" number for five entries

**Status: APPROVED by Remington, 2026-10-19: D1a, D2a, D3a, D4a (Option A, check only) and D4x-a as recommended. D5 (changelog row) and D6 (deploy) not approved: no changelog row added; not deployed.**

Implementation notes (2026-10-19): agents/clay.yaml other 0 → 6; agents/gpt-researcher.yaml other 2 → 7 and `count_note` 'Other: 7 vulnerability records (6 NVD, 1 GitHub Advisory Database).'; agents/julius-ai.yaml 5 → 7; agents/pactum.yaml 4 → 7; agents/skyvern.yaml 3 → 4. No source, kind, note, score or `last_reviewed` changed; Emergence WebVoyager stays `other`. Entry-page status lines updated for GPT Researcher ("7 other (vulnerability records)"), Julius AI ("7 other") and Skyvern ("4 other"). scripts/build_data.py gains `OTHER_KIND_BASE`, `kind_base()` and `derived_other()`; scripts/check_export.py gains the 0079 block (typed vs derived, scored-page "N other" vs derived, unknown kind base fails, scored page without the status text fails). Tamper test on a temporary copy: the five steps in section 5 plus a removed status line were each caught; copy discarded. Rebuild: only data/agents.json, data/agents.csv, llms-full.txt and agents/gpt-researcher.html, agents/julius-ai.html, agents/skyvern.html changed; counted numbers, scores, grades, titles and home counts unchanged; the 0078 check still passes.

Correction to Decision 0078: 0078 stated that entry pages show no "other" number. The 23 scored entry pages do show "N other" in their status line (maintained HTML); the 0079 check now covers that text.

**Outcome in one line (if recommended options are approved):** the typed `independent_source_count.other` changes for Clay 0 → 6, GPT Researcher 2 → 7, Julius AI 5 → 7, Pactum 4 → 7 and Skyvern 3 → 4, so that each number equals the sources actually listed under one written rule. No source is added or removed, no kind label changes, and the counted number, scores, grades, status and titles stay the same. A new check keeps the typed number equal to the number derived from the source list.

## 1. What happened (facts and file refs)
Investigated on 19 Oct 2026, about 03:16–03:22 ET, against commit 635ab62 (live as dpl_CKSgwVWxTRWjoCKaZiZhtbU4xVRs).

- **Where the number lives.** Each entry file declares `independent_source_count.other` by hand (`agents/<id>.yaml`, line 19 or 23).
  - `scripts/build_data.py` copies it into agents.json and agents.csv (`independent_other_sources`).
  - Since 0078, it also appears in llms-full.txt as "other sources (as in agents.json): M".
  - Nothing derives it from the source list, and no check compares the two (Decision 0078, finding 2).
- **Correction to Decision 0078.** 0078 said entry pages show no "other" number. That was incomplete.
  - The 23 scored entry pages show "Independent sources: N performance …, M other" in the status line, for example `public/agents/skyvern.html` "3 performance (1 peer-reviewed), 3 other".
  - These pages are maintained HTML. The text is typed, not generated.
  - The 11 Insufficient-evidence pages show only the performance number.
  - For all 23 scored pages the shown number equals the typed YAML value today. Among the five entries here, the pages for GPT Researcher, Julius AI and Skyvern show it; Clay and Pactum do not.
- **What the published definition says.** methodology.html, "Counted independent evidence" and "Performance source":
  - "Independent means not produced, funded or co-authored by the vendor or maintainer, and not published by a competing product to promote itself."
  - "Reviews, commentary, press coverage without original testing and product descriptions are listed as other sources."
  - "… user-review aggregates … court filings and vulnerability listings are recorded as other sources."
  - agents-data.html describes the field as "Independent performance and other sources as stated in the entry". schema.json gives the type only.
- **The 29 entries that already match.** In 29 of 34 entries the typed number equals the count of listed sources whose kind is `other`, `independent other` or `other (…)`, counting each listed record once. Several of these list more than one vulnerability record, and each record is counted:
  - OpenAI Codex: 6 NVD records.
  - Data Interpreter: 4 NVD records plus a ZDI advisory.
  - Aider, OpenHands and Skyvern: 2 NVD records each.
  - Browser Use: one vulnerability recorded twice (GHSA-x39x-9qw5-ghrf and CVE-2025-47241), counted as 2.
  - Kinds `anecdotal` and `customer or partner` appear only in Clay, Julius AI and Pactum. So the rule for them affects no other entry.

### 1a. Clay (typed 0)
History: set to 0 when the entry was added (commit 6619543, Decision 0006). The original kinds were "secondary", "anecdotal practitioner", "anecdotal aggregate" and "partner marketing". 0006 lists the ZenML page as "Secondary (restates Clay)". Decision 0010 renamed the kinds without recounting.

| # | Source | Kind label | Counted | Class under the definition |
|---|---|---|---|---|
| 1–7 | clay.com blog, Clay University (3 pages), developers.clay.com rate limits, clay.com/dpa, clay.com/privacy | vendor or maintainer | no | not other (vendor) |
| 8 | openai.com/index/clay/ (OpenAI customer story) | customer or partner | no | not other (partner marketing, not independent) |
| 9 | zenml.io LLMOps database summary of Clay's evaluation practices | independent other | no | other (third-party description; no original testing) |
| 10–12 | Three LinkedIn practitioner posts (10-row, 1,000-task and 100-row comparisons) | anecdotal | no | other (reviews or commentary without a reported method) |
| 13 | ai.g2.com Clay/Claygent page (232 reviews) | anecdotal | no | other (user-review aggregate) |
| 14 | trustpilot.com/review/clay.com (about 9 reviews) | anecdotal | no | other (user-review aggregate) |

Why it differs: 0006 treated secondary and anecdotal material as not even "other". The published definition names reviews and user-review aggregates as other sources. **Proposed: 6** (1 independent other + 5 anecdotal). Alternative D1b (anecdotal not counted as other): 1.

### 1b. GPT Researcher (typed 2)
History: Decision 0002 recorded "Security: 2 (NVD, GitHub Advisory DB)", one per database. Decision 0010 turned the `security` key into `other: 2` and added `count_note: 'Other: 2 security databases (NVD, GitHub Advisory Database).'`. The entry page says "3 performance, 2 other (security databases)".

| # | Source | Kind label | Counted | Class |
|---|---|---|---|---|
| 1 | arxiv.org/abs/2505.19253 (DeepResearchGym) | independent performance | yes | counted |
| 2 | cs.cmu.edu … ictir26 camera-ready (DeepResearchGym) | independent performance | no (`counted: false`, duplicate record) | not other |
| 3 | dl.acm.org/doi/10.1145/3805713.3820409 (DeepResearchGym) | independent performance | no (duplicate record) | not other |
| 4 | arxiv.org/abs/2507.05495 (Deep Research Comparator) | independent performance | yes | counted |
| 5 | dl.acm.org/doi/10.1145/3774905.3793116 (Comparator ACM record) | independent performance | no (duplicate record) | not other |
| 6 | arxiv.org/abs/2507.16075 (TTD-DR) | independent performance | yes | counted |
| 7–12 | NVD CVE-2026-5625, -5630, -5631, -5632, -5633, CVE-2026-37006 | independent other | no | other (vulnerability listing), 6 records |
| 13 | github.com/advisories/GHSA-8j86-h8gg-797p (CVE-2025-65720) | independent other | no | other (vulnerability listing) |
| 14–18 | Maintainer PR #1820, SECURITY.md, BENCHMARK.md, docs config page, repository | vendor or maintainer | no | not other |

Why it differs: the number counts databases (2) where every other entry counts listed records. There are 7 distinct CVE IDs here, so per-record and per-vulnerability both give 7. **Proposed: 7.** Also replace the `count_note` and the entry-page text (see section 4).

### 1c. Julius AI (typed 5)
History: Decision 0007 set 4 for four "other independent" items: tutorial, student-learning study, guide, poster. It listed the DA-bench page separately ("Unknown operator; no score"). Decision 0010 relabelled that page `independent other` without recounting. Decision 0076 added Vilakati: 4 → 5.

| # | Source | Kind label | Counted | Class |
|---|---|---|---|---|
| 1–4 | mdpi.com Applied Sciences 16(2):669; doi 10.18061/ojsm.6575; doi 10.1007/s11135-026-02898-5; doi 10.51244/ijrsi.2026.1309000109 | independent performance | yes | counted (4) |
| 5 | link.springer.com Discover Education 2024 (tutorial) | independent other | no | other |
| 6 | openalex.org/W7164553025 (Veredas do Direito 2026) | independent other | no | other |
| 7 | doi 10.1111/test.70019 (Vilakati 2025, illustration) | independent other | no | other |
| 8 | casrai.org guide | independent other | no | other |
| 9 | digitalcommons.usf.edu REU poster | independent other | no | other |
| 10–12 | rows.com, basedash.com, fastero.com comparisons | competitor | no | not other (competitor-run comparison) |
| 13 | dabench.com/tools/julius/ (listing; operator not identified; no score) | independent other | no | other (product listing) |
| 14 | aicustomerresearch.beehiiv.com newsletter test | anecdotal | no | other (review without a reported method) |
| 15–19 | julius.ai docs and policy pages (5) | vendor or maintainer | no | not other |

Why it differs: the DA-bench listing was relabelled but never counted, and the anecdotal newsletter was never counted. **Proposed: 7** (6 independent other + 1 anecdotal). Alternative D1b: 6.

### 1d. Pactum (typed 4)
History: Decision 0005 said "4 other independent sources (3 journalism, 1 law review)": Arkansas Democrat-Gazette, IEEE Spectrum, BBC and Hofstra Law Review. Three listed items were left out of the number: Bloomberg (dek only), the HBP teaching case (abstract only) and the PON blog (secondary summary). Decision 0010 labelled all seven `independent other`.

| # | Source | Kind label | Counted | Class |
|---|---|---|---|---|
| 1 | bth.diva-portal.org thesis (Nordenhög 2026) | independent performance | yes | counted |
| 2 | hbr.org 2022 Walmart case (customer co-written) | customer or partner | no | not other |
| 3 | hbsp.harvard.edu TB0756 teaching case (abstract only) | independent other | no | other (description) |
| 4 | bloomberg.com 2023-04-26 (dek only) | independent other | no | other (press, no original testing) |
| 5 | pon.harvard.edu blog summary of HBR case | independent other | no | other (commentary) |
| 6 | arkansasonline.com 2023-05-04 | independent other | no | other (press) |
| 7 | spectrum.ieee.org/ai-contracts | independent other | no | other (press) |
| 8 | bbc.com/news/business-55738540 | independent other | no | other (press) |
| 9 | hofstralawreview.org 2025 article | independent other | no | other (commentary) |
| 10 | pactum.com | vendor or maintainer | no | not other |

Why it differs: 0005 left out items it had not read in full or that only restated others. The definition has no "read in full" condition, and other entries count such items. For example, Consensus counts an abstract-only paper (O'Rourke 2026) in its 1 other. **Proposed: 7.**

### 1e. Skyvern (typed 3)
History: Decision 0027 lists four "Other source" items: the Emergence WebVoyager paper ("critique only, competing author"), Whose Agent Are You? and the two CVEs. The entry was created with `other: 3` (commit 47f5bbf). The record does not say why. Most likely the competing-author critique was left out, or it is a slip (not confirmed).

| # | Source | Kind label | Counted | Class |
|---|---|---|---|---|
| 1–3 | arxiv 2601.07263; arxiv 2601.08406; doi 10.1145/3832165 (AgentBreaker) | independent performance | yes | counted (3) |
| 4 | arxiv.org/abs/2606.20910 (Whose Agent Are You?) | other | no | other |
| 5 | nvd CVE-2025-49619 | other | no | other (vulnerability listing) |
| 6 | nvd CVE-2026-82447 | other | no | other (vulnerability listing) |
| 7 | arxiv.org/abs/2603.29020 (Emergence WebVoyager; Emergence AI makes the competing Agent-E; does not run Skyvern) | other | no | see D3: other (recommended) or competitor |
| 8 | skyvern.com blog, Skyvern 2.0 WebVoyager | vendor or maintainer | no | not other |
| 9 | webbench.ai (co-built with Skyvern) | excluded (vendor co-built) | no | not other |
| 10 | eval.skyvern.com | vendor or maintainer | no | not other |

**Proposed: 4**, with Emergence kept as `other` (D3a). If Emergence is relabelled `competitor` (D3b), Skyvern stays at 3. The same reasoning then reaches two more entries: Fellou (Brave blog, 5 → 4) and Perplexity Comet (Brave blog, 6 → 5, entry page "6 other" → "5 other").

## 2. What the rules say
- Scoring rules v0.1: only counted independent performance sources affect the grade (fewer than 3 is Insufficient; 3–4 B-; 5–6 B; 7+ A with conditions). "Other" sources never change a grade or score. This packet changes no counted value.
- The published "other" category covers reviews, commentary, press without original testing, product descriptions, user-review aggregates, court filings and vulnerability listings. It excludes vendor or maintainer material, competitor promotion, model-only tests and counted sources.
- **Competitor precedents:**
  - Competitor-run comparisons that promote the publisher's product use `competitor` or `excluded (competitor-run)`: Julius AI's Rows, Basedash and Fastero; Consensus's Elicit evaluation.
  - Competitor-authored critiques and security demonstrations have been kept as `other` with the competing author disclosed: Skyvern's Emergence (0027), Fellou's Brave (0031), Perplexity Comet's Brave (0028).
  - Competitor-authored measured studies have even been counted with a disclosure (0028 D3, 0059 D2a).
- Each study once (methodology) applies to counted sources. For "other", the 29 matching entries count each listed record, including Browser Use's two records of one vulnerability.

## 3. Counting rule (proposed, D1 and D2)
**Rule:** `other` = the number of listed source records that are not counted and whose kind base is `other`, `independent other` or `anecdotal`. Count each record once.
- A kind is either a base, or a base followed by a qualifier in parentheses, for example `other (used as a tool)`.
- These bases are not other: `independent performance` (counted, or `counted: false` duplicate or out-of-scope records), `vendor`, `vendor or maintainer`, `customer or partner`, `competitor`, `excluded`, `not counted`, `historical context`.
- Any other base is an error.

Checked against all 34 entries (simulation on a temporary copy):
- With the recommended corrections, all 34 match.
- Without them, exactly the five entries above fail (8 errors: 5 YAML mismatches and 3 entry-page mismatches).

Grouping alternatives for vulnerability listings (D2):

| Rule | GPT Researcher | Effect on the other 29 |
|---|---|---|
| a) Each listed record (recommended) | 7 | none; all 29 match |
| b) One per database (as 0002) | 2 | OpenAI Codex 9 → 4, Data Interpreter 6 → 3 (NVD and ZDI count as two databases), Aider 4 → 3, OpenHands 6 → 5, Skyvern 4 → 3 (Browser Use stays 3: GitHub Advisory and CVE.org are two databases). 5 more entries change |
| c) One per distinct vulnerability | 7 | Browser Use 3 → 2. Not workable as a rule: GitHub Copilot's single NVD search record covers about 25 CVEs, and Agent S's one record names 3 CVEs. It would need judgment, not a check |

## 4. Impact (recommended options)
**YAML (exact diffs):**
```
agents/clay.yaml            -  other: 0              +  other: 6
agents/gpt-researcher.yaml  -  other: 2              +  other: 7
                            -  count_note: 'Other: 2 security databases (NVD, GitHub Advisory Database).'
                            +  count_note: 'Other: 7 vulnerability records (6 NVD, 1 GitHub Advisory Database).'
agents/julius-ai.yaml       -  other: 5              +  other: 7
agents/pactum.yaml          -  other: 4              +  other: 7
agents/skyvern.yaml         -  other: 3              +  other: 4
```
No source, kind, note, factor note, summary, score or `last_reviewed` changes.

**Maintained entry pages (status line):**
- `public/agents/gpt-researcher.html`: "3 performance, 2 other (security databases)" → "3 performance, 7 other (vulnerability records)".
- `public/agents/julius-ai.html`: "4 performance (2 peer-reviewed), 5 other" → "… 7 other".
- `public/agents/skyvern.html`: "3 performance (1 peer-reviewed), 3 other" → "… 4 other".
- Clay and Pactum pages show no "other" number, so they do not change.

**Public files that change** (simulated rebuild on a temporary copy):

| File | Before sha1 | After sha1 | Change |
|---|---|---|---|
| data/agents.json | 691ee1f4f11e | 7ac5326b5251 | 5 `other` values (size unchanged, 134,707) |
| data/agents.csv | 7f312090caa2 | 46f60e677bae | 5 `independent_other_sources` cells (size unchanged, 13,020) |
| llms-full.txt | ef8c2355aa10 | d73b939bc4b0 | 5 count lines, "other sources (as in agents.json)" (size unchanged, 136,134) |
| agents/gpt-researcher.html | dc409439913e | dbbadddfdb11 | status line (9,379 → 9,382 bytes) |
| agents/julius-ai.html | 441490ea24e3 | 69474af12f4e | status line |
| agents/skyvern.html | dbfdb1a39cde | c262531ef056 | status line |

Unchanged and byte-identical in the simulation: schema.json, index.html, compare pages, citing.html, changelog.html, feeds, sitemap.xml, llms.txt and all other entry pages. The "all sources listed but not counted" numbers stay the same (14, 15, 15, 9, 7).

**Unchanged values:** counted (0, 3, 4, 1, 3), peer-reviewed counts, factor scores, overall scores (GPT Researcher 53, Julius AI 59, Skyvern 44; Clay and Pactum null), grades (B-, B-, B-; Insufficient ×2), status, titles. Home stays 23 scored / 11 insufficient.

**last_reviewed:** recommend no change. No new review or search was done; this is a bookkeeping correction of a derived number. Changing the date would imply a fresh evidence review and would also change the home page, sitemap and citing page.

**Changelog/feed (D5):**
- D5a, one row with 5 `entry_update` changes: 68 rows, 86 items (5 new). Changes changelog.html, updates.json and updates.xml.
- D5c, one `site_change` row: 82 items.
- D5b, no row: LOG only.

**Deploy (D6):** 57-file manifest; upload the 6 changed files (9 if D5a or D5c).

## 5. Proposed check (check_export.py block "0079") and comparison
**Option A — check only (recommended).** Add a kind map and a `derived_other(e)` helper to `scripts/build_data.py`. The check fails when the typed value, or a scored entry page's "N other", differs from the derived number. It also fails on any unknown kind base.
```python
# build_data.py
OTHER_KIND_BASE={
    'independent performance':'performance',   # counted, or counted: false (duplicate record or out of scope)
    'independent other':'other', 'other':'other',
    'anecdotal':'other',                        # reviews, practitioner posts, user-review aggregates
    'vendor':'not other', 'vendor or maintainer':'not other', 'customer or partner':'not other',
    'competitor':'not other', 'excluded':'not other', 'not counted':'not other', 'historical context':'not other',
}
def kind_base(k):
    k=str(k).strip(); m=re.match(r'^(.*?) \((.*)\)$',k)
    return m.group(1) if m else k
def derived_other(e):
    n=0
    for s in e['sources']:
        b=kind_base(s['kind'])
        if b not in OTHER_KIND_BASE: raise ValueError(f"{e['id']}: unknown source kind {s['kind']!r}")
        if OTHER_KIND_BASE[b]=='other' and not s['counted']: n+=1
    return n

# check_export.py
for k,e in y.items():
    try: d=B.derived_other(e)
    except ValueError as ex: E(f'0079 {ex}'); continue
    if e['independent_source_count']['other']!=d: E(f"0079 {k}: typed other {e['independent_source_count']['other']} != derived {d}")
    t=open(os.path.join(P,'agents',k+'.html')).read()
    m=re.search(r'Independent sources: \d+ performance(?: \([^)]*\))?, (\d+) other',t)
    if m and int(m.group(1))!=d: E(f'0079 {k}: entry page shows {m.group(1)} other, derived {d}')
    if not m and e['overall_score'] is not None: E(f'0079 {k}: scored entry page has no "N other" status text')
print('0079: checked, typed other equals derived other for all entries (and entry-page status text)')
```
**Option B — derive and replace.** The build writes `derived_other(e)` into agents.json, agents.csv and llms-full.txt, and the YAML field is ignored or removed.
- For: no drift is possible.
- Against: a kind label becomes the only input to a published number, so a mislabel silently changes the output with no cross-check. Entry-page text is typed, so it still needs the Option A page check. It also removes a field contributors fill in, which changes `_schema.example.yaml`.

**Recommendation: A.** It is the smaller change, keeps the YAML as the reviewed declaration, and turns any future mismatch (new source, relabel, page edit) into a visible failure.

**Tamper test (run in the simulation on a temporary copy; all caught, copy restored to 0 errors):**
1. Julius AI typed other changed to 6 and rebuilt → "typed other 6 != derived 7".
2. Skyvern Emergence relabelled `competitor` without changing the number → "typed other 4 != derived 3" and "entry page shows 4 other, derived 3".
3. Pactum BBC kind changed to an unknown base ("journalism") → "unknown source kind 'journalism'".
4. GPT Researcher page text changed to "2 other" → "entry page shows 2 other, derived 7".
5. A new `other` source added to Clay without updating the number → "typed other 6 != derived 7".

The existing 0078 check still passes, because agents.json, agents.csv and llms-full.txt are regenerated together.

## 6. Risks and uncertainties
- **Anecdotal as other (D1).** It matches the published wording (reviews, user-review aggregates). However, three LinkedIn posts are small practitioner tests, and one is graded against Clay's own output. Counting them raises Clay's visible "other" from 0 to 6, which could read as more evidence than exists. The number carries no weight in the grade, and the entry stays Insufficient evidence.
- **ZenML for Clay.** It summarises a Clay presentation. It is classed as independent other, like Pactum's restating press items. If it is treated as vendor-derived instead, Clay would be 5.
- **DA-bench listing for Julius AI.** The operator is not identified, so its independence is not established. It is kept as other (a product listing), as labelled since 0010.
- **Skyvern's typed 3.** The reason is not recorded in 0027. The proposed 4 follows 0027's own list.
- **Competitor label (D3).** "Published by a competing product to promote itself" needs judgment. The recommended reading keeps critiques and security demonstrations as other with a disclosure, as in three past decisions.
- **Per-record counting (D2).** One vulnerability recorded twice (Browser Use) counts twice. This is accepted for consistency and checkability.
- **The 0078 record** says entry pages show no "other" number. That is corrected here (section 1). The decision record for 0079 should note it.
- **Simulation only.** The sha1 values above come from a temporary copy at 635ab62. They will differ if anything else changes first.

## 7. Decision items
- **D1 Anecdotal sources.**
  - a) Count `anecdotal` as other: reviews, practitioner posts, user-review aggregates (**recommended**; matches the published definition). Clay 6, Julius AI 7.
  - b) Do not count them. Clay 1, Julius AI 6.
- **D2 Counting unit.**
  - a) Each listed record once (**recommended**; all 29 matching entries already do this). GPT Researcher 7.
  - b) One per database. GPT Researcher 2, and 5 more entries change.
  - c) One per distinct vulnerability. Needs judgment, so it cannot be checked.
- **D3 Emergence WebVoyager on Skyvern.**
  - a) Keep `other` with the existing competing-author disclosure (**recommended**; follows 0027, 0028 and 0031). Skyvern 4.
  - b) Relabel `competitor`. Skyvern stays 3, and for consistency Fellou's Brave item (5 → 4) and Perplexity Comet's Brave item (6 → 5, page text too) are relabelled.
- **D4 Corrections and check.**
  - a) Apply the five YAML corrections, the GPT Researcher `count_note`, and the three entry-page status lines; add Option A (check) with the tamper test (**recommended**).
  - b) Same, with Option B (derive and replace).
  - c) Check only, reporting mismatches without failing; no data change.
- **D4x last_reviewed.**
  - a) Unchanged (**recommended**).
  - b) Set to the implementation date for the five entries.
- **D5 Changelog row (separate approval).**
  - a) One row with `entry_update` for the five entries: "Data correction: the 'other sources' number now matches the sources listed for Clay, GPT Researcher, Julius AI, Pactum and Skyvern. No scores or grades changed." 68 rows, 86 items (**recommended**: the change is visible in agents.json/csv and on three entry pages).
  - b) No row (LOG only).
  - c) One `site_change` row (82 items).
- **D6 Deploy (separate approval).** Usual manifest procedure; 6 changed files (9 with D5a or D5c).

## 8. Minimum viable version
- Approve **D1a + D2a + D3a + D4a + D4x-a**: five YAML numbers, one count note, three entry-page status lines and the 0079 check. 6 public files change.
- D5 and D6 are decided separately.

## 9. Plain-English terms
- **Typed number:** a value someone enters by hand in the entry file rather than one the build works out.
- **Derived number:** a value the build works out from the list of sources.
- **Kind label:** the short tag on each source saying what sort of source it is (for example vendor, other, competitor).
- **Listed record:** one line in an entry's source list; one paper or one vulnerability page is one record.
- **Tamper test:** deliberately breaking a value to confirm that the check catches it.

*Informational only; not a guarantee, endorsement, or certification.*
