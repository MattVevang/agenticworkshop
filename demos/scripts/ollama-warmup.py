#!/usr/bin/env python3
"""
Ollama Model Warm-Up — Pre-Workshop Model Preloader

Loads all student-facing models into GPU memory before the workshop starts,
ensuring fast first responses when students begin their labs.

Usage:
    python ollama-warmup.py
    python ollama-warmup.py --base-url http://192.168.1.100:11434
    python ollama-warmup.py --models tinyllama:1.1b mistral:7b llava:7b
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

DEFAULT_BASE_URL = "http://localhost:11434"

# Models to preload in priority order (most-used first)
DEFAULT_MODELS = [
    "mistral:7b",
    "llama3.2:3b",
    "tinyllama:1.1b",
    "llava:7b",
]

WARMUP_PROMPT = "Hello"


def get_available_models(base_url):
    """Fetch models currently downloaded in Ollama."""
    try:
        resp = requests.get(f"{base_url}/api/tags", timeout=10)
        resp.raise_for_status()
        return [m["name"] for m in resp.json().get("models", [])]
    except Exception as e:
        print(f"  ❌ Could not list models: {e}")
        return []


def get_loaded_models(base_url):
    """Check which models are currently loaded in memory."""
    try:
        resp = requests.get(f"{base_url}/api/ps", timeout=10)
        resp.raise_for_status()
        return [m["name"] for m in resp.json().get("models", [])]
    except Exception:
        return []


def warmup_model(base_url, model):
    """Send a minimal prompt to force the model into memory."""
    url = f"{base_url}/api/generate"
    payload = {
        "model": model,
        "prompt": WARMUP_PROMPT,
        "stream": False,
    }

    try:
        start = time.perf_counter()
        resp = requests.post(url, json=payload, timeout=300)
        resp.raise_for_status()
        elapsed = time.perf_counter() - start

        data = resp.json()
        if "error" in data:
            return False, data["error"]
        return True, f"{elapsed:.1f}s"
    except requests.exceptions.Timeout:
        return False, "timed out (>300s)"
    except Exception as e:
        return False, str(e)


def check_env_recommendations(base_url):
    """Print recommendations for Ollama environment variables."""
    print("\n📋 Recommended Ollama Environment Variables for Workshop:")
    print("   (Set these before starting 'ollama serve')\n")

    env_vars = [
        ("OLLAMA_HOST", "0.0.0.0:11434", "Allow connections from Docker and student devices"),
        ("OLLAMA_NUM_PARALLEL", "4", "Handle up to 4 concurrent requests per model"),
        ("OLLAMA_MAX_LOADED_MODELS", "2", "Keep up to 2 models in VRAM simultaneously"),
        ("OLLAMA_KEEP_ALIVE", "2m", "Unload models 2 min after last request (cold loads are ~1s on NVMe)"),
    ]

    for var, value, description in env_vars:
        print(f"   {var}={value}")
        print(f"     └─ {description}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Pre-load Ollama models into GPU memory for the workshop.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Example:\n"
            "  python ollama-warmup.py\n"
            "  python ollama-warmup.py --base-url http://10.0.0.5:11434\n"
            "  python ollama-warmup.py --models mistral:7b llava:7b"
        ),
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Ollama API base URL (default: {DEFAULT_BASE_URL})",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=None,
        help="Specific models to warm up (default: all student-facing models)",
    )

    args = parser.parse_args()
    models_to_load = args.models if args.models else DEFAULT_MODELS

    print()
    print("=" * 60)
    print("  🔥 OLLAMA MODEL WARM-UP")
    print("=" * 60)
    print(f"  Target: {args.base_url}")

    # Check connectivity
    print("\n🔍 Checking Ollama connectivity...")
    try:
        resp = requests.get(f"{args.base_url}/api/version", timeout=10)
        resp.raise_for_status()
        version = resp.json().get("version", "unknown")
        print(f"  ✅ Ollama is running (version {version})")
    except Exception:
        print(f"  ❌ Cannot connect to Ollama at {args.base_url}")
        print("     Start Ollama with: ollama serve")
        sys.exit(1)

    # List available models
    available = get_available_models(args.base_url)
    if not available:
        print("  ❌ No models found. Pull models first.")
        sys.exit(1)

    print(f"  📦 {len(available)} model(s) available locally")

    # Check already loaded
    loaded = get_loaded_models(args.base_url)
    if loaded:
        print(f"  🧠 {len(loaded)} model(s) already in memory: {', '.join(loaded)}")

    # Filter to available models
    to_warmup = []
    skipped = []
    for m in models_to_load:
        if m in available or any(m.split(":")[0] == a.split(":")[0] for a in available):
            to_warmup.append(m)
        else:
            skipped.append(m)

    if skipped:
        print(f"\n  ⚠️  Skipping (not downloaded): {', '.join(skipped)}")

    if not to_warmup:
        print("  ❌ No requested models are available to warm up.")
        sys.exit(1)

    # Warm up models
    print(f"\n🔥 Warming up {len(to_warmup)} model(s)...\n")

    results = {"success": [], "failed": []}
    for i, model in enumerate(to_warmup, 1):
        print(f"  [{i}/{len(to_warmup)}] Loading {model} ...", end="", flush=True)
        ok, detail = warmup_model(args.base_url, model)
        if ok:
            print(f" ✅ loaded ({detail})")
            results["success"].append(model)
        else:
            print(f" ❌ failed ({detail})")
            results["failed"].append(model)

    # Summary
    print()
    print("=" * 60)
    loaded_after = get_loaded_models(args.base_url)
    print(f"  🧠 Models now in memory: {len(loaded_after)}")
    for m in loaded_after:
        print(f"     • {m}")
    print()

    if results["failed"]:
        print(f"  ⚠️  {len(results['failed'])} model(s) failed to load: {', '.join(results['failed'])}")
    else:
        print(f"  🎉 All {len(results['success'])} model(s) loaded successfully!")

    check_env_recommendations(args.base_url)

    print("=" * 60)
    print("  ✅ Workshop environment is warm and ready!")
    print("=" * 60)
    print()

    sys.exit(0 if not results["failed"] else 1)


if __name__ == "__main__":
    main()
