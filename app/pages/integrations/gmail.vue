<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<div class="reveal flex items-center gap-4"><span class="grid h-16 w-16 place-items-center rounded-3xl bg-gradient-to-br from-red-500 to-rose-500"><Mail class="h-8 w-8 text-white" /></span><div><p class="text-xs font-bold uppercase tracking-wider text-violet-300">Integration</p><h1 class="mt-1 text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl">CloudPilot × <span class="text-grad">Gmail</span></h1></div></div>
<p class="reveal mt-6 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:80ms">Turn emails into tasks, send updates from CloudPilot, and never lose a decision to the inbox again.</p>
<div class="reveal mt-8 flex flex-wrap gap-3" style="--d:160ms"><NuxtLink to="/signup" class="btn btn-white">Connect Gmail — free</NuxtLink><NuxtLink to="/integrations" class="btn btn-outline-light">All integrations</NuxtLink></div>
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
<div class="reveal mt-12 rounded-3xl bg-violet-600 p-8 text-center text-white"><h2 class="text-2xl font-extrabold">Your inbox, finally under control</h2><p class="mt-2 text-sm text-violet-100">Every email that needs action becomes a tracked task — nothing slips.</p><NuxtLink to="/signup" class="btn btn-white mt-5">Start free trial</NuxtLink></div>
</section>
</div></template>
<script setup lang="ts">
useSeoMeta({ title: 'Gmail integration — CloudPilot', description: 'Connect CloudPilot to Gmail: turn emails into tasks and send updates without leaving your inbox.' })
const syncs = [
{ t: 'Email → task in one click', d: 'A Gmail add-on turns any email into a task with owner, due date and the thread attached.' },
{ t: 'Send updates from CloudPilot', d: 'Notify stakeholders by email from inside a task — replies thread back automatically.' },
{ t: 'Smart triage', d: 'Rules route emails to the right project: invoices to Finance, bugs to Engineering.' },
{ t: 'Calendar-aware reminders', d: 'Due dates respect your calendar — no reminders during holidays or out-of-office.' },
{ t: 'Full thread history', d: 'Every email about a task stays attached to it, so context never gets lost.' },
{ t: 'Google Workspace SSO', d: 'Sign in with Google and provision the whole team in one step.' },
]
const steps = [
{ t: 'Connect with Google', d: 'From Settings → Integrations, sign in with your Google Workspace account.' },
{ t: 'Install the add-on', d: 'Add the CloudPilot add-on from the Google Workspace Marketplace.' },
{ t: 'Set your rules', d: 'Pick which labels become tasks and who gets notified. Done.' },
]
</script>
