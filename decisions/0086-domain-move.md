# Decision 0086: Move the site to www.agentclearinghouse.org

**Status: APPROVED by Remington, 2026-10-20 (t179u), D1–D8 as recommended. D1a keep www as the primary host; D2a one address-switch commit; D3a a permanent redirect from the old vercel.app address, prepared as a separate follow-up deploy; D5a one neutral changelog row, LOG entry and this record; D7a two deploys (address switch first, redirect second). Deploy 1 and deploy 2 each need separate approval.**

## 1. What happened
- The project registered **agentclearinghouse.org** (2026-10-20).
  - Both `agentclearinghouse.org` and `www.agentclearinghouse.org` are attached to the Vercel project and show a valid configuration.
  - The bare domain permanently redirects (308) to `www.agentclearinghouse.org`, keeping the path and query.
  - Let's Encrypt certificates for both names were issued on 2026-10-20 (about 11:34 ET).
- Before this change, every page, data file and feed named `https://agent-trust-clearinghouse.vercel.app` as the site's address:
  - canonical links, `og:url`, JSON-LD, sitemap, robots.txt, llms.txt, llms-full.txt;
  - `agents.json` / `agents.csv` URLs, the feeds' links, the citing page;
  - README and CITATION.cff.
- Where the address lives:
  - in one constant (`BASE`) in `scripts/build_data.py` for generated files;
  - as literal text in the hand-built pages (entry pages, home, methodology, changelog, data page);
  - in two check scripts (`check_export.py` README link check, `check_links.py` self-link skip).
- The feed item ids are domain-independent `tag:agent-trust-clearinghouse,2026:…` URIs (0065), so they don't change when the address changes. Feed readers won't see old items again.

## 2. What the rules say
- Static site, no JavaScript beyond JSON-LD, CC BY 4.0 data, neutral wording, page titles of 68 characters or fewer, stable feed ids (0065).
- Every commit, push and deploy needs Remington's approval.
- Vercel documents a host-scoped permanent redirect in `vercel.json` for sending a project's production `vercel.app` hostname to its custom domain, preserving path and query (https://vercel.com/docs/routing/redirects).
- Google:
  - recommends permanent redirects page by page, kept for at least 180 days (https://support.google.com/webmasters/answer/9370220);
  - doesn't follow cross-domain redirects for HTML verification files (https://support.google.com/webmasters/answer/9008080), so that one file is excluded from the redirect.

## 3. Risks and uncertainties
- **Search ranking:** a short dip is possible after an address change. Traffic is low now, so the cost is lowest.
- **Redirect rule:** the rule excludes the verification file using a path pattern. It was tested locally only, so it must be checked right after deploy 2, with rollback ready.
- **Old links:** they keep working while the Vercel project keeps its name. Before deploy 2 the old address serves the pages directly; after it, it redirects.
- **Name:** the domain avoids the phrase "Agent Trust", but the site name still contains it. No trademark search has been done.
- **Plan terms:** the Vercel Hobby plan is for non-commercial use, which the move doesn't change.

## 4. Decision
- **D1a:** primary host `https://www.agentclearinghouse.org`. The bare domain redirects to it (Vercel's recommended setup).
- **D2a:** switch `BASE` and every literal occurrence in public pages, README, CITATION.cff and the two check scripts, then regenerate.
  - LOG.md and the decision records keep the old address as history.
  - Feed item ids unchanged.
- **D3a (deploy 2):** a `vercel.json` redirect.
  - It only fires for the exact host `agent-trust-clearinghouse.vercel.app`.
  - It's permanent (308) and keeps path and query, except the Search Console verification file.
  - A check pins the rule.
- **D5a:** one changelog row stating that the directory has a new address and old links continue to work. No score or grade changes.
- **D7a:** deploy 1 (address switch, checked on both hosts), then deploy 2 (redirect, checked with curl).
  - Rollback target for deploy 1: `dpl_9uEJpHuMAozc8CfXNitrzBLHKhww`.
  - Rollback target for deploy 2: deploy 1.

## 5. Plain-English terms
- **Primary host:** the one address the site officially lives at. Other addresses forward to it.
- **308 redirect:** a permanent "this page now lives at the same path over there". Browsers and search engines follow it.
- **Canonical link:** a line in each page telling search engines which address is the original.
- **Feed item id:** the permanent label of each update, used by feed readers to avoid showing an update twice.

*Informational only. Scores and grades summarize cited public evidence under published rules; they are not a guarantee, endorsement or certification.*
