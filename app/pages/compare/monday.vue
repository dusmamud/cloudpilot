<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><Scale class="h-3.5 w-3.5" /> Compare</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">CloudPilot vs <span class="text-grad">Monday.com.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Monday.com is flexible — and famously fiddly. CloudPilot gives you the same boards with analytics and automations built in, ready on day one.</p>
<div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms"><NuxtLink to="/signup" class="btn btn-white">Try CloudPilot free</NuxtLink><NuxtLink to="/compare" class="btn btn-outline-light">All comparisons</NuxtLink></div>
</div></section>
<section class="mx-auto max-w-5xl px-4 py-14 sm:px-6">
<div class="reveal overflow-x-auto rounded-3xl border border-neutral-200 bg-white"><table class="w-full min-w-[560px] text-left text-sm"><thead><tr class="border-b border-neutral-200"><th class="px-5 py-4 font-bold">Capability</th><th class="bg-violet-50 px-5 py-4 font-bold text-violet-800">CloudPilot</th><th class="px-5 py-4 font-bold">Monday.com</th></tr></thead><tbody>
<tr v-for="r in rows" :key="r.f" class="border-b border-neutral-100 align-top last:border-0"><td class="px-5 py-4 font-bold">{{r.f}}</td><td class="bg-violet-50/60 px-5 py-4">{{r.cp}}</td><td class="px-5 py-4 text-neutral-600">{{r.x}}</td></tr>
</tbody></table></div>
<div class="reveal mt-10 grid gap-5 sm:grid-cols-3">
<div class="rounded-3xl bg-violet-600 p-6 text-white"><p class="text-3xl font-extrabold">Day 1</p><p class="mt-1 text-sm text-violet-100">Ready to use — no board-building project first</p></div>
<div class="rounded-3xl border border-neutral-200 bg-white p-6"><p class="text-3xl font-extrabold">Included</p><p class="mt-1 text-sm text-neutral-600">Analytics and automations on Pro, not add-ons</p></div>
<div class="rounded-3xl border border-neutral-200 bg-white p-6"><p class="text-3xl font-extrabold">1-click</p><p class="mt-1 text-sm text-neutral-600">Import boards from Monday.com in minutes</p></div>
</div>
<div class="reveal mt-10 rounded-3xl border border-neutral-200 bg-white p-8 text-center"><h2 class="text-2xl font-extrabold">Less setup, more shipping</h2><p class="mx-auto mt-2 max-w-xl text-sm leading-relaxed text-neutral-600">Monday.com boards need building before they help. CloudPilot ships with templates for launches, sprints and pipelines — your team starts working, not configuring.</p><NuxtLink to="/signup" class="btn btn-violet mt-5">Start free trial <ArrowRight class="h-4 w-4" /></NuxtLink></div>
</section>
</div></template>
<script setup lang="ts">
useSeoMeta({ title: 'CloudPilot vs Monday.com — CloudPilot', description: 'CloudPilot vs Monday.com: boards plus built-in analytics and automations, ready on day one.' })
const rows = [
{ f: 'Boards & timelines', cp: 'Included on every plan', x: 'Core feature, needs setup' },
{ f: 'Built-in analytics', cp: 'InsightPro dashboards included', x: 'Dashboards are a paid add-on on most plans' },
{ f: 'Automations', cp: 'Unlimited rules on Pro', x: 'Action limits per plan; overage charges apply' },
{ f: 'Real-time collaboration', cp: 'TeamSync threads on every task', x: 'Updates feed; no threaded discussions' },
{ f: 'Free plan', cp: 'Free forever, 3 projects', x: 'Free plan limited to 2 seats' },
{ f: 'Starting price (per user / mo)', cp: '$0 free, $19 Pro', x: '$0 free, $9 Basic, $12 Standard' },
]
</script>
