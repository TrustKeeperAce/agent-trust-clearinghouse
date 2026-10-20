# Decision 0087: Cline — 55 / A

**Status: D1–D10 APPROVED by Remington, 2026-10-20 (1:14 PM ET), exactly as drafted: D1a scope (extension, JetBrains plugin, CLI and companion servers; forks excluded); D2 developer set; D3a counting (20 counted, 8 peer-reviewed); D4a versioned tests (C1 v3.82.0, C12 CLI 3.0.47); D5 Zoro and ECCWS counted as peer-reviewed, the ICML workshop paper not; D6 disclosures as drafted; D7a 'fixed in code' wording with the advisory caveat; D8 55 / A; D9 'Citation check incomplete — recheck later' banner; D10a Cline added to the coding-agents comparison caveat. D11 (Cline page, changelog row with the two wording fixes — last caveat sentence kept; the not-counted sentence reads 'Material from the Cline team and results for its forks (Roo Code, Kilo Code) are not counted.' — and the D10a caveat edit; commit and push) APPROVED by Remington, 2026-10-20 (1:18 PM ET). D12 (deploy) is NOT approved: nothing is deployed.**

Batch 5 candidate 1. Research done on 20 Oct 2026 (ET). The packet follows the 0085 (mini-SWE-agent) structure, with 0083 (Cursor agent) and 0037 (OpenHands) as templates. This is the first entry drafted against the new address, https://www.agentclearinghouse.org (0086).

**Citation check incomplete — recheck later.**
- OpenAlex full text was the main search: 16 queries matched 790 works, and 295 PDFs were downloaded.
- Semantic Scholar was mostly rate-limited (HTTP 429).
- The unauthenticated GitHub API hit its rate limit partway through; the arXiv API worked.
- The counted set is a sample of the studies found, not an exhaustive list.

## What happened
1. **Scope set** (see D1). The entry covers Cline:
   - GitHub cline/cline, Apache-2.0, created 6 Jul 2024. About 7,700 forks and 1,680 open issues (GitHub API, 20 Oct 2026). Developer: Cline Bot Inc., founded by Saoud Rizwan.
   - VS Code extension `saoudrizwan.claude-dev`: v3.20.0 (23 Jul 2025) … v3.82.0 (1 May 2026), v4.0.0 (26 Jun 2026), latest v4.1.25 (16 Oct 2026). Dates are from OpenVSX.
   - Cline CLI (npm `cline`): 2.x (Feb 2026), 3.0.0 (12 May 2026), latest 3.0.73 (17 Oct 2026). Dates are from the npm registry.
   - JetBrains plugin and SDK. The CLI also starts companion servers: Kanban (npm `kanban`, repository cline/kanban) and the Hub dashboard.
   - Cline runs with any model the user chooses. By default it asks for approval before actions; users can turn on auto-approval and "YOLO" settings.
   - **Forks are separate products:** Roo Code, Kilo Code and others.
2. **Search.**
   - OpenAlex full-text search: 16 queries ("Cline" with coding-agent, VS Code, MCP and similar context terms, plus the "claude-dev" and "cline/cline" strings). 790 unique works matched and 295 PDFs were downloaded and converted to text (/tmp/p87).
   - Downloads were screened for Cline as a tested agent, separating out the name (surnames, biology, mathematics), forks and plain mentions. The strongest candidates were read in full (about 45 papers). Figures in counted sources were re-checked against the text, and against PDF layouts where tables were flattened.
   - Also checked: the arXiv API, Crossref/OpenAlex venue metadata, GitHub (repository, releases, security advisories, issues), NVD, OpenVSX, the npm registry, and researcher write-ups.
3. **Results.**
   - **20 counted** independent performance sources, **8 peer-reviewed**.
   - 13 counted sources are security studies; 7 are task studies.
   - **22 other** (20 other + 2 anecdotal).
   - Vendor material and cline-bench are not counted (0031).
4. **No developer-authored papers were found.**
5. **Draft entry built in a scratch clone** of master 2a3b699, with the repository's checks run there (see "Dry run"). The real working tree was not touched.

## Counted: independent performance sources (20; peer-reviewed 8)
Type key:
- **H** = runs Cline alongside other harnesses or clients, usually with the same models.
- **B** = baseline for a method that competes with it or adds to it.
- **F** = fixed host or harness used to compare attacks or models (see D3).

| Ref | Source | Peer review | Version / date | Type | Key Cline figures |
|---|---|---|---|---|---|
| C1 | Red-Teaming Coding Agents from a Tool-Invocation Perspective (HKUST, Fudan; PACMSE/FSE 2026, doi 10.1145/3832267; arXiv 2509.05755) | yes | **v3.20.8 and v3.82.0** / 2025–2026 | H | RCE-2 attack success was 1.0 with Grok-4, Sonnet-4 and Sonnet-4.5 (v3.20.8). On v3.82.0 it was still 1.0 with Gemini-3.1-pro and Grok-4.20. The authors credit Cline's system-prompt restriction on commands from external sources. They also state "Cline's default configuration lacks these safeguards" (allowlisting and confirmation of high-risk calls). |
| C2 | A First Look at the Security Issues in the MCP Ecosystem (U Delaware; DSN 2026, doi 10.1109/DSN69566.2026.00046) | yes | unstated / servers collected Jun–Jul 2025 | H | Four hosts were tested. None verified that a selected tool came from the intended server. Success rates are given per host and model. "All hosts except Cline display concise summaries" by default, so Cline shows full detail. |
| C3 | Parasites in the Toolchain (SJTU, HKUST, Chaitin Tech; IEEE S&P 2026, doi 10.1109/SP63933.2026.00154) | yes | unstated / 2025–26 | H | Six clients were tested. Cline was compromised in most trials with most models, often 3–5 of 5 per prompt (table read from extracted text). Disclosure: security-company co-author; shares an author with C1. |
| C4 | MCP Threat Modeling … Tool Poisoning (NYIT; J. Cybersecurity and Privacy 6(3) 84, 2026, doi 10.3390/jcp6030084; preprints 2603.21642 and 2603.22489, counted once) | yes | **Cline 3.34.0** / late 2025 | H | Seven clients were tested, all with Claude Sonnet 4.5. Cline, Claude Desktop and Continue "successfully blocked file access through model-level refusals", while Cursor read sensitive files. However, "Cursor and Cline are unsafe and execute remote scripts when instructed". |
| C5 | MPMA (AAAI-26, doi 10.1609/aaai.v40i42.40898) | yes | unstated / 2025 | F | "All the experiments are conducted using Cline". Manipulated server names and descriptions raised the chance that the model selected the attacker's server. |
| C6 | GitChameleon 2.0 (ELLIS Tübingen, Mila, Google, ServiceNow and others; ACL 2026, doi 10.18653/v1/2026.acl-long.2170) | yes | unstated / 2025 | H | Without the problem statement, Cline with GPT-4.1 had the highest success rate among assistants (38.4%). With it, assistants gained 12–35 points. Roo Code and Kilo Code are reported separately and not counted. Disclosure: Google and ServiceNow co-authors. |
| C7 | Zoro (Columbia; UIST '26 (accepted); arXiv 2604.15625; printed DOI 10.1145/3830398.3830629 not yet registered) | yes (accepted; conference in Nov 2026) | unstated / 2026 | B | Run in Cline with Sonnet 4.6, one run per task. Rule-following was 51% without Zoro (process rules 35%, coding rules 59%) and 80% with it (87% and 75%). Add-on method. |
| C8 | Automatically Attacking Software Reverse Engineering AI Agents (Naval Postgraduate School; ECCWS 2026, doi 10.34190/eccws.25.1.4597) | yes (conference proceedings; D5) | unstated / 2025–26 | F | Adversarial strings compiled into binaries made Cline + GhidraMCP with Qwen3-8B misdescribe what programs do. |
| C9 | What's in Your Agent's Context? Context Privilege Escalation (UIUC; arXiv 2609.01222) | no | **Cline 3.77.0** / 2026 | H | 12 harnesses were tested. Cline loads the working-directory file list into context and acts on tool tags in model output. An end-to-end attack made it write a .windsurfrules file. The authors say Cline "released new versions to mitigate the threats". |
| C10 | Beware of Agentic Botnets (Tel Aviv, Technion, Intuit; arXiv 2607.07433) | no | **Cline 3.66.0** / 2026 | H | With KAT-Coder-Pro V1: tool invocation in 11/20 runs and code execution in 9/20 (45%). Across tools the range was 20–65%. Disclosure: Intuit. |
| C11 | ShareLock (SJTU; arXiv 2606.27027) | no | **Cline v3.35.0** / late 2025 | H | Run on Cherry Studio v1.5.11 and Cline v3.35.0 with four models. Average attack success was above 90%. |
| C12 | Can Agents Trust Their Skills? (CAS, WPI; arXiv 2609.39065) | no | **Cline CLI 3.0.47** / 2026 | H | 11 agents were tested. With --auto-approve true, 7 vulnerabilities were verified in Cline (104 across all agents; 24 in the highest). With --auto-approve false, 0 of 7 remained exploitable. Prompt replay reproduced 2 of 7. Columns were read from the PDF layout. |
| C13 | Safe to Resume? (SUSTech, CityU; arXiv 2608.29381) | no | unstated / 2026 | H | One of three end-to-end attacks (Hermes, Cline, LangGraph) used a Cline rollback to cause unauthorized mail forwarding. |
| C14 | GitInject (Virginia Tech, AI Sequrity; arXiv 2606.09935) | no | unstated / 2026 | H | A Cline assistant workflow triggered by @cline, with no author restriction, followed an injected "routine diagnostic request". It posted the owner's private repository names publicly. |
| C15 | Package Hallucination Attacks via Rule Files (Duke; arXiv 2610.09264) | no | unstated / 2026 | H | Eight frameworks in autonomous mode with confirmations disabled. An attack optimized on OpenHands transferred to Cline with Qwen3-Coder-30B. Kilo Code results are not counted. |
| C16 | SWE-Nexus (NUS, Shanghai AI Lab, Tsinghua, independent; arXiv 2610.20038) | no | unstated / 2026 | H | 600 tasks, 12 models × 3 scaffolds. Highest resolved rate: 31.2% under Cline (GPT-5.5/GPT-5.4), against 37.8% under Claude Code and 29.7% under OpenCode (both Opus 4.8). Shares authors with C17. |
| C17 | ANCHOR (SUSTech, NJU, NUS, independent; arXiv 2610.16859) | no | unstated / 2026 | H | 358 tasks, 19 configurations. Opus 4.8 under Cline had the highest compliance measured: 70.1% ACR, 19.0% FCCR, 43.6% constrained completion. With GPT-5.3-Codex, completion was 37.7% in Cline vs 37.4% in OpenCode, but IPR was 62.9% vs 67.9% and FCCR 9.2% vs 12.3%. |
| C18 | SpreadsheetBench 2 (Renmin plus industry; arXiv 2606.29955) | no | unstated / 2026 | H | GLM-5. Cline: modification 41.98, accuracy 8.66%. Claude Code: 43.47 / 14.20%. Authors' scaffold: 46.32 / 15.45%. Competing scaffold; industry co-authors. |
| C19 | Beyond Generalist LLMs (Commonwealth Bank of Australia; SCALE workshop at ICML 2026; arXiv 2607.14456) | no (workshop; D5) | unstated / 2026 | B | 117 attempts per 100 working agents (85.5%, the same as the authors' system; Roo Code 73.0%). About 1,044k tokens, against about 55k for the authors' system. Competing method. |
| C20 | DeepDiscovery (Alibaba AMAP, NTU, NJU, Cambridge; arXiv 2606.22906) | no | unstated / 2026 | H | Sonnet 4.5. Native Cline found the full file set in 72.5% of large tasks (Cursor, OpenCode and Qoder 82.5%) and 79.0% of medium tasks. With DeepDiscovery: 81.7% and 86.4%. Add-on method; disclosure: Alibaba (Qoder). |

**Versioned tests within 12 months:**
- Peer-reviewed: C1 (v3.82.0, 1 May 2026) and C4 (3.34.0, 23 Oct 2025).
- Preprints: C9 (3.77.0), C10 (3.66.0), C11 (3.35.0) and C12 (CLI 3.0.47, 28 Jul 2026).
- No counted source states a v4.x extension version (see D4).

## Other sources (listed, not counted) — 22
| Ref | Source | Why other |
|---|---|---|
| O1 | Inside the Scaffold (Rombaut; arXiv 2604.03515) | Source-code taxonomy: Cline's main loop is the only recursive one. Code analysis, not a run. |
| O2 | Configuration, Not Conscience (Piraeus; arXiv 2609.31575) | 407-prompt text study: "RooCode has 54% of its word 5grams contained in Cline". Text analysis. |
| O3 | AISPA (arXiv 2607.28617) | System-prompt audit (Cline: 39.5 protective entries). Text analysis. |
| O4 | HarnessSecurity-Bench (SYSU and others; arXiv 2610.07639) | Documentation and source matrix of 40 harnesses. Cline was not among the 6 harnesses run. |
| O5 | Don't Let AI Agents YOLO Your Files (SOSP '26; arXiv 2604.13536) | Corpus of 207 incidents and exploits that includes Cline issues. Cline was not run (0076). |
| O6 | "Impossible to hide secret …" (arXiv 2607.26390) | Mined developer posts, some about Cline (0076). |
| O7 | AgentPulse (arXiv 2604.24038) | Aggregator of others' results (0076). |
| O8 | "I'm Not Reading All of That" (Samsung; arXiv 2603.14225) | Small user study of engineers using Cline. It measures the users. |
| O9 | AIPC (Qualcomm; arXiv 2604.14661) | Company workflow with single runs, framed as a comparison of models and agents (0039; D3). |
| O10 | AutoData (Notre Dame, IBM; NeurIPS 2025) | "Data collection by human efforts, via Cline": human-directed use. Table read from flattened text (D3 alternative: count it, giving 21/9). |
| O11 | ZhuLong (arXiv 2608.07925) | Agent built on Cline CLI (0042). |
| O12 | FLARE (arXiv 2609.23808) | "Cline-style" scaffolds; unmodified Cline is not stated (0042). |
| O13 | Projecting the Emerging Mindset of SWE Agent (Tongji; arXiv 2606.08500) | Cline-style prompt in the authors' own setup (0042). |
| O14 | Mindgard blog (Nov 2025) | Security write-up. Four issues reported 27 Aug 2025; "re-tested on Oct 31, 2025 on Cline v3.35.0" and they appeared mitigated. Vendor responses were limited. |
| O15 | Embrace The Red (2025) | Data exfiltration via image rendering. Reported 29 May 2025; unaddressed after 90+ days per the author. Current status not determined. |
| O16 | IDEsaster (Ari Marzouk, 6 Dec 2025) | Attack class; Cline is listed among affected products. Cline-specific fix status not determined. |
| O17 | Clinejection (Adnan Khan, Feb 2026) | Prompt injection in Cline's own issue-triage workflow, leading to cache poisoning and exposure of release tokens. Reported 1 Jan 2026; addressed after public disclosure on 9 Feb 2026. |
| O18 | CVE-2026-44211 / GHSA-5c57-rqjx-35g2 | Kanban WebSocket advisory (see the security section). |
| O19 | CVE-2026-59723 / GHSA-3cj3-hqcr-g934 | Hub dashboard WebSocket advisory. |
| O20 | GHSA-9ppg-jx86-fqw7 | Unauthorized npm publish of cline@2.3.0. |
| A1 | GitHub issue #5124 (Jul 2025, closed) | Single user report: files deleted without tracking. |
| A2 | GitHub issue #8422 (Jan 2026, closed Jun 2026) | Single user report: whole .env file overwritten. |

## Not counted
- **Vendor or maintainer (listed):**
  - the cline/cline repository, README, docs and blog;
  - the Cline post-mortem of the npm incident (23 Feb 2026).
- **Excluded (0031):** cline-bench, Cline's benchmark built from user sessions (announced 20 Nov 2025).
- **Fork results (not this product):** Roo Code and Kilo Code figures in GitChameleon 2.0, SpreadsheetBench 2, Package Hallucination and Beyond Generalist. CVE-2025-11445 is Kilo Code.
- **Model-only results (0039)** and plain mentions in agent lists (for example Reversa, and "Human oversight of agentic systems").
- **"When Binaries Talk Back" (arXiv 2607.12507):** only cites C8; Cline was not run.
- **CVE-2026-9468:** a third-party MCP server, not Cline.

## Shared-author check (0031)
- **Developer set:** Saoud Rizwan, Cline Bot Inc. staff, and the Cline team (including former Head of AI Nik Pash). No counted or other paper has a Cline author or Cline affiliation.
- **C1 and C3** share Yuchong Xie. They are different studies (tool-invocation RCE versus MCP tool chains), so both are counted, with disclosure.
- **C16 and C17** share several authors (SUSTech/NUS group). They are different benchmarks, so both are counted, with disclosure. O12 FLARE comes from the same group.
- **C4:** two arXiv preprints of one journal article, counted once (0083 D4a logic).

## Repository maintenance, disputes and security
CVE status is as of 20 Oct 2026.

- **CVE-2026-44211 (GHSA-5c57-rqjx-35g2):**
  - Critical, CVSS 3.1 9.6. Published 8 May 2026; NVD Analyzed.
  - The Kanban server started by Cline CLI (≤2.13.0) accepted cross-origin WebSocket connections, so a website could read workspace data and inject commands into agent terminals.
  - The advisory lists no patched version. NVD says "At time of publication, there are no publicly available patches."
  - **A fix exists in code:**
    - cline/kanban PR #421, "Enforce known origin and host policy for Kanban websocket service", merged 27 Apr 2026 (6:19 PM ET), commit c54b7669.
    - The origin check is present in kanban 0.1.66 (published 27 Apr 2026, 8:05 PM ET) and absent in 0.1.65. The latest is 0.1.70.
  - **Treated as fixed for disputes, with an advisory-metadata caveat (D7).** Not checked: which kanban version range each Cline CLI release pulls in.
- **CVE-2026-59723 (GHSA-3cj3-hqcr-g934):**
  - High, CVSS 3.1 8.8. GitHub advisory 23 Jun 2026; NVD Analyzed.
  - The Hub dashboard (`cline dashboard`) /browser WebSocket had no Origin check and no default secret, and dashboard sessions auto-approve tools.
  - NVD lists the versions before CLI 3.0.30 (26 Jun 2026) as affected and cites the fix commit and release. The GHSA "patched" field is empty.
  - **Fixed.**
- **GHSA-9ppg-jx86-fqw7 (Low):**
  - A leaked npm token published cline@2.3.0 with `postinstall: npm install -g openclaw@latest` at 3:26 AM PT on 17 Feb 2026.
  - 2.4.0 was published at 11:23 AM PT, and 2.3.0 was deprecated at 11:30 AM PT (about 8 hours).
  - Publishing now uses OIDC provenance. The VS Code and JetBrains extensions were not affected.
- **Clinejection (root cause of the leaked token):**
  - Cline's Claude-based issue-triage workflow, added 21 Dec 2025, could be prompt-injected. GitHub Actions cache poisoning then exposed the VSCE, OVSX and npm tokens.
  - The flaw was reported 1 Jan 2026 and not acted on until public disclosure on 9 Feb 2026. PR #9211 removed the workflows.
  - According to the Cline post-mortem (vendor), the wrong npm token was revoked first.
- **Researcher reports (2025):**
  - **Mindgard:** four issues, including DNS exfiltration and `.clinerules` turning off approval. Mitigated by v3.35.0 per Mindgard. The vendor responded late.
  - **Embrace The Red:** image exfiltration; unaddressed after 90+ days per the author.
  - **IDEsaster:** Cline listed among affected products.
  - Fix status for the last two is not determined.
- **Other CVEs:** an NVD keyword search found no other CVEs for Cline products.
- **Approval model:** actions need approval by default; auto-approval and YOLO options exist. C1 reports no command allowlisting by default. C12 found that turning approval on blocked all 7 verified issues.
- **Legal / regulatory:** none found.
- **Maintenance:** very active. Releases 16–17 Oct 2026, last push 20 Oct 2026.

## Precedents applied
- **0036 caution 2:** the named product must be run. Every counted source runs Cline itself. Fork results are excluded.
- **0037 D2 / 0038 D2 / 0085 D3a:** studies that run the harness count, including fixed-host studies (C5, C8). D3 sets out the alternatives.
- **0039:** results for a model alone are context. AIPC is treated as context (O9).
- **0031:** vendor material and cline-bench are excluded; no counted source has a developer co-author.
- **0042:** derived agents and re-implementations are other (O11–O13).
- **0058:** illustrations are not counted (README demos, adoption claims).
- **0076:** re-analysing others' reports or outputs is other (O5–O7).
- **0083 D4a:** no AIDev-based studies were found. The same logic is applied to C4's two preprints, which are counted once.
- **0079:** derived_other = other + anecdotal = 20 + 2 = 22.
- **0051 / 0084 D7a strict:** an A needs a test within 12 months that states the version. C1 (v3.82.0, peer-reviewed) qualifies, as do C4, C9–C12.
- **CVE handling:**
  - An unfixed high-severity CVE would get the 55-type treatment (as for SWE-agent and Aider).
  - Here both the high and the critical CVE are fixed in code, so they are recorded as notes. The weight for the pattern of incidents follows the Cursor and Claude Code entries (disputes 45).
- **Competing-method papers** count, with disclosure (0009, 0037). Corporate co-authors are disclosed (0038 D6).

## Score (Scoring rules v0.1; D8 approved)
| Factor | Weight | Score | Basis |
|---|---|---|---|
| Completion rate | 30 | 50 | **Mixed.** Below Claude Code on SWE-Nexus (C16), level with OpenCode on ANCHOR completion (C17), and well below Claude Code on SpreadsheetBench 2 accuracy (C18). The highest assistant result on GitChameleon without the problem statement (C6). Equal generation success to a specialist system but at about 19× the tokens (C19); lower file recall than Cursor, OpenCode and Qoder (C20). Same value as Claude Code (50). |
| Disputes | 20 | 45 | **Two high/critical CVEs**, both fixed in code; one advisory lacks a patched version. **A supply-chain incident** that grew out of a privately reported flaw left unaddressed for 5+ weeks, plus slow responses to several 2025 reports. No legal action. Same value as Cursor agent and Claude Code (45). |
| Adherence to limits | 25 | 40 | **Many successful injection and tool-poisoning attacks:** C1 (1.0 on v3.82.0 with two models), C3, C10 (45% code execution), C11 (>90%), C13–C15. No command allowlisting by default (C1). **Positives:** it refused poisoned file reads with Sonnet 4.5 (C4), and with approval on, 0 of 7 skill vulnerabilities remained (C12). Rule-following was 51% without add-ons (C7). Same as Cursor agent and Claude Code (40). |
| Evidence quality | 25 | 85 | **20 counted, 8 peer-reviewed** (FSE, DSN, S&P, AAAI, ACL), mostly 2026, with six versioned tests within 12 months. Kept at the bottom of the A band because 13 of the 20 are security studies, most do not state a version, none tests v4.x, two pairs share authors, and the sample is incomplete. |

0.30 × 50 + 0.20 × 45 + 0.25 × 40 + 0.25 × 85 = 55.25. This rounds to **55** under the half-up rule (Decision 0010).

**Grade A:**
- 20 counted (≥7) and 8 peer-reviewed (≥3).
- A test within 12 months that states the version: C1 v3.82.0 (peer-reviewed), plus C12 CLI 3.0.47, C9 3.77.0 and C10 3.66.0.

**Sensitivity:**
| Variant | Counted | Peer-reviewed | Versioned ≤12 months | Grade |
|---|---|---|---|---|
| D3a (recommended) | 20 | 8 | C1, C4, C9–C12 | A |
| D3a + count AutoData (O10) | 21 | 9 | same | A |
| D3b (drop fixed-host F: C5, C8) | 18 | 6 | same | A |
| D3c (same-model/harness comparisons only: drop C5, C7, C8, C19) | 16 | 5 | same | A |
| D4b (require a v4.x extension or CLI 3.0.x test within 12 months that is peer-reviewed) | 20 | 8 | none peer-reviewed | B |
| Preprints excluded entirely (illustration only, not a rule) | 8 | 8 | C1, C4 | A |

**Score range:**

| Change | Overall |
|---|---|
| As proposed | 55 |
| Disputes 50 | 56 (56.25) |
| Completion 55 | 57 (56.75) |
| Adherence 35 | 54 (54.0) |
| Evidence 80 | 54 (54.0) |

The plausible range is 54–57.

## Risks and uncertainties
1. **Model and harness attribution.** Each figure describes Cline with a given model and approval setting. Several security results come from the model obeying injected text, not from the harness alone.
2. **Security-heavy evidence.** 13 of 20 counted are security studies, many by authors proposing attacks. This could understate everyday reliability. The factor notes keep completion and adherence separate.
3. **Versions.** Most studies do not state a version. The extension moved to v4.0.0 (26 Jun 2026) and no counted test states v4.x. The CLI line (3.0.47) is current.
4. **CVE metadata.** The CVE-2026-44211 advisory and NVD say no patch, while the code fix shipped in kanban 0.1.66. If the CLI's dependency range did not pick up 0.1.66 for a period, exposure may have lasted longer. Wording says "fixes in code".
5. **Unresolved 2025 reports.** Embrace The Red and IDEsaster have no confirmed Cline fix. Mindgard's issues were mitigated in v3.35.0 per Mindgard.
6. **Peer-review calls.** C7 is accepted at UIST '26 (November); its printed DOI was not yet registered on 20 Oct 2026. C8 is ECCWS proceedings. C19 is an ICML workshop, treated as not peer-reviewed (D5).
7. **Flattened tables.** C1, C3, C12 and O10 figures were read from extracted text; C12 and C20 were rechecked against PDF layouts. The C3 per-client mapping is approximate, so only a range is quoted.
8. **Forks.** Roo Code and Kilo Code share much of Cline's code and prompt (O2). Readers may assume fork results apply; the scope says they do not.
9. **Sample.** 495 of 790 OpenAlex works were not downloaded. More counted sources likely exist (D9 banner).
10. **Disclosures.** Google and ServiceNow (C6), Chaitin (C3), Intuit (C10), Alibaba/Qoder (C20), Commonwealth Bank (C19), and industry co-authors (C18). Competing or add-on methods: C7, C18, C19, C20.

## Decisions (D1–D10 approved 2026-10-20; D11 approved 2026-10-20; D12 pending)
- **D1 Scope.**
  - (a) One entry for cline/cline: VS Code extension v3.x–v4.1.25, JetBrains plugin, CLI ≤3.0.73 (including GitHub Actions use) and companion servers under disputes. Forks are excluded. **Recommended.**
  - (b) Extension only. This drops C12 (CLI 3.0.47) and C14 (CI workflow), and moves both CVEs out of scope. 18 counted, 8 peer-reviewed, grade A. Not recommended: the CLI is the same agent and product.
  - (c) Include Roo Code and Kilo Code results. Not recommended: they are different products (0036 caution 2).
- **D2 Developer set.** Cline Bot Inc., Saoud Rizwan and the Cline team. Exclude cline-bench and vendor posts. **Recommended.**
- **D3 What counts.**
  - (a) Count independent studies that run unmodified Cline, including security attack studies and fixed-host studies (C5, C8), as in 0037/0038/0085 D3a. AutoData and AIPC are other. **Recommended.**
  - (b) Drop fixed-host studies: 18 / 6.
  - (c) Same-model or harness comparisons only: 16 / 5.
  - (d) Also count AutoData: 21 / 9.
  - Grade A and the score hold under all four.
- **D4 Versioning for A.**
  - (a) Accept C1 v3.82.0 (peer-reviewed, May 2026) and C12 CLI 3.0.47 (Jul 2026, current CLI line) as current-version tests, with C4, C9, C10 and C11 supporting. **Recommended:** 0051/0084 D7a requires a stated version within 12 months.
  - (b) Require a v4.x extension test, giving grade **B**. Not recommended. Note "none states a v4.x version" on the page instead, as drafted.
- **D5 Peer-review calls.** C7 counts as peer-reviewed (accepted; DOI printed but not yet registered). C8 counts (ECCWS proceedings). C19 does not (workshop paper). **Recommended.** Alternative: C19 as peer-reviewed gives 9; C7 as not yet published gives 7. A either way.
- **D6 Disclosures.** As listed in Risks item 10, plus the shared authors C1/C3 and C16/C17. **Recommended as drafted.**
- **D7 CVE wording.**
  - (a) "Two high or critical CVEs in companion servers of the command-line tool have fixes in code". The page gives detail on the missing patched-version field for CVE-2026-44211 and on the kanban 0.1.66 fix. Both are treated as fixed, so no 55-type treatment. **Recommended.**
  - (b) Treat CVE-2026-44211 as unfixed, as its advisory reads. The disputes factor would be judged against the 55-type rule, but other incidents keep it at about 45, so there is no score change. The wording would say "no patched version listed".
- **D8 Score.** 55 / A (50 / 45 / 40 / 85). Alternatives: 56 / A (disputes 50), or 54 / A (adherence 35).
- **D9 Recheck banner.** Show "Citation check incomplete — recheck later": OpenAlex only (295 of 790 downloaded), Semantic Scholar rate-limited. **Recommended.**
- **D10 Cross-reference / caveat edits (approved: D10a; applied in the final private draft, listed separately in the patch summary):**
  - (a) **Coding-agents comparison caveat** (scripts/build_data.py): "Open-source frameworks (OpenHands, SWE-agent, mini-SWE-agent, Aider)" becomes "… Aider, Cline)". The caveat says these are run with a model chosen by the user, which fits Cline. **Recommended** (0083/0085 precedent). Tested separately in the dry run (variant "xref").
  - (b) No other entry needs a cross-reference. Roo Code and Kilo Code have no entries. Claude Code, Cursor agent and OpenAI Codex pages are unaffected. C1/C3/C4/C6 also contain results for those entries, which may be used at their next review; no change now.
- **D11 (APPROVED 2026-10-20, 1:18 PM ET) Entry page + changelog row + feed item + decision record, with the approved D10a caveat edit.** As in the final private draft (combined scratch build). The page title is "Cline (open-source) — Agent Reputation & Trust Clearinghouse", 60 characters.
- **D12 (pending) Deploy.** This would be the first new entry on www.agentclearinghouse.org.

**Recommendation (approved 2026-10-20, 1:14 PM ET, for D1–D10 exactly as drafted):** D1a, D2, D3a, D4a, D5, D6, D7a, D8 (55 / A), D9 and D10a. D11 approved separately (2026-10-20, 1:18 PM ET); D12 held for separate approval.

## Final private draft (scratch clone of master 2a3b699; real tree untouched)
Combined build (entry page, changelog row, feed item, this decision record, D10a caveat edit): see final/final-results.txt for the check output, projected totals and manifest preview.

## Minimum viable version
Approve D1a, D3a, D7a and D8 at 55 / A with D9's banner, and leave the other wording as drafted. D10a can follow separately; skipping it only leaves Cline out of a caveat sentence.

## Plain-English terms
- **Harness / scaffold:** the code around a language model that makes it an agent (prompts, tools, approvals). Cline is a harness that runs in an editor or terminal.
- **Auto-approve / YOLO mode:** settings that let the agent run commands or edit files without asking each time.
- **Prompt injection / tool poisoning:** hidden instructions in files, web pages or tool descriptions that the model may follow.
- **MCP (Model Context Protocol):** a standard way to connect an agent to outside tools ("servers").
- **Same-model comparison:** the same model run in two harnesses, so differences come from the harness.
- **Fixed host:** a study that uses one harness for every run to compare attacks or models.
- **Peer-reviewed:** published at a venue that reviews papers before acceptance.
- **CVE / CVSS:** a public identifier for a security flaw, and its severity score (0–10).
- **Current-version test:** a test within the last 12 months that states the version tested; grade A needs one.

*Informational only; not a guarantee, endorsement, or certification.*
