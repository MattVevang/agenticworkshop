# Agentic AI 101 Workshop

Hands-on workshop for high school students exploring AI, large language models, and agentic development workflows. Includes a fully self-hosted lab environment powered by **Ollama** and **Open WebUI** running on a local GPU server.

## Purpose

This workshop is designed for high school students who are:
- Curious about how AI actually works under the hood
- Want to test, compare, and challenge AI models hands-on
- Interested in practical workflows, not just hype

The goal: make AI understandable, inspectable, and discussion-friendly — with real models running on real hardware in the room.

## What We Cover

| Topic | Description |
|-------|-------------|
| **AI Foundations** | What models are, how they're trained, parameters vs tokens |
| **Model Comparison** | Small vs large models, different families, speed vs quality |
| **Prompt Engineering** | How to write effective prompts and why it matters |
| **Hallucinations** | Why AI makes things up and how to catch it |
| **Privacy & Ethics** | Local vs cloud, who sees your data, responsible use |
| **Multimodal AI** | Models that understand images, not just text |
| **Agentic Workflows** | MCP, tool use, and how agents do real work |
| **Hands-On Labs** | 9 interactive labs run through Open WebUI |

## Repository Structure

```
├── labs/                        # 9 student lab exercises (markdown)
│   ├── lab-01-non-determinism.md
│   ├── lab-02-model-comparison.md
│   ├── lab-03-prompt-engineering.md
│   ├── lab-04-hallucination-detection.md
│   ├── lab-05-creative-and-multimodal.md
│   ├── lab-06-local-vs-cloud-discussion.md
│   ├── lab-07-bias-and-fairness.md
│   ├── lab-08-real-world-scenarios.md
│   └── lab-09-agents-and-tools.md       # Capstone: web search + tools (port 3001)
├── demos/
│   ├── token-prediction/        # Live token prediction visualizer (presenter tool)
│   └── scripts/                 # Model speed comparison, health check & warm-up utilities
├── resources/
│   ├── glossary.md              # Teen-friendly AI glossary (21 terms, quick-jump index)
│   ├── further-reading.md       # Curated learning links
│   ├── openwebui-quickstart.md  # Student quick-reference for Open WebUI
│   ├── ai-ethics-for-students.md # AI ethics & academic honesty guide
│   ├── spotting-ai-content.md   # How to spot AI-generated text, images & deepfakes
│   ├── cost-comparison.md       # Local vs cloud AI cost breakdown
│   ├── whats-next.md            # Career & learning pathways after the workshop
│   ├── model-cards.md           # Trading-card style model profiles
│   ├── prompt-disasters.md      # Funny bad AI outputs (educational)
│   ├── workshop-feedback.md     # Feedback collection & polling setup
│   └── ai-news-template.md     # Template for current AI news at workshop start
├── docker/
│   ├── docker-compose.yml       # Open WebUI container (no tools) — port 3000
│   ├── tools/
│   │   ├── docker-compose.yml   # Tool-enabled Open WebUI (web search) — port 3001
│   │   └── README.md            # Agentic instance guide & demo walkthrough
│   └── TROUBLESHOOTING.md       # Docker & workshop troubleshooting guide
├── generate_agentic_ai_101_workshop.py  # PowerPoint slide deck generator (25 slides)
└── .github/                     # Workflows and Copilot config
```

## Lab Server Setup

The workshop runs on a central server that students connect to via their browsers. No software installation needed on student devices.

### Prerequisites (server)

- **GPU**: NVIDIA GPU with ≥16GB VRAM (workshop server: RTX 5090, 32GB)
- **RAM**: ≥32GB system memory
- **Software**: Docker, Ollama (installed on host)

### 1. Start Ollama

Ollama should be running on the host and bound to all interfaces:

```powershell
# Set Ollama to listen on all interfaces (required for Docker connectivity)
# This should already be set as a system/user environment variable:
#   OLLAMA_HOST=0.0.0.0:11434
ollama serve
```

#### Recommended Ollama Environment Variables

Set these **before** starting `ollama serve` (as system or user environment variables on the host):

| Variable | Recommended Value | Purpose |
|----------|-------------------|---------|
| `OLLAMA_HOST` | `0.0.0.0:11434` | Accept connections from Docker and student devices |
| `OLLAMA_NUM_PARALLEL` | `4` | Handle up to 4 concurrent requests per model |
| `OLLAMA_MAX_LOADED_MODELS` | `2` | Keep up to 2 models resident in VRAM simultaneously |
| `OLLAMA_KEEP_ALIVE` | `2m` | Unload models 2 min after last use (cold loads are ~1s on NVMe) |
| `OLLAMA_CONTEXT_LENGTH` | `8192` | Reduce from default for workshop (short prompts don't need 128k) |

> **💡 Why this matters:** With 20+ students hitting the server simultaneously, you need fast concurrent responses and clean VRAM management. Models cold-load in ~1–1.5s on NVMe, so aggressive unloading prevents VRAM contention without meaningful delays. See [`resources/workshop-tuning-guide.md`](resources/workshop-tuning-guide.md) for full benchmark data and revert instructions.

### 2. Pull Models

Student-facing models (curated for the labs):

```powershell
ollama pull llama3.2:1b          # Drag race — small Llama (~1.6 GB VRAM)
ollama pull llama3.2:3b          # Default workshop model — fast & capable (~2.3 GB VRAM)
ollama pull llama3.1:8b          # Drag race — large Llama (~4.8 GB VRAM)
ollama pull mistral:7b           # Hallucination lab — reliably hallucinates (~8.3 GB VRAM)
ollama pull llava:7b             # Multimodal — can analyze images (~8.4 GB VRAM)
```

> **⚡ Performance note:** The three Llama models were benchmarked for concurrent classroom use. Even with 5 simultaneous users, llama3.1:8b responds in under 2.5 seconds. The default model (llama3.2:3b) handles 5 concurrent users with a max of 1.4 seconds. See [`resources/workshop-tuning-guide.md`](resources/workshop-tuning-guide.md).

Instructor demo models (larger, for live presentations):

```powershell
ollama pull gemma4:26b
ollama pull qwen3.5:27b
ollama pull deepseek-r1:32b
```

### 3. Start Open WebUI

```powershell
cd docker
docker compose up -d
```

Open WebUI will be available at **http://\<server-ip\>:3000**. Authentication is disabled for frictionless lab use (shared kiosk mode — all users see the same interface).

> **🛠️ Optional — tool-enabled "agentic" instance (port 3001):** A second, parallel Open WebUI
> instance gives a tool-capable model (`qwen3.6:35b`) **web search + native tool calling**, so it
> can answer **current-events** questions the older lab models can't. Run the labs on the no-tools
> instance (3000) first, then transition to 3001 to show how tools "change the game." See
> [`docker/tools/README.md`](docker/tools/README.md). Quick start:
>
> ```powershell
> cd docker\tools
> docker compose up -d                              # -> http://<server-ip>:3001
> python demos/scripts/openwebui-tools-setup.py     # enable + verify web search
> ```

### 4. Verify Setup

```powershell
python demos/scripts/ollama-health-check.py
```

### 5. Warm Up Models (Pre-Workshop)

Pre-load student-facing models into GPU memory so the first responses are fast:

```powershell
python demos/scripts/ollama-warmup.py
```

This sends a minimal prompt to each model, forcing it into VRAM. Run this 10–15 minutes before students arrive.

## Pre-Workshop Checklist

Run through this checklist the morning of (or evening before) the workshop:

- [ ] **Ollama running** with recommended environment variables set
- [ ] **All models pulled** (student-facing + instructor demo models)
- [ ] **Health check passes**: `python demos/scripts/ollama-health-check.py`
- [ ] **Models warmed up**: `python demos/scripts/ollama-warmup.py`
- [ ] **Open WebUI running**: `cd docker && docker compose up -d`
- [ ] **Browser test**: navigate to `http://<server-ip>:3000` from a student device
- [ ] **Server IP visible**: write it on the board or project it
- [ ] **Lab handouts ready**: print or share links to `labs/README.md`
- [ ] **Feedback form created** (optional): see `resources/workshop-feedback.md`

> **See also:** [`docker/TROUBLESHOOTING.md`](docker/TROUBLESHOOTING.md) for common issues and fixes.

### Student Access

Students open their browser and navigate to:

```
http://<server-ip>:3000
```

No login required. See [`resources/openwebui-quickstart.md`](resources/openwebui-quickstart.md) for the student quick-start guide.

## Model Inventory

| Model | Size | Best For | Lab Use |
|-------|------|----------|---------|
| `llama3.2:1b` | 1.2 GB | Speed demos, quality contrast | Labs 2, 5 |
| `llama3.2:3b` | 2.0 GB | **Default model** — fast & capable | Labs 1, 2, 3, 5, 7, 8, 9 |
| `llama3.1:8b` | 4.7 GB | Drag race large model, quality | Lab 2 |
| `mistral:7b` | 4.4 GB | Hallucination detection (validated) | Lab 4 |
| `llava:7b` | 4.7 GB | Image understanding | Lab 5 |

## Labs Overview

| Lab | Title | Time | Focus |
|-----|-------|------|-------|
| 1 | [Non-Determinism](labs/lab-01-non-determinism.md) | 15 min | Same prompt → different results |
| 2 | [Model Comparison](labs/lab-02-model-comparison.md) | 20 min | Same prompt → different models |
| 3 | [Prompt Engineering](labs/lab-03-prompt-engineering.md) | 20 min | Bad vs good prompts |
| 4 | [Hallucination Detection](labs/lab-04-hallucination-detection.md) | 20 min | Catching AI mistakes |
| 5 | [Creative & Multimodal](labs/lab-05-creative-and-multimodal.md) | 20 min | Images, stories, code |
| 6 | [Local vs Cloud](labs/lab-06-local-vs-cloud-discussion.md) | 15 min | Privacy and tradeoffs |
| 7 | [Bias & Fairness](labs/lab-07-bias-and-fairness.md) | 20 min | AI bias and responsibility |
| 8 | [Real-World Scenarios](labs/lab-08-real-world-scenarios.md) | 20 min | Practical AI problem-solving |
| 9 | [Agents & Tools](labs/lab-09-agents-and-tools.md) | 20–25 min | Capstone: web search + tools (port 3001) |

## Presenter Tools

### Token Prediction Visualizer

A live demo tool that shows students how LLMs generate text token-by-token:

```powershell
cd demos\token-prediction
pip install -r requirements.txt
python app.py
# Opens at http://localhost:5001
```

### Model Speed Comparison

Benchmark models side-by-side:

```powershell
python demos\scripts\model-speed-comparison.py
```

## Regenerating the Slide Deck

The workshop PowerPoint (25 slides, "Neon Mission Control" theme) is generated from code:

```powershell
pip install python-pptx
python generate_agentic_ai_101_workshop.py
```

Output: `Agentic_AI_101_Workshop.pptx`

> **Tip**: Add `*.pptx` and `~$*` to `.gitignore` to avoid committing generated binaries.

## Accessibility Notes

- **Markdown heading hierarchy**: All lab and resource documents use proper heading hierarchy (`#` → `##` → `###`) for screen reader compatibility
- **Images**: When adding images to slides or documents, include descriptive alt-text. The `resources/images/` directory is prepared for screenshot additions
- **Token prediction demo**: The neon theme uses color to convey information in probability bars. For color-blind students, the presenter should verbally describe the relative bar lengths. The bars also include percentage labels as a non-color indicator
- **Lab documents**: All exercises use text-based tables and structured formats that work with assistive technology

## Copilot Cloud Agent Setup

For **personal-account repositories**, Copilot cloud agent access is managed in GitHub account settings:

1. GitHub profile menu → **Copilot settings**
2. **Cloud agent** policy
3. Set repository access to include this repo
