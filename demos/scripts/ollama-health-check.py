#!/usr/bin/env python3
"""
Ollama Health Check — Agentic AI 101 Workshop Setup Verification

Verifies that Ollama is running, lists available models, tests inference,
and reports GPU info. Run this before the workshop to make sure everything
is ready.

Usage:
    python ollama-health-check.py
    python ollama-health-check.py --base-url http://192.168.1.100:11434
    python ollama-health-check.py --test-model tinyllama:1.1b
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
TEST_PROMPT = "Say hello in exactly 5 words."


def check_pass(label, detail=""):
    """Print a passing check."""
    msg = f"  ✅ PASS — {label}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return True


def check_fail(label, detail=""):
    """Print a failing check."""
    msg = f"  ❌ FAIL — {label}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return False


def check_warn(label, detail=""):
    """Print a warning."""
    msg = f"  ⚠️  WARN — {label}"
    if detail:
        msg += f" ({detail})"
    print(msg)


def check_ollama_running(base_url):
    """Check 1: Is Ollama reachable?"""
    print("\n🔍 Check 1: Ollama connectivity")
    try:
        resp = requests.get(f"{base_url}/api/version", timeout=10)
        resp.raise_for_status()
        version_info = resp.json()
        version = version_info.get("version", "unknown")
        return check_pass("Ollama is running", f"version {version}")
    except requests.exceptions.ConnectionError:
        return check_fail(
            "Cannot connect to Ollama",
            f"is it running at {base_url}? Start with: ollama serve"
        )
    except Exception as e:
        return check_fail("Unexpected error connecting to Ollama", str(e))


def check_models_available(base_url):
    """Check 2: Are any models downloaded?"""
    print("\n🔍 Check 2: Available models")
    try:
        resp = requests.get(f"{base_url}/api/tags", timeout=10)
        resp.raise_for_status()
        models = resp.json().get("models", [])

        if not models:
            check_fail("No models found", "pull a model with: ollama pull tinyllama:1.1b")
            return []

        check_pass(f"Found {len(models)} model(s)")
        print()
        print(f"    {'Model':<35} {'Size':>10} {'Quantization':<15} {'Modified'}")
        print(f"    {'-'*35} {'-'*10} {'-'*15} {'-'*20}")

        for m in models:
            name = m.get("name", "unknown")
            size_bytes = m.get("size", 0)
            if size_bytes > 1_000_000_000:
                size_str = f"{size_bytes / 1_000_000_000:.1f} GB"
            elif size_bytes > 1_000_000:
                size_str = f"{size_bytes / 1_000_000:.0f} MB"
            else:
                size_str = f"{size_bytes} B"

            details = m.get("details", {})
            quant = details.get("quantization_level", "—")
            modified = m.get("modified_at", "—")
            if isinstance(modified, str) and "T" in modified:
                modified = modified.split("T")[0]

            print(f"    {name:<35} {size_str:>10} {quant:<15} {modified}")

        return [m["name"] for m in models]

    except Exception as e:
        check_fail("Could not list models", str(e))
        return []


def check_inference(base_url, model):
    """Check 3: Can we actually run inference?"""
    print(f"\n🔍 Check 3: Inference test ({model})")

    url = f"{base_url}/api/generate"
    payload = {
        "model": model,
        "prompt": TEST_PROMPT,
        "stream": True,
    }

    try:
        start_time = time.perf_counter()
        first_token_time = None
        response_text = ""
        token_count = 0

        with requests.post(url, json=payload, stream=True, timeout=120) as resp:
            resp.raise_for_status()

            for line in resp.iter_lines():
                if not line:
                    continue

                chunk = json.loads(line)

                if "error" in chunk:
                    return check_fail("Inference error", chunk["error"])

                text = chunk.get("response", "")
                if text and first_token_time is None:
                    first_token_time = time.perf_counter()

                response_text += text
                if text:
                    token_count += 1

                if chunk.get("done", False):
                    break

        end_time = time.perf_counter()
        total_time = end_time - start_time
        ttft = first_token_time - start_time if first_token_time else 0

        check_pass("Inference working", f"{total_time:.2f}s total, {ttft:.2f}s to first token")
        print(f"    Tokens generated: {token_count}")
        if total_time > 0:
            print(f"    Throughput: {token_count / total_time:.1f} tokens/sec")
        print(f"    Response: \"{response_text.strip()[:100]}{'...' if len(response_text.strip()) > 100 else ''}\"")
        return True

    except requests.exceptions.Timeout:
        return check_fail("Inference timed out", "model may be too large for available hardware")
    except Exception as e:
        return check_fail("Inference failed", str(e))


def check_gpu_info(base_url):
    """Check 4: GPU / system info via Ollama's ps endpoint."""
    print("\n🔍 Check 4: GPU / loaded models info")
    try:
        resp = requests.get(f"{base_url}/api/ps", timeout=10)
        resp.raise_for_status()
        data = resp.json()
        running = data.get("models", [])

        if running:
            check_pass(f"{len(running)} model(s) currently loaded in memory")
            for m in running:
                name = m.get("name", "unknown")
                size = m.get("size", 0)
                vram = m.get("size_vram", 0)
                if size > 0:
                    size_str = f"{size / 1_000_000_000:.1f} GB"
                else:
                    size_str = "unknown"
                if vram > 0:
                    vram_str = f"{vram / 1_000_000_000:.1f} GB on GPU"
                    pct = (vram / size * 100) if size > 0 else 0
                    print(f"    {name}: {size_str} total, {vram_str} ({pct:.0f}% GPU offloaded)")
                else:
                    print(f"    {name}: {size_str} (CPU only)")
        else:
            check_warn("No models currently loaded in memory", "a model loads on first request")

        return True

    except requests.exceptions.ConnectionError:
        check_warn("Could not check loaded models", "Ollama may not support /api/ps")
        return True
    except Exception as e:
        check_warn("Could not retrieve GPU info", str(e))
        return True


def main():
    parser = argparse.ArgumentParser(
        description="Verify Ollama setup is ready for the workshop.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Example:\n"
            "  python ollama-health-check.py\n"
            "  python ollama-health-check.py --base-url http://10.0.0.5:11434\n"
            "  python ollama-health-check.py --test-model mistral:7b"
        ),
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Ollama API base URL (default: {DEFAULT_BASE_URL})",
    )
    parser.add_argument(
        "--test-model",
        default=None,
        help="Specific model to test inference with (default: smallest available)",
    )

    args = parser.parse_args()
    results = []

    print()
    print("=" * 60)
    print("  🩺 OLLAMA HEALTH CHECK")
    print("=" * 60)
    print(f"  Target: {args.base_url}")

    # Check 1: Connectivity
    ok = check_ollama_running(args.base_url)
    results.append(ok)
    if not ok:
        print_summary(results)
        sys.exit(1)

    # Check 2: Models
    models = check_models_available(args.base_url)
    results.append(len(models) > 0)

    # Check 3: Inference
    if models:
        test_model = args.test_model
        if test_model and test_model not in models:
            print(f"\n  ⚠️  Requested test model '{test_model}' not found, using smallest available")
            test_model = None
        if not test_model:
            # Pick the smallest model for a quick test
            test_model = models[0]
        ok = check_inference(args.base_url, test_model)
        results.append(ok)

        # Check 4: GPU info
        check_gpu_info(args.base_url)
    else:
        results.append(False)

    print_summary(results)
    sys.exit(0 if all(results) else 1)


def print_summary(results):
    """Print overall pass/fail summary."""
    passed = sum(1 for r in results if r)
    total = len(results)

    print()
    print("=" * 60)
    if all(results):
        print(f"  🎉 ALL CHECKS PASSED ({passed}/{total})")
        print("  Workshop environment is ready to go!")
    else:
        print(f"  ⚠️  {passed}/{total} CHECKS PASSED")
        print("  Fix the issues above before starting the workshop.")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
