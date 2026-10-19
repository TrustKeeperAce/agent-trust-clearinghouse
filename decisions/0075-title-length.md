**Status: APPROVED 2026-10-19 (D1a–D7a, Option B). D7a: deploy before Nov 1 and note the title-change date in the Nov 15 review. Deploy (D8) needs separate approval.**

# 0075 — Title length

## 1. What happened
- I read every `<title>` in `public/` (44 pages with a title; the Google verification file has none). On every page the title, `og:title` and `twitter:title` are the same text; 404.html has no og:title.
- Every title ends with the suffix ` — Agent Reputation & Trust Clearinghouse` (41 characters including the space and dash). Shortest title: Clay, 45; longest: 88.
- **Eleven titles are over 70, not four.** The export check (0069 D7a) warns only for *generated* pages (`gen_pages` = citing + the 3 compare pages), so 7 entry-page titles over 70 were never flagged:
  - flagged: compare/claude-code-and-openai-codex 88, compare/research-agents 82, compare/coding-agents 80, citing 72;
  - not flagged: agents/ui-tars-desktop 85, agents/storm 83, agents/data-interpreter 80, agents/openai-codex 75, agents/perplexity-comet 75, agents/browser-use 74, agents/agent-s 72.
- How the suffix is applied: **generated** for compare pages and citing.html (build_data.py, from the page title + SITE_NAME); **hand-written** in the HTML for entry pages, index, methodology, changelog, agents-data and 404 (the entry-page parenthetical, e.g. "(knowledge-storm library)", is hand-written too). No single function sets every title.
- Brand use elsewhere (unchanged by any option): header wordmark "Agent Reputation & Trust / Clearinghouse"; `og:site_name`; JSON-LD names; `SITE_NAME`; CITATION.cff `title` and author name; README H1; feeds title; llms.txt / llms-full.txt H1; the citing guidance and attribution text ("Agent Reputation & Trust Clearinghouse, CC BY 4.0, …").

## 2. Sources and what the rules say
- Google Search Central, "Influencing your title links in search results", https://developers.google.com/search/docs/appearance/title-link (fetched 2026-10-19):
  - "there's no limit on how long a `<title>` element can be, the title link is truncated in Google Search results as needed, typically to fit the device width" — truncation is by width, not a character count. **Google does not publish a 50–60 character figure**; that number is an industry rule of thumb, unverified.
  - "Brand your titles concisely … consider including just your site name at the beginning or end of each `<title>` element, separated … with a delimiter".
  - "Avoid repeated or boilerplate text"; Google may rewrite title links using the H1, og:title, anchor text and WebSite structured data; changes take "a few days to a few weeks" to be noticed.
  - "Google may omit the site name from the title link, if it's repetitive with the site name that's already shown in the search result."
- Site names: https://developers.google.com/search/docs/appearance/site-names — the site name in results comes mainly from `WebSite` structured data, which index.html already has (`"@type":"WebSite"`, name = the full brand). So the suffix is not needed for Google to show the brand.
- House rules: neutral wording, no best/top/ranking; no scoring or data changes; deploy needs separate approval.

## 3. Options (exact titles and lengths)
#### All current titles (title = og:title = twitter:title on every page; 404 has no og:title)

| Len | Page | Current title | Option A (short suffix) | Len A |
|---|---|---|---|---|
| 88 **>70** | compare/claude-code-and-openai-codex.html | Claude Code and Codex compared: public evidence — Agent Reputation & Trust Clearinghouse | Claude Code and Codex compared: public evidence — Agent Trust Clearinghouse | 75 |
| 85 **>70** | agents/ui-tars-desktop.html | UI-TARS Desktop (ByteDance, open-source app) — Agent Reputation & Trust Clearinghouse | UI-TARS Desktop (ByteDance, open-source app) — Agent Trust Clearinghouse | 72 |
| 83 **>70** | agents/storm.html | STORM / Co-STORM (knowledge-storm library) — Agent Reputation & Trust Clearinghouse | STORM / Co-STORM (knowledge-storm library) — Agent Trust Clearinghouse | 70 |
| 82 **>70** | compare/research-agents.html | Research agents compared: public evidence — Agent Reputation & Trust Clearinghouse | Research agents compared: public evidence — Agent Trust Clearinghouse | 69 |
| 80 **>70** | agents/data-interpreter.html | Data Interpreter (MetaGPT, open-source) — Agent Reputation & Trust Clearinghouse | Data Interpreter (MetaGPT, open-source) — Agent Trust Clearinghouse | 67 |
| 80 **>70** | compare/coding-agents.html | Coding agents compared: public evidence — Agent Reputation & Trust Clearinghouse | Coding agents compared: public evidence — Agent Trust Clearinghouse | 67 |
| 75 **>70** | agents/openai-codex.html | OpenAI Codex (CLI and cloud agent) — Agent Reputation & Trust Clearinghouse | OpenAI Codex (CLI and cloud agent) — Agent Trust Clearinghouse | 62 |
| 75 **>70** | agents/perplexity-comet.html | Perplexity Comet (agentic browser) — Agent Reputation & Trust Clearinghouse | Perplexity Comet (agentic browser) — Agent Trust Clearinghouse | 62 |
| 74 **>70** | agents/browser-use.html | Browser Use (open-source library) — Agent Reputation & Trust Clearinghouse | Browser Use (open-source library) — Agent Trust Clearinghouse | 61 |
| 72 **>70** | agents/agent-s.html | Agent S (open-source framework) — Agent Reputation & Trust Clearinghouse | Agent S (open-source framework) — Agent Trust Clearinghouse | 59 |
| 72 **>70** | citing.html | How to cite and quote this data — Agent Reputation & Trust Clearinghouse | How to cite and quote this data — Agent Trust Clearinghouse | 59 |
| 68 | agents/aide.html | AIDE (Weco AI, open-source) — Agent Reputation & Trust Clearinghouse | AIDE (Weco AI, open-source) — Agent Trust Clearinghouse | 55 |
| 68 | agents/github-copilot-coding-agent.html | GitHub Copilot coding agent — Agent Reputation & Trust Clearinghouse | GitHub Copilot coding agent — Agent Trust Clearinghouse | 55 |
| 68 | agents/openfactcheck.html | OpenFactCheck (open-source) — Agent Reputation & Trust Clearinghouse | OpenFactCheck (open-source) — Agent Trust Clearinghouse | 55 |
| 65 | agents/autokaggle.html | AutoKaggle (open-source) — Agent Reputation & Trust Clearinghouse | AutoKaggle (open-source) — Agent Trust Clearinghouse | 52 |
| 65 | agents/fellou.html | Fellou (agentic browser) — Agent Reputation & Trust Clearinghouse | Fellou (agentic browser) — Agent Trust Clearinghouse | 52 |
| 64 | agents/claude-code.html | Claude Code (Anthropic) — Agent Reputation & Trust Clearinghouse | Claude Code (Anthropic) — Agent Trust Clearinghouse | 51 |
| 64 | agents/openhands.html | OpenHands (open-source) — Agent Reputation & Trust Clearinghouse | OpenHands (open-source) — Agent Trust Clearinghouse | 51 |
| 64 | agents/swe-agent.html | SWE-agent (open-source) — Agent Reputation & Trust Clearinghouse | SWE-agent (open-source) — Agent Trust Clearinghouse | 51 |
| 62 | agents/skyvern.html | Skyvern (open-source) — Agent Reputation & Trust Clearinghouse | Skyvern (open-source) — Agent Trust Clearinghouse | 49 |
| 61 | agents/gemini-deep-research.html | Gemini Deep Research — Agent Reputation & Trust Clearinghouse | Gemini Deep Research — Agent Trust Clearinghouse | 48 |
| 61 | agents/google-deepmind-safe.html | Google DeepMind SAFE — Agent Reputation & Trust Clearinghouse | Google DeepMind SAFE — Agent Trust Clearinghouse | 48 |
| 61 | agents/openai-deep-research.html | OpenAI Deep Research — Agent Reputation & Trust Clearinghouse | OpenAI Deep Research — Agent Trust Clearinghouse | 48 |
| 60 | agents/aider.html | Aider (open-source) — Agent Reputation & Trust Clearinghouse | Aider (open-source) — Agent Trust Clearinghouse | 47 |
| 59 | agents/loki.html | Loki (open-source) — Agent Reputation & Trust Clearinghouse | Loki (open-source) — Agent Trust Clearinghouse | 46 |
| 58 | agents-data.html | For agents / data — Agent Reputation & Trust Clearinghouse | For agents / data — Agent Trust Clearinghouse | 45 |
| 58 | agents/devin.html | Devin (Cognition) — Agent Reputation & Trust Clearinghouse | Devin (Cognition) — Agent Trust Clearinghouse | 45 |
| 57 | agents/open-interpreter.html | Open Interpreter — Agent Reputation & Trust Clearinghouse | Open Interpreter — Agent Trust Clearinghouse | 44 |
| 56 | agents/claude-research.html | Claude Research — Agent Reputation & Trust Clearinghouse | Claude Research — Agent Trust Clearinghouse | 43 |
| 56 | agents/kimi-researcher.html | Kimi Researcher — Agent Reputation & Trust Clearinghouse | Kimi Researcher — Agent Trust Clearinghouse | 43 |
| 55 | 404.html | Page not found — Agent Reputation & Trust Clearinghouse | Page not found — Agent Trust Clearinghouse | 42 |
| 55 | agents/gpt-researcher.html | GPT Researcher — Agent Reputation & Trust Clearinghouse | GPT Researcher — Agent Trust Clearinghouse | 42 |
| 53 | agents/chatgpt-work.html | ChatGPT Work — Agent Reputation & Trust Clearinghouse | ChatGPT Work — Agent Trust Clearinghouse | 40 |
| 52 | methodology.html | Methodology — Agent Reputation & Trust Clearinghouse | Methodology — Agent Trust Clearinghouse | 39 |
| 51 | agents/perplexity.html | Perplexity — Agent Reputation & Trust Clearinghouse | Perplexity — Agent Trust Clearinghouse | 38 |
| 50 | agents/consensus.html | Consensus — Agent Reputation & Trust Clearinghouse | Consensus — Agent Trust Clearinghouse | 37 |
| 50 | agents/julius-ai.html | Julius AI — Agent Reputation & Trust Clearinghouse | Julius AI — Agent Trust Clearinghouse | 37 |
| 50 | changelog.html | Changelog — Agent Reputation & Trust Clearinghouse | Changelog — Agent Trust Clearinghouse | 37 |
| 50 | index.html | Directory — Agent Reputation & Trust Clearinghouse | Directory — Agent Trust Clearinghouse | 37 |
| 47 | agents/elicit.html | Elicit — Agent Reputation & Trust Clearinghouse | Elicit — Agent Trust Clearinghouse | 34 |
| 47 | agents/pactum.html | Pactum — Agent Reputation & Trust Clearinghouse | Pactum — Agent Trust Clearinghouse | 34 |
| 46 | agents/manus.html | Manus — Agent Reputation & Trust Clearinghouse | Manus — Agent Trust Clearinghouse | 33 |
| 45 | agents/clay.html | Clay — Agent Reputation & Trust Clearinghouse | Clay — Agent Trust Clearinghouse | 32 |

#### Option B: shorten the page-specific part, keep the full suffix

| Page | Now | New title | Len |
|---|---|---|---|
| agents/agent-s.html | 72 | Agent S (open-source) — Agent Reputation & Trust Clearinghouse | 62 |
| agents/browser-use.html | 74 | Browser Use (open-source) — Agent Reputation & Trust Clearinghouse | 66 |
| agents/data-interpreter.html | 80 | Data Interpreter (MetaGPT) — Agent Reputation & Trust Clearinghouse | 67 |
| agents/openai-codex.html | 75 | OpenAI Codex — Agent Reputation & Trust Clearinghouse | 53 |
| agents/perplexity-comet.html | 75 | Perplexity Comet — Agent Reputation & Trust Clearinghouse | 57 |
| agents/storm.html | 83 | STORM / Co-STORM — Agent Reputation & Trust Clearinghouse | 57 |
| agents/ui-tars-desktop.html | 85 | UI-TARS Desktop (ByteDance) — Agent Reputation & Trust Clearinghouse | 68 |
| citing.html | 72 | How to cite this data — Agent Reputation & Trust Clearinghouse | 62 |
| compare/claude-code-and-openai-codex.html | 88 | Claude Code and Codex — Agent Reputation & Trust Clearinghouse | 62 |
| compare/coding-agents.html | 80 | Coding agents compared — Agent Reputation & Trust Clearinghouse | 63 |
| compare/research-agents.html | 82 | Research agents compared — Agent Reputation & Trust Clearinghouse | 65 |

#### Option C: drop the suffix only where the full title would exceed 70

| Page | New title | Len |
|---|---|---|
| agents/agent-s.html | Agent S (open-source framework) | 31 |
| agents/browser-use.html | Browser Use (open-source library) | 33 |
| agents/data-interpreter.html | Data Interpreter (MetaGPT, open-source) | 39 |
| agents/openai-codex.html | OpenAI Codex (CLI and cloud agent) | 34 |
| agents/perplexity-comet.html | Perplexity Comet (agentic browser) | 34 |
| agents/storm.html | STORM / Co-STORM (knowledge-storm library) | 42 |
| agents/ui-tars-desktop.html | UI-TARS Desktop (ByteDance, open-source app) | 44 |
| citing.html | How to cite and quote this data | 31 |
| compare/claude-code-and-openai-codex.html | Claude Code and Codex compared: public evidence | 47 |
| compare/coding-agents.html | Coding agents compared: public evidence | 39 |
| compare/research-agents.html | Research agents compared: public evidence | 41 |

#### Option D: raise the guide to 90. No title changes (longest is 88).

Under Option A, 2 titles are still over 70 (Claude Code/Codex compare 75, UI-TARS 72), so A needs B-style trims on those two as well.

**Option A conflicts:** "Agent Trust Clearinghouse" is not the published name. CITATION.cff title and author, README H1, SITE_NAME, og:site_name, JSON-LD and the attribution text all say "Agent Reputation & Trust Clearinghouse". The title would be the only place with the short form, which makes the brand inconsistent and changes all 44 titles.

## 4. Impact
- **Search snippets:** B changes 11 titles, A changes 44, C changes 11 but those pages lose the brand (Google can still show it from WebSite data), D changes none. Every change needs a recrawl (days to weeks), so expect title churn in Search Console page and query data. The Nov 15 review uses a 28-day window: changes deployed now will be inside that window. Note the change date in the review.
- **Agents and feeds:** llms.txt and llms-full.txt use entry *names* from the data, not page titles, so they are unaffected. JSON-LD names and og:site_name are unchanged. og:title and twitter:title follow the title (same text) in every option. The citing guidance quotes SITE_NAME, not the title: unaffected. Feed item titles are separate: unaffected.
- **Checks that assume the suffix:** none today. check_export only measures length on generated pages. Option C would need a conditional suffix rule in the checks.
- **H1 and brand:** unchanged in every option.

## 5. Risks
- Brand inconsistency (Option A).
- Title churn around the Nov 15 baseline (any option except D). Mitigation: deploy as one batch, note the date in the review.
- Losing explanatory text: B drops parentheticals such as "(knowledge-storm library)" and "(CLI and cloud agent)" from the title. They stay in the H1, meta description and scope.
- Hand-written titles drift again. Mitigation: extend the check to every page.
- Option C makes the suffix inconsistent across pages (11 without, 33 with).

## 6. Proposed checks (check_export.py)
1. Title length on **all** pages (not only generated ones): error if over 70 (or a warning, per D3).
2. Suffix pattern: every title ends with ` — Agent Reputation & Trust Clearinghouse` (or the approved form), taken from SITE_NAME. Excludes the verification file.
3. Titles are unique across pages.
4. og:title and twitter:title equal the title.
5. Banned-word scan on titles (existing list: best/top/winner/stars/certified/verified/endorsed, and so on).

## 7. D-items
- **D1 Approach.** a) Option B: shorten the 11 page-specific parts, keep the full suffix (rec.: brand intact, fewest changes); b) Option A: short suffix plus 2 trims (44 changes, brand mismatch); c) Option C: drop the suffix on long pages; d) Option D: raise the guide to 90, no changes.
- **D2 B wording.** a) the titles in the Option B table (rec.); b) the user edits individual titles.
- **D3 Check severity.** a) over 70 on any page is an error (rec.; the hook then blocks drift); b) a warning only.
- **D4 Other checks.** a) suffix pattern, uniqueness, og/twitter equality and banned words (rec.); b) length only.
- **D5 Generation.** a) leave entry titles hand-written and rely on the checks (rec.); b) generate every title from a `title_short` field (larger change).
- **D6 Changelog row.** a) one row (rec.); b) none.
- **D7 Timing.** a) deploy together, before Nov 1, and note it in the Nov 15 review (rec.); b) wait until after Nov 15.
- **D8 Deploy** needs separate approval.

## 8. Minimum viable version
Option B for the 4 flagged pages only (citing and the 3 compare pages, all generated), plus check 1 as a warning on all pages. The 7 entry titles stay as they are for now.

## 9. Plain-English terms
- **Title / title link:** the page name shown in the browser tab and as the blue link in search results.
- **Suffix:** the site name added to the end of every title.
- **Truncation:** search results cut long titles to fit the screen width.
- **og:title / twitter:title:** the title shown when a link is shared in social apps.
- **Churn:** search tools briefly treating changed pages as new, which makes early statistics noisier.

## Implementation notes
- Compare and citing titles via build_data.py (COMPARE title fields; new CITE_DOC_TITLE for the <title> only, so the citing H1 and JSON-LD keep CITE_TITLE). Suffix now built from SITE_NAME.
- The 7 entry-page titles were edited by hand (title, og:title, twitter:title only).
- check_export.py: the generated-only 70-character warning is replaced by an error on every page, plus suffix, uniqueness, og/twitter equality and banned-word checks.
