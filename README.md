# Agent Reputation & Trust Clearinghouse

## Purpose
An **informational-only** public directory of digital-task AI agents with transparent, rule-based scores and cited public sources.

- Live site: https://www.agentclearinghouse.org/
- Current entries, scores and grades: the [home page](https://www.agentclearinghouse.org/) and [data/agents.json](https://www.agentclearinghouse.org/data/agents.json) (this README does not repeat counts or scores).

The Clearinghouse does not guarantee, endorse or certify any agent beyond what is explicitly stated in an entry. It handles no payments and is not a party to any transaction between users and agents.

## How this directory works
An overall score is given only when at least three independent performance sources (tests by someone other than the vendor that report their method and results) have tested the product covered by the entry; otherwise the entry is labeled Insufficient evidence. Scored entries show the four factor scores separately next to the overall score, and every entry lists its cited sources. The full data is open under CC BY 4.0. Listing order is not a ranking, and nothing here is an endorsement or certification.

## Scoring rules
Each entry is scored on four factors (completion rate, disputes, adherence to limits, evidence quality), each 0–100 and shown separately, with a weighted overall score and an evidence grade. The rules, weights, grade definitions and counting rules are published in one place: [methodology](https://www.agentclearinghouse.org/methodology.html) (source: `public/methodology.html`). `scripts/check_scores.py` recomputes every score and grade from the entry files.

## Site pages and data
- [Methodology](https://www.agentclearinghouse.org/methodology.html), including [How this directory works](https://www.agentclearinghouse.org/methodology.html#how-it-works)
- Comparison pages: [Claude Code and OpenAI Codex](https://www.agentclearinghouse.org/compare/claude-code-and-openai-codex.html), [coding agents](https://www.agentclearinghouse.org/compare/coding-agents.html), [research agents](https://www.agentclearinghouse.org/compare/research-agents.html)
- [Data and downloads](https://www.agentclearinghouse.org/agents-data.html): [agents.json](https://www.agentclearinghouse.org/data/agents.json), [agents.csv](https://www.agentclearinghouse.org/data/agents.csv), [schema.json](https://www.agentclearinghouse.org/data/schema.json)
- [How to cite](https://www.agentclearinghouse.org/citing.html)
- [Changelog](https://www.agentclearinghouse.org/changelog.html) and update feeds: [JSON Feed](https://www.agentclearinghouse.org/updates.json), [Atom](https://www.agentclearinghouse.org/updates.xml)
- For language models: [llms.txt](https://www.agentclearinghouse.org/llms.txt); [sitemap.xml](https://www.agentclearinghouse.org/sitemap.xml)

## Repository layout
- `agents/` — one YAML file per published entry (the source data). `_schema.example.yaml` is an example only.
- `data/changelog.yaml` — approved changes; source of the changelog page and both feeds.
- `decisions/` — numbered decision records; nothing is published until its packet is approved (see `decisions/README.md`).
- `docs/PROCESS.md` — working process notes.
- `public/` — the static site (plain HTML/CSS, no JavaScript), including generated pages and `public/data/`.
- `scripts/` — build and check scripts (below).
- `vercel.json` — response header for `/updates.xml`.
- `LOG.md` — action log (America/New_York times).

## Build and checks
Run from the repository root with Python 3:
- `python3 scripts/build_data.py` — regenerates `public/data/*`, the sitemap, the changelog table, the feeds, the comparison and citing pages, and other generated page sections from `agents/` and `data/changelog.yaml`.
- `sh scripts/check_all.sh` — runs `check_scores.py` (scores and grades), `check_export.py` (exports, pages, feeds, links and text checks) and a no-JavaScript scan.
- `python3 scripts/check_links.py` — outbound link check (network access needed).

## License
- **Code** (`scripts/`, `public/style.css`, `vercel.json`): [Apache License 2.0](LICENSE). SPDX: `Apache-2.0`.
- **Data and text** (`agents/`, `data/`, `public/data/`, feeds, generated pages, `decisions/`, `docs/`): [CC BY 4.0](LICENSE-DATA.md). SPDX: `CC-BY-4.0`.
- **Not licensed:** the project name, logo and favicon; third-party sources and agent trademarks.
- How to cite: [CITATION.cff](CITATION.cff) and https://www.agentclearinghouse.org/citing.html

Informational only. Provided as is, without warranties; not a guarantee, endorsement, or certification.

## Disclaimer
Informational only. Scores summarize cited public evidence under published rules; they are not a guarantee, endorsement, certification or ranking of quality. The Clearinghouse is not responsible for any agent's outcomes.
