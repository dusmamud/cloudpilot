<template><div class="mx-auto max-w-md px-4 py-16 sm:px-6">
<div class="reveal rounded-3xl border border-neutral-200 p-7 shadow-sm"><h1 class="text-2xl font-extrabold">Welcome back</h1><p class="mt-2 text-sm text-neutral-600">Demo login — use the demo account below.</p>
<form class="mt-6 space-y-4" @submit.prevent="submit">
<label class="block text-sm font-bold">Email<input v-model="email" type="email" required class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm outline-none focus:border-violet-500" /></label>
<label class="block text-sm font-bold">Password<input v-model="pw" type="password" required minlength="6" class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm outline-none focus:border-violet-500" /></label>
<p v-if="err" class="text-sm font-medium text-red-600">{{err}}</p>
<button class="w-full rounded-full bg-black py-3 text-sm font-bold text-white hover:bg-violet-700">Sign in</button></form>
<button @click="email='demo@cloudpilot.app'; pw='demo1234'" class="mt-3 w-full rounded-full border border-neutral-300 py-3 text-sm font-bold">Fill demo account</button>
<div v-if="ok" class="mt-5 rounded-2xl bg-emerald-50 p-4 text-sm"><p class="font-bold text-emerald-800">Signed in (demo) — welcome, Demo User.</p><p class="mt-1 text-emerald-700">Dashboard: 3 flows running, 2 alerts, 12 tasks due today. This is a front-end demo — no real account exists.</p><NuxtLink to="/" class="mt-2 inline-block font-bold text-emerald-800 underline">Back to home →</NuxtLink></div>
<p class="mt-4 text-center text-xs text-neutral-500">Demo: demo@cloudpilot.app / demo1234</p></div></div></template>
<script setup lang="ts">
useSeoMeta({title:'Sign in — CloudPilot',description:'Sign in to your CloudPilot workspace.'})
const email=ref(''), pw=ref(''), err=ref(''), ok=ref(false)
function submit(){ if(email.value==='demo@cloudpilot.app' && pw.value==='demo1234'){ok.value=true; err.value=''} else {err.value='Demo only: use demo@cloudpilot.app / demo1234'; ok.value=false} }
</script>
