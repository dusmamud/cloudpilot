<template>
  <div>
    <section class="bg-black text-white">
      <div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300">How it works</p>
        <h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Live in <span class='text-grad'>three steps.</span></h1>
        <p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">No consultants, no six-week onboarding. Connect your tools, pick a template, and watch CloudPilot do the repetitive work.</p>
        <div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms">
          <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-black hover:bg-violet-200">Start Free Trial</NuxtLink>
          <NuxtLink to="/pricing" class="rounded-full border border-white/30 px-6 py-3 text-sm font-bold hover:bg-white/10">See Pricing</NuxtLink>
        </div>
      </div>
    </section>
    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3"><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:0ms"><h2 class="text-lg font-bold">1 — Connect</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">Link Slack, Gmail, Salesforce and your calendar in one click. OAuth only, no passwords stored.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:80ms"><h2 class="text-lg font-bold">2 — Automate</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">Choose a template or build a flow in the visual editor. Test it on real data before you switch it on.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:160ms"><h2 class="text-lg font-bold">3 — Scale</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">Watch the dashboard, set alerts, and let your team focus on work only humans can do.</p></article></div></section><section class="mx-auto max-w-7xl px-4 pb-14 sm:px-6"><div class="grid gap-4 sm:grid-cols-2"><div class="reveal flex gap-3 rounded-2xl bg-violet-50 p-5" style="--d:0ms"><span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-violet-600 text-white"><Check class="h-4 w-4" /></span><p class="text-sm font-medium leading-relaxed">Average setup time: 9 minutes</p></div><div class="reveal flex gap-3 rounded-2xl bg-violet-50 p-5" style="--d:60ms"><span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-violet-600 text-white"><Check class="h-4 w-4" /></span><p class="text-sm font-medium leading-relaxed">120+ ready-made templates</p></div><div class="reveal flex gap-3 rounded-2xl bg-violet-50 p-5" style="--d:120ms"><span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-violet-600 text-white"><Check class="h-4 w-4" /></span><p class="text-sm font-medium leading-relaxed">Free migration help on Growth and Scale</p></div></div></section>
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
useSeoMeta({ title: 'How It Works — CloudPilot', description: 'From signup to first automation in three steps.' })

</script>
