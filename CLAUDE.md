# GivingBridge Consulting website

Source of truth for givingbridgeconsulting.com. Originally built in Claude Cowork; all page changes now happen here.

## Deploy
- GitHub `nelvin-gbc/givingbridge-website`, branch `main` → Netlify site `givingbridgeconsulting` (id `916e42ca-d9b7-4472-a208-e4a263f153ac`, team "GivingBridge Consulting + DBA").
- Netlify auto-deploys on every push to `main`. No build step; publish dir is the repo root. There is no `netlify.toml` yet.
- `www.` 301-redirects to the apex domain.
- Pushing to `main` publishes to the live site, so confirm with Nelvin before pushing.
- Local preview: `python3 -m http.server 8765` from the repo root (config in `.claude/launch.json`).

## Structure
- `index.html`: the whole homepage, with inline `<style>` and no build. It uses the "Field Guide" design (Oct 2026 brand refresh): a printed-manual feel with chapters.
  - Sections: `header .masthead` (wordmark, nav, audience line) → `.preface` hero + contents → `#diagnosis` (Ch. 1, symptoms table + reactive/steady diagram) → `#entries` (Ch. 2, three services as "field entries" + donor journey diagram) → `#procedure` (Ch. 3, checklist) → `#author` (Ch. 4, portrait + bio + facts row) → `#contact` (Ch. 5, dark band with booking button, contact list, HubSpot form) → `.colophon` footer.
  - Breakpoints: 1080px and 780px.
- `assets/`: `nelvin.jpg` (headshot, 1000px), `favicon.svg`, `apple-touch-icon.png` (180), `og-image.jpg` (1200×630 link preview).
- `concepts/` is gitignored: local design explorations (four concepts, the brand board, logo source files in `concepts/brand/`). Never deploy it.

## Brand
- Palette (A · Vermilion). Gold and cream were retired; don't reintroduce them.
  `--ink #1B3829` (deep green) · `--ink-deep #0F2219` · `--paper #F3F2EE` · `--paper-2 #E6E8E2` · `--accent #E4572E` (vermilion; text on it uses `--on-accent #0F2219`) · `--soft #CFE0D5` (celadon) · `--text #1D2420` · `--muted #66706A` · `--mid #2D5240`
- Type: IBM Plex Serif (headings and body) + IBM Plex Mono (labels, nav, buttons, small data).
- Logo: a tied-arch bridge (vermilion arch, two posts and a hairline deck in ink), redrawn from the original Cowork mark. Inline SVG in the header; source is `concepts/brand/mark.svg`; the favicon is the same drawing on a rounded green square.
- Avoid the "AI-built" look: no uppercase letter-spaced eyebrow labels, icon-card grids, scroll fade-ins, gradients, vanity stats, or margin side notes.

## Integrations
- Contact form: HubSpot embed (portal `244971559`, form `0434ccc6-e3a0-4eb1-a9cb-2956ae966a48`, region `na2`), rendered into `#hs-contact` and styled through `cssRequired` for the dark band. The account is on paid Starter (Sales + Service), which covers removing HubSpot branding, so `cssRequired` hides the embed's `.hs-form__virality-link`.
- Booking: Google Calendar appointment link `https://calendar.app.google/1Do2GPcDJhYSkQES9`.
- LinkedIn: company page `giving-bridge-consulting`.
