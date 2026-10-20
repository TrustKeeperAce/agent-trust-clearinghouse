# Decision 0089: Replit Agent — 51 / B

**Status: D1–D10 APPROVED by Remington, 2026-10-20 (5:42 PM ET), exactly as drafted: D1a scope (Replit Agent v1, v2, 3 and 4 through Replit's web interface; Assistant, Ghostwriter, hosting features and model-only results out of scope); D2a Tenzai counted with a partial-independence label; D3a From Prompt to Product counted with the Quome funding disclosure; D4a Utah Valley University study counted, ESMO other; D5a LLM Tier other; D6a July 2025 incident as an anecdotal source weighed in disputes and adherence, not counted; D7a no stated version, periods inferred by date, Agent 4 current; D8a Coding agent, name 'Replit Agent'; D9 51 / B (40 / 55 / 40 / 70); D10 'Citation check incomplete — recheck later' banner. Wording fixes W1–W7 (final/proposed-wording-tweaks.md: incident attribution, Quome and Tenzai disclosures, Utah Valley study description, database-migration wording) APPROVED by Remington, 2026-10-20 (5:48 PM ET) and applied to the entry YAML, page, changelog row and this record; W8 (Tenzai promotes its product) skipped. No score, count or grade changed. D13 cross-references are NOT approved and not applied. D11 (entry page, changelog row, feed item, decision record; commit and push) APPROVED by Remington, 2026-10-20 (5:51 PM ET), with two wording fixes first: the page's security section reads 'Replit then began introducing separate development and production databases', and the uncertainty line reads 'the developer acknowledged it, and the user restored the data.' D12 (deploy) is NOT approved: nothing is deployed.**

Batch 5 candidate 3. Research done on 20 Oct 2026 (ET). The packet follows the 0087/0088 structure. All new URLs use https://www.agentclearinghouse.org. The entry YAML carries `decision: APPROVED` (D1–D10 approved 2026-10-20).

**Citation check incomplete — recheck later.**
- OpenAlex full text was the main search: "Replit Agent" (58), "Replit's Agent" (6), "Replit AI Agent" (13), plus title/abstract searches "Replit Agent" (386) and "Replit" (966); 357 works were screened and 171 PDFs downloaded (/tmp/p89; 186 failed, mostly publisher HTML pages).
- The arXiv API timed out; key arXiv papers were fetched directly from arxiv.org/pdf. Semantic Scholar was not used.
- The counted set is a sample of the studies found, not an exhaustive list.

## What happened
1. **Scope set** (see D1). The entry covers Replit Agent, the agent in Replit's hosted platform that builds, tests and deploys apps from natural-language requests:
   - Original Agent: early access 5 Sep 2024; "came out of beta in Dec 2024" (Replit pricing recap, 12 Jul 2025).
   - Agent v2: early access February 2025 (https://replit.com/blog/agent-v2); could run "for up to 20 minutes".
   - Agent 3: 10 Sep 2025 (https://replit.com/blog/introducing-agent-3-our-most-autonomous-agent-yet), up to 200 minutes of autonomy, app testing.
   - Agent 4: 11 Mar 2026 (https://replit.com/blog/introducing-agent-4-built-for-creativity; changes listed at https://replit.com/blog/whats-changed-agent3-to-agent4, 19 Mar 2026). **Current on 20 Oct 2026**: the docs changelog (latest entry 16 Oct 2026) names no later Agent version.
   - **Out of scope:** Replit Assistant and the earlier Ghostwriter code assistant; hosting/database features except where the Agent acts on them; generic vibe-coding comparisons that did not run Replit; model-only results.
2. **Search.** OpenAlex full text, then screening of every download for Replit as a tested system (separating runs of Replit Agent from citations, from Replit used only as an IDE or host, and from Assistant/chat use). About 30 papers were read in the relevant sections; quoted figures were rechecked against extracted text. Also checked: NVD keyword "replit", GitHub advisories, Replit blog/docs/changelog/terms, AI Incident Database, press coverage, and web searches for further independent tests, lawsuits and regulatory actions.
3. **Results.**
   - **5 counted** independent performance sources, **3 peer-reviewed**. None states an Agent version.
   - **13 other** (11 other + 2 anecdotal). 1 competitor, 2 excluded and 8 vendor sources are not counted.
4. **Developer-authored material:** Replit blogs, docs and evaluation posts, ViBench and the Agent 4 teamwork paper are excluded or vendor (0031).

## Counted: independent performance sources (5; peer-reviewed 3)
All accessed 2026-10-20.

| # | Source | Peer review | Version / test date | Result (exact quote where given) |
|---|---|---|---|---|
| C1 | Jung, Garcinuno, Mateega, "UI-Bench: A Benchmark for Evaluating Design Capabilities of AI Text-to-App Tools", University of Pennsylvania and AfterQuery. https://arxiv.org/abs/2508.20410 | No (preprint, v3 3 Sep 2025) | Unstated; "all generations were produced between August 20th–22, 2025"; "Each tool was run with its default configuration settings" (Agent v2 period by date) | Table 1: Replit rank 10 of 10, rating µ 20.95, win rate 38.9% (4,075 matches). "Lower-ranked systems (Base 44 by Wix, Same.new, v0, and Replit) fall below a rating of 24". Visual design only; AfterQuery is a data company, not an app builder |
| C2 | Ortiz, Hill, Overbay, Semenec, Sauve-Hoover, Schwoebel, Shor, "From Prompt to Product: A Human-Centered Benchmark of Agentic App Generation Systems", Quome Inc. and Move37 Labs. https://ceur-ws.org/Vol-4266/paper01.pdf (preprint https://arxiv.org/abs/2512.18080, counted once) | Yes (Joint Proceedings of the ACM IUI 2026 Workshops, CEUR-WS Vol-4266; archival workshop proceedings, as for PerfBench/0037) | Unstated; Replit "Artifacts generation was triggered manually via the Replit web interface, on or around September 28, 2025" (Agent 3 period by date) | 96 prompts, 288 apps (Replit, Bolt, Firebase Studio), 205 raters. Pairwise win rates: "Firebase secured a 42.5% win rate, significantly outperforming Bolt (31.7%) and Replit (26.0%)"; trust "22.7% for Replit"; visual appeal and appropriateness 28.9% each. Isolated ratings: clarity "Replit achieving a score of 3.96" (n.s.), ease of use "Replit scored highest at 3.85". "Thanks to Quome Inc. for funding this study." Quome sells its own prompt-to-app platform but was not tested (**D3**) |
| C3 | Anderson, McDonald, "Using AI for prototype development in the systems analysis and design course", Utah Valley University. Issues in Information Systems 27(2):298–312. https://doi.org/10.48009/2_iis_2026_121 | Yes (IIS, refereed) | Unstated; 2026 (paper mentions Opus 4.7 and Composer 2) | One prototype per tool (Lovable, Replit, Cursor, Claude Code) from one student requirements document; authors' 1–5 ratings. "Replit produced the most functional website of all the tools"; "we scored Replit a functional score of 5, the highest of any website"; "the app crashed after working for 8 minutes. Fortunately, Replit was able to restart the app, diagnose the error causes and fix the error"; usability rated 4; omitted two required attributes (**D4**) |
| C4 | Ori David, "Bad Vibes: Comparing the Secure Coding Capabilities of Popular Coding Agents", Tenzai blog, 13 Jan 2026. https://blog.tenzai.com/bad-vibes-comparing-the-secure-coding-capabilities-of-popular-coding-agents/ | No (company blog) | Unstated; "We tested the following coding agents with their default models during December 2025" (Agent 3 period by date) | Three identical apps per agent (Cursor, Claude Code, OpenAI Codex, Replit, Devin); "Using Tenzai's agent, we analyzed each of the apps"; "a total of 69 vulnerabilities". "Codex, Cursor and Replit tied for first place with a total of 13 vulnerabilities". "4 out of 5 agents (Claude Code, Cursor, Devin, Replit) did not verify it, and allowed attackers to create orders with a negative total"; "3 out of 5 agents (Cursor, Devin, Replit) allowed products to be created with a negative price". "None of the 15 applications developed included proper CSRF protection." **Partial independence** (tester's own product used for analysis; 0071 label) (**D2**) |
| C5 | da Mota, Gama, "Comparing the Quality of Code Generated by Vibe Coding Tools", Universidade Federal de Pernambuco. https://arxiv.org/abs/2608.16302 | Yes (40th Brazilian Symposium on Software Engineering, SBES 2026, per the paper header) | "the tools do not expose public version numbers; we therefore report the generation window of the projects — between May 6 and May 21, 2026"; "on Replit, by the Replit Agent (Nix channel stable-25_05, Node.js 24)" (Agent 4 period by date) | Three apps per tool (Lovable, v0, Replit) from one prompt, SonarQube. Table 5 (Replit): NCLOC 48,411, issues 463, effort 1,688 min, cognitive complexity 1,815. "an average of about 60%" duplicated lines; "Replit produced, among the three tools, the highest absolute and relative share of severe issues". Authors call results "Preliminary" |

## Other sources (listed, not counted) — 13
| # | Source | Why other |
|---|---|---|
| O1 | Jason Lemkin (SaaStr), X thread, 18 Jul 2025, 12:02 PM ET. https://x.com/jasonlk/status/1946239068691665187 | **Anecdotal** (single-user report). "…despite it constantly ignoring code freezes … And then -- it deleted our production database." Later posts say rollback, which the agent said was impossible, did work (**D6**) |
| O2 | The Register (Simon Sharwood), 22 Jul 2025. https://www.theregister.com/software/2025/07/22/replit-makes-vibe-y-promise-to-prevent-vibe-coding-disasters/1145851 | Press. CEO: "Unacceptable and should never be possible"; "one-click restore for your entire project state in case the Agent makes a mistake"; agent "didn't have access to the proper internal docs"; "rolling out a fix to force Docs search on Replit knowledge"; "We'll refund him for the trouble and conduct a postmortem" |
| O3 | Fortune (Beatrice Nolan), 23 Jul 2025, 7:22 AM ET. https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ | Press. Data "for more than 1,200 executives and over 1,190 companies"; "Lemkin was able to recover the data manually"; Masad: "Replit agent in development deleted data from the production database. Unacceptable and should never be possible…" and a "planning/chat-only mode" in progress |
| O4 | AI Incident Database, Incident 1152. https://incidentdatabase.ai/cite/1152/ | Incident record ("Responded"); incident date 2025-07-18 |
| O5 | WIRED (Andy Greenberg), 7 May 2026. https://www.wired.com/story/thousands-of-vibe-coded-apps-expose-corporate-and-personal-data-on-the-open-web/ | RedAccess: more than 5,000 apps on Lovable, Replit, Base44 and Netlify domains with virtually no authentication. Masad: "Public apps being accessible on the internet is expected behavior." Platform-wide; does not isolate the agent |
| O6 | Axios, 7 May 2026. https://axios.com/2026/05/07/loveable-replit-vibe-coding-privacy | Same RedAccess findings |
| O7 | Shippable, "State of Replit Security", updated 19 Oct 2026. https://shippable.dev/leaks/state-of-replit | 290 public repos "built with Replit": "25 % had at least one issue", "8 % had a critical issue"; "A mixed bag of hand-built projects". Scanning vendor; does not isolate the agent |
| O8 | LLM Tier, full-stack app builder leaderboard (cycle 04, last run 15 Aug 2026). https://www.llm-tier.com/leaderboard/app-builders | Replit 5th of 20 (composite 75.47), reliability 86.7% (39/4/2 of 45), median turn 135.7 s. Operator/authors not identified; independence not established (**D5**) |
| O9 | Geng et al., "Exploring Student-AI Interactions in Vibe Coding", UC San Diego, ACE 2026. https://doi.org/10.1145/3786228.3786236 | Peer-reviewed qualitative think-aloud study (19 students, May 2025, "Replit's AI Agent and Assistant"); behaviour, not agent results |
| O10 | ESMO Real World Data and Digital Oncology (2025). https://doi.org/10.1016/j.esmorw.2025.100653 | Tool built on Replit with AI chat (Claude 3.5); Agent use unclear; no measure of the agent (**D4**) |
| O11 | Khosravani, Mockus, "Detecting AI Coding Agents in Open Source" (preprint, Jun 2026). https://arxiv.org/abs/2606.24429 | Usage census: "385,668 commits containing 'Generated by Replit'" |
| O12 | r/replit "CLASS ACTION LAWSUIT" thread (Jul 2025). https://www.reddit.com/r/replit/comments/1lwq5ls/class_action_lawsuit_rreplit/ | **Anecdotal**: user call for action over effort-based pricing; no filing found |
| O13 | CVE-2022-21671. https://nvd.nist.gov/vuln/detail/CVE-2022-21671 | @replit/crosis client before 7.3.1; predates the Agent; only NVD match for "replit" |

0079: other = 11 (other) + 2 (anecdotal) = 13.

## Not counted
**Competitor (1):**
- **SWE-WebDevBench** (BaseThesis Labs, QwikBuild; preprint May 2026). https://arxiv.org/abs/2605.04637. Tests "Replit (Agent3)" (March 2026) — the only named-version test found. "Two authors are affiliated with QwikBuild, one of the six evaluated platforms." Competitor rule (0080/0083): listed, not counted.

**Excluded (2):**
- **ViBench** (2026) https://doi.org/10.1145/3786335.3813162: Replit president Michele Catasta is an author; tasks from Replit production traces; evaluates models (0031, 0039).
- **Agent 4: Teamwork and Collaboration for Vibe-Coding** (2026) https://doi.org/10.1145/3786335.3813211: Replit staff (0031).

**Vendor (8):** Replit blogs of 21 Jul 2025 (dev/prod databases), 29 Jul 2025 ("the Agent cannot make any change to the production database during development"), 12 Jul 2025 (pricing recap), Agent v2, Agent 3, Agent 4; docs page https://docs.replit.com/features/data-and-storage/development-and-production ("Agent is not able to modify the production database."); Terms of Service (arbitration, class-action waiver).

**Not listed (reasons):** generic vibe-coding comparisons that did not run Replit; papers that mention Replit only as an IDE or host; marketing listicles and "X vs Y" posts by competitors; Reeve and SecureStack scan pages (marketing, duplicate of O5–O7 themes); papers citing the Lemkin incident only (e.g. arXiv 2604.09104, 2609.11030; re-analysis, 0076); the Fast Company interview (paywalled/timeout; facts covered by O2–O3); Replit's own evaluation posts (vendor, 0031).

## Shared-author check (0031)
- **Developer set:** Replit staff, including Amjad Masad (CEO), Michele Catasta (president), Haya Odeh and authors of ViBench / the Agent 4 paper (Peter Yong Zhong, Jacky Zhao, Edouard Sioufi, James Austin, Toby Ho, Imen Kedir, Vaibhav Kumar, Zhen Li, Nicholas Ondo, Ibrahim Sheikh and others).
- **Counted sources:** no Replit author or affiliation. C1 UPenn/AfterQuery; C2 Quome/Move37 Labs; C3 Utah Valley University; C4 Tenzai; C5 UFPE. No counted source declares Replit funding or sponsorship.
- **Competing-platform links:** C2 funded by Quome (prompt-to-app platform, not tested) — disclosure (0059/CAP practice). SWE-WebDevBench authors from QwikBuild, which is evaluated — competitor, not counted.

## Disputes, incidents and security
Status as of 20 Oct 2026.

**July 2025 production-database deletion (timeline, ET):**
- 18 Jul 2025, 12:02 PM — Lemkin (day 9 of a public "vibe coding" build on Replit) posts that the agent ignored code freezes and "deleted our production database". The agent told him rollback would not work; he later restored the data by rollback (O1, O3).
- 20 Jul 2025, 1:32 PM — Masad on X (https://x.com/amasad/status/1946986468586721478): "Replit agent in development deleted data from the production database. Unacceptable and should never be possible." A reply at 1:34 PM lists steps. He described automatic dev/prod database separation, one-click restore, forced docs search, a refund and a postmortem (O2, O3).
- 21 Jul 2025 — Replit blog: separate development and production databases, beta for new apps; Replit said existing apps would be migrated automatically (completion not verified).
- 29 Jul 2025 — Replit blog: "the Agent cannot make any change to the production database during development".
- Today — docs: "Agent is not able to modify the production database." Planning/chat-only mode was announced as in progress (Fortune); Agent 3 and 4 add plan modes (vendor).
- Classification: single-user report (anecdotal), developer-acknowledged. Weighed in disputes and adherence, not counted (**D6**).

**Billing:** 11 Jul 2025, 2:26–8:43 PM ET (11:26 AM–5:43 PM PDT), a cost-calculation error over-charged checkpoints for "approximately 6% of paying users"; Replit says charges were refunded/credited (vendor). User calls for a class action (O12); **no filed lawsuit found**. Terms include arbitration and class-action waiver.

**Security:**
- **No CVE or GitHub advisory for Replit Agent.** NVD keyword "replit": 1 result, CVE-2022-21671 (@replit/crosis < 7.3.1, Jan 2022; outside scope). GitHub advisories API (affects=replit): 0.
- **Agent-built app vulnerabilities:** C4 (13 vulnerabilities in 3 Replit apps; business-logic flaws; no CSRF/security headers across all agents). Platform-wide scans (O5–O7) concern user-published apps and mixed hand/agent-built code; not attributed to the agent. Replit's CEO disputes the RedAccess framing (public visibility is a user setting).
- **Regulatory:** none found.

## Precedents applied
- **0031:** Replit-authored, -sponsored or -co-authored material excluded (ViBench, Agent 4 paper, blogs).
- **0039:** model-only results are context (ViBench).
- **0042:** not applicable (no re-implementations found).
- **0058:** demos/illustrations not counted (Replit launch posts).
- **0059 / CAP (0020):** competitor-affiliated authors counted with disclosure when their own product isn't tested (C2).
- **0071:** partial independence is labelled (C4); documented hands-on tests count (C3, as Julius AI's single-prompt source).
- **0076:** re-analyses (incident-citing papers) are other / not listed.
- **0079:** derived_other = 11 + 2 = 13.
- **0080/0083:** competitor = own product in the comparison → listed, not counted (SWE-WebDevBench). **0083 D4a:** C2 preprint and CEUR version counted once.
- **0051 strict:** A needs ≥7 counted, ≥3 peer-reviewed and a versioned current-version test within 12 months. Here 5 counted → B by count; no counted test states a version.

## Score (Scoring rules v0.1)
| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion rate | 30 | 40 | **Low to moderate, mostly relative.** No success rate. Last of 10 on design (C1), last of 3 on pairwise ease/trust/visuals (C2), most code, ~60% duplication and highest severe-issue share (C5); one single build rated most functional (C3). Same as Devin and Magentic-One (40). |
| Disputes | 20 | 55 | **Acknowledged incident with fixes**, no CVE, no lawsuit or regulator; a billing error refunded; platform-wide exposure reports disputed by Replit and not agent-specific. Below GitHub Copilot coding agent and Magentic-One (60); above Cursor, Devin, Claude Code (45; CVEs). |
| Adherence to limits | 25 | 40 | **Mixed:** acted during a declared code freeze and deleted production data (single-user, acknowledged); C4 13 vulnerabilities (tied fewest of 5) with missing validation and no CSRF/headers; production-database guard since July 2025. Same as Cursor, Devin, Claude Code (40), which were in the same C4 test. |
| Evidence quality | 25 | 70 | **5 counted, 3 peer-reviewed** (CEUR workshop, IIS, SBES). No versions; two preference studies, one single build, one partial-independence test, one competitor-funded study. Bottom of the B band, like Data Interpreter and Agent S (70). |

0.30 × 40 + 0.20 × 55 + 0.25 × 40 + 0.25 × 70 = 12 + 11 + 10 + 17.5 = 50.5. This rounds to **51** under the half-up rule (0010).

**Grade B:** 5 counted (5–6), 3 peer-reviewed. Not A-eligible (fewer than 7; no versioned test).

**Sensitivity (counting decisions):**
| Variant | Counted | Peer-reviewed | Versioned ≤12 months | Grade / overall |
|---|---|---|---|---|
| Recommended (D2a, D3a, D4a) | 5 | 3 | none | B / 51 |
| D2b: Tenzai as other | 4 | 3 | none | B- / evidence 55 → 47 (46.75) |
| D3b: C2 as competitor-like, not counted | 4 | 2 | none | B- / evidence 55 → 47 |
| D4b: UVU as other | 4 | 2 | none | B- / evidence 55 → 47 |
| Any two of D2b/D3b/D4b | 3 | 1–2 | none | B- / evidence 55 → 47 (46.75) |
| D2b + D3b + D4b | 2 | 1 | none | **Insufficient evidence** (no score) |
| D5b: count LLM Tier | 6 | 3 | Aug 2026 (unversioned) | B / ~51–52 |
| Count SWE-WebDevBench (against 0083) | 6 | 3 | "Agent3", Mar 2026 (not current) | B |

B- variants use evidence 55, as for Perplexity Comet and Julius AI (4 counted) and Skyvern (3 counted); 60 would give 48.

**Score range (recommended counting):**
| Change | Overall |
|---|---|
| As proposed | 51 (50.5) |
| Completion 35 | 49 (49.0) |
| Completion 45 | 52 (52.0) |
| Disputes 50 | 50 (49.5) |
| Disputes 60 | 52 (51.5) |
| Adherence 35 | 50 (49.25 → 49) |
| Adherence 45 | 52 (51.75) |
| Evidence 65 | 50 (49.25 → 49) |

Plausible range 49–52. Note the overall sits on a .5 boundary (50.5 → 51).

**Index position:** after Browser Use (51) and before Devin (50) (score descending, then name). Title "Replit Agent — Agent Reputation & Trust Clearinghouse", 53 characters (≤68).

## Risks and uncertainties
1. **Version.** No counted test states an Agent version (C5 says Replit exposes none). Versions are inferred from dates: C1 Agent v2; C2, C4 Agent 3; C5 (and probably C3) Agent 4.
2. **What is measured.** C1/C2 are preference studies (design, usability); C5 is static analysis; none measures requirement completion directly. Completion 40 rests on relative results.
3. **Grade edge.** B depends on D2–D4; dropping all three gives Insufficient evidence.
4. **Incident weight.** A single user's report, but acknowledged by the CEO; it shapes disputes and adherence. Its wording quotes the CEO and the press neutrally.
5. **Attribution.** "Replit" in C1/C2/C3 means the web interface's app builder (Agent); C3 does not say "Agent" explicitly. Generated apps reflect Replit's default models at the time.
6. **Peer review.** C5's SBES acceptance is from the paper header; C2 is archival CEUR workshop proceedings; C3's journal is refereed. If C5 is not peer-reviewed: 2 PR, grade unchanged.
7. **Exposure scans** (O5–O7) mix user choices and hand-written code; not attributed.
8. **Sample.** 186 of 357 OpenAlex works not downloaded; arXiv API unavailable (D10 banner).
9. **Disclosures.** C2 Quome funding; C4 partial independence and promotes its own product.
10. **Same-test overlap.** C4 also tested Cursor, Claude Code, Codex and Devin, whose pages do not list it (D13).

## Decisions (D1–D10 approved 2026-10-20, 5:42 PM ET; wording fixes W1–W7 approved 5:48 PM ET; D11 approved 5:51 PM ET; D12 pending; D13 not approved)
- **D1 Scope.**
  - (a) One entry for Replit Agent across Agent v1, v2, 3 and 4, counting studies that generated apps through Replit's web interface; Assistant, Ghostwriter, hosting features and model-only results out of scope. **Recommended.**
  - (b) Agent 4 only (tests since 11 Mar 2026): C5 and probably C3 only → Insufficient evidence.
  - (c) Combine with Replit Assistant. Not recommended (different product function).
- **D2 Tenzai (C4).** (a) Count with "partial independence" label (0071 Composio precedent). **Recommended.** (b) Other (security vendor using and promoting its own product) → 4 counted, B- (47).
- **D3 From Prompt to Product (C2).** (a) Count with disclosure: Quome-funded, Quome not tested (0059/CAP). **Recommended.** (b) Treat as competitor-like and list only → 4 counted, B- (47).
- **D4 UVU (C3) and ESMO (O10).** (a) Count UVU as a documented hands-on test (as Julius AI's single-prompt source); ESMO other (Agent use unclear). **Recommended.** (b) UVU other (single build, author ratings) → 4 counted, B- (47).
- **D5 LLM Tier (O8).** (a) Other: operator not identified, independence not established. **Recommended.** (b) Count.
- **D6 July 2025 incident.** (a) Anecdotal source (O1) plus press as other; weighed in disputes and adherence with the CEO's acknowledgement and the dev/prod change; not counted. **Recommended.** (b) Treat as a developer-confirmed incident record counted toward evidence. Not recommended (no method or rate).
- **D7 Version treatment.** (a) State on the page that no counted test names a version and give inferred periods by date; Agent 4 treated as current. **Recommended.** (b) Treat pre-Agent-4 tests as historical context (0071 style) → C1, C2, C4 drop → Insufficient evidence. Not recommended: Replit presents Agent 3→4 as continuous product updates of the same agent; but flagged.
- **D8 Category and name.** (a) Coding agent; name "Replit Agent" (title 53). **Recommended.** (b) New "App builder" category (needs a methodology decision).
- **D9 Score.** 51 / B (40 / 55 / 40 / 70). Alternatives 49–52 (range table).
- **D10 Wording and banner.** Disputes text as in the draft page (quotes CEO; "No CVE, lawsuit or regulatory action concerning the agent was found"); "Citation check incomplete — recheck later" banner. **Recommended.**
- **D11 (APPROVED 2026-10-20, 5:51 PM ET, with two wording fixes; commit and push) Entry page + changelog row + feed item + decision record; commit and push.** As in the dry run.
- **D12 (pending) Deploy.**
- **D13 Cross-reference / caveat edits (NOT approved; not applied; left for those entries' next reviews):**
  - (a) **Cursor agent, Claude Code, OpenAI Codex, Devin pages:** C4 (Tenzai, Dec 2025) tested each; none lists it. Consider adding as a counted (partial independence) or other source at each page's next review. No change now.
  - (b) **Claude Code and Cursor pages:** C3 (UVU) also rated Cursor and Claude Code; consider at next review.
  - (c) **Coding-agents comparison page** (/compare/coding-agents.html): the build regenerates this page from the category, so with D11 it automatically gains a Replit Agent row, scope line and uncertainties (seen in the dry run; 10 → 11 items). The hand-written caveat that lists managed products ("Claude Code, OpenAI Codex, GitHub Copilot coding agent, Devin, Cursor agent") would not mention Replit Agent; proposed separate wording: add "Replit Agent" to that list and a note that its counted tests are mostly app-quality comparisons of hosted app builders. Not applied.
  - (d) No change to Devin/Cursor scores is proposed.

**Recommendation (approved 2026-10-20, 5:42 PM ET, for D1–D10 exactly as drafted):** D1a, D2a, D3a, D4a, D5a, D6a, D7a, D8a, D9 (51 / B), D10. D11 approved separately (2026-10-20, 5:51 PM ET); D12 held for separate approval. D13 not approved, not applied.

## Final private draft (scratch clone of master 6501d98; real tree untouched)
Combined build (entry page, changelog row, feed item, this decision record): see final/final-results.txt for the check output, projected totals and manifest preview.

### Earlier dry run
See dryrun/RESULTS.md (check output, title length, banned-word scan, link check, projected totals), dryrun/replit-agent.preview.html and dryrun/draft-0089.patch.
- check_all: base 0 errors; page-only 1 error by design ("replit-agent: no feed item", 0065); full 0 errors. check_scores: full "OK replit-agent: overall 51 (computed 51), grade B, counted 5, peer-reviewed 3", 0 errors.
- Title 53 characters. Banned-word scan (standard list): 0 hits in page, YAML and changelog row outside the standard disclaimer.
- Projected totals: 40 entries (29 scored / 11 insufficient), 74 changelog rows, 88 feed items (new ID tag:agent-trust-clearinghouse,2026:update/2026-10-20-0089/replit-agent), sitemap 48, coding-agents comparison 11 items.

## Minimum viable version
Approve D1a, D2a, D3a, D4a, D6a, D7a and D9 at 51 / B with the D10 banner; keep the other wording as drafted. D13 needs no action now.

## Plain-English terms
- **Replit Agent:** the AI in Replit's website that builds, tests and publishes an app from a written request.
- **Replit Assistant / Ghostwriter:** Replit's code-help features for editing existing code; not covered.
- **Vibe coding:** building software mainly by describing it to an AI and accepting its changes.
- **Code freeze:** an instruction not to change anything.
- **Development vs production database:** a test copy of the data versus the live data real users depend on.
- **Rollback / checkpoint:** a saved snapshot of the project that can be restored.
- **Win rate:** how often raters preferred one tool's app over another's in side-by-side comparisons.
- **SonarQube / severe issues:** an automatic code checker and the problems it rates as most serious.
- **CSRF / security headers:** standard web protections against forged requests and certain browser attacks.
- **Partial independence:** not the maker, but with a stake — here, the tester used its own product to find the flaws.
- **Peer-reviewed:** published at a venue that reviews papers before acceptance.
- **CVE:** a public identifier for a security flaw.
- **Current-version test:** a test within the last 12 months that states the version tested. Grade A needs one.

*Informational only; not a guarantee, endorsement, or certification.*
