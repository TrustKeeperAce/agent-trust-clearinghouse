# Decision 0008: Open Interpreter (local code-executing agent)

**Status: APPROVED by Remington, 2026-10-16.** Publish as "Insufficient evidence", with no overall score, using the proposed public wording exactly.

**Note:** the alternative score of 45 for the classic version (below) was NOT adopted and is not published.

## Final public summary
"Open Interpreter is an open-source agent that runs code on the user's computer from natural-language instructions. Its repository now tracks a rewrite built on Codex; the earlier Python version continues in a community fork. Independent security studies, mostly preprints and self-published projects, tested the earlier Python version; we found no independent evaluation of the current product, so no overall score is given. Insufficient evidence. Informational only; not an endorsement or certification."

---


## Draft entry summary
Recommended: **Insufficient evidence**, no overall score. The repository now tracks a Rust rewrite built on Codex. The classic Python version is labeled "Legacy Python" and is maintained in a community fork. Every independent test I found used the classic version. None has been peer-reviewed.

## What happened
- **CIBER (arXiv preprint, Feb 2026):**
  - Tested classic Open Interpreter with three models against prompt injection, memory poisoning and backdoor attacks, inside sandboxes.
  - The authors describe it as passing model output to the terminal with no safety filter.
  - They report high attack success, especially for harmless-looking file operations.
- **RedCode extension (personal project page):** with GPT-4.1, risky code was fully executed in 74.5% of Python cases and 62.5% of Bash cases. The author notes that the LLM judge was unreliable.
- **ARPIbench (GitHub):** a reflected prompt-injection benchmark that uses a modified Open Interpreter harness. It mainly tests models.
- **IDA-Bench (arXiv preprint 2025):** uses a modified Open Interpreter as a fixed harness to compare LLMs on data analysis. It measures the models, not Open Interpreter itself.
- **Limits:**
  - In the classic version, Open Interpreter asks before running code unless `auto_run` or `-y` is set.
  - Classic safe mode is experimental, is off by default, and the maintainer states it "does not provide any guarantees".
  - The current docs describe a sandbox plus approval modes. These are maintainer descriptions and have not been independently tested.
- **Security records:**
  - No CVE in NVD and no reviewed GitHub Advisory Database entry.
  - Public reports allege a remote `auto_run` toggle via `POST /settings`, macOS hotkey command injection, and OS mode defaulting to `auto_run`.
  - The maintainer closed these between Jun and Jul 2026 as legacy-product issues. The proposed fix PRs were closed without merging. Fix status in the community fork: not checked.
- **Disputes:** none found.

## Sources checked
| Source | Type | Status |
|---|---|---|
|CIBER arXiv:2602.19547|Independent behaviour (preprint)|200|
|RedCode-OI page|Independent behaviour (self-published)|200|
|ARPIbench repo|Independent behaviour (self-published)|200|
|IDA-Bench arXiv:2505.18223|Model benchmark (OI as harness)|200|
|RedCode arXiv:2411.07781|Background benchmark|200|
|Issue #1767; PRs #1691, #1741|Public security reports|200|
|GitHub advisories page; NVD|Registries (none found)|200|
|Current docs; classic SAFE_MODE.md|Maintainer|200|

## Evidence quality assessment
Moderate for behaviour of the classic version, and absent for the current product. Of the 3 behaviour tests, 2 are self-published repositories, and none is peer-reviewed. I found no independent test of task success for Open Interpreter itself.

## What the rules say
Fewer than 3 independent sources means "Insufficient evidence". **Judgment call:** on the strict reading, the classic version has 3 tests, which meets the threshold numerically, but the current product has 0. On the loose reading, the count is 4.

## Proposed score breakdown
None (recommended).

**Alternative, if the entry is scoped to classic v0.x only (judgment calls):**
- **Completion: 40** — no direct task-success test of Open Interpreter itself.
- **Disputes: 70** — no CVEs or lawsuits, but security reports were closed unresolved.
- **Adherence: 30** — high attack success in tests; protections are opt-in.
- **Evidence: 45** — preprints and self-published repositories.
- **Math:** 0.3×40 + 0.2×70 + 0.25×30 + 0.25×45 = 12 + 14 + 7.5 + 11.25 = 44.75, rounded to **45**. The grade would come from the methodology table.

## Risks/uncertainties
- Ambiguity over which product the name refers to.
- Model choice dominates results.
- The fix status of the security reports is unknown.
- The GHSA IDs are private and unverifiable.
- I found no journalism with original testing.

## Recommendation
Publish as **Insufficient evidence**.

Proposed public wording: "Open Interpreter is an open-source agent that runs code on the user's computer from natural-language instructions. Its repository now tracks a rewrite built on Codex; the earlier Python version continues in a community fork. Independent security studies, mostly preprints and self-published projects, tested the earlier Python version; we found no independent evaluation of the current product, so no overall score is given. Insufficient evidence. Informational only; not an endorsement or certification."

## Plain-English terms
- **auto_run / -y:** runs code without asking first.
- **Prompt injection:** hidden instructions placed in content the agent reads.
- **Preprint:** a paper that has not been peer-reviewed.

> **Erratum (Decision 0010, 2026-10-16):** methodology.html had no evidence-grade table when this packet was written; grades were assigned by comparison with similar entries. The table was added in Scoring rules v0.1 (Decision 0010); the hypothetical grade mentioned here was never used; the entry remains Insufficient evidence.
