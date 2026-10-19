# Decision 0069: Small consistency fixes

**Status: APPROVED by Remington, 2026-10-18: D1a–D7a.** D8 (deploy) needs separate approval. Source: the overnight review (private draft, 2026-10-18).

## Changes
- **D1a, footer:** methodology.html now has the shared footer, including "For agents / data". `build_footers()` copies the index footer to every page except google4c18d564fd1acb53.html, and check_export fails if any footer differs.
- **D2a, scope:** seven entries had `scope: null`. Each now uses the first sentence of its published summary, verbatim; the summary is shown on the entry page. agents.json changes only in `scope` for these 7 (agents.csv has no scope column, so it's unchanged).
  - The "(summary)" fallback code path on the compare pages is kept but currently unused.
  - check_scores warns on an empty scope; check_export prints the same warning.
- **D3a, feed type:** vercel.json adds one `headers` rule, for `/updates.xml` only: `Content-Type: application/atom+xml; charset=utf-8`. outputDirectory, cleanUrls and all build settings are unchanged, and check_export enforces exactly this rule.
- **D4a, grade notes:** a `grade_note` field (YAML, agents.json and schema) for aider, swe-agent, devin, github-copilot-coding-agent and storm. It's shown on each entry page directly under the grade explanation (`<p class="grade-note">`), and check_scores reports these as DOCUMENTED rather than WARN.
  - Each note uses only the counts and facts already in the entry YAML (`scores_rationale.evidence_quality`) and the decision records (0025 clarification; 0053 for SWE-agent).
  - No score or grade changed.
- **D5a, titles:** `<title>` (and og/twitter titles, which share the value) shortened on the research and Claude Code/Codex compare pages. H1s unchanged.
- **D6a, citing description:** trimmed to 137 characters.
- **D7a, checks:** footer equality; a WARN for generated-page titles over 70 characters and for meta descriptions over 160; the empty-scope WARN; grade notes match YAML and appear on the page; vercel.json settings fixed.
- **Changelog row:** 2026-10-18-0069.

## Scope source sentences
Each is the first sentence of the entry's summary, shown on its entry page.

| Entry | Scope (verbatim) |
|---|---|
| elicit | Elicit is a commercial AI research assistant that searches academic papers and supports systematic-review steps (screening and data extraction). |
| google-deepmind-safe | SAFE (Search-Augmented Factuality Evaluator) is open research code from Google DeepMind, described in a NeurIPS 2024 paper, that uses a language model and Google Search results to rate individual facts in long-form text. |
| openai-deep-research | OpenAI Deep Research is a commercial ChatGPT feature that writes cited research reports. |
| gemini-deep-research | Gemini Deep Research is a Google feature, in the Gemini app and as a Gemini API agent, that plans multi-step web research and writes cited reports. |
| gpt-researcher | GPT Researcher is an open-source research agent that writes cited reports. |
| browser-use | Browser Use is an open-source Python library (MIT licence) that lets a language model of the user's choice control a web browser to carry out tasks. |
| pactum | Pactum is a commercial procurement-negotiation agent. |

## Grade notes and their sources
- **aider (A):** from `evidence_quality`: "Eight independent sources, six peer-reviewed … Sifting the Noise tested v0.86.1; the test date is not stated, but its access dates (December 2025 to January 2026) place it within 12 months, so grade A. This score is below the methodology's suggested A range (85-100) because the A rests on a single recent versioned test whose date is inferred."
  - It replaces the page's older sentence "… which is a preprint". The YAML and the source list identify Sifting the Noise as ISSTA 2026, so "preprint" was out of date.
- **swe-agent (A):** from `evidence_quality` ("Sifting the Noise (ISSTA 2026) states the version tested (main-branch commit 1d3cfb, 5 December 2025) and ran within the last 12 months, so grade A") and the uncertainty "Grade A rests on a single recent versioned study whose authors also wrote another counted source (Vul4Py)" (decision 0053).
  - **It replaces a stale sentence on the live page:** "Grade B rather than A: no independent test from the last 12 months states the SWE-agent version". That was left over from before 0053 and contradicted the displayed grade A.
- **devin (B):** from `evidence_quality`: "Twelve independent sources, five peer-reviewed … Eleven are field studies largely from one dataset (AIDev, December 2024 to July 2025), so they are not independent samples … none states a version and none is within 12 months. Grade B."
- **github-copilot-coding-agent (B):** from `evidence_quality`: "Twelve independent sources, five peer-reviewed … All are field studies largely drawn from one dataset (AIDev) covering December 2024 to July 2025 … none states a version, and none is within 12 months. Grade B."
- **storm (B):** from `evidence_quality` ("None states the library version except WriteHERE (v1.1.0, 2025), so the A condition of a current-version test within 12 months is not met (grade B under the 0025 clarification)") and the page's existing sentence. That existing sentence was replaced by the note.

## Known remaining warnings (reported, not hidden)
The 70-character title warning fires on citing.html (72) and all three compare pages (80–88). The " — Agent Reputation & Trust Clearinghouse" suffix (41 characters) was not counted when the packet's shortened titles were chosen. A later decision could shorten the suffix on generated pages or raise the limit. No other warnings.

## Plain-English terms
- **Grade note:** a short public explanation of why the grade came out as it did, where the automatic check flags it for review.
- **Content type:** the label the server sends that tells software what kind of file it is.
