# Decision 0060: Traffic and traction measurement

**Status: APPROVED by Remington, 2026-10-18**, as recommended: D1a Google Search Console URL-prefix property verified by HTML file; D2a sitemap submitted; D3a no analytics script — Vercel built-in request statistics only (incl. AI-crawler totals); D4 monthly review on the 15th, aggregate totals only; D5 privacy-and-measurement section on methodology.html plus footer link; D6 no selling, no individual tracking, no ad tech; D7 traffic never used in scores or grades.


**Status:** proposal. Nothing has been implemented, deployed, connected, or signed up for. Every D-item needs approval before any change.

## Plain-English terms
- **Search Console:** Google's free tool for site owners. It reports how the site appears in Google Search (searches, clicks, which pages are indexed). It doesn't count visits from other sources.
- **Property:** Search Console's word for "the site you're tracking".
  - **URL-prefix property:** one exact address start, e.g. `https://agent-trust-clearinghouse.vercel.app/`.
  - **Domain property:** a whole domain and all its subdomains. Needs a DNS record.
- **Public suffix:** a domain under which strangers can each get their own site, like `.com` or `vercel.app`. Google won't verify domain properties on these.
- **Web analytics script:** a small piece of JavaScript in each page that reports a page view to an analytics service when someone loads the page.
- **Cookieless:** the visitor's browser stores nothing. Visitors are counted, roughly, from a short-lived hash of request details.
- **Log-based / no-JS counting:** visits are counted from the server's own request records, or from a tiny image request, not from a script.
- **Bot / AI crawler:** an automated program (search engine, AI company crawler) that fetches pages. Script-based analytics mostly don't see them, because they usually don't run JavaScript. Log-based counting does see them.
- **Aggregate counts:** totals such as "1,200 page views in September" or "top 10 pages". Nothing tied to a person.

## 1. What happened (facts, checked 2026-10-18 ET)

### Current site state (checked in the repo and on the live site)
- Static HTML in `public/`. vercel.json is `{ "outputDirectory": "public", "cleanUrls": false }`. No framework (Vercel `framework: null`).
- **No JavaScript.** The only `<script>` on the site is one `application/ld+json` structured-data block in index.html, which is data, not code. Every other page has no script at all.
- robots.txt allows all crawlers and points to `https://agent-trust-clearinghouse.vercel.app/sitemap.xml`. The sitemap exists and is live.
- `/_vercel/insights/script.js` currently returns 404, so Vercel Web Analytics is not enabled.
- **Vercel project** (read-only MCP `get_project`): prj_KR8IoAh8W9rZK1HoTlSuGkI2rqtE, team "TrustKeeper" (trust-keeper).
  - Domains: agent-trust-clearinghouse.vercel.app and agent-trust-clearinghouse-trust-keeper.vercel.app.
  - No custom domain. Deployment protection is on for all deployments except custom domains.
  - **Plan tier not shown** by the MCP team read (`get_team` returned only name, slug and id). Treated below as **unverified, probably Hobby**; please confirm in the Vercel dashboard under Settings → Billing.
- `vercel.app` is on the Public Suffix List (entries `vercel.app` and `vercel.dev` under "Vercel, Inc"): https://publicsuffix.org/list/public_suffix_list.dat

### Google Search Console
- **Property types:** https://support.google.com/webmasters/answer/34592
  - URL-prefix: "Many possible methods" of verification.
  - Domain: "DNS record verification only". Google also says: "We don't support domain-property verification of public suffixes."
  - **So a domain property is not available for `*.vercel.app`.** We don't control its DNS, and it is a public suffix. A **URL-prefix property for `https://agent-trust-clearinghouse.vercel.app/` is the only option** until there's a custom domain.
- **Verification:** https://support.google.com/webmasters/answer/9008080
  - **HTML file upload:** a Google-issued file at the site root, served without login. Redirects aren't followed. The file is tied to one Google account. Removing it loses verification.
  - **HTML meta tag:** `<meta name="google-site-verification" ...>` in the home page `<head>`. Tied to one Google account. Google checks for it periodically.
  - Google Analytics and Tag Manager methods exist, but both need Google's tracking scripts. Not suitable here.
  - Multiple owners can verify, each with their own token.
  - "Data is collected for a property as soon as anyone adds it in Search Console, even before verification."
- **What it measures:** Google Search performance (queries, impressions, clicks, average position), index coverage and page indexing, sitemap processing, and crawl issues. It does **not** report visitors from other sources (direct, links, AI tools).
- **Sitemap submission:** possible from the Sitemaps report once the property is verified. The robots.txt `Sitemap:` line already advertises it.
- **Owner and access:**
  - The verifying Google account becomes the verified owner.
  - Other people can be added as owners or users (Search Console Settings → Users and permissions). Users can be given full or restricted access without their own verification token.
  - If all verified owners lose access, everyone loses the property, so a second verified owner or a backup method is advisable.
- **Owner account: TBD (D2).** Options are Remington's personal Google account, or a project account such as the existing trustkeeperace@gmail.com mailbox used for corrections.

### Analytics options
| Option | Cookies | JS added | Cost / plan | Account needed | Data location / GDPR stance (vendor's own claims) | Counts bots / AI crawlers? | Sources |
|---|---|---|---|---|---|---|---|
| **Vercel Web Analytics** | None (no third-party cookies). Visitors identified by "a hash created from the incoming request", discarded after 24 h | Yes: a small inline queue snippet plus `<script defer src="/<unique-path>/script.js">`, served first-party from the same site. The HTML method doesn't need the npm package. Exact size not measured (not enabled) | **Hobby:** 50,000 events/month free, 1-month reporting window; collection pauses at the limit (3-day grace, then stops), never billed. **Pro:** $0.03 per 1K events, 12-month window; Web Analytics Plus $10/month for 24 months | None new (already on Vercel). Enable in the dashboard | Says it collects no personal identifiers and only aggregated data. Data stored per event: timestamp, URL, referrer, filtered query parameters, country/region/city, OS, browser, device type | Mostly no: needs JS execution, and most crawlers don't run it | https://vercel.com/docs/analytics/limits-and-pricing · https://vercel.com/docs/analytics/privacy-policy · https://vercel.com/docs/analytics/quickstart |
| **Plausible Cloud** | None ("No cookies, no persistent identifiers") | Yes, third-party script ("54 times smaller than Google Analytics") | From about $9/month (Starter, 10K pageviews), per the home-page pricing block. 30-day trial | New Plausible account | EU-hosted ("never leaves the EU"). Says no consent banner needed | Filters bots. Separately reports **visits referred by AI tools** (ChatGPT, Perplexity, Claude) | https://plausible.io/ · https://plausible.io/self-hosted-web-analytics |
| **Plausible CE (self-hosted)** | None | Yes (self-served) | Free software (AGPLv3), but needs a server to run and maintain (backups, upgrades, security) | Server or hosting account | Wherever we host it | Basic user-agent filtering only | https://plausible.io/self-hosted-web-analytics |
| **GoatCounter** | None; stores aggregates, not raw IPs or user agents | ~3.5 KB script, **or a no-JS image "pixel"**, or log-file import | Free hosted "for reasonable public usage" (donation-supported); self-host possible | New GoatCounter account | Says a GDPR notice probably isn't needed, with caveats ("I am not a lawyer") | Script/pixel: mostly humans. Log import: would see crawlers | https://www.goatcounter.com/ · https://www.goatcounter.com/help/gdpr |
| **Cloudflare Web Analytics** | Says it doesn't collect or use visitors' personal data | Yes, third-party JS "beacon" (Performance API); no DNS change needed | Free | New Cloudflare account | Personal-data claim as stated; retention and data location not checked here | Mostly no (JS) | https://developers.cloudflare.com/web-analytics/about/ |
| **Umami Cloud** | None ("does not use cookies") | Yes, third-party script | Hobby tier: 100K events/month, 1 site, 6-month retention (price shown as a tier, not confirmed on the page as $0). Pro has 1M events and 2-year retention | New Umami account | US and EU servers. Says GDPR/CCPA compliant, no banner needed | Mostly no (JS) | https://umami.is/pricing |
| **No-JS: Vercel Observability (built in)** | None | **None** | Observability is "available on all plans" with limits. It shows CDN Requests and lists an **"AI Traffic"** data source. Exact Hobby retention and metrics not confirmed | None new | Vercel's own request data | **Yes:** request-level, so it includes crawlers and AI bots | https://vercel.com/docs/observability |
| **No-JS: Vercel Drains** (send request logs to our own endpoint) | None | None | **Pro/Enterprise only**; $0.50 per GB. Static logs included as a data type | Pro plan plus a destination service | Wherever the destination is. Logs include IPs unless hidden ("hiding IP addresses" option) | Yes | https://vercel.com/docs/drains |
| **No-JS: GoatCounter pixel** | None | None (an `<img>` tag) | Free hosted | GoatCounter account | As above | Mostly humans (image requests from browsers) | https://www.goatcounter.com/ |

## 2. What the rules say
- The site is **informational only**: no guarantees, endorsements or certifications. Any traffic figures we publish or quote must not suggest more accuracy than the tools give.
- **Changes need Remington's approval** in the standard packet flow. I never deploy; the user deploys.
- **Prefer public, verifiable sources.** That applies to how we describe our own measurement too: the privacy notice should link to each tool's own privacy documentation.
- **Agent-friendliness** is a design goal: no JS, plain HTML, llms.txt, structured data. Adding any script changes that baseline and must be disclosed.
- **Neutral wording, and no score effects:** traffic data never feeds into agent scores or grades.

## 3. Review process (proposed)
- **Who sees the data:** Remington (account owner) and me as operator, through read access only. No public dashboard unless a later decision allows one.
- **Cadence:** fold it into the existing monthly improvement review on the 15th. Each month, add one aggregate line to LOG.md or the monthly report:
  - page views;
  - visitors (if the tool provides them);
  - top 5–10 pages;
  - top referrers (domains only);
  - Search Console clicks, impressions and indexed-page count;
  - AI-crawler request totals (if a log-based source is used).
- **What gets logged:** aggregate counts only. No IPs, no full user-agent strings, no individual sessions, no query strings beyond known-safe ones.
- **What is never done:**
  - no selling or sharing of data;
  - no individual tracking or fingerprinting;
  - no ad tech, retargeting or Google Analytics/Tag Manager;
  - no cross-site identifiers;
  - no session replays or heatmaps (some tools offer these; keep them off);
  - no use of traffic in scoring.

## 4. Connector, account and config steps for each option
| Option | Steps (all after approval; none done) |
|---|---|
| Search Console (URL-prefix) | 1. Owner signs in to Search Console with the chosen Google account (D2) and adds the URL-prefix property `https://agent-trust-clearinghouse.vercel.app/`.<br>2. Chooses the HTML file (recommended: a separate `google<token>.html` in `public/`, no change to page HTML) or the meta tag (one line in index.html `<head>`).<br>3. I add the file or tag in a packet commit; the user deploys.<br>4. Owner clicks Verify, submits `sitemap.xml`, and adds me or a backup owner under Users and permissions if wanted.<br>5. Optional: connect a Search Console connector for reporting later (needs its own approval) |
| Vercel Web Analytics | 1. Enable it in Vercel → project → Analytics (dashboard; owner).<br>2. Add the inline snippet and script tag (with the unique path Vercel shows) to every HTML page via apply_design.py.<br>3. Deploy (user).<br>4. Read monthly totals in the dashboard, or through the read-only Vercel MCP web-analytics tools if available.<br>5. Confirm the plan tier: Hobby pauses at 50K events and keeps 1 month of data, so monthly logging matters |
| Plausible / Umami / Cloudflare / GoatCounter (hosted) | New vendor account (owner) → add the site → copy the script tag (or the GoatCounter pixel) into the pages → deploy → read the dashboard. Each is a new third party processing visitor requests, to be named in the privacy notice |
| Vercel Observability (no-JS) | Nothing to install. Owner or operator opens Observability → CDN Requests / AI Traffic monthly and records the totals. Check what Hobby retains first |
| Vercel Drains | Upgrade to Pro → create a drain to a destination we control → set IP hiding → aggregate. Not recommended now |

## 5. Risks and mitigations
| Risk | Mitigation |
|---|---|
| **Privacy:** even cookieless tools process IPs transiently and store coarse location and device | Choose cookieless, aggregate-only tools; don't enable custom events with personal data; publish a privacy notice (draft below); log aggregates only |
| **Liability / public statement:** the site currently makes no privacy statement, and adding measurement without one would be inconsistent with its transparency | Add a short "Privacy and measurement" section to methodology.html **in the same release** as any measurement, and link it from the footer |
| **Agent readability:** a script adds bytes and a request to every page and breaks the "no JS" property. Agents that execute JS also get counted as visitors | Prefer no-JS or verification-file options first. If a script is added: one small, `defer`, first-party script, never required for content. Note it in llms.txt or methodology |
| **Performance:** extra request per page view | Same as above (defer, small). Recheck overflow and axe after the change; optionally compare page weight before and after |
| **Data accuracy:** script tools miss visitors with JS or ad blockers and most bots; log tools over-count bots; Search Console only covers Google Search, and its numbers are sampled or delayed | Never present traffic numbers as exact or as evidence of quality. Use labels like "about", with the tool name and date range. Don't publish traffic claims on the site without a separate decision |
| **Vendor lock-in / limits:** Hobby Web Analytics pauses at 50K events and keeps only 1 month | Log monthly totals in LOG.md so the history doesn't depend on vendor retention |
| **Account ownership:** a single Google owner who loses access means everyone loses the Search Console property | Two verified owners, or file plus meta-tag methods; record the owner account in LOG.md (no credentials) |
| **Scope creep:** heatmaps, replays, A/B tests | Out of scope; a new packet would be needed |

### Privacy-notice wording draft (for methodology.html, new section "Privacy and measurement")
> **Privacy and measurement.** This site does not use cookies, advertising, or cross-site tracking, and it does not sell or share visitor data. To understand whether the Clearinghouse is useful, we look at aggregate counts only: how many times pages are viewed, which pages and referring websites are most common, and how the site appears in Google Search (via Google Search Console). [If Vercel Web Analytics is enabled: Page views are counted with Vercel Web Analytics, which does not use cookies and does not store information that identifies individual visitors; see Vercel's privacy documentation.] We record only monthly totals. We never use traffic figures in agent scores or grades, and traffic numbers are approximate. Questions: trustkeeperace@gmail.com.

(Bracketed text depends on D3. Each tool named gets a link to its privacy page.)

## 6. Recommendation
- **Minimal viable setup (recommended):**
  1. **Search Console URL-prefix property, verified with the HTML file method.** One new static file; page HTML untouched; no JS. Then submit the sitemap.
  2. **Vercel Observability (built in, no JS)** for monthly request totals and AI-crawler traffic, after confirming what the current plan shows and keeps.
  3. **Privacy and measurement section** on methodology.html, published in the same release.
  4. **Monthly aggregate line** in LOG.md on the 15th.
  - Result: no JavaScript, no new third-party processor beyond Google Search Console, and both search and crawler visibility.
- **Next step if human visitor counts are wanted (D3):** Vercel Web Analytics. It is first-party, cookieless, free on Hobby within 50K events, and needs no new account. It does add a small script to every page, so it needs explicit approval of that trade-off.
- **Fuller options (not recommended now):** Plausible Cloud (best AI-referral reporting and bot filtering, about $9/month, EU-hosted), Umami or Cloudflare (free tiers, third-party scripts), GoatCounter pixel (no-JS, free, new account), Vercel Drains (Pro only).

## 7. D-items (each needs approval before implementation)
- **D1. Search Console**
  - **D1a (recommended):** URL-prefix property for `https://agent-trust-clearinghouse.vercel.app/`, HTML-file verification, sitemap submitted.
  - D1b: meta-tag verification instead (one line in index.html).
  - D1c: no Search Console.
- **D2. Search Console owner account**
  - **D2a (recommended):** Remington's chosen Google account as owner, with the project mailbox (trustkeeperace@gmail.com) as a second owner or user.
  - D2b: project mailbox only.
  - D2c: Remington only.
  - Remington signs in and verifies himself; I don't create or sign in to Google accounts.
- **D3. Visitor analytics**
  - **D3a (recommended for now):** none. Use Search Console plus Vercel Observability only (no JS).
  - D3b: Vercel Web Analytics (adds a first-party script; Hobby limits as above).
  - D3c: GoatCounter no-JS pixel (new account).
  - D3d: Plausible Cloud (paid, new account).
  - D3e: Cloudflare or Umami.
- **D4. Privacy notice:** approve the wording above, edited to match D1–D3, for methodology.html, plus a footer link. Required if any of D1, D3b–e is approved.
- **D5. Review process:** approve the monthly aggregate line on the 15th, read access for operator and owner, and the "never" list. Alternative: quarterly cadence.
- **D6. Crawler and AI-traffic reporting:** include AI-crawler totals from Vercel Observability in the monthly line (recommended), or leave them out.
- **D7. Rollout:**
  1. One packet commit (verification file, privacy section, footer link; plus a script only if D3b–e).
  2. Checks: check_scores, check_links, overflow and axe, plus a no-JS check unless D3b–e.
  3. Manifest; you deploy; then Remington verifies in Search Console.
  4. LOG note.

## Uncertainties
- Vercel plan tier not confirmed (the MCP team read didn't show it). Hobby versus Pro changes Web Analytics retention and Drains availability.
- What Vercel Observability shows and keeps on this plan (CDN Requests, AI Traffic) wasn't confirmed against the dashboard.
- Script sizes for Vercel, Cloudflare and Umami weren't measured. Plausible's size is a relative claim only.
- Vendor GDPR and "no banner needed" statements are the vendors' own. They aren't legal advice, and no lawyer has reviewed them.
- Plausible's monthly price comes from its home-page pricing block (the /pricing URL returned 404 on fetch).
- I haven't confirmed that the monthly improvement review on the 15th exists in the repo; it's taken from your instruction.
