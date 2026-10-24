# Decision 0099: GitHub Copilot CLI — 51 / B

**Status: APPROVED by Remington, 2026-10-24 (5:28 AM ET, t270u), as recommended:** 51 / B (completion 45, disputes 50, adherence 40, evidence 70; 5 counted, 0 peer-reviewed); D1a name and category (GitHub Copilot CLI, Coding agent), D2a scope with a 'What this entry does not cover' section, D3a (Microsoft- and GitHub-authored studies not counted), D4a (the Zenn hands-on test counted, so the grade is B; the fragility is stated in the grade note, summary and changelog row: otherwise B- / 46), D5a (three security studies counted), D6a scores, D7a ('GitHub Copilot CLI' added to the managed-products list in the coding-agents caveat), D8a advisory and dispute wording as drafted, D9a 'Model dependence' section, D10a banner kept, D11a (link to the Copilot coding agent entry from the new page only; that entry is not edited), D12a (14 regenerated related sections), D13a (independence statement in this record only). Batch 6. The entry YAML carries `decision: APPROVED`. The changelog row is dated 2026-10-24. Commit and push approved 2026-10-24 (6:01 AM ET, t271u commit approved, W1–W5 as recommended: W1 kept, W2–W4 applied, W5 skipped; deploy not approved); committed as d1382cb. Deploy (D15) needs separate approval. The real repository (HEAD fbbb588; live dpl_2kyj2v2PCGdzWMvNjmx2VfZiJzth) has not been modified. Drafted 23 Oct 2026 (9:45 PM ET, t269u).

**Wording (W-items, t271u, as recommended):** W1 kept (last_reviewed stays 2026-10-23; the row, feed item and as-of dates are 2026-10-24). W2 applied: disputes note says "two reports" instead of "two reported bypasses" (Adversa does not claim an approval bypass). W3 applied: summary says the advisories were fixed "on the day each was published" instead of "quickly". W4 applied: "Microsoft or GitHub authors" in the summary, and "Many" instead of "Most" in the vendor-studies uncertainty. W5 skipped: the two check-coverage gaps found by tamper tests (tie order among equal scores in the index; a banned word added only to page HTML) are left for a later packet. No score, grade, count, source or date changed.

**Citation check incomplete — recheck later.**
- **OpenAlex full text** was the main search ("Copilot CLI", "copilot-cli", "gh copilot", "GitHub Copilot in the CLI"). 125 works were screened; 78 full texts were downloaded (47 failed) and 77 with mentions were read in context.
- **Cross-entry recheck:** the 355 arXiv sources cited by the 43 live entries were re-downloaded and searched for Copilot CLI.
- **arXiv API:** added nothing. **Semantic Scholar:** rate-limited (HTTP 429), not used.
- **Security records:** GitHub repository advisories, OSV and NVD. The PromptArmor, Adversa AI, The Register and issue #1675 pages were fetched 23 Oct 2026.
- **Found, not reviewed:** Explicit Edit Benchmark (the leaderboard data download was blocked by the box's automatic safety review, and the fetch was not retried), a Universidad Pública de Navarra thesis, an OfficeBench gist by an author of unknown affiliation, Agent-HAnS and an SSRN "Context Rot" paper (not retrieved). FastContext (2606.14066) has been withdrawn from arXiv.
- Search notes: research/source-table.md.

## What happened (facts and sources)
1. **Product** (D1, D2). GitHub Copilot CLI (the `copilot` command; npm @github/copilot; https://github.com/github/copilot-cli) is GitHub's terminal coding agent. It is proprietary; the public repository carries issues, releases and the changelog. Users pick a model from Anthropic, OpenAI, Google or Microsoft, or leave the Auto setting on.

   | Date (ET) | Milestone (npm, changelog, advisories) |
   |---|---|
   | 6 Jan 2023 | github/copilot-cli repository created (before this product; see naming) |
   | 25 Sep 2025 | 0.0.1 on npm; public preview |
   | 25 Oct 2025 | gh copilot extension ("GitHub Copilot in the CLI") retired |
   | 1 Feb 2026 | 0.0.400 (tested in the Zenn hands-on test, C2) |
   | 25 Feb 2026 | 0.0.418; generally available. PromptArmor reports the env bypass |
   | 6 Mar 2026 | 0.0.423 fixes CVE-2026-29783; 1.0.0 released the same day |
   | 9 Mar 2026 | 1.0.3: env commands need approval |
   | 6 May 2026 | 1.0.43 fixes CVE-2026-45033 |
   | Jun 2026 | 1.0.65 (tested in Approval Laundering, C5) |
   | 3 Aug 2026 | 1.0.78: rewind restores only files Copilot changed (issue #1675) |
   | 17 Sep 2026 | Adversa AI reports the CCI exfiltration (published 6 Oct) |
   | 22 Oct 2026 | 1.0.103, latest stable; 204 npm versions in total |

   On 23 Oct 2026 the repository had about 11,300 stars.
2. **Naming** (D2, D11). GitHub has used the name for three products:
   - the 2023 GitHub Next "Copilot for CLI" preview;
   - the gh copilot extension (2023–25 Oct 2025), which suggested and explained single commands;
   - the current agent.

   GitHub Copilot coding agent, the cloud agent, has a live entry at 57/B; its scope already excludes Copilot CLI. Tasks that Copilot CLI hands to it with `&` run there. AWS Copilot CLI is an unrelated Amazon tool. Some papers say only "GitHub Copilot"; each was checked for which product it used.
3. **Results.**
   - **5 counted** independent performance sources: **0 peer-reviewed**, **2 state a version** (0.0.400, 1.0.65).
   - **9 other.**
   - **11 vendor sources listed, not counted**, plus about 20 further Microsoft- or GitHub-authored papers that used Copilot CLI as a research tool.
   - No competitor-authored head-to-head was found.

   | # | Source | Result for Copilot CLI |
   |---|---|---|
   | C1 | ProjDevBench (arXiv 2602.01655; UC Merced, SJTU and others) | Final 61.73 with GPT-5 (4th of 5), 67.18 with Sonnet 4.5 (4th of 5), 55.32 with Gemini 3 Pro Preview (last of 3); 71.10 → 36.63 easy → hard with Sonnet 4.5 |
   | C2 | Zenn hands-on test (individual developer; 0.0.400, 1 Feb 2026) | 180 runs on review tasks with GPT-5.2: mean time 48.05 s vs Codex CLI 48.19 s; AI-judged quality 26.67 vs 28.18 of 30 |
   | C3 | MOSAIC (arXiv 2607.02857; SYSU, PKU and others) | Command-composition attacks succeeded in 96.24% of cases; other agents 95.84–97.43% |
   | C4 | OpenART (arXiv 2608.00677; Fudan, Shanghai AI Lab) | Strict attack success averaged 89.1% (65.4–100% by model); 13 other agents 79.1–90.3%, Aider 59.1% |
   | C5 | Agent Approval Laundering (arXiv 2609.28586; IIE-CAS and others; 1.0.65) | An approved MCP call also used network access that the approval did not show; Qwen Code had the same gap, Claude Code a related one |
4. **Vendor material** is not counted (0031; D3). This covers Microsoft- or GitHub-authored studies and GitHub's own material:
   - YoloFS (SOSP 2026, peer-reviewed; a Microsoft Research co-author; 0.0.411);
   - Setup Complete (corresponding author at Microsoft; 1.0.60);
   - HealthAgentBench, TokenEconomizer, Lights-off (1.0.74), Exactly-once (1.0.86), Building to the Test (1.0.56), BC-Bench and the Microsoft adoption study;
   - the GitHub blog harness evaluation, the repository, the docs and the changelog.

   Affiliations were checked from the author blocks and email addresses. These studies include results both more and less favourable than the counted ones.
5. **Disputes and security** (D8). These are described on the page and not counted as tests.
   - **CVE-2026-29783** (GHSA-g8r9; high, CVSS 4.0 7.1 on the advisory and 7.5 on the CVE record): fixed in 0.0.423 on the day the advisory was published.
   - **CVE-2026-45033** (GHSA-9ccr; medium on the advisory, 8.5 on the CVE record): fixed in 1.0.43 on the day it was published. The advisory's "Affected versions" text says "prior to 1.0.42", while its range field and the CVE record say ≤ 1.0.42 / prior to 1.0.43.
   - **PromptArmor (Feb 2026):** GitHub said the env bypass was a known issue, not a significant risk and not eligible; the 1.0.3 changelog then made env commands need approval.
   - **Adversa AI (Oct 2026):** GitHub validated the report but told The Register it is "not a product vulnerability"; Adversa says it still reproduces. It is model-dependent: mai-code-1.1-flash ran the chain in 50% of attempts and two GPT-5.6 models refused.
   - **Issue #1675:** checkpoint restore deleted untracked files. The report was open from 25 Feb to 19 Sep 2026; the bot that closed it cited 1.0.86, but the rewind change was in 1.0.78.
   - No lawsuit or regulatory action was found.

## What the rules say
- **Grade (methodology / check_scores):** fewer than 3 counted sources is Insufficient evidence, 3–4 is B-, 5–6 is B, and A needs 7 or more with at least 3 peer-reviewed and at least 1 current-version test within 12 months. **5 counted → B.** Without C2 (D4b) there would be 4 → B-.
- **Evidence-quality bands:** B 70–84, B- 55–69. **70** is the floor of B: no peer-reviewed source, one blog test, and few stated versions.
- **Overall** = 0.30 × 45 + 0.20 × 50 + 0.25 × 40 + 0.25 × 70 = **51.00 → 51** (round half up).
- **Precedents:**
  - 0031: vendor material is not counted.
  - 0042: systems built on the agent are not counted.
  - 0071: documented hands-on tests count.
  - 0080/0083: competitor-authored sources are listed, not counted.
  - 0087 D3a: attack studies count.
  - 0079: other = other + anecdotal.
  - 0065: a new entry needs a feed item.
  - 0075: title of 68 characters or fewer.
  - 0090 D1: the coding-agents caveat must name every Coding agent entry.
  - 0098: related sections are regenerated from the category field.
- **Closest analogs:** Google Jules 50/B- (50/55/40/55, 3 counted), Replit Agent 51/B, Gemini CLI 53/A (45/45/35/85), Copilot coding agent 57/B (45/60/50/75).

## Factor reasoning (draft)
- **Completion 45 (range 40–50).** The evidence is thin and mixed. In ProjDevBench Copilot CLI is below most peers using the same model. In the Zenn test it is level with Codex CLI on review tasks only. GitHub's parity claims are not counted. Scoring 40 if C2 is not counted.
- **Disputes 50 (45–55).** Both CVEs were fixed on the day of the advisory and credited. Against that: two validated reports were declined as not vulnerabilities (one later changed in 1.0.3, one still reproducing); the data-loss bug stayed open for 7 months and was closed with the wrong release cited; and the CVE-2026-45033 version text is inconsistent. No lawsuit or regulatory action. Between Gemini CLI (45) and the coding agent (60).
- **Adherence 40 (35–45).** In the counted attack studies, attacks succeed about as often as against peers (96.24% and 89.1%), with one approval-record gap. Outside the counted studies there were three approval bypasses (two fixed) and model-dependent exfiltration in autopilot. Comparable to Claude Code, Cline and OpenCode (40). Gemini CLI got 35 because comparative studies showed more exposure than peers; here they show parity.
- **Evidence 70 (70–75).** 5 counted, 0 peer-reviewed, 2 versioned, a fast release cadence, and many vendor studies excluded.
- **Sensitivity:**
  - completion 40 → 50, 50 → 53;
  - disputes 45 → 50, 55 → 52;
  - adherence 35 → 50, 45 → 52;
  - evidence 75 → 52.
  - **Overall range 50–53 at B.** Without C2: 40/50/40/55 → 45.75 → **46, B-**.

## Risks and uncertainties
- **B rests on one blog test (C2).** It used one model and an AI judge, and covered review tasks only. The author was not sure the reasoning setting matched between the two tools.
- **No peer-reviewed independent test.** The only peer-reviewed study found (YoloFS) has a Microsoft co-author.
- **Versions:** only 2 of 5 counted sources state one. Approval behaviour changed in 0.0.423, 1.0.3 and 1.0.43.
- **Model dependence:** the Auto setting can change the model from one session to the next.
- **Naming:** three products share the name, and "GitHub Copilot" in papers is often ambiguous.
- **Dates:** the repository's 2023 creation predates the product. 0.0.423 and 1.0.0 both shipped on 6 Mar 2026. The CVE-2026-45033 version text is inconsistent. The ProjDevBench test date is inferred (the Gemini 3 Pro Preview release to the Feb 2026 preprint).
- **Possible under-count:** the Explicit Edit Benchmark and the thesis were not reviewed; the leaderboard fetch was blocked and not retried. Counting either could add sources, but would not change the grade below 7 counted.
- **Independence:** the clearinghouse repository is hosted on GitHub (account TrustKeeperAce), which is ordinary hosting use. No financial relationship with GitHub or Microsoft is known; funding was not checked beyond the 0091 policy.
- **Existing check gaps found in tamper tests (15 of 17 cases caught; final/tamper.txt):** check_all does not catch tie order among equal scores in the index, or a banned word added only to the page HTML. final_checks.py covers both for this draft.

## D-items (recommendations)
- **D1 Category and name:** Coding agent; "GitHub Copilot CLI", slug github-copilot-cli, homepage https://github.com/github/copilot-cli. Title "GitHub Copilot CLI — …" is within 68 characters. **Recommend (a) approve.**
- **D2 Scope:** covers the copilot command from the 25 Sep 2025 preview to 1.0.103.
  - Excludes the gh copilot extension, the 2023 GitHub Next preview, Copilot coding agent (including `&` hand-offs), IDE agent mode, code review, SDK-built products, AWS Copilot CLI and model-only results.
  - Includes a "What this entry does not cover" section.
  - **Recommend (a).**
- **D3 Vendor exclusion:** Microsoft- and GitHub-authored studies are not counted (0031), including the peer-reviewed YoloFS. (b) would count non-GitHub Microsoft Research work, which goes against 0031. **Recommend (a).**
- **D4 Zenn hands-on test (C2):**
  - (a) count it per 0071 → 5 counted, B, 51;
  - (b) list it as other → 4, B-, 46.
  - **Recommend (a)** for consistency with 0071 (the AI Agents Library review was counted), with the fragility stated in the grade note, summary and changelog row.
- **D5 Security studies counted (C3–C5) per 0087 D3a.** Approval Laundering is qualitative; (b) would list it as other, which gives 4 → B- (with D4a). **Recommend (a).**
- **D6 Scores:** 45/50/40/70 → 51 / B. **Recommend (a).**
- **D7 Caveat edit:** "…Google Jules, Gemini CLI, GitHub Copilot CLI) are tested as shipped." in scripts/build_data.py. check_all requires this. **Recommend (a).**
- **D8 Advisory and dispute wording as drafted:** GitHub's position is quoted via PromptArmor and The Register, and the CVE-2026-45033 version text is flagged. **Recommend (a).**
- **D9 Model dependence section**, including the Auto routing finding. **Recommend (a).**
- **D10 Keep the "Citation check incomplete — recheck later" banner**, with the not-reviewed items listed in this packet. **Recommend (a).**
- **D11 Cross-references:** the new page links to the Copilot coding agent entry in "What this entry does not cover". The coding agent entry's own text is **not** edited; its note already places the Copilot CLI CVEs outside its scope. **Recommend (a) as drafted.**
- **D12 0098 related sections:** the 14 existing Coding agent pages change only inside their regenerated "Other entries in this category" section (adding GitHub Copilot CLI), and the new page gets a 14-link section. This is required by check 0098. **Recommend (a).**
- **D13 Independence statement** (this packet only; not on the page): GitHub hosts the clearinghouse repository; no other relationship is known. (b) would also add a line to the page. **Recommend (a).**
- **D14 Commit/push** and **D15 Deploy:** not requested; each needs separate explicit approval.

## Files that would change (scratch dry run against fbbb588)
29 files: 656 insertions, 25 deletions (dryrun/patch-stat.txt, dryrun/changed-files.txt).
- **New (3):**
  - agents/github-copilot-cli.yaml;
  - decisions/0099-github-copilot-cli.md;
  - public/agents/github-copilot-cli.html.
- **Data and script (2):**
  - data/changelog.yaml (row 2026-10-23-0099);
  - scripts/build_data.py (caveat).
- **Existing entry pages (14, related section only):** aider, claude-code, cline, cursor-agent, devin, gemini-cli, github-copilot-coding-agent, google-jules, mini-swe-agent, openai-codex, opencode, openhands, replit-agent, swe-agent.
- **Generated (10):**
  - public/index.html;
  - public/llms.txt and public/llms-full.txt;
  - public/sitemap.xml;
  - public/compare/coding-agents.html;
  - public/changelog.html;
  - public/updates.json and public/updates.xml;
  - public/data/agents.json and the CSV.

  The exact list is in dryrun/changed-files.txt.
- **Totals:**
  - entries 43 → 44, scored 32 → 33, insufficient 11;
  - changelog rows 83 → 84, feed items 97 → 98, sitemap 51 → 52;
  - banners 25 → 26.
- Other entries' agents.json records are byte-identical; their scores, grades and source counts do not change.

## Minimum viable version
Approve D1–D13 as recommended → 51 / B. If the blog test is not accepted (D4b), the entry is 46 / B- with completion 40 and evidence 55, and all other items are unchanged. In either case, nothing goes live until D14 and D15 are approved separately.

## Plain-English terms
- **Counted source:** an independent test that the rules let into the grade.
- **Vendor:** GitHub, Microsoft or their staff.
- **Hands-on test:** one person's documented trial with a method and results.
- **Attack success rate:** the share of attack attempts that worked.
- **CVE / GHSA:** public security-advisory identifiers.
- **Autopilot:** a mode where Copilot CLI acts without asking at each step.
- **Auto:** a setting where GitHub picks the model.
- **Harness:** the agent software around the model.
- **Related section:** the "Other entries in this category" list added in 0098.

---
Informational only. Scores summarize cited public evidence under published rules; they are not a guarantee, endorsement, certification or ranking of quality.
