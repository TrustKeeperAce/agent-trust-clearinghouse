# Decision 0007: Julius AI (AI data-analysis agent)

**Status: APPROVED by Remington, 2026-10-16.** Publish as "Insufficient evidence", with no overall score, using the proposed public wording exactly.

**Deferred:** a methodology clarification on what counts as an independent performance source has been deferred. The methodology page is unchanged.

## Final public summary
"Julius AI is a commercial AI data-analysis tool that generates and runs code from natural-language prompts. Public evidence consists mainly of vendor materials, benchmarks published by competing products, and a small number of limited independent studies, including one peer-reviewed comparison that tested Julius with code execution disabled. We found fewer than three independent evaluations of its computed answers, so no overall score is given. Insufficient evidence. Informational only; not an endorsement or certification."

---


## Draft entry summary
Proposed: **Insufficient evidence**, no overall score. Two independent performance sources exist, and both are limited. There is one peer-reviewed comparison, but it tested Julius with code execution disabled. The other is a single-prompt observation in an education journal.

## What happened
- **Applied Sciences (MDPI) 2026 (peer-reviewed; venue confirmed via Crossref):**
  - Julius scored 85.7% accuracy vs 89.3% for GPT-4o on 45 bibliometric tasks, each run with 5 prompt styles.
  - Julius's code execution was disabled, so the result does not reflect how the product normally runs.
  - **Judgment call:** the paper has internal inconsistencies. Its tests are dated Jan–Mar 2024, yet it cites a GPT-4o version from May 2024, and it names a "Python 3.15" environment that doesn't exist.
- **Ohio Journal of School Mathematics 2025:**
  - One multiplication prompt. Julius reached the correct product via Python.
  - Its written step-by-step explanation contained arithmetic errors, yet it stated "The calculation is correct". This is relevant to hallucinated reasoning.
- **Other independent sources (not performance tests):**
  - Discover Education 2024: a tutorial whose author says the prompts "worked just as well" on Julius. Not a correctness test.
  - A 2026 quasi-experiment with 40 graduate students, listed under Veredas do Direito, a law and environment journal (an unusual fit). The DOI link returned 404.
  - A CASRAI guidance article advising users to verify test choice and assumptions and to export code.
  - A student REU poster (403; snippet only).
- **Competitor benchmarks:** Rows reports Julius at 75% on first try; Basedash reports 46.1% on its own BI benchmark. Both publish benchmarks of their own competing products, so they are not independent.
- **Academic data-agent benchmarks:** I found no sign that Julius was evaluated in DSBench, DA-Code, InfiAgent-DABench or BLADE.
- **Vendor statements:**
  - Data is not used to train models.
  - Storage is in the US.
  - SOC 2 Type II and TX-RAMP compliance is claimed.
  - Files are deleted after 1 hour of inactivity on the free tier and 7 days on paid plans.
  - Usage is limited by credits, which replaced message caps in 2026.
- **Disputes:** none found.

## Sources checked
| Source | Type | Status |
|---|---|---|
|MDPI Applied Sciences 2026|Independent performance (peer-reviewed; limited)|403 to curl; read via fetch|
|Ohio J. School Math 2025|Independent performance (one item)|200|
|Discover Education 2024|Other independent|200 (Julius detail from snippet)|
|Veredas do Direito 2026|Other independent (venue mismatch)|DOI 404|
|CASRAI guide|Other independent (guidance)|200|
|USF REU poster|Other independent (student)|403|
|Rows; Basedash|Competitor benchmark|200|
|DA-bench listing|Unknown operator; no score|200|
|beehiiv newsletter|Anecdotal|200|
|G2; Trustpilot|Anecdotal aggregates|403; not used|
|julius.ai privacy, security, files, credits, policy|Vendor|200|

## Evidence quality assessment
Weak. No study tests the product as normally used, with code execution on. Competitor benchmarks have an obvious conflict of interest. The vendor's code-visibility and privacy claims are stated by the vendor and have not been audited independently.

## What the rules say
Fewer than 3 independent sources means "Insufficient evidence" and no overall score. **Judgment call:** I count 2 independent performance sources, and both are limited. If the other independent sources were counted, the total could reach 3 or more, but none of them measures correctness. I recommend following the stricter reading, as we did for Pactum.

## Proposed score breakdown
None.
- **Completion/correctness:** only the limited sources above.
- **Disputes:** none found.
- **Adherence to limits:** the vendor documents credits and retention; not tested.
- **Evidence:** low.

## Risks/uncertainties
- The MDPI paper's inconsistencies.
- The product changes fast; credit-based billing started in 2026.
- The Veredas venue is unusual and its DOI didn't resolve.
- G2 and Trustpilot were unverified.
- The benchmark search was not exhaustive.

## Recommendation
Publish as **Insufficient evidence**.

Proposed public wording: "Julius AI is a commercial AI data-analysis tool that generates and runs code from natural-language prompts. Public evidence consists mainly of vendor materials, benchmarks published by competing products, and a small number of limited independent studies, including one peer-reviewed comparison that tested Julius with code execution disabled. We found fewer than three independent evaluations of its computed answers, so no overall score is given. Insufficient evidence. Informational only; not an endorsement or certification."

## Plain-English terms
- **Code execution disabled:** Julius answered without running its usual Python code.
- **Competitor benchmark:** a test published by a rival product's company.
- **Pass@1:** correct on the first try.
