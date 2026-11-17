<template>
  <div class="min-h-screen bg-white text-neutral-900">
    <header class="sticky top-0 z-50 bg-black text-white">
      <div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6">
        <NuxtLink to="/" class="flex items-center gap-2" aria-label="CloudPilot home">
          <span class="grid h-9 w-9 place-items-center rounded-full bg-gradient-to-br from-violet-500 to-fuchsia-500 text-xl font-black">C</span>
          <span class="text-lg font-bold tracking-tight">CloudPilot</span>
        </NuxtLink>
        <nav class="hidden items-center gap-1 lg:flex" aria-label="Primary">
          <div class="relative" @mouseenter="open='product'" @mouseleave="open=''">
            <button class="flex items-center gap-1 rounded-full px-3 py-2 text-sm font-medium hover:bg-white/10" @click="open = open==='product'?'':'product'">Product <span class="text-xs">▾</span></button>
            <div v-if="open==='product'" class="absolute left-0 top-full w-72 rounded-2xl bg-white p-2 text-neutral-900 shadow-2xl">
              <NuxtLink to="/features" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">Features</span><span class="text-sm text-neutral-500">Everything in one platform</span></NuxtLink>
              <NuxtLink to="/tools" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">Tools</span><span class="block text-sm text-neutral-500">FlowMaster, InsightPro, TeamSync</span></NuxtLink>
              <NuxtLink to="/integrations" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">Integrations</span><span class="block text-sm text-neutral-500">100+ tools, one click</span></NuxtLink>
              <NuxtLink to="/security" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">Security</span><span class="block text-sm text-neutral-500">SOC 2, GDPR, SSO</span></NuxtLink>
            </div>
          </div>
          <div class="relative" @mouseenter="open='solutions'" @mouseleave="open=''">
            <button class="flex items-center gap-1 rounded-full px-3 py-2 text-sm font-medium hover:bg-white/10" @click="open = open==='solutions'?'':'solutions'">Solutions <span class="text-xs">▾</span></button>
            <div v-if="open==='solutions'" class="absolute left-0 top-full w-72 rounded-2xl bg-white p-2 text-neutral-900 shadow-2xl">
              <NuxtLink to="/solutions" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">All solutions</span><span class="block text-sm text-neutral-500">By team and company size</span></NuxtLink>
              <NuxtLink to="/solutions/startups" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">For Startups</span><span class="block text-sm text-neutral-500">Ship fast, stay lean</span></NuxtLink>
              <NuxtLink to="/solutions/teams" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">For Teams</span><span class="block text-sm text-neutral-500">Collaborate in real-time</span></NuxtLink>
              <NuxtLink to="/solutions/enterprise" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">For Enterprise</span><span class="block text-sm text-neutral-500">Scale with control</span></NuxtLink>
            </div>
          </div>
          <NuxtLink to="/pricing" class="rounded-full px-3 py-2 text-sm font-medium hover:bg-white/10">Pricing</NuxtLink>
          <div class="relative" @mouseenter="open='resources'" @mouseleave="open=''">
            <button class="flex items-center gap-1 rounded-full px-3 py-2 text-sm font-medium hover:bg-white/10" @click="open = open==='resources'?'':'resources'">Resources <span class="text-xs">▾</span></button>
            <div v-if="open==='resources'" class="absolute left-0 top-full w-72 rounded-2xl bg-white p-2 text-neutral-900 shadow-2xl">
              <NuxtLink to="/blog" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">Blog</span><span class="block text-sm text-neutral-500">Guides and product news</span></NuxtLink>
              <NuxtLink to="/customers" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">Customers</span><span class="block text-sm text-neutral-500">Case studies that shipped</span></NuxtLink>
              <NuxtLink to="/help" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">Help Center</span><span class="block text-sm text-neutral-500">Answers in minutes</span></NuxtLink>
              <NuxtLink to="/changelog" class="block rounded-xl px-4 py-3 hover:bg-violet-50"><span class="block font-semibold">Changelog</span><span class="block text-sm text-neutral-500">What is new in CloudPilot</span></NuxtLink>
            </div>
          </div>
          <NuxtLink to="/about" class="rounded-full px-3 py-2 text-sm font-medium hover:bg-white/10">Company</NuxtLink>
        </nav>
        <div class="flex items-center gap-2">
          <NuxtLink to="/login" class="hidden rounded-full px-3 py-2 text-sm font-medium hover:bg-white/10 sm:block">Sign in</NuxtLink>
          <NuxtLink to="/request-demo" class="btn-arrow rounded-full border border-white/40 px-4 py-2 text-sm font-semibold hover:bg-white hover:text-black">Get Started</NuxtLink>
          <button class="grid h-11 w-11 place-items-center rounded-full bg-white text-black lg:hidden" @click="mobile=!mobile" aria-label="Menu">☰</button>
        </div>
      </div>
      <div v-if="mobile" class="border-t border-white/10 px-4 pb-6 pt-2 lg:hidden">
        <div class="grid gap-1 text-sm font-medium">
          <NuxtLink to="/features" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Features</NuxtLink>
          <NuxtLink to="/tools" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Tools</NuxtLink>
          <NuxtLink to="/solutions" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Solutions</NuxtLink>
          <NuxtLink to="/pricing" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Pricing</NuxtLink>
          <NuxtLink to="/blog" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Blog</NuxtLink>
          <NuxtLink to="/customers" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Customers</NuxtLink>
          <NuxtLink to="/about" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Company</NuxtLink>
          <NuxtLink to="/help" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Help Center</NuxtLink>
          <NuxtLink to="/login" @click="mobile=false" class="rounded-lg px-3 py-2.5 hover:bg-white/10">Sign in</NuxtLink>
        </div>
      </div>
    </header>
    <main><slot /></main>
    <footer class="bg-black text-white">
      <div class="mx-auto grid max-w-7xl gap-10 px-4 py-14 sm:grid-cols-2 sm:px-6 lg:grid-cols-5">
        <div class="lg:col-span-2">
          <div class="flex items-center gap-2"><span class="grid h-9 w-9 place-items-center rounded-full bg-gradient-to-br from-violet-500 to-fuchsia-500 text-xl font-black">C</span><span class="text-lg font-bold">CloudPilot</span></div>
          <p class="mt-4 max-w-sm text-sm leading-relaxed text-neutral-400">Simplify. Automate. Scale your business — all in one platform. Built for modern teams that move fast.</p>
          <form class="mt-5 flex max-w-sm gap-2" @submit.prevent="subscribed=true">
            <input v-model="email" type="email" required placeholder="Work email" class="min-w-0 flex-1 rounded-full border border-white/20 bg-white/10 px-4 py-2.5 text-sm text-white placeholder:text-neutral-400 outline-none focus:border-violet-400" />
            <button class="shrink-0 rounded-full bg-violet-600 px-4 py-2.5 text-sm font-semibold hover:bg-violet-500">Subscribe</button>
          </form>
          <p v-if="subscribed" class="mt-2 text-sm text-emerald-400">Thanks — you are on the list. Demo data only.</p>
        </div>
        <div><h3 class="text-sm font-bold uppercase tracking-wider text-neutral-400">Product</h3><ul class="mt-4 space-y-2.5 text-sm"><li><NuxtLink to="/features" class="hover:text-violet-300">Features</NuxtLink></li><li><NuxtLink to="/tools" class="hover:text-violet-300">Tools</NuxtLink></li><li><NuxtLink to="/pricing" class="hover:text-violet-300">Pricing</NuxtLink></li><li><NuxtLink to="/integrations" class="hover:text-violet-300">Integrations</NuxtLink></li><li><NuxtLink to="/changelog" class="hover:text-violet-300">Changelog</NuxtLink></li></ul></div>
        <div><h3 class="text-sm font-bold uppercase tracking-wider text-neutral-400">Company</h3><ul class="mt-4 space-y-2.5 text-sm"><li><NuxtLink to="/about" class="hover:text-violet-300">About</NuxtLink></li><li><NuxtLink to="/customers" class="hover:text-violet-300">Customers</NuxtLink></li><li><NuxtLink to="/careers" class="hover:text-violet-300">Careers</NuxtLink></li><li><NuxtLink to="/blog" class="hover:text-violet-300">Blog</NuxtLink></li><li><NuxtLink to="/contact" class="hover:text-violet-300">Contact</NuxtLink></li></ul></div>
        <div><h3 class="text-sm font-bold uppercase tracking-wider text-neutral-400">Resources</h3><ul class="mt-4 space-y-2.5 text-sm"><li><NuxtLink to="/help" class="hover:text-violet-300">Help Center</NuxtLink></li><li><NuxtLink to="/resources" class="hover:text-violet-300">Resources</NuxtLink></li><li><NuxtLink to="/roi-calculator" class="hover:text-violet-300">ROI Calculator</NuxtLink></li><li><NuxtLink to="/compare" class="hover:text-violet-300">Compare</NuxtLink></li><li><NuxtLink to="/security" class="hover:text-violet-300">Security</NuxtLink></li></ul></div>
      </div>
      <div class="border-t border-white/10"><div class="mx-auto flex max-w-7xl flex-wrap items-center justify-between gap-3 px-4 py-5 text-xs text-neutral-400 sm:px-6"><span>© 2026 CloudPilot. Demo site — all copy, prices and testimonials are mock data.</span><span class="flex gap-4"><NuxtLink to="/privacy-policy" class="hover:text-white">Privacy</NuxtLink><NuxtLink to="/terms" class="hover:text-white">Terms</NuxtLink><NuxtLink to="/cookie-policy" class="hover:text-white">Cookies</NuxtLink><NuxtLink to="/sitemap" class="hover:text-white">Sitemap</NuxtLink></span></div></div>
    </footer>
  </div>
</template>
<script setup lang="ts">
const open = ref('')
const mobile = ref(false)
const email = ref('')
const subscribed = ref(false)
</script>
