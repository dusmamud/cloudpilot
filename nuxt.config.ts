// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from '@tailwindcss/vite'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },
  css: ['~/assets/css/main.css'],
  vite: { plugins: [tailwindcss()] },
  nitro: { prerender: { autoSubfolderIndex: false } },
  routeRules: { '/**': { prerender: true } },
  app: {
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
        { name: 'twitter:card', content: 'summary_large_image' }
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap' }
      ],
      script: [{ type: 'application/ld+json', innerHTML: '{"@context":"https://schema.org","@type":"SoftwareApplication","name":"CloudPilot","applicationCategory":"BusinessApplication","operatingSystem":"Web","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","ratingCount":"12540"}}' }]
    }
  }
})
