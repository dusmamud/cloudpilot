<template>
  <div>
    <section class="bg-black text-white">
      <div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><Newspaper class="h-3.5 w-3.5" /> Press</p>
        <h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">The CloudPilot story, <span class="text-grad">ready to tell.</span></h1>
        <p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Press releases, coverage, logos and brand assets — everything a journalist needs to write about CloudPilot, in one place.</p>
        <div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms">
          <a href="#press-kit" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-black hover:bg-violet-200">Download press kit</a>
          <NuxtLink to="/contact" class="rounded-full border border-white/30 px-6 py-3 text-sm font-bold hover:bg-white/10">Contact the press team</NuxtLink>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 py-12 sm:px-6" aria-label="CloudPilot in numbers">
      <div class="grid grid-cols-2 gap-5 lg:grid-cols-4">
        <div class="reveal rounded-3xl border border-neutral-200 bg-white p-6 text-center" style="--d:0ms"><p class="text-3xl font-extrabold tracking-tight text-violet-700 sm:text-4xl">12,500+</p><p class="mt-1.5 text-sm text-neutral-600">Teams run on CloudPilot</p></div>
        <div class="reveal rounded-3xl border border-neutral-200 bg-white p-6 text-center" style="--d:80ms"><p class="text-3xl font-extrabold tracking-tight text-violet-700 sm:text-4xl">4.9 / 5</p><p class="mt-1.5 text-sm text-neutral-600">Average customer rating</p></div>
        <div class="reveal rounded-3xl border border-neutral-200 bg-white p-6 text-center" style="--d:160ms"><p class="text-3xl font-extrabold tracking-tight text-violet-700 sm:text-4xl">140+</p><p class="mt-1.5 text-sm text-neutral-600">Countries with active teams</p></div>
        <div class="reveal rounded-3xl border border-neutral-200 bg-white p-6 text-center" style="--d:240ms"><p class="text-3xl font-extrabold tracking-tight text-violet-700 sm:text-4xl">99.99%</p><p class="mt-1.5 text-sm text-neutral-600">Uptime, last 90 days</p></div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 pb-14 sm:px-6">
      <h2 class="reveal text-3xl font-extrabold tracking-tight sm:text-4xl">Press releases</h2>
      <p class="reveal mt-3 max-w-2xl text-base leading-relaxed text-neutral-600" style="--d:80ms">Official announcements from the CloudPilot team, newest first.</p>
      <div class="mt-8 grid gap-5 md:grid-cols-2">
        <article v-for="(r, i) in releases" :key="r.title" class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" :style="`--d:${i * 80}ms`">
          <div class="flex items-center gap-3 text-xs font-semibold"><span class="inline-flex items-center gap-1.5 rounded-full bg-violet-50 px-3 py-1 text-violet-700"><FileText class="h-3.5 w-3.5" /> {{ r.tag }}</span><time class="text-neutral-600">{{ r.date }}</time></div>
          <h3 class="mt-4 text-lg font-bold leading-snug">{{ r.title }}</h3>
          <p class="mt-2 text-sm leading-relaxed text-neutral-600">{{ r.excerpt }}</p>
        </article>
      </div>
    </section>

    <section class="bg-neutral-50">
      <div class="mx-auto max-w-7xl px-4 py-14 sm:px-6">
        <h2 class="reveal text-3xl font-extrabold tracking-tight sm:text-4xl">Coverage</h2>
        <p class="reveal mt-3 max-w-2xl text-base leading-relaxed text-neutral-600" style="--d:80ms">What industry publications have said about CloudPilot.</p>
        <div class="mt-8 grid gap-5 md:grid-cols-2">
          <figure v-for="(c, i) in coverage" :key="c.outlet" class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" :style="`--d:${i * 80}ms`">
            <Quote class="h-6 w-6 text-violet-600" aria-hidden="true" />
            <blockquote class="mt-4 text-base leading-relaxed text-neutral-900">&ldquo;{{ c.quote }}&rdquo;</blockquote>
            <figcaption class="mt-4 flex items-center justify-between gap-3 text-sm"><span class="font-bold">{{ c.outlet }}</span><time class="text-neutral-600">{{ c.date }}</time></figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section id="press-kit" class="mx-auto max-w-7xl scroll-mt-24 px-4 py-14 sm:px-6">
      <h2 class="reveal text-3xl font-extrabold tracking-tight sm:text-4xl">Press kit</h2>
      <p class="reveal mt-3 max-w-2xl text-base leading-relaxed text-neutral-600" style="--d:80ms">Logos, brand colours and product imagery. Free to use in editorial coverage of CloudPilot.</p>
      <div class="mt-8 grid gap-5 md:grid-cols-3">
        <article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:0ms">
          <div class="grid h-28 place-items-center rounded-2xl bg-black"><LogoMark class="h-16 w-16" /></div>
          <h3 class="mt-5 text-lg font-bold">Logo</h3>
          <p class="mt-1.5 text-sm leading-relaxed text-neutral-600">The CloudPilot mark — a bold C in a violet-to-white gradient. Use on dark backgrounds, with clear space around it.</p>
          <a href="/favicon.svg" download="cloudpilot-logo.svg" class="mt-5 inline-flex min-h-11 items-center gap-2 rounded-full bg-violet-600 px-5 text-sm font-bold text-white hover:bg-violet-700"><Download class="h-4 w-4" /> Download SVG</a>
        </article>
        <article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:80ms">
          <div class="grid h-28 grid-cols-3 overflow-hidden rounded-2xl"><span class="bg-violet-600" title="CloudPilot Violet #7C3AED" /><span class="bg-fuchsia-600" title="CloudPilot Fuchsia #C026D3" /><span class="bg-black" title="CloudPilot Ink #000000" /></div>
          <h3 class="mt-5 text-lg font-bold">Brand colours</h3>
          <p class="mt-1.5 text-sm leading-relaxed text-neutral-600">Violet <span class="font-semibold text-neutral-900">#7C3AED</span>, Fuchsia <span class="font-semibold text-neutral-900">#C026D3</span>, Ink <span class="font-semibold text-neutral-900">#000000</span>. Headlines use Inter ExtraBold.</p>
          <a href="/og-image.png" download="cloudpilot-brand.png" class="mt-5 inline-flex min-h-11 items-center gap-2 rounded-full bg-violet-600 px-5 text-sm font-bold text-white hover:bg-violet-700"><Download class="h-4 w-4" /> Download brand image</a>
        </article>
        <article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:160ms">
          <img src="/og-image.png" alt="CloudPilot brand image — logo and tagline on a dark violet gradient" width="1200" height="630" loading="lazy" decoding="async" class="h-28 w-full rounded-2xl object-cover" />
          <h3 class="mt-5 text-lg font-bold">Product imagery</h3>
          <p class="mt-1.5 text-sm leading-relaxed text-neutral-600">Key art and social sharing image (1200 × 630). For product screenshots, see the interactive product tour.</p>
          <div class="mt-5 flex flex-wrap gap-2">
            <a href="/og-image.png" download="cloudpilot-og-image.png" class="inline-flex min-h-11 items-center gap-2 rounded-full bg-violet-600 px-5 text-sm font-bold text-white hover:bg-violet-700"><Download class="h-4 w-4" /> Download PNG</a>
            <NuxtLink to="/product-tour" class="inline-flex min-h-11 items-center rounded-full border border-neutral-300 px-5 text-sm font-bold hover:border-violet-600 hover:text-violet-700">View product tour</NuxtLink>
          </div>
        </article>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 pb-14 sm:px-6">
      <div class="grid gap-5 lg:grid-cols-2">
        <div class="reveal rounded-3xl bg-black p-8 text-white sm:p-10">
          <h2 class="text-2xl font-extrabold tracking-tight sm:text-3xl">Talk to the press team</h2>
          <p class="mt-3 max-w-md text-sm leading-relaxed text-neutral-300">Interview requests, embargoed news, founder quotes and review accounts — we reply within one business day.</p>
          <div class="mt-6 flex flex-wrap items-center gap-3">
            <a href="mailto:press@cloudpilot.app" class="inline-flex min-h-11 items-center gap-2 rounded-full bg-white px-5 text-sm font-bold text-black hover:bg-violet-200"><Mail class="h-4 w-4" /> press@cloudpilot.app</a>
            <NuxtLink to="/contact" class="inline-flex min-h-11 items-center rounded-full border border-white/30 px-5 text-sm font-bold hover:bg-white/10">Contact form</NuxtLink>
          </div>
        </div>
        <div class="reveal rounded-3xl border border-neutral-200 bg-white p-8 sm:p-10" style="--d:80ms">
          <h2 class="text-2xl font-extrabold tracking-tight sm:text-3xl">About CloudPilot</h2>
          <p class="mt-3 text-sm leading-relaxed text-neutral-600">CloudPilot is the all-in-one platform that helps teams simplify, automate and scale their work. FlowMaster automates workflows, InsightPro turns data into decisions, and TeamSync keeps everyone collaborating in real time — so teams replace five tools with one. CloudPilot serves more than 12,500 teams in 140+ countries, from startups to enterprises.</p>
          <p class="mt-4 text-sm leading-relaxed text-neutral-600">Founded in 2024, CloudPilot is a remote-first company. All copy, statistics and coverage on this page are demo content for preview.</p>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-7xl px-4 pb-16 sm:px-6">
      <div class="reveal rounded-3xl bg-gradient-to-r from-violet-700 via-violet-600 to-fuchsia-600 px-6 py-12 text-center text-white sm:px-12">
        <h2 class="text-3xl font-extrabold tracking-tight sm:text-4xl">Ready to simplify, automate and scale?</h2>
        <p class="mx-auto mt-3 max-w-xl text-violet-100">Start free for 14 days. No credit card required. Cancel anytime.</p>
        <div class="mt-7 flex flex-wrap justify-center gap-3">
          <NuxtLink to="/signup" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-violet-700">Start Free Trial</NuxtLink>
          <NuxtLink to="/contact" class="rounded-full border border-white/40 px-6 py-3 text-sm font-bold">Talk to Sales</NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>
<script setup lang="ts">
useSeoMeta({
  title: 'Press — CloudPilot',
  description: 'Press releases, media coverage, logos and brand assets for journalists writing about CloudPilot.',
  ogTitle: 'Press — CloudPilot',
  ogDescription: 'Press releases, media coverage, logos and brand assets for journalists writing about CloudPilot.',
  twitterTitle: 'Press — CloudPilot',
  twitterDescription: 'Press releases, media coverage, logos and brand assets for journalists writing about CloudPilot.'
})

// Mock demo data only — no real coverage claims. Outlet names are invented.
const releases = [
  { tag: 'Product', date: 'Nov 2026', title: 'CloudPilot launches TeamSync 2.0 with real-time boards', excerpt: 'The rebuilt TeamSync adds live cursors, instant comments and board automations, so distributed teams plan together without the status meetings.' },
  { tag: 'Milestone', date: 'Oct 2026', title: 'CloudPilot passes 12,500 teams worldwide', excerpt: 'Two years after launch, teams in more than 140 countries run their projects, marketing and sales on CloudPilot — up from 8,000 teams a year ago.' },
  { tag: 'Product', date: 'Sep 2026', title: 'InsightPro adds AI forecasting to every plan', excerpt: 'Forecasts for revenue, churn and capacity now ship on all plans, including Free — no add-on, no setup, trained on your own workspace data.' },
  { tag: 'Company', date: 'Jun 2026', title: 'CloudPilot earns SOC 2 Type II certification', excerpt: 'Independent auditors verified CloudPilot controls across security, availability and confidentiality. The full report is available in the Trust Center.' }
]

const coverage = [
  { quote: 'The rare all-in-one tool that actually replaces three subscriptions.', outlet: 'TechDaily', date: 'Nov 2026' },
  { quote: 'CloudPilot\u2019s automation builder is the fastest we have tested.', outlet: 'SaaS Weekly', date: 'Oct 2026' },
  { quote: 'A clean, fast workspace teams adopt in a day, not a quarter.', outlet: 'The Workflow Journal', date: 'Sep 2026' },
  { quote: 'InsightPro turns scattered metrics into decisions in minutes.', outlet: 'Cloud Review', date: 'Aug 2026' }
]
</script>
