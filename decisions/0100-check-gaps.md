# Decision 0100: two consistency checks (listing order; banned wording anywhere on the public site)

**Status: APPROVED by Remington, 2026-10-24 (7:15 AM ET, t275u), as recommended: D1–D7 (a).**
- **D1 (a):** the order check enforces the published methodology rule ("Directory order"), recomputed from agents.json, and requires that sentence to be unchanged.
- **D2 (a):** 0100a covers both home-page tables, the home-page ItemList, the llms.txt Entries list, agents.json and agents.csv. Comparison pages and "Other entries in this category" sections stay on their existing exact-regeneration checks.
- **D3 (a):** 0100b scans every public .html, .txt, .xml, .json and .csv file for the full BANNED_CITE list (10 patterns). The wider 0094 drafting list stays a drafting aid.
- **D4 (a):** exceptions live in data/banned_word_allowlist.yaml (not deployed). Each row is an exact, case-sensitive phrase scoped to files, with a kind and a note. Unused rows, bare-word phrases, and pending-reword rows with wildcard files or fewer than two words are errors.
- **D5 (a):** the 42 existing study-result hits (35 × best, 7 × top) on 9 entry pages and llms-full.txt are allowed for now as 33 pending-reword rows. They are left for a later wording-only packet, which would reword them in the data and pages with no score, grade or count change and remove the rows. That packet would need its own changelog row and deploy.
- **D6 (a):** no changelog row or feed item, because no public file changes. No deploy is needed. The as-of date, sitemap lastmods and feeds are unaffected (no 0090 D3 row-date ripple).
- **D7 (a):** short maintainer note on both checks in docs/PROCESS.md.

Commit and push approved 2026-10-24 (7:46 AM ET, t276u commit approved, W1–W2 as recommended: W1 applied, W2 kept); no deploy needed (no public changes).

## What happened
- **Background.** The 0099 tamper tests (17 cases) caught 15 changes and missed 2:
  1. Moving the GitHub Copilot CLI row after Replit Agent on the home page. Both entries score 51, so the swap broke the tie-break order without changing any score.
  2. Adding a banned word ("best") to the summary on the entry page only, with nothing changed in the data.
- **Gap 1 (order).**
  - The ordering rule is published on the methodology page under "Directory order": "Entries with an overall score are listed from highest to lowest overall score. Equal scores are listed alphabetically by entry name (case-insensitive). Entries labeled Insufficient evidence are listed separately, alphabetically. Order is not a recommendation."
  - build_data.py sorts agents.json and agents.csv by that rule.
  - Three lists are edited by hand when an entry is added, and the checks counted their rows but never their order:
    - the two home-page tables (Scored, and Insufficient evidence);
    - the home-page ItemList in the structured data;
    - the Entries list in llms.txt.
  - 10 scores are shared by more than one entry, covering 23 of the 33 scored entries:

    | Score | Entries |
    |---|---|
    | 62 | Consensus, OpenAI Codex |
    | 61 | mini-SWE-agent, OpenHands |
    | 58 | Claude Research, SWE-agent |
    | 57 | Cursor agent, GitHub Copilot coding agent |
    | 55 | Claude Code, Cline, FacTool |
    | 54 | OpenCode, Perplexity |
    | 53 | Gemini CLI, GPT Researcher |
    | 51 | Browser Use, GitHub Copilot CLI, Replit Agent |
    | 50 | Devin, Google Jules, Magentic-One |
    | 49 | Agent S, Data Interpreter |

  - Every list on the live site is in the correct order today.
- **Gap 2 (banned wording).**
  - The banned-word lists in build_data.py are:
    - BANNED: best, top, winner(s), "which is better", star(s), ★, #1;
    - BANNED_CITE: BANNED plus certified, verified, endorsed.
  - The checks applied these lists only to selected generated text: comparison pages, the citing page, titles, the related sections, the funding section, the llms-full framing and the README.
  - Entry pages, the home page, the changelog, the feeds, llms.txt and the data files were not scanned.
- **Current site (5af5f16, live dpl_Am8LdYouhJ82DCGMmNJ4TTUAhusV).** A scan of all 63 public text files for the 10 BANNED_CITE patterns finds 135 hits in 32 files:

  | Kind | Hits | Files | Examples |
  |---|---|---|---|
  | Rule text | 15 | 5 | Text listing the words not to use, on the citing page and in the citation guidance in agents-data, agents.json, llms.txt and llms-full |
  | Names and quoted wording | 56 | 16 | 37 × "SWE-bench Verified"/"OSWorld-Verified"; Best-of-N/Best-of-3/Best-of-10; "A*STAR"; GitHub star counts; "top-ups"; quoted task text "five-star"; "best-effort replication" |
  | Not a claim | 22 | 13 | "not independently verified" (and similar); a study's own verification step, e.g. "7 vulnerabilities were verified" |
  | Study-result wording about an entry | 42 | 9 entry pages + llms-full.txt | "the best of seven", "the top of 7 research agents", "it was the best system tested", "Top RACE report-quality score" |

  - The study-result wording breaks down as 35 × best and 7 × top, on the Aider, Claude Code, Elicit, Gemini Deep Research, Manus, OpenAI Codex, OpenHands, Perplexity Comet and SWE-agent pages. Five of these hits are summary sentences that are repeated in llms-full.txt.
  - None of the 135 hits is a Clearinghouse statement that an entry is best, top, certified, verified or endorsed.
  - The 42 study-result hits report a source's own results and are in the approved entry data. They still use words on the banned list in public text, so they are flagged under D5 and not changed here.

## Rules that apply
- Informational only, with no ranking or endorsement wording. Order is not a recommendation (methodology, "Directory order").
- Scores, grades and source counts change only through an approved entry decision. This decision changes none of them.
- The banned list is never shortened.
- Changelog rows record public changes (0065). The 0090 D3 date ripple applies only when a row is added.

## Decisions
- **D1 (a):** the order check uses the published methodology rule. It recomputes the order from agents.json and requires the methodology sentence to be unchanged, so the rule and the check cannot drift apart.
- **D2 (a): scope of the order check (0100a)** covers:
  - both home-page tables;
  - the home-page ItemList, including positions 1..n and numberOfItems;
  - the llms.txt Entries list;
  - agents.json and agents.csv.

  Comparison pages and the "Other entries in this category" sections stay covered by their existing exact-regeneration checks (render_compare and 0098); tamper case X4 confirms this. The sitemap (sorted by id) and the changelog (date order, already checked) are not ranked lists.
- **D3 (a): scope of the wording check (0100b).** It scans every public .html, .txt, .xml, .json and .csv file (63 today) for the full BANNED_CITE list (10 patterns):
  - HTML: visible text, meta content and structured data;
  - JSON: every string value;
  - other files: text with markup removed.

  The wider drafting list from 0094 (leads, unlike, unique, first, trusted, recommend*, rating, rated, safe, guarantee*, endorse*) stays a drafting aid for new text. Applied site-wide it would hit standard text such as "Google DeepMind SAFE", "not a guarantee" and "not a ranking or recommendation".
- **D4 (a): the allowlist is a new data file, data/banned_word_allowlist.yaml (not deployed).** Its rules:
  - Each row gives an exact, case-sensitive phrase, the files it applies to, a kind and a note. The kinds are rule-text, name, not-a-claim and pending-reword.
  - A hit is allowed only inside that phrase in those files.
  - Every row must still cover a hit; an unused row is an error.
  - A phrase may not be a bare banned word.
  - A pending-reword row must name exact files and use at least two words of the existing text.
  - Today the file has 59 rows: 4 rule-text, 14 name, 8 not-a-claim and 33 pending-reword.
- **D5 (a): the 42 study-result hits are allowed for now as pending-reword rows.**
  - A separate wording-only packet would reword them on the 9 entry pages, in the data and in llms-full.txt (for example "the best of seven" → "the highest of the seven tested"). It would change no score, grade or count, and would remove the rows.
  - That packet changes public pages, so it would need a changelog row and a deploy. It is not part of 0100.
- **D6 (a):** no changelog row or feed item, because no public file changes. The decision record and the LOG line are in the repository. No deploy is needed.
- **D7 (a):** add a short maintainer note on both checks to docs/PROCESS.md.

## Implementation
- **scripts/check_export.py** gains two checks, 0100a and 0100b, and a docstring note. The added code is 84 lines; nothing existing is removed or changed.
- **data/banned_word_allowlist.yaml** is new, with 59 rows.
- **docs/PROCESS.md** gains a short note on the two checks.
- **decisions/0100-check-gaps.md** is this record.
- No change to public/, agents/, data/changelog.yaml, build_data.py, scores, grades, source counts, entry pages or dates.

## Dry run (scratch clone of 5af5f16)
- check_all: 0 errors. 0100a: 33 scored and 11 insufficient entries in order. 0100b: 135 hits, all 135 allowlisted, 0 not allowed.
- check_scores output is identical to 5af5f16.
- A full rebuild produces no change in public/, and public/ is byte-identical to 5af5f16.
- check_export runtime is unchanged (about 36 s).
- **Tamper tests:**
  - Core cases (the 17 from 0099 plus 2 new gap cases): 19 of 19 caught. The unchanged 5af5f16 tree catches 15 of 19, missing 0099 #11, 0099 #16 and both gap cases.
  - Extra edge cases: 12 of 12 caught. They cover:
    - ItemList, llms.txt, Insufficient-table and comparison-page swaps;
    - banned words only in the Atom feed, a meta description, llms-full.txt or the changelog page;
    - allowlisted wording copied to another page;
    - a "verified" claim on the home page;
    - a stale allowlist row;
    - an allowlist row widened to a bare word.
