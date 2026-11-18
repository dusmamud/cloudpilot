<template>
  <div>
    <button v-if="showButton" class="hidden min-h-11 items-center gap-2 rounded-full border border-white/20 px-3.5 text-sm text-neutral-300 transition hover:bg-white/10 hover:text-white md:flex" aria-label="Search ⌘K" @click="openPalette">
      <Search class="h-4 w-4" /><span class="hidden xl:inline">Search</span><kbd class="rounded-md bg-white/10 px-1.5 py-0.5 text-[11px] font-bold">⌘K</kbd>
    </button>
    <AnimatePresence>
      <Motion v-if="open" :initial="{ opacity: 0 }" :animate="{ opacity: 1 }" :exit="{ opacity: 0 }" :transition="{ duration: 0.15 }" class="fixed inset-0 z-[100] bg-black/60 backdrop-blur-sm" @click="close">
        <Motion :initial="{ opacity: 0, y: -12, scale: 0.98 }" :animate="{ opacity: 1, y: 0, scale: 1 }" :exit="{ opacity: 0, y: -12, scale: 0.98 }" :transition="{ duration: 0.2, ease: 'easeOut' }" class="mx-auto mt-24 w-[calc(100%-2rem)] max-w-xl overflow-hidden rounded-2xl bg-white shadow-2xl" @click.stop>
          <div class="flex items-center gap-3 border-b border-neutral-100 px-4">
            <Search class="h-5 w-5 shrink-0 text-neutral-400" />
            <input ref="inputEl" v-model="q" type="text" placeholder="Search pages, tools, docs…" class="h-14 flex-1 text-base text-neutral-900 outline-none placeholder:text-neutral-400" aria-label="Search pages" @keydown.down.prevent="move(1)" @keydown.up.prevent="move(-1)" @keydown.enter.prevent="go" @keydown.esc="close" />
            <kbd class="rounded-md bg-neutral-100 px-2 py-1 text-[11px] font-bold text-neutral-500">ESC</kbd>
          </div>
          <ul v-if="results.length" class="max-h-80 overflow-y-auto p-2" role="listbox" aria-label="Results">
            <li v-for="(r, i) in results" :key="r.to" role="option" :aria-selected="i === active">
              <NuxtLink :to="r.to" class="flex items-center justify-between gap-3 rounded-xl px-3 py-3 text-sm" :class="i === active ? 'bg-violet-100 text-violet-900' : 'hover:bg-neutral-50'" @click="close" @mouseenter="active = i">
                <span><span class="font-bold">{{ r.name }}</span><span class="block text-xs text-neutral-500">{{ r.desc }}</span></span>
                <span class="shrink-0 rounded-full bg-neutral-100 px-2.5 py-1 text-[11px] font-bold text-neutral-500">{{ r.group }}</span>
              </NuxtLink>
            </li>
          </ul>
          <p v-else class="px-5 py-8 text-center text-sm text-neutral-500">No pages match “{{ q }}”. Try “pricing”, “API” or “Slack”.</p>
          <div class="flex items-center gap-4 border-t border-neutral-100 px-4 py-2.5 text-[11px] text-neutral-400"><span>↑↓ navigate</span><span>↵ open</span><span>esc close</span></div>
        </Motion>
      </Motion>
    </AnimatePresence>
  </div>
</template>
<script setup lang="ts">
const props = defineProps<{ showButton?: boolean }>()
const open = ref(false)
const q = ref('')
const active = ref(0)
const inputEl = ref<HTMLInputElement | null>(null)
const pages = [
{ name: 'Home', to: '/', desc: 'Simplify. Automate. Scale your business.', group: 'Product' },
{ name: 'Features', to: '/features', desc: 'Everything in one platform', group: 'Product' },
{ name: 'Product tour', to: '/product-tour', desc: 'Click through the product, no account needed', group: 'Product' },
{ name: 'Tools', to: '/tools', desc: 'FlowMaster, InsightPro, TeamSync', group: 'Product' },
{ name: 'FlowMaster', to: '/tools/flowmaster', desc: 'Workflow automation', group: 'Product' },
{ name: 'InsightPro', to: '/tools/insightpro', desc: 'Advanced analytics', group: 'Product' },
{ name: 'TeamSync', to: '/tools/teamsync', desc: 'Team collaboration', group: 'Product' },
{ name: 'Integrations', to: '/integrations', desc: '100+ tools, one click', group: 'Product' },
{ name: 'Slack integration', to: '/integrations/slack', desc: 'Alerts and approvals in Slack', group: 'Product' },
{ name: 'Salesforce integration', to: '/integrations/salesforce', desc: 'Two-way deal sync', group: 'Product' },
{ name: 'Gmail integration', to: '/integrations/gmail', desc: 'Emails become tasks', group: 'Product' },
{ name: 'Developers & API', to: '/developers', desc: 'REST API, webhooks and SDKs', group: 'Product' },
{ name: 'Security', to: '/security', desc: 'SOC 2, GDPR, SSO', group: 'Product' },
{ name: 'Trust Center', to: '/trust-center', desc: 'Compliance, uptime, subprocessors', group: 'Product' },
{ name: 'Status', to: '/status', desc: 'Live service health and uptime', group: 'Product' },
{ name: 'Pricing', to: '/pricing', desc: '$0 / $19 / $49, monthly or yearly', group: 'Buy' },
{ name: 'ROI calculator', to: '/roi-calculator', desc: 'See what CloudPilot saves you', group: 'Buy' },
{ name: 'Compare', to: '/compare', desc: 'CloudPilot vs the old way', group: 'Buy' },
{ name: 'CloudPilot vs Asana', to: '/compare/asana', desc: 'Tasks, analytics and collaboration', group: 'Buy' },
{ name: 'CloudPilot vs Monday.com', to: '/compare/monday', desc: 'Ready on day one', group: 'Buy' },
{ name: 'CloudPilot vs Notion', to: '/compare/notion', desc: 'Workflows, not just pages', group: 'Buy' },
{ name: 'Start free trial', to: '/signup', desc: '14 days free, no credit card', group: 'Buy' },
{ name: 'Request a demo', to: '/request-demo', desc: '30-minute guided demo', group: 'Buy' },
{ name: 'Solutions', to: '/solutions', desc: 'By team and company size', group: 'Solutions' },
{ name: 'For Startups', to: '/solutions/startups', desc: 'Ship fast, stay lean', group: 'Solutions' },
{ name: 'For Teams', to: '/solutions/teams', desc: 'Collaborate in real-time', group: 'Solutions' },
{ name: 'For Enterprise', to: '/solutions/enterprise', desc: 'Scale with control', group: 'Solutions' },
{ name: 'Use cases', to: '/use-cases', desc: 'Project, marketing and sales', group: 'Solutions' },
{ name: 'Project management', to: '/use-cases/project-management', desc: 'Ship without status meetings', group: 'Solutions' },
{ name: 'Marketing campaigns', to: '/use-cases/marketing-campaigns', desc: 'Brief to results', group: 'Solutions' },
{ name: 'Sales pipeline', to: '/use-cases/sales-pipeline', desc: 'A pipeline that updates itself', group: 'Solutions' },
{ name: 'Templates', to: '/templates', desc: 'Ready-made workflows and boards', group: 'Resources' },
{ name: 'Customers', to: '/customers', desc: 'Case studies that shipped', group: 'Resources' },
{ name: 'Blog', to: '/blog', desc: 'Guides and product news', group: 'Resources' },
{ name: 'Help Center', to: '/help', desc: 'Answers in minutes', group: 'Resources' },
{ name: 'FAQ', to: '/faq', desc: 'Questions, answered', group: 'Resources' },
{ name: 'Changelog', to: '/changelog', desc: 'What is new in CloudPilot', group: 'Resources' },
{ name: 'Resources', to: '/resources', desc: 'Guides, templates and tools', group: 'Resources' },
{ name: 'How it works', to: '/how-it-works', desc: 'From signup to first win in a day', group: 'Resources' },
{ name: 'About', to: '/about', desc: 'Who builds CloudPilot', group: 'Company' },
{ name: 'Careers', to: '/careers', desc: 'Join the team', group: 'Company' },
{ name: 'Contact', to: '/contact', desc: 'Talk to a human', group: 'Company' },
{ name: 'Sign in', to: '/login', desc: 'Back to your workspace', group: 'Account' },
]
const results = computed(() => {
  const needle = q.value.trim().toLowerCase()
  const list = needle ? pages.filter(p => (p.name + ' ' + p.desc + ' ' + p.group).toLowerCase().includes(needle)) : pages.slice(0, 8)
  return list.slice(0, 8)
})
watch(q, () => { active.value = 0 })
function openPalette() { open.value = true; q.value = ''; active.value = 0; nextTick(() => inputEl.value?.focus()) }
function close() { open.value = false }
function move(d: number) { active.value = (active.value + d + results.value.length) % Math.max(1, results.value.length) }
function go() { const r = results.value[active.value]; if (r) { close(); navigateTo(r.to) } }
function onKey(e: KeyboardEvent) {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); open.value ? close() : openPalette() }
  if (e.key === 'Escape' && open.value) close()
}
onMounted(() => window.addEventListener('keydown', onKey))
onBeforeUnmount(() => window.removeEventListener('keydown', onKey))
defineExpose({ openPalette })
</script>
