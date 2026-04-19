#!/usr/bin/env python3
"""
Model Speed Comparison — Agentic AI 101 Workshop Demo

Sends the same prompt to multiple Ollama models and times each response,
printing a formatted comparison table.

Usage:
    python model-speed-comparison.py
    python model-speed-comparison.py --prompt "Write a haiku about coding"
    python model-speed-comparison.py --models llama3.2:1b llama3.1:8b
    python model-speed-comparison.py --base-url http://192.168.1.100:11434
"""

import argparse
import json
import sys
import time

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package is required. Install it with:")
    print("  pip install requests")
    sys.exit(1)

DEFAULT_MODELS = [
    "llama3.2:1b",
    "llama3.2:3b",
    "llama3.1:8b",
    "mistral:7b",
]

DEFAULT_PROMPT = "Explain what artificial intelligence is in exactly 3 sentences."

DEFAULT_BASE_URL = "http://localhost:11434"


def get_available_models(base_url):
    """Fetch the list of models currently available in Ollama."""
    try:
        resp = requests.get(f"{base_url}/api/tags", timeout=10)
        resp.raise_for_status()
        return [m["name"] for m in resp.json().get("models", [])]
    except Exception:
        return []


def benchmark_model(base_url, model, prompt):
    """
    Send a prompt to a model via Ollama's streaming API.
    Returns a dict with timing info and the generated text.
    """
    url = f"{base_url}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True,
    }

    result = {
        "model": model,
        "status": "error",
        "time_to_first_token": None,
        "total_time": None,
        "tokens": 0,
        "tokens_per_sec": 0.0,
        "response": "",
        "error": None,
    }

    try:
        start_time = time.perf_counter()
        first_token_time = None

        with requests.post(url, json=payload, stream=True, timeout=300) as resp:
            resp.raise_for_status()

            for line in resp.iter_lines():
                if not line:
                    continue

                chunk = json.loads(line)

                if "error" in chunk:
                    result["error"] = chunk["error"]
                    return result

                token_text = chunk.get("response", "")
                if token_text and first_token_time is None:
                    first_token_time = time.perf_counter()

                result["response"] += token_text
                if token_text:
                    result["tokens"] += 1

                if chunk.get("done", False):
                    break

        end_time = time.perf_counter()

        result["status"] = "ok"
        result["total_time"] = end_time - start_time
        if first_token_time is not None:
            result["time_to_first_token"] = first_token_time - start_time
        if result["total_time"] > 0 and result["tokens"] > 0:
            result["tokens_per_sec"] = result["tokens"] / result["total_time"]

    except requests.exceptions.ConnectionError:
        result["error"] = "Connection refused — is Ollama running?"
    except requests.exceptions.Timeout:
        result["error"] = "Request timed out (>300s)"
    except Exception as e:
        result["error"] = str(e)

    return result


def print_results(results, prompt):
    """Print a formatted comparison table."""
    print()
    print("=" * 80)
    print("  MODEL SPEED COMPARISON")
    print("=" * 80)
    print(f"  Prompt: \"{prompt}\"")
    print("-" * 80)
    print()

    header = f"{'Model':<22} {'Status':<8} {'First Token':>12} {'Total Time':>12} {'Tokens':>8} {'Tok/sec':>10}"
    print(header)
    print("-" * len(header))

    for r in results:
        if r["status"] == "ok":
            ttft = f"{r['time_to_first_token']:.2f}s" if r["time_to_first_token"] else "n/a"
            total = f"{r['total_time']:.2f}s" if r["total_time"] else "n/a"
            tps = f"{r['tokens_per_sec']:.1f}"
            print(f"{r['model']:<22} {'✓ ok':<8} {ttft:>12} {total:>12} {r['tokens']:>8} {tps:>10}")
        else:
            err = r["error"] or "unknown error"
            if len(err) > 40:
                err = err[:37] + "..."
            print(f"{r['model']:<22} {'✗ fail':<8} {'—':>12} {'—':>12} {'—':>8} {'—':>10}")
            print(f"  └─ {err}")

    print()

    ok_results = [r for r in results if r["status"] == "ok"]
    if ok_results:
        fastest = min(ok_results, key=lambda r: r["total_time"])
        most_tps = max(ok_results, key=lambda r: r["tokens_per_sec"])
        quickest_start = min(ok_results, key=lambda r: r["time_to_first_token"] or float("inf"))

        print("  🏆 Results:")
        print(f"     Fastest total:      {fastest['model']} ({fastest['total_time']:.2f}s)")
        print(f"     Fastest first token: {quickest_start['model']} ({quickest_start['time_to_first_token']:.2f}s)")
        print(f"     Highest throughput:  {most_tps['model']} ({most_tps['tokens_per_sec']:.1f} tok/s)")
        print()

    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="Compare response speed across multiple Ollama models.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n  python model-speed-comparison.py --models llama3.2:1b llama3.1:8b",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help=f"Prompt to send to each model (default: \"{DEFAULT_PROMPT}\")",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=None,
        help="Models to test (default: llama3.2:1b llama3.2:3b llama3.1:8b mistral:7b)",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Ollama API base URL (default: {DEFAULT_BASE_URL})",
    )
    parser.add_argument(
        "--show-responses",
        action="store_true",
        help="Print each model's full response text after the table",
    )

    args = parser.parse_args()

    models_to_test = args.models if args.models else DEFAULT_MODELS

    # Check Ollama connectivity
    print(f"\n🔍 Connecting to Ollama at {args.base_url} ...")
    available = get_available_models(args.base_url)
    if not available:
        print("⚠️  Could not reach Ollama or no models found.")
        print(f"   Make sure Ollama is running at {args.base_url}")
        print("   Start it with: ollama serve")
        sys.exit(1)

    print(f"✓  Found {len(available)} model(s): {', '.join(available)}")

    # Filter to models that are actually available
    skipped = []
    testing = []
    for m in models_to_test:
        # Check if model name matches (allow partial matching for tags)
        if any(m == a or m.split(":")[0] == a.split(":")[0] for a in available):
            testing.append(m)
        else:
            skipped.append(m)

    if skipped:
        print(f"⚠️  Skipping models not found locally: {', '.join(skipped)}")

    if not testing:
        print("❌ None of the requested models are available. Pull some models first:")
        print(f"   ollama pull {models_to_test[0]}")
        sys.exit(1)

    print(f"\n🏁 Benchmarking {len(testing)} model(s)...\n")

    results = []
    for i, model in enumerate(testing, 1):
        print(f"  [{i}/{len(testing)}] Testing {model} ...", end="", flush=True)
        result = benchmark_model(args.base_url, model, args.prompt)
        if result["status"] == "ok":
            print(f" ✓ {result['total_time']:.2f}s ({result['tokens']} tokens)")
        else:
            print(f" ✗ {result['error']}")
        results.append(result)

    print_results(results, args.prompt)

    if args.show_responses:
        print("\n📝 Full Responses:\n")
        for r in results:
            print(f"--- {r['model']} ---")
            if r["status"] == "ok":
                print(r["response"].strip())
            else:
                print(f"(error: {r['error']})")
            print()


if __name__ == "__main__":
    main()
