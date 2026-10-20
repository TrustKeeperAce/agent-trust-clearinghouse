# Decision packet 0090: Loose ends and polish (review only)

**Status: APPROVED by Remington, 2026-10-20 (6:53 PM ET), as recommended: D1(a), D2, D3(a), D4, D5, D6 (keep all 22 banners), D8 (no link changes), D9 (one polish changelog row 2026-10-20-0090). D7 REJECTED (keep the best/top/leader wording). D10 commit AND push APPROVED by Remington, 2026-10-20 (7:06 PM ET), with optional wording fixes O1 (changelog row: 'notes that Replit Agent builds and deploys apps in its own hosted platform') and O2 (coding-agents caveat 2: 'several of its counted tests compare app builders') applied first. Deploy NOT approved: nothing is deployed.** Review prepared 2026-10-20, 6:24–6:50 PM ET, against master ff5c865 (live as dpl_GPN1bKhGWAuB3pSzPKMaCsLrARcq); the approved set was dry-run on a scratch clone only.

**Outcome in one line:** six small text and consistency fixes plus one changelog row. **No score, grade, source count, last-reviewed date or scoring rule changes.** data/agents.json, agents.csv, index.html and sitemap.xml come out byte-identical. All 22 recheck banners stay.

## What happened
- **Reviewed:** all 40 entry pages, the three comparison pages, index, methodology, citing, agents-data, llms.txt and llms-full.txt, sitemap, feeds, README and CITATION.cff, scripts/build_data.py, and the agents/*.yaml files.
- **Pending items:** follow-ups in the private working notes for 0083, 0087, 0088 and 0089 and in decision records 0052 and 0056–0080.
- **Scripted scans:**
  - counts written in the text compared with the data;
  - page Category and Type lines compared with agents.json;
  - "Data as of" dates;
  - old vercel.app URLs;
  - meta and og descriptions;
  - JSON-LD types, checked for ratings markup;
  - a banned-word scan of all public text;
  - the full link check (scripts/check_links.py), run on the live repo and on the scratch copy.
- **Citation services for the banners**, checked 6:29–6:36 PM ET:
  - Semantic Scholar refused 5 of 6 tries (HTTP 429); one lookup succeeded at 6:35 PM.
  - The arXiv API did not respond on any of the 6 tries.
  - OpenAlex responded normally.
- **Dry run:** a scratch clone of ff5c865 with the proposed changes applied and the site rebuilt; patch and check outputs were kept as private working notes.

## What the rules say
- Informational only. No guarantee, endorsement, certification, ranking or ratings markup, and no new pages. The banned-word lists from 0066, 0067 and 0072 apply.
- PROCESS.md citation gate: Semantic Scholar citations plus a keyword search, with OpenAlex as the fallback. 0052 B3: "Remove each note when its follow-up packet is closed."
- Changes to entry pages are recorded in the changelog. Precedent 0069 (small consistency fixes) used one row with `changes: []`, and it did not change last_reviewed or decision_packet.
- Precedent 0074: "best" and "top" used to describe study results in entry text are allowed ("no rewording proposed").
- PROCESS.md link rule: never change the link for a counted source without a decision.

## Findings
1. **Coding-agents comparison caveat is out of date.**
   - The "managed products" list leaves out Replit Agent, which is the 11th coding agent and was added in 0089.
   - The second caveat ("cloud agents … and others are command-line tools") does not fit Replit Agent, a hosted app builder, or editor agents such as Cursor and Cline.
   - Nothing checks that this list stays complete.
2. **Aider summary count is stale.** It says "Eight independent studies … (five peer-reviewed)", but the data, grade note and factor note say 6 of 8. 0051 marked Sifting the Noise as peer-reviewed and left the summary unchanged.
3. **Two "Data as of" dates are stale.** agents-data.html says 2026-10-18 and llms.txt says 2026-10-19; the data is dated 2026-10-20. Both dates are typed by hand. The comparison pages, citing page and llms-full.txt get their dates from the data, and those are correct.
4. **Kimi Researcher banner has no reason line.** 0076 replaced the reason line with "Rechecked in Decision 0076 … no new independent test", but the banner stayed, and 0076 says the Semantic Scholar gate was not rerun. The page now looks contradictory.
5. **Type lines differ between page and data.**
   - The Google DeepMind SAFE page shows "research code". The data says "research code (Apache-2.0 code; CC-BY other materials; bundled FActScore code MIT)".
   - The Manus page shows "commercial". The data says "commercial (free tier with credits; paid plans)".
   - The other 38 entries match.
6. **Recheck banners:** 22 found and none can be cleared now (see the table).
7. **Checked and clean, no change needed:**
   - Homepage totals (29 scored / 11 insufficient) are generated and correct.
   - All 40 llms.txt lines match the data, and sitemap lastmod dates match last_reviewed.
   - No old vercel.app URL appears outside historical decision, changelog and feed text.
   - No meta description is longer than 160 characters, and og descriptions match.
   - JSON-LD uses only ItemList, BreadcrumbList, Dataset, WebSite, WebPage and Organization; there is no ratings markup.
   - Other counts written in the text match the data.
8. **Noted, no change proposed:**
   - Date formats are mixed ("17 October 2026", "19 Oct 2026", "2026-10-17") in approved entry text.
   - Type labels are written several ways ("open source", "open-source", "Open-source").
   - Four summaries use "best", "top" or "leader(s)" to describe study results (Aider, Perplexity Comet, SWE-agent, Gemini Deep Research). This is allowed under 0074 (see D7).
9. **Link check** (731 outbound links, 6:31 PM ET): 638 OK, 87 bot-blocks, 6 failures. None is a confirmed dead link:
   - Two DOIs (Consensus 10.5206/cjils-rcsib.v49i1.23075; Cline 10.52202/085713-5769) are registered and resolve in the DOI handle API, but the publisher sites timed out from the box.
   - Two Fellou blog posts returned 503, a server error.
   - A Wayback Machine copy (OpenAI Deep Research) timed out.
   - **os-world.github.io** (an other source on Agent S) now redirects to http://osworld-v1.xlang.ai/, which timed out. The site appears to have moved.
   - The scratch copy shows the same 6 failures. Its one new outbound link, the 0090 decision record on GitHub, was rate-limited (429) and will exist only after a push.

### Recheck banners: 22 found, 0 can be cleared now
All 22 show "Citation check incomplete — recheck later." Claude Code's banner adds "about 13 candidate studies not yet screened". The test for clearing: the follow-up packet is closed (0052 B3) and the Semantic Scholar check has been done or the OpenAlex fallback has been completed. Today Semantic Scholar refused 5 of 6 tries and the arXiv API did not respond, so neither condition can be met in this review. Removing a banner would not change any score by itself. **Finishing the screening could change counted sets** for entries that list unscreened candidates; those entries are marked ⚠ in the table.

| Entry | What the banner is waiting for (from the entry's reason line) | Verdict |
|---|---|---|
| AIDE ⚠ | 6 named candidates not screened (BioML-bench, OPT-BENCH, MLE memory paper, MLAlgo-Bench, Tree-Notebook, RE-Bench) | Stays; needs an evidence pass |
| Aider ⚠ | 5 named candidates not screened (AAAI 2026, two ESEM 2026, TOSEM, CSIT 2026) | Stays; needs an evidence pass |
| ChatGPT Work | 0052: Semantic Scholar unavailable; OpenAlex title screen only | Stays |
| Claude Code ⚠ | About 13 candidate studies not screened | Stays; needs an evidence pass |
| Claude Research | 0052 (as ChatGPT Work) | Stays |
| Clay | 0080: OpenAlex full text done; Semantic Scholar unavailable | Stays |
| Cline | OpenAlex: 790 matched, 295 downloaded; Semantic Scholar rate-limited | Stays |
| Cursor agent ⚠ | Semantic Scholar and arXiv unavailable; several MSR 2026 papers not screened | Stays; needs an evidence pass |
| Devin | Semantic Scholar rate-limited; OpenAlex used | Stays |
| FacTool | 29 citing works not downloaded; Semantic Scholar rate-limited | Stays |
| Gemini Deep Research | 0057: Eye paper paywalled until 2027; AMCIS paper read as abstract only; Semantic Scholar unavailable | Stays (Eye not readable before 1 Jan 2027) |
| GitHub Copilot coding agent | Semantic Scholar rate-limited; OpenAlex used | Stays |
| Google DeepMind SAFE | 0058: Semantic Scholar unavailable for SAFE | Stays |
| Kimi Researcher | No reason line on the page (0076 did not rerun Semantic Scholar) | Stays; reason line added in D4 |
| Magentic-One | OpenAlex: 284 matched, 244 downloaded; Semantic Scholar and arXiv unavailable | Stays |
| mini-SWE-agent | OpenAlex: 458 matched, 419 downloaded; Semantic Scholar and arXiv unavailable | Stays |
| OpenAI Codex ⚠ | Figures not taken from 6 papers; batch citation search not fully screened | Stays; needs an evidence pass |
| OpenAI Deep Research | 0057: Eye paper paywalled until 2027; Semantic Scholar unavailable | Stays (Eye after 1 Jan 2027) |
| Perplexity Comet | 0052 | Stays |
| Perplexity | 0056: Semantic Scholar unavailable | Stays |
| Replit Agent | OpenAlex: 357 screened, 171 downloaded; arXiv unavailable; Semantic Scholar not used | Stays (added today in 0089) |
| STORM | 0052 | Stays |

## Decisions (D-items; approved 2026-10-20, 6:53 PM ET, except D7 rejected and D10 not approved)
- **D1 Coding-agents caveats** — **APPROVED: (a)** (scripts/build_data.py; compare/coding-agents.html is regenerated).
  - (a) Add "Replit Agent" to the managed-products list, and replace the second caveat with: "Some entries are cloud agents that open pull requests, some are command-line or editor tools, and Replit Agent builds and deploys whole apps inside Replit's hosted platform, so several of its counted tests compare app builders; read each scope before comparing." (Three of Replit Agent's five counted tests compare app builders.) Also add a check_export rule that fails the build if any Coding agent entry is missing from the first caveat. **Recommended.**
  - (b) Add "Replit Agent" to the list only, with no new second-caveat wording and no check. This is the 0087 D10a pattern.
  - Risk: low. "Tested as shipped" is approved wording, although Cursor and Replit let the user pick a model.
- **D2 Aider summary** — **APPROVED:** change "(five peer-reviewed)" to "(six peer-reviewed)" in agents/aider.yaml and the page; llms-full.txt is regenerated. This corrects text to match existing data; no count changes. **Recommended.**
- **D3 "Data as of" dates** — **APPROVED: (a)**
  - (a) build_data.py fills in the date on agents-data.html and llms.txt from the data (the 0072 D7a pattern), and check_export fails if either date is stale. Both become 2026-10-20. **Recommended.**
  - (b) A one-time hand edit of the two dates, with no generator or check. The dates would go stale again after the next entry.
- **D4 Kimi Researcher** — **APPROVED:** add one sentence to the "Rechecked in Decision 0076" line: "The Semantic Scholar citation check was not rerun, so the citation check is still incomplete." The banner stays. **Recommended.**
  - Alternative: remove the banner instead. **Not recommended**, because the gate was not rerun.
- **D5 Type lines** — **APPROVED:** make the SAFE and Manus page Type lines match the data exactly. **Recommended.**
  - Alternative: no change.
- **D6 Banners** — **APPROVED (all 22 kept):** keep all 22, and clear none in this packet. **Recommended.**
  - The first clearing step belongs in its own evidence pass when Semantic Scholar and arXiv respond.
  - The ⚠ entries need screening, which could change counts.
- **D7 "best", "top" and "leader" in four summaries** — **REJECTED (no change; 0074 wording kept):**
  - (a) No change, following 0074. **Recommended**, to keep this packet small.
  - (b) Reword to neutral terms such as "highest … of three agents" on Aider, Perplexity Comet, SWE-agent and Gemini Deep Research. This would change 4 more entry pages. Remington's call.
- **D8 Links** — **APPROVED (no link changes):** no link changes now; recheck the 6 failures at the monthly link check. **Recommended.**
  - os-world.github.io is an other (uncounted) source on Agent S. Replacing it would change a source record, so it would go in an entry update.
- **D9 Changelog** — **APPROVED (row 2026-10-20-0090):** one "polish" row, 2026-10-20-0090, with `changes: []`, following 0069. There is no last_reviewed or decision_packet change, and it adds one site-level feed item (88 → 89 items, 74 → 75 changelog rows). **Recommended.**
  - Alternative: entry_update feed items for Aider, Kimi Researcher, SAFE and Manus.
  - Drafted row: "Wording and consistency fixes: the coding agents comparison now names Replit Agent among the managed products and notes that Replit Agent builds and deploys apps in its own hosted platform; the Aider summary now says six of its eight counted studies are peer-reviewed, matching the data; the as-of dates on the For agents / data page and llms.txt are now generated from the data; the Kimi Researcher page now says why its citation check is still incomplete; the Type line on the Google DeepMind SAFE and Manus pages now matches the data. No score, grade or source count changes."
- **D10 Publishing** — **commit and push APPROVED 2026-10-20 (7:06 PM ET), with O1 and O2; deploy NOT approved:** implementing, committing, pushing and deploying each need separate approval. This packet would also be added as decisions/0090-polish.md, with a LOG.md line.

### Out of scope: needs its own packet
These items add sources or could change counts, so they are not in this packet:
- **0089 D13 (a):** Tenzai "Bad Vibes" tested Cursor, Claude Code, Codex and Devin.
  - Under 0089 D2a it is a performance test (partial independence), so consistency points to counting it on those pages.
  - Adding it as "other" would still change each page's other count.
- **0089 D13 (b):** the Utah Valley study also rated Cursor and Claude Code.
- **0089 D13 (c):** the managed-products caveat edit, which is now covered by D1. Its "(d)" item proposed no score change.
- **0088 D13 (a)–(c):** Magentic-One studies C1 and C2 on the Data Interpreter page, C5 on the Codex page, and the Magentic-UI reserve sources.
- **0087 D10b:** Cline studies C1, C3, C4 and C6 include Claude Code, Cursor and Codex results.
- **0083 follow-ups:** SWE-Bench Mobile (Codex CLI and Claude Code), and the MSR task-level and CI-footprints papers (Copilot, Devin, Codex).
- **Clearing banners:** an evidence pass per entry, starting with the ⚠ entries.
- **Policy question:** does a completed OpenAlex fallback (PROCESS.md) alone allow a banner to be cleared? Recent entries kept the banner anyway (0087–0089 D10).
- **Eye paper recheck** (OpenAI and Gemini Deep Research): after 1 Jan 2027.

## Final private draft (scratch clone of ff5c865 with the approved D1(a), D2, D3(a), D4, D5 and D9 applied)
Patch, check outputs and manifest preview were kept as private working notes. Earlier dry-run results below.

### Dry-run results
- **Files changed (16 + 1 new):**
  - agents/aider.yaml, agents/kimi-researcher.yaml, data/changelog.yaml
  - public/agents/aider.html, kimi-researcher.html, google-deepmind-safe.html, manus.html
  - public/agents-data.html, changelog.html, compare/coding-agents.html, llms.txt, llms-full.txt, updates.json, updates.xml
  - scripts/build_data.py, scripts/check_export.py
  - new: decisions/0090-polish.md
- **check_all:** 0 errors (75 changelog rows, 89 feed items; titles max 68; no-JS ok).
- **check_scores:** 0 errors, 0 warnings, 6 documented.
- **Score diff:** 0 differences across scores, overall, grade, counted, peer-reviewed, source counts, status, last_reviewed, category, type, sources and decision_packets for all 40 entries. agents.json, agents.csv, index.html and sitemap.xml are byte-identical.
- **New checks:** each fails as intended when tested against a deliberately broken copy (caveat without Replit; stale llms.txt date).
- **Banned-word scan** of the added lines: no new hits. The only matches are words carried over unchanged from the lines being edited, plus the standard disclaimer.
- **Link check:** the same 6 failures as the live repo, and no new failures.

## Minimum viable version
D1 (b) plus D2 plus the D9 row, which touches 2 entry or compare pages. Everything else can wait.

## Risks
- **Very low overall:** text only, with no data-field changes.
- D3 adds a generator step. It follows the 0072 pattern, and a broken copy fails the check.
- D1 (a)'s caveat wording was changed to "several of its counted tests" (O2) so that it is less likely to go stale.

## Plain-English terms
- **Recheck banner:** the note at the top of a page saying the search for citing studies was not finished.
- **Caveat:** a short warning printed on a comparison page.
- **Changelog row:** a public line describing a change.
- **Feed item:** the same change in the machine-readable update feeds.
- **Dry run:** trying the changes on a throwaway copy.
- **Patch preview:** the exact line-by-line differences that would be applied.

---
Informational only; not a guarantee, endorsement, or certification. Scores are based on public sources and the stated rules at the time of review.
