# Decision 0092: Google Jules — 50 / B-

**Status: APPROVED by Remington, 2026-10-20 (9:17 PM ET), as recommended:** 50 / B- (3 counted: C1, C2 limited, C3; 0 peer-reviewed), D1–D9 as recommended, D11, D12 banner, D13 caveat edit applied; D14 cross-references NOT applied (noted only). The page states the fragility plainly (the score rests on the minimum three counted sources; dropping any one would leave it unscored; no counted test names a version; Gemini 3-era Jules is untested). Batch 6. The entry YAML carries `decision: APPROVED`. Commit, push and deploy (D15, D16) are not yet approved.

**Citation check incomplete — recheck later.**
- **OpenAlex full text** was the main search: "Jules" with agent, coding agent and Google terms, plus the AIDev titles. 368 unique works were screened. 210 PDFs were downloaded and grepped; 158 downloads failed.
- **arXiv:** the API timed out, so only the abstract search page was used and key papers were fetched from arxiv.org/pdf.
- **Semantic Scholar:** returned HTTP 429, so it was not used.
- **Not found:** the paper "Who Migrates the Schema" (Zenodo/doi.org fetch failed). It is listed for recheck.
- **Other sources:** coding-agent sources already in the repo were re-grepped for Jules (research/ca-jules.json).
- **Search log:** see research/source-table.md.
- The counted set is a sample of what was found, not an exhaustive list.

## What happened
1. **Scope set** (D1). Google Jules (https://jules.google) is Google's asynchronous coding agent. It clones a GitHub repo into a cloud VM, proposes a plan, edits code and runs commands, then returns a branch or pull request.

   | Date | Milestone (Google sources: changelog, blogs) |
   |---|---|
   | 11 Dec 2024 | Announced as an experiment on Gemini 2.0 Flash |
   | 19 May 2025 | Public beta |
   | 6 Aug 2025 | Out of beta, on Gemini 2.5 Pro |
   | 2 Oct 2025 | Jules Tools CLI (npm @google/jules; latest 0.1.42, 16 Dec 2025) |
   | 3 Oct 2025 | Jules API |
   | 19 Nov 2025 | Gemini 3 Pro |
   | Dec 2025 | Scheduled and suggested tasks |
   | 26 Jan 2026 | Planning critic (vendor claims 9.5% fewer failures) |
   | 30 Jan 2026 | Gemini 3 Flash base |
   | 2 Feb 2026 | MCP |
   | 19 Feb 2026 | CI Fixer; commits can be authored under the user's name |
   | 9 Mar 2026 | Gemini 3.1 Pro (latest changelog entry) |

   **Out of scope (D1):**
   - Gemini CLI, Gemini Code Assist (including its GitHub PR review), Google Antigravity, Firebase Studio and AlphaEvolve.
   - Model-only Gemini results.
   - The Dec 2024 research configuration that Google benchmarked on SWE-bench Verified (vendor).
2. **Search.** I screened OpenAlex and arXiv results, separating:
   - tests of Jules;
   - mentions;
   - AIDev dataset descriptions;
   - studies that pool all agents without a Jules-specific result.

   Only studies that use AIDev v4/v5-era data report Jules separately. No benchmark that runs Jules (e.g. a SWE-bench harness run of the product) was found.
3. **Results:**
   - **3 counted** independent performance sources, **0 peer-reviewed**. None states a Jules version.
   - **15 other** (11 other + 4 anecdotal).
   - **Not counted:** 1 competitor, 1 excluded and 4 vendor sources.
4. **Developer-authored material:** Google blogs, changelog, FAQ and the Google-authored proactivity paper are vendor or excluded (0031).

## Counted: independent performance sources (3; peer-reviewed 0)
All accessed 2026-10-20.

| # | Source | Peer review / independence | Version / test date | Result |
|---|---|---|---|---|
| C1 | Qi et al., "Merged, Not Measured" (Univ. of Arizona, Wuhan Univ., CAS, CSULB, RIT). https://arxiv.org/abs/2609.37985 | Preprint (Sep 2026). "The authors declare no conflict of interest"; no Google author or funding | AIDev v4 (PRs in repos >100 stargazers, to 24 Oct 2025); version not stated | 17 Jules performance fixes. 15 were closed in 6 repos and 11 merged (73%), the same share as Codex and Claude Code; Copilot 50%, Cursor 42%, Devin 30%. All recorded merges were by someone other than the bot account. **Small sample** (D2) |
| C2 | Bhavnagri (Wilson College, Univ. of Mumbai), "AI Coding Agents on GitHub: Repository Popularity as a Hidden Confounder", IJRASET 14(IX), Sep 2026. https://doi.org/10.22214/ijraset.2026.84804 | Journal with no review dates and low assurance → **peer_reviewed false**, labelled "limited" (0076 D4a; D4). Single author; no funding stated | Full AIDev v4 snapshot, 24 Dec 2024–24 Oct 2025; version not stated | 38,691 of 43,600 decided Jules PRs merged (88.74%). Comparison agents: Codex 93.20, Claude Code 87.84, Cursor 80.39, Copilot 77.63, Devin 69.74. 76.4% of Jules PRs went to unstarred repos and 0.95% to repos with ≥100 stars. The Jules rate fell 16.6 points across 4 popularity bands. Cursor-vs-Jules odds ratio 2.063 pooled → 1.370 within-repo (101 repos), i.e. the gap roughly halves |
| C3 | Will Schenk, TheFocus.AI, "June 2025 Coding Agent Report" for the Turing Post newsletter, 5 Jun 2025. https://labs.thefocus.ai/reports/june-2025-coding-agents.pdf (the old thefocus.ai URL now returns 404) | Not peer-reviewed. No funding or sponsor disclosed; TheFocus.AI is a consultancy, not a coding-agent vendor. Public artifact repo The-Focus-AI/idears-jules | Public beta, early June 2025 | 15 tools got the same greenfield Node/Docker prompt. Review was AI-assisted (Claude Sonnet) plus a manual build. Jules scored **21/25** (4/5/4/4/4), level with Copilot Agent (21); Cursor Agent, v0 and Warp 24; Codex Agent 18; Replit 15. Single build per tool (D3) |

C1 and C2 both use AIDev v4. Each study counts once (0040 D3), with a shared-dataset caveat.

## Other sources (listed, not counted) — 15
| # | Source | Why other |
|---|---|---|
| O1 | Embrace The Red (Johann Rehberger), 13 Aug 2025. https://embracethered.com/blog/posts/2025/google-jules-vulnerable-to-data-exfiltration-issues/ | Security research (demonstration). Data exfiltration via Markdown image and view_text_website before plan approval; plans auto-approved after 30 s (later 2 min). Reported 21 May 2025 |
| O2 | Embrace The Red, 14 Aug 2025. https://embracethered.com/blog/posts/2025/google-jules-remote-code-execution-zombai/ | Demonstration. GitHub-issue injection → Jules downloads and runs Sliver C2 malware; unrestricted outbound internet. Shared 1 Jun 2025. He says Google triaged it as an abuse risk and closed it 13 Jun 2025 as already being tracked; questions on a mitigation timeline went unanswered |
| O3 | Embrace The Red, 15 Aug 2025. https://embracethered.com/blog/posts/2025/google-jules-invisible-prompt-injection/ | Demonstration. Invisible Unicode tag instructions were followed; a backdoor was added |
| O4 | AIDev v5 dataset card (Li, Zhang, Hassan; Queen's Univ.; cutoff 31 Mar 2026). https://huggingface.co/datasets/hao-li/AIDev-7.6M | Dataset statistics. 296,411 Jules PRs in 41,125 repos, 63.4% merged. Jules bot PR volume fell ~15× after late Jan 2026 |
| O5 | LogicStar "Agents in the Wild" dashboard. https://insights.logicstar.ai/ | Live dashboard by a coding-agent company (D6). 1,638,208 Jules PRs since 15 May 2025; 965,607/1,225,005 merged (78.82%) |
| O6 | PR Arena (GitHub user aavetis). https://prarena.ai/ | Live dashboard; operator unidentified. 205,695/243,419 ready PRs merged (84.5%). Data quality unclear (Cursor shows 101.7%) (D6) |
| O7 | Farrag, "Reviewing Beyond the Change", arXiv 2610.15567 | Review-comment study. 18.2% of comments on Jules PRs came from the delegator and 3.4% were addressed. Not a performance measure |
| O8 | Soualhi & Suleiman, "Co-Modifying…", arXiv 2610.12849 | Descriptive (3/27 and 1/26 Jules PRs) |
| O9 | Selvanayagam & Ghaleb, "AI-to-AI Code Reviews", ESEM 2026 emerging results, arXiv 2608.21311 | Jules authors PRs but does not review; no Jules performance measure |
| O10 | Khosravani & Mockus, "Detecting AI Coding Agents in Open Source", arXiv 2606.24429 | Usage census. 209,911 Jules commits in 16,924 projects by Oct 2025; 215,804 by Apr 2026; peak Aug 2025 |
| O11 | HarnessSecurity-Bench, arXiv 2610.07639 | Documentation audit of 40 harnesses; Jules is mostly "unknown". Not a test |
| O12 | Jon Atkinson blog, 23 May 2025. https://www.jonatkinson.co.uk/blog/codex-jules-claude-comparison/ | **Anecdotal.** One Django task; Jules graded C, took ~1 hour and skipped the migration squash |
| O13 | yoav.blog, 10 Jun 2025. https://yoav.blog/2025/06/10/comparing-ai-coding-agents-with-a-real-task/ | **Anecdotal.** "Jules completely hallucinated the issue content…" |
| O14 | Robert Matsuoka, HyperDev, 22 May 2025. https://hyperdev.matsuoka.com/p/google-jules-first-look-not-ready | **Anecdotal.** Launch-day errors and timeouts |
| O15 | StepChange blog (Niall OHiggins), 28 May 2025. Archived copy: https://web.archive.org/web/20250528191935/https://stepchange.work/blog/can-ai-beat-a-human-dev-jules-vs-codex-on-live-django-issues-with-apx | **Anecdotal.** Two Django issues found by the company's own APX tool; both agents missed model changes. The original Ghost URL (stepchange-blog.ghost.io) returns 402 "Site unavailable" and stepchange.work did not respond on 20 Oct 2026, so the archived copy is linked (link recheck below) |

0079: other = 11 + 4 = 15.

## Not counted
**Competitor (1):**
- Popescu, Gros, Botocan, Pandita, Devanbu, Izadi, "Investigating Autonomous Agent Contributions in the Wild", MSR 2026 (peer-reviewed). https://doi.org/10.1145/3793302.3793354 (arXiv 2604.00917).
  - Affiliations: TU Delft, UC Davis and **GitHub** (Rahul Pandita).
  - It compares Copilot with Jules (~18,500 Jules PRs, Jun–Aug 2025).
  - Competitor rule (0080/0083): the author's product is in the comparison → listed, not counted (D5).

**Excluded (1):**
- Bui & Evangelopoulos (Google), "Agentic Coding Needs Proactivity, Not Just Autonomy", arXiv 2605.06717. Google authors (0031).

**Vendor (4):**
- Google Developers Blog, 11 Dec 2024. Research version 51.8% on SWE-bench Verified; the leaderboard submission lists 52.2%.
- blog.google GA post, 6 Aug 2025.
- Jules changelog.
- Jules FAQ ("with internet access"; "You are responsible for the code you run").

**Not listed:**
- Papers that mention Jules only in related work.
- AIDev papers that pool all agents with no Jules-specific result.
- Gemini CLI/Code Assist studies.
- Listicles and launch-week news without a test.
- Model-only Gemini benchmarks.

## Shared-author check (0031)
- **Developer set:** Google/Google DeepMind/Google Labs staff.
- **Counted sources:** no Google author, affiliation or funding (C1 universities; C2 Univ. of Mumbai college; C3 TheFocus.AI).
- **Competing-platform links:**
  - MSR study: GitHub co-author, Copilot compared → competitor.
  - LogicStar: a company in the agent space.
  - AIDev (used by C1/C2): Queen's University, which is independent.

## Disputes, incidents and security (status 20 Oct 2026)
- **Prompt injection (Embrace The Red, O1–O3).** Attribution is to Johann Rehberger's own posts throughout.
  - **Timeline:** reported 21 May 2025 and 1 Jun 2025. He says Google closed the second report on 13 Jun 2025 as "already tracking". Published 13–15 Aug 2025.
  - **Google's response:** no public statement from Google about a fix was found. The FAQ still says the VM has internet access.
  - **Weighting:** weighed in disputes and adherence; not counted (D9).
- **Beta reliability (anecdotal):** launch-week errors and timeouts; one hallucinated issue; one skipped step.
- **Activity drop:** Jules bot PR volume fell ~15× after late Jan 2026 (AIDev card). From 19 Feb 2026 commits can carry the user's name, so the cause is unclear (possibly attribution rather than use). This is an uncertainty, not a dispute.
- **Security records:** no CVE or GitHub advisory for Jules. NVD "jules" gives 4 hits, all WordPress plugins by Jules Colle; GHSA gives 0.
- **Legal:** no lawsuit or regulatory action found.

## Precedents applied
- **0031:** Google-authored material is excluded or vendor.
- **0039:** model-only results are context.
- **0040 D3:** C1 and C2 count once each despite the shared AIDev dataset; this is caveated.
- **0058:** launch demos are not counted.
- **0071:** a documented hands-on test counts (C3).
- **0076 D4a:** C2 is counted as limited, with peer_reviewed false.
- **0079:** other = 11 + 4.
- **0080/0083:** MSR is a competitor source.
- **0051:** A is impossible (3 counted, 0 peer-reviewed, no versioned test).
- **0010:** half-up rounding.
- **0065:** feed item required.
- **0075:** title ≤68 characters.
- **0090 D1:** coding-agents caveat must name every Coding agent entry (D13).

## Score (Scoring rules v0.1)
| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion rate | 30 | 50 | **Moderate, mixed.** No task success rate. C1: 73% merged, level with Codex/Claude Code (n=15). C2: 88.74% merged, second of six, but inflated by unstarred repos (−16.6 points across popularity bands). C3: 21/25, mid-pack. Comparable: Devin 40, Copilot 45, Replit 40 |
| Disputes | 20 | 55 | No CVE, lawsuit or regulator. One researcher's disclosed weaknesses; by his account, closed by Google as "already tracking"; no public fix statement |
| Adherence to limits | 25 | 40 | **Weak in demonstrations:** data exfiltration before plan approval, malware run after auto-approval, hidden instructions followed; open internet in the VM. Offsetting points: plan-first design and human merge. Single-researcher evidence, 2025 |
| Evidence quality | 25 | 55 | 3 counted, 0 peer-reviewed, no versions, 2025 data, shared dataset, one small sample, one low-assurance venue, one single build. Same as Skyvern/Julius B- (55) |

0.30×50 + 0.20×55 + 0.25×40 + 0.25×55 = 15 + 11 + 10 + 13.75 = 49.75 → **50**.

**Grade B-:** 3 counted, which is the minimum to score.

**Fragility (counting decisions):**
| Variant | Counted | Peer-reviewed | Result |
|---|---|---|---|
| Recommended | 3 | 0 | **B- / 50** |
| D2b: drop C1 (small Jules sample) | 2 | 0 | **Insufficient evidence** |
| D3b: TheFocus as other | 2 | 0 | **Insufficient evidence** |
| D4b: IJRASET not counted | 2 | 0 | **Insufficient evidence** |
| D5b: count MSR (against 0083) | 4 | 1 | B- (evidence ~60 → ~51) |
| Count Atkinson (anecdotal) or LogicStar | 4 | 0 | B- / 50 |
| Drop C3 + count MSR | 3 | 1 | B- / ~50 |

**Every borderline counted source is decisive:** reversing any one of D2–D4 makes the entry Insufficient evidence.

**Score range (recommended counting):**
| Change | Overall |
|---|---|
| As proposed | 50 (49.75) |
| Completion 45 / 55 | 48 (48.25) / 51 (51.25) |
| Disputes 50 / 60 | 49 (48.75) / 51 (50.75) |
| Adherence 35 / 45 | 49 (48.5) / 51 (51.0) |
| Evidence 50 / 60 | 49 (48.5) / 51 (51.0) |

Plausible range 48–51.

**Index position:** after Devin (Cognition) (50) and before Magentic-One (open-source) (50); confirmed in the dry run.

## Risks and uncertainties
1. **Version.** No counted source states a version. All data are May–Oct 2025 (beta / Gemini 2.5 Pro). The Gemini 3 era and features from Nov 2025 on (critic, CI Fixer, MCP) are untested.
2. **Merge rate ≠ correctness.** Merge rates depend on reviewer behaviour and repo popularity, and most Jules PRs went to unstarred repos.
3. **Minimum evidence.** The entry rests on 3 sources, 2 of them on one dataset. It is maximally fragile.
4. **Venue assurance.** IJRASET's review process could not be confirmed. If it is judged unacceptable, the entry is Insufficient.
5. **C3 method.** It is a single build, AI-assisted scoring, by one author, and the report's own wording is promotional. The page avoids quoting its verdict.
6. **Security currency.** The demonstrations date from 2025. Whether Google mitigated them is unknown.
7. **Attribution drift.** User-name commits since Feb 2026 may hide Jules activity from bot-account studies.
8. **Search gaps.** 158 PDFs failed to download; arXiv API and Semantic Scholar were unavailable; "Who Migrates the Schema" was not retrieved (D12 banner).
9. **Dashboards.** LogicStar and PR Arena rates disagree (78.8% vs 84.5%), and PR Arena shows an impossible Cursor figure.

## Decisions (D1–D13 approved 2026-10-20, 9:17 PM ET, as recommended; D14 not applied; D15–D16 not yet approved)
- **D1 Scope.**
  - (a) **Recommended.** One entry for Jules across web app, GitHub issue label, Jules Tools CLI and API, beta to current. Exclude Gemini CLI, Code Assist, Antigravity, Firebase Studio, AlphaEvolve, model-only results and the Dec 2024 research configuration.
  - (b) Current (Gemini 3.x, 2026) only → 0 counted → Insufficient evidence.
- **D2 C1 Merged, Not Measured.**
  - (a) **Recommended.** Count; note the small Jules sample.
  - (b) Other → Insufficient evidence.
- **D3 TheFocus (C3).**
  - (a) **Recommended.** Count as a documented hands-on test with method and public artifacts (0071).
  - (b) Other (newsletter, single build, AI-assisted scoring) → Insufficient evidence.
- **D4 IJRASET (C2).**
  - (a) **Recommended.** Count as limited, peer_reviewed false (0076 D4a).
  - (b) Not count → Insufficient evidence.
- **D5 MSR 2026 study.**
  - (a) **Recommended.** Competitor (GitHub co-author; Copilot compared), listed, not counted (0080/0083).
  - (b) Count with disclosure → 4 counted / 1 peer-reviewed, still B-.
- **D6 Dashboards and dataset card** (LogicStar, PR Arena, AIDev v5).
  - (a) **Recommended.** Other (live, unversioned, operators in the agent market or unidentified).
  - (b) Count LogicStar → 4 counted.
- **D7 Blog tests.**
  - (a) **Recommended.** Anecdotal (no reported method; single tasks; StepChange tests via its own product).
  - (b) Count Atkinson.
- **D8 Version treatment.**
  - (a) **Recommended.** Treat as one product. State on the page that no counted test names a version, all data are from 2025, and Gemini 3-era Jules is untested.
  - (b) Mark historical → Insufficient evidence.
- **D9 Embrace The Red.**
  - (a) **Recommended.** Other; weighed in disputes (55) and adherence (40), attributed to the researcher, with "according to him" for Google's triage.
  - (b) Treat as a counted security test → 4 counted.
- **D10 Name and category.**
  - (a) **Recommended.** "Google Jules", Coding agent, slug google-jules. Title "Google Jules — Agent Reputation & Trust Clearinghouse" (53 chars).
  - (b) "Jules (Google)".
- **D11 Score.** 50 / B- (50 / 55 / 40 / 55). Range 48–51.
- **D12 Banner and wording.**
  - "Citation check incomplete — recheck later".
  - Disputes text as in the draft page.
  - The TheFocus verdict wording is not quoted.
  - Recheck the StepChange link (HTTP 402) and the ACM DOI (403 to bots). Done: see Link recheck.
- **D13 Required caveat edit.** Add "Google Jules" to coding-agents caveat 1 in scripts/build_data.py: "(Claude Code, OpenAI Codex, GitHub Copilot coding agent, Devin, Cursor agent, Replit Agent, Google Jules) are tested as shipped." **Required** for check_all (0090 D1 check). The alternative is to defer the whole entry. It is applied only in the scratch dry run.
- **D14 Cross-references (NOT applied; candidates only).**
  - (a) C2 IJRASET reports Codex, Copilot, Cursor, Devin and Claude Code merge rates; none of those pages lists it.
  - (b) C3 TheFocus tested Cursor, Copilot agent, Codex, Claude Code, Replit, Aider and others; none lists it.
  - (c) The MSR 2026 study (Copilot vs Jules) is not on the Copilot page; for Copilot it would be developer-authored.
  - (d) C1 is already listed on the Copilot/Cursor/Devin pages.
  - No score changes are proposed for other entries.
- **D15 (later, not requested)** Entry page, changelog row, feed item and decision record commit/push.
- **D16 (later, not requested)** Deploy.

**Recommendation (APPROVED 2026-10-20, 9:17 PM ET):** D1a, D2a, D3a, D4a, D5a, D6a, D7a, D8a, D9a, D10a, D11 (50 / B-), D12, D13. D14 to be left for those entries' next reviews.

## Link recheck (20 Oct 2026, ~9:30 PM ET)
- **MSR 2026 study, https://doi.org/10.1145/3793302.3793354: valid, kept.**
  - The DOI is registered: the doi.org handle record points to https://dl.acm.org/doi/10.1145/3793302.3793354, and doi.org answers 302 to that page.
  - Crossref metadata matches: "Investigating Autonomous Agent Contributions in the Wild: Activity Patterns and Code Change over Time", Proceedings of the 23rd International Conference on Mining Software Repositories, 13 Apr 2026, Popescu, Gros, Botocan, Pandita, Devanbu, Izadi.
  - The ACM page answers automated requests with a Cloudflare challenge ("Just a moment…", 403), so the 403 is a bot block, not a dead link.
  - Open copy: https://arxiv.org/abs/2604.00917 (200; affiliations include GitHub for Rahul Pandita; 18,468 Jules PRs, June–August 2025). The note already cites arXiv 2604.00917.
- **StepChange blog: original not live; replaced with an archived copy.**
  - https://stepchange-blog.ghost.io/… and the blog's home page both return 402 with a Ghost "Site unavailable" page, so the whole blog is offline.
  - The canonical URL https://stepchange.work/blog/can-ai-beat-a-human-dev-jules-vs-codex-on-live-django-issues-with-apx did not respond (TLS error from the box; 500 from the fetch service).
  - The Wayback Machine copy (snapshot 28 May 2025) loads and matches the text used: "Jules' response (4 min)…", "Proposed directly dropping indexes through Django migrations without adjusting the corresponding Django models".
  - The source is anecdotal and not counted, so the change does not affect the score.

## Private dry run (scratch clones of b5e0b52; real tree untouched)
See dryrun/RESULTS.md, dryrun/google-jules.preview.html and dryrun/draft-0092.patch. Draft changelog row: draft-changelog-row.yaml. Feed item text: feed-item.txt.

## Final private patch (scratch clone of b5e0b52; real tree untouched)
final/final-0092.patch (15 files: entry YAML, this decision record, entry page, changelog row, update feeds, index, llms files, sitemap, data exports, coding-agents comparison, D13 caveat in scripts/build_data.py). Checks: final/check_all-scratch.txt (0 errors), final/check_scores-scratch.txt ("OK google-jules: overall 50 (computed 50), grade B-, counted 3, peer-reviewed 0"), final/final-checks.txt (totals 41 / 30 scored + 11 insufficient / 77 rows / 91 feed items / sitemap 49; zero score diffs for the other 40 entries; wording, banned-word and link checks). Deploy manifest /workspace/manifest-0092 and verify script /workspace/verify-0092/v92.py prepared; not deployed (rollback target dpl_EedTY2xZNnfFMc8bDNFQbJQoCUSk).

## Minimum viable version
Approve D1a, D2a, D3a, D4a, D8a, D11 (50 / B-) and D13 with the D12 banner; keep the other wording as drafted. D14 needs no action now. The alternative minimum is to hold Jules as Insufficient evidence / not added until a peer-reviewed or versioned independent test appears.

## Plain-English terms
- **Google Jules:** Google's AI that takes a coding task, works on your GitHub project in a cloud computer, and hands back proposed changes.
- **Asynchronous agent:** it works in the background while you do something else.
- **Pull request (PR) / merge rate:** a proposed code change; the share that the project's maintainers accepted.
- **AIDev:** a public dataset of pull requests opened by AI coding agents on GitHub.
- **Prompt injection:** hidden or planted text that tricks an AI into following someone else's instructions.
- **Data exfiltration:** secretly sending data out to someone else's server.
- **Command-and-control (C2) malware:** software that lets an attacker remotely control a machine.
- **Auto-approve:** the plan goes ahead on its own after a timer if the user doesn't respond.
- **Unstarred repository:** a GitHub project nobody has bookmarked; usually small or personal.
- **Odds ratio:** how many times likelier one outcome is for one group than another.
- **Competitor source:** a study whose authors' own product is in the comparison.

---
*Informational only. This is a private draft summarizing cited public evidence under published rules; it is not a guarantee, endorsement, certification or ranking of quality, and nothing here has been published.*
