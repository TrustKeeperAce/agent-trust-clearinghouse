# Decision packet 0080: Evidence pass 4 (Pactum, Clay, OpenFactCheck, Fellou)

**Status: APPROVED by Remington, 2026-10-19: D1a, D2a, D3a, D4a, D5a, D6a and D7 as recommended. D8 (changelog row) and D9 (deploy) are not approved: no changelog row was added and nothing is deployed.**

Implementation notes (2026-10-19): Data: agents/pactum.yaml, agents/clay.yaml, agents/openfactcheck.yaml, agents/fellou.yaml (`last_reviewed` 2026-10-19; this decision added to each `decision_packet`). Scores stay null, counted numbers are unchanged, and all four stay Insufficient evidence. Pactum: one uncertainty line on the pass-4 result; no new records. Clay: Sixtyfour and SyncGTM added as `competitor`; the 0052 recheck line replaced with the pass-4 line (citation check still incomplete); one line on the competitor tests; other stays 6. OpenFactCheck: first uncertainty line updated with the 19 Oct OpenAlex recheck (13 papers read in full). Fellou: Decodo added as `other` with the publisher disclosure; other 5 → 6; Journal du Net and Writingmate named in the informal-reviews uncertainty; Semantic Scholar line updated. The four entry pages carry the same text, records and dates. D7: Decodo's findings on eight other entries are logged in a private note for the monthly review; no public change.

*Per-entry drafts referenced below were kept as private working notes and are summarised in this record.*

**Outcome in one line (if the recommended options are approved):** no grade or score changes. All four entries stay **Insufficient evidence**: Pactum 1 counted, Clay 0, OpenFactCheck 0, Fellou 0. Only source records, uncertainty lines and last_reviewed change. Fellou's other count goes 5 → 6; all other counts are unchanged.

## 0. Selection
These are the four remaining Insufficient entries not covered by passes 0076 and 0077, as Remington asked in t148u. No entry could reach a score in this pass, so no sub-scores are drafted.

## 1. What happened (facts and sources)
Searches ran on 19 Oct 2026, about 03:35–03:50 ET. Tools used:
- OpenAlex: citing works, and full-text search for "Claygent", "Fellou", "Pactum" and "OpenFactCheck"
- arXiv, ACL Anthology, AAAI OJS, FLAIRS, Research Square and other open PDFs (read with pdftotext)
- web search
- Semantic Scholar: the citations endpoint and snippet search returned **HTTP 429** at 03:40 and again about 03:45 ET. The only exception was the EMNLP OpenFactCheck demo (48 citations, unchanged).

Every recorded source was read in full unless flagged.

### Pactum (1 counted)
- **No new test of Pactum found.**
- Two 2026 negotiation studies used other AI systems:
  - "Is There a Human Premium in Negotiations?" (Group Decision and Negotiation, Oct 2026, https://doi.org/10.1007/s10726-026-10027-8) uses its own LLM broker.
  - "Brave new procurement deals" (J. Purchasing & Supply Mgmt, 2025) uses a ChatGPT chatbot.
- The IJOPM "Impact pathway" paper (https://doi.org/10.1108/ijopm-12-2025-1238) is conceptual; read by abstract only.
- Vendor (Honeywell case study) and commentary items (PASA, otontechnology) restate known figures.

### Clay (0 counted)
- **No independent benchmark of Claygent found.**
- Two new tests were published by **competing vendors**:
  - **Sixtyfour** LinkedIn post, about Feb 2026 (https://www.linkedin.com/posts/christopher-price-59a24b178_we-benchmarked-our-research-agents-against-activity-7425305026103013376-Q-DL): 184 leads; Clay 66% accuracy, against 93% for Sixtyfour's own product.
  - **SyncGTM** review, Mar 2026, updated Sep 2026 (https://syncgtm.com/blog/clay-review): 78% email match on 2,000 contacts; Claygent correct 70–80% of the time on narrow tasks. The page closes by offering SyncGTM as an alternative.
- Smaller practitioner items:
  - Outbound Kitchen podcast OK27 (one prompt, 7 models)
  - Jacob Tuwiner / Sculpted (20 rows, agency)
  - Will Breton (not Claygent-specific)
- Clay's own July 2026 blog post (internal suite; no scores published).
- An agency re-calculation of Clay's provider benchmark (Automation Jinn): no new data.
- The OpenAlex full-text search for "Claygent" found one passing mention (a student thesis). The 0052 citation recheck is still incomplete because Semantic Scholar was unavailable.

### OpenFactCheck (0 counted)
- **13 newer citing papers were read in full; none ran OpenFactCheck as a tested system.** The list with links is in `openfactcheck.md`: VEX-Bench, SoK Formal Methods, 2606.21359, 2605.21071, Valiant, CaseFacts, FactSearch, Pro-QuEST, TAIGR (ACL), MedSNIP, the Lightweight Retrieval-Grounded preprint, Religious text fact-checking and CogSLLaM.
- MedSNIP shares authors with OpenFactCheck (Iqbal, Y. Wang), so it would be excluded in any case (0031).
- Four survey or framework papers were not read in full (flagged).
- Maintenance is unchanged: 2.0.0a10 is the latest release (13 Jul 2026) and the last push was 15 Aug 2026.

### Fellou (0 counted; CAP excluded under 0031)
- **Decodo "Agentic Capability Report"** (26 Aug 2026, https://decodo.com/blog/agentic-capability-report):
  - Decodo sells web-data and proxy APIs for AI agents.
  - The report scores 45 tools mainly from vendor documentation.
  - In its hands-on check ("we only ran each task twice per tool"; no per-task results), Fellou "got stuck on complex layouts, looped at times, and couldn't get past CAPTCHAs" (documented 19 → adjusted 17).
- **Writingmate** (updated 1 Aug 2026, https://writingmate.ai/blog/ai-browser-agents-2026-comet-dia-fellou-polar-tested): one task across 4 browsers. Fellou finished after one intervention (a loop). The publisher promotes its own alternative product.
- **Journal du Net** (16 Oct 2025, https://www.journaldunet.com/intelligence-artificielle/1545063-comparaison-de-4-navigateurs-agentiques/): press hands-on review. Unstable and buggy, with no task counts.
- SAGE 0.2 (FLAIRS-39) and a TechRxiv survey only mention Fellou.
- The OpenAlex full-text search found only "Configuration, Not Conscience", already screened in 0031.
- CAP is unchanged and stays excluded.

## 2. What the rules say (Scoring rules v0.1, unchanged)
- An overall score needs at least **3 independent performance sources**: tests that report their method and results, on the entry's product, version and scope.
- Independence means "not produced, funded or co-authored by the vendor or maintainer, and not published by a competing product to promote itself." Benchmarks by a competitor promoting itself use kind `competitor` (the Julius AI precedent: Rows, Basedash, Fastero).
- Precedents:
  - Reviews, commentary, press without original testing and user-review aggregates are other sources. Anecdotal records count toward "other" (0079).
  - 0031: a shared author with the developer means excluded.
  - 0042: re-implementations are other.
  - 0058: illustrations are not counted.
  - 0076: re-scoring others' outputs is other.
  - 0039: model-only tests are context for app entries.
- 0079: the typed `independent_source_count.other` must equal derived_other, which counts uncounted records whose base kind is other, independent other or anecdotal. `competitor`, vendor, excluded and similar kinds are not counted in it.
- Grades: below 3 counted is Insufficient; 3–4 is B-; 5–6 is B; 7+ is A (with 3+ peer-reviewed and a current-version test).

## 3. Proposed changes (before → after, recommended options)
| | Pactum | Clay | OpenFactCheck | Fellou |
|---|---|---|---|---|
| Counted | 1 → 1 | 0 → 0 | 0 → 0 | 0 → 0 |
| New records | none | +2 `competitor` (Sixtyfour, SyncGTM) | none | +1 `other` (Decodo) |
| Other (typed = derived) | 7 → 7 | 6 → 6 | 2 → 2 | **5 → 6** |
| Grade / scores | Insufficient / null | Insufficient / null | Insufficient / null | Insufficient / null |
| Text | +1 uncertainty line | 0052 recheck line replaced; +1 competitor line | first uncertainty updated | 2 uncertainty lines updated |
| last_reviewed | 2026-10-16 → 2026-10-19 | 2026-10-16 → 2026-10-19 | 2026-10-17 → 2026-10-19 | 2026-10-17 → 2026-10-19 |

**Other-count changes under non-recommended options:**
- Clay D2b: 6 → 8. Clay D3b: +1.
- Fellou D5b: 5 → 7. Fellou D6b: stays 5. Fellou D6c: stays 5.

The typed value must be set to the derived value in every case.

**Simulation** (a copy of the repo at /tmp/sim80, not the repo; recommended options applied; rebuilt):
- `check_all.sh` passes: check_scores, check_export with 0078 and 0079 consistent, no-JS. The result is 0 errors.
- With Fellou left at other 5, check_export fails with "typed other 5 != derived 6", as intended.
- Public files that would change: the 4 entry pages, `public/data/agents.json`, `public/data/agents.csv` (last_reviewed and Fellou other), `public/llms-full.txt`, `public/index.html` and `public/sitemap.xml` (lastmod).
- The Insufficient status lines show no other number, so no status text changes.
- A changelog row (D8) would also change `changelog.html`, `updates.json`, `updates.xml` and probably `citing.html`, as in 0077.
- Simulated sha1s will differ from the real ones once the decision file and LOG are added. The real sha1s would be taken at implementation time.

## 4. Risks and uncertainties
- **Semantic Scholar was unavailable (429)** on every call except one. Snippet search for "Fellou", "Claygent" and "Pactum negotiation", and citation counts for two OFC papers, could not be run. Clay's 0052 recheck stays open.
- **SyncGTM (Clay)** is borderline between `competitor` and `anecdotal` (D3). It reports a hands-on test, but sells an alternative and recommends it.
- **Decodo (Fellou)** is borderline between `other` and `competitor` (D6):
  - It is not a browser agent, but it sells tools to agent builders.
  - Its report ranks tools, and the ranking words must not be repeated on our pages.
  - It does run hands-on checks. Even so, two runs per task with no results table do not meet "method and results" for a counted source.
- The **Sixtyfour** method page on its blog was not reviewed. It is a competitor in any case, so it would not be counted.
- **Not read in full:**
  - OFC: TRACE (IJIES), a low-resource fact-checking thesis, a systematic review and the Narrative Integrity review.
  - Pactum: IJOPM (abstract only).
  - Any of these could contain a run; by their titles and abstracts it is unlikely.
- The **LinkedIn and podcast** items cannot be archived reliably, and their figures may change or disappear.
- **Decodo also reports results for Devin, Browser Use, Comet, Manus, Skyvern, Agent S2, OpenHands and UI-TARS.** These are out of scope here (D7).

## 5. Decision items
- **D1 Pactum.**
  - a) Stays Insufficient. Add the pass-4 uncertainty line and set last_reviewed to 2026-10-19; no new records (**recommended**).
  - b) As a), and also list the otontechnology blog as `other` (other 7 → 8). Not recommended: it restates vendor figures.
  - c) No change.
- **D2 Clay records.**
  - a) Add Sixtyfour and SyncGTM as `competitor`, replace the 0052 recheck line with the pass-4 line (still incomplete), add the competitor uncertainty line and set last_reviewed (other stays 6) (**recommended**).
  - b) As a), and also add Outbound Kitchen OK27 and Tuwiner/Sculpted as `anecdotal` (other 6 → 8).
  - c) As a), and also add "and two competitor tests" to the summary.
  - d) No change.
- **D3 Clay: SyncGTM kind (borderline).**
  - a) `competitor` (**recommended**; the Fastero precedent).
  - b) `anecdotal` (other +1).
- **D4 OpenFactCheck.**
  - a) Stays Insufficient. Update the first uncertainty line with the 19 Oct recheck (13 papers read in full) and set last_reviewed (**recommended**).
  - b) No change.
- **D5 Fellou records.**
  - a) Add Decodo (kind per D6), name Journal du Net and Writingmate in the informal-reviews uncertainty, update the Semantic Scholar line and set last_reviewed (**recommended**; other 5 → 6 with D6a).
  - b) As a), and also record Writingmate as `competitor` and Journal du Net as `other` (other 5 → 7).
  - c) As a), and also add a Decodo sentence to factor_notes.completion_rate (marked not counted).
  - d) No change.
- **D6 Fellou: Decodo kind (borderline).**
  - a) `other`, with disclosure "publisher sells web-data tools for AI agents" (**recommended**).
  - b) `competitor` (other stays 5).
  - c) Do not record; treat it as an informal review in the uncertainty line (other stays 5).
- **D7 Decodo findings on other entries.** Log them for the monthly review and take no action in this packet (**recommended**). The alternative is a separate packet later.
- **D8 Changelog row.** One entry_update row for the four entries, with no score change. This needs **separate approval** and is not recommended to bundle with D1–D6.
- **D9 Deploy.** This needs **separate explicit approval**, with the usual manifest. The rollback base is dpl_GSyq3vsNLNyMtuVBFmC2uTMHW6rY. Not recommended to bundle.

Implementing any of D1–D6 would also add `decisions/0080-evidence-pass-4.md` and a LOG.md entry, then rebuild, run check_all.sh, run a banned-word scan, commit and push, as in 0077.

## 6. MVP (smallest approvable set)
- **D1a + D2a + D3a + D4a + D5a + D6a + D7.**
  - Data edits are limited to the 4 YAML files and their 4 entry pages, plus the decision file and LOG.
  - Fellou other 5 → 6; no grade or score changes.
- **Narrowest option:** D4a + D1a only (text and dates), deferring the Clay and Fellou records to the monthly review.
- D8 and D9 follow only with separate approval.

## 7. Plain-English terms
- **Insufficient evidence:** fewer than 3 qualifying independent tests, so no score and no grade.
- **Independent performance source:** a test by someone other than the maker, or a competitor promoting itself, that explains how it tested and what it found.
- **Counted:** the source tested this product, in the scope the entry covers.
- **Other source:** useful background that does not count toward the 3, such as commentary, informal reviews and press.
- **Competitor source:** a test or review published by a company that sells a competing product. It is listed but not counted, and it is not part of the "other" number.
- **Anecdotal:** a small personal or practitioner check, or a user-review aggregate. It counts toward the "other" number.
- **derived_other:** the "other" number the site works out from the listed records. The typed number in each file must match it, or the checks fail.
- **Borderline:** a classification where a reasonable reviewer could choose a different kind. Each borderline case has its own decision item.

*Informational only; not a guarantee, endorsement, or certification.*
