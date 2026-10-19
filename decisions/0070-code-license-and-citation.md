# Decision packet 0070 — Code license + CITATION.cff

**Status: APPROVED by Remington, 2026-10-18, D1a–D8a as recommended** (Apache-2.0 for code; unmodified LICENSE + LICENSE-DATA.md + NOTICE + README section; Copyright 2026 TrustKeeperAce; path scope as in §4; name/logo/favicon reserved; CITATION.cff as drafted; license checks; site sentences + changelog row). D9 deploy needs separate approval; D10 Jenqyang PR is for Remington to send.
**Not legal advice.** Choosing a license is a legal decision for the owner. This packet sets out facts, options and trade-offs. If any doubt matters (patents, employer rights, trademarks), ask a lawyer.

Files: `LICENSE` (unmodified Apache-2.0 text from apache.org), `LICENSE-DATA.md` (CC BY 4.0 scope, replacing today's LICENSE text), `NOTICE`, `CITATION.cff`, `README-license-section.md`, `spdx-header-snippet.txt`.

## 1. What happened (facts and sources)
- **Current state (repo, read 2026-10-18 21:15 ET):** one `LICENSE` file at the root. It grants CC BY 4.0 for the data (`agents/*.yaml`, `public/data/`), `decisions/` and the site text (`public/*.html`, `public/agents/*.html`, `public/llms.txt`). It says: "the scripts in scripts/, the stylesheet and the logo/favicon are not licensed under CC BY 4.0 by this file; no license is granted for them here." `public/agents-data.html` and `citing.html` repeat this ("The code (scripts/), the stylesheet and the logo/favicon are not licensed for reuse"). `llms.txt` says "Data and site text: CC BY 4.0". README has no license section. Source: Packet 0061 D3a.
- **Not listed in the current LICENSE:** `data/changelog.yaml`, `docs/`, `README.md`, `LOG.md`, `public/compare/*.html`, the feeds (`updates.json/xml`), `sitemap.xml`, `robots.txt`, `vercel.json`. These are a gap in scope today.
- **File split (git ls-files):** agents 36, decisions 65, public 55, scripts 6 (`build_data.py`, `apply_design.py`, `check_*.py`, `check_all.sh`), data 1, docs 1, plus LICENSE, LOG.md, README.md, vercel.json. The HTML templates live inside `scripts/build_data.py`. The generated pages are the output.
- **GitHub account:** `TrustKeeperAce` is a personal (User) account with no public display name (api.github.com/users/TrustKeeperAce).
- **Awesome-AI-Agents (Jenqyang)** CONTRIBUTING.md (https://github.com/Jenqyang/Awesome-AI-Agents/blob/main/CONTRIBUTING.md, fetched 2026-10-18):
  > "Standard OSS by default: entries should use a clearly open-source license. Source-available, commercial, or mixed-proprietary licensing will usually be rejected."
  > "5. Confirm the repository has a standard open-source license clearly visible in GitHub metadata or the repo itself."
  > "Open-source status and license clarity" (review criterion); "Neutral language (no unverifiable claims like "best"/"first" …)".
  The list includes "Apache-2.0 reputation layer for AI agents" (INAM Protocol), alongside many MIT entries.
- **Creative Commons FAQ** (https://creativecommons.org/faq/, "Can I apply a Creative Commons license to software?"): "We recommend against using Creative Commons licenses for software… CC licenses do not contain specific terms about the distribution of source code… Many software licenses also address patent rights."
- **choosealicense.com:** MIT: "A short and simple permissive license with conditions only requiring preservation of copyright and license notices." (https://choosealicense.com/licenses/mit/). Apache-2.0: "…Contributors provide an express grant of patent rights." (https://choosealicense.com/licenses/apache-2.0/).
- **SPDX identifiers** (https://spdx.org/licenses/): `MIT`, `Apache-2.0`, `BSD-2-Clause`, `MPL-2.0`, `CC-BY-4.0`.
- **CFF 1.2.0** (https://citation-file-format.github.io/, schema at github.com/citation-file-format/citation-file-format): `license` accepts one SPDX id or a list. `type` is `software` or `dataset`. GitHub shows a "Cite this repository" button when `CITATION.cff` is at the root (docs.github.com, "About CITATION files"). The draft passes `cffconvert --validate` ("valid according to schema version 1.2.0") and jsonschema against the official schema.

## 2. What the rules say (project constraints)
- Informational only; no guarantee, endorsement, certification or ranking. Any license needs a warranty disclaimer that matches this; all four options have one.
- Data and text stay CC BY 4.0 (0061). Nothing in this packet changes scores, data or site wording, except the license-scope sentences.
- No account creation and no outbound submissions. The Jenqyang PR remains a draft for Remington to send.
- Deploying the changed page text needs separate approval.

## 3. Options for the code
| | MIT | Apache-2.0 | BSD-2-Clause | MPL-2.0 |
|---|---|---|---|---|
| Length | ~20 lines | ~200 lines | ~25 lines | ~370 lines |
| Patent grant | none explicit | explicit, with termination if the licensee sues | none | explicit |
| Trademark/name | silent | §6: no trademark rights granted | silent | §2.3: no trademark rights |
| Warranty disclaimer | yes ("AS IS") | yes (§7–8) | yes | yes |
| Duties on reusers | keep notice | keep notice + NOTICE file, mark changed files | keep notice | share changes to MPL files (file-level copyleft) |
| Jenqyang fit | yes | yes | yes | yes, but less common |

- **MIT.** Why: simplest and most familiar, and the most common license on the Jenqyang list. Risks: no explicit patent grant (low relevance for a static-site generator), and no explicit trademark clause, so name protection relies on trademark law and the README.
- **Apache-2.0.** Why: the explicit trademark clause fits a project whose name and trust signal matter (forks can't imply they are us), the patent grant is explicit, and its long disclaimer matches the no-guarantee stance. Risks: longer, NOTICE/changed-file duties are a small burden on reusers, and it is incompatible with GPLv2-only code (irrelevant here).
- **BSD-2-Clause:** about the same as MIT. No reason to prefer it.
- **MPL-2.0:** keeps modifications to our files open, but adds copyleft complexity with no clear benefit for a few scripts.
- **Keep no code license (status quo):** blocks the Jenqyang listing and leaves "all rights reserved" on the code.

## 4. How the code license interacts with CC BY 4.0
Proposed rule (in `LICENSE-DATA.md`):
- **Apache-2.0 (or MIT):** `scripts/**` (including the HTML templates inside `build_data.py`), `public/style.css`, `vercel.json`.
- **CC BY 4.0:** `agents/`, `data/`, `public/data/*.json|csv`, the feeds, `llms.txt`, `sitemap.xml`, `robots.txt`, all generated `public/**/*.html`, `decisions/`, `docs/`, `README.md`, `LOG.md`.
- **Generated files:** output takes the license of its content, not of the generator. `public/data/*.json` is data, so CC BY 4.0. This matches the usual position that a tool's license doesn't attach to its output. The generated HTML carries markup structure from the templates, so the draft notes that this structure is also available under the code license, which removes any ambiguity for anyone reusing the layout.
- **Default rule:** anything under `scripts/` or `*.css` is code; everything else is CC BY 4.0 unless a file header says otherwise.
- **Excluded:** the name, logo and favicon (D5), the Google verification token, and third-party sources and trademarks.
- **GitHub detection:** GitHub's license detector (licensee) recognizes a root `LICENSE` containing unmodified license text. Putting Apache-2.0 there gives the "Apache-2.0" badge that Jenqyang's step 5 relies on. The CC BY scope moves to `LICENSE-DATA.md`. Keeping the custom text in `LICENSE` would leave GitHub showing "Other".
- **Pages to update on implementation:** the license sentence on `agents-data.html` and `citing.html`, a line in `llms.txt`, and the README section. Feeds and `agents.json` keep `license: CC BY 4.0`, which stays correct.

## 5. Risks and uncertainties
- **Mixed licensing:** Jenqyang warns against "mixed-proprietary" licensing. Code + CC BY data is open on both sides, but a reviewer might still read it as mixed. Mitigation: a clear README section.
- **Listing still uncertain:** Jenqyang also weighs "real ecosystem value" and maintainability signals. A license is necessary but may not be enough.
- **Copyright holder:** "TrustKeeperAce" is a pseudonymous account. Whether the holder should be Remington's legal name, the account or the project is a legal choice (D3).
- **Irreversibility:** a license granted on published code can't be withdrawn for copies already taken. Relicensing later is possible only for new versions.
- **Scope drift:** new file types may land without a rule. The default rule plus an optional check (D7) addresses this.
- **Name/logo:** Apache §6 does not create trademark rights; it only declines to grant any.
- **Third-party content** in source lists is not ours to license; the draft says so.
- **CFF unknowns:** no DOI, no ORCID, no `date-released` (none invented). Whether `type` is dataset or software is D6.

## 6. Decision items
- **D1 Code license.** a) Apache-2.0 (**recommended**: explicit trademark clause and patent grant, the disclaimer matches the no-guarantee stance, accepted by Jenqyang). b) MIT (simplest, most common). c) BSD-2-Clause. d) MPL-2.0. e) No code license (no listing).
- **D2 File layout.** a) `LICENSE` = unmodified code-license text, `LICENSE-DATA.md` = CC BY scope, and a README section (**recommended**, so GitHub detects it). b) Keep a combined custom `LICENSE` (GitHub shows "Other", which risks Jenqyang step 5). c) `LICENSES/` folder in REUSE style (heavier).
- **D3 Copyright line.** a) "Copyright 2026 TrustKeeperAce" (draft default, matches the repo). b) Remington's legal name. c) "Agent Reputation & Trust Clearinghouse contributors". This is Remington's choice.
- **D4 Path scope.** a) As in §4, including the "markup also under code license" note (**recommended**). b) Make the generated HTML entirely CC BY with no note. c) Code license for all of `public/` except data (blurs the text license).
- **D5 Logo, favicon and name.** a) Reserved, not licensed (**recommended**; protects the trust signal and matches today). b) Logo under CC BY 4.0. c) Logo under the code license.
- **D6 CITATION.cff.** a) Add it as drafted: `type: dataset`, entity author "Agent Reputation & Trust Clearinghouse", `license: [CC-BY-4.0, Apache-2.0]`, no DOI/ORCID/date-released (**recommended**). b) `type: software`. c) Add a personal author (name/ORCID only if Remington supplies them). d) No CFF. Optional sub-items: add `date-released` at release; a Zenodo DOI later (needs an account, so out of scope now).
- **D7 Checks and headers.** a) Add a check that `LICENSE` is the unmodified license text, `LICENSE-DATA.md` exists, `CITATION.cff` validates and the site license sentences match (**recommended**). b) Also add SPDX headers to the 6 scripts and style.css. c) No checks.
- **D8 Site text update + changelog row.** a) Update the license sentences on agents-data.html, citing.html and llms.txt, plus a changelog/feed row (**recommended**). b) Repo-only change; leave the site wording (it would then be inaccurate).
- **D9 Deploy:** needs separate approval. **D10 Jenqyang PR:** drafted for Remington to send himself after D1–D9, not by us.

**Minimal viable version:** D1a + D2a + D3a + D5a + D6a + D8a, with the D7a check. That is 4 new files, LICENSE rewritten, and 3 page sentences changed.

## 7. Plain-English terms
- **License:** permission others need to copy, change or share your work. Without one, the default is "all rights reserved".
- **Permissive license (MIT, Apache, BSD):** anyone can reuse the code, even in closed products, if they keep the notice.
- **Copyleft (MPL):** changed versions of the covered files must stay open.
- **Patent grant:** a promise not to sue users over patents in the contributed code.
- **Trademark clause:** says the license does not let others use your name or logo.
- **Warranty disclaimer:** "as is", with no promise that it works and no liability. This matches our "informational only" stance.
- **SPDX identifier:** the standard short code for a license, e.g. `Apache-2.0`.
- **CITATION.cff:** a small YAML file that tells people (and GitHub's "Cite this repository" button) how to cite the project.
- **DOI / ORCID:** permanent IDs for a work / a person. We have neither and none was invented.
- **NOTICE file:** an Apache-2.0 convention; reusers must keep its attribution text.

*Not legal advice; this is a decision for the owner.*
