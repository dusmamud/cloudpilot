<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><Target class="h-3.5 w-3.5" /> Use cases</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">One platform, <span class="text-grad">every job.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Pick the work you do most. Each use case shows the exact workflow, the tools involved and the time it saves.</p>
</div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
<NuxtLink v-for="u in cases" :key="u.to" :to="u.to" class="reveal card-hover group block rounded-3xl border border-neutral-200 bg-white p-6">
<span class="grid h-12 w-12 place-items-center rounded-2xl bg-violet-100 text-violet-700"><component :is="u.icon" class="h-6 w-6" /></span>
<h3 class="mt-4 text-lg font-bold group-hover:text-violet-700">{{u.name}}</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">{{u.desc}}</p>
<p class="mt-4 text-sm font-bold text-violet-700">Saves {{u.saves}} <ArrowRight class="inline h-4 w-4 transition group-hover:translate-x-1" /></p>
</NuxtLink>
</div>
<div class="reveal mt-10 rounded-3xl bg-violet-600 p-8 text-center text-white"><h2 class="text-2xl font-extrabold">Don't see your use case?</h2><p class="mt-2 text-sm text-violet-100">CloudPilot is flexible — build any workflow with FlowMaster, or ask us.</p><div class="mt-5 flex flex-wrap justify-center gap-3"><NuxtLink to="/product-tour" class="btn btn-white">Take the product tour</NuxtLink><NuxtLink to="/contact" class="btn btn-outline-light">Talk to us</NuxtLink></div></div>
</section>
</div></template>
<script setup lang="ts">
import { Workflow, Megaphone, TrendingUp } from '@lucide/vue'
useSeoMeta({ title: 'Use cases — CloudPilot', description: 'See how teams use CloudPilot for project management, marketing campaigns and sales pipelines.' })
const cases = [
{ to: '/use-cases/project-management', name: 'Project management', desc: 'Plan, assign and ship work without the status meetings. Boards, timelines and automations included.', saves: '6 hrs / week', icon: Workflow },
{ to: '/use-cases/marketing-campaigns', name: 'Marketing campaigns', desc: 'Run multi-channel campaigns from one dashboard — briefs, assets, budgets and results.', saves: '8 hrs / week', icon: Megaphone },
{ to: '/use-cases/sales-pipeline', name: 'Sales pipeline', desc: 'A pipeline that updates itself: health scores, follow-up reminders and close plans.', saves: '5 hrs / week', icon: TrendingUp },
]
</script>
