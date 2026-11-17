<template>
  <div>
    <!-- HERO — same-to-same as reference -->
    <section class="hero-grad text-white">
      <div class="mx-auto max-w-7xl px-4 pb-10 pt-14 sm:px-6 sm:pt-20">
        <div class="grid gap-10 lg:grid-cols-2 lg:items-start">
          <div>
            <p class="reveal inline-flex items-center gap-2 rounded-full border border-white/25 bg-white/10 px-3 py-1 text-xs font-semibold">✦ All-in-One SaaS Platform ✦</p>
            <h1 class="reveal mt-6 text-5xl font-extrabold leading-[1.02] tracking-tight sm:text-6xl lg:text-7xl" style="--d:80ms">
              Simplify.<br />Automate.<br /><span class="text-grad">Scale Your</span><br /><span class="text-grad">Business.</span><br />All in One Platform.
            </h1>
          </div>
          <div class="reveal lg:pt-24" style="--d:160ms">
            <p class="max-w-md text-base leading-relaxed text-violet-100 sm:text-lg">CloudPilot helps teams automate workflows, collaborate in real-time, and make data-driven decisions — faster than ever.</p>
            <div class="mt-7 flex flex-wrap items-center gap-5">
              <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-black shadow-lg hover:bg-violet-100">Start Free Trial</NuxtLink>
              <button @click="showDemo = !showDemo" class="flex items-center gap-2 text-sm font-semibold hover:text-violet-200">Watch Demo <span class="grid h-8 w-8 place-items-center rounded-full border border-white/50 text-xs">▶</span></button>
            </div>
            <div v-if="showDemo" class="mt-6 overflow-hidden rounded-2xl bg-black/60 p-5 text-sm leading-relaxed text-violet-100">
              <p class="font-bold text-white">60-second demo — what you would see:</p>
              <p class="mt-2">1. A new deal lands in Salesforce → FlowMaster creates the onboarding tasks automatically.<br />2. InsightPro flags the deal as at-risk and alerts the owner in Slack.<br />3. The team resolves it together in TeamSync — no meeting needed.</p>
              <p class="mt-2 text-xs text-violet-300">Demo video is a placeholder in this demo build.</p>
            </div>
          </div>
        </div>
        <div class="mt-14 flex flex-wrap items-end justify-between gap-6 border-t border-white/15 pt-6 sm:mt-20">
          <div class="reveal flex items-center gap-3">
            <div class="flex -space-x-2">
              <img src="/images/hero-woman.webp" alt="Happy CloudPilot user" class="h-10 w-10 rounded-full border-2 border-white object-cover" />
              <span class="grid h-10 w-10 place-items-center rounded-full border-2 border-white bg-violet-500 text-xs font-bold">AK</span>
              <span class="grid h-10 w-10 place-items-center rounded-full border-2 border-white bg-fuchsia-500 text-xs font-bold">JM</span>
            </div>
            <div>
              <p class="text-amber-300 tracking-widest">★★★★★</p>
              <p class="text-sm font-semibold"><CountUp :to="12540" suffix="+" /> happy users</p>
            </div>
          </div>
          <NuxtLink to="/features" class="btn-arrow reveal flex items-center gap-2 rounded-full bg-black px-5 py-2.5 text-sm font-semibold text-white shadow-lg" style="--d:120ms">Explore Platform <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6" /></svg></NuxtLink>
          <div class="reveal flex gap-3" style="--d:200ms">
            <img src="/images/flowmaster.webp" alt="FlowMaster cloud" class="animate-floaty h-16 w-16 rounded-2xl object-cover shadow-lg sm:h-20 sm:w-20" />
            <img src="/images/insightpro.webp" alt="InsightPro chart" class="animate-floaty h-16 w-16 rounded-2xl object-cover shadow-lg sm:h-20 sm:w-20" style="animation-delay:.6s" />
            <img src="/images/teamsync.webp" alt="TeamSync people" class="animate-floaty h-16 w-16 rounded-2xl object-cover shadow-lg sm:h-20 sm:w-20" style="animation-delay:1.2s" />
          </div>
        </div>
      </div>
    </section>

    <!-- Integrations marquee -->
    <section class="overflow-hidden border-b border-neutral-100 py-6">
      <div class="animate-marquee flex w-max gap-3">
        <span v-for="n in 2" :key="n" class="flex gap-3">
          <span v-for="t in ['Salesforce','Slack','Gmail','HubSpot','Notion','Stripe','Zoom','Asana','Zendesk','Shopify']" :key="t" class="rounded-full border border-neutral-200 px-5 py-2 text-sm font-semibold text-neutral-600">{{ t }}</span>
        </span>
      </div>
    </section>

    <!-- ABOUT US -->
    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
      <p class="reveal inline-flex items-center gap-2 rounded-full border border-neutral-200 px-3 py-1 text-xs font-bold uppercase tracking-wider">▦ About Us</p>
      <div class="mt-6 grid gap-10 lg:grid-cols-2">
        <h2 class="reveal text-4xl font-extrabold leading-[1.08] tracking-tight sm:text-5xl" style="--d:80ms">Smart Solutions<br />Designed to <span class="text-grad">Drive</span><br /><span class="text-grad">Your Success.</span></h2>
        <p class="reveal max-w-md text-base leading-relaxed text-neutral-600 lg:justify-self-end" style="--d:160ms">We empower businesses with powerful tools to streamline operations, boost productivity, and accelerate growth.</p>
      </div>
      <div class="mt-12 grid gap-10 lg:grid-cols-2">
        <div class="reveal flex items-start gap-4">
          <img src="/images/hero-woman.webp" alt="CloudPilot customer" class="h-16 w-16 rounded-full object-cover" />
          <p class="max-w-xs text-sm leading-relaxed text-neutral-600">Everything you need to manage and grow your business in one place.</p>
        </div>
        <div class="reveal" style="--d:120ms">
          <h3 class="text-xl font-bold">Why CloudPilot?</h3>
          <p class="mt-3 max-w-lg text-sm leading-relaxed text-neutral-600">From task automation and team collaboration to advanced analytics and reporting, CloudPilot provides a complete suite of tools built for modern businesses. Focus on what matters most while we handle the rest.</p>
          <div class="mt-6 grid grid-cols-3 gap-4 text-center">
            <div><p class="text-3xl font-extrabold text-violet-700"><CountUp :to="12540" suffix="+" /></p><p class="mt-1 text-xs font-medium text-neutral-500">Happy users</p></div>
            <div><p class="text-3xl font-extrabold text-violet-700"><CountUp :to="98" suffix="%" /></p><p class="mt-1 text-xs font-medium text-neutral-500">Stay after trial</p></div>
            <div><p class="text-3xl font-extrabold text-violet-700"><CountUp :to="49" prefix="$" suffix="M+" /></p><p class="mt-1 text-xs font-medium text-neutral-500">Hours saved / yr</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURED TOOLS -->
    <section class="bg-neutral-50">
      <div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="reveal inline-flex items-center gap-2 rounded-full border border-neutral-200 bg-white px-3 py-1 text-xs font-bold uppercase tracking-wider">▦ Featured Tools</p>
        <div class="mt-6 flex flex-wrap items-end justify-between gap-6">
          <h2 class="reveal max-w-xl text-4xl font-extrabold leading-[1.08] tracking-tight sm:text-5xl" style="--d:80ms">Powerful Tools<br />Built for <span class="text-grad">Your Business</span></h2>
          <div class="reveal" style="--d:160ms">
            <p class="max-w-sm text-sm leading-relaxed text-neutral-600">Explore our suite of powerful tools designed to simplify workflows, improve collaboration, and drive better results.</p>
            <NuxtLink to="/tools" class="mt-4 inline-block rounded-full bg-black px-5 py-2.5 text-sm font-bold text-white hover:bg-violet-700">View All Tools</NuxtLink>
          </div>
        </div>
        <div class="mt-10 grid gap-6 md:grid-cols-3">
          <NuxtLink to="/tools/flowmaster" class="reveal card-hover group block overflow-hidden rounded-3xl bg-white shadow-sm">
            <div class="relative"><img src="/images/flowmaster.webp" alt="FlowMaster — Workflow Automation" class="h-64 w-full object-cover transition duration-500 group-hover:scale-105" /><span class="absolute bottom-3 left-3 rounded-full bg-white/90 px-3 py-1 text-xs font-bold">◉ FlowMaster</span></div>
            <div class="p-5"><p class="text-sm font-bold"><span class="text-violet-700">01</span> — Workflow Automation</p><p class="mt-2 text-sm text-neutral-600">Automate approvals, reminders and handoffs — no code.</p></div>
          </NuxtLink>
          <NuxtLink to="/tools/insightpro" class="reveal card-hover group block overflow-hidden rounded-3xl bg-white shadow-sm" style="--d:100ms">
            <div class="relative"><img src="/images/insightpro.webp" alt="InsightPro — Advanced Analytics" class="h-64 w-full object-cover transition duration-500 group-hover:scale-105" /><span class="absolute bottom-3 left-3 rounded-full bg-white/90 px-3 py-1 text-xs font-bold">◉ InsightPro</span></div>
            <div class="p-5"><p class="text-sm font-bold"><span class="text-violet-700">02</span> — Advanced Analytics</p><p class="mt-2 text-sm text-neutral-600">Dashboards and alerts that explain themselves.</p></div>
          </NuxtLink>
          <NuxtLink to="/tools/teamsync" class="reveal card-hover group block overflow-hidden rounded-3xl bg-white shadow-sm" style="--d:200ms">
            <div class="relative"><img src="/images/teamsync.webp" alt="TeamSync — Team Collaboration" class="h-64 w-full object-cover transition duration-500 group-hover:scale-105" /><span class="absolute bottom-3 left-3 rounded-full bg-white/90 px-3 py-1 text-xs font-bold">◉ TeamSync</span></div>
            <div class="p-5"><p class="text-sm font-bold"><span class="text-violet-700">03</span> — Team Collaboration</p><p class="mt-2 text-sm text-neutral-600">Real-time boards, comments and shared work.</p></div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS + TESTIMONIALS + FAQ -->
    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
      <h2 class="reveal text-center text-3xl font-extrabold tracking-tight sm:text-4xl">Live in three steps. <span class="text-grad">Loved in week one.</span></h2>
      <div class="mt-10 grid gap-5 md:grid-cols-3">
        <div v-for="(s,i) in steps" :key="s.t" class="reveal rounded-3xl border border-neutral-200 p-6" :style="`--d:${i*90}ms`"><p class="text-4xl font-black text-violet-200">0{{ i+1 }}</p><h3 class="mt-3 text-lg font-bold">{{ s.t }}</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">{{ s.d }}</p></div>
      </div>
      <div class="mt-14 grid gap-5 md:grid-cols-3">
        <blockquote v-for="(q,i) in quotes" :key="q.n" class="reveal rounded-3xl bg-violet-50 p-6" :style="`--d:${i*90}ms`">
          <p class="text-amber-500">★★★★★</p>
          <p class="mt-3 text-sm leading-relaxed">“{{ q.t }}”</p>
          <footer class="mt-4 flex items-center gap-3"><span class="grid h-10 w-10 place-items-center rounded-full bg-violet-600 text-xs font-bold text-white">{{ q.i }}</span><span><span class="block text-sm font-bold">{{ q.n }}</span><span class="block text-xs text-neutral-500">{{ q.r }}</span></span></footer>
        </blockquote>
      </div>
      <div class="mx-auto mt-14 max-w-3xl">
        <h3 class="reveal text-center text-2xl font-extrabold">Frequently asked questions</h3>
        <div class="mt-6 space-y-3">
          <div v-for="f in faqs" :key="f.q" class="reveal overflow-hidden rounded-2xl border border-neutral-200">
            <button @click="faqOpen = faqOpen===f.q ? '' : f.q" class="flex w-full items-center justify-between gap-4 px-5 py-4 text-left text-sm font-bold">{{ f.q }}<span>{{ faqOpen===f.q ? '−' : '+' }}</span></button>
            <p v-if="faqOpen===f.q" class="border-t border-neutral-100 px-5 py-4 text-sm leading-relaxed text-neutral-600">{{ f.a }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="mx-auto max-w-7xl px-4 pb-16 sm:px-6">
      <div class="reveal rounded-3xl bg-black px-6 py-14 text-center text-white sm:px-12">
        <h2 class="text-3xl font-extrabold tracking-tight sm:text-4xl">Simplify. Automate. <span class="text-grad">Scale.</span></h2>
        <p class="mx-auto mt-3 max-w-xl text-neutral-300">Join 12,540+ teams on CloudPilot. Free for 14 days, no credit card required.</p>
        <div class="mt-7 flex flex-wrap justify-center gap-3">
          <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-black">Start Free Trial</NuxtLink>
          <NuxtLink to="/pricing" class="rounded-full border border-white/40 px-6 py-3 text-sm font-bold">See Pricing</NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>
<script setup lang="ts">
useSeoMeta({ title: 'CloudPilot — Simplify. Automate. Scale Your Business.', description: 'CloudPilot helps teams automate workflows, collaborate in real-time, and make data-driven decisions — faster than ever.' })
const showDemo = ref(false)
const faqOpen = ref('Is there really a free trial?')
const steps = [
  { t: 'Connect your tools', d: 'Link Slack, Gmail, Salesforce and your calendar in one click. OAuth only — no passwords stored.' },
  { t: 'Automate the busywork', d: 'Pick a template or build a flow in the visual editor. Test it on real data before switching it on.' },
  { t: 'Scale with insight', d: 'Watch live dashboards, set alerts, and let your team focus on work only humans can do.' }
]
const quotes = [
  { t: 'We replaced five tools in a week. The first month alone saved us 40 hours a week.', n: 'Maya Chen', r: 'Ops Lead, Nimbus', i: 'MC' },
  { t: 'InsightPro flagged a churn risk we would have missed. That one alert paid for a year.', n: 'James Okafor', r: 'Founder, Loopwork', i: 'JO' },
  { t: 'Approvals went from three days to four hours. Our clients noticed before we did.', n: 'Priya Sharma', r: 'COO, Fieldset', i: 'PS' }
]
const faqs = [
  { q: 'Is there really a free trial?', a: 'Yes — 14 days on the Growth plan, no credit card required. Your data stays exportable if you cancel.' },
  { q: 'Do I need to write code?', a: 'No. FlowMaster is drag-and-drop. Developers can use the API and webhooks if they want to.' },
  { q: 'Can I cancel anytime?', a: 'Yes, in two clicks from Settings. No lock-in, no exit fees, export anytime.' },
  { q: 'Is my data safe?', a: 'SOC 2 Type II, GDPR, AES-256 at rest and TLS 1.3 in transit. See the Security page for the full list.' }
]
</script>
