# TraceSurgery public-site deployment

This directory is a static microsite. No backend, analytics, external JavaScript, or external fonts are required.

## GitHub Pages
1. Put the contents of this directory in the repository root or `docs/`.
2. Enable Pages in repository settings.
3. If using the included workflow, keep `.github/workflows/deploy-pages.yml`.
4. After the final URL exists, add the canonical URL to `index.html`, `robots.txt`, and `sitemap.xml`. Do not invent a canonical URL before deployment.

## Netlify
Drag-and-drop this directory, or deploy it as the publish directory. `netlify.toml` contains security/cache headers.

## Vercel
Import the repository as a static site. `vercel.json` contains headers and clean routing.

## Post-deploy checks
- Open `/`, `/TraceSurgery_v1.0.1_paper.pdf`, and `/assets/tracesurgery-demo.mp4`.
- Check mobile and desktop layout.
- Run link checks.
- Add the real canonical URL only after deployment.
- Re-run social-card preview after the canonical URL is known.

## Evidence boundary
The site must continue to distinguish local deterministic validation from external frontier-model evidence. Do not replace `pending` labels with performance claims until the external study passes the repository evidence gate.
