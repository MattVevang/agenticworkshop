# 🛠️ Tool-Enabled (Agentic) Open WebUI Instance

A **second, independent** Open WebUI instance for the workshop — one that gives a
tool-capable model (**`qwen3.6:35b`**) **native function calling** and **web search**,
so it can reach *outside itself* and answer questions about **current events** that its
training data can't possibly contain.

It runs **in parallel** with the default workshop instance, on a **different port**, so you
can switch between "AI on its own" and "AI with tools" live in front of students.

| Instance | Folder | Port | Tools | Use it for |
|---|---|---|---|---|
| **Default** | [`docker/`](../) | **3000** | ❌ none | Labs 1–8, plus the "no-tools" side of Lab 9, with the older, smaller models that **don't** support tools. Shows what a model knows *on its own*. |
| **Tools** (this one) | `docker/tools/` | **3001** | ✅ web search + native tool calling | Showing how a modern, tool-capable model **changes the game** by searching the live web. |

The two instances share the same host **Ollama** backend (and therefore the same pulled
models), but use **separate containers, ports, and data volumes** — neither one affects the
other.

---

## Why have a separate instance?

The workshop labs intentionally use **older, smaller models** (`llama3.2:3b`, `mistral:7b`, …)
that **cannot call tools**. That's great for teaching the fundamentals: students see what a
model "knows" purely from its training data, watch it hallucinate, and learn its limits.

But some students arrive thinking *"AI is dumb — it just makes stuff up."* This instance is the
**plot twist**: the *same* kind of local model, given a **web-search tool**, can suddenly answer
*"Who is the president **right now**?"* or *"What happened in the news **today**?"* correctly,
with citations. It turns an abstract idea ("agents use tools") into something they can *see*.

> Keep this instance "in your back pocket." Run the labs on port **3000** first, then transition
> to port **3001** for the "now watch *this*" moment.

---

## Quick start

**Prerequisites:** Docker running, Ollama running on the host (`OLLAMA_HOST=0.0.0.0:11434`),
and a tool-capable model pulled:

```powershell
ollama pull qwen3.6:35b      # ~24 GB; reports the "tools" capability in Ollama
# (qwen3.6:27b also works and is configured by the setup script if present)
```

**1. Start the instance** (this does **not** touch the port-3000 instance):

```powershell
cd docker\tools
docker compose up -d
```

Open it at **http://\<server-ip\>:3001**.

**2. One-time model setup** — turns the Web Search capability + native tool calling **on by
default** for the Qwen models, so students don't have to flip any switches, then verifies it:

```powershell
# from the repo root
python demos/scripts/openwebui-tools-setup.py
```

You should see `✅ PASS — the web search tool is wired up and the model uses it.`

That's it. The instance is ready.

---

## The demo: "AI on its own" vs "AI with tools"

This is the litmus test that proves tools are actually working.

### Step 1 — Ask the *default* (no-tools) instance — http://\<server-ip\>:3000

Pick a model like `llama3.2:3b` and ask:

> *What is today's date, and who is the current President of the United States?*

It will hedge, guess, or answer from stale training data — it has **no way** to know "today."
This is the honest limitation of a model running on its own.

### Step 2 — Ask the *tools* instance — http://\<server-ip\>:3001

Select **`qwen3.6:35b`**, make sure the **Web Search** toggle in the chat box is **on**
(the setup script turns it on by default), and ask the same question. The model will:

1. **Decide on its own** that it needs to look this up,
2. Call the built-in **`search_web`** tool,
3. Read the results (and optionally **`fetch_url`** a page for more detail),
4. Answer with the **current** information **and a citation**.

### Questions that show it best

A model trained through 2024 may *already* know who won the November 2024 election, so the
classic "who is the president" question sometimes gets answered from memory. For a demo that
**only** works with live web access, prefer questions whose answers are clearly **after** the
training cutoff:

- *"What is today's date?"*
- *"What's the biggest technology news story this week?"*
- *"What is the current price of Bitcoin (or a specific stock) right now?"*
- *"What's the latest stable version of Python / Node.js / \<tool\>?"*
- *"Who won \<a game / award / election that happened in the last few weeks\>?"*

Then re-ask on the no-tools instance to show the contrast.

> 💡 **Teaching beat:** toggle Web Search **off** in the chat box on the *same* tools instance and
> ask again — the model goes back to "I can't know that." Same model, tool on vs off. That single
> toggle *is* the lesson.

---

## How it works (for instructors)

Open WebUI calls this **Native (Agentic) Mode**: instead of Open WebUI silently stuffing search
results into the prompt, the **model itself** is handed a set of tools and decides when to use
them. The two web tools are:

| Tool | What it does |
|---|---|
| `search_web` | Runs a web search and returns titles, links, and snippets. |
| `fetch_url`  | Opens a specific page and extracts its full text for the model to read. |

For these tools to appear, **three things** must line up — all handled for you here:

1. **Web search enabled globally** — set in [`docker-compose.yml`](./docker-compose.yml)
   via `ENABLE_WEB_SEARCH=true` and `WEB_SEARCH_ENGINE=duckduckgo` (no API key needed).
2. **The model's Web Search capability is on** — set by the setup script (it's on by default
   for all models anyway).
3. **Web Search is toggled on for the chat** — the setup script makes it a **default feature**
   for the Qwen models, so it's already on in every new chat (students can still toggle it off).

Plus the model is put in **native function calling** mode globally via
`DEFAULT_MODEL_PARAMS={"function_calling":"native"}` in the compose file. (There is no separate
`FUNCTION_CALLING_MODE` variable — `function_calling` is a key inside `DEFAULT_MODEL_PARAMS`.)

> ℹ️ Native tool calling needs a **capable** model. `qwen3.6:35b` advertises the `tools`
> capability in Ollama and handles it well. The small lab models (≤8B) generally **cannot** call
> tools reliably — which is exactly why they live on the no-tools instance.

---

## Verifying / re-verifying

`openwebui-tools-setup.py` doubles as a checker:

```powershell
python demos/scripts/openwebui-tools-setup.py --verify-only
```

It asks each model a current-events question with web search **off** then **on**, and confirms
the model either retrieved sources or issued a `search_web` tool call.

> Note: over the plain HTTP API the agentic answer comes back **empty**, because Open WebUI runs
> the search-and-answer loop in the **browser** (over a WebSocket). That's expected — the script
> reports the **tool call itself** as proof. To see the full cited answer, use the **UI** at
> :3001.

---

## Web search providers (reliability)

The default engine is **DuckDuckGo**, which needs **no API key** — ideal for a workshop. It uses
the DDGS metasearch (DuckDuckGo, Brave, Wikipedia, Yandex, …) under the hood. If you want more
consistent results, edit [`docker-compose.yml`](./docker-compose.yml) and switch
`WEB_SEARCH_ENGINE` to a keyed provider, then add its key:

```yaml
- WEB_SEARCH_ENGINE=tavily
- TAVILY_API_KEY=tvly-xxxxxxxx
```

`tavily`, `brave`, `serper`, and `searxng` (self-hosted, fully private) are all good options.
After changing the file: `docker compose up -d` from `docker\tools`.

---

## Running both instances together

```powershell
# default no-tools instance (port 3000)
cd docker
docker compose up -d

# tool-enabled instance (port 3001)
cd tools
docker compose up -d
```

They have distinct compose project names (`open-webui` vs `open-webui-tools`), container names,
and volumes, so they coexist cleanly. Stop the tools instance with:

```powershell
cd docker\tools
docker compose down            # add -v to also wipe its data volume
```

---

## Reset / revert

```powershell
# Remove the per-model config (back to auto-discovered defaults), keep the container
python demos/scripts/openwebui-tools-setup.py --revert

# Wipe the instance entirely (chats, settings, model config)
cd docker\tools
docker compose down -v
```

---

## This instance powers Lab 9

There's a ready-made student lab built around this instance:
**[`labs/lab-09-agents-and-tools.md`](../../labs/lab-09-agents-and-tools.md) — "Agents & Tools."**

It walks students through the whole arc: a no-tools model hits a wall on live-data questions,
then the *same* kind of question succeeds here on port 3001 with web search — including watching
the agent decide to search, refine, and cite. Run it as a **capstone** after the other labs.

Other ways to use the contrast:

- **Extend Lab 4 (Hallucination Detection):** have students provoke a confident wrong answer about
  a recent event on the no-tools instance, then watch the tools instance get it right with a
  source — a concrete lesson in *grounding*.
- **Extend Lab 8 (Real-World Scenarios):** give a task that needs *current* data ("plan around
  this weekend's weather", "summarize today's headlines about X") and compare the two instances.

> **Before running Lab 9:** start this instance (`docker compose up -d` from `docker\tools`) and
> run `python demos/scripts/openwebui-tools-setup.py` once — expect `✅ PASS`.

---

## See also

- [`docker/TROUBLESHOOTING.md`](../TROUBLESHOOTING.md) — Docker, Ollama, and web-search troubleshooting
- [`demos/scripts/README.md`](../../demos/scripts/README.md) — the setup script and other utilities
