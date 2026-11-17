<template>
  <div>
    <section class="bg-black text-white">
      <div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 sm:py-20">
        <p class="reveal inline-flex items-center gap-2 rounded-full border border-white/20 px-3.5 py-1.5 text-xs font-semibold uppercase tracking-wider text-violet-300">Security & Trust</p>
        <h1 class="reveal mt-5 max-w-3xl text-4xl font-extrabold leading-[1.05] tracking-tight sm:text-5xl" style="--d:80ms">Your data, <span class='text-grad'>locked down.</span></h1>
        <p class="reveal mt-5 max-w-2xl text-base leading-relaxed text-neutral-300 sm:text-lg" style="--d:160ms">Security is not a feature tier at CloudPilot. Encryption, access controls and audit logs ship on every plan.</p>
        <div class="reveal mt-8 flex flex-wrap gap-3" style="--d:240ms">
          <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-black hover:bg-violet-200">Start Free Trial</NuxtLink>
          <NuxtLink to="/pricing" class="rounded-full border border-white/30 px-6 py-3 text-sm font-bold hover:bg-white/10">See Pricing</NuxtLink>
        </div>
      </div>
    </section>
    <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6"><div class="grid gap-5 sm:grid-cols-2 lg:grid-cols-3"><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:0ms"><h3 class="text-lg font-bold">SOC 2 Type II</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">Audited annually. Report available under NDA on request.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:80ms"><h3 class="text-lg font-bold">GDPR & CCPA</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">EU data residency available on Scale. DPA included.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:160ms"><h3 class="text-lg font-bold">SSO & SCIM</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">SAML, OIDC, Google and Okta SSO, plus automated provisioning.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:240ms"><h3 class="text-lg font-bold">Encryption</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">AES-256 at rest, TLS 1.3 in transit, keys rotated regularly.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:320ms"><h3 class="text-lg font-bold">Audit Logs</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">Every action, every admin change, exportable for 365 days.</p></article><article class="reveal card-hover rounded-3xl border border-neutral-200 bg-white p-6" style="--d:400ms"><h3 class="text-lg font-bold">Backups</h3><p class="mt-2 text-sm leading-relaxed text-neutral-600">Hourly backups, 30-day retention, tested restores monthly.</p></article></div></section>
    <section class="mx-auto max-w-7xl px-4 py-16 sm:px-6">
      <div class="reveal rounded-3xl bg-gradient-to-r from-violet-700 via-violet-600 to-fuchsia-600 px-6 py-12 text-center text-white sm:px-12">
        <h2 class="text-3xl font-extrabold tracking-tight sm:text-4xl">Ready to simplify, automate and scale?</h2>
        <p class="mx-auto mt-3 max-w-xl text-violet-100">Start free for 14 days. No credit card required. Cancel anytime.</p>
        <div class="mt-7 flex flex-wrap justify-center gap-3">
          <NuxtLink to="/request-demo" class="rounded-full bg-white px-6 py-3 text-sm font-bold text-violet-700">Start Free Trial</NuxtLink>
          <NuxtLink to="/contact" class="rounded-full border border-white/40 px-6 py-3 text-sm font-bold">Talk to Sales</NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>
<script setup lang="ts">
useSeoMeta({ title: 'Security — CloudPilot', description: 'SOC 2 Type II, GDPR, SSO and audit logs.' })

</script>
