// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },
  modules: ['motion-v/nuxt'],
  css: ['~/assets/css/main.css'],
  vite: { plugins: [tailwindcss()] },
  nitro: { prerender: { autoSubfolderIndex: false } },
  routeRules: { '/**': { prerender: true } },
  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
    head: {
      title: 'CloudPilot — Simplify. Automate. Scale Your Business.',
      htmlAttrs: { lang: 'en' },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'CloudPilot helps teams automate workflows, collaborate in real-time, and make data-driven decisions — faster than ever. All in one platform.' },
        { property: 'og:title', content: 'CloudPilot — All-in-One SaaS Platform' },
        { property: 'og:description', content: 'Simplify. Automate. Scale Your Business. All in One Platform.' },
        { property: 'og:type', content: 'website' },
        { property: 'og:image', content: 'https://cloudpilot-saas.pages.dev/og-image.png' },
        { property: 'og:image:width', content: '1200' },
        { property: 'og:image:height', content: '630' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:image', content: 'https://cloudpilot-saas.pages.dev/og-image.png' }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        // Self-hosted Inter (public/fonts/inter-var.woff2) — preloaded so the
        // headline font is requested with the HTML, not after a stylesheet.
        { rel: 'preload', href: '/fonts/inter-var.woff2', as: 'font', type: 'font/woff2', crossorigin: '' }
      ],
      script: [{ type: 'application/ld+json', innerHTML: '{"@context":"https://schema.org","@type":"SoftwareApplication","name":"CloudPilot","applicationCategory":"BusinessApplication","operatingSystem":"Web","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","ratingCount":"12540"}}' }]
    }
  }
})
