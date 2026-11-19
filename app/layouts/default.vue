<template>
  <div class="min-h-screen bg-white text-neutral-900">
    <header class="sticky top-0 z-50 bg-black text-white transition-shadow" :class="scrolled ? 'shadow-lg shadow-black/40' : ''">
      <!-- Scroll progress -->
      <Motion :style="{ scaleX: progress }" class="h-0.5 origin-left bg-gradient-to-r from-violet-500 via-fuchsia-500 to-violet-400" aria-hidden="true" />
      <div class="mx-auto flex h-16 max-w-7xl items-center justify-between gap-2 px-4 sm:h-[72px] sm:px-6">
        <NuxtLink to="/" class="flex min-h-11 shrink-0 items-center gap-2.5" aria-label="CloudPilot home">
          <LogoMark class="h-10 w-10 shrink-0" />
          <span class="whitespace-nowrap text-lg font-bold tracking-tight">CloudPilot</span>
        </NuxtLink>
        <nav class="hidden items-center gap-1 lg:flex" aria-label="Primary">
          <div class="relative" @mouseenter="open = 'product'" @mouseleave="open = ''">
            <button class="flex min-h-11 items-center gap-1.5 rounded-full px-4 text-sm font-medium transition hover:bg-white/10" :aria-expanded="open === 'product'" aria-haspopup="true" @click="open = 'product'">
              Product <ChevronDown class="h-4 w-4 transition-transform duration-200" :class="open === 'product' ? 'rotate-180' : ''" />
            </button>
            <AnimatePresence>
              <Motion v-if="open === 'product'" :initial="{ opacity: 0, y: 8 }" :animate="{ opacity: 1, y: 0 }" :exit="{ opacity: 0, y: 8 }" :transition="{ duration: 0.18, ease: 'easeOut' }" class="absolute left-0 top-full w-72 rounded-2xl bg-white p-2 text-neutral-900 shadow-2xl ring-1 ring-black/5">
                <NuxtLink to="/features" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Features</span><span class="block text-sm text-neutral-500">Everything in one platform</span></NuxtLink>
                <NuxtLink to="/tools" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Tools</span><span class="block text-sm text-neutral-500">FlowMaster, InsightPro, TeamSync</span></NuxtLink>
                <NuxtLink to="/product-tour" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Product tour</span><span class="block text-sm text-neutral-500">Click through it, no account needed</span></NuxtLink>
                <NuxtLink to="/templates" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Templates</span><span class="block text-sm text-neutral-500">Ready-made workflows and boards</span></NuxtLink>
                <NuxtLink to="/developers" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Developers</span><span class="block text-sm text-neutral-500">API, webhooks and SDKs</span></NuxtLink>
                <NuxtLink to="/integrations" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Integrations</span><span class="block text-sm text-neutral-500">100+ tools, one click</span></NuxtLink>
                <NuxtLink to="/security" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Security</span><span class="block text-sm text-neutral-500">SOC 2, GDPR, SSO</span></NuxtLink>
              </Motion>
            </AnimatePresence>
          </div>
          <div class="relative" @mouseenter="open = 'solutions'" @mouseleave="open = ''">
            <button class="flex min-h-11 items-center gap-1.5 rounded-full px-4 text-sm font-medium transition hover:bg-white/10" :aria-expanded="open === 'solutions'" aria-haspopup="true" @click="open = 'solutions'">
              Solutions <ChevronDown class="h-4 w-4 transition-transform duration-200" :class="open === 'solutions' ? 'rotate-180' : ''" />
            </button>
            <AnimatePresence>
              <Motion v-if="open === 'solutions'" :initial="{ opacity: 0, y: 8 }" :animate="{ opacity: 1, y: 0 }" :exit="{ opacity: 0, y: 8 }" :transition="{ duration: 0.18, ease: 'easeOut' }" class="absolute left-0 top-full w-72 rounded-2xl bg-white p-2 text-neutral-900 shadow-2xl ring-1 ring-black/5">
                <NuxtLink to="/solutions" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">All solutions</span><span class="block text-sm text-neutral-500">By team and company size</span></NuxtLink>
                <NuxtLink to="/use-cases" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Use cases</span><span class="block text-sm text-neutral-500">Projects, marketing, sales</span></NuxtLink>
                <NuxtLink to="/solutions/startups" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">For Startups</span><span class="block text-sm text-neutral-500">Ship fast, stay lean</span></NuxtLink>
                <NuxtLink to="/solutions/teams" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">For Teams</span><span class="block text-sm text-neutral-500">Collaborate in real-time</span></NuxtLink>
                <NuxtLink to="/solutions/enterprise" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">For Enterprise</span><span class="block text-sm text-neutral-500">Scale with control</span></NuxtLink>
              </Motion>
            </AnimatePresence>
          </div>
          <NuxtLink to="/pricing" class="flex min-h-11 items-center rounded-full px-4 text-sm font-medium transition hover:bg-white/10">Pricing</NuxtLink>
          <div class="relative" @mouseenter="open = 'resources'" @mouseleave="open = ''">
            <button class="flex min-h-11 items-center gap-1.5 rounded-full px-4 text-sm font-medium transition hover:bg-white/10" :aria-expanded="open === 'resources'" aria-haspopup="true" @click="open = 'resources'">
              Resources <ChevronDown class="h-4 w-4 transition-transform duration-200" :class="open === 'resources' ? 'rotate-180' : ''" />
            </button>
            <AnimatePresence>
              <Motion v-if="open === 'resources'" :initial="{ opacity: 0, y: 8 }" :animate="{ opacity: 1, y: 0 }" :exit="{ opacity: 0, y: 8 }" :transition="{ duration: 0.18, ease: 'easeOut' }" class="absolute left-0 top-full w-72 rounded-2xl bg-white p-2 text-neutral-900 shadow-2xl ring-1 ring-black/5">
                <NuxtLink to="/blog" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Blog</span><span class="block text-sm text-neutral-500">Guides and product news</span></NuxtLink>
                <NuxtLink to="/customers" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Customers</span><span class="block text-sm text-neutral-500">Case studies that shipped</span></NuxtLink>
                <NuxtLink to="/help" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Help Center</span><span class="block text-sm text-neutral-500">Answers in minutes</span></NuxtLink>
                <NuxtLink to="/changelog" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Changelog</span><span class="block text-sm text-neutral-500">What is new in CloudPilot</span></NuxtLink>
                <NuxtLink to="/faq" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">FAQ</span><span class="block text-sm text-neutral-500">Questions, answered</span></NuxtLink>
                <NuxtLink to="/trust-center" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Trust Center</span><span class="block text-sm text-neutral-500">Compliance, uptime, subprocessors</span></NuxtLink>
                <NuxtLink to="/status" class="block rounded-xl px-4 py-3 transition hover:bg-violet-50"><span class="block font-semibold">Status</span><span class="block text-sm text-neutral-500">Live service health</span></NuxtLink>
              </Motion>
            </AnimatePresence>
          </div>
          <NuxtLink to="/about" class="flex min-h-11 items-center rounded-full px-4 text-sm font-medium transition hover:bg-white/10">Company</NuxtLink>
        </nav>
        <div class="flex items-center gap-2">
          <LazyCommandPalette ref="palette" show-button />
          <NuxtLink to="/login" class="hidden min-h-11 items-center rounded-full px-4 text-sm font-medium transition hover:bg-white/10 sm:flex">Sign in</NuxtLink>
          <NuxtLink to="/signup" class="btn btn-outline-light btn-sm max-[400px]:hidden">Get Started</NuxtLink>
          <button class="grid h-11 w-11 shrink-0 place-items-center rounded-full bg-white text-black transition hover:bg-violet-100 lg:hidden" :aria-expanded="mobile" aria-controls="mobile-menu" aria-label="Toggle menu" @click="mobile = !mobile">
            <component :is="mobile ? X : Menu" class="h-5 w-5" />
          </button>
        </div>
      </div>
      <AnimatePresence>
        <Motion v-if="mobile" id="mobile-menu" :initial="{ height: 0, opacity: 0 }" :animate="{ height: 'auto', opacity: 1 }" :exit="{ height: 0, opacity: 0 }" :transition="{ duration: 0.25, ease: 'easeInOut' }" class="overflow-hidden border-t border-white/10 lg:hidden">
          <nav class="grid gap-1 px-4 pb-6 pt-3 text-sm font-medium" aria-label="Mobile">
            <NuxtLink to="/features" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Features</NuxtLink>
            <NuxtLink to="/tools" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Tools</NuxtLink>
            <NuxtLink to="/solutions" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Solutions</NuxtLink>
            <NuxtLink to="/pricing" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Pricing</NuxtLink>
            <NuxtLink to="/blog" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Blog</NuxtLink>
            <NuxtLink to="/customers" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Customers</NuxtLink>
            <NuxtLink to="/about" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Company</NuxtLink>
            <NuxtLink to="/help" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Help Center</NuxtLink>
            <NuxtLink to="/product-tour" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Product tour</NuxtLink>
            <NuxtLink to="/faq" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">FAQ</NuxtLink>
            <button class="flex min-h-12 w-full items-center gap-2 rounded-xl px-3 text-left transition hover:bg-white/10" @click="mobile = false; palette?.openPalette()"><Search class="h-4 w-4" /> Search pages <kbd class="ml-auto rounded-md bg-white/10 px-1.5 py-0.5 text-[11px] font-bold">⌘K</kbd></button>
            <NuxtLink to="/login" class="flex min-h-12 items-center rounded-xl px-3 transition hover:bg-white/10" @click="mobile = false">Sign in</NuxtLink>
            <NuxtLink to="/signup" class="btn btn-violet mt-2 w-full" @click="mobile = false">Get Started <ArrowRight class="h-4 w-4" /></NuxtLink>
          </nav>
        </Motion>
      </AnimatePresence>
    </header>
    <main><slot /></main>
    <footer class="bg-black text-white">
      <div class="mx-auto grid max-w-7xl gap-10 px-4 py-14 sm:grid-cols-2 sm:px-6 lg:grid-cols-5">
        <div class="lg:col-span-2">
          <div class="flex items-center gap-2.5"><LogoMark class="h-10 w-10" /><span class="text-lg font-bold">CloudPilot</span></div>
          <p class="mt-4 max-w-sm text-sm leading-relaxed text-neutral-400">Simplify. Automate. Scale your business — all in one platform. Built for modern teams that move fast.</p>
          <form class="mt-5 flex max-w-sm gap-2" @submit.prevent="subscribed = true">
            <label for="newsletter-email" class="sr-only">Work email</label>
            <input id="newsletter-email" v-model="email" type="email" required placeholder="Work email" class="h-12 min-w-0 flex-1 rounded-full border border-white/20 bg-white/10 px-4 text-sm text-white placeholder:text-neutral-400 outline-none focus:border-violet-400" />
            <button class="btn btn-violet shrink-0">Subscribe</button>
          </form>
          <p v-if="subscribed" class="mt-2 flex items-center gap-1.5 text-sm text-emerald-400"><CheckCircle2 class="h-4 w-4" /> Thanks — you are on the list. Demo data only.</p>
        </div>
        <nav aria-label="Product"><p class="text-sm font-bold uppercase tracking-wider text-neutral-400">Product</p><ul class="mt-4 space-y-1 text-sm"><li><NuxtLink to="/features" class="flex min-h-11 items-center hover:text-violet-300">Features</NuxtLink></li><li><NuxtLink to="/tools" class="flex min-h-11 items-center hover:text-violet-300">Tools</NuxtLink></li><li><NuxtLink to="/pricing" class="flex min-h-11 items-center hover:text-violet-300">Pricing</NuxtLink></li><li><NuxtLink to="/integrations" class="flex min-h-11 items-center hover:text-violet-300">Integrations</NuxtLink></li><li><NuxtLink to="/product-tour" class="flex min-h-11 items-center hover:text-violet-300">Product tour</NuxtLink></li><li><NuxtLink to="/templates" class="flex min-h-11 items-center hover:text-violet-300">Templates</NuxtLink></li><li><NuxtLink to="/developers" class="flex min-h-11 items-center hover:text-violet-300">Developers</NuxtLink></li><li><NuxtLink to="/changelog" class="flex min-h-11 items-center hover:text-violet-300">Changelog</NuxtLink></li></ul></nav>
        <nav aria-label="Company"><p class="text-sm font-bold uppercase tracking-wider text-neutral-400">Company</p><ul class="mt-4 space-y-1 text-sm"><li><NuxtLink to="/about" class="flex min-h-11 items-center hover:text-violet-300">About</NuxtLink></li><li><NuxtLink to="/customers" class="flex min-h-11 items-center hover:text-violet-300">Customers</NuxtLink></li><li><NuxtLink to="/careers" class="flex min-h-11 items-center hover:text-violet-300">Careers</NuxtLink></li><li><NuxtLink to="/press" class="flex min-h-11 items-center hover:text-violet-300">Press</NuxtLink></li><li><NuxtLink to="/blog" class="flex min-h-11 items-center hover:text-violet-300">Blog</NuxtLink></li><li><NuxtLink to="/contact" class="flex min-h-11 items-center hover:text-violet-300">Contact</NuxtLink></li></ul></nav>
        <nav aria-label="Resources"><p class="text-sm font-bold uppercase tracking-wider text-neutral-400">Resources</p><ul class="mt-4 space-y-1 text-sm"><li><NuxtLink to="/help" class="flex min-h-11 items-center hover:text-violet-300">Help Center</NuxtLink></li><li><NuxtLink to="/resources" class="flex min-h-11 items-center hover:text-violet-300">Resources</NuxtLink></li><li><NuxtLink to="/roi-calculator" class="flex min-h-11 items-center hover:text-violet-300">ROI Calculator</NuxtLink></li><li><NuxtLink to="/compare" class="flex min-h-11 items-center hover:text-violet-300">Compare</NuxtLink></li><li><NuxtLink to="/faq" class="flex min-h-11 items-center hover:text-violet-300">FAQ</NuxtLink></li><li><NuxtLink to="/trust-center" class="flex min-h-11 items-center hover:text-violet-300">Trust Center</NuxtLink></li><li><NuxtLink to="/status" class="flex min-h-11 items-center hover:text-violet-300">Status</NuxtLink></li><li><NuxtLink to="/security" class="flex min-h-11 items-center hover:text-violet-300">Security</NuxtLink></li></ul></nav>
      </div>
      <div class="border-t border-white/10"><div class="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-3 px-4 py-5 text-xs text-neutral-400 sm:px-6"><span>© 2026 CloudPilot. Demo site — all copy, prices and testimonials are mock data.</span><span class="flex items-center gap-4"><NuxtLink to="/privacy-policy" class="flex min-h-11 items-center hover:text-white">Privacy</NuxtLink><NuxtLink to="/terms" class="flex min-h-11 items-center hover:text-white">Terms</NuxtLink><NuxtLink to="/cookie-policy" class="flex min-h-11 items-center hover:text-white">Cookies</NuxtLink><NuxtLink to="/sitemap" class="flex min-h-11 items-center hover:text-white">Sitemap</NuxtLink></span></div></div>
    </footer>
    <AnimatePresence>
      <Motion v-if="showTop" :initial="{ opacity: 0, y: 12 }" :animate="{ opacity: 1, y: 0 }" :exit="{ opacity: 0, y: 12 }" :transition="{ duration: 0.2, ease: 'easeOut' }" class="fixed bottom-6 right-6 z-40">
        <button class="grid h-12 w-12 place-items-center rounded-full bg-violet-600 text-white shadow-xl transition hover:bg-violet-700" aria-label="Back to top" @click="toTop"><ArrowUp class="h-5 w-5" /></button>
      </Motion>
    </AnimatePresence>
  </div>
</template>
<script setup lang="ts">
import { Menu, X } from '@lucide/vue'

const open = ref('')
const mobile = ref(false)
const showTop = ref(false)
const palette = ref<{ openPalette: () => void } | null>(null)
const email = ref('')
const subscribed = ref(false)
const scrolled = ref(false)
const route = useRoute()

// Self-referencing canonical + BreadcrumbList on every page (audit: no
// canonical tag site-wide, no breadcrumb schema). Names come from the URL
// segments; visuals are untouched — this is head metadata only.
const siteUrl = 'https://cloudpilot-saas.pages.dev'
const canonicalUrl = computed(() => siteUrl + (route.path === '/' ? '/' : route.path))
const crumbs = computed(() => {
  const parts = route.path.split('/').filter(Boolean)
  const items = [{ name: 'Home', url: siteUrl + '/' }]
  let acc = ''
  for (const p of parts) {
    acc += '/' + p
    items.push({ name: p.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '), url: siteUrl + acc })
  }
  return items
})
useHead(() => ({
  link: [{ rel: 'canonical', href: canonicalUrl.value }],
  script: [{
    type: 'application/ld+json',
    innerHTML: JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      itemListElement: crumbs.value.map((c, i) => ({ '@type': 'ListItem', position: i + 1, name: c.name, item: c.url }))
    })
  }]
}))

// Scroll progress bar (motion-v, spring-smoothed)
const { scrollYProgress } = useScroll()
const progress = useSpring(scrollYProgress, { stiffness: 120, damping: 30, mass: 0.4 })

const onScroll = () => { scrolled.value = window.scrollY > 8; showTop.value = window.scrollY > 600 }
const toTop = () => window.scrollTo({ top: 0, behavior: 'smooth' })
const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') { open.value = ''; mobile.value = false } }
const onDocClick = (e: MouseEvent) => { if (!(e.target as HTMLElement).closest('header nav')) open.value = '' }

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('keydown', onKey)
  document.addEventListener('click', onDocClick)
  onScroll()
})
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('keydown', onKey)
  document.removeEventListener('click', onDocClick)
})
watch(() => route.path, () => { open.value = ''; mobile.value = false })
</script>
