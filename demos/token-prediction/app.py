"""
Token Prediction Visualization Demo
====================================
A Flask web app that streams LLM token generation from a local Ollama instance,
visualizing the real top-k token probabilities for each generated token.

Usage:
    pip install -r requirements.txt
    python app.py

Environment variables:
    OLLAMA_URL  – Base URL for Ollama (default: http://localhost:11434)
    FLASK_PORT  – Port for this app (default: 5001)
"""

import json
import math
import os
import time

import requests
from flask import Flask, Response, jsonify, render_template, request, stream_with_context

app = Flask(__name__)

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
DEFAULT_MODEL = "llama3.2:3b"


@app.route("/")
def index():
    """Serve the single-page UI."""
    return render_template("index.html", default_model=DEFAULT_MODEL)


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
    SSE endpoint – streams token events with real logprobs from Ollama.

    Expected JSON body:
        { "prompt": "...", "model": "llama3.2:3b", "num_predict": 100 }

    Each SSE message is a JSON object with the token, timing, and top-5
    candidate probabilities the model considered before choosing.
    """
    body = request.get_json(force=True)
    prompt = body.get("prompt", "")
    model = body.get("model", DEFAULT_MODEL)
    num_predict = body.get("num_predict", 100)

    if not prompt.strip():
        return jsonify({"error": "prompt is required"}), 400

    ollama_payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,
        "logprobs": True,
        "top_logprobs": 5,
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

                    # Extract real logprobs and convert to percentages
                    logprobs_raw = chunk.get("logprobs", [])
                    if logprobs_raw:
                        entry = logprobs_raw[0]
                        candidates = []
                        for alt in entry.get("top_logprobs", []):
                            prob_pct = math.exp(alt["logprob"]) * 100
                            candidates.append({
                                "token": alt["token"],
                                "prob": round(prob_pct, 2),
                            })
                        # Add "Other" bucket for remaining probability mass
                        top_sum = sum(c["prob"] for c in candidates)
                        if top_sum < 99.9:
                            candidates.append({
                                "token": "…other",
                                "prob": round(100.0 - top_sum, 2),
                            })
                        event_data["candidates"] = candidates

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


if __name__ == "__main__":
    port = int(os.environ.get("FLASK_PORT", 5001))
    print(f"Token Prediction Demo starting on http://localhost:{port}")
    print(f"Ollama endpoint: {OLLAMA_URL}")
    app.run(host="0.0.0.0", port=port, debug=True)
