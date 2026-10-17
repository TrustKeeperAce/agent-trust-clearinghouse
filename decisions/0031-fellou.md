# Decision 0031: Fellou (agentic browser)

**Status: APPROVED by Remington, 2026-10-17**, as Insufficient evidence, as recommended. Category: Browser/web agent. Decisions:
1. D1: Insufficient evidence (0 counted independent performance sources; minimum 3).
2. D2: CAP (COLM 2026) is **excluded for Fellou** as vendor-affiliated. One author did the work during an internship at FellouAI, and FellouAI is listed as an affiliation. Fellou's CAP figures are listed, not counted. CAP stays counted, with disclosure, on Browser Use, Comet and Manus. Even if counted, Fellou would have 1 source, so the outcome is the same.
3. D3: Scope is the Fellou desktop browser and its built-in agent from Fellou 2.0 (3 June 2025) onward, treated as continuous. Fellou says earlier versions no longer work. The open-source Eko framework (MIT) is out of scope.
4. D4: Vendor figures are listed, not counted: Online-Mind2Web 80%, shown on the leaderboard as "unknown evaluation method"; and the Web Bench 72% claim.
5. D5: Security notes are neutral, with no severity wording and no exploit text.
   - Brave (competing browser maker): reported 20 Aug 2025, published 21 Oct 2025; fix status not stated.
   - The Register: a reporter reproduced a similar result.
   - LayerX BioShocking (security vendor): reported 30 Oct 2025; status "no response".
   - All three are listed as other sources, following the Comet precedent.
6. D6: No lawsuits, regulatory actions or CVEs were found. Privacy-policy facts are stated as the vendor's own statements, unverified: the controller is ASI X Inc. (Delaware), and data may be transferred to the US, Japan and Singapore.
7. D7: Informal hands-on reviews are noted in the uncertainties, not counted: Zapier, TheToolNerd, meshedsociety and the laike9m blog.

## Counted independent performance sources (0; minimum 3)
None.

## Listed, not counted
- CAP, arXiv 2608.08392 (COLM 2026, full read): Fellou scored 7.0% full success and 24.0% partial completion on 198 cross-site tasks (Complex-A 28.0%, Complex-P 25.0%), averaging 22.1 min per task, Nov–Dec 2025. Excluded (D2).
- TaskSense, arXiv 2511.09309 (full read): ran Fellou on Windows with three other agents, but its Fig. 5 reports results pooled across all four agents only. No results specific to Fellou.
- WAAA!, arXiv 2605.05509 (full read): Fellou appears only in a capability table; it was not attacked or tested.
- "Configuration, Not Conscience", arXiv 2609.31575: Fellou's system prompt is one entry in a large corpus. This is not a performance test.
- Brave (Oct 2025), The Register (28 Oct 2025) and LayerX BioShocking: demonstrations. Other sources.
- Vendor: Fellou 2.0 launch post, Eko 2.0 post, privacy policy.

## Checked, no Fellou test found
- Papers: Privacy Practices of Browser Agents (2512.07725), Whose Agent Are You? (2606.20910), Mind the Web (2506.07153), BrowseSafe (2511.20597), KNOWS / The Hard Part Comes After Search (2609.30604).
- Industry reports: hCaptcha browser-agent report, Guardio Scamlexity, Berkeley CLTC AgentWatch (tested Atlas, Claude, Comet, Copilot and Gemini only).
- Benchmarks: Online-Mind2Web (vendor submission only) and Web Bench (no independent Fellou entry found).

## Search method
OpenAlex keyword searches and citations of CAP; web searches on benchmarks, security, reviews, company and legal matters; full text read for every candidate.

## Citation check (gate, run 2026-10-17 before publishing)
Semantic Scholar Graph API, with requests spaced minutes apart (about 10:15 AM to 1:10 PM EDT, with breaks):
- Citations of CAP (arXiv 2608.08392): retrieved. 1 citing paper, "Learn from Move: the Next Step for GUI Agents" (arXiv 2610.16720, OpenMOSS). Full text read; it does not mention Fellou.
- Keyword search "Fellou": retrieved. 0 results (no paper has Fellou in its title or abstract).
- Snippet (full-text) search "Fellou": HTTP 429 on every attempt; not obtained. The semanticscholar.org website search returned a bot challenge (HTTP 202) to curl.
Result: no independent test of Fellou found. The outcome is unchanged: Insufficient evidence, 0 counted.

## Disclosures
- CAP's Fellou-intern tie, already disclosed on Browser Use and Comet, is the reason for D2.
- Brave makes a competing browser, and LayerX sells browser security products.

## Uncertainties
- The Semantic Scholar full-text (snippet) search could not be run because of rate limits; the citation and keyword checks were completed.
- D2 is a judgment call.
- Fellou has no public version numbers after 2.0, so the version each source tested is unknown.
- The fix status of the Brave and LayerX findings is unknown.
- The informal reviews describe instability and failures on complex pages. They are not systematic and are not counted.
