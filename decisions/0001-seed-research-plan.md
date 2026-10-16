# Decision 0001 — Seed research plan (8 candidates)

- **Status:** Proposed — awaiting Remington's approval
- **Date:** 2026-10-16 (America/New_York)
- **Scope:** A *plan* for what to research. This packet contains no agent entries, no scores, and no evaluations.

> **Privacy rule:** All research drafts produced under this plan stay private. They are not committed to this public repo and not published on the site until Remington approves each resulting decision packet.

## 1. What happened (facts + sources)
We need a small seed set across the five Phase 1 categories. Eight candidates were proposed. Light existence checks only (public footprint / maintenance), done 2026-10-16 via the GitHub API:

| # | Candidate | Category | Type | Quick existence check (2026-10-16) |
|---|---|---|---|---|
| 1 | OpenAI Deep Research | Research | Commercial | Public product with official OpenAI docs/announcements (not re-checked in depth). |
| 2 | GPT Researcher (`assafelovic/gpt-researcher`) | Research | Open source | Repo active: last push 2026-10-10, latest release v3.7.0 (2026-09-26), ~30k stars, not archived. Source: https://github.com/assafelovic/gpt-researcher |
| 3 | Loki / OpenFactVerification (`Libr-AI/OpenFactVerification`) | Verification | Open source | **Looks unmaintained:** last push 2024-10-03, latest release v0.0.2 (2024-04-21); not archived, ~1.2k stars. Source: https://github.com/Libr-AI/OpenFactVerification |
| 4 | Perplexity | Verification | Commercial | Public citation-backed answer engine (not re-checked in depth). |
| 5 | Pactum | Negotiation | Commercial | Public company site; evidence expected to be mostly vendor case studies. |
| 6 | Clay | Data enrichment | Commercial | Public product with docs and review-site listings (not re-checked in depth). |
| 7 | Julius AI | Simple analysis | Commercial | Public product (not re-checked in depth). |
| 8 | Open Interpreter | Simple analysis | Open source | Repo active: GitHub now resolves to `openinterpreter/openinterpreter`; last push 2026-10-11, latest release rust-v0.0.56 (2026-10-07), ~69k stars. Source: https://github.com/openinterpreter/openinterpreter |

### Per-candidate plan

**1. OpenAI Deep Research — Research**
- *Why it qualifies:* Autonomous multi-step web research agent producing cited reports; a digital task with checkable outputs.
- *Sources to check:* Official docs/system card/changelog; published benchmarks where applicable (BrowseComp, Humanity's Last Exam, GAIA); independent tests and news coverage; academic papers evaluating deep-research agents.
- *Flags:* Many headline benchmark numbers are vendor-reported — count them as vendor claims unless independently reproduced. Product changes often; pin review dates.

**2. GPT Researcher — Research**
- *Why it qualifies:* Widely used open-source autonomous research agent; transparent code and issue history.
- *Sources to check:* GitHub releases, issues (bug/failure reports as dispute signals), docs; independent benchmarks or papers citing it; independent blog tests.
- *Flags:* Results depend heavily on the underlying LLM and configuration the user chooses; must state which setup evidence refers to.

**3. Loki / OpenFactVerification — Verification**
- *Why it qualifies:* Open-source automated fact-verification pipeline (claim decomposition → evidence retrieval → verdict).
- *Sources to check:* GitHub repo/issues/releases, the associated paper, any independent evaluations.
- *Flags:* **Appears unmaintained** (no push since Oct 2024; last release Apr 2024). Likely thin independent evidence. Proposed swap below.

**4. Perplexity — Verification (narrow scope)**
- *Why it qualifies:* Answer engine that returns citation-backed answers; relevant to "find and cite sources for a claim."
- *Sources to check:* Official docs/changelog; independent citation-accuracy studies (e.g., academic and journalism studies of AI search citation accuracy); independent reviews (G2/Capterra); news coverage, including publisher disputes.
- *Flags:* It is a **general answer engine, not a dedicated verification agent** — scope the entry narrowly to citation-backed answering / source attribution. Publisher legal disputes exist in the news; record as facts with sources, without characterization.

**5. Pactum — Negotiation**
- *Why it qualifies:* Commercial autonomous procurement-negotiation agent.
- *Sources to check:* Company site and case studies (vendor), independent news/analyst coverage, academic work on AI negotiation, independent reviews if any.
- *Flags:* **Thin-evidence flag** — public evidence is mostly vendor case studies. Expected outcome: "Insufficient evidence" (fewer than 3 independent sources), which is a useful worked example of the rule.

**6. Clay — Data enrichment**
- *Why it qualifies:* Data-enrichment platform with AI research agent features for filling in company/contact data.
- *Sources to check:* Official docs/changelog; G2/Capterra reviews; independent tests/news; data-accuracy comparisons.
- *Flags:* Partly a workflow tool rather than a pure agent — scope to its AI agent/enrichment features. Reviews may mix product UX with agent performance; data-privacy/compliance questions should be noted as uncertainties, not judged.

**7. Julius AI — Simple analysis**
- *Why it qualifies:* AI agent for data analysis/charting on user-supplied files.
- *Sources to check:* Official docs/changelog; G2/Capterra and other independent reviews; independent tests; any benchmark mentions.
- *Flags:* Likely limited independent, rigorous testing; risk of reliance on vendor marketing and anonymous anecdotes.

**8. Open Interpreter — Simple analysis**
- *Why it qualifies:* Open-source agent that runs code locally to complete analysis and computer tasks.
- *Sources to check:* GitHub releases/issues, docs, independent tests/reviews, papers citing it.
- *Flags:* Repo appears to have moved/renamed and shifted toward a Rust rewrite — confirm which product version the evidence covers. Executes code on the user's machine: adherence-to-limits evidence is especially important. Outcomes depend on chosen LLM.

## 2. What the rules say
- Scoring rules v0: Completion rate 30%, Disputes 20% (fewer = higher), Adherence to limits 25%, Evidence quality 25% (independent third-party high, vendor claims low, anonymous anecdotes lowest). Each factor 0–100 shown separately plus weighted overall.
- Fewer than 3 independent sources ⇒ "Insufficient evidence" and no overall score.
- Informational only: no guarantees, endorsements, certifications, or verification beyond what is stated; no payments; the Clearinghouse is not responsible for outcomes.
- Nothing is published without an approved decision packet.

## 3. Risks / uncertainties
- Vendor-reported benchmarks may be mistaken for independent evidence — must be classified carefully.
- Products change fast; scores can go stale. Each entry needs a "last reviewed" date.
- Open-source agents' quality depends on user-chosen models/configs.
- Category fit is imperfect for Perplexity (general answer engine) and Clay (platform with agent features).
- Loki appears unmaintained; scoring it may describe an abandoned project.
- Mentioning disputes/legal matters carries reputational/defamation risk — stick to sourced facts, neutral wording.
- The quick checks above confirm public footprint only; they are not evaluations.

## 4. Recommendation
**Approve the plan, with these adjustments:**
1. Proceed with research on candidates 1, 2, 4, 5, 6, 7, 8.
2. Keep **Pactum** in the set as the expected **"Insufficient evidence"** example.
3. Scope **Perplexity** narrowly to citation-backed answering / source attribution.
4. **Loki / OpenFactVerification looks unmaintained** (no activity since Oct 2024). Propose swapping it for **Google DeepMind SAFE (Search-Augmented Factuality Evaluator, `google-deepmind/long-form-factuality`)** — active (last push 2026-06-18), with a published paper. Caveat: SAFE is closer to an evaluation method than a user-facing agent, so if Remington prefers, keep Loki and label it as unmaintained. Needs Remington's choice.
5. All research drafts stay private (not committed, not published) until Remington approves each entry's packet.

Reasons: covers all five categories with commercial and open-source mixes, includes a deliberate thin-evidence test case, and avoids spending effort on a likely abandoned project.

## 5. Plain-English terms
- **Agent:** AI software that carries out multi-step digital tasks on its own.
- **Independent source:** Evidence from someone with no stake in the product (e.g., researchers, journalists, independent testers).
- **Vendor claim:** Something the product's maker says about itself.
- **Benchmark (GAIA, BrowseComp):** Standard test sets used to compare AI agents on research/browsing tasks.
- **Unmaintained:** No recent updates or fixes from the project's developers.
- **Insufficient evidence:** We found fewer than 3 independent sources, so we don't give an overall score.
- **Decision packet:** A short document like this one that lays out facts, rules, risks and a recommendation for approval.
