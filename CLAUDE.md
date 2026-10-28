# GivingBridge Consulting website

Source of truth for givingbridgeconsulting.com. Originally built in Claude Cowork; all page changes now happen here.

## Deploy
- GitHub `nelvin-gbc/givingbridge-website`, branch `main` → Netlify site `givingbridgeconsulting` (id `916e42ca-d9b7-4472-a208-e4a263f153ac`, team "GivingBridge Consulting + DBA").
- Netlify auto-deploys on every push to `main`. No build step; publish dir is the repo root. `netlify.toml` hides repo files (CLAUDE.md, README.md, .gitignore, netlify.toml) with a 404 and sets security and cache headers. `404.html` is the branded not-found page.
- `www.` 301-redirects to the apex domain.
- Pushing to `main` publishes to the live site. Nelvin has approved pushing as part of each change (2026-10-25), so no confirmation is needed: commit, push, wait for the Netlify deploy to show `ready`, then spot-check the live pages.
- Local preview: `python3 -m http.server 8765` from the repo root (config in `.claude/launch.json`).

## Structure
- `index.html`: the homepage. All pages, the homepage included, share `assets/site.css` (no inline style blocks, except the HubSpot `cssRequired` on the homepage). No build step. It uses the "Field Guide" design (Oct 2026 brand refresh): a printed-manual feel with chapters.
  - Sections: `header .masthead` (wordmark, nav, audience line) → `.preface` hero + contents → `#diagnosis` (Ch. 1, symptoms table + reactive/steady diagram) → `#entries` (Ch. 2, three services as "field entries": 2.1 `#donor-strategy` (custom project or Sprint, with donor journey diagram), 2.2 `#ai-fundraising` (AI Sprint or workshop), 2.3 `#associate-boards`) → `#procedure` (Ch. 3, checklist) → `#author` (Ch. 4, portrait + bio + facts row) → `#faq` (Ch. 5, nine FAQs, mirrored in JSON-LD and llms.txt) → `#contact` (Ch. 6, dark band with booking button, contact list, HubSpot form) → `.colophon` footer.
  - Breakpoints: 1080px and 780px.
- **Cache busting:** every page, the homepage included, links `/assets/site.css?v=…`, and browsers cache it for an hour. Whenever `site.css` changes, bump the `?v=` value in every subpage, or visitors keep the old styles.
- Other pages:
  - `health-check/`: $79 Fundraising Health Check offer. The buy button is a Stripe Payment Link (not created yet: the button is temporarily email-first, with a prefilled mailto and an optional call link, and the Stripe version is kept in an HTML comment beside it; step 1 of "How it works" also needs updating at swap time). Nelvin wants this offer email-forward, with calls always optional, because calls add friction; Stripe redirects to `health-check/questionnaire/?session_id={CHECKOUT_SESSION_ID}`.
  - `health-check/questionnaire/`: Netlify Form `health-check` (needs form detection enabled in Netlify), posts to `health-check/thanks/`. Stores `stripe_session_id`. noindex.
  - `sprint/`: $1,200 / 3-week Donor Strategy Sprint. CTA is a scoping call; invoiced after.
  - `ai-sprint/`: $1,800 / 3-week AI Fundraising Sprint (workflow audit, prompt library in their voice, AI policy covering donor data, team training). Email-first CTA.
  - `ai-workshop/`: $1,000 / 90-minute AI for Fundraisers workshop (live, virtual; also pitched to associations and AFP chapters). Email-first CTA.
  - `resources/`: detailed, branded write-ups of Tovera (tovera.org) and The Nonprofit AI Brief (nonprofitaibrief.org). Credit line is Nelvin's name; public figures only; those sites do not link back. Not on the homepage; it lives only on /resources/, which the nav links to through a Resources dropdown.
- `assets/`: `nelvin.jpg` (headshot, 1000px), `favicon.svg`, `apple-touch-icon.png` (180), `og-image.jpg` (1200×630 link preview), `site.css`, `resources/` (screenshots and logo crops of Tovera and the Brief).
- `concepts/` is gitignored: local design explorations (four concepts, the brand board, logo source files in `concepts/brand/`). Never deploy it.

## Brand
- Palette (A · Vermilion). Gold and cream were retired; don't reintroduce them.
  `--ink #1B3829` (deep green) · `--ink-deep #0F2219` · `--paper #FFFFFF` · `--paper-2 #EDF2EE` · `--accent #E4572E` (vermilion; text on it uses `--on-accent #0F2219`) · `--soft #CFE0D5` (celadon) · `--text #1D2420` · `--muted #66706A` · `--mid #2D5240`
- Type: IBM Plex Serif (headings and body) + IBM Plex Mono (labels, nav, buttons, small data).
- Logo: the original GivingBridge "g" mark (hand-lettered g in a petal burst), used single-color, deep green in the header and white on green for the favicon, next to the IBM Plex Serif "GivingBridge" wordmark. Files: `assets/logo-g.svg` (green), `assets/logo-g-white.svg`, `assets/favicon.svg`, `assets/apple-touch-icon.png`, all converted from the vector PDFs in `~/Documents/Claude/Projects/GivingBridge Consulting/package_print_mhmi0api (1)/black/`. Don't use the original multicolor or yellow versions on the site.
- Avoid the "AI-built" look: no uppercase letter-spaced eyebrow labels, icon-card grids, scroll fade-ins, gradients, vanity stats, or margin side notes.

## Integrations
- Contact form: HubSpot embed (portal `244971559`, form `0434ccc6-e3a0-4eb1-a9cb-2956ae966a48`, region `na2`), rendered into `#hs-contact` and styled through `cssRequired` for the dark band. The account is on paid Starter (Sales + Service), which covers removing HubSpot branding, so `cssRequired` hides the embed's `.hs-form__virality-link`.
- Booking: Google Calendar appointment link `https://calendar.app.google/1Do2GPcDJhYSkQES9`.
- LinkedIn: company page `giving-bridge-consulting`.

## Offer lineup (as of 2026-10-27)
- Services: Donor Strategy, AI for Fundraising, Associate Board Development. Fixed price: Health Check $79 (five areas, including AI readiness), Donor Strategy Sprint $1,200, AI Fundraising Sprint $1,800, AI workshop $1,000.
- Fractional Development was removed because Nelvin doesn't have the capacity. A FAQ answer says it isn't offered right now; don't reintroduce it without asking.
- The paid AI offers are the done-with-you version of the free Nonprofit AI Playbook (nonprofitaibrief.org/playbook). Don't position them as another toolkit.
- Nelvin prefers email-first CTAs with an optional call (calls add friction).
- Guarantees (approved 2026-10-27): Health Check: if the report doesn't tell them something new, the $79 is refunded. Both sprints: if the Week 2 drafts aren't on track, the full fee is refunded and the client keeps what was delivered. Credit: the $79 counts toward either sprint if booked within 60 days. The workshop has no guarantee (not yet decided). These appear in price cards (`.guarantee`), the FAQs, the homepage pricing FAQ, llms.txt, and the follow-up emails.

## Search, AI visibility and security
- `robots.txt` allows all crawlers, including AI ones (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, …), and blocks the questionnaire, thanks and `_internal` pages. `sitemap.xml` lists the 4 public pages (update `lastmod` when pages change). `llms.txt` is a plain-language summary for AI assistants; keep services, prices and facts in sync with the pages.
- **Regenerate with `python3 scripts/build_seo.py`** after changing services, prices, pages or FAQ text: it rewrites every page's JSON-LD and `sitemap.xml`. New public pages must be added to its `PAGES` map. `llms.txt` is maintained by hand.
- Every public page has JSON-LD (`@graph`): Organization/ProfessionalService, Person (Nelvin), Service + Offer (with prices), WebSite entries for Tovera and the Brief, FAQPage (generated from the visible `<details>` FAQs; regenerate if the FAQ text changes), and BreadcrumbList on subpages. Only state facts that are visible on the site.
- `netlify.toml` sets a CSP allowing only self, Google Fonts and the HubSpot form (js-na2.hsforms.net, forms-na2.hsforms.com), plus HSTS, X-Frame-Options DENY, Permissions-Policy, COOP and nosniff. **If you add a third-party script, embed or font, add its domain to the CSP** or it will be blocked. Test CSP changes with a draft deploy (`netlify deploy --dir .`) before pushing.
- `/.well-known/security.txt` lists the security contact (expires 2027-10-25; renew it).
- No database or user accounts, so database row-level security (RLS) doesn't apply to this site.

## Copy and design conventions (from the 2026-10-27 buyer and designer review)
- Section labels: the hero is "Preface", then "Ch. 1, 2…", and the dark closing band is the last chapter ("Getting in touch"). "Entry 2.x" appears only inside homepage Ch. 2; "Step n" is used for procedures.
- No eyebrow or kicker labels above headlines, no "New" badges, no dagger footnotes.
- Primary call to action = vermilion `.btn-accent`; secondary = green `.btn` or a quiet link. The HubSpot submit button is an outline so it doesn't compete with the main button.
- Visible brand name is "GivingBridge"; "Giving Bridge Consulting LLC" appears only in the legal footer and in schema `legalName`.
- Avoid AI-sounding copy: balanced "X, not Y" contrasts, "Nothing vague", "No jargon, no hype", "actually".
- QA checklist before pushing UI changes: check hover and focus states (hover the dropdown items, not just open the menu), 375px and 1280px widths, and every page that shares the changed CSS. Avoid one-letter class names (`.q` is the questionnaire row; reusing it once broke the nav).
- Line length: body text is capped at about 36em (roughly 70 characters) via `.ch-body p, li, dd`. Do not let paragraphs run the full sheet width.
