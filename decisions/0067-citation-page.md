# Decision 0067: Citation examples page ("How to cite and quote this data")

**Status: APPROVED by Remington, 2026-10-18**, as recommended:
- **D1a:** a new /citing.html, with the data page's licence section trimmed to a summary and a link.
- **D2a:** formats are a plain sentence, APA-style (entry and dataset), BibTeX (dataset) and an agent quote template.
- **D3a:** example values are generated at build time. They use the alphabetically first entry with evidence grade A and the alphabetically first Insufficient-evidence entry.
- **D4a:** the typed-in OpenHands example is replaced everywhere by the generated one.
- **D5b:** links from methodology, the data page and llms.txt. No footer link.
- **D6a:** "certified", "verified" and "endorsed" are added to the banned wording for generated pages, excluding the don'ts table.
- **D7b:** no CITATION.cff until the domain is decided (0064).
- **D8a:** existing disclaimer wording is reused, plus one "examples generated as of" sentence.
- **D9a:** checks are in check_export.py and the pre-commit hook.
- **D10:** deploy needs separate approval.

## What changed
- **`scripts/build_data.py`:**
  - `example_entries`, `score_phrase` and `quote_line` added. `CITATION` is now generated, and it ends with a link to /citing.html.
  - `render_citing` and `build_citing` write the following:
    - citing.html;
    - the agents-data.html `#license` summary (licence, code scope, suggested citation, link; the `#citation` anchor is kept);
    - the llms.txt citation line and a "How to cite" page link;
    - the methodology link (in "Data and license", before the Disclaimer);
    - a sitemap entry.
  - Compare pages: the quoted entry uncertainties list now carries `class="quoted"`. It is excluded from the new-word scan only.
- **Examples at implementation:**
  - Aider (open-source): 52/100, grade A, as of 2026-10-17.
  - AutoKaggle: insufficient evidence, as of 2026-10-17.
  - These change automatically when the data changes.
- **`scripts/check_export.py` checks that:**
  - citing.html matches a fresh render;
  - the example values equal agents.json, independently recomputed;
  - the required text is present: disclaimers, licence link, generated-as-of note, attribution line, code scope, LICENSE link;
  - the wording for Insufficient entries is safe (no "0/100", no "None");
  - banned wording (the 0066 list plus certified, verified and endorsed) is absent outside the don'ts table, and the new words are present inside it;
  - JSON-LD is only WebPage/BreadcrumbList, there is no rating markup, and there is no script;
  - there is exactly one Dataset block site-wide;
  - citing.html is in the sitemap and llms.txt, the links are present, and a changelog row exists;
  - the old typed-in example is gone and updates.json carries the current guidance;
  - compare pages have no new banned words outside the quoted uncertainties.
- **Changelog row:** 2026-10-18-0067. No score or grade changes.

## Not changed (reported)
"verified" already appears on existing pages, and they were not reworded:
- **The usage note** on agents-data.html and in llms.txt ("Do not describe an entry as 'verified', 'certified'…"). This is a prohibition, like the don'ts table.
- **Entry pages:** benchmark names (SWE-bench Verified, OSWorld-Verified) and uncertainty text ("not independently verified").
- **compare/research-agents.html:** a quoted uncertainty.

The new-word check is scoped to citing.html and the compare pages' own text.

## Plain-English terms
- **Generated example:** filled in from the data when the site is built, so it can't go stale silently.
- **Don'ts table:** the only place where the prohibited words appear on purpose.
