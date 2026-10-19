**Status: APPROVED 2026-10-18 (D1a–D7a; D6a = GitHub About note only, no change made). Commit/push approved; no deploy (README is not a site file).**

# 0073 — README refresh (D6a from 0072)

Proposed text: `0073/README.md`; diff: `0073/README.diff`. Nothing is changed in the repo.

## 1. What happened
The README (README.md, 37 lines, last substantively edited in 0070) still describes the project before any entries were published. Outdated or inaccurate lines:
1. L1 `# Agent Reputation & Trust Clearinghouse — Phase 1` — Phase 1 ended long ago; 34 entries are live.
2. L4 `Phase 1 sets up the structure, rules, and site. **No agent entries are published yet.**` — false.
3. L6 `does not guarantee, endorse, certify, or verify any agent` — the word "verify" is now on the banned list from 0067 (outside the don'ts table); harmless in a negative but best dropped.
4. L8 `## Scoring rules (v0)` — the rules are "Scoring rules v0.1" (methodology.html, check_scores.py, CITATION.cff).
5. L14 Disputes note `Fewer documented disputes/complaints = higher score` — methodology now defines disputes more fully (complaints, legal/regulatory actions, security advisories; pending = allegations). Repeating the table invites drift.
6. L16 evidence-quality note — matches methodology in substance, but is a duplicate.
7. L18 `fewer than 3 independent sources` — the rule counts independent *performance* sources (methodology; 0072 callout). Also omits evidence grades.
8. L20 `Full methodology: public/methodology.html` — no link to the live page.
9. L23 `agents/ — published entries (none yet)` — false.
10. L22–26 layout omits `scripts/`, `data/changelog.yaml`, `docs/PROCESS.md`, `vercel.json`, the generated `public/data/`.
11. Missing entirely: live site URL; compare pages; citing.html; agents-data.html and the JSON/CSV/schema exports; changelog + updates.json / updates.xml; llms.txt; sitemap; how to build (`scripts/build_data.py`) and check (`scripts/check_all.sh`, pre-commit hook).
12. L37 Disclaimer wording differs from the site's fixed disclaimer (FEED_DISCLAIMER) and omits "ranking".
The License section (L28–34, approved in 0070) is current and is kept byte-identical.

## 2. What the rules say
Informational only; no guarantee, endorsement, certification, ranking or "best/top/winner/which is better/stars/certified/verified/endorsed" language (0066/0067 banned list; 0072 adds unlike/only/first/unique for new text). No numbers or dates that go stale unless generated. Prefer pointing to live pages/data over restating rules. The 0072 callout may be reused verbatim. Code Apache-2.0, data/text CC BY 4.0 (0070).

## 3. Proposed wording
Full text in `0073/README.md`. Section status:
- Title — CHANGED: `# Agent Reputation & Trust Clearinghouse`
- Purpose — CHANGED (new first paragraph + live-site/data bullets; "verify" dropped).
- How this directory works — NEW (0072 callout, verbatim, 4 sentences).
- Scoring rules — CHANGED: replaces the table and v0 rule with a one-paragraph pointer to methodology.html and check_scores.py.
- Site pages and data — NEW (links to every public page/file).
- Repository layout — CHANGED (adds scripts/, data/changelog.yaml, docs/PROCESS.md, vercel.json; removes "none yet").
- Build and checks — NEW.
- License — UNCHANGED (byte-identical, checked).
- Disclaimer — CHANGED: first sentence = site FEED_DISCLAIMER verbatim; keeps "not responsible for any agent's outcomes".

Only numbers left outside the License section: "four factors", "0–100", "three" (in the callout) — stable rule constants, already checked against check_scores.py by the 0072 check.

## 4. Verification done (draft)
- Banned-word scan of proposed README (0066/0067/0072 lists, plus Phase 1, No agent entries, guaranteed, #1, rank): 0 hits ("ranking" appears only in negated disclaimer/callout text, as on the site).
- Callout verbatim = build_data.HOW_CALLOUT: yes. Disclaimer = FEED_DISCLAIMER: yes. License section identical to current: yes.
- All 18 live links return 200 (2026-10-18 ~22:59 ET); LICENSE, LICENSE-DATA.md, CITATION.cff exist.
- Claims checked against repo: build_data.py `__main__` runs build, feeds, compare, citing, grade notes, footers, how, index dates; check_all.sh runs check_scores, check_export and the no-JS grep; check_links.py is the outbound link check; vercel.json only sets the /updates.xml header; site has no JavaScript (no-JS scan passes); decisions/README.md says nothing is published until approved.

## 5. Related files that should stay consistent
- `docs/PROCESS.md` L17–18: hook instruction installs only check_scores; the actual local hook also runs check_export. Stale — propose updating (D4).
- `decisions/README.md`: lists 5 sections; current packets use more (D-items, MVP, checks). Minor; optional (D4).
- `CITATION.cff` abstract: accurate; does not mention feeds/llms.txt — fine, no change needed. `version: "Scoring rules v0.1"` matches.
- `llms.txt`, `agents-data.html`: license and links current (0070/0072); no change.
- GitHub repo About (set on GitHub, not changed here): description "Informational-only directory of digital-task AI agents with transparent scores", **no homepage URL, no topics**; license detected Apache-2.0. Suggest (user action, optional): homepage https://agent-trust-clearinghouse.vercel.app/ and topics e.g. ai-agents, agent-evaluation, open-data, dataset.
- Decision-number gaps (0032, 0062–0064, 0068 not in decisions/) are drafts/deferred items; not a README issue.

## 6. Proposed checks (add to check_export.py)
1. README must not contain: "Phase 1", "No agent entries", "(none yet)", "Scoring rules (v0)".
2. README License section byte-equal to an expected constant (as 0070's README check, tightened).
3. README relative links exist in repo; live URLs map to files in public/ (offline check, no network).
4. README contains HOW_CALLOUT verbatim and FEED_DISCLAIMER.
5. Stale-count guard: no digits outside License/code/paths except the allowed rule constants (four, 0–100, three).
6. Banned-word scan applied to README (negated disclaimer phrases allowed as on the site).
Optional: generate the callout/disclaimer/pages list into README from build_data.py between markers.

## 7. Risks
- Drift between README and site → mitigated by checks 1–5 and pointing instead of restating.
- README repeating a callout that later changes → check 4 fails loudly; or generate it (D3b).
- Implied endorsement through "transparent" wording → kept as already-approved site/CITATION wording.
- README is repo-only: commit needs approval; nothing deploys (README is not a site file).

## 8. D-items
- **D1 README text.** a) adopt `0073/README.md` as is (rec.); b) MVP only (title, Purpose, layout fixes); c) keep current.
- **D2 Scoring rules section.** a) pointer paragraph, no table (rec., avoids drift); b) keep the table, synced to methodology wording and v0.1, plus a check.
- **D3 Generated parts.** a) hand-written + checks (rec.); b) build_data.py writes callout/disclaimer/page list between markers; c) no checks.
- **D4 Related docs.** a) also fix docs/PROCESS.md hook line (rec.); b) also update decisions/README.md section list; c) README only.
- **D5 Checks.** a) add checks 1–6 to check_export.py (rec.); b) checks 1–2 only.
- **D6 GitHub About.** a) note only; user may add homepage + topics on GitHub (rec.); b) no change.
- **D7 Changelog row.** a) none — repo-only doc change, not a site change (rec.); b) add a row (feed would become 74 items).
- **D8 Commit/push** needs separate approval. No deploy needed (README is not served).

## 9. Minimum viable version
Replace L1, L4 and L23; change "(v0)" to v0.1 and "independent sources" to "independent performance sources"; add the live-site URL. Add check 1.

## 10. Plain-English terms
- **README:** the front-page text of the GitHub repository.
- **Independent performance source:** a test by someone other than the vendor that reports its method and results.
- **Generated:** written by the build script from the data, so it can't fall out of date.
- **Pre-commit hook:** a local script that runs the checks before each commit and blocks it on errors.
- **Drift:** two places that should say the same thing slowly disagreeing.

## Implementation notes
- README replaced with 0073/README.md; License section byte-identical to the 0070 text (checked).
- docs/PROCESS.md hook line now installs check_scores.py and check_export.py, matching the local hook.
- check_export.py: 6 README checks (0073 block); each tamper-tested to fail, then restored.
- No changelog row (D7a); decisions/README.md untouched.
