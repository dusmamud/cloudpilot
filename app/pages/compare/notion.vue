<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><Scale class="h-3.5 w-3.5" /> Compare</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">CloudPilot vs <span class="text-grad">Notion.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Notion is a brilliant notebook. CloudPilot is built to run work — with owners, due dates, automations and analytics that chase the work for you.</p>
<div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms"><NuxtLink to="/signup" class="btn btn-white">Try CloudPilot free</NuxtLink><NuxtLink to="/compare" class="btn btn-outline-light">All comparisons</NuxtLink></div>
</div></section>
<section class="mx-auto max-w-5xl px-4 py-14 sm:px-6">
<div class="reveal overflow-x-auto rounded-3xl border border-neutral-200 bg-white"><table class="w-full min-w-[560px] text-left text-sm"><thead><tr class="border-b border-neutral-200"><th class="px-5 py-4 font-bold">Capability</th><th class="bg-violet-50 px-5 py-4 font-bold text-violet-800">CloudPilot</th><th class="px-5 py-4 font-bold">Notion</th></tr></thead><tbody>
<tr v-for="r in rows" :key="r.f" class="border-b border-neutral-100 align-top last:border-0"><td class="px-5 py-4 font-bold">{{r.f}}</td><td class="bg-violet-50/60 px-5 py-4">{{r.cp}}</td><td class="px-5 py-4 text-neutral-600">{{r.x}}</td></tr>
</tbody></table></div>
<div class="reveal mt-10 grid gap-5 sm:grid-cols-3">
<div class="rounded-3xl bg-violet-600 p-6 text-white"><p class="text-3xl font-extrabold">Built to run work</p><p class="mt-1 text-sm text-violet-100">Owners, due dates and automations — not just pages</p></div>
<div class="rounded-3xl border border-neutral-200 bg-white p-6"><p class="text-3xl font-extrabold">Analytics</p><p class="mt-1 text-sm text-neutral-600">InsightPro dashboards — no formulas required</p></div>
<div class="rounded-3xl border border-neutral-200 bg-white p-6"><p class="text-3xl font-extrabold">1-click</p><p class="mt-1 text-sm text-neutral-600">Import Notion pages and databases</p></div>
</div>
<div class="reveal mt-10 rounded-3xl border border-neutral-200 bg-white p-8 text-center"><h2 class="text-2xl font-extrabold">Docs are not a workflow</h2><p class="mx-auto mt-2 max-w-xl text-sm leading-relaxed text-neutral-600">Notion pages don't remind anyone, don't escalate, and don't report. CloudPilot keeps the flexibility of a doc with the discipline of a workflow engine.</p><NuxtLink to="/signup" class="btn btn-violet mt-5">Start free trial <ArrowRight class="h-4 w-4" /></NuxtLink></div>
</section>
</div></template>
<script setup lang="ts">
useSeoMeta({ title: 'CloudPilot vs Notion — CloudPilot', description: 'CloudPilot vs Notion: a workflow platform with owners, due dates, automations and analytics — not just pages.' })
const rows = [
{ f: 'Docs & wikis', cp: 'Rich docs with tasks embedded', x: 'Best-in-class docs and wikis' },
{ f: 'Task ownership & due dates', cp: 'First-class, with reminders', x: 'Possible via databases, manual setup' },
{ f: 'Automations', cp: 'Unlimited rules on Pro', x: 'Basic automations on paid plans' },
{ f: 'Analytics & reporting', cp: 'InsightPro dashboards included', x: 'Charts via formulas; no native dashboards' },
{ f: 'Real-time collaboration', cp: 'TeamSync threads on every task', x: 'Comments on pages' },
{ f: 'Starting price (per user / mo)', cp: '$0 free, $19 Pro', x: '$0 free, $10 Plus, $20 Business' },
]
</script>
