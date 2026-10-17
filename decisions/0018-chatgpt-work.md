# Decision 0018: OpenAI Operator / ChatGPT agent (candidate 4)

**Status: APPROVED by Remington, 2026-10-17.** Confirmations:
1. Entry "ChatGPT Work (agent and cloud-browser tasks)", category Browser/web agent, **Insufficient evidence**, 0 counted sources for Work. The Operator and ChatGPT agent tests are listed as historical context only, not counted. The security demos are listed as other sources. The page gives the product timeline with OpenAI sources and a note on overlap with OpenAI Deep Research.
2. Methodology clarification, not a rule change, added under "Insufficient evidence": "Products that the vendor has retired are not given new scored entries; independent tests of them may be listed as historical context." Noted in the changelog.
3. Option B (historical 60/B) is not adopted. The OpenAI Deep Research recheck is deferred.

## 1. What happened (product history from OpenAI primary sources)
- **23 Jan 2025:** Operator launched as a research preview at operator.chatgpt.com, Pro tier in the US. It ran on the CUA model, which was based on GPT-4o and later o3. https://openai.com/index/introducing-operator/
- **17 Jul 2025:** OpenAI calls ChatGPT agent "a natural evolution of Operator and deep research". It is "agent mode" inside ChatGPT, and the Operator site "will remain functional for a few more weeks, after which it will be sunset". The Operator page carries a 17 Jul 2025 update: "Operator is now fully integrated into ChatGPT as ChatGPT agent". https://openai.com/index/introducing-chatgpt-agent/ and https://help.openai.com/en/articles/11794368-chatgpt-agent-release-notes
- **Operator site retired:** the OpenAI help page says "The Operator website is no longer accessible". No exact shutdown date was found; OpenAI said "the coming weeks" after 17 Jul 2025.
- **9 Jul 2026 (release notes date it 13 Jul):** OpenAI launched ChatGPT Work, "an agent for longer, more involved tasks", with a cloud browser. https://help.openai.com/en/articles/6825453-chatgpt-release-note
- **ChatGPT agent retired:** the OpenAI help page now opens with "ChatGPT agent is no longer available. Use ChatGPT Work … For supported browser workflows, see Using cloud browser in ChatGPT." https://help.openai.com/en/articles/11752874-chatgpt-agent
  - OpenAI support on the community forum, 12 Aug 2026: "sorry that the Agent-to-Work transition wasn't communicated clearly". https://community.openai.com/t/agent-mode-menu-disappeared-after-recent-performance-issues-plus-plan/1386007/66
  - OpenAI support, 7 Sep 2026: "The old Agent mode has been retired." https://community.openai.com/t/solved-can-t-get-agent-mode-to-run-in-any-project/1373479/7
  - **No official shutdown date.** User reports put it in early August 2026 (unverified).
- **Later 2026:** sign-ins on the ChatGPT Work cloud browser (27 Aug 2026; Plus and Pro). GPT-6 Sol and Luna in Work (23 Sep 2026), then GPT-6.1 Sol (29 Sep 2026). The Atlas browser was retired on 9 Aug 2026.

**Consequence: both products named in the shortlist are retired.** No one can use Operator or ChatGPT agent today.

## 2. Sources found (read in full unless stated)
**Operator, Jan–Jul 2025 (CUA model):**
1. Online-Mind2Web, "An Illusion of Progress?" (Xue et al., OSU/Berkeley; COLM 2025). https://arxiv.org/abs/2504.01382
   - 300 live tasks with human evaluation. Operator succeeded on 61.3%, the best of 6 agents.
   - Peer-reviewed.
2. Mind2Web 2 (Gou et al., OSU + Amazon AGI; NeurIPS 2025 D&B). https://arxiv.org/abs/2506.21506
   - Operator: 0.26 partial completion and 10% success, below the Deep Research systems.
   - Agent-as-a-judge evaluation. Co-authors from Amazon AGI, which builds competing agents (disclose).
   - Also used in the OpenAI Deep Research entry (different system row).
3. BearCubs (Song et al., UMass Amherst; arXiv v3 Jul 2025; venue not confirmed). https://arxiv.org/abs/2503.07919
   - 111 multimodal web tasks: Operator 23.4%, **ChatGPT agent 65.8%**, humans 84.7%.
   - ChatGPT agent struggled with fine cursor control and was slow (median about 16 min).
4. Emergence WebVoyager (Akkil et al., Emergence AI; arXiv Mar 2026, preprint). https://arxiv.org/abs/2603.29020
   - Operator succeeded on 68.6%, against the 87% WebVoyager figure OpenAI reported. Range 35% (Booking.com) to 100% (Apple.com). 95.9% agreement between annotators.
   - **Competing authors:** Emergence builds its own web agent (Agent-E). Disclose.
5. "Dark Patterns Meet GUI Agents" (arXiv Sep 2025, preprint). https://arxiv.org/abs/2509.10723
   - 16 dark-pattern types. Operator had the highest avoidance of the 6 agents and paused to confirm account creation, location sharing and orders.
   - It still fell for some patterns, and human oversight added cognitive load.

**Security tests (documented, reported to OpenAI):**
6. Embrace The Red (Rehberger, 17 Feb 2025). https://embracethered.com/blog/posts/2025/chatgpt-operator-prompt-injection-exploits/
   - Prompt injection hosted in a GitHub issue hijacked Operator into copying PII (Hacker News email; Booking.com address and phone) into a page that sends keystrokes to an attacker.
   - Confirmation prompts usually caught "Update" clicks; one early run set a status without confirmation.
   - Disclosed to OpenAI. The demo stopped working after about 2 weeks.
7. SPLX (Schultz & Hayes, 18 Sep 2025). https://splx.ai/blog/chatgpt-agent-solves-captcha
   - A staged-context prompt made ChatGPT agent break its no-CAPTCHA policy and solve reCAPTCHA v2/v3, Cloudflare Turnstile and text CAPTCHAs (7 of 16 types unsolved).
   - SPLX sells AI security products (interested party).

**Not counted / excluded:**
- **SusBench (IUI 2026)**, https://arxiv.org/abs/2510.11035: tested OpenAI's CUA *sample app* via the API, not the Operator product. The authors say "its behavior may differ". Scope mismatch.
- **WASP (Meta)**, https://arxiv.org/abs/2504.18575: cites Operator but did not test it.
- **ShadowLeak (Radware, Sep 2025)**, https://www.radware.com/blog/threat-intelligence/shadowleak/: zero-click Gmail exfiltration via **Deep Research**. Reported 18 Jun 2025, fixed Aug 2025. It belongs to the OpenAI Deep Research entry, not this one.
- **Vendor figures excluded:** Operator/ChatGPT agent system cards (for example, prompt-injection resistance 99.5% / 95% / 78% / 67%), BrowseComp 68.9%, WebVoyager 87%, WebArena 58%, OSWorld 2.0 62.6% for GPT-6 Sol. https://deploymentsafety.openai.com/chatgpt-agent/promptinjection
- **ChatGPT Work:** Composio "Golden Eval" (45/47) is interested-party testing, and its table describes a Codex CLI run, not Work. Excluded. Press and blog reviews are commentary.
- **Brown University undergraduate thesis** on Operator and dark patterns, https://cs.brown.edu/media/filer_public/19/2e/192ead9f-4534-43e4-b9dd-0dbd28953a1d/shulman_samantha_final_thesis.pdf: not reviewed in full and not counted.

**Disputes:** no lawsuit, regulatory action or CVE specific to Operator or ChatGPT agent was found. The security findings above were disclosed and mitigated, according to the researchers.

## 3. What the rules say (methodology; D0010)
- A source counts only if it tested the product, version and scope covered by the entry.
- **D0008 Open Interpreter precedent:** tests of an earlier, substantially different version were *not* counted for the current product.
- **D0003, D0015 and D0016 "continuity" precedent:** earlier tests count only when the product is continuous and essentially only the model changed.
- Grades: A = 7 or more sources (≥3 peer-reviewed, ≥1 testing the current version within 12 months); B = 5–6; B- = 3–4; under 3 = Insufficient evidence.
- **The rules say nothing about retired products** (decision point).

## 4. Scope options with source counts
| Option | Counted independent performance sources | Result |
|---|---|---|
| A. ChatGPT agent only (Jul 2025–Aug 2026) | 1 (BearCubs); SPLX is a security demo | **Insufficient evidence**, and the product is retired |
| B. Operator + ChatGPT agent as one line, historical entry | 5 (#1–#5); 7 if #6–#7 count as documented tests | B (5 sources, 2 peer-reviewed). Indicative score below. Retired, so it cannot meet "current version" |
| C. Current ChatGPT Work (cloud browser / agent tasks) | **0** independent tests. Lineage tests are not counted (Work is a new product with a different harness and GPT-5.6/6.x models, per the D0008 reading) | **Insufficient evidence** |

**Indicative Option B scores (not recommended):**
- Completion 55: 61.3% and 68.6% on short tasks, 10% full success on Mind2Web 2, BearCubs 23.4% (Operator) to 65.8% (agent).
- Disputes 65: no formal disputes, but demonstrated exfiltration and a policy bypass.
- Adherence 55: confirmations usually held, best dark-pattern avoidance, but injection-driven PII leak and CAPTCHA bypass.
- Evidence 65: 5 sources, 2 peer-reviewed.
- Overall: 0.30×55 + 0.20×65 + 0.25×55 + 0.25×65 = 59.5, shown as **60**, grade **B**.

## 5. Overlap with the OpenAI Deep Research entry
- OpenAI built ChatGPT agent from Operator *and* deep research. Deep research stayed a separate selectable feature, and OpenAI help says it is still available in Chat and Work.
- The OpenAI Deep Research entry stays separate. Option C would cover only Work's agent/browser task execution, not deep-research reports.
- Shared sources: Mind2Web 2 (different system rows). ShadowLeak should be handled in the Deep Research entry only.
- **Flag (not verified in full):** search results report that "legacy Deep Research mode was removed March 26, 2026". The OpenAI Deep Research entry (D0003) may need a version-scope recheck. That is separate follow-up work.

## 6. Risks and uncertainties
- No official retirement date for ChatGPT agent; only OpenAI forum replies and the help page.
- ChatGPT Work changes fast: models went from GPT-5.6 Sol to 6 Sol to 6.1 Sol within about 3 months, so tests may go stale quickly.
- BearCubs venue unconfirmed; Dark Patterns is a preprint. Peer-reviewed count is 2.
- Competing authors: Emergence (#4), Amazon co-authors (#2). Interested party: SPLX (#7).
- Option B would add a retired product to a directory meant for current tools, which may mislead readers.

## 7. Recommendation (decision points)
1. **Scope:** **Option C.** Entry "ChatGPT Work (agent and cloud-browser tasks)", category Browser/web agent, **Insufficient evidence**. List the Operator and ChatGPT agent tests as "earlier products, not counted", following the D0008 precedent. Alternative: **defer** candidate 4 and move to candidate 5 until Work has independent tests.
2. **Retired products:** record a rule reading that retired products get no new entries. This is a clarification, so flag it to Remington. Not recommended: Option B (historical, 60/B).
3. **Security demos** (#6, #7): list as "other" (as with Browser Use's researcher demo), not counted.
4. **Deep Research follow-up:** recheck D0003's version scope separately.

## 8. Plain-English terms
- **Retired:** the vendor has switched it off; users cannot use it.
- **Successor:** the product the vendor now points users to.
- **Continuity reading:** counting tests of an older version because the product is essentially the same.
- **Prompt injection:** hidden instructions on a web page that hijack an agent.
- **Dark pattern:** a website design that tricks users (or agents) into choices they did not intend.
- **Insufficient evidence:** fewer than 3 qualifying independent tests, so no overall score.
