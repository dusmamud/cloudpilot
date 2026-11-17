<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><HelpCircle class="h-3.5 w-3.5" /> FAQ</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Questions, <span class="text-grad">answered.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Everything buyers and new users ask us most. Still stuck? The Help Center has step-by-step guides.</p>
<div class="reveal mt-8 flex flex-wrap gap-2" style="--d:240ms"><button v-for="c in cats" :key="c" class="min-h-11 rounded-full px-5 text-sm font-bold transition" :class="cat===c?'bg-white text-black':'border border-white/30 text-white hover:bg-white/10'" @click="cat=c; open=-1">{{c}}</button></div>
</div></section>
<section class="mx-auto max-w-4xl px-4 py-14 sm:px-6"><div class="space-y-3">
<article v-for="(q,i) in shown" :key="q.q" class="reveal overflow-hidden rounded-2xl border border-neutral-200 bg-white">
<button class="flex min-h-14 w-full items-center justify-between gap-4 px-5 py-4 text-left text-sm font-bold sm:text-base" :aria-expanded="open===i" @click="open=open===i?-1:i">{{q.q}}<component :is="open===i?Minus:Plus" class="h-5 w-5 shrink-0 text-violet-600" /></button>
<AnimatePresence><Motion v-if="open===i" :initial="{height:0,opacity:0}" :animate="{height:'auto',opacity:1}" :exit="{height:0,opacity:0}" :transition="{duration:0.25,ease:'easeInOut'}" class="overflow-hidden"><p class="px-5 pb-5 text-sm leading-relaxed text-neutral-600">{{q.a}}</p></Motion></AnimatePresence>
</article>
</div>
<div class="reveal mt-10 rounded-3xl bg-violet-600 p-8 text-center text-white"><h2 class="text-2xl font-extrabold">Didn't find your answer?</h2><p class="mt-2 text-sm text-violet-100">Our team replies within one business day.</p><div class="mt-5 flex flex-wrap justify-center gap-3"><NuxtLink to="/help" class="btn btn-white">Visit Help Center</NuxtLink><NuxtLink to="/contact" class="btn btn-outline-light">Contact us</NuxtLink></div></div>
</section>
</div></template>
<script setup lang="ts">
import { Minus, Plus } from '@lucide/vue'
useSeoMeta({ title: 'FAQ — CloudPilot', description: 'Frequently asked questions about CloudPilot pricing, trial, security and integrations.' })
useHead({ script: [{ type: 'application/ld+json', innerHTML: JSON.stringify({ '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: [{ '@type': 'Question', name: 'Is there a free trial?', acceptedAnswer: { '@type': 'Answer', text: 'Yes. Every plan starts with a 14-day free trial. No credit card required.' } }, { '@type': 'Question', name: 'Can I cancel anytime?', acceptedAnswer: { '@type': 'Answer', text: 'Yes. Cancel in two clicks from billing settings; you keep access until the period ends.' } }] }) }] })
const cats = ['All', 'Getting started', 'Billing', 'Security', 'Integrations']
const cat = ref('All')
const open = ref(0)
const all = [
{ c: 'Getting started', q: 'Is there a free trial?', a: 'Yes. Every plan starts with a 14-day free trial with full Pro features. No credit card is required to start, and you can cancel in two clicks.' },
{ c: 'Getting started', q: 'How long does setup take?', a: 'Most teams are running in under an hour. Import from Asana, Monday or a CSV, connect Slack and Gmail, and your first workflow is live the same day.' },
{ c: 'Getting started', q: 'Do you offer a demo?', a: 'Yes — book a 30-minute guided demo from the Request Demo page, or take the self-serve Product Tour to click through the product yourself.' },
{ c: 'Billing', q: 'Can I cancel anytime?', a: 'Yes. Cancel from billing settings in two clicks. You keep access until the end of the paid period, and your data stays exportable for 90 days.' },
{ c: 'Billing', q: 'What payment methods do you accept?', a: 'All major cards, plus invoicing and bank transfer on Enterprise. Prices are in USD and exclude local taxes.' },
{ c: 'Billing', q: 'Do you offer discounts for nonprofits or education?', a: 'Yes — registered nonprofits and schools get 50% off all paid plans. Contact sales with your registration documents.' },
{ c: 'Security', q: 'Is my data safe with CloudPilot?', a: 'Data is encrypted in transit (TLS 1.3) and at rest (AES-256), hosted in SOC 2 Type II audited infrastructure. See the Trust Center for certifications, subprocessors and our DPA.' },
{ c: 'Security', q: 'Do you support SSO and SCIM?', a: 'Yes. SSO with Google, Okta and Entra ID is on Pro and Enterprise; SCIM user provisioning is available on Enterprise.' },
{ c: 'Integrations', q: 'Which tools does CloudPilot connect to?', a: '100+ native integrations including Slack, Salesforce, Gmail, HubSpot, GitHub, Zoom and Stripe — plus a REST API and webhooks for everything else.' },
{ c: 'Integrations', q: 'Can I build a custom integration?', a: 'Yes. The public API covers flows, tasks, users and analytics, with JavaScript, Python and Go SDKs. See the Developers page.' },
]
const shown = computed(() => cat.value === 'All' ? all : all.filter(q => q.c === cat.value))
</script>
