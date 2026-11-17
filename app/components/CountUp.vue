<template><span ref="el">{{ display }}</span></template>
<script setup lang="ts">
const props = defineProps<{ to: number; suffix?: string; prefix?: string; duration?: number }>()
const display = ref((props.prefix || '') + '0' + (props.suffix || ''))
const el = ref<HTMLElement | null>(null)
let started = false
onMounted(() => {
  const io = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting && !started) {
      started = true
      const t0 = performance.now(); const dur = props.duration || 900
      const tick = (t: number) => {
        const p = Math.min(1, (t - t0) / dur)
        const v = Math.round(props.to * (1 - Math.pow(1 - p, 3)))
        display.value = (props.prefix || '') + v.toLocaleString('en-US') + (props.suffix || '')
        if (p < 1) requestAnimationFrame(tick)
      }
      requestAnimationFrame(tick); io.disconnect()
    }
  }, { threshold: 0.4 })
  if (el.value) io.observe(el.value)
})
</script>
