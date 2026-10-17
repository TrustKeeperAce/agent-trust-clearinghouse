# Decision 0005: Pactum

**Status: APPROVED by Remington, 2026-10-16.** Publish as "Insufficient evidence", with no overall score, using the 0005b proposed public wording exactly.

## Final public summary
"Pactum is a commercial procurement-negotiation agent. Public evidence consists mainly of vendor materials, a 2022 Harvard Business Review case study co-written by Walmart executives and university researchers (64% supplier agreement in a pilot), and a 2026 master's thesis analysing 148 negotiations at one customer (64.9% agreement; about half of agreements included a discount, with a median discount of zero; suppliers rated the process more favourably than the outcome). We found fewer than three independent evaluations, so no overall score is given. Insufficient evidence. Informational only; not an endorsement or certification."

---

## Part A: Initial packet (0005)
Accessed 2026-10-16.

## Draft entry summary
Pactum is a commercial product in the Negotiation category. Proposed status: **Insufficient evidence**, with no overall score. I found **0 verified independent performance sources** and 4 other independent sources (3 journalism, 1 law review), none of which has original outcome data.

## What happened
- **HBR (Nov 2022):** written by two Walmart International executives and two University of Arkansas professors. It reports the Walmart Canada pilot:
  - Agreement with 64% of invited tail-end suppliers, against a 20% target.
  - 11-day average turnaround.
  - 83% of suppliers who reached agreement described the system as easy to use.
- **Later figures** (68% close rate, 3% savings) come from Pactum, as restated by PON and the Arkansas Democrat-Gazette.
- **The vendor site today** describes "digital workers" for indirect procurement that follow a customer "rulebook". It says "Your team makes the final call", and claims 11% and 5.2% average savings (vendor claims).
- **Disputes:** none found (no lawsuits, regulatory actions or formal complaints). The only criticism is an anonymous forum post describing take-it-or-leave-it binary terms.

## Sources checked
| Source | Type | Shows | URL |
|---|---|---|---|
|HBR 2022|Customer-coauthored (not independent)|Pilot outcomes|hbr.org/2022/11/how-walmart-automated-supplier-negotiations|
|PON Harvard|Secondary summary|Restates HBR|pon.harvard.edu/…chatbot-negotiations…|
|Arkansas Democrat-Gazette|Journalism (restates)|Vendor figures; Lacity quote|arkansasonline.com/news/2023/may/04/…|
|IEEE Spectrum|Journalism (descriptive)|Product description|spectrum.ieee.org/ai-contracts|
|BBC 2021|Journalism (descriptive)|Walmart test, CEO quotes|bbc.com/news/business-55738540|
|Hofstra Law Review 2025|Legal commentary|Regulatory questions|hofstralawreview.org/…AA.3.Steward.pdf|
|RollOnFriday forum|Anonymous anecdote|Supplier-side complaint|rollonfriday.com/discussion/…|
|pactum.com|Vendor|Claims, guardrails|pactum.com|

**Not counted:**
- A BTH thesis using 148 Pactum cases. It is visible only as a search snippet and its page is behind a bot check. The snippet says 64.9% agreement, but median discount 0.
- Bloomberg Businessweek (paywalled, 403).
- An HBP/Thunderbird teaching case (paid).

## Evidence quality assessment
The only primary outcome data was co-written by the customer's own executives, together with academics. Everything else either restates those figures or vendor figures, or is anecdotal. I found no peer-reviewed independent study of Pactum. The two peer-reviewed procurement-chatbot papers I found test other systems: a custom ChatGPT bot (JPSM 2025) and a field experiment (MSOM 2022).

## What the rules say
With fewer than 3 independent sources, the entry is marked "Insufficient evidence" and gets no overall score. Factor notes are allowed.

## Proposed score breakdown
None.
- **Completion:** pilot agreement of 64%, from a customer-coauthored source; no independent replication.
- **Disputes:** none documented; this is weak evidence, given how thin the coverage is.
- **Adherence:** the vendor and an HBR coauthor say it stays within buyer-set trade-offs; untested.
- **Evidence:** low.

## Risks/uncertainties
- The product has changed: from a chatbot (2021) to multi-agent procurement software (2026).
- Promising thesis data is unverified.
- Paywalled journalism was not reviewed.
- Do not present vendor savings figures as findings.

## Recommendation
**More info (or publish as "Insufficient evidence").** Before revisiting the score:
1. Retrieve the BTH thesis PDF by browser.
2. Read the Bloomberg piece and the HBP case.
3. Search for independent peer-reviewed field studies.

If published now, proposed wording: "Pactum is a commercial procurement-negotiation agent. Public evidence consists mainly of vendor materials and a 2022 Harvard Business Review case study co-written by Walmart executives and university researchers, which reported agreements with 64% of invited suppliers in a pilot. We found fewer than three independent evaluations, so no overall score is given. Insufficient evidence. Informational only; not an endorsement or certification."

## Plain-English terms
- **Tail-end suppliers:** many small suppliers that are rarely renegotiated.
- **Customer-coauthored:** written partly by the client's own staff.
- **Insufficient evidence:** too few independent sources to score.

---

## Part B: More-info follow-up (0005b)
Accessed 2026-10-16. Supersedes the 0005 assessment where they differ.

## Draft entry summary
Pactum is a commercial product in the Negotiation category. Status remains **Insufficient evidence**, with no overall score. Independent performance sources: **1, and it is only partly independent** (an unreviewed master's thesis). There are also 4 other independent sources (journalism and a law review) and 1 teaching-case abstract; none has original outcome data.

## What happened (new evidence)
**1. BTH master's thesis.** Nordenhög, Blekinge Institute of Technology, May 2026, diva2:2063902. Advisor: senior lecturer Maryna Brychko.
- **Data:** a single case at an anonymised "company X", a Pactum customer that has used it since Dec 2025, procurement module only.
  - 148 concluded negotiation cases from Pactum system logs, linked to company X's ERP data.
  - The thesis says the data was "provided by the organization" (the customer), not by Pactum.
  - I found no acknowledgements, funding statement, conflict-of-interest declaration or disclosure of the author's relationship to company X.
- **Results:**
  - **Outcomes:** agreement in 96 of 148 cases (64.9%); 50 expired and 2 were declined.
  - **Discounts:** 47 agreements had a positive discount, 48 had zero and 1 was negative. Median discount and median savings were 0. Mean discount was 3.84% and mean savings USD 203.93 per case. The worst case was −21.93% (−USD 4,422.44), which the thesis explains as a baseline taken from another supplier.
  - **Concentration:** the top 5 cases produced 63.15% of positive savings.
  - **Cycle time:** median 1.69 h, mean 33.41 h, maximum 602.57 h.
  - **Execution:** 83.3% of agreements could be matched to ERP purchase records. The thesis says the unmatched 16.7% may reflect data limitations rather than execution failure.
  - **Supplier view:** voluntary scores from 60 agreement cases, mean feedback 3.52/5 and mean outcome satisfaction 2.70/5.
- **The author's stated limitations:**
  - Single case, early implementation period.
  - The regressions have low explanatory power.
  - Supplier scores are voluntary and sparse.
  - Results are not generalisable, and the analysis makes no causal claims.
  - The thesis reports no guardrail failures.

**2. Bloomberg Businessweek (2023-04-26):** only the dek is visible: "…the retail giant is wringing more savings from contracts." Not counted.

**3. HBP teaching case TB0756** (Thunderbird; Youngdahl, Patel, Shah, Sutton; 2025-02-17). The free abstract mentions efficiency gains, cost savings and higher supplier engagement, but also difficulty maintaining supplier relationships and balancing automation against personal contact. It is a teaching case and the full text was not reviewed, so it is not counted as performance evidence.

## Sources checked
| Source | Type | Shows | URL |
|---|---|---|---|
|BTH thesis 2026|Partly independent, performance (not peer-reviewed; customer-provided data)|148-case outcomes|bth.diva-portal.org/smash/get/diva2:2063902/FULLTEXT01.pdf|
|HBR 2022|Customer-coauthored|Walmart pilot: 64% agreement|hbr.org/2022/11/how-walmart-automated-supplier-negotiations|
|HBP TB0756 abstract|Teaching case (abstract only)|Benefits and relationship challenges|hbsp.harvard.edu/product/TB0756-PDF-ENG|
|Bloomberg 2023|Journalism (dek only)|n/a|bloomberg.com/news/articles/2023-04-26/…|
|PON, Arkansas Democrat-Gazette, IEEE Spectrum, BBC|Journalism and secondary|Restate HBR/vendor figures or describe the product|(see 0005)|
|Hofstra Law Review|Legal commentary|Regulatory questions|(see 0005)|
|RollOnFriday|Anonymous anecdote|Supplier complaint|(see 0005)|
|pactum.com|Vendor|Claims; "your team makes the final call"|pactum.com|

## Evidence quality assessment
The thesis is the first evidence not written by Pactum or by the customer's own staff. It is careful and shows both the positive and the null results. But it is a student thesis, not peer-reviewed, built on one customer's data for 148 cases, and it discloses nothing about affiliations or funding. Its figures differ from the vendor's: median discount 0% versus a vendor-stated 5.2% average on single-source deals (and the vendor's figure is an average, not a median). No other independent performance evaluation was found.

## What the rules say
Fewer than 3 independent sources means "Insufficient evidence" and no overall score. With only 1 partly independent performance source, the threshold is not met.

## Proposed score breakdown
None. Factor notes:
- **Completion:** agreement 64.9% (thesis) and 64% (customer-coauthored HBR pilot); 34% of thesis cases expired.
- **Disputes:** none documented.
- **Adherence:** vendor-described buyer rulebook and human final award; untested independently.
- **Evidence:** low to moderate.

## Remaining risks
- Author independence from company X is unknown.
- One customer, early period, procurement module only.
- The product changed between 2021 and 2026.
- Paywalled and teaching-case content was not reviewed.
- Do not present vendor savings figures as findings.
- Do not frame the thesis's median-zero result as a failure: the author interprets it cautiously.

## Recommendation
**Publish as "Insufficient evidence" (no score)**, or keep it private pending more independent studies.

Proposed public wording: "Pactum is a commercial procurement-negotiation agent. Public evidence consists mainly of vendor materials, a 2022 Harvard Business Review case study co-written by Walmart executives and university researchers (64% supplier agreement in a pilot), and a 2026 master's thesis analysing 148 negotiations at one customer (64.9% agreement; about half of agreements included a discount, with a median discount of zero; suppliers rated the process more favourably than the outcome). We found fewer than three independent evaluations, so no overall score is given. Insufficient evidence. Informational only; not an endorsement or certification."

## Plain-English terms
- **Median zero:** at least half of the agreements produced no discount.
- **ERP match:** the agreed deal shows up in the company's purchase records.
- **Expired:** the supplier didn't finish the negotiation.
- **Partly independent:** written by an outsider, but using data supplied by the customer.
