# CloudPilot — All-in-One SaaS Platform

Nuxt 4 (Vue 3.5) + Tailwind CSS v4 + TypeScript, statically prerendered with `nuxt generate`.

Home page is built same-to-same from the CloudPilot reference image: dark hero (black → violet → white), "Simplify. Automate. Scale Your Business. All in One Platform.", About Us, Why CloudPilot?, and the three Featured Tools — FlowMaster, InsightPro, TeamSync — with pastel 3D imagery.

## Stack

- Nuxt 4.6.4, Vue 3.5, Vite, TypeScript
- Tailwind CSS v4.3.5 via `@tailwindcss/vite` (`vite.plugins` in `nuxt.config.ts`, `@import "tailwindcss"` in `app/assets/css/main.css`)
- Static SSG: `nuxt generate` → `.output/public/` (74 prerendered routes, 36 pages)
- Motion: pure CSS + IntersectionObserver, 500ms reveals, stagger 50–200ms, `prefers-reduced-motion` respected

## Pages (36)

Home, Features, Pricing (monthly/yearly toggle), How It Works, About, Contact, Request Demo (validated form), Login (demo: demo@cloudpilot.app / demo1234), Tools + 3 tool pages, Solutions + 3 role pages, Customers + 3 case studies, Integrations, Security, Compare, Changelog, Resources, ROI Calculator (live sliders), Help Center (live search), Careers, Blog + 3 posts, Privacy / Terms / Cookie Policy, Sitemap.

## Develop

```bash
npm install
npm run dev        # http://localhost:3000
npm run generate   # static build to .output/public
```

## Deploy

GitHub Actions (`.github/workflows/deploy-cloudflare-pages.yml`) deploys `.output/public` to Cloudflare Pages project `cloudpilot` (https://cloudpilot.pages.dev). Requires repo secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`, and the Pages project created in Cloudflare.

All copy, prices, stats and testimonials are mock/demo data.
