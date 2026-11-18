<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6"><p class="reveal inline-flex rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300">Blog</p><h1 class="reveal mt-5 text-4xl font-extrabold sm:text-5xl">Notes on <span class="text-grad">working smarter.</span></h1><p class="reveal mt-4 max-w-xl text-neutral-300">Guides, playbooks and product news from the CloudPilot team.</p></div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 md:grid-cols-3">
<NuxtLink v-for="(p,i) in posts" :key="p.slug" :to="'/blog/'+p.slug" class="reveal card-hover rounded-3xl border border-neutral-200 p-6" :style="`--d:${i*90}ms`"><p class="text-xs font-bold uppercase tracking-wider text-violet-700">{{p.tag}} · {{p.date}}</p><h2 class="mt-2 text-xl font-bold leading-snug">{{p.t}}</h2><p class="mt-2 text-sm leading-relaxed text-neutral-600">{{p.d}}</p><span class="mt-4 inline-block text-sm font-bold text-violet-700">Read <ArrowRight class="inline h-4 w-4" /></span></NuxtLink>
</div></section></div></template>
<script setup lang="ts">
useSeoMeta({title:'Blog — CloudPilot',description:'Guides and product news from CloudPilot.'})
const posts=[
{slug:'automate-workflows',tag:'Playbook',date:'Nov 2026',t:'21 workflows every ops team should automate first',d:'Start with approvals, renewals and status updates — the three that eat the most time.'},
{slug:'data-driven-decisions',tag:'Analytics',date:'Oct 2026',t:'Data-driven decisions without a data team',d:'You do not need a warehouse. You need alerts that tell you what changed and why.'},
{slug:'remote-team-collaboration',tag:'Teams',date:'Oct 2026',t:'How distributed teams stay in sync without more meetings',d:'Async by default, live when it matters, and one shared board everyone trusts.'}]
</script>
