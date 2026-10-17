# Decision 0011: Site polish

**Status: APPROVED by Remington, 2026-10-16.** Items 1–5 approved as drafted, plus all optional extras (Item 6); site name standardized to "Agent Reputation & Trust Clearinghouse". No score, grade, status, approved summary or last-reviewed date changed.

## 1. What happened
- Decision 0010 is live (dpl_HxZk4HKddfBk8zgjvRyG5cGLVPtd, 2026-10-16 22:05 EDT; logged in `LOG.md`).
- All 8 entries show "Last reviewed: 2026-10-16" in the header line (`public/agents/*.html`) and in the directory's "Last reviewed" column (`public/index.html`). Source: YAML `last_reviewed`. No definition of "review" exists anywhere.
- Every page (10) now has one standardized footer (Decision 0010, fix 9).
- No public changelog exists; history lives in `decisions/` (repo) and `LOG.md` (internal, includes deploy ids).
- No correction channel is published.
- **Regression from 0010 fix 6:** Pactum's Bloomberg source lost its "paywalled; not reviewed" qualifier; it now reads `note: Bloomberg Businessweek (2023-04-26) (journalism)` with no `access_note` (`agents/pactum.yaml`, `public/agents/pactum.html`).
- No page has a `<meta name="description">`; titles follow "<Name> — Agent Trust Clearinghouse" (index: "Agent Trust Clearinghouse — Directory").

## 2. Items

### Item 1 — "Last reviewed" date
- **Current state:** shown on entry header + index; value = YAML `last_reviewed`; undefined meaning.
- **Risk:** readers may read it as "verified current as of"; a typo fix bumping the date would overstate freshness.
- **Recommendation: APPROVE.**
- **Proposed rule (methodology, new section):**
  > **Last reviewed.** The date (America/New_York) an approved decision packet last re-checked an entry's sources and scores against the current rules. Wording, formatting or link-label fixes do not change it. A rules change that leaves an entry's outcome unchanged (e.g. Decision 0010) does not change it either. It is not a guarantee that information is current.
- **Date source:** YAML `last_reviewed` only; the page and index must match it. Shown in the entry header line (unchanged) and the index column (unchanged), plus a link:
  ```html
  <p>Category: … · Last reviewed: 2026-10-16 (<a href="/methodology.html#last-reviewed">what this means</a>)</p>
  ```
- **Impact:** no dates change (all 2026-10-16; Decision 0010 does not count as a review).

### Item 2 — Standard footer
- **Current state:** identical on all 10 pages since 0010.
- **Recommendation: APPROVE keeping it as-is** and adding links only. Exact text:
  ```html
  <footer><p>Informational only; not a guarantee, endorsement, or certification. Scores are based on public sources and the stated rules at the time of review. The Clearinghouse is not responsible for any agent's outcomes.</p>
  <p><a href="/methodology.html">Methodology</a> · <a href="/changelog.html">Changelog</a> · <a href="mailto:trustkeeperace@gmail.com?subject=Correction%20request">Request a correction</a></p></footer>
  ```
- **Risk:** low; links depend on Items 3–4 (drop the corresponding link if either is rejected).

### Item 3 — Public changelog page (`/changelog.html`)
- **Include:** approved decisions only — date, decision number, one-line plain summary, and any score/grade/status change (before → after); rules-version changes.
- **Exclude:** private drafts, rejected/deferred proposals' content (state only "deferred" when a published decision says so), deploy ids, internal tooling notes, research-in-progress, personal data.
- **Format:** newest first, plain table. Each row links to the decision file in the public repo.
- **Recommendation: APPROVE.** Risk: must be updated in the same commit as each change (add to publishing checklist).
- **Mockup:**
  ```html
  <h1>Changelog</h1>
  <p>Approved changes to entries and rules, newest first. Each item links to its decision packet. Informational only.</p>
  <table><thead><tr><th>Date</th><th>Decision</th><th>Change</th></tr></thead><tbody>
  <tr><td>2026-10-16</td><td>0010</td><td>Scoring rules v0.1: exact .5 rounds up (permanent); independent performance source rule; evidence grade table; wording cleanups. No score, grade or status changed.</td></tr>
  <tr><td>2026-10-16</td><td>0009</td><td>Added Google DeepMind SAFE: overall 66, grade B-.</td></tr>
  <tr><td>2026-10-16</td><td>0008</td><td>Added Open Interpreter: Insufficient evidence.</td></tr>
  <tr><td>2026-10-16</td><td>0007</td><td>Added Julius AI: Insufficient evidence.</td></tr>
  <tr><td>2026-10-16</td><td>0006</td><td>Added Clay: Insufficient evidence.</td></tr>
  <tr><td>2026-10-16</td><td>0005</td><td>Added Pactum: Insufficient evidence.</td></tr>
  <tr><td>2026-10-16</td><td>0004</td><td>Added Perplexity: overall 54, grade B. Interim rounding note (exact .5 rounds up).</td></tr>
  <tr><td>2026-10-16</td><td>0003</td><td>Added OpenAI Deep Research: overall 65, grade B.</td></tr>
  <tr><td>2026-10-16</td><td>0002</td><td>Added GPT Researcher: overall 53, grade B-.</td></tr>
  <tr><td>2026-10-16</td><td>0001</td><td>Seed list approved; Loki replaced by Google DeepMind SAFE. Scoring rules v0 published.</td></tr>
  </tbody></table>
  ```
  Links: `<a href="https://github.com/TrustKeeperAce/agent-trust-clearinghouse/blob/master/decisions/0010-rules-clarifications.md">0010</a>` etc.

### Item 4 — Correction requests (email only)
- **Channel:** `mailto:trustkeeperace@gmail.com` only. No forms, no scripts, no analytics, no data stored on the site.
- **Risks:** inbox may receive vendor pressure or personal data; promising timelines or outcomes creates expectations. Wording below avoids both.
- **Recommendation: APPROVE.** Add a section to `methodology.html` (anchor `#corrections`) and the footer link (Item 2).
- **Exact wording:**
  > **Corrections.** If you believe an entry contains a factual error or misses a relevant public source, email <a href="mailto:trustkeeperace@gmail.com?subject=Correction%20request">trustkeeperace@gmail.com</a> with the entry name, what you believe is wrong, and links to public sources.
  > - Requests are reviewed under the same published rules as every entry. A request may or may not lead to a change; any change is made through an approved decision and listed in the changelog.
  > - We do not promise a response or a response time.
  > - Entries are not removed, added or re-scored for payment, and we do not accept payment for any listing or change.
  > - Please do not send confidential or personal information. Only public sources can be used.
  > - Sending a request does not create any agreement or obligation.

### Item 5 — Bloomberg paywall regression (from 0010 fix 6)
- **Recommendation: APPROVE (restore).** Exact change in `agents/pactum.yaml`:
  ```yaml
  - url: https://www.bloomberg.com/news/articles/2023-04-26/walmart-uses-pactum-ai-tools-to-handle-vendor-negotiations
    kind: independent other
    accessed: '2026-10-16'
    note: Bloomberg Businessweek (2023-04-26) (journalism)
    access_note: not reviewed (paywalled)
  ```
  Page line: `… — independent other, accessed 2026-10-16; not reviewed (paywalled)</li>`. No count/status change.

### Item 6 (optional) — trivial polish
- Add `<meta name="description">` per page, e.g. index: `"Informational directory of AI agents with rule-based, separately shown factor scores. Not a guarantee, endorsement, or certification."`; entries: `"<Name>: factor scores, sources and evidence grade under Scoring rules v0.1. Informational only."` (Insufficient entries: "…sources and Insufficient evidence status…").
- Make the index `<h1>` ("Agent Reputation &amp; Trust Clearinghouse") match the titles ("Agent Trust Clearinghouse"), or the reverse — pick one name.
- Add `id` anchors on methodology sections (`#rounding`, `#insufficient-evidence`, `#evidence-grade`, `#last-reviewed`, `#corrections`) so entry pages can deep-link.

## 3. Plain-English terms
- **mailto link:** a link that opens your own email app addressed to us; the site itself collects nothing.
- **Changelog:** a public list of approved changes, with dates.
- **Meta description:** the short summary search engines may show under a page title.
- **Regression:** something accidentally lost in an earlier change.
