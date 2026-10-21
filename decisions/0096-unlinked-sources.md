# Decision 0096: three listed sources linked on their entry pages; check that every source is linked

**Status: APPROVED by Remington, 2026-10-21 (5:00 PM ET, t254u), as recommended:**
- **D1 (a):** add the 3 missing links to the "Not counted" lists of the two entry pages, in the same format and order as the data.
- **D2 (a):** new process check: every source in agents.json is linked on its entry page.
- **D3 (a):** one site_change changelog row and its feed item.
- **D4 (a):** last-reviewed dates unchanged.
- **D5 (a):** llms-full.txt / llms.txt wording unchanged.
- **D6 (a):** page-only links and the chatgpt-work homepage slug are noted below for a later packet.

Commit, push and deploy each need separate approval.

## What happened
- **The gap.** Decision 0095 found that 3 of the 826 sources in data/agents.json were not linked on their entry pages. All three are listed but not counted:

  | Entry | URL | Kind | What it is |
  |---|---|---|---|
  | mini-swe-agent | https://www.swebench.com/ | not counted (affiliated leaderboard) | SWE-bench leaderboards |
  | mini-swe-agent | https://hal.cs.princeton.edu/ | not counted (leaderboard) | Holistic Agent Leaderboard |
  | replit-agent | https://arxiv.org/abs/2605.04637 | competitor | SWE-WebDevBench |

  All three URLs resolved (HTTP 200) on 21 Oct 2026.
- **Cause: an omission in the build template, not a data error.** Entry pages are static HTML, written once by a per-entry build script. That script places sources under page headings by the part of the kind before " (", using fixed lists. Any other kind was silently left out:
  - the 0085 (mini-SWE-agent) script had no list for "not counted";
  - the 0089 (Replit Agent) script had no "competitor" (the 0094 script includes it).
- **The data is correct and linking is right.** Each source is properly listed but not counted:
  - the SWE-bench leaderboards under 0031 and 0036 cautions 1 and 4;
  - HAL under 0036 caution 3;
  - SWE-WebDevBench under the 0083 competitor rule.

  Both pages already mention them in their text, and the SWE-agent page links both leaderboards the same way.

## What changes
- **public/agents/mini-swe-agent.html:** two items are added to "Not counted", after pull request #794 and before CodeClash.
- **public/agents/replit-agent.html:** one item is added first in "Not counted", before ViBench.
- **Format:** each item is rendered from agents/*.yaml exactly as the build scripts render sources: `<li><a href="URL">note</a> — accessed DATE</li>`, HTML-escaped. Nothing else on either page changes.
- **scripts/check_export.py:** new check "0096". Every source URL in agents.json must appear as a link on its entry page, and a missing one is an error. This is a process rule, not a scoring rule.
- **Changelog row and feed item** 2026-10-21-0096 (site_change, no per-agent changes).
- **Not changed:**
  - scores, grades, counts, last-reviewed dates;
  - agents.json, agents.csv and the YAML files;
  - the sitemap, llms.txt and llms-full.txt;
  - the other 41 entry pages.

  Last reviewed stays as it is because the methodology says link fixes do not change it.

## Noted for a later packet (D6)
Links on entry pages that are not sources in agents.json (recording them would change listed-source counts):
- **In older "Excluded sources" or "Not counted" lists (11):**
  - gemini-deep-research: arXiv 2507.16075, 2602.11685;
  - consensus: doi 10.5206/cjils-rcsib.v49i1.23075;
  - claude-research: arXiv 2508.15804, 2510.14240, 2601.08536, 2604.03173;
  - browser-use: arXiv 2508.16688, github.com/browser-use/benchmark, the digitalapplied.com blog;
  - chatgpt-work: arXiv 2510.11035.
- **In the text of entry pages (11):**
  - agent-s: NVD CVE-2026-84886 and CVE-2026-84887;
  - data-interpreter: NVD CVE-2026-0760, CVE-2026-0761 and CVE-2026-19059;
  - skyvern: commit db856cd;
  - chatgpt-work: the OpenAI community forum post and the Operator announcement;
  - kimi-researcher: the sedaily and sina.cn reports;
  - manus: the Manus Max release post.
- **chatgpt-work homepage slug:** the homepage is `https://help.openai.com/en/articles/6825453-chatgpt-release-note`, but the Wayback Machine has a copy only of `…-chatgpt-release-notes`. Both return 403 to automated requests, so this is not verified.
