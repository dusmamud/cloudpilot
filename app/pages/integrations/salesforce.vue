<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<div class="reveal flex items-center gap-4"><span class="grid h-16 w-16 place-items-center rounded-3xl bg-gradient-to-br from-sky-500 to-blue-600"><Cloud class="h-8 w-8 text-white" /></span><div><p class="text-xs font-bold uppercase tracking-wider text-violet-300">Integration</p><h1 class="mt-1 text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl">CloudPilot × <span class="text-grad">Salesforce</span></h1></div></div>
<p class="reveal mt-6 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:80ms">Two-way sync between Salesforce and CloudPilot — deals become work automatically, and work updates the deal.</p>
<div class="reveal mt-8 flex flex-wrap gap-3" style="--d:160ms"><NuxtLink to="/signup" class="btn btn-white">Connect Salesforce — free</NuxtLink><NuxtLink to="/integrations" class="btn btn-outline-light">All integrations</NuxtLink></div>
</div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6">
<h2 class="reveal text-3xl font-extrabold">What syncs</h2>
<div class="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
<div v-for="f in syncs" :key="f.t" class="reveal rounded-3xl border border-neutral-200 bg-white p-6"><CheckCircle2 class="h-6 w-6 text-emerald-600" /><h3 class="mt-3 font-bold">{{f.t}}</h3><p class="mt-1 text-sm leading-relaxed text-neutral-600">{{f.d}}</p></div>
</div>
<h2 class="reveal mt-14 text-3xl font-extrabold">Set up in 3 steps</h2>
<ol class="mt-6 space-y-4">
<li v-for="(s,i) in steps" :key="s.t" class="reveal flex gap-4 rounded-3xl border border-neutral-200 bg-white p-6"><span class="grid h-11 w-11 shrink-0 place-items-center rounded-full bg-violet-100 text-base font-extrabold text-violet-700">{{i+1}}</span><div><h3 class="font-bold">{{s.t}}</h3><p class="mt-1 text-sm leading-relaxed text-neutral-600">{{s.d}}</p></div></li>
</ol>
<div class="reveal mt-12 rounded-3xl bg-violet-600 p-8 text-center text-white"><h2 class="text-2xl font-extrabold">Close the loop between sales and delivery</h2><p class="mt-2 text-sm text-violet-100">Deals, onboarding and delivery — one flow, no re-typing.</p><NuxtLink to="/use-cases/sales-pipeline" class="btn btn-white mt-5">See the sales use case</NuxtLink></div>
</section>
</div></template>
<script setup lang="ts">
useSeoMeta({ title: 'Salesforce integration — CloudPilot', description: 'Two-way Salesforce sync: deals become onboarding work automatically, and work updates the deal.' })
const syncs = [
{ t: 'Deal closed → work starts', d: 'When a deal closes, FlowMaster creates the full onboarding task list automatically.' },
{ t: 'Two-way field sync', d: 'Stage, amount, owner and close date stay identical in both systems, in real time.' },
{ t: 'Health scores on the deal', d: 'CloudPilot health scores show inside Salesforce, so reps see risk early.' },
{ t: 'Activities logged automatically', d: 'Calls, tasks and comments in CloudPilot appear on the Salesforce record.' },
{ t: 'Custom object mapping', d: 'Map any Salesforce object to CloudPilot flows — no code, just field pickers.' },
{ t: 'Sandbox support', d: 'Test the integration in a Salesforce sandbox before going live.' },
]
const steps = [
{ t: 'Connect with OAuth', d: 'From Settings → Integrations, sign in to Salesforce. No API keys to manage.' },
{ t: 'Map your fields', d: 'Pick which objects and fields sync. Defaults work for most teams.' },
{ t: 'Turn on automations', d: 'Enable the deal-closed flow and watch onboarding start itself.' },
]
</script>
