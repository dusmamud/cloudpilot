<template><div class="mx-auto max-w-md px-4 py-16 sm:px-6">
<div class="reveal rounded-3xl border border-neutral-200 p-7 shadow-sm"><h1 class="text-2xl font-extrabold">Start your free trial</h1><p class="mt-2 text-sm text-neutral-600">14 days free, full Pro features. No credit card required.</p>
<form v-if="!ok" class="mt-6 space-y-4" novalidate @submit.prevent="submit">
<label class="block text-sm font-bold">Full name<input v-model="name" required class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm outline-none focus:border-violet-500" placeholder="Ada Lovelace" /></label>
<label class="block text-sm font-bold">Work email<input v-model="email" type="email" required class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm outline-none focus:border-violet-500" placeholder="ada@company.com" /></label>
<label class="block text-sm font-bold">Password<input v-model="pw" type="password" required minlength="8" class="mt-1 w-full rounded-xl border border-neutral-300 px-4 py-3 text-sm outline-none focus:border-violet-500" placeholder="8+ characters" /></label>
<label class="block text-sm font-bold">Plan<select v-model="plan" class="mt-1 w-full rounded-xl border border-neutral-300 bg-white px-4 py-3 text-sm outline-none focus:border-violet-500"><option value="free">Free — $0</option><option value="pro">Pro — $19/user/mo</option><option value="enterprise">Enterprise — custom</option></select></label>
<label class="flex items-start gap-2 text-xs leading-relaxed text-neutral-600"><input v-model="agree" type="checkbox" required class="mt-0.5 h-4 w-4 accent-violet-600" /> I agree to the <NuxtLink to="/terms" class="font-bold text-violet-700 underline">Terms</NuxtLink> and <NuxtLink to="/privacy-policy" class="font-bold text-violet-700 underline">Privacy Policy</NuxtLink>.</label>
<p v-if="err" class="text-sm font-medium text-red-600">{{err}}</p>
<button class="btn btn-violet w-full">Create my workspace</button>
</form>
<div v-if="ok" class="mt-6 rounded-2xl bg-emerald-50 p-5 text-sm"><p class="flex items-center gap-2 font-bold text-emerald-800"><CheckCircle2 class="h-5 w-5" /> Workspace created (demo)</p><p class="mt-2 leading-relaxed text-emerald-700">Welcome, {{name}}! Your {{plan}} trial is ready. This is a front-end demo — no real account was created. Try the <NuxtLink to="/product-tour" class="font-bold underline">Product Tour</NuxtLink> next.</p><NuxtLink to="/" class="btn btn-dark mt-4">Back to home</NuxtLink></div>
<p class="mt-4 text-center text-xs text-neutral-500">Already have an account? <NuxtLink to="/login" class="font-bold text-violet-700 underline">Sign in</NuxtLink> · Prefer a guided demo? <NuxtLink to="/request-demo" class="font-bold text-violet-700 underline">Request demo</NuxtLink></p></div></div></template>
<script setup lang="ts">
useSeoMeta({ title: 'Sign up — CloudPilot', description: 'Start a 14-day free CloudPilot trial. No credit card required.' })
const route = useRoute()
const name = ref(''), email = ref(''), pw = ref(''), err = ref(''), ok = ref(false), agree = ref(false)
const plan = ref(typeof route.query.plan === 'string' && ['free', 'pro', 'enterprise'].includes(route.query.plan) ? route.query.plan : 'pro')
function submit() {
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) { err.value = 'Enter a valid work email.'; return }
  if (pw.value.length < 8) { err.value = 'Password needs at least 8 characters.'; return }
  if (!agree.value) { err.value = 'Please accept the Terms and Privacy Policy.'; return }
  err.value = ''; ok.value = true
}
</script>
