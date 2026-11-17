<template><div class="mx-auto max-w-2xl px-4 py-16 sm:px-6">
<div class="reveal rounded-3xl border border-neutral-200 p-7 shadow-sm"><h1 class="text-3xl font-extrabold">Start your free trial</h1><p class="mt-2 text-sm leading-relaxed text-neutral-600">14 days on Growth, no credit card. We will email your workspace link.</p>
<form class="mt-7 space-y-4" @submit.prevent="submit" novalidate>
<label class="block text-sm font-bold">Full name<input v-model="f.name" class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm outline-none focus:border-violet-500" /></label>
<label class="block text-sm font-bold">Work email<input v-model="f.email" type="email" class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm outline-none focus:border-violet-500" /></label>
<label class="block text-sm font-bold">Company size<select v-model="f.size" class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm"><option>1–10</option><option>11–50</option><option>51–200</option><option>200+</option></select></label>
<p v-if="err" class="text-sm font-medium text-red-600">{{err}}</p>
<button class="w-full rounded-full bg-black py-3 text-sm font-bold text-white hover:bg-violet-700">Start Free Trial</button></form>
<div v-if="ok" class="mt-5 rounded-2xl bg-emerald-50 p-4 text-sm font-medium text-emerald-800">Thanks {{f.name || 'there'}} — your demo workspace link is on its way to {{f.email}}. (Demo form — nothing was sent.)</div></div></div></template>
<script setup lang="ts">
useSeoMeta({title:'Start Free Trial — CloudPilot',description:'Start your 14-day free CloudPilot trial.'})
const f=reactive({name:'',email:'',size:'11–50'}); const err=ref(''); const ok=ref(false)
function submit(){ if(!f.name.trim()){err.value='Please enter your name.'; return} if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(f.email)){err.value='Please enter a valid work email.'; return} err.value=''; ok.value=true }
</script>
