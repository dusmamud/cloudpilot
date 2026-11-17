<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><Play class="h-3.5 w-3.5" /> Product tour</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Click through CloudPilot. <span class="text-grad">No account needed.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">A hands-on tour of the three tools and the automations that tie them together. Pick a step — the product panel below changes live.</p>
</div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6">
<div class="reveal flex flex-wrap gap-2" role="tablist" aria-label="Tour steps">
<button v-for="(s,i) in steps" :key="s.title" role="tab" :aria-selected="step===i" class="flex min-h-12 items-center gap-2 rounded-full px-5 text-sm font-bold transition" :class="step===i?'bg-violet-600 text-white':'border border-neutral-300 bg-white hover:border-violet-400 hover:text-violet-700'" @click="step=i"><component :is="s.icon" class="h-4 w-4" /> {{i+1}}. {{s.title}}</button>
</div>
<AnimatePresence mode="wait"><Motion :key="step" :initial="{opacity:0,y:12}" :animate="{opacity:1,y:0}" :exit="{opacity:0,y:-8}" :transition="{duration:0.25,ease:'easeOut'}" class="mt-8">
<div class="overflow-hidden rounded-3xl border border-neutral-200 bg-white shadow-sm">
<div class="flex items-center gap-2 border-b border-neutral-100 px-5 py-3"><span class="h-3 w-3 rounded-full bg-red-400" /><span class="h-3 w-3 rounded-full bg-amber-400" /><span class="h-3 w-3 rounded-full bg-emerald-400" /><span class="ml-3 text-xs font-bold text-neutral-500">cloudpilot.app / {{steps[step].slug}}</span></div>
<div class="p-5 sm:p-7">
<!-- Step 1: FlowMaster board -->
<div v-if="step===0" class="grid gap-4 sm:grid-cols-3">
<div v-for="col in board" :key="col.name" class="rounded-2xl bg-neutral-50 p-4"><p class="flex items-center justify-between text-xs font-bold uppercase tracking-wider text-neutral-500">{{col.name}}<span class="rounded-full bg-white px-2 py-0.5 text-neutral-700 ring-1 ring-neutral-200">{{col.tasks.length}}</span></p><div class="mt-3 space-y-2"><div v-for="t in col.tasks" :key="t" class="rounded-xl bg-white p-3 text-sm font-medium shadow-sm ring-1 ring-neutral-100">{{t}}</div></div></div>
</div>
<!-- Step 2: InsightPro chart -->
<div v-if="step===1"><div class="flex items-end gap-3 sm:gap-4" style="height:220px"><div v-for="(b,i) in bars" :key="i" class="flex flex-1 flex-col items-center gap-2"><span class="text-xs font-bold text-neutral-700">${{b}}k</span><div class="w-full max-w-16 rounded-t-xl bg-gradient-to-t from-violet-600 to-fuchsia-400 transition-all duration-500" :style="{height:(b*1.6)+'px'}" /></div></div><div class="mt-4 flex flex-wrap gap-6 border-t border-neutral-100 pt-4 text-sm"><span><strong class="text-lg">$48k</strong><br /><span class="text-neutral-500">Revenue this month</span></span><span><strong class="text-lg">+32%</strong><br /><span class="text-neutral-500">vs last month</span></span><span><strong class="text-lg">1.4%</strong><br /><span class="text-neutral-500">Churn, down from 2.1%</span></span></div></div>
<!-- Step 3: TeamSync thread -->
<div v-if="step===2" class="space-y-4">
<div v-for="m in thread" :key="m.who" class="flex gap-3"><img :src="m.img" :alt="m.who" class="h-10 w-10 shrink-0 rounded-full object-cover" /><div class="rounded-2xl rounded-tl-none bg-neutral-50 px-4 py-3 ring-1 ring-neutral-100"><p class="text-sm font-bold">{{m.who}} <span class="ml-1 font-medium text-neutral-400">{{m.when}}</span></p><p class="mt-1 text-sm leading-relaxed text-neutral-600">{{m.text}}</p></div></div>
<div class="flex gap-2"><input v-model="reply" class="h-12 flex-1 rounded-full border border-neutral-300 px-4 text-sm outline-none focus:border-violet-500" placeholder="Write a reply…" @keyup.enter="sendReply" /><button class="btn btn-violet btn-sm" @click="sendReply">Send</button></div>
<p v-if="sent" class="flex items-center gap-2 text-sm font-medium text-emerald-700"><CheckCircle2 class="h-4 w-4" /> Reply posted to the thread (demo).</p>
</div>
<!-- Step 4: Automations -->
<div v-if="step===3" class="space-y-3">
<div v-for="(a,i) in autos" :key="a.name" class="flex items-center justify-between gap-4 rounded-2xl border border-neutral-200 px-4 py-3.5"><div><p class="text-sm font-bold">{{a.name}}</p><p class="text-xs text-neutral-500">{{a.rule}}</p></div><button class="relative h-7 w-12 shrink-0 rounded-full transition" :class="a.on?'bg-violet-600':'bg-neutral-300'" :aria-pressed="a.on" :aria-label="a.name" @click="a.on=!a.on"><span class="absolute top-0.5 h-6 w-6 rounded-full bg-white shadow transition-all" :class="a.on?'left-[22px]':'left-0.5'" /></button></div>
<p class="text-sm text-neutral-500">{{autos.filter(a=>a.on).length}} of {{autos.length}} automations running — they fired <strong class="text-neutral-900">1,284 times</strong> this week.</p>
</div>
</div>
</div>
</Motion></AnimatePresence>
<div class="reveal mt-8 flex flex-wrap items-center justify-between gap-4"><button class="btn btn-outline-dark" :disabled="step===0" @click="step--"><ArrowLeft class="h-4 w-4" /> Previous</button><button v-if="step<3" class="btn btn-dark" @click="step++">Next step <ArrowRight class="h-4 w-4" /></button><NuxtLink v-else to="/signup" class="btn btn-violet">Start free trial <ArrowRight class="h-4 w-4" /></NuxtLink></div>
</section>
</div></template>
<script setup lang="ts">
import { Workflow, BarChart3, Users, Zap } from '@lucide/vue'
useSeoMeta({ title: 'Product tour — CloudPilot', description: 'Click through FlowMaster, InsightPro, TeamSync and automations. No account needed.' })
const step = ref(0)
const steps = [
{ title: 'FlowMaster board', slug: 'flows/onboarding', icon: Workflow },
{ title: 'InsightPro analytics', slug: 'analytics/revenue', icon: BarChart3 },
{ title: 'TeamSync thread', slug: 'teams/product', icon: Users },
{ title: 'Automations', slug: 'automations', icon: Zap },
]
const board = [
{ name: 'To do', tasks: ['Draft Q3 launch plan', 'Review Nimbus contract'] },
{ name: 'Doing', tasks: ['Onboard 3 new hires', 'Prep sales kickoff'] },
{ name: 'Done', tasks: ['Ship v2.4 changelog', 'Migrate to new billing'] },
]
const bars = [18, 26, 22, 34, 30, 44, 52, 48]
const thread = [
{ who: 'Mia Carter', when: '10:24', img: '/images/hero-woman.webp', text: 'The Nimbus onboarding flow is live — FlowMaster created all 14 tasks automatically. Zero manual work.' },
{ who: 'Alex Chen', when: '10:31', img: '/images/avatar-man1.webp', text: 'InsightPro flagged one at-risk deal. I have already messaged the owner.' },
{ who: 'David Park', when: '10:40', img: '/images/avatar-man2.webp', text: 'Resolved in-thread, no meeting needed. This is exactly why we switched.' },
]
const reply = ref('')
const sent = ref(false)
function sendReply() { if (reply.value.trim()) { sent.value = true; reply.value = '' } }
const autos = ref([
{ name: 'New deal → onboarding tasks', rule: 'When a deal closes in Salesforce, create 14 onboarding tasks', on: true },
{ name: 'At-risk deal alert', rule: 'When health score drops below 60, alert the owner in Slack', on: true },
{ name: 'Weekly digest', rule: 'Every Monday 9 AM, email a summary to the whole team', on: false },
{ name: 'Invoice follow-up', rule: '3 days after an invoice is overdue, send a reminder', on: true },
])
</script>
