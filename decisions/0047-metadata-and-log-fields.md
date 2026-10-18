# Decision 0047: Metadata and evidence-log fields (grouped trivial fixes; no score impact)

**Status: APPROVED by Remington, 2026-10-17** (D1–D5 as drafted). YAML only; no public/ changes; no deploy. check_scores output identical before and after.



## What happened (facts and sources)
The consistency pass compared every entry's YAML with agents/_schema.example.yaml and with the evidence-log fields used since 0040 (version_tested, test_date, peer_reviewed on counted sources; accessed on every source). These gaps were found (audit-raw.txt):
1. **Required top-level fields missing in 19 entries** (last_reviewed, decision, decision_packet, notes).
   - 13 older entries: agent-s, chatgpt-work, claude-code, data-interpreter, fellou, loki, openfactcheck, openhands, perplexity-comet, skyvern, storm, swe-agent, ui-tars-desktop.
   - 6 newer entries: aider, aide, autokaggle, openai-codex, github-copilot-coding-agent, devin.
   - The values are already public elsewhere:
     - last_reviewed is taken from each page's "Last reviewed" line.
     - decision_packet is taken from the existing decisions/ file (0042 for aide and autokaggle; 0030 for loki and openfactcheck).
     - decision is APPROVED (all published entries were approved).
     - notes is the standard disclaimer.
2. **Counted sources without version_tested, test_date or peer_reviewed** in 5 Insufficient-evidence entries (9 sources). The values are filled from the existing source notes:
   - julius-ai: Abbasi et al., Applied Sciences 2026, peer-reviewed. Ohio Journal of School Mathematics 2025, review status unclear, so recorded as false.
   - kimi-researcher: DeepResearch Bench, ICLR 2026, run 29 Jun–1 Jul 2025 on the official UI, peer-reviewed. ICBCBench, preprint, access date unstated.
   - loki: two 2026 preprints.
   - pactum: a 2026 master's thesis.
   - skyvern: two Jan 2026 preprints; WebTrap Park code accessed 11 Jan 2026.
   - Version is "unstated" in all 9; none of these sources states a product version.
3. **17 "other" or vendor source rows without an access date**: devin (8) and github-copilot-coding-agent (9). They were read on 2026-10-17 during 0044 and 0045, so that date is added.
4. **Duplicate records of one study without an explanation**, added as count_note. The counts themselves are already correct and unchanged:
   - gpt-researcher: 6 rows = 3 studies.
   - openai-deep-research: 7 rows = 5.
   - browser-use: 8 rows = 7.

## What the rules say
- The schema (agents/_schema.example.yaml) lists last_reviewed, decision, decision_packet and notes for every entry, and accessed for every source.
- The evidence log records version_tested and test_date on counted sources (practice since 0040, and needed to apply the grade-A "test within 12 months that states the version" condition).
- The methodology's scoring rules, weights and grade table are not affected by metadata.

## Verification (local draft)
- check_scores gives the same output on the draft as on master: 0 errors, the same 6 warnings, and identical scores, grades and counts for all 34 entries.
- No public/ file changes. The draft changes YAML only (24 files, small diffs; no comments lost).
- No count changes: count_note is explanatory only.

## Risks and uncertainties
- The Ohio Journal of School Mathematics review status is unclear. It is recorded as peer_reviewed: false, which is conservative, and Julius AI stays Insufficient either way.
- last_reviewed is copied from the page. It is the page's existing statement, not a new review.
- Filling "unstated" is not a finding that the version is unknowable; it records that the source does not say.
- YAML is re-serialised by the script. Diffs were checked: only the added keys change.

## Recommendation
**Approve.** These are bookkeeping fixes that make the evidence log complete and match the schema. They change no score, grade, count or public page. The bigger items found in the pass are kept out of this packet and will get their own packets: grade-A basis checks, citation-gate backfill, template sections, SusVibes, and the Agent S TOCTOU flag.

## Decisions requested
- **D1:** Add the four top-level fields to the 19 entries, with values as listed in the diff.
- **D2:** Add version_tested, test_date and peer_reviewed to the 9 counted sources in the 5 Insufficient entries, with the Ohio Journal source recorded as false.
- **D3:** Add accessed: 2026-10-17 to the 17 devin and Copilot rows.
- **D4:** Add count_note to gpt-researcher, openai-deep-research and browser-use. Leave Open Interpreter as is (it already explains its out-of-scope rows).
- **D5:** Rollout: one commit, YAML only, no deploy needed (no public/ change). Changelog row optional; recommend none, since nothing public changes, and a LOG line instead.

## Plain-English terms
- **YAML:** the data file behind each entry page.
- **Evidence log:** the list of sources for an entry, with what each one tested, when, and whether it was peer-reviewed.
- **Schema:** the template that says which fields every entry file should have.
- **Count note:** a short explanation of how the source rows add up to the counted number.
