# Decision 0043: OpenAI Codex (CLI and cloud agent) — 62 / A

**Status: APPROVED by Remington, 2026-10-17** (D1–D8 approved as recommended). Category: Coding agent. Slug: openai-codex. The entry carries a visible note: "Citation check incomplete — recheck later."
Entry: agents/openai-codex.yaml and public/agents/openai-codex.html.

## Candidate and scope issues
Batch 4 #7, "OpenAI Codex". The name covers three different things:

1. **Codex agent products, April 2025 onward:**
   - Codex CLI: open source, Apache-2.0, GitHub openai/codex, about 130k stars. Latest release rust-v0.163.0 (15 Oct 2026, 17:30 EDT). Includes headless `codex exec`.
   - The IDE extension and the desktop app.
   - The cloud Codex agent in ChatGPT, which opens pull requests.
2. **GPT-Codex models** (GPT-5.x-Codex), which are often run inside other harnesses such as Gemini CLI or OpenHands.
3. **The 2021 Codex model** (HumanEval era; early GitHub Copilot). Deprecated.

**Proposed scope:** item 1 only (D1). Model-only results and items 2–3 are out of scope (0036 caution 2: the named product must be tested). The entry combines CLI and cloud, following the Claude Code precedent, where the CLI, headless mode and pull-request field studies were counted together. Alternative: CLI only. That would drop the 2 pull-request field studies and leave 24 counted (5 peer-reviewed); grade A is unchanged.

## Affiliation checks
- **Developer: OpenAI.** Not counted:
  - OpenAI system cards, launch posts and benchmark claims.
  - OpenAI co-authored benchmarks, e.g. EVMbench (OpenAI, Paradigm, OtterSec).
- **Author blocks:** I scanned the author block and acknowledgements of every screened paper. No counted study has OpenAI-affiliated authors.
- **Funding and in-kind support** (disclosed; still counted per 0040 D4):
  - MT-Sec acknowledges "generous gifts from Google DeepMind and OpenAI".
  - CORE-Bench case study: "compute credit from OpenAI".
  - SkillsBench thanks OpenAI among the model providers.
- **Terminal-Bench 2.0** has an Anthropic co-author (Carlini) and no OpenAI authors. It was excluded for Claude Code only (CAP/Fellou precedent), so it counts for Codex (D4).
- **Other disclosures:**
  - SWE Atlas: Scale AI, which runs commercial leaderboards.
  - Overeager and SNARE: overlapping Griffith/Quantstamp authors.
  - MT-Sec and SecRepoBench share UMD authors (SecRepoBench does not test Codex).

## Proposed score
| Factor | Weight | Score |
|---|---|---|
| Completion | 30% | 60 |
| Disputes | 20% | 55 |
| Adherence | 25% | 45 |
| Evidence | 25% | 85 |

- 18 + 11 + 11.25 + 21.25 = 61.5, which rounds half up to **62, grade A**.
- check_scores on a temporary repo copy: "OK openai-codex: overall 62 (computed 62), grade A, counted 26, peer-reviewed 5".
- **Evidence was scored on the evidence, not to fit the grade.**
  - It is the largest counted set so far (26), with versioned 2026 tests.
  - Peer-reviewed sources are only 5, and most sources are preprints with heavy model dependence.
  - Claude Code had 15 counted and 5 peer-reviewed, also at 85. More preprints do not raise the score above that.
- **Rationale:**
  - **Completion 60.** Codex CLI was first or top on Terminal-Bench 2.0, WideSWE, TEBench, SWE Atlas, SWE-Duel and Timeline-Bench. Its cloud pull requests had the highest acceptance in both field studies. It trailed Claude Code or OpenCode on SWE-RPG, RuBench and ResearchClawBench, and absolute rates on hard tasks stay low. Comparables: Claude Code 50, OpenHands 50.
  - **Disputes 55.**
    - Seven CVEs on the CLI and desktop app (CVSS 4.1–9.8), all with a fix advisory or fix pull requests referenced.
    - OpenAI is the CVE Numbering Authority (CNA) for three of them (the two September 2026 CLI CVEs and the macOS app CVE).
    - No Codex-specific legal or regulatory action.
    - Claude Code was 45, with 35 advisories, a source leak and DMCA takedowns.
  - **Adherence 45.**
    - Out-of-scope actions: 5.4–13.5% (Overeager) and 11.2% (SNARE). Lower than Claude Code, higher than OpenHands.
    - ABTest anomaly rate reached 59.9% with a small model.
    - MT-Sec: correct-and-secure output dropped in multi-turn use.
    - The CVEs include approval and sandbox bypasses.
    - Claude Code was 40.

## Counted (26 independent performance sources)
| # | Source | Peer review | Version / date | Key figures |
|---|---|---|---|---|
| 1 | BountyBench 2505.15216 (Stanford) | NeurIPS 2025 | unstated; 2025 | Codex CLI o3-high: detect 12.5%, patch 90%; o4-mini patch 90% |
| 2 | Terminal-Bench 2.0 2601.11868 | ICLR 2026 | unstated; 2025–26 | Codex CLI + GPT-5.2 63%, highest average |
| 3 | Comparing AI Coding Agents 2602.08915 | MSR 2026 | cloud agent; May–Jul 2025 | Pull-request acceptance 59.6–88.6% by task type (highest of 5); 79.9% in the common window |
| 4 | MT-Sec 2510.13859 (UMD) | EMNLP 2026 (author homepage) | codex-cli 0.39.0; 2025 | C&S 50.1% single-turn → 29.0% multi-turn; overall 36.2%. OpenAI gift disclosed |
| 5 | TerminalWorld 2605.22535 | ASE 2026 extended abstract | unstated (GPT-5.5); 2026 | 48.5% pass (56.1% resolved) |
| 6 | Rise of AI Teammates 2507.15003 (Queen's) | preprint | cloud agent; 2025 | Pull-request acceptance 64% (Devin 49%, Copilot 35%) |
| 7 | SkillsBench 2602.12670 | preprint | unstated (GPT-5.5); 2026 | 66.5% with Skills (OpenHands + GPT-5.5 67.3%). Thanks OpenAI |
| 8 | SWE-RPG 2608.09072 | preprint | unstated; 2026 | 28.5% (Claude Code 32.8%, OpenCode 33.0%) |
| 9 | ResearchClawBench 2606.07591 | preprint | unstated; 2026 | 18.4/100 (Claude Code 21.5) |
| 10 | SWE-bench Science 2608.19799 | preprint | unstated; 2026 | Pass-to-pass 93.28–98.32%; best overall was a Claude Code configuration |
| 11 | Overeager 2605.18583 | preprint | Codex CLI 0.90.0; 2026 | Out-of-scope 5.4–13.5% (Claude Code 11.8–27.7%, OpenHands 0.2–4.5%) |
| 12 | SNARE 2605.28122 | preprint | Codex CLI 0.57.0; 2026 | Overeager 11.2% (Claude Code 19.6%, OpenHands 42.8%) |
| 13 | Tool-surface ablation 2607.10569 (RIT) | preprint | unstated; 2026 | Code-only restriction cut cost 19.9% on SWE-bench |
| 14 | ABTest 2604.03362 | preprint | unstated; 2026 | Anomaly rate 59.9% (GPT-5.1-Codex-Mini) / 28.4% (GPT-4o-mini) |
| 15 | Amazing Agent Race 2604.10261 | preprint | unstated (GPT-5.4); 2026 | About 37%; Claude Code matched with 6× fewer tokens |
| 16 | TEBench 2605.06125 | preprint | unstated; 2026 | Top composite 72.3%; executability 99.2% |
| 17 | SWE Atlas 2605.08366 (Scale AI) | preprint | unstated (GPT-5.4); 2026 | 43.49% pass@1, top |
| 18 | MMTB 2605.10966 | preprint | unstated (GPT-5.2); 2026 | 16.2% |
| 19 | Push Your Agent 2605.23574 | preprint | unstated (gpt-5.4); 2026 | 3 of 9 at 100 artifacts |
| 20 | CORE-Bench case study 2606.26158 (Princeton) | preprint | v0.122 / v0.130.0; 2026 | 92.3–97.4% on corrected CORE-Bench Hard. OpenAI credit disclosed |
| 21 | RuBench 2607.06411 | preprint | 0.142.5 / 0.144.0; Jul 2026 | 66.7% (Claude Code + Opus 4.8 78.7%) |
| 22 | WideSWE 2609.33382 | preprint | v0.147.0; Sep 2026 | 42.50%, best of 7 |
| 23 | Timeline-Bench 2609.35143 | preprint | 0.155.1; Sep 2026 | 26.8% (15/56), best of 16 |
| 24 | SWE-Duel 2610.12569 (SMU) | preprint (under review, ICLR 2027) | 0.62; 2026 | Ranked first; 98.3% defect repair |
| 25 | 1GC-7RC 2605.17046 | preprint | unstated (gpt-5.5); 2026 | Stopped early; used about 50% of its time budget |
| 26 | HarnessSecurity-Bench 2610.07639 | preprint | unstated; 2026 | Protection from security settings varied by mechanism and task |

## Other (not counted)
- **CVEs:**
  - CVE-2025-59532: sandbox writable-root bug; patched in 0.39.0 (GitHub advisory).
  - CVE-2025-55345: symlink file overwrite; CVSS 8.8; JFrog; fix PR #1705.
  - CVE-2025-61260: project configuration runs commands without confirmation; ≤0.23.0; CVSS 9.8; Check Point.
  - CVE-2025-54558: ripgrep auto-approve; before 0.9.0; CVSS 4.1.
  - CVE-2026-19591 and CVE-2026-19592: PowerShell safe-command misparse and Git fsmonitor helper; CVSS 8.8 and 7.3; published by OpenAI; fix PRs #22643 and #22652.
  - CVE-2026-14898: macOS app remote-image exfiltration after prompt injection; CVSS 6.5.
  - Not counted as Codex CVEs: third-party wrappers (AgentAPI, Claude Code UI, CodexBar, @ai-sdk/harness-opencode).
- **Approval Laundering** (working draft, Codex v0.154.0): security analysis.
- **All Smoke, No Alarm:** only 15–18% of Codex test code had strong oracles, the lowest of 5 agents. Descriptive.
- **Investigating Agent Contributions:** descriptive.
- **FSE 2026 bug study** (Claude Code, Codex, Gemini CLI): bug reports.
- **AgentLens (Microsoft):** tests GPT-Codex models, not the product.
- **DeepSWE:** uses Codex CLI as a judge and mentions it; not a clear product test.

## Not counted
- OpenAI vendor material and EVMbench.
- 2021 Codex model studies.
- GPT-Codex models run in other harnesses.
- Aggregator leaderboards.

## Citation gate
- **Semantic Scholar:**
  - Codex queries ran 19:38–19:48 EDT and returned only 429s.
  - Per the workflow, I switched to OpenAlex and noted it: oa_codexcli.json (715, saved in the 0041 batch) and oa_codex_cli2.json (716).
  - I also reused papers already downloaded for the Claude Code, OpenHands, SWE-agent and Aider research.
- **No full 30-minute wait.** With 26 counted, 5 peer-reviewed, and versioned tests in Jul–Sep 2026, Codex is not near any threshold or grade boundary.
- **Batch searches for the next candidates (saved; not screened):**
  - GitHub Copilot coding agent: S2 s2_cx2.json (200 OK), OpenAlex oa_copilot_agent.json (49).
  - Devin: S2 s2_cx3.json (200 OK), OpenAlex oa_devin.json (3,313; noisy).
- **Unscreened or figures not extracted** (→ "Citation check incomplete — recheck later"):
  - BeyondSWE (v0.118.0)
  - PostTrainBench
  - Re-Evaluating EVMBench
  - ProcCtrlBench
  - DeepSWE
  - Act As a Real Researcher
  - The remainder of the OpenAlex Codex sets
- **Files:** /workspace/batch-next/cx/, cx_extract.txt, s2log.txt.

## Reading depth
- Targeted checks only: figures, version, date, authors, acknowledgements. No full reads.
- No single paper could move the grade. The A rests on several versioned 2026 tests.

## Rules applied
- 0036 cautions: vendor not counted; named product must be tested; versions and dates recorded; neutral CVE wording; productivity and field studies can count.
- 0040 D3: pull-request field studies count.
- 0040 D4: in-kind or funding support is disclosed and the source still counts.
- Excluded co-author sources are excluded only for that product.

## Risks
- **CLI vs cloud:** combining them mixes benchmark (CLI) and field (cloud) evidence. CLI-only scope leaves the score and grade essentially unchanged.
- **Funding disclosures:** sources with OpenAI funding or credits (MT-Sec, CORE-Bench, SkillsBench) could be challenged. Removing them leaves 23 counted and 4 peer-reviewed, so A holds.
- **Model dependence:** results depend heavily on very recent models, so the completion score could age quickly.
- **MT-Sec venue** comes from the author's homepage only.

## Decisions requested
- **D1** Scope: Codex agent products from April 2025 (CLI including exec, IDE extension and desktop app, cloud agent). Out of scope: the 2021 Codex model and GPT-Codex models in other harnesses. Alternative: CLI only.
- **D2** Category Coding agent; name "OpenAI Codex (CLI and cloud agent)"; slug openai-codex.
- **D3** Vendor rules:
  - OpenAI-authored and OpenAI co-authored material is not counted (including EVMbench).
  - Funding and credit sources count with disclosure (MT-Sec, CORE-Bench, SkillsBench).
- **D4** Terminal-Bench 2.0 counts for Codex (it was excluded only for Claude Code).
- **D5** CVE wording as drafted. Seven CVEs list fix references. Third-party wrapper CVEs are excluded.
- **D6** Score 60/55/45/85 = 62, grade A.
- **D7** Visible "Citation check incomplete — recheck later" note.
- **D8** Pull-request field studies of the cloud agent count (0040 D3).

## Recommendation
Approve D1–D8 and publish at 62/A with the recheck note.

## Plain-English summary
26 outside studies tested OpenAI's Codex agent. In 2026 it was often at or near the top of coding benchmarks, and its cloud pull requests had the highest acceptance rates in field studies. It still trails competitors on some tasks and scores low on very hard ones. Seven published security flaws in the CLI or desktop app have fixes referenced, and its rate of out-of-scope actions was moderate. Score 62, grade A.

## Draft files (private)
- /workspace/private-drafts/codex.yaml (proposed agents/openai-codex.yaml)
- /workspace/private-drafts/codex-preview/openai-codex.html (overflow check passed at 375 and 1280, light and dark)
- /workspace/private-drafts/build_preview_0043.py
