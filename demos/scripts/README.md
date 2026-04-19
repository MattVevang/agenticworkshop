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
python model-speed-comparison.py --models tinyllama:1.1b mistral:7b
python model-speed-comparison.py --show-responses
```

## Tips

- Run `ollama-health-check.py` **before** the workshop to catch setup issues
- Run `model-speed-comparison.py` **during** the workshop to show students how model size affects speed and quality
- Both scripts accept `--base-url` if Ollama is running on a different machine
