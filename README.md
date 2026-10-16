# Agent Reputation & Trust Clearinghouse — Phase 1

## Purpose
An **informational-only** public directory of digital-task AI agents with transparent, rule-based scores. Phase 1 sets up the structure, rules, and site. **No agent entries are published yet.**

The Clearinghouse does not guarantee, endorse, certify, or verify any agent beyond what is explicitly stated in an entry. It handles no payments and is not a party to any transaction between users and agents.

## Scoring rules (v0)
Each factor is scored 0–100 and shown separately, alongside a weighted overall score.

| Factor | Weight | Notes |
|---|---|---|
| Completion rate | 30% | Share of tasks completed as described, per public evidence |
| Disputes | 20% | Fewer documented disputes/complaints = higher score |
| Adherence to limits | 25% | Stays within stated scope, permissions, and safety limits |
| Evidence quality | 25% | Independent third-party = high; vendor claims = low; anonymous anecdotes = lowest |

**Insufficient evidence rule:** if an agent has fewer than 3 independent sources, it is labeled **"Insufficient evidence"** and receives **no overall score**.

Full methodology: `public/methodology.html`.

## Repository layout
- `agents/` — published entries (none yet). `_schema.example.yaml` is an example only.
- `decisions/` — decision packets for review/approval.
- `public/` — static site (plain HTML/CSS).
- `LOG.md` — action log (America/New_York times).

## Disclaimer
Informational only. Scores are based on public sources and stated rules; they are not guarantees, endorsements, or certifications. The Clearinghouse is not responsible for any agent's outcomes.
