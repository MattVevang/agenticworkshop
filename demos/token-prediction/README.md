# Token Prediction Visualizer

A live demo that shows how Large Language Models generate text one token at a time.  
Built for the **Agentic AI 101** workshop — designed to look great on a projector.

![Dark theme, two-panel layout](https://img.shields.io/badge/theme-dark%20mode-0B101A)
![Flask](https://img.shields.io/badge/backend-Flask-22D3EE)
![Ollama](https://img.shields.io/badge/LLM-Ollama-A78BFA)

## What It Shows Students

| Feature | Description |
|---------|-------------|
| **Token-by-token streaming** | Text appears live with a typewriter cursor |
| **Per-token timing** | Each token shows how many milliseconds it took |
| **Speed chart** | Real-time sparkline of tokens/second |
| **Conceptual probabilities** | Animated bar charts explaining how the model picks the next token |
| **Multiple models** | Dropdown lists every model installed in Ollama |

## Prerequisites

- **Python 3.9+**
- **Ollama** running locally — <https://ollama.com>
- At least one model pulled, e.g.:
  ```bash
  ollama pull llama3.2:3b
  ```

## Quick Start

```bash
cd demos/token-prediction

# Create a virtual environment (optional but recommended)
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open **http://localhost:5001** in your browser.

## Configuration

| Environment Variable | Default | Description |
|----------------------|---------|-------------|
| `OLLAMA_URL` | `http://localhost:11434` | Base URL for the Ollama API |
| `FLASK_PORT` | `5001` | Port the demo runs on |

Example:

```bash
set OLLAMA_URL=http://192.168.1.50:11434
python app.py
```

## Presenter Tips

1. **Open the app full-screen** (F11 in most browsers) — the dark theme is projector-friendly.
2. **Start with a simple prompt** like `"The capital of France is"` — students instantly see the model complete it.
3. **Point out the right panel** — explain that the bar charts show *conceptual* probabilities (labelled clearly in the UI).
4. **Try code generation** — use `"def fibonacci(n):"` to show the model writing code token by token.
5. **Adjust max tokens** — the number input controls how many tokens to generate; keep it low (30–60) for quick demos.

## Architecture

```
Browser  ──SSE──▶  Flask /api/generate  ──stream──▶  Ollama /api/generate
                        │
                        ▼
                  Token-by-token JSON events
                  { token, elapsed_ms, tokens_per_second, done }
```

The Flask server acts as a thin SSE proxy — it streams Ollama's response and enriches each token with timing metadata.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| "Cannot connect to Ollama" | Make sure `ollama serve` is running |
| No models in dropdown | Run `ollama pull llama3.2:3b` first |
| Slow generation | Use a smaller model like `llama3.2:1b` or `phi3:mini` |
| Port conflict | Set `FLASK_PORT=5002` before running |
