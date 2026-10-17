# Internal process notes

This file is for maintainers. It describes internal process only and does not change the scoring rules.

## Evidence fields for counted sources (Decision 0033)
Each source whose `kind` starts with `independent performance` records:
- `peer_reviewed`: true or false.
- `version_tested`: the product version, tier or model as stated by the source, or `unstated`.
- `test_date`: when testing or data collection happened (YYYY-MM, YYYY-MM-DD, a range, or `unstated`). This is not the publication date.
- `counted: false`: only for a duplicate record of a study that is already counted, or for a source that is outside the entry's scope.

## Consistency check before each commit
Run `python3 scripts/check_scores.py`. It recomputes each overall score (30/20/25/25, rounded half up) and checks the evidence grade against the counted sources and the grade rules.
- ERROR lines must be resolved before committing.
- WARN lines mark judgment calls, such as whether the A-grade current-version test can be shown from the data. They must be explained in the entry's decision packet.

To run it automatically as a local git hook (not version-controlled), run:
`printf '#!/bin/sh\npython3 scripts/check_scores.py || exit 1\n' > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit`

## Monthly link check
Run `python3 scripts/check_links.py`. It reports three groups:
- **OK.**
- **BOT-BLOCK (HTTP 403, 429 or 202):** the site usually refuses automated requests. These are not treated as dead links.
- **FAILURE:** 404, 410 or 5xx, or no response after one retry.

For each FAILURE:
- Find a working replacement that supports the same statement, or an archived copy, or mark the link "unavailable as of YYYY-MM-DD".
- Never change the link for a counted source without a decision.

## Citation-gate fallback rule (Decision 0033)
Before publishing a new entry, the citation gate looks for independent tests that would change the outcome.
- **Required:**
  - Semantic Scholar citations of the key papers, plus a Semantic Scholar keyword search for the product name.
  - If Semantic Scholar keeps refusing requests (for example HTTP 429) for more than 30 minutes, use OpenAlex citations plus an OpenAlex keyword search instead.
- **Best effort:** a full-text search (Semantic Scholar snippet search or equivalent). Record the outcome in the decision, including when it could not be run.
- **Timebox:** about 30 minutes for the gate. Then record what was completed and proceed or stop, according to the instruction for that entry.
- **Reading:** any candidate that appears to test the product as a system is read in full before it is counted.
- No API key is used.

## Deploys
Unchanged. Deploys are done only by the owner. After each deploy, a LOG-only note with the deploy id and commit is added.

## Coding agent evidence cautions (Decision 0036)
These are internal guidance under the existing rules; they do not change the scoring rules.
1. **Vendor-reported benchmarks are not counted.** SWE-bench (Verified, Lite, Multimodal, Pro), Terminal-Bench, maintainer leaderboards such as Aider's, and similar results that the developer reports, runs or self-submits are listed as vendor sources.
2. **The named product must be tested.** A study of a model inside a generic or third-party scaffold does not count for a product built on that model. For example, Claude in mini-SWE-agent is not a test of Claude Code; the named agent itself must be run.
3. **Maintainer-verified leaderboards are other sources.** SWE-bench "verified" submissions, HAL entries and similar leaderboards are listed, not counted (OSWorld-Verified precedent, 0025). A study by the maintainers that runs the agent themselves can count, subject to caution 4.
4. **Affiliation checks.** A source that shares authors with the developer is excluded for that product (the CAP and Fellou precedent). This matters for overlapping groups, such as Princeton's SWE-bench, SWE-agent and HAL. Competing-method authors count, with disclosure.
5. **Version and test date.** Record `version_tested` and `test_date` for every counted source. An A grade needs a stated version or tier, or a dated test of the hosted current product (0035).
6. **Contamination and benchmark quality.** Critiques of contamination or task validity are reported neutrally as context, not as performance tests.
7. **Security.** Describe CVEs, prompt-injection and sandbox findings neutrally: CVSS attributed, fix status noted, no exploit links.
8. **Productivity studies.** Controlled or randomised developer studies can count if they name and use the agent, with version and date recorded.
