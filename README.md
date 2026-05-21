# AgentixGov

> **A Universal Multi-Agent Swarm Intelligence Engine for Government Policy Simulation**

AgentixGov is a full-stack AI-powered platform that simulates how government policies propagate through society using a multi-agent social media simulation. Upload policy documents, auto-generate a knowledge graph, configure realistic AI agents, run simulations on Twitter/Reddit-style platforms, and receive rich analytical reports — all in one cohesive pipeline.

---

## Overview

AgentixGov transforms raw policy documents into a live swarm simulation in five guided steps:

```
[1] Build Knowledge Graph  ->  [2] Configure Environment  ->  [3] Run Simulation  ->  [4] Generate Report  ->  [5] Interactive Analysis
```

Each step is powered by LLMs (via OpenAI-compatible APIs) and backed by Zep Cloud's temporal knowledge graph memory, enabling agents to remember, react, and evolve opinions over multiple rounds.

---

## Key Features

| Feature | Description |
|---|---|
| Document Ingestion | Upload PDF, Markdown, and TXT policy files (up to 50MB) |
| Ontology Generation | LLM auto-extracts entities, relationships, and key themes |
| Knowledge Graph | Zep Cloud stores and queries a persistent temporal graph of all entities |
| Agent Profiling | AI-generated citizen agent profiles (demographics, opinions, behaviors) |
| Social Simulation | OASIS-powered multi-round Twitter & Reddit social media simulations |
| Report Agent | Reflective multi-tool report generation with structured analysis |
| Interactive Chat | Post-simulation Q&A with the Report Agent |
| i18n Support | Full English and Chinese (Simplified) interface |
| History Database | Browse and revisit all past simulation projects |

---

## Architecture

```
AgentixGov/
+-- backend/                    # Python / Flask API server
|   +-- app/
|   |   +-- __init__.py         # Flask app factory
|   |   +-- config.py           # Centralized config (env-based)
|   |   +-- api/
|   |   |   +-- graph.py        # /api/graph  -- ontology & knowledge graph
|   |   |   +-- simulation.py   # /api/simulation -- agent setup & sim runs
|   |   |   +-- report.py       # /api/report -- report generation & chat
|   |   +-- models/
|   |   |   +-- project.py      # Project lifecycle & file management
|   |   |   +-- task.py         # Async background task tracking
|   |   +-- services/
|   |   |   +-- ontology_generator.py        # LLM ontology extraction
|   |   |   +-- graph_builder.py             # Zep graph construction
|   |   |   +-- text_processor.py            # Document chunking
|   |   |   +-- oasis_profile_generator.py   # AI agent profile creation
|   |   |   +-- simulation_config_generator.py # Sim parameters & events
|   |   |   +-- simulation_manager.py        # Project-level sim state
|   |   |   +-- simulation_runner.py         # OASIS multi-round executor
|   |   |   +-- simulation_ipc.py            # IPC for live sim control
|   |   |   +-- report_agent.py              # Reflective report builder
|   |   |   +-- zep_entity_reader.py         # Entity queries from Zep
|   |   |   +-- zep_graph_memory_updater.py  # Post-sim graph memory sync
|   |   |   +-- zep_tools.py                 # Zep Cloud tool wrappers
|   |   +-- utils/
|   |       +-- llm_client.py    # Unified OpenAI-format LLM client
|   |       +-- file_parser.py   # PDF/MD/TXT text extraction
|   |       +-- logger.py        # Structured logging setup
|   |       +-- retry.py         # Exponential backoff retry utility
|   |       +-- locale.py        # Backend i18n support
|   |       +-- zep_paging.py    # Zep Cloud paged result helper
|   +-- run.py                  # Entry point (UTF-8 safe, Windows compatible)
|   +-- requirements.txt        # Python dependencies
|   +-- pyproject.toml          # uv project config
|
+-- frontend/                   # Vue 3 + Vite SPA
|   +-- src/
|   |   +-- App.vue             # Root component (glassmorphism theme)
|   |   +-- main.js             # Vue app bootstrap with i18n & router
|   |   +-- router/             # Vue Router page definitions
|   |   +-- store/
|   |   |   +-- pendingUpload.js # Global upload state
|   |   +-- api/                # Axios API client modules
|   |   +-- i18n/               # vue-i18n setup
|   |   +-- views/
|   |   |   +-- Home.vue              # Landing / project list
|   |   |   +-- MainView.vue          # Main shell layout
|   |   |   +-- Process.vue           # 5-step workflow wrapper
|   |   |   +-- SimulationView.vue    # Simulation configuration UI
|   |   |   +-- SimulationRunView.vue # Live simulation run panel
|   |   |   +-- ReportView.vue        # Report display
|   |   |   +-- InteractionView.vue   # Post-sim interactive chat
|   |   +-- components/
|   |       +-- Step1GraphBuild.vue   # Step 1: Upload & graph build
|   |       +-- Step2EnvSetup.vue     # Step 2: Agent & env configuration
|   |       +-- Step3Simulation.vue   # Step 3: Sim parameters
|   |       +-- Step4Report.vue       # Step 4: Report viewer
|   |       +-- Step5Interaction.vue  # Step 5: Interactive Q&A
|   |       +-- GraphPanel.vue        # D3.js knowledge graph visualizer
|   |       +-- HistoryDatabase.vue   # Past projects browser
|   |       +-- LanguageSwitcher.vue  # EN / ZH toggle
|   +-- index.html
|   +-- vite.config.js
|
+-- locales/
|   +-- en.json                 # English translations
|   +-- zh.json                 # Chinese (Simplified) translations
|   +-- languages.json          # Language registry
|
+-- static/
|   +-- image/                  # Static image assets
|
+-- .env.example                # Template for environment variables
+-- .gitignore
+-- package.json                # Root monorepo scripts (concurrently)
+-- LICENSE                     # AGPL-3.0
```

---

## Technology Stack

### Backend

| Layer | Technology |
|---|---|
| Framework | Flask 3.0+ with Flask-CORS |
| LLM Interface | OpenAI SDK (unified format -- works with any OpenAI-compatible API) |
| Memory / Graph | Zep Cloud 3.13 (temporal knowledge graph) |
| Social Simulation | OASIS via camel-oasis 0.2.5 + camel-ai 0.2.78 |
| PDF Parsing | PyMuPDF |
| Data Validation | Pydantic 2.0+ |
| Env Management | python-dotenv |
| Package Manager | uv (ultra-fast Python package manager) |
| Python Version | 3.11+ |

### Frontend

| Layer | Technology |
|---|---|
| Framework | Vue 3 (Composition API, script setup) |
| Build Tool | Vite 7 |
| Routing | Vue Router 4 |
| Internationalisation | Vue i18n 11 |
| HTTP Client | Axios 1.14 |
| Graph Visualisation | D3.js 7 |
| UI Style | Glassmorphism dark theme (custom vanilla CSS) |

---

## Getting Started

### Prerequisites

- Node.js >= 18.0.0
- Python >= 3.11
- uv (Python package manager) — https://github.com/astral-sh/uv
- A Zep Cloud account & API key — https://www.getzep.com/
- An LLM API key (OpenAI, Azure OpenAI, or any OpenAI-compatible provider)

---

### 1. Clone the Repository

```bash
git clone https://github.com/dheerajpatel3448w/multi-agent-swarm-gov-policy-simulator.git
cd multi-agent-swarm-gov-policy-simulator
```

---

### 2. Configure Environment Variables

Copy the example env file and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```env
# Primary LLM
LLM_API_KEY=your_openai_or_compatible_api_key
LLM_BASE_URL=https://api.openai.com/v1
LLM_MODEL_NAME=gpt-4o-mini

# Boost LLM (optional, for heavy report tasks)
LLM_BOOST_API_KEY=your_boost_api_key
LLM_BOOST_BASE_URL=https://api.openai.com/v1
LLM_BOOST_MODEL_NAME=gpt-4o

# Zep Cloud
ZEP_API_KEY=your_zep_cloud_api_key
```

> **Tip:** You can point `LLM_BASE_URL` to any OpenAI-compatible provider such as Groq, Together AI, Ollama, or Azure OpenAI.

---

### 3. Install All Dependencies

```bash
# Install root & frontend Node dependencies
npm run setup

# Install backend Python dependencies via uv
npm run setup:backend

# Or do everything at once:
npm run setup:all
```

---

### 4. Run the Development Server

```bash
npm run dev
```

This starts both services concurrently:

| Service | URL |
|---|---|
| Frontend (Vite) | http://localhost:5173 |
| Backend (Flask) | http://localhost:5001 |
| Health Check | http://localhost:5001/health |

---

## Workflow Walkthrough

### Step 1 — Build Knowledge Graph

1. Create a new project and give it a name.
2. Upload one or more policy documents (PDF, Markdown, or plain text, up to 50 MB).
3. AgentixGov extracts and chunks the text, then calls the LLM to auto-generate an **ontology** — a structured map of entities (people, organisations, policies, locations) and their relationships.
4. The ontology is pushed to **Zep Cloud** to build a persistent temporal knowledge graph.
5. The interactive **D3.js graph panel** visualises all nodes and edges.

### Step 2 — Configure Simulation Environment

1. Set the simulation platform: **Twitter** or **Reddit**.
2. Configure the number of AI agents and their demographic distributions.
3. The `OasisProfileGenerator` uses the knowledge graph to create realistic citizen agent profiles — each with unique opinions, communication styles, and behavioural tendencies.
4. Define simulation parameters: max rounds, event triggers, platform-specific actions.

### Step 3 — Run Simulation

1. Launch the simulation. AgentixGov spawns an isolated subprocess via `SimulationRunner`.
2. Agents interact across multiple rounds using OASIS actions:
   - **Twitter**: `CREATE_POST`, `LIKE_POST`, `REPOST`, `FOLLOW`, `QUOTE_POST`, `DO_NOTHING`
   - **Reddit**: `CREATE_POST`, `CREATE_COMMENT`, `LIKE_POST`, `DISLIKE_POST`, `SEARCH_POSTS`, `TREND`, `FOLLOW`, `MUTE`, and more
3. Live round-by-round progress is streamed to the UI via IPC (Inter-Process Communication).
4. Agent actions and memory updates are written back to the Zep knowledge graph after each round.

### Step 4 — Generate Report

1. The `ReportAgent` performs a **reflective multi-tool analysis** over the simulation data.
2. It queries the Zep knowledge graph, aggregates agent action logs, identifies opinion trends, and generates a structured analytical report.
3. The report includes: sentiment analysis, key narrative shifts, policy reception heatmaps, and agent cluster behaviour.

### Step 5 — Interactive Analysis

1. Ask follow-up questions about the simulation in natural language.
2. The Report Agent uses its accumulated context and Zep graph tools to provide grounded, evidence-backed answers.

---

## API Reference

### Graph API — `/api/graph`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/graph/project` | Create a new project |
| GET | `/api/graph/project` | List all projects |
| GET | `/api/graph/project/:id` | Get project details |
| DELETE | `/api/graph/project/:id` | Delete a project |
| POST | `/api/graph/project/:id/files` | Upload documents |
| POST | `/api/graph/project/:id/ontology` | Generate ontology |
| POST | `/api/graph/project/:id/build` | Build knowledge graph |
| GET | `/api/graph/project/:id/graph` | Query graph nodes/edges |

### Simulation API — `/api/simulation`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/simulation/profiles` | Generate agent profiles |
| POST | `/api/simulation/config` | Generate simulation config |
| POST | `/api/simulation/run` | Start a simulation run |
| GET | `/api/simulation/run/:id/status` | Get live run status |
| POST | `/api/simulation/run/:id/stop` | Stop a running simulation |
| GET | `/api/simulation/run/:id/history` | Get full action history |

### Report API — `/api/report`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/report/generate` | Generate analytical report |
| GET | `/api/report/:id` | Get a completed report |
| POST | `/api/report/:id/chat` | Interactive Q&A with report agent |

---

## Configuration Reference

All configuration is managed via the root `.env` file:

| Variable | Default | Description |
|---|---|---|
| `LLM_API_KEY` | required | Primary LLM API key |
| `LLM_BASE_URL` | `https://api.openai.com/v1` | Primary LLM base URL |
| `LLM_MODEL_NAME` | `gpt-4o-mini` | Primary LLM model name |
| `LLM_BOOST_API_KEY` | optional | High-power LLM for reports |
| `LLM_BOOST_BASE_URL` | optional | Boost LLM base URL |
| `LLM_BOOST_MODEL_NAME` | optional | Boost LLM model name |
| `ZEP_API_KEY` | required | Zep Cloud API key |
| `FLASK_HOST` | `0.0.0.0` | Flask bind host |
| `FLASK_PORT` | `5001` | Flask bind port |
| `FLASK_DEBUG` | `True` | Flask debug mode |
| `OASIS_DEFAULT_MAX_ROUNDS` | `10` | Default simulation rounds |
| `REPORT_AGENT_MAX_TOOL_CALLS` | `5` | Max tool calls per report cycle |
| `REPORT_AGENT_MAX_REFLECTION_ROUNDS` | `2` | Report reflection depth |
| `REPORT_AGENT_TEMPERATURE` | `0.5` | Report LLM temperature |

---

## Available Scripts

From the **project root**:

| Command | Description |
|---|---|
| `npm run dev` | Start both frontend and backend concurrently |
| `npm run backend` | Start the Flask backend only |
| `npm run frontend` | Start the Vite frontend only |
| `npm run setup` | Install root + frontend Node dependencies |
| `npm run setup:backend` | Install backend Python dependencies via uv |
| `npm run setup:all` | Full install (Node + Python) |
| `npm run build` | Build the frontend for production |

From the **`backend/` directory**:

| Command | Description |
|---|---|
| `uv run python run.py` | Run the Flask server directly |
| `uv run python test_llm.py` | Test LLM connectivity |

---

## Internationalisation (i18n)

AgentixGov supports **English** and **Chinese (Simplified)** out of the box.

- Translation files live in `locales/en.json` and `locales/zh.json`
- The `LanguageSwitcher` component in the UI lets users toggle between languages at any time
- The backend also has locale support via `utils/locale.py`

To add a new language:
1. Add a new `xx.json` translation file to `locales/`
2. Register it in `locales/languages.json`
3. Import and register it in `frontend/src/i18n/`

---

## UI Design

The frontend uses a **dark glassmorphism** aesthetic inspired by government telemetry dashboards:

- **Color palette**: Deep navy background (`#050a14`), ocean blue accent (`#00e5ff`), alert red (`#ff3366`), amber orange (`#ff9900`)
- **Glassmorphism panels**: Frosted-glass cards with `backdrop-filter: blur(12px)`
- **Telemetry grid overlay**: Subtle CSS grid background for a command-centre feel
- **Typography**: Inter, Orbitron, Space Grotesk (Google Fonts)
- **Graph visualisation**: Interactive D3.js force-directed graph with zoom, pan, and node selection

---

## Security Notes

- The `.env` file is listed in `.gitignore` and should **never** be committed to version control.
- CORS is configured to allow all origins on `/api/*` by default. Restrict this in production.
- File uploads are sandboxed to `backend/uploads/` with UUID-prefixed filenames to prevent path traversal.
- Allowed upload types are strictly limited to: `pdf`, `md`, `txt`, `markdown`.

---

## Troubleshooting

**Backend fails to start — "Configuration errors"**
Make sure `.env` exists at the project root and both `LLM_API_KEY` and `ZEP_API_KEY` are set.

**Windows console encoding issues**
The backend automatically configures UTF-8 encoding on Windows at startup. Use Windows Terminal for best results.

**Simulation subprocess crashes silently**
Check `backend/logs/` for detailed error output. The `SimulationRunner` registers a cleanup handler so all subprocesses are terminated cleanly on server shutdown.

**Graph not loading**
Verify your `ZEP_API_KEY` is valid and your Zep Cloud account is active. Check the browser console and `backend/logs/` for API errors.

---

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

See [LICENSE](./LICENSE) for the full text.

---

## Author

**Dheeraj Patel**
- GitHub: [@dheerajpatel3448w](https://github.com/dheerajpatel3448w)

---

*Built with AgentixGov — turning policy documents into living social simulations.*
