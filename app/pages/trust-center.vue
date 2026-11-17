<template><div>
<section class="bg-black text-white"><div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
<p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300"><ShieldCheck class="h-3.5 w-3.5" /> Trust Center</p>
<h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Your data, <span class="text-grad">guarded.</span></h1>
<p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Certifications, encryption, uptime and subprocessors — everything your security review needs, in one place. Demo data: certifications are aspirational, not audited.</p>
</div></section>
<section class="mx-auto max-w-7xl px-4 py-14 sm:px-6">
<div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-4">
<div v-for="b in badges" :key="b.n" class="reveal rounded-3xl border border-neutral-200 bg-white p-6 text-center"><component :is="b.icon" class="mx-auto h-8 w-8 text-violet-600" /><h3 class="mt-3 font-bold">{{b.n}}</h3><p class="mt-1 text-sm text-neutral-600">{{b.d}}</p></div>
</div>
<div class="reveal mt-10 grid gap-5 rounded-3xl bg-violet-600 p-8 text-white sm:grid-cols-3"><div><p class="text-3xl font-extrabold">99.99%</p><p class="mt-1 text-sm text-violet-100">Uptime, trailing 12 months</p></div><div><p class="text-3xl font-extrabold">TLS 1.3 + AES-256</p><p class="mt-1 text-sm text-violet-100">Encryption in transit and at rest</p></div><div><p class="text-3xl font-extrabold">EU + US</p><p class="mt-1 text-sm text-violet-100">Data residency regions</p></div></div>
<h2 class="reveal mt-14 text-3xl font-extrabold">How we protect your data</h2>
<div class="mt-6 grid gap-5 sm:grid-cols-2">
<div v-for="p in protections" :key="p.t" class="reveal rounded-3xl border border-neutral-200 bg-white p-6"><h3 class="flex items-center gap-2 font-bold"><CheckCircle2 class="h-5 w-5 text-emerald-600" /> {{p.t}}</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">{{p.d}}</p></div>
</div>
<h2 class="reveal mt-14 text-3xl font-extrabold">Subprocessors</h2>
<p class="reveal mt-3 text-sm leading-relaxed text-neutral-600">The third-party services that process CloudPilot customer data. We notify customers 30 days before adding a new one.</p>
<div class="reveal mt-6 overflow-x-auto rounded-3xl border border-neutral-200"><table class="w-full min-w-[560px] text-left text-sm"><thead><tr class="border-b border-neutral-200 bg-neutral-50"><th class="px-5 py-3 font-bold">Vendor</th><th class="px-5 py-3 font-bold">Purpose</th><th class="px-5 py-3 font-bold">Location</th></tr></thead><tbody>
<tr v-for="s in subs" :key="s.v" class="border-b border-neutral-100 last:border-0"><td class="px-5 py-3 font-bold">{{s.v}}</td><td class="px-5 py-3 text-neutral-600">{{s.p}}</td><td class="px-5 py-3 text-neutral-600">{{s.l}}</td></tr>
</tbody></table></div>
<div class="reveal mt-10 flex flex-wrap gap-3"><NuxtLink to="/status" class="btn btn-outline-dark">Live status</NuxtLink><NuxtLink to="/security" class="btn btn-outline-dark">Security overview</NuxtLink><NuxtLink to="/privacy-policy" class="btn btn-outline-dark">Privacy policy</NuxtLink><a href="/.well-known/security.txt" class="btn btn-outline-dark">security.txt</a></div>
<p class="reveal mt-6 text-sm text-neutral-500">Report a vulnerability: security@cloudpilot.app — see <a href="/.well-known/security.txt" class="font-bold text-violet-700 underline">/.well-known/security.txt</a>. We acknowledge reports within 48 hours.</p>
</section>
</div></template>
<script setup lang="ts">
import { ShieldCheck, Lock, Globe, FileText } from '@lucide/vue'
useSeoMeta({ title: 'Trust Center — CloudPilot', description: 'CloudPilot security, compliance, uptime and subprocessors. SOC 2, GDPR, encryption and data residency.' })
const badges = [
{ n: 'SOC 2 Type II', d: 'Audited annually. Report available under NDA.', icon: ShieldCheck },
{ n: 'GDPR', d: 'EU data residency and a signed DPA on request.', icon: Globe },
{ n: 'ISO 27001', d: 'Information security management, certified.', icon: FileText },
{ n: 'CCPA', d: 'California privacy rights, honoured in full.', icon: Lock },
]
const protections = [
{ t: 'Encryption everywhere', d: 'TLS 1.3 in transit, AES-256 at rest, and per-workspace encryption keys on Enterprise.' },
{ t: 'Access control', d: 'SSO, SCIM provisioning, role-based permissions and audit logs on every plan above Free.' },
{ t: 'Backups & recovery', d: 'Continuous backups with point-in-time restore. RPO 5 minutes, RTO 1 hour.' },
{ t: 'Penetration testing', d: 'Independent pen-tests twice a year, plus a public bug-bounty programme.' },
]
const subs = [
{ v: 'Cloudflare', p: 'CDN, DNS and edge hosting', l: 'Global' },
{ v: 'AWS (us-east-1, eu-west-1)', p: 'Compute and database hosting', l: 'US / EU' },
{ v: 'Stripe', p: 'Payment processing', l: 'US' },
{ v: 'SendGrid', p: 'Transactional email', l: 'US' },
{ v: 'Sentry', p: 'Error monitoring', l: 'US' },
]
</script>
