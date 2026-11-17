<template>
  <!-- CloudPilot mark, traced from the reference: a standalone bold "C" —
       violet at the top fading to white at the bottom. No circle, no container. -->
  <svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
    <defs>
      <linearGradient id="cp-c-mark" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#7c3aed" />
        <stop offset="40%" stop-color="#a78bfa" />
        <stop offset="65%" stop-color="#e9d5ff" />
        <stop offset="100%" stop-color="#ffffff" />
      </linearGradient>
    </defs>
    <path d="M 32.6 11.7 A 15 15 0 1 0 32.6 36.3" stroke="url(#cp-c-mark)" stroke-width="8" stroke-linecap="butt" />
  </svg>
</template>
