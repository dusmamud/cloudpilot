<template>
  <div>
    <section class="bg-black text-white">
      <div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300">Features</p>
        <h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Everything you need.<br/>Nothing you <span class='text-grad'>don't.</span></h1>
        <p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">FlowMaster automates the busywork, InsightPro turns data into decisions, and TeamSync keeps everyone on the same page — without switching tabs.</p>
        <div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms">
          <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-black hover:bg-violet-200">Start Free Trial</NuxtLink>
          <NuxtLink to="/pricing" class="rounded-full border border-white/30 px-6 py-3 text-sm font-bold hover:bg-white/10">See Pricing</NuxtLink>
        </div>
      </div>
    </section>
    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3"><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:0ms"><h2 class="text-lg font-bold">Workflow Automation</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">Drag-and-drop flows that route approvals, send reminders and sync tools — no code needed.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:80ms"><h2 class="text-lg font-bold">Advanced Analytics</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">Live dashboards, custom reports and alerts that tell you what changed and why.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:160ms"><h2 class="text-lg font-bold">Team Collaboration</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">Comments, mentions, shared boards and real-time editing built for distributed teams.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:240ms"><h2 class="text-lg font-bold">Integrations</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">100+ native integrations with Slack, Salesforce, Gmail, HubSpot and more.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:320ms"><h2 class="text-lg font-bold">Security & Permissions</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">SSO, SCIM, granular roles and audit logs on every plan above Starter.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:400ms"><h2 class="text-lg font-bold">Mobile Apps</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">iOS and Android apps so approvals and updates never wait for a desk.</p></article></div></section><section class="mx-auto max-w-7xl px-4 pb-14 sm:px-6"><div class="grid gap-4 sm:grid-cols-2"><div class="reveal flex gap-3 rounded-2xl bg-violet-50 p-5" style="--d:0ms"><span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-violet-600 text-white"><Check class="h-4 w-4" /></span><p class="text-sm font-medium leading-relaxed">Set up in under 10 minutes</p></div><div class="reveal flex gap-3 rounded-2xl bg-violet-50 p-5" style="--d:60ms"><span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-violet-600 text-white"><Check class="h-4 w-4" /></span><p class="text-sm font-medium leading-relaxed">No credit card for the free trial</p></div><div class="reveal flex gap-3 rounded-2xl bg-violet-50 p-5" style="--d:120ms"><span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-violet-600 text-white"><Check class="h-4 w-4" /></span><p class="text-sm font-medium leading-relaxed">Cancel anytime, export anytime</p></div></div></section>
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
useSeoMeta({ title: 'Features — CloudPilot', description: 'Every tool your team needs, in one place.' })

</script>
