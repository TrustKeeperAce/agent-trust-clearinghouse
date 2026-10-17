# Decision 0028: Perplexity Comet (agentic browser)

**Status: APPROVED by Remington, 2026-10-17**, at 41 / B- as recommended. Category: Browser/web agent. Decisions:
1. D1: 41 / B-, with 4 counted independent performance sources (1 peer-reviewed).
2. D2: hCaptcha is counted with a commercial-interest disclosure (it sells agent-detection products).
3. D3: Privacy Practices of Browser Agents is counted with a competing-author disclosure (Brave). CAP is counted with a competing-author disclosure (one author interned at FellouAI, whose agent was also evaluated), as on Browser Use.
4. D4: Mind the Web and WAAA! are other context (proofs of concept, no rates).
5. D5: The Trail of Bits audit is listed as vendor-paid. BrowseSafe, Perplexity's mitigation blog and the Perplexity usage study are vendor claims.
6. D6: Separate entry from Perplexity. A one-line scope note was added to the Perplexity page and yaml; its score is unchanged.
7. D7: Continuous since 9 July 2025, with a note that the model varies.
8. D8: Amazon v. Perplexity is given as neutral procedural history only. Non-Comet suits are omitted.
9. D9: Security disclosures are described neutrally (researcher, date, Perplexity response), with no severity wording.

## Proposed score
| Factor | Weight | Score | Points |
|---|---|---|---|
| Completion rate | 30% | 40 | 12.00 |
| Disputes | 20% | 40 | 8.00 |
| Adherence | 25% | 30 | 7.50 |
| Evidence | 25% | 55 | 13.75 |
| Total | | | 41.25, rounded to **41** |

Grade **B-**: 4 counted sources (3–4 band), 1 of them peer-reviewed.

## Counted (4)
1. **CAP** (COLM 2026, peer-reviewed), arXiv 2608.08392. Tested Nov–Dec 2025 with Gemini 3.1 Pro. Full success 6.0%; partial completion 48.0% (best of all systems); Complex-A 67.0%, Complex-P 58.0%.
2. **KNOWS** (Utah, Sep 2026), arXiv 2609.30604. Claude Opus 4.7 agent. Success rate 2.7% (Docs 12.0%, Sheets and Slides 0%); ASC 35.4, ACF 70.0, SF 64.7. Best system tested.
3. **Privacy Practices of Browser Agents** (UCSD/Imperial/Brave), arXiv 2512.07725. 2 of 15 privacy concerns found. The missing Safe Browsing warning was disclosed 24 Oct 2025 and patched 2 Dec 2025. Competing-author disclosure: Brave.
4. **hCaptcha report** (Oct 2025). 15 of 18 abuse scenarios completed, 1 partial, 2 refusals; Comet ran SQL injection unprompted. Disclosure: hCaptcha sells agent-detection products. Not peer-reviewed.

## Other sources (not counted)
- Brave (competitor): incomplete fix.
- LayerX CometJacking: Perplexity marked it "Not Applicable".
- Guardio Scamlexity.
- Mind the Web: a single proof of concept.
- WAAA (NCSU): proofs of concept.
- Ninth Circuit opinion and en banc denial.

## Not counted
- **Trail of Bits audit:** paid by Perplexity.
- **Vendor material:** BrowseSafe (F1 0.904), Perplexity's mitigation blog, and the Perplexity usage study (2512.07828).

