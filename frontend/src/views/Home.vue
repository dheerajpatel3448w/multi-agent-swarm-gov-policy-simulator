<template>
  <div class="command-center">
    <!-- Navbar / Header -->
    <header class="glass-panel cc-header">
      <div class="brand-group">
        <div class="logo-pulse"></div>
        <h1 class="telemetry-title">AgentixGov | Command Center</h1>
      </div>
      <div class="status-group">
        <span class="status-indicator online"></span>
        <span class="status-text">SYSTEM ONLINE: ACTIVE SIMULATION ENGINE</span>
        <LanguageSwitcher class="lang-switch" />
      </div>
    </header>

    <main class="cc-main">
      <!-- Left Column: Metrics & Architecture -->
      <section class="cc-col-left">
        <div class="glass-panel widget architecture-widget">
          <div class="widget-header">
            <span class="widget-title">Digital Twin Architecture</span>
          </div>
          <div class="widget-body">
            <p class="arch-desc">
              Multi-agent AI architecture simulating real-world citizens, government officers, and resources. 
              Zero-risk policy testing and emergent behavior prediction via Graph Knowledge Base.
            </p>
            <div class="agent-stats">
              <div class="stat-item">
                <span class="stat-val text-blue">10,000+</span>
                <span class="stat-lbl">Autonomous Personas</span>
              </div>
              <div class="stat-item">
                <span class="stat-val text-blue">Live</span>
                <span class="stat-lbl">Action-Observation Loop</span>
              </div>
              <div class="stat-item">
                <span class="stat-val text-orange">Zep</span>
                <span class="stat-lbl">Vector Memory</span>
              </div>
            </div>
          </div>
        </div>

        <div class="glass-panel widget workflow-widget">
          <div class="widget-header">
            <span class="widget-title">Simulation Pipeline</span>
          </div>
          <div class="widget-body pipeline-list">
            <div class="pipe-step">
              <div class="pipe-node">1</div>
              <div class="pipe-info">
                <strong>Policy Input</strong>
                <span>Define government scheme or intervention</span>
              </div>
            </div>
            <div class="pipe-step">
              <div class="pipe-node">2</div>
              <div class="pipe-info">
                <strong>Environment Synthesis</strong>
                <span>Generate mapped GraphRAG social connections</span>
              </div>
            </div>
            <div class="pipe-step">
              <div class="pipe-node">3</div>
              <div class="pipe-info">
                <strong>Emergent Simulation</strong>
                <span>Agents react independently based on context</span>
              </div>
            </div>
            <div class="pipe-step">
              <div class="pipe-node">4</div>
              <div class="pipe-info">
                <strong>Bottleneck Prediction</strong>
                <span>Detect anomalies (e.g. panic buying, traffic)</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Right Column: Control Console -->
      <section class="cc-col-right">
        <div class="glass-panel widget console-widget">
          <div class="widget-header">
            <span class="widget-title">Simulation Launch Console</span>
            <span class="widget-badge">B2G-SECURE</span>
          </div>
          <div class="widget-body">
            <!-- Reality Seed Upload -->
            <div class="console-group">
              <label class="console-label">Base Reality Seed (PDF/MD/TXT)</label>
              <div 
                class="upload-area"
                :class="{ 'drag-over': isDragOver, 'has-files': files.length > 0 }"
                @dragover.prevent="handleDragOver"
                @dragleave.prevent="handleDragLeave"
                @drop.prevent="handleDrop"
                @click="triggerFileInput"
              >
                <input
                  ref="fileInput"
                  type="file"
                  multiple
                  accept=".pdf,.md,.txt"
                  @change="handleFileSelect"
                  style="display: none"
                  :disabled="loading"
                />
                
                <div v-if="files.length === 0" class="upload-empty">
                  <div class="upload-icon">â‡ª</div>
                  <span>Initialize System Context</span>
                  <small>Drag & Drop or Click to Browse</small>
                </div>
                
                <div v-else class="file-list">
                  <div v-for="(file, index) in files" :key="index" class="file-item glass-item">
                    <span class="file-name">{{ file.name }}</span>
                    <button @click.stop="removeFile(index)" class="remove-btn">Ã—</button>
                  </div>
                </div>
              </div>
            </div>

            <!-- Simulation Prompt -->
            <div class="console-group">
              <label class="console-label">Policy / Event Injection</label>
              <textarea
                v-model="formData.simulationRequirement"
                class="glass-input telemetry-textarea"
                placeholder="e.g. Initiate 'Free Ration Distribution' in Sector 4. Track local police and citizen response."
                rows="5"
                :disabled="loading"
              ></textarea>
            </div>

            <!-- Launch Button -->
            <div class="console-action">
              <button 
                class="launch-btn"
                @click="startSimulation"
                :disabled="!canSubmit || loading"
              >
                <div class="btn-glow"></div>
                <span class="btn-text" v-if="!loading">INITIALIZE DIGITAL TWIN</span>
                <span class="btn-text" v-else>SYNTHESIZING ENVIRONMENT...</span>
              </button>
            </div>
          </div>
        </div>
      </section>
    </main>
    
    <!-- History View Integration -->
    <div class="history-container">
      <HistoryDatabase />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import HistoryDatabase from '../components/HistoryDatabase.vue'
import LanguageSwitcher from '../components/LanguageSwitcher.vue'

const router = useRouter()

const formData = ref({
  simulationRequirement: ''
})

const files = ref([])
const loading = ref(false)
const error = ref('')
const isDragOver = ref(false)
const fileInput = ref(null)

const canSubmit = computed(() => {
  return formData.value.simulationRequirement.trim() !== '' && files.value.length > 0
})

const triggerFileInput = () => {
  if (!loading.value) fileInput.value?.click()
}

const handleFileSelect = (event) => {
  addFiles(Array.from(event.target.files))
}

const handleDragOver = () => {
  if (!loading.value) isDragOver.value = true
}

const handleDragLeave = () => {
  isDragOver.value = false
}

const handleDrop = (e) => {
  isDragOver.value = false
  if (loading.value) return
  addFiles(Array.from(e.dataTransfer.files))
}

const addFiles = (newFiles) => {
  const validFiles = newFiles.filter(file => {
    const ext = file.name.split('.').pop().toLowerCase()
    return ['pdf', 'md', 'txt'].includes(ext)
  })
  files.value.push(...validFiles)
}

const removeFile = (index) => {
  files.value.splice(index, 1)
}

const startSimulation = () => {
  if (!canSubmit.value || loading.value) return
  
  import('../store/pendingUpload.js').then(({ setPendingUpload }) => {
    setPendingUpload(files.value, formData.value.simulationRequirement)
    router.push({
      name: 'Process',
      params: { projectId: 'new' }
    })
  })
}
</script>

<style scoped>
.command-center {
  padding: 2rem;
  max-width: 1600px;
  margin: 0 auto;
}

.cc-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  margin-bottom: 2rem;
}

.brand-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo-pulse {
  width: 12px;
  height: 12px;
  background: var(--ocean-blue);
  border-radius: 50%;
  box-shadow: 0 0 10px var(--ocean-blue);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(0, 229, 255, 0.4); }
  70% { box-shadow: 0 0 0 10px rgba(0, 229, 255, 0); }
  100% { box-shadow: 0 0 0 0 rgba(0, 229, 255, 0); }
}

.telemetry-title {
  font-size: 1.5rem;
  margin: 0;
}

.status-group {
  display: flex;
  align-items: center;
  gap: 1rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.status-indicator.online {
  width: 8px;
  height: 8px;
  background: #00ff88;
  border-radius: 50%;
  box-shadow: 0 0 8px #00ff88;
}

.lang-switch {
  margin-left: 1rem;
  filter: invert(1) hue-rotate(180deg); /* Quick dark mode fix if component is light */
}

.cc-main {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.widget {
  padding: 1.5rem;
  margin-bottom: 2rem;
}

.widget-header {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-glass);
  padding-bottom: 1rem;
  margin-bottom: 1rem;
}

.widget-title {
  font-family: 'Orbitron', sans-serif;
  color: var(--ocean-blue);
  letter-spacing: 1px;
}

.widget-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.7rem;
  background: var(--accent-red);
  color: white;
  padding: 2px 6px;
  border-radius: 4px;
}

.arch-desc {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
}

.agent-stats {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

.stat-item {
  background: rgba(0,0,0,0.3);
  border: 1px solid var(--border-glass);
  border-radius: 8px;
  padding: 1rem;
  flex: 1;
  text-align: center;
}

.stat-val {
  display: block;
  font-family: 'Orbitron', sans-serif;
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.text-blue { color: var(--ocean-blue); }
.text-orange { color: var(--accent-orange); }

.stat-lbl {
  font-size: 0.75rem;
  color: var(--text-secondary);
  text-transform: uppercase;
}

.pipeline-list {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.pipe-step {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
}

.pipe-node {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: rgba(0, 229, 255, 0.1);
  border: 1px solid var(--ocean-blue);
  color: var(--ocean-blue);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'JetBrains Mono', monospace;
  font-weight: bold;
}

.pipe-info strong {
  display: block;
  color: var(--text-primary);
  margin-bottom: 0.2rem;
}

.pipe-info span {
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.console-group {
  margin-bottom: 1.5rem;
}

.console-label {
  display: block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.8rem;
  color: var(--ocean-blue);
  margin-bottom: 0.5rem;
  text-transform: uppercase;
}

.upload-area {
  border: 1px dashed var(--ocean-blue);
  background: rgba(0, 229, 255, 0.05);
  border-radius: 8px;
  padding: 2rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s;
  min-height: 120px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.upload-area:hover, .drag-over {
  background: rgba(0, 229, 255, 0.15);
  border-color: #fff;
}

.upload-empty .upload-icon {
  font-size: 2rem;
  color: var(--ocean-blue);
  margin-bottom: 0.5rem;
}

.upload-empty span {
  display: block;
  font-weight: bold;
}

.upload-empty small {
  color: var(--text-secondary);
}

.file-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 100%;
}

.glass-item {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid var(--border-glass);
  padding: 0.5rem 1rem;
  border-radius: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.remove-btn {
  background: none;
  border: none;
  color: var(--accent-red);
  font-size: 1.2rem;
}

.glass-input {
  width: 100%;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-glass);
  border-radius: 8px;
  padding: 1rem;
  color: var(--text-primary);
  font-family: 'Inter', sans-serif;
  resize: vertical;
}

.glass-input:focus {
  outline: none;
  border-color: var(--ocean-blue);
  box-shadow: 0 0 10px rgba(0, 229, 255, 0.2);
}

.launch-btn {
  width: 100%;
  padding: 1.2rem;
  background: transparent;
  border: 1px solid var(--ocean-blue);
  color: var(--ocean-blue);
  font-family: 'Orbitron', sans-serif;
  font-size: 1.1rem;
  font-weight: bold;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  transition: all 0.3s;
}

.launch-btn:hover:not(:disabled) {
  background: rgba(0, 229, 255, 0.1);
  box-shadow: 0 0 20px rgba(0, 229, 255, 0.3);
  color: #fff;
}

.launch-btn:disabled {
  border-color: var(--text-secondary);
  color: var(--text-secondary);
  cursor: not-allowed;
}

.history-container {
  margin-top: 3rem;
}

@media (max-width: 1024px) {
  .cc-main { grid-template-columns: 1fr; }
}
</style>


