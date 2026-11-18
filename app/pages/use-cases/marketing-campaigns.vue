<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><Megaphone class="h-3.5 w-3.5" /> Use case</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Marketing campaigns, <span class="text-grad">from brief to results.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Briefs, assets, budgets and results in one place — so the campaign ships on time and you can prove what it returned.</p>
<div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms"><NuxtLink to="/signup" class="btn btn-white">Start free trial</NuxtLink><NuxtLink to="/templates" class="btn btn-outline-light">Browse marketing templates</NuxtLink></div>
</div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6">
<div class="grid gap-5 sm:grid-cols-3">
<div v-for="(p,i) in pains" :key="p.t" class="reveal rounded-3xl border border-neutral-200 bg-white p-6"><p class="text-sm font-bold text-violet-700">Problem {{i+1}}</p><h2 class="mt-2 text-lg font-bold">{{p.t}}</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">{{p.d}}</p></div>
</div>
<h2 class="reveal mt-14 text-3xl font-extrabold">How it works</h2>
<ol class="mt-6 space-y-4">
<li v-for="(s,i) in steps" :key="s.t" class="reveal flex gap-4 rounded-3xl border border-neutral-200 bg-white p-6"><span class="grid h-11 w-11 shrink-0 place-items-center rounded-full bg-violet-100 text-base font-extrabold text-violet-700">{{i+1}}</span><div><h3 class="font-bold">{{s.t}}</h3><p class="mt-1 text-sm leading-relaxed text-neutral-600">{{s.d}}</p></div></li>
</ol>
<div class="reveal mt-12 grid gap-5 rounded-3xl bg-violet-600 p-8 text-white sm:grid-cols-3"><div v-for="m in metrics" :key="m.l"><p class="text-3xl font-extrabold"><CountUp :to="m.v" :suffix="m.s" /></p><p class="mt-1 text-sm text-violet-100">{{m.l}}</p></div></div>
<div class="reveal mt-10 flex flex-wrap gap-3"><span class="text-sm font-bold">Built with:</span><NuxtLink to="/tools/flowmaster" class="rounded-full border border-neutral-300 px-4 py-2 text-sm font-bold hover:border-violet-400 hover:text-violet-700">FlowMaster</NuxtLink><NuxtLink to="/tools/insightpro" class="rounded-full border border-neutral-300 px-4 py-2 text-sm font-bold hover:border-violet-400 hover:text-violet-700">InsightPro</NuxtLink><NuxtLink to="/tools/teamsync" class="rounded-full border border-neutral-300 px-4 py-2 text-sm font-bold hover:border-violet-400 hover:text-violet-700">TeamSync</NuxtLink></div>
</section>
</div></template>
<script setup lang="ts">
useSeoMeta({ title: 'Marketing campaigns — CloudPilot', description: 'Run multi-channel marketing campaigns on CloudPilot: briefs, assets, budgets and results in one dashboard.' })
const pains = [
{ t: 'Assets scattered everywhere', d: 'Designs in Drive, copy in docs, feedback in chat. Every asset lives on its campaign card, with approvals attached.' },
{ t: 'Budgets nobody can see', d: 'Spend hides in spreadsheets. The campaign dashboard shows budget vs actuals, live, for every channel.' },
{ t: 'Results come too late', d: 'You learn what worked after the money is spent. InsightPro alerts you mid-flight when a channel underperforms.' },
]
const steps = [
{ t: 'Brief in one page', d: 'Audience, message, channels and budget — one brief everyone works from.' },
{ t: 'Assets with approvals', d: 'Design and copy move through review automatically. No more chasing sign-offs in chat.' },
{ t: 'Launch on schedule', d: 'FlowMaster schedules every post, ad and email, and nudges owners before deadlines.' },
{ t: 'Measure and repeat', d: 'Channel results roll up into one report. Clone the winners into next quarter in one click.' },
]
const metrics = [
{ v: 8, s: ' hrs', l: 'saved per campaign, per week' },
{ v: 41, s: '%', l: 'higher on-time launch rate' },
{ v: 3.2, s: 'x', l: 'average return on campaign spend' },
]
</script>
