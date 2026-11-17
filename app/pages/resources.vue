<template>
  <div>
    <section class="bg-black text-white">
      <div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300">Resources</p>
        <h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Learn, then <span class='text-grad'>ship faster.</span></h1>
        <p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Practical guides written by the team that builds CloudPilot — not generic AI listicles.</p>
        <div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms">
          <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-black hover:bg-violet-200">Start Free Trial</NuxtLink>
          <NuxtLink to="/pricing" class="rounded-full border border-white/30 px-6 py-3 text-sm font-bold hover:bg-white/10">See Pricing</NuxtLink>
        </div>
      </div>
    </section>
    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3"><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:0ms"><h3 class="text-lg font-bold">The Automation Playbook</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">21 workflows every ops team should automate first.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:80ms"><h3 class="text-lg font-bold">ROI Calculator</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">Work out what automation saves your team, in minutes.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:160ms"><h3 class="text-lg font-bold">Template Library</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">120+ ready-made flows for sales, support and ops.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:240ms"><h3 class="text-lg font-bold">Migration Guide</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">Move from spreadsheets and five tools to one, in a week.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:320ms"><h3 class="text-lg font-bold">Webinars</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">Live every Thursday: automation clinic with our team.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:400ms"><h3 class="text-lg font-bold">API Docs</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">REST + webhooks, with examples in curl, Python and JS.</p></article></div></section>
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
useSeoMeta({ title: 'Resources — CloudPilot', description: 'Guides, templates and calculators.' })

</script>
