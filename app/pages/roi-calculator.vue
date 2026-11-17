<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6"><p class="reveal inline-flex rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300">ROI Calculator</p><h1 class="reveal mt-5 max-w-2xl text-4xl font-extrabold sm:text-5xl">What is automation <span class="text-grad">worth to you?</span></h1><p class="reveal mt-4 max-w-xl text-neutral-300">Move the sliders. The maths is live — and deliberately conservative.</p></div></section>
<section class="mx-auto max-w-3xl px-4 py-14 sm:px-6"><div class="reveal rounded-3xl border border-neutral-200 p-6 sm:p-8">
<label class="block text-sm font-bold">Team size: {{team}} people</label><input v-model.number="team" type="range" min="5" max="500" class="w-full accent-violet-600" />
<label class="mt-6 block text-sm font-bold">Manual hours per person per week: {{hours}}</label><input v-model.number="hours" type="range" min="1" max="20" class="w-full accent-violet-600" />
<label class="mt-6 block text-sm font-bold">Average hourly cost: ${{rate}}</label><input v-model.number="rate" type="range" min="20" max="150" step="5" class="w-full accent-violet-600" />
<div class="mt-8 grid gap-4 text-center sm:grid-cols-3">
<div class="rounded-2xl bg-violet-50 p-5"><p class="text-3xl font-extrabold text-violet-700">${{saved.toLocaleString()}}</p><p class="mt-1 text-xs font-medium text-neutral-500">Saved per year*</p></div>
<div class="rounded-2xl bg-violet-50 p-5"><p class="text-3xl font-extrabold text-violet-700">{{hrsSaved.toLocaleString()}}</p><p class="mt-1 text-xs font-medium text-neutral-500">Hours saved per year</p></div>
<div class="rounded-2xl bg-violet-50 p-5"><p class="text-3xl font-extrabold text-violet-700">{{payback}} days</p><p class="mt-1 text-xs font-medium text-neutral-500">Payback period</p></div></div>
<p class="mt-4 text-xs text-neutral-500">*Assumes CloudPilot automates 60% of manual hours, at Growth pricing. Demo calculator — your mileage will vary.</p>
<NuxtLink to="/request-demo" class="mt-6 block rounded-full bg-black py-3 text-center text-sm font-bold text-white">Start Free Trial</NuxtLink>
</div></section></div></template>
<script setup lang="ts">
useSeoMeta({title:'ROI Calculator — CloudPilot',description:'Work out what workflow automation saves your team.'})
const team=ref(25), hours=ref(6), rate=ref(50)
const hrsSaved=computed(()=> Math.round(team.value*hours.value*0.6*52))
const saved=computed(()=> hrsSaved.value*rate.value)
const payback=computed(()=> Math.max(1, Math.round(15*12*team.value*12 / Math.max(1,saved.value) * 365)))
</script>
