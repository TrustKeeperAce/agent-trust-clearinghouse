# Decision 0012: SEO basics

**Status: APPROVED by Remington, 2026-10-16.** Applied to `public/`. No score, grade, status, summary or visible wording changed, and `style.css` was not touched.

## What happened
Remington approved basic search-engine setup for https://agent-trust-clearinghouse.vercel.app.

## What was added
- `sitemap.xml` lists all 11 public pages with lastmod 2026-10-16. The 404 page is excluded.
- `robots.txt` allows all crawlers and points to the sitemap.
- Each page (except 404) has a canonical link to its absolute URL.
- Each page (except 404) has Open Graph and Twitter text tags (title, description, url, type, site name; card "summary"). There is no image.
- Every page has an inline SVG favicon: a plain slate square, with no checkmark, seal or badge.
- The index has a JSON-LD `WebSite` block (`application/ld+json`). It is data only and does not run.
- `404.html` uses the existing styles and the standard footer and is marked `noindex`.
- All pages already had `lang="en"` and a viewport tag.

## Checks
- The sitemap is valid XML.
- All internal links resolve.
- All 12 HTML pages have unique titles and descriptions.
- No scripts run: the JSON-LD block is the only script tag.
- There are no analytics or tracking.

## Risks
- Indexing timing is not controlled by us.
- The vercel.app domain cannot be verified with a DNS record in Search Console (see the private notes).

## Plain-English terms
- **Sitemap:** a list of pages for search engines.
- **Canonical link:** tells search engines which URL is the official one.
- **Open Graph:** the text shown when a link is shared.
- **JSON-LD:** a machine-readable description of the site.
