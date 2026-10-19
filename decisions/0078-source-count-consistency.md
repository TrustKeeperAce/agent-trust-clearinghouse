# Decision packet 0078 — Consistent "other sources" count across outputs

**Status: APPROVED by Remington, 2026-10-19: D1a, D2a, D3a, D4a as recommended. D5 (changelog row) and D6 (deploy) not approved: no changelog row added; not deployed.**

Implementation notes (2026-10-19): scripts/build_data.py gains `source_counts(e)` (counted = sources marked counted; other = the declared `independent_source_count.other`, as in agents.json; listed_uncounted = all listed sources not counted) and `other_text()` (a null `other` would print "not stated" in llms-full.txt, matching null in agents.json and an empty cell in agents.csv; no entry has a null today). `llms_full_text()` uses it for the new count line and the heading "Sources listed but not counted:"; the agents.csv counted/other columns and the compare-page counted figure also read from it, with byte-identical output. scripts/check_export.py gains the 0078 block (json counted/other, csv counted/other, llms-full count line, list length, old label and old heading absent). Tamper test on a temporary copy: changed count digit, deleted list line, changed CSV other, old label, YAML other changed without rebuild — each caught; copy discarded. Rebuild: only public/llms-full.txt changed (133788 → 136134 bytes; sha1 a7de4be6d11e → ef8c2355aa10); 34 count lines and 34 headings; no score, grade, title, schema or data value changed.

Monthly review note (D4a): the declared `other` value does not match the listed other-type sources for clay, gpt-researcher, julius-ai, pactum and skyvern. These are left unchanged and need a later packet with per-entry review.

**Outcome in one line (if recommended options are approved):** only `public/llms-full.txt` changes. Its count line would show the same "other sources" number as `agents.json` and `agents.csv`, plus a separately labelled count of all sources listed but not counted. A new check would keep the outputs in step. No score, grade, title, schema or data value changes.

## 1. What happened (facts and file refs)
Investigated on 19 Oct 2026, about 03:03–03:10 ET, against commit b29715d (live as dpl_AovNKnU1LuYtfQ2PfBAA4nnE6duh).

**Root cause.** The word "other" is computed in two different ways.

- **agents.json and agents.csv** copy a hand-entered number from each entry file, `independent_source_count.other`. Nothing derives it from the source list.
  - JSON: `scripts/build_data.py` line 36 (`'independent_source_count':{'performance':isc.get('performance'),'other':isc.get('other')}`).
  - CSV column `independent_other_sources`: lines 68 and 81–82.
  - Schema: line 62 (integer or null; no description).
- **llms-full.txt** counts every source that is not counted.
  - `scripts/build_data.py` line 487: `o=[s for s in e['sources'] if not s['counted']]`.
  - Line 493 prints this as `other listed sources: {len(o)}`.
  - Line 497 lists the same set under the heading "Other sources:".
  - The set includes vendor and maintainer sources, competitor items, model-only tests, historical context, duplicate records of counted studies (counted: false) and leaderboards, as well as true other sources.
- **The counted number is consistent everywhere.**
  - `counted()` at line 24 is the only definition.
  - It is used for JSON `counted_performance_sources` (line 37), the CSV, the llms-full counted line, and the compare pages (line 271). Entry pages are maintained HTML; their status line shows the counted number.
  - `check_export.py` line 26 also checks it against the declared `performance` value.
- **No check covers "other".** `check_export.py` compares the JSON with the YAML-derived entries (line 24) and the CSV counted column (line 37), but never compares the "other" value with the source list or with llms-full.txt.

**Where a source count appears (all outputs checked):**

| Output | What it shows | Definition |
|---|---|---|
| agents.json `independent_source_count.other` | number | declared in YAML |
| agents.csv `independent_other_sources` | number | same as JSON |
| schema.json | type only (integer or null) | no wording |
| agents-data.html (field table) | "Independent performance and other sources as stated in the entry, and the number of counted performance sources." | declared |
| llms-full.txt | "other listed sources: N"; list headed "Other sources:" | all uncounted |
| llms.txt | no counts ("source counts" mentioned in the agents.json link text only) | — |
| Entry pages | "Independent performance sources: N" only; sources grouped under headings such as "Other sources (not counted)" and "Vendor statements" | no "other" number |
| Compare pages, citing page, feeds, changelog | counted number only, or no counts | — |

**What the methodology says.** methodology.html, "Counted independent evidence" (also in llms-full.txt):
- "Reviews, commentary, press coverage without original testing and product descriptions are listed as other sources; they can inform factor scores but do not count toward the 3."
- The "Performance source" paragraph adds "user-review aggregates … court filings and vulnerability listings are recorded as other sources."
- Neither treats vendor statements as "other". The published meaning is closer to the declared number than to "everything not counted".

**Per-entry comparison (today).** All 34 entries differ: llms-full.txt always shows the larger number.

| Entry | Counted | Other: agents.json / CSV (declared) | llms-full "other listed sources" today | Gap | Uncounted by kind: other-type / vendor / competitor / model-only / historical / uncounted perf. record / other labels |
|---|---|---|---|---|---|
| agent-s | 8 | 5 | 9 | +4 | 5 / 3 / 0 / 0 / 1 / 0 / 0 |
| aide | 13 | 6 | 7 | +1 | 6 / 1 / 0 / 0 / 0 / 0 / 0 |
| aider | 8 | 4 | 5 | +1 | 4 / 0 / 0 / 0 / 0 / 0 / 1 |
| autokaggle | 2 | 2 | 3 | +1 | 2 / 1 / 0 / 0 / 0 / 0 / 0 |
| browser-use | 11 | 3 | 6 | +3 | 3 / 2 / 0 / 0 / 0 / 1 / 0 |
| chatgpt-work | 2 | 3 | 10 | +7 | 3 / 2 / 0 / 0 / 5 / 0 / 0 |
| claude-code | 17 | 7 | 9 | +2 | 7 / 1 / 0 / 0 / 0 / 0 / 1 |
| claude-research | 4 | 2 | 5 | +3 | 2 / 3 / 0 / 0 / 0 / 0 / 0 |
| clay | 0 | 0 | 14 | +14 | 1 / 7 / 0 / 0 / 0 / 0 / 6 |
| consensus | 6 | 1 | 5 | +4 | 1 / 3 / 1 / 0 / 0 / 0 / 0 |
| data-interpreter | 9 | 6 | 9 | +3 | 6 / 1 / 0 / 0 / 0 / 0 / 2 |
| devin | 12 | 7 | 8 | +1 | 7 / 1 / 0 / 0 / 0 / 0 / 0 |
| elicit | 10 | 2 | 4 | +2 | 2 / 2 / 0 / 0 / 0 / 0 / 0 |
| fellou | 0 | 5 | 9 | +4 | 5 / 4 / 0 / 0 / 0 / 0 / 0 |
| gemini-deep-research | 8 | 2 | 4 | +2 | 2 / 2 / 0 / 0 / 0 / 0 / 0 |
| github-copilot-coding-agent | 12 | 6 | 9 | +3 | 6 / 3 / 0 / 0 / 0 / 0 / 0 |
| google-deepmind-safe | 4 | 2 | 4 | +2 | 2 / 2 / 0 / 0 / 0 / 0 / 0 |
| gpt-researcher | 3 | 2 | 15 | +13 | 7 / 5 / 0 / 0 / 0 / 3 / 0 |
| julius-ai | 4 | 5 | 15 | +10 | 6 / 5 / 3 / 0 / 0 / 0 / 1 |
| kimi-researcher | 2 | 2 | 5 | +3 | 2 / 3 / 0 / 0 / 0 / 0 / 0 |
| loki | 2 | 3 | 5 | +2 | 3 / 2 / 0 / 0 / 0 / 0 / 0 |
| manus | 0 | 4 | 13 | +9 | 4 / 3 / 0 / 0 / 6 / 0 / 0 |
| open-interpreter | 0 | 8 | 15 | +7 | 8 / 3 / 0 / 0 / 0 / 4 / 0 |
| openai-codex | 26 | 9 | 11 | +2 | 9 / 2 / 0 / 0 / 0 / 0 / 0 |
| openai-deep-research | 5 | 2 | 8 | +6 | 2 / 4 / 0 / 0 / 0 / 2 / 0 |
| openfactcheck | 0 | 2 | 5 | +3 | 2 / 3 / 0 / 0 / 0 / 0 / 0 |
| openhands | 12 | 6 | 9 | +3 | 6 / 1 / 0 / 0 / 0 / 0 / 2 |
| pactum | 1 | 4 | 9 | +5 | 7 / 1 / 0 / 0 / 0 / 0 / 1 |
| perplexity | 6 | 3 | 5 | +2 | 3 / 2 / 0 / 0 / 0 / 0 / 0 |
| perplexity-comet | 4 | 6 | 10 | +4 | 6 / 4 / 0 / 0 / 0 / 0 / 0 |
| skyvern | 3 | 3 | 7 | +4 | 4 / 3 / 0 / 0 / 0 / 0 / 0 |
| storm | 7 | 2 | 5 | +3 | 2 / 2 / 0 / 0 / 0 / 0 / 1 |
| swe-agent | 10 | 6 | 9 | +3 | 6 / 1 / 0 / 0 / 0 / 0 / 2 |
| ui-tars-desktop | 1 | 4 | 10 | +6 | 4 / 2 / 0 / 4 / 0 / 0 / 0 |

Key for the last column: "other-type" means the kind starts with "other" or "independent other". "Uncounted perf. record" means kind "independent performance" with `counted: false` (a duplicate record of a counted study, or an out-of-scope test). "Other labels" covers anecdotal, customer or partner, leaderboard and excluded or affiliated items.

**Second finding: the declared number does not always match the source list.** In 29 of 34 entries, the declared "other" equals the number of sources whose kind starts with "other" or "independent other". It differs in 5:

| Entry | Declared other | Other-type kinds listed | Likely reason (not confirmed) |
|---|---|---|---|
| clay | 0 | 1 | ZenML summary of Clay's own practices (secondary, vendor-derived) |
| gpt-researcher | 2 | 7 | 7 CVE/advisory records, probably declared as 2 groups |
| julius-ai | 5 | 6 | 0076 recorded 4 → 5; one listed item is not in the declared count |
| pactum | 4 | 7 | 7 journalism, commentary and teaching-case items |
| skyvern | 3 | 4 | Emergence WebVoyager is labelled kind "other" but is a competitor (0076 calls it competitor) |

These numbers reflect earlier per-entry judgements and are published in agents.json/csv. Changing them would be a data change for 5 entries, so this packet only flags them (D4).

## 2. What the rules say
- Scoring rules v0.1 use only the **counted** number, which must be 3 or more for a score. The "other" number plays no part in scores or grades.
- Published definition: other sources are reviews, commentary, press without original testing, product descriptions, user-review aggregates, court filings and vulnerability listings. Vendor statements, competitor benchmarks and model-only tests are listed separately on entry pages.
- The data page describes `independent_source_count` as numbers "as stated in the entry". The schema fixes the field shape (`performance`, `other`: integer or null).
- llms.txt and the data page (from 0074) say llms-full.txt is "generated from the same data as agents.json". Today the two report different numbers under the same word.

## 3. Options compared
| | (a) llms-full adopts the agents.json number | (b) agents.json adopts the broader count | (c) Keep both numbers, label them differently |
|---|---|---|---|
| Change | llms-full line shows the declared "other" | `independent_source_count.other` = all uncounted, for all 34 entries | Two clearly named numbers |
| Files | llms-full.txt | agents.json, agents.csv, schema/data-page wording, 34 YAMLs or a new derived field | llms-full.txt (and optionally the data page) |
| Schema or definition | unchanged | changes meaning of a published field; CSV values change for 34 rows; downstream users affected | unchanged |
| Matches methodology | yes | no (would count vendor statements as "other") | yes |
| Problem left over | the llms-full list under "Other sources:" would still be longer than the number | — | none |

**Recommended: (a) + (c) together, applied to llms-full.txt only.**
- Line 493 becomes:
  `- Counted independent performance sources: 2; other sources (as in agents.json): 2; all sources listed but not counted: 3`
- Line 497's heading "Other sources:" becomes "Sources listed but not counted:". The heading then matches what the list holds (vendor, model-only, duplicate records and so on).
- agents.json, agents.csv, schema.json, entry pages and the data page are unchanged.
- This is the smallest change that makes every output that uses the word "other" give the same number, and it leaves the published schema and definitions as they are.

## 4. Impact (recommended option)
- **Public files changed: 1.** `public/llms-full.txt`: 34 count lines and up to 34 list headings (every entry has at least one uncounted source). The size grows by about 34 × 45 bytes, roughly 1.5 KB, which stays well under the 250,000-byte limit (now 133,788).
- **Repo-only:**
  - `scripts/build_data.py`: a shared `source_counts(e)` function, used by `llms_full_text()`.
  - `scripts/check_export.py`: the 0078 block.
  - `decisions/0078-…md`, `LOG.md`.
- **Unchanged:** agents.json, agents.csv, schema.json, llms.txt, all HTML pages, sitemap, feeds (unless D5a adds a row).
- **Scores, grades, titles, entry order, last-reviewed dates:** none change. The build copies values; nothing in the change touches scoring.
- **Per-entry after values:** the "other sources (as in agents.json)" number equals column 3 of the table above. The "all sources listed but not counted" number equals today's llms-full number (column 4). No value is lost; the old number is kept under a clearer name.
- If D5a is approved, the changelog gets one site_change row: 68 rows and 82 feed items.

## 5. Proposed check (check_export.py block "0078")
```python
# 0078: one definition of source counts for every output
def source_counts(e):            # in build_data.py; imported here as B.source_counts
    return {'counted': sum(1 for s in e['sources'] if s['counted']),
            'other': e['independent_source_count']['other'],
            'listed_uncounted': sum(1 for s in e['sources'] if not s['counted'])}

LF = open(os.path.join(P, 'llms-full.txt')).read()
if 'other listed sources' in LF: E('0078: old llms-full label present')
csvrow = {r['id']: r for r in rows}
for k, e in y.items():
    sc = B.source_counts(e)
    if sc['counted'] != x[k]['counted_performance_sources']: E(f'0078 {k}: json counted')
    if sc['other'] != x[k]['independent_source_count']['other']: E(f'0078 {k}: json other')
    if csvrow[k]['counted_performance_sources'] != str(sc['counted']): E(f'0078 {k}: csv counted')
    if csvrow[k]['independent_other_sources'] != ('' if sc['other'] is None else str(sc['other'])): E(f'0078 {k}: csv other')
    m = re.search(r'^### ' + re.escape(e['name']) + r'\n(.*?)(?=^### |^## Changes)', LF, re.S | re.M)
    if not m: E(f'0078 {k}: llms-full section missing'); continue
    blk = m.group(1)
    want = (f"- Counted independent performance sources: {sc['counted']}; other sources (as in agents.json): "
            f"{sc['other']}; all sources listed but not counted: {sc['listed_uncounted']}")
    if want not in blk: E(f'0078 {k}: llms-full count line')
    lst = re.search(r'^Sources listed but not counted:\n((?:- .*\n)+)', blk, re.M)
    n = len(lst.group(1).splitlines()) if lst else 0
    if n != sc['listed_uncounted']: E(f'0078 {k}: llms-full list length')
print('0078: checked')
```
- **Optional report line (D4b):** print, without failing the check, the entries where the declared "other" differs from the number of other-type kinds (today: clay, gpt-researcher, julius-ai, pactum, skyvern).
- **Tamper test** (on a temporary copy; restore with `git checkout -- public`). Each step must make `check_export.py` exit 1 with a 0078 error:
  1. Change one llms-full count digit, e.g. AutoKaggle "other sources (as in agents.json): 2" → 3.
  2. Delete one line under "Sources listed but not counted:" for Loki.
  3. Change `independent_other_sources` for one CSV row.
  4. Re-insert the old phrase "other listed sources".
  5. Change `independent_source_count.other` in one YAML without rebuilding. This is caught by the existing JSON-vs-YAML check and by 0078.
- After restoring, `check_all.sh` must pass with 0 errors.

## 6. Risks and uncertainties
- **The declared "other" is still hand-entered.** The 5 drift cases show it can fall out of step with the source list. This packet makes the outputs agree with each other, not with the list. D4 covers the follow-up.
- **Two numbers may confuse readers** at first. The labels say which is which, and the larger one names exactly what the list below it holds.
- **Kind labels vary** (about 40 distinct strings, e.g. "other", "independent other", "vendor (not counted)"). The new check does not depend on kind text, only on `counted` and the declared value.
- **Consumers of llms-full.txt** who parse "other listed sources" would need the new phrase. The file is plain text for language models, and no published parser contract exists.
- **Not checked:** external sites that may have copied llms-full numbers. The file has been live since 18 Oct (0074).

## 7. Decision items
- **D1 Fix approach.**
  - a) llms-full.txt shows the agents.json "other" number plus a separately labelled "all sources listed but not counted" number, and the list heading becomes "Sources listed but not counted:" (**recommended**: smallest change; no schema, data or definition change).
  - b) llms-full.txt shows only the agents.json number and keeps the heading "Other sources:" (smaller, but the list length would no longer match any number shown).
  - c) agents.json/csv adopt the broader count (changes a published field for 34 entries and conflicts with the methodology definition; not recommended).
  - d) No change.
- **D2 Shared function and check.**
  - a) Add `source_counts(e)` to build_data.py, use it in `llms_full_text()`, and add the 0078 check_export block with the tamper test above (**recommended**).
  - b) Check only, without the shared function.
- **D3 Data-page wording.**
  - a) No change; "as stated in the entry" stays (**recommended**; definition stable).
  - b) Add one sentence to agents-data.html: "`other` counts independent non-performance sources such as reviews, commentary and vulnerability listings; vendor, competitor and model-only items are listed in `sources` but not included." This changes agents-data.html and its sha1.
- **D4 Declared-vs-listed drift (clay, gpt-researcher, julius-ai, pactum, skyvern).**
  - a) No data change now. Note it for the monthly review and handle it in a later packet with per-entry review (**recommended**).
  - b) Same as a), plus a non-failing report line in check_export listing the drifted entries.
  - c) Correct the 5 declared values now. This changes agents.json/csv for 5 entries and needs entry_update changelog rows and per-entry judgement. Not recommended inside this packet.
- **D5 Changelog row (separate approval).**
  - a) Add one site_change row: "llms-full.txt now shows the same 'other sources' number as agents.json, plus a separately labelled count of all sources listed but not counted; no scores or grades changed." That makes 68 rows and 82 feed items (**recommended**: a public file changes in a way readers may notice).
  - b) No row (LOG only), as for the README-only change in 0073.
- **D6 Deploy (separate approval).** Deploying the changed llms-full.txt (plus changelog.html and the feeds if D5a) needs its own approval after implementation, using the usual manifest procedure.

## 8. Minimum viable version
- Approve **D1a + D2a + D3a + D4a**: build_data.py and check_export.py changes, regenerated llms-full.txt, with nothing else public changing.
- D5 and D6 are decided separately. With D5b and no deploy, the MVP is repo-only until the next deploy.

## 9. Plain-English terms
- **Counted source:** an independent test of the product, in scope, that counts toward the 3 needed for a score.
- **Other source:** a review, commentary, press report, product description or vulnerability listing. It is listed and can inform notes, but it does not count toward the 3.
- **Declared count:** a number typed into the entry file by a reviewer, as opposed to one the build works out from the source list.
- **Sources listed but not counted:** every source on the entry that is not counted. This includes other sources, vendor statements, competitor items, model-only tests and duplicate records of studies already counted.
- **Drift:** two numbers that should match but have fallen out of step.
- **Tamper test:** deliberately breaking an output to confirm that the check catches it.
- **Site change row:** a changelog and feed item for a change to the site that does not alter any entry's score or grade.

*Informational only; not a guarantee, endorsement, or certification.*
