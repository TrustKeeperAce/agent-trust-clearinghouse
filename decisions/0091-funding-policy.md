# Decision packet 0091: Funding and conflict-of-interest policy + GitHub Sponsors donation link (review only)

**Status: APPROVED by Remington, 2026-10-20 (7:36 PM ET): D1(a), D2(a), D3(a) with the $500 individual naming threshold, D4(a) (the 'no ties' sentence kept as drafted), D5(a), D6(a) with SPONSORS_LIVE OFF for this release (the not-yet-open wording) and the footer 'Funding' link on every page, D7(a) (no-perk tiers, documented only), D8(a) (FUNDING.yml later, not in this change), D9, D10 (one changelog row 2026-10-20-0091 as drafted), D11 (publishing order). 'Donations only' confirmed. **Commit AND push APPROVED by Remington, 2026-10-20 (8:15 PM ET), with wording fixes W1 (consistent apostrophes), W2 (heading 'Changes.') and W4 (plainer closing line); W3 skipped ('quarterly donation totals' kept). Deploy NOT approved; SPONSORS_LIVE stays off.** Drafting approved 2026-10-20 at 7:06 PM ET; final private patch built on a scratch clone only (see 'Final private draft' below).

**Outcome in one line:** one new section on the existing methodology page ("Funding and conflicts of interest"), a one-line change to the privacy promise, a "Funding" link in the shared footer, a donation link that stays off until the Sponsors profile exists, and one changelog row. **No score, grade, source count, entry or scoring-rule changes.** agents.json, agents.csv, schema.json, sitemap.xml, llms.txt and llms-full.txt come out byte-identical.

## What happened (facts + sources)
- **Starting point:** the private deep dive (private working notes) and the earlier private draft 0063 (monetization readiness). 0063 says: "whoever pays should never also be the party being rated"; disclose donors who are listed vendors; payment tools need their own packet.
- **What the site promises today** (public/methodology.html):
  - Privacy: "This site does not use cookies, advertising, or cross-site tracking, and it does not sell or share visitor data. It contains no tracking scripts."
  - Corrections: "Entries are not removed, added or re-scored for payment, and we do not accept payment for any listing or change."
  - How it works (generated): "Entries are not removed, added or re-scored for payment."
  - Every page has the same footer, generated from the index footer by `build_footers()` and checked by check_export ("footers differ").
- **Vercel Hobby:** "Hobby teams are restricted to non-commercial personal use only", and "**Asking for Donations does not fall under commercial usage.**" (https://vercel.com/docs/limits/fair-use-guidelines, checked 2026-10-20). A plain donation link keeps the site on the free plan. Selling anything (tiers with goods, ads, sponsors) would not.
- **GitHub account:** the public API shows TrustKeeperAce is a personal account (`type: User`) created 2026-10-16 with 1 public repo. https://github.com/sponsors/TrustKeeperAce currently redirects (302) to the plain profile, so **no Sponsors profile exists yet**.
- **GitHub Sponsors facts (all checked 2026-10-20):**
  - **Fees:** "does not charge any fees for sponsorships from personal accounts, so 100% … go to the sponsored developer". Organizations pay "up to 6%" (3% card plus 3% GitHub). https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/about-github-sponsors-for-open-source-contributors
  - **Eligibility:** "Anyone who contributes to an open source project and lives in a supported region". The United States is on the list. Documentation counts as a contribution. https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors
  - **Setup needs:** contact info; payouts by bank account (through Stripe Connect) or a fiscal host (which can **only be chosen at sign-up**); a tax form; **2FA turned on**; then "Request approval". "It may take a few days for GitHub to review your application." Your region and your bank's region must match. https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/setting-up-github-sponsors-for-your-personal-account
  - **Tax:** US taxpayers must submit a **W-9 before publishing** the profile. "GitHub does not withhold tax." GitHub's page says it sends a 1099-NEC to US taxpayers who earn more than $600 in a year; the IRS threshold may have changed since, so check with a tax professional. "Sponsorships are generally not tax deductible." https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/tax-information-for-github-sponsors
  - **Payout timing:** the first payout comes "60 days after the first sponsorship is initiated" (a probation period), then monthly through Stripe Connect. ACH/wire payouts have a $100 minimum balance. https://docs.github.com/en/site-policy/github-terms/github-sponsors-additional-terms (§3.3)
  - **Terms:** you must register "with your true identity". Tier rewards are optional. The Additional Terms say the "primary focus … should not be advertising" (§2.3.3). Same URL.
  - **Visibility:** each sponsor chooses "who can see your sponsorship". https://docs.github.com/en/sponsors/sponsoring-open-source-contributors/sponsoring-an-open-source-contributor
  - **Blocking:** when you block a user, "their sponsorship of you is canceled" and they cannot sponsor you. https://docs.github.com/articles/blocking-a-user-from-your-personal-account. **Not verified:** whether a personal account can block an *organization* account the same way.

## What the rules say
- **Hard rules:** scores can never be bought; no guarantees, endorsements, certifications or ratings markup; no payments or escrow without approval; companies being scored must not be able to influence scores.
- **Pages:** no automated page creation, and any new page needs its own approval.
- **Changelog:** a change to entry pages or the site is paired with a changelog row. Precedents 0069 and 0090 used one site-level row with `changes: []`.
- **Banned words:** the standard BANNED_CITE list from 0066, 0067 and 0072, plus the 0090 extended list.
- **Deploys:** done only by the owner. Commit, push and deploy each need separate approval (PROCESS.md).

## Risks and uncertainties
- **New account:** the GitHub account is 4 days old, and GitHub reviews applications. It might ask for more information or take longer than "a few days". Not verified.
- **Organizations can sponsor:** a listed company's GitHub org could sponsor. The policy says cancel and return; blocking works for users, but for organizations it isn't verified. Refunds are the maintainer's job (GitHub Additional Terms §3.6), and a refund path through Stripe isn't verified. That is why the policy says "return it where we can" and requires a changelog note.
- **The policy is strict:** "a company that makes an AI agent in one of the directory's categories" excludes most large AI companies, including Microsoft, which owns GitHub. That makes **GitHub-funded programs** (for example GitHub's own pooled funds) excluded money too. This is intended; flagged so Remington knows.
- **"Donations only" is a promise:** a later newsletter or site sponsor would need a new approved decision that changes this section. That is fine and stated in the policy, but the change would be public.
- **The conflict-of-interest sentence is Remington's own statement:** "As of 20 October 2026, the maintainer reports no such ties." Only Remington can confirm it (see D4).
- **Expected money is small:** realistically $0–$20/month for months (deep dive, estimate). This packet is about trust readiness, not income.
- **Personal information:** GitHub requires your true identity, and Stripe holds bank and tax details. What sponsors see on the profile is whatever Remington writes. The policy never names him.

## Decisions (D-items)
- **D1 Where the policy lives:** **APPROVED: (a).**
  - (a) A new section `#funding` on the existing methodology page, placed just before "Privacy and measurement". It is generated from build_data constants (the 0072 how-it-works pattern) and checked word for word. **Recommended:** lowest change and no new page.
  - (b) A new page /funding.html. Needs a separate page-creation approval, plus a title, sitemap entry, llms.txt line and checks. Not recommended now.
  - (c) README only. Not visible to site readers. Not recommended.
- **D2 Donations from companies whose products are listed:** **APPROVED: (a).**
  - (a) **Refuse.** No donations from listed companies, companies making agents in the directory's categories, their parents or subsidiaries, or anyone giving on their behalf. Any that arrive are cancelled, returned where possible, and noted in the changelog. Employees may give personally and get nothing in return. **Recommended.** It matches "whoever pays should never also be the party being scored" (0063).
  - (b) Accept with public disclosure. Easier to run, but readers could fairly suspect influence. Not recommended.
  - (c) Refuse only listed companies, and accept other AI-agent makers with disclosure. A middle option; harder to explain.
- **D3 Disclosure thresholds:** **APPROVED: (a), $500 threshold.**
  - (a) Quarterly changelog row with the number of donations and the total (only when there were any). Every organization donor is named. Individuals over $500 in a calendar year are named, or the amount above $500 is returned if they don't want to be named. **Recommended.**
  - (b) Yearly totals only. Simpler, but less transparent.
  - (c) Name every donor. Raises privacy concerns for small personal gifts. Not recommended.
  - Remington's call: the $500 figure is a judgment. Lower it to $250 for stricter rules, or raise it to $1,000 for fewer refunds.
- **D4 Conflict-of-interest statement:** **APPROVED: (a), sentence kept as drafted.** keep the sentence "As of 20 October 2026, the maintainer reports no such ties" **only if Remington confirms it is true**. Paying for a listed product as an ordinary customer (for example a coding-agent subscription) is not treated as a tie; say so if that applies.
  - (a) Confirm and keep. **Recommended, if true.**
  - (b) Drop the sentence. The rule still applies.
  - (c) List specific ties. If there are any, that needs its own short review.
- **D5 Edit to the "no advertising" promise:** **APPROVED: (a).**
  - (a) Change it to: "This site does not use cookies, advertising, sponsored placements, or cross-site tracking, and it does not sell or share visitor data. It contains no tracking scripts. Links to other sites are plain links; once you follow one, that site's own privacy terms apply." Also add "See Funding and conflicts of interest." to the existing Corrections bullet about payment. **Recommended:** it stays true with a donation link (a plain link to GitHub is neither advertising nor tracking) and makes "no sponsored placements" explicit.
  - (b) No edit. Still technically true, but it doesn't mention the new outbound payment link.
- **D6 Donation link: placement, wording, timing:** **APPROVED: (a), SPONSORS_LIVE off for this release; footer Funding link on every page.**
  - (a) Put the link **only inside the methodology #funding section**, as "To donate: Support the Clearinghouse on GitHub Sponsors." It is followed by: "GitHub and its payment processor, Stripe, handle payments, and GitHub’s own privacy statement and terms apply there. The Clearinghouse is not a registered charity, so donations are generally not tax-deductible." The shared footer gets "Funding", which links to the policy rather than the payment page. It sits between "How to cite" and "Privacy". The link is controlled by a `SPONSORS_LIVE` switch. Until the profile is approved and live, the section shows: "Donations are not open yet. When they open, a link will appear here and the change will be listed in the changelog." A check fails the build if a Sponsors link appears while the switch is off, or anywhere other than methodology.html while it is on. **Recommended.**
  - (b) Footer link labelled "Support" that goes straight to GitHub Sponsors. More visible, but puts a payment link on every entry page next to scores.
  - (c) Policy only, and decide on donations later.
- **D7 GitHub Sponsors tiers and rewards:** **APPROVED: (a), documented only (set up by Remington on GitHub).**
  - (a) No rewards beyond a thank-you. Suggested tiers: monthly $3, $5 and $10, and one-time $5 and $25, all described as "General support. No perks; donations never affect scores." No names, logos or links on the site. **Recommended:** keeps it a donation (Vercel) and matches "no perks".
  - (b) Names on a supporters list. Not recommended now, because it drifts toward advertising.
- **D8 Repository Sponsor button (.github/FUNDING.yml with `github: TrustKeeperAce`):** **APPROVED: (a), later; not in this change.**
  - (a) Later, as its own small change after the profile is live. **Recommended.**
  - (b) Never.
- **D9 Checks:** **APPROVED.** add the check_export rules that were dry-run:
  - the section is word for word;
  - the privacy sentence is present;
  - the Corrections link is present;
  - the footer link is present;
  - the Sponsors link appears only when live and only on methodology;
  - the banned-word scan covers the section.

  **Recommended.** Each check fails as intended on a deliberately broken copy.
- **D10 Changelog row:** **APPROVED (row 2026-10-20-0091 as drafted).** one site-level row, `2026-10-20-0091` (date set when published), with `changes: []`. **Recommended.** Drafted text, in the not-live variant:
  > Added a Funding and conflicts of interest section to the methodology: money never affects scores, grades, inclusion, review timing, order or wording; no donations from companies whose products are listed or that make AI agents in the directory's categories; no paid listings, advertising or affiliate links for listed agents; quarterly donation totals. Donations are not open yet. The privacy section now also says the site has no sponsored placements, and every page footer links to the new section. No score, grade or source count changes.

  When the link goes live later, a second short row ("Donations can now be made through GitHub Sponsors") goes with flipping the switch.
- **D11 Publishing order:** **APPROVED (order); commit and push APPROVED 2026-10-20 8:15 PM ET (with W1, W2, W4; W3 skipped); deploy NOT approved.** each step needs separate approval.
  1. Implement on master.
  2. Commit and push.
  3. Deploy the **not-live** variant (policy first).
  4. Remington sets up GitHub Sponsors himself (steps below).
  5. Once github.com/sponsors/TrustKeeperAce shows the Sponsors page, a follow-up commit and deploy turn on `SPONSORS_LIVE` with its changelog row.

  This packet would also be added as decisions/0091-funding-policy.md, with a LOG.md line. **Recommended.** Alternative: publish both together after the profile is live, which means one deploy but a delay.

## Policy text (final, as committed; wording fixes W1, W2 and W4 applied)
**Funding and conflicts of interest**

The Clearinghouse is run by one person and is free to use. Money never affects scores, factor scores, evidence grades, which entries are included or reviewed, when they are reviewed, listing order, or entry wording.
- **Donations only.** The only money we accept is voluntary donations. A donation is not payment for anything: donors get no early access, no preview of reviews, no say in what is reviewed or when, and no listing, badge, logo or link on this site.
- **Not from listed companies.** We do not accept donations from a company whose product is listed here, from a company that makes an AI agent in one of the directory’s categories, from their parent or subsidiary companies, or from anyone giving on their behalf. If such a donation arrives, we cancel it, return it where we can, and note it in the changelog. People who work at these companies may give personally; their donations are treated like any other and come with nothing in return.
- **No paid placements.** We do not sell listings, profile pages, featured spots, badges, advertising or sponsored placements, and we do not use affiliate links for listed agents. Corrections are free and follow the same published rules for everyone, including the makers of listed products.
- **Disclosure.** If any donations are received in a quarter, we publish the number of donations and the total in the changelog. Any organization that donates is named. An individual who gives more than $500 in a calendar year is named; if they prefer not to be named, we return the amount above $500.
- **Conflicts of interest.** If the maintainer has a financial or personal tie to a listed product or its maker (for example employment, paid work, shares, or a close family member who works there), it is disclosed on that entry and in its decision record. Paying for a product as an ordinary customer is not treated as a tie. As of 20 October 2026, the maintainer reports no such ties. *(Needs D4 confirmation.)*
- **Concerns.** If you believe money or a conflict has affected an entry, email trustkeeperace@gmail.com. Concerns are reviewed under the same rules as correction requests, and any change is listed in the changelog.
- **Changes.** This policy changes only through an approved decision, listed in the changelog.

*Until the profile is live:* Donations are not open yet. When they open, a link will appear here and the change will be listed in the changelog.
*Once live:* To donate: **Support the Clearinghouse on GitHub Sponsors** (https://github.com/sponsors/TrustKeeperAce). GitHub and its payment processor, Stripe, handle payments, and GitHub’s own privacy statement and terms apply there. The Clearinghouse is not a registered charity, so donations are generally not tax-deductible.

Informational only. Funding does not change the scores, which are rule-based summaries of public evidence, not a guarantee, endorsement, or certification.

## What Remington must do himself (do not start until D-items are approved; nothing here was done for him)
1. **Turn on 2FA:** GitHub → profile picture → Settings → Password and authentication → Enable two-factor authentication.
2. Go to **https://github.com/sponsors** → **Get sponsored** → choose the personal account TrustKeeperAce → fill in contact info.
3. **Payout method:** choose **bank account** (Stripe Connect). A fiscal host can only be chosen at this step. Check that your name and date of birth are exact, because they are hard to change later.
4. Read the GitHub Sponsors Additional Terms and Privacy Statement → **Submit**.
5. **Profile:** Your sponsors → Dashboard → Profile details. Suggested short bio: "Maintainer of the Agent Trust Clearinghouse, an informational directory of AI agents with rule-based scores." Suggested introduction: "Donations support the time spent reviewing public evidence. Donations never affect scores, grades, inclusion or wording, and come with no perks. Companies whose products are listed, or that make AI agents in the directory's categories, cannot donate. Policy: https://www.agentclearinghouse.org/methodology.html#funding". The policy link works only after the policy is deployed.
6. **Tiers (D7):** monthly $3, $5 and $10, and one-time $5 and $25. Description: "General support. No perks; donations never affect scores." Do **not** add a private repo, early access or a logo reward.
7. Dashboard → **Stripe Connect account**: add bank details. Dashboard → Overview → **tax forms**: complete the **W-9**.
8. Dashboard → **Request approval**. GitHub says review "may take a few days".
9. When https://github.com/sponsors/TrustKeeperAce shows the Sponsors page, tell the bot. It then prepares the switch-on (D11 step 5).
10. **After a payment arrives from a listed company or AI-agent maker:** do not keep it. Block the account if it's a user (this cancels the sponsorship), ask about a refund, and note it in the changelog.

**Informational notes, not advice:**
- Sponsorship income is generally taxable, and GitHub does not withhold tax.
- GitHub may issue a 1099-NEC.
- Keep a simple log of money received.
- Ask a tax professional how this applies to you.

## Dry-run results (both variants)
- **Base:** committed master **ee3af9a**. Rebuilding base without changes gives no drift.
- **Files changed (55 including 1 new placeholder):**
  - scripts/build_data.py, scripts/check_export.py, data/changelog.yaml, public/methodology.html
  - the shared footer on every other page (50 HTML pages compared: changelog and methodology changed outside the footer; all others changed in the footer only, checks/entry-pages-footer-only.txt)
  - public/changelog.html, updates.json, updates.xml (one new feed item)
  - new: decisions/0091-funding-policy.md (placeholder)
- **check_all:** 0 errors in both variants (40 entries; titles max 68; no-JS ok).
- **check_scores:** 0 errors, 0 warnings, 6 documented. Same as base.
- **Score diff: zero.** agents.json, agents.csv, schema.json, sitemap.xml, llms.txt and llms-full.txt are byte-identical to base.
- **New checks:** each fails as intended when tested against a broken copy: a Sponsors link while not live, a missing footer link, and a banned word in the section.
- **Banned-word scan:** no new banned wording. The only net-new hits are "guarantee" inside the standard negated disclaimer.
- **Link check** (live variant, 7:18 PM ET): 734 outbound links: 651 OK, 76 bot-blocked, 7 failures. Six of the failures are the same pre-existing ones reported in 0090 (two DOIs timing out, two Fellou 503s, os-world.github.io, one Wayback timeout). The seventh is the new decisions/0091 GitHub link, which exists only after a push. The GitHub Sponsors URL returns OK, but only as a redirect to the plain profile until the profile is approved. All 58 internal links are OK, including /methodology.html#funding.

## Final private draft (approved set; scratch clone of 938b266 = origin/master after the 0090 deploy LOG commit)
Patch, check outputs and manifest preview were kept as private working notes.
- **Files changed: 55** (54 modified + 1 new):
  - data/changelog.yaml, scripts/build_data.py, scripts/check_export.py
  - public/methodology.html (new #funding section, privacy sentence, Corrections link), public/changelog.html, updates.json, updates.xml
  - shared footer only: index, 404, agents-data, citing, 3 compare pages, 40 entry pages
  - new: decisions/0091-funding-policy.md
- **check_all:** 0 errors (40 entries, 40 CSV rows; 0075 titles: 49, max 68; no-JS ok). **check_scores:** 0 errors, 0 warnings, 6 documented (same as base).
- **Score diff: none.** All fields of all 40 agents.json entries are identical. agents.json, agents.csv, schema.json, sitemap.xml, llms.txt and llms-full.txt are byte-identical to 938b266.
- **Totals:** 40 entries (29 scored / 11 insufficient), changelog rows 75 → 76, feed items 89 → 90 (JSON and Atom).
- **D9 checks:** pass on the patched build. Each fails as intended on a broken copy: Sponsors link while off, footer link missing, banned word in section, privacy sentence reverted, Corrections link missing.
- **Banned-word scan:** no new banned wording. The only net-new hits are "guarantee" in the standard negated disclaimer.
- **Link check** (7:45 PM ET): 733 outbound links: 648 OK, 79 bot-blocked, 6 failures. These are the same 6 known failures as in 0090: two DOIs timing out, two Fellou 503s, os-world.github.io and one Wayback timeout. The new decisions/0091 GitHub link was rate-limited in this run; an earlier run got 404, because the file exists only after a push. All 58 internal links are OK.
- **Manifest preview** against the live site (dpl_8cyfG6LZGPdhGDY8hUYbq2fFPZL2, plain HTTPS reads, no Vercel calls):
  - All 62 base files match live byte for byte.
  - The patched build would upload 51 files (49 HTML pages for the footer, plus updates.json and updates.xml); 11 are unchanged.
  - With the deploy vercel.json, that is 63 deployment files.

## Minimum viable version
D1(a) + D2(a) + D5(a) + D10 in the **not-live** variant, without the footer link if you want only one page touched. Removing the footer link drops the change from 55 files to about 8 (methodology, two scripts, changelog yaml/html, two feeds, decision record). The donation link waits until the profile exists.

## Plain-English terms
- **GitHub Sponsors:** GitHub's donation feature. Money is handled by Stripe, a payment company.
- **2FA:** a second login step, such as a code from a phone app.
- **W-9:** a US tax form that gives your taxpayer number to the payer.
- **1099-NEC:** a US form reporting money paid to you.
- **Fiscal host:** an organization that receives money on a project's behalf.
- **Switch (`SPONSORS_LIVE`):** one setting that decides whether the donation link appears.
- **Dry run:** trying the change on a throwaway copy.
- **Patch preview:** the exact line-by-line changes that would be applied.

---
Informational only; not a guarantee, endorsement, or certification. Scores are based on public sources and the stated rules at the time of review.
