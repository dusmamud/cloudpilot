<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6"><p class="reveal inline-flex rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300">Help Center</p><h1 class="reveal mt-5 text-4xl font-extrabold sm:text-5xl">How can we <span class="text-grad">help?</span></h1>
<input v-model="q" placeholder="Search help articles…" class="reveal mt-6 w-full max-w-xl rounded-full border border-white/25 bg-white/10 px-5 py-3 text-sm text-white placeholder:text-neutral-400 outline-none focus:border-violet-400" /></div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
<article v-for="(a,i) in filtered" :key="a.t" class="reveal rounded-3xl border border-neutral-200 p-6" :style="`--d:${i*70}ms`"><p class="text-xs font-bold uppercase tracking-wider text-violet-700">{{a.c}}</p><h2 class="mt-2 text-lg font-bold">{{a.t}}</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">{{a.d}}</p></article>
</div><p v-if="!filtered.length" class="py-10 text-center text-neutral-500">No articles match “{{q}}”. Try “billing”, “SSO” or “flows”.</p></section></div></template>
<script setup lang="ts">
useSeoMeta({title:'Help Center — CloudPilot',description:'Answers to common CloudPilot questions.'})
const q=ref('')
const articles=[
{c:'Getting started',t:'Create your first flow',d:'Connect one tool, pick a template, and test it on real data in under 10 minutes.'},
{c:'Billing',t:'Change or cancel your plan',d:'Settings › Billing. Downgrades apply at the next cycle; exports stay available for 30 days.'},
{c:'Security',t:'Set up SSO and SCIM',d:'SAML and OIDC are on Scale. Add your IdP in Settings › Security, then test with one user.'},
{c:'Flows',t:'Why did my flow not run?',d:'Check the run log first — 9 times out of 10 a trigger condition or a disconnected tool is the cause.'},
{c:'Integrations',t:'Connect Slack in one click',d:'Integrations › Slack › Authorise. No admin token needed for the basic connection.'},
{c:'Account',t:'Invite teammates and guests',d:'Invite by email from Settings › Members. Guests are free on Growth and Scale.'}]
const filtered=computed(()=>{const s=q.value.trim().toLowerCase(); return s? articles.filter(a=>(a.t+a.d+a.c).toLowerCase().includes(s)) : articles})
</script>
