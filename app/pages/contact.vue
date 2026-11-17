<template><div class="mx-auto max-w-2xl px-4 py-16 sm:px-6">
<div class="reveal rounded-3xl border border-neutral-200 p-7 shadow-sm"><h1 class="text-3xl font-extrabold">Contact us</h1><p class="mt-2 text-sm text-neutral-600">Sales, support or press — we reply within one business day. Demo contact details.</p>
<div class="mt-5 grid gap-3 text-sm sm:grid-cols-3"><div class="rounded-2xl bg-violet-50 p-4"><b>Email</b><br/>hello@cloudpilot.app</div><div class="rounded-2xl bg-violet-50 p-4"><b>Phone</b><br/>+1 (415) 555-0132</div><div class="rounded-2xl bg-violet-50 p-4"><b>Office</b><br/>San Francisco, CA</div></div>
<form class="mt-7 space-y-4" @submit.prevent="submit"><label class="block text-sm font-bold">Name<input v-model="n" required class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm" /></label><label class="block text-sm font-bold">Message<textarea v-model="m" required rows="4" class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm"></textarea></label><button class="w-full rounded-full bg-black py-3 text-sm font-bold text-white">Send message</button></form>
<p v-if="ok" class="mt-4 rounded-2xl bg-emerald-50 p-4 text-sm font-medium text-emerald-800">Thanks — message received (demo, nothing was sent).</p></div></div></template>
<script setup lang="ts">
useSeoMeta({title:'Contact — CloudPilot',description:'Contact the CloudPilot team.'})
const n=ref(''), m=ref(''), ok=ref(false); function submit(){ok.value=true}
</script>
