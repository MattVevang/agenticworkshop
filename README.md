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
│   └── lab-09-custom-modelfile.md       # Bonus: Ollama Modelfile customization
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
│   ├── docker-compose.yml       # Open WebUI container definition
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
| `OLLAMA_MAX_LOADED_MODELS` | `3` | Keep up to 3 models resident in VRAM simultaneously |
| `OLLAMA_KEEP_ALIVE` | `2h` | Prevent model unloading during the workshop (default is 5 min) |

> **💡 Why this matters:** With 20+ students hitting the server simultaneously, cold model loads cause long waits. These settings keep models warm and handle concurrent requests.

### 2. Pull Models

Student-facing models (curated for the labs):

```powershell
ollama pull tinyllama:1.1b      # Ultra-fast, shows quality tradeoffs
ollama pull llama3.2:3b          # Small but capable
ollama pull mistral:7b           # Solid mid-size general model
ollama pull llava:7b             # Multimodal — can analyze images
ollama pull qwen3.5:9b           # Strong general model
ollama pull deepseek-r1:14b      # Reasoning-focused model
ollama pull phi4:14b             # Microsoft's model
```

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
| `tinyllama:1.1b` | 637 MB | Speed demos, quality contrast | Labs 1, 2 |
| `llama3.2:3b` | 2.0 GB | Balance of speed and quality | Labs 1, 2, 3 |
| `mistral:7b` | 4.4 GB | General purpose, good default | Labs 2, 3, 4 |
| `llava:7b` | 4.7 GB | Image understanding | Lab 5 |
| `qwen3.5:9b` | 6.6 GB | Strong reasoning | Labs 2, 4 |
| `deepseek-r1:14b` | 9.0 GB | Chain-of-thought reasoning | Labs 2, 4 |
| `phi4:14b` | 9.1 GB | Microsoft model diversity | Lab 2 |

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
| 9 | [Custom Modelfile](labs/lab-09-custom-modelfile.md) | 15 min | Bonus: build an AI personality |

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
