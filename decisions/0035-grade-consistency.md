# Decision 0035: A-grade "current-version test" consistency (Browser Use)

**Status: APPROVED by Remington, 2026-10-17** (Option 1: Browser Use A → B; score and order unchanged).

## Issue
Both Browser Use and STORM have 7+ counted sources and 3+ peer-reviewed ones, and neither has a recent test that states the library version. STORM was graded B under the 0025 clarification; Browser Use was graded A as a judgment call. `scripts/check_scores.py` (Decision 0033) flagged both.

## Option 2 check (re-reading full texts, 2026-10-17)
Searched the full text of all seven counted Browser Use studies for a stated library version, commit or release:
- Online-Mind2Web (arXiv 2504.01382, COLM 2025): no version.
- Holistic Agent Leaderboard (arXiv 2510.11977, plus the leaderboard page): describes the "Browser-Use" scaffold and cites the repository. Gives versions for other scaffolds (e.g. OpenHands v0.34.0) but none for Browser-Use. The page labels runs by model date only.
- CAP (arXiv 2608.08392, COLM 2026; Nov–Dec 2025): "Browser-Use" with default configuration; repository cited, no version.
- Skim (arXiv 2605.16565, 2026): repository cited "accessed 2026-05-14"; no version.
- VPI-Bench (arXiv 2506.02456, ICLR 2026): documentation cited "accessed 2025-05-15"; no version.
- Patlan et al. (arXiv 2506.17318): repository cited; no version.
- The Hidden Dangers of Browsing AI Agents (arXiv 2505.13076): audits v0.1.44 (fixed in 0.1.45, 2025). This is a version, but an old one, not a recent current-version test.

Result: no explicit version supports the A condition.

## Change (Option 1)
- Browser Use evidence grade: A → B.
- Unchanged: overall score 51, factor scores, sources, counts and directory order.
- The evidence-quality factor score stays 85, slightly above the methodology's guide range for B (70–84). That range is a guide, and differences must be explained. Lowering the factor would change the overall score, which this decision does not do. The explanation is in the evidence-quality note.
- Files changed: `agents/browser-use.yaml` (grade and evidence-quality note), `public/agents/browser-use.html` (grade line and note), `public/index.html` (grade cell), `public/changelog.html` (new row), `public/llms.txt` (grade).
- STORM: no change (stays B).
- Elicit: stays A. Wei et al. tested the Pro tier Dec 2025–May 2026.
