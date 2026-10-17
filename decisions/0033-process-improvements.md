# Decision 0033: Process improvements from the first monthly review

**Status: APPROVED by Remington, 2026-10-17**, including commit and deploy. Source: private improvement review of 2026-10-17, items 1–3 and 5.

## 1. Structured evidence fields and a consistency check
- Added `peer_reviewed`, `version_tested` and `test_date` to every counted independent-performance source in all 13 scored entries. 11 entries had none of these fields; Data Interpreter and Comet had partial ones.
- Values come from the existing notes. `unstated` is used where a value cannot be determined.
- Added `counted: false` to duplicate records of already-counted studies: Browser Use (HAL page), GPT Researcher (two camera-ready / ACM records and the Comparator ACM record) and OpenAI Deep Research (arXiv and OpenReview records).
- Added `counted: false` to Open Interpreter's three out-of-scope studies, matching its existing count note.
- No score, grade, count or note text changed. Only the YAML quoting style changed when the files were re-saved; the content is otherwise identical.
- Added `scripts/check_scores.py`: a read-only recompute of scores and grades. It is installed as a local pre-commit hook (not version-controlled) and documented in `docs/PROCESS.md`.
- Result: 0 errors and 2 warnings (Browser Use, STORM). Both are about the A-grade current-version condition. See the separate private packet, decision-0035 (grade consistency).

## 2. Links and accessibility
- **Julius AI:** the publisher page for DOI 10.18623/rvd.v23.7013 is unavailable (the DOI resolves to a 404 on the journal site). The link was replaced with the OpenAlex bibliographic record, with an "unavailable as of 2026-10-17" note. The source is not counted (independent other).
- **Kimi Researcher:** the Phoenix Weekly link (ifengweekly.com) gives no response and has no archived copy. It now reads "Phoenix Weekly (page unavailable as of 2026-10-17)" without a link. The OECD and other reports for the same statement remain. Not counted.
- **Fellou:** the two fellou.ai blog links still returned 503 on recheck and have no archived copy (the Internet Archive was offline). They were annotated "page unavailable (HTTP 503) as of 2026-10-17"; the links were kept. These are vendor sources, not counted.
- Added a "Skip to main content" link to all 28 pages, with CSS so it is hidden until it receives keyboard focus.
- Added `scripts/check_links.py`, a monthly link check that separates BOT-BLOCK (403/429/202) from FAILURE.
- Also found, not changed (outside the approved list): `os-world.github.io` (Agent S, other source, not counted) now redirects to `osworld-v1.xlang.ai`, which timed out. Suggested as a follow-up.

## 3. Citation-gate fallback rule
Written into `docs/PROCESS.md` (internal; not on the public site). Required: Semantic Scholar citations plus keyword search, or OpenAlex citations plus keyword search if Semantic Scholar refuses requests for more than 30 minutes. Best effort: full-text search, with the outcome recorded. Timebox about 30 minutes. No API key.

## 4. Batch 4 shortlist
Private packet: `/workspace/private-drafts/decision-0034-batch4-shortlist.md`.

## 5. Deploy-log process
Unchanged.
