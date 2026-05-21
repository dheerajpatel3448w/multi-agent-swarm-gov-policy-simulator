<template>
  <div class="gov-bg">
    <!-- Grid overlay for telemetry feel -->
    <div class="grid-overlay"></div>
    <router-view class="app-content" />
  </div>
</template>

<script setup>
// Use Vue Router to manage pages
</script>

<style>
/* Global style reset & variables */
:root {
  --bg-base: #050a14;
  --bg-panel: rgba(10, 15, 26, 0.65);
  --bg-panel-hover: rgba(10, 15, 26, 0.85);
  --text-primary: #e0f2fe;
  --text-secondary: #94a3b8;
  --ocean-blue: #00e5ff;
  --ocean-blue-dim: rgba(0, 229, 255, 0.2);
  --accent-red: #ff3366;
  --accent-orange: #ff9900;
  --border-glass: rgba(0, 229, 255, 0.15);
  --glass-blur: blur(12px);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: 'Inter', 'Orbitron', 'Space Grotesk', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--text-primary);
  background-color: var(--bg-base);
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
}

.gov-bg {
  min-height: 100vh;
  position: relative;
  z-index: 1;
}

/* Telemetry Grid Overlay */
.grid-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(var(--ocean-blue-dim) 1px, transparent 1px),
    linear-gradient(90deg, var(--ocean-blue-dim) 1px, transparent 1px);
  background-size: 40px 40px;
  opacity: 0.15;
  pointer-events: none;
  z-index: -1;
}

.app-content {
  position: relative;
  z-index: 2;
}

/* Glassmorphism Utilities */
.glass-panel {
  background: var(--bg-panel);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border: 1px solid var(--border-glass);
  border-radius: 12px;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
  transition: all 0.3s ease;
}

.glass-panel:hover {
  border-color: rgba(0, 229, 255, 0.4);
  box-shadow: 0 8px 32px 0 rgba(0, 229, 255, 0.1);
}

/* Scrollbar styles */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 0, 0, 0.2);
}

::-webkit-scrollbar-thumb {
  background: var(--ocean-blue-dim);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--ocean-blue);
}

/* Global button styles */
button {
  font-family: inherit;
  cursor: pointer;
}

/* Title Font */
.telemetry-title {
  font-family: 'Orbitron', sans-serif;
  color: var(--ocean-blue);
  text-transform: uppercase;
  letter-spacing: 2px;
  text-shadow: 0 0 10px var(--ocean-blue-dim);
}
</style>
