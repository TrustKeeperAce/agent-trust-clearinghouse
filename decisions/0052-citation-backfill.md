# Decision 0052: Citation backfill

**Status: APPROVED by Remington, 2026-10-17**, as recommended: D1 SWE-agent moved to its own packet (0053); D2 B1 OpenHands Sifting the Noise row (12 counted, 7 peer-reviewed, A, scores unchanged); D3 B4 Aider decision-record note; D4 B2 Claude Code WideSWE and Timeline-Bench rows (17 counted, 6 peer-reviewed, A, scores unchanged); D5 Elicit moved to its own packet (0054); D6 B3 recheck note on 13 entries; D7 follow-up order as listed in Part 4. No score or grade changes. Part of the consistency pass.

**Aider note (B4):** Test dates firmed up via the commit and release dates of the other tested agents (Dec 2025).

## Search method note
- Semantic Scholar: tried for about 5 minutes (9 tries, 22:19 to 22:24 ET). Every try returned HTTP 429 (rate limited), so it gave no results.
- OpenAlex: used as the fallback. It ran 1 or 2 searches per entry, limited to items published from 2025-01-01, with up to 25 hits per search. That came to 812 hits across the 20 entries.
- Screening: hits were screened by title against each entry's existing sources. Full reads were done only for items that could change a score or grade, and only where time allowed. Those were Sifting the Noise, WideSWE and Timeline-Bench, plus OpenAlex abstracts for the Elicit papers.
- Plain terms:
  - "Counted" means an independent test that counts toward the evidence grade.
  - "Peer-reviewed" means it was published in a reviewed journal or conference.
  - "Score could change" means the new finding might move one of the four factor scores.

## Part 1: 0051 D7 flags

D1. SWE-agent: Sifting the Noise (ISSTA 2026, doi 10.1145/3832100)
- Search: done earlier (0051 D7). This draft read the full text.
- What it tested: SWE-agent at commit 1d3cfb798a2c, dated 2025-12-05 on GitHub, so inside the 12-month window. Models were Claude Sonnet 4, GPT-5 and DeepSeek Chat.
- Task: deciding whether static-analysis warnings are real or false positives.
- Results:
  - OWASP false-positive rate with Claude Sonnet 4 was 6.3%, the best in the study. It was 14.1% with GPT-5 and 13.1% with DeepSeek.
  - On post-cutoff OSS-Fuzz, SWE-agent with Claude Sonnet 4 found 95.5% of false positives, with 95.5% precision.
- Independence: no developer co-authors were found.
- Effect if counted: 9 → 10 counted, 7 → 8 peer-reviewed, and now a recent test that states the version. That meets every Grade A condition, so the grade would go B → A.
- Score: the completion or adherence notes could change. Evidence 80 sits in the B band and must not be fitted to the grade.
- Recommendation: FLAG FOR ITS OWN PACKET (0053). It changes the grade, so do not batch it here.

D2. OpenHands: Sifting the Noise (same paper)
- What it tested: OpenHands Agent SDK v1.5.2, released 2025-12-11.
- Results: OWASP false-positive rate was 14.9% with Claude Sonnet 4, 16.3% with GPT-5 and 15.8% with DeepSeek. That is mid-pack in the study.
- Effect: 11 → 12 counted, 6 → 7 peer-reviewed. The grade stays A.
- Score: unlikely to change. It is a narrow security-triage task, in line with the existing results.
- Recommendation: BATCH IN 0052 (wording below).

D3. Aider: Sifting the Noise (already counted in 0051)
- The test dates are now firmer: the SWE-agent commit is dated 2025-12-05 and the OpenHands SDK was released 2025-12-11. Both support the 0051 inference that the Aider v0.86.1 runs fall inside the 12-month window.
- Effect: none on counts, scores or grade.
- Recommendation: an optional one-clause addition to the Aider decision-record note. No page change is needed.

D4. Claude Code: WideSWE (arXiv 2609.33382) and Timeline-Bench (arXiv 2609.35143)
- Independence:
  - WideSWE is by Zhejiang University and Tsinghua University authors.
  - Timeline-Bench is by TensorTest (Ritivel Labs Inc.).
  - Neither has Anthropic authors or stated Anthropic funding.
  - Both are preprints, so not peer-reviewed.
- WideSWE: cross-repository tasks, 120 tasks over 253 repositories. Claude Code configurations fully solved 10.83% to 37.50%. The top result was Codex CLI with GPT-5.6-sol at 42.50%. Claude Code (with Claude Opus 5 and other models) states its version as v2.1.139.
- Timeline-Bench: 56 video-editing tasks, using Claude Code 2.1.278.
  - Claude Opus 5 resolved 23.2% (13/56), second of 16 agents.
  - Claude Fable 5.1 resolved 17.9% (10/56).
  - Agents claimed full success in 93% of runs, including 95.5% of edits that failed a test.
- Effect: 15 → 17 counted. Peer-reviewed stays at 6. The grade stays A.
- Score: completion is unlikely to change, since both results show partial success on long tasks, as the current notes already say. The Timeline-Bench over-claiming finding is worth one sentence.
- Recommendation: BATCH IN 0052 (wording below).

D5. Elicit: four candidates (abstracts read via OpenAlex; full text not read)
- Mazzali 2026, BMC Med Res Methodol (10.1186/s12874-026-02892-3):
  - Search overlap was 8%.
  - Screening recall was 90.9% at title/abstract, with 42.9% precision.
  - Full-text recall was 100%, with 62.5% precision.
- Meliante 2025, JMIR AI (10.2196/68592):
  - Search was incomplete.
  - Data extraction was accurate in 51.40% of cases.
- Spillias 2025, Environ Evid (10.1186/s13750-025-00362-9): GPT-4 Turbo and Elicit were unreliable at detecting whether data were present.
- Hilkenmeier 2025, SSCR: already listed, not counted (abstract only). 81.4% accuracy vs 86.7% for humans.
- More titles found in this sweep, not yet screened:
  - Acta Derm Venereol 2026, Elicit vs a systematic review.
  - Cochrane ESM 2025 (10.1002/cesm.70033), Elicit vs human data extraction in RCTs.
  - OSF / Research Square preprints from 2025–26.
- Effect: 7 → up to 10 or more counted, all peer-reviewed. The grade stays A.
- Score: COULD CHANGE. Meliante's 51.4% extraction accuracy goes against the "good extraction" basis of the completion score. The test versions and dates are not yet checked, and pre-May-2025 Elicit may be out of scope.
- Recommendation: FLAG FOR ITS OWN PACKET (0054), with full reads. Do not batch.

## Part 2: 20-entry sweep (OpenAlex title screen)

Columns:
- Hits = OpenAlex hits screened.
- Candidates = titles relevant enough to read in full.
- Effect if counted = the best case before any full read.

| Entry | Current | Hits | Candidates (not yet read in full) | Effect if counted | Score could change? | "Citation check incomplete" note? |
|---|---|---|---|---|---|---|
| perplexity | 54/B, 6 perf | 50 | PLoS ONE 2025 (10.1371/journal.pone.0326351); PeerJ 2025 (10.7717/peerj.18847); PLoS ONE 2026 pediatric chest pain (10.1371/journal.pone.0359170); Semin Ophthalmol 2025 (10.1080/08820538.2025.2547077); Bul. Inst. Politeh. 2026 human evaluation (10.2478/bipcm-2026-0028) | 6 → up to 11, could reach A | Yes (completion/accuracy) | Yes, until the follow-up packet |
| elicit | 68/A, 7 | 25 | See D5 | Stays A | Yes | Yes (via 0054) |
| consensus | 62/B, 6 | 48 | Can. J. Inf. Libr. Sci. 2025, Elicit/SciSpace/Consensus (10.5206/cjils-rcsib.v49i1.23075) | 6 → 7, could reach A | Possibly | Yes |
| openai-deep-research | 65/B, 5 | 49 | ANZ J Surg 2025 (10.1111/ans.70161, may be commentary); Eye 2025 deep-research agents and systematic review (10.1038/s41433-025-04138-w) | 5 → up to 7 | Possibly | Yes |
| gemini-deep-research | 63/B, 7 | 25 | Eye 2025 (same as above); JAIS 2026 investment-analysis evaluation; arXiv 2607.20891 "Is Deep Research Reliable?" | Peer-reviewed 2 → up to 4, could reach A | Possibly | Yes |
| claude-research | 58/B-, 4 | 50 | None relevant by title | None | No | Yes (query noisy) |
| chatgpt-work | Insufficient, 0 | 50 | None independent (book titles and a Zenodo practitioner note) | None | No | Yes (query noisy) |
| manus | Insufficient, 0 current | 47 | None testing Manus 2.0. 2025-version titles only (historical context). | None | No | No (already recent and thorough) |
| julius-ai | Insufficient, 2 perf | 25 | Int. Sci. J. 2025 mixed-methods comparison (10.62341/absm3091); Taiwan Educ. Res. Monthly 2025 hands-on test. Most hits were promo-code spam. | 2 → up to 4, could reach B- | Yes (first scores) | Yes |
| clay | Insufficient, 0 | 17 | None | None | No | Yes (query noisy) |
| pactum | Insufficient, 1 partial | 25 | KTH 2026 thesis, AI procurement case study (not peer-reviewed; independence unchecked) | Possibly 1 → 2, still Insufficient | No | No |
| google-deepmind-safe | 66/B-, 3 | 47 | Factuality-evaluation papers that may use SAFE as a baseline: VeriFact (EMNLP 2025), FactBench (ACL 2025), DnDScore (EMNLP 2025), arXiv 2610.18415 reproducibility | 3 → 5 or more, could reach B | Yes | Yes |
| open-interpreter | Insufficient, 0 | 25 | None | None | No | No |
| kimi-researcher | Insufficient, 2 | 49 | None (Kimi model technical reports only) | None | No | Yes (query noisy) |
| agent-s | 49/B, 8 | 50 | None new (Agent S2 already listed) | None | No | No |
| storm | 56/B, 7 | 49 | IJIRT 2026 STORM/Co-STORM study (low-assurance venue). The query was mostly weather and medical noise. | Probably none | No | Yes |
| skyvern | Insufficient, 2 | 25 | None | None | No | No |
| perplexity-comet | 41/B-, 4 | 39 | None (one Zenodo software record) | None | No | Yes (query noisy) |
| data-interpreter | 49/B, 9 | 25 | None | None | No | No |
| browser-use | 51/B, 7 | 47 | arXiv 2609.32915 AgentTell (side-channel leakage); 2512.07725 Privacy Practices of Browser Agents; 2512.12594 ceLLMate (sandboxing); 2609.35814 controlled interventions. Each must be checked for whether it tests the Browser Use library. TOCTOU (2603.00476) is already known (0050 D7). | Possibly 7 → 9 or more | Possibly (adherence) | Yes |

Not done: full reads of the sweep candidates above. Dates, versions and independence are still unchecked for them. No sweep candidate is proposed for counting in 0052.

## Part 3: proposed batched changes (low impact, for approval)

B1. OpenHands
- Add source row: "Sifting the Noise (ISSTA 2026; doi 10.1145/3832100): OpenHands Agent SDK v1.5.2 (released 2025-12-11) triaging static-analysis warnings; OWASP false-positive rate 14.9% (Claude Sonnet 4), 16.3% (GPT-5), 15.8% (DeepSeek Chat). Independent; peer-reviewed."
- Counts: 12 counted, 7 peer-reviewed. Grade A unchanged. Scores unchanged.

B2. Claude Code
- Add two source rows:
  - "WideSWE (arXiv 2609.33382, Sept 2026; Zhejiang University, Tsinghua University): cross-repository tasks; Claude Code v2.1.139 configurations fully solved 10.83%–37.50% of 120 tasks (best overall: Codex CLI, 42.50%). Independent preprint."
  - "Timeline-Bench (arXiv 2609.35143, Sept 2026; TensorTest): 56 video-editing tasks; Claude Code 2.1.278 with Claude Opus 5 resolved 23.2% (2nd of 16), with Claude Fable 5.1 17.9%; agents claimed full success in 93% of runs, including most failed edits. Independent preprint."
- Counts: 17 counted, 6 peer-reviewed. Grade A unchanged. Scores unchanged.

B3. "Citation check incomplete — recheck later" note
- Add it to: perplexity, consensus, openai-deep-research, gemini-deep-research, claude-research, chatgpt-work, julius-ai, clay, google-deepmind-safe, kimi-researcher, storm, perplexity-comet, browser-use. Remove each note when its follow-up packet is closed.
- Proposed wording: "Citation check incomplete — recheck later (0052: Semantic Scholar unavailable; OpenAlex title screen only)."

B4. Aider (optional)
- Decision-record note only: "Test dates firmed up via the commit and release dates of the other tested agents (Dec 2025)."

Rollout: one changelog row ("0052: citation backfill, OpenHands and Claude Code sources added; recheck notes"), then check_scores, check_links, overflow and axe, then commit, push and manifest-0052.

## Part 4: proposed follow-up packets (each needs its own approval)
- 0053: SWE-agent B → A (Sifting the Noise).
- 0054: Elicit, four or more new peer-reviewed tests, with a possible completion-score effect.
- Later, one per entry or small group: Perplexity, Gemini/OpenAI Deep Research, Consensus, Google DeepMind SAFE, Julius AI, Browser Use library.

## Pending (not decided)
- Browser Use TOCTOU (0050 D7): still pending and undecided.

## Decisions requested
D1 SWE-agent to 0053 · D2 B1 OpenHands batch · D3 B4 Aider note (optional) · D4 B2 Claude Code batch · D5 Elicit to 0054 · D6 B3 recheck notes (list and wording) · D7 follow-up order
