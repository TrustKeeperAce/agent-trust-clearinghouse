# Decision 0014: Design v2 (directory order, mobile layout, semantics)

**Status: APPROVED by Remington, 2026-10-16, in full:** sorting with the directory-order rule (including "Order is not a recommendation."), stacked-card layout, design v2 including the "Source" label, ItemList JSON-LD and llms.txt. Applied to `public/` via build.py; the optional "Small differences are not meaningful." line was not part of the approval and was not added.

**Private preview:** `/workspace/private-drafts/design-v2-preview/site/`. It was built by `build.py` from a copy of `public/`.
- Screenshots are in `…/design-v2-preview/screenshots/`.
- Overflow test results are in `…/overflow-results.txt`.

## 1. What happened / current state (live, Decision 0013)
- **Directory order:** the directory is one table in the order entries were added (GPT Researcher, ODR, Perplexity, SAFE, then the 4 Insufficient entries mixed in after).
- **Narrow screens:** below 640px, tables scroll sideways, so on phones the score and grade columns can sit off-screen.
- **Nav:** the nav lacks Changelog.
- **Semantics:**
  - There are no `<main>` or `<header>` landmarks.
  - Tables have no captions and no `th scope`.
  - The entry facts line is a single `<p>` joined with "·" separators.
- **JSON-LD:** the index has only a `WebSite` block.
- **robots.txt:** it already allows all crawlers (`User-agent: *` / `Allow: /`) and points to the sitemap. Confirmed; no change needed.

## 2. Proposed changes (before → after)

### 2.1 Directory order (Part A1)
- **Before:** one table in insertion order.
- **After:** two static tables with no JavaScript:
  - **"Scored entries (highest overall score first)":** SAFE 66, OpenAI Deep Research 65, Perplexity 54, GPT Researcher 53.
  - **"Insufficient evidence (no overall score)":** Clay, Julius AI, Open Interpreter, Pactum, in alphabetical order.
- **Proposed rule (methodology / index note):**
  > Entries with an overall score are listed from highest to lowest overall score. Equal scores are listed alphabetically by entry name (case-insensitive). Entries labeled Insufficient evidence are listed separately, alphabetically. Order is not a recommendation.
- The evidence grade is deliberately **not** used as a tie-break, so that order never looks like a combined ranking.

### 2.2 No horizontal scroll (Part A2)
- **Before:** tables scroll sideways under 640px.
- **After:** under 640px every data table (directory, factor breakdown, changelog, methodology) stacks into cards. Each field is labelled by its column header (Agent, Category, Overall score, Evidence grade, Last reviewed; or Factor, Weight, Score, Note).
- The stacking is pure CSS using `data-label`. The HTML stays a real table for screen readers.
- **Test:**
  - Tool: headless google-chrome, with each page loaded in a fixed-width iframe because headless windows can't be narrower than 500px.
  - Coverage: all 12 pages × 360/390/768/1280px × dark/light. The `prefers-color-scheme` result was checked and matched the intended mode in every run.
  - Result: **`scrollWidth` ≤ viewport on every page, at every width, in both modes; 0 overflows.**

### 2.3 Visual refinements
| Role | Dark | Ratio vs bg / surface / raised | Light | Ratio vs bg / surface / raised |
|---|---|---|---|---|
| Base background | `#0E1116` | — | `#FAFBFC` | — |
| Surface (cards, tables) | `#151A21` | — | `#FFFFFF` | — |
| Raised (table header) | `#1B222B` | — | `#F3F5F8` | — |
| Text (off-white / near-black) | `#ECEFF3` | 16.4 / 15.2 / 13.9 | `#161A1F` | 16.9 / 17.5 / 16.0 |
| Muted | `#A3ADB9` | 8.3 / 7.7 / 7.1 | `#4A5462` | 7.4 / 7.7 / 7.0 |
| Links | `#8AC2FF` | 10.1 / 9.4 / 8.6 | `#0B57B0` | 6.8 / 7.0 / 6.4 |
| Focus ring | `#FFD479` | 13.5 / 12.4 / 11.4 | `#A34E00` | 5.6 / 5.8 / 5.3 |
| Hairline borders (decorative) | `#2B333D` | 1.5 | `#D5DBE2` | 1.4 |

- **Contrast:** all text is AAA (≥7:1) except light-mode links at 6.4–7.0, which are AA. Focus rings are ≥3:1 everywhere.
- **Depth:** created with a 1px hairline plus a very soft shadow (`0 1px 2px` + `0 8px 24px`, low alpha), not with gradients or glow.
- **Typography:**
  - Same system font stack as now.
  - h1 `clamp(1.75rem, 2.4vw + 1.1rem, 2.6rem)` at weight 700 with −0.025em letter-spacing.
  - h2 1.2rem at weight 650.
  - Labels 0.75rem, uppercase, +0.08em letter-spacing.
  - Body 1rem with line-height 1.65.
  - Text capped at 72ch.
  - Tabular numbers in tables.
- **Spacing scale:** 4, 8, 12, 16, 24, 32, 48 and 64px. Max width 1000px.
- **Header:** the site name on the left and a nav with Directory · Methodology · **Changelog** on the right. It wraps on mobile.
- **Hero (index):** the existing h1 and the existing one-line description, now in the muted colour. No new claims.
- **"How scores work" strip:** a card with three neutral facts copied from the methodology page, plus a "Read the methodology" link:
  > Four factors, shown separately: completion 30%, disputes 20%, adherence 25%, evidence 25%. · Fewer than 3 independent performance sources: no overall score. · Evidence grade describes the evidence, not the agent.
- **Cards and tables:** they share one card style (surface colour, 12px radius, hairline, soft shadow).
- **Scores:** plain semibold numbers, with no colour coding, bars, stars, badges, seals or checkmarks. Grades are plain text.

### 2.4 Semantic HTML (agent- and assistive-tech-friendly)
- **Landmarks:** `<header>`, `<nav aria-label="Primary">`, `<main>` and `<footer>` on every page.
- **Tables:**
  - Each table has a visually hidden `<caption>`.
  - Column headers use `th scope="col"`.
  - The first cell of each row is `th scope="row"` (agent name, or factor name).
  - Dates are wrapped in `<time datetime>`.
- **Entry facts:** the "·"-separated line becomes a `<dl>` with Category / Type / Scope / Source / Last reviewed.
  - All existing values are unchanged.
  - The only new visible word is the label **"Source"** for the existing vendor or project link. It needs approval, or I can drop the label and keep just the link.

### 2.5 Structured data
- **Index:** keep `WebSite` and add an `ItemList` of the 8 entries in display order, with `name` and `url` only.
- **No `Rating`, `AggregateRating` or `Review` markup.** Search engines can render those as star ratings or review snippets. That would imply an endorsement or a consumer rating, would misstate a 0–100 multi-factor score as a single "rating", and would be easy to misread for Insufficient entries. Google's review-snippet policies also restrict self-serving or editorial review markup.
- **Entry pages:** no new JSON-LD, which is the conservative choice. `WebPage` adds nothing beyond the existing meta tags. `Dataset` would overstate what a page is.

### 2.6 llms.txt (optional, low effort)
- A plain-text `/llms.txt` with:
  - a one-paragraph site summary, the standard disclaimer and the scoring basics;
  - links to Directory, Methodology and Changelog;
  - a list of entries, each with its overall score and grade or "Insufficient evidence";
  - the corrections address.
- **Risk:** low. It is an informal convention that crawlers may ignore. It must be updated in the same commit whenever scores change; add it to the publishing checklist.
- **Recommendation:** approve, but leave it out of the sitemap.

### 2.7 Performance
- **No JavaScript.** The only `<script>` tag is the inert JSON-LD block.
- **No webfonts or images.**
- **CSS** is about 4.2 KB uncompressed (about 1.3 KB gzipped). The target is under 6 KB.

## 3. Content unchanged
- **Checked:** for all 8 entry pages, the visible text from Summary through Sources is identical word for word to `public/`. The only addition is the hidden table caption, which is read by screen readers only.
- **Unchanged:** all scores (66/65/54/53), grades (B-/B/B/B-), statuses, summaries, disclaimers, last-reviewed dates, methodology wording and footer text.
- **New visible text:**
  - the two table headings on the index;
  - the "How scores work" strip (restated from the methodology);
  - the "Source" label;
  - the "Changelog" link in the nav;
  - the site name in the header.

## 4. Risks / uncertainties
- **Neutrality:** a polished look and a "highest first" sort can look like an endorsement ranking. Mitigation: the "Order is not a recommendation" note, no colour or badges, and disclaimers unchanged. Reject the sort if this is a concern; alphabetical order is the alternative.
- **Score precision:** the sort can suggest precision. SAFE (66) and ODR (65) differ by 1 point, which is within judgment-call noise. Consider adding to the index note: "Small differences are not meaningful."
- **Statistic check ("73% judge credibility by design"):**
  - **I could not verify it, so do not use it.** No credible source for "73%" was found.
  - The closest primary source is Fogg et al., *How Do People Evaluate a Web Site's Credibility?* (Stanford Persuasive Technology Lab / Consumer WebWatch, 2002). There, 46.1% of 2,440 comments mentioned "design look" and 28.5% mentioned information design. The commonly quoted "75%" is a secondary sum of those two numbers, not a Stanford finding. The study is also from 2002.
  - Nothing should go on the site.
- **Testing limits:** headless Chrome only, and narrow widths were emulated with an iframe. Safari/iOS, Firefox and real screen readers have not been tested.
- **Upkeep:** `build.py` rewrites the HTML; adopting v2 means updating the publishing steps (index order, ItemList and llms.txt must change together).

## 5. Recommendation
**APPROVE** items 2.1–2.7, including the tie-break rule, the "Order is not a recommendation" note (plus, optionally, "Small differences are not meaningful.") and the "Source" label.
- **Before deploy:** re-run the overflow and contrast checks and do a manual keyboard pass.
- **Alternatives:** **MORE INFO** if you want an alphabetical-only directory, or llms.txt dropped.

## 6. Plain-English terms
- **Tie-break:** how to order entries with equal scores.
- **Stacked cards:** on phones, each table row becomes a small box with labelled lines.
- **scrollWidth:** the full width of a page. If it is larger than the screen, the page scrolls sideways.
- **Landmarks:** labelled page regions (header, nav, main, footer) that screen readers can jump between.
- **JSON-LD ItemList:** machine-readable list of the entries (names and links only).
- **Rating markup:** structured data that can make search results show stars. Deliberately not used.
- **llms.txt:** a plain-text summary file some AI tools read.
