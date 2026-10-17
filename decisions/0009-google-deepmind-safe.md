# Decision 0009: Google DeepMind SAFE (Search-Augmented Factuality Evaluator)

**Status: APPROVED by Remington, 2026-10-16.** Publish with overall score 66, evidence grade B-, using the proposed public wording exactly.

## Final public summary
"SAFE (Search-Augmented Factuality Evaluator) is open research code from Google DeepMind, described in a NeurIPS 2024 paper, that uses a language model and Google Search results to rate individual facts in long-form text. The authors report 72% agreement with crowdsourced annotators. Independent peer-reviewed studies report agreement with human annotators of about 84% on biography facts and strong correlation on factual labels, alongside weaker results for its claim extraction; these studies were conducted by researchers proposing alternative methods. Commentators have questioned the authors' comparison with crowdworkers rather than expert fact-checkers. Overall score 66. Informational only; not an endorsement or certification."

---

Accessed 2026-10-16. Category: Verification. Research evaluator, not a consumer product.

## Draft entry summary
SAFE is scoreable: there are 3 independent peer-reviewed studies that test its behaviour. Proposed overall score: **66**. All 3 come from authors proposing competing evaluators (judgment flag).

## What happened
**Authors' claims (NeurIPS 2024; venue confirmed from the proceedings PDF):**
- 72.0% agreement with crowdsourced labels on 16,011 facts.
- On 100 sampled disagreements, SAFE was correct 76% of the time (re-labelled by the authors).
- Cost of $0.19 per response, about 20 times cheaper than crowdsourcing.

**Independent studies:**
- **Zhao et al. (Findings of ACL 2025):**
  - 84.48% agreement with internet-enabled annotators on 786 biography facts.
  - Measured cost of $0.49 per response and about 28 minutes per response.
- **FactBench (ACL 2025):** compared with human labels on 160 responses, SAFE's response-level Pearson correlation was 0.95 on factual labels and 0.60 on other labels.
- **VeriScore (Findings of EMNLP 2024):**
  - In a pairwise human study, raters preferred SAFE's extracted claims only 26 of 360 times.
  - It critiques SAFE for extracting unverifiable claims and for relevance checks that drop relevant claims.

**Critique:** VentureBeat and ForkLog report Gary Marcus's view that "superhuman" means better than crowdworkers, not expert fact-checkers.

**Disputes:** none beyond this academic critique.

**Maintenance:**
- Official research code; the repo is not archived, and its last push was 2026-06-18.
- Licensing: code Apache-2.0, other materials CC-BY, bundled FActScore code MIT.

## Sources checked
| Source | Type | Status |
|---|---|---|
|NeurIPS 2024 paper|Authors (vendor) claims|200|
|Findings ACL 2025.161|Independent behaviour|200|
|ACL 2025 long 1587 (FactBench)|Independent behaviour|200|
|Findings EMNLP 2024.552 (VeriScore)|Independent behaviour|200|
|VentureBeat|Journalism/critique|429 (rate limit); search index|
|ForkLog|Journalism/critique|200|
|GitHub repo, README, LICENSE|Authors|200|
|Godbole & Jia, Findings ACL 2025|Checked; excluded (does not test SAFE)|200|

## Evidence quality assessment
Good venues, but narrow coverage:
- Samples are small (786 facts; 160 responses; 360 items).
- The domains are mainly biographies and chat prompts.
- Each independent study promotes its own alternative method.

## What the rules say
The rules need at least 3 independent sources. The strict and loose readings agree: 3 under each. The paper's 72% and 76% figures are the authors' own claims.

## Proposed score breakdown (judgment calls)
- **Completion / rating accuracy: 65.** Independent agreement and correlation are good on factual labels (84%; Pearson 0.95). Results are weaker on other labels (0.60) and for claim extraction.
- **Disputes: 80.** No legal disputes. Public critique of the "superhuman" framing.
- **Adherence to limits: 60.**
  - Clear licences and stated limitations; it is maintained research code.
  - Independently measured cost ($0.49 per response) is higher than the authors' $0.19, though the setups differ.
- **Evidence quality: 60.** 3 peer-reviewed sources, but small samples and authors who promote competing methods.

**Math:** 0.30×65 + 0.20×80 + 0.25×60 + 0.25×60 = 19.5 + 16 + 15 + 15 = 65.5, rounded half up to **66**. The grade comes from the methodology table; OpenAI Deep Research scored 65 and received B.

## Risks/uncertainties
- Results depend on which LLM SAFE runs with and on the Serper search API.
- The cost figures aren't directly comparable.
- VentureBeat could only be read through the search index.
- I found no independent study using expert fact-checkers.

## Recommendation
Publish with an overall score of **66**.

Proposed public wording: "SAFE (Search-Augmented Factuality Evaluator) is open research code from Google DeepMind, described in a NeurIPS 2024 paper, that uses a language model and Google Search results to rate individual facts in long-form text. The authors report 72% agreement with crowdsourced annotators. Independent peer-reviewed studies report agreement with human annotators of about 84% on biography facts and strong correlation on factual labels, alongside weaker results for its claim extraction; these studies were conducted by researchers proposing alternative methods. Commentators have questioned the authors' comparison with crowdworkers rather than expert fact-checkers. Overall score 66. Informational only; not an endorsement or certification."

## Plain-English terms
- **Agreement:** the share of facts where SAFE's label matches the humans' label.
- **Pearson correlation:** how closely scores move together (1 means a perfect match).
- **Claim extraction:** splitting text into individual checkable statements.
