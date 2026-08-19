#!/usr/bin/env python3
"""
Configure & verify the TOOL-ENABLED Open WebUI instance (port 3001).

The tool-enabled instance (docker/tools/docker-compose.yml) already ships with
web search enabled globally and native (agentic) function calling on by default,
so a tool-capable model like qwen3.6:35b can search the web on its own the moment
you toggle "Web Search" on in a chat.

This script is an optional convenience that, for each tool-capable model:
  - pins the Web Search + Builtin Tools capabilities on,
  - sets Function Calling to Native (agentic tool calling),
  - turns Web Search ON BY DEFAULT in new chats (a per-model Default Feature),
so students get the full agentic experience with zero per-chat clicking. They can
still toggle Web Search OFF in any chat to see the "no tools" contrast.

It then VERIFIES the setup by asking a current-events question the model's training
data can't possibly know, with and without web search, and reports whether the
tool call actually worked.

Usage:
    python openwebui-tools-setup.py                       # configure + verify
    python openwebui-tools-setup.py --webui-url http://localhost:3001
    python openwebui-tools-setup.py --no-default-on       # capability on, but not auto-ON per chat
    python openwebui-tools-setup.py --verify-only         # skip config, just run the check
    python openwebui-tools-setup.py --revert              # remove the model config entries
    python openwebui-tools-setup.py --models qwen3.6:35b  # limit to specific model(s)

Requires:
    - The tool-enabled instance running (docker/tools/docker-compose.yml) with WEBUI_AUTH=false
    - Ollama running with at least one tool-capable model pulled
"""

import argparse
import json
import sys
import urllib.error
import urllib.request

# Emoji-safe output on Windows consoles that default to cp1252.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

# Tool-capable workshop models to configure when --models is not given.
# Any of these that aren't pulled (or don't advertise the Ollama "tools"
# capability) are skipped automatically.
DEFAULT_TOOL_MODELS = ["qwen3.6:35b", "qwen3.6:27b"]

# Mirror of Open WebUI's DEFAULT_CAPABILITIES so we don't regress vision/citations/etc.
# when we write an explicit per-model capabilities map.
CAPABILITIES = {
    "file_context": True,
    "vision": True,
    "file_upload": True,
    "web_search": True,
    "image_generation": True,
    "code_interpreter": True,
    "terminal": True,
    "citations": True,
    "status_updates": True,
    "builtin_tools": True,
}

# Primary check uses the user's classic "who is the president" prompt. A model
# trained through 2024 sometimes answers this from memory (it may already know the
# 2024 election result), so if it doesn't reach for a tool we retry with a question
# that truly cannot be answered without live data.
VERIFY_QUESTION = (
    "Who is the current President of the United States as of June 2026? "
    "Answer in one short sentence and cite your source."
)
VERIFY_QUESTION_FALLBACK = (
    "Use web search to tell me the single biggest technology news story from this "
    "week of June 2026, and cite the source URL."
)


def _post(url, token, payload, method="POST"):
    data = json.dumps(payload).encode()
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    return urllib.request.urlopen(req, timeout=300)


def _get(url, token):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    req = urllib.request.Request(url, headers=headers)
    return json.loads(urllib.request.urlopen(req, timeout=30).read())


def get_token(base_url):
    """Sign in as the default admin user (WEBUI_AUTH=false mode)."""
    resp = _post(
        f"{base_url}/api/v1/auths/signin",
        None,
        {"email": "admin@localhost", "password": ""},
    )
    return json.loads(resp.read())["token"]


def tool_capable_models(base_url, token):
    """Return the set of model ids that advertise Ollama's 'tools' capability."""
    result = _get(f"{base_url}/api/models", token)
    capable = {}
    for m in result.get("data", []):
        caps = (m.get("ollama") or {}).get("capabilities") or []
        if "tools" in caps:
            capable[m["id"]] = caps
    return capable


def configure_model(base_url, token, model_id, default_on):
    """Create/update the model entry: capabilities + native FC + default web search."""
    meta = {"capabilities": dict(CAPABILITIES)}
    if default_on:
        meta["defaultFeatureIds"] = ["web_search"]
    payload = {
        "id": model_id,
        "name": model_id,
        "base_model_id": model_id,
        "meta": meta,
        "params": {"function_calling": "native"},
    }
    try:
        _post(f"{base_url}/api/v1/models/create", token, payload)
        return True
    except urllib.error.HTTPError as e:
        body = e.read()[:300].decode("utf-8", "replace")
        # Open WebUI returns 400/401/409 with an "already registered" message when
        # a config entry for this model id already exists — update it instead.
        if e.code in (400, 401, 409) or "already registered" in body.lower():
            try:
                _post(f"{base_url}/api/v1/models/model/update?id={urllib.request.quote(model_id)}", token, payload)
                return True
            except urllib.error.HTTPError as e2:
                print(f"    update failed: {e2.code} {e2.read()[:200].decode('utf-8','replace')}")
                return False
        print(f"    create failed: {e.code} {body}")
        return False


def revert_model(base_url, token, model_id):
    """Delete the model config entry (reverts to auto-discovered defaults)."""
    url = f"{base_url}/api/v1/models/model/delete?id={urllib.request.quote(model_id)}"
    try:
        _post(url, token, {})
        return True
    except urllib.error.HTTPError:
        return False


def ask(base_url, token, model_id, web_search, question=VERIFY_QUESTION):
    body = {
        "model": model_id,
        "messages": [{"role": "user", "content": question}],
        "stream": False,
    }
    if web_search:
        body["features"] = {"web_search": True}
    resp = _post(f"{base_url}/api/chat/completions", token, body)
    r = json.loads(resp.read())
    choice = r.get("choices", [{}])[0]
    msg = choice.get("message", {})
    tool_names = [
        (tc.get("function") or {}).get("name")
        for tc in (msg.get("tool_calls") or [])
    ]
    return {
        "content": (msg.get("content") or "").strip(),
        "sources": r.get("sources") or msg.get("sources") or [],
        "tool_calls": [t for t in tool_names if t],
        "finish_reason": choice.get("finish_reason"),
    }


def _searched(result):
    """True if the model retrieved web data (RAG) or invoked the search_web tool."""
    return bool(result["sources"]) or ("search_web" in result["tool_calls"])


def verify(base_url, token, model_id):
    print(f"\n🔎 Verifying tool calling on {model_id} ...")

    base = ask(base_url, token, model_id, web_search=False)
    print(f"\n   [Web Search OFF]  {base['content'][:280] or '(no text returned)'}")

    print(f"\n   [Web Search ON ]  Q: {VERIFY_QUESTION}")
    web = ask(base_url, token, model_id, web_search=True)
    if not _searched(web):
        # The model answered from memory; retry with a question that needs live data.
        print("   (model answered without searching — retrying with a live-data question)")
        print(f"   [Web Search ON ]  Q: {VERIFY_QUESTION_FALLBACK}")
        web = ask(base_url, token, model_id, web_search=True, question=VERIFY_QUESTION_FALLBACK)

    if web["sources"]:
        print(f"\n   ✅ Web data retrieved: {len(web['sources'])} source(s).")
        if web["content"]:
            print(f"      Answer: {web['content'][:280]}")
    elif "search_web" in web["tool_calls"]:
        print("\n   ✅ The model autonomously issued a `search_web` tool call "
              "(native agentic tool calling).")
        print("      Over the HTTP API the answer is empty because Open WebUI runs the")
        print("      search loop in the browser/WebSocket pipeline — open the chat in the")
        print("      UI to watch it search and answer with a citation.")

    ok = _searched(web) and not _searched(base)
    print("\n   RESULT:", "✅ PASS — the web search tool is wired up and the model uses it."
          if ok else "⚠️  INCONCLUSIVE — see the answers above and `docker logs open-webui-tools`.")
    return ok


def main():
    parser = argparse.ArgumentParser(description="Configure & verify the tool-enabled Open WebUI instance.")
    parser.add_argument("--webui-url", default="http://localhost:3001",
                        help="Tool-enabled Open WebUI URL (default: http://localhost:3001)")
    parser.add_argument("--models", nargs="+", default=None,
                        help=f"Model id(s) to configure (default: {', '.join(DEFAULT_TOOL_MODELS)})")
    parser.add_argument("--no-default-on", action="store_true",
                        help="Enable the capability but do NOT turn Web Search on by default per chat")
    parser.add_argument("--verify-only", action="store_true", help="Skip configuration, only run verification")
    parser.add_argument("--revert", action="store_true", help="Remove the model config entries")
    args = parser.parse_args()

    try:
        token = get_token(args.webui_url)
    except Exception as e:
        print(f"❌ Could not sign in to Open WebUI at {args.webui_url}: {e}")
        print("   Is the tool-enabled instance running?  cd docker\\tools && docker compose up -d")
        sys.exit(1)

    capable = tool_capable_models(args.webui_url, token)
    wanted = args.models if args.models else DEFAULT_TOOL_MODELS
    targets = [m for m in wanted if m in capable]
    missing = [m for m in wanted if m not in capable]
    for m in missing:
        print(f"⚠️  Skipping {m}: not available or it doesn't advertise the 'tools' capability.")
    if not targets:
        print("❌ No tool-capable target models found. Pull one (e.g. `ollama pull qwen3.6:35b`) and retry.")
        sys.exit(1)

    if args.revert:
        for m in targets:
            ok = revert_model(args.webui_url, token, m)
            print(f"  {'↩️  reverted' if ok else '⚠️  no entry'}: {m}")
        print("\nDone. Models are back to their auto-discovered defaults.")
        return

    if not args.verify_only:
        default_on = not args.no_default_on
        print(f"Configuring {len(targets)} model(s): {', '.join(targets)}")
        print(f"  • Web Search capability + Builtin Tools: ON")
        print(f"  • Function Calling: Native (agentic)")
        print(f"  • Web Search default-on in new chats: {'YES' if default_on else 'no (toggle per chat)'}\n")
        for m in targets:
            ok = configure_model(args.webui_url, token, m, default_on)
            print(f"  {'✅ configured' if ok else '❌ failed'}: {m}")

    all_ok = all(verify(args.webui_url, token, m) for m in targets)
    print("\n" + ("🎉 Tool-enabled instance is ready for the workshop."
                  if all_ok else "Review the output above — verification was not conclusive."))
    sys.exit(0 if all_ok else 2)


if __name__ == "__main__":
    main()
