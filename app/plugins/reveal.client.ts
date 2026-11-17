export default defineNuxtPlugin(() => {
  if (typeof window === 'undefined') return
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('revealed'); io.unobserve(e.target) }
  }, { threshold: 0.12 })
  const observe = () => document.querySelectorAll('.reveal:not(.revealed)').forEach((el) => io.observe(el))
  // observe on route change + initial
  const nuxtApp = useNuxtApp()
  nuxtApp.hook('page:finish', () => setTimeout(observe, 50))
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', observe)
  else setTimeout(observe, 50)
})
