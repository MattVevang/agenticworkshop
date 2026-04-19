#!/usr/bin/env python3
"""
Hide non-workshop models in Open WebUI.

Creates model entries with hidden=True for all Ollama models that are NOT
in the workshop list. Hidden models are filtered out of the model dropdown
in the Open WebUI frontend.

Usage:
    python openwebui-hide-models.py
    python openwebui-hide-models.py --unhide          # Revert: show all models
    python openwebui-hide-models.py --webui-url http://192.168.1.100:3000

Requires:
    - Open WebUI running with WEBUI_AUTH=false
    - Ollama running and accessible from Open WebUI
"""

import argparse
import json
import sys
import urllib.request
import urllib.error

WORKSHOP_MODELS = {
    "llama3.2:1b",
    "llama3.2:3b",
    "llama3.1:8b",
    "mistral:7b",
    "llava:7b",
}


def get_token(base_url: str) -> str:
    """Sign in as the default admin user (WEBUI_AUTH=false mode)."""
    data = json.dumps({"email": "admin@localhost", "password": ""}).encode()
    req = urllib.request.Request(
        f"{base_url}/api/v1/auths/signin",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())["token"]


def get_ollama_models(base_url: str, token: str) -> list[str]:
    """Get all model IDs from the /api/models endpoint."""
    req = urllib.request.Request(
        f"{base_url}/api/models",
        headers={"Authorization": f"Bearer {token}"},
    )
    resp = urllib.request.urlopen(req)
    result = json.loads(resp.read())
    return [m["id"] for m in result.get("data", []) if not m["id"].startswith("arena")]


def hide_model(base_url: str, token: str, model_id: str) -> bool:
    """Create a model entry with hidden=True."""
    payload = json.dumps({
        "id": model_id,
        "name": model_id,
        "meta": {"hidden": True},
        "params": {},
        "base_model_id": model_id,
    }).encode()
    req = urllib.request.Request(
        f"{base_url}/api/v1/models/create",
        data=payload,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    try:
        urllib.request.urlopen(req)
        return True
    except urllib.error.HTTPError as e:
        if e.code == 400:
            # Model entry already exists — update it
            payload = json.dumps({
                "id": model_id,
                "name": model_id,
                "meta": {"hidden": True},
                "params": {},
            }).encode()
            req = urllib.request.Request(
                f"{base_url}/api/v1/models/update",
                data=payload,
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
                method="POST",
            )
            try:
                urllib.request.urlopen(req)
                return True
            except urllib.error.HTTPError:
                return False
        return False


def unhide_model(base_url: str, token: str, model_id: str) -> bool:
    """Delete the model entry (removes the hidden flag)."""
    req = urllib.request.Request(
        f"{base_url}/api/v1/models/delete?id={urllib.request.quote(model_id)}",
        headers={"Authorization": f"Bearer {token}"},
        method="DELETE",
    )
    try:
        urllib.request.urlopen(req)
        return True
    except urllib.error.HTTPError:
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Hide or unhide non-workshop models in Open WebUI.",
    )
    parser.add_argument(
        "--webui-url",
        default="http://localhost:3000",
        help="Open WebUI URL (default: http://localhost:3000)",
    )
    parser.add_argument(
        "--unhide",
        action="store_true",
        help="Revert: remove hidden flag from all models",
    )
    args = parser.parse_args()

    try:
        token = get_token(args.webui_url)
    except Exception as e:
        print(f"❌ Could not sign in to Open WebUI at {args.webui_url}: {e}")
        sys.exit(1)

    all_models = get_ollama_models(args.webui_url, token)
    non_workshop = [m for m in all_models if m not in WORKSHOP_MODELS]

    if args.unhide:
        print(f"Unhiding {len(non_workshop)} non-workshop models...")
        for model_id in sorted(non_workshop):
            if unhide_model(args.webui_url, token, model_id):
                print(f"  ✅ Visible: {model_id}")
            else:
                print(f"  ⚠️  Skipped: {model_id} (no hidden entry)")
        print("\n🔓 All models visible. Refresh browser to see changes.")
    else:
        print(f"Workshop models (visible): {', '.join(sorted(WORKSHOP_MODELS))}")
        print(f"Hiding {len(non_workshop)} non-workshop models...\n")
        for model_id in sorted(non_workshop):
            if hide_model(args.webui_url, token, model_id):
                print(f"  🔒 Hidden: {model_id}")
            else:
                print(f"  ❌ Failed: {model_id}")
        print(f"\n✅ Done! Only workshop models visible. Refresh browser (Ctrl+Shift+R).")


if __name__ == "__main__":
    main()
