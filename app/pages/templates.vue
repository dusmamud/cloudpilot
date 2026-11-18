<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><LayoutGrid class="h-3.5 w-3.5" /> Templates</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Start from a template, <span class="text-grad">not a blank page.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Ready-made workflows, dashboards and boards built by the CloudPilot team. One click copies them into your workspace.</p>
<div class="reveal mt-8 flex flex-wrap gap-2" style="--d:240ms"><button v-for="c in cats" :key="c" class="min-h-11 rounded-full px-5 text-sm font-bold transition" :class="cat===c?'bg-white text-black':'border border-white/30 text-white hover:bg-white/10'" @click="cat=c">{{c}}</button></div>
</div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
<article v-for="t in shown" :key="t.name" class="reveal card-hover flex flex-col rounded-3xl border border-neutral-200 bg-white p-6">
<span class="grid h-12 w-12 place-items-center rounded-2xl bg-violet-100 text-violet-700"><component :is="t.icon" class="h-6 w-6" /></span>
<h2 class="mt-4 text-lg font-bold">{{t.name}}</h2><p class="mt-2 flex-1 text-sm leading-relaxed text-neutral-600">{{t.desc}}</p>
<p class="mt-4 text-xs font-semibold uppercase tracking-wider text-neutral-600">{{t.cat}} · Used by {{t.uses}} teams</p>
<NuxtLink to="/signup" class="btn btn-outline-dark mt-4 w-full">Use template <ArrowRight class="h-4 w-4" /></NuxtLink>
</article>
</div>
<p v-if="!shown.length" class="py-10 text-center text-sm text-neutral-500">No templates in this category yet.</p>
</section>
</div></template>
<script setup lang="ts">
import { Workflow, BarChart3, Users, Rocket, Megaphone, Briefcase, Calendar, Target, HeartHandshake, TrendingUp } from '@lucide/vue'
useSeoMeta({ title: 'Templates — CloudPilot', description: 'Ready-made workflow, dashboard and board templates. One click copies them into your workspace.' })
const cats = ['All', 'Project', 'Marketing', 'Sales', 'People']
const cat = ref('All')
const all = [
{ cat: 'Project', name: 'Product launch plan', desc: 'Every task from announcement to retro, with owners and due dates pre-filled.', uses: '2,400', icon: Rocket },
{ cat: 'Project', name: 'Sprint board', desc: 'Two-week sprints with backlog, in-progress and review columns plus velocity tracking.', uses: '3,100', icon: Workflow },
{ cat: 'Project', name: 'Bug triage flow', desc: 'Auto-assign, prioritise and escalate bugs with severity rules built in.', uses: '1,800', icon: Target },
{ cat: 'Marketing', name: 'Campaign tracker', desc: 'Channels, budgets, assets and results in one dashboard your whole team can read.', uses: '2,900', icon: Megaphone },
{ cat: 'Marketing', name: 'Content calendar', desc: 'Plan, draft, review and publish — with approvals and a publishing checklist.', uses: '2,200', icon: Calendar },
{ cat: 'Marketing', name: 'SEO dashboard', desc: 'Rankings, traffic and content gaps, refreshed daily from your analytics.', uses: '1,500', icon: BarChart3 },
{ cat: 'Sales', name: 'Sales pipeline', desc: 'Stages, health scores and follow-up reminders that keep deals moving.', uses: '3,600', icon: TrendingUp },
{ cat: 'Sales', name: 'Customer onboarding', desc: 'A 14-task onboarding flow that fires automatically when a deal closes.', uses: '2,700', icon: HeartHandshake },
{ cat: 'People', name: 'New hire onboarding', desc: 'Day-one checklist, buddy assignments and 30-60-90 goals for every hire.', uses: '1,900', icon: Users },
{ cat: 'People', name: '1:1 meeting notes', desc: 'Shared agendas, action items and a running history for every report.', uses: '1,400', icon: Briefcase },
]
const shown = computed(() => cat.value === 'All' ? all : all.filter(t => t.cat === cat.value))
</script>
