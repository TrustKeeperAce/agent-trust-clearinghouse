# Decision 0095: llms-full.txt size — source lists replaced by a pointer

**Status: APPROVED by Remington, 2026-10-21 (4:12 PM ET, t249u), as recommended:**
- **D1 (a2):** a pointer line replaces each entry's source-address lists in llms-full.txt. One explanatory sentence goes under "## Entries", and the llms.txt description is reworded.
- **D2 (a):** the 200,000 / 250,000-byte limits from 0074 are unchanged.
- **D3 (a):** the 0078 list-length check is replaced by the 0095 pointer check. The optional all-sources-linked check is not added.
- **D4 (a):** one changelog row, 2026-10-21-0095, with its feed item.
- **D5 (a):** the split-by-category trigger is recorded below.
- **D6:** noted only.
- **D7 (a):** wording as drafted.

Commit, push and deploy each need separate approval.

## What happened
- **The warning.** With decision 0094, public/llms-full.txt reached 202,798 bytes. That passed the 0074 warning threshold (200,000 bytes; the error is at 250,000). About 6 more entries of the recent size (about 7,600 bytes each) would have reached the error. The build also asserts the 250,000-byte limit.
- **Where the bytes were.** Source addresses and their list headings took 76,241 bytes (38%). Each line repeated its kind and access date. Each entry page already lists the same sources with titles, findings and access dates. data/agents.json lists every source URL with its kind and access date.
- **Why the limits exist.** Decision 0074 set them for "size / context cost", so the whole file fits comfortably in an AI tool's context window (200 KB is about 50k tokens).
- **Outside guidance** (conventions, not standards):
  - The llms.txt proposal (https://llmstxt.org/) keeps detail "behind the links".
  - Mintlify (https://www.mintlify.com/blog/scaling-llms-txt) moved from a 100,000-character cut-off to a hierarchy of files.
  - Geodocs (https://geodocs.dev/technical/llms-txt-advanced-section-patterns) suggests a single llms-full.txt below about 200 KB and a split between 200 KB and 1 MB.

## What changes
- **public/llms-full.txt** no longer lists source addresses. Each entry with sources has one line instead: "Sources: see the entry page above; the complete list, with kinds and access dates, is in data/agents.json."
- **The "## Entries" introduction** adds: "Source lists are not repeated in this file. Each entry page lists its sources with titles, findings and access dates, separating counted from not counted sources; data/agents.json lists every source URL with its kind and access date."
- **Unchanged in the file:** all other text, including scores, grades, grade notes, the source-count line, last-reviewed dates, scope, summaries, uncertainties and per-entry disclaimers.
- **Size:** 202,798 → 131,354 bytes (−71,444, −35.2%). Headroom is about 15 recent-size entries to the warning and about 27 to the error.
- **public/llms.txt:** the llms-full.txt line now says "(scores, grades, scope, summary, uncertainties, source counts; each entry links to its page for the full source list)".
- **scripts/build_data.py:** the generator change, plus the constants LLMS_FULL_SOURCES_NOTE and LLMS_FULL_SOURCES_LINE.
- **scripts/check_export.py:** the 0078 rule that the "Sources listed but not counted" list length must equal the count is replaced by a 0095 rule:
  - no source lists in any entry block;
  - exactly one pointer line in each entry that has sources;
  - the explanatory note appears once.

  The 0078 count-line check and all 0074 checks are kept.
- **Changelog row and feed item** 2026-10-21-0095.
- **Not changed:** any entry page, score, grade, source record, agents.json, agents.csv, schema.json, sitemap, the other pages, the scoring rules, and the size thresholds.

## Trigger for the next step (D5)
When public/llms-full.txt next passes 180,000 bytes, prepare a decision packet to split it by category, with llms-full.txt as the index and one file per category. Nothing is built for this now.

## Noted, not changed (D6)
Three source URLs in agents.json are not linked on their entry pages:
- mini-swe-agent: https://www.swebench.com/ and https://hal.cs.princeton.edu/ (not-counted leaderboards);
- replit-agent: https://arxiv.org/abs/2605.04637 (SWE-WebDevBench, competitor, listed but not counted).

The wording above therefore says entry pages list "its sources" and calls only agents.json complete. A separate later packet may add the links.

## Supersedes
- **0074 D2(a)** (full source URLs in llms-full.txt), for llms-full.txt only. agents.json keeps every source.
- **The 0078 llms-full list-length rule.** The rest of 0078 is unchanged.
