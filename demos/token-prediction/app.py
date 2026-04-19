"""
Token Prediction Visualization Demo
====================================
A Flask web app that streams LLM token generation from a local Ollama instance,
visualizing the token-by-token process for educational purposes.

Usage:
    pip install -r requirements.txt
    python app.py

Environment variables:
    OLLAMA_URL  – Base URL for Ollama (default: http://localhost:11434)
    FLASK_PORT  – Port for this app (default: 5001)
"""

import json
import os
import time

import requests
from flask import Flask, Response, jsonify, render_template, request, stream_with_context

app = Flask(__name__)

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
DEFAULT_MODEL = "llama3.2:3b"

# ---------------------------------------------------------------------------
# Pre-computed conceptual probability data
# ---------------------------------------------------------------------------
# Shown alongside real token generation to illustrate what the model "considers"
# at each step. Clearly labelled as a conceptual example in the UI.

CONCEPTUAL_EXAMPLES = [
    {
        "context": '"The capital of France is"',
        "candidates": [
            {"token": " Paris", "prob": 92.1},
            {"token": " Lyon", "prob": 3.4},
            {"token": " the", "prob": 2.0},
            {"token": " located", "prob": 1.3},
            {"token": " known", "prob": 0.8},
        ],
    },
    {
        "context": '"Once upon a"',
        "candidates": [
            {"token": " time", "prob": 96.7},
            {"token": " day", "prob": 1.2},
            {"token": " hill", "prob": 0.8},
            {"token": " warm", "prob": 0.5},
            {"token": " starry", "prob": 0.3},
        ],
    },
    {
        "context": '"Water boils at 100 degrees"',
        "candidates": [
            {"token": " Celsius", "prob": 78.5},
            {"token": " C", "prob": 12.3},
            {"token": " centigrade", "prob": 4.1},
            {"token": " Fahr", "prob": 3.0},
            {"token": " when", "prob": 1.2},
        ],
    },
    {
        "context": '"The quick brown fox"',
        "candidates": [
            {"token": " jumps", "prob": 72.4},
            {"token": " jumped", "prob": 14.2},
            {"token": " ran", "prob": 5.1},
            {"token": " is", "prob": 4.8},
            {"token": " was", "prob": 2.3},
        ],
    },
    {
        "context": '"def hello_world("',
        "candidates": [
            {"token": "):", "prob": 55.3},
            {"token": "name", "prob": 22.1},
            {"token": "self", "prob": 10.4},
            {"token": "msg", "prob": 6.7},
            {"token": "args", "prob": 3.2},
        ],
    },
]


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.route("/")
def index():
    """Serve the single-page UI."""
    return render_template(
        "index.html",
        default_model=DEFAULT_MODEL,
        conceptual_examples=json.dumps(CONCEPTUAL_EXAMPLES),
    )


@app.route("/api/models")
def list_models():
    """Proxy Ollama's model list so the front-end can populate a selector."""
    try:
        resp = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        resp.raise_for_status()
        data = resp.json()
        models = [m["name"] for m in data.get("models", [])]
        return jsonify({"models": models})
    except requests.RequestException as exc:
        return jsonify({"error": str(exc), "models": []}), 502


@app.route("/api/generate", methods=["POST"])
def generate():
    """
    SSE endpoint – streams token events from Ollama to the browser.

    Expected JSON body:
        { "prompt": "...", "model": "llama3.2:3b", "num_predict": 200 }

    Each SSE message is a JSON object:
        { "token": " Paris", "done": false, "elapsed_ms": 42 }
    The final message has done=true and includes summary stats.
    """
    body = request.get_json(force=True)
    prompt = body.get("prompt", "")
    model = body.get("model", DEFAULT_MODEL)
    num_predict = body.get("num_predict", 200)

    if not prompt.strip():
        return jsonify({"error": "prompt is required"}), 400

    ollama_payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,
        "options": {
            "num_predict": num_predict,
        },
    }

    def event_stream():
        token_count = 0
        start_time = time.perf_counter()
        last_token_time = start_time

        try:
            with requests.post(
                f"{OLLAMA_URL}/api/generate",
                json=ollama_payload,
                stream=True,
                timeout=120,
            ) as resp:
                resp.raise_for_status()

                for raw_line in resp.iter_lines():
                    if not raw_line:
                        continue
                    chunk = json.loads(raw_line)
                    now = time.perf_counter()

                    token_text = chunk.get("response", "")
                    done = chunk.get("done", False)

                    elapsed_ms = round((now - last_token_time) * 1000, 1)
                    total_elapsed = round((now - start_time) * 1000, 1)
                    last_token_time = now

                    if token_text:
                        token_count += 1

                    tps = round(token_count / ((now - start_time) or 0.001), 1)

                    event_data = {
                        "token": token_text,
                        "done": done,
                        "elapsed_ms": elapsed_ms,
                        "total_elapsed_ms": total_elapsed,
                        "token_count": token_count,
                        "tokens_per_second": tps,
                    }

                    # Include Ollama summary fields when generation is done
                    if done:
                        for key in (
                            "total_duration",
                            "load_duration",
                            "prompt_eval_count",
                            "eval_count",
                            "eval_duration",
                        ):
                            if key in chunk:
                                event_data[key] = chunk[key]

                    yield f"data: {json.dumps(event_data)}\n\n"

                    if done:
                        break

        except requests.ConnectionError:
            yield f"data: {json.dumps({'error': 'Cannot connect to Ollama. Is it running?', 'done': True})}\n\n"
        except requests.RequestException as exc:
            yield f"data: {json.dumps({'error': str(exc), 'done': True})}\n\n"

    return Response(
        stream_with_context(event_stream()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", 5001))
    print(f"Token Prediction Demo starting on http://localhost:{port}")
    print(f"Ollama endpoint: {OLLAMA_URL}")
    app.run(host="0.0.0.0", port=port, debug=True)
