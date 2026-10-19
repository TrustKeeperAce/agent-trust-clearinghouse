# Decision packet 0071 — Evidence pass 1: Manus, ChatGPT Work, Open Interpreter

**Status: APPROVED by Remington, 2026-10-18: D1a, D2a, D3a, D4a as recommended; implementation and changelog row approved. Deploy needs separate approval.**

Implementation notes (2026-10-18): Composio's "45 of 47" was re-checked on the source page and confirmed (results table "Passed 47/47 45/47"; text "passed 45 of 47"). The page labels the OpenAI harness "ChatGPT work" in its setup table but "Codex CLI" in its results table and one paragraph; this is recorded as an uncertainty on the entry. The slug was already chatgpt-work since Decision 0018 and no other slug was ever published, so no redirect was needed.
Data: agents/manus.yaml, agents/chatgpt-work.yaml, agents/open-interpreter.yaml. All three stay Insufficient (counted 0 / 2 / 0).
Note: the "ChatGPT agent" entry is now **ChatGPT Work** (slug `chatgpt-work`, Decision 0018). ChatGPT agent and Operator are retired and listed only as historical context.

**Outcome in one line:** no entry reaches 3 counted independent performance sources. All three stay **Insufficient evidence**, with no scores and no grade. The changes are new sources, updated notes and counts, and `last_reviewed` 2026-10-18.

## 1. What happened (facts and sources; web searches run 2026-10-18, about 21:43–21:46 ET)
### Manus (current product: Manus 2.0, 28 Sep 2026, "a new architecture")
- No independent test of Manus 2.0 was found. The coverage found says so explicitly:
  - New Runtime: "no independent benchmark is supplied" (https://newruntime.com/analysis/manus-s-efficiency-gains-are-a-harness-result-not-an-agent-verdict/).
  - On The Wire: "Independent reaction is thin" (https://onthewire.ai/article/manus-2-0-launches-with-cascade-harness-manus-studio-and-cue-an-app-for-personal).
  - AIReport.NET: "Independent verification is still pending".
- Vendor claim, not used: Cascade had "23.2% fewer tokens… 28.2% less time… 32% less" cost "in one tested configuration" (https://manus.im/blog/introducing-manus-2-0).
- Salt Labs (already listed): the press release is dated 1 Oct 2026 and says "The research was conducted earlier this year", so before 2.0. The flaw was fixed through Meta's bug bounty (https://salt.security/press-releases/salt-labs-research-a-single-email-could-hijack-an-ai-agent-and-reach-a-users-connected-accounts). Implicator dates the disclosure 24 Sep (https://www.implicator.ai/manus-cue-agents-phone-numbers-wallets/). The current note says "October 2026"; the draft clarifies the date.
- Cue agents (own email, phone number, wallet; invite-only) are not independently tested.
- No lawsuit and no new regulatory action were found beyond what the entry already records.

### ChatGPT Work (launched 9 Jul 2026)
- **AI Agents Library**, "I Tested ChatGPT Work on 10 Real Business Tasks" (https://www.aiagentslibrary.com/blog/chatgpt-work-review/):
  - Tested 25 Aug–3 Sep 2026 on ChatGPT Plus (GPT-5.6 Sol where recorded).
  - Stated method: 5 criteria scored 0–2 each, one attempt per task. Mean 9.15/10.
  - Failures: the webpage was built but not published; one accuracy error (inferred follow-ups listed as agreed).
  - Disclosed: "Self-funded and not sponsored". 2 of the 10 tasks used the author's own Skills, and the site sells training.
- **Composio Golden Eval**, 20 Jul 2026 (https://composio.dev/content/chatgpt-work-vs-claude-cowork):
  - "47 scenarios and 94 trials: one run per scenario"; ChatGPT Work with GPT-5.6 Sol passed 45 of 47 (confirmed on the page at implementation).
  - All tasks ran through Composio's own MCP product. Composio is an integration vendor, not an agent competitor.
- **Simon Willison**, "Understanding ChatGPT Work", 30 Aug 2026 (https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/):
  - Hands-on documentation of the Work Cloud tools: code execution with internet access, a full browser, a persistent workspace, subagents.
  - Concludes it "combines all three" lethal-trifecta conditions. No attack is demonstrated, and it is not a performance test.
- **Assistant Benchmark** lists ChatGPT Work as "0 of 15 dimensions tested" (https://assistantbenchmark.com/agents/chatgpt-work).
- No peer-reviewed or preprint evaluation of ChatGPT Work was found. OpenAI's system-card prompt-injection evaluations are vendor-produced and model-level, so not used.

### Open Interpreter (current product: Rust fork of OpenAI Codex; first `rust-v` release 20 Jun 2026)
- **GuardFall** (Adversa AI, 30 Jun 2026; https://adversa.ai/blog/opensource-ai-coding-agents-shell-injection-vulnerability/; CSA note at https://labs.cloudsecurityalliance.org/research/csa-research-note-guardfall-ai-coding-agent-shell-injection/):
  - Surveyed 11 agents "as of May 2026", including `OpenInterpreter/open-interpreter`: "no static guard (default)".
  - Its mention of the optional `safe_mode` (Semgrep), a Python-version feature, and the May date show it tested the **earlier Python version**. Outside scope, so not counted.
- **MrTechKing repository scan** of the Rust product (commit b171530, 27 Sep 2026; https://www.mrtechking.com/open-interpreter-github/):
  - "Nothing malicious"; the installer and updater pipe a remote script to the shell; 101 dependency advisories, none critical.
  - A code scan, not a test of the agent's behaviour, so recorded as other.
- Terminal-Bench 2.1 figures for the Rust product are published by the maintainer, so not used.
- No independent benchmark, study or CVE for the Rust product was found.

## 2. What the rules say (Scoring rules v0.1, unchanged)
- An overall score needs at least 3 **independent performance sources**: tests that report method and results, including documented hands-on tests and security evaluations.
- Reviews, commentary, press coverage without original testing and vulnerability listings are **other** sources; they do not count toward the 3.
- A source counts only if it tested the **product, version and scope** covered by the entry. Each study counts once.
- Independent means not from the vendor, a customer's staff, or a competing product promoting itself. Partial independence is labeled.
- Grades: B- needs 3–4 sources, B needs 5–6, A needs 7+ (3 peer-reviewed, 1 current and recent). Below 3 means Insufficient evidence, with no grade and no score.

## 3. Proposed changes (before → after)
| | Manus | ChatGPT Work | Open Interpreter |
|---|---|---|---|
| Status / grade | Insufficient → Insufficient | Insufficient → Insufficient | Insufficient → Insufficient |
| Scores | null → null | null → null | null → null |
| Counted performance | 0 → 0 | 0 → **2** | 0 → 0 |
| Other sources | 3 → 4 (+New Runtime) | 2 → 3 (+Willison) | 7 → 8 (+repo scan) |
| Listed, not counted | +0 | — | +GuardFall (Python version) |
| Text | Salt Labs date clarified; 2 uncertainties added | summary, completion and evidence notes updated; 2 uncertainties added | count note; adherence note gains the GuardFall finding; 1 uncertainty added |
| last_reviewed | 2026-10-17 → 2026-10-18 | 2026-10-17 → 2026-10-18 | 2026-10-16 → 2026-10-18 |

New public summary sentence for ChatGPT Work: "Independent tests exist for Operator and ChatGPT agent but are not counted. Two independent tests of ChatGPT Work were found (a hands-on review and an integration vendor's benchmark), fewer than the three required, so no overall score is given."

## 4. What is missing
- **Manus:** any independent test of Manus 2.0 (benchmark, study or security test after 28 Sep 2026). Three are needed.
- **ChatGPT Work:** one more independent performance source, ideally a study, benchmark or security evaluation with a stated model and date.
- **Open Interpreter:** any independent evaluation of the Rust product. All behavioural evidence concerns the Python version.

## 5. Risks and uncertainties
- **ChatGPT Work counting** is the main judgment call:
  - Composio is an integration vendor and the tasks ran through its product, so the source carries a "partial independence" label.
  - AI Agents Library is a single-author, single-run review that used the author's own Skills in 2 of 10 tasks and promotes its own training.
  - Both used GPT-5.6 Sol; the product has since moved to GPT-6.x. The entry scope is the product, not the model, but results may not transfer.
- **Second-hand figure (resolved):** the Composio "45 of 47" was confirmed on the page at implementation; see the implementation notes above.
- **GuardFall version:** the Python version is inferred from the date and the `safe_mode` reference; the post does not state a version or commit.
- **Fast change:** all three products changed within the last 4 months, so evidence will go stale quickly.
- **Search coverage:** searches used a web index only. Semantic Scholar/OpenAlex checks were not rerun (as in 0052), so recent preprints may be missed.
- **Rule boundary:** neither "review" nor "documented hands-on test" is precisely defined; the AI Agents Library page sits on that line.

## 6. Decision items
- **D1 Manus.**
  - a) Keep Insufficient. Add the New Runtime commentary, clarify the Salt Labs date, add 2 uncertainties, set last_reviewed 2026-10-18 (**recommended**).
  - b) No change.
  - c) Also add the vendor's Cascade figures as an explicitly "not used" vendor source.
- **D2 ChatGPT Work.**
  - a) Keep Insufficient, with **2 counted** (AI Agents Library; Composio labeled partially independent). Update summary and notes, add Willison as other (**recommended**; both report method and results, and neither is the vendor or a competing agent).
  - b) Count only AI Agents Library (1); record Composio as other, because the test promotes the author's own product.
  - c) Like a), but re-fetch Composio to confirm "45 of 47" before approval.
  - d) No change.
- **D3 Open Interpreter.**
  - a) Keep Insufficient. List GuardFall as Python-version, outside scope and not counted; record the repo scan as other; extend the adherence note; set last_reviewed 2026-10-18 (**recommended**).
  - b) Count the repo scan as an "audit" performance source (still Insufficient; we advise against, since it doesn't test behaviour).
  - c) No change.
- **D4 Recheck cadence:** a) Recheck all three in the 15 Nov monthly review (**recommended**; ChatGPT Work is 1 source from B-). b) Recheck only on correction requests.
- **D5 Publishing:** implementing the changes, adding a changelog row (62 rows, 72 feed items) and deploying each need separate approval.

## 7. Plain-English terms
- **Insufficient evidence:** fewer than 3 qualifying independent tests, so no score and no grade.
- **Independent performance source:** a test by someone other than the maker that says how it tested and what it found.
- **Counted:** the source tested the current product, not an older or retired version.
- **Other source:** useful background (commentary, scans, documentation) that does not count toward the 3.
- **Historical context:** tests of earlier versions or retired products, shown for reference only.
- **Partial independence:** not the maker, but with a stake, for example a test run through the tester's own product.
- **Prompt injection:** hidden instructions in content the agent reads that make it do something the user didn't ask for.

*Informational only; not a guarantee, endorsement, or certification.*
