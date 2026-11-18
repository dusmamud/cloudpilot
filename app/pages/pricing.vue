<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6"><p class="reveal inline-flex rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300">Pricing</p><h1 class="reveal mt-5 max-w-2xl text-4xl font-extrabold sm:text-5xl">Simple pricing, <span class="text-grad">no surprises.</span></h1><p class="reveal mt-4 max-w-xl text-neutral-300">Start free. Upgrade when your team grows. Prices in USD, per user per month.</p>
<div class="reveal mt-8 inline-flex rounded-full border border-white/25 p-1 text-sm font-semibold"><button @click="yearly=false" :class="!yearly?'bg-white text-black rounded-full px-4 py-2.5 min-h-11':'px-4 py-2.5 min-h-11'">Monthly</button><button @click="yearly=true" :class="yearly?'bg-white text-black rounded-full px-4 py-2.5 min-h-11':'px-4 py-2.5 min-h-11'">Yearly −20%</button></div></div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 lg:grid-cols-3">
<div v-for="(p,i) in plans" :key="p.name" class="reveal card-hover rounded-3xl border p-7" :class="p.hot?'border-violet-600 bg-violet-50 shadow-xl':'border-neutral-200 bg-white'" :style="`--d:${i*90}ms`">
<p class="text-sm font-bold uppercase tracking-wider text-violet-700">{{p.name}}</p><p class="mt-3 text-5xl font-extrabold">${{ yearly ? p.yearly : p.monthly }}<span class="text-base font-medium text-neutral-600">/user/mo</span></p><p class="mt-2 text-sm text-neutral-600">{{p.desc}}</p>
<ul class="mt-6 space-y-2.5 text-sm"><li v-for="f in p.feats" :key="f" class="flex gap-2"><Check class="mt-0.5 h-4 w-4 shrink-0 text-violet-600" />{{f}}</li></ul>
<NuxtLink to="/request-demo" class="mt-7 block rounded-full bg-black py-3 text-center text-sm font-bold text-white hover:bg-violet-700">{{p.cta}}</NuxtLink></div>
</div><p class="mt-6 text-center text-xs text-neutral-500">All prices are demo/mock data. Taxes may apply. Cancel anytime.</p></section>
</div></template>
<script setup lang="ts">
useSeoMeta({title:'Pricing — CloudPilot',description:'Simple CloudPilot pricing: Starter free, Growth $19, Scale $49 per user per month.'})
const yearly=ref(true)
const plans=[
{name:'Starter',monthly:0,yearly:0,desc:'For small teams getting started.',cta:'Start Free',feats:['Up to 5 users','FlowMaster — 5 active flows','TeamSync boards','Community support']},
{name:'Growth',monthly:19,yearly:15,desc:'For teams that want to automate properly.',cta:'Start 14-Day Trial',feats:['Unlimited users & flows','InsightPro analytics','100+ integrations','Priority support','Guest access'],hot:true},
{name:'Scale',monthly:49,yearly:39,desc:'For companies that need control.',cta:'Talk to Sales',feats:['Everything in Growth','SSO, SCIM & audit logs','EU data residency','99.99% uptime SLA','Named success manager']}]
</script>
