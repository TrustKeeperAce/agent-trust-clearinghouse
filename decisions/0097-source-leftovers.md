# Decision 0097: leftover links from 0096 (ChatGPT Work release-notes address, 22 page-only links, reverse link check)

**Status: APPROVED by Remington, 2026-10-23 (4:34 PM ET, t261u), as recommended:**
- **D1 (a):** ChatGPT Work homepage: use `https://help.openai.com/en/articles/6825453-chatgpt-release-notes` (with "s") in agents/chatgpt-work.yaml and for the two links on the entry page.
- **D2 (a):** keep the 11 links in older "Excluded sources" / "Not counted" lists on their pages as page-only links; do not add them to agents.json.
- **D3 (a):** keep the 11 links in page text as page-only citations; update the Seoul Economic Daily link on Kimi Researcher to the address it permanently redirects to.
- **D4 (a):** record the 22 page-only links in data/page_only_links.yaml and add check 0097 (the reverse of 0096): every outbound link on an entry page must be a source of that entry in agents.json, its homepage, a decision record in this repository, or a recorded page-only link; every recorded link must still be on its page and must not also be a source.
- **D5 (a):** one site_change changelog row and its feed item.
- **D6 (a):** last-reviewed dates unchanged.
- **D7 (a):** not done here: adding any page-only link to agents.json as a listed, not counted source. It would change listed-source counts, so it needs its own packet.

Wording choices W1–W4 kept as drafted.

Commit and push approved 2026-10-23 (5:06 PM ET, t262u commit approved, W1–W4 as recommended; deploy not approved); committed as fe3e7a8. Deploy needs separate approval.

## What happened
Decision 0096 linked the three agents.json sources that were missing from their pages and noted three leftovers for a later packet. Checked again on 23 October 2026:

- **ChatGPT Work homepage address.** The data uses `…/6825453-chatgpt-release-note`; the OpenAI Deep Research entry uses `…/6825453-chatgpt-release-notes`. Both addresses open the same OpenAI Help Center article, titled "ChatGPT release notes". The help center finds articles by their number (6825453), so the words after it do not change which page opens. Both return HTTP 403 to automated requests (a Cloudflare check), but a fetch through a reading service returned the same article for both. The address with "s" matches the article's title and the other entry, so it is the one to use.
- **Links in older "Excluded sources" / "Not counted" lists (11).** These lists were written into the pages before excluded items were recorded in the data. Each line says why the item is not counted (vendor-authored, competitor-published, retracted, tests the model rather than the product, restates a vendor figure, commentary without testing). All 11 open (HTTP 200; the Consensus DOI leads to the publisher page, which marks the article "[Retracted]"). Three of the Claude Research items (ReportBench, DeepResearch Bench II and the Rao, Wong and Callison-Burch study) are already counted sources on the Gemini Deep Research entry, where they test that product.
- **Links in page text (11).** These support sentences in timelines, security and disputes paragraphs: five NVD vulnerability records, a Skyvern fix commit, an OpenAI forum reply, the Operator announcement, two news reports about Kimi and the Manus 1.6 release post. Each related fact already has a listed source in the data where one applies (for example CVE-2026-84885 for the Agent S group, the ZDI advisory and CVE-2026-19060 for Data Interpreter, the CVE record for Skyvern, and the OECD incident record for Kimi). All 11 open. The Seoul Economic Daily address now permanently redirects (HTTP 308) from a 30 April path to a 1 May path; the article is the same.

## What the rules say
- Scores count only independent performance sources under the published rules. None of these 22 links is counted, and none would be under the current rules.
- Every listed source is linked on its entry page (0096). Nothing yet required the reverse.
- Last reviewed changes only when a packet re-checks an entry's sources and scores; wording, formatting or link-label fixes do not change it (methodology).

## What changes (recommended set)
- **agents/chatgpt-work.yaml** (homepage) and **public/data/agents.json** (homepage field only, rebuilt).
- **public/agents/chatgpt-work.html:** two links to the release notes use the address with "s".
- **public/agents/kimi-researcher.html:** the Seoul Economic Daily link uses its current address.
- **data/page_only_links.yaml** (new, not published): the 22 page-only links, each with its entry, place and a short note.
- **scripts/check_export.py:** check 0097, described above. Process rule only.
- **Changelog row and feed item** 2026-10-23-0097 (site_change, no per-agent changes). The row is dated on the day it is committed. The "Data as of" date on agents-data.html, llms.txt, citing.html and the compare pages, and the sitemap lastmods of the site pages, follow the newest changelog date (0090 D3), so they change to that date; entry-page lastmods do not.
- **Not changed:** scores, grades, counted and listed source counts, last-reviewed dates, agents.csv, the sitemap, llms.txt, llms-full.txt and the other 41 entry pages.

## Not done here
- Adding page-only links to agents.json (D7): would raise listed-not-counted counts and, for "other" kinds, the typed other count shown on pages and in agents.csv.
- NVD links that redirect to a lower-case address (HTTP 301) are left as they are; they open the right record.
- The ChatGPT Work timeline gives 9 July 2026 for the launch, while the release-notes article lists "Introducing ChatGPT Work" under 13 July 2026. The same 13 July section also refers to a change "beginning July 9", so the dates may describe different things. Noted for a later re-check; not changed here.

## Plain-English terms
- **Page-only link:** a link shown on an entry page for context that is not one of the entry's listed sources in the data.
- **Listed source / counted source:** every source in agents.json is listed; only independent performance sources that meet the rules are counted toward a score.
- **Redirect:** when a website sends a visitor from an old address to a new one.

*Informational only. Scores summarize cited public evidence under published rules; they are not a guarantee, endorsement, certification or ranking of quality.*
