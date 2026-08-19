# 🎬 Demo Scripts

Utility scripts for the **Agentic AI 101** workshop. These help instructors set up, verify, and demonstrate the Ollama + Open WebUI environment.

## Prerequisites

- Python 3.8+
- `requests` library: `pip install requests`
- Ollama running locally or on a network server

## Scripts

### 🩺 `ollama-health-check.py`

Pre-workshop setup verification. Checks that Ollama is running, lists available models, tests inference, and reports GPU/memory info.

```bash
python ollama-health-check.py
python ollama-health-check.py --base-url http://192.168.1.100:11434
python ollama-health-check.py --test-model mistral:7b
```

### 🏎️ `model-speed-comparison.py`

Live demo script that benchmarks multiple models side by side. Sends the same prompt to each model, measures time-to-first-token and total generation time, and prints a comparison table.

```bash
python model-speed-comparison.py
python model-speed-comparison.py --prompt "Write a haiku about coding"
python model-speed-comparison.py --models llama3.2:1b llama3.1:8b
python model-speed-comparison.py --show-responses
```

### 🔒 `openwebui-hide-models.py`

Hides non-workshop models from the Open WebUI dropdown so students only see the 5 workshop models. Run after starting the container.

```bash
python openwebui-hide-models.py
python openwebui-hide-models.py --unhide              # Revert: show all models
python openwebui-hide-models.py --webui-url http://biglittle.local:3000
```

### 🛠️ `openwebui-tools-setup.py`

Configures and verifies the **tool-enabled** Open WebUI instance (port **3001** — see
[`docker/tools/`](../../docker/tools/README.md)). For each tool-capable model (default:
`qwen3.6:35b`, `qwen3.6:27b`) it turns on the Web Search capability + native (agentic) function
calling and makes web search a default feature, then verifies the model actually reaches for the
`search_web` tool.

```bash
python openwebui-tools-setup.py                       # configure + verify
python openwebui-tools-setup.py --verify-only         # just run the current-events check
python openwebui-tools-setup.py --no-default-on       # capability on, but not auto-on per chat
python openwebui-tools-setup.py --revert              # remove the per-model config entries
python openwebui-tools-setup.py --webui-url http://biglittle.local:3001
```

## Tips

- Run `ollama-health-check.py` **before** the workshop to catch setup issues
- Run `model-speed-comparison.py` **during** the workshop to show students how model size affects speed and quality
- Both scripts accept `--base-url` if Ollama is running on a different machine
