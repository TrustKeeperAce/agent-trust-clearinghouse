# Decision 0102: freeze the directory (no longer actively maintained) and serve it on agent-trust-clearinghouse.vercel.app

**Status: APPROVED by Remington, 2026-10-29 (12:42 PM ET, t284u).** The user decided to freeze the Clearinghouse and explicitly approved preparing and executing the freeze, including commit, push and production deploy of this change only. The unapproved 0101 rewording is not included.

## Background
- Namecheap canceled the order for agentclearinghouse.org and the domain was deleted (registry lookup 404 since 24 October 2026). It is not being restored.
- Since decision 0086, vercel.json redirected every path on agent-trust-clearinghouse.vercel.app (except the Search Console verification file) with a 308 to https://www.agentclearinghouse.org/, so the site was unreachable.
- The Vercel project's domain settings were checked: agent-trust-clearinghouse.vercel.app has no redirect configured there. The redirect came only from vercel.json.

## Decisions
- **D1:** remove the `redirects` block from vercel.json (the 0086 old-host redirect). The check in scripts/check_export.py now requires that vercel.json has no redirects. No domain is added or bought, and the project domain settings are unchanged.
- **D2:** add this notice at the top of every HTML page (all pages except the Search Console verification file):
  > This directory is no longer actively maintained. Information may be out of date. Scores were informational only and are not guarantees or endorsements.

  It is added by the build (scripts/apply_design.py), not by hand-editing outputs. The comparison and citing pages inherit it from the shared page shell. A plain style rule `.frozen-notice` is added to public/style.css.
- **D3:** one site-change changelog row and feed item, 2026-10-29-0102, saying the directory is frozen and no longer maintained. The "Data as of" date moves to 2026-10-29 because the build sets it automatically from the newest changelog row.
- **D4:** canonical tags, og:url, the sitemap, llms files and feed URLs still name https://www.agentclearinghouse.org. This is a known limitation: those URLs no longer resolve. They were left unchanged because the user asked for minimal upkeep.

No score, grade, source record, source count, entry content or last-reviewed date changes. agents.json entries are identical; only its dataset date fields change.

Rollback target: dpl_Am8LdYouhJ82DCGMmNJ4TTUAhusV (0099).
