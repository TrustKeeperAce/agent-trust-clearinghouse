# Decision 0013: Visual design refresh

**Status: APPROVED by Remington, 2026-10-16, with option (a): dark theme by default, automatic light theme.** Applied as previewed to `public/style.css` only; no HTML changes. Preview screenshots remain private.

## 1. What happened / current state
- `public/style.css` is 4 lines: a system font, `#222` text on white, grey `#ccc` table borders, a `#f3f3f3` table header, and a light theme only.
- It is readable and accessible. It looks unstyled, has no visible focus style beyond the browser default, and has no dark mode.
- The site has no JavaScript (only an inert JSON-LD block), no webfonts and no images.

## 2. Proposal: one new `style.css`, with no HTML changes
- **Theme:** dark by default (the "dark-mode vibe"). It switches automatically to a light palette when the user's system prefers light (`prefers-color-scheme: light`). `color-scheme: dark light` makes form controls and scrollbars match.
- **No JavaScript and no theme toggle.** The visitor's operating-system setting decides.

### Palette (WCAG contrast measured against the page background / table surface)
| Role | Dark | Ratio (bg / surface) | Light | Ratio (bg / surface) |
|---|---|---|---|---|
| Background | `#0E1116` | — | `#FFFFFF` | — |
| Surface (tables) | `#161B22` | — | `#F5F7FA` | — |
| Text | `#E6EDF3` | 16.0 / 14.6 (AAA) | `#1B1F24` | 16.6 / 15.4 (AAA) |
| Muted text (meta, footer, table headers) | `#9DA7B3` | 7.8 / 7.1 (AAA) | `#4B5563` | 7.6 / 7.0 (AAA) |
| Links | `#79B8FF` | 9.1 / 8.3 (AAA) | `#0A58B8` | 6.8 / 6.3 (AA, near AAA) |
| Reserved accent (headings only, optional) | `#C9A6FF` | 9.4 / 8.6 | `#6B3FB5` | 7.0 / 6.5 |
| Focus ring | `#FFD479` | 13.5 / 12.3 (≥3:1 non-text) | `#B35900` | 4.8 / 4.5 (≥3:1 non-text) |
| Borders (decorative) | `#30363D` | 1.6 | `#D0D7DE` | 1.5 |

- Borders are decorative only. Table meaning never depends on borders, and links are always underlined, so links never rely on colour alone.
- **Deliberately no green, gold seals, badges, checkmarks, shields or "verified" styling.** Scores and grades use plain text in the normal text colour. Grades are not colour-coded, so no grade looks like a pass or fail. The favicon stays a plain slate square.

### Typography
- System font stack: `ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`.
  - Why: zero download, instant render, native look, no third-party font requests (privacy), and good hinting on every platform. A webfont would add 20–100 KB and a layout shift for little gain.
- **Sizes:**
  - Body 16px with line-height 1.6.
  - h1 `clamp(1.75rem, 3vw + 1rem, 2.5rem)`, with tight -0.02em letter-spacing.
  - h2 1.25rem.
  - Table headers 0.8125rem, uppercase, letter-spacing 0.06em, muted colour.
  - Footer 0.875rem.
- Text lines are capped at 70ch for readability.
- `font-variant-numeric: tabular-nums` on tables, so score columns line up.

### Layout and spacing
- Spacing scale: 4, 8, 12, 16, 24, 32 and 48px (`--s1` to `--s7`).
- Max content width is 960px with 24px gutters (16px on mobile).
- The nav is a row with 24px gaps and a bottom hairline. h2 gets 48px of space above it.

### Tables
- Tables sit on the surface colour inside one 10px rounded border, with row separators only and 12×16px cell padding.
- Below 640px wide, tables scroll horizontally instead of squashing.

### Score display
- The score column is semibold. "Overall score: NN" stays as text at 1.125rem.
- No bars, gauges, stars or colours. Bars would imply precision and gauges would imply a rating or certification.

### Focus and motion
- `:focus-visible` gives a 3px outline with a 3px offset in the focus colour, on every link.
- Hover thickens the link underline.
- `prefers-reduced-motion` is respected; there are no animations anyway.

## 3. Before → after (per element)
| Element | Before | After |
|---|---|---|
| Page | White, `#222` text | Near-black `#0E1116` with soft white text; white with `#1B1F24` text on light-preference systems |
| Nav | Plain inline links | Semibold row with a hairline divider |
| h1 | Browser default | Large and tight, with a muted subtitle line |
| Entry meta line | Plain text | Muted colour |
| Tables | Grey grid on white | Rounded card on the surface colour, row lines only, small-caps-style headers, tabular numbers |
| Score / grade | Plain text | Same text, semibold; no colour coding |
| Links | Browser blue | Brand blue with offset underline, thicker on hover, visible focus ring |
| Footer | Grey, small | Muted, hairline above, more top spacing; disclaimer text unchanged |
| 404 / changelog / methodology | Same base | Inherit the same styles; no per-page CSS |

## 4. Risks / uncertainties
- **Dark by default:** some visitors on light-preference systems get the light theme automatically. Visitors with no stated preference get dark, which a few may find harder for long reading. Mitigation: light is one OS setting away. The alternative is to default to light and offer dark only under `prefers-color-scheme: dark` (one-line swap).
- **Perception:** a "premium" look could be read as more authoritative than the evidence supports. Mitigation: no badges, seals, colour-coded grades or green, and disclaimers stay in place.
- **Testing limits:** contrast was computed with the WCAG formula, and the preview was checked in headless Chrome only. It has not been tested on Safari, Firefox, Windows High Contrast or with a screen reader. The HTML is unchanged, so semantics and screen-reader output are unaffected.
- **Speed:** the CSS is about 2 KB, with no fonts or images. Speed impact is negligible.

## 5. Recommendation
**APPROVE**, with a choice between:
- **(a)** dark default, as previewed; or
- **(b)** light default with automatic dark.

I recommend **(a)**, which matches the brief. The change is CSS only, so scores, wording and HTML are untouched. Before deploy: re-run the contrast check and a quick manual keyboard-focus check.

## 6. Plain-English terms
- **WCAG AA / AAA:** accessibility standards. Text needs a contrast ratio of at least 4.5:1 (AA) or 7:1 (AAA) against its background.
- **prefers-color-scheme:** the visitor's system light/dark setting, which the browser shares with the page.
- **Focus ring:** the outline showing which link is selected when using a keyboard.
- **System font stack:** using fonts already on the device instead of downloading one.
- **Tabular numbers:** digits of equal width, so columns of numbers line up.
