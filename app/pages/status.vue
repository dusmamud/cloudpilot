<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-emerald-300"><span class="h-2 w-2 rounded-full bg-emerald-400" /> All systems operational</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">CloudPilot <span class="text-grad">status.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Live service health, 90-day uptime and incident history. Updated every minute. Demo data.</p>
</div></section>
<section class="mx-auto max-w-4xl px-4 py-14 sm:px-6">
<div class="space-y-3">
<div v-for="s in services" :key="s.n" class="reveal flex items-center justify-between gap-4 rounded-2xl border border-neutral-200 bg-white px-5 py-4"><span class="flex items-center gap-3 text-sm font-bold"><span class="h-2.5 w-2.5 rounded-full" :class="s.ok?'bg-emerald-500':'bg-amber-400'" /> {{s.n}}</span><span class="text-sm text-neutral-500">{{s.u}}% uptime · {{s.ok?'Operational':'Degraded'}}</span></div>
</div>
<h2 class="reveal mt-12 text-2xl font-extrabold">Uptime — last 90 days</h2>
<div class="reveal mt-4 flex h-16 items-end gap-[3px]" role="img" aria-label="90-day uptime chart, 99.99 percent">
<div v-for="(d,i) in days" :key="i" class="flex-1 rounded-sm" :class="d===2?'bg-amber-400':d===1?'bg-emerald-300':'bg-emerald-500'" :style="{height:(d===2?55:d===1?80:100)+'%'}" :title="'Day '+(i+1)+(d===2?' — partial outage':d===1?' — minor degradation':' — no incidents')" />
</div>
<div class="mt-2 flex justify-between text-xs text-neutral-500"><span>90 days ago</span><span class="font-bold text-neutral-900">99.99% uptime</span><span>Today</span></div>
<h2 class="reveal mt-12 text-2xl font-extrabold">Incident history</h2>
<div class="mt-4 space-y-3">
<article v-for="inc in incidents" :key="inc.t" class="reveal rounded-2xl border border-neutral-200 bg-white p-5"><p class="flex flex-wrap items-center gap-2 text-sm font-bold">{{inc.t}} <span class="rounded-full px-2.5 py-0.5 text-xs" :class="inc.sev==='Minor'?'bg-amber-100 text-amber-800':'bg-emerald-100 text-emerald-800'">{{inc.sev}}</span></p><p class="mt-2 text-sm leading-relaxed text-neutral-600">{{inc.d}}</p><p class="mt-2 text-xs text-neutral-400">{{inc.date}} · Resolved in {{inc.res}}</p></article>
</div>
<div class="reveal mt-10 rounded-3xl bg-violet-600 p-8 text-center text-white"><h2 class="text-2xl font-extrabold">Get notified about incidents</h2><p class="mt-2 text-sm text-violet-100">Subscribe to status updates by email or webhook.</p><NuxtLink to="/contact" class="btn btn-white mt-5">Subscribe to updates</NuxtLink></div>
</section>
</div></template>
<script setup lang="ts">
useSeoMeta({ title: 'Status — CloudPilot', description: 'Live CloudPilot service status, 90-day uptime and incident history.' })
const services = [
{ n: 'Web app', u: '100.00', ok: true },
{ n: 'API', u: '99.99', ok: true },
{ n: 'Integrations', u: '99.98', ok: true },
{ n: 'Notifications & email', u: '100.00', ok: true },
]
const days = Array.from({ length: 90 }, (_, i) => (i === 41 ? 2 : i === 17 || i === 63 ? 1 : 0))
const incidents = [
{ t: 'Elevated API errors in EU region', sev: 'Minor', d: 'A configuration change caused elevated 5xx errors on the EU API for 18 minutes. Rolled back; no data loss.', date: 'Nov 4, 2026', res: '18 min' },
{ t: 'Slack integration delays', sev: 'Minor', d: 'Webhook deliveries to Slack were delayed by up to 9 minutes while a queue drained. All events delivered.', date: 'Oct 21, 2026', res: '42 min' },
{ t: 'Scheduled maintenance — database upgrade', sev: 'Maintenance', d: 'Planned upgrade completed on schedule with 4 minutes of read-only mode. Announced 7 days in advance.', date: 'Oct 2, 2026', res: '4 min' },
]
</script>
