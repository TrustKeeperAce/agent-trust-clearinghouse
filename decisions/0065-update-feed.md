# Decision 0065: Agent update feed (current URL)

**Status: APPROVED by Remington, 2026-10-18.** This decision implements the 0064 Part 2 design (D7a JSON Feed + Atom, D8a single source file, D9a backfill, D10a domain-independent ids, D11a citation guidance) for the current URL https://agent-trust-clearinghouse.vercel.app only.
- No domain change (0064 Part 1 is not approved).
- No purchases.
- Not deployed by this decision.

## What changed
- **`data/changelog.yaml`** is the new single source of truth for approved changes.
  - It has 57 rows: the 56 existing changelog rows, plus this one.
  - Each row has a stable id (`YYYY-MM-DD-<packet>`), date, decision packet ids and link, the change text, and per-agent `changes` with `before` and `after` values (overall score, evidence grade, status).
  - Before and after values were copied from `agents/*.yaml` in git history. Each change records its `source_commit`.
  - `before` is null for new entries. Values that could not be recovered would be null, never guessed. None were unrecoverable.
- **`scripts/build_data.py`** now also generates:
  - the changelog table in `public/changelog.html` (identical markup for the 56 existing rows);
  - `public/updates.json` (JSON Feed 1.1);
  - `public/updates.xml` (Atom);
  - `<link rel="alternate">` feed links in the head of index, changelog and the data page.
- **Feed items:**
  - One item per agent change, or one per row when no entry changed: 67 items.
  - Ids are `tag:agent-trust-clearinghouse,2026:update/<row id>[/<agent id>]`. They don't depend on the domain and are never reused.
  - Each item carries type (new_entry / score_change / entry_update / site_change), agent id, before and after, status, decision packets, entry URL, an as_of date and the fixed disclaimer: "Informational only. Scores summarize cited public evidence under published rules; they are not a guarantee, endorsement, certification or ranking of quality."
- **Citation guidance** (name, score, grade, as-of date, link; informational, not a guarantee, endorsement, certification or ranking) was added to llms.txt, the data page and the feed. Feed links were added to llms.txt and the data page.
- **The sitemap is unchanged.** It lists HTML pages; the feeds are linked from page heads and llms.txt instead.
- **`scripts/check_export.py`** (run by check_all.sh and the pre-commit hook) now checks:
  - the changelog page matches the source file;
  - ids are unique and stable against the last committed feed;
  - each agent's latest feed values match agents.json (and, through the existing checks, the entry pages);
  - every referenced agent, entry URL and decision packet exists;
  - both feeds contain the same items;
  - the disclaimer is on every item;
  - updates.json is valid JSON Feed 1.1 and updates.xml is well-formed Atom;
  - the feed links and citation guidance are present and up to date.
- No JavaScript, no cookies, no ratings markup. No score, grade or status changes.

## Plain-English terms
- **Feed:** a file listing recent changes that apps and agents can check automatically.
- **JSON Feed / Atom:** two standard feed formats, one JSON and one XML.
- **Stable id:** an identifier that never changes, so readers don't see duplicates.
- **as_of:** the date the values in an item were current.
