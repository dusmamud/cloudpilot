<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><Code2 class="h-3.5 w-3.5" /> Developers</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Build on CloudPilot. <span class="text-grad">Ship in an afternoon.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">A REST API, webhooks and SDKs for everything the product does — flows, tasks, users and analytics.</p>
<div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms"><NuxtLink to="/signup" class="btn btn-white">Get an API key</NuxtLink><NuxtLink to="/trust-center" class="btn btn-outline-light">Security &amp; compliance</NuxtLink></div>
</div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6">
<h2 class="reveal text-3xl font-extrabold">Quickstart</h2>
<div class="mt-6 grid gap-5 lg:grid-cols-3">
<div v-for="(s,i) in quick" :key="s.t" class="reveal rounded-3xl border border-neutral-200 bg-white p-6"><span class="grid h-11 w-11 place-items-center rounded-full bg-violet-100 text-base font-extrabold text-violet-700">{{i+1}}</span><h3 class="mt-4 font-bold">{{s.t}}</h3><p class="mt-1 text-sm leading-relaxed text-neutral-600">{{s.d}}</p></div>
</div>
<h2 class="reveal mt-14 text-3xl font-extrabold">Your first API call</h2>
<pre class="reveal mt-6 overflow-x-auto rounded-3xl bg-neutral-950 p-5 text-sm leading-relaxed text-violet-100"><code>curl https://api.cloudpilot.app/v1/flows \
  -H "Authorization: Bearer YOUR_API_KEY"

# → 200 OK
# { "flows": [{ "id": "fl_onboarding",
#   "name": "New hire onboarding",
#   "tasks": 14, "status": "active" }] }</code></pre>
<h2 class="reveal mt-14 text-3xl font-extrabold">Core endpoints</h2>
<div class="reveal mt-6 overflow-x-auto rounded-3xl border border-neutral-200"><table class="w-full min-w-[560px] text-left text-sm"><thead><tr class="border-b border-neutral-200 bg-neutral-50"><th class="px-5 py-3 font-bold">Method</th><th class="px-5 py-3 font-bold">Endpoint</th><th class="px-5 py-3 font-bold">What it does</th></tr></thead><tbody>
<tr v-for="e in endpoints" :key="e.p" class="border-b border-neutral-100 last:border-0"><td class="px-5 py-3"><span class="rounded-full px-2.5 py-1 text-xs font-bold" :class="e.m==='GET'?'bg-emerald-100 text-emerald-800':'bg-violet-100 text-violet-800'">{{e.m}}</span></td><td class="px-5 py-3 font-mono text-xs sm:text-sm">{{e.p}}</td><td class="px-5 py-3 text-neutral-600">{{e.d}}</td></tr>
</tbody></table></div>
<h2 class="reveal mt-14 text-3xl font-extrabold">SDKs &amp; limits</h2>
<div class="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
<div v-for="s in sdks" :key="s.n" class="reveal rounded-3xl border border-neutral-200 bg-white p-6"><component :is="s.icon" class="h-6 w-6 text-violet-600" /><h3 class="mt-3 font-bold">{{s.n}}</h3><p class="mt-1 text-sm text-neutral-600">{{s.d}}</p></div>
</div>
<p class="reveal mt-6 text-sm text-neutral-500">Rate limit: 1,000 requests/minute per key on Pro, 10,000 on Enterprise. Webhooks retry for 24 hours. API versioning: <code class="rounded bg-neutral-100 px-1.5 py-0.5 font-mono text-xs">/v1</code> is stable; breaking changes ship as <code class="rounded bg-neutral-100 px-1.5 py-0.5 font-mono text-xs">/v2</code>.</p>
</section>
</div></template>
<script setup lang="ts">
import { KeyRound, Webhook, Gauge, BookOpen, Code2 } from '@lucide/vue'
useSeoMeta({ title: 'Developers — CloudPilot API', description: 'CloudPilot REST API, webhooks and SDKs. Build on flows, tasks, users and analytics.' })
const quick = [
{ t: 'Get an API key', d: 'Sign up, open Settings → API, and create a key. Keys are scoped per workspace and can be revoked anytime.' },
{ t: 'Make your first call', d: 'List your flows with one curl command. Every response is JSON, every error explains itself.' },
{ t: 'Subscribe to webhooks', d: 'Get task.completed, deal.closed and alert.fired events pushed to your endpoint in real time.' },
]
const endpoints = [
{ m: 'GET', p: '/v1/flows', d: 'List all workflows in the workspace' },
{ m: 'POST', p: '/v1/flows', d: 'Create a workflow from a template' },
{ m: 'GET', p: '/v1/tasks', d: 'List tasks, filter by owner, status or due date' },
{ m: 'POST', p: '/v1/tasks', d: 'Create a task and assign it' },
{ m: 'GET', p: '/v1/analytics/revenue', d: 'Revenue, churn and activity metrics' },
{ m: 'POST', p: '/v1/webhooks', d: 'Register a webhook subscription' },
]
const sdks = [
{ n: 'JavaScript / TypeScript', d: 'npm i @cloudpilot/sdk — typed client, ESM + CJS.', icon: Code2 },
{ n: 'Python', d: 'pip install cloudpilot — async client included.', icon: BookOpen },
{ n: 'Go', d: 'go get github.com/cloudpilot/sdk-go', icon: Gauge },
{ n: 'Webhooks', d: 'Signed events with HMAC verification.', icon: Webhook },
]
</script>
