<template>
  <div>
    <section class="bg-black text-white">
      <div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-violet-300">Changelog</p>
        <h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">What shipped <span class='text-grad'>lately.</span></h1>
        <p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Every release, in plain language. No marketing fluff.</p>
        <div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms">
          <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-black hover:bg-violet-200">Start Free Trial</NuxtLink>
          <NuxtLink to="/pricing" class="rounded-full border border-white/30 px-6 py-3 text-sm font-bold hover:bg-white/10">See Pricing</NuxtLink>
        </div>
      </div>
    </section>
    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3"><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:0ms"><h3 class="text-lg font-bold">v2.4 — Nov 2026</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">AI workflow suggestions, faster dashboards, and a new mobile approvals inbox.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:80ms"><h3 class="text-lg font-bold">v2.3 — Oct 2026</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">InsightPro alerts, 12 new integrations, and bulk editing for boards.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:160ms"><h3 class="text-lg font-bold">v2.2 — Sep 2026</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">TeamSync threaded comments, guest access, and SOC 2 renewal.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:240ms"><h3 class="text-lg font-bold">v2.1 — Aug 2026</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">FlowMaster templates library, CSV import v2, and dark mode.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:320ms"><h3 class="text-lg font-bold">v2.0 — Jul 2026</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">The all-in-one relaunch: FlowMaster, InsightPro and TeamSync in one app.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:400ms"><h3 class="text-lg font-bold">v1.9 — Jun 2026</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">Performance: dashboards load 40% faster on mobile.</p></article></div></section>
    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6">
      <div class="reveal rounded-3xl bg-gradient-to-r from-violet-700 via-violet-600 to-fuchsia-600 px-6 py-12 text-center text-white sm:px-12">
        <h2 class="text-3xl font-extrabold tracking-tight sm:text-4xl">Ready to simplify, automate and scale?</h2>
        <p class="mx-auto mt-3 max-w-xl text-violet-100">Start free for 14 days. No credit card required. Cancel anytime.</p>
        <div class="mt-7 flex flex-wrap justify-center gap-3">
          <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-violet-700">Start Free Trial</NuxtLink>
          <NuxtLink to="/contact" class="rounded-full border border-white/40 px-6 py-3 text-sm font-bold">Talk to Sales</NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>
<script setup lang="ts">
useSeoMeta({ title: 'Changelog — CloudPilot', description: 'What is new in CloudPilot.' })

</script>
