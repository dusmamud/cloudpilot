<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><TrendingUp class="h-3.5 w-3.5" /> Use case</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">A sales pipeline <span class="text-grad">that updates itself.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Health scores, follow-up reminders and close plans — so reps sell and managers forecast, instead of both doing admin.</p>
<div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms"><NuxtLink to="/signup" class="btn btn-white">Start free trial</NuxtLink><NuxtLink to="/integrations/salesforce" class="btn btn-outline-light">See the Salesforce integration</NuxtLink></div>
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
<div class="reveal mt-10 flex flex-wrap gap-3"><span class="text-sm font-bold">Built with:</span><NuxtLink to="/tools/flowmaster" class="rounded-full border border-neutral-300 px-4 py-2 text-sm font-bold hover:border-violet-400 hover:text-violet-700">FlowMaster</NuxtLink><NuxtLink to="/tools/insightpro" class="rounded-full border border-neutral-300 px-4 py-2 text-sm font-bold hover:border-violet-400 hover:text-violet-700">InsightPro</NuxtLink><NuxtLink to="/integrations/salesforce" class="rounded-full border border-neutral-300 px-4 py-2 text-sm font-bold hover:border-violet-400 hover:text-violet-700">Salesforce integration</NuxtLink></div>
</section>
</div></template>
<script setup lang="ts">
useSeoMeta({ title: 'Sales pipeline — CloudPilot', description: 'Run your sales pipeline on CloudPilot: health scores, follow-up reminders and forecasts that update themselves.' })
const pains = [
{ t: 'Deals go quiet', d: 'A deal with no activity for a week is a deal at risk. CloudPilot flags it and reminds the owner before it slips.' },
{ t: 'Forecasts are guesses', d: 'Managers add up gut feelings. Health scores and stage history turn the forecast into a number you can defend.' },
{ t: 'Admin eats selling time', d: 'Reps update the CRM after every call. Two-way Salesforce sync does it for them, in real time.' },
]
const steps = [
{ t: 'Connect Salesforce', d: 'Two-way sync in one click. Deals, contacts and activities flow both ways automatically.' },
{ t: 'Score every deal', d: 'Health scores combine activity, engagement and stage age — at-risk deals surface themselves.' },
{ t: 'Never miss a follow-up', d: 'FlowMaster creates the next step the moment a call ends, and reminds the rep until it is done.' },
{ t: 'Forecast with confidence', d: 'InsightPro turns the pipeline into a weighted forecast your CFO will actually trust.' },
]
const metrics = [
{ v: 5, s: ' hrs', l: 'saved per rep, every week' },
{ v: 27, s: '%', l: 'higher win rate on scored deals' },
{ v: 92, s: '%', l: 'forecast accuracy at quarter close' },
]
</script>
