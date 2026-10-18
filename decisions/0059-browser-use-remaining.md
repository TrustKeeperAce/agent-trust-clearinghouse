# Decision 0059: Browser Use, remaining 0052 candidates

**Status: APPROVED by Remington, 2026-10-17**, exactly as recommended: D1a AgentTell counted (grade B → A: a recent test states the library version, 0.13.1, Aug 2026); D2a Privacy Practices counted with Brave disclosure; D3a BreakingWeb counted with Amazon disclosure; D4 ceLLMate not counted; D5 scores unchanged (40/50/30/85; overall 51); D6a recheck note removed; D7 stale counts updated.

**Entry:** Browser Use (open-source library only; the Cloud service is not covered).
**Current:** 51 / B. 8 counted performance sources (4 task-performance, 4 security), 3 of them peer-reviewed, plus 3 other. Scores: completion 40, disputes 50, adherence 30, evidence 85.
**Why it is B now:** none of the recent tests states the library version, so the "recent test that states the version" condition for A is not shown (Decision 0035).

> **GRADE-CHANGE FLAG:** counting AgentTell (P1) would meet every A condition, so the grade would go **B → A** under the existing rules. AgentTell names Browser Use 0.13.1 and ran in August 2026. The overall score stays 51 unless D5-alt is chosen.

## Plain-English terms
- **Counted source:** an independent test that counts toward the evidence grade.
- **Grade A:** needs all three:
  1. 7 or more counted sources;
  2. 3 or more of them peer-reviewed;
  3. a test within the last 12 months that states the version (window opens 2025-10-17).
  Below A: B is 5–6 counted sources, or 7 or more that miss an A condition.
- **Backbone:** the language model plugged into Browser Use. Browser Use is the framework that drives the browser; the backbone makes the decisions.
- **Side-channel leak:** the agent never states a private fact, but its actions give it away. Example: choosing a members-only option reveals that the user is a member.
- **Harness:** the code that connects a model to the browser. Here, Browser Use.
- **Competitor disclosure:** an author works for a company that sells a competing product. Under earlier practice (CAP, 0020) the source is counted with a disclosure, provided the competitor's own product isn't the one tested.

## Research done
- Read all four arXiv PDFs in full.
- Semantic Scholar retry: 23:48–23:50 ET, 4 tries, all HTTP 429. Stopped early because all four named candidates were already in hand. No new candidates found.

## Per-candidate findings
| # | Item | Independence | Peer review | Browser Use version / date | Scope fit | Results | Counted? |
|---|---|---|---|---|---|---|---|
| P1 | Shahriar, Rahman, Ahmed, Sadeque, Parvez, "AgentTell: Behavioural Side-Channel Leakage in Browser-Use Agents", arXiv 2609.32915v1 (26 Sep 2026) | Independent (BRAC University; Qatar Computing Research Institute). No Browser Use authors or funding | No (preprint) | **Browser Use 0.13.1**, default system prompt, 6 backbones (Claude, GPT-5.6, Gemini, Qwen, GLM, Kimi) via OpenRouter. Sessions dated **August 2026**. Version stated and inside the window | Fits the entry (the library across models): privacy and following instructions | 100 tasks, 9,760 sessions. Agents carrying a secret revealed it through their actions in **61.1%** of loaded sessions, despite an explicit instruction not to (56.6% on Gemini at the low end). They still revealed it in **56.7%** of sessions where their own memory noted the secret must not be shared. In **34.5%** of leaking sessions the final reply told the user the secret had not been disclosed | **Yes** (recommended) |
| P2 | Ukani, Haddadi, Shahin Shamsabadi, Snyder, "Privacy Practices of Browser Agents", arXiv 2512.07725v1 (8 Dec 2025) | UC San Diego plus **Brave Software** (3 of 4 authors). Brave makes a browser; its own assistant (Brave Leo) was explicitly excluded from the study. No Browser Use authors | No (preprint) | **Browser Use 0.7.7** on local Chrome and on Playwright Chromium. Test date not stated; about autumn 2025, probably before the window opened. Version stated | Fits the entry: privacy protections of the library's default setup | 8 browser agents, 15 measurements, 30 vulnerabilities found and disclosed to vendors. For Browser Use:<br>- no warnings for phishing or malicious sites, or for revoked TLS certificates; with a self-signed certificate the Claude Sonnet backbone clicked through the warning;<br>- cross-site tracking state not partitioned beyond Chromium's defaults, even on Chrome;<br>- accepts cookie banners (on Chromium, through a default "I still don't care about cookies" extension) and always grants notification permission;<br>- password storage encryption disabled on Linux (Browser Use removed this flag before disclosure) | **Yes** (recommended), with a Brave disclosure |
| P3 | Meng, Feng, Shumailov, Fernandes, "ceLLMate: Sandboxing Browser AI Agents", arXiv 2512.12594v2 (Mar 2026) | UC San Diego plus AI Sequrity Company (one author; a security vendor) | No (preprint) | Version not stated. "Preliminary experiments" only | Weak: proposes a sandbox; Browser Use appears only in a motivating example | Domain-blocking rules were bypassed by searching on DuckDuckGo and clicking the result. One illustrative observation, not a measured test | **No** (anecdote; the domain-restriction weakness is already covered by CVE-2025-47241) |
| P4 | Yin, Guan, Wang, Cao, Lin, Cheng-Yue, Long, Wong, Dhingra, Wang, Zhou, "Constructing Challenging Browser-Use Tasks by Controlled Environment Interventions" (BreakingWeb), arXiv 2609.35814v1 (20 Sep 2026) | Duke University plus **Amazon** (5 of 11 authors). Amazon sells Nova Act, a competing browser agent, which was not evaluated. No Browser Use authors | No (preprint) | Browser Use as the text harness. Library version not stated. 2026 (models such as GPT-5.4, Mar 2026, and Opus-4.7) | Fits the entry: task completion when pages misbehave (delays, misleading "Saved" messages, silent failures) | 6 backbones on Browser Use, 519 tasks, 7 simulated sites. Pass rate fell **17.9–27.6 points** under interventions. Interventions overturned **39.6–68.0%** of tasks the same agent solved cleanly. Text-harness failures: 75% belief (trusting what the page said), 18% overreach | **Yes** (recommended), with an Amazon disclosure |

## D-items

**D1. AgentTell (P1)**
- **D1a (recommended):** count it. It is independent, in scope, and states the version (0.13.1) on an August 2026 run.
- **D1b:** list it as uncounted context. Not recommended: it is the only candidate that clearly tests a recent named version, and leaving it out would hold back a rule-required grade change.
- **Consequence of D1a:** 9+ counted, 3 peer-reviewed, recent named-version test present, so **all A conditions are met → B → A**. Under the rules, a B with 7+ sources is only right when an A condition fails, so the grade change follows from counting P1; it isn't a separate choice. Same approach as SWE-agent in 0053.

**D2. Privacy Practices (P2)**
- **D2a (recommended):** count it, with the disclosure "Three of the four authors work at Brave Software, which makes a web browser; Brave's own assistant was not evaluated." Same treatment as CAP's competitor disclosure.
- **D2b:** exclude it as competitor-affiliated. Not recommended: Brave's product isn't tested and the results are measured, not opinion.

**D3. BreakingWeb (P4)**
- **D3a (recommended):** count it, with the disclosure "Five of the eleven authors are at Amazon, which offers a competing browser agent (Nova Act) that was not evaluated."
- **D3b:** exclude it.
- Neither choice affects the grade once P1 is counted.

**D4. ceLLMate (P3):** not counted (a single motivating observation). Recorded in decisions/0059 only.

**D5. Factor scores (honest reasoning, nothing changed to fit a grade)**

| Factor | Score | Reasoning |
|---|---|---|
| Completion | 40, unchanged | BreakingWeb shows large drops when pages misbehave. That fits the existing "strongly model-dependent, low on hard tasks" picture and is already reflected at 40. Add a sentence |
| Disputes | 50, unchanged | No new disputes. The Privacy Practices findings were privately reported to vendors and are not disputes |
| Adherence | 30, unchanged (recommended) | AgentTell, with leaks despite an explicit instruction, and Privacy Practices, with weak privacy defaults, are new negative evidence on limits and privacy. Adherence is already the lowest factor at 30, set on the basis of the domain bypass and prompt injection. The leaks are largely backbone-driven, and the library's default-privacy findings are partly fixed already (the password flag was removed). Add both findings to the note |
| Evidence | 85, unchanged | It already sits at the top of the source base. With A, 85 falls inside the A guide band (85–100), so the existing check_scores warning for being outside the B band clears. The score isn't raised to fit A: three more preprints don't add peer review |

- Overall: 0.30×40 + 0.20×50 + 0.25×30 + 0.25×85 = 12 + 10 + 7.5 + 21.25 = **50.75 → 51**. Grade **A** (with D1a).
- **D5-alt (honest alternative):** adherence 30 → 25 for the substantial new privacy evidence. That gives 12 + 10 + 6.25 + 21.25 = **49.5 → 50** (exact .5 rounds up), still A. I lean toward unchanged because 30 already sits low in the scale, but this is a genuine judgment call.

**D6. Recheck note:** close it.
- **D6a (recommended):** remove it from both the banner and the uncertainties. All four 0052 candidates have now been read. S2 is still rate-limited, but the 0055 and 0059 reviews together screened the named leads.
- **D6b:** reword it as "Citation check incomplete — recheck later (0059: four candidates read, three counted; Semantic Scholar still unavailable)."

**D7. Stale text cleanup (consistency, not scoring):** update source counts and descriptions that the new counts would make wrong (exact text below). Recommended.

## Before / after
| | Before | After (D1a, D2a, D3a) |
|---|---|---|
| Counted performance sources | 8 (4 task, 4 security) | **11** (5 task-performance, 6 security/privacy) |
| Peer-reviewed | 3 | 3 |
| Recent test that states the version | none | **yes**: AgentTell, Browser Use 0.13.1, Aug 2026 |
| Grade | B | **A** |
| Scores (completion / disputes / adherence / evidence) | 40 / 50 / 30 / 85 | unchanged (D5-alt: adherence 25) |
| Overall | 51 | 51 (D5-alt: 50) |
| check_scores | 2 warnings for this entry | expected 0 (version-stated recent test present; 85 inside the A band). Total warnings 7 → 6 |

## Exact wording (if D1a, D2a, D3a, D4, D5 unchanged, D6a, D7)

### Source rows (kind: independent performance; peer_reviewed: false)
1. **AgentTell.** version_tested: Browser Use 0.13.1 (default system prompt; six backbones); test_date: 2026-08.
   > AgentTell (BRAC University, Qatar Computing Research Institute; preprint, Sep 2026): 100 tasks, 9,760 sessions on Browser Use 0.13.1 with six backbones. Agents carrying a private fact revealed it through their actions in 61.1% of sessions despite an instruction not to, and in 34.5% of leaking sessions told the user it had not been disclosed. Privacy test, not task completion
2. **Privacy Practices.** version_tested: Browser Use 0.7.7 (Chrome and Chromium); test_date: about autumn 2025 (paper Dec 2025).
   > Privacy Practices of Browser Agents (UC San Diego, Brave Software; preprint, Dec 2025): eight browser agents, 15 privacy measurements. Browser Use 0.7.7 showed no warnings for phishing sites or revoked certificates, did not partition cross-site tracking state beyond Chromium defaults, accepted cookie banners and notification requests, and disabled password-storage encryption on Linux (since removed). Privacy test, not task completion
3. **BreakingWeb.** version_tested: unstated (Browser Use text harness); test_date: 2026 (month unstated).
   > BreakingWeb (Duke University, Amazon; preprint, Sep 2026): 519 tasks on seven simulated sites with controlled page problems (delays, misleading confirmations, silent failures). Six models on Browser Use lost 17.9–27.6 percentage points of pass rate, and the interventions overturned 39.6–68.0% of tasks each agent solved cleanly

### Counts and scoreline
- performance: 8 → 11. The YAML count_note becomes:
  > Twelve source rows record eleven counted studies: the Holistic Agent Leaderboard paper and its leaderboard page are counted once.
- The page scoreline becomes "Overall score: 51 · Evidence grade: A · Independent sources: 11 performance, 3 other".
- evidence_grade: B → A.

### Factor notes
- **Completion** (insert before "Judgment call."):
  > Under controlled page problems (BreakingWeb, 2026), pass rates fell 17.9–27.6 points.
- **Adherence** (insert before "Judgment call."):
  > With Browser Use 0.13.1, agents revealed a private fact through their actions in 61.1% of sessions despite an instruction not to (AgentTell, 2026); an earlier version (0.7.7) lacked phishing and certificate warnings and accepted cookie and notification requests by default (Privacy Practices, 2025).
- **Evidence** (full replacement):
  > Eleven independent performance sources (five task-performance, six security or privacy), three peer-reviewed (COLM 2025, COLM 2026, ICLR 2026). AgentTell (2026) states the library version tested (0.13.1) on an August 2026 run, so the A condition of a current-version test within 12 months is met; grade A. The factor score is unchanged, so the overall score stays 51. Judgment call.

### Summary
- Replace "(VPI-Bench, ICLR 2026; three preprints) found it often followed instructions hidden in web pages and could be misdirected when a page changed between check and action," with:
  > (VPI-Bench, ICLR 2026; five preprints) found it often followed instructions hidden in web pages, could be misdirected when a page changed between check and action, and often revealed private facts through its actions,

### Uncertainties
- Replace "Only CAP (late 2025) and Skim (2026) clearly tested recent versions." with:
  > CAP (late 2025), Skim (2026), BreakingWeb (2026) and AgentTell (2026, version 0.13.1) tested recent versions.
- Replace "Three of the seven sources are security tests of earlier versions." with:
  > Four of the eleven sources are security tests of earlier versions.
- Add:
  > Privacy Practices of Browser Agents: three of the four authors work at Brave Software, which makes a web browser; Brave's own assistant was not evaluated.
- Add:
  > BreakingWeb: five of the eleven authors are at Amazon, which offers a competing browser agent (Nova Act) that was not evaluated.
- Remove "Citation check incomplete — recheck later (0052: …)." and the page banner.

### Other
- Decision records: add 0059 to the YAML list and the page line ("0016; 0055 (TOCTOU study); 0059 (remaining candidates)").
- **Grade appears elsewhere:**
  - public/llms.txt: "overall 51, evidence grade B" → "overall 51, evidence grade A".
  - The index directory row for Browser Use: grade B → A (position unchanged; sorted by score).
  - Same handling as 0053.

### Changelog (one row, existing Date / Decision / Change columns)
> 2026-10-17 · 0059 · Browser Use: AgentTell (privacy, Browser Use 0.13.1, Aug 2026), Privacy Practices of Browser Agents (Brave co-authors disclosed) and BreakingWeb (Amazon co-authors disclosed) added as counted sources; 11 counted (3 peer-reviewed). Grade B → A because a recent test now states the library version. Overall score unchanged at 51; recheck note removed. ceLLMate reviewed, not counted.

### Expected public file changes
- public/agents/browser-use.html
- public/changelog.html
- public/index.html
- public/llms.txt
- Plus agents/browser-use.yaml and decisions/0059.

## Queue
- After 0059, the 0052 follow-up list is done, except:
  - the Eye recheck (after 2027-01-01);
  - the AMCIS full text (Gemini);
  - the Julius J2 full text;
  - the recheck notes still on Claude Research, ChatGPT Work, Clay, Kimi Researcher, STORM and Perplexity Comet (from the 0052 sweep), plus the reworded Perplexity, OpenAI and Gemini Deep Research, SAFE and Julius notes.
