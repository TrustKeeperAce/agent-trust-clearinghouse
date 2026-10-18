# Decision 0061: Agent distribution plan

**Status: APPROVED by Remington, 2026-10-18**, minimal setup as recommended: D1a JSON + CSV + JSON Schema export generated from YAML with an export check; D2a llms.txt updated (data links, as-of date, usage note, Optional section), no llms-full.txt; D3a CC BY 4.0 for data and site text (LICENSE file; scripts, stylesheet and logo not covered); D4a Dataset JSON-LD on the data page only, index ItemList marked Descending with 'not a ranking of quality', no Review/AggregateRating/Rating; D5a no mirrors; D6a robots.txt open to all crawlers with a stance comment; D7a two listings (llmstxthub.com, Jenqyang/Awesome-AI-Agents) drafted for Remington to send himself after deploy; D8a no MCP server now; D9a sitemap lastmod generated from last_reviewed and changelog dates.



## Plain-English terms
- **llms.txt**: a Markdown file at the site root that gives AI agents a short summary of the site and a list of links (proposal: https://llmstxt.org/, v2 dated Aug 10, 2026).
- **llms-full.txt**: a widely used convention, though not part of the llmstxt.org spec: one file holding the full text, so an agent can read everything in one fetch.
- **JSON-LD / schema.org**: machine-readable labels inside a page's `<script type="application/ld+json">` block. They describe what the page is (for example a website, a list, or a dataset).
- **Dataset / ItemList / DataDownload**: schema.org types. ItemList means "a list of things". Dataset means "a downloadable collection of data". DataDownload means "a file to download".
- **Review / AggregateRating**: schema.org types for star ratings. Google may show them as stars in search results.
- **Export**: a copy of the directory data as a file (JSON or CSV) that programs can read directly.
- **CORS**: a browser rule about which other websites may fetch a file. `Access-Control-Allow-Origin: *` means any site may.
- **Awesome list**: a curated GitHub README of links on one topic. People add entries by pull request (PR) or issue.
- **MCP server**: a small service that lets AI assistants query a data source as a tool. We do not have one.

## 1. What happened: audit of the current state (checked 2026-10-18, America/New_York)

### llms.txt (`/llms.txt`, 5,219 bytes, served `text/plain; charset=utf-8`)
- **Good:**
  - Follows the llmstxt.org structure: H1, blockquote summary, a notes paragraph, then H2 link lists.
  - States "Informational only; not a guarantee, endorsement, or certification."
  - Explains the factor weights and the rule for "Insufficient evidence".
  - Lists all 34 entries with their overall score and grade, and gives the corrections email.
- **Gaps:**
  - No "as of" date or scoring-rules version per entry. "Scoring rules v0.1" appears only once.
  - No link to a machine-readable export, because none exists.
  - No sentence telling an agent how to cite or quote the scores.
  - No `## Optional` section. The spec uses that heading by convention for secondary links.
  - No Markdown versions of pages. The v2 spec suggests `page.html.md` alternates, discovered through `rel="alternate" type="text/markdown"` links or a `Link:` header (https://llmstxt.org/). This is optional; our HTML is already plain and has no JavaScript.

### JSON-LD
- **index.html only:**
  - A `WebSite` item whose description says "Not a guarantee, endorsement, or certification."
  - An `ItemList` ("Directory entries", `numberOfItems` 34, `itemListOrder` ItemListUnordered). Each entry has only `name` and `url`.
- **Good:** it contains no Review, AggregateRating or Rating markup, and no scores.
- **Gaps:**
  - Entry pages, methodology.html and changelog.html have no JSON-LD.
  - There is no Dataset markup, which Google Dataset Search needs (https://developers.google.com/search/docs/appearance/structured-data/dataset).
  - `itemListOrder` says Unordered, but the visible table is sorted by score (highest first). It is cautious, but technically inaccurate. Possible fixes: keep it, or switch to ItemListOrderDescending with a "sorted by overall score; not a ranking of quality" note in the description.

### sitemap.xml (36 URLs, `application/xml`)
- **Coverage:**
  - Includes all 33 entry pages, `/`, `/methodology.html` and `/changelog.html`.
  - Excludes llms.txt, robots.txt and the Search Console verification file. That is correct: the sitemap should list only indexable HTML pages.
- **lastmod accuracy:**
  - `/`, `/methodology.html` and `/changelog.html` show 2026-10-17. Decision 0060 changed all three on 2026-10-18 (privacy section, changelog row, footer link), so these dates are now stale.
  - Google uses `lastmod` only "if it's consistently and verifiably accurate" and for significant changes (https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap).
  - The footer link alone is not a significant change for the entry pages, so their dates can stay.
  - Fix: update those three dates in the next public packet, and have the generator set `lastmod` from each entry's `last_reviewed` and the latest changelog date rather than by hand.

### robots.txt
- `User-agent: * / Allow: /` plus the sitemap line. In practice this is an "open to all crawlers" stance, including AI search crawlers and AI training crawlers.
- OpenAI documents separate tokens: OAI-SearchBot for search, GPTBot for training, and ChatGPT-User for user-triggered fetches, to which "robots.txt rules may not apply" (https://platform.openai.com/docs/bots).
- Recommendation: keep the site open. The goal is that agents can read and cite it. Write the stance down explicitly (D6) instead of leaving it implicit.

### Headers and content types (live checks with `curl -I`)
- HTML is `text/html; charset=utf-8`. llms.txt and robots.txt are `text/plain; charset=utf-8`. The sitemap is `application/xml` with no charset; that is acceptable because XML declares its own encoding.
- Vercel already sends `Access-Control-Allow-Origin: *` on every static file, so any site can already fetch future JSON or CSV exports.
- `cache-control: public, max-age=0, must-revalidate` means data is never served stale from the CDN. Good for accuracy.
- HSTS (HTTPS-only) is on.
- `/` returned `308` to a HEAD request from curl, but `/index.html` returns 200 and the earlier full fetches of `/` worked. Worth one check in the next packet (likely just a HEAD quirk). Not a blocker.
- No `/llms-full.txt` (404) and no `/data/` path yet.
- The repository has no LICENSE file, so data and text are "all rights reserved" by default. Anyone reusing the data has no clear permission. This is the main gap for distribution (D3).

## 2. What the rules say (sources)
- **llms.txt v2** (https://llmstxt.org/):
  - Only the H1 is required.
  - Linked content should be LLM-friendly, and the file should stay small.
  - It names three directories: llmstxt.site, directory.llmstxt.cloud and llmstxthub.com. All returned HTTP 200 today.
- **Google review snippets** (https://developers.google.com/search/docs/appearance/structured-data/review-snippet):
  - AggregateRating is for "an aggregate evaluation of an item by many people". Our scores are one editor's rule-based assessment, not many people's ratings.
  - "Don't aggregate reviews or ratings from other websites." We build our scores from third-party sources.
  - Ratings for organizations must be "sourced directly from users".
  - Using it risks being judged spammy markup, which can bring a structured-data manual action.
  - Separately, star markup visually implies "rated / recommended", which is against our stance.
  - **Conclusion: do not use Review, AggregateRating or Rating anywhere.**
- **Google Dataset markup** (same Dataset URL as above):
  - Requires `name` and a `description` of 50–5,000 characters.
  - Recommends `license` with a versioned URL (for example `https://creativecommons.org/licenses/by/4.0`), `distribution` with DataDownload `contentUrl` and `encodingFormat`, plus `version`, `creator`, `isAccessibleForFree`, `temporalCoverage` and `variableMeasured`.
  - Markup goes on the canonical landing page.
  - This fits a "For agents / data" page and implies no endorsement.
- **CC BY 4.0** (https://creativecommons.org/licenses/by/4.0/): anyone may reuse, including commercially, if they credit us. Kaggle and Hugging Face both list it as a standard choice.
- **Hacker News Show HN** (https://news.ycombinator.com/showhn.html):
  - Show HN is for things people can try.
  - Off topic: "blog posts, sign-up pages, newsletters, **lists, and other reading material** … Make a regular submission instead."
  - "Please don't ask friends to upvote or comment."
  - The general guidelines say "Please don't use HN primarily for promotion. It's ok to post your own stuff part of the time" (https://news.ycombinator.com/newsguidelines.html).
  - → A plain directory is probably **not** a valid Show HN. A downloadable dataset or tool may be borderline. A regular submission is safer.
- **Product Hunt** (https://help.producthunt.com/en/articles/479557-how-to-post-a-product, May 28, 2025):
  - Needs a personal account that has completed onboarding; company accounts cannot post.
  - Makers are recommended to post their own product.
  - A post needs a URL, tagline, topics, a thumbnail, at least 2 gallery images, pricing (free) and a first comment. Launches go live at 12:01 AM Pacific.
- **Reddit spam policy** (https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam, updated Oct 6, 2026):
  - Bans repeated or unsolicited mass posting.
  - If your posts are mostly links to something you run, "be thoughtful about the frequency".
  - Each community's own rules and moderators decide; read them before posting.
- **Awesome lists (GitHub, last activity checked through the GitHub API on 2026-10-18):**
  - **e2b-dev/awesome-ai-agents** (~30.5k stars, last push 2026-08-21, not archived):
    - Accepts a PR or a Google Form ("Submit new product here", https://forms.gle/UXQFCogLYrPFvfoUA), in alphabetical order and in the correct category.
    - It lists individual agents; there is no category for meta-resources or directories.
    - Fit: weak. A directory isn't an agent. It could be suggested as a resource, but rejection is likely.
  - **kyrolabs/awesome-agents** (~2.9k stars, pushed 2026-10-17):
    - The contributing guide requires open source, "demonstrate traction", and rejects "brand new repo without demonstrated traction" and brand-new users. Checks are applied automatically.
    - Fit: not now. Revisit only once there is traction and an open data license.
  - **Jenqyang/Awesome-AI-Agents** (~1.3k stars, pushed 2026-10-16):
    - Its scope explicitly includes "Benchmark/Evaluator" and "Related resources".
    - Its quality bar asks for an open-source license, "evidence over marketing" and an active repo.
    - Fit: **best of the awesome lists**, once a LICENSE exists. An entry under "Benchmark/Evaluator" or "Related resources" would need an open repo and license.
  - **slavakurilyak/awesome-ai-agents** (~2.5k stars, pushed 2026-10-04):
    - Lists only projects with a public repository and a substantive commit within the last 6 months, submitted through an issue form. "Hosted products without their own qualifying repository are not eligible."
    - Fit: weak. It is for agent projects, not directories.
  - **thedaviddias/llms-txt-hub** (llmstxthub.com, ~0.9k stars, pushed 2026-10-17):
    - Lists sites that publish llms.txt; there is a submit page at https://llmstxthub.com/submit.
    - Fit: **good**. This is exactly what we have, and it is low effort.
  - **SecretiveShell/Awesome-llms-txt** (~0.1k stars, pushed 2026-09-28): small. Fit: fair, low reach.
- **MCP Registry** (https://registry.modelcontextprotocol.io, repo pushed 2026-10-14):
  - Lists only MCP servers. Publishing uses the `mcp-publisher` CLI and namespace verification (GitHub or DNS/HTTP), not PRs.
  - The repo README still describes the registry as a "preview" with possible breaking changes; its last status update is the Oct 2025 API freeze.
  - Not applicable unless we build an MCP server (fuller option, D8). **punkpeye/awesome-mcp-servers** (~96k stars) is likewise for MCP servers only.
- **Hugging Face Datasets** (https://huggingface.co/docs/hub/datasets-cards):
  - The dataset card is a README.md with YAML metadata (license, tags, pretty_name). A free account is required.
  - Good for discoverability among ML and agent builders. The card can carry the disclaimer and license.
- **Kaggle Datasets** (https://www.kaggle.com/docs/datasets):
  - Free account. Recommends CSV with column descriptions, and supports CC BY 4.0.
  - It can import from **a GitHub repository or remote URLs and set up automatic interval updates**, which limits stale mirrors.
  - Fit: fair. The audience is data scientists rather than agent buyers.
- **data.world:** the Open Data Community was **retired on July 13, 2026** and its public datasets are no longer available (https://data.world/community/goodbye/). Not an option.
- **Papers with Code:** shut down July 24, 2025; it now redirects to Hugging Face Trending Papers (https://github.com/paperswithcode/paperswithcode-data/issues/116). That page is for arXiv papers only, so not applicable unless we write a paper.
- **Newsletters (Ben's Bites, TLDR AI):** both sites are live (HTTP 200). Neither has a verified public editorial-submission rule, and most placements are paid sponsor slots. Treat these as "send a short tip email if it fits", with low priority and editorial acceptance not guaranteed. Not verified.

## 3. Options

### A. Static additions (no JavaScript; all generated from the YAML files)
1. **`/data/agents.json`**: one object with:
   - `dataset` (name, version = scoring-rules version plus data date, `generated` date, license URL, source repo, corrections contact);
   - `disclaimer` ("Informational only; not a guarantee, endorsement, or certification. Scores reflect public sources and the stated rules as of each entry's last_reviewed date.");
   - `usage_note` (see section 4);
   - `entries[]`: `id` (the stable slug, for example `elicit`), `name`, `url`, `category`, `type`, `scope`, `status`, the four factor scores, `overall_score` (null if insufficient), `evidence_grade`, `independent_source_count`, `last_reviewed`, `decision_packet`, and `sources[]` (url, kind, accessed).
2. **`/data/agents.csv`**: a flat version, one row per entry. It has no source lists (those stay in the JSON). Its first row is a header, and a `disclaimer` column is repeated on every row so that copied rows keep it.
3. **`/data/schema.json`**: a JSON Schema for the export, so agents and validators know the field meanings and ranges (0–100, null allowed).
4. **`/agents-data.html` ("For agents / data")**:
   - Plain HTML: what the files are, field definitions, license, how to cite, update cadence and the corrections route.
   - Carries the **Dataset JSON-LD** (with `distribution` for JSON and CSV, `license`, `version`, `dateModified`, `creator`, `isAccessibleForFree: true`, `variableMeasured` naming the four factors, and a description that includes the disclaimer).
   - Linked from the footer, llms.txt and the methodology page.
5. **llms.txt updates:** add the data and "For agents" links, an "as of" line, the usage note, and a `## Optional` section (changelog, schema).
6. **llms-full.txt (optional):** methodology plus every entry's summary, factor notes and sources in one Markdown file. About 100–200 KB, generated. D2 decides whether to add it.
7. **JSON-LD on entry pages (optional):**
   - Use a minimal `WebPage` with `about: {"@type": "SoftwareApplication" or "Thing", name, url}` and `isPartOf` pointing to the Dataset.
   - **No** Review, AggregateRating or Rating. Scores appear only as visible text and in the export.
   - D4 decides whether to do this at all; the benefit is small.
8. **Stable IDs:** the slug is the permanent ID. Renamed entries keep their slug, and removed entries stay in the export as `status: "withdrawn"` with a date, never silently dropped. This protects mirrors and citations.
9. **Content types:**
   - Vercel serves `.json` as `application/json` and `.csv` as `text/csv` by default. Verify after the first deploy and add a `headers` rule in vercel.json only if needed.
   - CORS `*` is already present.
   - Each file stays small (under about 200 KB), so scraping load is negligible.
10. **Checks:** extend `check_scores` or add a `check_export` step that confirms the export matches the YAML exactly (same counts, same scores, same grades) and that every row carries the disclaimer. Exports are rebuilt in every packet that changes an entry.

### B. Listing venues, with fit, effort, account and risk (Remington posts everything)
| Venue | Status 2026 | Fit | Effort | Account | Risk |
|---|---|---|---|---|---|
| llmstxthub.com submit | live, active | High (we publish llms.txt) | 10 min form/PR | maybe GitHub | Low |
| llmstxt.site, directory.llmstxt.cloud | live (HTTP 200); submission rules not verified | Med | 10 min | unknown | Low |
| Jenqyang/Awesome-AI-Agents (Benchmark/Evaluator) | active | Med–High once licensed | 30 min PR | GitHub | Rejection if no license; self-promo optics |
| e2b-dev/awesome-ai-agents | active (Aug 2026) | Low (agent list) | form | none (form) | Likely ignored |
| kyrolabs / slavakurilyak lists | active | Not eligible now | — | GitHub | Auto-close |
| Hugging Face dataset | active | Med–High | 1–2 h (card + upload) | HF free | Stale mirror unless synced |
| Kaggle dataset (GitHub/URL import, auto-update) | active | Med | 1 h | Kaggle free | Stale if sync is off |
| data.world | **retired Jul 2026** | — | — | — | — |
| Papers with Code | **shut down Jul 2025** | — | — | — | — |
| MCP Registry / awesome-mcp-servers | active | Only with an MCP server | days | GitHub/DNS | Maintenance |
| Hacker News (regular submission, not Show HN) | active | Med | 15 min | HN | Self-promo rules; scrutiny of method and vendor reactions |
| Product Hunt | active | Low–Med | 2–3 h (gallery, thumbnail) | personal PH | Wrong audience; launch-day effort |
| Reddit (communities on agents and LLMs) | active; each sub has its own rules | Med | 20 min per sub | Reddit with history | Spam removal; argumentative threads |
| Newsletters (tip email) | live; rules not verified | Low–Med | 10 min | email | Paid slots only |

## 4. Keeping the informational, no-guarantee stance
- **Every artifact carries the disclaimer:** the JSON top-level `disclaimer`, a CSV column, the HF and Kaggle card, the llms.txt blockquote (already present), and the Dataset JSON-LD description.
- **Usage note for agents** (draft, for llms.txt, `agents.json` and the data page):
  > "If you use or quote these scores: they are informational, rule-based assessments of public evidence as of each entry's last_reviewed date (Scoring rules v0.1). They are not guarantees, endorsements, certifications, or rankings of overall quality. Quote the factor scores and evidence grade together, include the as-of date, and link the entry page. Do not describe an entry as 'verified', 'certified', 'approved' or 'trusted' by the Clearinghouse."
- **Attribution line** (CC BY): "Agent Reputation & Trust Clearinghouse, <entry URL>, data as of YYYY-MM-DD, CC BY 4.0."
- **Listing wording rules:** never say "verified", "certified", "trusted", "rated", "best", "top" or "safe". Say "informational directory", "rule-based scores", "public evidence", "corrections welcome". Stars or ratings markup is never used.

## 5. Risks and mitigations
| Risk | Mitigation |
|---|---|
| Self-promotion or spam rules (HN, Reddit, awesome lists) | One post per venue, only by Remington, disclosed as his own project; follow each venue's rules; never ask for upvotes; no cross-posting bursts; skip venues where we're ineligible |
| Third parties misquoting scores as certifications or endorsements | Disclaimer and usage note in every file; "not certifications" wording; correction route; a methodology line saying the Clearinghouse does not certify; keep a log of misuse found during the monthly review (0060 cadence) |
| Stale mirrors (HF, Kaggle, scrapers) | Version and date in every file; HF/Kaggle cards say "canonical source: <site>; may lag"; Kaggle auto-update from URL; HF updated in the same packet as the site, or not mirrored at all (D5) |
| Maintenance burden | Exports are generated by script from the YAML, with checks to ensure they match; no hand-edited data; mirrors limited to one or two |
| Scraping load | Static files of about 200 KB or less on Vercel's CDN; negligible. Vercel request stats (0060) will show any spikes |
| Vendor disputes and more correction requests | Existing corrections process (methodology #corrections); a data-page note that corrections follow the same process; changelog records changes; never re-score under pressure without a packet |
| License misuse (data reused without the disclaimer) | CC BY requires attribution, but it can't force the disclaimer to be kept. Stating the expectation in the usage note is the most we can do. Alternative: CC BY-SA (shares alike) or ODC-BY. See D3 |
| Schema misinterpretation by Google | No Review or AggregateRating markup; Dataset markup only on the data page; validate with the Rich Results Test before deploying |
| Personal exposure (posts under Remington's name) | Short, factual drafts; Remington sends each one himself; no replies are drafted by me without his request |

## 6. Recommendation
- **Minimal viable (recommended now, one public packet):**
  1. License decision (D3: CC BY 4.0 for data, plus a LICENSE file).
  2. `/data/agents.json`, `/data/agents.csv` and `/data/schema.json`, generated with checks.
  3. A "For agents / data" page with Dataset JSON-LD and a footer link.
  4. llms.txt updated (data links, usage note, as-of date, `## Optional`).
  5. Sitemap `lastmod` fixed and generated automatically.
  6. A robots.txt stance comment.
  7. Then exactly **two** outbound listings, drafted for Remington: **llmstxthub.com** and the **Jenqyang/Awesome-AI-Agents** PR or issue.
  - No llms-full.txt, no entry-page JSON-LD and no mirrors yet.
- **Fuller options (later, each its own packet):**
  - llms-full.txt and `.md` page alternates.
  - A Hugging Face dataset mirror (and/or Kaggle with auto-update).
  - One HN regular submission and one or two Reddit posts once the export exists.
  - Product Hunt only if there's a reason to.
  - A read-only MCP server listed on the MCP Registry, which requires hosting a server, namespace verification and ongoing maintenance.

## 7. D-items (each needs approval)
- **D1 Machine-readable export.**
  - **(a) Recommended:** JSON + CSV + JSON Schema at `/data/`, generated from YAML, with an export check.
  - (b) JSON only.
  - (c) No export; llms.txt only.
- **D2 llms.txt and llms-full.txt.**
  - **(a) Recommended:** update llms.txt (data links, usage note, as-of date, Optional section); no llms-full.txt yet.
  - (b) Also add llms-full.txt.
  - (c) Also add `.md` page alternates.
- **D3 Data license.**
  - **(a) Recommended:** CC BY 4.0 for the data and site text (https://creativecommons.org/licenses/by/4.0/), plus a LICENSE file in the repo. Simple and widely accepted by HF, Kaggle and awesome lists.
  - (b) ODC-BY 1.0 (designed for databases).
  - (c) CC BY-SA 4.0 (copies must stay under the same license; more protective, less adopted).
  - (d) CC0 (no conditions; loses attribution).
  - (e) No license (all rights reserved; blocks most listings).
  - This is a legal choice that Remington should make himself. I can't give legal advice.
- **D4 Structured data.**
  - **(a) Recommended:** Dataset JSON-LD on the data page only. Keep the index ItemList and correct `itemListOrder` to Descending with "sorted by overall score; not a ranking of quality". Never use Review, AggregateRating or Rating.
  - (b) Also add a minimal WebPage `about` block to entry pages.
  - (c) No changes.
- **D5 Mirrors.**
  - **(a) Recommended:** none yet.
  - (b) Hugging Face dataset, updated in each packet.
  - (c) Kaggle with URL auto-update.
  - (d) Both.
- **D6 robots.txt stance.**
  - **(a) Recommended:** stay open to all crawlers, including AI search and training crawlers, and add a comment line that says so and points to llms.txt.
  - (b) Allow search and user-triggered agents but disallow training crawlers (for example GPTBot).
  - (c) No change.
- **D7 Outbound listings, phase 1** (drafted by me, sent by Remington).
  - **(a) Recommended:** llmstxthub.com plus Jenqyang/Awesome-AI-Agents, after D1/D3 are live.
  - (b) (a) plus one HN regular submission.
  - (c) (b) plus Reddit and Product Hunt.
  - (d) None.
- **D8 MCP server.**
  - **(a) Recommended:** not now; revisit after 0060 traffic data (three monthly reviews).
  - (b) Draft a separate packet for a read-only MCP server.
- **D9 Sitemap lastmod.**
  - **(a) Recommended:** fix the three stale dates and generate `lastmod` from `last_reviewed` and the changelog.
  - (b) Fix by hand only.

## 8. Outbound drafts (for Remington to send himself; not sent)
- **llmstxthub.com** (https://llmstxthub.com/submit):
  - Name: Agent Reputation & Trust Clearinghouse.
  - URL: https://agent-trust-clearinghouse.vercel.app/
  - llms.txt: https://agent-trust-clearinghouse.vercel.app/llms.txt
  - Description: "Informational directory of digital-task AI agents with transparent, rule-based factor scores from public evidence. Not a guarantee, endorsement, or certification."
- **Jenqyang/Awesome-AI-Agents** (PR or issue; section "Benchmark/Evaluator" or "Related resources", whichever the maintainer prefers):
  > `- [Agent Reputation & Trust Clearinghouse](https://agent-trust-clearinghouse.vercel.app/) - Informational directory of AI agents with rule-based factor scores (completion, disputes, adherence, evidence quality) built from cited public sources; open data (CC BY 4.0) at /data/agents.json. Not a certification.`
  - PR body: "Hi, I maintain this directory. It scores agents only from independent public sources, using published rules, and shows each factor separately. Data and methodology are open. Happy to move it to a different section or drop it if it's out of scope."
- **HN regular submission (only if D7b):**
  - Title: "Agent Reputation & Trust Clearinghouse: rule-based scores for AI agents from public evidence".
  - Link: the site. No "Show HN" prefix (lists and reading material are off-topic for Show HN).
  - First comment: what it is, how sources are counted, that it is not a certification, and where to send corrections.

## 9. Uncertainties
- Submission rules for llmstxt.site and directory.llmstxt.cloud were not verified beyond the sites being live.
- Newsletter editorial policies were not verified.
- Reddit rules vary by community; each one must be checked before posting.
- Whether Jenqyang's maintainer accepts directories or meta-resources under "Benchmark/Evaluator" is a judgment call. Its contributing text lists "Related resources" as in scope.
- The `/` HEAD 308 result needs one more check.
- Google Dataset Search inclusion is not guaranteed.
- The license choice has legal implications; this packet doesn't give legal advice.
- The MCP Registry's own README still says "preview"; its status could change.
