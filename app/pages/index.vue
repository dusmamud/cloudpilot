<template>
  <div>
    <!-- HERO — same-to-same as reference, rebuilt mobile-first -->
    <section class="hero-grad text-white">
      <div class="mx-auto max-w-7xl px-4 pb-8 pt-10 sm:px-6 sm:pb-10 sm:pt-16 lg:pt-20">
        <div class="grid gap-8 lg:grid-cols-2 lg:items-start lg:gap-12">
          <div>
            <Motion :initial="{ opacity: 0, y: 16 }" :animate="{ opacity: 1, y: 0 }" :transition="{ duration: 0.5, ease: 'easeOut' }">
              <p class="inline-flex items-center gap-2 rounded-full border border-white/25 bg-white/10 px-3.5 py-1.5 text-xs font-semibold"><Sparkles class="h-3.5 w-3.5" /> All-in-One SaaS Platform</p>
            </Motion>
            <Motion :initial="{ opacity: 0, y: 24 }" :animate="{ opacity: 1, y: 0 }" :transition="{ duration: 0.6, delay: 0.08, ease: 'easeOut' }">
              <h1 class="mt-6 text-[2.6rem] font-extrabold leading-[1.04] tracking-tight sm:text-6xl lg:text-[4.4rem]">
                Simplify.<br />Automate.<br /><span class="text-grad">Scale Your</span><br /><span class="text-grad">Business.</span><br />All in One Platform.
              </h1>
            </Motion>
          </div>
          <Motion :initial="{ opacity: 0, y: 24 }" :animate="{ opacity: 1, y: 0 }" :transition="{ duration: 0.6, delay: 0.18, ease: 'easeOut' }" class="lg:pt-24">
            <p class="max-w-md text-base leading-relaxed text-violet-100 sm:text-lg">CloudPilot helps teams automate workflows, collaborate in real-time, and make data-driven decisions — faster than ever.</p>
            <div class="mt-7 flex flex-wrap items-center gap-4">
              <NuxtLink to="/request-demo" class="btn btn-white">Start Free Trial</NuxtLink>
              <button class="flex min-h-12 items-center gap-2.5 text-sm font-semibold transition hover:text-violet-200" :aria-expanded="showDemo" @click="showDemo = !showDemo">
                Watch Demo
                <span class="grid h-10 w-10 place-items-center rounded-full border border-white/50"><Play class="h-4 w-4 fill-white" /></span>
              </button>
            </div>
            <AnimatePresence>
              <Motion v-if="showDemo" :initial="{ height: 0, opacity: 0 }" :animate="{ height: 'auto', opacity: 1 }" :exit="{ height: 0, opacity: 0 }" :transition="{ duration: 0.3, ease: 'easeInOut' }" class="overflow-hidden">
                <div class="mt-6 rounded-2xl bg-black/60 p-5 text-sm leading-relaxed text-violet-100">
                  <p class="font-bold text-white">60-second demo — what you would see:</p>
                  <ol class="mt-2 list-decimal space-y-1 pl-5">
                    <li>A new deal lands in Salesforce — FlowMaster creates the onboarding tasks automatically.</li>
                    <li>InsightPro flags the deal as at-risk and alerts the owner in Slack.</li>
                    <li>The team resolves it together in TeamSync — no meeting needed.</li>
                  </ol>
                  <p class="mt-2 text-xs text-violet-300">Demo video is a placeholder in this demo build.</p>
                </div>
              </Motion>
            </AnimatePresence>
          </Motion>
        </div>
        <!-- Bottom bar sits on the pale lavender fade: DARK text for contrast -->
        <Motion :initial="{ opacity: 0, y: 16 }" :animate="{ opacity: 1, y: 0 }" :transition="{ duration: 0.6, delay: 0.3, ease: 'easeOut' }" class="mt-12 flex flex-wrap items-end justify-between gap-6 border-t border-black/10 pt-6 text-neutral-900 sm:mt-16">
          <div class="flex items-center gap-3">
            <div class="flex -space-x-2">
              <img src="/images/hero-woman.webp" alt="Happy CloudPilot user" class="h-11 w-11 rounded-full border-2 border-white object-cover" />
              <span class="grid h-11 w-11 place-items-center rounded-full border-2 border-white bg-violet-500 text-xs font-bold text-white">AK</span>
              <span class="grid h-11 w-11 place-items-center rounded-full border-2 border-white bg-fuchsia-500 text-xs font-bold text-white">JM</span>
            </div>
            <div>
              <p class="flex items-center gap-0.5" aria-label="Rated 5 out of 5 stars">
                <Star v-for="n in 5" :key="n" class="h-4 w-4 fill-amber-400 text-amber-400" />
              </p>
              <p class="mt-0.5 text-sm font-semibold"><CountUp :to="12540" suffix="+" /> happy users</p>
            </div>
          </div>
          <NuxtLink to="/features" class="btn btn-dark btn-arrow">Explore Platform <ArrowRight class="h-4 w-4" /></NuxtLink>
          <div class="flex gap-3">
            <span class="tool-bg-flowmaster animate-floaty grid h-16 w-16 place-items-center rounded-2xl p-1.5 shadow-lg sm:h-20 sm:w-20"><img src="/images/flowmaster.png" alt="FlowMaster cloud" class="tool-object max-h-full max-w-full object-contain" /></span>
            <span class="tool-bg-insightpro animate-floaty grid h-16 w-16 place-items-center rounded-2xl p-1.5 shadow-lg sm:h-20 sm:w-20" style="animation-delay:.6s"><img src="/images/insightpro.png" alt="InsightPro chart" class="tool-object max-h-full max-w-full object-contain" /></span>
            <span class="tool-bg-teamsync animate-floaty grid h-16 w-16 place-items-center rounded-2xl p-1.5 shadow-lg sm:h-20 sm:w-20" style="animation-delay:1.2s"><img src="/images/teamsync.png" alt="TeamSync people" class="tool-object max-h-full max-w-full object-contain" /></span>
          </div>
        </Motion>
      </div>
    </section>

    <!-- Integrations marquee -->
    <section class="overflow-hidden border-b border-neutral-100 py-6" aria-label="Integrations">
      <div class="animate-marquee flex w-max gap-3">
        <span v-for="n in 2" :key="n" class="flex gap-3" :aria-hidden="n === 2">
          <span v-for="t in ['Salesforce', 'Slack', 'Gmail', 'HubSpot', 'Notion', 'Stripe', 'Zoom', 'Asana', 'Zendesk', 'Shopify']" :key="t" class="rounded-full border border-neutral-200 px-5 py-2.5 text-sm font-semibold text-neutral-600">{{ t }}</span>
        </span>
      </div>
    </section>

    <!-- ABOUT US -->
    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
      <p class="reveal inline-flex items-center gap-2 rounded-full border border-neutral-200 px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider"><Layers class="h-3.5 w-3.5 text-violet-600" /> About Us</p>
      <div class="mt-6 grid gap-6 lg:grid-cols-2 lg:gap-10">
        <h2 class="reveal text-4xl font-extrabold leading-[1.08] tracking-tight sm:text-5xl" style="--d:80ms">Smart Solutions<br />Designed to <span class="text-grad-light">Drive</span><br /><span class="text-grad-light">Your Success.</span></h2>
        <p class="reveal max-w-md text-base leading-relaxed text-neutral-600 lg:justify-self-end" style="--d:160ms">We empower businesses with powerful tools to streamline operations, boost productivity, and accelerate growth.</p>
      </div>
      <div class="mt-12 grid gap-10 lg:grid-cols-2">
        <div class="reveal flex items-start gap-4">
          <img src="/images/hero-woman.webp" alt="CloudPilot customer" class="h-16 w-16 shrink-0 rounded-full object-cover" />
          <p class="max-w-xs text-sm leading-relaxed text-neutral-600">Everything you need to manage and grow your business in one place.</p>
        </div>
        <div class="reveal" style="--d:120ms">
          <h3 class="text-xl font-bold">Why CloudPilot?</h3>
          <p class="mt-3 max-w-lg text-sm leading-relaxed text-neutral-600">From task automation and team collaboration to advanced analytics and reporting, CloudPilot provides a complete suite of tools built for modern businesses. Focus on what matters most while we handle the rest.</p>
          <div class="mt-6 grid grid-cols-3 gap-4 text-center">
            <div><p class="text-3xl font-extrabold text-violet-700 sm:text-4xl"><CountUp :to="12540" suffix="+" /></p><p class="mt-1 text-xs font-medium text-neutral-500">Happy users</p></div>
            <div><p class="text-3xl font-extrabold text-violet-700 sm:text-4xl"><CountUp :to="98" suffix="%" /></p><p class="mt-1 text-xs font-medium text-neutral-500">Stay after trial</p></div>
            <div><p class="text-3xl font-extrabold text-violet-700 sm:text-4xl"><CountUp :to="49" prefix="$" suffix="M+" /></p><p class="mt-1 text-xs font-medium text-neutral-500">Hours saved / yr</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURED TOOLS -->
    <section class="bg-neutral-50">
      <div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="reveal inline-flex items-center gap-2 rounded-full border border-neutral-200 bg-white px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider"><LayoutGrid class="h-3.5 w-3.5 text-violet-600" /> Featured Tools</p>
        <div class="mt-6 flex flex-wrap items-end justify-between gap-6">
          <h2 class="reveal max-w-xl text-4xl font-extrabold leading-[1.08] tracking-tight sm:text-5xl" style="--d:80ms">Powerful Tools<br />Built for <span class="text-grad-light">Your Business</span></h2>
          <div class="reveal" style="--d:160ms">
            <p class="max-w-sm text-sm leading-relaxed text-neutral-600">Explore our suite of powerful tools designed to simplify workflows, improve collaboration, and drive better results.</p>
            <NuxtLink to="/tools" class="btn btn-dark mt-5">View All Tools</NuxtLink>
          </div>
        </div>
        <div class="mt-10 grid gap-6 md:grid-cols-3">
          <NuxtLink to="/tools/flowmaster" class="reveal card-hover group block overflow-hidden rounded-3xl bg-white shadow-sm ring-1 ring-black/5">
            <div class="tool-bg-flowmaster relative grid aspect-square place-items-center overflow-hidden"><img src="/images/flowmaster.png" alt="FlowMaster — Workflow Automation" class="tool-object w-4/5 transition duration-500 group-hover:scale-105" /><span class="absolute bottom-4 left-4 inline-flex items-center gap-2 text-base font-bold text-white drop-shadow-md"><Workflow class="h-5 w-5" /> FlowMaster</span></div>
            <div class="p-5 sm:p-6"><p class="text-sm font-bold"><span class="text-violet-700">01</span> — Workflow Automation</p><p class="mt-2 text-sm leading-relaxed text-neutral-600">Automate approvals, reminders and handoffs — no code.</p></div>
          </NuxtLink>
          <NuxtLink to="/tools/insightpro" class="reveal card-hover group block overflow-hidden rounded-3xl bg-white shadow-sm ring-1 ring-black/5" style="--d:100ms">
            <div class="tool-bg-insightpro relative grid aspect-square place-items-center overflow-hidden"><img src="/images/insightpro.png" alt="InsightPro — Advanced Analytics" class="tool-object w-4/5 transition duration-500 group-hover:scale-105" /><span class="absolute bottom-4 left-4 inline-flex items-center gap-2 text-base font-bold text-white drop-shadow-md"><BarChart3 class="h-5 w-5" /> InsightPro</span></div>
            <div class="p-5 sm:p-6"><p class="text-sm font-bold"><span class="text-violet-700">02</span> — Advanced Analytics</p><p class="mt-2 text-sm leading-relaxed text-neutral-600">Dashboards and alerts that explain themselves.</p></div>
          </NuxtLink>
          <NuxtLink to="/tools/teamsync" class="reveal card-hover group block overflow-hidden rounded-3xl bg-white shadow-sm ring-1 ring-black/5" style="--d:200ms">
            <div class="tool-bg-teamsync relative grid aspect-square place-items-center overflow-hidden"><img src="/images/teamsync.png" alt="TeamSync — Team Collaboration" class="tool-object w-4/5 transition duration-500 group-hover:scale-105" /><span class="absolute bottom-4 left-4 inline-flex items-center gap-2 text-base font-bold text-white drop-shadow-md"><Users class="h-5 w-5" /> TeamSync</span></div>
            <div class="p-5 sm:p-6"><p class="text-sm font-bold"><span class="text-violet-700">03</span> — Team Collaboration</p><p class="mt-2 text-sm leading-relaxed text-neutral-600">Real-time boards, comments and shared work.</p></div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS + TESTIMONIALS + FAQ -->
    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
      <h2 class="reveal text-center text-3xl font-extrabold tracking-tight sm:text-4xl">Live in three steps. <span class="text-grad-light">Loved in week one.</span></h2>
      <div class="mt-10 grid gap-5 md:grid-cols-3">
        <div v-for="(s, i) in steps" :key="s.t" class="reveal rounded-3xl border border-neutral-200 p-6" :style="`--d:${i * 90}ms`">
          <span class="grid h-12 w-12 place-items-center rounded-2xl bg-violet-100 text-lg font-black text-violet-700">0{{ i + 1 }}</span>
          <h3 class="mt-4 text-lg font-bold">{{ s.t }}</h3>
          <p class="mt-2 text-sm leading-relaxed text-neutral-600">{{ s.d }}</p>
        </div>
      </div>
      <div class="mt-14 grid gap-5 md:grid-cols-3">
        <blockquote v-for="(q, i) in quotes" :key="q.n" class="reveal rounded-3xl bg-violet-50 p-6" :style="`--d:${i * 90}ms`">
          <p class="flex items-center gap-0.5" :aria-label="`Rated 5 out of 5 by ${q.n}`">
            <Star v-for="n in 5" :key="n" class="h-4 w-4 fill-amber-400 text-amber-400" />
          </p>
          <p class="mt-3 text-sm leading-relaxed">“{{ q.t }}”</p>
          <footer class="mt-4 flex items-center gap-3"><span class="grid h-10 w-10 shrink-0 place-items-center rounded-full bg-violet-600 text-xs font-bold text-white">{{ q.i }}</span><span><span class="block text-sm font-bold">{{ q.n }}</span><span class="block text-xs text-neutral-500">{{ q.r }}</span></span></footer>
        </blockquote>
      </div>
      <div class="mx-auto mt-14 max-w-3xl">
        <h3 class="reveal text-center text-2xl font-extrabold">Frequently asked questions</h3>
        <div class="mt-6 space-y-3">
          <div v-for="f in faqs" :key="f.q" class="reveal overflow-hidden rounded-2xl border border-neutral-200">
            <button class="flex min-h-14 w-full items-center justify-between gap-4 px-5 text-left text-sm font-bold" :aria-expanded="faqOpen === f.q" @click="faqOpen = faqOpen === f.q ? '' : f.q">
              {{ f.q }}<component :is="faqOpen === f.q ? Minus : Plus" class="h-5 w-5 shrink-0 text-violet-600" />
            </button>
            <AnimatePresence>
              <Motion v-if="faqOpen === f.q" :initial="{ height: 0, opacity: 0 }" :animate="{ height: 'auto', opacity: 1 }" :exit="{ height: 0, opacity: 0 }" :transition="{ duration: 0.25, ease: 'easeInOut' }" class="overflow-hidden">
                <p class="border-t border-neutral-100 px-5 py-4 text-sm leading-relaxed text-neutral-600">{{ f.a }}</p>
              </Motion>
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="mx-auto max-w-7xl px-4 pb-16 sm:px-6 sm:pb-20">
      <div class="reveal rounded-3xl bg-black px-6 py-14 text-center text-white sm:px-12">
        <h2 class="text-3xl font-extrabold tracking-tight sm:text-4xl">Simplify. Automate. <span class="text-grad">Scale.</span></h2>
        <p class="mx-auto mt-3 max-w-xl text-neutral-300">Join 12,540+ teams on CloudPilot. Free for 14 days, no credit card required.</p>
        <div class="mt-7 flex flex-wrap justify-center gap-3">
          <NuxtLink to="/request-demo" class="btn btn-white">Start Free Trial</NuxtLink>
          <NuxtLink to="/pricing" class="btn btn-outline-light">See Pricing</NuxtLink>
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
