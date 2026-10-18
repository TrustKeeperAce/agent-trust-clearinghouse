# Decision 0046: Design and branding pass

**Status: APPROVED by Remington, 2026-10-17** (D1–D8 approved as drafted: blue-accent dark-first palette; four-bar logo and favicon; hero labels, counts line and disclaimer above the fold; thin single-colour score bars; light mode follows the visitor's system setting; content order unchanged; rollout as one commit; changelog row). Layout and labels only. No score, rule or content-text changes.

## Accessibility audit (before rollout)
- **Tool:** axe-core 4.10.2 via Playwright/Chromium. Tags: WCAG 2.0/2.1 A and AA, WCAG 2.2 AA, best-practice.
- **Pages:** index, openai-codex, autokaggle, methodology, changelog and 404, at 1280 and 375, dark and light. 24 runs on the design copy, repeated on the final repo public/.
- **Violations:** 0 in every run (critical 0, serious 0, moderate 0, minor 0).
  - Rules passed per run: index 39, openai-codex 40, autokaggle 34, methodology 37, changelog 34, 404 29.
- **Needs review:** axe could not compute colour-contrast for elements over the decorative radial background glow (index 31, openai-codex 112, autokaggle 40, methodology 56, changelog 12, 404 15 elements per run).
  - Re-run with the glow and card gradients flattened to their base colours: 0 violations and 0 needs-review in all 24 runs.
  - The peak glow colour was also checked by hand. Dark #1a2438: text 13.18, muted 6.96, links 8.46. Light #e2e7f5: text 14.67, muted 6.21, links 5.65. All are at least 4.5:1.
- **Fixes needed:** none. Lighthouse was not run; axe covers the same accessibility rule set.

## Rollout notes
- scripts/apply_design.py (added) applies the design markup to every page in public/. It is idempotent and refreshes the index hero counts. The per-entry build scripts call it after writing pages.
- Future index-row edits must handle score cells written as <span class="bar" style="--v:N">N</span>.
- Checks before commit:
  - check_scores: 0 errors, 6 approved warnings.
  - check_links: 39 internal links OK; outbound unchanged (two fellou.ai 503s, one os-world timeout, bot blocks and 429s).
  - Overflow: 152 checks (38 pages × 375/1280 × dark/light), 0 failures.
  - JSON-LD identical on all 38 pages. llms.txt, sitemap.xml and robots.txt unchanged versus d8dd312.
  - Visible text changed only on the index (hero labels and counts) and the changelog (the 0046 row).

---

The base is the current master public/ (commit de663ce, same content as the live dpl_AhBYbX2viDdCAY1EQvion3MPBUas).

## What changed (layout and labels only)
- **style.css (rewritten, 4.4 KB → 8.8 KB):**
  - Dark-first palette with a light mode via prefers-color-scheme.
  - Wider 1120 px layout, stronger type scale (h1 up to 3.4 rem, weight 780), and a soft radial glow behind the top of the page.
  - Card surfaces for the facts, the score panel and "How scores work".
  - Pill navigation with the current page marked.
  - Print stylesheet: black on white, navigation and buttons hidden, external URLs printed after links.
  - Reduced-motion rule kept. System fonts only.
- **Logo and favicon (new, original):**
  - The abstract mark is a rounded square holding four horizontal bars sized 30/20/25/25, the four factor weights. It is not a shield, seal, check, star or ribbon.
  - The wordmark is "Agent Reputation & Trust" over "CLEARINGHOUSE".
  - The header uses the mark inline (aria-hidden, CSS-coloured, so it follows light and dark mode) next to text. The brand is still real text.
  - favicon.svg (440 B) replaces the grey data-URI square. logo.svg (955 B) is a standalone asset for README and social use; no page references it yet.
  - theme-color meta tags are added for dark and light.
- **Index hero (labels and layout):**
  - New eyebrow "Informational directory".
  - The existing h1 and lede are unchanged.
  - The disclaimer "Informational only; not a guarantee, endorsement, or certification." is shown in a bordered notice above the fold. It is the same sentence as the footer.
  - Two links styled as buttons: "Browse scored entries" (#scored) and "Read the methodology".
  - A count line, "21 scored entries · 13 with insufficient evidence", computed from the table at build time.
  - The "How scores work" box now opens with weight bars (Completion 30%, Disputes 20%, Adherence 25%, Evidence 25%). These are aria-hidden; the existing text list is unchanged.
- **Score visual:**
  - Every overall score and factor score keeps its number as text, followed by a thin, single-colour horizontal bar whose length is the score out of 100.
  - On entry pages, the existing "Overall score…" line becomes a panel with a longer bar.
  - "Status: Insufficient evidence" gets the same panel with no bar.
  - "Citation check incomplete — recheck later." gets a yellow-edged note.
  - There is no colour coding by score (no red, amber or green), no rings, dials, stars or badges, and evidence grades stay plain text.
- **Entry template:** applied to all 34 entries and to the index, methodology, changelog and 404 pages by build_design_0046.py (rerun with rebuild.sh). Facts become cards: 4 columns at 900 px and wider, with Type double-width; they stack on mobile.
- **Unchanged (verified):**
  - All visible text on every page except the index hero and the brand split. No other page's text changed.
  - JSON-LD (including ItemList) on all 38 pages.
  - llms.txt, sitemap.xml and robots.txt (byte-identical).
  - URLs, scores, rules and disclaimers.
  - No JS, no external fonts, CDNs or trackers. The only page assets are /style.css and /favicon.svg.

## Checks
- **check_scores:** 0 errors, 6 warnings, the same approved set as before (the YAML is unchanged).
- **check_links (design copy):** 39 internal links all OK, favicon included. The outbound results match the live site: the two fellou.ai links returned 503, os-world.github.io timed out (it passes on other runs), and the rest are ACM/DOI bot blocks and GitHub 429s.
- **Overflow:** index, openai-codex, autokaggle, methodology, changelog and 404 all pass at 375 and 1280 pixels, dark and light: 0 failures in 24 checks.
- **Contrast (WCAG AA, computed from the palette):** all 28 pairs pass. Every pair and its requirement:

| Pair | Needed | Dark | Light |
|---|---|---|---|
| Body text on background / surface / raised | 4.5 | 16.53 / 15.43 / 13.95 | 16.93 / 18.15 / 16.45 |
| Muted text on background / surface / raised | 4.5 | 8.73 / 8.15 / 7.37 | 7.16 / 7.68 / 6.96 |
| Links on background / surface / raised | 4.5 | 10.61 / 9.91 / 8.96 | 6.52 / 6.99 / 6.34 |
| Bar fill on surface / raised | 3 | 6.75 / 6.11 | 5.90 / 5.35 |
| Bar fill on bar track | 3 | 4.60 | 4.57 |
| Focus ring on background | 3 | 13.85 | 5.37 |
| Primary button text | 4.5 | 7.24 | 5.90 |

## Rules and constraints applied
- Static HTML/CSS with no JS dependency; semantic HTML kept (tables, th scope, dl, skip link, focus ring, aria-current).
- Structured data, llms.txt, sitemap and robots are unchanged.
- No external requests.
- AA contrast. Works at 375 and 1280.
- Light mode is still available through prefers-color-scheme. Print-readable.
- The disclaimer is more prominent (above the fold on the index, footer kept on all pages).
- No certification-like visuals or wording.

## Risks
- **Seal-like visuals:** mitigated. The bars are flat lines, not circular. They have no score-based colour and no icons, and the logo avoids shield, check and seal shapes. The remaining risk is that a filled bar is read as quality; the number and grade stay alongside, and "Evidence grade describes the evidence, not the agent" stays.
- **Accessibility:**
  - The bars are decorative (CSS backgrounds or aria-hidden) and the numbers are always text.
  - The weight bars duplicate the list; they are aria-hidden to avoid repetition for screen readers.
  - Contrast was computed from the palette, not from an automated audit of rendered pages. An axe or Lighthouse pass before rollout is recommended.
- **Inline style="--v:N" attributes** are generated from the existing numbers, which adds one point of drift if the build is skipped. The plan is to fold this into the per-entry build scripts (D7).
- **The hero count line** is new derived text. It must be regenerated whenever entries change (it is built from the table).
- **Light-mode default:** browsers with no stated preference get light. A no-JS toggle is not possible without storing state.
- **CSS size** doubles to 8.8 KB, still small. color-mix is not used.

## Decisions requested
- **D1 Palette:** dark-first near-black (#0a0d12) with a single blue accent (#6f9bff dark, #2f5bd3 light) and amber only for focus and recheck notes. Alternative: a teal accent.
- **D2 Logo:** the four-bar mark (factor weights) plus the two-line wordmark, inline in the header, with favicon.svg. No shield, check or seal shapes.
- **D3 Hero copy:**
  - Approve the labels "Informational directory", "Browse scored entries" and "Read the methodology".
  - Approve the counts line.
  - Approve repeating the disclaimer sentence above the fold.
  - Alternative: drop the counts line.
- **D4 Score visual:** a thin single-colour linear bar next to the number (index, entry panel, factor table), with no score-based colours. Alternative: numbers only, with no bars.
- **D5 Light mode:** keep following the visitor's system setting (dark when they prefer dark, light otherwise). Alternative: force dark unless the visitor prefers light. Recommended: keep following the system setting.
- **D6 Entry layout:** fact cards, score panel and recheck note styling; content order unchanged. Option: move the score panel above the Summary. That is a layout-only change, but it reorders reading flow, so it is not done in this draft.
- **D7 Rollout:**
  1. Merge as one commit after approval: style.css, favicon.svg, logo.svg, and all 38 pages transformed by the build script.
  2. Update the per-entry build scripts to emit the new markup.
  3. Manifest plus files.json.
  4. You deploy.
  5. Post-deploy, check 200s and screenshots.
- **D8 Changelog/LOG:** a changelog row "Design refresh (layout and labels only; no score or rule changes)", plus a decisions/0046 record.

## Recommendation
Approve D1–D8 as drafted. D4 with bars, D5 following the system setting, D6 without reordering.

## Plain-English terms
- **Dark-first:** designed for dark backgrounds first, with a matching light version.
- **prefers-color-scheme:** the browser setting that says whether the visitor wants dark or light.
- **WCAG AA contrast:** a standard minimum difference between text and background (4.5:1 for normal text).
- **Favicon:** the small icon in the browser tab.
- **aria-hidden:** hidden from screen readers because the same information is already in text.
- **Static:** plain files, with no code running in the browser.

## Draft files (private, superseded)
- design-0046/assets/: style.css, logo.svg, favicon.svg
- design-0046/build_design_0046.py, rebuild.sh, public/ (built copy), before/ (copy of the current site)
- design-0046/screenshots/*.png
